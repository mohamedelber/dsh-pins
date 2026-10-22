# Real-photo test pins (free Unsplash photos uploaded Nov 2025 or later), Oct 22
import sys,os,re; sys.path.insert(0,'/home/claude/dsh-pins'); os.chdir('/home/claude/dsh-pins')
from PIL import Image
from pinh2 import pin_cozy
O='src/real-test/'; T='tools/cozy/tiles/'; os.makedirs(O,exist_ok=True)
ids={}; topic=None
for l in open('scout/unsplash-recent.md'):
    if l.startswith('## '): topic=l[3:5].strip('. '); ids[topic]=[]; continue
    m=re.search(r'(photo-\d{13}-[0-9a-f]+)',l)
    if m and topic and '|' in l: ids[topic].append('scout/real/'+m.group(1)+'.jpg')
def P(t,i): return ids[t][i]
def cr(src,box,name):
    p=T+name; im=Image.open(src).convert('RGB'); w,h=im.size
    im.crop((int(box[0]*w),int(box[1]*h),int(box[2]*w),int(box[3]*h))).save(p); return p
J=[]
def mk(out,num,w,t1,t2,sub,hero,mid,tiles,seed):
    a=cr(hero,(0,0,0.5,1),out+'-hl.png'); b=cr(hero,(0.5,0,1,1),out+'-hr.png')
    pin_cozy([a,mid,b]+[x for x,_ in tiles],num,w,t1,t2,sub,['','','']+[y for _,y in tiles],O+out+'.jpg',seed=seed); J.append(out); print('ok',out)
mk('real-christmas-mantel','16','Christmas','Mantel','Ideas',"cozy, simple\nand natural",P('1',0),P('3',9),
 [(P('1',1),'Flocked mini trees'),(P('1',5),'Garland in a mirror'),(P('3',4),'Pinecones and ribbon'),(P('3',5),'Dried oranges'),(P('1',6),'Festive shelf'),(P('3',13),'Simple wreath')],201)
mk('real-christmas-table','16','Christmas','Table','Decorations',"for small tables",P('2',7),P('2',1),
 [(P('2',4),'Pine centerpiece'),(P('2',1),'Ribbon napkin'),(P('2',2),'Candles and greenery'),(P('2',5),'Velvet bow'),(P('2',3),'Mini tree accent'),(P('2',0),'Fairy lights')],203)
mk('real-pantry','22','Pantry','Organization','Ideas',"baskets, jars\nand labels",P('4',0),P('4',2),
 [(P('4',1),'Wire baskets'),(P('4',2),'Glass jars'),(P('4',3),'Pantry cabinets'),(P('4',7),'Sort by meal'),(P('4',9),'Clear bins'),(P('4',4),'Open shelving')],207)
mk('real-entryway','20','Small','Entryway','Ideas',"to stop clutter\nat the door",P('5',7),P('5',0),
 [(P('5',6),'Bench by the door'),(P('5',10),'Shoe cabinet'),(P('5',2),'Coat stand'),(P('5',8),'Statement mirror'),(P('5',4),'Narrow hallway'),(P('5',5),'Mirror and shelf')],211)
mk('real-kitchen-counter','16','Kitchen','Counter Decor','Ideas',"keep your prep\nspace clear",P('8',1),P('8',0),
 [(P('8',7),'Wood countertops'),(P('8',10),'Sage cabinets'),(P('8',9),'Marble backsplash'),(P('8',11),'Clear island'),(P('8',3),'Flowers and books'),(P('8',5),'Fruit bowl')],213)
mk('real-bathroom-counter','14','Bathroom','Counter','Decor Ideas',"for a calm vanity",P('7',3),P('7',2),
 [(P('7',0),'Rolled towels'),(P('7',4),'Warm wood vanity'),(P('7',6),'Stone countertop'),(P('7',2),'Brass tap'),(P('7',7),'Green marble'),(P('7',1),'Bold wall colour')],217)
ims=[Image.open(O+j+'.jpg').resize((330,495)) for j in J]
s=Image.new('RGB',(340*len(ims),495),'white')
for n,im in enumerate(ims): s.paste(im,(n*340,0))
s.save('/tmp/claude-0/-home-claude/66ced7db-2a2d-58db-8d1b-26fd0ebe8295/scratchpad/real-pins.jpg')
