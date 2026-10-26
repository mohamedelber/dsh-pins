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
O='src/blanket-storage/pins/'; os.makedirs(O,exist_ok=True); s='src/blanket-storage/blanket-storage-ideas-'
H=s+'01-basket-and-ladder.jpg'; L=s+'02-blanket-ladder.jpg'; B=s+'03-storage-bench.jpg'; U=s+'04-under-bed-box.jpg'; C=s+'05-linen-closet.jpg'
PIN=cr('gen/out/blanket-storage/06-pin.png',(0,0,1,1),'bs-pin.png')
pin_cozy([cr(H,(0,0,.5,1),'bs-hl.png'),PIN,cr(H,(.5,0,1,1),'bs-hr.png'),L,B,U,C,cr(H,(.3,.3,.75,.9),'bs-h2.png'),cr(C,(.3,0,1,.4),'bs-c2.png')],'14','Ideas','Blanket Storage','Ideas',"for throws and\nbulky comforters",
 ['','','','Leaning ladder','Bench at the bed foot','Under-bed box','Linen closet shelves','Basket by the sofa','Cotton bags up top'],O+'bs-cozy.jpg',seed=751)
pin_cozy([cr(H,(.45,0,1,1),'bs-hl2.png'),cr(PIN,(0,.3,1,1),'bs-pl.png'),cr(L,(.3,0,1,1),'bs-lr.png'),H,U,B,C,cr(U,(0,.3,.7,1),'bs-u2.png'),cr(B,(.1,.3,.9,.9),'bs-b2.png')],'8','inches','Will It Fit','Under the Bed?',"measure first, then\nstore your blankets",
 ['','','','Rolled throws','Low box on wheels','Ottoman or bench','Top shelf for bulk','Check the clearance','Fold to fit'],O+'bs-cozy2.jpg',seed=757)
sheet(O+'bs-cozy.jpg',O+'bs-cozy2.jpg','bs-pins.jpg')
