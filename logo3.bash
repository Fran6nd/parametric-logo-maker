#!/bin/sh
cp wolf.png tmp.png

./squarify.py tmp.png
./draw_circle.py tmp.png --inner-radius 550 --color BLACK


#./draw_text_on_circle_up.py tmp.png "FREEDOM RATHER THAN SATIETY" 500 arial.ttf 50
#./draw_text.py tmp.png "FREEDOM RATHER THAN SATIETY" arial.ttf  50 --radius 500 --on-circle
./draw_text.py tmp.png "La liberté " arial.ttf  50 --radius 500 --on-circle --rotation -5
#./draw_text_on_circle_up.py tmp.png "Libertas potior quam saturitas" 500 arial.ttf 50
#./draw_text_on_circle_down.py tmp.png "ALBUS  LUPUS" 500 arial.ttf 50
#./draw_text.py tmp.png "WHITE WEREWOLF" arial.ttf  50 --radius 500 --rotation 180 --reversed --on-circle
./draw_text.py tmp.png "plutôt que le collier" arial.ttf  50 --radius 500 --rotation 180 --reversed --on-circle

#./black_white.py tmp.png
./flip.py tmp.png
./keep_only_the_circle.py tmp.png 
./black_white.py tmp.png