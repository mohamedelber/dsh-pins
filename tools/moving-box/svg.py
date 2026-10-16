import re
T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';K1='#D9B48A';K2='#E8CFA6';K3='#C29A6B';KE='#8C6A45'
desc=("Six common moving boxes drawn from the front with typical sizes and what to pack in each. Small box, 16 by 12 by 12 inches, 1.5 cubic feet: books, dishes, canned food and tools. "
"Medium box, 18 by 18 by 16 inches, 3 cubic feet: kitchen items, toys, decor and shoes. Large box, 18 by 18 by 24 inches, 4.5 cubic feet: bedding, towels and pillows. "
"Extra-large box, 24 by 18 by 24 inches, 6 cubic feet: comforters and light bulky items. Wardrobe box, about 24 inches wide and tall, with a hanging bar: clothes on hangers. "
"Dish pack, about 18 by 18 by 28 inches with double walls and dividers: plates and glasses. Rule: the heavier the item, the smaller the box.")
s=[];a=s.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="mb-t mb-d"><title id="mb-t">Moving box sizes and what to pack in each</title><desc id="mb-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">Moving Box Sizes</text>')
a(f'<text x="60" y="130" font-size="22" fill="{G}">Typical sizes. The heavier the item, the smaller the box.</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
base=600; k=7.2
boxes=[("Small","16 x 12 x 12 in","1.5 cu ft",16,12,["Books","Dishes","Canned food","Tools"]),
("Medium","18 x 18 x 16 in","3 cu ft",18,16,["Kitchen items","Toys","Decor","Shoes"]),
("Large","18 x 18 x 24 in","4.5 cu ft",18,24,["Bedding","Towels","Pillows","Lampshades"]),
("Extra-large","24 x 18 x 24 in","6 cu ft",24,24,["Comforters","Cushions","Light, bulky","items"]),
("Wardrobe","about 24 in wide","with a hanging bar",24,48,["Clothes on","hangers"]),
("Dish pack","about 18 x 18 x 28 in","double-wall",18,28,["Plates","Glasses","with dividers"])]
a(f'<line x1="40" y1="{base}" x2="1160" y2="{base}" stroke="{T}" stroke-width="4"/>')
x=60; gap=[0]
for i,(nm,dim,vol,w,h,items) in enumerate(boxes):
    W=w*k*0.92; H=h*k; y=base-H; d=16
    a(f'<polygon points="{x+d},{y-d} {x+W+d},{y-d} {x+W},{y} {x},{y}" fill="{K2}" stroke="{KE}" stroke-width="2"/>')
    a(f'<polygon points="{x+W},{y} {x+W+d},{y-d} {x+W+d},{base-d} {x+W},{base}" fill="{K3}" stroke="{KE}" stroke-width="2"/>')
    a(f'<rect x="{x}" y="{y}" width="{W}" height="{H}" fill="{K1}" stroke="{KE}" stroke-width="2"/>')
    if nm!="Wardrobe": a(f'<rect x="{x+W/2-9}" y="{y}" width="18" height="{min(H*0.3,40)}" fill="#EFE3CF" opacity=".9"/>')
    if nm=="Wardrobe":
        by=y+30
        a(f'<line x1="{x+10}" y1="{by}" x2="{x+W-10}" y2="{by}" stroke="{T}" stroke-width="4"/>')
        for j in range(4):
            hx=x+28+j*((W-56)/3)
            a(f'<path d="M{hx},{by} q-6,-10 0,-14 q6,4 0,14 l-18,18 h36 z" fill="none" stroke="{T}" stroke-width="2"/>')
            a(f'<rect x="{hx-16}" y="{by+18}" width="32" height="{H-80}" rx="6" fill="{SG if j%2==0 else SGL}" stroke="#7E9578" stroke-width="1.5"/>')
    if nm=="Dish pack":
        for j in (1,2): a(f'<line x1="{x}" y1="{y+H*j/3}" x2="{x+W}" y2="{y+H*j/3}" stroke="{KE}" stroke-width="1.5" stroke-dasharray="6 5"/>')
    cx=x+W/2
    a(f'<text x="{cx}" y="{base+36}" font-size="21" font-weight="700" fill="{T}" text-anchor="middle">{nm}</text>')
    a(f'<text x="{cx}" y="{base+62}" font-size="16" fill="{A}" font-weight="700" text-anchor="middle">{dim}</text>')
    a(f'<text x="{cx}" y="{base+84}" font-size="15" fill="{G}" text-anchor="middle">{vol}</text>')
    for j,it in enumerate(items):
        a(f'<text x="{cx}" y="{base+116+j*22}" font-size="15" fill="{T}" text-anchor="middle">{it}</text>')
    x+=W+d+26
# weight arrow
a(f'<line x1="60" y1="215" x2="690" y2="215" stroke="{A}" stroke-width="3"/><polygon points="690,207 706,215 690,223" fill="{A}"/>')
a(f'<text x="60" y="201" font-size="17" font-weight="700" fill="{A}">Small to extra-large: the bigger the box, the lighter the items</text>')
a(f'<text x="60" y="880" font-size="14" fill="{G}">Typical US moving box sizes (U-Haul). Sizes vary by store; keep every box light enough to lift safely.</text>')
a('</svg>')
svg=re.sub(r'"([^"]*)"',lambda q:'"'+re.sub(r'(\d+\.\d{2,})',lambda m:str(round(float(m.group(1)),1)),q.group(1))+'"',''.join(s))
open('z.svg','w').write(svg); print(x)
