#!/usr/bin/python

import pygame
import os

import common



class graphics(object):

  def __init__ (self):

    pygame.font.init()

    self.font = pygame.font.SysFont(common.defaultfont, 16)
    self.bigfont = pygame.font.SysFont(common.defaultfont, 24)

    self.menubartext = None




  def render(self):

    common.screen.fill(common.bgcolor)

    #Render menu bar
    pygame.draw.rect(common.screen, (220,220,220), (0, 0, common.width, common.menubar.height))

    #Render menu bar text
    #common.screen.blit(self.menubartext, (2, 0))



    #Render info bar
    common.infobar.render()


    #Render text on info bar
    text = self.bigfont.render(common.infobar.text, True, (0,0,0), (common.infobar.bgcolor))

    xpos = common.width/2 - text.get_width()/2
    ypos = common.menubar.height + (common.infobar.height/2 - text.get_height()/2)

    common.screen.blit(text, (xpos, ypos))




    #Render board
    common.board.render()


    #text = self.font.render("Menu", True, (0,0,0), (230,230,230))


    #Refreshes pygame screen
    pygame.display.flip()



  #Loads all graphics and creates surfaces used to render them with transparency
  def loadall(self):

    #TODO: create menu bar text surface

    #Logo/Icon
    self.logo = pygame.image.load(os.path.join(common.resdir, "logo.ico")).convert()


    #Grid tile image
    self.gridtile = pygame.Surface((common.tilesize, common.tilesize))
    pygame.draw.rect(self.gridtile, (225,255,255), (0,0, common.tilesize, common.tilesize))


    #'X' image
    self.ximg = pygame.Surface((common.tilesize-1, common.tilesize-1), flags=pygame.SRCALPHA)
    image = pygame.image.load(os.path.join(common.resdir, "x.png"))
    self.ximg.blit(image, (0,0))


    #'O' image
    self.oimg = pygame.Surface((common.tilesize-1, common.tilesize-1), flags=pygame.SRCALPHA)
    image = pygame.image.load(os.path.join(common.resdir, "o.png"))
    self.oimg.blit(image, (0,0))