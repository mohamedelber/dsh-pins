import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from pinh2 import pin_bold
from pinh import pin_collage,pin_checklist,pin_a
G='gen/out/xmas-lights/'; F='gen/out/xmas-lights-fix/'; O='pins-N/'
pin_checklist('Christmas Tree','Lights Cheat Sheet','100 lights per foot',
 [('6 ft tree','600 lights'),('7 ft tree','700 lights'),('7.5 ft tree','750 lights'),('9 ft tree','900 lights')],
 'Fuller look? Use 150 per foot',G+'01-hero.png',O+'xmas-lights-checklist.jpg',photo_ay=0.5)
pin_bold(F+'04-pin-v2.png','HOW MANY','LIGHTS?','Christmas tree calculator','100\nPER FT',O+'xmas-lights-bold.jpg',ay=0.75)
pin_collage(G+'01-hero.png',F+'02-closeup-v2.png',G+'03-tabletop.png','700','Lights for a','7 ft Christmas Tree',O+'xmas-lights-K.jpg',ay=(0.5,0.5,0.5))
pin_a([G+'01-hero.png',F+'02-closeup-v2.png',G+'03-tabletop.png',F+'04-pin-v2.png'],['How Many Lights','for a Christmas Tree?'],O+'xmas-lights-A.jpg')
