import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
from pinh import pin_checklist
G='gen/out/chandelier-calc/'; O='pins-N/'; T='tools/cozy/tiles/'
def cr(src,box,name):
    p=T+name; Image.open(src).crop(box).save(p); return p
H=G+'01-hero.png'; F=G+'02b-foyer.png'; L=G+'03-living-fixed.png'; I=G+'04-island.png'; B=G+'05-bedroom.png'; P=G+'07-pin.png'
im=Image.open(G+'06b-too-small-right.png'); w,h=im.size; A=T+'ch-after.png'; im.crop((772,0,w,h)).save(A); S=T+'ch-small.png'; im.crop((0,0,764,h)).save(S)
pin_checklist('Chandelier Size','Cheat Sheet','the 3 numbers you need',
 [('Room','length + width (ft) = width (in)'),('Over a table','1/2 to 2/3 of the table width'),('Hang it','30-36 in above the table'),('Walkways','bottom at least 7 ft up')],
 'Check the ceiling box weight rating',H,O+'chandelier-size-checklist.jpg',photo_ay=0.12)
pin_cozy([cr(H,(0,0,700,1024),'ch-hl.png'),P,cr(H,(836,0,1536,1024),'ch-hr.png'),H,F,I,L,B,A],'Free','Size','Chandelier','Calculator',"for every room\nin your home",
 ['','','','Dining table','Two-story foyer','Island pendants','Living room','Bedroom','Long table'],O+'chandelier-size-cozy.jpg',seed=131)
pin_cozy([cr(F,(0,0,620,1024),'ch-fl.png'),cr(P,(0,500,1024,1536),'ch-pinlow.png'),cr(I,(768,0,1536,1024),'ch-ir.png'),S,A,H,I,F,L],'What','Size','Chandelier','Do I Need?',"free size calculator",
 ['','','','Too small','Just right','Half the table width','30-36 in apart','7 ft clearance','Room rule'],O+'chandelier-size-cozy2.jpg',seed=137)
