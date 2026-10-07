from PIL import Image, ImageDraw, ImageFont
import os
FD=os.path.join(os.path.dirname(os.path.abspath(__file__)),"fonts")
if not os.path.isdir(FD): FD="/home/claude/dsh-pins/fonts"
def dm(sz): return ImageFont.truetype(os.path.join(FD,"DMSerifDisplay-Regular.ttf"),sz)
def pf(sz,w=400):
    f=ImageFont.truetype(os.path.join(FD,"PlayfairDisplay[wght].ttf"),sz)
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f
def fit(d,t,fn,maxw,s):
    while s>24 and d.textlength(t,font=fn(s))>maxw: s-=3
    return fn(s)
def pin_h(src,num,l1,l2,sub,out,anchor=0.5,fade=0.52,top=(252,249,244)):
    W,H=1000,1500
    im=Image.open(src).convert("RGB")
    r=max(W/im.width,H/im.height); im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS)
    x=(im.width-W)//2; y0=int((im.height-H)*anchor); im=im.crop((x,y0,x+W,y0+H)).convert("RGBA")
    from PIL import ImageFilter
    m=Image.new("L",(W,H),0); md=ImageDraw.Draw(m)
    cy=int(H*0.20); rx=int(W*0.42); ry=int(H*0.24)
    md.ellipse([W//2-rx,cy-ry,W//2+rx,cy+ry],fill=int(255*0.90))
    m=m.filter(ImageFilter.GaussianBlur(90))
    ov=Image.new("RGBA",(W,H),top+(0,)); ov.putalpha(m)
    im=Image.alpha_composite(im,ov); d=ImageDraw.Draw(im); cx=W//2
    OL=(78,92,58); DK=(38,33,30); TC=(176,98,52)
    MAXW=int(W*0.70); fn=dm(250); bb=d.textbbox((0,0),num,font=fn,anchor="ls"); nw=bb[2]-bb[0]; nh=bb[3]-bb[1]
    ny=55; d.text((cx,ny+nh),num,font=fn,fill=OL,anchor="ms")
    my=ny+nh*0.55
    for s in (-1,1):
        bx=cx+s*(nw/2+48)
        for (dx1,dy1,dx2,dy2) in ((0,-34,44,-62),(0,0,52,0),(0,34,44,62)):
            d.line([(bx+s*dx1,my+dy1),(bx+s*dx2,my+dy2)],fill=TC,width=6)
    y=ny+nh+48
    f1=fit(d,l1,dm,MAXW,104); d.text((cx,y),l1,font=f1,fill=DK,anchor="mt"); y+=f1.size*1.0
    f2=fit(d,l2,dm,MAXW,104); d.text((cx,y),l2,font=f2,fill=TC,anchor="mt"); y+=f2.size*1.08
    f3=fit(d,sub,lambda s:pf(s,500),MAXW-60,50); d.text((cx,y),sub,font=f3,fill=DK,anchor="mt")
    im.convert("RGB").save(out,"JPEG",quality=86,optimize=True,progressive=True)

def pin_i(src,l1,l2,out,anchor=0.5,pos="top"):
    """Idea pin: full photo of one idea, short centered hook in a soft cream pill."""
    W,H=1000,1500
    im=Image.open(src).convert("RGB")
    r=max(W/im.width,H/im.height); im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS)
    x=(im.width-W)//2; y0=int((im.height-H)*anchor); im=im.crop((x,y0,x+W,y0+H)).convert("RGBA")
    d0=ImageDraw.Draw(im); MAXW=int(W*0.66)
    f1=fit(d0,l1,lambda s:pf(s,500),MAXW,46); f2=fit(d0,l2,dm,MAXW,76)
    w=max(d0.textlength(l1,font=f1),d0.textlength(l2,font=f2))+90
    h=f1.size+f2.size+70
    y=70 if pos=="top" else H-h-80
    ov=Image.new("RGBA",(W,H)); od=ImageDraw.Draw(ov)
    od.rounded_rectangle([W/2-w/2,y,W/2+w/2,y+h],radius=36,fill=(252,249,244,232))
    im=Image.alpha_composite(im,ov); d=ImageDraw.Draw(im)
    d.text((W/2,y+28),l1,font=f1,fill=(38,33,30),anchor="mt")
    d.text((W/2,y+38+f1.size),l2,font=f2,fill=(176,98,52),anchor="mt")
    im.convert("RGB").save(out,"JPEG",quality=86,optimize=True,progressive=True)

def _cover(src,w,h,ax=0.5,ay=0.5):
    im=Image.open(src).convert("RGB")
    r=max(w/im.width,h/im.height); im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS)
    x=int((im.width-w)*ax); y=int((im.height-h)*ay); return im.crop((x,y,x+w,y+h))

