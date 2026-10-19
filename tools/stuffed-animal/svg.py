T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';W1='#D9B48A';W2='#B98A5E'
s=[];a=s.append
desc=("Diagram of a four-zone system for storing stuffed animals by how often they are played with. Zone 1, bed buddies: one to three favorites on the bed "
"(not for babies under 12 months). Zone 2, play zone: this week's toys in one open basket or storage tower at the child's height. Zone 3, rotation bin: "
"a lidded under-bed or closet bin, swapped every few weeks. Zone 4, keepsake box: clean, dry, labeled and stored indoors, not in the attic. "
"Toys that fit no zone are donated if clean and safe.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="sa-t sa-d"><title id="sa-t">The 4-zone stuffed animal system</title><desc id="sa-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">The 4-Zone Stuffed Animal System</text>')
a(f'<text x="60" y="128" font-size="22" fill="{G}">Store plush toys by how often they are played with, not all in one pile</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
# arrow band
a(f'<rect x="60" y="168" width="1080" height="44" rx="22" fill="{SGL}"/>')
a(f'<text x="90" y="198" font-size="19" font-weight="700" fill="#3F5E39">Played with every day</text>')
a(f'<text x="1110" y="198" font-size="19" font-weight="700" fill="#3F5E39" text-anchor="end">Kept for memories</text>')
a(f'<path d="M420 190 L780 190" stroke="{SG}" stroke-width="4" stroke-dasharray="2 10" stroke-linecap="round"/><path d="M776 180 L792 190 L776 200 Z" fill="{SG}"/>')
def bear(cx,cy,r,col,ear='#fff'):
    a(f'<circle cx="{cx-r*0.72}" cy="{cy-r*0.78}" r="{r*0.36}" fill="{col}"/><circle cx="{cx+r*0.72}" cy="{cy-r*0.78}" r="{r*0.36}" fill="{col}"/>')
    a(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}"/>')
    a(f'<ellipse cx="{cx}" cy="{cy+r*0.28}" rx="{r*0.42}" ry="{r*0.3}" fill="{ear}" fill-opacity="0.75"/>')
    a(f'<circle cx="{cx-r*0.34}" cy="{cy-r*0.15}" r="{r*0.09}" fill="{T}"/><circle cx="{cx+r*0.34}" cy="{cy-r*0.15}" r="{r*0.09}" fill="{T}"/>')
CW=252; GAP=24; X0=60; Y0=240; CH=486
cards=[("1","Bed buddies","1 to 3 favorites","On the bed or a bedside shelf","Not for babies under 12 months"),
("2","Play zone","This week's toys","One basket or tower at kid height","If it does not fit, it rotates"),
("3","Rotation bin","The rest","Lidded bin under the bed or in the closet","Swap a few every 2 to 4 weeks"),
("4","Keepsake box","Sentimental ones","Clean, dry, labeled box indoors","Not in the attic or basement")]
cols=[A,SG,W2,G]
for i,(n,t,s1,s2,s3) in enumerate(cards):
    x=X0+i*(CW+GAP)
    a(f'<rect x="{x}" y="{Y0}" width="{CW}" height="{CH}" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
    a(f'<circle cx="{x+36}" cy="{Y0+38}" r="22" fill="{cols[i]}"/><text x="{x+36}" y="{Y0+46}" font-size="22" font-weight="700" fill="#fff" text-anchor="middle">{n}</text>')
    a(f'<text x="{x+68}" y="{Y0+46}" font-size="24" font-weight="700" fill="{T}">{t}</text>')
    # illustration area
    iy=Y0+80; ih=200
    a(f'<rect x="{x+16}" y="{iy}" width="{CW-32}" height="{ih}" rx="12" fill="#FBF6EF"/>')
    cx=x+CW/2
    if i==0:
        # bed
        a(f'<rect x="{x+34}" y="{iy+60}" width="16" height="120" rx="4" fill="{W2}"/>')
        a(f'<rect x="{x+44}" y="{iy+120}" width="{CW-90}" height="44" rx="8" fill="#FFFDF9" stroke="{BR}" stroke-width="2"/>')
        a(f'<rect x="{x+44}" y="{iy+158}" width="{CW-90}" height="12" fill="{W1}"/>')
        a(f'<rect x="{x+56}" y="{iy+104}" width="58" height="24" rx="10" fill="#fff" stroke="{BR}" stroke-width="2"/>')
        bear(x+140,iy+100,20,SA); bear(x+182,iy+106,15,'#C9D7C4')
    elif i==1:
        # tower with straps
        a(f'<rect x="{cx-70}" y="{iy+20}" width="140" height="168" rx="6" fill="none" stroke="{W2}" stroke-width="8"/>')
        for k in range(5): bear(cx-42+(k%3)*42,iy+60+(k//3)*60,16,[SA,'#C9D7C4','#E8C4B0'][k%3])
        bear(cx-21,iy+158,15,SA); bear(cx+24,iy+156,16,'#E8C4B0')
        for k in range(5):
            xx=cx-56+k*28
            a(f'<line x1="{xx}" y1="{iy+24}" x2="{xx}" y2="{iy+184}" stroke="{SG}" stroke-width="4"/>')
    elif i==2:
        # bed edge with under-bed bin
        a(f'<rect x="{x+30}" y="{iy+40}" width="{CW-60}" height="40" rx="8" fill="#FFFDF9" stroke="{BR}" stroke-width="2"/>')
        a(f'<rect x="{x+30}" y="{iy+80}" width="{CW-60}" height="12" fill="{W1}"/>')
        a(f'<rect x="{x+38}" y="{iy+92}" width="10" height="90" fill="{W2}"/><rect x="{x+CW-48}" y="{iy+92}" width="10" height="90" fill="{W2}"/>')
        a(f'<rect x="{x+56}" y="{iy+120}" width="{CW-90}" height="58" rx="6" fill="#EAF1F5" fill-opacity="0.9" stroke="#9FB3BF" stroke-width="2"/>')
        a(f'<rect x="{x+52}" y="{iy+114}" width="{CW-82}" height="10" rx="4" fill="#C9D6DD"/>')
        for k in range(4): bear(x+82+k*36,iy+152,13,[SA,'#C9D7C4','#E8C4B0',SA][k])
        a(f'<circle cx="{x+70}" cy="{iy+182}" r="5" fill="{G}"/><circle cx="{x+CW-46}" cy="{iy+182}" r="5" fill="{G}"/>')
    else:
        # keepsake box with tissue + label
        a(f'<rect x="{cx-84}" y="{iy+70}" width="168" height="110" rx="6" fill="{W1}"/>')
        a(f'<path d="M{cx-92} {iy+70} L{cx-70} {iy+40} L{cx+70} {iy+40} L{cx+92} {iy+70} Z" fill="{SA}"/>')
        bear(cx-20,iy+64,18,'#E8C4B0'); bear(cx+26,iy+66,15,'#C9D7C4')
        a(f'<path d="M{cx-60} {iy+72} q30 -18 60 0 q30 -18 60 0" fill="none" stroke="#fff" stroke-width="5"/>')
        a(f'<rect x="{cx-44}" y="{iy+108}" width="88" height="40" rx="4" fill="#FFFDF9"/>')
        a(f'<line x1="{cx-32}" y1="{iy+122}" x2="{cx+32}" y2="{iy+122}" stroke="{BR}" stroke-width="3"/><line x1="{cx-32}" y1="{iy+136}" x2="{cx+16}" y2="{iy+136}" stroke="{BR}" stroke-width="3"/>')
    ty=iy+ih+40
    a(f'<text x="{x+20}" y="{ty}" font-size="21" font-weight="700" fill="{cols[i] if i!=1 else "#5E7A57"}">{s1}</text>')
    def wrap(txt,y,size,col,w=26):
        words=txt.split(); line=''; ys=y
        for wd in words:
            if len(line+' '+wd)>w:
                a(f'<text x="{x+20}" y="{ys}" font-size="{size}" fill="{col}">{line.strip()}</text>'); ys+=size+8; line=wd
            else: line+=' '+wd
        a(f'<text x="{x+20}" y="{ys}" font-size="{size}" fill="{col}">{line.strip()}</text>'); return ys
    yy=wrap(s2,ty+36,18,T)
    a(f'<line x1="{x+20}" y1="{yy+22}" x2="{x+CW-20}" y2="{yy+22}" stroke="{BR}" stroke-width="2" stroke-dasharray="4 6"/>')
    wrap(s3,yy+52,17,G,27)
# donate strip
a(f'<rect x="60" y="750" width="1080" height="76" rx="14" fill="{SA}" fill-opacity="0.45" stroke="{W1}" stroke-width="2"/>')
a(f'<text x="90" y="782" font-size="21" font-weight="700" fill="{T}">No zone left? Let it go.</text>')
a(f'<text x="90" y="810" font-size="18" fill="{G}">Donate clean, undamaged toys; throw away worn ones with loose eyes, torn seams or spilling stuffing.</text>')
a(f'<text x="60" y="866" font-size="16" fill="{G}">Zone sizes are our own rule of thumb: let the play zone be one basket or tower, and rotate the rest.</text>')
a('</svg>')
open('z.svg','w').write('\n'.join(s))
