import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
from pinh import pin_checklist
S='src/board-batten/board-and-batten-calculator-'; O='pins-N/'; T='tools/cozy/tiles/'
def cr(src,box,name):
    p=T+name; Image.open(src).crop(box).save(p); return p
H=S+'01-bedroom-board-and-batten.jpg'; D=S+'02-dining-room-wainscot.jpg'; E=S+'03-entryway-batten-hooks.jpg'; G=S+'04-grid-board-and-batten.jpg'; N=S+'05-nursery-board-and-batten.jpg'; I=S+'06-installing-battens.jpg'; P=T+'bb-pin.jpg'
pin_checklist('Board and Batten','Cheat Sheet','space your battens evenly',
 [('Gap','12 to 24 in, most popular 16 to 20'),('Formula','(wall − battens × width) ÷ gaps'),('Boards','1x4 = 3 1/2 in actual width'),('Height','half to two-thirds of the wall')],
 'Add 10% extra boards for cuts',H,O+'board-and-batten-checklist.jpg',photo_ay=0.3)
pin_cozy([cr(H,(0,0,700,1024),'bb-hl.png'),P,cr(H,(836,0,1536,1024),'bb-hr.png'),D,E,G,N,I,H],'Free','Tool','Board and Batten','Calculator',"spacing, cuts\nand boards to buy",
 ['','','','Dining room','Entryway','Grid wall','Nursery','DIY install','Bedroom'],O+'board-and-batten-cozy.jpg',seed=191)
pin_cozy([cr(D,(0,0,760,1024),'bb-dl.png'),cr(P,(0,300,1024,1324),'bb-plow.png'),cr(H,(300,0,1324,1024),'bb-hc.png'),E,N,G,D,I,H],'How','Far','Apart Should','Battens Be?',"free spacing calculator",
 ['','','','Hooks on the rail','Half wall','Grid squares','Wainscot','DIY install','Feature wall'],O+'board-and-batten-cozy2.jpg',seed=197)
