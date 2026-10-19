T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';W1='#D9B48A';W2='#B98A5E'
s=[];a=s.append;SC=2.6;WY=206
def ftin(x):
    f=int(x//12);i=int(round(x-f*12)); return f"{f}'{i}\"" if i else f"{f}'"
P=[("Queen bed",60,80,"8 x 10 ft rug",120,96,8,320),("King bed",76,80,"9 x 12 ft rug",144,108,0,880)]
desc=("Top-down diagram of rug size under a boho bed. A queen bed, 60 by 80 inches, sits on an 8 by 10 foot rug turned sideways, leaving 30 inches of rug on each side and about 24 inches at the foot. "
"A king bed, 76 by 80 inches, sits on a 9 by 12 foot rug, leaving 34 inches on each side and about 28 inches at the foot. Aim for 18 to 24 inches or more of rug showing on the sides and foot. "
"Below is a boho color palette: cream, terracotta, rust, sage, rattan and white oak.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="bo-t bo-d"><title id="bo-t">Rug size under a boho bed</title><desc id="bo-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">What Size Rug Goes Under the Bed?</text>')
a(f'<text x="60" y="128" font-size="22" fill="{G}">The jute or wool rug that anchors a boho bedroom, from above</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
for n,bw,bl,rn,rw,rd,d,cx in P:
    a(f'<line x1="{cx-250}" y1="{WY}" x2="{cx+250}" y2="{WY}" stroke="{W2}" stroke-width="6" stroke-linecap="round"/>')
    ry=WY+d*SC; RW=rw*SC; RD=rd*SC
    a(f'<rect x="{cx-RW/2}" y="{ry}" width="{RW}" height="{RD}" rx="6" fill="#E9D3B0" stroke="{W1}" stroke-width="3"/>')
    a(f'<rect x="{cx-RW/2+10}" y="{ry+10}" width="{RW-20}" height="{RD-20}" rx="4" fill="none" stroke="{W2}" stroke-width="2" stroke-dasharray="6 6" stroke-opacity="0.6"/>')
    BW=bw*SC;BL=bl*SC;bx=cx-BW/2
    for nx in (bx-8-57,bx+BW+8):
        a(f'<rect x="{nx}" y="{WY+4}" width="57" height="47" rx="6" fill="{W1}" stroke="{W2}" stroke-width="2"/>')
    a(f'<rect x="{bx}" y="{WY+2}" width="{BW}" height="{BL}" rx="10" fill="#fff" stroke="{BR}" stroke-width="2"/>')
    a(f'<rect x="{bx}" y="{WY+2}" width="{BW}" height="16" rx="6" fill="{W2}"/>')
    pw=(BW-24)/2
    a(f'<rect x="{bx+8}" y="{WY+26}" width="{pw}" height="36" rx="9" fill="{BG}" stroke="{BR}" stroke-width="2"/><rect x="{bx+16+pw}" y="{WY+26}" width="{pw}" height="36" rx="9" fill="{BG}" stroke="{BR}" stroke-width="2"/>')
    a(f'<rect x="{bx}" y="{WY+2+BL*0.55}" width="{BW}" height="{BL*0.45}" rx="8" fill="{A}" fill-opacity="0.55"/>')
    side=(rw-bw)/2; foot=d+rd-bl
    yy=WY+BL*0.45
    a(f'<line x1="{cx-RW/2}" y1="{yy}" x2="{bx}" y2="{yy}" stroke="{T}" stroke-width="2"/><rect x="{cx-RW/2+(side*SC)/2-30}" y="{yy-26}" width="60" height="24" rx="12" fill="#fff"/><text x="{cx-RW/2+(side*SC)/2}" y="{yy-8}" font-size="15" font-weight="700" fill="{T}" text-anchor="middle">{int(side)} in</text>')
    fy1=WY+2+BL; fy2=ry+RD
    a(f'<line x1="{cx}" y1="{fy1}" x2="{cx}" y2="{fy2}" stroke="{T}" stroke-width="2"/><rect x="{cx+8}" y="{(fy1+fy2)/2-12}" width="64" height="24" rx="12" fill="#fff"/><text x="{cx+40}" y="{(fy1+fy2)/2+6}" font-size="15" font-weight="700" fill="{T}" text-anchor="middle">{int(round(foot))} in</text>')
    a(f'<text x="{cx}" y="534" font-size="24" font-weight="700" fill="{T}" text-anchor="middle">{n} <tspan font-weight="400" font-size="18" fill="{G}">{bw} x {bl} in</tspan></text>')
    a(f'<rect x="{cx-100}" y="550" width="200" height="44" rx="22" fill="{A}"/><text x="{cx}" y="579" font-size="20" font-weight="700" fill="#fff" text-anchor="middle">{rn}</text>')
a(f'<rect x="60" y="626" width="1080" height="64" rx="14" fill="#fff" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="84" y="666" font-size="19" fill="{T}"><tspan font-weight="700" fill="{A}">Rule of thumb:</tspan> let 18 to 24 in or more of rug show on both sides and at the foot of the bed.</text>')
a(f'<text x="60" y="734" font-size="20" font-weight="700" fill="{T}">A simple boho palette</text>')
pal=[("#F3E9DC","Cream"),("#C8643C","Terracotta"),("#A4482A","Rust"),("#9AAE8C","Sage"),("#C9A46A","Rattan"),("#D9BE94","White oak")]
x=60
for c,l in pal:
    a(f'<rect x="{x}" y="752" width="168" height="54" rx="10" fill="{c}" stroke="{BR}" stroke-width="2"/><text x="{x+84}" y="830" font-size="16" fill="{G}" text-anchor="middle">{l}</text>')
    x+=182
a(f'<text x="60" y="874" font-size="15" fill="{G}">Rug sizes and the 18 to 24 in guide from Ruggable and The Citizenry rug guides. Rug placed sideways under the bed, nightstands on the rug.</text>')
a('</svg>')
import re
open('z.svg','w').write(re.sub(r'(\d+\.\d{1,2})\d+',r'\1','\n'.join(s)))
