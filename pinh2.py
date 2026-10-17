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
