#!/usr/bin/python

import random

import pygame

import common



class ai(object):

  def __init__(self):
    pass


  #TODO: Add in changetile
  def taketurn(self):

    x,y = random.randint(0, common.gridsize-1), random.randint(0, common.gridsize-1)

    if common.tilegrid[x][y] == "neutral":

      common.tilegrid[x][y] = "player2"
      common.aimovefirst = False
      common.board.player1turn = True

    else:
      return

    common.board.checkforend()