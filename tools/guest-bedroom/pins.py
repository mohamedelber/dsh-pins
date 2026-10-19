import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_grid,pin_bold
from pinh import pin_collage,pin_a,pin_checklist
G='gen/out/guest-bedroom/'; O='pins-N/'; S='/tmp/claude-0/-home-claude/66ced7db-2a2d-58db-8d1b-26fd0ebe8295/scratchpad/'
H=G+'01-hero.png'; L=G+'02-luggage-fixed.png'; D=G+'03-daybed-office.png'; C=G+'04-closet.png'; N=G+'05-nightstand.png'; P=G+'07-pin.png'
im=Image.open(G+'06-before-after.png'); w,h=im.size; im.crop((w//2+6,0,w,h)).save(S+'gb-after.png'); AFT=S+'gb-after.png'
pin_checklist('Guest Bedroom','Checklist','what guests really need',
 [('Bed','best size the room fits'),('Nightstand','lamp, water, charger'),('Unpack','luggage rack + empty hangers'),('Sleep','blackout curtains, extra blanket')],
 'Fit a smoke alarm in the room',H,O+'guest-bedroom-checklist.jpg',photo_ay=0.5)
pin_bold(P,'MAKE GUESTS','FEEL AT HOME','18 guest bedroom ideas','EASY\nSETUP',O+'guest-bedroom-bold.jpg',ay=0.8)
pin_collage(H,N,L,'18','Guest Bedroom','Ideas',O+'guest-bedroom-K.jpg',ay=(0.5,0.5,0.5))
pin_a([N,L,D,C],['18 Guest Bedroom','Ideas for Small','Spaces'],O+'guest-bedroom-A.jpg')
pin_grid([H,N,L,C,D,AFT],'18','cozy','GUEST BEDROOM','IDEAS',['The right bed','Bedside basics','Luggage rack','Empty hangers','Office combo','Calm and clear'],O+'guest-bedroom-grid.jpg')
