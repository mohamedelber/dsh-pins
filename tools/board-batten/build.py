import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
HD="https://homedepot.com/c/ah/how-to-make-a-board-and-batten-wall-accent/9ba683603be9fa5395fab90118469a03"
LOW="https://www.lowes.com/n/buying-guide/moulding-buying-guide"
BV="https://www.bobvila.com/articles/board-and-batten-101/"
BVS="https://www.bobvila.com/articles/how-to-find-a-wall-stud/"
HGTV="https://www.hgtv.com/design/decorating/design-101/how-to-install-board-and-batten-accent-wall"
HG="https://homeguide.com/costs/wainscoting-cost"
AMM="https://angelamariemade.com/diy-board-and-batten-wall/"
THD="https://www.thehandymansdaughter.com/wainscoting-vs-board-and-batten/"
YHL="https://www.younghouselove.com/how-to-install-board-and-batten/"
JSD="https://www.jennasuedesign.com/diy-board-and-batten-tutorial/"
MDL="https://www.megandauphineeliving.com/board-and-batten-wall-everything-you-need-to-know/"
CCL="https://thecrazycraftlady.com/choosing-your-board-and-batten-style/"
FMB="https://freshmommyblog.com/board-and-batten-grid-wall/"
RH="https://www.realhomes.com/advice/how-to-diy-a-board-and-batten-wall"
AT="https://www.apartmenttherapy.com/wainscoting-height-260241"
ATB="https://www.archtoolbox.com/lumber-dimensions/"
NEC="https://sonicelectric.com/blogs/news/nec-314-20-box-extenders"
HBR="https://www.homebuilding.co.uk/advice/diy-wall-panelling"
D2F="https://doors2floors.co.uk/blogs/advice/wall-panelling-guide"
BAB="https://www.bookabuilderuk.com/blog/board-batten-wall-ideas"
WPW="https://wallpanelsworld.co.uk/blog/wall-panelling-height/"
p("How far apart should board and batten be? Most walls look best with gaps of about 12 to 24 in between battens, and 16 to 20 in is the most popular. Put a batten in each corner, then use this formula: gap = (wall width − number of battens × batten width) ÷ (number of battens − 1). This free <strong>board and batten calculator</strong> does the math, the cut lengths and the shopping list in two taps.")
p("Pick your wall width and the style: classic (about 5 ft high with a ledge), wainscot, full wall or grid. You get the number of battens, the exact gap, how long to cut each batten and how many boards to buy, with a drawing of your wall. Open <em>More options</em> to type your exact wall width, choose 1x2 to 1x6 boards, change the gap or switch to centimeters.")
add('<!-- wp:html -->\n'+open('tool.html').read()+'\n<!-- /wp:html -->')
h2("Board and Batten Spacing Chart")
table(["Wall width","1x3 battens","1x4 battens","1x2 battens (grid)"],[
["8 ft (96 in)","6 battens, 16 1/4 in gaps","6 battens, 15 in gaps","6 battens, 17 3/8 in gaps"],
["10 ft (120 in)","7 battens, 17 1/8 in gaps","7 battens, 15 7/8 in gaps","8 battens, 15 3/8 in gaps"],
["12 ft (144 in)","9 battens, 15 1/4 in gaps","8 battens, 16 5/8 in gaps","9 battens, 16 3/8 in gaps"],
["14 ft (168 in)","10 battens, 15 7/8 in gaps","9 battens, 17 1/8 in gaps","11 battens, 15 1/8 in gaps"],
["16 ft (192 in)","11 battens, 16 1/2 in gaps","11 battens, 15 3/8 in gaps","12 battens, 15 7/8 in gaps"]])
p("The chart aims for about 16 in gaps, with a batten in each corner. Walls are rarely an exact number of feet, so measure yours and type the width into the calculator for gaps to the nearest 1/8 in.")
diagram(re.sub(r'(\d+\.\d{1,2})\d+',r'\1',open('z.svg').read()),"Board and batten spacing: on a 123 1/2 in wall, seven 1x4 battens (3 1/2 in wide) with one in each corner leave six gaps of 16 1/2 in, under a 1x4 top rail and 1x2 ledge at 60 in. The formula: gap = (wall width − battens × batten width) ÷ (battens − 1).")
img(1)
h2("How to Calculate Board and Batten Spacing")
lst(["<strong>Measure the wall</strong> from corner to corner at the height of the panelling. Home Depot's tip: "+ext(HD,"You’ll calculate your measurements by wall, not by room.")+"",
"<strong>Pick a batten size and a rough gap,</strong> for example 1x4 boards (3 1/2 in actual width) and about 16 in.",
"<strong>Count the battens:</strong> wall width minus one batten, divided by (gap + batten width), rounded, plus one.",
"<strong>Find the exact gap:</strong> subtract the width of all the battens from the wall width, then divide by the number of gaps (battens − 1).",
"<strong>Cut a spacer block</strong> to that exact gap and use it between battens as you install them."],ordered=True)
p(f"Here is a real example from Angela Marie Made, and Home Depot's guide uses the same numbers: a 123.5 in wall with seven 1x4 battens (24.5 in of boards) leaves 99 in of open wall, and Home Depot says to {ext(HD,'Divide 99 by 6 (the number of spaces between 7 boards), for a total of 16.5 inches.')} If your count is odd, Homebuilding &amp; Renovating notes that {ext(HBR,"If you have an odd number of slats, it's a good idea to start in the middle")}.")
h2("How Far Apart Should Board and Batten Be?")
p(f"There is no single rule, but most designers stay in a narrow range. The Crazy Craft Lady says {ext(CCL,'Most vertical battens are spaced between 16 and 20 inches apart')}, and Megan Dauphinee Living notes that {ext(MDL,'Most tutorials recommend spacing boards 12-24 inches apart.')}")
lst([f"<strong>12 to 14 in:</strong> a busy, traditional look. The Handyman's Daughter says {ext(THD,'Narrower spacing often gives a more cottagey feel.')}",
"<strong>16 to 20 in:</strong> the most popular choice for bedrooms, living rooms and hallways.",
f"<strong>20 to 24 in:</strong> a calmer, more modern wall. {ext(THD,'Wider spacing is more modern and creates a bold statement.')}"])
p(f"Narrow gaps also cost more: {ext(THD,'Keep in mind that the narrower your spacing, the more material you will need.')} Battens rarely line up with studs, because {ext(BVS,'Standard stud spacing is 16 inches on center')} and your battens sit at the gap plus their own width. That is why many DIYers glue them; Jenna Sue Design uses adhesive {ext(JSD,'for reinforcement, since the boards don’t usually end up in studs')}.")
h2("Board Sizes: 1x2, 1x3, 1x4 or 1x6?")
table(["Board","Actual width","Best for"],[
["1x2","1 1/2 in (38 mm)","grid walls, ledges on top of the rail"],
["1x3","2 1/2 in (64 mm)","small walls, a lighter look"],
["1x4","3 1/2 in (89 mm)","classic battens and top rails"],
["1x6","5 1/2 in (140 mm)","baseboards and big rooms"]])
p(f"Lumber is named by its rough size, so a 1x4 is really about 3/4 x 3 1/2 in ({ext(ATB,'Archtoolbox lumber table')}). Always use the actual width in the formula. Most battens are pre-primed MDF or pine; The Handyman's Daughter warns that {ext(THD,'Though MDF is cheap, it dents easily and sucks up paint like a sponge!')}, and Angela Marie Made suggests wood {ext(AMM,'especially for rooms with a high water exposure')}.")
h2("How High Should Board and Batten Be?")
img(2)
table(["Style","Height on an 8 ft wall","Notes"],[
["Wainscot","about 32 to 42 in (one third)","classic dining rooms and hallways"],
["Classic","about 48 to 64 in (half to two thirds)","the most common DIY height"],
["Full wall","floor to ceiling","feature walls behind a bed or sofa"],
["Grid","floor to ceiling","squares of about 24 in or less"]])
p(f"For traditional wainscot, HomeGuide says {ext(HG,'The standard height of wainscoting is one-third of the wall’s height.')} Board and batten usually goes taller: Young House Love says it {ext(YHL,'typically looks the best between 1/2 and 2/3 up your wall')}, and HGTV notes, {ext(HGTV,'For our eight-foot wall, we are installing board and batten at a height of five feet.')} Apartment Therapy adds that {ext(AT,'in many classically inspired homes, the height of the wainscot is the same as the height of the windowsills')}.")
p(f"To find the batten length, subtract the baseboard and top rail from the panel height. HGTV's example: {ext(HGTV,'To determine the length of the battens for our 5’ tall wall, we subtracted 5-1/2” for the baseboard and 3-1/2” for the top trim.')} That leaves 51 in battens, the same number the calculator gives for its classic style.")
h2("Top Rail, Ledge and Baseboard")
img(3)
p(f"Most board and batten walls finish with a 1x4 top rail and a 1x2 laid flat on top as a ledge. Young House Love says {ext(YHL,'A flat ledge looks more substantial and creates a spot to lean artwork or something on top.')} At the bottom, you can keep your baseboard, but Bob Vila suggests that {ext(BV,'For a uniform look, remove the baseboard and install a new base, using a board the same thickness as your battens.')}")
h2("Grid Board and Batten")
img(4)
p(f"A grid wall adds horizontal rails between the battens to make squares or rectangles. Fresh Mommy Blog says {ext(FMB,'The key to creating a gorgeous grid wall is to create squares with the grids')}, and suggests thin boards: {ext(FMB,'We used 1×2’s on our grid wall, and I wouldn’t go larger than 1×3’s, purely based on aesthetics.')} Choose <em>Grid</em> in the calculator to get the rows and the number of short rails to cut.")
h2("How Much Material Do You Need?")
p("The calculator counts every piece: battens, top rail, ledge and grid rails, then rounds up to whole boards. For a 10 ft wall in the classic style with 1x4 battens, that is 7 battens cut to 51 in, a 1x4 top rail and a 1x2 ledge: 10 boards of 1x4 and 3 of 1x2, 8 ft long, including about 10% extra.")
lst([f"<strong>Extra:</strong> Lowe's says {ext(LOW,'Remember to add 10% to the total length for mitering.')}",
f"<strong>Nails:</strong> 18-gauge brad nails (or 16-gauge finish nails). For nails that reach the studs, Home Depot says {ext(HD,'The nails should be about 2 inches long.')} Between studs, shorter 1 1/4 in brads only hold the batten while the construction adhesive sets. Jenna Sue Design: {ext(JSD,'I used 3-4 nails per batten and they went up so easy.')}",
"<strong>Adhesive:</strong> construction adhesive on the back of each batten. Skip it only if every batten is nailed into studs or you want to remove the wall later.",
f"<strong>Caulk and filler:</strong> Angela Marie Made says {ext(AMM,'Next, caulk all seams and corners with a paintable caulk.')} Fill the nail holes with spackle or wood filler.",
f"<strong>Paint:</strong> two coats. Real Homes notes, {ext(RH,"If you're using pre-primed MDF, you can skip this step and go straight to the paint.")}"])
h2("Board and Batten Cost")
p(f"DIY is cheap: Angela Marie Made says {ext(AMM,'This project cost us only $84 total to complete a 10ft. wall.')} Hiring a pro costs more. Bob Vila says {ext(BV,'For professional board-and-batten wainscoting you can expect to pay somewhere between $7 to $20 per square foot')}, and HomeGuide puts it at $10 to $23 per square foot. The calculator shows a rough pro price for your wall.")
h2("How to Install Board and Batten")
img(6)
lst(["<strong>Plan the layout</strong> with the calculator and mark each batten with a pencil and a level. Move the layout if a batten lands on an outlet.",
"<strong>Fix the top rail</strong> level across the wall, then the corner battens.",
"<strong>Add the battens</strong> with adhesive and brad nails, using your spacer block for every gap.",
"<strong>Add the ledge</strong> on top of the rail.",
"<strong>Caulk, fill and paint.</strong>"],ordered=True)
p(f"On heavily textured walls, Home Depot suggests a backer first: {ext(HD,'Attach a 1/8-inch panel board, like plywood, cut to size, on the wall.')} Outlets and switches need care. If a batten covers part of a box, the box must end up flush with the wood; when a box is recessed too far, {ext(NEC,'a listed box extender must be installed to bring the box opening flush with the finished wall surface')}. Turn off the power at the breaker before removing a cover plate, and if you are not sure, hire an electrician.")
img(5)
h2("How the Board and Batten Calculator Works")
lst(["<strong>Battens:</strong> one in each corner. Number = round((wall width − batten width) ÷ (target gap + batten width)) + 1.",
"<strong>Gap:</strong> (wall width − battens × batten width) ÷ (battens − 1), rounded to the nearest 1/8 in.",
"<strong>Heights:</strong> classic 62.5% of the ceiling height (60 in on an 8 ft wall), wainscot about 37.5% (36 in), full and grid to the ceiling. You can type your own panel height.",
"<strong>Cut length:</strong> panel height − baseboard (5 1/2 in) − top rail (3 1/2 in).",
"<strong>Boards:</strong> pieces per board for each size, plus about 10% extra (at least one spare). Nail and adhesive counts are our own estimates."])
h2("Batten Wall Panelling in the UK")
p(f"In the UK, board and batten is usually called batten wall panelling, and it is measured in millimetres. Book a Builder notes that {ext(BAB,'MDF thickness is typically 9mm to 12mm for battens')} and that {ext(BAB,'Spacing typically sits between 300mm and 600mm centres.')} For height, Doors2Floors says {ext(D2F,'Dado panelling looks right at roughly a third of the wall height')}, while Wall Panels World says {ext(WPW,'Half height panelling sits approximately 1.2m from the floor, creating a balanced division of wall space.')} Homebuilding &amp; Renovating adds: {ext(HBR,'We recommend always using a qualified electrician to remove sockets or switch')}. Choose <em>Centimeters</em> in More options to get every result in cm.")
add(open('savebox.html').read())
h2("Board and Batten FAQ")
h3("How far apart should board and batten be?")
p("Most walls use gaps of 12 to 24 in (30 to 60 cm), and 16 to 20 in is the most popular. Pick a rough gap, then adjust it so every gap is equal and there is a batten in each corner.")
h3("How do you calculate board and batten spacing?")
p("Subtract the total width of all your battens from the wall width, then divide by the number of gaps, which is one less than the number of battens. For example, (123.5 − 7 × 3.5) ÷ 6 = 16.5 in.")
h3("How many battens do I need for a 10 ft wall?")
p("With 1x4 battens and gaps of about 16 in, you need 7 battens with gaps of 15 7/8 in. With 1x3 battens, 7 battens give gaps of about 17 1/8 in.")
h3("What size boards are used for board and batten?")
p("1x3 or 1x4 boards are the most common battens, with a 1x4 top rail and a 1x2 ledge. Grid walls usually use 1x2 boards. Remember that a 1x4 is really 3 1/2 in wide.")
h2("More Free Home Tools")
p(f"Finishing the room? Our {a('baseboard-calculator','baseboard calculator')} works out how much baseboard to buy, the {a('wallpaper-calculator','wallpaper calculator')} covers the wall above the panelling, and our {a('picture-hanging-height-calculator','picture hanging height calculator')} shows where to hang art on your new ledge wall.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script.*?</script>|<style.*?</style>|<svg.*?</svg>','',html))
print(len(html.encode()),'words',len(txt.split()),'kw',txt.lower().count('board and batten calculator'),txt.lower().count('board and batten'))
