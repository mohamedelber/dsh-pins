T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';OAK='#C9A06B';CR='#FBF7F0';OKL='#E9D8BE'
s=[];a=s.append
desc=("Elevation of an example fitted wardrobe 2.2 metres high and 2 metres wide, in three bays. Left: double hanging, with the lower rail at 90 cm and the upper rail at about 2 m, giving shirts on the upper rail about 90 cm of drop and trousers on the lower rail 60 to 70 cm. "
"Middle: one rail at 180 cm for dresses and coats, which need 100 to 150 cm of drop. Right: shelves 35 to 40 cm apart, enough for a stack of about 10 jumpers (about 30 cm), with drawers below and boxes for out-of-season clothes on top. "
"Hanging needs an internal depth of at least 60 cm. Most-worn clothes go in the middle zone, between knee and head height.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="ow-t ow-d"><title id="ow-t">A wardrobe organised by height</title><desc id="ow-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="42" font-weight="700" fill="{T}">A Wardrobe, Organised by Height</text>')
a(f'<text x="60" y="116" font-size="21" fill="{G}">Where each type of clothing fits, in cm</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
k=2.75; X=150; fl=770; H=220; W=200
top=fl-H*k
a(f'<rect x="{X}" y="{top}" width="{W*k}" height="{H*k}" fill="{OKL}" stroke="{T}" stroke-width="4"/>')
bw=W*k/3
for i in (1,2): a(f'<line x1="{X+i*bw}" y1="{top}" x2="{X+i*bw}" y2="{fl}" stroke="{T}" stroke-width="3"/>')
# top boxes zone: shelf at 200cm across all
a(f'<line x1="{X}" y1="{fl-205*k}" x2="{X+W*k}" y2="{fl-205*k}" stroke="{T}" stroke-width="3"/>')
for i in range(3):
    for j in range(2):
        bx=X+i*bw+12+j*(bw/2-6); a(f'<rect x="{bx}" y="{fl-219*k}" width="{bw/2-18}" height="{12*k}" rx="4" fill="#D8CBBB" stroke="#B5A898"/>')
def rail(x0,x1,h): a(f'<line x1="{x0+8}" y1="{fl-h*k}" x2="{x1-8}" y2="{fl-h*k}" stroke="#8C8C8C" stroke-width="5"/>')
def clothes(x0,x1,h,drop,cols):
    n=9; w=(x1-x0-24)/n
    for i in range(n):
        cx=x0+12+i*w; a(f'<rect x="{cx+1}" y="{fl-h*k+6}" width="{w-2}" height="{drop*k}" rx="3" fill="{cols[i%len(cols)]}"/>')
# left bay: double hanging rails at 196 and 90
x0,x1=X,X+bw
rail(x0,x1,198); clothes(x0,x1,198,88,['#F3EEE6','#C9D6E3','#9DB4CC','#E8C9C0','#5B6F8A'])
rail(x0,x1,90); clothes(x0,x1,90,72,['#3E4A5C','#B9A88F','#2F2F2F','#6B7F95'])
# middle bay: single rail 180
x0,x1=X+bw,X+2*bw
rail(x0,x1,180); clothes(x0,x1,180,140,['#7A8C70','#C2A68A','#2F3A48','#D9CFC0','#8E5A4A'])
# right bay: shelves
x0,x1=X+2*bw,X+3*bw
for h in (75,110,145,180):
    a(f'<line x1="{x0}" y1="{fl-h*k}" x2="{x1}" y2="{fl-h*k}" stroke="{T}" stroke-width="3"/>')
for h in (75,110,145):
    for j in range(2):
        sx=x0+14+j*(bw/2-6)
        for m in range(4): a(f'<rect x="{sx}" y="{fl-(h+3+m*6.5)*k-6*k}" width="{bw/2-22}" height="{6*k}" rx="3" fill="{["#E9E2D6","#B7C4CF","#C9B8A3","#8FA0B0"][m]}"/>')
for h in (25,50):
    a(f'<rect x="{x0+10}" y="{fl-(h+22)*k}" width="{bw-20}" height="{22*k}" fill="#F6EFE4" stroke="{T}" stroke-width="2"/><circle cx="{x0+bw/2}" cy="{fl-(h+11)*k}" r="5" fill="{T}"/>')
a(f'<rect x="{X-20}" y="{fl}" width="{W*k+40}" height="8" fill="#B98A5E"/>')
# dims on left
def dim(h,lab,xx,col=A):
    a(f'<line x1="{xx}" y1="{fl}" x2="{xx}" y2="{fl-h*k}" stroke="{col}" stroke-width="2"/><line x1="{xx-6}" y1="{fl-h*k}" x2="{xx+6}" y2="{fl-h*k}" stroke="{col}" stroke-width="2"/>')
    a(f'<text x="{xx-10}" y="{fl-h*k+5}" font-size="15" font-weight="700" fill="{col}" text-anchor="end">{lab}</text>')
dim(90,'90 cm',X-20); dim(198,'~2 m',X-60)
# labels under bays
for i,(t1,t2) in enumerate([("Double hanging","shirts above, trousers below"),("Long hanging","rail at 180 cm"),("Shelves 35-40 cm apart","drawers below")]):
    cx=X+bw*i+bw/2
    a(f'<text x="{cx}" y="{fl+34}" font-size="16" font-weight="700" fill="{T}" text-anchor="middle">{t1}</text><text x="{cx}" y="{fl+54}" font-size="14" fill="{G}" text-anchor="middle">{t2}</text>')
# right info panel
RX=800
a(f'<rect x="{RX}" y="150" width="340" height="650" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
rows=[("Depth for hanging","60 cm min"),("Shirts, blouses","about 90 cm drop"),("Dresses","about 150 cm"),("Coats","about 100 cm"),("Trousers, hung","60-70 cm"),("10 folded jumpers","about 30 cm"),("10 folded T-shirts","about 25 cm")]
a(f'<text x="{RX+22}" y="190" font-size="20" font-weight="700" fill="{A}">Space each item needs</text>')
for i,(l,v) in enumerate(rows):
    y=232+i*44
    a(f'<text x="{RX+22}" y="{y}" font-size="15" fill="{T}">{l}</text><text x="{RX+318}" y="{y}" font-size="15" font-weight="700" fill="{T}" text-anchor="end">{v}</text>')
    a(f'<line x1="{RX+22}" y1="{y+14}" x2="{RX+318}" y2="{y+14}" stroke="{BR}"/>')
a(f'<rect x="{RX+18}" y="560" width="304" height="220" rx="12" fill="{SGL}"/>')
for i,t in enumerate(["Zones","Top: out-of-season boxes","Middle: what you wear most","Bottom: shoes and drawers","Don't overfill the rail: clothes","need air and room to hang."]):
    a(f'<text x="{RX+36}" y="{596+i*30}" font-size="{17 if i==0 else 15}" font-weight="{700 if i==0 else 400}" fill="{T}">{t}</text>')
a(f'<text x="60" y="858" font-size="14" fill="{G}">Example only. Sources: FCI London (depth, rail heights, drop lengths), IKEA PAX planning guide (coats, trousers, folded stacks),</text>')
a(f'<text x="60" y="880" font-size="14" fill="{G}">Timberwise (don\'t overfill). Upper rail height and layout: our worked example.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
