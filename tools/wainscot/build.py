import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
HG="https://homeguide.com/costs/wainscoting-cost"
MET="https://www.metrie.com/the-finished-space/en-blog-how-high-should-wainscoting-be"
BVH="https://www.bobvila.com/articles/wainscoting-height/"
BVB="https://www.bobvila.com/articles/how-to-install-beadboard/"
TOHI="https://www.thisoldhouse.com/walls/how-to-install-wainscoting"
TOHE="https://www.thisoldhouse.com/walls/how-to-install-easy-diy-wainscoting"
TOHID="https://www.thisoldhouse.com/walls/wainscoting-ideas"
TOHD="https://www.thisoldhouse.com/walls/wainscoting-designs"
LB="https://laurelberninteriors.com/wainscoting-one-thing-you-must-never-do/"
MMSH="https://missmustardseed.com/proper-heights-for-wainscoting/"
MMSP="https://missmustardseed.com/picture-frame-molding-tutorial/"
JLC="https://www.jlconline.com/how-to/interiors/an-introduction-to-wainscotting_o"
JLCSP="https://www.jlconline.com/how-to/interiors/simple-panel-wainscot_o"
FHBS="https://www.finehomebuilding.com/project-guides/finish-trim-carpentry/a-simple-approach-to-raised-panel-wainscot"
FHBE="https://finehomebuilding.com/?p=171798"
FHBCR="https://finehomebuilding.com/?p=107443"
FH="https://www.familyhandyman.com/project/how-to-build-a-wainscoted-wall/"
TDC="https://thriftydecorchick.com/2009/11/squares-on-my-walls.html"
A2D="https://www.addicted2decorating.com/how-to-install-picture-frame-molding-the-easiest-wainscoting-style-ever.html"
HGTV="https://www.hgtv.com/decorating/diy/how-to-easily-install-picture-frame-molding"
ETWP="https://cdn.architecturaldepot.com/pdf/installation/wainscot-wall-paneled.pdf"
HD48="https://homedepot.com/p/EUCATILE-32-sq-ft-3-16-in-x-48-in-x-96-in-Beadboard-White-True-Bead-Panel-975-759/205669196"
LOW="https://www.lowes.com/n/buying-guide/moulding-buying-guide"
FX="https://www.fixr.com/costs/wainscoting-installation"
HDBB="https://www.homedepot.com/c/ah/how-to-install-beadboard-wainscoting/9ba683603be9fa5395fab90d81eec51"
IHD="https://www.idealhome.co.uk/all-rooms/hallway/hallway-dado-rail-trend"
HOW="https://www.howdens.com/-/media/howdens/assets/clh_asset_products/clh_asset_levela_108973/clh_asset_levelb_110625/ass_25504875.pdf"
p("How do you lay out wainscoting? Set the top of the chair rail at about a third of the wall, which is 32 in on an 8 ft wall, then divide the wall into equal boxes or panels. For picture frame moulding, box width = (wall width − (boxes + 1) × gap) ÷ boxes, with a gap of about 3 in. This free <strong>wainscoting calculator</strong> does the layout and the shopping list for you in two taps.")
p("Pick your wall width and the style: picture frame boxes, raised or flat panels, tall two-row boxes or beadboard. You get the number of boxes or panels, their exact size, where to mark each one and how many lengths of moulding to buy, with a drawing of your wall. Open <em>More options</em> to type your exact wall width, change the height, the gap or the box width, or switch to centimeters.")
add('<!-- wp:html -->\n'+open('tool.html').read()+'\n<!-- /wp:html -->')
h2("Wainscoting Layout Chart")
table(["Wall width","Picture frame boxes (3 in gaps)","Box size at 32 in / 36 in high","Raised or flat panels (1x4 stiles)"],[
["8 ft (96 in)","3 boxes","28 x 18 in / 28 x 22 in","4 panels, 19 5/8 in wide"],
["10 ft (120 in)","4 boxes","26 1/4 x 18 in / 26 1/4 x 22 in","5 panels, 19 3/4 in wide"],
["12 ft (144 in)","5 boxes","25 1/4 x 18 in / 25 1/4 x 22 in","6 panels, 19 7/8 in wide"],
["14 ft (168 in)","6 boxes","24 1/2 x 18 in / 24 1/2 x 22 in","7 panels, 20 in wide"],
["16 ft (192 in)","7 boxes","24 x 18 in / 24 x 22 in","8 panels, 20 1/8 in wide"]])
p("The chart aims for boxes about 24 in wide and panels about 20 in wide, with a 5 1/2 in baseboard and a 2 1/2 in chair rail. Real walls are rarely a round number of feet, so measure each wall and type it into the calculator.")
diagram(re.sub(r'(\d+\.\d{1,2})\d+',r'\1',open('z.svg').read()),"Wainscoting layout: on a 10 ft wall with the chair rail at 32 in, four picture frame boxes 26 1/4 in wide and 18 in tall leave 3 in gaps between the boxes, at the corners and above and below. Box width = (wall − (boxes + 1) × gap) ÷ boxes; panel width = (wall − (panels + 1) × stile) ÷ panels.")
img(1)
h2("How High Should Wainscoting Be?")
p(f"The classic rule is a third of the wall. Metrie, a trim maker, says {ext(MET,'Traditionally, wainscoting runs about one-third of the wall’s height.')} HomeGuide puts it in numbers: {ext(HG,'This means a room with 8-foot ceilings should have 32-inch-high wainscoting.')} On a 9 ft wall, Bob Vila says {ext(BVH,'3-foot (or 36-inch) wainscoting will look great')}.")
table(["Ceiling height","Classic (one third)","Tall (about two-thirds)"],[
["8 ft (2.4 m)","32 in (81 cm)","64 in (163 cm)"],
["9 ft (2.7 m)","36 in (91 cm)","72 in (183 cm)"],
["10 ft (3.0 m)","40 in (102 cm)","80 in (203 cm)"]])
p(f"Sources disagree on going higher. This Old House says {ext(TOHI,'Classic wainscotting is between 36 and 42 inches from the ground, while modern wainscotting might be taller.')} Others prefer lower: Fine Homebuilding's trim writer advises {ext(FHBCR,'err on the side of too low rather than too high')}. Everyone agrees on one thing. Laurel Bern warns: {ext(LB,'But the one thing you must never do with your wainscoting is apply it halfway up the wall.')} If a windowsill sits close to a third of the wall, line the chair rail up with it.")
h2("How to Lay Out Picture Frame Wainscoting")
p(f"Picture frame moulding, also called shadow boxes, is the easiest style: mitred boxes of thin moulding on a flat wall. This Old House explains the math: {ext(TOHE,'Add 1 to the number of frames on a given wall and multiply by your chosen spacing between frames.')} {ext(TOHE,'Subtract that sum from the total wall length, then divide the remainder by the number of frames.')}")
lst(["<strong>Measure the wall</strong> between corners, or between a corner and a door or window.",
"<strong>Pick a gap,</strong> usually 3 in, and use it at the corners, between boxes and above and below the boxes.",
"<strong>Pick a rough box width,</strong> about 20 to 30 in, and round the number of boxes to a whole number.",
"<strong>Work out the exact width:</strong> wall − (boxes + 1) × gap, divided by the number of boxes.",
"<strong>Box height</strong> = chair rail height − chair rail − baseboard − two gaps."],ordered=True)
p(f"Thrifty Decor Chick's 14 ft wall shows how it works: {ext(TDC,'Take the remaining 147 inches and divide it by six boxes -- each box will be 24.5 inches wide.')} For the gap, she says, {ext(TDC,'I do a standard three inches all the way around.')} Miss Mustard Seed {ext(MMSP,'played with 2-4″ and landed on a 3″ space on all sides of each box')}.")
img(6)
p(f"Cut every corner at 45 degrees; HGTV notes the angle {ext(HGTV,'is a standard setting on a miter saw (or miter box if a hand saw is being used)')}. Boxes on one wall should match, though JLC says boxes don't need to be identical across the room: {ext(JLC,'similar is better')}.")
h2("Raised and Flat Panel Wainscoting")
img(2)
p(f"Panel wainscoting is built like a door: vertical stiles and horizontal rails frame each panel. Raised panels have beveled edges; flat (recessed) panels are plainer. This Old House says {ext(TOHID,'Raised panel wainscoting is the most traditional style, dating back to colonial times.')} The layout rule is simple: {ext(TOHI,'Remember that each wall has one more stile than panel')}, so panel width = (wall − (panels + 1) × stile width) ÷ panels.")
p(f"Most stiles and top rails are 1x4 boards, 3 1/2 in wide, with a wider bottom rail. Elite Trimworks recommends {ext(ETWP,'18” to 24" between stiles')}. For shape, Fine Homebuilding says panels {ext(FHBS,'should be wider than they are tall, and to my eye, an odd number of panels looks best')}, while JLC's author prefers them {ext(JLCSP,'taller than they are wide')}. Pick what you like and keep it the same on every wall.")
img(3)
h2("Beadboard Wainscoting")
img(4)
p(f"Beadboard is the quickest style to install in sheets. Home Depot sells beadboard panels where {ext(HD48,'Each sheet is 48 in. x 96 in. to cover 32 sq. ft.')} Traditional planks are narrower: Bob Vila notes that {ext(BVB,'each board is about 3 1⁄2 inches wide')}. Home Depot's tip for the last piece: {ext(HDBB,'Cut or plane as much of the last panel or board as needed to make it fit.')}")
h2("How Much Moulding Do You Need?")
p("Each picture frame box takes four pieces, two at its width and two at its height, so the moulding you need is the total perimeter of all the boxes. The calculator packs those pieces into 8, 12 or 16 ft lengths so you buy whole lengths, then adds the chair rail. For a 10 ft wall with four boxes, that is 8 pieces at 26 1/4 in and 8 at 18 in: 6 lengths of 8 ft box moulding and 3 of chair rail, including about 10% extra.")
lst([f"<strong>Extra:</strong> Lowe's says {ext(LOW,'Remember to add 10% to the total length for mitering.')}",
"<strong>Nails:</strong> 18-gauge brad nails, about 1 1/4 in long for thin moulding.",
"<strong>Finish:</strong> caulk the joints, fill the nail holes and paint. Painting the boxes and wall the same color gives the classic built-in look."])
h2("Wainscoting Cost")
p(f"Wainscoting costs vary a lot by style. HomeGuide says {ext(HG,'Flat panel wainscoting costs $10 to $15 per square foot and is the simplest option.')} and raised panel costs $12 to $30 per square foot installed. Fixr puts beadboard at $9 to $23 per square foot. Picture frame moulding is the cheapest DIY option, because you only buy moulding and paint.")
table(["Style","Installed cost per sq ft","DIY difficulty"],[
["Picture frame","not priced by these sources","easiest"],
["Beadboard","about $9 to $23 (Fixr)","easy"],
["Flat panel","about $10 to $15 (HomeGuide)","moderate"],
["Raised panel","about $12 to $30 (HomeGuide)","hardest"]])
h2("Outlets, Windows and Corners")
p(f"Plan the layout around what is already on the wall. For outlets, JLC says {ext(JLC,'ideally, these should be inside a panel or in the middle of a stile.')} Under windows, Family Handyman suggests you {ext(FH,'Divide the panel under the windows with a stile in the middle.')} At outside corners, mitre the trim. If you need to move or extend an outlet box, turn off the power first or hire an electrician.")
img(5)
p("On stairs, keep the boxes parallel to the stair slope and the same width along each flight. Measure each run of stairs separately.")
h2("How the Wainscoting Calculator Works")
lst(["<strong>Height:</strong> a third of the ceiling height (32 in on an 8 ft ceiling), or two-thirds for two rows of boxes. You can choose 36 in, 42 in or type your own.",
"<strong>Picture frame:</strong> boxes = round((wall − gap) ÷ (target width + gap)); box width = (wall − (boxes + 1) × gap) ÷ boxes; box height = height − chair rail (2 1/2 in) − baseboard (5 1/2 in) − 2 gaps.",
"<strong>Panels:</strong> 1x4 stiles (3 1/2 in), a 1x4 top rail, a 1x6 bottom rail and a cap; panel width = (wall − (panels + 1) × stile) ÷ panels.",
"<strong>Moulding:</strong> all pieces packed into the length you choose, plus about 10% extra (at least one spare).",
"<strong>Estimates:</strong> your moulding and rail sizes may differ. Check the numbers with your own boards before you cut."])
h2("Dado Rail and Box Panelling in the UK")
p(f"In the UK, wainscoting is usually called panelling under a dado rail. Ideal Home says {ext(IHD,'A dado rail in a hallway is generally best placed at about one third of the wall height')} and {ext(IHD,'which typically works out around 85 to 100 centimetres from the floor')}. UK fitting guides use wider gaps than US blogs: Howdens' example uses 150 mm, and the same formula gives {ext(HOW,'Divide 2850mm by 4 panels = 713mm panel width')}. Choose <em>Centimeters</em> in More options to get every result in cm.")
add(open('savebox.html').read())
h2("Wainscoting FAQ")
h3("How high should wainscoting be?")
p("About a third of the wall: 32 in (81 cm) on an 8 ft ceiling and 36 in (91 cm) on a 9 ft ceiling. For a bolder look, go to about two-thirds. Avoid putting the chair rail halfway up the wall.")
h3("How do you calculate wainscoting box spacing?")
p("Choose a gap, usually 3 in. Multiply it by the number of boxes plus one, subtract that from the wall width, then divide by the number of boxes. For example, (120 − 5 × 3) ÷ 4 = 26 1/4 in boxes on a 10 ft wall.")
h3("How far apart should picture frame moulding be?")
p("Most DIYers use 3 in between boxes, with the same gap at the corners and above and below the boxes. Gaps of 2 3/4 to 4 in are common in the US; UK guides often use 100 to 150 mm.")
h3("How much moulding do I need for wainscoting?")
p("Add up the perimeter of every box (twice the width plus twice the height), add about 10% for mitres, then add the chair rail along the full wall. A 10 ft wall with four boxes takes about 30 linear ft of box moulding before the extra.")
h2("More Free Home Tools")
p(f"Prefer vertical battens? Our {a('board-and-batten-calculator','board and batten calculator')} works out the spacing and boards. Use the {a('baseboard-calculator','baseboard calculator')} for the trim below, and our {a('picture-hanging-height-calculator','picture hanging height calculator')} for art above the chair rail.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script.*?</script>|<style.*?</style>|<svg.*?</svg>','',html))
print(len(html.encode()),'words',len(txt.split()),'kw',txt.lower().count('wainscoting calculator'),txt.lower().count('wainscot'))
