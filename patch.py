import sys
from PIL import Image, ImageDraw

im = Image.open(sys.argv[1]) # Can be many different formats.
pix = im.load()
print(im.size)  # Get the width and hight of the image for iterating over
size = min(im.size[0], im.size[1])
rect = Image.new("RGBA", (size, size), (255, 255, 255, 0))
rect.paste(im,  (int(-(im.size[0] / 2 - size / 2)),(int(-(im.size[1] / 2 - size / 2)))))
draw = ImageDraw.Draw(rect)
draw.ellipse(((0,0),( rect.size[0], rect.size[0])),width=10, outline=(0, 0, 0))
draw.ellipse(((25,25), (rect.size[0]-25, rect.size[0]-25)),width=10, outline=(0, 0, 0))
rect.save(sys.argv[2])  # Save the modified pixels as .png