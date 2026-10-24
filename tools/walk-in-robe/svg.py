T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';W1='#D9B48A';W2='#B98A5E'
s=[];a=s.append
k=0.085
D=600; WALK=900
desc=("Top-down plans of four walk-in robe layouts with typical Australian minimum room widths. "
f"Single-sided: one 600 mm deep run of robes plus a 900 mm walkway, about {D+WALK} mm wide. "
f"Galley: robes on both long walls with a 900 mm walkway between, about {D+WALK+D} mm wide. "
"L-shape: robes on two walls meeting in a corner, with the walkway kept clear in front of both. "
"U-shape: robes on three walls, a practical minimum of about 2400 mm wide and about 2600 mm or more to feel comfortable. "
"Shelf-only or shoe sections can be 300 to 450 mm deep, which frees up walkway.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="wr-t wr-d"><title id="wr-t">Walk-in robe layouts and minimum widths</title><desc id="wr-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="42" font-weight="700" fill="{T}">How Wide Does a Walk-In Robe Need to Be?</text>')
a(f'<text x="60" y="116" font-size="21" fill="{G}">Seen from above: 600 mm deep robes, 900 mm walkway, typical sizes in mm</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
def panel(px,py,title,width,label,robes):
    # robes: list of (side) 'L','R','T'(back wall, top)
    L=2400
    ox=px+(250-width*k)/2; oy=py+70
    a(f'<rect x="{px}" y="{py}" width="250" height="330" rx="14" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
    a(f'<text x="{px+125}" y="{py+38}" font-size="21" font-weight="700" fill="{T}" text-anchor="middle">{title}</text>')
    a(f'<rect x="{ox}" y="{oy}" width="{width*k}" height="{L*k}" fill="{SGL}" stroke="{T}" stroke-width="3"/>')
    for r in robes:
        if r=='L': a(f'<rect x="{ox}" y="{oy}" width="{D*k}" height="{L*k}" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
        if r=='R': a(f'<rect x="{ox+width*k-D*k}" y="{oy}" width="{D*k}" height="{L*k}" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
        if r=='T': a(f'<rect x="{ox}" y="{oy}" width="{width*k}" height="{D*k}" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
    # door gap at bottom
    a(f'<rect x="{ox+width*k/2-30}" y="{oy+L*k-3}" width="60" height="6" fill="#FFFFFF"/>')
    a(f'<text x="{ox+width*k/2}" y="{oy+L*k+20}" font-size="13" fill="{G}" text-anchor="middle">door</text>')
    a(f'<text x="{px+125}" y="{py+316}" font-size="19" font-weight="700" fill="{A}" text-anchor="middle">{label}</text>')
panel(60,150,'Single-sided',D+WALK,f'about {D+WALK:,} wide',['L'])
panel(335,150,'Galley',D+WALK+D,f'about {D+WALK+D:,} wide',['L','R'])
panel(610,150,'L-shape',1800,'2,400 x 1,800 room',['L','T'])
panel(885,150,'U-shape',2400,'2,400 to 2,600+',['L','R','T'])
# legend + notes
y=530
a(f'<rect x="60" y="{y}" width="28" height="22" fill="{W1}" stroke="{W2}" stroke-width="2"/><text x="100" y="{y+18}" font-size="18" fill="{T}">Robes, about 600 mm deep for hanging</text>')
a(f'<rect x="520" y="{y}" width="28" height="22" fill="{SGL}" stroke="{T}" stroke-width="2"/><text x="560" y="{y+18}" font-size="18" fill="{T}">Walkway, 900 mm comfortable (800 mm absolute minimum)</text>')
def card(x,yy,w,h,title,lines,col):
    a(f'<rect x="{x}" y="{yy}" width="{w}" height="{h}" rx="12" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/><rect x="{x}" y="{yy}" width="8" height="{h}" rx="4" fill="{col}"/>')
    a(f'<text x="{x+24}" y="{yy+34}" font-size="19" font-weight="700" fill="{T}">{title}</text>')
    for i,l in enumerate(lines): a(f'<text x="{x+24}" y="{yy+64+i*24}" font-size="16" fill="{G}">{l}</text>')
card(60,590,520,160,'Save width with shallow sections',['Shelves only: about 450 mm deep','Shoes and drawers: 300 to 380 mm deep','Hanging needs 520 to 550 mm inside the robe'],SG)
card(620,590,520,160,'Rail heights',['Long hanging: rail at about 1,800 mm','Double hanging: rails at about 1,800 and 900 mm','Shoe shelves: 220 to 260 mm apart'],A)
a(f'<text x="60" y="800" font-size="14" fill="{G}">Widths add the robe depth and walkway: 600 + 900 = 1,500 mm; 600 + 900 + 600 = 2,100 mm. L-shape uses Kitchenfox&#8217;s 2,400 x 1,800 mm minimum room.</text>')
a(f'<text x="60" y="822" font-size="14" fill="{G}">Sources: Silva Wardrobe Co, TNT Wardrobes, Kitchenfox and Houzz Australia. Check your own room before ordering.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
