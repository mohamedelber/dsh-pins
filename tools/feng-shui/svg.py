T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';OAK='#C9A06B';CR='#FBF7F0';RED='#B8432F'
s=[];a=s.append
desc=("Left: plan of an example 12 by 12 foot bedroom with a queen bed (60 by 80 inches) in the commanding position: headboard against a solid wall, the door visible diagonally from the bed but not in line with it, nightstands on both sides, at least 24 inches of space on each side and at the foot, and the bed away from the window. "
"Right: two layouts feng shui practitioners advise against, the feet pointing straight out of the door and the headboard under a window, and our worked minimum for a queen: 108 by 104 inches of clear floor, using the Sleep Foundation's 24 inch guideline.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="fs-t fs-d"><title id="fs-t">Feng shui bedroom layout: the commanding position, measured</title><desc id="fs-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="42" font-weight="700" fill="{T}">The Commanding Position, Measured</text>')
a(f'<text x="60" y="116" font-size="21" fill="{G}">An example 12 x 12 ft bedroom with a queen bed</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
k=3.4; X=70; Y=170; R=144
def P(x,y): return X+x*k, Y+y*k
a(f'<rect x="{X}" y="{Y}" width="{R*k}" height="{R*k}" fill="{CR}" stroke="{T}" stroke-width="6"/>')
# window on right wall y 44-100
wx,wy=P(R,44); a(f'<rect x="{wx-5}" y="{wy}" width="10" height="{56*k}" fill="#BFD9E6" stroke="{T}" stroke-width="2"/>')
a(f'<text x="{wx+12}" y="{wy+28*k+5}" font-size="14" fill="{G}">window</text>')
# door bottom wall x 100-132
dx,dy=P(100,R); a(f'<line x1="{dx}" y1="{dy}" x2="{dx+32*k}" y2="{dy}" stroke="{CR}" stroke-width="8"/>')
a(f'<path d="M{dx+32*k} {dy} L{dx+32*k} {dy-32*k} A{32*k} {32*k} 0 0 0 {dx} {dy}" fill="none" stroke="{G}" stroke-width="2" stroke-dasharray="5 4"/>')
a(f'<line x1="{dx+32*k}" y1="{dy}" x2="{dx+32*k}" y2="{dy-32*k}" stroke="{T}" stroke-width="3"/>')
a(f'<text x="{dx+16*k}" y="{dy+24}" font-size="15" font-weight="700" fill="{T}" text-anchor="middle">door</text>')
# bed headboard on left wall, y 30-90, x 0-80
bx,by=P(0,30); a(f'<rect x="{bx}" y="{by}" width="{80*k}" height="{60*k}" rx="6" fill="#FFFFFF" stroke="{T}" stroke-width="3"/>')
a(f'<rect x="{bx}" y="{by}" width="{6*k}" height="{60*k}" fill="{OAK}"/>')
for py in (34,62):
    x1,y1=P(9,py); a(f'<rect x="{x1}" y="{y1}" width="{14*k}" height="{24*k}" rx="6" fill="{SGL}" stroke="{SG}" stroke-width="2"/>')
x1,y1=P(30,30); a(f'<rect x="{x1}" y="{y1}" width="{50*k}" height="{60*k}" rx="4" fill="{SG}" opacity=".55"/>')
cx,cy=P(55,60); a(f'<text x="{cx}" y="{cy-6}" font-size="17" font-weight="700" fill="{T}" text-anchor="middle">Queen bed</text><text x="{cx}" y="{cy+16}" font-size="14" fill="{T}" text-anchor="middle">60 x 80 in</text>')
# nightstands
for py in (8,92):
    x1,y1=P(2,py); a(f'<rect x="{x1}" y="{y1}" width="{18*k}" height="{18*k}" fill="{OAK}"/>')
# clearance dims
def dimv(x,y1,y2,lab,side=1):
    X1,Y1=P(x,y1); X2,Y2=P(x,y2)
    a(f'<line x1="{X1}" y1="{Y1}" x2="{X2}" y2="{Y2}" stroke="{A}" stroke-width="2"/>')
    for yy in (Y1,Y2): a(f'<line x1="{X1-6}" y1="{yy}" x2="{X1+6}" y2="{yy}" stroke="{A}" stroke-width="2"/>')
    a(f'<text x="{X1+10*side}" y="{(Y1+Y2)/2+5}" font-size="14" font-weight="700" fill="{A}" text-anchor="{"start" if side>0 else "end"}">{lab}</text>')
dimv(60,0,30,'30 in')
dimv(60,90,144,'54 in')
X1,Y1=P(80,80); X2,_=P(144,80)
a(f'<line x1="{X1}" y1="{Y1}" x2="{X2}" y2="{Y1}" stroke="{A}" stroke-width="2"/><text x="{(X1+X2)/2}" y="{Y1-8}" font-size="14" font-weight="700" fill="{A}" text-anchor="middle">64 in at the foot</text>')
# sightline
sx,sy=P(14,60); ex,ey=P(116,140)
a(f'<line x1="{sx}" y1="{sy}" x2="{ex}" y2="{ey}" stroke="{T}" stroke-width="2" stroke-dasharray="8 6"/>')
a(f'<text x="{(sx+ex)/2+10}" y="{(sy+ey)/2+34}" font-size="14" fill="{T}" transform="rotate(38 {(sx+ex)/2+10} {(sy+ey)/2+34})">door in view, not in line</text>')
a(f'<text x="{bx}" y="{Y+R*k+56}" font-size="14" fill="{G}">Solid wall behind, nightstands both sides, 24 in or more clear.</text>')
# right column
RX=650
a(f'<rect x="{RX}" y="150" width="490" height="660" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="{RX+24}" y="190" font-size="21" font-weight="700" fill="{T}">Layouts practitioners avoid</text>')
def mini(ox,oy,kind):
    m=1.25; W=144*m
    a(f'<rect x="{ox}" y="{oy}" width="{W}" height="{W}" fill="{CR}" stroke="{T}" stroke-width="4"/>')
    if kind=='door':
        a(f'<line x1="{ox+56*m}" y1="{oy+W}" x2="{ox+88*m}" y2="{oy+W}" stroke="{CR}" stroke-width="7"/>')
        a(f'<rect x="{ox+42*m}" y="{oy}" width="{60*m}" height="{80*m}" fill="{SG}" opacity=".55" stroke="{T}" stroke-width="2"/>')
        a(f'<line x1="{ox+72*m}" y1="{oy+82*m}" x2="{ox+72*m}" y2="{oy+W-4}" stroke="{RED}" stroke-width="3" stroke-dasharray="6 5"/>')
    else:
        a(f'<rect x="{ox+42*m}" y="{oy-4}" width="{60*m}" height="9" fill="#BFD9E6" stroke="{T}" stroke-width="2"/>')
        a(f'<rect x="{ox+42*m}" y="{oy+6}" width="{60*m}" height="{80*m}" fill="{SG}" opacity=".55" stroke="{T}" stroke-width="2"/>')
        a(f'<line x1="{ox+W}" y1="{oy+100*m}" x2="{ox+W}" y2="{oy+132*m}" stroke="{CR}" stroke-width="7"/>')
    a(f'<g stroke="{RED}" stroke-width="7" stroke-linecap="round"><line x1="{ox+W-34}" y1="{oy+12}" x2="{ox+W-12}" y2="{oy+34}"/><line x1="{ox+W-12}" y1="{oy+12}" x2="{ox+W-34}" y2="{oy+34}"/></g>')
mini(RX+24,215,'door'); mini(RX+262,215,'win')
a(f'<text x="{RX+24}" y="{215+180+28}" font-size="15" font-weight="700" fill="{T}">Feet in line with</text><text x="{RX+24}" y="{215+180+48}" font-size="15" font-weight="700" fill="{T}">the door</text>')
a(f'<text x="{RX+262}" y="{215+180+28}" font-size="15" font-weight="700" fill="{T}">Headboard under</text><text x="{RX+262}" y="{215+180+48}" font-size="15" font-weight="700" fill="{T}">a window</text>')
a(f'<rect x="{RX+24}" y="490" width="442" height="290" rx="12" fill="{SGL}"/>')
a(f'<text x="{RX+44}" y="526" font-size="19" font-weight="700" fill="{T}">Room check for a queen bed</text>')
rows=[("Bed (Sleep Foundation)","60 x 80 in"),("Space each side","24 in + 24 in"),("Space at the foot","24 in"),("Clear floor needed","108 x 104 in"),("In feet","9 ft x 8 ft 8 in")]
for i,(l,v) in enumerate(rows):
    yy=566+i*40; bold=' font-weight="700"' if i>=3 else ''
    a(f'<text x="{RX+44}" y="{yy}" font-size="16" fill="{T}"{bold}>{l}</text><text x="{RX+446}" y="{yy}" font-size="16" fill="{A if i>=3 else T}" text-anchor="end"{bold}>{v}</text>')
a(f'<text x="{RX+44}" y="{566+5*40-4}" font-size="13" fill="{G}">Plus a 36 in clear path from the door (Hunker).</text>')
a(f'<text x="60" y="850" font-size="14" fill="{G}">Example only. Placement rules: feng shui practitioners Anjie Cho, Rosanna Deflorian (Livingetc) and Sarah McAllister (Tom\'s Guide); a tradition,</text>')
a(f'<text x="60" y="872" font-size="14" fill="{G}">not science. Clearance: Sleep Foundation (24 in) and Hunker (36 in from the door). Room check: our worked example.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
