T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';W1='#D9B48A';W2='#B98A5E'
s=[]
a=s.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="dt-t dt-d"><title id="dt-t">Small downstairs toilet space guide</title><desc id="dt-d">Plan view of a small downstairs toilet about 800 mm wide and 1400 mm deep. The toilet sits on the back wall, a compact basin is on a side wall, and a clear zone in front of the toilet is at least 500 mm deep and ideally 760 mm. The door opens outwards to save space. Four notes: room size 800 by 1400 mm is comfortable and 700 by 1300 mm is about the smallest; leave 500 to 760 mm in front of the toilet; use a compact or corner basin on a side wall; and add an extractor fan, or for a toilet only, an opening window. A tip says new toilets need ventilation under the Building Regulations and plumbing and electrics need a qualified installer.</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">Downstairs Toilet Space Guide</text>')
a(f'<text x="60" y="130" font-size="22" fill="{G}">What fits in a small cloakroom, seen from above</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
a(f'<rect x="60" y="160" width="600" height="540" rx="16" fill="#FBF6EF" stroke="{BR}" stroke-width="2"/>')
# room 800x1400 at 0.33 px/mm -> 264x462
x0,y0,w,h=228,200,264,462
a(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="#FFFFFF" stroke="{T}" stroke-width="6"/>')
# door gap bottom
a(f'<rect x="{x0+40}" y="{y0+h-4}" width="200" height="8" fill="#FFFFFF"/>')
a(f'<path d="M{x0+40},{y0+h} L{x0+40},{y0+h+26}" stroke="{W2}" stroke-width="4"/>')
a(f'<text x="{x0+140}" y="{y0+h+26}" font-size="15" fill="{G}" text-anchor="middle">door opens outwards</text>')
# concealed cistern ledge back wall
a(f'<rect x="{x0}" y="{y0}" width="{w}" height="40" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
a(f'<text x="{x0+w/2}" y="{y0+26}" font-size="14" fill="{T}" text-anchor="middle">boxed-in cistern + ledge</text>')
# toilet bowl projection ~ 500mm->165px from wall
a(f'<path d="M{x0+92},{y0+40} L{x0+172},{y0+40} L{x0+172},{y0+90} Q{x0+172},{y0+165} {x0+132},{y0+165} Q{x0+92},{y0+165} {x0+92},{y0+90} Z" fill="#FFFFFF" stroke="{G}" stroke-width="3"/>')
a(f'<ellipse cx="{x0+132}" cy="{y0+105}" rx="24" ry="38" fill="{SGL}" stroke="{G}" stroke-width="2"/>')
# clear zone
cz=y0+165
a(f'<rect x="{x0+72}" y="{cz}" width="120" height="251" fill="{A}" fill-opacity="0.08" stroke="{A}" stroke-width="2" stroke-dasharray="7 6"/>')
a(f'<line x1="{x0+72}" y1="{cz+165}" x2="{x0+192}" y2="{cz+165}" stroke="{A}" stroke-width="2"/>')
a(f'<text x="{x0+132}" y="{cz+150}" font-size="14" font-weight="700" fill="{A}" text-anchor="middle">500 mm min</text>')
a(f'<text x="{x0+132}" y="{cz+236}" font-size="14" font-weight="700" fill="{A}" text-anchor="middle">760 mm ideal</text>')
# basin on right side wall
bx=x0+w-83
a(f'<rect x="{bx}" y="{y0+230}" width="83" height="115" rx="12" fill="#FFFFFF" stroke="{G}" stroke-width="3"/>')
a(f'<ellipse cx="{bx+45}" cy="{y0+287}" rx="24" ry="38" fill="{SGL}" stroke="{G}" stroke-width="2"/>')
# dimensions
a(f'<line x1="{x0}" y1="182" x2="{x0+w}" y2="182" stroke="{A}" stroke-width="3"/><line x1="{x0}" y1="172" x2="{x0}" y2="192" stroke="{A}" stroke-width="3"/><line x1="{x0+w}" y1="172" x2="{x0+w}" y2="192" stroke="{A}" stroke-width="3"/>')
a(f'<text x="{x0+w/2}" y="174" font-size="16" font-weight="700" fill="{A}" text-anchor="middle">800 mm</text>')
a(f'<line x1="{x0+w+24}" y1="{y0}" x2="{x0+w+24}" y2="{y0+h}" stroke="{A}" stroke-width="3"/><line x1="{x0+w+14}" y1="{y0}" x2="{x0+w+34}" y2="{y0}" stroke="{A}" stroke-width="3"/><line x1="{x0+w+14}" y1="{y0+h}" x2="{x0+w+34}" y2="{y0+h}" stroke="{A}" stroke-width="3"/>')
a(f'<text x="{x0+w+42}" y="{y0+h/2+6}" font-size="16" font-weight="700" fill="{A}">1400 mm</text>')
# fan symbol top-left corner
a(f'<circle cx="{x0+30}" cy="{y0+70}" r="16" fill="#FFFFFF" stroke="{SG}" stroke-width="3"/><path d="M{x0+30},{y0+58} L{x0+30},{y0+82} M{x0+18},{y0+70} L{x0+42},{y0+70}" stroke="{SG}" stroke-width="2"/>')
# number markers
for n,(cx,cy) in enumerate([(x0-30,y0+h/2),(x0+132,cz+205),(bx+41,y0+212),(x0-30,y0+70)],1):
    a(f'<circle cx="{cx}" cy="{cy}" r="17" fill="{T}"/><text x="{cx}" y="{cy+7}" font-size="18" font-weight="700" fill="#FFFFFF" text-anchor="middle">{n}</text>')
cards=[("Room size","800 × 1400 mm is comfortable."),("Space in front","At least 500 mm, ideally 760 mm."),("Basin","Compact or corner, on a side wall."),("Fresh air","Extractor fan, or an opening window.")]
for i,(t1,t2) in enumerate(cards):
    y=170+i*128
    a(f'<rect x="690" y="{y}" width="450" height="114" rx="14" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
    a(f'<circle cx="728" cy="{y+42}" r="19" fill="{T}"/><text x="728" y="{y+49}" font-size="20" font-weight="700" fill="#FFFFFF" text-anchor="middle">{i+1}</text>')
    a(f'<text x="762" y="{y+50}" font-size="22" font-weight="700" fill="{T}">{t1}</text><text x="762" y="{y+82}" font-size="16" fill="{G}">{t2}</text>')
a(f'<rect x="60" y="730" width="1080" height="100" rx="14" fill="{SGL}" stroke="{SG}" stroke-width="2"/><rect x="60" y="730" width="10" height="100" rx="5" fill="{SG}"/>')
a(f'<text x="96" y="771" font-size="20" fill="{T}"><tspan font-weight="700">Before you build:</tspan> a new toilet needs extract ventilation or, for a</text>')
a(f'<text x="96" y="805" font-size="20" fill="{T}">toilet only, an opening window. Use qualified installers.</text>')
a(f'<text x="60" y="872" font-size="15" fill="{G}">Sizes: Homebuilding &amp; Renovating toilet dimensions guide. Ventilation: Planning Portal (Approved Document F). Measure your own space.</text>')
a('</svg>')
import re
svg=''.join(s)
svg=re.sub(r'(\d+\.\d{2,})',lambda m:str(round(float(m.group(1)),1)),svg)
open('z.svg','w').write(svg)
