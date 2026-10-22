# CSV-48 (Oct 22): fresh cozy pins for winning topics + Christmas
import sys,os; sys.path.insert(0,'/home/claude/dsh-pins'); os.chdir('/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
O='src/cozy48/'; T='tools/cozy/tiles/'; os.makedirs(O,exist_ok=True); os.makedirs(T,exist_ok=True)
F='fetch/out/'
def cr(src,box,name):
    p=T+name; im=Image.open(src).convert('RGB'); w,h=im.size
    box=tuple(int(v*(w if i%2==0 else h)) for i,v in enumerate(box)); im.crop(box).save(p); return p
def after(src,name): return cr(src,(0.505,0,1,1),name)
L=lambda f:(0,0,0.5,1); R=(0.5,0,1,1)
J=[]
def mk(out,num,w,t1,t2,sub,hero,mid,tiles,seed):
    a=cr(hero,(0,0,0.5,1),out+'-hl.png'); b=cr(hero,(0.5,0,1,1),out+'-hr.png')
    files=[x[0] for x in tiles]; labels=[x[1] for x in tiles]
    pin_cozy([a,mid,b]+files,num,w,t1,t2,sub,['','','']+labels,O+out+'.jpg',seed=seed); J.append(out); print('ok',out)
e=F+'entryway-0'
mk('entryway-cozy48','20','Small','Entryway','Ideas',"to stop clutter\nat the door",e+'1-small-entryway.jpg',cr(e+'5-drop-zone.jpg',(0.2,0,0.8,1),'en-mid.png'),
 [(e+'3-shoe-cabinet.jpg','Slim shoe cabinet'),(e+'4-peg-rail-hooks.jpg','Peg rail hooks'),(e+'2-narrow-entryway.jpg','Narrow hallway'),(e+'6-apartment-entry.jpg','Apartment entry'),(e+'5-drop-zone.jpg','Drop zone'),(after(e+'7-before-after.jpg','en-after.png'),'Clear floor')],101)
l=F+'lego-storage-0'
mk('lego-cozy48','16','LEGO','Storage','Ideas',"no more bricks\non the floor",l+'1-kids-room.jpg',cr(l+'4-display-shelf.jpg',(0.2,0,0.8,1),'lg-mid.png'),
 [(l+'2-sorting-drawers.jpg','Sort by color'),(l+'3-play-table.jpg','Play table bins'),(l+'5-play-mat-bag.jpg','Play mat bag'),(l+'6-sets-and-manuals.jpg','Sets and manuals'),(l+'4-display-shelf.jpg','Display ledge'),(after(l+'7-before-after.jpg','lg-after.png'),'Tidy room')],103)
p=F+'pantry-shelving-0'
mk('pantry-shelving-cozy48','16','Pantry','Shelving','Ideas',"depths, spacing\nand layouts",p+'1-walk-in-u-shape.jpg',cr(p+'9-led-shelf-lights.jpg',(0.2,0,0.8,1),'ps-mid.png'),
 [(p+'2-reach-in.jpg','Reach-in pantry'),(p+'3-adjustable.jpg','Adjustable tracks'),(p+'4-shallow-shelves.jpg','Shallow shelves'),(p+'5-pull-out-drawers.jpg','Pull-out drawers'),(p+'6-corner.jpg','Corner shelves'),(p+'9-led-shelf-lights.jpg','LED shelf lights')],107)
u=F+'under-sink-0'
mk('under-sink-cozy48','15','Under','Bathroom Sink','Organization',"ideas that fit\naround the pipes",F+'open-bathroom-cabinet-under-a-sink-showing-neatl.jpg',cr(u+'5-clear-bins-turntable.jpg',(0.2,0,0.8,1),'us-mid.png'),
 [(u+'2-u-shaped-organizer.jpg','U-shaped organizer'),(u+'3-tension-rod.jpg','Tension rod'),(u+'4-door-bins.jpg','Door bins'),(u+'5-clear-bins-turntable.jpg','Clear bins'),(F+'open-bathroom-cabinet-under-a-sink-showing-neatl.jpg','Baskets by category'),(after(u+'6-before-after.jpg','us-after.png'),'Calm cabinet')],109)
k=F+'walkin-0'
mk('walk-in-cozy48','18','Small','Walk-In Closet','Ideas',"make every\ninch count",k+'1-small-walk-in-closet.jpg',cr(k+'3-double-hanging-rods.jpg',(0.2,0,0.8,1),'wk-mid.png'),
 [(k+'2-narrow-walk-in-closet.jpg','Narrow layout'),(k+'3-double-hanging-rods.jpg','Double rods'),(k+'4-corner-shelves.jpg','Corner shelves'),(k+'5-shoe-storage.jpg','Shoe shelves'),(k+'6-accessory-drawer.jpg','Accessory drawer'),(after(k+'7-before-after.jpg','wk-after.png'),'Neat and calm')],113)
t=F+'over-toilet-0'
mk('over-toilet-cozy48','18','Over the','Toilet Storage','Ideas',"for small\nbathrooms",F+'a-slim-white-over-the-toilet-storage-cabinet-wit-1.jpg',cr(t+'5-ladder-shelf.jpg',(0.2,0,0.8,1),'ot-mid.png'),
 [(t+'2-etagere.jpg','Etagere'),(t+'3-wall-cabinet.jpg','Wall cabinet'),(t+'4-floating-shelves.jpg','Floating shelves'),(t+'5-ladder-shelf.jpg','Ladder shelf'),(F+'a-slim-white-over-the-toilet-storage-cabinet-wit-1.jpg','Slim cabinet'),(after(t+'6-before-after.jpg','ot-after.png'),'Calm and tidy')],127)
s='src/purse/purse-storage-0'
mk('purse-cozy48','18','Purse','Storage','Ideas',"keep every bag\nin shape",s+'1-handbag-shelves-dividers.jpg',cr(s+'7-entryway-everyday-bag.jpg',(0.2,0,0.8,1),'pu-mid.png'),
 [(s+'6-clear-handbag-boxes.jpg','Clear boxes'),(s+'7-entryway-everyday-bag.jpg','Everyday bag hook'),(s+'2-acrylic-shelf-dividers.jpg','Acrylic dividers'),(s+'5-clutches-in-drawer.jpg','Clutch drawer'),(s+'3-hanging-purse-organizer.jpg','Hanging organizer'),(after(s+'8-before-after.jpg','pu-after.png'),'Tidy shelf')],131)
c='src/kitchen-counter-decor/kitchen-counter-decor-0'
mk('kitchen-counter-cozy48','16','Kitchen','Counter Decor','Ideas',"keep your prep\nspace clear",c+'3-coffee-corner.jpg',cr('src/kitchen-counter-decor/pin-kitchen-counter-tray-dusk.jpg',(0,0.3,1,1),'kc-mid.png'),
 [(c+'2-stove-tray.jpg','Stove tray'),(c+'7-fall-counter.jpg','Seasonal touch'),(c+'5-cookbook-herbs.jpg','Fresh herbs'),(c+'1-styled-counter.jpg','Styled corner'),(c+'4-island-fruit-bowl.jpg','Fruit bowl'),(after(c+'8-before-after.jpg','kc-after.png'),'Clear counter')],137)
x='src/christmas-table/christmas-table-0'
mk('christmas-table-cozy48','16','Christmas','Table','Decorations',"for small tables",x+'4-bistro-table-for-two.jpg',cr('src/christmas-table/pin-christmas-table-H-bright.jpg',(0,0.3,1,1),'ct-mid.png'),
 [(x+'6-sideboard-buffet.jpg','Sideboard buffet'),(x+'3-place-setting-rosemary.jpg','Rosemary napkins'),(x+'7-ornament-bowl-centerpiece.jpg','Ornament bowl'),(x+'5-bud-vases-row.jpg','Bud vases'),(x+'2-low-garland-centerpiece.jpg','Low garland'),(after(x+'8-before-after.jpg','ct-after.png'),'Ready to dine')],139)
y='src/christmas/christmas-0'
mk('christmas-storage-cozy48','18','Christmas','Decoration','Storage',"ornaments, lights\nand wreaths",y+'7-wrapping-paper-station.jpg',cr(y+'5-wreath-closet.jpg',(0.2,0,0.8,1),'cs-mid.png'),
 [(y+'5-wreath-closet.jpg','Wreath storage'),(y+'4-string-lights-basket.jpg','Tangle-free lights'),(y+'2-ornament-box-dividers.jpg','Ornament dividers'),(y+'6-tree-storage-bag.jpg','Tree bag'),(y+'1-labeled-bins-shelves.jpg','Labeled bins'),(after(y+'8-before-after.jpg','cs-after.png'),'Tidy shelf')],149)
m='src/christmas-mantel/christmas-mantel-0'
mk('christmas-mantel-cozy48','16','Christmas','Mantel','Ideas',"simple, cozy\nand natural",m+'7-natural-tones.jpg',cr('src/christmas-mantel/pin-christmas-mantel-night-glow.jpg',(0,0.3,1,1),'cm-mid.png'),
 [(cr(m+'3-mirror-wreath.jpg',(0,0,1,0.52),'cm-mw.png'),'Mirror and wreath'),(m+'6-knit-stockings.jpg','Knit stockings'),(m+'4-mini-trees.jpg','Mini trees'),(cr(m+'2-houses-oranges.jpg',(0.3,0.25,1,1),'cm-or.png'),'Dried oranges'),(m+'5-faux-mantel-shelf.jpg','No-fireplace shelf'),(after(m+'8-before-after.jpg','cm-after.png'),'Finished mantel')],151)
g='src/gift-wrap/gift-wrap-storage-ideas-0'
mk('gift-wrap-cozy48','16','Gift Wrap','Storage','Ideas',"ready for\nthe holidays",g+'1-gift-wrap-station.jpg',cr(g+'5-rolling-cart.jpg',(0.2,0,0.8,1),'gw-mid.png'),
 [(g+'2-under-bed-box.jpg','Under-bed box'),(g+'3-gift-bags-filed.jpg','Gift bags filed'),(g+'4-ribbon-drawer.jpg','Ribbon drawer'),(g+'5-rolling-cart.jpg','Rolling cart'),(g+'1-gift-wrap-station.jpg','Wrap station'),(after(g+'6-before-after.jpg','gw-after.png'),'Tidy closet')],157)
# contact sheet
ims=[Image.open(O+j+'.jpg').resize((250,375)) for j in J]
for i in range(0,len(ims),6):
    s=Image.new('RGB',(250*6+50,375),'white')
    for n,im in enumerate(ims[i:i+6]): s.paste(im,(n*260,0))
    s.save(f'/tmp/claude-0/-home-claude/66ced7db-2a2d-58db-8d1b-26fd0ebe8295/scratchpad/c48-{i//6}.jpg')
