from PIL import Image, ImageFilter, ImageDraw
def fix(src, boxes, out=None, crop=None, size=None, r=6):
    im=Image.open(src).convert('RGB')
    for b in boxes:
        x0,y0,x1,y1=b; pad=4
        bl=im.filter(ImageFilter.GaussianBlur(r))
        m=Image.new('L',im.size,0); ImageDraw.Draw(m).rectangle((x0-pad,y0-pad,x1+pad,y1+pad),fill=255); m=m.filter(ImageFilter.GaussianBlur(4))
        im=Image.composite(bl,im,m)
    if crop: im=im.crop(crop)
    if size: im=im.resize(size,Image.LANCZOS)
    if out: im.save(out,quality=82,progressive=True,optimize=True)
    return im
