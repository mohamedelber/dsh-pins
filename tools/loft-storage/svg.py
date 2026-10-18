T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';W1='#D9B48A';W2='#B98A5E';INS='#F2D27A'
s=[];a=s.append
desc=("Cross-section of a loft boarded for storage. Ceiling joists sit on the ceiling below. Insulation fills between the joists and a cross layer goes on top, about 270 mm in total for mineral wool. "
"Loft legs raise the storage boards above the insulation so it is not squashed. A gap is left at the eaves so air can flow and stop condensation. "
"Light storage boxes go on the boards; keep loads light, keep clear of flues, and check with building control before converting the loft into a room.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="lf-t lf-d"><title id="lf-t">How to board a loft for storage</title><desc id="lf-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">Board a Loft for Storage</text>')
a(f'<text x="60" y="128" font-size="22" fill="{G}">Raise the boards so the insulation stays full depth</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
# geometry
CL=640  # ceiling line (top of plasterboard)
L,R=90,1110
apex=(600,170)
# roof
a(f'<path d="M{L-20} {CL-20} L{apex[0]} {apex[1]} L{R+20} {CL-20}" fill="none" stroke="{W2}" stroke-width="14" stroke-linejoin="round"/>')
a(f'<path d="M{L} {CL-20} L{apex[0]} {apex[1]+18} L{R} {CL-20} Z" fill="#FBF7F0"/>')
# ceiling plasterboard
a(f'<rect x="{L-30}" y="{CL}" width="{R-L+60}" height="14" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="{L-30}" y="{CL+44}" font-size="17" fill="{G}">Ceiling of the room below</text>')
# joists (100 mm = 40px) and insulation
J=40; ins1=CL-J; ins_top=CL-108  # 270mm ~ 108px
IX1,IX2=215,985
a(f'<rect x="{IX1}" y="{ins_top}" width="{IX2-IX1}" height="{CL-ins_top}" fill="{INS}" opacity="0.85"/>')
for k in range(9):
    jx=L+60+k*112
    a(f'<rect x="{jx}" y="{ins1}" width="16" height="{J}" fill="{W2}"/>')
# insulation texture
for k in range(0,IX2-IX1-36,26):
    a(f'<path d="M{IX1+6+k} {ins_top+20} q8 -10 16 0 q8 10 16 0" fill="none" stroke="#D9B04F" stroke-width="2"/>')
# legs + boards (walkway between x 330 and 870)
BX1,BX2=345,865; BT=ins_top-30
for k in range(5):
    lx=L+60+(k+2)*112+3
    a(f'<rect x="{lx}" y="{BT+14}" width="10" height="{CL-J-BT-14}" fill="{G}"/>')
a(f'<rect x="{BX1}" y="{BT}" width="{BX2-BX1}" height="14" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
# boxes
for k,(bw,bh) in enumerate([(110,70),(110,70),(110,70),(110,70)]):
    bx=BX1+22+k*125
    a(f'<rect x="{bx}" y="{BT-bh}" width="{bw}" height="{bh}" rx="6" fill="#EAF0F3" stroke="{G}" stroke-width="2"/>')
    a(f'<rect x="{bx-4}" y="{BT-bh-8}" width="{bw+8}" height="10" rx="3" fill="#CFDCE3" stroke="{G}" stroke-width="1.5"/>')
# eaves gaps arrows
for x,dirn in [(120,1),(1080,-1)]:
    a(f'<path d="M{x} {CL-6} q{dirn*30} -20 {dirn*70} -40" fill="none" stroke="{SG}" stroke-width="4" stroke-dasharray="8 6"/>')
    a(f'<path d="M{x+dirn*72} {CL-48} l{-dirn*16} 2 l{dirn*8} 14 z" fill="{SG}"/>')
# callouts
def callout(x1,y1,x2,y2,lines,col=T,anchor="start"):
    a(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{G}" stroke-width="1.5"/>')
    a(f'<circle cx="{x1}" cy="{y1}" r="5" fill="{A}"/>')
    for i,l in enumerate(lines):
        a(f'<text x="{x2+(6 if anchor=="start" else -6)}" y="{y2+5+i*24}" font-size="19" font-weight="{700 if i==0 else 400}" fill="{col if i==0 else G}" text-anchor="{anchor}">{l}</text>')
callout(BX1+400,BT-80,820,260,["Light storage only","clear lidded boxes"],A)
callout(BX1+60,BT+7,330,300,["Boards on loft legs","above the insulation"],T,"end")
callout(L+60+3*112+8,CL-30,520,730,[],T)
a(f'<text x="528" y="752" font-size="19" font-weight="700" fill="{T}">Loft legs stand on the joists</text>')
dx=950
a(f'<line x1="{dx}" y1="{ins_top}" x2="{dx}" y2="{CL}" stroke="{A}" stroke-width="2.5"/>')
a(f'<line x1="{dx-8}" y1="{ins_top}" x2="{dx+8}" y2="{ins_top}" stroke="{A}" stroke-width="2.5"/>')
a(f'<line x1="{dx-8}" y1="{CL}" x2="{dx+8}" y2="{CL}" stroke="{A}" stroke-width="2.5"/>')
a(f'<text x="{dx+12}" y="{ins_top+44}" font-size="19" font-weight="700" fill="{A}">~270 mm</text>')
a(f'<text x="1140" y="{CL+44}" font-size="17" font-weight="700" fill="{SG}" text-anchor="end">Eaves gaps keep air flowing</text>')
# bottom rules row
TY=790
rules=["Do not squash insulation","Keep vents and flues clear","Converting? Ask building control"]
for i,t in enumerate(rules):
    x=60+i*370
    a(f'<rect x="{x}" y="{TY}" width="350" height="54" rx="12" fill="{SGL if i<2 else "#F6E1D6"}" stroke="{BR}" stroke-width="2"/>')
    a(f'<text x="{x+175}" y="{TY+35}" font-size="19" font-weight="700" fill="{A if i==2 else T}" text-anchor="middle">{t}</text>')
a(f'<text x="60" y="878" font-size="16" fill="{G}">270 mm mineral wool and not squashing it: Which?. Light loads, vents and flues: council boarding guidance. Not to scale.</text>')
a('</svg>')
open('z.svg','w').write('\n'.join(s))
