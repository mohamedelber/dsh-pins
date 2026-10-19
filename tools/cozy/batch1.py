import sys,os; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
O='pins-N/'; T='tools/cozy/tiles/'; os.makedirs(T,exist_ok=True)
def after(src,name):
    im=Image.open(src); w,h=im.size; p=T+name; im.crop((w//2+8,0,w,h)).save(p); return p
def cr(src,box,name):
    p=T+name; Image.open(src).crop(box).save(p); return p
# --- guest bedroom (18) ---
g='gen/out/guest-bedroom/'
H=g+'01-hero.png'; L=g+'02-luggage-fixed.png'; D=g+'03-daybed-office.png'; C=g+'04-closet.png'; N=g+'05-nightstand.png'; P=g+'07-pin.png'; A=after(g+'06-before-after.png','gb-after.png')
hl=cr(H,(0,0,700,1024),'gb-hl.png'); hr=cr(H,(836,0,1536,1024),'gb-hr.png'); pt=cr(P,(0,500,1024,1536),'gb-pinlow.png')
pin_cozy([hl,P,hr,H,N,L,C,D,A],'18','Guest','Bedroom','Ideas',"to make guests\nfeel at home",
 ['','','','The right bed','Bedside basics','Luggage rack','Empty hangers','Office combo','Calm and clear'],O+'guest-bedroom-cozy.jpg',seed=11)
pin_cozy([cr(D,(0,0,768,1024),'gb-dl.png'),pt,cr(N,(200,0,1024,1024),'gb-nr.png'),A,D,H,N,C,L],'18','Small','Guest Room','Ideas',"cozy, simple\nand easy to host",
 ['','','','Clear the clutter','Daybed office','Hotel-style bed','Water and a lamp','Room to unpack','Fresh towels'],O+'guest-bedroom-cozy2.jpg',seed=23)
# --- boho bedroom (20) ---
b='gen/out/boho-bedroom/'
H=b+'01-hero-fixed.png'; M=b+'02-macrame.png'; C=b+'03-canopy.png'; X=b+'04-textiles.png'; PL=b+'05-plants-fixed.png'; P=b+'07-pin.png'; A=after(b+'06-before-after.png','bo-after.png')
pin_cozy([cr(H,(0,0,700,1024),'bo-hl.png'),P,cr(H,(836,0,1536,1024),'bo-hr.png'),H,X,C,M,PL,A],'20','Boho','Bedroom','Ideas',"warm, natural\nand easy to copy",
 ['','','','Natural base','Layered textiles','Light canopy','Macrame wall','Plant corner','Warm and calm'],O+'boho-bedroom-cozy.jpg',seed=31)
pin_cozy([cr(C,(0,0,700,1024),'bo-cl.png'),cr(P,(0,500,1024,1536),'bo-pinlow.png'),cr(PL,(300,0,940,1024),'bo-pr.png'),X,PL,A,C,M,H],'20','Cozy','Boho','Bedroom Ideas',"on a budget",
 ['','','','Rust and cream throws','Tall plant in a basket','Jute rug','Sheer canopy','Macrame hanging','Rattan wall art'],O+'boho-bedroom-cozy2.jpg',seed=47)
# --- studio apartment (20) ---
s='gen/out/studio-apartment/'
H=s+'01-hero-notv.png'; CN=s+'02-curtain-nook.png'; SO=s+'03-sofa-zone.png'; DL=s+'04-drop-leaf.png'; SB=s+'05-storage-bed.png'; P=s+'07-pin-fixed.png'; A=after(s+'06-before-after.png','st-after.png')
w,h=Image.open(H).size
pin_cozy([cr(H,(0,0,w//2,h),'st-hl.png'),P,cr(H,(w//2,0,w,h),'st-hr.png'),H,CN,SO,SB,DL,A],'20','Studio','Apartment','Ideas',"one room,\nsix smart zones",
 ['','','','Bookshelf divider','Curtain bed nook','Sofa as a wall','Storage bed','Drop-leaf table','Clear zones'],O+'studio-apartment-cozy.jpg',seed=53)
pin_cozy([cr(CN,(0,0,768,1024),'st-cl.png'),cr(P,(0,500,1024,1536),'st-pinlow.png'),cr(SO,(768,0,1536,1024),'st-sr.png'),A,SB,DL,H,SO,CN],'20','Small','Studio','Apartment Ideas',"layouts, storage\nand decor",
 ['','','','Zoned layout','Drawers under the bed','Table for two','Open shelf divider','Sofa back to the bed','Hidden bed nook'],O+'studio-apartment-cozy2.jpg',seed=61)
# --- stuffed animal storage (16) ---
f='gen/out/stuffed-animal/'
H=f+'01-hero.png'; Z=f+'02-zoo-close.png'; BB=f+'03-beanbag-fixed.png'; U=f+'04-underbed.png'; LG=f+'05-ledges.png'; P=f+'07-pin-fixed.png'; A=after(f+'06-before-after.png','sa-after.png')
pin_cozy([cr(H,(0,0,768,1024),'sa-hl.png'),P,cr(LG,(560,0,1536,700),'sa-lr.png'),H,BB,U,LG,Z,A],'16','Stuffed','Animal','Storage Ideas',"tame the plush pile",
 ['','','','Storage tower','Bean bag cover','Under-bed bin','Wall shelves','Elastic straps','Tidy corner'],O+'stuffed-animal-cozy.jpg',seed=71)
pin_cozy([cr(U,(300,200,1300,1024),'sa-ul.png'),cr(P,(0,500,1024,1536),'sa-pinlow.png'),cr(H,(768,0,1536,1024),'sa-hr.png'),A,Z,LG,BB,H,U],'16','Plush','Toy','Storage Ideas',"for kids' rooms",
 ['','','','Tidy corner','Stuffed animal zoo','Display ledges','Bean bag storage','Kid-height tower','Rotation bin'],O+'stuffed-animal-cozy2.jpg',seed=83)
