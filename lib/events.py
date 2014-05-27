#!/usr/bin/python

import pygame

import common



class event(object):

  #Deals with new events
  def newevent(self, event):

    #Quit event
    if event.type == pygame.QUIT:
      common.running = False


    #Dealing with held key functions, and check if ai has to go first
    elif event.type == pygame.USEREVENT+1:
      if common.aimovefirst:
        common.ai.taketurn()

      self.keyread()

    #Only used if player2 is not enabled
    #elif event.type == pygame.USEREVENT+2:
    #  if not common.player2enabled and not common.board.player1turn:
    #    common.ai.taketurn()


    #window resize event
    #elif event.type == pygame.VIDEORESIZE:
    #  self.resize(event)


    elif event.type == pygame.KEYDOWN:

      #'r' key resets board
      if event.key == pygame.K_r:
        common.board.resetboard()

      else:
        return



    elif event.type == pygame.MOUSEBUTTONDOWN:
      common.mx, common.my = event.pos

      #Left mouse button; changes gridspace to be owned by player1/player2
      if event.button == 1:
        #If clicked on menu button
        if common.my <= common.menubar.height:
          common.menubar.event()

        #If a winner has already been decided
        elif common.board.winner != None:
          return

        #Clicked elsewhere, no winner yet
        else:
          common.board.changetile()


      #middle mouse button
      if event.button == 2:
        return


      #Right mouse button
      if event.button == 3:
        return





    elif event.type == pygame.MOUSEBUTTONUP:
      return


    elif event.type == pygame.MOUSEMOTION:
      common.mx, common.my = event.pos


    else:
      #print "Undefined Event: ", pygame.event.event_name(event.type), "\n",
      return


  #Dealing with held key events
  def keyread(self):
    pass



  #User resized window
  #def resize(self, event):
  #  common.width = event.w
  #  common.height = event.h

  #  common.screen = pygame.display.set_mode((common.width, common.height), pygame.RESIZABLE)

  #  #print "Window Resized To: ", common.width, " by ", common.height, "\n",