from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
exec(open('checklist.py').read())
for n in ['Mont-R','Mont-B','Lora-R','Lora-B']:
    pdfmetrics.registerFont(TTFont(n, f'f/{n}.ttf'))
INK=HexColor('#342E2A'); MUT=HexColor('#6E645C'); AC=HexColor('#C85A32'); SG=HexColor('#8FA689'); BG=HexColor('#F7F1E9'); BD=HexColor('#E6DCCF'); SGL=HexColor('#EEF3EC')
W,H=letter; M=46
def wrap(c,txt,font,size,width):
    words=txt.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if c.stringWidth(t,font,size)<=width: cur=t
        else: lines.append(cur); cur=w
    lines.append(cur); return lines
def header(c,sub,page):
    c.setFillColor(BG); c.rect(0,H-112,W,112,stroke=0,fill=1)
    c.setFillColor(AC); c.setFont('Mont-B',9); c.drawString(M,H-38,'FREE PRINTABLE')
    c.setFillColor(INK); c.setFont('Lora-B',29); c.drawString(M,H-70,'First Apartment Checklist')
    c.setFillColor(MUT); c.setFont('Mont-R',10.3); c.drawString(M,H-92,sub)
    c.setFont('Mont-R',9); c.drawRightString(W-M,H-38,'dailyspacehacks.com')
    c.setFont('Mont-R',8.5); c.drawRightString(W-M,H-92,f'Page {page} of 2')
    c.setFillColor(MUT); c.setFont('Mont-R',7.8)
    c.drawString(M,22,'Tick each item as you buy or do it. The tag shows when you need it. Check your lease and local rules.  ·  Free for personal use')
def tag(c,x,y,t):
    w=c.stringWidth(t,'Mont-B',7.2)+10
    c.setFillColor(HexColor(TAGS[t])); c.roundRect(x-w,y-3,w,11.5,5.5,stroke=0,fill=1)
    c.setFillColor(HexColor('#FFFFFF')); c.setFont('Mont-B',7.2); c.drawString(x-w+5,y,t)
def box(c,x,y,w,title,items):
    tw=w-30-62; lines=[(wrap(c,t,'Mont-R',9.8,tw),g) for t,g in items]
    h=32+sum(len(l)*12.4+7 for l,_ in lines)+4
    c.setStrokeColor(BD); c.setFillColor(HexColor('#FFFDF9')); c.roundRect(x,y-h,w,h,8,stroke=1,fill=1)
    c.setFillColor(SGL); c.roundRect(x,y-26,w,26,8,stroke=0,fill=1); c.rect(x,y-26,w,10,stroke=0,fill=1)
    c.setFillColor(HexColor('#3F5E39')); c.setFont('Mont-B',11.5); c.drawString(x+12,y-17.5,title)
    yy=y-44
    for l,g in lines:
        c.setStrokeColor(SG); c.setLineWidth(1.1); c.setFillColor(HexColor('#FFFFFF')); c.roundRect(x+12,yy-2.5,9.5,9.5,2,stroke=1,fill=1)
        c.setFillColor(INK); c.setFont('Mont-R',9.8)
        for i,s in enumerate(l): c.drawString(x+28,yy-i*12.4,s)
        tag(c,x+w-10,yy,g)
        yy-=len(l)*12.4+7
    return h
def legend(c,x,y,w):
    items=[("Before","before moving day"),("Day 1","for your first night"),("Week 1","in the first week"),("Later","when budget allows")]
    h=30+len(items)*15+6
    c.setStrokeColor(BD); c.setFillColor(HexColor('#FFFDF9')); c.roundRect(x,y-h,w,h,8,stroke=1,fill=1)
    c.setFillColor(HexColor('#FBEFE6')); c.roundRect(x,y-26,w,26,8,stroke=0,fill=1); c.rect(x,y-26,w,10,stroke=0,fill=1)
    c.setFillColor(HexColor('#9A3F1F')); c.setFont('Mont-B',11.5); c.drawString(x+12,y-17.5,'When you need it')
    for i,(t,d) in enumerate(items):
        yy=y-44-i*15; tag(c,x+12+c.stringWidth(t,'Mont-B',7.2)+10,yy,t)
        c.setFillColor(INK); c.setFont('Mont-R',8.9); c.drawString(x+80,yy,d)
    return h
def page(c,rooms,sub,pg,extra=False):
    header(c,sub,pg)
    colw=(W-2*M-14)/2; xs=[M,M+colw+14]; ys=[H-128,H-128]
    for t,items in rooms:
        col=0 if ys[0]>=ys[1] else 1
        h=box(c,xs[col],ys[col],colw,t,items); ys[col]-=h+12
    if extra:
        col=0 if ys[0]>=ys[1] else 1
        h=legend(c,xs[col],ys[col],colw); ys[col]-=h+12
        y=min(ys)-2; tips=[('Measure first','doorways, stairs and the bedroom before you buy a bed or sofa.'),('Day 1 items first','so the first night has light, a bed, a towel and toilet paper.'),('Borrow or buy used','for the Later items, and inspect secondhand furniture for bed bugs.'),('Keep receipts','and photos of what you own for renters insurance.')]
        hh=30+len(tips)*17+8
        c.setStrokeColor(BD); c.setFillColor(HexColor('#FFFDF9')); c.roundRect(M,y-hh,W-2*M,hh,8,stroke=1,fill=1)
        c.setFillColor(HexColor('#FBEFE6')); c.roundRect(M,y-26,W-2*M,26,8,stroke=0,fill=1); c.rect(M,y-26,W-2*M,10,stroke=0,fill=1)
        c.setFillColor(HexColor('#9A3F1F')); c.setFont('Mont-B',11.5); c.drawString(M+12,y-17.5,'Before you shop')
        for i,(a,b) in enumerate(tips):
            yy=y-44-i*17; c.setFillColor(INK); c.setFont('Mont-B',9.8); c.drawString(M+12,yy,a+':'); w=c.stringWidth(a+': ','Mont-B',9.8)
            c.setFont('Mont-R',9.8); c.drawString(M+12+w,yy,b)
        ys=[y-hh-12,y-hh-12]
        y=min(ys)-2; hh=y-40
        if hh>60:
            c.setStrokeColor(BD); c.setFillColor(HexColor('#FFFDF9')); c.roundRect(M,40,W-2*M,hh,8,stroke=1,fill=1)
            c.setFillColor(INK); c.setFont('Mont-B',10.5); c.drawString(M+12,40+hh-17,'Notes: landlord contact, utility account numbers, move-in date')
            c.setStrokeColor(BD); yy=40+hh-36
            while yy>52: c.line(M+12,yy,W-M-12,yy); yy-=19
    c.showPage()
c=canvas.Canvas('first-apartment-checklist-printable.pdf',pagesize=letter)
c.setTitle('Printable First Apartment Checklist'); c.setAuthor('Daily Space Hacks'); c.setSubject('First apartment checklist: what to buy and set up')
page(c,ROOMS[:4],'Paperwork, safety and tools, kitchen and bathroom: what to buy and set up.',1)
page(c,ROOMS[4:],'Bedroom, living room, cleaning and your first week, plus when you need each item.',2,extra=True)
c.save(); print('saved')
