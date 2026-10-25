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
O='src/small-porch/pins/'; os.makedirs(O,exist_ok=True); s='src/small-porch/small-porch-ideas-'
H=s+'01-inside-porch.jpg'; EX=s+'02-brick-porch.jpg'; SB=s+'03-shoe-bench.jpg'; CA=s+'04-canopy-porch.jpg'; PL=s+'05-porch-plants.jpg'
PIN=cr('gen/out/small-porch/06-pin.png',(0,0,1,1),'po-pin.png')
pin_cozy([cr(H,(0,0,.5,1),'po-hl.png'),PIN,cr(H,(.5,0,1,1),'po-hr.png'),SB,CA,PL,EX,cr(H,(0,.4,.5,1),'po-h2.png'),cr(PL,(.1,.2,.7,.9),'po-p2.png')],'11','Ideas','Small Porch','Ideas',"for a tiny UK\nentrance",
 ['','','','A bench for shoes','An open canopy','Plants and a mirror','Brick and glass porch','Hooks, not a stand','A sill for plants'],O+'po-cozy.jpg',seed=601)
pin_cozy([cr(SB,(0,0,.6,1),'po-sl.png'),cr(PIN,(0,.3,1,1),'po-pl.png'),cr(CA,(.3,0,1,1),'po-cr.png'),EX,H,SB,cr(CA,(.2,.3,.8,1),'po-c2.png'),cr(H,(.3,.5,.9,1),'po-h3.png'),cr(PL,(.4,.4,1,1),'po-p3.png')],'3','m²','Small Porch','Rules and Sizes',"sizes, rules\nand costs",
 ['','','','Up to 3 m² outside','Mat 80% of the door','Bench 40 cm deep','A tiled step','Grippy, frost-proof floor','Warm white light'],O+'po-cozy2.jpg',seed=607)
sheet(O+'po-cozy.jpg',O+'po-cozy2.jpg','po-pins.jpg')
