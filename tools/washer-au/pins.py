import sys,os; sys.path.insert(0,'/home/claude/dsh-pins'); os.chdir('/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
O='src/washer-au/pins/'; T='tools/cozy/tiles/'; os.makedirs(O,exist_ok=True)
def cr(src,box,name):
    p=T+name; im=Image.open(src).convert('RGB'); w,h=im.size
    im.crop((int(box[0]*w),int(box[1]*h),int(box[2]*w),int(box[3]*h))).save(p); return p
s='src/washer-au/front-loader-vs-top-loader-'
H=s+'01-side-by-side.jpg'; F=s+'02-front-loader-under-bench.jpg'; TL=s+'03-top-loader-lid-open.jpg'; SE=s+'04-door-seal.jpg'
PIN=cr('gen/out/washer-au/05-pin.png',(0,0,1,1),'wa-pin.png')
HF=cr(H,(0,0,.5,1),'wa-hf.png'); HT=cr(H,(.5,0,1,1),'wa-ht.png')
pin_cozy([HF,PIN,HT,F,TL,SE,cr(F,(0,.2,.6,1),'wa-f2.png'),cr(TL,(.1,0,.7,1),'wa-t2.png'),cr(SE,(.15,.1,.85,.9),'wa-s2.png')],'2','Washers','Front Loader vs','Top Loader',"which is better\nfor your laundry",
 ['','','','Fits under a bench','Lid needs space above','Leave the door open','Less water per wash','Quicker cycles','Dry the door seal'],O+'wa-cozy.jpg',seed=471)
pin_cozy([HT,cr(PIN,(0,.3,1,1),'wa-pl.png'),HF,TL,F,SE,cr(TL,(.1,0,.7,1),'wa-t3.png'),cr(F,(0,.2,.6,1),'wa-f3.png'),cr(SE,(.15,.1,.85,.9),'wa-s3.png')],'5','Questions','Front or Top','Loader Washer?',"water, speed, price\nand space compared",
 ['','','','Cheaper to buy','Spins clothes drier','Musty smell? Air it','Clear space above','Under a benchtop','Wipe the seal'],O+'wa-cozy2.jpg',seed=479)
a=Image.open(O+'wa-cozy.jpg').resize((500,750)); b=Image.open(O+'wa-cozy2.jpg').resize((500,750))
c=Image.new('RGB',(1010,750),'white'); c.paste(a,(0,0)); c.paste(b,(510,0)); c.save('/tmp/claude-0/-home-claude/aa9f44c6-b1c7-520d-9978-96402d6712cc/scratchpad/wa-pins.jpg')
