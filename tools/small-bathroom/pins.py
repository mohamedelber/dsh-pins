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
O='src/small-bathroom/pins/'; os.makedirs(O,exist_ok=True); s='src/small-bathroom/small-bathroom-ideas-'
H=s+'01-5x8-bathroom.jpg'; CS=s+'02-curbless-shower.jpg'; WM=s+'03-wall-mounted-sink.jpg'; WP=s+'04-wallpaper.jpg'; PD=s+'05-pocket-door.jpg'
PIN=cr('gen/out/small-bathroom/06-pin.png',(0,0,1,1),'sb-pin.png')
pin_cozy([cr(H,(0,0,.5,1),'sb-hl.png'),PIN,cr(H,(.5,0,1,1),'sb-hr.png'),CS,WM,WP,PD,cr(H,(.3,.05,.75,.75),'sb-h2.png'),cr(H,(0,0,.45,.8),'sb-h3.png')],'12','Ideas','Small Bathroom','Ideas',"that make a tiny\nbath feel bigger",
 ['','','','Curbless shower','Wall-mounted sink','Powder room wallpaper','A pocket door','Mirror and sconces','Glass, not a curtain'],O+'sb-cozy.jpg',seed=651)
pin_cozy([cr(CS,(0,0,.6,1),'sb-cl.png'),cr(PIN,(0,.3,1,1),'sb-pl.png'),cr(WP,(.3,0,1,1),'sb-wr.png'),H,PD,CS,cr(H,(.3,.05,.75,.75),'sb-h4.png'),cr(WM,(.1,.1,.9,.9),'sb-w2.png'),cr(H,(.25,.45,.75,1),'sb-h5.png')],'5','x 8 ft','Small Bathroom','Layout Guide',"code vs NKBA\nclearances",
 ['','','','Vanity 21 in deep','Pocket door: 10 sq ft','Large tile, few lines','Sconces 65-70 in up','Half bath tricks','Floating vanity'],O+'sb-cozy2.jpg',seed=657)
sheet(O+'sb-cozy.jpg',O+'sb-cozy2.jpg','sb-pins.jpg')
