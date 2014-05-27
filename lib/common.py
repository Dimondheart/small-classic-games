#!/usr/bin/python

import os


defaultfont = "FreeMono, Monospace"
bgcolor = (120,120,120)
gridlinecolor = (40,40,40)

name = "Tic Tac Toe"
version = "0"
player2enabled = False

tilesize = 128
tilegrid = []

gridsize = 3
width = gridsize*tilesize+1
height = gridsize*tilesize+1

#Root directory of this program
rootdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

#Directory where recources are stored
resdir = os.path.join(rootdir, "res")