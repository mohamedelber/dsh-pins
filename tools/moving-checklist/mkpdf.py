from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
for n in ['Mont-R','Mont-B','Lora-R','Lora-B']:
    pdfmetrics.registerFont(TTFont(n, f'f/{n}.ttf'))
INK=HexColor('#342E2A'); MUT=HexColor('#6E645C'); AC=HexColor('#C85A32'); SG=HexColor('#8FA689'); BG=HexColor('#F7F1E9'); BD=HexColor('#E6DCCF'); SGL=HexColor('#EEF3EC')
W,H=letter  # 612 x 792; content kept within 8.0 in so it also prints on A4
M=50
P1=[('8 weeks before',['Set your moving date and a rough budget.','Get written quotes from at least three movers, or book a van or truck.','Start a moving folder for quotes, receipts and contracts.','Declutter room by room: sell, donate or recycle.','Renting: give notice in writing and check the deposit rules.','Selling: line up moving day with closing or completion.','Tell the school and look up doctors near the new home.']),
('6 weeks before',['Order boxes, tape and packing paper.','Measure large furniture and the doors of the new home.','Use up frozen food and pantry items.','Pack things you rarely use: seasonal clothes, books, decor.','Get your pet’s records from the vet.']),
('4 weeks before',['Forward your mail (USPS change of address or Royal Mail Redirection).','Book the switch of electricity, gas, water and internet.','Update your address with the bank, employer and insurers.','Pack room by room; label each box with room and contents.','Book time off work and childcare for moving day.','Set up insurance for the new home from moving day.']),
('2 weeks before',['Confirm date, time and both addresses with the movers.','Plan parking for the van or truck at both homes.','Refill prescriptions.','Return borrowed items and library books.','Take apart furniture; bag and tape the screws to each piece.'])]
P2=[('Moving week',['Pack a first-night essentials box: bedding, towels, chargers, toilet paper, medicine, kettle, snacks.','Pack a bag of clothes and toiletries for a few days.','Clean as you go, or book a move-out clean.','Plan a quiet room or a sitter for pets.']),
('The day before',['Empty, defrost and clean the fridge and freezer.','Charge phones and power banks.','Keep documents, keys, medicine and valuables with you.']),
('Moving day',['Take meter readings and photos before you leave.','Renting: photograph every room after cleaning.','Last walk-through: cupboards, attic or loft, garage, shed.','Lock up and hand over the keys as agreed.','At the new home: meter readings, check every box arrived.','Make the beds first.']),
('First week in your new home',['Unpack the kitchen and bathroom first.','Test smoke and carbon monoxide alarms.','Find the main water shutoff and the breaker panel or fuse box.','Change or rekey the locks if you own the home.','Update your driver\u2019s license and voter registration.','Update your pet’s microchip details.','Flatten and recycle the boxes.'])]
def wrap(c,txt,font,size,width):
    words=txt.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if c.stringWidth(t,font,size)<=width: cur=t
        else: lines.append(cur); cur=w
    lines.append(cur); return lines
def header(c,sub,page):
    c.setFillColor(BG); c.rect(0,H-118,W,118,stroke=0,fill=1)
    c.setFillColor(AC); c.setFont('Mont-B',9); c.drawString(M,H-40,'FREE PRINTABLE')
    c.setFillColor(INK); c.setFont('Lora-B',30); c.drawString(M,H-74,'Moving Checklist')
    c.setFillColor(MUT); c.setFont('Mont-R',10.5); c.drawString(M,H-96,sub)
    c.setFont('Mont-R',9); c.drawRightString(W-M,H-40,'dailyspacehacks.com')
    c.setFont('Mont-R',8.5); c.drawRightString(W-M,H-96,f'Page {page} of 2')
    if page==1:
        c.setFillColor(INK); c.setFont('Mont-B',10); c.drawRightString(W-M-118,H-72,'Moving day:'); c.setStrokeColor(MUT); c.setLineWidth(.8); c.line(W-M-112,H-74,W-M,H-74)
    c.setFillColor(MUT); c.setFont('Mont-R',8)
    c.drawString(M,24,'Get a version with your own dates at dailyspacehacks.com/moving-checklist-printable/  ·  Free for personal use')
