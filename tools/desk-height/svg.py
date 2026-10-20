T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#CFDDCB';BG='#F7F1E9';W1='#D9B48A';W2='#B98A5E'
s=[];a=s.append
desc=("Side view of a person sitting at a desk with the ergonomic rules. The desk or keyboard is at elbow height so the elbows bend at about 90 degrees and the forearms are level. "
"The chair is set so the feet are flat on the floor and the thighs are about level. The top of the screen is at or slightly below eye level, about an arm's length away. A table shows desk heights by person height.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="dh-t dh-d"><title id="dh-t">Ergonomic desk height guide</title><desc id="dh-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="84" font-size="44" font-weight="700" fill="{T}">The Right Desk Height</text>')
a(f'<text x="60" y="124" font-size="22" fill="{G}">Desk at elbow height, feet flat, screen at eye level</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
fl=780; k=6.2  # px per inch
def Y(i): return fl-i*k
a(f'<line x1="60" y1="{fl}" x2="700" y2="{fl}" stroke="{W2}" stroke-width="4"/>')
# chair
cx=170; seat=17
a(f'<rect x="{cx}" y="{Y(seat)}" width="110" height="12" rx="5" fill="{SG}"/><rect x="{cx-6}" y="{Y(seat+22)}" width="14" height="{22*k}" rx="6" fill="{SG}"/>')
a(f'<line x1="{cx+55}" y1="{Y(seat)+12}" x2="{cx+55}" y2="{fl-14}" stroke="{G}" stroke-width="7"/><line x1="{cx+15}" y1="{fl-8}" x2="{cx+95}" y2="{fl-8}" stroke="{G}" stroke-width="7"/>')
# desk
dx0=360; desk=26.5
a(f'<rect x="{dx0}" y="{Y(desk)}" width="300" height="12" fill="{W1}"/><line x1="{dx0+15}" y1="{Y(desk)+12}" x2="{dx0+15}" y2="{fl}" stroke="{W2}" stroke-width="8"/><line x1="{dx0+285}" y1="{Y(desk)+12}" x2="{dx0+285}" y2="{fl}" stroke="{W2}" stroke-width="8"/>')
# monitor
eye=48; mx=600
a(f'<rect x="{mx}" y="{Y(eye)}" width="14" height="{14*k}" fill="{T}"/><line x1="{mx+7}" y1="{Y(eye-14)}" x2="{mx+7}" y2="{Y(desk)}" stroke="{G}" stroke-width="6"/><rect x="{mx-20}" y="{Y(desk)-6}" width="54" height="6" fill="{G}"/>')
# person (simple)
hipx=cx+40; hipy=Y(seat+3); knee=(hipx+105,hipy); foot=(hipx+105,fl-6)
sh=(hipx-6,Y(seat+24)); head=(sh[0]+4,Y(seat+31)); elbow=(sh[0]+8,Y(desk+1.5)); hand=(dx0+40,Y(desk+1.5))
P="#E9C46A"
for p1,p2 in [((hipx,hipy),knee),(knee,foot),((hipx,hipy),sh),(sh,elbow),(elbow,hand)]:
    a(f'<line x1="{p1[0]}" y1="{p1[1]}" x2="{p2[0]}" y2="{p2[1]}" stroke="{P}" stroke-width="22" stroke-linecap="round"/>')
a(f'<circle cx="{head[0]}" cy="{head[1]}" r="38" fill="{P}"/><line x1="{foot[0]-10}" y1="{fl-8}" x2="{foot[0]+30}" y2="{fl-8}" stroke="{P}" stroke-width="16" stroke-linecap="round"/>')
# keyboard
a(f'<rect x="{dx0+20}" y="{Y(desk)-8}" width="80" height="8" rx="2" fill="{T}"/>')
# eye line
a(f'<line x1="{head[0]+30}" y1="{Y(eye)}" x2="{mx}" y2="{Y(eye)}" stroke="{SG}" stroke-width="3" stroke-dasharray="10 8"/>')
def lab(x,y,t1,t2,anchor='start'):
    a(f'<text x="{x}" y="{y}" font-size="20" font-weight="700" fill="{A}" text-anchor="{anchor}">{t1}</text><text x="{x}" y="{y+24}" font-size="16" fill="{G}" text-anchor="{anchor}">{t2}</text>')
lab(360,Y(eye)-40,'Top of screen at eye level','about an arm’s length away')
lab(392,Y(desk)+64,'Desk at elbow height','elbows at about 90°')
lab(150,fl+40,'Feet flat, thighs level','raise the chair, add a footrest')
# table
tx=760; ty=200
a(f'<rect x="{tx}" y="{ty}" width="380" height="520" rx="18" fill="#fff" stroke="#E6DCCF" stroke-width="2"/>')
a(f'<text x="{tx+24}" y="{ty+46}" font-size="22" font-weight="700" fill="{T}">Desk height by your height</text>')
a(f'<text x="{tx+24}" y="{ty+86}" font-size="15" font-weight="700" fill="{G}">You</text><text x="{tx+136}" y="{ty+86}" font-size="15" font-weight="700" fill="{G}">Sitting</text><text x="{tx+252}" y="{ty+86}" font-size="15" font-weight="700" fill="{G}">Standing</text>')
rows=[('5 ft 0 in', '22.5-24.5 in', '35.5-37.5 in'), ('5 ft 4 in', '23.5-25.5 in', '37.5-39.5 in'), ('5 ft 8 in', '25.5-27.5 in', '40.5-42.5 in'), ('6 ft 0 in', '26.5-28.5 in', '43-45 in'), ('6 ft 4 in', '28.5-30.5 in', '45.5-47.5 in')]
for i,(h,si,st) in enumerate(rows):
    y=ty+136+i*70
    if i%2==0: a(f'<rect x="{tx+12}" y="{y-36}" width="356" height="56" rx="10" fill="{SGL}" fill-opacity="0.5"/>')
    a(f'<text x="{tx+24}" y="{y}" font-size="17" font-weight="700" fill="{T}">{h}</text><text x="{tx+136}" y="{y}" font-size="16" fill="{A}" font-weight="700">{si}</text><text x="{tx+252}" y="{y}" font-size="16" fill="{A}" font-weight="700">{st}</text>')
a(f'<text x="{tx+24}" y="{ty+490}" font-size="14" fill="{G}">Estimates with normal shoes. Your own</text><text x="{tx+24}" y="{ty+508}" font-size="14" fill="{G}">elbow height is the best guide.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
