#!/usr/bin/env python3
import sys
from PIL import Image

im = Image.open(sys.argv[1]) # Can be many different formats.
pix = im.load()
for x in range(0,int(im.size[0]/2)):
    for y in range(0,im.size[1]):
        col = pix[x,y]
        if col[0] > 128:
            col = (0,0,0,255)
        else:
            col = (255,255,255,255)
        pix[x,y] = col
for x in range(0,im.size[0]):
    for y in range(0,int(im.size[1]/2)):
        col = pix[x,y]
        if col[0] > 128:
            col = (0,0,0,255)
        else:
            col = (255,255,255,255)
        pix[x,y] = col
im.save(sys.argv[2] if  len(sys.argv) == 3 else sys.argv[1])  # Save the modified pixels as .png