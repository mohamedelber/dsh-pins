T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';OAK='#C9A06B';CR='#FBF7F0';BLU='#BFD9E6'
s=[];a=s.append
desc=("Plan of an example small ensuite 1.8 by 2.0 metres (3.6 square metres). A 900 by 900 mm shower with a frameless screen sits in one corner, a 600 mm wide by 460 mm deep wall-hung vanity beside it, and the toilet on the side wall. "
"Because there is less than 1.2 m between the toilet pan and the doorway, the door is a 720 mm cavity slider, as the NCC requires a sliding, outward-opening or lift-off door in that case. "
"Right: the rules that apply in Australia: shower walls waterproofed to at least 1800 mm, the whole shower floor waterproofed, the wall behind a vanity water resistant 150 mm above the basin, a 25 litre per second exhaust fan ducted outside, no switches in the electrical zones closest to water, and licensed trades for plumbing, electrical and, in some states, waterproofing.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="se-t se-d"><title id="se-t">A small ensuite, measured</title><desc id="se-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="42" font-weight="700" fill="{T}">A Small Ensuite, Measured</text>')
a(f'<text x="60" y="116" font-size="21" fill="{G}">An example 1.8 x 2.0 m layout and the Australian rules behind it</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
k=0.27; X=130; Y=175; W=1800; D=2000
def P(x,y): return X+x*k, Y+y*k
a(f'<rect x="{X}" y="{Y}" width="{W*k}" height="{D*k}" fill="{CR}" stroke="{T}" stroke-width="8"/>')
# shower top-left 900x900
x0,y0=P(0,0); a(f'<rect x="{x0}" y="{y0}" width="{900*k}" height="{900*k}" fill="{SGL}"/>')
a(f'<line x1="{x0+900*k}" y1="{y0}" x2="{x0+900*k}" y2="{y0+700*k}" stroke="#7FA9C2" stroke-width="5"/>')
a(f'<line x1="{x0}" y1="{y0+900*k}" x2="{x0+900*k}" y2="{y0+900*k}" stroke="{G}" stroke-width="2" stroke-dasharray="6 5"/>')
cx,cy=P(450,450); a(f'<text x="{cx}" y="{cy-6}" font-size="16" font-weight="700" fill="{T}" text-anchor="middle">Shower</text><text x="{cx}" y="{cy+16}" font-size="14" fill="{T}" text-anchor="middle">900 x 900 mm</text>')
nx,ny=P(150,0); a(f'<rect x="{nx}" y="{ny}" width="{600*k}" height="10" fill="#9FC0A0"/><text x="{nx+300*k}" y="{ny+30}" font-size="12" fill="{G}" text-anchor="middle">niche</text>')
# vanity
vx,vy=P(1000,0); a(f'<rect x="{vx}" y="{vy}" width="{600*k}" height="{460*k}" fill="{OAK}"/><ellipse cx="{vx+300*k}" cy="{vy+230*k}" rx="{200*k}" ry="{140*k}" fill="#FFFFFF"/>')
a(f'<text x="{vx+300*k}" y="{vy+460*k+22}" font-size="14" fill="{T}" text-anchor="middle">vanity 600 x 460</text>')
# toilet on right wall
tx,ty=P(W-700,1150); a(f'<rect x="{tx+500*k}" y="{ty}" width="{200*k}" height="{400*k}" fill="#E8E8E8" stroke="{G}"/><ellipse cx="{tx+260*k}" cy="{ty+200*k}" rx="{260*k}" ry="{180*k}" fill="#FFFFFF" stroke="{G}" stroke-width="2"/>')
a(f'<text x="{tx+250*k}" y="{ty-12}" font-size="14" fill="{T}" text-anchor="middle">toilet</text>')
# door bottom wall, cavity slider
dx,dy=P(1000,D); a(f'<rect x="{dx}" y="{dy-4}" width="{720*k}" height="8" fill="{CR}"/>')
a(f'<rect x="{dx-720*k-4}" y="{dy+6}" width="{720*k}" height="8" fill="#B0B0B0"/>')
a(f'<line x1="{dx}" y1="{dy+10}" x2="{dx-720*k}" y2="{dy+10}" stroke="{A}" stroke-width="2" marker-end="url(#ar)"/>')
a(f'<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8z" fill="{A}"/></marker></defs>')
a(f'<text x="{dx+360*k}" y="{dy+40}" font-size="14" font-weight="700" fill="{A}" text-anchor="middle">720 mm cavity slider</text>')
# 1.2 m check: pan front to door
px,py=P(W-520,1550); a(f'<line x1="{px}" y1="{py}" x2="{px}" y2="{Y+D*k-4}" stroke="{A}" stroke-width="2" stroke-dasharray="4 4"/>')
a(f'<text x="{px-10}" y="{py+70}" font-size="13" font-weight="700" fill="{A}" text-anchor="end">under 1.2 m</text><text x="{px-10}" y="{py+88}" font-size="13" fill="{A}" text-anchor="end">to the door</text>')
# dims
a(f'<line x1="{X}" y1="{Y-24}" x2="{X+W*k}" y2="{Y-24}" stroke="{T}" stroke-width="2"/><text x="{X+W*k/2}" y="{Y-32}" font-size="15" font-weight="700" fill="{T}" text-anchor="middle">1.8 m</text>')
a(f'<line x1="{X-24}" y1="{Y}" x2="{X-24}" y2="{Y+D*k}" stroke="{T}" stroke-width="2"/><text x="{X-32}" y="{Y+D*k/2}" font-size="15" font-weight="700" fill="{T}" text-anchor="middle" transform="rotate(-90 {X-32} {Y+D*k/2})">2.0 m</text>')
a(f'<text x="{X}" y="{Y+D*k+80}" font-size="15" font-weight="700" fill="{T}">3.6 m²: within the 3 to 5 m² most Australian ensuites take</text>')
# right panel
RX=720
a(f'<rect x="{RX}" y="150" width="420" height="560" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
y=192
def head(t):
    global y; a(f'<text x="{RX+22}" y="{y}" font-size="18" font-weight="700" fill="{A}">{t}</text>'); y+=28
def line(t):
    global y; a(f'<text x="{RX+22}" y="{y}" font-size="14.5" fill="{T}" xml:space="preserve">{t}</text>'); y+=25
head('Waterproofing (NCC Part 10.2)')
for l in ['• Shower walls: at least 1800 mm up','• The whole shower floor, including any hob','• No screen? Waterstop 1500 mm from the rose','• Vanity wall: 150 mm above the basin']: line(l)
y+=14; head('Air and electrics')
for l in ['• Exhaust fan: 25 L/s, ducted outside','• No window? 10-minute fan run-on','• No switches in zones 0 and 1;','   zone 2 runs 0.6 m out from the shower']: line(l)
y+=14; head('Who does the work')
for l in ['• Licensed plumber and electrician','• NSW: licensed waterproofer over $5,000','• QLD: QBCC waterproofing licence class']: line(l)
y+=14; head('Toilet door (NCC 10.4.2)')
for l in ['• Under 1.2 m from pan to doorway:','   door slides, opens out or lifts off']: line(l)
a(f'<text x="60" y="858" font-size="14" fill="{G}">Example only. Sources: NCC 2022 Housing Provisions, VBA, NSW Government (AS/NZS 3000 zones, waterproofing licence), QBCC, Blueleaf (sizes).</text>')
a(f'<text x="60" y="880" font-size="14" fill="{G}">Layout and fixture positions: our worked example. Check your state’s rules and your certifier before you build.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
