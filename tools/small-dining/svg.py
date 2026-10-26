T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';OAK='#C9A06B';OAKD='#A97F4C';CR='#FBF7F0'
s=[];a=s.append
desc=("Two floor plans of the same 120 by 80 cm table for four. With chairs on both long sides and 75 cm clear on every side, the dining area needs 270 by 230 cm. "
"With a built-in banquette on one long side, 50 cm deep with the table overlapping the seat by 10 cm, the table edge sits 40 cm from the wall and the area needs 270 by 195 cm, saving 35 cm of room depth. "
"Planning numbers: 60 cm of table edge per diner; a 90 to 100 cm round table seats four and 70 to 80 cm seats two; 60 cm from table to wall is a tight minimum, 75 cm comfortable, 100 to 110 cm to walk behind; banquette seat about 45 cm high and 45 to 50 cm deep; pendant 70 to 90 cm above the table, half to two thirds of the table width; rug at least 60 cm bigger than the table on each side; sideboard 30 to 40 cm deep.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="sd-t sd-d"><title id="sd-t">Small dining room planning numbers</title><desc id="sd-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="78" font-size="40" font-weight="700" fill="{T}">Small Dining Room: The Numbers</text>')
a(f'<text x="60" y="114" font-size="20" fill="{G}">One 120 x 80 cm table for four, planned two ways (to scale)</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
k=1.15
def chair(x,y,w=42,h=42):
    a(f'<rect x="{x}" y="{y}" width="{w*k}" height="{h*k}" rx="6" fill="#E9DFD2" stroke="{OAKD}" stroke-width="1.5"/>')
def plan(X,Y,title,bench):
    W=270; D=195 if bench else 230
    a(f'<text x="{X}" y="{Y-16}" font-size="18" font-weight="700" fill="{A}">{title}</text>')
    a(f'<rect x="{X}" y="{Y}" width="{W*k}" height="{D*k}" fill="{SGL}" stroke="{SG}" stroke-width="2" stroke-dasharray="7 5"/>')
    top=40 if bench else 75
    tx=X+75*k; ty=Y+top*k
    if bench:
        a(f'<line x1="{X-6}" y1="{Y}" x2="{X+W*k+6}" y2="{Y}" stroke="{T}" stroke-width="7"/><text x="{X+W*k/2}" y="{Y-34}" font-size="12" fill="{G}" text-anchor="middle"></text>')
        a(f'<rect x="{X+40*k}" y="{Y}" width="{190*k}" height="{50*k}" rx="4" fill="#8FA689" stroke="#5F7A59" stroke-width="1.5"/>')
        a(f'<text x="{X+W*k/2}" y="{Y+16}" font-size="12" font-weight="700" fill="#FFFFFF" text-anchor="middle">banquette 50 cm deep</text>')
    a(f'<rect x="{tx}" y="{ty}" width="{120*k}" height="{80*k}" rx="4" fill="{OAK}" stroke="{OAKD}" stroke-width="2" fill-opacity="0.92"/>')
    a(f'<text x="{tx+60*k}" y="{ty+40*k+5}" font-size="14" font-weight="700" fill="{T}" text-anchor="middle">120 x 80 cm</text>')
    for cx in (tx+12*k, tx+66*k):
        chair(cx,ty+80*k+6)
        if not bench: chair(cx,ty-42*k-6)
    # dims
    a(f'<line x1="{X-14}" y1="{Y}" x2="{X-14}" y2="{Y+D*k}" stroke="{T}" stroke-width="1.5"/><text x="{X-22}" y="{Y+D*k/2}" font-size="15" font-weight="700" fill="{T}" text-anchor="middle" transform="rotate(-90 {X-22} {Y+D*k/2})">{D} cm</text>')
    a(f'<line x1="{X}" y1="{Y+D*k+16}" x2="{X+W*k}" y2="{Y+D*k+16}" stroke="{T}" stroke-width="1.5"/><text x="{X+W*k/2}" y="{Y+D*k+36}" font-size="15" font-weight="700" fill="{T}" text-anchor="middle">270 cm</text>')
    # clearance labels
    a(f'<text x="{X+37*k}" y="{ty+40*k+5}" font-size="12" fill="#4F6B49" text-anchor="middle">75</text><text x="{X+(W-37)*k}" y="{ty+40*k+5}" font-size="12" fill="#4F6B49" text-anchor="middle">75</text>')
    a(f'<text x="{tx+120*k+8}" y="{Y+D*k-20}" font-size="12" fill="#4F6B49">75 cm clear</text>')
    if not bench: a(f'<text x="{tx+120*k+8}" y="{Y+28}" font-size="12" fill="#4F6B49">75 cm clear</text>')
    else: a(f'<text x="{X+W*k+12}" y="{Y+top*k+5}" font-size="13" font-weight="700" fill="{A}">table edge 40 cm</text><text x="{X+W*k+12}" y="{Y+top*k+23}" font-size="13" font-weight="700" fill="{A}">from the wall</text>')
plan(90,178,'With chairs all round',False)
plan(90,540,'With a wall banquette',True)
a(f'<text x="420" y="408" font-size="15" font-weight="700" fill="{T}">2.7 x 2.3 m</text><text x="420" y="430" font-size="13" fill="{G}">for four, chairs</text>')
a(f'<text x="420" y="740" font-size="15" font-weight="700" fill="{A}">2.7 x 1.95 m</text><text x="420" y="762" font-size="13" fill="{G}">saves 35 cm of depth</text>')
# right panel
RX=600
a(f'<rect x="{RX}" y="150" width="560" height="660" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="{RX+26}" y="192" font-size="21" font-weight="700" fill="{A}">Planning numbers</text>')
rows=[("Per diner","60 cm of table edge"),("Table for four","120 cm long, at least 90 wide"),("Round table","70–80 cm seats 2, 90–100 cm seats 4"),
("Table to wall","60 tight, 75 comfortable"),("To walk behind","100–110 cm"),("Banquette seat","about 45 cm high, 45–50 deep"),("Pendant height","70–90 cm above the table top"),
("Pendant width","1/2 to 2/3 of the table width"),("Rug","table + at least 60 cm each side"),("Sideboard depth","30–40 cm, not 42+")]
y=236
for l,v in rows:
    a(f'<text x="{RX+26}" y="{y}" font-size="16" font-weight="700" fill="{T}">{l}</text><text x="{RX+220}" y="{y}" font-size="16" fill="{T}">{v}</text><line x1="{RX+26}" y1="{y+16}" x2="{RX+534}" y2="{y+16}" stroke="{BR}"/>')
    y+=54
a(f'<text x="60" y="852" font-size="14" fill="{G}">Example plans use 75 cm clear and 42 cm chairs. Sources: IKEA GB, Oak Furnitureland, La Redoute, a UK builders\' guide (Bookabuilder), Tala,</text>')
a(f'<text x="60" y="874" font-size="14" fill="{G}">Blakes London via Homes &amp; Gardens. Check your own room and chairs before you buy.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
