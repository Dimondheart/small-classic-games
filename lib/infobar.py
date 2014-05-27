#!/usr/bin/python

import pygame

import common


class infobar(object):

  height = 0

  bgcolor = (245,245,245)

  text = ""


  def __init__(self):

    self.height = 40

    #Adds needed space to window height
    common.height += self.height



  def render(self):

    pygame.draw.rect(common.screen, self.bgcolor, (0, common.menubar.height, common.width, self.height))




    #Decide what text to render
    if common.board.winner != None:

      if common.board.winner == "tie":
        self.text = "Tie!"


      elif common.player2enabled:

        if common.board.winner == "player1":
          self.text = "Player 1 Wins!"

        else:
          self.text = "Player 2 Wins!"
          

      elif common.board.winner == "player1":
        self.text = "You Win!"


      elif common.board.winner == "player2":
        self.text = "You Lose!"


    elif common.board.player1turn == True:
      self.text = "Player 1's Turn"


    else:
      self.text = "Computer's Turn"