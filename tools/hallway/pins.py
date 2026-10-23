import sys,os; sys.path.insert(0,'/home/claude/dsh-pins'); os.chdir('/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
O='src/hallway/pins/'; T='tools/cozy/tiles/'; os.makedirs(O,exist_ok=True); os.makedirs(T,exist_ok=True)
def cr(src,box,name):
    p=T+name; im=Image.open(src).convert('RGB'); w,h=im.size
    im.crop((int(box[0]*w),int(box[1]*h),int(box[2]*w),int(box[3]*h))).save(p); return p
s='src/hallway/hallway-storage-ideas-'
H=s+'01-narrow-hallway.jpg'; R=s+'02-peg-rail.jpg'; B=s+'03-storage-bench.jpg'; U=s+'04-under-stairs-pull-outs.jpg'; C=s+'05-alcove-cupboard.jpg'; BA=s+'06-before-after.jpg'
P=cr('gen/out/hallway/07-pin.png',(.25,0,1,1),'hw-pin.png')
AF=cr(BA,(.5,0,1,1),'hw-after.png')
pin_cozy([cr(H,(0,0,.5,1),'hw-hl.png'),P,cr(H,(.5,0,1,1),'hw-hr.png'),R,B,cr(U,(.2,0,.85,1),'hw-u.png'),C,AF,cr(H,(.1,.3,.45,1),'hw-cab.png')],'10','Hallway','Storage Ideas','for Narrow Halls',"slim depths that\nkeep the floor clear",
 ['','','','Peg rail at two heights','Bench with cubbies','Under-stairs pull-outs','Alcove cupboard','After: floor cleared','Slim shoe cabinet'],O+'hallway-cozy.jpg',seed=421)
pin_cozy([cr(BA,(0,0,.5,1),'hw-before.png'),cr(P,(0,.33,1,1),'hw-pl.png'),AF,U,R,cr(H,(.1,.3,.45,1),'hw-cab2.png'),B,C,cr(R,(0,.5,1,1),'hw-bench.png')],'10','Ideas','Small Hallway','Storage',"what fits in a hall\nunder 1 metre wide",
 ['','','','Fill under the stairs','Hooks, one per peg','Shoe cabinet 17 to 22 cm','Bench if 1.2 m wide','Cupboard in an alcove','Baskets under a bench'],O+'hallway-cozy2.jpg',seed=433)
a=Image.open(O+'hallway-cozy.jpg').resize((500,750)); b=Image.open(O+'hallway-cozy2.jpg').resize((500,750))
c=Image.new('RGB',(1010,750),'white'); c.paste(a,(0,0)); c.paste(b,(510,0)); c.save('/tmp/claude-0/-home-claude/aa9f44c6-b1c7-520d-9978-96402d6712cc/scratchpad/hw-pins.jpg')
