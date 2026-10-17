import re
T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';W1='#D9B48A';W2='#B98A5E'
desc=("Four rooms drawn from above showing how big a rug should be. Living room: the rug sits under the front legs of the sofa and chairs, with about 12 to 18 inches of bare floor to the walls. "
"Dining room: the rug extends 24 to 36 inches past every side of the table so pulled-out chairs stay on it. Bedroom: the rug lies across the lower two-thirds of the bed and extends at least 24 inches past each side. "
"Hallway: a runner stops about 4 to 6 inches from each wall and each end.")
s=[];a=s.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="rg-t rg-d"><title id="rg-t">Rug size rules by room</title><desc id="rg-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">Rug Size Rules by Room</text>')
a(f'<text x="60" y="130" font-size="22" fill="{G}">Seen from above. Size the rug to the furniture, then check the border.</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
def room(x,y,w,h,title,rule):
    a(f'<text x="{x}" y="{y-16}" font-size="24" font-weight="700" fill="{T}">{title}</text>')
    a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fff" stroke="{T}" stroke-width="5"/>')
    a(f'<text x="{x}" y="{y+h+34}" font-size="17" font-weight="700" fill="{A}">{rule}</text>')
def rug(x,y,w,h): a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{SGL}" stroke="{SG}" stroke-width="3" stroke-dasharray="10 6"/>')
def dim(x1,y1,x2,y2,lab,tx,ty,anchor="middle"):
    a(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{A}" stroke-width="3"/>')
    a(f'<text x="{tx}" y="{ty}" font-size="16" font-weight="700" fill="{A}" text-anchor="{anchor}">{lab}</text>')
# living
x,y,w,h=60,200,500,290
room(x,y,w,h,"Living room","Front legs on the rug, 12–18 in of floor to the walls")
rug(x+60,y+50,w-120,h-100)
a(f'<rect x="{x+110}" y="{y+h-80}" width="{w-220}" height="70" rx="12" fill="{W2}"/>')  # sofa
a(f'<rect x="{x+190}" y="{y+110}" width="{w-380}" height="60" rx="8" fill="{W1}"/>')  # table
for cx in (x+95,x+w-95-70): a(f'<rect x="{cx}" y="{y+30}" width="70" height="60" rx="10" fill="{W2}"/>')
dim(x,y+20,x+60,y+20,"",0,0); a(f'<text x="{x+66}" y="{y+26}" font-size="15" fill="{A}" font-weight="700">border</text>')
# dining
x,y,w,h=640,200,500,290
room(x,y,w,h,"Dining room","24–36 in of rug past every side of the table")
rug(x+50,y+30,w-100,h-60)
a(f'<rect x="{x+150}" y="{y+105}" width="{w-300}" height="80" rx="6" fill="{W1}"/>')
for i in range(3):
    cx=x+165+i*65
    a(f'<rect x="{cx}" y="{y+62}" width="40" height="36" rx="6" fill="{W2}"/><rect x="{cx}" y="{y+192}" width="40" height="36" rx="6" fill="{W2}"/>')
dim(x+w-150,y+145,x+w-50,y+145,"24–36 in",x+w-100,y+137)
# bedroom
x,y,w,h=60,585,500,235
room(x,y,w,h,"Bedroom","At least 24 in past each side, under the lower two-thirds")
rug(x+90,y+60,w-180,165)
a(f'<rect x="{x+175}" y="{y+6}" width="{w-350}" height="174" rx="10" fill="{W2}" opacity=".95"/>')
a(f'<rect x="{x+185}" y="{y+14}" width="{w-370}" height="40" rx="8" fill="#F3EDE4"/>')
for nx in (x+110,x+w-110-50): a(f'<rect x="{nx}" y="{y+8}" width="50" height="40" rx="4" fill="{W1}"/>')
dim(x+w-175,y+130,x+w-90,y+130,"24 in+",x+w-132,y+122)
# hallway
x,y,w,h=640,660,500,110
room(x,y,w,h,"Hallway runner","4–6 in of floor at each side and end")
rug(x+22,y+22,w-44,h-44)
dim(x+w-22,y+h/2,x+w,y+h/2,"",0,0)
a(f'<text x="{x+w-26}" y="{y+h/2-8}" font-size="15" fill="{A}" font-weight="700" text-anchor="end">4–6 in</text>')
a(f'<text x="60" y="892" font-size="14" fill="{G}">Rules of thumb from The Home Depot rug size guide and Fibreworks custom rug guide. Measure your own furniture before you buy.</text>')
a('</svg>')
svg=''.join(s)
open('z.svg','w').write(svg)
