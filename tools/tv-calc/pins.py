import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from pinh2 import pin_map,pin_bold
from pinh import pin_collage
G='gen/out/tv-calc/'; O='pins-N/'
pin_map(G+'04-pin-evening.png','how high to','MOUNT A TV',
 [(510,575,'Centre at eye level'),(510,735,'Bottom edge above decor'),(600,920,'Low media console'),(200,1150,'Measure eye height here'),(980,700,'Lamp beside, not behind'),(860,1150,'Note your distance')],
 O+'tv-height-map.jpg',sub='Free TV mounting height calculator',ay=0.5)
pin_bold(G+'04-pin-evening.png','TV HEIGHT','CALCULATOR','Get it right first time','2 TAPS\nFREE',O+'tv-height-bold.jpg',ay=0.6)
pin_collage(G+'01-hero-living.png',G+'02-bedroom.png',G+'03-fireplace.png','42"','How High to','Mount a TV',O+'tv-height-K.jpg',ay=(0.4,0.4,0.4))
