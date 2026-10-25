T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';OAK='#C9A06B';CR='#FBF7F0';BRK='#B5654A'
s=[];a=s.append
desc=("Left: plan of an example small porch measuring 2.0 by 1.5 metres externally, which is 3 square metres, the most a porch can have under permitted development in England. "
"With single-skin walls about 10 cm thick, the inside is about 1.8 by 1.4 metres, or 2.5 square metres. A bench 40 cm deep sits on one side, coat hooks on the other, and a 60 by 85 cm doormat inside the outer door. "
"Right: the permitted development checks for a porch in England (3 square metres measured externally, no more than 3 metres high, at least 2 metres from a boundary next to a highway, not for flats, maisonettes or where an Article 4 direction or condition applies), "
"when a porch is normally exempt from Building Regulations (ground level, under 30 square metres, front door kept, heating not extended into it, glazing and electrics still comply), and where safety glass is needed.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="po-t po-d"><title id="po-t">A 3 square metre porch, measured</title><desc id="po-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="42" font-weight="700" fill="{T}">A Small Porch, Measured</text>')
a(f'<text x="60" y="116" font-size="21" fill="{G}">What fits in 3 m², and the rules that decide its size</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
k=2.2; X=80; Y=240  # px per cm
W=200; D=150; t=10
# house wall
a(f'<rect x="{X-50}" y="{Y-40}" width="{W*k+100}" height="40" fill="{BRK}"/>')
a(f'<text x="{X+W*k/2}" y="{Y-14}" font-size="15" fill="#FFFFFF" text-anchor="middle" font-weight="700">HOUSE WALL</text>')
# porch walls
a(f'<rect x="{X}" y="{Y}" width="{W*k}" height="{D*k}" fill="{BRK}"/>')
a(f'<rect x="{X+t*k}" y="{Y}" width="{(W-2*t)*k}" height="{(D-t)*k}" fill="{CR}"/>')
# front door (house) gap
hx=X+(W/2-42)*k; a(f'<rect x="{hx}" y="{Y-40}" width="{84*k}" height="40" fill="#E8D9C4"/>')
a(f'<text x="{hx+42*k}" y="{Y-50}" font-size="14" fill="{T}" text-anchor="middle">front door stays</text>')
# outer door gap bottom
ox=X+(W/2-42)*k; oy=Y+(D-t)*k
a(f'<rect x="{ox}" y="{oy}" width="{84*k}" height="{t*k}" fill="#BFD9E6" stroke="{T}" stroke-width="1"/>')
a(f'<text x="{ox+42*k}" y="{oy+t*k+22}" font-size="14" fill="{T}" text-anchor="middle">glazed outer door</text>')
# doormat
mx=X+(W/2-42.5)*k; my=oy-60*k
a(f'<rect x="{mx}" y="{my}" width="{85*k}" height="{60*k}" fill="#D9B98A" stroke="#A9895A" stroke-width="2"/>')
a(f'<text x="{mx+42.5*k}" y="{my+30*k+5}" font-size="14" fill="{T}" text-anchor="middle">mat 60 x 85 cm</text>')
# bench left
bx=X+t*k; by=Y+20*k
a(f'<rect x="{bx}" y="{by}" width="{40*k}" height="{100*k}" fill="{OAK}"/>')
a(f'<text x="{bx+20*k}" y="{by+50*k}" font-size="14" fill="{T}" text-anchor="middle" transform="rotate(-90 {bx+20*k} {by+50*k})">bench 40 cm deep</text>')
# hooks right
for i in range(4):
    hy=Y+(25+i*18)*k; a(f'<circle cx="{X+(W-t)*k-8}" cy="{hy}" r="6" fill="{T}"/>')
a(f'<text x="{X+(W-t)*k-20}" y="{Y+50*k}" font-size="14" fill="{T}" text-anchor="end" transform="rotate(-90 {X+(W-t)*k-20} {Y+50*k})">coat hooks</text>')
# dims
def dh(x1,x2,y,lab,col=A):
    a(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{col}" stroke-width="2"/>')
    for xx in (x1,x2): a(f'<line x1="{xx}" y1="{y-6}" x2="{xx}" y2="{y+6}" stroke="{col}" stroke-width="2"/>')
    a(f'<text x="{(x1+x2)/2}" y="{y+22}" font-size="15" font-weight="700" fill="{col}" text-anchor="middle">{lab}</text>')
def dv(x,y1,y2,lab,col=A):
    a(f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{col}" stroke-width="2"/>')
    for yy in (y1,y2): a(f'<line x1="{x-6}" y1="{yy}" x2="{x+6}" y2="{yy}" stroke="{col}" stroke-width="2"/>')
    a(f'<text x="{x+12}" y="{(y1+y2)/2+5}" font-size="15" font-weight="700" fill="{col}">{lab}</text>')
dh(X,X+W*k,Y+D*k+52,'2.0 m outside')
dv(X+W*k+20,Y,Y+D*k,'1.5 m outside')
dh(X+t*k,X+(W-t)*k,Y+D*k+100,'about 1.8 m inside',G)
a(f'<rect x="{X}" y="{Y+D*k+140}" width="{W*k}" height="70" rx="10" fill="{SGL}"/>')
a(f'<text x="{X+W*k/2}" y="{Y+D*k+170}" font-size="17" font-weight="700" fill="{T}" text-anchor="middle">3.0 m² outside = about 2.5 m² inside</text>')
a(f'<text x="{X+W*k/2}" y="{Y+D*k+195}" font-size="14" fill="{G}" text-anchor="middle">The 3 m² limit is measured externally, so walls eat into it.</text>')
# right panel
RX=690
a(f'<rect x="{RX}" y="150" width="450" height="660" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
y=190
def head(t_):
    global y; a(f'<text x="{RX+24}" y="{y}" font-size="19" font-weight="700" fill="{A}">{t_}</text>'); y+=30
def line(t_,b=False):
    global y; a(f'<text x="{RX+24}" y="{y}" font-size="15" fill="{T}" xml:space="preserve">{t_}</text>'); y+=27
head('No planning permission (England) if:')
for l in ['✓ 3 m² or less, measured outside','✓ no part higher than 3 m','✓ 2 m or more from a boundary next','   to a highway (a road or public path)','✓ a house, not a flat or maisonette','✓ no Article 4 direction or condition','Listed building? Consent still needed.']: line(l)
y+=22; head('Building Regs: normally exempt if:')
for l in ['✓ at ground level and under 30 m²','✓ the front door stays in place','✓ house heating not extended into it','Glazing and fixed wiring must still comply.']: line(l)
y+=22; head('Safety glass needed:')
for l in ['• in doors, below 1500 mm','• within 300 mm of a door edge','• other glazing below 800 mm']: line(l)
a(f'<text x="60" y="850" font-size="14" fill="{G}">Example only. Sources: Planning Portal and legislation.gov.uk (Class D), Planning Portal (Building Regulations), gov.uk circular on porches,</text>')
a(f'<text x="60" y="872" font-size="14" fill="{G}">Lancaster City Council (safety glass), First Mats (mat size). Wall thickness and inside size: our worked example. Wales has the same limits.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
