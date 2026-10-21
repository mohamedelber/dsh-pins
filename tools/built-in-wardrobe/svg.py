T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';W1='#D9B48A';W2='#B98A5E'
s=[];a=s.append
k=0.26; X0=150; FL=812
def X(mm): return X0+mm*k
def Y(mm): return FL-mm*k
desc=("Front view of an example built-in wardrobe 2,000 mm wide and 2,360 mm high, 600 mm deep, with the doors removed. "
"Bay A, 800 mm wide, is long hanging with a rail at about 1,900 mm and a storage shelf above. "
"Bay B, 600 mm wide, is double hanging with an upper rail at about 1,900 mm and a lower rail at about 900 mm. "
"Bay C, 600 mm wide, has a drawer bank up to about 900 mm and adjustable shelves about 350 mm apart above it. "
"Hinged doors should be no wider than about 600 mm each; allow at least 600 mm depth for hanging, or about 650 mm with sliding doors.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="bw-t bw-d"><title id="bw-t">Built-in wardrobe interior heights</title><desc id="bw-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="44" font-weight="700" fill="{T}">Built-In Wardrobe Interior Heights</text>')
a(f'<text x="60" y="118" font-size="22" fill="{G}">A 2 m wardrobe, doors removed, typical UK sizes in mm</text>')
a(f'<text x="1140" y="50" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
W=2000;H=2360
# carcass
a(f'<rect x="{X(0)}" y="{Y(H)}" width="{W*k}" height="{H*k}" fill="#FFFFFF" stroke="{W2}" stroke-width="5"/>')
for m in (800,1400): a(f'<line x1="{X(m)}" y1="{Y(H)}" x2="{X(m)}" y2="{Y(0)}" stroke="{W2}" stroke-width="4"/>')
a(f'<line x1="{X0-40}" y1="{FL}" x2="{X(W)+40}" y2="{FL}" stroke="{T}" stroke-width="4"/>')
def shelf(x1,x2,mm): a(f'<rect x="{X(x1)+2}" y="{Y(mm)-4}" width="{(x2-x1)*k-4}" height="8" fill="{W1}" stroke="{W2}" stroke-width="1.5"/>')
def rail(x1,x2,mm): a(f'<line x1="{X(x1)+8}" y1="{Y(mm)}" x2="{X(x2)-8}" y2="{Y(mm)}" stroke="#8C8C8C" stroke-width="6" stroke-linecap="round"/>')
def garments(x1,x2,mm,length,col,n):
    w=(x2-x1)*k-24; step=w/n
    for i in range(n):
        cx=X(x1)+12+step*(i+0.5)
        a(f'<path d="M{cx} {Y(mm)} l-3 -9" stroke="{G}" stroke-width="2" fill="none"/>')
        a(f'<path d="M{cx-step*0.42} {Y(mm)+8} L{cx} {Y(mm)+1} L{cx+step*0.42} {Y(mm)+8} L{cx+step*0.36} {Y(mm)+length*k} L{cx-step*0.36} {Y(mm)+length*k} Z" fill="{col}" stroke="#fff" stroke-width="1.5"/>')
# Bay A long hang
shelf(0,800,2000); rail(0,800,1900); garments(0,800,1900,1350,SG,6)
# Bay B double hang
shelf(800,1400,2000); rail(800,1400,1900); garments(800,1400,1900,800,SA,5)
rail(800,1400,900); garments(800,1400,900,700,'#C9B49A',5)
# Bay C drawers + shelves
for i,(b,t) in enumerate(((0,300),(300,600),(600,900))):
    a(f'<rect x="{X(1400)+8}" y="{Y(t)+4}" width="{600*k-16}" height="{(t-b)*k-8}" rx="4" fill="{SGL}" stroke="{SG}" stroke-width="2"/>')
    a(f'<rect x="{X(1700)-16}" y="{Y((b+t)/2)-3}" width="32" height="6" rx="3" fill="{W2}"/>')
for m in (900,1250,1600,2000): shelf(1400,2000,m)
for m,c in ((900,3),(1250,3),(1600,3)):
    for j in range(c): a(f'<rect x="{X(1400)+18+j*44}" y="{Y(m)-4-26}" width="38" height="26" rx="4" fill="{"#E3D3BE" if j%2 else "#CFC2B0"}"/>')
# top storage boxes
for x1 in (60,860,1460): a(f'<rect x="{X(x1)}" y="{Y(2000)-4-60}" width="120" height="60" rx="4" fill="#E9DFD2" stroke="{BR}" stroke-width="2"/>')
# bay letters
for x1,x2,L in ((0,800,'A'),(800,1400,'B'),(1400,2000,'C')):
    a(f'<circle cx="{(X(x1)+X(x2))/2}" cy="{Y(H)-26}" r="17" fill="{A}"/><text x="{(X(x1)+X(x2))/2}" y="{Y(H)-20}" font-size="18" font-weight="700" fill="#fff" text-anchor="middle">{L}</text>')
# left height dims
def hdim(mm,label,x=X0-18):
    a(f'<line x1="{x}" y1="{Y(mm)}" x2="{X(0)}" y2="{Y(mm)}" stroke="{A}" stroke-width="1.5" stroke-dasharray="5 4"/>')
    a(f'<text x="{x-6}" y="{Y(mm)+6}" font-size="16" font-weight="700" fill="{A}" text-anchor="end">{label}</text>')
hdim(H,'2,360'); hdim(1900,'1,900'); hdim(900,'900'); hdim(0,'0')
a(f'<text x="{X0-70}" y="{Y(H)-16}" font-size="14" fill="{G}" text-anchor="middle">mm</text>')
# width dims bottom
def wdim(x1,x2,label,y):
    a(f'<line x1="{X(x1)}" y1="{y}" x2="{X(x2)}" y2="{y}" stroke="{A}" stroke-width="2.5"/><line x1="{X(x1)}" y1="{y-8}" x2="{X(x1)}" y2="{y+8}" stroke="{A}" stroke-width="2.5"/><line x1="{X(x2)}" y1="{y-8}" x2="{X(x2)}" y2="{y+8}" stroke="{A}" stroke-width="2.5"/>')
    a(f'<text x="{(X(x1)+X(x2))/2}" y="{y+24}" font-size="16" font-weight="700" fill="{A}" text-anchor="middle">{label}</text>')
wdim(0,800,'800',836); wdim(800,1400,'600',836); wdim(1400,2000,'600',836)
# legend right
LX=740
def card(y,h,title,lines,col):
    a(f'<rect x="{LX}" y="{y}" width="400" height="{h}" rx="12" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
    a(f'<rect x="{LX}" y="{y}" width="8" height="{h}" rx="4" fill="{col}"/>')
    a(f'<text x="{LX+24}" y="{y+32}" font-size="19" font-weight="700" fill="{T}">{title}</text>')
    for i,l in enumerate(lines): a(f'<text x="{LX+24}" y="{y+60+i*24}" font-size="15" fill="{G}">{l}</text>')
card(170,112,'A  Long hanging',['Rail at about 1,900 mm','Dresses and coats hang full length'],SG)
card(296,112,'B  Double hanging',['Rails at about 1,900 mm and 900 mm','Two rows of shirts, skirts, trousers'],SA)
card(422,112,'C  Drawers and shelves',['Drawer bank up to about 900 mm','Shelves about 350–400 mm apart'],SGL)
card(548,136,'Depth and doors',['At least 600 mm deep for hanging','About 650 mm or more with sliding doors','Hinged doors no wider than ~600 mm'],A)
a(f'<text x="60" y="880" font-size="13" fill="{G}">Typical figures from FCI London, The Little Design Corner, Online Bedrooms and Häfele; check your own room and fittings.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
