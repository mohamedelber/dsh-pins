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
O='src/kitchen-island/pins/'; os.makedirs(O,exist_ok=True); s='src/kitchen-island/kitchen-island-ideas-'
H=s+'01-green-island-drawers.jpg'; TR=s+'02-kitchen-trolley.jpg'; PD=s+'03-pan-drawers.jpg'; SS=s+'04-seating-side-shelves.jpg'; PE=s+'05-peninsula.jpg'
PIN=cr('gen/out/kitchen-island/06-pin.png',(0,0,1,1),'ki-pin.png')
pin_cozy([cr(H,(0,0,.5,1),'ki-hl.png'),PIN,cr(H,(.5,0,1,1),'ki-hr.png'),TR,PD,SS,PE,cr(H,(.15,.4,.6,1),'ki-h2.png'),cr(SS,(.5,.3,1,1),'ki-s2.png')],'12','Ideas','Kitchen Island','Ideas',"that add storage,\neven in a small kitchen",
 ['','','','Trolley on wheels','Deep pan drawers','Seating side shelves','A peninsula instead','Drawers on the work side','Cookbooks on the end'],O+'ki-cozy.jpg',seed=761)
pin_cozy([cr(TR,(0,0,.65,1),'ki-tl.png'),cr(PIN,(0,.3,1,1),'ki-pl.png'),cr(PE,(.3,0,1,1),'ki-pr.png'),H,PE,TR,PD,cr(SS,(0,.2,.6,1),'ki-s3.png'),cr(PD,(.3,.3,1,1),'ki-d2.png')],'1','metre','Small Kitchen','Island Ideas',"1 m walkways: what\nfits and what doesn't",
 ['','','','Oak top, two stools','Peninsula saves floor','Rolls out of the way','Pans in drawers','30 cm overhang','Lids in one place'],O+'ki-cozy2.jpg',seed=767)
sheet(O+'ki-cozy.jpg',O+'ki-cozy2.jpg','ki-pins.jpg')
