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
O='src/small-ensuite/pins/'; os.makedirs(O,exist_ok=True); s='src/small-ensuite/small-ensuite-ideas-'
H=s+'01-skylight-ensuite.jpg'; N=s+'02-shower-niche.jpg'; V=s+'03-wall-hung-vanity.jpg'; C=s+'04-cavity-slider.jpg'; TL=s+'05-sage-tiles.jpg'
PIN=cr('gen/out/small-ensuite/06-pin.png',(0,0,1,1),'se-pin.png')
pin_cozy([cr(H,(0,0,.5,1),'se-hl.png'),PIN,cr(H,(.5,0,1,1),'se-hr.png'),N,V,C,TL,cr(H,(.35,.3,.75,1),'se-h2.png'),cr(H,(.15,0,.6,.45),'se-h3.png')],'10','Ideas','Small Ensuite','Ideas',"for Australian\nhomes",
 ['','','','A recessed niche','Wall-hung vanity','A cavity slider','Large, calm tiles','Drawers, not doors','A skylight'],O+'se-cozy.jpg',seed=641)
pin_cozy([cr(V,(0,0,.6,1),'se-vl.png'),cr(PIN,(0,.3,1,1),'se-pl.png'),cr(TL,(.3,0,1,1),'se-tr.png'),H,N,C,cr(TL,(.1,.2,.9,.9),'se-t2.png'),cr(N,(.1,.1,.7,.8),'se-n2.png'),cr(V,(.1,.3,.9,1),'se-v2.png')],'1.8','x 2.0 m','Small Ensuite','Layout and Rules',"what fits in\n3.6 m²",
 ['','','','Frameless glass screen','Niche 900 mm up','Slider saves floor','Waterproof to 1800 mm','Hand-held shower rail','LED under the vanity'],O+'se-cozy2.jpg',seed=647)
sheet(O+'se-cozy.jpg',O+'se-cozy2.jpg','se-pins.jpg')
