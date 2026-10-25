T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';OAK='#C9A06B';CR='#FBF7F0'
s=[];a=s.append
desc=("Plan of an example 5 by 8 foot bathroom (40 square feet). A 60 by 30 inch tub runs across the back wall. The toilet and a 24 inch vanity, with its sink centerline 22 inches from the end wall, share the left wall, so all the plumbing is on one wall. "
"The toilet centerline is 18 inches from the tub, the NKBA recommendation (code minimum 15 inches), and there are 32 inches clear in front of the toilet and 39 inches in front of the vanity, above the NKBA's 30 inches (code minimum 21). "
"A 32 inch pocket door on the long wall saves the floor a swinging door would need. Right: code minimums compared with NKBA recommendations, and the fan, outlet and water-efficiency numbers for a small bathroom.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="sb-t sb-d"><title id="sb-t">A 5x8 bathroom, measured</title><desc id="sb-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="42" font-weight="700" fill="{T}">A 5 x 8 Bathroom, Measured</text>')
a(f'<text x="60" y="116" font-size="21" fill="{G}">One plumbing wall, a pocket door and the clearances that matter</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
k=5.8; X=150; Y=170; W=60; D=96
def P(x,y): return X+x*k, Y+y*k
a(f'<rect x="{X}" y="{Y}" width="{W*k}" height="{D*k}" fill="{CR}" stroke="{T}" stroke-width="8"/>')
x0,y0=P(0,0); a(f'<rect x="{x0}" y="{y0}" width="{60*k}" height="{30*k}" fill="#FFFFFF" stroke="{G}" stroke-width="2"/><rect x="{x0+5*k}" y="{y0+4*k}" width="{50*k}" height="{22*k}" rx="40" fill="{SGL}"/>')
a(f'<text x="{x0+30*k}" y="{y0+16*k}" font-size="15" font-weight="700" fill="{T}" text-anchor="middle">Tub 60 x 30 in</text>')
a(f'<line x1="{x0}" y1="{y0+30*k}" x2="{x0+60*k}" y2="{y0+30*k}" stroke="#7FA9C2" stroke-width="5"/>')
# toilet centered y=48, depth 28
tx,ty=P(0,48)
a(f'<rect x="{tx}" y="{ty-9*k}" width="{8*k}" height="{18*k}" fill="#E8E8E8" stroke="{G}"/><ellipse cx="{tx+18*k}" cy="{ty}" rx="{10*k}" ry="{7.5*k}" fill="#FFFFFF" stroke="{G}" stroke-width="2"/>')
a(f'<text x="{tx+12*k}" y="{ty-11*k}" font-size="14" fill="{T}" text-anchor="middle">toilet</text>')
# centerline dim
a(f'<line x1="{tx+30*k}" y1="{Y+30*k}" x2="{tx+30*k}" y2="{ty}" stroke="{A}" stroke-width="2"/><line x1="{tx+2*k}" y1="{ty}" x2="{tx+33*k}" y2="{ty}" stroke="{A}" stroke-width="1.5" stroke-dasharray="4 4"/>')
a(f'<text x="{tx+32*k}" y="{Y+40*k}" font-size="14" font-weight="700" fill="{A}">18 in to</text><text x="{tx+32*k}" y="{Y+43*k}" font-size="14" font-weight="700" fill="{A}">centerline</text>')
# clear in front of toilet 28->60
a(f'<line x1="{tx+28*k}" y1="{ty+12*k}" x2="{X+60*k}" y2="{ty+12*k}" stroke="{A}" stroke-width="2"/><text x="{tx+44*k}" y="{ty+10*k}" font-size="14" font-weight="700" fill="{A}" text-anchor="middle">32 in clear</text>')
# vanity y 68-92 depth 21
vx,vy=P(0,62); a(f'<rect x="{vx}" y="{vy}" width="{21*k}" height="{24*k}" fill="{OAK}"/><ellipse cx="{vx+11*k}" cy="{vy+12*k}" rx="{6*k}" ry="{8*k}" fill="#FFFFFF"/>')
a(f'<text x="{vx+11*k}" y="{vy-8}" font-size="14" fill="{T}" text-anchor="middle">vanity 24 x 21</text>')
a(f'<line x1="{vx+21*k}" y1="{vy+20*k}" x2="{X+60*k}" y2="{vy+20*k}" stroke="{A}" stroke-width="2"/><text x="{vx+40*k}" y="{vy+18*k}" font-size="14" font-weight="700" fill="{A}" text-anchor="middle">39 in clear</text>')
# plumbing wall highlight
a(f'<line x1="{X-14}" y1="{Y}" x2="{X-14}" y2="{Y+D*k}" stroke="{SG}" stroke-width="8"/><text x="{X-26}" y="{Y+D*k/2}" font-size="14" font-weight="700" fill="#4F6B49" text-anchor="middle" transform="rotate(-90 {X-26} {Y+D*k/2})">one plumbing wall</text>')
# pocket door right wall y 58-90
dx,dy=P(60,58); a(f'<rect x="{dx-4}" y="{dy}" width="8" height="{32*k}" fill="{CR}"/><rect x="{dx+8}" y="{dy-32*k+4}" width="8" height="{32*k}" fill="#B0B0B0"/>')
a(f'<text x="{dx+24}" y="{dy+12*k}" font-size="14" font-weight="700" fill="{A}">32 in</text><text x="{dx+24}" y="{dy+15*k}" font-size="14" font-weight="700" fill="{A}">pocket</text><text x="{dx+24}" y="{dy+18*k}" font-size="14" font-weight="700" fill="{A}">door</text>')
a(f'<line x1="{X}" y1="{Y-22}" x2="{X+W*k}" y2="{Y-22}" stroke="{T}" stroke-width="2"/><text x="{X+W*k/2}" y="{Y-30}" font-size="15" font-weight="700" fill="{T}" text-anchor="middle">5 ft (60 in)</text>')
a(f'<text x="{X}" y="{Y+D*k+34}" font-size="15" font-weight="700" fill="{T}">8 ft (96 in) deep: 40 sq ft</text>')
# right panel table
RX=660
a(f'<rect x="{RX}" y="150" width="480" height="560" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="{RX+22}" y="190" font-size="19" font-weight="700" fill="{A}">Code minimum vs NKBA</text>')
a(f'<text x="{RX+300}" y="222" font-size="13" font-weight="700" fill="{G}" text-anchor="middle">Code</text><text x="{RX+410}" y="222" font-size="13" font-weight="700" fill="{G}" text-anchor="middle">NKBA</text>')
rows=[("Clear space in front","21 in","30 in"),("Toilet center to side","15 in","18 in"),("Shower size","30 x 30 in","36 x 36 in"),("Sink center to wall","15 in","20 in"),("Door width","—","32 in")]
for i,(l,c1,c2) in enumerate(rows):
    y=254+i*38
    a(f'<text x="{RX+22}" y="{y}" font-size="15" fill="{T}">{l}</text><text x="{RX+300}" y="{y}" font-size="15" fill="{T}" text-anchor="middle">{c1}</text><text x="{RX+410}" y="{y}" font-size="15" font-weight="700" fill="{A}" text-anchor="middle">{c2}</text><line x1="{RX+22}" y1="{y+14}" x2="{RX+458}" y2="{y+14}" stroke="{BR}"/>')
y=470
a(f'<text x="{RX+22}" y="{y}" font-size="19" font-weight="700" fill="{A}">Also check</text>'); y+=32
for l in ["Fan: 1 CFM per sq ft, 50 CFM minimum","Outlets: GFCI protected","Toilet: WaterSense 1.28 gal per flush","Showerhead: WaterSense 2.0 gal per min","Shower valve: anti-scald, max 120°F","Shower walls: water-resistant to 6 ft"]:
    a(f'<text x="{RX+22}" y="{y}" font-size="15" fill="{T}">• {l}</text>'); y+=30
a(f'<text x="60" y="852" font-size="14" fill="{G}">Example only. Sources: Bob Vila (NKBA and code figures), HVI (fans), EPA WaterSense, NEC 210.8 (GFCI), IRC P2708 (showers). Local codes vary,</text>')
a(f'<text x="60" y="874" font-size="14" fill="{G}">so check with your building department. Layout: our worked example.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
