#!/usr/bin/env python3
import sys
import argparse
from PIL import Image, ImageDraw

def draw_centered_circle(image_path, inner_radius=None, outer_radius=None):
    im = Image.open(image_path)
    width, height = im.size
    draw = ImageDraw.Draw(im)

    if outer_radius is None:
        outer_radius = min(width, height) / 2

    if inner_radius is None:
        # Draw a full black circle
        center = (width / 2, height / 2)
        draw.ellipse(
            (
                (center[0] - outer_radius, center[1] - outer_radius),
                (center[0] + outer_radius, center[1] + outer_radius)
            ),
            fill=(0, 0, 0),
            outline=(0, 0, 0)
        )
    else:
        center = (width / 2, height / 2)
        draw.ellipse(
            (
                (center[0] - outer_radius, center[1] - outer_radius),
                (center[0] + outer_radius, center[1] + outer_radius)
            ),
            fill=None,
            outline=(0, 0, 0),
            width=int(outer_radius - inner_radius)
        )

    im.save(image_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Draw a centered circle on an image.")
    parser.add_argument("image_path", type=str, help="Path to the image file.")
    parser.add_argument("--inner-radius", type=int, default=None, help="Inner radius of the circle. If not specified, the circle will be filled.")
    parser.add_argument("--outer-radius", type=int, default=None, help="Outer radius of the circle. If not specified, the circle will fill the smallest dimension of the image.")

    args = parser.parse_args()

    draw_centered_circle(args.image_path, args.inner_radius, args.outer_radius)
