import os, sys
#import PIL
import mahotas
import numpy    
import pylab
import scipy
from PIL import Image,ImageDraw
from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import Image, Image



print "Reading image to im"
im = Image.open("track.png")
im = im.resize((900,600),Image.ANTIALIAS);

Image._show(im)

px = [] 
py = [] 

def onmouse(event):
    px.append(event.x)
    py.append(event.y)
    return px,py





#===============================================================================
# print 'Reading image from file'
# trackimage = mahotas.imread('track.png')
# 
# pylab.imshow(trackimage)
# pylab.show()
# 
# Image._show(trackimage)
#===============================================================================
#===============================================================================
# draw = ImageDraw.Draw(trackimage)
# draw.line((100,200,150,300), fill=128)
#===============================================================================








