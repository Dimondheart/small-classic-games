#!/usr/bin/python

import random

import pygame

import common



class board(object):

  #Total space to move board down for header elements (menu bar, etc)
  topheader = 0

  player1turn = True
  winner = None



  def __init__(self):

    self.player1turn = bool(random.randint(0,1))

    #If ai has to move first, then this is used to tell ai to move first
    if not self.player1turn and not common.player2enabled:
      common.aimovefirst = True

    else:
      common.aimovefirst = False


    #How far the grid is moved down in the window
    self.topheader = common.menubar.height+common.infobar.height

    #Occupy tilegrid with tiles
    for column in xrange(0, common.gridsize):
      common.tilegrid.append([])

      for row in xrange(0, common.gridsize):
        common.tilegrid[column].append("neutral")



  def resetboard(self):

    for column in xrange(0, common.gridsize):
      for row in xrange(0, common.gridsize):
        common.tilegrid[column][row] = "neutral"

    self.winner = None

    self.player1turn = bool(random.randint(0,1))

    if not self.player1turn and not common.player2enabled:
      common.aimovefirst = True



  def changetile(self):

    tilex = (common.mx)/common.tilesize
    tiley = (common.my-self.topheader)/common.tilesize

    #Checks if mouseclick is inside tilegrid, and checks owner of tile if so
    try:
      tiletype = common.tilegrid[tilex][tiley]
    except IndexError:
      return

    #Checks if tile has been claimed already
    if tiletype != "neutral":
      return

    #If it is player1's turn
    if self.player1turn:
      common.tilegrid[tilex][tiley] = "player1"
      self.player1turn = not self.player1turn

    #Else if player2 is not ai controlled
    elif common.player2enabled:
      common.tilegrid[tilex][tiley] = "player2"
      self.player1turn = not self.player1turn

    self.checkforend()

    #Ai takes its turn if enabled and no winner has been declared
    if self.winner == None and not common.player2enabled:
      while not self.player1turn:
        common.ai.taketurn()



  def checkforend(self):

    #Check columns
    for column in xrange(0, common.gridsize):
      for row in xrange(1, common.gridsize):

        if common.tilegrid[column][row] != "neutral" and common.tilegrid[column][row] == common.tilegrid[column][row-1]:
          self.winner = common.tilegrid[column][row]

        else:
          self.winner = None
          break

      if self.winner != None:
        break

    #Checks if previous check decided a winner
    if self.winner != None:
      return




    #Check topleft -> bottomright diagonal
    topleftcorner = common.tilegrid[0][0]

    if topleftcorner != "neutral":
      for n in xrange(1, common.gridsize):
        if common.tilegrid[n][n] == common.tilegrid[n-1][n-1]:
          self.winner = topleftcorner

        else:
          self.winner = None
          break

    #Checks if previous check decided a winner
    if self.winner != None:
      return




    #Check topright -> bottomleft diagonal
    toprightcorner = common.tilegrid[common.gridsize-1][0]

    if toprightcorner != "neutral":
      for n in xrange(common.gridsize-1, 0, -1):
        if toprightcorner == common.tilegrid[common.gridsize-1-n][n]:
          self.winner = toprightcorner

        else:
          print n
          self.winner = None
          break

    #Checks if previous check decided a winner
    if self.winner != None:
      return




    #Check rows
    for row in xrange(0, common.gridsize):
      for column in xrange(1, common.gridsize):
        if common.tilegrid[column][row] != "neutral" and common.tilegrid[column][row] == common.tilegrid[column-1][row]:
          self.winner = common.tilegrid[column][row]

        else:
          self.winner = None
          break

      if self.winner != None:
        return

    #Checks if previous check decided a winner
    if self.winner != None:
      return




    #Check for tie
    for column in xrange(0, common.gridsize):
      for row in xrange(0, common.gridsize):

        if common.tilegrid[column][row] == "neutral":
          self.winner = None
          break

        else:
          self.winner = "tie"

      if self.winner == None:
        return




  def render(self):

    #Render grid background
    pygame.draw.rect(common.screen, (120,120,120), (0, self.topheader, common.gridsize*common.tilesize, common.gridsize*common.tilesize))



    #Render tiles
    for column in xrange(0, common.gridsize):
      for row in xrange(0, common.gridsize):
        common.screen.blit(common.graphics.gridtile, (column*common.tilesize, row*common.tilesize+self.topheader))



    #Horizontal gridlines
    for gridx in xrange(0, (common.gridsize+1)*common.tilesize, common.tilesize):

      startpos = (gridx, self.topheader)
      endpos = (gridx, common.gridsize*common.tilesize+self.topheader)

      pygame.draw.line(common.screen, common.gridlinecolor, startpos, endpos)


    #Vertical gridlines
    for gridy in xrange(0, (common.gridsize+1)*common.tilesize, common.tilesize):

      startpos = (0, gridy+self.topheader)
      endpos = (common.gridsize*common.tilesize, gridy+self.topheader)

      pygame.draw.line(common.screen, common.gridlinecolor, startpos, endpos)



    #Render 'X's and 'O's
    for column in xrange(0, common.gridsize):
      for row in xrange(0, common.gridsize):

        if common.tilegrid[column][row] == 'neutral':
          continue

        elif common.tilegrid[column][row] == 'player1':
          common.screen.blit(common.graphics.ximg, (column*common.tilesize+1,row*common.tilesize+self.topheader+1))

        elif common.tilegrid[column][row] == 'player2':
          common.screen.blit(common.graphics.oimg, (column*common.tilesize+1,row*common.tilesize+self.topheader+1))