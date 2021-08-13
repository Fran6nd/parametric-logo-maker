#!/usr/bin/env python3
import sys
import math
from PIL import Image, ImageDraw

im = Image.open(sys.argv[1]) # Can be many different formats.
draw = ImageDraw.Draw(im)
pix = im.load()
draw.ellipse(((0,0),( im.size[0], im.size[0])),width=10, outline=(0, 0, 0))
draw.ellipse(((25,25), (im.size[0]-25, im.size[0]-25)),width=10, outline=(0, 0, 0))

im.save(sys.argv[2] if  len(sys.argv) == 3 else sys.argv[1])  # Save the modified pixels as .png