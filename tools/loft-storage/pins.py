import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_map,pin_grid,pin_bold,pin_cozy
from pinh import pin_collage,pin_a,pin_checklist
G='gen/out/loft-storage/'; O='pins-N/'; SC='/tmp/claude-0/-home-claude/66ced7db-2a2d-58db-8d1b-26fd0ebe8295/scratchpad/'
im=Image.open(G+'06-before-after.png'); w,h=im.size; im.crop((w//2+6,0,w,h)).save(SC+'lf-after.png')
hero=Image.open(G+'01-hero-boarded-loft.png')
hero.crop((0,300,620,1024)).save(SC+'lf-boxes-left.png')
hero.crop((900,300,1536,1024)).save(SC+'lf-boxes-right.png')
hero.crop((380,500,1150,1024)).save(SC+'lf-walkway.png')
pinp=Image.open(G+'07-pin-evening.png')
pinp.crop((440,640,1024,960)).save(SC+'lf-drawers.png')
pin_checklist('Loft Storage','Checklist','before you put anything up there',
 [('Raise the boards','loft legs over full insulation'),('Clear lidded boxes','one category per box'),('Zone by use','yearly items by the hatch'),('Keep eaves clear','air flow stops condensation')],
 'Light storage only: joists are not a floor',G+'01-hero-boarded-loft.png',O+'loft-storage-checklist.jpg',photo_ay=0.6)
pin_map(G+'07-pin-evening.png','loft bedroom','EAVES STORAGE',
 [(560,740,'Eaves drawers'),(760,870,'Deep drawers for bedding'),(970,960,'Basket for throws'),(300,1000,'Bench for blankets'),(713,1360,'Wool rug for warmth'),(320,700,'Soft lamp light')],
 O+'loft-storage-map.jpg',sub='Use the space under the slope',ay=1.0)
pin_grid([G+'01-hero-boarded-loft.png',G+'02-eaves-drawers.png',G+'03-low-shelving.png',G+'04-eaves-cupboard-inside.png',G+'05-built-in-shelves.png',SC+'lf-after.png'],
 '16','smart','LOFT STORAGE','IDEAS',['Boarded walkway','Eaves drawers','Low shelving','Eaves cupboard','Sloped shelves','Clear boxes'],O+'loft-storage-grid.jpg')
pin_bold(G+'01-hero-boarded-loft.png','LOFT','STORAGE','Board it the right way','16\nIDEAS',O+'loft-storage-bold.jpg',ay=0.7)
pin_collage(G+'01-hero-boarded-loft.png',G+'02-eaves-drawers.png',G+'03-low-shelving.png','16','Loft Storage','Ideas',O+'loft-storage-K.jpg',ay=(0.6,0.5,0.5))
pin_a([G+'02-eaves-drawers.png',G+'04-eaves-cupboard-inside.png',G+'03-low-shelving.png',G+'05-built-in-shelves.png'],['16 Loft Storage Ideas','for Eaves, Attics and','Loft Conversions'],O+'loft-storage-A.jpg')
pin_cozy([SC+'lf-boxes-left.png',G+'07-pin-evening.png',SC+'lf-boxes-right.png',SC+'lf-walkway.png',G+'02-eaves-drawers.png',G+'03-low-shelving.png',G+'04-eaves-cupboard-inside.png',G+'05-built-in-shelves.png',SC+'lf-after.png'],
 '16','Loft','Storage','Ideas',"boarded lofts, eaves\nand conversions",
 ['','','','Raised walkway','Eaves drawers','Low shelving','Eaves cupboard','Sloped shelves','Clear boxes'],O+'loft-storage-cozy.jpg',ays=[0.5,0.6,0.5,0.5,0.5,0.5,0.5,0.5,0.5])
