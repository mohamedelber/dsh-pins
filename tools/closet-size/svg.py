T='#342E2A';A='#C85A32';G='#6E645C';SG='#8FA689';SGL='#CFDDCB';BG='#F7F1E9';W1='#E9D8BE';W2='#B98A5E'
s=[];a=s.append
desc=("Five top-down walk-in closet plans with their smallest comfortable sizes. Each side of hanging clothes needs about 24 inches of depth and the walkway needs about 36 inches, or 24 inches if tight. "
"One wall: 5 feet wide. Two facing walls: 7 feet wide. L-shape: about 5 by 5 feet. U-shape: 7 feet wide. U-shape with a center island: about 12 by 12 feet.")
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 900" font-family="Poppins, sans-serif" role="img" aria-labelledby="wc-t wc-d"><title id="wc-t">Walk-in closet sizes by layout</title><desc id="wc-d">{desc}</desc>')
a(f'<rect width="1200" height="900" fill="{BG}"/>')
a(f'<text x="60" y="84" font-size="44" font-weight="700" fill="{T}">Walk-In Closet Sizes by Layout</text>')
a(f'<text x="60" y="124" font-size="22" fill="{G}">24 in for hanging clothes on each side + a 36 in walkway</text>')
a(f'<text x="1140" y="60" font-size="18" fill="{G}" text-anchor="end">dailyspacehacks.com</text>')
F=22
def plan(cx,top,Wi,Li,kind,name,size):
    k=F/12; w=Wi*k; h=Li*k; x=cx-w/2; y=top; d=24*k
    a(f'<rect x="{x-5}" y="{y-5}" width="{w+10}" height="{h+10}" fill="{W2}"/><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#FBF8F3"/>')
    def band(bx,by,bw,bh): a(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="{SGL}" stroke="{SG}" stroke-width="2"/>')
    if kind=='one': band(x,y,d,h)
    if kind=='two': band(x,y,d,h); band(x+w-d,y,d,h)
    if kind=='L': band(x,y,d,h); band(x+d,y,w-d,d)
    if kind in('U','isl'): band(x,y,d,h); band(x+w-d,y,d,h); band(x+d,y,w-2*d,d)
    if kind=='isl': a(f'<rect x="{cx-12*k}" y="{y+d+36*k}" width="{24*k}" height="{48*k}" rx="4" fill="{W1}" stroke="{W2}" stroke-width="2"/><text x="{cx}" y="{y+d+36*k+24*k+5}" font-size="13" fill="{G}" text-anchor="middle" transform="rotate(-90 {cx} {y+d+36*k+24*k})">island</text>')
    # door gap
    dw=30*k
    dx=(x+d+(w-d-dw)/2) if kind in('one','L') else (cx-dw/2)
    a(f'<rect x="{dx}" y="{y+h-1}" width="{dw}" height="7" fill="{BG}"/><text x="{dx+dw/2}" y="{y+h+22}" font-size="14" fill="{G}" text-anchor="middle">door</text>')
    # aisle arrow across (horizontal) at mid height
    if kind=='one': ax0,ax1=x+d,x+w
    elif kind=='L': ax0,ax1=x+d,x+w
    elif kind=='isl': ax0,ax1=x+d,cx-12*k
    else: ax0,ax1=x+d,x+w-d
    ay=y+h*0.62 if kind!='isl' else y+d+60*k
    a(f'<line x1="{ax0+3}" y1="{ay}" x2="{ax1-3}" y2="{ay}" stroke="{A}" stroke-width="2.5"/><path d="M{ax0+3} {ay} l9 -6 v12 z M{ax1-3} {ay} l-9 -6 v12 z" fill="{A}"/>')
    a(f'<text x="{(ax0+ax1)/2}" y="{ay-9}" font-size="14" font-weight="700" fill="{A}" text-anchor="middle">36 in</text>')
    a(f'<text x="{x+d/2}" y="{y+h*0.3}" font-size="12" fill="#3F5E39" text-anchor="middle" transform="rotate(-90 {x+d/2} {y+h*0.3})">24 in</text>')
    a(f'<text x="{cx}" y="{y+h+52}" font-size="22" font-weight="700" fill="{T}" text-anchor="middle">{name}</text>')
    a(f'<text x="{cx}" y="{y+h+80}" font-size="19" fill="{A}" font-weight="700" text-anchor="middle">{size}</text>')
plan(190,190,60,84,'one','One wall','5 ft wide')
plan(520,190,84,84,'two','Two walls','7 ft wide')
plan(870,190,60,60,'L','L-shape','from 5 x 5 ft')
plan(300,500,84,96,'U','U-shape','7 ft wide')
plan(700,470,144,144,'isl','With an island','about 12 x 12 ft')
a(f'<rect x="1000" y="560" width="26" height="18" fill="{SGL}" stroke="{SG}" stroke-width="2"/><text x="1036" y="575" font-size="17" fill="{T}">clothes, 24 in</text>')
a(f'<line x1="1000" y1="612" x2="1026" y2="612" stroke="{A}" stroke-width="3"/><text x="1036" y="618" font-size="17" fill="{T}">walkway</text>')
a(f'<text x="1000" y="660" font-size="15" fill="{G}">Tight fit: a 24 in</text><text x="1000" y="682" font-size="15" fill="{G}">walkway makes each</text><text x="1000" y="704" font-size="15" fill="{G}">plan 1 ft narrower</text><text x="1000" y="726" font-size="15" fill="{G}">(2 ft with an island).</text>')
a('</svg>')
open('z.svg','w').write(''.join(s))