def pin_collage(top,bl,br,num,l1,l2,out,ay=(0.5,0.5,0.5)):
    """Collage: one wide photo on top, cream title band, two photos below."""
    W,H,G=1000,1500,10; th=560; bh=H-th-380-2*G; band=380
    c=Image.new("RGB",(W,H),(252,249,244))
    c.paste(_cover(top,W,th,ay=ay[0]),(0,0))
    c.paste(_cover(bl,(W-G)//2,bh,ay=ay[1]),(0,th+band+2*G))
    c.paste(_cover(br,(W-G)//2,bh,ay=ay[2]),((W+G)//2,th+band+2*G))
    d=ImageDraw.Draw(c); OL=(78,92,58); DK=(38,33,30); TC=(176,98,52)
    y0=th+G; d.rectangle([0,y0,W,y0+band],fill=(252,249,244))
    MAXW=int(W*0.80)
    fn=dm(150); bb=d.textbbox((0,0),num,font=fn,anchor="ls"); nh=bb[3]-bb[1]; nw=bb[2]-bb[0]
    yy=y0+34; d.text((W/2,yy+nh),num,font=fn,fill=OL,anchor="ms")
    for s in (-1,1):
        bx=W/2+s*(nw/2+34); my=yy+nh*0.5
        for (a,b,c2,e) in ((0,-22,30,-40),(0,0,36,0),(0,22,30,40)):
            d.line([(bx+s*a,my+b),(bx+s*c2,my+e)],fill=TC,width=5)
    y=yy+nh+26
    f1=fit(d,l1,dm,MAXW,86); d.text((W/2,y),l1,font=f1,fill=DK,anchor="mt"); y+=f1.size*1.02
    f2=fit(d,l2,dm,MAXW,86); d.text((W/2,y),l2,font=f2,fill=TC,anchor="mt")
    c.save(out,"JPEG",quality=86,optimize=True,progressive=True)

def pin_labels(src,l1,l2,labels,out,anchor=0.5):
    """Labeled photo: title glow on top, cream label pills with thin leader lines and dots."""
    from PIL import ImageFilter
    W,H=1000,1500
    im=_cover(src,W,H,ay=anchor).convert("RGBA")
    m=Image.new("L",(W,H),0); md=ImageDraw.Draw(m)
    md.ellipse([W//2-400,-120,W//2+400,420],fill=int(255*0.9)); m=m.filter(ImageFilter.GaussianBlur(80))
    ov=Image.new("RGBA",(W,H),(252,249,244,0)); ov.putalpha(m); im=Image.alpha_composite(im,ov)
    d=ImageDraw.Draw(im); DK=(38,33,30); TC=(176,98,52)
    MAXW=int(W*0.72)
    f1=fit(d,l1,dm,MAXW,92); d.text((W/2,60),l1,font=f1,fill=DK,anchor="mt")
    f2=fit(d,l2,dm,MAXW,92); d.text((W/2,60+f1.size*1.02),l2,font=f2,fill=TC,anchor="mt")
    fl=pf(34,600)
    for text,(px,py),(tx,ty) in labels:
        tw=d.textlength(text,font=fl); w=tw+48; h=64
        x0=px; x1=px+w
        cxp=x0 if tx<x0 else (x1 if tx>x1 else tx); cyp=py+h/2
        d.line([(cxp,cyp),(tx,ty)],fill=(252,249,244),width=4)
        d.rounded_rectangle([x0,py,x1,py+h],radius=32,fill=(252,249,244,240))
        d.text((x0+w/2,py+h/2),text,font=fl,fill=DK,anchor="mm")
        d.ellipse([tx-11,ty-11,tx+11,ty+11],fill=TC,outline=(252,249,244),width=4)
    im.convert("RGB").save(out,"JPEG",quality=86,optimize=True,progressive=True)
