#!/bin/sh
python3 squarify.py wolf.png tmp.png


python3 merge.py tmp.png cross.jpg tmp.png

python3 black_white.py tmp.png
python3 keep_only_the_circle.py tmp.png