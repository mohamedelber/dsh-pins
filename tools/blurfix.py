from PIL import Image, ImageFilter, ImageDraw
# IPTC DigitalSourceType = trainedAlgorithmicMedia (Google gen-AI guidance, Oct 2026).
# Article images only: Pinterest pins (pinh2) are NOT tagged, Pinterest labels tagged pins "AI modified".
AI_XMP=(b'<?xpacket begin="\xef\xbb\xbf" id="W5M0MpCehiHzreSzNTczkc9d"?><x:xmpmeta xmlns:x="adobe:ns:meta/">'
 b'<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description rdf:about="" '
 b'xmlns:Iptc4xmpExt="http://iptc.org/std/Iptc4xmpExt/2008-02-29/"><Iptc4xmpExt:DigitalSourceType>'
 b'http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia</Iptc4xmpExt:DigitalSourceType>'
 b'</rdf:Description></rdf:RDF></x:xmpmeta><?xpacket end="w"?>')
def fix(src, boxes, out=None, crop=None, size=None, r=6, ai=True):
    im=Image.open(src).convert('RGB')
    for b in boxes:
        x0,y0,x1,y1=b; pad=4
        bl=im.filter(ImageFilter.GaussianBlur(r))
        m=Image.new('L',im.size,0); ImageDraw.Draw(m).rectangle((x0-pad,y0-pad,x1+pad,y1+pad),fill=255); m=m.filter(ImageFilter.GaussianBlur(4))
        im=Image.composite(bl,im,m)
    if crop: im=im.crop(crop)
    if size: im=im.resize(size,Image.LANCZOS)
    if out:
        kw={'xmp':AI_XMP} if ai else {}
        im.save(out,quality=82,progressive=True,optimize=True,**kw)
    return im
