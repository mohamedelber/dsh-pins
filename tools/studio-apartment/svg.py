T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';W1='#D9B48A';W2='#B98A5E'
s=[];a=s.append
desc=("Top-down floor plan of an example 20 by 22 foot studio apartment, about 440 square feet, divided into six zones. "
"A, entry drop zone by the door. B, kitchen along the bottom wall. C, a small round dining table for two near the kitchen. "
"D, living zone with a sofa on a rug facing a TV console on the right wall. E, sleep zone with a queen bed in the top left corner, "
"screened from the living zone by an open bookshelf divider. F, a small work desk on the left wall. A 36 inch walkway runs from the door into the middle of the room.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="st-t st-d"><title id="st-t">Studio apartment zone plan</title><desc id="st-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">The Studio Apartment Zone Plan</text>')
a(f'<text x="60" y="128" font-size="22" fill="{G}">One room, six zones: give every activity its own spot</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
F=28; X0=80; Y0=176; W=20*F; H=22*F
# room
a(f'<rect x="{X0-10}" y="{Y0-10}" width="{W+20}" height="{H+20}" fill="{W2}"/>')
a(f'<rect x="{X0}" y="{Y0}" width="{W}" height="{H}" fill="#FBF8F3"/>')
# windows top
for wx in (X0+60,X0+330):
    a(f'<rect x="{wx}" y="{Y0-10}" width="150" height="10" fill="#CFE0E8"/><line x1="{wx}" y1="{Y0-5}" x2="{wx+150}" y2="{Y0-5}" stroke="#9FB3BF" stroke-width="2"/>')
# door bottom right
dx=X0+430
a(f'<rect x="{dx}" y="{Y0+H}" width="84" height="10" fill="#FBF8F3"/><path d="M{dx} {Y0+H} A84 84 0 0 1 {dx+84} {Y0+H-84}" fill="none" stroke="{G}" stroke-width="2" stroke-dasharray="5 5"/><line x1="{dx+84}" y1="{Y0+H}" x2="{dx+84}" y2="{Y0+H-84}" stroke="{G}" stroke-width="3"/>')
# zone tints
def zone(x,y,w,h,col,op=0.35): a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{col}" fill-opacity="{op}"/>')
zone(X0+8,Y0+8,232,250,SGL,0.8)          # sleep
zone(X0+272,Y0+8,280,250,SA,0.45)        # living
zone(X0+8,Y0+272,120,150,'#E8D9EE',0.6)  # work
zone(X0+140,Y0+380,200,110,'#F4DCCB',0.7) # dining
zone(X0+8,Y0+H-90,330,82,'#E6E1D8',0.9)   # kitchen
zone(X0+400,Y0+H-140,152,132,'#EAF1F5',0.9) # entry
# bed (E)
a(f'<rect x="{X0+14}" y="{Y0+40}" width="14" height="150" rx="3" fill="{W2}"/>')
a(f'<rect x="{X0+28}" y="{Y0+40}" width="187" height="150" rx="8" fill="#FFFDF9" stroke="{BR}" stroke-width="2"/>')
a(f'<rect x="{X0+36}" y="{Y0+52}" width="44" height="56" rx="8" fill="#fff" stroke="{BR}" stroke-width="2"/><rect x="{X0+36}" y="{Y0+122}" width="44" height="56" rx="8" fill="#fff" stroke="{BR}" stroke-width="2"/>')
a(f'<rect x="{X0+100}" y="{Y0+40}" width="115" height="150" rx="6" fill="{SG}" fill-opacity="0.55"/>')
# divider bookshelf
a(f'<rect x="{X0+246}" y="{Y0+16}" width="22" height="200" rx="3" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
for k in range(5): a(f'<line x1="{X0+246}" y1="{Y0+16+40*k}" x2="{X0+268}" y2="{Y0+16+40*k}" stroke="{W2}" stroke-width="2"/>')
# living: rug, sofa, coffee table, TV
a(f'<rect x="{X0+300}" y="{Y0+40}" width="200" height="190" rx="6" fill="{SA}" fill-opacity="0.8"/>')
a(f'<rect x="{X0+282}" y="{Y0+40}" width="80" height="190" rx="14" fill="{SG}"/><rect x="{X0+282}" y="{Y0+40}" width="26" height="190" rx="10" fill="#6F8F69"/>')
a(f'<rect x="{X0+392}" y="{Y0+100}" width="60" height="70" rx="8" fill="{W1}"/>')
a(f'<rect x="{X0+W-30}" y="{Y0+60}" width="24" height="150" rx="3" fill="{W2}"/><rect x="{X0+W-14}" y="{Y0+80}" width="6" height="110" fill="{T}"/>')
# work desk (F)
a(f'<rect x="{X0+12}" y="{Y0+300}" width="56" height="110" rx="4" fill="{W1}"/><circle cx="{X0+92}" cy="{Y0+355}" r="18" fill="#fff" stroke="{BR}" stroke-width="3"/>')
# dining (C)
cx,cy=X0+240,Y0+440
a(f'<circle cx="{cx}" cy="{cy}" r="42" fill="{W1}"/><circle cx="{cx-64}" cy="{cy}" r="16" fill="#fff" stroke="{BR}" stroke-width="3"/><circle cx="{cx+64}" cy="{cy}" r="16" fill="#fff" stroke="{BR}" stroke-width="3"/>')
# kitchen (B)
a(f'<rect x="{X0+8}" y="{Y0+H-64}" width="330" height="56" fill="#FFFDF9" stroke="{BR}" stroke-width="2"/>')
a(f'<rect x="{X0+20}" y="{Y0+H-58}" width="62" height="46" rx="4" fill="#DDE4E8"/><circle cx="{X0+140}" cy="{Y0+H-36}" r="14" fill="none" stroke="{G}" stroke-width="3"/><circle cx="{X0+176}" cy="{Y0+H-36}" r="14" fill="none" stroke="{G}" stroke-width="3"/><rect x="{X0+226}" y="{Y0+H-56}" width="56" height="40" rx="6" fill="#E6EEF2" stroke="#9FB3BF" stroke-width="2"/>')
# entry (A): bench + hooks
a(f'<rect x="{X0+W-40}" y="{Y0+H-130}" width="32" height="110" rx="4" fill="{W1}"/>')
for k in range(3): a(f'<circle cx="{X0+W-4}" cy="{Y0+H-115+k*30}" r="5" fill="{T}"/>')
# walkway
a(f'<path d="M{dx+42} {Y0+H-10} L{dx+42} {Y0+380} L{X0+300} {Y0+380} L{X0+300} {Y0+300}" fill="none" stroke="{A}" stroke-width="4" stroke-dasharray="10 9" stroke-linecap="round"/>')
a(f'<path d="M{X0+290} {Y0+305} L{X0+300} {Y0+288} L{X0+310} {Y0+305} Z" fill="{A}"/>')
a(f'<rect x="{X0+352}" y="{Y0+392}" width="150" height="30" rx="15" fill="#fff" stroke="{A}" stroke-width="2"/><text x="{X0+427}" y="{Y0+413}" font-size="16" font-weight="700" fill="{A}" text-anchor="middle">36 in walkway</text>')
# markers
def mk(x,y,l):
    a(f'<circle cx="{x}" cy="{y}" r="20" fill="{T}"/><text x="{x}" y="{y+7}" font-size="20" font-weight="700" fill="#fff" text-anchor="middle">{l}</text>')
mk(X0+W-80,Y0+H-110,'A'); mk(X0+366,Y0+H-36,'B'); mk(X0+156,Y0+390,'C'); mk(X0+520,Y0+250,'D'); mk(X0+215,Y0+228,'E'); mk(X0+108,Y0+300,'F')
# dimension labels
a(f'<text x="{X0+W/2}" y="{Y0+H+42}" font-size="17" fill="{G}" text-anchor="middle">20 ft (6.1 m)</text>')
a(f'<text x="{X0-26}" y="{Y0+H/2}" font-size="17" fill="{G}" text-anchor="middle" transform="rotate(-90 {X0-26} {Y0+H/2})">22 ft (6.7 m)</text>')
# legend
LX=720; ly=196
items=[("A","Entry drop zone","hooks, a bench, a tray for keys"),
("B","Kitchen","keep the counters clear"),
("C","Dining for two","a small round or drop-leaf table"),
("D","Living zone","sofa on a rug, TV on the wall"),
("E","Sleep zone","bed in the corner farthest from the door"),
("F","Work spot","a desk that is not your bed")]
for l,t1,t2 in items:
    a(f'<circle cx="{LX+20}" cy="{ly}" r="19" fill="{T}"/><text x="{LX+20}" y="{ly+7}" font-size="19" font-weight="700" fill="#fff" text-anchor="middle">{l}</text>')
    a(f'<text x="{LX+52}" y="{ly+7}" font-size="22" font-weight="700" fill="{T}">{t1}</text>')
    a(f'<text x="{LX+52}" y="{ly+34}" font-size="17" fill="{G}">{t2}</text>')
    ly+=78
a(f'<rect x="{LX}" y="{ly-14}" width="420" height="104" rx="12" fill="{SGL}"/>')
a(f'<rect x="{LX+18}" y="{ly+6}" width="16" height="60" rx="2" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
a(f'<text x="{LX+50}" y="{ly+24}" font-size="19" font-weight="700" fill="{T}">Open bookshelf divider</text>')
a(f'<text x="{LX+50}" y="{ly+50}" font-size="17" fill="{G}">screens the bed but lets light through;</text>')
a(f'<text x="{LX+50}" y="{ly+74}" font-size="17" fill="{G}">anchor it to the wall or floor</text>')
a(f'<text x="60" y="878" font-size="16" fill="{G}">Example plan for a 20 x 22 ft (about 440 sq ft) studio. Our own sample layout: swap zones to fit your windows and door.</text>')
a('</svg>')
open('z.svg','w').write('\n'.join(s))
