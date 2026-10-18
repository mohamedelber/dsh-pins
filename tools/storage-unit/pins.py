import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from pinh2 import pin_bold
from pinh import pin_collage,pin_checklist,pin_a
G='gen/out/storage-unit/'; O='pins-N/'
H=G+'01-hero.png'; B=G+'02-boxes.png'; S=G+'03-small.png'; P=G+'04-pin.png'
pin_checklist('Storage Unit','Size Cheat Sheet','what fits in each size',
 [('Studio','5 x 10 ft (50 sq ft)'),('1 to 2 bedrooms','10 x 10 ft (100 sq ft)'),('3 bedrooms','10 x 15 ft (150 sq ft)'),('4 bedrooms or a car','10 x 20 ft (200 sq ft)')],
 'Want an aisle? Go one size up',H,O+'storage-unit-checklist.jpg',photo_ay=0.5)
pin_bold(P,'WHAT SIZE','STORAGE UNIT?','Free size calculator','6\nSIZES',O+'storage-unit-bold.jpg',ay=0.7)
pin_collage(H,B,S,'10x10','Storage Unit','for a 2 Bedroom Home',O+'storage-unit-K.jpg',ay=(0.5,0.5,0.5))
pin_a([H,B,S,P],['What Size Storage','Unit Do I Need?'],O+'storage-unit-A.jpg')
