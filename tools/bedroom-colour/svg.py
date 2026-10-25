T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';BG='#F7F1E9';BR='#D8CBBB';CR='#FFFFFF'
s=[];a=s.append
desc=("Four cards show how window direction changes bedroom paint colours in the UK. North-facing: cool, bluish light makes colours look darker, so warm shades such as plaster pink, terracotta and warm white work, or go dark on purpose with a deep blue. "
"South-facing: warm, bright light for most of the day, so cool shades such as mint, pale blue and cool white stay fresh. East-facing: the most sun in the morning, then cooler, muted light. West-facing: cooler mornings and warm evening light; for both, judge colours at the times you use the room. "
"Below, a light reflectance value scale from 0 (black, absorbs light) to 100 (white, reflects light), and the 60-30-10 rule: 60 percent main colour on the walls, 30 percent secondary colour on bedding, curtains or furniture, 10 percent accent in cushions, throws and art.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="bc-t bc-d"><title id="bc-t">Pick a bedroom colour by the light</title><desc id="bc-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="78" font-size="40" font-weight="700" fill="{T}">Pick a Bedroom Colour by the Light</text>')
a(f'<text x="60" y="114" font-size="21" fill="{G}">Which way your window faces changes how the same paint looks</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
cards=[("N","North-facing window",["Cool, bluish light all day:","colours look darker and greyer"],"Go warm",[("#D9B6A2","plaster pink"),("#B0624A","terracotta"),("#EFE5D8","warm white")],"or go dark on purpose: deep blue"),
("S","South-facing window",["Warm, bright light most of","the day: colours look warmer"],"Cool shades stay fresh",[("#C4DCCB","mint"),("#C4D3DF","pale blue"),("#F2F4F1","cool white")],"strong sun can wash out pale tones"),
("E","East-facing window",["Most sun in the morning, then","cooler, muted light later"],"Test at the hours you use it",[("#A9B59B","sage"),("#CDBDA6","stone"),("#AFC0CC","soft blue")],"in a bedroom, mornings and night"),
("W","West-facing window",["Cooler mornings, then warm","golden light in the evening"],"Test at the hours you use it",[("#EDE2D2","warm white"),("#D9B6A2","plaster pink"),("#7E8457","olive")],"check under your lamps too")]
for i,(d,ttl,lines,lead,sw,note) in enumerate(cards):
    x=60+(i%2)*550; y=150+(i//2)*255; w=530; h=235
    a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{CR}" stroke="{BR}" stroke-width="2"/>')
    a(f'<circle cx="{x+44}" cy="{y+44}" r="26" fill="{A}"/><text x="{x+44}" y="{y+53}" font-size="26" font-weight="700" fill="#FFFFFF" text-anchor="middle">{d}</text>')
    a(f'<text x="{x+86}" y="{y+40}" font-size="22" font-weight="700" fill="{T}">{ttl}</text>')
    a(f'<text x="{x+86}" y="{y+66}" font-size="15" fill="{G}">{lines[0]}</text><text x="{x+86}" y="{y+86}" font-size="15" fill="{G}">{lines[1]}</text>')
    a(f'<text x="{x+24}" y="{y+122}" font-size="16" font-weight="700" fill="{A}">{lead}</text>')
    for j,(c,n) in enumerate(sw):
        sx=x+24+j*160
        a(f'<rect x="{sx}" y="{y+134}" width="146" height="54" rx="8" fill="{c}" stroke="{BR}"/><text x="{sx+73}" y="{y+208}" font-size="14" fill="{T}" text-anchor="middle">{n}</text>')
    a(f'<text x="{x+w-20}" y="{y+226}" font-size="13" font-style="italic" fill="{G}" text-anchor="end">{note}</text>')
# LRV bar
y=690
a(f'<text x="60" y="{y-14}" font-size="19" font-weight="700" fill="{T}">Light reflectance value (LRV)</text>')
a('<defs><linearGradient id="lrv"><stop offset="0" stop-color="#1E1E1E"/><stop offset="1" stop-color="#FFFFFF"/></linearGradient></defs>')
a(f'<rect x="60" y="{y}" width="520" height="36" rx="8" fill="url(#lrv)" stroke="{BR}"/>')
a(f'<text x="60" y="{y+58}" font-size="14" font-weight="700" fill="{T}">0 = black</text><text x="580" y="{y+58}" font-size="14" font-weight="700" fill="{T}" text-anchor="end">100 = white</text>')
a(f'<text x="60" y="{y+82}" font-size="14" fill="{G}">Low: absorbs light, feels cosy</text><text x="580" y="{y+82}" font-size="14" fill="{G}" text-anchor="end">High: reflects the light you have</text>')
# 60-30-10
X=640;W=500
a(f'<text x="{X}" y="{y-14}" font-size="19" font-weight="700" fill="{T}">The 60-30-10 rule</text>')
for (f,c,lab,tc),x0 in zip([(0.6,'#A9B59B','60% walls','#342E2A'),(0.3,'#EFE5D8','30% fabrics','#342E2A'),(0.1,'#B0624A','10%','#FFFFFF')],[X,X+W*0.6,X+W*0.9]):
    a(f'<rect x="{x0}" y="{y}" width="{W*f}" height="36" fill="{c}" stroke="{BR}"/><text x="{x0+W*f/2}" y="{y+24}" font-size="14" font-weight="700" fill="{tc}" text-anchor="middle">{lab}</text>')
a(f'<text x="{X}" y="{y+58}" font-size="14" fill="{G}">Main colour on the walls, a second colour in fabrics or</text>')
a(f'<text x="{X}" y="{y+80}" font-size="14" fill="{G}">furniture, and a 10% accent in cushions, throws and art</text>')
a(f'<text x="60" y="846" font-size="14" fill="{G}">Swatches are approximate screen colours, not paint matches: always test a real sample. Sources: Dulux, Dulux Heritage, Farrow &amp; Ball, Little Greene</text>')
a(f'<text x="60" y="868" font-size="14" fill="{G}">and Lick experts via Homes &amp; Gardens, Livingetc and Ideal Home. Light direction is for the UK and other northern-hemisphere homes.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
