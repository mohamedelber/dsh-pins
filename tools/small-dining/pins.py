import sys,os; sys.path.insert(0,'/home/claude/dsh-pins'); os.chdir('/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
T='tools/cozy/tiles/'
SP='/tmp/claude-0/-home-claude/aa9f44c6-b1c7-520d-9978-96402d6712cc/scratchpad/'
def cr(src,box,name):
    p=T+name; im=Image.open(src).convert('RGB'); w,h=im.size
    im.crop((int(box[0]*w),int(box[1]*h),int(box[2]*w),int(box[3]*h))).save(p); return p
def sheet(a,b,n):
    a=Image.open(a).resize((500,750)); b=Image.open(b).resize((500,750))
    c=Image.new('RGB',(1010,750),'white'); c.paste(a,(0,0)); c.paste(b,(510,0)); c.save(SP+n)
O='src/small-dining/pins/'; os.makedirs(O,exist_ok=True); s='src/small-dining/small-dining-room-ideas-'
H=s+'01-round-pedestal-table.jpg'; B=s+'02-banquette-drawers.jpg'; DL=s+'03-drop-leaf-table.jpg'; SB=s+'04-sideboard-shelves.jpg'; LD=s+'05-living-dining-zone.jpg'
PIN=cr('gen/out/small-dining/06-pin.png',(0,0,1,1),'sd-pin.png')
pin_cozy([cr(H,(0,0,.5,1),'sd-hl.png'),PIN,cr(H,(.5,0,1,1),'sd-hr.png'),B,DL,SB,LD,cr(H,(.2,.3,.8,1),'sd-h2.png'),cr(B,(.3,.3,1,1),'sd-b2.png')],'12','Ideas','Small Dining','Room Ideas',"with the real\nmeasurements",
 ['','','','Wall banquette','Drop-leaf table','Slim sideboard','Zone it with a rug','Round pedestal table','Drawers under the bench'],O+'sd-cozy.jpg',seed=741)
pin_cozy([cr(B,(0,0,.6,1),'sd-bl.png'),cr(PIN,(0,.3,1,1),'sd-pl.png'),cr(DL,(.3,0,1,1),'sd-dr.png'),H,B,LD,DL,cr(SB,(0,0,.7,.7),'sd-s2.png'),cr(H,(.25,0,.75,.45),'sd-h3.png')],'60','cm','Small Dining','Room Layout',"60 cm per diner,\n75 cm to the wall",
 ['','','','Round seats 4 at 1 m','Banquette saves space','One room, two zones','Folds flat to the wall','Shelves, not cabinets','Pendant 75-90 cm up'],O+'sd-cozy2.jpg',seed=747)
sheet(O+'sd-cozy.jpg',O+'sd-cozy2.jpg','sd-pins.jpg')
