T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';W1='#D9B48A';W2='#B98A5E';CH='#5A5550'
s=[];a=s.append
desc=("Top-down floor plan of an example two-car garage, 20 by 20 feet, turned into a man cave with five zones. "
"A, lounge with a sofa on a rug facing a TV on the right wall. B, bar counter with two stools along the left wall. C, game table in the middle left. "
"D, storage wall with a workbench and closed cabinets along the back wall. E, a clear 36 inch path from the house door to the lounge. "
"A carbon monoxide alarm sits near the door to the house, outlets along the workbench are GFCI protected, and the insulated garage door is at the front.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="mc-t mc-d"><title id="mc-t">Garage man cave zone plan</title><desc id="mc-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">The Garage Man Cave Zone Plan</text>')
a(f'<text x="60" y="128" font-size="22" fill="{G}">One two-car garage, five zones, and room to walk</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
F=28; X0=80; Y0=186; W=20*F; H=20*F
a(f'<rect x="{X0-10}" y="{Y0-10}" width="{W+20}" height="{H+20}" fill="{CH}"/>')
a(f'<rect x="{X0}" y="{Y0}" width="{W}" height="{H}" fill="#EFEDE9"/>')
# garage door bottom
gx=X0+56; gw=16*F
a(f'<rect x="{gx}" y="{Y0+H}" width="{gw}" height="10" fill="#FFFFFF" stroke="{G}" stroke-width="2"/>')
for k in range(1,8): a(f'<line x1="{gx+k*gw/8}" y1="{Y0+H}" x2="{gx+k*gw/8}" y2="{Y0+H+10}" stroke="{G}" stroke-width="1.5"/>')
a(f'<text x="{gx+gw/2}" y="{Y0+H+36}" font-size="16" fill="{G}" text-anchor="middle">Insulated garage door · 20 ft (6.1 m) wide wall</text>')
# house door top right
dx=X0+420
a(f'<rect x="{dx}" y="{Y0-10}" width="84" height="10" fill="#EFEDE9"/><path d="M{dx} {Y0} A84 84 0 0 0 {dx+84} {Y0+84}" fill="none" stroke="{G}" stroke-width="2" stroke-dasharray="5 5"/><line x1="{dx+84}" y1="{Y0}" x2="{dx+84}" y2="{Y0+84}" stroke="{G}" stroke-width="3"/>')
a(f'<text x="{dx+42}" y="{Y0-18}" font-size="15" fill="{G}" text-anchor="middle">Door to house</text>')
def zone(x,y,w,h,col,op): a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{col}" fill-opacity="{op}"/>')
zone(X0+8,Y0+8,392,92,'#E6E1D8',0.95)     # D storage
zone(X0+300,Y0+170,252,300,SA,0.5)        # A lounge
zone(X0+8,Y0+300,110,250,'#F4DCCB',0.85)  # B bar
zone(X0+128,Y0+150,160,170,SGL,0.9)       # C game
# D: cabinets + workbench + pegboard
a(f'<rect x="{X0+12}" y="{Y0+12}" width="70" height="56" rx="3" fill="#9A9590"/><rect x="{X0+326}" y="{Y0+12}" width="70" height="56" rx="3" fill="#9A9590"/>')
a(f'<rect x="{X0+90}" y="{Y0+12}" width="228" height="56" rx="3" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
for k in range(4): a(f'<rect x="{X0+110+k*52}" y="{Y0+24}" width="30" height="10" rx="2" fill="{W2}"/>')
# GFCI marks
for gxk in (X0+120,X0+290):
    a(f'<rect x="{gxk-9}" y="{Y0+2}" width="18" height="10" rx="2" fill="#fff" stroke="{A}" stroke-width="2"/>')
# CO alarm near house door
a(f'<circle cx="{X0+540}" cy="{Y0+120}" r="16" fill="#fff" stroke="{A}" stroke-width="3"/><text x="{X0+540}" y="{Y0+126}" font-size="13" font-weight="700" fill="{A}" text-anchor="middle">CO</text>')
# A lounge: rug, sofa, table, TV on right wall
a(f'<rect x="{X0+330}" y="{Y0+200}" width="180" height="230" rx="6" fill="{SA}" fill-opacity="0.9"/>')
a(f'<rect x="{X0+312}" y="{Y0+210}" width="78" height="210" rx="14" fill="#B5763F"/><rect x="{X0+312}" y="{Y0+210}" width="26" height="210" rx="10" fill="#8E5A2E"/>')
a(f'<rect x="{X0+412}" y="{Y0+270}" width="52" height="90" rx="8" fill="{W1}"/>')
a(f'<rect x="{X0+W-28}" y="{Y0+220}" width="22" height="190" rx="3" fill="{W2}"/><rect x="{X0+W-12}" y="{Y0+250}" width="6" height="130" fill="{T}"/>')
# B bar along left wall
a(f'<rect x="{X0+10}" y="{Y0+320}" width="46" height="210" rx="4" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
for yy in (Y0+380,Y0+460): a(f'<circle cx="{X0+86}" cy="{yy}" r="16" fill="#fff" stroke="{BR}" stroke-width="3"/>')
# C game table
cx,cy=X0+208,Y0+235
a(f'<circle cx="{cx}" cy="{cy}" r="44" fill="{W1}"/>')
for ax,ay in ((-62,0),(62,0),(0,-62),(0,62)): a(f'<circle cx="{cx+ax}" cy="{cy+ay}" r="14" fill="#fff" stroke="{BR}" stroke-width="3"/>')
# E walkway
a(f'<path d="M{dx+42} {Y0+96} L{dx+42} {Y0+150} L{X0+360} {Y0+150} L{X0+360} {Y0+186}" fill="none" stroke="{A}" stroke-width="4" stroke-dasharray="10 9" stroke-linecap="round"/>')
a(f'<path d="M{X0+350} {Y0+182} L{X0+360} {Y0+198} L{X0+370} {Y0+182} Z" fill="{A}"/>')
a(f'<rect x="{X0+226}" y="{Y0+478}" width="0" height="0"/>')
def mk(x,y,l): a(f'<circle cx="{x}" cy="{y}" r="20" fill="{T}"/><text x="{x}" y="{y+7}" font-size="20" font-weight="700" fill="#fff" text-anchor="middle">{l}</text>')
mk(X0+525,Y0+455,'A'); mk(X0+96,Y0+316,'B'); mk(X0+150,Y0+176,'C'); mk(X0+372,Y0+86,'D'); mk(X0+480,Y0+150,'E')
a(f'<text x="{X0-26}" y="{Y0+H/2}" font-size="17" fill="{G}" text-anchor="middle" transform="rotate(-90 {X0-26} {Y0+H/2})">20 ft (6.1 m)</text>')
LX=720; ly=206
items=[("A","Lounge","sofa on a rug, TV on the side wall"),("B","Bar","counter and stools along a wall"),("C","Game table","cards, board games or a small table"),("D","Storage wall","workbench, pegboard, closed cabinets"),("E","Clear path","36 in from the house door")]
for l,t1,t2 in items:
    a(f'<circle cx="{LX+20}" cy="{ly}" r="19" fill="{T}"/><text x="{LX+20}" y="{ly+7}" font-size="19" font-weight="700" fill="#fff" text-anchor="middle">{l}</text>')
    a(f'<text x="{LX+52}" y="{ly+7}" font-size="22" font-weight="700" fill="{T}">{t1}</text><text x="{LX+52}" y="{ly+34}" font-size="17" fill="{G}">{t2}</text>')
    ly+=76
a(f'<rect x="{LX}" y="{ly-12}" width="420" height="150" rx="12" fill="#fff" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="{LX+20}" y="{ly+20}" font-size="19" font-weight="700" fill="{A}">Safety first</text>')
a(f'<circle cx="{LX+32}" cy="{ly+48}" r="13" fill="#fff" stroke="{A}" stroke-width="3"/><text x="{LX+32}" y="{ly+53}" font-size="10" font-weight="700" fill="{A}" text-anchor="middle">CO</text><text x="{LX+56}" y="{ly+54}" font-size="17" fill="{T}">CO alarm; never run engines inside</text>')
a(f'<rect x="{LX+23}" y="{ly+76}" width="18" height="10" rx="2" fill="#fff" stroke="{A}" stroke-width="2"/><text x="{LX+56}" y="{ly+87}" font-size="17" fill="{T}">GFCI-protected outlets</text>')
a(f'<text x="{LX+22}" y="{ly+122}" font-size="17" fill="{T}">Heaters 3 ft from anything that burns</text>')
a(f'<text x="60" y="878" font-size="16" fill="{G}">Example plan for a 20 x 20 ft two-car garage. Our own sample layout: check local permit rules before converting a garage.</text>')
a('</svg>')
import re
open('z.svg','w').write(re.sub(r'(\d+\.\d{1,2})\d+',r'\1','\n'.join(s)))
