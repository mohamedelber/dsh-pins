import sys,os; sys.path.insert(0,'/home/claude/dsh-pins'); os.chdir('/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
O='src/garage-uk/pins/'; T='tools/cozy/tiles/'; os.makedirs(O,exist_ok=True)
def cr(src,box,name):
    p=T+name; im=Image.open(src).convert('RGB'); w,h=im.size
    im.crop((int(box[0]*w),int(box[1]*h),int(box[2]*w),int(box[3]*h))).save(p); return p
s='src/garage-uk/garage-storage-ideas-'
H=s+'01-tidy-garage.jpg'; B=s+'02-shelving-boxes.jpg'; K=s+'03-bikes-on-hooks.jpg'; P=s+'04-pegboard-workbench.jpg'; G=s+'05-garden-tool-rail.jpg'; BA=s+'06-before-after.jpg'
PIN=cr('gen/out/garage-uk/07-pin.png',(0,0,1,1),'gg-pin.png')
AF=cr(BA,(.5,0,1,1),'gg-after.png'); BF=cr(BA,(0,0,.5,1),'gg-before.png')
pin_cozy([cr(H,(0,0,.5,1),'gg-hl.png'),PIN,cr(H,(.5,0,1,1),'gg-hr.png'),B,K,P,G,BF,AF],'10','Garage','Storage Ideas','to Clear the Floor',"shelving, hooks and\na pegboard wall",
 ['','','','Lidded boxes on shelves','Bikes on wall hooks','Pegboard over a bench','Garden tool rail','Before','After'],O+'gg-cozy.jpg',seed=481)
pin_cozy([BF,cr(PIN,(0,.3,1,1),'gg-pl.png'),AF,K,B,G,P,cr(H,(.6,.15,1,.75),'gg-bikes2.png'),cr(B,(0,.3,1,.9),'gg-b2.png')],'10','Ideas','Small Garage','Storage UK',"what fits in a\nsingle garage",
 ['','','','30 cm of wall per bike','Shelving rated per shelf','Tools heads up','Every tool on a hook','Hang bikes by the wheel','Clear boxes with lids'],O+'gg-cozy2.jpg',seed=487)
a=Image.open(O+'gg-cozy.jpg').resize((500,750)); b=Image.open(O+'gg-cozy2.jpg').resize((500,750))
c=Image.new('RGB',(1010,750),'white'); c.paste(a,(0,0)); c.paste(b,(510,0)); c.save('/tmp/claude-0/-home-claude/aa9f44c6-b1c7-520d-9978-96402d6712cc/scratchpad/gg-pins.jpg')
