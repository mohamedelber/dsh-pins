import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_map,pin_grid,pin_bold
from pinh import pin_collage,pin_a,pin_checklist
G='gen/out/tupperware/'; O='pins-N/'
# after half of before/after
im=Image.open(G+'06-before-after.png'); w,h=im.size; im.crop((w//2+6,0,w,h)).save('/tmp/claude-0/-home-claude/f83b8538-bfe1-526d-9871-d75f72442669/scratchpad/tw-after.png')
AFT='/tmp/claude-0/-home-claude/f83b8538-bfe1-526d-9871-d75f72442669/scratchpad/tw-after.png'
pin_map(G+'07-pin-evening.png','no more lid hunting','HOW TO ORGANIZE TUPPERWARE',
 [(280,680,'Big boxes nested'),(530,740,'Medium sizes together'),(330,880,'Small cubes stacked'),(840,900,'Lids filed upright'),(560,1080,'Snack size up front'),(660,980,'Dividers stop sliding')],
 O+'tupperware-map.jpg',sub='One drawer, five simple zones',ay=0.76)
pin_grid([G+'01-hero-drawer.png',G+'02-cabinet-lid-rack.png',G+'05-pegboard-drawer.png',G+'04-bins-by-use.png',G+'03-matching-glass-set.png',AFT],
 '15','smart','TUPPERWARE','ORGANIZATION IDEAS',['Nest by shape','Lid rack','Pegboard drawer','Bins by use','One matching set','Lids at the back'],O+'tupperware-grid.jpg')
pin_bold(G+'05-pegboard-drawer.png','NO MORE','LID AVALANCHE','How to organize Tupperware','6 EASY\nSTEPS',O+'tupperware-bold.jpg',ay=0.6)
pin_collage(G+'01-hero-drawer.png',G+'02-cabinet-lid-rack.png',G+'04-bins-by-use.png','15','Tupperware','Organization Ideas',O+'tupperware-K.jpg')
pin_a([G+'02-cabinet-lid-rack.png',G+'05-pegboard-drawer.png',G+'04-bins-by-use.png',G+'03-matching-glass-set.png'],['15 Tupperware','Organization Ideas','for Cabinets & Drawers'],O+'tupperware-A.jpg')
pin_checklist('Tupperware','Clean-Out Checklist','do this before you buy organizers',
 [('Match every lid','no partner? it goes'),('Toss damaged ones','cracked, warped, no seal'),('Nest by shape','rectangles, squares, rounds'),('File lids upright','largest at one end')],
 'Keep only what fits in one drawer',G+'01-hero-drawer.png',O+'tupperware-checklist.jpg',photo_ay=0.5)
