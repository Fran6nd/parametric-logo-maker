#!/usr/bin/env python3
import sys
from PIL import Image, ImageDraw, ImageFont

def get_text_dimensions(text_string, font):
    ascent, descent = font.getmetrics()
    (text_width, text_height) = font.getbbox(text_string)[2:4]
    return text_width, ascent + descent

def draw_text_centered(image_path, text, font_path, font_size):
    im = Image.open(image_path)
    draw = ImageDraw.Draw(im)
    
    font = ImageFont.truetype(font_path, font_size)
    text_width, text_height = get_text_dimensions(text, font)
    
    width, height = im.size
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    
    draw.text((x, y), text, font=font, fill=(0, 0, 0))
    
    im.save(image_path)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: script.py <image_path> <text> <font_path> <font_size>")
    else:
        image_path = sys.argv[1]
        text = sys.argv[2]
        font_path = sys.argv[3]
        font_size = int(sys.argv[4])
        
        draw_text_centered(image_path, text, font_path, font_size)
