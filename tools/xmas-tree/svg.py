T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';SA='#ECCDA0';GR='#4F6B4A'
s=[];a=s.append
desc=("Side view, to scale, of three ways to store a 7.5 foot artificial tree in a closet with a 96 inch (8 foot) ceiling. "
"A rolling duffel bag of about 51 by 15.5 by 23.5 inches lying flat takes 51 inches of floor; stood on end it needs 51 inches of height and a footprint of about 15.5 by 23.5 inches. "
"An upright storage bag with a rolling stand, about 89 inches tall, 50 inches wide and 30 inches deep, keeps the tree assembled but needs a 50 by 30 inch footprint and at least 89 inches of height. "
"Typical section counts: trees of 5 feet and under have 2 sections, 6 to 8 feet have 3, and 9 feet and up have 4 to 5.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="xt-t xt-d"><title id="xt-t">Will your Christmas tree bag fit the closet?</title><desc id="xt-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="80" font-size="42" font-weight="700" fill="{T}">Will the Tree Bag Fit Your Closet?</text>')
a(f'<text x="60" y="116" font-size="21" fill="{G}">Bag sizes for a 7.5 ft tree, drawn to scale against an 8 ft ceiling</text>')
a(f'<text x="1140" y="30" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
k=5.2; floor=700; ceil=floor-96*k
a(f'<rect x="60" y="{ceil-6:.0f}" width="1080" height="6" fill="{BR}"/>')
a(f'<text x="70" y="{ceil+22:.0f}" font-size="15" fill="{G}">8 ft ceiling (96 in)</text>')
a(f'<rect x="60" y="{floor}" width="1080" height="8" fill="#B98A5E"/>')
def bag(x,w,h,label,sub,col=GR):
    a(f'<rect x="{x}" y="{floor-h*k:.1f}" width="{w*k:.1f}" height="{h*k:.1f}" rx="10" fill="{col}" opacity="0.9"/>')
    a(f'<text x="{x+w*k/2:.1f}" y="{floor+40}" font-size="17" font-weight="700" fill="{T}" text-anchor="middle">{label}</text>')
    a(f'<text x="{x+w*k/2:.1f}" y="{floor+64}" font-size="14" fill="{G}" text-anchor="middle">{sub}</text>')
# duffel flat
bag(90,51,23.5,'Duffel, lying flat','51 in of floor, 23.5 in high')
# duffel on end
bag(470,15.5,51,'Duffel, on end','15.5 x 23.5 in footprint')
# upright
bag(800,50,89,'Upright bag','50 x 30 in footprint, 89 in tall','#8FA689')
# tree icon inside upright
cx=800+50*k/2
a(f'<polygon points="{cx:.0f},{floor-86*k:.0f} {cx-22*k:.0f},{floor-8*k:.0f} {cx+22*k:.0f},{floor-8*k:.0f}" fill="{GR}" opacity="0.5"/>')
# dims
a(f'<line x1="{470+15.5*k+14:.0f}" y1="{floor}" x2="{470+15.5*k+14:.0f}" y2="{floor-51*k:.0f}" stroke="{A}" stroke-width="2"/>')
a(f'<text x="{470+15.5*k+22:.0f}" y="{floor-25*k:.0f}" font-size="16" font-weight="700" fill="{A}">51 in</text>')
a(f'<line x1="{800+50*k+14:.0f}" y1="{floor}" x2="{800+50*k+14:.0f}" y2="{floor-89*k:.0f}" stroke="{A}" stroke-width="2"/>')
a(f'<text x="{800+50*k+20:.0f}" y="{floor-45*k:.0f}" font-size="16" font-weight="700" fill="{A}" transform="rotate(-90 {800+50*k+28:.0f} {floor-45*k:.0f})">89 in</text>')
# sections box
a(f'<rect x="90" y="250" width="330" height="150" rx="14" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
a(f'<text x="110" y="284" font-size="18" font-weight="700" fill="{T}">Typical sections by tree height</text>')
for j,t in enumerate(("5 ft and under: 2 sections","6 to 8 ft: 3 sections","9 ft and up: 4 to 5 sections")):
    a(f'<text x="110" y="{318+j*28}" font-size="16" fill="{T}">{t}</text>')
a(f'<text x="60" y="820" font-size="14" fill="{G}">Bag sizes from Home Depot listings (Simple Living Solutions rolling bag; TreeKeeper upright bag with rolling stand). Sections: Treetime.</text>')
a(f'<text x="60" y="842" font-size="14" fill="{G}">Example only: measure your closet and check the bag listing for your tree height and width.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
