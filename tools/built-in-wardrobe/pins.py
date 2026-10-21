import sys,os; sys.path.insert(0,'/home/claude/dsh-pins'); os.chdir('/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
O='src/built-in-wardrobe/pins/'; T='tools/cozy/tiles/'
def cr(src,box,name):
    p=T+name; Image.open(src).crop(box).save(p); return p
g='gen/out/built-in-wardrobe/'
H=g+'01-hero.png'; AL=g+'02-alcove.png'; IN=g+'03-interior.png'; EV=g+'04-eaves.png'; SL=g+'05-sliding.png'; P=g+'06-pin.png'
inL=cr(IN,(60,0,1060,1024),'bw-inl.png'); inR=cr(IN,(1040,0,1536,1024),'bw-inr.png')
pin_cozy([cr(H,(0,0,768,1024),'bw-hl.png'),P,cr(H,(768,0,1536,1024),'bw-hr.png'),H,AL,inL,EV,SL,inR],'10','Built In','Wardrobe','Ideas',"with real\nmeasurements",
 ['','','','Floor to ceiling','Alcove wardrobes','Long and double hang','Eaves storage','Sliding doors','Drawers and shelves'],O+'built-in-wardrobe-cozy.jpg',seed=91)
pin_cozy([cr(AL,(0,0,768,1024),'bw-al.png'),cr(P,(0,500,1024,1536),'bw-pinlow.png'),cr(SL,(400,0,1300,1024),'bw-sl.png'),inR,SL,EV,H,inL,AL],'10','Fitted','Wardrobe','Ideas',"for small\nbedrooms",
 ['','','','Drawers and shelves','Sliding doors','Eaves storage','Wall to wall','Double hanging','Alcove wardrobes'],O+'built-in-wardrobe-cozy2.jpg',seed=97)
a=Image.open(O+'built-in-wardrobe-cozy.jpg'); b=Image.open(O+'built-in-wardrobe-cozy2.jpg')
s=Image.new('RGB',(a.width*2+20,a.height),'white'); s.paste(a,(0,0)); s.paste(b,(a.width+20,0)); s.resize((s.width//2,s.height//2)).save('/tmp/claude-0/-home-claude/66ced7db-2a2d-58db-8d1b-26fd0ebe8295/scratchpad/bw-pins.jpg')
