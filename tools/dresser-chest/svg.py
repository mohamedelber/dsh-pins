T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';OAK='#C9A06B';OAKD='#A97F4C';CR='#FBF7F0'
s=[];a=s.append
desc=("Two IKEA STORKLINTA 6-drawer units with the same drawers and price, drawn to scale. The wide, low dresser is 55 1/8 inches wide, 18 7/8 deep and 29 1/2 tall; the tall chest of drawers is 27 1/2 wide, 18 7/8 deep and 47 1/4 tall. Both are taller than 27 inches, so the federal tip-over standard applies and both should be anchored to the wall. "
"In plan, the dresser covers 7.2 square feet and the chest 3.6 square feet; with 36 inches clear in front to open drawers, they need about 21 and 10.5 square feet. "
"The dresser holds 8.4 cubic feet and the chest 6.8 cubic feet, so the chest uses half the floor for 81 percent of the storage: 1.89 cubic feet per square foot of floor against 1.16.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="dc-t dc-d"><title id="dc-t">Dresser vs chest of drawers: same drawers, different shape</title><desc id="dc-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="78" font-size="40" font-weight="700" fill="{T}">Dresser vs Chest: Same Drawers, Different Shape</text>')
a(f'<text x="60" y="114" font-size="20" fill="{G}">IKEA STORKLINTA 6-drawer, wide and tall versions, same price, drawn to scale</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
# left panel elevation
a(f'<rect x="40" y="140" width="600" height="470" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="64" y="178" font-size="19" font-weight="700" fill="{A}">Front view</text>')
k=6.4; FL=560
def unit(x,w,h,cols,rows):
    W=w*k; H=h*k; y=FL-H
    a(f'<rect x="{x}" y="{y}" width="{W}" height="{H}" rx="3" fill="{OAK}" stroke="{OAKD}" stroke-width="2"/>')
    cw=(W-8)/cols; rh=(H-8)/rows
    for c in range(cols):
        for r in range(rows):
            dx=x+4+c*cw; dy=y+4+r*rh
            a(f'<rect x="{dx+2}" y="{dy+2}" width="{cw-4}" height="{rh-4}" rx="2" fill="#D9B786" stroke="{OAKD}" stroke-width="1"/><circle cx="{dx+cw/2}" cy="{dy+rh/2}" r="3.5" fill="{T}"/>')
    return x,y,W,H
x1,y1,W1,H1=unit(100,55.125,29.5,2,3)
x2,y2,W2,H2=unit(470,27.5,47.25,1,6)
a(f'<line x1="60" y1="{FL}" x2="620" y2="{FL}" stroke="{T}" stroke-width="3"/>')
a(f'<text x="{x1+W1/2}" y="{y1-12}" font-size="16" font-weight="700" fill="{T}" text-anchor="middle">Dresser: 55 1/8 W x 29 1/2 H in</text>')
a(f'<text x="{x2+W2/2}" y="{y2-34}" font-size="16" font-weight="700" fill="{T}" text-anchor="middle">Chest of drawers:</text><text x="{x2+W2/2}" y="{y2-14}" font-size="16" font-weight="700" fill="{T}" text-anchor="middle">27 1/2 W x 47 1/4 H in</text>')
y27=FL-27*k
a(f'<line x1="60" y1="{y27}" x2="620" y2="{y27}" stroke="{A}" stroke-width="2" stroke-dasharray="8 6"/>')
a(f'<text x="64" y="{y27-8}" font-size="14" font-weight="700" fill="{A}">27 in</text>')
a(f'<text x="64" y="590" font-size="14" fill="{T}">Both are over 27 in tall: the federal tip-over standard applies. Anchor both.</text>')
# right panel plan
RX=660
a(f'<rect x="{RX}" y="140" width="500" height="470" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="{RX+24}" y="178" font-size="19" font-weight="700" fill="{A}">Floor plan, with 36 in to open drawers</text>')
p=3.6; WY=220
a(f'<line x1="{RX+20}" y1="{WY}" x2="{RX+480}" y2="{WY}" stroke="{T}" stroke-width="6"/><text x="{RX+250}" y="{WY-8}" font-size="13" fill="{G}" text-anchor="middle">wall</text>')
def plan(x,w,lab1,lab2):
    W=w*p; D=18.875*p; C=36*p
    a(f'<rect x="{x}" y="{WY}" width="{W}" height="{D}" fill="{OAK}" stroke="{OAKD}" stroke-width="2"/>')
    a(f'<rect x="{x}" y="{WY+D}" width="{W}" height="{C}" fill="{SGL}" stroke="{SG}" stroke-width="1.5" stroke-dasharray="6 4"/>')
    a(f'<text x="{x+W/2}" y="{WY+D/2+5}" font-size="14" font-weight="700" fill="{T}" text-anchor="middle">{lab1}</text>')
    a(f'<text x="{x+W/2}" y="{WY+D+C/2}" font-size="13" fill="#4F6B49" text-anchor="middle">36 in clear</text>')
    a(f'<text x="{x+W/2}" y="{WY+D+C+26}" font-size="15" font-weight="700" fill="{A}" text-anchor="middle">{lab2}</text>')
plan(RX+28,55.125,'7.2 sq ft','21 sq ft in use')
plan(RX+28+55.125*p+40,27.5,'3.6 sq ft','10.5 sq ft in use')
a(f'<text x="{RX+24}" y="560" font-size="14" fill="{T}">The chest frees about 10 sq ft of floor in a small</text>')
a(f'<text x="{RX+24}" y="582" font-size="14" fill="{T}">bedroom. Wayfair and Coleman suggest 36 in in front.</text>')
# bottom table
TY=640
a(f'<rect x="40" y="{TY}" width="1120" height="170" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
cols=[(64,'start','',''),(430,'middle','Floor area','sq ft'),(600,'middle','Storage','cu ft'),(770,'middle','Storage per','sq ft of floor'),(950,'middle','Price','Oct 2026')]
for x,anc,h1,h2 in cols[1:]:
    a(f'<text x="{x}" y="{TY+34}" font-size="15" font-weight="700" fill="{G}" text-anchor="{anc}">{h1}</text><text x="{x}" y="{TY+52}" font-size="12" fill="{G}" text-anchor="{anc}">{h2}</text>')
rows=[('Wide dresser (6 drawers)','7.2','8.4','1.16','$249.99',T),('Tall chest (6 drawers)','3.6','6.8','1.89','$249.99',A)]
for i,(n,f,v,r,pr,c) in enumerate(rows):
    y=TY+88+i*36
    a(f'<text x="64" y="{y}" font-size="17" font-weight="700" fill="{c}">{n}</text>')
    for (x,anc,_,_),val in zip(cols[1:],[f,v,r,pr]):
        a(f'<text x="{x}" y="{y}" font-size="17" font-weight="700" fill="{c}" text-anchor="{anc}">{val}</text>')
a(f'<text x="64" y="{TY+156}" font-size="15" font-style="italic" fill="{T}">The tall chest uses half the floor for 81% of the storage.</text>')
a(f'<text x="60" y="846" font-size="14" fill="{G}">Sizes and storage capacity from IKEA US product pages (STORKLINTA 6-drawer, checked Oct 26, 2026; prices change). Clearance: Wayfair and</text>')
a(f'<text x="60" y="868" font-size="14" fill="{G}">Coleman Furniture guides. 27 in threshold: CPSC clothing storage unit rule (16 CFR part 1261), in force since Sept 1, 2023.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
