T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0'
PRICE=0.1834; YRS=12
chest_kwh,up_kwh=215,395
cy,uy=chest_kwh*PRICE,up_kwh*PRICE
s=[];a=s.append
desc=(f"Left: floor footprint from above of a 7 cubic foot chest freezer, about 37.5 by 21.75 inches, and a 13 cubic foot upright freezer, about 27.75 by 23 inches. "
f"Right: electricity cost over a 12-year life at the US average residential price of 18.34 cents per kWh (June 2026): ENERGY STAR chest freezer about {chest_kwh} kWh a year, about ${cy:.0f} a year or ${cy*YRS:,.0f} over 12 years; "
f"ENERGY STAR upright about {up_kwh} kWh a year, about ${uy:.0f} a year or ${uy*YRS:,.0f} over 12 years.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="fz-t fz-d"><title id="fz-t">Chest vs upright freezer: space and running cost</title><desc id="fz-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="42" font-weight="700" fill="{T}">Chest vs Upright Freezer, Measured</text>')
a(f'<text x="60" y="116" font-size="21" fill="{G}">Floor space from above, and 12 years of electricity</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
k=7.5
# panel left
a(f'<rect x="60" y="150" width="500" height="600" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="84" y="190" font-size="21" font-weight="700" fill="{T}">Floor space (inches)</text>')
cx,cy0=100,240
a(f'<rect x="{cx}" y="{cy0}" width="{37.5*k}" height="{21.75*k}" rx="8" fill="{SGL}" stroke="{SG}" stroke-width="3"/>')
a(f'<text x="{cx+37.5*k/2}" y="{cy0+21.75*k/2+2}" font-size="17" font-weight="700" fill="{T}" text-anchor="middle">7 cu ft chest</text>')
a(f'<text x="{cx+37.5*k/2}" y="{cy0+21.75*k/2+24}" font-size="14" fill="{G}" text-anchor="middle">37.5 x 21.75 in</text>')
ux,uy0=100,450
a(f'<rect x="{ux}" y="{uy0}" width="{27.75*k}" height="{23.125*k}" rx="8" fill="{SA}" stroke="#B98A5E" stroke-width="3"/>')
a(f'<text x="{ux+27.75*k/2}" y="{uy0+23.125*k/2+2}" font-size="17" font-weight="700" fill="{T}" text-anchor="middle">13 cu ft upright</text>')
a(f'<text x="{ux+27.75*k/2}" y="{uy0+23.125*k/2+24}" font-size="14" fill="{G}" text-anchor="middle">27.75 x 23 in</text>')
a(f'<text x="{ux+27.75*k+20}" y="{uy0+60}" font-size="15" fill="{G}">Almost twice the</text>')
a(f'<text x="{ux+27.75*k+20}" y="{uy0+82}" font-size="15" fill="{G}">space inside, on</text>')
a(f'<text x="{ux+27.75*k+20}" y="{uy0+104}" font-size="15" fill="{G}">a smaller footprint</text>')
a(f'<text x="84" y="725" font-size="14" fill="{G}">Allow about 3 in on all sides (Frigidaire spec sheets)</text>')
# panel right bars
a(f'<rect x="600" y="150" width="540" height="600" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="624" y="190" font-size="21" font-weight="700" fill="{T}">12 years of electricity</text>')
a(f'<text x="624" y="216" font-size="15" fill="{G}">ENERGY STAR models at 18.34¢ per kWh</text>')
BX=624; BW=440; MX=900
for i,(name,kwh,yr,col) in enumerate((('Chest',chest_kwh,cy,SG),('Upright',up_kwh,uy,A))):
    yy=290+i*200
    a(f'<text x="{BX}" y="{yy}" font-size="20" font-weight="700" fill="{T}">{name}: about {kwh} kWh a year</text>')
    a(f'<text x="{BX}" y="{yy+26}" font-size="15" fill="{G}">about ${yr:.0f} a year</text>')
    w=BW*yr*YRS/MX
    a(f'<rect x="{BX}" y="{yy+46}" width="{w:.1f}" height="44" rx="8" fill="{col}"/>')
    a(f'<text x="{BX+w+12:.1f}" y="{yy+76}" font-size="22" font-weight="700" fill="{T}">${yr*YRS:,.0f}</text>')
a(f'<text x="624" y="725" font-size="14" fill="{G}">Manual defrost models use about half the energy of auto defrost</text>')
a(f'<text x="60" y="800" font-size="14" fill="{G}">Sizes: GE FCM7SKWW chest and Frigidaire FFUE1326AW upright spec sheets. Energy use: ENERGY STAR. Price: EIA, June 2026.</text>')
a(f'<text x="60" y="822" font-size="14" fill="{G}">Cost totals are our estimate (kWh x 18.34¢ x 12 years). Your model, settings and electricity rate will differ.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
print(round(cy,2),round(uy,2),round(cy*YRS),round(uy*YRS))
