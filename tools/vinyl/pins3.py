import sys,os; sys.path.insert(0,'/home/claude/dsh-pins'); os.chdir('/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
T='tools/cozy/tiles/'
SP='/tmp/claude-0/-home-claude/aa9f44c6-b1c7-520d-9978-96402d6712cc/scratchpad/'
def cr(src,box,name):
    p=T+name; im=Image.open(src).convert('RGB'); w,h=im.size
    im.crop((int(box[0]*w),int(box[1]*h),int(box[2]*w),int(box[3]*h))).save(p); return p
def sheet(a,b,n):
    a=Image.open(a).resize((500,750)); b=Image.open(b).resize((500,750))
    c=Image.new('RGB',(1010,750),'white'); c.paste(a,(0,0)); c.paste(b,(510,0)); c.save(SP+n)
# vinyl
O='src/vinyl/pins/'; os.makedirs(O,exist_ok=True); s='src/vinyl/how-to-store-vinyl-records-'
H=s+'01-cube-shelf.jpg'; D=s+'02-upright-dividers.jpg'; SL=s+'03-inner-sleeve.jpg'; C=s+'04-record-crate.jpg'
PIN=cr('gen/out/vinyl/05b-pin.png',(0,0,1,1),'vn-pin.png')
pin_cozy([cr(H,(0,0,.5,1),'vn-hl.png'),PIN,cr(H,(.5,0,1,1),'vn-hr.png'),D,SL,C,cr(H,(.15,.25,.6,.75),'vn-h2.png'),cr(SL,(.25,.1,.95,.9),'vn-s2.png'),cr(D,(.1,.1,.9,.9),'vn-d2.png')],'7','Steps','How to Store','Vinyl Records',"so they never\nwarp",
 ['','','','Upright, with dividers','New inner sleeves','A crate by the deck','Never stacked flat','Clean before storing','Same sizes together'],O+'vn-cozy.jpg',seed=551)
pin_cozy([cr(C,(0,0,.6,1),'vn-cl.png'),cr(PIN,(0,.3,1,1),'vn-pl.png'),cr(H,(.5,0,1,1),'vn-hr2.png'),H,D,SL,cr(C,(.3,.3,.9,.9),'vn-c2.png'),cr(D,(.1,.1,.9,.9),'vn-d3.png'),cr(SL,(.25,.1,.95,.9),'vn-s3.png')],'65','to 70°F','Vinyl Record','Storage Tips',"upright, cool,\ndark and dry",
 ['','','','Check the shelf load','Full-height dividers','Lose the shrink wrap','Away from the sun','Dividers 4 to 6 in apart','Poly inner sleeves'],O+'vn-cozy2.jpg',seed=557)
sheet(O+'vn-cozy.jpg',O+'vn-cozy2.jpg','vn-pins.jpg')
# alcove
O='src/alcove/pins/'; os.makedirs(O,exist_ok=True); s='src/alcove/alcove-shelving-ideas-'
H=s+'01-alcoves-both-sides.jpg'; F=s+'02-floating-oak-shelves.jpg'; C=s+'03-alcove-cupboards.jpg'; DK=s+'04-alcove-desk.jpg'; W=s+'05-alcove-wardrobe.jpg'; L=s+'06-lit-alcove-shelves.jpg'
PIN=cr('gen/out/alcove/07-pin.png',(0,0,1,1),'al-pin.png')
pin_cozy([cr(H,(0,0,.5,1),'al-hl.png'),PIN,cr(H,(.5,0,1,1),'al-hr.png'),F,C,DK,W,L,cr(H,(.62,.15,1,.95),'al-h2.png')],'10','Ideas','Alcove Shelving','Ideas',"for the space beside\nthe chimney breast",
 ['','','','Oak floating shelves','Cupboards below','An alcove desk','An alcove wardrobe','Lit display shelves','Paint it to match'],O+'al-cozy.jpg',seed=563)
pin_cozy([cr(L,(0,0,.6,1),'al-ll.png'),cr(PIN,(0,.3,1,1),'al-pl.png'),cr(F,(.3,0,1,1),'al-fr.png'),C,F,L,DK,W,cr(C,(.1,.1,.9,.9),'al-c2.png')],'30','cm Deep','Alcove Shelves','That Fit',"depths, spacing\nand UK costs",
 ['','','','Deeper shelves below','25 mm boards span more','Warm white LEDs','Desk 69 to 71 cm high','Check wardrobe depth','Shelves 20 to 30 cm apart'],O+'al-cozy2.jpg',seed=569)
sheet(O+'al-cozy.jpg',O+'al-cozy2.jpg','al-pins.jpg')
# xmas tree
O='src/xmas-tree/pins/'; os.makedirs(O,exist_ok=True); s='src/xmas-tree/how-to-store-an-artificial-christmas-tree-'
H=s+'01-tree-and-bag.jpg'; FS=s+'02-folded-sections.jpg'; BC=s+'03-bag-in-closet.jpg'; UB=s+'04-upright-bag.jpg'
PIN=cr('gen/out/xmas-tree/05-pin.png',(0,0,1,1),'xt-pin.png')
pin_cozy([cr(H,(0,0,.5,1),'xt-hl.png'),PIN,cr(H,(.5,0,1,1),'xt-hr.png'),FS,BC,UB,cr(H,(.3,.45,.9,1),'xt-h2.png'),cr(FS,(.2,.1,.8,.9),'xt-f2.png'),cr(BC,(.2,0,.8,1),'xt-b2.png')],'7','Steps','How to Store an','Artificial Tree',"so it looks full\nnext Christmas",
 ['','','','Fold and tie sections','Off the floor','Upright bag option','Bag, not the old box','Top section first','Cool, dry closet'],O+'xt-cozy.jpg',seed=571)
pin_cozy([cr(BC,(0,0,.6,1),'xt-bl.png'),cr(PIN,(0,.3,1,1),'xt-pl.png'),cr(UB,(.3,0,1,1),'xt-ur.png'),H,FS,BC,cr(FS,(.2,.1,.8,.9),'xt-f3.png'),cr(UB,(.1,.1,.9,.9),'xt-u2.png'),cr(H,(.3,.45,.9,1),'xt-h3.png')],'3','Sections','Christmas Tree','Storage Tips',"bags, closets\nand pre-lit trees",
 ['','','','Check the lights first','Ribbon, not too tight','Closet, not attic','Stand in its own bag','Measure the bag','Dust and dry it'],O+'xt-cozy2.jpg',seed=577)
sheet(O+'xt-cozy.jpg',O+'xt-cozy2.jpg','xt-pins.jpg')
