T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';OAK='#C9A06B';CR='#FBF7F0'
s=[];a=s.append
desc=("Left: elevation of a hallway wall 240 cm high, with a dado rail at about one third of the wall height (85 to 100 cm), picture-frame panels below it with 3 to 7 cm gaps, wall lights at 170 to 180 cm and a picture centred at 145 cm. "
"Right: plan of an example 100 cm wide hall. A 30 cm deep console leaves 70 cm, less than the 75 cm pinch-point allowance in Building Regulations guidance for new homes, so a 20 to 25 cm shelf suits halls this narrow. A runner leaving 10 to 13 cm of floor each side is about 74 to 80 cm wide.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="hw-t hw-d"><title id="hw-t">Hallway heights and widths, measured</title><desc id="hw-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="42" font-weight="700" fill="{T}">A Hallway, Measured</text>')
a(f'<text x="60" y="116" font-size="21" fill="{G}">The heights and widths that make hallway ideas work</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
# elevation
k=2.5; x0=80; fl=760; W=120
top=fl-240*k
a(f'<rect x="{x0}" y="{top}" width="{W*k}" height="{240*k}" fill="{CR}" stroke="{T}" stroke-width="3"/>')
d=92
a(f'<rect x="{x0}" y="{fl-d*k}" width="{W*k}" height="{d*k}" fill="{SG}"/>')
a(f'<rect x="{x0}" y="{fl-d*k-5}" width="{W*k}" height="8" fill="#6F8A69"/>')
pw=(W-4*5)/3
for i in range(3):
    px=x0+(5+i*(pw+5))*k
    a(f'<rect x="{px:.0f}" y="{fl-(d-8)*k:.0f}" width="{pw*k:.0f}" height="{(d-20)*k:.0f}" fill="none" stroke="#E9EFE6" stroke-width="3"/>')
# art at 145 centre
ah=40
a(f'<rect x="{x0+W*k/2-40:.0f}" y="{fl-(145+ah/2)*k:.0f}" width="80" height="{ah*k:.0f}" fill="{SA}" stroke="{OAK}" stroke-width="4"/>')
# lights at 175
for lx in (x0+35, x0+W*k-35):
    a(f'<circle cx="{lx}" cy="{fl-175*k:.0f}" r="11" fill="#FFE6B0" stroke="{A}" stroke-width="3"/>')
a(f'<rect x="{x0-10}" y="{fl}" width="{W*k+20}" height="8" fill="#B98A5E"/>')
def dim(h,label,col=A,xx=x0+W*k+20):
    a(f'<line x1="{xx}" y1="{fl}" x2="{xx}" y2="{fl-h*k:.0f}" stroke="{col}" stroke-width="2"/>')
    a(f'<line x1="{xx-6}" y1="{fl-h*k:.0f}" x2="{xx+6}" y2="{fl-h*k:.0f}" stroke="{col}" stroke-width="2"/>')
    a(f'<text x="{xx+12}" y="{fl-h*k+5:.0f}" font-size="15" font-weight="700" fill="{col}">{label}</text>')
dim(92,'Dado rail 85-100 cm (about 1/3)',A,x0+W*k+60)
dim(145,'Picture centre 145 cm',T,x0+W*k+40)
dim(175,'Wall lights 170-180 cm',A,x0+W*k+20)
a(f'<text x="{x0}" y="{fl+36}" font-size="15" fill="{G}">Picture-frame panels: leave 3-7 cm between boxes</text>')
# plan
px=760; py=170
a(f'<rect x="{px-24}" y="150" width="404" height="640" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="{px}" y="190" font-size="21" font-weight="700" fill="{T}">Plan: a 100 cm wide hall</text>')
s2=3.0; hy=230; L=140
a(f'<rect x="{px}" y="{hy}" width="{100*s2}" height="{L*s2}" fill="{CR}" stroke="{T}" stroke-width="3"/>')
a(f'<rect x="{px}" y="{hy+30}" width="{30*s2}" height="{70*s2}" fill="{OAK}"/>')
a(f'<text x="{px+15*s2}" y="{hy+30+35*s2}" font-size="13" fill="{T}" text-anchor="middle" transform="rotate(-90 {px+15*s2} {hy+30+35*s2})">30 cm console</text>')
a(f'<line x1="{px+30*s2}" y1="{hy+L*s2/2-60}" x2="{px+100*s2}" y2="{hy+L*s2/2-60}" stroke="{A}" stroke-width="2"/>')
a(f'<text x="{px+65*s2}" y="{hy+L*s2/2-68}" font-size="15" font-weight="700" fill="{A}" text-anchor="middle">70 cm left</text>')
a(f'<rect x="{px+11*s2}" y="{hy+L*s2-120}" width="{78*s2}" height="100" fill="{SGL}" stroke="{SG}" stroke-width="2"/>')
a(f'<text x="{px+50*s2}" y="{hy+L*s2-64}" font-size="14" fill="{T}" text-anchor="middle">runner ~78 cm wide</text>')
yy=hy+L*s2+40
for j,t in enumerate(("New-home guidance: obstructions such","as radiators may narrow a hall to 750 mm.","Under ~105 cm wide? Use a 20-25 cm shelf.","Runners: leave 10-13 cm of floor each side.")):
    a(f'<text x="{px}" y="{yy+j*22}" font-size="14" fill="{G if j<3 else T}">{t}</text>')
a(f'<text x="60" y="850" font-size="14" fill="{G}">Example only. Sources: Ideal Home (dado height), Orac (panel gaps), Tiffany Lighting Direct (wall lights), Livingetc (57-inch rule),</text>')
a(f'<text x="60" y="872" font-size="14" fill="{G}">Approved Document M (hall widths, new homes), Ruglove (runner gaps). Console depth and walkway: our worked example.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
