#!/usr/bin/env python3

import sys
from PIL import Image, ImageDraw

im1 = Image.open(sys.argv[1])
im2 = Image.open(sys.argv[2]) # Can be many different formats.*
im2 = im2.resize(im1.size)
pix1 = im1.load()
pix2 = im2.load()
for x in range(0, im1.size[0]):
    for y in range(0, im1.size[1]):

        if pix1[x,y][0] > 128 and pix2[x,y][0] > 128:
            pix1[x,y] = (0,0,0,255)
        elif  pix1[x,y][0] > 128:
            pix1[x,y] = (255,255,255,255)
        elif pix1[x,y][0] <= 128 and pix2[x,y][0] > 128:
            pix1[x,y] = (255,255,255,255)
        elif  pix1[x,y][0] <= 128:
            pix1[x,y] = (0,0,0,255)
im1.save(sys.argv[3])  # Save the modified pixels as .png