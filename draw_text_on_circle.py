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

def get_text_dimensions(text_string, font):
    # https://stackoverflow.com/a/46220683/9263761
    ascent, descent = font.getmetrics()
    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent
    return (text_width, text_height)

def draw_char(s, module, arg, reversed = False):
    if s != " ":
        arg = -arg
        center = Vector2D(int(im.size[0]/2), int(im.size[0]/2))
        pos = Vector2D(0, module)
        pos = pos.setArg(arg * 0.0174533)
        pos = pos + center
        txt=Image.new('L', get_text_dimensions(s,f))
        d = ImageDraw.Draw(txt)
        d.text( (0, 0), s,  font=f, fill=255)
        w=txt.rotate(-arg - 90 if not reversed else -arg + 90,  expand=1)
        im.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (int(pos.x-w.size[0]/2),int(pos.y-w.size[1]/2)),  w)
def draw_text(s, module, arg, angle_step):
    offset = 0

    for c in s:
        draw_char(c, module, arg - offset, True if angle_step < 0 else False)
        offset = offset + angle_step

def draw_text_centered(s, module, angle_step):
    total_angle = (len(s)-1) * angle_step
    draw_text(s, module, 90+total_angle/2 if angle_step>0 else total_angle/2 -90, angle_step)
draw_text_centered( "Præstat cautela quam medela".upper(), 500,6)
draw_text_centered( "Ad impossibile neno tenatur".upper(), 500,-6)
im.save(sys.argv[1])  # Save the modified pixels as .png