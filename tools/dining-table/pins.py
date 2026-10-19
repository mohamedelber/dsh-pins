import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from pinh2 import pin_bold
from pinh import pin_collage,pin_checklist,pin_a
G='gen/out/dining-table/'; O='pins-N/'
H=G+'01-hero.png'; B=G+'02-round.png'; S=G+'03-extending.png'; P=G+'04-pin.png'
pin_checklist('Dining Table','Size Cheat Sheet','table size for every group',
 [('4 people','36 x 48 to 60 in, or 36 to 44 in round'),('6 people','36 to 40 x 60 to 72 in'),('8 people','36 to 40 x 84 to 96 in'),('Space around it','at least 36 in to the wall')],
 '24 in of table edge per person',H,O+'dining-table-checklist.jpg',photo_ay=0.5)
pin_bold(S,'WHAT SIZE','DINING TABLE?','Free size calculator','24 IN\nA SEAT',O+'dining-table-bold.jpg',ay=0.7)
pin_collage(H,B,S,'6','Dining Table Size','for 6 People',O+'dining-table-K.jpg',ay=(0.5,0.5,0.5))
pin_a([H,B,S,P],['What Size Dining','Table Do I Need?'],O+'dining-table-A.jpg')
