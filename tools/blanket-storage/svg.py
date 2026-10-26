T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';OAK='#C9A06B';OAKD='#A97F4C';CR='#FBF7F0';BL='#9DB4C0'
s=[];a=s.append
desc=("Left: measuring under a bed. Two IKEA bed frames list 7 7/8 and 8 1/4 inches of clearance underneath. A 6.3-inch drawer unit and a 7-inch wheeled box fit; a 7 1/2-inch case is tight on the lower frame. Bed risers that add 5 1/4 inches raise an 8 1/4-inch clearance to 13 1/2 inches. "
"Right: inside storage space, calculated from listed dimensions (inside for the ottoman and bench, outside for the soft case): a 32-inch storage ottoman holds about 2.4 cubic feet, a 40-inch storage bench about 3.4, and a 35 1/2-inch under-bed case about 3.2. "
"Bottom: a folded duvet needs 14 to 16 inches between shelves, against a typical fixed 12; the three blanket ladders we checked list load limits from 2.2 pounds per bar to 20 pounds; keep blankets at least 3 feet from space heaters.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="bs-t bs-d"><title id="bs-t">Blanket storage: will it fit?</title><desc id="bs-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="78" font-size="40" font-weight="700" fill="{T}">Blanket Storage: Will It Fit?</text>')
a(f'<text x="60" y="114" font-size="20" fill="{G}">Measure the space first; real product sizes in inches</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
# left panel: under bed
a(f'<rect x="40" y="140" width="580" height="500" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="64" y="180" font-size="20" font-weight="700" fill="{A}">Under the bed</text>')
k=22; FL=560
a(f'<line x1="60" y1="{FL}" x2="600" y2="{FL}" stroke="{T}" stroke-width="3"/>')
def bed(x,w,clr,lab):
    y=FL-clr*k
    a(f'<rect x="{x}" y="{y-34}" width="{w}" height="34" rx="4" fill="{OAK}" stroke="{OAKD}" stroke-width="2"/>')
    a(f'<rect x="{x}" y="{y}" width="12" height="{clr*k}" fill="{OAKD}"/><rect x="{x+w-12}" y="{y}" width="12" height="{clr*k}" fill="{OAKD}"/>')
    a(f'<text x="{x+w/2}" y="{y-44}" font-size="14" font-weight="700" fill="{T}" text-anchor="middle">{lab}</text>')
    return y
y1=bed(70,300,8.25,'IKEA frame: 8 1/4 in clear')
boxes=[(92,6.3,'6.3 in unit','#E9DFD2'),(182,7,'7 in box',BL),(272,7.5,'7 1/2 in case','#B9C9AE')]
for x,h,l,c in boxes:
    a(f'<rect x="{x}" y="{FL-h*k}" width="80" height="{h*k}" rx="4" fill="{c}" stroke="{G}" stroke-width="1.5"/><text x="{x+40}" y="{FL-h*k/2+5}" font-size="12" font-weight="700" fill="{T}" text-anchor="middle">{l}</text>')
a(f'<line x1="385" y1="{y1}" x2="385" y2="{FL}" stroke="{A}" stroke-width="2"/><text x="392" y="{(y1+FL)/2}" font-size="14" font-weight="700" fill="{A}">8 1/4</text>')
# risers bed
y2=bed(440,150,13.5,'+ 5 1/4 in risers')
a(f'<line x1="428" y1="{y2}" x2="428" y2="{FL}" stroke="{A}" stroke-width="2"/><text x="515" y="{(y2+FL)/2}" font-size="15" font-weight="700" fill="{A}" text-anchor="middle">13 1/2 in</text>')
a(f'<text x="64" y="600" font-size="14" fill="{T}">Another IKEA frame lists just 7 7/8 in: the 7 1/2 in case is tight there.</text>')
a(f'<text x="64" y="622" font-size="14" fill="{T}">Measure from the floor to the lowest rail, not to the mattress.</text>')
# right panel: capacity
RX=650
a(f'<rect x="{RX}" y="140" width="510" height="500" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="{RX+24}" y="180" font-size="20" font-weight="700" fill="{A}">Space inside (cubic feet)</text>')
a(f'<text x="{RX+24}" y="204" font-size="13" fill="{G}">From listed sizes: inside for ottoman and bench, outside for the case</text>')
items=[('Storage ottoman, 32 in','28.4 x 12.25 x 11.75 in inside',2.37),('Storage bench, 40 in','37.75 x 15.75 x 9.75 in inside',3.35),('Under-bed case, 35 1/2 in','35.5 x 20.75 x 7.5 in',3.20)]
y=250
for n,d,v in items:
    a(f'<text x="{RX+24}" y="{y}" font-size="16" font-weight="700" fill="{T}">{n}</text><text x="{RX+24}" y="{y+20}" font-size="13" fill="{G}">{d}</text>')
    a(f'<rect x="{RX+24}" y="{y+32}" width="{v*120}" height="28" rx="6" fill="{SG}"/><text x="{RX+34+v*120}" y="{y+52}" font-size="16" font-weight="700" fill="{T}">{v:.1f}</text>')
    y+=118
a(f'<text x="{RX+24}" y="608" font-size="13" fill="{G}">The inside size, not the outside size, decides what fits.</text>')
# bottom strip
TY=665
a(f'<rect x="40" y="{TY}" width="1120" height="140" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
cards=[('14–16 in','between shelves for a','folded duvet (fixed: often 12 in)'),('2.2–20 lb','load limits listed on the','three ladders we checked'),('3 ft','clear between blankets','and any space heater')]
for i,(big,l1,l2) in enumerate(cards):
    x=70+i*370
    a(f'<text x="{x}" y="{TY+58}" font-size="34" font-weight="700" fill="{A}">{big}</text><text x="{x}" y="{TY+90}" font-size="15" fill="{T}">{l1}</text><text x="{x}" y="{TY+112}" font-size="15" fill="{T}">{l2}</text>')
a(f'<text x="60" y="846" font-size="14" fill="{G}">Sources: IKEA US (MALM and NEIDEN frames, SKUBB), Sterilite, Brightroom and Mainstays listings, Target (Linon and HomePop), Closet World,</text>')
a(f'<text x="60" y="868" font-size="14" fill="{G}">Yamazaki, VASAGLE and DecMode listings, U.S. Fire Administration. Checked Oct 26, 2026. Sizes vary by model: measure yours.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
