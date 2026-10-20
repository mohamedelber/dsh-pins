import sys; sys.path.insert(0,'/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
from pinh import pin_checklist
S='src/desk-height/desk-height-calculator-'; O='pins-N/'; T='tools/cozy/tiles/'
def cr(src,box,name):
    p=T+name; Image.open(src).crop(box).save(p); return p
H=S+'01-home-office-desk.jpg'; ST=S+'02-standing-desk.jpg'; SV=S+'03-desk-chair-monitor-heights.jpg'; SM=S+'04-small-desk-nook.jpg'; K=S+'05-kids-desk.jpg'; M=S+'06-monitor-height.jpg'; P=T+'desk-pin-fixed.jpg'
pin_checklist('Desk Height','Cheat Sheet','set up your desk right',
 [('Desk','at elbow height, elbows at 90°'),('Chair','feet flat, thighs level'),('Screen','top at eye level, arm’s length away'),('Standing','about 38 to 47 in for most adults')],
 'A standard desk is 28 to 30 in tall',H,O+'desk-height-checklist.jpg',photo_ay=0.5)
pin_cozy([cr(H,(0,0,700,1024),'dh-hl.png'),P,cr(H,(836,0,1536,1024),'dh-hr.png'),ST,SV,M,SM,K,H],'Free','Tool','Desk Height','Calculator',"sitting and\nstanding desks",
 ['','','','Standing desk','Chair and desk','Screen height','Small desk nook','Kids desk','Home office'],O+'desk-height-cozy.jpg',seed=171)
pin_cozy([cr(SV,(0,0,760,1024),'dh-sl.png'),cr(P,(0,500,1024,1536),'dh-plow.png'),cr(ST,(0,0,1024,1024),'dh-st.png'),H,M,ST,SV,SM,K],'How','High','Should My Desk','Be?',"free desk height calculator",
 ['','','','Elbow height','Eye level screen','Sit-stand desk','Feet flat','Wall desk','Kids setup'],O+'desk-height-cozy2.jpg',seed=177)
