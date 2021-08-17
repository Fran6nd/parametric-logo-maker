#!/bin/sh
cp wolf.png tmp.png
./squarify.py tmp.png

./draw_circle.py tmp.png
./draw_text_on_circle.py tmp.png "Libertas·potior·quam·saturitas" 500 /mnt/c/Windows/Fonts/arial.ttf 50
./black_white.py tmp.png
./keep_only_the_circle.py tmp.png