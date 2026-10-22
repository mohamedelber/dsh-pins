import sys,os; sys.path.insert(0,'/home/claude/dsh-pins'); os.chdir('/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
O='src/au-laundry/pins/'; T='tools/cozy/tiles/'
def cr(src,box,name):
    p=T+name; im=Image.open(src).convert('RGB'); w,h=im.size
    im.crop((int(box[0]*w),int(box[1]*h),int(box[2]*w),int(box[3]*h))).save(p); return p
g='gen/out/au-laundry/'; H=g+'01-hero.png'; S=g+'02-side-by-side.png'; G=g+'03-galley-fix.png'; B=g+'04-bathroom-fix.png'; P=g+'05-pin.png'
pin_cozy([cr(H,(0,0,.5,1),'al-hl.png'),P,cr(H,(.5,0,1,1),'al-hr.png'),H,S,G,B,cr(S,(.55,0,1,1),'al-tub.png'),cr(G,(.5,0,1,1),'al-shelf.png')],'7','Steps','to Plan a','Small Laundry',"layouts, tubs\nand storage",
 ['','','','Single wall','Side by side','Galley layout','Laundry in a bathroom','Tub in the benchtop','Shelves opposite'],O+'small-laundry-cozy.jpg',seed=301)
pin_cozy([cr(S,(0,0,.5,1),'al-sl.png'),cr(P,(0,.33,1,1),'al-pinlow.png'),cr(B,(.4,0,1,1),'al-br.png'),G,cr(H,(0,0,.6,1),'al-stack.png'),S,B,H,cr(G,(0,0,.5,1),'al-gl.png')],'5','Small','Laundry','Layouts',"in mm that\nreally fit",
 ['','','','Galley layout','Stack to save width','Machines under a benchtop','Laundry in a bathroom','Single wall with a tub','Clear walkway'],O+'small-laundry-cozy2.jpg',seed=307)
a=Image.open(O+'small-laundry-cozy.jpg').resize((500,750)); b=Image.open(O+'small-laundry-cozy2.jpg').resize((500,750))
s=Image.new('RGB',(1010,750),'white'); s.paste(a,(0,0)); s.paste(b,(510,0)); s.save('/tmp/claude-0/-home-claude/66ced7db-2a2d-58db-8d1b-26fd0ebe8295/scratchpad/al-pins.jpg')
