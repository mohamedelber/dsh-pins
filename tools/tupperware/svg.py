T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';W1='#D9B48A';W2='#B98A5E'
s=[];a=s.append
desc=("Top-down map of a kitchen drawer organized for food storage containers. Zone A along the back: lids filed upright in a divider, largest at the left. "
"Zone B front left: rectangular containers nested largest to smallest. Zone C: square containers nested. Zone D: round containers nested. "
"Zone E along the front: an everyday set with lids on for lunches and leftovers. Rules: every base needs a matching lid, nest by shape, "
"file lids upright by size, and keep only what fits.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="tw-t tw-d"><title id="tw-t">The container drawer map</title><desc id="tw-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">The Container Drawer Map</text>')
a(f'<text x="60" y="128" font-size="22" fill="{G}">One drawer or cabinet shelf, five zones, no more lid hunting</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
# drawer box (top-down)
X,Y,DW,DH=60,170,660,600
a(f'<rect x="{X-14}" y="{Y-14}" width="{DW+28}" height="{DH+28}" rx="10" fill="{W2}"/>')
a(f'<rect x="{X}" y="{Y}" width="{DW}" height="{DH}" rx="4" fill="#FBF7F1"/>')
a(f'<text x="{X+DW/2}" y="{Y+DH+50}" font-size="18" fill="{G}" text-anchor="middle">front of drawer (you stand here)</text>')
# zone A lids file at back
ay=Y+20; ah=120
a(f'<rect x="{X+20}" y="{ay}" width="{DW-40}" height="{ah}" rx="6" fill="{SGL}" stroke="{SG}" stroke-width="2"/>')
x=X+40
for i in range(16):
    w=10; h=96-i*3
    a(f'<rect x="{x}" y="{ay+(ah-h)/2}" width="{w}" height="{h}" rx="3" fill="{SG if i%2==0 else "#A9BBA4"}"/>')
    x+=w+40 if i in (5,11) else w+20
a(f'<line x1="{X+20}" y1="{ay+ah+18}" x2="{X+DW-20}" y2="{ay+ah+18}" stroke="{W1}" stroke-width="8" stroke-linecap="round"/>')
# zones B C D
zy=ay+ah+40; zh=250
def nest_rect(cx,cy,w,h,n,col):
    for i in range(n):
        k=1-i*0.2
        a(f'<rect x="{cx-w*k/2}" y="{cy-h*k/2}" width="{w*k}" height="{h*k}" rx="{10*k+2}" fill="none" stroke="{col}" stroke-width="4"/>')
def nest_circ(cx,cy,r,n,col):
    for i in range(n):
        a(f'<circle cx="{cx}" cy="{cy}" r="{r*(1-i*0.22)}" fill="none" stroke="{col}" stroke-width="4"/>')
bw=(DW-80)/3
for j in range(3):
    bx=X+20+j*(bw+20)
    a(f'<rect x="{bx}" y="{zy}" width="{bw}" height="{zh}" rx="6" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
cxs=[X+20+bw/2+j*(bw+20) for j in range(3)]
nest_rect(cxs[0],zy+70,150,95,4,A); nest_rect(cxs[0],zy+185,150,95,4,A)
nest_rect(cxs[1],zy+70,110,110,4,W2); nest_rect(cxs[1],zy+185,110,110,3,W2)
nest_circ(cxs[2],zy+70,55,4,G); nest_circ(cxs[2],zy+185,55,3,G)
# zone E front
ey=zy+zh+20; eh=DH-(ey-Y)-20
a(f'<rect x="{X+20}" y="{ey}" width="{DW-40}" height="{eh}" rx="6" fill="{SA}" fill-opacity="0.45" stroke="{W1}" stroke-width="2"/>')
for i in range(4):
    ex=X+40+i*140
    a(f'<rect x="{ex}" y="{ey+15}" width="120" height="{eh-30}" rx="10" fill="#FFFFFF" stroke="{A}" stroke-width="3"/>')
    a(f'<rect x="{ex+8}" y="{ey+23}" width="104" height="{eh-46}" rx="7" fill="{SGL}"/>')
# markers
def mk(x,y,l):
    a(f'<circle cx="{x}" cy="{y}" r="22" fill="{A}"/><text x="{x}" y="{y+8}" font-size="22" font-weight="700" fill="#fff" text-anchor="middle">{l}</text>')
mk(X+DW-36,ay+22,'A'); mk(X+20+bw-6,zy+22,'B'); mk(X+40+2*bw-6,zy+22,'C'); mk(X+60+3*bw-6,zy+22,'D'); mk(X+DW-36,ey+eh/2,'E')
# legend
LX=780
items=[("A","Lids, filed upright","largest at the left, so the","right size is easy to spot"),
("B","Rectangles, nested","biggest at the bottom,","two stacks side by side"),
("C","Squares, nested","one shape family","per section"),
("D","Rounds, nested","bowls and soup tubs","fit inside each other"),
("E","Everyday set, lids on","lunch and leftover boxes","you grab most often")]
ly=200
for l,t1,t2,t3 in items:
    a(f'<circle cx="{LX+22}" cy="{ly}" r="20" fill="{A}"/><text x="{LX+22}" y="{ly+7}" font-size="20" font-weight="700" fill="#fff" text-anchor="middle">{l}</text>')
    a(f'<text x="{LX+56}" y="{ly+7}" font-size="23" font-weight="700" fill="{T}">{t1}</text>')
    a(f'<text x="{LX+56}" y="{ly+36}" font-size="18" fill="{G}">{t2}</text>')
    a(f'<text x="{LX+56}" y="{ly+60}" font-size="18" fill="{G}">{t3}</text>')
    ly+=104
a(f'<rect x="{LX}" y="{ly-20}" width="360" height="86" rx="12" fill="{SGL}"/>')
a(f'<text x="{LX+20}" y="{ly+14}" font-size="19" font-weight="700" fill="{T}">Match test: every base</text>')
a(f'<text x="{LX+20}" y="{ly+44}" font-size="19" font-weight="700" fill="{T}">needs a lid, or it goes</text>')
a(f'<text x="60" y="868" font-size="16" fill="{G}">Works the same on a cabinet shelf: lids at the back, nested bases in the middle, everyday set at the front.</text>')
a('</svg>')
open('z.svg','w').write('\n'.join(s))
