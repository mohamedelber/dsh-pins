import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
from pinh import pin_checklist
S='src/wainscot/wainscoting-calculator-'; O='pins-N/'; T='tools/cozy/tiles/'
def cr(src,box,name):
    p=T+name; Image.open(src).crop(box).save(p); return p
H=S+'01-dining-room-picture-frame.jpg'; R=S+'02-hallway-panel-wainscoting.jpg'; SH=S+'03-bedroom-shaker-panels.jpg'; B=S+'04-bathroom-beadboard.jpg'; ST=S+'05-staircase-wainscoting.jpg'; L=S+'06-living-room-two-rows.jpg'; P=T+'ws-pin.jpg'
pin_checklist('Wainscoting','Cheat Sheet','lay out boxes and panels',
 [('Height','1/3 of the wall: 32 in at 8 ft'),('Gap','3 in around every box'),('Box width','(wall − (boxes+1) × gap) ÷ boxes'),('Avoid','splitting the wall in half')],
 'Add 10% extra moulding for mitres',H,O+'wainscoting-checklist.jpg',photo_ay=0.6)
pin_cozy([cr(H,(0,0,700,1024),'ws-hl.png'),P,cr(H,(836,0,1536,1024),'ws-hr.png'),R,SH,B,ST,L,H],'Free','Tool','Wainscoting','Calculator',"boxes, panels\nand moulding to buy",
 ['','','','Hallway panels','Shaker wall','Beadboard','Staircase','Two rows','Dining room'],O+'wainscoting-cozy.jpg',seed=201)
pin_cozy([cr(R,(0,0,760,1024),'ws-rl.png'),cr(P,(0,300,1024,1324),'ws-plow.png'),cr(H,(300,0,1324,1024),'ws-hc.png'),ST,B,L,SH,R,H],'Easy','DIY','Picture Frame','Wainscoting',"free layout calculator",
 ['','','','Stair boxes','Beadboard bath','Two rows','Shaker panels','Hallway','Dining room'],O+'wainscoting-cozy2.jpg',seed=207)
