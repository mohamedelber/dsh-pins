import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from pinh2 import pin_bold
from pinh import pin_collage,pin_checklist,pin_a
G='gen/out/picture-height/'; O='pins-N/'
H=G+'01-hero.png'; B=G+'02-gallery.png'; S=G+'03-tools.png'; P=G+'04-pin.png'
pin_checklist('Picture Hanging','Height Cheat Sheet','where the art should sit',
 [('Open wall','center at 57 in (145 cm)'),('Above a sofa','4 to 10 in above the back'),('Above a bed','8 to 10 in above the headboard'),('Gallery wall','2 to 3 in between frames')],
 'Nail = 57 + half the frame - hanger drop',H,O+'picture-height-checklist.jpg',photo_ay=0.4)
pin_bold(B,'HOW HIGH','TO HANG ART','Free height calculator','57\nINCHES',O+'picture-height-bold.jpg',ay=0.0)
pin_collage(H,B,P,'57"','How High to Hang','Pictures',O+'picture-height-K.jpg',ay=(0.4,0.5,0.6))
pin_a([H,B,S,P],['How High to Hang','Pictures and Art'],O+'picture-height-A.jpg')
