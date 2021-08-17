#!/bin/sh
cp wolf.png tmp.png
./squarify.py tmp.png

./draw_circle.py tmp.png
./draw_text_on_circle_up.py tmp.png "Libertas·potior" 500 /mnt/c/Windows/Fonts/arial.ttf 50
./draw_text_on_circle_down.py tmp.png "quam saturitas" 500 /mnt/c/Windows/Fonts/arial.ttf 50
./black_white.py tmp.png
./keep_only_the_circle.py tmp.png