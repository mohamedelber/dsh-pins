T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#CFDDCB';BG='#F7F1E9';W1='#E9D8BE';W2='#B98A5E'
s=[];a=s.append
desc=("Top view of a 16 by 14 foot kitchen with an L-shaped run of cabinets and an island. The work aisle between the cabinets and the island is 42 inches for one cook or 48 inches for two. "
"The island is 48 inches deep including a 15 inch overhang, with stools 24 inches apart on the far side and 44 inches behind the stools so people can walk past. A 36 inch walkway runs around the open end.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="ki-t ki-d"><title id="ki-t">Kitchen island clearances</title><desc id="ki-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="84" font-size="44" font-weight="700" fill="{T}">Kitchen Island Clearances</text>')
a(f'<text x="60" y="124" font-size="22" fill="{G}">The spacing that makes an island work, from the NKBA guidelines</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
k=3.6
X0=110; Y0=170; L=192; W=168
def X(i): return X0+i*k
def Y(i): return Y0+i*k
a(f'<rect x="{X0}" y="{Y0}" width="{L*k}" height="{W*k}" fill="#FBF8F3" stroke="{T}" stroke-width="3"/>')
CD=25
a(f'<rect x="{X0}" y="{Y0}" width="{L*k}" height="{CD*k}" fill="{SGL}" stroke="{SG}" stroke-width="2"/><rect x="{X0}" y="{Y(CD)}" width="{CD*k}" height="{(W-CD)*k}" fill="{SGL}" stroke="{SG}" stroke-width="2"/>')
a(f'<text x="{X(L/2)}" y="{Y(CD/2)+7}" font-size="18" fill="#3F5E39" text-anchor="middle">cabinets and counter, 25 in deep</text>')
ix=CD+42; iy=CD+42; il=84; idp=48
a(f'<rect x="{X(ix)}" y="{Y(iy)}" width="{il*k}" height="{idp*k}" rx="6" fill="{W1}" stroke="{W2}" stroke-width="2.5"/>')
a(f'<line x1="{X(ix)}" y1="{Y(iy+33)}" x2="{X(ix+il)}" y2="{Y(iy+33)}" stroke="{W2}" stroke-width="2" stroke-dasharray="7 6"/>')
a(f'<text x="{X(ix+il/2)}" y="{Y(iy+16)+7}" font-size="19" font-weight="700" fill="{T}" text-anchor="middle">island 7 ft x 48 in</text>')
a(f'<text x="{X(ix+il/2)}" y="{Y(iy+41)+6}" font-size="15" fill="{G}" text-anchor="middle">15 in overhang</text>')
for j in range(3):
    cx=X(ix+12+24*j+6); a(f'<circle cx="{cx}" cy="{Y(iy+idp+9)}" r="{8*k}" fill="#fff" stroke="{W2}" stroke-width="2.5"/>')
a(f'<text x="{X(ix+2)}" y="{Y(iy+idp+25)}" font-size="16" fill="{G}">24 in per stool</text>')
def dim(x1,y1,x2,y2,label,lx,ly,anchor='middle'):
    a(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{A}" stroke-width="3"/>')
    a(f'<circle cx="{x1}" cy="{y1}" r="4" fill="{A}"/><circle cx="{x2}" cy="{y2}" r="4" fill="{A}"/>')
    a(f'<text x="{lx}" y="{ly}" font-size="18" font-weight="700" fill="{A}" text-anchor="{anchor}">{label}</text>')
mx=X(ix+80)
dim(mx,Y(CD),mx,Y(iy),'42 to 48 in work aisle',mx-12,Y(CD+24),'end')
dim(mx,Y(iy+idp),mx,Y(W),'44 in behind stools',mx-12,Y(iy+idp+42),'end')
dim(X(CD),Y(iy+20),X(ix),Y(iy+20),'42 in',X(CD+(ix-CD)/2),Y(iy+20)-10)
dim(X(ix+il),Y(iy+20),X(L),Y(iy+20),'36 in+',X(ix+il+(L-ix-il)/2),Y(iy+20)-10)
bx=X0+L*k+40
items=[("Work aisle","42 in for one cook, 48 in for two"),("Walkway","at least 36 in"),("Behind stools","44 in to walk past"),("Each stool","24 in of counter"),("Knee space","15 in at 36 in high")]
for i,(t1,t2) in enumerate(items):
    y=190+i*112
    a(f'<rect x="{bx}" y="{y}" width="{1140-bx}" height="96" rx="14" fill="#fff" stroke="#E6DCCF" stroke-width="2"/>')
    a(f'<text x="{bx+22}" y="{y+40}" font-size="21" font-weight="700" fill="{T}">{t1}</text><text x="{bx+22}" y="{y+72}" font-size="17" fill="{A}" font-weight="700">{t2}</text>')
a(f'<text x="{X0}" y="{Y0+W*k+44}" font-size="18" fill="{G}">Example: a 16 x 14 ft kitchen with L-shaped cabinets. Sizes are minimums; more space feels better.</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
