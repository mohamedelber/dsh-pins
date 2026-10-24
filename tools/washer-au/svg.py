T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0'
s=[];a=s.append
desc=("Front loader versus top loader in numbers. Water for a normal cold wash in CHOICE tests of 8 kg machines: front loaders averaged about 56 litres, top loaders about 119 litres. "
"Cycle time: front loaders averaged about 131 minutes, top loaders about 62 minutes. Fastest spin speeds: front loaders up to 1600 rpm, top loaders up to 1100 rpm. "
"Space: a front loader can sit under a benchtop or have a dryer stacked on it, while a top loader needs clear space above for the lid, about 1440 to 1470 mm high with the lid open on one Fisher and Paykel model.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="wa-t wa-d"><title id="wa-t">Front loader vs top loader in numbers</title><desc id="wa-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="42" font-weight="700" fill="{T}">Front Loader vs Top Loader in Numbers</text>')
a(f'<text x="60" y="116" font-size="21" fill="{G}">Typical figures from Australian tests and product guides</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
rows=[('Water per cold wash','litres, CHOICE average, 8 kg machines',56,119,'56 L','119 L',130),
('Cycle time','minutes, CHOICE average',131,62,'131 min','62 min',140),
('Fastest spin speed','rpm, faster spin = shorter drying',1600,1100,'1,600 rpm','1,100 rpm',1700)]
y=170; BX=470; BW=440
for title,sub,f,t,fl,tl,mx in rows:
    a(f'<text x="60" y="{y+20}" font-size="20" font-weight="700" fill="{T}">{title}</text>')
    a(f'<text x="60" y="{y+46}" font-size="15" fill="{G}">{sub}</text>')
    for i,(v,l,col,name) in enumerate(((f,fl,SG,'Front'),(t,tl,A,'Top'))):
        yy=y+i*40
        a(f'<text x="{BX-12}" y="{yy+22}" font-size="16" fill="{T}" text-anchor="end">{name}</text>')
        w=BW*v/mx
        a(f'<rect x="{BX}" y="{yy+4}" width="{w:.1f}" height="26" rx="6" fill="{col}"/>')
        a(f'<text x="{BX+w+10:.1f}" y="{yy+23}" font-size="17" font-weight="700" fill="{T}">{l}</text>')
    y+=130
# space panel
py=570
a(f'<rect x="60" y="{py}" width="1080" height="230" rx="14" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="84" y="{py+38}" font-size="20" font-weight="700" fill="{T}">Space</text>')
# front loader under bench
fx=110; fy=py+70
a(f'<rect x="{fx-20}" y="{fy}" width="200" height="12" fill="#D9B48A"/>')
a(f'<rect x="{fx}" y="{fy+12}" width="120" height="120" rx="6" fill="#FFFFFF" stroke="{T}" stroke-width="2"/><circle cx="{fx+60}" cy="{fy+76}" r="36" fill="{SGL}" stroke="{T}" stroke-width="2"/>')
a(f'<text x="{fx+230}" y="{fy+40}" font-size="17" font-weight="700" fill="{T}">Front loader</text>')
for i,l in enumerate(['Fits under a benchtop','A dryer can stack on top','Loading means bending']):
    a(f'<text x="{fx+230}" y="{fy+68+i*24}" font-size="15" fill="{G}">{l}</text>')
# top loader with lid
tx=640; ty=py+70
a(f'<rect x="{tx}" y="{ty+12}" width="120" height="120" rx="6" fill="#FFFFFF" stroke="{T}" stroke-width="2"/>')
a(f'<line x1="{tx+6}" y1="{ty+12}" x2="{tx+30}" y2="{ty-58}" stroke="{T}" stroke-width="4" stroke-linecap="round"/>')
a(f'<line x1="{tx+150}" y1="{ty-58}" x2="{tx+150}" y2="{ty+132}" stroke="{A}" stroke-width="2"/><line x1="{tx+142}" y1="{ty-58}" x2="{tx+158}" y2="{ty-58}" stroke="{A}" stroke-width="2"/><line x1="{tx+142}" y1="{ty+132}" x2="{tx+158}" y2="{ty+132}" stroke="{A}" stroke-width="2"/>')
a(f'<text x="{tx+166}" y="{ty+40}" font-size="17" font-weight="700" fill="{T}">Top loader</text>')
for i,l in enumerate(['Needs clear space above','Lid open: about 1,440 to','1,470 mm on one F&amp;P model','Loads from above']):
    a(f'<text x="{tx+166}" y="{ty+68+i*24}" font-size="15" fill="{G}">{l}</text>')
a(f'<text x="60" y="842" font-size="14" fill="{G}">Sources: CHOICE test averages (water, time), Appliances Online (spin), Fisher &amp; Paykel WA1068G2 guide (lid height). Individual models vary.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
