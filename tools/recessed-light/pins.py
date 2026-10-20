import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
from pinh import pin_checklist
S='src/recessed-light/recessed-lighting-calculator-'; O='pins-N/'; T='tools/cozy/tiles/'
def cr(src,box,name):
    p=T+name; Image.open(src).crop(box).save(p); return p
H=S+'01-living-room-recessed-lights.jpg'; K=S+'02-kitchen-recessed-lights.jpg'; B=S+'03-bedroom-recessed-lights.jpg'; BA=S+'04-bathroom-shower-light.jpg'; HA=S+'05-hallway-recessed-lights.jpg'; AR=S+'06-accent-lights-art.jpg'; P=T+'rl-pin.jpg'
pin_checklist('Recessed Lighting','Cheat Sheet','space your lights right',
 [('Spacing','ceiling height ÷ 2 (8 ft = 4 ft)'),('Walls','half the spacing (about 2 ft)'),('Kitchen','12 to 18 in from the cabinets'),('Brightness','10 to 20 lm per sq ft living')],
 'Wall washers: at least 1.5 ft from the wall',H,O+'recessed-lighting-checklist.jpg',photo_ay=0.0)
pin_cozy([cr(H,(0,0,700,1024),'rl-hl.png'),P,cr(H,(836,0,1536,1024),'rl-hr.png'),K,B,BA,HA,AR,H],'Free','Tool','Recessed Lighting','Calculator',"how many lights\nand how far apart",
 ['','','','Kitchen','Bedroom','Bathroom','Hallway','Art wall','Living room'],O+'recessed-lighting-cozy.jpg',seed=181)
pin_cozy([cr(K,(0,0,760,1024),'rl-kl.png'),cr(P,(0,400,1024,1424),'rl-plow.png'),cr(H,(300,0,1324,1024),'rl-hc.png'),HA,B,K,AR,BA,H],'How','Many','Recessed Lights','Do I Need?',"free lighting calculator",
 ['','','','Even spacing','Soft and warm','Over the counters','Wall washing','Shower light','Open plan'],O+'recessed-lighting-cozy2.jpg',seed=187)
