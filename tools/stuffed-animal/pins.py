import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_grid,pin_bold,pin_cozy
from pinh import pin_collage,pin_a,pin_checklist
G='gen/out/stuffed-animal/'; O='pins-N/'; S='/tmp/claude-0/-home-claude/66ced7db-2a2d-58db-8d1b-26fd0ebe8295/scratchpad/'
H=G+'01-hero.png'; Z=G+'02-zoo-close.png'; B=S+'03fix.png'; U=G+'04-underbed.png'; L=G+'05-ledges.png'; P=G+'07-pin-fixed.png'
im=Image.open(G+'06-before-after.png'); w,h=im.size; im.crop((w//2+6,0,w,h)).save(S+'sa-after.png'); AFT=S+'sa-after.png'
def crop(src,box,name):
    Image.open(src).crop(box).save(S+name); return S+name
c1=crop(H,(0,0,768,1024),'sa-c1.png'); c2=crop(L,(560,0,1536,700),'sa-c2.png'); c3=crop(U,(300,200,1300,1024),'sa-c3.png')
pin_checklist('Stuffed Animal','Storage Cheat Sheet','the 4-zone plush system',
 [('Bed buddies','1 to 3 favorites, never in a crib'),('Play zone','one basket or tower at kid height'),('Rotation bin','lidded, under the bed'),('Keepsake box','clean, dry, labeled, indoors')],
 'No zone left? Donate it',H,O+'stuffed-animal-checklist.jpg',photo_ay=0.5)
pin_bold(P,'TAME THE','PLUSH PILE','16 stuffed animal storage ideas','4 ZONE\nSYSTEM',O+'stuffed-animal-bold.jpg',ay=0.8)
pin_collage(H,B,U,'16','Stuffed Animal','Storage Ideas',O+'stuffed-animal-K.jpg',ay=(0.5,0.5,0.5))
pin_a([Z,B,U,L],['16 Stuffed Animal','Storage Ideas','for Kids’ Rooms'],O+'stuffed-animal-A.jpg')
pin_grid([H,B,U,L,Z,AFT],'16','clever','STUFFED ANIMAL','STORAGE IDEAS',['Storage tower','Bean bag cover','Under-bed bin','Wall shelves','Elastic straps','Tidy corner'],O+'stuffed-animal-grid.jpg')
