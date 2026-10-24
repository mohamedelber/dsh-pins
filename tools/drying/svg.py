T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0'
P=26.32
rows=[('Airer by an open window',0,'0p','no power, slowest'),
('Heat pump tumble dryer',35,'~35p','Which? per load'),
('Heated airer, 6 h',0.3*6*P,None,'300 W, our estimate'),
('Dehumidifier',26*2,'~52p','Which?: 26p per litre, ~2 litres a load'),
('Condenser tumble dryer',89,'~89p','Which? per load')]
s=[];a=s.append
desc=("Estimated cost to dry one load of washing indoors at the Ofgem price cap of 26.32p per kWh (October to December 2026). "
+"; ".join(f"{r[0]}: about {round(r[1])}p" for r in rows)
+". The heated airer cost is our estimate from its wattage and 6 hours; tumble dryer and dehumidifier costs are Which? figures.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="dr-t dr-d"><title id="dr-t">Cost to dry one load indoors</title><desc id="dr-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="42" font-weight="700" fill="{T}">What It Costs to Dry One Load</text>')
a(f'<text x="60" y="116" font-size="21" fill="{G}">At the Ofgem cap of 26.32p per kWh, October to December 2026</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
BX=470; BW=560; MX=95; y=170
for name,c,lab,note in rows:
    lab=lab or f'~{round(c)}p'
    col=SG if c<20 else (SA if c<50 else A)
    a(f'<text x="{BX-16}" y="{y+26}" font-size="19" font-weight="700" fill="{T}" text-anchor="end">{name}</text>')
    a(f'<text x="{BX-16}" y="{y+50}" font-size="14" fill="{G}" text-anchor="end">{note}</text>')
    w=max(BW*c/MX,6)
    a(f'<rect x="{BX}" y="{y+10}" width="{w:.1f}" height="34" rx="8" fill="{col}"/>')
    a(f'<text x="{BX+w+12:.1f}" y="{y+35}" font-size="20" font-weight="700" fill="{T}">{lab}</text>')
    y+=110
a(f'<text x="60" y="800" font-size="15" fill="{G}">Heated airer figure is our estimate: 300 W x 6 hours x 26.32p. Drying times vary with the load, room and weather.</text>')
a(f'<text x="60" y="824" font-size="15" fill="{G}">Tumble dryer and dehumidifier figures from Which?; heated airer wattage from Dunelm.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
for r in rows: print(r[0],round(r[1],1))
