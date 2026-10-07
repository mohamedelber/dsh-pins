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
    cy=int(H*0.20); rx=int(W*0.50); ry=int(H*0.24)
    md.ellipse([W//2-rx,cy-ry,W//2+rx,cy+ry],fill=int(255*0.90))
    m=m.filter(ImageFilter.GaussianBlur(90))
    ov=Image.new("RGBA",(W,H),top+(0,)); ov.putalpha(m)
    im=Image.alpha_composite(im,ov); d=ImageDraw.Draw(im); cx=W//2
    OL=(78,92,58); DK=(38,33,30); TC=(176,98,52)
    fn=dm(300); bb=d.textbbox((0,0),num,font=fn,anchor="ls"); nw=bb[2]-bb[0]; nh=bb[3]-bb[1]
    ny=55; d.text((cx,ny+nh),num,font=fn,fill=OL,anchor="ms")
    my=ny+nh*0.55
    for s in (-1,1):
        bx=cx+s*(nw/2+48)
        for (dx1,dy1,dx2,dy2) in ((0,-34,44,-62),(0,0,52,0),(0,34,44,62)):
            d.line([(bx+s*dx1,my+dy1),(bx+s*dx2,my+dy2)],fill=TC,width=6)
    y=ny+nh+48
    f1=fit(d,l1,dm,W-80,120); d.text((cx,y),l1,font=f1,fill=DK,anchor="mt"); y+=f1.size*1.0
    f2=fit(d,l2,dm,W-80,120); d.text((cx,y),l2,font=f2,fill=TC,anchor="mt"); y+=f2.size*1.08
    f3=fit(d,sub,lambda s:pf(s,500),W-170,60); d.text((cx,y),sub,font=f3,fill=DK,anchor="mt")
    im.convert("RGB").save(out,"JPEG",quality=86,optimize=True,progressive=True)
