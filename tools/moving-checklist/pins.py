import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from pinh2 import pin_bold
from pinh import pin_collage,pin_checklist,pin_a
G='gen/out/moving-checklist/'; O='pins-N/'
H=G+'01-hero.png'; K=G+'02-kitchen.png'; E=G+'03-essentials.png'; P=G+'04-pin.png'
pin_checklist('Moving Checklist','Week by Week','free printable PDF',
 [('8 weeks before','book movers, declutter'),('4 weeks before','forward mail, switch utilities'),('Moving week','pack an essentials box'),('Moving day','meter readings and photos')],
 'Starting late? Do the catch-up list first',H,O+'moving-checklist-checklist.jpg',photo_ay=0.5)
pin_bold(P,'FREE PRINTABLE','MOVING CHECKLIST','Week by week + PDF','8 WEEKS\nPLAN',O+'moving-checklist-bold.jpg',ay=0.75)
pin_collage(H,K,E,'8','Week Moving Checklist','Free Printable',O+'moving-checklist-K.jpg',ay=(0.5,0.5,0.5))
pin_a([H,K,E,P],['Printable Moving','Checklist (Free PDF)'],O+'moving-checklist-A.jpg')
