T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';W1='#D9B48A';W2='#B98A5E'
s=[];a=s.append
desc=("Two common European laundry layouts drawn from the front, with typical sizes. Side by side: a front-loading washer and a dryer, each about 600 mm wide, "
"sit under one benchtop, so the cupboard needs to be about 1,200 to 1,300 mm wide, or about 1,700 mm with a compact laundry tub. Stacked: the dryer sits on the washer on a stacking kit, "
"so the cupboard can be about 700 mm wide but needs about 1,800 mm of height for the machines. In both layouts allow a cupboard depth of about 650 to 700 mm for the hoses and the door. "
"A vented dryer must be ducted to outside air; condenser and heat pump dryers collect or drain the water instead. Sizes are typical; always check your own appliances.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="el-t el-d"><title id="el-t">European laundry sizes: side by side or stacked</title><desc id="el-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">European Laundry Sizes</text>')
a(f'<text x="60" y="128" font-size="22" fill="{G}">Two common layouts, seen from the front</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
FL=660  # floor y
def washer(x,y,w,h,glass=True,label=''):
    o=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#FFFFFF" stroke="{G}" stroke-width="3"/>'
    o+=f'<rect x="{x+10}" y="{y+10}" width="{w-20}" height="26" rx="4" fill="#F0ECE6"/>'
    o+=f'<circle cx="{x+w-30}" cy="{y+23}" r="8" fill="#FFFFFF" stroke="{G}" stroke-width="2"/>'
    r=min(w,h)*0.3
    if glass:
        o+=f'<circle cx="{x+w/2:.0f}" cy="{y+h*0.58:.0f}" r="{r:.0f}" fill="#DDE7EC" stroke="{G}" stroke-width="4"/><circle cx="{x+w/2:.0f}" cy="{y+h*0.58:.0f}" r="{r*0.7:.0f}" fill="#C9D8DF"/>'
    else:
        o+=f'<circle cx="{x+w/2:.0f}" cy="{y+h*0.58:.0f}" r="{r:.0f}" fill="#FFFFFF" stroke="{G}" stroke-width="4"/>'
    o+=f'<text x="{x+w/2:.0f}" y="{y+h-12:.0f}" font-size="15" fill="{G}" text-anchor="middle">{label}</text>'
    return o
def dimh(x1,x2,y,t):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{A}" stroke-width="3"/><line x1="{x1}" y1="{y-10}" x2="{x1}" y2="{y+10}" stroke="{A}" stroke-width="3"/><line x1="{x2}" y1="{y-10}" x2="{x2}" y2="{y+10}" stroke="{A}" stroke-width="3"/>'
            f'<text x="{(x1+x2)/2:.0f}" y="{y+30}" font-size="19" font-weight="700" fill="{A}" text-anchor="middle">{t}</text>')
# Layout 1: side by side
a(f'<text x="90" y="200" font-size="24" font-weight="700" fill="{T}">1. Side by side</text>')
k=0.25  # px per mm
X=90; ww=round(600*k); hh=round(850*k)
a(f'<rect x="{X-8}" y="{FL-hh-30}" width="{2*ww+16+6}" height="14" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
a(f'<text x="{X+2*ww+20:.0f}" y="{FL-hh-40}" font-size="15" fill="{G}" text-anchor="middle">benchtop</text>')
a(washer(X,FL-hh,ww,hh,True,'washer'))
a(washer(X+ww+6,FL-hh,ww,hh,False,'dryer'))
a(f'<line x1="60" y1="{FL}" x2="560" y2="{FL}" stroke="{T}" stroke-width="4"/>')
a(f'<text x="{X+ww/2:.0f}" y="{FL-hh-48}" font-size="15" fill="{A}" text-anchor="middle" font-weight="700">600 mm each</text>')
a(dimh(X-8,X+2*ww+14,FL+26,'about 1,200–1,300 mm'))
a(f'<text x="{X+2*ww+40}" y="{FL-hh/2:.0f}" font-size="17" fill="{T}">+ compact tub:</text><text x="{X+2*ww+40}" y="{FL-hh/2+24:.0f}" font-size="17" font-weight="700" fill="{T}">about 1,700 mm</text>')
# Layout 2: stacked
X2=720; a(f'<text x="{X2-20}" y="200" font-size="24" font-weight="700" fill="{T}">2. Stacked</text>')
wh=round(850*k)
a(washer(X2,FL-wh,ww,wh,True,'washer'))
a(f'<rect x="{X2-4}" y="{FL-wh-12}" width="{ww+8}" height="10" fill="{G}"/>')
a(washer(X2,FL-2*wh-12,ww,wh,False,'dryer'))
a(f'<text x="{X2+ww+18}" y="{FL-wh-3}" font-size="15" fill="{G}">stacking kit</text>')
a(f'<line x1="{X2-60}" y1="{FL}" x2="1140" y2="{FL}" stroke="{T}" stroke-width="4"/>')
a(dimh(X2-25,X2+ww+25,FL+26,'about 700 mm'))
vx=X2+ww+120; top=FL-2*wh-12
a(f'<line x1="{vx}" y1="{top}" x2="{vx}" y2="{FL}" stroke="{A}" stroke-width="3"/><line x1="{vx-10}" y1="{top}" x2="{vx+10}" y2="{top}" stroke="{A}" stroke-width="3"/><line x1="{vx-10}" y1="{FL}" x2="{vx+10}" y2="{FL}" stroke="{A}" stroke-width="3"/>')
a(f'<text x="{vx+16}" y="{(top+FL)/2-6:.0f}" font-size="19" font-weight="700" fill="{A}">about</text><text x="{vx+16}" y="{(top+FL)/2+18:.0f}" font-size="19" font-weight="700" fill="{A}">1,800 mm</text>')
# notes
ny=FL+150
for i,(h,t) in enumerate([("Depth","Allow about 650–700 mm for hoses and the door"),("Dryer air","Vented dryers must vent to outside air; heat pump dryers need no duct")]):
    x=60+i*550
    a(f'<rect x="{x}" y="{ny-30}" width="530" height="66" rx="12" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
    a(f'<text x="{x+18}" y="{ny-3}" font-size="18" font-weight="700" fill="{T}">{h}</text><text x="{x+18}" y="{ny+22}" font-size="15" fill="{G}">{t}</text>')
a(f'<text x="60" y="{ny+60}" font-size="13" fill="{G}">Typical sizes; check your appliances. Dryer venting: Energy Rating (Australian Government).</text>')
a('</svg>')
open('z.svg','w').write(''.join(s)); print(ny+62)
