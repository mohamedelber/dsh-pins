T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';W='#D9B48A';WD='#B98A5E';BD='#D8CBBB'
s=[];a=s.append
desc=("Three top-down walk-in pantry plans with 16 inch deep shelves. U-shape: shelves on three walls around a 36 to 48 inch aisle, so the room needs to be at least about 68 inches (5 ft 8 in) wide. "
"Galley: shelves on two facing walls with the same aisle, also about 68 inches wide. Single wall: shelves on one wall only, about 52 inches wide. "
"Notes: 36 inches is the minimum aisle, 42 to 48 inches is more comfortable, 60 inches or more for a wheelchair, and the top shelf should stay within about 69 to 76 inches of reach.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 820" font-family="Poppins, sans-serif" role="img" aria-labelledby="wl-t wl-d"><title id="wl-t">Walk-in pantry layouts and aisle widths</title><desc id="wl-d">{desc}</desc>')
a(f'<rect width="1200" height="820" fill="{BG}"/>')
a(f'<text x="60" y="84" font-size="44" font-weight="700" fill="{T}">Walk-In Pantry Layouts</text>')
a(f'<text x="60" y="124" font-size="22" fill="{G}">Top view with 16 in deep shelves: how wide the room needs to be</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
def panel(x,title,walls,width_in,sub):
    a(f'<rect x="{x}" y="160" width="340" height="470" rx="18" fill="#FFFFFF" stroke="{BD}" stroke-width="2"/>')
    a(f'<text x="{x+170}" y="204" font-size="26" font-weight="700" fill="{T}" text-anchor="middle">{title}</text>')
    k=3.2; rw=width_in*k; rx=x+170-rw/2; ry=240; rh=290
    a(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" fill="#FBF8F3" stroke="{T}" stroke-width="5"/>')
    # door gap at bottom
    a(f'<rect x="{x+170-40}" y="{ry+rh-4}" width="80" height="8" fill="#FBF8F3"/>')
    a(f'<text x="{x+170}" y="{ry+rh+26}" font-size="15" fill="{G}" text-anchor="middle">door</text>')
    d=16*k
    if 'L' in walls: a(f'<rect x="{rx+2.5}" y="{ry+2.5}" width="{d}" height="{rh-5-(0 if walls=="L" else 0)}" fill="{W}" stroke="{WD}" stroke-width="2"/>')
    if 'R' in walls: a(f'<rect x="{rx+rw-2.5-d}" y="{ry+2.5}" width="{d}" height="{rh-5}" fill="{W}" stroke="{WD}" stroke-width="2"/>')
    if 'B' in walls: a(f'<rect x="{rx+2.5}" y="{ry+2.5}" width="{rw-5}" height="{d}" fill="{W}" stroke="{WD}" stroke-width="2"/>')
    # aisle arrow
    ax1=rx+2.5+(d if 'L' in walls else 0); ax2=rx+rw-2.5-(d if 'R' in walls else 0); ay=ry+rh*0.62
    a(f'<line x1="{ax1+6}" y1="{ay}" x2="{ax2-6}" y2="{ay}" stroke="{A}" stroke-width="3"/>')
    a(f'<path d="M{ax1+6},{ay} l12,-8 v16 z M{ax2-6},{ay} l-12,-8 v16 z" fill="{A}"/>')
    a(f'<text x="{(ax1+ax2)/2}" y="{ay-14}" font-size="17" font-weight="700" fill="{A}" text-anchor="middle">36–48 in</text>')
    a(f'<text x="{(ax1+ax2)/2}" y="{ay+28}" font-size="14" fill="{G}" text-anchor="middle">aisle</text>')
    a(f'<text x="{x+170}" y="{ry+rh+62}" font-size="20" font-weight="700" fill="{T}" text-anchor="middle">{sub}</text>')
    a(f'<text x="{x+170}" y="{ry+rh+88}" font-size="15" fill="{G}" text-anchor="middle">wide, with a 36 in aisle</text>')
panel(60,'U-shape','LRB',68,'At least ~68 in')
panel(430,'Galley','LR',68,'At least ~68 in')
panel(800,'Single wall','R',52,'At least ~52 in')
a(f'<rect x="60" y="655" width="1080" height="100" rx="14" fill="{SGL}" stroke="{SG}" stroke-width="2"/>')
a(f'<text x="88" y="696" font-size="19" fill="{T}"><tspan font-weight="700">Aisle:</tspan> 36 in minimum, 42–48 in is more comfortable, 60 in or more for a wheelchair.</text>')
a(f'<text x="88" y="728" font-size="19" fill="{T}"><tspan font-weight="700">Reach:</tspan> keep the top shelf within about 69–76 in of the floor.</text>')
a(f'<text x="60" y="795" font-size="15" fill="{G}">Aisle and reach figures: dimensions.com. Room widths are our estimates: aisle + shelf depth on each shelved side.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
