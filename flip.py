#!/usr/bin/env python3
import sys
from PIL import Image

im = Image.open(sys.argv[1])
pix = im.load()
for x in range(0,im.size[0]):
    for y in range(0,im.size[1]):
        col = pix[x,y]
        if col[0] > 128:
            col = (0,0,0,255)
        else:
            col = (255,255,255,255)
        pix[x,y] = col
im.save(sys.argv[2] if  len(sys.argv) == 3 else sys.argv[1])