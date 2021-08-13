#!/bin/sh
./squarify.py wolf.png tmp.png
./draw_circle.py tmp.png
./black_white.py tmp.png
./merge.py tmp.png cross.jpg tmp.png
./keep_only_the_circle.py tmp.png