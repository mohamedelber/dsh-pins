T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0'
rows=[
("Sofa and rug zoning","no wall needed",0,3,"None","Low"),
("Row of tall plants","soft, living screen",1,2,"None","Low to medium"),
("Folding screen","moves anywhere",2,1,"None","Low"),
("Open bookcase","storage both sides",1,2,"Anchor it","Medium"),
("Tension rod curtain","renter friendly",3,1,"None","Low"),
("Ceiling track curtain","closes fully",3,1,"Small screws","Low"),
("Slatted partition","airy, modern",1,3,"Fixings or kit","Medium"),
("Glass partition","light, some sound cut",0,3,"Fitted","High"),
("Sliding panels or doors","full closure",3,1,"Fitted","High"),
]
s=[];a=s.append
desc="Comparison of nine room divider ideas by privacy, how much light passes through, whether drilling or fitting is needed and typical cost. "+" ".join(f"{r[0]}: privacy {r[2]} of 3, light {r[3]} of 3, installation {r[4].lower()}, cost {r[5].lower()}." for r in rows)
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="rd-t rd-d"><title id="rd-t">Which room divider is right for you?</title><desc id="rd-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">Which Room Divider?</text>')
a(f'<text x="60" y="128" font-size="22" fill="{G}">Nine ways to divide a room, compared at a glance</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
cx=[60,500,660,820,1000]
hy=185
for x,t,anc in [(cx[0],"Divider","start"),(cx[1]+50,"Privacy","middle"),(cx[2]+50,"Light","middle"),(cx[3]+80,"Drilling","middle"),(cx[4]+70,"Cost","middle")]:
    a(f'<text x="{x}" y="{hy}" font-size="19" font-weight="700" fill="{A}" text-anchor="{anc}">{t}</text>')
a(f'<line x1="60" y1="{hy+14}" x2="1140" y2="{hy+14}" stroke="{BR}" stroke-width="2"/>')
y0=hy+30; rh=68
def dots(x,y,n,col):
    out=''
    for i in range(3):
        f=col if i<n else '#FFFFFF'
        out+=f'<circle cx="{x+20+i*30}" cy="{y}" r="11" fill="{f}" stroke="{col}" stroke-width="2.5"/>'
    return out
for i,(n,sub,pv,lt,dr,co) in enumerate(rows):
    y=y0+i*rh
    if i%2==0: a(f'<rect x="50" y="{y}" width="1100" height="{rh-6}" rx="10" fill="#FFFDF9"/>')
    my=y+(rh-6)/2
    a(f'<text x="70" y="{my-4:.0f}" font-size="21" font-weight="700" fill="{T}">{n}</text>')
    a(f'<text x="70" y="{my+20:.0f}" font-size="15" fill="{G}">{sub}</text>')
    a(dots(cx[1],my,pv,A)); a(dots(cx[2],my,lt,SG))
    colr=SG if dr=="None" else (A if dr=="Fitted" else '#B98A5E')
    a(f'<text x="{cx[3]+80}" y="{my+7:.0f}" font-size="18" font-weight="600" fill="{colr}" text-anchor="middle">{dr}</text>')
    a(f'<text x="{cx[4]+70}" y="{my+7:.0f}" font-size="18" fill="{T}" text-anchor="middle">{co}</text>')
fy=y0+len(rows)*rh+22
a(f'<text x="60" y="{fy}" font-size="15" fill="{G}">Dots: more filled = more privacy or more light. Anchor tall bookcases to a wall, and check building rules before fitting a new partition.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
print(fy)
