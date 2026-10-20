T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#CFDDCB';BG='#F7F1E9';W1='#D9B48A';W2='#B98A5E';Y='#E9C46A';GD='#3F5E39'
s=[];a=s.append
desc=("Side view of a room with an 8 ft ceiling and three recessed lights. The lights are 4 ft apart, half the ceiling height, and the first light is 2 ft from the wall, half the spacing, "
"so the cones of light meet evenly on the floor. A table shows the spacing and wall distance for 8, 9, 10 and 12 ft ceilings and how many lumens per square foot each room needs.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="rl-t rl-d"><title id="rl-t">Recessed lighting spacing guide</title><desc id="rl-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="84" font-size="44" font-weight="700" fill="{T}">Recessed Lighting Spacing</text>')
a(f'<text x="60" y="124" font-size="22" fill="{G}">Half the ceiling height apart, half that from the walls</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
k=50; x0=110; ce=270; fl=ce+8*k; xr=x0+12*k
# room section
a(f'<rect x="{x0}" y="{ce}" width="{12*k}" height="{8*k}" fill="#fff"/>')
lights=[x0+2*k,x0+6*k,x0+10*k]
a(f'<clipPath id="rl-c"><rect x="{x0}" y="{ce}" width="{12*k}" height="{8*k}"/></clipPath><g clip-path="url(#rl-c)">')
for lx in lights:
    a(f'<polygon points="{lx-10},{ce+8} {lx+10},{ce+8} {lx+2.25*k},{fl} {lx-2.25*k},{fl}" fill="{Y}" fill-opacity="0.28"/>')
a('</g>')
a(f'<line x1="{x0-20}" y1="{ce}" x2="{xr+20}" y2="{ce}" stroke="{T}" stroke-width="6"/>')
a(f'<line x1="{x0-20}" y1="{fl}" x2="{xr+20}" y2="{fl}" stroke="{W2}" stroke-width="6"/>')
a(f'<line x1="{x0}" y1="{ce}" x2="{x0}" y2="{fl}" stroke="{T}" stroke-width="6"/><line x1="{xr}" y1="{ce}" x2="{xr}" y2="{fl}" stroke="{T}" stroke-width="6"/>')
for lx in lights:
    a(f'<rect x="{lx-16}" y="{ce}" width="32" height="9" rx="3" fill="{Y}" stroke="{W2}" stroke-width="2"/>')
# simple furniture: sofa and table silhouettes
a(f'<rect x="{x0+40}" y="{fl-70}" width="190" height="70" rx="14" fill="{SGL}"/><rect x="{x0+40}" y="{fl-110}" width="40" height="110" rx="12" fill="{SGL}"/>')
a(f'<rect x="{x0+330}" y="{fl-48}" width="150" height="10" rx="3" fill="{W1}"/><line x1="{x0+345}" y1="{fl-38}" x2="{x0+345}" y2="{fl}" stroke="{W2}" stroke-width="6"/><line x1="{x0+465}" y1="{fl-38}" x2="{x0+465}" y2="{fl}" stroke="{W2}" stroke-width="6"/>')
# dimensions above ceiling
dy=ce-34
def dim(x1,x2,y,col,t,dash=False):
    d=' stroke-dasharray="8 6"' if dash else ''
    a(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{col}" stroke-width="3"{d}/><line x1="{x1}" y1="{y-10}" x2="{x1}" y2="{y+10}" stroke="{col}" stroke-width="3"/><line x1="{x2}" y1="{y-10}" x2="{x2}" y2="{y+10}" stroke="{col}" stroke-width="3"/>')
    a(f'<text x="{(x1+x2)/2}" y="{y-16}" font-size="20" font-weight="700" fill="{col}" text-anchor="middle">{t}</text>')
dim(x0,lights[0],dy,GD,'2 ft',True)
dim(lights[0],lights[1],dy,A,'4 ft apart')
dim(lights[1],lights[2],dy,A,'4 ft apart')
dim(lights[2],xr,dy,GD,'2 ft',True)
# ceiling height dimension on the left
hx=x0-50
a(f'<line x1="{hx}" y1="{ce}" x2="{hx}" y2="{fl}" stroke="{T}" stroke-width="3"/><line x1="{hx-10}" y1="{ce}" x2="{hx+10}" y2="{ce}" stroke="{T}" stroke-width="3"/><line x1="{hx-10}" y1="{fl}" x2="{hx+10}" y2="{fl}" stroke="{T}" stroke-width="3"/>')
a(f'<text x="{hx-14}" y="{(ce+fl)/2}" font-size="20" font-weight="700" fill="{T}" text-anchor="middle" transform="rotate(-90 {hx-14} {(ce+fl)/2})">8 ft ceiling</text>')
a(f'<text x="{x0+6*k}" y="{fl+46}" font-size="21" font-weight="700" fill="{A}" text-anchor="middle">Spacing = ceiling height ÷ 2</text>')
a(f'<text x="{x0+6*k}" y="{fl+76}" font-size="21" font-weight="700" fill="{GD}" text-anchor="middle">Wall distance = spacing ÷ 2</text>')
a(f'<text x="{x0+6*k}" y="{fl+106}" font-size="17" fill="{G}" text-anchor="middle">so the cones of light meet evenly</text>')
# table card
tx=790; ty=190
a(f'<rect x="{tx}" y="{ty}" width="360" height="610" rx="18" fill="#fff" stroke="#E6DCCF" stroke-width="2"/>')
a(f'<text x="{tx+24}" y="{ty+44}" font-size="22" font-weight="700" fill="{T}">Spacing by ceiling</text>')
a(f'<text x="{tx+24}" y="{ty+80}" font-size="15" font-weight="700" fill="{G}">Ceiling</text><text x="{tx+130}" y="{ty+80}" font-size="15" font-weight="700" fill="{G}">Apart</text><text x="{tx+236}" y="{ty+80}" font-size="15" font-weight="700" fill="{G}">To wall</text>')
rows=[('8 ft','4 ft','2 ft'),('9 ft','4 ft 6 in','2 ft 3 in'),('10 ft','5 ft','2 ft 6 in'),('12 ft','6 ft','3 ft')]
for i,(c,ap,w) in enumerate(rows):
    y=ty+120+i*48
    if i%2==0: a(f'<rect x="{tx+12}" y="{y-30}" width="336" height="44" rx="10" fill="{SGL}" fill-opacity="0.5"/>')
    a(f'<text x="{tx+24}" y="{y}" font-size="17" font-weight="700" fill="{T}">{c}</text><text x="{tx+130}" y="{y}" font-size="17" font-weight="700" fill="{A}">{ap}</text><text x="{tx+236}" y="{y}" font-size="17" font-weight="700" fill="{GD}">{w}</text>')
a(f'<text x="{tx+24}" y="{ty+350}" font-size="22" font-weight="700" fill="{T}">Light per room</text>')
a(f'<text x="{tx+24}" y="{ty+378}" font-size="14" fill="{G}">lumens per sq ft</text>')
rr=[('Hallway','5 to 10'),('Living, bedroom','10 to 20'),('Kitchen, dining','30 to 40'),('Bathroom','20 to 50+')]
for i,(r,v) in enumerate(rr):
    y=ty+418+i*42
    a(f'<text x="{tx+24}" y="{y}" font-size="17" fill="{T}">{r}</text><text x="{tx+336}" y="{y}" font-size="17" font-weight="700" fill="{A}" text-anchor="end">{v}</text>')
a(f'<text x="{tx+24}" y="{ty+590}" font-size="14" fill="{G}">Room area x lumens = total light</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
