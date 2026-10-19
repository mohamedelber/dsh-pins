T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';W1='#D9B48A';W2='#B98A5E'
s=[];a=s.append
desc=("Top-down plan of an example 12 by 13 foot apartment living room with spacing rules. A sofa sits against the bottom wall with a coffee table 16 to 18 inches in front of it. "
"A 6 by 9 foot rug sits under the front legs of the sofa and the armchair. The TV hangs on the opposite wall above a low console. "
"A 30 to 36 inch walkway runs from the door on the right wall past the end of the sofa. Anchor the TV and tall shelves to the wall.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="lr-t lr-d"><title id="lr-t">Small living room spacing guide</title><desc id="lr-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">The Small Living Room Spacing Guide</text>')
a(f'<text x="60" y="128" font-size="22" fill="{G}">The measurements that make a small room feel easy to move around</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
F=38; X0=84; Y0=182; W=12*F; H=13*F
def X(f): return X0+f*F
def Y(f): return Y0+f*F
a(f'<rect x="{X0-10}" y="{Y0-10}" width="{W+20}" height="{H+20}" fill="{W2}"/><rect x="{X0}" y="{Y0}" width="{W}" height="{H}" fill="#FBF8F3"/>')
# window on left wall
a(f'<rect x="{X0-10}" y="{Y(7.8)}" width="10" height="{3.6*F}" fill="#CFE0E8"/>')
# door right wall
dy=Y(1); a(f'<rect x="{X0+W}" y="{dy}" width="10" height="{3*F}" fill="#FBF8F3"/><path d="M{X0+W} {dy} A{3*F} {3*F} 0 0 0 {X0+W-3*F} {dy+3*F}" fill="none" stroke="{G}" stroke-width="2" stroke-dasharray="5 5"/><line x1="{X0+W}" y1="{dy+3*F}" x2="{X0+W-3*F}" y2="{dy+3*F}" stroke="{G}" stroke-width="3"/>')
a(f'<text x="{X0+W+18}" y="{dy+1.5*F+6}" font-size="15" fill="{G}" transform="rotate(90 {X0+W+18} {dy+1.5*F+6})" text-anchor="middle">Door</text>')
# rug 9x6
a(f'<rect x="{X(1.5)}" y="{Y(5.6)}" width="{9*F}" height="{6*F}" rx="6" fill="{SA}" fill-opacity="0.85" stroke="{W1}" stroke-width="2"/>')
# TV console + TV on top wall
a(f'<rect x="{X(3.5)}" y="{Y0+4}" width="{5*F}" height="{1.2*F}" rx="4" fill="{W1}" stroke="{W2}" stroke-width="2"/><rect x="{X(4.1)}" y="{Y0}" width="{3.8*F}" height="8" fill="{T}"/>')
a(f'<text x="{X(6)}" y="{Y(1.2)+22}" font-size="15" fill="{G}" text-anchor="middle">TV on the wall, console below</text>')
# sofa bottom wall
a(f'<rect x="{X(2.5)}" y="{Y(10)}" width="{7*F}" height="{3*F-4}" rx="14" fill="{SG}"/><rect x="{X(2.5)}" y="{Y(12.1)}" width="{7*F}" height="{0.85*F}" rx="10" fill="#6F8F69"/>')
# coffee table
a(f'<rect x="{X(4)}" y="{Y(6.77)}" width="{4*F}" height="{1.9*F}" rx="30" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
# armchair left
a(f'<rect x="{X(0.3)}" y="{Y(5.4)}" width="{2.7*F}" height="{2.7*F}" rx="14" fill="#E3C9A8" stroke="{W2}" stroke-width="2"/><rect x="{X(0.3)}" y="{Y(5.4)}" width="{0.7*F}" height="{2.7*F}" rx="10" fill="#C9A47A"/>')
# floor lamp + plant
a(f'<circle cx="{X(1.4)}" cy="{Y(11.8)}" r="16" fill="#fff" stroke="{BR}" stroke-width="3"/><circle cx="{X(1.4)}" cy="{Y(11.8)}" r="6" fill="{A}"/>')
a(f'<circle cx="{X(0.9)}" cy="{Y(0.9)}" r="20" fill="{SG}"/>')
# dimension: sofa to table
y1=Y(8.67); y2=Y(10)
a(f'<line x1="{X(6)}" y1="{y1}" x2="{X(6)}" y2="{y2}" stroke="{A}" stroke-width="3"/><line x1="{X(6)-8}" y1="{y1}" x2="{X(6)+8}" y2="{y1}" stroke="{A}" stroke-width="3"/><line x1="{X(6)-8}" y1="{y2}" x2="{X(6)+8}" y2="{y2}" stroke="{A}" stroke-width="3"/>')
a(f'<rect x="{X(6)+12}" y="{(y1+y2)/2-14}" width="88" height="28" rx="14" fill="#fff" stroke="{A}" stroke-width="2"/><text x="{X(6)+56}" y="{(y1+y2)/2+6}" font-size="15" font-weight="700" fill="{A}" text-anchor="middle">16-18 in</text>')
# walkway
wx=X(10.75)
a(f'<path d="M{wx} {Y(4.4)} L{wx} {Y(12.6)}" stroke="{A}" stroke-width="4" stroke-dasharray="10 9" stroke-linecap="round"/><path d="M{wx-10} {Y(12.6)-14} L{wx} {Y(12.6)+2} L{wx+10} {Y(12.6)-14} Z" fill="{A}"/>')
a(f'<rect x="{wx-58}" y="{Y(4.6)}" width="116" height="28" rx="14" fill="#fff" stroke="{A}" stroke-width="2"/><text x="{wx}" y="{Y(4.6)+20}" font-size="15" font-weight="700" fill="{A}" text-anchor="middle">30-36 in path</text>')
# rug label
a(f'<text x="{X(6)}" y="{Y(6.1)+4}" font-size="15" fill="{G}" text-anchor="middle">6 x 9 ft rug</text>')
# room dims
a(f'<text x="{X0+W/2}" y="{Y0+H+40}" font-size="17" fill="{G}" text-anchor="middle">12 ft (3.7 m)</text>')
a(f'<text x="{X0-28}" y="{Y0+H/2}" font-size="17" fill="{G}" text-anchor="middle" transform="rotate(-90 {X0-28} {Y0+H/2})">13 ft (4 m)</text>')
LX=670; ly=200
items=[("16-18 in","Sofa to coffee table","close enough to reach a drink"),("30-36 in","Main walkway","18-24 in only where it is tight"),("Front legs","On the rug","sofa and chairs both touch it"),("30°","TV size","about 52 in at 7 ft away"),("Anchor","TV and tall shelves","strap them to the wall")]
for k,(big,t1,t2) in enumerate(items):
    a(f'<rect x="{LX}" y="{ly}" width="470" height="92" rx="14" fill="#fff" stroke="{BR}" stroke-width="2"/>')
    a(f'<rect x="{LX}" y="{ly}" width="132" height="92" rx="14" fill="{A if k<4 else T}"/><rect x="{LX+118}" y="{ly}" width="14" height="92" fill="{A if k<4 else T}"/>')
    a(f'<text x="{LX+66}" y="{ly+55}" font-size="{24 if len(big)<9 else 20}" font-weight="700" fill="#fff" text-anchor="middle">{big}</text>')
    a(f'<text x="{LX+152}" y="{ly+40}" font-size="21" font-weight="700" fill="{T}">{t1}</text><text x="{LX+152}" y="{ly+68}" font-size="17" fill="{G}">{t2}</text>')
    ly+=108
a(f'<text x="60" y="872" font-size="15" fill="{G}">Example 12 x 13 ft room, our own layout. Spacing: Emily Henderson and Wayfair; rug: Ruggable; TV: SMPTE via Sound &amp; Vision.</text>')
a('</svg>')
import re
open('z.svg','w').write(re.sub(r'(\d+\.\d{1,2})\d+',r'\1','\n'.join(s)))
