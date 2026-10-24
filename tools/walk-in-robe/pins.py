import sys,os; sys.path.insert(0,'/home/claude/dsh-pins'); os.chdir('/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
O='src/walk-in-robe/pins/'; T='tools/cozy/tiles/'; os.makedirs(O,exist_ok=True)
def cr(src,box,name):
    p=T+name; im=Image.open(src).convert('RGB'); w,h=im.size
    im.crop((int(box[0]*w),int(box[1]*h),int(box[2]*w),int(box[3]*h))).save(p); return p
s='src/walk-in-robe/walk-in-robe-ideas-'
H=s+'01-galley-robe.jpg'; L=s+'02-l-shaped-robe.jpg'; SH=s+'03-shoe-tower.jpg'; LED=s+'04-led-strip-lighting.jpg'; DR=s+'05-accessory-drawer.jpg'; BA=s+'06-before-after.jpg'
PIN=T+'wr-pin.jpg'
AF=cr(BA,(.5,0,1,1),'wr-after.png'); BF=cr(BA,(0,0,.5,1),'wr-before.png')
pin_cozy([cr(H,(0,0,.5,1),'wr-hl.png'),PIN,cr(H,(.5,0,1,1),'wr-hr.png'),L,SH,DR,LED,AF,cr(H,(.55,.1,1,.9),'wr-dbl.png')],'10','Ideas','Walk In Robe','for Every Room',"layouts, widths and\nclever storage",
 ['','','','L-shape in a corner','Shoe tower','Accessory drawer','LED strip lighting','After: clear walkway','Double hanging'],O+'wr-cozy.jpg',seed=461)
pin_cozy([BF,cr(PIN,(0,.3,1,1),'wr-pl.png'),AF,SH,L,LED,DR,H,cr(L,(.5,0,1,1),'wr-shelf.png')],'10','Ideas','Small Walk-In','Robe Storage',"how wide it needs\nto be and what fits",
 ['','','','One pair per shelf','Single wall or L-shape','Warm sensor lights','Belts and scarves','Galley, both sides','Shirts on one wall'],O+'wr-cozy2.jpg',seed=467)
a=Image.open(O+'wr-cozy.jpg').resize((500,750)); b=Image.open(O+'wr-cozy2.jpg').resize((500,750))
c=Image.new('RGB',(1010,750),'white'); c.paste(a,(0,0)); c.paste(b,(510,0)); c.save('/tmp/claude-0/-home-claude/aa9f44c6-b1c7-520d-9978-96402d6712cc/scratchpad/wr-pins.jpg')
