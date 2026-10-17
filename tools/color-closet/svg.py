T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#DCE5D6';BG='#F7F1E9';BR='#D8CBBB';W2='#B98A5E'
cols=[("White","#FFFFFF"),("Cream","#F3E9D2"),("Beige","#D9C3A0"),("Pink","#E8A7B5"),("Red","#C0392B"),("Orange","#E07B39"),("Yellow","#E9C46A"),("Green","#7FA37A"),("Blue","#5B8DB8"),("Navy","#2C3E62"),("Purple","#7D5A8C"),("Grey","#9A9A9A"),("Brown","#7A5536"),("Black","#262626")]
s=[];a=s.append
desc=("Recommended color coded closet order on one hanging rail, left to right: "+", ".join(c for c,_ in cols)+
". Three ways to use it: rainbow order with neutrals at both ends; light to dark, which matches the KonMari advice that colors get lighter from left to right if reversed; and category first, then color inside each category.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="cc-t cc-d"><title id="cc-t">Color coded closet order</title><desc id="cc-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="88" font-size="44" font-weight="700" fill="{T}">The Color Coded Closet Order</text>')
a(f'<text x="60" y="128" font-size="22" fill="{G}">Hang from left to right: light neutrals, the rainbow, dark neutrals</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
# rail
RY=200
a(f'<rect x="50" y="{RY-6}" width="1100" height="12" rx="6" fill="{W2}"/>')
n=len(cols); x0=78; step=(1100-56)/(n-1)
for i,(nm,c) in enumerate(cols):
    x=x0+i*step
    # hanger hook + shoulders
    a(f'<path d="M{x} {RY+6} q0 -22 10 -22" fill="none" stroke="{G}" stroke-width="3"/>')
    a(f'<path d="M{x} {RY+6} L{x-30} {RY+34} L{x+30} {RY+34} Z" fill="none" stroke="{W2}" stroke-width="4" stroke-linejoin="round"/>')
    # shirt shape
    w=60; top=RY+32; h=230
    stroke=BR if c in ("#FFFFFF","#F3E9D2") else c
    a(f'<path d="M{x-w/2} {top} L{x-w/2-12} {top+40} L{x-w/2} {top+52} L{x-w/2} {top+h} L{x+w/2} {top+h} L{x+w/2} {top+52} L{x+w/2+12} {top+40} L{x+w/2} {top} Z" fill="{c}" stroke="{stroke}" stroke-width="2"/>')
    a(f'<text x="{x}" y="{top+h+34}" font-size="17" fill="{T}" text-anchor="middle" font-weight="600">{nm}</text>')
# bracket labels
by=RY+330
def brace(x1,x2,label,col):
    a(f'<path d="M{x1} {by} v12 h{x2-x1} v-12" fill="none" stroke="{col}" stroke-width="3"/>')
    a(f'<text x="{(x1+x2)/2}" y="{by+42}" font-size="19" font-weight="700" fill="{col}" text-anchor="middle">{label}</text>')
brace(x0-34,x0+2*step+34,"light neutrals",G)
brace(x0+3*step-34,x0+10*step+34,"rainbow order: red, orange, yellow, green, blue, purple",A)
brace(x0+11*step-34,x0+13*step+34,"dark neutrals",G)
# three methods
my=640
boxes=[("1  Rainbow","Neutrals at both ends,","colors in rainbow order.","Best for colorful wardrobes."),
("2  Light to dark","One smooth gradient.","Reverse it for the KonMari","look: lighter to the right."),
("3  Category first","Tops, pants, dresses,","then color inside each","group. Easiest to keep.")]
bw=340
for i,(t,l1,l2,l3) in enumerate(boxes):
    bx=60+i*(bw+30)
    a(f'<rect x="{bx}" y="{my}" width="{bw}" height="170" rx="14" fill="#FFFFFF" stroke="{BR}" stroke-width="2"/>')
    a(f'<text x="{bx+24}" y="{my+46}" font-size="25" font-weight="700" fill="{A if i==2 else T}">{t}</text>')
    for k,l in enumerate((l1,l2,l3)):
        a(f'<text x="{bx+24}" y="{my+88+k*28}" font-size="19" fill="{G}">{l}</text>')
a(f'<text x="60" y="868" font-size="16" fill="{G}">Rainbow order follows the visible spectrum (IAU Office of Astronomy for Education). Light-to-dark tip: KonMari.</text>')
a('</svg>')
open('z.svg','w').write('\n'.join(s))
