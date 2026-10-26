T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';OAK='#C9A06B';OAKD='#A97F4C';CR='#FBF7F0';UN='#E9DFD2'
s=[];a=s.append
desc=("Two cross-sections of a galley-style kitchen with 60 cm deep units on both walls and a 1 metre walkway on each side of an island. "
"A slim 60 cm deep prep island with no seating needs a room about 3.8 metres wide: 60 + 100 + 60 + 100 + 60 cm. "
"A 90 cm deep island with a 30 cm worktop overhang for stools, and 1.2 metres behind the stools, needs about 4.3 metres: 60 + 100 + 90 + 120 + 60 cm. "
"Planning numbers: 1 m walkways, 1.2 m for two cooks or a main route; smallest island about 100 by 100 cm, a butcher's block from 60 cm; worktop 90 cm high, breakfast bar 100 to 110 cm; about 30 cm overhang, more needs support; 60 cm per stool; pendants 70 to 80 cm above the worktop; sockets at least 30 cm from a sink and RCD protected.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="ki-t ki-d"><title id="ki-t">Do you have room for a kitchen island?</title><desc id="ki-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="78" font-size="40" font-weight="700" fill="{T}">Do You Have Room for an Island?</text>')
a(f'<text x="60" y="114" font-size="20" fill="{G}">Room width needed, wall to wall, with 1 m walkways (cm, to scale)</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
k=1.3
def row(Y,title,isl,stool,total,col,walk2=100):
    a(f'<text x="60" y="{Y-18}" font-size="19" font-weight="700" fill="{A}">{title}</text>')
    x=60
    segs=[(60,'units',UN),(100,'1 m walk',SGL),(isl,'island',OAK),(walk2,'1 m walk' if walk2==100 else '1.2 m',SGL),(60,'units',UN)]
    for w,l,c in segs:
        a(f'<rect x="{x}" y="{Y}" width="{w*k}" height="110" fill="{c}" stroke="{G}" stroke-width="1.5"/>')
        if l=='island' and stool:
            a(f'<rect x="{x+60*k}" y="{Y}" width="{30*k}" height="110" fill="#E6C998" stroke="{OAKD}" stroke-dasharray="4 3"/>')
        sub='60 + 30' if (l=='island' and stool) else ('behind stools' if l=='1.2 m' else str(w))
        a(f'<text x="{x+w*k/2}" y="{Y+52}" font-size="14" font-weight="700" fill="{T}" text-anchor="middle">{l}</text><text x="{x+w*k/2}" y="{Y+72}" font-size="12" fill="{G}" text-anchor="middle">{sub}</text>')
        x+=w*k
    a(f'<line x1="60" y1="{Y+128}" x2="{x}" y2="{Y+128}" stroke="{T}" stroke-width="2"/><text x="{(60+x)/2}" y="{Y+152}" font-size="17" font-weight="700" fill="{col}" text-anchor="middle">{total}</text>')
row(180,'Slim prep island, no seating',60,False,'about 3.8 m wide',T)
row(410,'Island with stools on one side (30 cm overhang)',90,True,'about 4.3 m wide',A,120)
a(f'<text x="60" y="640" font-size="15" fill="{T}">Too narrow? A trolley 43 cm deep, a drop-leaf island or a peninsula</text>')
a(f'<text x="60" y="662" font-size="15" fill="{T}">joined to the units needs far less floor.</text>')
RX=700
a(f'<rect x="{RX}" y="150" width="460" height="660" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="{RX+24}" y="190" font-size="21" font-weight="700" fill="{A}">Planning numbers</text>')
rows=[("Walkway","1 m; 1.2 m for two cooks"),("Behind stools","90 cm to 1.2 m"),("Smallest island","about 100 x 100 cm"),("Butcher's block","from 60 cm"),("Worktop height","90 cm"),("Breakfast bar","100–110 cm"),("Stool overhang","about 30 cm, more needs support"),("Per stool","60 cm of worktop"),("Pendants","70–80 cm above the top"),("Sockets","30 cm from a sink, RCD")]
y=232
for l,v in rows:
    a(f'<text x="{RX+24}" y="{y}" font-size="15" font-weight="700" fill="{T}">{l}</text><text x="{RX+180}" y="{y}" font-size="15" fill="{T}">{v}</text><line x1="{RX+24}" y1="{y+16}" x2="{RX+436}" y2="{y+16}" stroke="{BR}"/>')
    y+=56
a(f'<text x="60" y="852" font-size="14" fill="{G}">Example widths are our own sums. Sources: Wren, Harvey Jones, Magnet, Wickes, Homebuilding, Naked Kitchens, DFS, Tala, NICEIC.</text>')
a(f'<text x="60" y="874" font-size="14" fill="{G}">Use our kitchen island size calculator for your own room.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
