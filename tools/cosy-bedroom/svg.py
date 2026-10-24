T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';W1='#D9B48A';W2='#B98A5E'
s=[];a=s.append
k=0.13; RW,RL=3700,3600; ox,oy=90,170
BW,BL=1350,1900; RUGW,RUGL=2450,3050
ov=(RUGW-BW)//2
desc=(f"Top-down plan of a small UK double bedroom about 3.7 by 3.6 metres. A 135 cm double bed sits against the inside wall with a 245 cm wide rug under it, "
f"so about {ov//10} cm of rug shows on each side, inside the 45 to 60 cm a Laura Ashley designer recommends. Warm white 2700 to 3000K lamps on both bedside tables. "
"The radiator under the window is left uncovered and curtains stop clear of it. The wardrobe stands on an internal wall to reduce condensation. Aim for a bedroom temperature of about 16 to 18 degrees C.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="cb-t cb-d"><title id="cb-t">Cosy small bedroom plan</title><desc id="cb-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="42" font-weight="700" fill="{T}">A Cosy Small Bedroom, Measured</text>')
a(f'<text x="60" y="116" font-size="21" fill="{G}">Example UK double bedroom, about 3.7 x 3.6 m, seen from above</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
X=lambda mm: ox+mm*k; Y=lambda mm: oy+mm*k
a(f'<rect x="{ox}" y="{oy}" width="{RW*k}" height="{RL*k}" fill="#FFFFFF" stroke="{T}" stroke-width="5"/>')
# window on bottom wall (external), radiator under it
a(f'<rect x="{X(900)}" y="{Y(RL)-5}" width="{1400*k}" height="10" fill="#BFD4E0" stroke="{T}" stroke-width="2"/>')
a(f'<rect x="{X(1000)}" y="{Y(RL)-26}" width="{1200*k}" height="12" fill="#FFFFFF" stroke="{A}" stroke-width="2"/>')
a(f'<text x="{X(1600)}" y="{Y(RL)-34}" font-size="12" fill="{A}" text-anchor="middle">radiator kept clear</text>')
# curtains either side
for cx in (800,2300): a(f'<rect x="{X(cx)}" y="{Y(RL)-14}" width="{100*k*1.3}" height="10" fill="{SG}"/>')
# rug centred on bed, bed against top wall
bx=(RW-BW)/2
rx=(RW-RUGW)/2
a(f'<rect x="{X(rx)}" y="{Y(900)}" width="{RUGW*k}" height="{(RUGL-900)*k}" fill="{SA}" opacity="0.7" stroke="{W2}" stroke-width="2" stroke-dasharray="6 4"/>')
a(f'<rect x="{X(bx)}" y="{Y(0)}" width="{BW*k}" height="{BL*k}" rx="8" fill="#F3ECE2" stroke="{T}" stroke-width="2"/>')
a(f'<rect x="{X(bx)+8}" y="{Y(0)+8}" width="{BW*k-16}" height="34" rx="6" fill="#FFFFFF" stroke="{BR}"/>')
a(f'<text x="{X(RW/2)}" y="{Y(BL/2)+8}" font-size="15" font-weight="700" fill="{T}" text-anchor="middle">Bed 135 x 190</text>')
# overhang dims
yy=Y(1500)
a(f'<line x1="{X(rx)}" y1="{yy}" x2="{X(bx)}" y2="{yy}" stroke="{A}" stroke-width="2"/>')
a(f'<text x="{(X(rx)+X(bx))/2}" y="{yy-8}" font-size="13" font-weight="700" fill="{A}" text-anchor="middle">{ov//10} cm</text>')
a(f'<line x1="{X(bx+BW)}" y1="{yy}" x2="{X(rx+RUGW)}" y2="{yy}" stroke="{A}" stroke-width="2"/>')
a(f'<text x="{(X(bx+BW)+X(rx+RUGW))/2}" y="{yy-8}" font-size="13" font-weight="700" fill="{A}" text-anchor="middle">{ov//10} cm</text>')
# bedside tables with lamps
for tx in (bx-450,bx+BW+30):
    a(f'<rect x="{X(tx)}" y="{Y(30)}" width="{420*k}" height="{400*k}" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
    a(f'<circle cx="{X(tx+210)}" cy="{Y(230)}" r="11" fill="#FFE6B0" stroke="{A}" stroke-width="2"/>')
# wardrobe on internal (left) wall
a(f'<rect x="{X(0)+3}" y="{Y(1300)}" width="{550*k}" height="{1200*k}" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
a(f'<text x="{X(275)}" y="{Y(1900)}" font-size="12" fill="{T}" text-anchor="middle" transform="rotate(-90 {X(275)} {Y(1900)})">wardrobe, inside wall</text>')
a(f'<text x="{X(RW/2)}" y="{Y(RL)+28}" font-size="13" fill="{G}" text-anchor="middle">window on outside wall</text>')
# right side cards
LX=610
def card(y,h,title,lines,col):
    a(f'<rect x="{LX}" y="{y}" width="530" height="{h}" rx="12" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/><rect x="{LX}" y="{y}" width="8" height="{h}" rx="4" fill="{col}"/>')
    a(f'<text x="{LX+24}" y="{y+32}" font-size="19" font-weight="700" fill="{T}">{title}</text>')
    for i,l in enumerate(lines): a(f'<text x="{LX+24}" y="{y+60+i*23}" font-size="15" fill="{G}">{l}</text>')
card(160,100,'Temperature: about 16 to 18°C',['The Sleep Charity’s ideal range for a bedroom'],A)
card(276,100,'Light: warm white 2700 to 3000K',['Two low lamps instead of one bright ceiling light'],'#E8B04A')
card(392,124,'Rug: 45 to 60 cm showing',['Laura Ashley’s design head; a 245 cm rug','under a 135 cm double gives about 55 cm'],SA)
card(532,124,'Window: curtains, not radiator',['Close curtains at night, but keep the','radiator uncovered (Energy Saving Trust)'],SG)
card(672,100,'Damp: wardrobe on an inside wall',['Advice from Tandridge District Council'],W2)
a(f'<text x="60" y="860" font-size="14" fill="{G}">Example plan only. Rug width from Ruggable UK size guide; measure your own room before buying.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
