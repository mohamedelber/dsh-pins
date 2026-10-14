import re
T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';W2='#B98A5E'
s=[];a=s.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="cu-t cu-d"><title id="cu-t">How to measure for curtains</title><desc id="cu-d">Front view of a window with a curtain pole above it. Measure the window width, then add about 20 centimetres (8 inches) on each side for the pole so open curtains clear the glass. For standard fullness each curtain in a pair is about as wide as the pole. Measure the drop from the top of the pole: to 1 centimetre above the sill for sill length, about 15 centimetres below the sill for below-sill length, or to 1 centimetre above the floor for floor length.</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">How to Measure for Curtains</text>')
a(f'<text x="60" y="130" font-size="22" fill="{G}">Pole width first, then the drop to where you want the curtains to end</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
FL=760; wx0,wx1=330,630; wy0,wy1=300,560; py=245; ext=110
a(f'<line x1="60" y1="{FL}" x2="830" y2="{FL}" stroke="{T}" stroke-width="5"/>')
a(f'<rect x="{wx0}" y="{wy0}" width="{wx1-wx0}" height="{wy1-wy0}" fill="#DCEAF0" stroke="#FFFFFF" stroke-width="12"/>')
a(f'<line x1="{(wx0+wx1)//2}" y1="{wy0}" x2="{(wx0+wx1)//2}" y2="{wy1}" stroke="#fff" stroke-width="8"/>')
a(f'<rect x="{wx0-18}" y="{wy1}" width="{wx1-wx0+36}" height="14" fill="#EFE6DA" stroke="{BR}" stroke-width="2"/>')
# curtains open
for x in (wx0-ext, wx1+ext-120):
    a(f'<rect x="{x}" y="{py+6}" width="120" height="{FL-6-py-8}" fill="{SG}" opacity=".85"/>')
    for q in range(1,4): a(f'<line x1="{x+30*q}" y1="{py+10}" x2="{x+30*q}" y2="{FL-10}" stroke="#7E9578" stroke-width="2"/>')
a(f'<line x1="{wx0-ext-14}" y1="{py}" x2="{wx1+ext+14}" y2="{py}" stroke="{T}" stroke-width="8"/>')
for x in (wx0-ext-20, wx1+ext+20): a(f'<circle cx="{x}" cy="{py}" r="11" fill="{T}"/>')
# dims: window width
yW=wy0+40
a(f'<line x1="{wx0+10}" y1="{yW}" x2="{wx1-10}" y2="{yW}" stroke="{A}" stroke-width="3"/><text x="{(wx0+wx1)//2}" y="{yW-10}" font-size="18" font-weight="700" fill="{A}" text-anchor="middle">window width</text>')
# extension
a(f'<line x1="{wx1}" y1="{py-38}" x2="{wx1+ext}" y2="{py-38}" stroke="{A}" stroke-width="3"/><line x1="{wx1}" y1="{py-48}" x2="{wx1}" y2="{py-28}" stroke="{A}" stroke-width="3"/><line x1="{wx1+ext}" y1="{py-48}" x2="{wx1+ext}" y2="{py-28}" stroke="{A}" stroke-width="3"/>')
a(f'<text x="{wx1+ext/2:.0f}" y="{py-56}" font-size="17" font-weight="700" fill="{A}" text-anchor="middle">+20 cm (8 in)</text>')
a(f'<line x1="{wx0-ext}" y1="{py-38}" x2="{wx0}" y2="{py-38}" stroke="{A}" stroke-width="3"/><line x1="{wx0-ext}" y1="{py-48}" x2="{wx0-ext}" y2="{py-28}" stroke="{A}" stroke-width="3"/><line x1="{wx0}" y1="{py-48}" x2="{wx0}" y2="{py-28}" stroke="{A}" stroke-width="3"/>')
a(f'<text x="{wx0-ext/2:.0f}" y="{py-56}" font-size="17" font-weight="700" fill="{A}" text-anchor="middle">+20 cm (8 in)</text>')
# drop lines on right side
xd=860
for yv,lab,col in ((wy1-6,'Sill: 1 cm above sill',T),(wy1+80,'Below sill: about 15 cm',T),(FL-6,'Floor: 1 cm above floor',T)):
    a(f'<line x1="{xd-20}" y1="{yv}" x2="{xd+10}" y2="{yv}" stroke="{G}" stroke-width="2"/>')
    a(f'<text x="{xd+20}" y="{yv+6}" font-size="18" fill="{col}">{lab}</text>')
a(f'<line x1="{xd-5}" y1="{py}" x2="{xd-5}" y2="{FL-6}" stroke="{A}" stroke-width="3" stroke-dasharray="8 6"/>')
a(f'<line x1="{wx1+ext+14}" y1="{py}" x2="{xd+5}" y2="{py}" stroke="{G}" stroke-width="2" stroke-dasharray="4 5"/>')
a(f'<text x="{xd+20}" y="{py+6}" font-size="18" font-weight="700" fill="{A}">Drop starts at the top of the pole</text>')
cards=[("Pole width","Window + 20 cm (8 in) each side"),("Each curtain","About the pole width (2x fullness)"),("Drop","Top of pole to where it should end")]
for i,(t1,t2) in enumerate(cards):
    x=60+i*365
    a(f'<rect x="{x}" y="790" width="345" height="62" rx="12" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/><text x="{x+18}" y="816" font-size="18" font-weight="700" fill="{T}">{t1}</text><text x="{x+18}" y="840" font-size="15" fill="{G}">{t2}</text>')
a(f'<text x="60" y="880" font-size="14" fill="{G}">Rules of thumb from Dunelm and Home Depot measuring guides. Ready-made sizes vary by shop.</text>')
a('</svg>')
svg=re.sub(r'"([^"]*)"',lambda q:'"'+re.sub(r'(\d+\.\d{2,})',lambda m:str(round(float(m.group(1)),1)),q.group(1))+'"',''.join(s))
open('z.svg','w').write(svg)
