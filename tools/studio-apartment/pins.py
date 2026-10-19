import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_grid,pin_bold
from pinh import pin_collage,pin_a,pin_checklist
G='gen/out/studio-apartment/'; O='pins-N/'; S='/tmp/claude-0/-home-claude/66ced7db-2a2d-58db-8d1b-26fd0ebe8295/scratchpad/'
H=S+'st-hero.png'; C=G+'02-curtain-nook.png'; SO=G+'03-sofa-zone.png'; T=G+'04-drop-leaf.png'; B=G+'05-storage-bed.png'; P=G+'07-pin-fixed.png'
im=Image.open(G+'06-before-after.png'); w,h=im.size; im.crop((w//2+6,0,w,h)).save(S+'st-after.png'); AFT=S+'st-after.png'
pin_checklist('Studio Apartment','Layout Cheat Sheet','one room, six zones',
 [('Bed','far corner, away from the door'),('Divider','open bookshelf or curtain'),('Living','sofa on its own rug'),('Walkway','keep 36 in clear')],
 'Store under the bed and up the walls',H,O+'studio-apartment-checklist.jpg',photo_ay=0.5)
pin_bold(P,'MAKE ONE ROOM','FEEL LIKE THREE','20 studio apartment ideas','ZONE\nPLAN',O+'studio-apartment-bold.jpg',ay=0.8)
pin_collage(H,C,SO,'20','Studio Apartment','Ideas',O+'studio-apartment-K.jpg',ay=(0.5,0.5,0.5))
pin_a([C,SO,B,T],['20 Studio Apartment','Ideas for Small','Spaces'],O+'studio-apartment-A.jpg')
pin_grid([H,C,SO,B,T,AFT],'20','smart','STUDIO APARTMENT','IDEAS',['Bookshelf divider','Curtain bed nook','Sofa as a wall','Storage bed','Drop-leaf table','Clear zones'],O+'studio-apartment-grid.jpg')
