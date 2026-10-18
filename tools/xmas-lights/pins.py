import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from pinh2 import pin_bold
from pinh import pin_collage,pin_checklist
G='gen/out/wardrobe-depth/'; O='pins-N/'
pin_checklist('Wardrobe Depth','Cheat Sheet','measure before you buy',
 [('Hinged doors','60 cm (24 in) deep'),('Sliding doors','71 cm (28 in) deep'),('Shelves only','55 cm (22 in) deep'),('Pull-out rail','from 30 cm (12 in) inside')],
 'Hangers are about 46 cm (18 in) wide',G+'01-hero-interior.png',O+'wardrobe-depth-checklist.jpg',photo_ay=0.5)
pin_bold(G+'04-pin-evening.png','WARDROBE','DEPTH','Standard sizes + calculator','60 CM\n24 IN',O+'wardrobe-depth-bold.jpg',ay=0.8)
pin_collage(G+'01-hero-interior.png',G+'02-sliding-doors.png',G+'03-shallow-alcove.png','60cm','Standard','Wardrobe Depth',O+'wardrobe-depth-K.jpg',ay=(0.5,0.5,0.5))
