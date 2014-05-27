#!/usr/bin/python

import pygame

import common



class menubar(object):

  height = 0


  def __init__(self):

    self.height = 20

    #Adds menu bar's height to window height 
    common.height += self.height




  def event(self):
    pass