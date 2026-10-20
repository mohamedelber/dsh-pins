import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
from pinh import pin_checklist
G='gen/out/closet-size/'; S='src/closet-size/'; O='pins-N/'; T='tools/cozy/tiles/'
def cr(src,box,name):
    p=T+name; Image.open(src).crop(box).save(p); return p
H=G+'01-hero.png'; SM=S+'walk-in-closet-size-02-small-one-wall.jpg'; TW=G+'03b-double-sided.png'; L=S+'walk-in-closet-size-04-l-shaped-closet.jpg'; I=G+'05-u-shape-island.png'; D=G+'06-double-hang.png'; P=G+'07-pin.png'
pin_checklist('Walk-In Closet','Size Cheat Sheet','the numbers to plan with',
 [('One wall','5 ft wide: 24 in + 36 in walkway'),('Two walls','7 ft wide'),('Hanging depth','24 in for clothes'),('Walkway','36 in, 24 in if tight')],
 'With an island: about 12 x 12 ft',H,O+'walk-in-closet-size-checklist.jpg',photo_ay=0.3)
pin_cozy([cr(H,(0,0,700,1024),'wc-hl.png'),P,cr(H,(836,0,1536,1024),'wc-hr.png'),SM,TW,L,I,D,H],'Free','Tool','Walk-In Closet','Size Calculator',"for every layout\nand wardrobe",
 ['','','','One wall','Two walls','L-shape','With an island','Double hang','36 in walkway'],O+'walk-in-closet-size-cozy.jpg',seed=141)
pin_cozy([cr(TW,(0,0,620,1024),'wc-tl.png'),cr(P,(0,500,1024,1536),'wc-plow.png'),cr(I,(768,0,1536,1024),'wc-ir.png'),SM,H,I,L,D,TW],'How','Big','Walk-In Closet','Sizes',"minimum, average\nand layout sizes",
 ['','','','From 5 x 5 ft','7 ft wide','12 x 12 ft','Corner storage','Double the rod','Two-wall'],O+'walk-in-closet-size-cozy2.jpg',seed=147)
