T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#CFDDCB';BG='#F7F1E9';GD='#3F5E39';PN='#DCE6D8';BT='#B9CBB3'
s=[];a=s.append
desc=("Front view of a 123 1/2 in wide wall with board and batten 60 in high: seven 1x4 battens, 3 1/2 in wide, with a batten in each corner and 16 1/2 in gaps between them, "
"under a 1x4 top rail with a 1x2 ledge, above the baseboard. The formula box shows gap = (wall width minus battens times batten width) divided by (battens minus 1), the actual widths of 1x2 to 1x6 boards and the common 12 to 24 in gap.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="bb-t bb-d"><title id="bb-t">Board and batten spacing guide</title><desc id="bb-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="84" font-size="44" font-weight="700" fill="{T}">Board and Batten Spacing</text>')
a(f'<text x="60" y="124" font-size="22" fill="{G}">Battens in both corners, equal gaps in between</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
W=123.5;k=5.3;x0=70;fl=720;H=96;P=60;b=3.5;n=7;gap=(W-n*b)/(n-1)
def X(i): return x0+i*k
def Y(i): return fl-i*k
a(f'<rect x="{x0}" y="{Y(H)}" width="{W*k}" height="{H*k}" fill="#FBF8F3" stroke="{T}" stroke-width="3"/>')
a(f'<rect x="{x0}" y="{Y(P)}" width="{W*k}" height="{P*k}" fill="{PN}"/>')
a(f'<rect x="{x0}" y="{Y(5.5)}" width="{W*k}" height="{5.5*k}" fill="{BT}" stroke="{SG}" stroke-width="1.5"/>')
a(f'<rect x="{x0}" y="{Y(P)}" width="{W*k}" height="{3.5*k}" fill="{BT}" stroke="{SG}" stroke-width="1.5"/>')
a(f'<rect x="{x0-6}" y="{Y(P)-8}" width="{W*k+12}" height="8" fill="{SG}"/>')
for i in range(n):
    xx=X(i*(b+gap))
    a(f'<rect x="{xx}" y="{Y(P-3.5)}" width="{b*k}" height="{(P-9)*k}" fill="{BT}" stroke="{SG}" stroke-width="1.5"/>')
a(f'<line x1="{x0-20}" y1="{fl}" x2="{x0+W*k+20}" y2="{fl}" stroke="#B98A5E" stroke-width="6"/>')
# gap dimension between battens 1 and 2 inside panel
g1=X(b);g2=X(b+gap);gy=Y(30)
a(f'<line x1="{g1}" y1="{gy}" x2="{g2}" y2="{gy}" stroke="{A}" stroke-width="3"/><line x1="{g1}" y1="{gy-10}" x2="{g1}" y2="{gy+10}" stroke="{A}" stroke-width="3"/><line x1="{g2}" y1="{gy-10}" x2="{g2}" y2="{gy+10}" stroke="{A}" stroke-width="3"/>')
a(f'<text x="{(g1+g2)/2}" y="{gy-38}" font-size="20" font-weight="700" fill="{A}" text-anchor="middle">16 1/2 in</text><text x="{(g1+g2)/2}" y="{gy-16}" font-size="18" font-weight="700" fill="{A}" text-anchor="middle">gap</text>')
# batten width callout on batten 4
bx=X(3*(b+gap));a(f'<line x1="{bx+b*k}" y1="{Y(42)-6}" x2="{bx+b*k+10}" y2="{Y(42)-6}" stroke="{GD}" stroke-width="2"/><text x="{bx+b*k+14}" y="{Y(42)}" font-size="16" font-weight="700" fill="{GD}">1x4</text><text x="{bx+b*k+14}" y="{Y(42)+20}" font-size="14" fill="{GD}">3 1/2 in</text>')
# wall width dimension below floor
wy=fl+34
a(f'<line x1="{x0}" y1="{wy}" x2="{x0+W*k}" y2="{wy}" stroke="{T}" stroke-width="3"/><line x1="{x0}" y1="{wy-10}" x2="{x0}" y2="{wy+10}" stroke="{T}" stroke-width="3"/><line x1="{x0+W*k}" y1="{wy-10}" x2="{x0+W*k}" y2="{wy+10}" stroke="{T}" stroke-width="3"/>')
a(f'<text x="{x0+W*k/2}" y="{wy+32}" font-size="20" font-weight="700" fill="{T}" text-anchor="middle">Wall 123 1/2 in: 7 battens, 6 gaps</text>')
# labels above panel
a(f'<text x="{x0+W*k/2}" y="{Y(P)-22}" font-size="18" font-weight="700" fill="{GD}" text-anchor="middle">1x4 top rail + 1x2 ledge at 60 in</text>')
a(f'<text x="{x0+W*k/2}" y="{Y(2)+5}" font-size="15" font-weight="700" fill="{GD}" text-anchor="middle">baseboard</text>')
# right card
tx=790;ty=170
a(f'<rect x="{tx}" y="{ty}" width="360" height="640" rx="18" fill="#fff" stroke="#E6DCCF" stroke-width="2"/>')
a(f'<text x="{tx+24}" y="{ty+44}" font-size="22" font-weight="700" fill="{T}">The gap formula</text>')
for i,l in enumerate(['Gap = (wall width','  − battens × batten width)','  ÷ (battens − 1)']):
    a(f'<text x="{tx+24}" y="{ty+82+i*28}" font-size="18" font-weight="700" fill="{A}" xml:space="preserve">{l}</text>')
a(f'<text x="{tx+24}" y="{ty+180}" font-size="16" fill="{T}">(123.5 − 7 × 3.5) ÷ 6</text><text x="{tx+24}" y="{ty+206}" font-size="16" font-weight="700" fill="{T}">= 99 ÷ 6 = 16.5 in</text>')
a(f'<text x="{tx+24}" y="{ty+262}" font-size="22" font-weight="700" fill="{T}">Actual board widths</text>')
for i,(nm,wd) in enumerate([('1x2','1 1/2 in (38 mm)'),('1x3','2 1/2 in (64 mm)'),('1x4','3 1/2 in (89 mm)'),('1x6','5 1/2 in (140 mm)')]):
    y=ty+302+i*40
    if i%2==0: a(f'<rect x="{tx+12}" y="{y-26}" width="336" height="38" rx="9" fill="{SGL}" fill-opacity="0.5"/>')
    a(f'<text x="{tx+24}" y="{y}" font-size="17" font-weight="700" fill="{T}">{nm}</text><text x="{tx+336}" y="{y}" font-size="17" font-weight="700" fill="{GD}" text-anchor="end">{wd}</text>')
a(f'<text x="{tx+24}" y="{ty+490}" font-size="22" font-weight="700" fill="{T}">Common gaps</text>')
a(f'<text x="{tx+24}" y="{ty+526}" font-size="17" fill="{T}">12 to 24 in (30 to 60 cm)</text>')
a(f'<text x="{tx+24}" y="{ty+556}" font-size="17" fill="{T}">most popular: 16 to 20 in</text>')
a(f'<text x="{tx+24}" y="{ty+604}" font-size="14" fill="{G}">Add 10% extra boards for cuts</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
