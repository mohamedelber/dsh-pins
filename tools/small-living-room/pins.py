import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
from pinh import pin_checklist
G='gen/out/small-apartment-living-room/'; O='pins-N/'; T='tools/cozy/tiles/'
def cr(src,box,name):
    p=T+name; Image.open(src).crop(box).save(p); return p
H=G+'01-hero.png'; W=G+'02-wall-storage.png'; N=G+'03-nesting-tables.png'; M=G+'04-mirror-light.png'; D=G+'05-dining-nook.png'; P=G+'07-pin.png'
im=Image.open(G+'06-before-after-fixed.png'); w,h=im.size; A=T+'lr-after.png'; im.crop((772,0,w,h)).save(A)
MC=T+'lr-mirror.png'; Image.open(M).crop((0,0,820,1024)).save(MC)
pin_checklist('Small Living Room','Spacing Guide','the numbers that matter',
 [('Coffee table','16-18 in from the sofa'),('Walkway','30-36 in wide'),('Rug','front legs of every seat on it'),('TV','about 52 in at 7 ft away')],
 'Anchor the TV and tall shelves',H,O+'small-living-room-checklist.jpg',photo_ay=0.5)
pin_cozy([cr(H,(0,0,768,1024),'lr-hl.png'),P,cr(H,(768,0,1536,1024),'lr-hr.png'),H,N,W,MC,D,A],'20','Small','Apartment','Living Room Ideas',"smart, cozy\nand renter-friendly",
 ['','','','Round coffee table','Nesting tables','Shelves around the TV','Big mirror','Dining nook','Calm and open'],O+'small-living-room-cozy.jpg',seed=113)
pin_cozy([cr(D,(0,0,700,1024),'lr-dl.png'),cr(P,(0,500,1024,1536),'lr-pinlow.png'),cr(N,(300,0,1024,1024),'lr-nr.png'),A,W,N,H,MC,D],'20','Cozy','Small Living','Room Ideas',"for apartments",
 ['','','','Clear the floor','Wall storage','Round tables','Rug under every seat','Mirror and sconce','Table for two'],O+'small-living-room-cozy2.jpg',seed=127)
