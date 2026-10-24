T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0'
lo,hi=35,45; cube=13/12
cl,ch=lo*cube,hi*cube
s=[];a=s.append
desc=(f"Left: records stored the right way, standing upright with full-height dividers every 4 to 6 inches, compared with records leaning at an angle or stacked flat, which can warp them. "
f"Right: the Library of Congress puts LPs at 35 to 45 pounds per shelf-foot, so a full 13-inch cube holds about {cl:.0f} to {ch:.0f} pounds by our estimate, against IKEA's listed 29 pound maximum load per KALLAX shelf, and a 3-foot shelf about {lo*3} to {hi*3} pounds. "
"Library of Congress storage conditions: a steady 65 to 70 degrees F and 45 to 50 percent relative humidity, away from sunlight and heat.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="vr-t vr-d"><title id="vr-t">How to store vinyl records: upright, supported and cool</title><desc id="vr-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="42" font-weight="700" fill="{T}">Storing Vinyl, by the Numbers</text>')
a(f'<text x="60" y="116" font-size="21" fill="{G}">How records should stand, and how much they weigh</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
# left panel
a(f'<rect x="60" y="150" width="520" height="620" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="84" y="190" font-size="21" font-weight="700" fill="{T}">Upright, with dividers</text>')
cols=['#C85A32','#8FA689','#E8B04A','#6E645C','#B98A5E','#DCE5D6']
x0,yb=100,400
a(f'<rect x="{x0-10}" y="{yb}" width="460" height="10" fill="#B98A5E"/>')
x=x0;i=0
for grp in range(3):
    for k in range(9):
        a(f'<rect x="{x}" y="{yb-170}" width="12" height="170" fill="{cols[(i)%6]}" stroke="#FFFFFF" stroke-width="1"/>'); x+=13;i+=1
    a(f'<rect x="{x}" y="{yb-178}" width="8" height="178" fill="{T}"/>'); x+=12
a(f'<line x1="{x0+121}" y1="{yb+30}" x2="{x0+254}" y2="{yb+30}" stroke="{A}" stroke-width="2"/>')
a(f'<text x="{x0+186}" y="{yb+56}" font-size="15" font-weight="700" fill="{A}" text-anchor="middle">dividers 4 to 6 in apart</text>')
a(f'<text x="{x0+400}" y="{yb-60}" font-size="40" font-weight="700" fill="{SG}" text-anchor="middle">✓</text>')
# bad
yb2=650
a(f'<text x="84" y="500" font-size="21" font-weight="700" fill="{T}">Leaning or stacked flat</text>')
a(f'<rect x="{x0-10}" y="{yb2}" width="460" height="10" fill="#B98A5E"/>')
for k in range(6):
    xx=x0+k*14
    a(f'<rect x="{xx}" y="{yb2-125}" width="12" height="125" fill="{cols[k%6]}" transform="rotate(22 {xx} {yb2})"/>')
for k in range(6):
    a(f'<rect x="{x0+230}" y="{yb2-12-k*13}" width="170" height="12" fill="{cols[k%6]}" stroke="#FFFFFF" stroke-width="1"/>')
a(f'<text x="{x0+430}" y="{yb2-60}" font-size="40" font-weight="700" fill="{A}" text-anchor="middle">✗</text>')
a(f'<text x="84" y="{yb2+50}" font-size="15" fill="{G}">Both put uneven weight on the discs and can warp them</text>')
a(f'<text x="84" y="{yb2+74}" font-size="15" fill="{G}">(Library of Congress; U.S. and Australian National Archives)</text>')
# right panel
a(f'<rect x="620" y="150" width="520" height="380" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="644" y="190" font-size="21" font-weight="700" fill="{T}">How much LPs weigh</text>')
a(f'<text x="644" y="216" font-size="15" fill="{G}">35 to 45 lb per shelf-foot (Library of Congress)</text>')
BX=644;MX=140;BW=330
rows=[('13-in cube, full',cl,ch,SA),('3-ft shelf, full',lo*3,hi*3,SA)]
yy=262
for n,l,h,c in rows:
    a(f'<text x="{BX}" y="{yy}" font-size="17" font-weight="700" fill="{T}">{n}</text>')
    a(f'<rect x="{BX}" y="{yy+12}" width="{BW*l/MX:.1f}" height="34" rx="6" fill="{c}"/>')
    a(f'<rect x="{BX+BW*l/MX:.1f}" y="{yy+12}" width="{BW*(h-l)/MX:.1f}" height="34" fill="{A}" opacity="0.55"/>')
    a(f'<text x="{BX+BW*h/MX+12:.1f}" y="{yy+36}" font-size="19" font-weight="700" fill="{T}">{l:.0f}-{h:.0f} lb</text>')
    yy+=86
x29=BX+BW*29/MX
a(f'<line x1="{x29:.1f}" y1="268" x2="{x29:.1f}" y2="{268+46}" stroke="{T}" stroke-width="2" stroke-dasharray="6 4"/>')
a(f'<text x="{x29+6:.1f}" y="{268+66}" font-size="14" fill="{T}">29 lb: IKEA max load per KALLAX shelf</text>')
a(f'<text x="644" y="{yy+30}" font-size="14" fill="{G}">Cube and shelf totals: our estimate from the LoC figure.</text>')
# conditions
a(f'<rect x="620" y="550" width="520" height="220" rx="16" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="644" y="590" font-size="21" font-weight="700" fill="{T}">Where to keep them</text>')
for j,(t1,c) in enumerate((("Steady 65 to 70°F, 45 to 50% humidity",SG),("Out of sunlight, away from heat",'#E8B04A'),("Not in the attic or garage",A),("Off the floor, never in a hot car",'#B98A5E'))):
    a(f'<rect x="644" y="{612+j*38}" width="8" height="26" rx="3" fill="{c}"/><text x="664" y="{631+j*38}" font-size="17" fill="{T}">{t1}</text>')
a(f'<text x="60" y="820" font-size="14" fill="{G}">Sources: Library of Congress; U.S. National Archives; National Archives of Australia; IKEA KALLAX product page.</text>')
a(f'<text x="60" y="842" font-size="14" fill="{G}">Example only: check the rated load of your own shelf before filling it.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
print(round(cl,1),round(ch,1))
