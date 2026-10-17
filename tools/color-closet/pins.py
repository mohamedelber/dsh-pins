import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_map,pin_grid,pin_bold
from pinh import pin_collage,pin_a,pin_checklist
G='gen/out/color-closet/'; O='pins-N/'; SC='/tmp/claude-0/-home-claude/f83b8538-bfe1-526d-9871-d75f72442669/scratchpad/'
im=Image.open(G+'06-before-after.png'); w,h=im.size; im.crop((w//2+6,0,w,h)).save(SC+'cc-after.png')
pin_map(G+'07-pin-evening.png','the order that works','COLOR CODED CLOSET',
 [(90,1050,'Light neutrals first'),(240,1050,'Pinks and reds'),(450,1050,'Oranges and yellows'),(660,1050,'Greens'),(800,1050,'Blues and navy'),(950,1050,'Dark neutrals last')],
 O+'color-closet-map.jpg',sub='Hang left to right in this order',ay=1.0)
pin_grid([G+'01-hero-rail.png',G+'02-drawer-file-fold.png',G+'03-shelf-stacks.png',G+'04-walk-in.png',G+'05-neutral-capsule.png',SC+'cc-after.png'],
 '14','easy','COLOR CODED','CLOSET IDEAS',['Rainbow rail','File-fold drawer','Sweater stacks','Walk-in gradient','Light to dark','Matching hangers'],O+'color-closet-grid.jpg')
pin_bold(G+'07-pin-evening.png','COLOR CODE','YOUR CLOSET','The order that works','7 EASY\nSTEPS',O+'color-closet-bold.jpg',ay=1.0)
pin_collage(G+'01-hero-rail.png',G+'02-drawer-file-fold.png',G+'03-shelf-stacks.png','14','Color Coded','Closet Ideas',O+'color-closet-K.jpg')
pin_a([G+'04-walk-in.png',G+'05-neutral-capsule.png',G+'02-drawer-file-fold.png',G+'03-shelf-stacks.png'],['14 Color Coded Closet','Ideas and the Best','Color Order'],O+'color-closet-A.jpg')
pin_checklist('Color Coded Closet','Order Checklist','hang from left to right',
 [('Light neutrals','white, cream, beige'),('Warm colors','pink, red, orange, yellow'),('Cool colors','green, blue, navy, purple'),('Dark neutrals','grey, brown, black')],
 'Sort by category first, then by color',G+'01-hero-rail.png',O+'color-closet-checklist.jpg',photo_ay=0.45)
