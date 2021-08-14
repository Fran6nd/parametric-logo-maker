#!/usr/bin/env python3
import sys
import math
from PIL import Image, ImageDraw

im = Image.open(sys.argv[1]) # Can be many different formats.
draw = ImageDraw.Draw(im)
pix = im.load()

for x in range(0, im.size[0]):
    for y in range(0, im.size[1]):
        if(math.sqrt(math.pow(x-im.size[0]/2,2)+ math.pow(y-im.size[0]/2,2))) > im.size[0]/2:
            pix[x,y] = (255,255,255, 0)

im.save(sys.argv[1])  # Save the modified pixels as .png