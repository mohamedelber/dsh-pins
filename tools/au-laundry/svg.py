T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';W1='#D9B48A';W2='#B98A5E'
s=[];a=s.append;k=0.19
desc=("Top-down plans of three small Australian laundry layouts with typical sizes in millimetres. "
"Layout 1, single wall: a washing machine with a dryer stacked on top in a 625 mm wide space next to a 499 mm tub cabinet, about 1,150 mm of wall, 650 mm deep, with about 900 mm of standing room in front. "
"Layout 2, side by side: washer and dryer under a benchtop next to the tub, about 1,750 mm of wall. "
"Layout 3, galley: machines and tub on one wall, 350 mm deep shelves on the opposite wall and about 900 mm of walkway between, about 1,900 mm wide in total. "
"These are planning guides based on typical appliance sizes, not building rules.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="al-t al-d"><title id="al-t">Small laundry layouts in mm</title><desc id="al-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="44" font-weight="700" fill="{T}">Small Laundry Layouts in mm</text>')
a(f'<text x="60" y="118" font-size="22" fill="{G}">Three plans seen from above, with typical Australian sizes</text>')
a(f'<text x="1140" y="50" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
def box(x,y,w,h,fill,label,sub=None,circle=False):
    a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill}" stroke="{G}" stroke-width="2"/>')
    if circle: a(f'<circle cx="{x+w/2}" cy="{y+h*0.62}" r="{min(w,h)*0.22}" fill="none" stroke="{G}" stroke-width="2"/>')
    a(f'<text x="{x+w/2}" y="{y+20}" font-size="14" font-weight="700" fill="{T}" text-anchor="middle">{label}</text>')
    if sub: a(f'<text x="{x+w/2}" y="{y+h-8}" font-size="11" fill="{G}" text-anchor="middle">{sub}</text>')
def hdim(x1,x2,y,label):
    a(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{A}" stroke-width="2.5"/><line x1="{x1}" y1="{y-7}" x2="{x1}" y2="{y+7}" stroke="{A}" stroke-width="2.5"/><line x1="{x2}" y1="{y-7}" x2="{x2}" y2="{y+7}" stroke="{A}" stroke-width="2.5"/>')
    a(f'<text x="{(x1+x2)/2}" y="{y-8}" font-size="15" font-weight="700" fill="{A}" text-anchor="middle">{label}</text>')
def vdim(x,y1,y2,label):
    a(f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{A}" stroke-width="2.5"/><line x1="{x-7}" y1="{y1}" x2="{x+7}" y2="{y1}" stroke="{A}" stroke-width="2.5"/><line x1="{x-7}" y1="{y2}" x2="{x+7}" y2="{y2}" stroke="{A}" stroke-width="2.5"/>')
    a(f'<text x="{x+10}" y="{(y1+y2)/2+5}" font-size="14" font-weight="700" fill="{A}">{label}</text>')
def panel(x0,title,sub):
    a(f'<text x="{x0}" y="180" font-size="22" font-weight="700" fill="{T}">{title}</text><text x="{x0}" y="204" font-size="15" fill="{G}">{sub}</text>')
Y=270
# 1 single wall
x=70; panel(x,'1. Single wall','stacked washer and dryer')
a(f'<rect x="{x}" y="{Y-8}" width="{1150*k}" height="8" fill="{T}"/>')
box(x,Y,625*k,650*k,'#FFFFFF','W + D','stacked',True); box(x+625*k,Y,499*k,630*k,'#E3ECEF','Tub','45 L')
a(f'<rect x="{x}" y="{Y+650*k}" width="{1150*k}" height="{900*k}" fill="{SGL}" opacity="0.7"/><text x="{x+575*k}" y="{Y+650*k+900*k/2+5}" font-size="13" fill="{G}" text-anchor="middle">standing room</text>')
hdim(x,x+1150*k,Y-22,'~1,150')
vdim(x+1150*k+14,Y,Y+650*k,'650'); vdim(x+1150*k+14,Y+650*k,Y+1550*k,'900')
# 2 side by side
x=420; panel(x,'2. Side by side','under one benchtop')
a(f'<rect x="{x}" y="{Y-8}" width="{1750*k}" height="8" fill="{T}"/>')
a(f'<rect x="{x}" y="{Y}" width="{1750*k}" height="{650*k}" fill="{W1}" opacity="0.35"/>')
box(x,Y,625*k,650*k,'#FFFFFF','W',None,True); box(x+625*k,Y,625*k,650*k,'#FFFFFF','D'); box(x+1250*k,Y,499*k,630*k,'#E3ECEF','Tub','45 L')
a(f'<rect x="{x}" y="{Y+650*k}" width="{1750*k}" height="{900*k}" fill="{SGL}" opacity="0.7"/><text x="{x+875*k}" y="{Y+650*k+900*k/2+5}" font-size="13" fill="{G}" text-anchor="middle">standing room</text>')
hdim(x,x+1750*k,Y-22,'~1,750')
vdim(x+1750*k+14,Y,Y+650*k,'650'); vdim(x+1750*k+14,Y+650*k,Y+1550*k,'900')
# 3 galley
x=860; panel(x,'3. Galley','shelves opposite')
a(f'<rect x="{x}" y="{Y-8}" width="{1150*k}" height="8" fill="{T}"/>')
box(x,Y,625*k,650*k,'#FFFFFF','W + D','stacked',True); box(x+625*k,Y,499*k,630*k,'#E3ECEF','Tub','45 L')
a(f'<rect x="{x}" y="{Y+650*k}" width="{1150*k}" height="{900*k}" fill="{SGL}" opacity="0.7"/><text x="{x+575*k}" y="{Y+650*k+900*k/2+5}" font-size="13" fill="{G}" text-anchor="middle">walkway</text>')
a(f'<rect x="{x}" y="{Y+1550*k}" width="{1150*k}" height="{350*k}" fill="{SA}" stroke="{W2}" stroke-width="2"/><text x="{x+575*k}" y="{Y+1550*k+350*k/2+5}" font-size="13" fill="{T}" text-anchor="middle">shelves</text>')
a(f'<rect x="{x}" y="{Y+1900*k}" width="{1150*k}" height="8" fill="{T}"/>')
vdim(x+1150*k+14,Y,Y+650*k,'650'); vdim(x+1150*k+14,Y+650*k,Y+1550*k,'900'); vdim(x+1150*k+14,Y+1550*k,Y+1900*k,'350')
a(f'<text x="{x+1150*k+70}" y="{Y+1900*k+30}" font-size="15" font-weight="700" fill="{A}" text-anchor="end">~1,900 total</text>')
# notes
def card(x,y,w,title,lines):
    h=40+len(lines)*22
    a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/><text x="{x+18}" y="{y+28}" font-size="17" font-weight="700" fill="{T}">{title}</text>')
    for i,l in enumerate(lines): a(f'<text x="{x+18}" y="{y+52+i*22}" font-size="14" fill="{G}">{l}</text>')
card(60,680,520,'Typical sizes used',['Front loader and dryer: about 600 mm wide','Space for a machine: allow about 625 mm','45 L tub cabinet: about 499 mm wide','Slim tubs: 300–310 mm wide'])
card(620,680,520,'Before you build',['New houses need a tub and washer space','Vented dryers must be ducted outside','Floor and wall behind taps: water resistant','Plumbing and power: licensed trades only'])
a(f'<text x="60" y="880" font-size="13" fill="{G}">Planning guide from typical appliance sizes (Fisher &amp; Paykel, Haier, Clark) and NCC Housing Provisions; not building rules. Measure your own machines.</text>')
a('</svg>')
import re
open('z.svg','w').write(re.sub(r'(\d+\.\d{2})\d+',r'\1',''.join(s)))
