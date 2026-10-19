import sys
T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';W1='#D9B48A';W2='#B98A5E'
C=int(sys.argv[1]) if len(sys.argv)>1 else 24   # walking space in inches, sides and foot
beds=[("Twin",38,75),("Full",54,75),("Queen",60,80),("King",76,80)]
def ftin(x):
    f=int(x//12); i=int(round(x-f*12))
    if i==12: f+=1; i=0
    return f"{f}'{i}\"" if i else f"{f}'"
s=[];a=s.append
rows=[(n,w,l,w+2*C,l+C) for n,w,l in beds]
desc=("Top-down diagram comparing the smallest guest room for each standard US bed size, with "+str(C)+" inches of walking space on both sides and at the foot of the bed. "
+" ".join(f"{n} bed {w} by {l} inches needs a room about {ftin(rw)} wide by {ftin(rl)} long." for n,w,l,rw,rl in rows)+" Add space for a nightstand, a dresser and the door swing.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="gb-t gb-d"><title id="gb-t">Smallest guest room for each bed size</title><desc id="gb-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">What Bed Fits Your Guest Room?</text>')
a(f'<text x="60" y="128" font-size="22" fill="{G}">The smallest room for each bed size, with {C} in of walking space around it</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
SC=2.3  # px per inch
base=560; x=42
for i,(n,w,l,rw,rl) in enumerate(rows):
    RW=rw*SC; RL=rl*SC
    y=base-RL
    a(f'<rect x="{x}" y="{y}" width="{RW}" height="{RL}" rx="4" fill="#FFFDF9" stroke="{W2}" stroke-width="4"/>')
    # clearance zone
    a(f'<rect x="{x+4}" y="{y+4}" width="{RW-8}" height="{RL-8}" fill="{SGL}" fill-opacity="0.55"/>')
    bx=x+C*SC; by=y
    a(f'<rect x="{bx}" y="{by+2}" width="{w*SC}" height="{l*SC}" rx="8" fill="#fff" stroke="{BR}" stroke-width="2"/>')
    a(f'<rect x="{bx}" y="{by+2}" width="{w*SC}" height="14" rx="6" fill="{W1}"/>')
    pw=min(28,(w*SC-24)/2) if w>45 else w*SC-20
    if w>45:
        a(f'<rect x="{bx+8}" y="{by+22}" width="{(w*SC-24)/2}" height="34" rx="8" fill="{BG}" stroke="{BR}" stroke-width="2"/><rect x="{bx+16+(w*SC-24)/2}" y="{by+22}" width="{(w*SC-24)/2}" height="34" rx="8" fill="{BG}" stroke="{BR}" stroke-width="2"/>')
    else:
        a(f'<rect x="{bx+10}" y="{by+22}" width="{w*SC-20}" height="34" rx="8" fill="{BG}" stroke="{BR}" stroke-width="2"/>')
    a(f'<rect x="{bx}" y="{by+l*SC*0.45}" width="{w*SC}" height="{l*SC*0.55}" rx="6" fill="{SG}" fill-opacity="0.45"/>')
    # labels
    cx=x+RW/2
    a(f'<text x="{cx}" y="{base+40}" font-size="24" font-weight="700" fill="{T}" text-anchor="middle">{n}</text>')
    a(f'<text x="{cx}" y="{base+68}" font-size="17" fill="{G}" text-anchor="middle">bed {w} x {l} in</text>')
    a(f'<rect x="{cx-86}" y="{base+86}" width="172" height="58" rx="12" fill="{A}"/>')
    a(f'<text x="{cx}" y="{base+110}" font-size="15" fill="#fff" text-anchor="middle">room at least</text>')
    a(f'<text x="{cx}" y="{base+134}" font-size="21" font-weight="700" fill="#fff" text-anchor="middle">{ftin(rw)} x {ftin(rl)}</text>')
    if i==3:
        # dimension arrows for clearance on king
        a(f'<line x1="{x+4}" y1="{y+RL-40}" x2="{bx}" y2="{y+RL-40}" stroke="{A}" stroke-width="2"/><text x="{x+C*SC/2}" y="{y+RL-48}" font-size="14" font-weight="700" fill="{A}" text-anchor="middle">{C} in</text>')
        a(f'<line x1="{bx+w*SC/2}" y1="{by+l*SC+2}" x2="{bx+w*SC/2}" y2="{y+RL-4}" stroke="{A}" stroke-width="2"/><text x="{bx+w*SC/2+8}" y="{by+l*SC+C*SC/2+6}" font-size="14" font-weight="700" fill="{A}">{C} in</text>')
    x+=RW+16
a(f'<rect x="60" y="158" width="1080" height="64" rx="14" fill="#fff" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="84" y="198" font-size="19" fill="{T}"><tspan font-weight="700" fill="{A}">Rule of thumb:</tspan> about 10 x 10 ft for a queen; in a smaller room, pick a full or twin, or push the bed to a wall.</text>')
# notes box
a(f'<rect x="60" y="760" width="1080" height="56" rx="12" fill="{SGL}"/>')
a(f'<text x="84" y="795" font-size="18" fill="{T}"><tspan font-weight="700">Add room for:</tspan> a nightstand (about 18 to 24 in wide), a dresser or luggage rack, and the swing of the door.</text>')
a(f'<text x="60" y="852" font-size="15" fill="{G}">Bed size plus {C} in on both sides and at the foot (the Dimensions.com minimum for a queen bedroom, used for all sizes). Headboard against the wall. Standard US mattress sizes.</text>')
a('</svg>')
open('z.svg','w').write('\n'.join(s))
