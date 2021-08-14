#!/bin/sh
cp wolf.png tmp.png
./squarify.py tmp.png

./draw_circle.py tmp.png
./merge.py tmp.png cross.jpg


./draw_circle.py tmp.png
./keep_only_the_circle.py tmp.png
./black_white.py tmp.png