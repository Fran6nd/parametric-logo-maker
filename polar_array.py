#!/usr/bin/env python3
import sys
import argparse
import math
from PIL import Image

def create_polar_array(target_image_path, overlay_image_path, count, offset_rotation, radius, lookat_center, input_scale, input_offset_rotation):
    # Load the target image
    target_image = Image.open(target_image_path).convert('RGBA')
    target_width, target_height = target_image.size
    
    # Load and scale the overlay image
    overlay_image = Image.open(overlay_image_path).convert('RGBA')
    
    if input_scale < 0 or input_scale > 1:
        raise ValueError("input_scale must be between 0 and 1.")
    
    # Resize the overlay image based on input_scale
    if input_scale < 1:
        new_size = (int(overlay_image.width * input_scale), int(overlay_image.height * input_scale))
        overlay_image = overlay_image.resize(new_size, Image.BICUBIC)
    
    overlay_width, overlay_height = overlay_image.size
    
    # Create a copy of the target image to draw on
    result_image = target_image.copy()
    
    # Calculate the center of the target image
    center_x, center_y = target_width / 2, target_height / 2
    
    # Draw the overlay images in a polar array
    for i in range(count):
        angle = (360 / count) * i + offset_rotation
        angle_rad = math.radians(angle)
        x = center_x + radius * math.cos(angle_rad) - overlay_width / 2
        y = center_y + radius * math.sin(angle_rad) - overlay_height / 2
        
        if lookat_center:
            # Apply input offset rotation to the overlay image
            rotation_angle = -angle - input_offset_rotation
            rotated_overlay = overlay_image.rotate(rotation_angle, resample=Image.BICUBIC)
        else:
            # No rotation applied
            rotated_overlay = overlay_image
        
        # Paste the rotated overlay image onto the result image
        result_image.paste(rotated_overlay, (int(x), int(y)), rotated_overlay)

    # Save the result image
    result_image.save(target_image_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a polar array of images.")
    parser.add_argument("output_image", type=str, help="Path to save the output image file.")
    parser.add_argument("overlay_image", type=str, help="Path to the overlay image file.")
    parser.add_argument("--count", type=int, default=2, help="Number of overlay images in the polar array.")
    parser.add_argument("--offset-rotation", type=float, default=0, help="Offset rotation in degrees for the polar array.")
    parser.add_argument("--radius", type=int, default=50, help="Radius of the polar array.")
    parser.add_argument("--no-lookat-center", action='store_true', help="Deactivate default behavior of rotating images towards the center of the array.")
    parser.add_argument("--input-scale", type=float, default=1.0, help="Scale factor for the overlay image between 0 and 1.")
    parser.add_argument("--input-offset-rotation", type=float, default=0, help="Additional rotation applied to the overlay images before placing them in the array.")

    args = parser.parse_args()
    
    # Validate the input_scale argument
    if args.input_scale < 0 or args.input_scale > 1:
        print("Error: --input-scale must be between 0 and 1.")
        sys.exit(1)
    
    create_polar_array(
        target_image_path=args.output_image,
        overlay_image_path=args.overlay_image,
        count=args.count,
        offset_rotation=args.offset_rotation,
        radius=args.radius,
        lookat_center=not args.no_lookat_center,
        input_scale=args.input_scale,
        input_offset_rotation=args.input_offset_rotation
    )
