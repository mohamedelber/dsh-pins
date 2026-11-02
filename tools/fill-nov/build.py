# Fill pins for empty days Nov 10-16 (3/day), user approved Nov 2. pin_cozy only, article images as tiles.
import sys,os; sys.path.insert(0,'/home/claude/dsh-pins'); os.chdir('/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
O='src/fill-nov/'; T='tools/fill-nov/tiles/'; os.makedirs(O,exist_ok=True); os.makedirs(T,exist_ok=True)
def c(folder,f,mode,key):
    p=f'src/{folder}/{f}.jpg'
    if mode=='f': return p
    im=Image.open(p).convert('RGB'); w,h=im.size
    box={'l':(0,0,w//2,h),'r':(w//2,0,w,h),'t':(0,0,w,h*2//3),'b':(0,h//3,w,h)}[mode]
    out=f'{T}{key}-{f}-{mode}.jpg'; im.crop(box).save(out); return out
def mk(key,folder,num,w,t1,t2,sub,seed,hero,mid,tiles):
    a=c(folder,hero,'l',key); b=c(folder,hero,'r',key); m=c(folder,mid[0],mid[1],key)
    ts=[c(folder,f,md,key) for f,md,_ in tiles]
    pin_cozy([a,m,b]+ts,num,w,t1,t2,sub,['','','']+[l for _,_,l in tiles],O+key+'.jpg',seed=seed); print('ok',key)
CT='christmas-table-';CM='christmas-mantel-';AC='airing-cupboard-';HS='hat-storage-';SD='under-stairs-cupboard-doors-';GB='guest-bedroom-ideas-';CS='christmas-';EL='european-laundry-ideas-';BR='box-room-bedroom-ideas-';GW='gift-wrap-storage-ideas-';BT='boot-room-';CC='color-coded-closet-';TL='christmas-tree-lights-';LS='loft-storage-ideas-';CF='coffee-table-decor-'
mk('xmas-table','christmas-table','16','Christmas','Table','Ideas','for small tables\nthat feel cozy',301,CT+'04-bistro-table-for-two',(CT+'02-low-garland-centerpiece','f'),
 [(CT+'01-small-round-table-set','f','Small round table'),(CT+'03-place-setting-rosemary','f','Rosemary place card'),(CT+'05-bud-vases-row','f','Row of bud vases'),(CT+'06-sideboard-buffet','f','Sideboard buffet'),(CT+'07-ornament-bowl-centerpiece','f','Ornament bowl'),(CT+'02-low-garland-centerpiece','f','Low garland')])
mk('airing','airing-cupboard','16','Airing','Cupboard','Ideas','storage ideas\nthat work',303,AC+'04-full-height-shelves',(AC+'02-slatted-shelves','f'),
 [(AC+'01-hero','l','Shelves above the tank'),(AC+'03-bedding-sets','f','Bedding in pillowcases'),(AC+'05-door-rack','f','Rack on the door'),(AC+'06-freestanding-unit','f','Freestanding unit'),(AC+'02-slatted-shelves','t','Slatted pine shelves'),(AC+'01-hero','r','Keep the tank clear')])
mk('hat','hat','18','Hat','Storage','Ideas','beanies, caps\nand sun hats',305,HS+'07-beanie-basket-bench',(HS+'01-entryway-peg-rail','f'),
 [(HS+'02-wall-cap-rack','f','Wall cap rack'),(HS+'03-over-door-cap-hanger','f','Over the door hanger'),(HS+'04-caps-in-drawer','f','Caps in a drawer'),(HS+'05-hat-boxes-closet-shelf','f','Hat boxes on a shelf'),(HS+'06-straw-hat-wall-display','f','Straw hat wall'),(HS+'01-entryway-peg-rail','f','Peg rail by the door')])
mk('xmas-mantel','christmas-mantel','16','Christmas','Mantel','Ideas','cozy, simple\nlooks',307,CM+'07-natural-tones',(CM+'03-mirror-wreath','f'),
 [(CM+'01-white-mantel-stockings','f','White mantel'),(CM+'02-houses-oranges','f','Houses and oranges'),(CM+'04-mini-trees','f','Mini trees'),(CM+'05-faux-mantel-shelf','f','No fireplace? Use a shelf'),(CM+'06-knit-stockings','f','Knit stockings'),(CM+'03-mirror-wreath','f','Wreath on a mirror')])
mk('stair-doors','under-stairs-doors','12','Under','Stairs Cupboard','Doors','ideas that fit\nthe slope',309,SD+'04-terracotta-door',(SD+'01-angled-shaker-doors','f'),
 [(SD+'02-hidden-flush-doors','f','Hidden flush doors'),(SD+'03-ledged-cottage-door','f','Cottage door'),(SD+'05-sliding-door','f','Sliding door'),(SD+'06-lit-cupboard-inside','f','Light inside'),(SD+'01-angled-shaker-doors','f','Angled shaker doors'),(SD+'04-terracotta-door','f','Bold colour')])
mk('guest','guest-bedroom','18','Guest','Bedroom','Ideas','ready for\nholiday guests',311,GB+'01-guest-bedroom',(GB+'05-nightstand','f'),
 [(GB+'02-luggage-rack','f','Luggage rack'),(GB+'03-daybed-office','f','Office with a daybed'),(GB+'04-guest-closet','f','Space to unpack'),(GB+'05-nightstand','f','Lamp and water'),(GB+'06-before-after','l','Before'),(GB+'06-before-after','r','After')])
mk('xmas-storage','christmas','18','Christmas','Decoration','Storage','smart ideas\nthat work',313,CS+'01-labeled-bins-shelves',(CS+'02-ornament-box-dividers','f'),
 [(CS+'03-egg-carton-cups','f','Egg cartons for baubles'),(CS+'04-string-lights-basket','f','Lights without tangles'),(CS+'05-wreath-closet','f','Wreath on a hook'),(CS+'06-tree-storage-bag','f','Tree storage bag'),(CS+'07-wrapping-paper-station','f','Wrapping station'),(CS+'02-ornament-box-dividers','f','Box with dividers')])
mk('euro-laundry','euro-laundry','16','European','Laundry','Ideas','hide a laundry\nin a cupboard',315,EL+'07-handleless-doors',(EL+'02-stacked-cupboard','f'),
 [(EL+'01-side-by-side-hallway','f','Hallway laundry'),(EL+'03-kitchen-laundry','f','In the kitchen'),(EL+'04-compact-tub','f','Compact tub'),(EL+'05-pull-out-hampers','f','Pull-out hampers'),(EL+'06-overhead-cupboards-rail','f','Hanging rail'),(EL+'08-sliding-doors','f','Sliding doors')])
mk('box-room','box-room','18','Box Room','Bedroom','Ideas','clever ways to\nuse a tiny room',317,BR+'02-high-sleeper-desk',(BR+'01-single-bed-shelves','f'),
 [(BR+'03-bulkhead-wardrobe','f','Over the stair bulkhead'),(BR+'04-office-daybed','f','Office and guest room'),(BR+'05-built-in-wardrobe','f','Built-in wardrobe'),(BR+'06-nursery','f','Small nursery'),(BR+'07-before-after','l','Before'),(BR+'07-before-after','r','After')])
mk('gift-wrap','gift-wrap','16','Gift Wrap','Storage','Ideas','paper, bags\nand ribbon',319,GW+'01-gift-wrap-station',(GW+'03-gift-bags-filed','f'),
 [(GW+'02-under-bed-box','f','Under-bed box'),(GW+'04-ribbon-drawer','f','Ribbon drawer'),(GW+'05-rolling-cart','f','Rolling cart'),(GW+'03-gift-bags-filed','f','Bags filed upright'),(GW+'06-before-after','l','Before'),(GW+'06-before-after','r','After')])
mk('boot-room','boot-room','18','Boot','Room Ideas','for Muddy Boots','benches, hooks\nand welly racks',321,BT+'07-welly-rack-slate-floor',(BT+'01-sage-bench-hero','f'),
 [(BT+'02-hallway-nook','f','Hallway nook'),(BT+'03-under-stairs','f','Under the stairs'),(BT+'04-tall-cupboard','f','Tall cupboard'),(BT+'05-porch','f','In the porch'),(BT+'08-belfast-sink','f','Sink for muddy paws'),(BT+'09-dog-station','f','Dog station')])
mk('color-closet','color-closet','14','Color','Coded Closet','Ideas','organize clothes\nby color',323,CC+'05-light-to-dark',(CC+'01-rainbow-rail','f'),
 [(CC+'02-file-fold-drawer','f','File-fold drawer'),(CC+'03-sweater-stacks','f','Sweater stacks'),(CC+'04-walk-in','f','Walk-in closet'),(CC+'01-rainbow-rail','f','Rainbow rail'),(CC+'06-before-after','l','Before'),(CC+'06-before-after','r','After')])
mk('tree-lights','xmas-lights','','Christmas','Tree Lights','Calculator','how many lights\nyour tree needs',325,TL+'01-lit-tree-living-room',(TL+'02-lights-deep-in-branches','f'),
 [(TL+'03-small-tree-basket','f','Small tree'),(TL+'02-lights-deep-in-branches','t','Weave lights deep'),(TL+'01-lit-tree-living-room','r','Lit from inside'),(TL+'01-lit-tree-living-room','f','Even glow'),(TL+'03-small-tree-basket','b','Tabletop tree'),(TL+'02-lights-deep-in-branches','b','Warm white')])
mk('loft','loft-storage','16','Loft','Storage','Ideas','store the\nChristmas boxes',327,LS+'01-boarded-loft',(LS+'03-low-shelving','f'),
 [(LS+'02-eaves-drawers','f','Eaves drawers'),(LS+'04-eaves-cupboard','f','Eaves cupboard'),(LS+'05-sloped-shelves','f','Shelves under the slope'),(LS+'03-low-shelving','f','Low shelving'),(LS+'06-before-after','l','Before'),(LS+'06-before-after','r','After')])
mk('coffee-table','coffee-table-decor','16','Coffee','Table Decor','Ideas','plus Christmas\nlooks',329,CF+'07-christmas-dough-bowl',(CF+'02-woven-tray','f'),
 [(CF+'01-round-oak','f','Round oak table'),(CF+'03-rule-of-three','f','Rule of three'),(CF+'04-small-round','f','Small round table'),(CF+'05-baskets-shelf','f','Baskets underneath'),(CF+'06-plants','f','Add a plant'),(CF+'02-woven-tray','f','Woven tray')])
