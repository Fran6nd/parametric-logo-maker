#!/bin/sh
./squarify.py wolf.png tmp.png

./draw_circle.py tmp.png
./keep_only_the_circle.py tmp.png
./draw_text_on_circle.py tmp.png /mnt/c/Windows/Fonts/arial.ttf 50