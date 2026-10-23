import sys,os; sys.path.insert(0,'/home/claude/dsh-pins'); os.chdir('/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
O='src/dryer/pins/'; T='tools/cozy/tiles/'
def cr(src,box,name):
    p=T+name; im=Image.open(src).convert('RGB'); w,h=im.size
    im.crop((int(box[0]*w),int(box[1]*h),int(box[2]*w),int(box[3]*h))).save(p); return p
s='src/dryer/heat-pump-vs-condenser-dryer-'
H=s+'01-utility-room.jpg'; K=s+'02-stacked.jpg'; F=s+'03-lint-filter.jpg'; W=s+'04-water-tank.jpg'; V=s+'05-vented.jpg'; D=s+'06-folded.jpg'; P=s+'07-pin.jpg'
pin_cozy([cr(H,(0,0,.5,1),'dr-hl.png'),P,cr(H,(.5,0,1,1),'dr-hr.png'),H,cr(K,(.3,0,.72,.9),'dr-k.png'),W,V,F,D],'3','Dryer Types','Heat Pump vs','Condenser',"running costs\nand the 2027 ban",
 ['','','','Under a worktop','Stacked with a kit','Condenser water tank','Vented to outside','Clean the filter','Utility room setup'],O+'dryer-cozy.jpg',seed=401)
pin_cozy([cr(K,(0,0,.5,1),'dr-kl.png'),cr(P,(0,.33,1,1),'dr-pl.png'),cr(D,(.4,0,1,1),'dr-dr.png'),K,cr(H,(.5,0,1,1),'dr-hr2.png'),V,W,F,H],'5','Checks','Before You Buy','a Tumble Dryer',"heat pump, condenser\nor vented",
 ['','','','Room to stack?','Solid door dryer','Outside wall?','Tank or drain hose?','Filter after every load','Space under a worktop'],O+'dryer-cozy2.jpg',seed=409)
a=Image.open(O+'dryer-cozy.jpg').resize((500,750)); b=Image.open(O+'dryer-cozy2.jpg').resize((500,750))
c=Image.new('RGB',(1010,750),'white'); c.paste(a,(0,0)); c.paste(b,(510,0)); c.save('/tmp/claude-0/-home-claude/66ced7db-2a2d-58db-8d1b-26fd0ebe8295/scratchpad/dr-pins.jpg')
