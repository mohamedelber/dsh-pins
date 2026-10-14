import re
T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';W1='#D9B48A';W2='#B98A5E';SA='#ECCDA0'
s=[];a=s.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="br-t br-d"><title id="br-t">Box room layout guide</title><desc id="br-d">Plan view of a typical box room about 2.4 by 2.2 metres. A UK single bed, 90 by 190 centimetres, runs along the long wall under the window side. A walkway of about 60 centimetres is kept beside the bed. A wardrobe about 60 centimetres deep sits in the corner over the stair bulkhead, and the door swings into the room without hitting the bed. For comparison, the Nationally Described Space Standard for new homes in England asks for a single bedroom of at least 7.5 square metres and 2.15 metres wide, so many older box rooms are smaller than that.</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">Box Room Layout Guide</text>')
a(f'<text x="60" y="130" font-size="22" fill="{G}">A typical 2.4 x 2.2 m box room, seen from above</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
k=230; X=110; Y=190; RW=round(2.4*k); RH=round(2.2*k)
# walls
a(f'<rect x="{X}" y="{Y}" width="{RW}" height="{RH}" fill="#FFFDF9" stroke="{T}" stroke-width="10"/>')
# window on top wall
a(f'<rect x="{X+60}" y="{Y-8}" width="{round(1.0*k)}" height="16" fill="#CFE0E8" stroke="{G}" stroke-width="2"/>')
a(f'<text x="{X+60+0.5*k:.0f}" y="{Y-18}" font-size="16" fill="{G}" text-anchor="middle">window</text>')
# bed along left wall, head at top
bw=round(0.9*k); bh=round(1.9*k)
a(f'<rect x="{X+6}" y="{Y+6}" width="{bw}" height="{bh}" rx="8" fill="{SGL}" stroke="{SG}" stroke-width="3"/>')
a(f'<rect x="{X+20}" y="{Y+18}" width="{bw-28}" height="46" rx="10" fill="#FFFFFF" stroke="{SG}" stroke-width="2"/>')
a(f'<text x="{X+6+bw/2:.0f}" y="{Y+bh/2:.0f}" font-size="20" font-weight="700" fill="{T}" text-anchor="middle">Single bed</text><text x="{X+6+bw/2:.0f}" y="{Y+bh/2+26:.0f}" font-size="16" fill="{G}" text-anchor="middle">90 x 190 cm</text>')
# walkway
wx=X+6+bw; ww=round(0.6*k)
a(f'<rect x="{wx}" y="{Y+6}" width="{ww}" height="{RH-12}" fill="{SA}" opacity="0.45"/>')
a(f'<line x1="{wx}" y1="{Y+RH-40}" x2="{wx+ww}" y2="{Y+RH-40}" stroke="{A}" stroke-width="3"/><line x1="{wx}" y1="{Y+RH-52}" x2="{wx}" y2="{Y+RH-28}" stroke="{A}" stroke-width="3"/><line x1="{wx+ww}" y1="{Y+RH-52}" x2="{wx+ww}" y2="{Y+RH-28}" stroke="{A}" stroke-width="3"/>')
a(f'<text x="{wx+ww/2:.0f}" y="{Y+RH/2-10:.0f}" font-size="18" font-weight="700" fill="{A}" text-anchor="middle">60 cm</text><text x="{wx+ww/2:.0f}" y="{Y+RH/2+14:.0f}" font-size="15" fill="{G}" text-anchor="middle">walkway</text>')
# bulkhead + wardrobe top-right
bkw=round(1.0*k); bkd=round(0.6*k); bx=X+RW-6-bkw
a(f'<rect x="{bx}" y="{Y+6}" width="{bkw}" height="{bkd}" fill="{W1}" stroke="{W2}" stroke-width="3"/>')
a(f'<line x1="{bx+bkw/2:.0f}" y1="{Y+6}" x2="{bx+bkw/2:.0f}" y2="{Y+6+bkd}" stroke="{W2}" stroke-width="2"/>')
a(f'<text x="{bx+bkw/2:.0f}" y="{Y+6+bkd/2-4:.0f}" font-size="17" font-weight="700" fill="{T}" text-anchor="middle">Wardrobe</text><text x="{bx+bkw/2:.0f}" y="{Y+6+bkd/2+18:.0f}" font-size="14" fill="{T}" text-anchor="middle">on stair bulkhead</text>')
a(f'<text x="{bx+bkw/2:.0f}" y="{Y+6+bkd+22:.0f}" font-size="15" fill="{G}" text-anchor="middle">about 60 cm deep</text>')
# door bottom-right with swing
dw=round(0.76*k); dx=X+RW-6-dw; dy=Y+RH
a(f'<rect x="{dx}" y="{dy-6}" width="{dw}" height="12" fill="{BG}"/>')
a(f'<line x1="{dx+dw}" y1="{dy}" x2="{dx+dw}" y2="{dy-dw}" stroke="{T}" stroke-width="4"/>')
a(f'<path d="M{dx},{dy} A{dw},{dw} 0 0 1 {dx+dw},{dy-dw}" fill="none" stroke="{G}" stroke-width="2" stroke-dasharray="6 6"/>')
a(f'<text x="{dx+dw/2:.0f}" y="{dy+28}" font-size="16" fill="{G}" text-anchor="middle">door swing</text>')
# dimensions
a(f'<text x="{X+RW/2:.0f}" y="{Y+RH+60}" font-size="18" fill="{T}" text-anchor="middle">2.4 m</text>')
a(f'<text x="{X-24}" y="{Y+RH/2:.0f}" font-size="18" fill="{T}" text-anchor="middle" transform="rotate(-90 {X-24} {Y+RH/2:.0f})">2.2 m</text>')
# right column tips
tips=[("Bed on the long wall","Keeps the middle of the floor clear"),("60 cm to walk","Enough to get in and dress"),("Wardrobe 55 to 60 cm","Deep enough for hangers"),("Check the door","It must open past the bed")]
for i,(t1,t2) in enumerate(tips):
    y=200+i*112
    a(f'<rect x="{X+RW+50}" y="{y}" width="{1140-(X+RW+50)}" height="92" rx="12" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
    a(f'<circle cx="{X+RW+86}" cy="{y+46}" r="18" fill="{T}"/><text x="{X+RW+86}" y="{y+53}" font-size="18" font-weight="700" fill="#FFFFFF" text-anchor="middle">{i+1}</text>')
    a(f'<text x="{X+RW+118}" y="{y+40}" font-size="19" font-weight="700" fill="{T}">{t1}</text><text x="{X+RW+118}" y="{y+68}" font-size="15" fill="{G}">{t2}</text>')
a(f'<text x="60" y="822" font-size="18" fill="{T}"><tspan font-weight="700">Good to know:</tspan> new homes in England aim for single bedrooms of at least 7.5 m² and 2.15 m wide.</text>')
a(f'<text x="60" y="872" font-size="14" fill="{G}">Space standard: Nationally Described Space Standard (GOV.UK, new homes only). Other sizes: common UK sizes and our rule of thumb.</text>')
a('</svg>')
svg=re.sub(r'"([^"]*)"',lambda q:'"'+re.sub(r'(\d+\.\d{2,})',lambda m:str(round(float(m.group(1)),1)),q.group(1))+'"',''.join(s))
open('z.svg','w').write(svg)
