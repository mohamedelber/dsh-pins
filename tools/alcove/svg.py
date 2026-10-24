T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';OAK='#C9A06B'
s=[];a=s.append
desc=("Left: front view of an example 100 cm wide alcove beside a chimney breast, with a cupboard below and four shelves above spaced about 30 cm apart, a 150 mm cable zone marked along the ceiling and the corners, and a note that 18 mm MDF starts to sag visibly at about 600 to 700 mm, so wider alcoves need 25 mm boards or a mid support. "
"Right: shelf depth compared with a typical alcove depth of 300 to 450 mm: books 200 to 250 mm, media and storage 300 to 400 mm, a drinks cabinet 300 to 350 mm, and a hanging wardrobe at least 600 mm, which stands proud of most alcoves.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="al-t al-d"><title id="al-t">Alcove shelving measurements</title><desc id="al-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="42" font-weight="700" fill="{T}">An Alcove, Measured</text>')
a(f'<text x="60" y="116" font-size="21" fill="{G}">Shelf spacing, spans and depths for a UK chimney-breast alcove</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
k=2.3; x0=150; top=165; H=240; W=100
yb=top+H*k
a(f'<rect x="{x0-70}" y="{top}" width="70" height="{H*k:.0f}" fill="{SGL}" stroke="{BR}"/>')
a(f'<text x="{x0-35}" y="{top+H*k/2:.0f}" font-size="14" fill="{G}" text-anchor="middle" transform="rotate(-90 {x0-35} {top+H*k/2:.0f})">chimney breast</text>')
a(f'<rect x="{x0}" y="{top}" width="{W*k:.0f}" height="{H*k:.0f}" fill="#FFFFFF" stroke="{T}" stroke-width="3"/>')
# cable zones
z=15*k
a(f'<rect x="{x0}" y="{top}" width="{W*k:.0f}" height="{z:.1f}" fill="{A}" opacity="0.15"/>')
a(f'<rect x="{x0}" y="{top}" width="{z:.1f}" height="{H*k:.0f}" fill="{A}" opacity="0.15"/>')
a(f'<rect x="{x0+W*k-z:.1f}" y="{top}" width="{z:.1f}" height="{H*k:.0f}" fill="{A}" opacity="0.15"/>')
# cupboard 85 cm tall
ch=85
a(f'<rect x="{x0}" y="{yb-ch*k:.0f}" width="{W*k:.0f}" height="{ch*k:.0f}" fill="{SG}" stroke="{T}" stroke-width="2"/>')
a(f'<line x1="{x0+W*k/2:.0f}" y1="{yb-ch*k+6:.0f}" x2="{x0+W*k/2:.0f}" y2="{yb-4}" stroke="{T}" stroke-width="2"/>')
a(f'<rect x="{x0-4}" y="{yb-ch*k-8:.0f}" width="{W*k+8:.0f}" height="8" fill="{OAK}"/>')
# shelves at 30 cm spacing above cupboard
ys=[]
y=ch+30
while y< H-25:
    ys.append(y); a(f'<rect x="{x0}" y="{yb-y*k-6:.0f}" width="{W*k:.0f}" height="7" fill="{OAK}"/>'); y+=30
for i in range(len(ys)-1):
    pass
xa=x0+W*k+18
a(f'<line x1="{xa}" y1="{yb-ys[0]*k:.0f}" x2="{xa}" y2="{yb-ys[1]*k:.0f}" stroke="{A}" stroke-width="2"/>')
a(f'<text x="{xa+8}" y="{yb-(ys[0]+15)*k+5:.0f}" font-size="15" font-weight="700" fill="{A}">~30 cm</text>')
a(f'<line x1="{x0}" y1="{yb+22}" x2="{x0+W*k:.0f}" y2="{yb+22}" stroke="{T}" stroke-width="2"/>')
a(f'<text x="{x0+W*k/2:.0f}" y="{yb+46}" font-size="15" font-weight="700" fill="{T}" text-anchor="middle">example: 100 cm wide</text>')
a(f'<text x="{x0+W*k/2:.0f}" y="{yb-ch*k/2:.0f}" font-size="14" fill="#FFFFFF" text-anchor="middle">cupboard</text>')
nx=x0+W*k+100
for j,(t1,t2,c) in enumerate((("Cables may run within","150 mm of ceiling, corners",A),("Shelves 20 to 30 cm","apart for books",OAK),("18 mm MDF sags at","about 600-700 mm",T),("Over 800 mm span?","25 mm board + support",T))):
    yy=top+40+j*92
    a(f'<rect x="{nx}" y="{yy-18}" width="8" height="48" rx="3" fill="{c}"/>')
    a(f'<text x="{nx+18}" y="{yy}" font-size="15" font-weight="700" fill="{T}">{t1}</text>')
    a(f'<text x="{nx+18}" y="{yy+22}" font-size="15" fill="{G}">{t2}</text>')
# right panel depths
px=700
a(f'<rect x="{px}" y="150" width="440" height="610" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="{px+24}" y="190" font-size="21" font-weight="700" fill="{T}">How deep? (mm)</text>')
a(f'<text x="{px+24}" y="216" font-size="15" fill="{G}">Shaded band: typical alcove depth 300-450 mm</text>')
sc=0.45; bx=px+24
a(f'<rect x="{bx+300*sc}" y="232" width="{150*sc}" height="440" fill="{SA}" opacity="0.55"/>')
rows=[("Books",200,250,SG),("Media, storage",300,400,SG),("Drinks cabinet",300,350,SG),("Hanging wardrobe",600,680,A)]
yy=262
for n,l,h,c in rows:
    a(f'<text x="{bx}" y="{yy}" font-size="17" font-weight="700" fill="{T}">{n}</text>')
    a(f'<rect x="{bx}" y="{yy+12}" width="{l*sc}" height="30" rx="5" fill="{c}"/>')
    a(f'<rect x="{bx+l*sc}" y="{yy+12}" width="{(h-l)*sc}" height="30" fill="{c}" opacity="0.5"/>')
    a(f'<text x="{bx+h*sc+10}" y="{yy+34}" font-size="16" font-weight="700" fill="{T}">{l}-{h}</text>')
    yy+=100
a(f'<text x="{bx}" y="{yy+4}" font-size="14" fill="{G}">A wardrobe usually stands proud of the</text>')
a(f'<text x="{bx}" y="{yy+24}" font-size="14" fill="{G}">chimney breast unless the alcove is deep.</text>')
a(f'<text x="60" y="830" font-size="14" fill="{G}">Example layout only; measure your own alcove. Sources: Squote (depths, MDF sag), Bookabuilder and Homebuilding &amp; Renovating (shelf depths),</text>')
a(f'<text x="60" y="852" font-size="14" fill="{G}">Hunker (spacing), FCI London (wardrobe depth), wiring regulations guidance (cable zones).</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
