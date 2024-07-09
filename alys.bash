#!/bin/sh
cp black1000.png alys_front.png
./merge.py alys_front.png center.png
./draw_centered_disc.py alys_front.png --inner-radius 400 --outer-radius 420 --color BLACK
./flip.py alys_front.png
./draw_centered_disc.py alys_front.png --inner-radius 420
./flip.py alys_front.png
./draw_text.py alys_front.png "21/07/1992" Candal.ttf 70 --radius 460 --on-circle --rotation 180 --reversed

./draw_text.py alys_front.png "ALICE*H" Candal.ttf  70  --on-circle --radius 460
./flip.py alys_front.png
./draw_text.py alys_front.png '"ALYS"      ' Candal.ttf  50  --on-circle --radius 370 --rotation 180 --reversed
./flip.py alys_front.png

cp black1000.png alys_rear.png
#./flip.py alys_rear.png
./merge.py alys_rear.png center_rear.png
./draw_centered_disc.py alys_rear.png --inner-radius 375 --outer-radius 420 --color WHITE
./draw_centered_disc.py alys_rear.png --inner-radius 420
./draw_text_centered.py alys_rear.png "32" arial.ttf 600
./flip.py alys_rear.png
./draw_text_on_circle_down.py alys_rear.png "21/07/2024" 450 Candal.ttf 70
./draw_text_on_circle_up.py alys_rear.png "********************************" 470 Candal.ttf 70
#./draw_text_on_circle_up.py alys_rear.png "RADIUS NOVUS IN VULTU TUO" 450 Candal.ttf 70
./draw_centered_disc.py alys_rear.png --inner-radius 500 --outer-radius 1000
#./draw_centered_disc.py alys_rear.png --inner-radius 300 --outer-radius 350 --color WHITE