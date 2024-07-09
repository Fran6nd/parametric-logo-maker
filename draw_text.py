#!/usr/bin/env python3
import sys
import math
import argparse
from PIL import Image, ImageDraw, ImageFont, ImageOps
from vector2D import Vector2D

# Function to get the dimensions of the text based on the font
def get_text_dimensions(text_string, font):
    ascent, descent = font.getmetrics()
    (text_width, text_height) = font.getbbox(text_string)[2:4]
    return text_width, ascent + descent

# Function to draw a single character at a specified angle and position on the image
def draw_char(im, f, s, module, arg, color, reversed=False):
    if s != " ":
        arg = -arg  # Reverse the angle
        center = Vector2D(int(im.size[0] / 2), int(im.size[0] / 2))  # Center of the image
        pos = Vector2D(0, module)  # Initial position vector
        pos = pos.setArg(arg * 0.0174533)  # Set the angle in radians
        pos = pos + center  # Calculate the position
        txt = Image.new('L', get_text_dimensions(s, f))  # Create a new image for the character
        d = ImageDraw.Draw(txt)
        d.text((0, 0), s, font=f, fill=255)  # Draw the character on the image
        w = txt.rotate(-arg - 90 if not reversed else -arg + 90, expand=1)  # Rotate the character image
        im.paste(ImageOps.colorize(w, (0, 0, 0), color), (int(pos.x - w.size[0] / 2), int(pos.y - w.size[1] / 2)), w)  # Paste the rotated character on the original image

# Function to draw text on a circular path
def draw_text(im, f, s, module, arg, angle_step, color, reversed=False):
    offset = 0
    if reversed:
        s = s[::-1]  # Reverse the string if the reversed flag is set
    for c in s:
        draw_char(im, f, c, module, arg - offset, color, reversed)  # Draw each character
        offset = offset + angle_step  # Increment the angle offset for the next character

# Function to center text on a circular path
def draw_text_centered_on_circle(im, f, s, module, angle_step, rotation, color, reversed=False):
    total_angle = (len(s) - 1) * angle_step
    draw_text(im, f, s, module, 90 + rotation + total_angle / 2 if angle_step > 0 else rotation + total_angle / 2 - 90, angle_step, color, reversed)

# Function to center text horizontally and optionally rotate it
def draw_text_centered_horizontally(im, text, font, rotation, color):
    draw = ImageDraw.Draw(im)
    text_width, text_height = get_text_dimensions(text, font)
    
    width, height = im.size
    x = (width - text_width) / 2  # Calculate horizontal center
    y = (height - text_height) / 2  # Calculate vertical center

    # Create a new image for the text and draw the text on it
    text_image = Image.new('RGBA', (text_width, text_height), (255, 255, 255, 0))
    text_draw = ImageDraw.Draw(text_image)
    text_draw.text((0, 0), text, font=font, fill=color)

    rotated_text = text_image.rotate(rotation, expand=1)  # Rotate the text image
    im.paste(rotated_text, (int(x - (rotated_text.width - text_width) / 2), int(y - (rotated_text.height - text_height) / 2)), rotated_text)  # Paste the rotated text on the original image

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Draw text on an image, either on a circle or centered horizontally.")
    parser.add_argument("image_path", type=str, help="Path to the image file.")
    parser.add_argument("text", type=str, help="Text to draw on the image.")
    parser.add_argument("font_path", type=str, help="Path to the .ttf font file.")
    parser.add_argument("font_size", type=int, help="Font size to use for the text.")
    parser.add_argument("--on-circle", action='store_true', help="Draw text on a circle.")
    parser.add_argument("--radius", type=int, default=None, help="Radius of the circle (required if --on-circle is specified).")
    parser.add_argument("--angle-step", type=float, default=6, help="Angle step between characters for circular text. Default is 6.")
    parser.add_argument("--reversed", action='store_true', help="Reverse text orientation. For circular text, top of letters toward outside. For horizontal text, rotates 180°.")
    parser.add_argument("--rotation", type=float, default=0, help="Rotation in degrees for text orientation.")
    parser.add_argument("--color", type=str, choices=["BLACK", "WHITE"], default="BLACK", help="Text color: BLACK or WHITE. Default is BLACK.")

    args = parser.parse_args()

    im = Image.open(args.image_path)  # Open the image file
    f = ImageFont.truetype(args.font_path, args.font_size)  # Load the font
    color = (0, 0, 0) if args.color == "BLACK" else (255, 255, 255)  # Determine the color

    if args.on_circle:
        if args.radius is None:
            print("Error: --radius is required when --on-circle is specified.")
            sys.exit(1)
        draw_text_centered_on_circle(im, f, args.text.upper(), args.radius, args.angle_step, args.rotation, color, args.reversed)  # Draw text on a circle
    else:
        if args.reversed:
            args.text = args.text[::-1]  # Reverse the text if the reversed flag is set
        draw_text_centered_horizontally(im, args.text.upper(), f, args.rotation, color)  # Draw text centered horizontally

    im.save(args.image_path)  # Save the modified image
