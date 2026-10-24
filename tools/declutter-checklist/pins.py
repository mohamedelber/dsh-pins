import sys,os; sys.path.insert(0,'/home/claude/dsh-pins'); os.chdir('/home/claude/dsh-pins')
from PIL import Image, ImageDraw, ImageFont
from pinh2 import pin_cozy
T='tools/cozy/tiles/'; O='src/declutter/pins/'; os.makedirs(O,exist_ok=True)
def cr(src,box,name):
    p=T+name; im=Image.open(src).convert('RGB'); w,h=im.size
    im.crop((int(box[0]*w),int(box[1]*h),int(box[2]*w),int(box[3]*h))).save(p); return p
H='src/declutter/declutter-checklist-01-four-boxes.jpg'; PIN=cr('gen/out/declutter/02-pin.png',(0,0,1,1),'dc-pin.png')
pin_cozy([cr(H,(0,0,.5,1),'dc-hl.png'),PIN,cr(H,(.5,0,1,1),'dc-hr.png'),cr(H,(0,.2,.3,.8),'dc-b1.png'),cr(H,(.27,.2,.53,.8),'dc-b2.png'),cr(H,(.5,.2,.76,.8),'dc-b3.png'),cr(H,(.73,.2,1,.8),'dc-b4.png'),cr(PIN,(.15,.5,.95,1),'dc-p2.png'),cr(H,(.05,.6,.4,1),'dc-clip.png')],'44','Items','Declutter','Checklist',"free printable,\nroom by room",
 ['','','','Donate','Books and mugs','Old tech: take-back','Shred papers','A clear closet','Tick as you go'],O+'dc-cozy.jpg',seed=581)
# pin 2: printable page
W,Hh=1000,1500; c=Image.new('RGB',(W,Hh),'#F7F1E9'); d=ImageDraw.Draw(c)
F='tools/declutter-checklist/f/'
t1=ImageFont.truetype(F+'Lora-B.ttf',82); t2=ImageFont.truetype(F+'Mont-B.ttf',30); t3=ImageFont.truetype(F+'Mont-R.ttf',28)
d.text((W//2,70),'FREE PRINTABLE',font=t2,fill='#C85A32',anchor='mm')
d.text((W//2,160),'Declutter Checklist',font=t1,fill='#342E2A',anchor='mm')
d.text((W//2,245),'7 rooms · 44 items · where each one goes',font=t3,fill='#6E645C',anchor='mm')
pg=Image.open('/tmp/claude-0/-home-claude/aa9f44c6-b1c7-520d-9978-96402d6712cc/scratchpad/dchi-1.png').convert('RGB'); pg.thumbnail((860,1120))
x=(W-pg.width)//2; y=300
d.rectangle((x+12,y+14,x+pg.width+12,y+pg.height+14),fill='#D8CBBB'); c.paste(pg,(x,y))
d.text((W//2,Hh-40),'dailyspacehacks.com',font=t3,fill='#6E645C',anchor='mm')
c.save(O+'dc-printable.jpg',quality=88)
a=Image.open(O+'dc-cozy.jpg').resize((500,750)); b=c.resize((500,750)); s=Image.new('RGB',(1010,750),'white'); s.paste(a,(0,0)); s.paste(b,(510,0)); s.save('/tmp/claude-0/-home-claude/aa9f44c6-b1c7-520d-9978-96402d6712cc/scratchpad/dc-pins.jpg')
