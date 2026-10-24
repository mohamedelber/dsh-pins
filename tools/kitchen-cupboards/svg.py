T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';W1='#D9B48A';W2='#B98A5E'
s=[];a=s.append
k=0.30; FL=830; X0=150
WT=900; GAP=450; WH=720; WB=WT+GAP; WTOP=WB+WH
def Y(mm): return FL-mm*k
desc=(f"Side view of a standard UK kitchen wall with typical sizes. Worktop at about 900 mm. Base units about 560 mm deep below it. "
f"Wall units start about 450 to 500 mm above the worktop, so their bottom shelf sits at about {WB} to {WT+500} mm, and a 720 mm wall unit reaches about {WTOP} mm. "
"Zone 1, everyday items: top drawers, the worktop and the lowest wall shelf, roughly between waist and shoulder height. "
"Zone 2, heavy and bulky items: base cupboards and deep drawers. Zone 3, rarely used light items: the top wall shelf and above. Cleaning products in a high or locked cupboard away from food.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="kc-t kc-d"><title id="kc-t">Kitchen cupboard zones by height</title><desc id="kc-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="40" font-weight="700" fill="{T}">What Goes Where in Kitchen Cupboards</text>')
a(f'<text x="60" y="118" font-size="22" fill="{G}">Side view of a standard UK kitchen, typical heights in mm</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
WALL=X0+40
a(f'<rect x="{X0}" y="{Y(2250)}" width="40" height="{2250*k}" fill="#E9DFD2"/>')
a(f'<line x1="{X0-20}" y1="{FL}" x2="{X0+330}" y2="{FL}" stroke="{T}" stroke-width="4"/>')
# base unit 560 deep
BD=560*k; WD=300*k
a(f'<rect x="{WALL}" y="{Y(870)}" width="{BD}" height="{(870-100)*k}" fill="{SG}" stroke="{T}" stroke-width="2"/>')
a(f'<rect x="{WALL}" y="{Y(100)}" width="{BD-12}" height="{100*k}" fill="#A9B8A3"/>')
a(f'<rect x="{WALL}" y="{Y(WT)}" width="{BD+20}" height="{30*k}" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
a(f'<line x1="{WALL+4}" y1="{Y(720)}" x2="{WALL+BD-4}" y2="{Y(720)}" stroke="{T}" stroke-width="1.5"/>')
a(f'<line x1="{WALL+4}" y1="{Y(430)}" x2="{WALL+BD-4}" y2="{Y(430)}" stroke="{T}" stroke-width="1.5" stroke-dasharray="4 3"/>')
# wall unit
a(f'<rect x="{WALL}" y="{Y(WTOP)}" width="{WD}" height="{WH*k}" fill="{SGL}" stroke="{T}" stroke-width="2"/>')
for m in (WB+240,WB+480): a(f'<line x1="{WALL+3}" y1="{Y(m)}" x2="{WALL+WD-3}" y2="{Y(m)}" stroke="{T}" stroke-width="1.5"/>')
# zones bands to the right
ZX=WALL+BD+70; ZW=330
def band(lo,hi,col,num,title,lines):
    a(f'<rect x="{ZX}" y="{Y(hi)}" width="{ZW}" height="{(hi-lo)*k}" rx="10" fill="{col}" opacity="0.9"/>')
    a(f'<circle cx="{ZX+28}" cy="{Y(hi)+30}" r="17" fill="{A}"/><text x="{ZX+28}" y="{Y(hi)+36}" font-size="18" font-weight="700" fill="#fff" text-anchor="middle">{num}</text>')
    a(f'<text x="{ZX+56}" y="{Y(hi)+37}" font-size="20" font-weight="700" fill="{T}">{title}</text>')
    for i,l in enumerate(lines): a(f'<text x="{ZX+20}" y="{Y(hi)+66+i*23}" font-size="16" fill="{T}">{l}</text>')
band(WB+480,WTOP+250,'#EFE6DA','3','Rarely used, light',['Top shelf and above:','party glasses, spare jars'])
band(720,WB+480,'#DCE5D6','1','Every day',['Lowest wall shelf, worktop,','top drawers: plates, mugs,','cutlery, oil, everyday food'])
band(0,720,'#ECCDA0','2','Heavy and bulky',['Base cupboards and deep','drawers: pans, mixing bowls,','small appliances, tins'])
# height labels left
def hl(mm,t):
    a(f'<line x1="{X0-14}" y1="{Y(mm)}" x2="{X0}" y2="{Y(mm)}" stroke="{A}" stroke-width="2"/>')
    a(f'<text x="{X0-20}" y="{Y(mm)+6}" font-size="16" font-weight="700" fill="{A}" text-anchor="end">{t}</text>')
hl(WTOP,f'~{WTOP:,}'); hl(WB,f'~{WB:,}'); hl(WT,'~900'); hl(0,'0')
# gap dimension
gx=WALL+WD+26
a(f'<line x1="{gx}" y1="{Y(WB)}" x2="{gx}" y2="{Y(WT)}" stroke="{A}" stroke-width="2"/><line x1="{gx-8}" y1="{Y(WB)}" x2="{gx+8}" y2="{Y(WB)}" stroke="{A}" stroke-width="2"/><line x1="{gx-8}" y1="{Y(WT)}" x2="{gx+8}" y2="{Y(WT)}" stroke="{A}" stroke-width="2"/>')
a(f'<text x="{gx+12}" y="{(Y(WB)+Y(WT))/2+6}" font-size="15" font-weight="700" fill="{A}">450–500</text>')
# depth labels
a(f'<text x="{WALL+BD/2}" y="{FL+26}" font-size="15" fill="{G}" text-anchor="middle">base ~560 deep</text>')
a(f'<text x="{WALL+WD/2}" y="{Y(WTOP)-12}" font-size="15" fill="{G}" text-anchor="middle">wall ~300 deep</text>')
# cleaning note card
cx=ZX+ZW+30
a(f'<rect x="{cx}" y="{Y(WTOP+250)}" width="250" height="230" rx="12" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<rect x="{cx}" y="{Y(WTOP+250)}" width="8" height="230" rx="4" fill="{A}"/>')
for i,l in enumerate(['Cleaning products','','Keep them away from','food, in their original','containers, and high up','or locked if children','visit (RoSPA).']):
    a(f'<text x="{cx+24}" y="{Y(WTOP+250)+36+i*25}" font-size="{19 if i==0 else 16}" font-weight="{700 if i==0 else 400}" fill="{T}">{l}</text>')
a(f'<rect x="{cx}" y="{Y(WTOP+250)+250}" width="250" height="170" rx="12" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<rect x="{cx}" y="{Y(WTOP+250)+250}" width="8" height="170" rx="4" fill="{SG}"/>')
for i,l in enumerate(['Near where you use it','','Mugs by the kettle,','plates by the dishwasher,','spices by the hob.']):
    a(f'<text x="{cx+24}" y="{Y(WTOP+250)+286+i*25}" font-size="{19 if i==0 else 16}" font-weight="{700 if i==0 else 400}" fill="{T}">{l}</text>')
a(f'<text x="60" y="878" font-size="14" fill="{G}">Typical UK sizes from cutmy.co.uk and Worktop Express; your kitchen may differ. Zones follow NHS advice to keep everyday items at waist or worktop level.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
