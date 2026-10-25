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
O='src/bedroom-colour/pins/'; os.makedirs(O,exist_ok=True); s='src/bedroom-colour/bedroom-colour-ideas-'
H=s+'01-sage-green.jpg'; NV=s+'02-navy-colour-drench.jpg'; PK=s+'03-plaster-pink.jpg'; TT=s+'04-two-tone-terracotta.jpg'; SM=s+'05-paint-samples.jpg'
PIN=cr('gen/out/bedroom-colour/06-pin.png',(0,0,1,1),'bc-pin.png')
pin_cozy([cr(H,(0,0,.5,1),'bc-hl.png'),PIN,cr(H,(.5,0,1,1),'bc-hr.png'),NV,PK,TT,SM,cr(H,(.3,0,.8,.7),'bc-h2.png'),cr(NV,(.1,.3,.8,1),'bc-n3.png')],'14','Ideas','Bedroom Colour','Ideas',"designers choose,\nfrom sage to navy",
 ['','','','Navy colour drench','Plaster pink','Two-tone terracotta','Sample big first','Soft sage green','Moody and cosy'],O+'bc-cozy.jpg',seed=711)
pin_cozy([cr(NV,(0,0,.6,1),'bc-nl.png'),cr(PIN,(0,.3,1,1),'bc-pl.png'),cr(TT,(.3,0,1,1),'bc-tr.png'),H,SM,PK,cr(NV,(.15,.2,.85,.9),'bc-n2.png'),cr(TT,(0,.3,.7,1),'bc-t2.png'),cr(H,(0,.3,.6,1),'bc-h3.png')],'14','Shades','Paint Colours','for Bedrooms',"picked by which way\nthe room faces",
 ['','','','Sage green','Test in daylight','Plaster pink','Deep navy','Terracotta','Rust accents'],O+'bc-cozy2.jpg',seed=717)
sheet(O+'bc-cozy.jpg',O+'bc-cozy2.jpg','bc-pins.jpg')
