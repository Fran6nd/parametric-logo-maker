#!/bin/sh
cp black1000.png alys_front.png
./merge.py alys_front.png center.png
./draw_circle.py alys_front.png --inner-radius 400 --outer-radius 420 --color BLACK
./flip.py alys_front.png
./draw_circle.py alys_front.png --inner-radius 420
./flip.py alys_front.png
./draw_text.py alys_front.png "21/07/1992" Candal.ttf 70 --radius 460 --on-circle --rotation 180 --reversed

./draw_text.py alys_front.png "ALICE*H" Candal.ttf  70  --on-circle --radius 460
./flip.py alys_front.png
./draw_text.py alys_front.png '"ALYS"      ' Candal.ttf  50  --on-circle --radius 370 --rotation 180 --reversed
./flip.py alys_front.png

cp black1000.png alys_rear.png
#./flip.py alys_rear.png
./merge.py alys_rear.png center_rear.png
./draw_circle.py alys_rear.png --inner-radius 375 --outer-radius 420 --color WHITE
./draw_circle.py alys_rear.png --inner-radius 420
./draw_text.py alys_rear.png "32" arial.ttf 600
./flip.py alys_rear.png
./draw_text.py alys_rear.png "21/07/2024" Candal.ttf 70 --on-circle --radius 460 --rotation 180 --reversed
./draw_text.py alys_rear.png "********************************" Candal.ttf 70 --on-circle --radius 450 
./draw_circle.py alys_rear.png --inner-radius 500 --outer-radius 1000