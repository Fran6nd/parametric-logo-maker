#!/bin/sh
cp black1000.png alys.png
./flip.py alys.png
./draw_centered_disc.py alys.png 
./flip.py alys.png
./draw_centered_disc.py alys.png --outer-radius 400
#./flip.py alys.png
./draw_text_on_circle_down.py alys.png "DEPUIS 1992" 450 Candal.ttf 70
./draw_text_on_circle_up.py alys.png "ALICE" 450 Candal.ttf 70
#./flip.py alys.png