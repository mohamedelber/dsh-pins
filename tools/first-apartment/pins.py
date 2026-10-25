import sys,os; sys.path.insert(0,'/home/claude/dsh-pins'); os.chdir('/home/claude/dsh-pins')
from PIL import Image, ImageDraw, ImageFont
from pinh2 import pin_cozy
SP='/tmp/claude-0/-home-claude/aa9f44c6-b1c7-520d-9978-96402d6712cc/scratchpad/'
T='tools/cozy/tiles/'; O='src/first-apartment/pins/'; os.makedirs(O,exist_ok=True)
def cr(src,box,name):
    p=T+name; im=Image.open(src).convert('RGB'); w,h=im.size
    im.crop((int(box[0]*w),int(box[1]*h),int(box[2]*w),int(box[3]*h))).save(p); return p
s='src/first-apartment/first-apartment-checklist-'
H=s+'01-move-in-day.jpg'; K=s+'02-kitchen-basics.jpg'; B=s+'03-bathroom-basics.jpg'; TL=s+'04-tools-safety.jpg'
PIN=cr('gen/out/first-apartment/05-pin.png',(0,0,1,1),'fa-pin.png')
pin_cozy([cr(H,(0,0,.5,1),'fa-hl.png'),PIN,cr(H,(.5,0,1,1),'fa-hr.png'),K,B,TL,cr(H,(.05,.35,.45,1),'fa-h2.png'),cr(K,(.1,.3,.9,1),'fa-k2.png'),cr(TL,(.5,0,1,.6),'fa-t2.png')],'53','Items','First Apartment','Checklist',"free printable,\nwhat to buy and when",
 ['','','','Kitchen basics','Bathroom on Day 1','Tools and safety','Photograph every room','Two cutting boards','A fire extinguisher'],O+'fa-cozy.jpg',seed=631)
W,Hh=1000,1500; c=Image.new('RGB',(W,Hh),'#F7F1E9'); d=ImageDraw.Draw(c)
F='tools/first-apartment/f/'
t1=ImageFont.truetype(F+'Lora-B.ttf',74); t2=ImageFont.truetype(F+'Mont-B.ttf',30); t3=ImageFont.truetype(F+'Mont-R.ttf',28)
d.text((W//2,70),'FREE PRINTABLE',font=t2,fill='#C85A32',anchor='mm')
d.text((W//2,160),'First Apartment Checklist',font=t1,fill='#342E2A',anchor='mm')
d.text((W//2,245),'53 items · tagged Before, Day 1, Week 1, Later',font=t3,fill='#6E645C',anchor='mm')
pg=Image.open(SP+'fahi-1.png').convert('RGB'); pg.thumbnail((860,1120))
x=(W-pg.width)//2; y=300
d.rectangle((x+12,y+14,x+pg.width+12,y+pg.height+14),fill='#D8CBBB'); c.paste(pg,(x,y))
d.text((W//2,Hh-40),'dailyspacehacks.com',font=t3,fill='#6E645C',anchor='mm')
c.save(O+'fa-printable.jpg',quality=88)
a=Image.open(O+'fa-cozy.jpg').resize((500,750)); b=c.resize((500,750)); s2=Image.new('RGB',(1010,750),'white'); s2.paste(a,(0,0)); s2.paste(b,(510,0)); s2.save(SP+'fa-pins.jpg')
