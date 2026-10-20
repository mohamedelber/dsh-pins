import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
from pinh import pin_checklist
G='gen/out/baseboard-calc/'; O='pins-N/'; T='tools/cozy/tiles/'
def cr(src,box,name):
    p=T+name; Image.open(src).crop(box).save(p); return p
H=G+'01-hero.png'; M=G+'02-measure.png'; C=G+'03-corner.png'; TB=G+'04-tall-baseboard.png'; S=G+'05b-stock-lengths.png'; D=G+'06-door-casing.png'; P=G+'07b-pin.png'
pin_checklist('Baseboard','Cheat Sheet','how much to buy',
 [('Measure','add up every wall'),('Doors','take off about 3 ft each'),('Waste','add 10%, or 15% for corners'),('Boards','divide by 8, 12 or 16 ft and round up')],
 'One tube of caulk covers about 55 ft',H,O+'baseboard-calculator-checklist.jpg',photo_ay=0.6)
pin_cozy([cr(H,(0,0,700,1024),'bb-hl.png'),P,cr(H,(836,0,1536,1024),'bb-hr.png'),M,C,S,D,TB,H],'Free','Tool','Baseboard','Calculator',"how much trim\nto buy",
 ['','','','Measure walls','Coped corner','8, 12 or 16 ft','Stop at doors','Tall baseboard','Add 10% waste'],O+'baseboard-calculator-cozy.jpg',seed=151)
pin_cozy([cr(M,(0,0,760,1024),'bb-ml.png'),cr(P,(0,500,1024,1536),'bb-plow.png'),cr(S,(776,0,1536,1024),'bb-sr.png'),H,C,D,TB,S,M],'How','Much','Baseboard','Do I Need?',"free trim calculator",
 ['','','','Linear feet','Inside corner','Minus doors','Ceiling height','Board lengths','Tape and pencil'],O+'baseboard-calculator-cozy2.jpg',seed=157)