def box(c,x,y,w,title,items):
    tw=w-44; lines=[(wrap(c,t,'Mont-R',10.8,tw)) for t in items]
    h=34+sum(len(l)*14.2+8 for l in lines)+6
    c.setStrokeColor(BD); c.setFillColor(HexColor('#FFFDF9')); c.roundRect(x,y-h,w,h,8,stroke=1,fill=1)
    c.setFillColor(SGL); c.roundRect(x,y-28,w,28,8,stroke=0,fill=1); c.rect(x,y-28,w,10,stroke=0,fill=1)
    c.setFillColor(HexColor('#3F5E39')); c.setFont('Mont-B',12.5); c.drawString(x+12,y-18.5,title)
    yy=y-48
    for l in lines:
        c.setStrokeColor(SG); c.setLineWidth(1.1); c.setFillColor(HexColor('#FFFFFF')); c.roundRect(x+12,yy-2.5,10,10,2,stroke=1,fill=1)
        c.setFillColor(INK); c.setFont('Mont-R',10.8)
        for i,s in enumerate(l): c.drawString(x+30,yy-i*14.2,s)
        yy-=len(l)*14.2+8
    return h
WHO=['Post office','Bank and cards','Employer','Doctor and dentist','Insurers','Phone and internet','Subscriptions','School','Tax office','Driver\u2019s license','Voter registration','Family and friends']
def who(c,x,y,w):
    rows=(len(WHO)+1)//2; h=34+rows*16+8
    c.setStrokeColor(BD); c.setFillColor(HexColor('#FFFDF9')); c.roundRect(x,y-h,w,h,8,stroke=1,fill=1)
    c.setFillColor(HexColor('#FBEFE6')); c.roundRect(x,y-28,w,28,8,stroke=0,fill=1); c.rect(x,y-28,w,10,stroke=0,fill=1)
    c.setFillColor(HexColor('#9A3F1F')); c.setFont('Mont-B',12.5); c.drawString(x+12,y-18.5,'Who to tell you are moving')
    for i,t in enumerate(WHO):
        cx=x+12+(i%2)*(w/2-6); cy=y-48-(i//2)*16
        c.setStrokeColor(AC); c.setLineWidth(1.1); c.setFillColor(HexColor('#FFFFFF')); c.roundRect(cx,cy-2.5,10,10,2,stroke=1,fill=1)
        c.setFillColor(INK); c.setFont('Mont-R',9.8); c.drawString(cx+16,cy,t)
    return h
def page(c,data,sub,pg,notes=False):
    header(c,sub,pg)
    colw=(W-2*M-16)/2; xs=[M,M+colw+16]; ys=[H-136,H-136]
    order=[0,1,0,1] if not notes else [0,1,0,1]
    for i,(t,items) in enumerate(data):
        col=0 if ys[0]>=ys[1] else 1
        h=box(c,xs[col],ys[col],colw,t,items); ys[col]-=h+14
    if pg==1:
        col=0 if ys[0]>=ys[1] else 1
        who(c,xs[col],ys[col],colw)
    if notes:
        y=min(ys)-4; hh=y-48
        c.setStrokeColor(BD); c.setFillColor(HexColor('#FFFDF9')); c.roundRect(M,48,W-2*M,hh,8,stroke=1,fill=1)
        c.setFillColor(INK); c.setFont('Mont-B',11); c.drawString(M+12,48+hh-18,'Notes and important numbers')
        c.setStrokeColor(BD)
        yy=48+hh-40
        while yy>60:
            c.line(M+12,yy,W-M-12,yy); yy-=20
    c.showPage()
c=canvas.Canvas('moving-checklist-printable.pdf',pagesize=letter)
c.setTitle('Printable Moving Checklist'); c.setAuthor('Daily Space Hacks'); c.setSubject('Week-by-week moving checklist')
page(c,P1,'Week by week, from 8 weeks out to moving day. Tick each task as you go.',1)
page(c,P2,'Moving week, moving day and your first week in the new home.',2,notes=True)
c.save()
print('saved')
