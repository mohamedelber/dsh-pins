import sys,os; sys.path.insert(0,'/home/claude/dsh-pins'); os.chdir('/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
O='src/kitchen-cupboards/pins/'; T='tools/cozy/tiles/'; os.makedirs(O,exist_ok=True)
def cr(src,box,name):
    p=T+name; im=Image.open(src).convert('RGB'); w,h=im.size
    im.crop((int(box[0]*w),int(box[1]*h),int(box[2]*w),int(box[3]*h))).save(p); return p
s='src/kitchen-cupboards/how-to-organise-kitchen-cupboards-'
H=s+'01-organised-cupboards.jpg'; S=s+'02-sorted-worktop.jpg'; P=s+'03-pan-drawer.jpg'; C=s+'04-turntable-riser.jpg'; BA=s+'05-before-after.jpg'
PIN=cr('gen/out/kitchen-cupboards/07-pin.png',(0,0,1,1),'kc-pin.png')
AF=cr(BA,(.5,0,1,.6),'kc-after.png'); BF=cr(BA,(0,0,.5,.6),'kc-before.png')
pin_cozy([cr(H,(0,0,.5,1),'kc-hl.png'),PIN,cr(H,(.5,0,1,1),'kc-hr.png'),S,P,C,BF,AF,cr(H,(.25,0,.75,.5),'kc-shelf.png')],'7','Steps','How to Organise','Kitchen Cupboards',"what goes where\nin a UK kitchen",
 ['','','','Sort into groups','Pans low, lids upright','Turntable and riser','Before','After','Bowls above plates'],O+'kc-cozy.jpg',seed=441)
pin_cozy([BF,cr(PIN,(0,.3,1,1),'kc-pl.png'),AF,C,P,cr(H,(.25,0,.75,.5),'kc-shelf2.png'),S,H,cr(S,(.5,0,1,1),'kc-s2.png')],'7','Easy Steps','Kitchen Cupboard','Organisation',"shelf risers, lid racks\nand zones that work",
 ['','','','Spin the corner','Nest the saucepans','Shelf riser for bowls','Empty and sort first','Jars on the top shelf','Give-away box'],O+'kc-cozy2.jpg',seed=449)
a=Image.open(O+'kc-cozy.jpg').resize((500,750)); b=Image.open(O+'kc-cozy2.jpg').resize((500,750))
c=Image.new('RGB',(1010,750),'white'); c.paste(a,(0,0)); c.paste(b,(510,0)); c.save('/tmp/claude-0/-home-claude/aa9f44c6-b1c7-520d-9978-96402d6712cc/scratchpad/kc-pins.jpg')
