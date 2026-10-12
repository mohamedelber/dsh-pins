T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';W1='#D9B48A';W2='#B98A5E';SA='#ECCDA0'
s=[];a=s.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="us-t us-d"><title id="us-t">Under stairs shoe storage planner</title><desc id="us-d">Side view of a straight staircase with the space underneath split into three zones by height. Low end, under about 50 cm high: shallow drawers or cubbies for flat shoes and trainers. Middle, about 50 to 120 cm: pull-out units with angled shelves for most everyday pairs. Tall end, over about 120 cm: boots and wellies, a bench or coat hooks. Shelf gaps as a rule of thumb: about 15 cm for trainers, 25 cm for ankle boots and 45 cm for wellies. Keep coats, shoes and other combustible items well away from a fuse board under the stairs, and keep the hallway and stairs clear as an escape route.</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">Under Stairs Shoe Storage Planner</text>')
a(f'<text x="60" y="130" font-size="22" fill="{G}">Match the storage to the height under each step</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
FL=640; X0=90; X1=1110; TOP=190
a(f'<line x1="60" y1="{FL}" x2="1140" y2="{FL}" stroke="{T}" stroke-width="4"/>')
# stair stringer: from (X0,FL) up to (X1,TOP)
n=12; dx=(X1-X0)/n; dy=(FL-TOP)/n
pts=[(X0,FL)]
for i in range(n):
    x=X0+i*dx; y=FL-(i+1)*dy
    pts+= [(x,y),(x+dx,y)]
path='M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)
a(f'<path d="{path} L{X1},{FL} Z" fill="#FFFDF9" stroke="none"/>')
a(f'<path d="{path}" fill="none" stroke="{W2}" stroke-width="6"/>')
a(f'<line x1="{X1}" y1="{TOP}" x2="{X1}" y2="{FL}" stroke="{BR}" stroke-width="3"/>')
# zone boundaries: x where underside height = 50cm and 120cm (assume full height 260cm -> FL-TOP px)
H=260; k=(FL-TOP)/H
def xat(hcm): return X0+(hcm/H)*(X1-X0)
xa,xb=xat(50),xat(120)
for x in (xa,xb):
    a(f'<line x1="{x:.0f}" y1="{FL}" x2="{x:.0f}" y2="{FL-((x-X0)/(X1-X0))*(FL-TOP):.0f}" stroke="{A}" stroke-width="3" stroke-dasharray="9 7"/>')
# zone fills: cubbies in low, pull-outs in middle, bench/boots in tall
for i in range(3):
    x=X0+60+i*48; h=min(40,((x+44-X0)/(X1-X0))*(FL-TOP)-14)
    a(f'<rect x="{x:.0f}" y="{FL-h:.0f}" width="40" height="{h:.0f}" rx="4" fill="{SA}" stroke="{W2}" stroke-width="2"/>')
for i in range(3):
    x=xa+20+i*((xb-xa-40)/3); w=(xb-xa-40)/3-10; hmax=((x-X0)/(X1-X0))*(FL-TOP)-12
    a(f'<rect x="{x:.0f}" y="{FL-hmax:.0f}" width="{w:.0f}" height="{hmax:.0f}" rx="5" fill="{SGL}" stroke="{SG}" stroke-width="3"/>')
    a(f'<circle cx="{x+w/2:.0f}" cy="{FL-hmax/2:.0f}" r="6" fill="{W2}"/>')
bx=xb+30
a(f'<rect x="{bx:.0f}" y="{FL-110}" width="230" height="16" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
a(f'<rect x="{bx+10:.0f}" y="{FL-94}" width="14" height="94" fill="{SG}"/><rect x="{bx+206:.0f}" y="{FL-94}" width="14" height="94" fill="{SG}"/>')
for j,x in enumerate((bx+40,bx+80,bx+150)):
    hh=60 if j<2 else 80
    a(f'<path d="M{x:.0f},{FL} L{x:.0f},{FL-hh} L{x+18:.0f},{FL-hh} L{x+18:.0f},{FL-20} L{x+28:.0f},{FL-12} L{x+28:.0f},{FL} Z" fill="#4E5B47"/>')
# fuse board
fx=X1-80
a(f'<rect x="{fx}" y="{TOP+60}" width="56" height="44" rx="4" fill="#FFFFFF" stroke="{G}" stroke-width="2"/><path d="M{fx+30},{TOP+68} l-8,14 h10 l-8,14" stroke="{A}" stroke-width="3" fill="none"/>')
a(f'<rect x="{fx-26}" y="{TOP+38}" width="108" height="88" rx="10" fill="none" stroke="{A}" stroke-width="3" stroke-dasharray="8 6"/>')
# labels
for x,t1,t2 in ((X0+100,"LOW: trainers","under 50 cm"),((xa+xb)/2,"MIDDLE: pull-outs","50 to 120 cm"),(bx+115,"TALL: boots, bench","over 120 cm")):
    a(f'<text x="{x:.0f}" y="{FL+36}" font-size="20" font-weight="700" fill="{T}" text-anchor="middle">{t1}</text><text x="{x:.0f}" y="{FL+60}" font-size="16" fill="{G}" text-anchor="middle">{t2}</text>')
a(f'<text x="{fx+28}" y="{TOP+148}" font-size="15" fill="{A}" text-anchor="middle">fuse board:</text><text x="{fx+28}" y="{TOP+166}" font-size="15" fill="{A}" text-anchor="middle">keep clear</text>')
cards=[("Fuse board","Keep shoes and coats well away"),("Escape route","Keep the hallway and stairs clear"),("Dry first","Wet shoes dry before closing away")]
for i,(t1,t2) in enumerate(cards):
    x=60+i*365
    a(f'<rect x="{x}" y="710" width="345" height="70" rx="12" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/><text x="{x+20}" y="740" font-size="19" font-weight="700" fill="{T}">{t1}</text><text x="{x+20}" y="766" font-size="16" fill="{G}">{t2}</text>')
a(f'<text x="60" y="820" font-size="18" fill="{T}"><tspan font-weight="700">Shelf gaps (rule of thumb):</tspan> trainers 15 cm, ankle boots 25 cm, wellies 45 cm.</text>')
a(f'<text x="60" y="872" font-size="14" fill="{G}">Fuse board advice: London Fire Brigade and Electrical Safety First. Clear escape routes: Northumberland Fire and Rescue. Heights and gaps: our rule of thumb.</text>')
a('</svg>')
import re
svg=re.sub(r'(\d+\.\d{2,})',lambda m:str(round(float(m.group(1)),1)),''.join(s))
open('z.svg','w').write(svg)
