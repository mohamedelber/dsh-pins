T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0'
LOADS=3*52; YRS=5
opts=[('Heat pump tumble dryer',350,54.32,'£350 to buy (Which?), £54.32 a year'),
('Dehumidifier + airer',234.90,0.26*2*LOADS,'£234.90 (20L compressor), 26p a litre x 2 L a load'),
('Condenser tumble dryer',220,138.91,'£220 to buy (Which?), £138.91 a year')]
rows=[(n,b,r,b+r*YRS,note) for n,b,r,note in opts]
s=[];a=s.append
desc=(f"Estimated five-year cost of drying three loads a week ({LOADS} loads a year). "
+"; ".join(f"{n}: £{b:.0f} to buy plus about £{r:.0f} a year, about £{t:.0f} over five years" for n,b,r,t,_ in rows)
+". Purchase prices and running costs from Which? and retailer listings, October 2026; totals are our estimate.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="dh-t dh-d"><title id="dh-t">Five-year cost of drying laundry</title><desc id="dh-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="42" font-weight="700" fill="{T}">Five Years of Drying, Costed</text>')
a(f'<text x="60" y="116" font-size="21" fill="{G}">Buying price plus running costs, three loads a week</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
X0=380; W=640; MX=950; y=190
for n,b,r,t,note in rows:
    a(f'<text x="60" y="{y+30}" font-size="21" font-weight="700" fill="{T}">{n}</text>')
    a(f'<text x="60" y="{y+58}" font-size="14" fill="{G}">{note}</text>')
    bw=W*b/MX; rw=W*r*YRS/MX
    a(f'<rect x="{X0}" y="{y+80}" width="{bw:.1f}" height="40" rx="6" fill="{SA}"/>')
    a(f'<rect x="{X0+bw:.1f}" y="{y+80}" width="{rw:.1f}" height="40" fill="{SG}"/>')
    a(f'<text x="{X0+bw+rw+14:.1f}" y="{y+108}" font-size="22" font-weight="700" fill="{T}">~£{t:,.0f}</text>')
    y+=180
a(f'<rect x="60" y="{y+10}" width="26" height="20" fill="{SA}"/><text x="96" y="{y+26}" font-size="16" fill="{T}">Price to buy</text>')
a(f'<rect x="260" y="{y+10}" width="26" height="20" fill="{SG}"/><text x="296" y="{y+26}" font-size="16" fill="{T}">Five years of running costs</text>')
a(f'<text x="60" y="830" font-size="14" fill="{G}">Our estimate from Which? running costs at 26.32p per kWh (dryers) and 26p per litre extracted (dehumidifier), and October 2026 prices.</text>')
a(f'<text x="60" y="852" font-size="14" fill="{G}">New condenser dryers cannot be placed on the GB market from 19 January 2027. Prices and energy rates change.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
for n,b,r,t,_ in rows: print(n,round(b),round(r,2),round(t))
