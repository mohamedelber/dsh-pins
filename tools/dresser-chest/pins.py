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
O='src/dresser-chest/pins/'; os.makedirs(O,exist_ok=True); s='src/dresser-chest/dresser-vs-chest-of-drawers-'
H=s+'01-side-by-side.jpg'; D=s+'02-dresser.jpg'; C=s+'03-chest-of-drawers.jpg'; AN=s+'04-anti-tip-strap.jpg'; DR=s+'05-drawer-dividers.jpg'
PIN=cr('gen/out/dresser-chest/06-pin.png',(0,0,1,1),'dc-pin.png')
pin_cozy([cr(H,(0,0,.6,1),'dc-hl.png'),PIN,cr(H,(.6,0,1,1),'dc-hr.png'),D,C,AN,DR,cr(H,(.08,.35,.62,.85),'dc-h2.png'),cr(C,(.55,.1,1,.9),'dc-c2.png')],'vs','','Dresser or','Chest of Drawers?',"which fits your\nbedroom better",
 ['','','','Wide dresser','Tall chest','Anchor it','Drawer dividers','Wide and low','Fits a narrow wall'],O+'dc-cozy.jpg',seed=731)
pin_cozy([cr(C,(.4,0,1,1),'dc-cl.png'),cr(PIN,(0,.3,1,1),'dc-pl.png'),cr(D,(0,0,.65,1),'dc-dl.png'),C,D,DR,AN,cr(H,(.6,0,1,1),'dc-hr2.png'),cr(DR,(0,0,.7,.8),'dc-d2.png')],'81','%','Tall Chest:','Half the Floor',"81% of the storage of\nthe same wide dresser",
 ['','','','Narrow wall pick','Long wall pick','File-fold clothes','Anti-tip strap','Tall and narrow','Top drawer first'],O+'dc-cozy2.jpg',seed=737)
sheet(O+'dc-cozy.jpg',O+'dc-cozy2.jpg','dc-pins.jpg')
