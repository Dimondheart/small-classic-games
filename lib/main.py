#!/usr/bin/python

import sys

#Debuging, python outputs written to file
class debuglogger(object):

  def __init__(self, logtype):
    if logtype == "outputs":
      self.stdoutlog = open("log_python.log", "w")

    elif logtype == "errors":
      self.stderrlog = open("log_error.log", "w")

    self.type = logtype


  def write(self, message):
    if self.type == "outputs":
      self.stdoutlog.write(message)

    elif self.type == "errors":
      self.stderrlog.write(message)

#Redirects python stdout and stderr to files
#sys.stdout = debuglogger("outputs")
sys.stderr = debuglogger("errors")


import pygame

import common
import events
import graphics
import ai
import menubar
import infobar
import board




class main(object):

  #Initialization actions
  def startup(self):

    #Make instances of all functions
    common.events = events.event()
    common.graphics = graphics.graphics()
    common.ai = ai.ai()
    common.menubar = menubar.menubar()
    common.infobar = infobar.infobar()
    common.board = board.board()

    #Initialize pygame
    pygame.init()

    #Load main window
    common.screen = pygame.display.set_mode((common.width, common.height))#, pygame.RESIZABLE)
    pygame.display.set_caption(common.name + " v." + common.version)
    common.screen.fill(common.bgcolor)

    #Load all recources and set icon
    common.graphics.loadall()
    pygame.display.set_icon(common.graphics.logo)

    common.running = True

    #Run main loop
    self.loop()


  #main loop function
  def loop(self):

    #Timer for handling held key events
    pygame.time.set_timer(pygame.USEREVENT+1, 30)

    #Timer for ai to check if it can take its turn
    pygame.time.set_timer(pygame.USEREVENT+2, 50)

    #Actual main loop
    while common.running:
      for event in pygame.event.get():
        common.events.newevent(event)
      common.graphics.render()
    common.running = False

    self.cleanup()


  #Termination function
  def cleanup(self):

    print common.tilegrid
    #For stopping the event timer
    pygame.time.set_timer(pygame.USEREVENT+1, 0)

    sys.exit(0)



if __name__ == '__main__':
  m = main()
  m.startup()