#!/usr/bin/env python3
import sys
import argparse
import math
from PIL import Image

def create_polar_array(output_image_path, overlay_image_path, count, offset_rotation, radius, lookat_center, input_scale):
    # Load and scale the overlay image
    overlay_image = Image.open(overlay_image_path).convert('RGBA')
    
    if input_scale < 0 or input_scale > 1:
        raise ValueError("input_scale must be between 0 and 1.")
    
    # Resize the overlay image based on input_scale
    if input_scale < 1:
        new_size = (int(overlay_image.width * input_scale), int(overlay_image.height * input_scale))
        overlay_image = overlay_image.resize(new_size, Image.Resampling.LANCZOS)
    
    overlay_width, overlay_height = overlay_image.size
    
    # Create a new image with a transparent background
    result_image = Image.new('RGBA', (2 * radius + overlay_width, 2 * radius + overlay_height), (255, 255, 255, 0))
    
    # Calculate the center of the new image
    center_x, center_y = result_image.size[0] / 2, result_image.size[1] / 2
    
    # Draw the overlay images in a polar array
    for i in range(count):
        angle = (360 / count) * i + offset_rotation
        angle_rad = math.radians(angle)
        x = center_x + radius * math.cos(angle_rad) - overlay_width / 2
        y = center_y + radius * math.sin(angle_rad) - overlay_height / 2
        
        # Paste the overlay image onto the result image
        result_image.paste(overlay_image, (int(x), int(y)), overlay_image)

    # Save the result image
    result_image.save(output_image_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a polar array of images.")
    parser.add_argument("output_image", type=str, help="Path to save the output image file.")
    parser.add_argument("overlay_image", type=str, help="Path to the overlay image file.")
    parser.add_argument("--count", type=int, default=2, help="Number of overlay images in the polar array.")
    parser.add_argument("--offset-rotation", type=float, default=0, help="Offset rotation in degrees for the polar array.")
    parser.add_argument("--radius", type=int, default=50, help="Radius of the polar array.")
    parser.add_argument("--no-lookat-center", action='store_true', help="Do not center the array on the new image's center.")
    parser.add_argument("--input-scale", type=float, default=1.0, help="Scale factor for the overlay image between 0 and 1.")

    args = parser.parse_args()
    
    # Validate the input_scale argument
    if args.input_scale < 0 or args.input_scale > 1:
        print("Error: --input-scale must be between 0 and 1.")
        sys.exit(1)
    
    create_polar_array(
        output_image_path=args.output_image,
        overlay_image_path=args.overlay_image,
        count=args.count,
        offset_rotation=args.offset_rotation,
        radius=args.radius,
        lookat_center=not args.no_lookat_center,
        input_scale=args.input_scale
    )
