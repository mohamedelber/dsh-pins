T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#CFDDCB';BG='#F7F1E9';W2='#B98A5E'
s=[];a=s.append
desc=("How to work out baseboard for a 12 by 14 foot room with one door. Add the four walls: 12 + 14 + 12 + 14 = 52 feet. "
"Take off about 3 feet for the doorway: 49 feet. Add 10 percent for waste and cuts: about 54 feet. That is five 12 foot boards.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="bb-t bb-d"><title id="bb-t">How to measure for baseboard</title><desc id="bb-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="84" font-size="44" font-weight="700" fill="{T}">How to Measure for Baseboard</text>')
a(f'<text x="60" y="124" font-size="22" fill="{G}">Example: a 12 x 14 ft room with one door</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
F=30; X0=110; Y0=200; Wd=14*F; H=12*F
a(f'<rect x="{X0}" y="{Y0}" width="{Wd}" height="{H}" fill="#FBF8F3" stroke="{SG}" stroke-width="14"/>')
dx=X0+Wd*0.62; dw=3*F
a(f'<rect x="{dx}" y="{Y0+H-9}" width="{dw}" height="18" fill="#FBF8F3"/><path d="M{dx} {Y0+H} A{dw} {dw} 0 0 1 {dx+dw} {Y0+H-dw}" fill="none" stroke="{G}" stroke-width="2" stroke-dasharray="5 5"/><line x1="{dx+dw}" y1="{Y0+H}" x2="{dx+dw}" y2="{Y0+H-dw}" stroke="{G}" stroke-width="3"/>')
a(f'<text x="{dx+dw/2}" y="{Y0+H+34}" font-size="16" fill="{A}" font-weight="700" text-anchor="middle">door: minus 3 ft</text>')
a(f'<text x="{X0+Wd/2}" y="{Y0-22}" font-size="20" font-weight="700" fill="{T}" text-anchor="middle">14 ft</text>')
a(f'<text x="{X0+Wd/4}" y="{Y0+H+34}" font-size="20" font-weight="700" fill="{T}" text-anchor="middle">14 ft</text>')
a(f'<text x="{X0-22}" y="{Y0+H/2}" font-size="20" font-weight="700" fill="{T}" text-anchor="middle" transform="rotate(-90 {X0-22} {Y0+H/2})">12 ft</text>')
a(f'<text x="{X0+Wd+30}" y="{Y0+H/2}" font-size="20" font-weight="700" fill="{T}" text-anchor="middle" transform="rotate(90 {X0+Wd+30} {Y0+H/2})">12 ft</text>')
a(f'<text x="{X0+Wd/2}" y="{Y0+H/2-6}" font-size="20" fill="#3F5E39" text-anchor="middle">baseboard runs along</text><text x="{X0+Wd/2}" y="{Y0+H/2+22}" font-size="20" fill="#3F5E39" text-anchor="middle">every wall</text>')
# steps on right
sx=640; sy=210
steps=[("1","Add up the walls","12 + 14 + 12 + 14 = 52 ft"),("2","Take off the doorways","52 − 3 = 49 ft"),("3","Add 10% for waste","49 x 1.1 = about 54 ft"),("4","Round up to boards","54 ÷ 12 = 4.5, so buy 5 boards of 12 ft")]
for i,(n,t1,t2) in enumerate(steps):
    y=sy+i*118
    a(f'<rect x="{sx}" y="{y}" width="500" height="96" rx="16" fill="#fff" stroke="#E6DCCF" stroke-width="2"/>')
    a(f'<circle cx="{sx+48}" cy="{y+48}" r="26" fill="{T}"/><text x="{sx+48}" y="{y+57}" font-size="24" font-weight="700" fill="#fff" text-anchor="middle">{n}</text>')
    a(f'<text x="{sx+92}" y="{y+42}" font-size="22" font-weight="700" fill="{T}">{t1}</text><text x="{sx+92}" y="{y+74}" font-size="20" fill="{A}" font-weight="700">{t2}</text>')
a(f'<rect x="110" y="700" width="1030" height="110" rx="16" fill="{SGL}"/>')
a(f'<text x="140" y="744" font-size="21" fill="{T}" font-weight="700">Tip: buy boards as long as your longest wall.</text>')
a(f'<text x="140" y="780" font-size="19" fill="{G}">Cope inside corners, miter outside corners at 45 degrees, and nail into studs about every 16 in.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
