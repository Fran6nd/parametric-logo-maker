#!/usr/bin/env python3
import sys
import math
from PIL import Image, ImageDraw

im = Image.open(sys.argv[1]) # Can be many different formats.
draw = ImageDraw.Draw(im)
pix = im.load()
draw.ellipse(((0,0),( im.size[0], im.size[0])),width=30, outline=(0, 0, 0))
draw.ellipse(((55,55), (im.size[0]-55, im.size[0]-55)),width=10, outline=(0, 0, 0))

im.save(sys.argv[1])  # Save the modified pixels as .png