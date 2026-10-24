import sys,os; sys.path.insert(0,'/home/claude/dsh-pins'); os.chdir('/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
T='tools/cozy/tiles/'
def cr(src,box,name):
    p=T+name; im=Image.open(src).convert('RGB'); w,h=im.size
    im.crop((int(box[0]*w),int(box[1]*h),int(box[2]*w),int(box[3]*h))).save(p); return p
SP='/tmp/claude-0/-home-claude/aa9f44c6-b1c7-520d-9978-96402d6712cc/scratchpad/'
def sheet(a,b,n):
    a=Image.open(a).resize((500,750)); b=Image.open(b).resize((500,750))
    c=Image.new('RGB',(1010,750),'white'); c.paste(a,(0,0)); c.paste(b,(510,0)); c.save(SP+n)
# drying
O='src/drying/pins/'; os.makedirs(O,exist_ok=True); s='src/drying/how-to-dry-clothes-indoors-'
H=s+'01-bathroom-airer.jpg'; A=s+'02-airer-not-radiator.jpg'; D=s+'03-dehumidifier.jpg'
PIN=cr('gen/out/drying/04-pin.png',(0,0,1,1),'dr-pin.png')
pin_cozy([cr(H,(0,0,.5,1),'dr-hl.png'),PIN,cr(H,(.5,0,1,1),'dr-hr.png'),H,A,D,cr(A,(.15,.1,.75,.9),'dr-a2.png'),cr(D,(.5,.2,1,.9),'dr-d2.png'),cr(H,(.1,0,.6,.6),'dr-h2.png')],'7','Steps','How to Dry Clothes','Indoors',"without damp\nor mould",
 ['','','','One room, door shut','Airer, not radiator','Dehumidifier on','Space between items','Laundry mode','Window slightly open'],O+'dr-cozy.jpg',seed=491)
pin_cozy([cr(A,(0,0,.5,1),'dr-al.png'),cr(PIN,(0,.3,1,1),'dr-pl.png'),cr(A,(.5,0,1,1),'dr-ar.png'),D,H,A,cr(D,(.5,.2,1,.9),'dr-d3.png'),cr(H,(.1,0,.6,.6),'dr-h3.png'),cr(A,(.15,.1,.75,.9),'dr-a3.png')],'2','Litres','Drying Clothes','Indoors in Winter',"what each load\nadds to the air",
 ['','','','About 52p a load','Use the fastest spin','Keep off radiators','Check the humidity','Open a window','Hang shirts on hangers'],O+'dr-cozy2.jpg',seed=497)
sheet(O+'dr-cozy.jpg',O+'dr-cozy2.jpg','dr-pins.jpg')
# dehum
O='src/dehum/pins/'; os.makedirs(O,exist_ok=True); s='src/dehum/dehumidifier-vs-tumble-dryer-'
U=s+'01-utility-room.jpg'; DA=s+'02-dehumidifier-airer.jpg'; F=s+'03-dryer-filter.jpg'; PIN=T+'dh-pin.jpg'
pin_cozy([cr(U,(0,0,.5,1),'dh-ul.png'),PIN,cr(U,(.5,0,1,1),'dh-ur.png'),DA,F,U,cr(DA,(.45,.2,1,1),'dh-d2.png'),cr(F,(.1,.15,.8,1),'dh-f2.png'),cr(DA,(0,0,.6,.9),'dh-a2.png')],'5','Years','Dehumidifier vs','Tumble Dryer',"which is cheaper\nto dry clothes",
 ['','','','Dries the house too','Clean the filter','Room for both?','About 52p a load','Heat pump: about 35p','Slower but small'],O+'dh-cozy.jpg',seed=501)
pin_cozy([cr(F,(0,0,.6,1),'dh-fl.png'),cr(PIN,(0,.3,1,1),'dh-pl.png'),cr(DA,(.4,0,1,1),'dh-dr.png'),U,DA,F,cr(U,(.5,.2,1,1),'dh-u2.png'),cr(DA,(0,0,.6,.9),'dh-a3.png'),cr(F,(.1,.15,.8,1),'dh-f3.png')],'5','Questions','Dryer or','Dehumidifier?',"cost, speed, space\nand damp compared",
 ['','','','Room for both?','Best for small flats','Best for daily washing','Needs a dedicated spot','Dry on an airer','Clean the lint filter'],O+'dh-cozy2.jpg',seed=503)
sheet(O+'dh-cozy.jpg',O+'dh-cozy2.jpg','dh-pins.jpg')
# cosy
O='src/cosy-bedroom/pins/'; os.makedirs(O,exist_ok=True); s='src/cosy-bedroom/cosy-bedroom-ideas-'
W1=s+'01-warm-bedroom.jpg'; L=s+'02-bedside-lighting.jpg'; B=s+'03-layered-bedding.jpg'; C=s+'04-lined-curtains.jpg'; R=s+'05-reading-corner.jpg'; BA=s+'06-before-after.jpg'
PIN=cr('gen/out/cosy-bedroom/07-pin.png',(0,0,1,1),'cb-pin.png')
BF=cr(BA,(0,0,.5,1),'cb-before.png'); AF=cr(BA,(.5,0,1,1),'cb-after.png')
pin_cozy([cr(W1,(0,0,.5,1),'cb-wl.png'),PIN,cr(W1,(.5,0,1,1),'cb-wr.png'),L,B,C,R,BF,AF],'10','Ideas','Cosy Bedroom','Ideas',"to make a small\nroom feel warm",
 ['','','','Two warm lamps','Layer the bed','Lined curtains','A reading corner','Before','After'],O+'cb-cozy.jpg',seed=509)
pin_cozy([BF,cr(PIN,(0,.3,1,1),'cb-pl.png'),AF,B,L,R,C,cr(W1,(.2,.4,.8,1),'cb-rug.png'),cr(B,(.2,.1,.8,.9),'cb-b2.png')],'16','to 18°C','Cosy Small','Bedroom Ideas',"warm, soft light\nand texture",
 ['','','','13.5 tog for winter','Warm white 2700K','One chair, one lamp','Keep radiators clear','Knitted throw on top','Mix textures'],O+'cb-cozy2.jpg',seed=521)
sheet(O+'cb-cozy.jpg',O+'cb-cozy2.jpg','cb-pins.jpg')
