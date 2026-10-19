import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
from pinh import pin_checklist
G='gen/out/garage-man-cave/'; O='pins-N/'; T='tools/cozy/tiles/'
def cr(src,box,name):
    p=T+name; Image.open(src).crop(box).save(p); return p
H=G+'01-hero.png'; B=G+'02-bar.png'; BC=None; P3=G+'03-game.png'; S=G+'04-storage-fixed.png'; L=G+'05-lounge-fixed.png'; P=G+'07-pin.png'
BC=cr(B,(600,0,1024,1024),'mc-barcrop.png')
im=Image.open(G+'06-before-after-fixed.png'); w,h=im.size; A=T+'mc-after.png'; im.crop((764,0,w,h)).save(A)
pin_checklist('Garage Man Cave','Checklist','before you move in',
 [('Insulate','walls and the garage door'),('Power','GFCI outlets, own circuits'),('Zones','lounge, bar, games, storage'),('Safety','CO alarm, no engines inside')],
 'Check permits before converting',H,O+'garage-man-cave-checklist.jpg',photo_ay=0.5)
pin_cozy([cr(H,(0,0,700,1024),'mc-hl.png'),P,cr(H,(836,0,1536,1024),'mc-hr.png'),H,BC,P3,S,L,A],'18','Garage','Man Cave','Ideas',"lounge, bar, games\nand a tidy tool wall",
 ['','','','TV and sofa zone','Simple bar','Pool table corner','One storage wall','Warm lounge corner','Finished garage'],O+'garage-man-cave-cozy.jpg',seed=91)
pin_cozy([cr(P3,(0,0,700,1024),'mc-gl.png'),cr(P,(0,500,1024,1536),'mc-pinlow.png'),cr(B,(300,0,1024,1024),'mc-br.png'),A,L,H,BC,S,P3],'18','Man Cave','Ideas','for a Garage',"cozy, warm\nand easy to plan",
 ['','','','Clear and finished','Recliner and mini-split','Wood slat TV wall','Bar with stools','Pegboard workbench','Game night table'],O+'garage-man-cave-cozy2.jpg',seed=103)
