#!/bin/sh
cp wolf.png tmp.png
./squarify.py tmp.png

./draw_circle.py tmp.png
./keep_only_the_circle.py tmp.png
./draw_text_on_circle.py tmp.png "Libetas potiorquam saturitas" 500 /mnt/c/Windows/Fonts/arial.ttf 50