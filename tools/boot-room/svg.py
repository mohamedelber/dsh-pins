T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';W1='#D9B48A';W2='#B98A5E';SA='#ECCDA0'
s=[];a=s.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="br-t br-d"><title id="br-t">Boot room layout guide</title><desc id="br-d">Side view of a boot room wall by the back door, split into four zones. Wipe: a doormat and a boot tray right by the door. Sit: a bench about 45 to 48 cm high and 38 to 45 cm deep, with baskets underneath. Hang: adult hooks about 165 to 175 cm from the floor and lower hooks about 100 to 120 cm for children. Store: a shelf above the hooks for hats and gloves. Leave about 90 cm of clear floor in front of the bench. A tip says to hang wet coats with space around them, keep the room ventilated and not dry clothes on radiators.</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">Boot Room Layout Guide</text>')
a(f'<text x="60" y="130" font-size="22" fill="{G}">Four zones and the heights that work</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
a(f'<rect x="60" y="160" width="640" height="540" rx="16" fill="#FBF6EF" stroke="{BR}" stroke-width="2"/>')
k=2.4; fl=660; X0=150
def Y(cm): return fl-cm*k
a(f'<line x1="80" y1="{fl}" x2="680" y2="{fl}" stroke="{T}" stroke-width="4"/>')
# door on the right
a(f'<rect x="560" y="{Y(200)}" width="110" height="{200*k}" fill="{SGL}" stroke="{SG}" stroke-width="3"/><circle cx="578" cy="{Y(100)}" r="6" fill="{G}"/><text x="615" y="{Y(185)}" font-size="14" fill="{G}" text-anchor="middle">back door</text>')
# mat + boot tray
a(f'<rect x="545" y="{fl-6}" width="125" height="6" fill="{W2}"/>')
a(f'<rect x="440" y="{fl-8}" width="95" height="8" rx="2" fill="{T}"/>')
for bx in (452,478,504):
    a(f'<path d="M{bx},{fl-8} L{bx},{fl-62} L{bx+16},{fl-62} L{bx+16},{fl-24} L{bx+24},{fl-18} L{bx+24},{fl-8} Z" fill="#4E5B47"/>')
a(f'<text x="487" y="{fl+24}" font-size="13" fill="{G}" text-anchor="middle">boot tray</text><text x="607" y="{fl+24}" font-size="13" fill="{G}" text-anchor="middle">mat</text>')
# bench 47cm
bw=270
a(f'<rect x="{X0}" y="{Y(47)}" width="{bw}" height="12" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
a(f'<rect x="{X0+6}" y="{Y(47)+12}" width="12" height="{47*k-12}" fill="{SG}"/><rect x="{X0+bw-18}" y="{Y(47)+12}" width="12" height="{47*k-12}" fill="{SG}"/>')
for i in range(3):
    bx=X0+26+i*78
    a(f'<rect x="{bx}" y="{Y(30)}" width="66" height="{30*k}" rx="5" fill="{SA}" stroke="{W2}" stroke-width="2"/>')
# hooks rail at 170 and 110
for h,lab in ((170,'adults'),(110,'children')):
    a(f'<rect x="{X0}" y="{Y(h)-6}" width="{bw}" height="10" fill="{W1}" stroke="{W2}" stroke-width="1.5"/>')
    for i in range(4):
        hx=X0+30+i*70
        a(f'<path d="M{hx},{Y(h)+4} l0,10 q0,8 8,8" stroke="{T}" stroke-width="3" fill="none"/>')
# coat on adult hook
a(f'<path d="M{X0+30},{Y(170)+14} l-22,28 l6,110 l34,0 l6,-110 Z" fill="#7A6A4F"/>')
# shelf at 190
a(f'<rect x="{X0}" y="{Y(192)}" width="{bw}" height="10" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
a(f'<rect x="{X0+20}" y="{Y(192)-34}" width="60" height="34" rx="4" fill="{SA}" stroke="{W2}" stroke-width="2"/><rect x="{X0+100}" y="{Y(192)-34}" width="60" height="34" rx="4" fill="{SA}" stroke="{W2}" stroke-width="2"/>')
# dimension lines on left
def dim(h,txt,x=110):
    a(f'<line x1="{x}" y1="{fl}" x2="{x}" y2="{Y(h)}" stroke="{A}" stroke-width="2.5"/><line x1="{x-8}" y1="{Y(h)}" x2="{x+8}" y2="{Y(h)}" stroke="{A}" stroke-width="2.5"/>')
    a(f'<text x="{x-14}" y="{Y(h)+5}" font-size="15" font-weight="700" fill="{A}" text-anchor="end">{txt}</text>')
dim(47,'45–48',125); dim(110,'100–120',125); dim(170,'165–175',125)
a(f'<text x="96" y="{fl+24}" font-size="13" fill="{G}" text-anchor="middle">cm</text>')
a(f'<text x="{X0+180}" y="{Y(192)-12}" font-size="14" fill="{G}">hats, gloves</text>')
a(f'<text x="{X0+bw/2}" y="{fl+24}" font-size="13" fill="{G}" text-anchor="middle">bench, 38–45 cm deep</text>')
# zone badges
for n,(cx,cy) in enumerate([(487,Y(40)),(X0+bw+28,Y(47)),(X0+bw+28,Y(140)),(X0+bw+28,Y(197))],1):
    a(f'<circle cx="{cx}" cy="{cy}" r="17" fill="{T}"/><text x="{cx}" y="{cy+7}" font-size="18" font-weight="700" fill="#FFFFFF" text-anchor="middle">{n}</text>')
cards=[("Wipe","Mat and boot tray right by the door."),("Sit","Bench 45–48 cm, 90 cm clear in front."),("Hang","Hooks at 165–175 cm and 100–120 cm."),("Store","Shelf above the hooks for hats, gloves.")]
for i,(t1,t2) in enumerate(cards):
    y=170+i*128
    a(f'<rect x="730" y="{y}" width="410" height="114" rx="14" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
    a(f'<circle cx="768" cy="{y+42}" r="19" fill="{T}"/><text x="768" y="{y+49}" font-size="20" font-weight="700" fill="#FFFFFF" text-anchor="middle">{i+1}</text>')
    a(f'<text x="802" y="{y+50}" font-size="22" font-weight="700" fill="{T}">{t1}</text><text x="802" y="{y+82}" font-size="16" fill="{G}">{t2}</text>')
a(f'<rect x="60" y="730" width="1080" height="100" rx="14" fill="{SGL}" stroke="{SG}" stroke-width="2"/><rect x="60" y="730" width="10" height="100" rx="5" fill="{SG}"/>')
a(f'<text x="96" y="771" font-size="20" fill="{T}"><tspan font-weight="700">Wet coats:</tspan> hang them with space around them, keep the room</text>')
a(f'<text x="96" y="805" font-size="20" fill="{T}">ventilated and do not dry clothes on radiators.</text>')
a(f'<text x="60" y="872" font-size="14" fill="{G}">Bench sizes adapted from UK public seating guidance (via Wheels for Wellbeing). Damp advice: South Kesteven DC. Hooks and 90 cm floor: our rule of thumb.</text>')
a('</svg>')
import re
svg=re.sub(r'(\d+\.\d{2,})',lambda m:str(round(float(m.group(1)),1)),''.join(s))
open('z.svg','w').write(svg)
