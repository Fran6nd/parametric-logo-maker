import sys
import math
from PIL import Image, ImageDraw

im = Image.open(sys.argv[1]) # Can be many different formats.
draw = ImageDraw.Draw(im)
pix = im.load()
#draw.ellipse(((0,0),( im.size[0], im.size[0])),width=10, outline=(0, 0, 0))
#draw.ellipse(((25,25), (im.size[0]-25, im.size[0]-25)),width=10, outline=(0, 0, 0))

for x in range(0, im.size[0]):
    for y in range(0, im.size[1]):
        if(math.sqrt(math.pow(x-im.size[0]/2,2)+ math.pow(y-im.size[0]/2,2))) > im.size[0]/2:
            pix[x,y] = (pix[x,y][0],pix[x,y][1],pix[x,y][2], 0)

im.save(sys.argv[2] if  len(sys.argv) == 3 else sys.argv[1])  # Save the modified pixels as .png