#!/usr/bin/env python3
import sys
import math
from PIL import Image, ImageDraw, ImageFont, ImageOps
from vector2D import Vector2D

im = Image.open(sys.argv[1]) # Can be many different formats.
draw = ImageDraw.Draw(im)
pix = im.load()

for x in range(0, im.size[0]):
    for y in range(0, im.size[1]):
        pass
f =  ImageFont.truetype(sys.argv[2], int(sys.argv[3]))

def draw_char(s, module, arg):
    arg = -arg
    center = Vector2D(int(im.size[0]/2), int(im.size[0]/2))
    pos = Vector2D(0, module)
    pos = pos.setArg(arg * 0.0174533)
    pos = pos + center
    txt=Image.new('L', (50,int(sys.argv[3])))
    d = ImageDraw.Draw(txt)
    d.text( (0, 0), s,  font=f, fill=255)
    w=txt.rotate(-arg - 90,  expand=1)
    im.paste( ImageOps.colorize(w, (0,0,0), (255,0,0)), (int(pos.x),int(pos.y)),  w)
def draw_text(s, module, arg):
    offset = 0

    for c in s:
        draw_char(c, module, arg - offset)
        offset = offset + 10
draw_text( "Salut c'est moi! trololo !!! 1 2 3 4 5 ", 500, 180)
im.save(sys.argv[1])  # Save the modified pixels as .png