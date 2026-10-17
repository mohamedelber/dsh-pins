import re
T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';W1='#D9B48A';W2='#B98A5E';SA='#ECCDA0'
desc=("Three butler's pantry layouts drawn from above with typical sizes. Single wall: one run of 24-inch-deep base cabinets and at least a 36-inch walkway, so the space is about 60 inches, or 5 feet, wide. "
"Galley: cabinets on both walls with a 42-inch work aisle between them, about 90 inches, or 7 and a half feet, wide in total. L-shape: cabinets on two walls meeting in a corner, with the same 42-inch aisle in front. "
"Base cabinets are about 24 inches deep with a 25-inch countertop, and upper cabinets about 12 inches deep. Aisle guidance from the NKBA Kitchen Planning Guidelines.")
s=[];a=s.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" font-family="Poppins, sans-serif" role="img" aria-labelledby="bp-t bp-d"><title id="bp-t">Butler\'s pantry layouts and sizes</title><desc id="bp-d">{desc}</desc>')
a(f'<rect width="1200" height="800" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">Butler\'s Pantry Layouts and Sizes</text>')
a(f'<text x="60" y="130" font-size="22" fill="{G}">Seen from above. Plan the aisle first, then the cabinets.</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
k=3.6
def cab(x,y,w,h): a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{W1}" stroke="{W2}" stroke-width="3"/>')
def wall(x1,y1,x2,y2): a(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{T}" stroke-width="8" stroke-linecap="square"/>')
def dimv(x,y1,y2,lab,side=1):
    a(f'<line x1="{x}" y1="{y1+4}" x2="{x}" y2="{y2-4}" stroke="{A}" stroke-width="3"/>')
    for yy in (y1,y2): a(f'<line x1="{x-10}" y1="{yy}" x2="{x+10}" y2="{yy}" stroke="{A}" stroke-width="3"/>')
    a(f'<text x="{x+14*side}" y="{(y1+y2)/2+6}" font-size="17" font-weight="700" fill="{A}" text-anchor="{"start" if side>0 else "end"}">{lab}</text>')
top=215; L=96*k
# panel 1 single wall: width 60 in drawn vertically (depth direction = y)
x0=80
a(f'<text x="{x0}" y="{top-20}" font-size="24" font-weight="700" fill="{T}">1. Single wall</text>')
wall(x0,top,x0+L*0.75,top)
cab(x0,top+4,L*0.75,24*k)
a(f'<rect x="{x0}" y="{top+4+24*k}" width="{L*0.75}" height="{36*k}" fill="{SGL}" opacity=".6"/>')
a(f'<text x="{x0+L*0.375}" y="{top+4+12*k+6}" font-size="16" fill="{T}" text-anchor="middle">base cabinets</text>')
a(f'<text x="{x0+L*0.375}" y="{top+4+24*k+18*k+6}" font-size="16" fill="{G}" text-anchor="middle">walkway</text>')
wall(x0,top+4+60*k,x0+L*0.75,top+4+60*k)
dimv(x0+L*0.75+22,top+4,top+4+24*k,'24 in')
dimv(x0+L*0.75+22,top+4+24*k,top+4+60*k,'36 in min')
a(f'<text x="{x0}" y="{top+60*k+46}" font-size="18" font-weight="700" fill="{T}">About 5 ft wide</text>')
a(f'<text x="{x0}" y="{top+60*k+70}" font-size="15" fill="{G}">Pass-through between</text><text x="{x0}" y="{top+60*k+90}" font-size="15" fill="{G}">kitchen and dining room</text>')
# panel 2 galley
x0=495
a(f'<text x="{x0}" y="{top-20}" font-size="24" font-weight="700" fill="{T}">2. Galley</text>')
GL=L*0.75
wall(x0,top,x0+GL,top); cab(x0,top+4,GL,24*k)
a(f'<rect x="{x0}" y="{top+4+24*k}" width="{GL}" height="{42*k}" fill="{SGL}" opacity=".6"/>')
cab(x0,top+4+66*k,GL,24*k); wall(x0,top+8+90*k,x0+GL,top+8+90*k)
a(f'<text x="{x0+GL/2}" y="{top+4+45*k+6}" font-size="16" fill="{G}" text-anchor="middle">work aisle</text>')
dimv(x0+GL+22,top+4,top+4+24*k,'24 in')
dimv(x0+GL+22,top+4+24*k,top+4+66*k,'42 in')
dimv(x0+GL+22,top+4+66*k,top+4+90*k,'24 in')
a(f'<text x="{x0}" y="{top+90*k+46}" font-size="18" font-weight="700" fill="{T}">About 7.5 ft wide</text>')
a(f'<text x="{x0}" y="{top+90*k+70}" font-size="15" fill="{G}">Most storage and</text><text x="{x0}" y="{top+90*k+90}" font-size="15" fill="{G}">counter space</text>')
# panel 3 L shape
x0=880
a(f'<text x="{x0}" y="{top-20}" font-size="24" font-weight="700" fill="{T}">3. L-shape</text>')
LL=60*k
wall(x0,top,x0+LL,top); wall(x0,top,x0,top+4+66*k)
cab(x0+4,top+4,LL-4,24*k); cab(x0+4,top+4+24*k,24*k,42*k)
a(f'<rect x="{x0+4+24*k}" y="{top+4+24*k}" width="{LL-4-24*k}" height="{42*k}" fill="{SGL}" opacity=".6"/>')
a(f'<text x="{x0+4+24*k+(LL-4-24*k)/2}" y="{top+4+45*k+6}" font-size="15" fill="{G}" text-anchor="middle">aisle</text>')
dimv(x0+LL+22,top+4+24*k,top+4+66*k,'42 in')
a(f'<text x="{x0}" y="{top+90*k+46}" font-size="18" font-weight="700" fill="{T}">Fits a square room</text>')
a(f'<text x="{x0}" y="{top+90*k+70}" font-size="15" fill="{G}">Corner holds a sink</text><text x="{x0}" y="{top+90*k+90}" font-size="15" fill="{G}">or a coffee station</text>')
cards=[("Base cabinets","24 in deep, 36 in high"),("Upper cabinets","About 12 in deep"),("Aisle","36 in to walk, 42 in to work")]
for i,(t1,t2) in enumerate(cards):
    x=60+i*365
    a(f'<rect x="{x}" y="{top+90*k+112}" width="345" height="62" rx="12" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/><text x="{x+18}" y="{top+90*k+138}" font-size="18" font-weight="700" fill="{T}">{t1}</text><text x="{x+18}" y="{top+90*k+162}" font-size="15" fill="{G}">{t2}</text>')
a(f'<text x="60" y="775" font-size="14" fill="{G}">Aisle widths from the NKBA Kitchen Planning Guidelines (36 in walkway, 42 in work aisle for one cook). Cabinet sizes are typical US stock sizes.</text>')
a('</svg>')
svg=re.sub(r'"([^"]*)"',lambda q:'"'+re.sub(r'(\d+\.\d{2,})',lambda m:str(round(float(m.group(1)),1)),q.group(1))+'"',''.join(s))
open('z.svg','w').write(svg)
