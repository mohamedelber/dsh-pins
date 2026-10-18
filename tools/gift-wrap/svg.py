T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';W1='#D9B48A';W2='#B98A5E'
s=[];a=s.append
desc=("How to size gift wrap storage. Step 1: measure your longest roll; typical roll widths include 24, 30 and 36 inches. "
"Step 2: an upright bin should be at least two thirds as tall as the roll, for example 20 inches or more for a 30-inch roll. "
"Step 3: a flat under-bed box needs an inside length of at least the roll length plus 1 inch, for example 31 inches or more for a 30-inch roll, and must be lower than the gap under the bed. "
"Gift bags are filed upright by size and tissue paper is stored flat. Keep wrap at least 3 feet from heaters and out of attics and basements.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="gw-t gw-d"><title id="gw-t">How to size gift wrap storage</title><desc id="gw-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">Size Your Gift Wrap Storage</text>')
a(f'<text x="60" y="128" font-size="22" fill="{G}">Measure the longest roll first, then pick a container that fits it</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')

def card(x,y,w,h,n,title):
    a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
    a(f'<circle cx="{x+36}" cy="{y+40}" r="20" fill="{A}"/>')
    a(f'<text x="{x+36}" y="{y+48}" font-size="22" font-weight="700" fill="#FFFFFF" text-anchor="middle">{n}</text>')
    a(f'<text x="{x+68}" y="{y+49}" font-size="25" font-weight="700" fill="{T}">{title}</text>')

def roll(x,y,L,d,fill,vertical=False):
    # roll drawn as rectangle with elliptical end
    if vertical:
        a(f'<rect x="{x-d/2}" y="{y}" width="{d}" height="{L}" fill="{fill}" stroke="{G}" stroke-width="1.5"/>')
        a(f'<ellipse cx="{x}" cy="{y}" rx="{d/2}" ry="{d/5}" fill="{fill}" stroke="{G}" stroke-width="1.5"/>')
        a(f'<ellipse cx="{x}" cy="{y}" rx="{d/5}" ry="{d/12}" fill="{W2}"/>')
    else:
        a(f'<rect x="{x}" y="{y-d/2}" width="{L}" height="{d}" fill="{fill}" stroke="{G}" stroke-width="1.5"/>')
        a(f'<ellipse cx="{x+L}" cy="{y}" rx="{d/5}" ry="{d/2}" fill="{fill}" stroke="{G}" stroke-width="1.5"/>')
        a(f'<ellipse cx="{x+L}" cy="{y}" rx="{d/12}" ry="{d/5}" fill="{W2}"/>')

def dim_h(x1,x2,y,label,col=A):
    a(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{col}" stroke-width="2"/>')
    a(f'<line x1="{x1}" y1="{y-8}" x2="{x1}" y2="{y+8}" stroke="{col}" stroke-width="2"/>')
    a(f'<line x1="{x2}" y1="{y-8}" x2="{x2}" y2="{y+8}" stroke="{col}" stroke-width="2"/>')
    a(f'<text x="{(x1+x2)/2}" y="{y-12}" font-size="18" font-weight="700" fill="{col}" text-anchor="middle">{label}</text>')

def dim_v(x,y1,y2,label,col=A,anchor="start",dx=14):
    a(f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{col}" stroke-width="2"/>')
    a(f'<line x1="{x-8}" y1="{y1}" x2="{x+8}" y2="{y1}" stroke="{col}" stroke-width="2"/>')
    a(f'<line x1="{x-8}" y1="{y2}" x2="{x+8}" y2="{y2}" stroke="{col}" stroke-width="2"/>')
    a(f'<text x="{x+dx}" y="{(y1+y2)/2+6}" font-size="18" font-weight="700" fill="{col}" text-anchor="{anchor}">{label}</text>')

CY=165; CH=440; CW=340
xs=[60,430,800]
# card 1: measure the roll
card(xs[0],CY,CW,CH,1,"Measure the roll")
x=xs[0]
for i,(L,c,lab) in enumerate([(160,SGL,"24 in"),(200,SA,"30 in"),(240,'#E8B9A3',"36 in")]):
    yy=CY+130+i*95
    roll(x+40,yy,L,40,c)
    a(f'<text x="{x+40+L+22}" y="{yy+7}" font-size="20" font-weight="700" fill="{T}">{lab}</text>')
a(f'<text x="{x+30}" y="{CY+405}" font-size="18" fill="{G}">Typical roll widths. Measure</text>')
a(f'<text x="{x+30}" y="{CY+429}" font-size="18" fill="{G}">your longest roll: that is L.</text>')

# card 2: upright bin
card(xs[1],CY,CW,CH,2,"Upright bin")
x=xs[1]; bx=x+70; bw=150; floor=CY+370; bh=150
for k,c in enumerate([SGL,SA,'#E8B9A3',SGL,SA]):
    roll(bx+22+k*27,floor-225,225,24,c,vertical=True)
a(f'<path d="M{bx} {floor-bh} L{bx+bw} {floor-bh} L{bx+bw-10} {floor} L{bx+10} {floor} Z" fill="{W1}" stroke="{W2}" stroke-width="3"/>')
for k in range(1,5):
    a(f'<line x1="{bx+4}" y1="{floor-bh+k*30}" x2="{bx+bw-4}" y2="{floor-bh+k*30}" stroke="{W2}" stroke-width="1.5"/>')
a(f'<line x1="{x+30}" y1="{floor}" x2="{x+CW-30}" y2="{floor}" stroke="{G}" stroke-width="2"/>')
dim_v(bx+bw+24,floor-225,floor,"L",G)
dim_v(bx+bw+70,floor-bh,floor,"2/3 L",A)
a(f'<text x="{x+30}" y="{CY+405}" font-size="18" fill="{G}">At least 2/3 of L tall, e.g.</text>')
a(f'<text x="{x+30}" y="{CY+429}" font-size="18" fill="{G}">20 in+ for 30-inch rolls.</text>')

# card 3: under-bed box
card(xs[2],CY,CW,CH,3,"Under-bed box")
x=xs[2]
# bed frame
a(f'<rect x="{x+25}" y="{CY+120}" width="{CW-50}" height="26" rx="6" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
a(f'<rect x="{x+25}" y="{CY+90}" width="{CW-50}" height="30" rx="8" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<rect x="{x+31}" y="{CY+146}" width="14" height="170" fill="{W2}"/>')
a(f'<rect x="{x+CW-45}" y="{CY+146}" width="14" height="170" fill="{W2}"/>')
a(f'<line x1="{x+20}" y1="{CY+316}" x2="{x+CW-20}" y2="{CY+316}" stroke="{G}" stroke-width="2"/>')
# box
bxx=x+62; bww=230; byy=CY+236; bhh=80
a(f'<rect x="{bxx}" y="{byy}" width="{bww}" height="{bhh}" rx="6" fill="#EAF0F3" fill-opacity="0.9" stroke="{G}" stroke-width="2"/>')
for k,c in enumerate([SGL,SA,'#E8B9A3']):
    roll(bxx+10,byy+22+k*21,200,18,c)
dim_h(bxx,bxx+bww,byy-14,"L + 1 in")
a(f'<text x="{x+30}" y="{CY+381}" font-size="18" fill="{G}">Inside length L + 1 in,</text>')
a(f'<text x="{x+30}" y="{CY+405}" font-size="18" fill="{G}">e.g. 31 in+ for 30-inch rolls;</text>')
a(f'<text x="{x+30}" y="{CY+429}" font-size="18" fill="{G}">must fit the gap under the bed.</text>')

# bottom tips row
TY=640
tips=[("Gift bags","File upright by size:","small, medium, large."),
("Tissue paper","Store flat in a shallow","box or drawer."),
("Where to keep it","Indoors, 3 ft+ from heaters,","not attic or basement.")]
for i,(t,l1,l2) in enumerate(tips):
    tx=xs[i]
    a(f'<rect x="{tx}" y="{TY}" width="{CW}" height="170" rx="16" fill="{SGL if i<2 else "#F6E1D6"}" stroke="{BR}" stroke-width="2"/>')
    a(f'<text x="{tx+26}" y="{TY+52}" font-size="25" font-weight="700" fill="{A if i==2 else T}">{t}</text>')
    a(f'<text x="{tx+26}" y="{TY+98}" font-size="19" fill="{T}">{l1}</text>')
    a(f'<text x="{tx+26}" y="{TY+128}" font-size="19" fill="{T}">{l2}</text>')
a(f'<text x="60" y="868" font-size="16" fill="{G}">2/3 and +1 in are practical rules of thumb. Heater distance: USFA. Avoid attics and basements for paper: Library of Congress.</text>')
a('</svg>')
open('z.svg','w').write('\n'.join(s))
