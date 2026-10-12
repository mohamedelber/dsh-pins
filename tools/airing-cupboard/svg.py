T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';W1='#D9B48A';W2='#B98A5E';SA='#ECCDA0'
s=[];a=s.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="ac-t ac-d"><title id="ac-t">Airing cupboard shelves layout guide</title><desc id="ac-d">Front view of an airing cupboard with a hot water cylinder on the floor and slatted shelves above it, split into four zones. Zone 1, keep clear: the cylinder, its pipes, valves and the immersion heater switch need space around them so they can be reached. Zone 2, warm shelf: the shelf just above the cylinder is for finishing off items that are only slightly damp. Zone 3, everyday: towels and bedding you use every week. Zone 4, top shelf: spare duvets and pillows in breathable cotton bags. Tips: use slatted shelves with small gaps and do not cover them with boards, do not put soaking wet items inside, and fit an insulation jacket at least 80 mm thick if the cylinder needs one.</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">Airing Cupboard Shelves Guide</text>')
a(f'<text x="60" y="130" font-size="22" fill="{G}">What goes where, from the cylinder up</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
# cupboard frame
X0,X1,Y0,FL=110,560,170,690
a(f'<rect x="{X0-14}" y="{Y0-14}" width="{X1-X0+28}" height="{FL-Y0+14}" rx="6" fill="#FBF6EF" stroke="{BR}" stroke-width="3"/>')
a(f'<rect x="{X0}" y="{Y0}" width="{X1-X0}" height="{FL-Y0}" fill="#FFFDF9" stroke="{BR}" stroke-width="2"/>')
a(f'<line x1="{X0-30}" y1="{FL}" x2="{X1+30}" y2="{FL}" stroke="{T}" stroke-width="4"/>')
# cylinder
cx,cw,ch=140,150,230
a(f'<rect x="{cx}" y="{FL-ch}" width="{cw}" height="{ch}" rx="40" fill="#FFFFFF" stroke="{G}" stroke-width="3"/>')
a(f'<text x="{cx+cw/2}" y="{FL-ch/2+6}" font-size="16" fill="{G}" text-anchor="middle">cylinder</text>')
for px in (cx+40,cx+110):
    a(f'<line x1="{px}" y1="{FL-ch}" x2="{px}" y2="{Y0}" stroke="{W2}" stroke-width="7"/>')
a(f'<rect x="{cx+cw+14}" y="{FL-150}" width="26" height="26" rx="4" fill="{SGL}" stroke="{G}" stroke-width="2"/>')
# keep clear dashed zone
a(f'<rect x="{cx-14}" y="{FL-ch-24}" width="{cw+70}" height="{ch+20}" rx="16" fill="none" stroke="{A}" stroke-width="3" stroke-dasharray="10 8"/>')
# shelves (slatted) across right side and above
def shelf(y,x0,x1):
    for i in range(int((x1-x0)/26)):
        a(f'<rect x="{x0+i*26+2}" y="{y}" width="20" height="10" rx="2" fill="{W1}" stroke="{W2}" stroke-width="1"/>')
ys=[FL-ch-60, FL-ch-140, Y0+75]
for y in ys: shelf(y,X0+4,X1-4)

# stacks
def stack(x,y,n,c1,c2,w=80):
    for i in range(n):
        a(f'<rect x="{x}" y="{y-14*(i+1)}" width="{w}" height="13" rx="4" fill="{c1 if i%2==0 else c2}" stroke="{BR}" stroke-width="1"/>')
stack(330,ys[0],3,'#FFFFFF',SGL); stack(430,ys[0],2,'#FFFFFF','#F3E7D6')
stack(140,ys[1],4,SGL,'#FFFFFF'); stack(250,ys[1],4,'#FFFFFF',SA); stack(360,ys[1],3,SGL,'#FFFFFF'); stack(460,ys[1],4,'#FFFFFF',SGL)
a(f'<rect x="150" y="{ys[2]-58}" width="150" height="56" rx="18" fill="#F3E7D6" stroke="{BR}" stroke-width="2"/><rect x="330" y="{ys[2]-50}" width="120" height="48" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')

# badges
for n,(bx,by) in enumerate([(cx+cw+60,FL-40),(X1+28,ys[0]-20),(X1+28,ys[1]-30),(X1+28,ys[2]-30)],1):
    a(f'<circle cx="{bx}" cy="{by}" r="17" fill="{T}"/><text x="{bx}" y="{by+7}" font-size="18" font-weight="700" fill="#FFFFFF" text-anchor="middle">{n}</text>')
cards=[("Keep clear","Cylinder, pipes, valves and switch."),("Warm shelf","Finish off slightly damp items."),("Everyday","Towels and bedding you use weekly."),("Top shelf","Spare duvets in cotton bags.")]
for i,(t1,t2) in enumerate(cards):
    y=170+i*128
    a(f'<rect x="640" y="{y}" width="500" height="114" rx="14" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
    a(f'<circle cx="678" cy="{y+42}" r="19" fill="{T}"/><text x="678" y="{y+49}" font-size="20" font-weight="700" fill="#FFFFFF" text-anchor="middle">{i+1}</text>')
    a(f'<text x="712" y="{y+50}" font-size="22" font-weight="700" fill="{T}">{t1}</text><text x="712" y="{y+82}" font-size="17" fill="{G}">{t2}</text>')
a(f'<rect x="60" y="730" width="1080" height="100" rx="14" fill="{SGL}" stroke="{SG}" stroke-width="2"/><rect x="60" y="730" width="10" height="100" rx="5" fill="{SG}"/>')
a(f'<text x="96" y="771" font-size="20" fill="{T}"><tspan font-weight="700">Keep air moving:</tspan> slatted shelves, never covered with boards;</text>')
a(f'<text x="96" y="805" font-size="20" fill="{T}">no soaking wet items; cylinder jacket at least 80 mm thick.</text>')
a(f'<text x="60" y="872" font-size="14" fill="{G}">Airing tips: Viessmann UK. Jacket thickness: Energy Saving Trust. Zones: our rule of thumb; follow your cylinder and boiler manuals.</text>')
a('</svg>')
import re
svg=re.sub(r'(\d+\.\d{2,})',lambda m:str(round(float(m.group(1)),1)),''.join(s))
open('z.svg','w').write(svg)
