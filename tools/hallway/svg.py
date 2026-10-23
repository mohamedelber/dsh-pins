T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';W1='#D9B48A';W2='#B98A5E'
s=[];a=s.append
k=5.4; X0=70
desc=("Top-down depth budget for narrow hallways. Each bar is a hallway width: 90, 100, 110 and 120 cm. "
"Keeping about 75 cm clear to walk through leaves room for storage on one wall of about 15 cm in a 90 cm hall (hooks, a peg rail or a picture-ledge shelf), "
"about 25 cm in a 100 cm hall (a slim shoe cabinet 17 to 22 cm deep), about 35 cm in a 110 cm hall (a 28 to 30 cm shoe cabinet or a slim console table) "
"and about 45 cm in a 120 cm hall (a storage bench). The 75 cm figure is the narrowest width Approved Document M allows at a short obstruction in new accessible homes, used here as a rule of thumb.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="hw-t hw-d"><title id="hw-t">Hallway storage depth budget</title><desc id="hw-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="44" font-weight="700" fill="{T}">How Deep Can Hallway Storage Be?</text>')
a(f'<text x="60" y="118" font-size="22" fill="{G}">Seen from above: storage on one wall, about 75 cm kept clear to walk</text>')
a(f'<text x="1140" y="50" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
rows=[(90,'Hooks, peg rail, picture-ledge shelf'),(100,'Slim shoe cabinet 17–22 cm deep'),(110,'Shoe cabinet 28–30 cm or slim console'),(120,'Storage bench about 40–45 cm deep')]
y=190; H=96
for w,fit in rows:
    d=w-75
    # wall line
    a(f'<rect x="{X0}" y="{y}" width="12" height="{H}" fill="{W2}"/>')
    a(f'<rect x="{X0+12+w*k}" y="{y}" width="12" height="{H}" fill="{W2}"/>')
    # storage zone
    a(f'<rect x="{X0+12}" y="{y}" width="{d*k}" height="{H}" fill="{A}" opacity="0.85"/>')
    a(f'<text x="{X0+12+d*k/2}" y="{y+H/2+8}" font-size="22" font-weight="700" fill="#fff" text-anchor="middle">{d}</text>')
    # walkway
    a(f'<rect x="{X0+12+d*k}" y="{y}" width="{75*k}" height="{H}" fill="{SGL}" stroke="{SG}" stroke-width="2" stroke-dasharray="7 5"/>')
    a(f'<text x="{X0+12+d*k+75*k/2}" y="{y+H/2+8}" font-size="20" fill="{T}" text-anchor="middle">75 cm clear</text>')
    # width label
    a(f'<text x="{X0+24+w*k+16}" y="{y+40}" font-size="24" font-weight="700" fill="{T}">{w} cm hall</text>')
    a(f'<text x="{X0+24+w*k+16}" y="{y+70}" font-size="17" fill="{G}">{fit}</text>')
    y+=H+42
# legend
ly=y+6
a(f'<rect x="{X0}" y="{ly}" width="28" height="22" fill="{A}" opacity="0.85"/><text x="{X0+40}" y="{ly+18}" font-size="18" fill="{T}">Storage depth (cm) on one wall</text>')
a(f'<rect x="{X0+400}" y="{ly}" width="28" height="22" fill="{SGL}" stroke="{SG}" stroke-width="2" stroke-dasharray="5 4"/><text x="{X0+440}" y="{ly+18}" font-size="18" fill="{T}">Walkway left clear</text>')
a(f'<rect x="{X0+700}" y="{ly}" width="12" height="22" fill="{W2}"/><text x="{X0+724}" y="{ly+18}" font-size="18" fill="{T}">Wall</text>')
a(f'<text x="60" y="866" font-size="14" fill="{G}">75 cm = narrowest point Approved Document M allows at a short obstruction in new accessible homes; a rule of thumb, not a rule for older homes.</text>')
a(f'<text x="60" y="886" font-size="14" fill="{G}">Measure at skirting height, and leave the door swing and any radiator clear. Cabinet depths: IKEA UK listings, October 2026.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
