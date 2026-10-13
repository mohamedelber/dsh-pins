import math,re
T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';W1='#D9B48A';W2='#B98A5E';SA='#ECCDA0'
s=[];a=s.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="ud-t ud-d"><title id="ud-t">How to measure for under stairs cupboard doors</title><desc id="ud-d">Side view of a straight staircase with the space underneath closed in by three doors whose top edges follow the slope of the stairs. Measure four things: the full width of the opening along the floor (W), the height at the tall end (H1), the height at the short end (H2) and the angle of the slope, copied with a sliding bevel or a cardboard template. Measure heights at both ends and in the middle because floors and stairs are rarely perfectly level. Leave an even gap of about 2 to 3 mm around each door. Keep any gas meter or fuse board easy to reach. Under current building rules in England a private stair is no steeper than 42 degrees.</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">How to Measure Under Stairs Doors</text>')
a(f'<text x="60" y="130" font-size="22" fill="{G}">Four measurements before you buy or build</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
FL=620; XL=200; XR=1000; HT=FL-400; HS=FL-90   # tall end on the left
# stairs above: string line from (XL,HT) to (XR,HS) extended
a(f'<line x1="60" y1="{FL}" x2="1140" y2="{FL}" stroke="{T}" stroke-width="4"/>')
# steps sawtooth above string
n=8; dx=(XR-XL)/n; dy=(HS-HT)/n
pts=[]
for i in range(n+1):
    x=XL+i*dx; y=HT+i*dy
    pts.append((x,y-28))
path='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)
st=[]
for i in range(n):
    x=XL+i*dx; y=HT+i*dy-28
    st.append(f'M{x:.1f},{y:.1f} h{dx:.1f} v{dy:.1f}')
a(f'<path d="{" ".join(st)}" fill="none" stroke="{W2}" stroke-width="5"/>')
a(f'<line x1="{XL}" y1="{HT}" x2="{XR}" y2="{HS}" stroke="{W2}" stroke-width="10"/>')
# cupboard front polygon
a(f'<path d="M{XL},{FL} L{XL},{HT} L{XR},{HS} L{XR},{FL} Z" fill="#FFFDF9" stroke="{BR}" stroke-width="3"/>')
# three doors with angled tops, gap
def yat(x): return HT+(x-XL)*(HS-HT)/(XR-XL)
edges=[XL+14,XL+275,XL+535,XR-14]
for i in range(3):
    x0=edges[i]+(0 if i==0 else 6); x1=edges[i+1]-(0 if i==2 else 6)
    y0=yat(x0)+14; y1=yat(x1)+14
    a(f'<path d="M{x0:.0f},{FL-10} L{x0:.0f},{y0:.0f} L{x1:.0f},{y1:.0f} L{x1:.0f},{FL-10} Z" fill="{SGL}" stroke="{SG}" stroke-width="3"/>')
    # hinges on left edge, knob right
    for hy in (y0+40, FL-60):
        a(f'<rect x="{x0-3:.0f}" y="{hy:.0f}" width="8" height="26" rx="2" fill="{G}"/>')
    ky=max(y1+50,(y1+FL)/2)
    a(f'<circle cx="{x1-22:.0f}" cy="{ky:.0f}" r="8" fill="{W2}"/>')
# dimension W
yW=FL+44
a(f'<line x1="{XL}" y1="{yW}" x2="{XR}" y2="{yW}" stroke="{A}" stroke-width="3"/><line x1="{XL}" y1="{yW-12}" x2="{XL}" y2="{yW+12}" stroke="{A}" stroke-width="3"/><line x1="{XR}" y1="{yW-12}" x2="{XR}" y2="{yW+12}" stroke="{A}" stroke-width="3"/>')
a(f'<rect x="{(XL+XR)/2-120:.0f}" y="{yW-16}" width="240" height="32" fill="{BG}"/><text x="{(XL+XR)/2:.0f}" y="{yW+8}" font-size="22" font-weight="700" fill="{A}" text-anchor="middle">W: full width</text>')
# H1 left
xH=XL-50
a(f'<line x1="{xH}" y1="{HT}" x2="{xH}" y2="{FL}" stroke="{A}" stroke-width="3"/><line x1="{xH-12}" y1="{HT}" x2="{xH+12}" y2="{HT}" stroke="{A}" stroke-width="3"/><line x1="{xH-12}" y1="{FL}" x2="{xH+12}" y2="{FL}" stroke="{A}" stroke-width="3"/>')
a(f'<text x="{xH-16}" y="{(HT+FL)/2-8:.0f}" font-size="22" font-weight="700" fill="{A}" text-anchor="end">H1</text><text x="{xH-16}" y="{(HT+FL)/2+18:.0f}" font-size="16" fill="{G}" text-anchor="end">tall end</text>')
# H2 right (moved out, angle construction at the short end)
xh=XR+130
a(f'<line x1="{xh}" y1="{HS}" x2="{xh}" y2="{FL}" stroke="{A}" stroke-width="3"/><line x1="{xh-12}" y1="{HS}" x2="{xh+12}" y2="{HS}" stroke="{A}" stroke-width="3"/><line x1="{xh-12}" y1="{FL}" x2="{xh+12}" y2="{FL}" stroke="{A}" stroke-width="3"/>')
a(f'<line x1="{XR}" y1="{HS}" x2="{xh}" y2="{HS}" stroke="{G}" stroke-width="1.5" stroke-dasharray="4 5"/>')
a(f'<text x="{xh-12}" y="{FL-14}" font-size="22" font-weight="700" fill="{A}" text-anchor="end">H2</text><text x="{xh}" y="{FL+30}" font-size="16" fill="{G}" text-anchor="middle">short end</text>')
sl=(HS-HT)/(XR-XL); L=110
a(f'<line x1="{XR}" y1="{HS}" x2="{XR+L}" y2="{HS+L*sl:.1f}" stroke="{A}" stroke-width="2.5" stroke-dasharray="7 6"/>')
r=70; ang=math.atan(sl)
a(f'<path d="M{XR+r},{HS} A{r},{r} 0 0 1 {XR+r*math.cos(ang):.1f},{HS+r*math.sin(ang):.1f}" fill="none" stroke="{A}" stroke-width="3"/>')
a(f'<text x="{XR+20}" y="{HS-44}" font-size="22" font-weight="700" fill="{A}">Angle</text><text x="{XR+20}" y="{HS-20}" font-size="15" fill="{G}">sliding bevel</text>')
# gap callout
a(f'<text x="{XL+150}" y="{FL-62}" font-size="17" fill="{T}" text-anchor="middle">2 to 3 mm gap</text><text x="{XL+150}" y="{FL-40}" font-size="17" fill="{T}" text-anchor="middle">around each door</text>')
cards=[("Measure 3 times","Heights at both ends and the middle"),("Make a template","Cardboard copy of the sloping top"),("Keep access","Meter and fuse board easy to open")]
for i,(t1,t2) in enumerate(cards):
    x=60+i*365
    a(f'<rect x="{x}" y="712" width="345" height="70" rx="12" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/><text x="{x+20}" y="742" font-size="19" font-weight="700" fill="{T}">{t1}</text><text x="{x+20}" y="768" font-size="16" fill="{G}">{t2}</text>')
a(f'<text x="60" y="822" font-size="18" fill="{T}"><tspan font-weight="700">Good to know:</tspan> in England a private stair built to current rules is no steeper than 42°.</text>')
a(f'<text x="60" y="872" font-size="14" fill="{G}">Stair pitch: Approved Document K, via the British Woodworking Federation. Gap and measuring steps: our rule of thumb.</text>')
a('</svg>')
svg=re.sub(r'(\d+\.\d{2,})',lambda m:str(round(float(m.group(1)),1)),''.join(s))
open('z.svg','w').write(svg)
