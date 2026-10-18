import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from pinh2 import pin_bold
from pinh import pin_collage,pin_checklist,pin_a
G='gen/out/wallpaper/'; O='pins-N/'
H=G+'01-hero.png'; RO=G+'02-rolls.png'; RM=G+'03-room.png'; PN=G+'04-pin.png'
pin_checklist('How Much','Wallpaper?','plain paper, standard rolls',
 [('Feature wall 3 m (10 ft)','2 rolls'),('Room 3 x 4 m, 2.4 m high','7 rolls'),('Room 12 x 12 ft, 8 ft high','10 rolls'),('Large pattern repeat','add 1 to 3 rolls')],
 'Always buy 1 spare roll, same batch',H,O+'wallpaper-checklist.jpg',photo_ay=0.5)
pin_bold(PN,'HOW MANY','ROLLS?','Free wallpaper calculator','+1\nSPARE',O+'wallpaper-bold.jpg',ay=0.7)
pin_collage(H,RO,RM,'2','Rolls for a','Feature Wall',O+'wallpaper-K.jpg',ay=(0.5,0.5,0.5))
pin_a([H,RO,RM,PN],['How Much Wallpaper','Do I Need?'],O+'wallpaper-A.jpg')
