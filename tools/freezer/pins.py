import sys,os; sys.path.insert(0,'/home/claude/dsh-pins'); os.chdir('/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
O='src/freezer/pins/'; T='tools/cozy/tiles/'; os.makedirs(O,exist_ok=True)
def cr(src,box,name):
    p=T+name; im=Image.open(src).convert('RGB'); w,h=im.size
    im.crop((int(box[0]*w),int(box[1]*h),int(box[2]*w),int(box[3]*h))).save(p); return p
s='src/freezer/chest-freezer-vs-upright-freezer-'
H=s+'01-chest-and-upright.jpg'; C=s+'02-chest-baskets.jpg'; U=s+'03-upright-shelves.jpg'
PIN=cr('gen/out/freezer/04-pin.png',(0,0,1,1),'fz-pin.png')
pin_cozy([cr(H,(0,0,.5,1),'fz-hl.png'),PIN,cr(H,(.5,0,1,1),'fz-hr.png'),C,U,H,cr(C,(.1,.1,.7,.9),'fz-c2.png'),cr(U,(.3,.45,.65,.85),'fz-u2.png'),cr(U,(.6,.05,.85,.55),'fz-u3.png')],'2','Freezers','Chest Freezer vs','Upright Freezer',"which is better\nfor your home",
 ['','','','Baskets and bins','Shelves and drawers','Basement or garage?','Lower running cost','Pull-out drawers','Door bins'],O+'fz-cozy.jpg',seed=531)
pin_cozy([cr(U,(0,0,1,1),'fz-uf.png'),cr(PIN,(0,.3,1,1),'fz-pl.png'),cr(C,(0,0,1,1),'fz-cf.png'),H,C,U,cr(H,(0,.3,.55,1),'fz-h2.png'),cr(C,(.1,.1,.7,.9),'fz-c3.png'),cr(U,(.3,.45,.65,.85),'fz-u4.png')],'5','Questions','Chest or Upright','Freezer?',"cost, space and\norganization compared",
 ['','','','Smaller footprint','Buy in bulk? Chest','Food at eye level','Set it to 0°F','Sort food into bins','Easy to see food'],O+'fz-cozy2.jpg',seed=541)
a=Image.open(O+'fz-cozy.jpg').resize((500,750)); b=Image.open(O+'fz-cozy2.jpg').resize((500,750))
c=Image.new('RGB',(1010,750),'white'); c.paste(a,(0,0)); c.paste(b,(510,0)); c.save('/tmp/claude-0/-home-claude/aa9f44c6-b1c7-520d-9978-96402d6712cc/scratchpad/fz-pins.jpg')
