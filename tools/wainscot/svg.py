T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#CFDDCB';BG='#F7F1E9';GD='#3F5E39';PN='#DCE6D8';BT='#B9CBB3'
s=[];a=s.append
desc=("Front view of a 10 ft (120 in) wall with picture frame wainscoting 32 in high, a third of an 8 ft wall: four moulding boxes 26 1/4 in wide and 18 in tall, "
"with 3 in gaps between the boxes, at the corners, under the chair rail and above the baseboard. A card shows the box width formula, the panel width formula for stiles and rails, and common wainscot heights.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="ws-t ws-d"><title id="ws-t">Wainscoting layout guide</title><desc id="ws-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="84" font-size="44" font-weight="700" fill="{T}">Wainscoting Layout</text>')
a(f'<text x="60" y="124" font-size="22" fill="{G}">Equal boxes, equal gaps, a third of the wall</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
W=120;k=5.3;x0=70;fl=720;H=96;Ht=32;g=3;n=4;base=5.5;cap=2.5
bw=(W-(n+1)*g)/n;bh=Ht-cap-base-2*g
def X(i): return x0+i*k
def Y(i): return fl-i*k
a(f'<rect x="{x0}" y="{Y(H)}" width="{W*k}" height="{H*k}" fill="#FBF8F3" stroke="{T}" stroke-width="3"/>')
a(f'<rect x="{x0}" y="{Y(Ht)}" width="{W*k}" height="{Ht*k}" fill="{PN}"/>')
a(f'<rect x="{x0}" y="{Y(base)}" width="{W*k}" height="{base*k}" fill="{BT}" stroke="{SG}" stroke-width="1.5"/>')
a(f'<rect x="{x0-6}" y="{Y(Ht)}" width="{W*k+12}" height="{cap*k}" fill="{SG}"/>')
for i in range(n):
    bx=X(g+i*(bw+g));a(f'<rect x="{bx}" y="{Y(base+g+bh)}" width="{bw*k}" height="{bh*k}" fill="none" stroke="#5E7A57" stroke-width="5"/>')
a(f'<line x1="{x0-20}" y1="{fl}" x2="{x0+W*k+20}" y2="{fl}" stroke="#B98A5E" stroke-width="6"/>')
# gap dim between box 1 and 2 above boxes
gx1=X(g+bw);gx2=X(2*g+bw);gy=Y(Ht)-60
a(f'<line x1="{gx1}" y1="{Y(base+g+bh)}" x2="{gx1}" y2="{gy}" stroke="{A}" stroke-width="1.5" stroke-dasharray="5 4"/><line x1="{gx2}" y1="{Y(base+g+bh)}" x2="{gx2}" y2="{gy}" stroke="{A}" stroke-width="1.5" stroke-dasharray="5 4"/>')
a(f'<text x="{(gx1+gx2)/2}" y="{gy-10}" font-size="20" font-weight="700" fill="{A}" text-anchor="middle">3 in gap</text>')
# box width dim below floor
b1=X(g);b2=X(g+bw);wy=fl+30
a(f'<line x1="{b1}" y1="{wy}" x2="{b2}" y2="{wy}" stroke="{A}" stroke-width="3"/><line x1="{b1}" y1="{wy-10}" x2="{b1}" y2="{wy+10}" stroke="{A}" stroke-width="3"/><line x1="{b2}" y1="{wy-10}" x2="{b2}" y2="{wy+10}" stroke="{A}" stroke-width="3"/>')
a(f'<text x="{(b1+b2)/2}" y="{wy+30}" font-size="19" font-weight="700" fill="{A}" text-anchor="middle">box 26 1/4 in</text>')
a(f'<text x="{X(g+bw/2)}" y="{Y(base+g+bh/2)+7}" font-size="18" font-weight="700" fill="{GD}" text-anchor="middle">18 in tall</text>')
# height dim right
hx=x0+W*k+34
a(f'<line x1="{hx}" y1="{Y(Ht)}" x2="{hx}" y2="{fl}" stroke="{T}" stroke-width="3"/><line x1="{hx-10}" y1="{Y(Ht)}" x2="{hx+10}" y2="{Y(Ht)}" stroke="{T}" stroke-width="3"/><line x1="{hx-10}" y1="{fl}" x2="{hx+10}" y2="{fl}" stroke="{T}" stroke-width="3"/>')
a(f'<text x="{hx-12}" y="{(Y(Ht)+fl)/2}" font-size="18" font-weight="700" fill="{T}" text-anchor="middle" transform="rotate(-90 {hx-12} {(Y(Ht)+fl)/2})">32 in</text>')
a(f'<text x="{x0+W*k-12}" y="{Y(Ht)-14}" font-size="20" font-weight="700" fill="{GD}" text-anchor="end">chair rail at 1/3 of an 8 ft wall</text>')
a(f'<text x="{x0+W*k/2}" y="{fl+100}" font-size="20" font-weight="700" fill="{T}" text-anchor="middle">10 ft wall: 4 boxes, 5 gaps</text>')
# card
tx=800;ty=170
a(f'<rect x="{tx}" y="{ty}" width="350" height="650" rx="18" fill="#fff" stroke="#E6DCCF" stroke-width="2"/>')
a(f'<text x="{tx+24}" y="{ty+44}" font-size="21" font-weight="700" fill="{T}">Picture frame boxes</text>')
for i,l in enumerate(['Box width = (wall','  − (boxes + 1) × gap)','  ÷ boxes']):
    a(f'<text x="{tx+24}" y="{ty+80+i*26}" font-size="17" font-weight="700" fill="{A}" xml:space="preserve">{l}</text>')
a(f'<text x="{tx+24}" y="{ty+170}" font-size="15" fill="{T}">(120 − 5 × 3) ÷ 4 = 26 1/4 in</text>')
a(f'<text x="{tx+24}" y="{ty+226}" font-size="21" font-weight="700" fill="{T}">Raised or flat panels</text>')
for i,l in enumerate(['Panel width = (wall','  − (panels + 1) × stile)','  ÷ panels']):
    a(f'<text x="{tx+24}" y="{ty+262+i*26}" font-size="17" font-weight="700" fill="{A}" xml:space="preserve">{l}</text>')
a(f'<text x="{tx+24}" y="{ty+352}" font-size="15" fill="{T}">1x4 stiles (3 1/2 in), one more</text><text x="{tx+24}" y="{ty+374}" font-size="15" fill="{T}">stile than panels</text>')
a(f'<text x="{tx+24}" y="{ty+430}" font-size="21" font-weight="700" fill="{T}">Height</text>')
for i,(r,v) in enumerate([('8 ft ceiling','32 in'),('9 ft ceiling','36 in'),('Tall','about 2/3'),('Avoid','halfway')]):
    y=ty+470+i*40
    if i%2==0: a(f'<rect x="{tx+12}" y="{y-26}" width="326" height="38" rx="9" fill="{SGL}" fill-opacity="0.5"/>')
    a(f'<text x="{tx+24}" y="{y}" font-size="17" fill="{T}">{r}</text><text x="{tx+326}" y="{y}" font-size="17" font-weight="700" fill="{GD}" text-anchor="end">{v}</text>')
a(f'<text x="{tx+24}" y="{ty+632}" font-size="14" fill="{G}">Add 10% extra moulding for mitres</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
