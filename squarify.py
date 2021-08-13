#!/usr/bin/env python3
import sys
from PIL import Image, ImageDraw

im = Image.open(sys.argv[1]) # Can be many different formats.
pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over
size = min(im.size[0], im.size[1])
rect = Image.new("RGBA", (size, size), (255, 255, 255, 0))
rect.paste(im,  (int(-(im.size[0] / 2 - size / 2)),(int(-(im.size[1] / 2 - size / 2)))))
rect.save(sys.argv[2] if  len(sys.argv) == 3 else sys.argv[1])  # Save the modified pixels as .png