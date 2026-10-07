from PIL import Image, ImageDraw, ImageFont
F="/usr/share/fonts/truetype/google-fonts/"
def lora(sz,w=700,it=False):
    f=ImageFont.truetype(F+("Lora-Italic-Variable.ttf" if it else "Lora-Variable.ttf"),sz)
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f
def fit(d,text,font_fn,maxw,start):
    s=start
    while s>20:
        f=font_fn(s)
        if d.textlength(text,font=f)<=maxw: return f
        s-=4
    return font_fn(s)
def pin_h(src,num,l1,l2,sub,out,fade=0.50,cream=(250,246,240),anchor=1.0):
    W,H=1000,1500
    im=Image.open(src).convert("RGB")
    r=max(W/im.width,H/im.height); im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS)
    x=(im.width-W)//2; yy=int((im.height-H)*anchor); im=im.crop((x,yy,x+W,yy+H))
    ov=Image.new("RGBA",(W,H),(0,0,0,0)); od=ImageDraw.Draw(ov)
    fh=int(H*fade)
    for y in range(fh):
        t=y/fh
        a=int(255*(0.97 if t<0.55 else 0.97*(1-(t-0.55)/0.45)**1.6))
        od.line([(0,y),(W,y)],fill=cream+(a,))
    im=Image.alpha_composite(im.convert("RGBA"),ov); d=ImageDraw.Draw(im)
    cx=W//2; y=60
    fn=lora(200,700); tw=d.textlength(num,font=fn)
    d.text((cx,y),num,font=fn,fill=(95,111,78),anchor="mt")
    # rays
    for side in (-1,1):
        bx=cx+side*(tw/2+28)
        for dy,ang in ((-40,0.55),(0,0),(40,-0.55)):
            x0=bx; y0=y+110+dy; x1=x0+side*44; y1=y0-ang*44*1
            d.line([(x0,y0),(x1,y1)],fill=(200,90,50),width=7)
    y+=225
    f1=fit(d,l1,lambda s:lora(s,700),W-110,104)
    d.text((cx,y),l1,font=f1,fill=(52,46,42),anchor="mt"); y+=f1.size*1.08
    f2=fit(d,l2,lambda s:lora(s,700),W-110,104)
    d.text((cx,y),l2,font=f2,fill=(200,90,50),anchor="mt"); y+=f2.size*1.15
    f3=fit(d,sub,lambda s:lora(s,500,True),W-160,54)
    d.text((cx,y),sub,font=f3,fill=(52,46,42),anchor="mt")
    im.convert("RGB").save(out,"JPEG",quality=86,optimize=True,progressive=True)
