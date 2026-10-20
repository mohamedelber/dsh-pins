import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
from pinh import pin_checklist
S='src/island-size/kitchen-island-size-calculator-'; G='gen/out/island-size/'; O='pins-N/'; T='tools/cozy/tiles/'
def cr(src,box,name):
    p=T+name; Image.open(src).crop(box).save(p); return p
H=G+'01-hero.png'; SM=S+'02-small-island.jpg'; SE=G+'03-seating.png'; WA=S+'04-work-aisle.jpg'; SI=G+'05-sink-island.png'; C=G+'06-cart.png'; P=G+'07-pin.png'
pin_checklist('Kitchen Island','Size Cheat Sheet','the clearances that matter',
 [('Work aisle','42 in, or 48 in for two cooks'),('Walkway','at least 36 in'),('Stools','24 in of counter each'),('Behind stools','44 in to walk past')],
 'Most kitchens need about 13 ft of width',H,O+'kitchen-island-size-checklist.jpg',photo_ay=0.5)
pin_cozy([cr(H,(0,0,700,1024),'ki-hl.png'),P,cr(H,(836,0,1536,1024),'ki-hr.png'),SM,SE,WA,SI,C,H],'Free','Tool','Kitchen Island','Size Calculator',"what fits your\nkitchen",
 ['','','','Small island','Stool spacing','Work aisle','Sink island','Rolling cart','Big island'],O+'kitchen-island-size-cozy.jpg',seed=161)
pin_cozy([cr(SE,(0,0,760,1024),'ki-sl.png'),cr(P,(0,500,1024,1536),'ki-plow.png'),cr(WA,(776,0,1536,1024),'ki-wr.png'),H,SM,SE,WA,SI,C],'How','Big','Kitchen Island','Can I Fit?',"free size calculator",
 ['','','','10 ft island','4 ft island','24 in per stool','42 in aisle','Prep and seats','Small kitchen'],O+'kitchen-island-size-cozy2.jpg',seed=167)
