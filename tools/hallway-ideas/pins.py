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
# hallway
O='src/hallway-ideas/pins/'; os.makedirs(O,exist_ok=True); s='src/hallway-ideas/hallway-ideas-'
H=s+'01-victorian-hallway.jpg'; PF=s+'02-picture-frame-panelling.jpg'; DG=s+'03-dark-green-hallway.jpg'; SR=s+'04-stair-runner.jpg'; WP=s+'05-wallpaper-panelling.jpg'
PIN=cr('gen/out/hallway-ideas/06-pin.png',(0,0,1,1),'hw-pin.png')
pin_cozy([cr(H,(0,0,.5,1),'hw-hl.png'),PIN,cr(H,(.5,0,1,1),'hw-hr.png'),PF,DG,SR,WP,cr(H,(.2,.5,.8,1),'hw-h2.png'),cr(DG,(.2,.1,.8,.9),'hw-d2.png')],'11','Ideas','Hallway Ideas','That Work',"paint, panelling\nand light",
 ['','','','Picture-frame panels','A dark colour drench','A gallery up the stairs','Paper above panelling','Keep old Victorian tiles','Trim the same colour'],O+'hw-cozy.jpg',seed=581)
pin_cozy([cr(PF,(0,0,.6,1),'hw-pl.png'),cr(PIN,(0,.3,1,1),'hw-pl2.png'),cr(WP,(.3,0,1,1),'hw-wr.png'),H,DG,SR,cr(PF,(.2,.1,.9,.9),'hw-p2.png'),cr(SR,(.1,.1,.9,.9),'hw-s2.png'),cr(WP,(.1,.2,.8,.9),'hw-w2.png')],'85','to 100 cm','Hallway Decor','Ideas',"the heights that\nmake them work",
 ['','','','Dado at about 1/3','Lights at 170 to 180 cm','Art centred at 145 cm','Wipeable paint','10 cm each side of runner','Paper above the dado'],O+'hw-cozy2.jpg',seed=587)
sheet(O+'hw-cozy.jpg',O+'hw-cozy2.jpg','hw-pins.jpg')
# feng shui
O='src/feng-shui/pins/'; os.makedirs(O,exist_ok=True); s='src/feng-shui/feng-shui-bedroom-'
H=s+'01-calm-bedroom.jpg'; CP=s+'02-commanding-position.jpg'; NS=s+'03-nightstand.jpg'; MR=s+'04-mirror-placement.jpg'
PIN=cr('gen/out/feng-shui/05-pin.png',(0,0,1,1),'fs-pin.png')
pin_cozy([cr(H,(0,0,.5,1),'fs-hl.png'),PIN,cr(H,(.5,0,1,1),'fs-hr.png'),CP,NS,MR,cr(H,(.25,.3,.75,.9),'fs-h2.png'),cr(CP,(.1,.1,.9,.9),'fs-c2.png'),cr(NS,(.2,.1,.8,.9),'fs-n2.png')],'7','Steps','Feng Shui','Bedroom',"a calm layout,\nstep by step",
 ['','','','Commanding position','Two nightstands','Mirror away from the bed','Clear under the bed','Solid wall behind','Soft, earthy colors'],O+'fs-cozy.jpg',seed=593)
pin_cozy([cr(CP,(0,0,.6,1),'fs-cl.png'),cr(PIN,(0,.3,1,1),'fs-pl.png'),cr(MR,(.3,0,1,1),'fs-mr.png'),H,NS,MR,cr(CP,(.2,.1,.9,.9),'fs-c3.png'),cr(H,(.25,.3,.75,.9),'fs-h3.png'),cr(NS,(.2,.1,.8,.9),'fs-n3.png')],'24','Inches','Feng Shui','Bedroom Layout',"where to put\nthe bed",
 ['','','','See the door, not in line','No window behind','Cover mirrored doors','24 in on each side','Earthy, soft tones','Dark, cool and quiet'],O+'fs-cozy2.jpg',seed=599)
sheet(O+'fs-cozy.jpg',O+'fs-cozy2.jpg','fs-pins.jpg')
