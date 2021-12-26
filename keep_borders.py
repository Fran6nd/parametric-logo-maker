#!/usr/bin/env python3
import sys
from PIL import Image


im = Image.open(sys.argv[1])
pix = im.load()

def build_possibilities(x, y, size):
    input = [(-1, -1), (-1,0),(-1,1), (1,1), (1, 0), (1, -1) ,(0,1), (0, -1)]
    #input = [(-1,0), (1, 0), (0,1), (0, -1)]
    output = []
    for i in range(len(input)):
        input[i] = (input[i][0] + x, input[i][1] + y)
    for  i in input:
        if i[0]>= 0 and i[1] >= 0 and i[0] < size[0] and i[1] < size[1]:
            output.append(i)
    return output

def copy(array):
    output = []
    for x in range (im.size[0]):
        output.append([])
        for y in range(im.size[1]):
            output[x].append(array[x,y])
    return output
    
basepix = copy(pix)
for x in range(0,im.size[0]):
    for y in range(0,im.size[1]):
        col = basepix[x][y]
        if col[0] < 128:
            poss = build_possibilities(x,y,im.size)
            blank = 0
            for p in poss:
                if basepix[p[0]][ p[1]][0] > 128:
                    blank = blank + 1
            if blank:
                pix[x, y]= (0,0,0,255)
            else:
                pix[x, y]= (255,255,255,255)

im.save(sys.argv[1])