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
O='src/organise-wardrobe/pins/'; os.makedirs(O,exist_ok=True); s='src/organise-wardrobe/organise-wardrobe-'
H=s+'01-organised-wardrobe.jpg'; DR=s+'02-double-hanging.jpg'; FF=s+'03-file-folded-drawer.jpg'; SD=s+'04-shelf-dividers.jpg'; SS=s+'05-seasonal-storage.jpg'
PIN=cr('gen/out/organise-wardrobe/06-pin.png',(0,0,1,1),'ow-pin.png')
pin_cozy([cr(H,(0,0,.5,1),'ow-hl.png'),PIN,cr(H,(.5,0,1,1),'ow-hr.png'),DR,FF,SD,SS,cr(H,(.15,.05,.45,.95),'ow-h2.png'),cr(DR,(.1,.1,.9,.9),'ow-d2.png')],'7','Steps','How to Organise','Your Wardrobe',"in one\nafternoon",
 ['','','','Add a second rail','File-fold drawers','Short, divided stacks','Pack off-season clean','Matching slim hangers','Category, then colour'],O+'ow-cozy.jpg',seed=611)
pin_cozy([cr(DR,(0,0,.6,1),'ow-dl.png'),cr(PIN,(0,.3,1,1),'ow-pl.png'),cr(SD,(.3,0,1,1),'ow-sr.png'),H,SD,FF,cr(SS,(.1,.2,.9,.9),'ow-s2.png'),cr(H,(.45,.05,.95,.95),'ow-h3.png'),cr(FF,(.1,.1,.9,.8),'ow-f2.png')],'90','cm','Wardrobe','Organisation Tips',"the space each\nitem needs",
 ['','','','Shirts need 90 cm','Jumpers: fold, not hang','File-fold T-shirts','No cardboard boxes','Most-worn at eye level','Stand them on end'],O+'ow-cozy2.jpg',seed=617)
sheet(O+'ow-cozy.jpg',O+'ow-cozy2.jpg','ow-pins.jpg')
