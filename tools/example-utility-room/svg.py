T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';W1='#D9B48A';W2='#B98A5E'
s=[];a=s.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="ur-t ur-d"><title id="ur-t">Small utility room layout guide</title><desc id="ur-d">Two front views of a small utility room. Side by side: a washing machine and a tumble dryer, each about 60 cm wide, sit under a worktop next to a sink unit, which needs about 180 cm of wall. Stacked: the dryer sits on the washing machine with a stacking kit in a column about 60 cm wide. Four notes: measure the wall, depth and height; plan the appliances first; add a worktop and a sink; and ventilate, because a new utility room needs extract ventilation and a vented dryer needs its hose to the outside. A tip says to clean the dryer filter after every use and never leave it running overnight.</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">Small Utility Room Layout Guide</text>')
a(f'<text x="60" y="130" font-size="22" fill="{G}">Two ways to fit a washer and dryer</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
a(f'<rect x="60" y="160" width="600" height="540" rx="16" fill="#FBF6EF" stroke="{BR}" stroke-width="2"/>')
fl=640
a(f'<line x1="80" y1="{fl}" x2="640" y2="{fl}" stroke="{T}" stroke-width="4"/>')
# side by side: scale 2 px per cm -> 60cm=120px... total 180cm=360px too wide with stacked. use 1.75px/cm
k=1.75
x=90
def app(x,y,w,h,lab):
    a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#FFFFFF" stroke="{G}" stroke-width="3"/>')
    a(f'<circle cx="{x+w/2}" cy="{y+h*0.58}" r="{w*0.3}" fill="{SGL}" stroke="{G}" stroke-width="3"/>')
    a(f'<text x="{x+w/2}" y="{y+18}" font-size="13" fill="{G}" text-anchor="middle">{lab}</text>')
aw=60*k; ah=85*k
app(x,fl-ah,aw,ah,'washer'); app(x+aw,fl-ah,aw,ah,'dryer')
a(f'<rect x="{x+2*aw}" y="{fl-ah}" width="{aw}" height="{ah}" fill="{SG}" stroke="{G}" stroke-width="2"/><text x="{x+2.5*aw}" y="{fl-ah/2+5}" font-size="13" fill="#FFFFFF" text-anchor="middle">sink unit</text>')
a(f'<rect x="{x-4}" y="{fl-ah-10}" width="{3*aw+8}" height="12" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
a(f'<rect x="{x+2*aw+12}" y="{fl-ah-16}" width="{aw-24}" height="10" rx="3" fill="#FFFFFF" stroke="{G}" stroke-width="2"/>')
# wall cabinets
a(f'<rect x="{x}" y="{fl-ah-150}" width="{3*aw}" height="80" fill="{SGL}" stroke="{SG}" stroke-width="2"/>')
# dimension 180
a(f'<line x1="{x}" y1="{fl+22}" x2="{x+3*aw}" y2="{fl+22}" stroke="{A}" stroke-width="3"/><line x1="{x}" y1="{fl+12}" x2="{x}" y2="{fl+32}" stroke="{A}" stroke-width="3"/><line x1="{x+3*aw}" y1="{fl+12}" x2="{x+3*aw}" y2="{fl+32}" stroke="{A}" stroke-width="3"/>')
a(f'<text x="{x+1.5*aw}" y="{fl+50}" font-size="15" font-weight="700" fill="{A}" text-anchor="middle">about 180 cm</text>')
a(f'<text x="{x+1.5*aw}" y="200" font-size="17" font-weight="700" fill="{T}" text-anchor="middle">Side by side</text>')
# stacked
sx=500
app(sx,fl-ah,aw,ah,'washer'); app(sx,fl-2*ah-6,aw,ah,'dryer')
a(f'<rect x="{sx-2}" y="{fl-ah-6}" width="{aw+4}" height="6" fill="{W2}"/>')
a(f'<line x1="{sx}" y1="{fl+22}" x2="{sx+aw}" y2="{fl+22}" stroke="{A}" stroke-width="3"/><line x1="{sx}" y1="{fl+12}" x2="{sx}" y2="{fl+32}" stroke="{A}" stroke-width="3"/><line x1="{sx+aw}" y1="{fl+12}" x2="{sx+aw}" y2="{fl+32}" stroke="{A}" stroke-width="3"/>')
a(f'<text x="{sx+aw/2}" y="{fl+50}" font-size="15" font-weight="700" fill="{A}" text-anchor="middle">about 60 cm</text>')
a(f'<text x="{sx+aw/2}" y="200" font-size="17" font-weight="700" fill="{T}" text-anchor="middle">Stacked</text>')
a(f'<text x="{sx+aw+8}" y="{fl-ah-2}" font-size="12" fill="{G}">kit</text>')
a(f'<circle cx="{sx+aw/2}" cy="250" r="18" fill="#FFFFFF" stroke="{SG}" stroke-width="3"/><path d="M{sx+aw/2},236 L{sx+aw/2},264 M{sx+aw/2-14},250 L{sx+aw/2+14},250" stroke="{SG}" stroke-width="2"/><text x="{sx+aw/2}" y="286" font-size="12" fill="{G}" text-anchor="middle">extract fan</text>')
for n,(cx,cy) in enumerate([(x-0,fl-ah-175),(x+aw,fl-ah/2),(x+2*aw+aw/2,fl-ah-40),(sx-22,250)],1):
    a(f'<circle cx="{cx}" cy="{cy}" r="17" fill="{T}"/><text x="{cx}" y="{cy+7}" font-size="18" font-weight="700" fill="#FFFFFF" text-anchor="middle">{n}</text>')
cards=[("Measure first","Wall length, depth and height."),("Appliances first","Each is about 60 cm wide."),("Worktop + sink","A surface to sort, fold and rinse."),("Fresh air","Extract fan; vent the dryer outside.")]
for i,(t1,t2) in enumerate(cards):
    y=170+i*128
    a(f'<rect x="690" y="{y}" width="450" height="114" rx="14" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
    a(f'<circle cx="728" cy="{y+42}" r="19" fill="{T}"/><text x="728" y="{y+49}" font-size="20" font-weight="700" fill="#FFFFFF" text-anchor="middle">{i+1}</text>')
    a(f'<text x="762" y="{y+50}" font-size="22" font-weight="700" fill="{T}">{t1}</text><text x="762" y="{y+82}" font-size="16" fill="{G}">{t2}</text>')
a(f'<rect x="60" y="730" width="1080" height="100" rx="14" fill="{SGL}" stroke="{SG}" stroke-width="2"/><rect x="60" y="730" width="10" height="100" rx="5" fill="{SG}"/>')
a(f'<text x="96" y="771" font-size="20" fill="{T}"><tspan font-weight="700">Dryer safety:</tspan> clean the filter after every use and never leave</text>')
a(f'<text x="96" y="805" font-size="20" fill="{T}">the dryer running overnight or while you are out.</text>')
a(f'<text x="60" y="872" font-size="15" fill="{G}">Ventilation: Planning Portal. Dryer safety: Cornwall Fire and Rescue Service. Sizes are typical; check your appliance manuals.</text>')
a('</svg>')
import re
svg=re.sub(r'(\d+\.\d{2,})',lambda m:str(round(float(m.group(1)),1)),''.join(s))
open('z.svg','w').write(svg)
