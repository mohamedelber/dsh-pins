BG='#F7F1E9';T='#342E2A';A='#C85A32';SAND='#ECCDA0';SG='#8FA689';SGL='#DCE5D6';G='#6E645C';W1='#D9B48A';W2='#B98A5E';BD='#D8CBBB'
o=[]
def t(x,y,s,sz=20,c=T,w='normal',anc='start'):o.append(f'<text x="{x}" y="{y}" font-size="{sz}" fill="{c}" font-weight="{w}" text-anchor="{anc}">{s}</text>')
def r(x,y,w,h,f,s='none',sw=0,rx=0):o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{f}" stroke="{s}" stroke-width="{sw}" rx="{rx}"/>')
def l(x1,y1,x2,y2,c=A,sw=3,d=''):o.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{sw}" {d}/>')
def dryer(x,y,w=120,h=150,lab='DRYER'):
    r(x,y,w,h,'#FFFFFF',G,2,6); r(x,y,w,24,'#F2EDE6',G,1,6)
    o.append(f'<circle cx="{x+w/2}" cy="{y+24+(h-44)/2}" r="{min(w,h-44)*0.4}" fill="#FFFFFF" stroke="{G}" stroke-width="2"/>')
    t(x+w/2,y+h-8,lab,13,G,'bold','middle')
def washer(x,y,w=120,h=150):
    r(x,y,w,h,'#FFFFFF',G,2,6); r(x,y,w,24,'#F2EDE6',G,1,6)
    o.append(f'<circle cx="{x+w/2}" cy="{y+24+(h-44)/2}" r="{min(w,h-44)*0.4}" fill="#CFE3EA" stroke="{G}" stroke-width="2"/>')
    t(x+w/2,y+h-8,'WASHER',13,G,'bold','middle')
def panel(x,y,title,sub):
    r(x,y,560,350,'#FFFFFF',BD,2,14); t(x+20,y+38,title,24,T,'bold'); t(x+20,y+64,sub,16,G)
# header
t(40,62,'Where Each Tumble Dryer Can Go',40,T,'bold'); t(40,96,'Four common small-space setups, checked against UK manufacturer manuals',19,G)
t(1160,62,'dailyspacehacks.com',18,G,'normal','end')
# A under worktop
X,Y=40,120; panel(X,Y,'A. Under a worktop','Heat pump or condenser')
r(X+60,Y+110,440,22,W1,W2,2); l(X+60,Y+300,X+500,Y+300,G,3)
washer(X+90,Y+140); dryer(X+300,Y+140)
l(X+300,Y+136,X+420,Y+136,A,2); t(X+432,Y+170,'gap above',15,A,'bold'); t(X+432,Y+190,'and at sides:',15,A,'bold'); t(X+432,Y+210,'see manual',13,G)
l(X+294,Y+150,X+294,Y+285,A,2,'stroke-dasharray="5 4"'); l(X+426,Y+150,X+426,Y+285,A,2,'stroke-dasharray="5 4"')
t(X+60,Y+330,'Keep the front air intake and plinth clear',15,T,'bold')
# B stacked
X,Y=620,120; panel(X,Y,'B. Stacked on a washer','Dryer always on top')
l(X+60,Y+330,X+300,Y+330,G,3); washer(X+110,Y+198,130,130); r(X+104,Y+184,142,14,SAND,W2,2); dryer(X+110,Y+84,130,100)
t(X+258,Y+196,'stacking kit',15,A,'bold')
t(X+290,Y+238,'Use the kit made',15,T); t(X+290,Y+258,'for your two models',15,T)
t(X+290,Y+105,'Check the washer is',15,T); t(X+290,Y+125,'deep enough for',15,T); t(X+290,Y+145,'the dryer above',15,T)
t(X+290,Y+296,'Never put the washer',15,A,'bold'); t(X+290,Y+316,'on top of the dryer',15,A,'bold')
# C cupboard
X,Y=40,490; panel(X,Y,'C. In a cupboard or alcove','Heat pump or condenser')
r(X+70,Y+90,220,230,SGL,SG,3); dryer(X+120,Y+150,120,150)
for i in range(6): l(X+300,Y+110+i*14,X+330,Y+110+i*14,SG,3)
t(X+300,Y+100,'vents',14,SG,'bold')
o.append(f'<path d="M{X+240} {Y+290} C{X+300} {Y+300},{X+300} {Y+250},{X+330} {Y+250}" fill="none" stroke="{A}" stroke-width="3"/>')
t(X+340,Y+246,'drain hose to waste',15,A,'bold'); t(X+340,Y+266,'(no tank to empty)',13,G)
t(X+350,Y+150,'Airflow in and out',15,T); t(X+350,Y+170,'Room temp: see manual',15,T); t(X+350,Y+190,'Not behind a',15,T); t(X+350,Y+210,'lockable door',15,T)
# D vented
X,Y=620,490; panel(X,Y,'D. Vented dryer','Needs an outside wall or window')
r(X+440,Y+80,40,250,'#E9DFD3',G,2); t(X+460,Y+76,'OUTSIDE',13,G,'bold','middle'); t(X+460,Y+92,'WALL',13,G,'bold','middle')
dryer(X+120,Y+170,120,150,'VENTED')
o.append(f'<path d="M{X+240} {Y+210} C{X+320} {Y+210},{X+360} {Y+150},{X+440} {Y+150}" fill="none" stroke="{SAND}" stroke-width="16" stroke-linecap="round"/>')
o.append(f'<path d="M{X+240} {Y+210} C{X+320} {Y+210},{X+360} {Y+150},{X+440} {Y+150}" fill="none" stroke="{W2}" stroke-width="2" stroke-dasharray="4 5"/>')
t(X+300,Y+128,'hose max 2.4 m',15,A,'bold'); t(X+300,Y+148,'(Hotpoint manual)',13,G)
t(X+40,Y+120,'Hot damp air',15,T); t(X+40,Y+140,'goes outside',15,T)
t(40,880,'Gaps, temperatures and hose lengths vary by model: always follow the installation guide for your dryer.',16,G)
svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, Arial, sans-serif" role="img" aria-labelledby="dt dd"><title id="dt">Where each tumble dryer can go</title><desc id="dd">Four setups: under a worktop, stacked on a washer with a stacking kit, in a ventilated cupboard with a drain hose, and a vented dryer with a hose to an outside wall.</desc><rect width="1200" height="900" fill="{BG}"/>'+''.join(o)+'</svg>'
import re; svg=re.sub(r'(\d+\.\d{2})\d+',r'\1',svg)
open('z.svg','w').write(svg)
