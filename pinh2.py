"""New pin templates (Oct 17) based on top-ranking Pinterest pins for our keywords:
idea map (numbered markers on one photo), numbered grid with labels, bold condensed title with hook tags."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
FD=os.path.join(os.path.dirname(os.path.abspath(__file__)),"fonts")
def _var(name,sz,w=None):
    f=ImageFont.truetype(os.path.join(FD,name),sz)
    if w:
        try: f.set_variation_by_axes([w])
        except Exception: pass
    return f
def anton(sz): return ImageFont.truetype(os.path.join(FD,"Anton-Regular.ttf"),sz)
def script(sz,w=700): return _var("DancingScript[wght].ttf",sz,w)
def mont(sz,w=600): return _var("Montserrat[wght].ttf",sz,w)
W,H=1000,1500
INK=(33,30,28); CREAM=(250,246,238); SAGE=(84,118,88); TERRA=(196,92,52); SUN=(246,201,72)
def cover(im,w,h,ax=0.5,ay=0.5):
    r=max(w/im.width,h/im.height); im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS)
    x=int((im.width-w)*ax); y=int((im.height-h)*ay); return im.crop((x,y,x+w,y+h))
def fitf(d,t,fn,maxw,s,minimum=28):
    while s>minimum and d.textlength(t,font=fn(s))>maxw: s-=2
    return fn(s)
def badge(d,x,y,n,r=30,fill=TERRA):
    d.ellipse([x-r,y-r,x+r,y+r],fill=fill,outline=CREAM,width=5)
    d.text((x,y+1),str(n),font=mont(int(r*1.15),800),fill=CREAM,anchor="mm")

def pin_map(photo,top_script,title,markers,out,sub=None,ay=0.5):
    """Idea map: script kicker + bold title, one photo with numbered markers, legend of 6 labels."""
    c=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(c)
    d.text((W/2,40),top_script,font=script(64),fill=TERRA,anchor="mt")
    f=fitf(d,title,anton,920,104); d.text((W/2,118),title,font=f,fill=INK,anchor="mt")
    y0=118+f.size+30
    if sub:
        d.text((W/2,y0-6),sub,font=mont(28,600),fill=SAGE,anchor="mt"); y0+=40
    ph=H-250-y0
    im=Image.open(photo).convert("RGB"); sc=max(W/im.width,ph/im.height)
    pim=cover(im,W,ph,ay=ay); c.paste(pim,(0,y0))
    ox=(im.width*sc-W)/2; oy=(im.height*sc-ph)*ay
    for i,(mx,my,_) in enumerate(markers):
        badge(d,mx*sc-ox,y0+my*sc-oy,i+1,r=32)
    ly=y0+ph+18; colw=W//2
    for i,(_,_,lab) in enumerate(markers):
        cx=40+(i%2)*colw; cy=ly+(i//2)*54
        badge(d,cx+22,cy+24,i+1,r=22)
        d.text((cx+56,cy+24),lab,font=fitf(d,lab,lambda s:mont(s,600),colw-100,30),fill=INK,anchor="lm")
    d.text((W/2,H-26),"dailyspacehacks.com  ·  save for later",font=mont(24,600),fill=SAGE,anchor="mm")
    c.save(out,"JPEG",quality=88,optimize=True,progressive=True)

def pin_grid(imgs,num,script_word,title1,title2,labels,out,footer="Save this for your next reset"):
    """Numbered grid: big number + script word + bold title, 2x3 photo tiles each with a number badge and a label bar."""
    c=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(c)
    d.text((70,40),num,font=anton(190),fill=TERRA,anchor="lt")
    nx=70+d.textlength(num,font=anton(190))+24
    d.text((nx,52),script_word,font=script(70),fill=SAGE,anchor="lt")
    f1=fitf(d,title1,anton,W-nx-50,92); d.text((nx,132),title1,font=f1,fill=INK,anchor="lt")
    f2=fitf(d,title2,anton,W-nx-50,64); d.text((nx,132+f1.size+8),title2,font=f2,fill=INK,anchor="lt")
    top=300; g=10; tw=(W-3*g)//2; th=(H-top-90-2*g)//3
    for i,src in enumerate(imgs[:6]):
        x=g+(i%2)*(tw+g); y=top+(i//2)*(th+g)
        c.paste(cover(Image.open(src).convert("RGB"),tw,th),(x,y))
        d.rectangle([x,y+th-58,x+tw,y+th],fill=(33,30,28))
        d.text((x+tw/2+18,y+th-29),labels[i],font=fitf(d,labels[i],lambda s:mont(s,700),tw-90,30),fill=CREAM,anchor="mm")
        badge(d,x+34,y+th-29,i+1,r=24)
    d.text((W/2,H-52),footer,font=script(42),fill=TERRA,anchor="mm")
    d.text((W/2,H-8),"dailyspacehacks.com",font=mont(20,600),fill=SAGE,anchor="mb")
    c.save(out,"JPEG",quality=88,optimize=True,progressive=True)

def pin_bold(photo,num_line,title2,tag,sticker,out,ay=0.6):
    """Bold hook: full photo, white title card with huge condensed title, terracotta tag line and a yellow sticker."""
    c=cover(Image.open(photo).convert("RGB"),W,H,ay=ay); d=ImageDraw.Draw(c)
    card=[50,70,950,560]
    sh=Image.new("RGBA",(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sh); sd.rounded_rectangle([card[0]+8,card[1]+12,card[2]+8,card[3]+12],28,fill=(0,0,0,90))
    c=Image.alpha_composite(c.convert("RGBA"),sh.filter(ImageFilter.GaussianBlur(14))).convert("RGB"); d=ImageDraw.Draw(c)
    d.rounded_rectangle(card,28,fill=CREAM)
    f1=fitf(d,num_line,anton,820,170); d.text((W/2,110),num_line,font=f1,fill=INK,anchor="mt")
    y=110+f1.size+14
    f2=fitf(d,title2,anton,820,96); d.text((W/2,y),title2,font=f2,fill=INK,anchor="mt"); y+=f2.size+26
    tw=d.textlength(tag,font=mont(38,800))+60
    d.rounded_rectangle([W/2-tw/2,y,W/2+tw/2,y+70],35,fill=TERRA)
    d.text((W/2,y+35),tag,font=mont(38,800),fill=CREAM,anchor="mm")
    # sticker
    s=Image.new("RGBA",(300,300),(0,0,0,0)); sdd=ImageDraw.Draw(s); sdd.ellipse([10,10,290,290],fill=SUN+(255,),outline=INK+(255,),width=6)
    words=sticker.split("\n")
    for i,wd in enumerate(words):
        sdd.text((150,150+(i-(len(words)-1)/2)*58),wd,font=mont(46,800),fill=INK,anchor="mm")
    s=s.rotate(12,resample=Image.BICUBIC)
    c=c.convert("RGBA"); c.alpha_composite(s,(660,card[3]-70)); c=c.convert("RGB"); d=ImageDraw.Draw(c)
    d.rounded_rectangle([W/2-190,H-80,W/2+190,H-30],25,fill=CREAM)
    d.text((W/2,H-55),"dailyspacehacks.com",font=mont(26,700),fill=SAGE,anchor="mm")
    c.save(out,"JPEG",quality=88,optimize=True,progressive=True)

# ---- Cozy grid (Oct 17, user liked a "9 Cozy Small Apartment Ideas" pin) ----
import random, math
def dmserif(sz): return ImageFont.truetype(os.path.join(FD,"DMSerifDisplay-Regular.ttf"),sz)
def play(sz,w=500): return _var("PlayfairDisplay[wght].ttf",sz,w)
PAPER=(246,238,224); BROWN=(58,44,34)
def _torn(w,h,seed=7,rough=10):
    """Cream torn-paper blob as RGBA (w x h)."""
    rnd=random.Random(seed); im=Image.new("RGBA",(w,h),(0,0,0,0)); d=ImageDraw.Draw(im)
    pts=[]; cx,cy=w/2,h/2; n=140
    for i in range(n):
        a=2*math.pi*i/n; rx=w/2-rough*2; ry=h/2-rough*2
        # superellipse for a soft rectangle
        ca,sa=math.cos(a),math.sin(a); e=0.32
        x=cx+rx*math.copysign(abs(ca)**e,ca); y=cy+ry*math.copysign(abs(sa)**e,sa)
        j=rnd.uniform(-rough,rough); pts.append((x+j*ca,y+j*sa))
    d.polygon(pts,fill=PAPER+(255,))
    return im.filter(ImageFilter.GaussianBlur(0.8))
def _leaf(d,x,y,s=1.0,col=BROWN):
    d.line([(x,y),(x+28*s,y-120*s)],fill=col,width=3)
    for k in range(5):
        t=k/5; px=x+28*s*t; py=y-120*s*t
        for side in (-1,1):
            lx=px+side*26*s; ly=py-22*s
            d.ellipse([min(px,lx)-2,ly-8*s,max(px,lx)+2,ly+10*s],outline=col,width=2)
def _heart(d,x,y,s=1.0,col=BROWN):
    pts=[]
    for i in range(60):
        t=2*math.pi*i/60; hx=16*math.sin(t)**3; hy=13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t)
        pts.append((x+hx*s*2.2,y-hy*s*2.2))
    d.line(pts+[pts[0]],fill=col,width=3)
def _warm(im,amt=0.12):
    ov=Image.new("RGB",im.size,(255,196,130)); return Image.blend(im,ov,amt)
def pin_cozy(imgs9,num,word,title1,title2,sub,labels9,out,warm=0.10,ays=None,seed=7):
    """3x3 warm photo grid, torn-paper cream badge (big serif number + title + spaced caps subtitle),
    cream pill labels with dark number circles on tiles 4-9 (1-3 sit under the badge)."""
    c=Image.new("RGB",(W,H),PAPER); g=8; tw=(W-2*g)//3; th=(H-2*g)//3
    for i,src in enumerate(imgs9[:9]):
        x=(i%3)*(tw+g); y=(i//3)*(th+g)
        im=cover(Image.open(src).convert("RGB"),tw,th,ay=(ays[i] if ays else 0.5))
        c.paste(_warm(im,warm) if warm else im,(x,y))
    d=ImageDraw.Draw(c)
    bw,bh=720,520; bx=(W-bw)//2; by=110
    # labels
    for i in range(9):
        x=(i%3)*(tw+g); y=(i//3)*(th+g)
        if i<3: continue
        lab=labels9[i]; words=lab.split(); half=(len(words)+1)//2
        l1=" ".join(words[:half]); l2=" ".join(words[half:])
        f=play(25,500)
        wmax=max(d.textlength(l1,font=f),d.textlength(l2,font=f))
        pw=int(wmax+92); ph=94 if l2 else 54
        lx=x+16; ly=(by+bh+18) if i in (3,4,5) else y+22
        pill=_torn(pw+16,ph+14,seed=seed+i,rough=4); c.paste(pill,(lx-8,ly-7),pill); d=ImageDraw.Draw(c)
        cx,cy=lx+30,ly+ph/2
        d.ellipse([cx-21,cy-21,cx+21,cy+21],fill=BROWN); d.text((cx,cy+1),str(i+1),font=play(26,700),fill=PAPER,anchor="mm")
        d.text((lx+62,ly+(12 if l2 else ph/2)),l1,font=f,fill=BROWN,anchor="la" if l2 else "lm")
        if l2: d.text((lx+62,ly+47),l2,font=f,fill=BROWN,anchor="la")
    # badge
    sh=Image.new("RGBA",(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sh); sd.rounded_rectangle([bx+20,by+24,bx+bw-10,by+bh+10],60,fill=(0,0,0,70))
    c=Image.alpha_composite(c.convert("RGBA"),sh.filter(ImageFilter.GaussianBlur(18)))
    t=_torn(bw,bh,seed=seed,rough=12); c.alpha_composite(t,(bx,by)); c=c.convert("RGB"); d=ImageDraw.Draw(c)
    fnum=dmserif(170); nw=d.textlength(num,font=fnum); fw=dmserif(110); ww=d.textlength(word,font=fw)
    sx=W/2-(nw+18+ww)/2
    d.text((sx,by+185),num,font=fnum,fill=INK,anchor="ls"); d.text((sx+nw+18,by+175),word,font=fw,fill=INK,anchor="ls")
    f1=fitf(d,title1,dmserif,640,92); d.text((W/2,by+285),title1,font=f1,fill=INK,anchor="ms")
    f2=fitf(d,title2,dmserif,640,92); d.text((W/2,by+285+f1.size*0.92),title2,font=f2,fill=INK,anchor="ms")
    ys=by+285+f1.size*0.92+58
    for k,line in enumerate(sub.split("\n")):
        fs=mont(24,500); sp="  ".join(line) if False else line
        txt=" ".join(list(line.upper())).replace("   ","    ")
        fs=fitf(d,txt,lambda s:mont(s,500),600,24)
        d.text((W/2,ys+k*36),txt,font=fs,fill=INK,anchor="ms")
    _heart(d,bx+bw-56,by+bh-60,0.7)
    d.text((W/2,H-18),"dailyspacehacks.com",font=mont(22,600),fill=PAPER,anchor="ms",stroke_width=3,stroke_fill=BROWN)
    c.save(out,"JPEG",quality=88,optimize=True,progressive=True)
