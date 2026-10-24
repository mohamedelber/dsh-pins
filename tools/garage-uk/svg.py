T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';W1='#D9B48A';W2='#B98A5E'
s=[];a=s.append
k=0.10
GW,GL=2400,4900
CAR_W,CAR_L=2000,4300
door=800
left=GW-CAR_W
desc=(f"Top-down plan of a typical UK single garage, about 2.4 m wide by 4.9 m long, with a family car about 2 m wide including mirrors and 4.3 m long parked inside. "
f"That leaves only about {left} mm of width in total, far less than the 800 to 1000 mm needed on each side to open the doors, so a car and side shelving rarely fit together in an older single garage. "
f"The car also leaves about {GL-CAR_L} mm of length, enough for a shallow shelf or wall rack across the back wall. "
"With no car, the whole garage can be used: deep shelving down one side, a workbench at the back and bikes and tools on the other wall, keeping a clear path down the middle.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="gg-t gg-d"><title id="gg-t">How much room a UK single garage really has</title><desc id="gg-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="42" font-weight="700" fill="{T}">Will a Car and Storage Both Fit?</text>')
a(f'<text x="60" y="116" font-size="21" fill="{G}">Typical UK single garage, about 2.4 x 4.9 m, seen from above (mm)</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
def garage(ox,oy,title):
    a(f'<text x="{ox+GW*k/2}" y="{oy-18}" font-size="21" font-weight="700" fill="{T}" text-anchor="middle">{title}</text>')
    a(f'<rect x="{ox}" y="{oy}" width="{GW*k}" height="{GL*k}" fill="#FFFFFF" stroke="{T}" stroke-width="4"/>')
    a(f'<line x1="{ox+12}" y1="{oy+GL*k}" x2="{ox+GW*k-12}" y2="{oy+GL*k}" stroke="#FFFFFF" stroke-width="6"/>')
    a(f'<text x="{ox+GW*k/2}" y="{oy+GL*k+22}" font-size="14" fill="{G}" text-anchor="middle">garage door</text>')
# left: car inside
ox,oy=120,190
garage(ox,oy,'With a car')
cx=ox+(GW-CAR_W)/2*k; cy=oy+(GL-CAR_L)*k-10
a(f'<rect x="{cx}" y="{cy}" width="{CAR_W*k}" height="{CAR_L*k}" rx="18" fill="{SA}" stroke="{W2}" stroke-width="2"/>')
a(f'<text x="{cx+CAR_W*k/2}" y="{cy+CAR_L*k/2}" font-size="17" font-weight="700" fill="{T}" text-anchor="middle">Car</text>')
a(f'<text x="{cx+CAR_W*k/2}" y="{cy+CAR_L*k/2+22}" font-size="14" fill="{T}" text-anchor="middle">~2,000 wide</text>')
a(f'<text x="{cx+CAR_W*k/2}" y="{cy+CAR_L*k/2+40}" font-size="14" fill="{T}" text-anchor="middle">with mirrors</text>')
a(f'<rect x="{ox+4}" y="{oy+4}" width="{GW*k-8}" height="{(GL-CAR_L)*k-18}" fill="{SGL}" stroke="{SG}" stroke-width="2" stroke-dasharray="5 4"/>')
# door swing arcs
r=door*k
a(f'<text x="{cx-60}" y="{cy+150}" font-size="13" fill="{A}">doors</text>')
a(f'<path d="M{cx} {cy+60} A{r} {r} 0 0 0 {cx-r*0.7:.1f} {cy+60+r*0.7:.1f}" fill="none" stroke="{A}" stroke-width="2.5"/>')
a(f'<path d="M{cx+CAR_W*k} {cy+60} A{r} {r} 0 0 1 {cx+CAR_W*k+r*0.7:.1f} {cy+60+r*0.7:.1f}" fill="none" stroke="{A}" stroke-width="2.5"/>')
# notes for left
nx=ox+GW*k+40
def note(x,y,title,lines,col):
    a(f'<rect x="{x}" y="{y}" width="330" height="{48+len(lines)*24}" rx="12" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/><rect x="{x}" y="{y}" width="8" height="{48+len(lines)*24}" rx="4" fill="{col}"/>')
    a(f'<text x="{x+22}" y="{y+32}" font-size="18" font-weight="700" fill="{T}">{title}</text>')
    for i,l in enumerate(lines): a(f'<text x="{x+22}" y="{y+60+i*24}" font-size="15" fill="{G}">{l}</text>')
note(nx,200,'Only ~400 mm spare',['in total across the width,','but doors need 800 to','1,000 mm on each side'],A)
note(nx,340,f'~{GL-CAR_L} mm at the back',['room for one shallow','shelf or a wall rack'],SG)
# right: no car
ox2,oy2=760,190
garage(ox2,oy2,'Storage only')
# shelving left side 450 deep
a(f'<rect x="{ox2+4}" y="{oy2+4}" width="{450*k}" height="{GL*k-8}" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
a(f'<text x="{ox2+4+450*k/2}" y="{oy2+GL*k/2}" font-size="13" fill="{T}" text-anchor="middle" transform="rotate(-90 {ox2+4+450*k/2} {oy2+GL*k/2})">shelving 450 deep</text>')
# workbench back
a(f'<rect x="{ox2+4+450*k}" y="{oy2+4}" width="{GW*k-8-450*k}" height="{600*k}" fill="{SA}" stroke="{W2}" stroke-width="2"/>')
a(f'<text x="{ox2+4+450*k+(GW*k-8-450*k)/2}" y="{oy2+4+600*k/2+5}" font-size="13" fill="{T}" text-anchor="middle">workbench</text>')
# right wall bikes/tools 300
a(f'<rect x="{ox2+GW*k-4-300*k}" y="{oy2+4+600*k}" width="{300*k}" height="{GL*k-8-600*k}" fill="{SGL}" stroke="{SG}" stroke-width="2"/>')
a(f'<text x="{ox2+GW*k-4-300*k/2}" y="{oy2+GL*k/2+60}" font-size="13" fill="{T}" text-anchor="middle" transform="rotate(-90 {ox2+GW*k-4-300*k/2} {oy2+GL*k/2+60})">bikes and tools ~300</text>')
mid=GW-450-300
a(f'<text x="{ox2+4+450*k+mid*k/2}" y="{oy2+GL*k/2+80}" font-size="14" font-weight="700" fill="{A}" text-anchor="middle">~{mid:,}</text>')
a(f'<text x="{ox2+4+450*k+mid*k/2}" y="{oy2+GL*k/2+98}" font-size="13" fill="{A}" text-anchor="middle">clear path</text>')
note(ox2-330-30,560,'No car? Use all of it',['Deep shelving one side,','bikes and tools on the','other, bench at the back'],SG)
a(f'<text x="60" y="842" font-size="14" fill="{G}">Sizes: single garage 2.4 x 4.9 m, car about 2 m wide with mirrors, 80 to 100 cm door space each side (Homebuilding).</text>')
a(f'<text x="60" y="862" font-size="14" fill="{G}">Car length 4.3 m (RAC Foundation). Bike racks take about 30 cm of wall per bike (GaragePride). Measure your own first.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
