import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_map,pin_grid,pin_bold,pin_cozy
from pinh import pin_collage,pin_a,pin_checklist
G='gen/out/gift-wrap/'; O='pins-N/'; SC='/tmp/claude-0/-home-claude/66ced7db-2a2d-58db-8d1b-26fd0ebe8295/scratchpad/'
im=Image.open(G+'06-before-after.png'); w,h=im.size; im.crop((w//2+6,0,w,h)).save(SC+'gw-after.png')
hero=Image.open(G+'01-hero-station.png')
hero.crop((300,420,720,1024)).save(SC+'gw-basket.png')
hero.crop((330,110,1100,420)).save(SC+'gw-ribbon.png')
hero.crop((680,420,1100,1024)).save(SC+'gw-bags.png')
pinp=Image.open(G+'07-pin-evening.png')
pinp.crop((500,620,1024,1000)).save(SC+'gw-gifts.png')
pin_checklist('Gift Wrap Storage','Checklist','one zone for everything',
 [('Rolls','upright bin or under-bed box'),('Gift bags','filed upright by size'),('Tissue paper','flat in a shallow box'),('Ribbon and tape','divided drawer or caddy')],
 'Measure your longest roll first',G+'01-hero-station.png',O+'gift-wrap-checklist.jpg',photo_ay=0.6)
pin_map(G+'07-pin-evening.png','set up a','GIFT WRAP STATION',
 [(130,980,'Rolls upright in a basket'),(820,575,'Ribbon on a dowel'),(740,760,'Wrap at the counter'),(930,1050,'Scissors and tape kit'),(720,1260,'Drawers for tags'),(415,800,'Jar for small bits')],
 O+'gift-wrap-map.jpg',sub='Gift wrap storage in one corner',ay=1.0)
pin_grid([G+'01-hero-station.png',G+'02-under-bed-box.png',G+'03-bags-filed.png',G+'04-ribbon-drawer.png',G+'05-door-back-closet.png',SC+'gw-after.png'],
 '16','clever','GIFT WRAP','STORAGE IDEAS',['Wrap station','Under-bed box','Bags by size','Ribbon drawer','Rolling cart','Tidy corner'],O+'gift-wrap-grid.jpg')
pin_bold(G+'07-pin-evening.png','GIFT WRAP','STORAGE','That actually works','16\nIDEAS',O+'gift-wrap-bold.jpg',ay=1.0)
pin_collage(G+'01-hero-station.png',G+'02-under-bed-box.png',G+'03-bags-filed.png','16','Gift Wrap','Storage Ideas',O+'gift-wrap-K.jpg',ay=(0.6,0.5,0.5))
pin_a([G+'03-bags-filed.png',G+'04-ribbon-drawer.png',G+'02-under-bed-box.png',G+'05-door-back-closet.png'],['16 Gift Wrap Storage','Ideas for Paper,','Bags and Ribbon'],O+'gift-wrap-A.jpg',ays=(0.5,0.5,0.5,0.6))
pin_cozy([SC+'gw-ribbon.png',G+'07-pin-evening.png',SC+'gw-bags.png',SC+'gw-basket.png',G+'02-under-bed-box.png',G+'03-bags-filed.png',G+'04-ribbon-drawer.png',G+'05-door-back-closet.png',SC+'gw-after.png'],
 '16','Gift','Wrap Storage','Ideas',"paper, bags and ribbon\nsorted in one place",
 ['','','','Rolls in a basket','Under-bed box','Bags by size','Ribbon drawer','Rolling cart','Tidy corner'],O+'gift-wrap-cozy.jpg',ays=[0.5,0.55,0.5,0.6,0.5,0.5,0.5,0.6,0.5])
