import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
TOH="https://www.thisoldhouse.com/walls/how-to-install-baseboards"
BV="https://www.bobvila.com/articles/installing-trim/"
BV2="https://www.bobvila.com/articles/how-to-install-baseboard/"
LW="https://lowes.com/n/buying-guide/moulding-buying-guide"
HD="https://www.homedepot.com/c/ah/how-to-install-baseboard/9ba683603be9fa5395fab901a97a162"
AT="https://www.angi.com/articles/baseboard-trim-sizes.htm"
AY="https://www.angi.com/articles/types-of-baseboards.htm"
HA="https://www.homeadvisor.com/cost/walls-and-ceilings/install-baseboard"
HS="https://www.homeserve.com/en-us/blog/cost-guide/install-baseboard"
HP="https://www.houseplans.com/blog/interior-trim-scale-proportion"
BE="https://images.thdstatic.com/catalog/pdfImages/35/3579c54d-a385-4155-9c15-a555d615d4eb.pdf"
PG="https://images.thdstatic.com/catalog/pdfImages/27/27182e9f-21f8-436a-9def-9e127a172672.pdf"
HB="https://www.homebuilding.co.uk/advice/skirting-board-sizes"
p("How much baseboard do you need? Add up the length of every wall, take off about 3 ft for each doorway and add 10% for waste. A 12 x 12 ft bedroom has 48 ft of wall, or 45 ft once you take off one door, so you buy about 50 ft of baseboard, or five 12 ft boards. This free <strong>baseboard calculator</strong> does the math in two taps.")
p("Pick the room size and the number of doorways. You get the linear feet to buy, how many boards, a cost estimate and how much caulk you need. Open <em>More options</em> to type exact measurements, switch to meters for skirting board, or change the board length and waste.")
add('<!-- wp:html -->\n'+open('tool.html').read()+'\n<!-- /wp:html -->')
h2("How to Measure for Baseboard")
diagram(re.sub(r'(\d+\.\d{1,2})\d+',r'\1',open('z.svg').read()),"How to measure for baseboard in a 12 x 14 ft room with one door: add up the walls (52 ft), take off 3 ft for the door (49 ft), add 10% for waste (about 54 ft) and round up to five 12 ft boards.")
lst(["<strong>Measure each wall</strong> at floor level, from corner to corner, and add them up. For a simple rectangle, that is 2 x (length + width).",
"<strong>Take off the doorways.</strong> Baseboard stops at the door casing, so subtract each opening. A standard interior door plus its casing is about 3 ft.",
"<strong>Add 10% for waste</strong> to cover cuts, corners and mistakes.",
"<strong>Divide by the board length</strong> and round up to whole boards."],ordered=True)
p(f"Bob Vila says to {ext(BV,'measure the length of each wall from corner to corner, subtracting any openings for doors or closets')}, and This Old House adds that {ext(TOH,'it’s wise to add an extra 10% to account for waste and mistakes')}.")
img(2)
img(6)
h2("Baseboard Chart by Room Size")
table(["Room","Wall length","Minus 1 door","Buy (+10%)","12 ft boards"],[
["10 x 10 ft","40 ft","37 ft","41 ft","4"],
["10 x 12 ft","44 ft","41 ft","46 ft","4"],
["12 x 12 ft","48 ft","45 ft","50 ft","5"],
["12 x 14 ft","52 ft","49 ft","54 ft","5"],
["14 x 16 ft","60 ft","57 ft","63 ft","6"],
["16 x 20 ft","72 ft","69 ft","76 ft","7"]])
p("Take off another 3 ft for each extra doorway or open closet. For an open plan or a whole floor, measure every wall and enter the total in <em>More options</em>.")
h2("Baseboard Lengths: 8, 12 or 16 Feet?")
img(5)
p(f"Bob Vila notes that home stores {ext(BV,'sell baseboard and crown molding in 8-foot and 12-foot lengths')}, and many stores also carry 16 ft boards. Lowe's advises: {ext(LW,'use longer lengths of moulding in large rooms so that fewer cuts will be required')}. If a wall is longer than one board, This Old House explains that {ext(TOH,'scarf joints are used to join two pieces of baseboard along a long wall where a single piece isn’t long enough')}.")
p("Longer boards also mean fewer seams. A 10 ft wall cut from 8 ft boards needs a seam and leaves a 6 ft offcut; one 12 ft board covers it in one piece.")
h2("How Much Extra Baseboard for Waste?")
img(3)
p(f"Most guides say to add 10%; Lowe's says to {ext(LW,'add 10% to the total length for mitering')}. Bob Vila suggests more, {ext(BV,'about 20 percent extra material to account for mistakes, offcuts, and overlapping joints')}, which makes sense for a first DIY job. Rooms with many outside corners, like a bay window or a chimney breast, need more too: Home Depot says that for outside corners you should {ext(HD,'cut them a few inches longer than the wall to allow for miter cuts')}.")
p(f"For inside corners, This Old House says {ext(TOH,'coping one piece to fit the profile of the adjoining board typically produces the best results')}. Coping gives a tighter joint than a miter when the walls are not perfectly square.")
h2("Baseboard Cost per Linear Foot")
table(["Type","Material cost per linear foot","Good for"],[
["MDF","$1 to $1.40","painted rooms, dry areas"],
["Pine","$1.40 to $1.85","paint or stain"],
["PVC","$0.90 to $1.40","bathrooms, basements, damp areas"],
["Solid wood","$1.40 to $5, up to $10 for cherry or mahogany","stained wood looks"],
["Installed by a pro","$5.70 to $9","materials and labor"]])
p(f"Material prices are from Angi’s guides to {ext(AY,'baseboard types')} and {ext('https://www.angi.com/articles/mdf-vs-pine-baseboard.htm','MDF vs. pine')}. For installation, HomeAdvisor says {ext(HA,'contractors charge between $5.70 and $9.00 per linear foot for baseboard installation')}, and HomeServe gives a similar {ext(HS,'$6 to $9 per linear foot')}. Taller and more detailed profiles cost more.")
h2("What Height Baseboard Should You Use?")
img(4)
table(["Ceiling height","Baseboard height"],[
["8 ft","3-1/4 to 5-1/4 in"],
["9 ft","4-1/4 to 5-1/4 in, or taller for a bold look"],
["10 ft or more","5-1/4 to 7-1/4 in"]])
p(f"Angi says {ext(AT,'the most common baseboard heights are 3 1/4 inches, 4 1/4 inches, and 5 1/4 inches')}, and that {ext(AT,'rooms with ceilings ten feet or higher need taller baseboards from five to seven inches or more')}. Some designers go taller: a Houseplans.com guide suggests {ext(HP,'a baseboard height that’s approximately 7% of the wall height')}, which is about 7 to 8 in for an 8 or 9 ft wall. Treat both as style choices, not rules.")
h2("Nails, Caulk and Shoe Molding")
lst([f"<strong>Nails:</strong> Bob Vila says to {ext(BV,'nail into the lower 1½ inch of the trim with 2-inch finishing nails spaced roughly 16 inches apart')}. A 15 or 16 gauge finish nailer works well for baseboard.",
f"<strong>Caulk:</strong> {ext(BE,'each 10.1 fl oz cartridge will cover 55 linear feet with a 3/16” bead')}, so a 12 x 12 ft room needs one tube for the top edge.",
f"<strong>Shoe molding and quarter round:</strong> measure them the same way. A Pergo planner says to subtract the doorways from the perimeter {ext(PG,'to determine the total length of wall base or quarter round')}. The calculator adds it for you when you tick the box."])
h2("How the Baseboard Calculator Works")
lst(["<strong>Wall length:</strong> 2 x (length + width) for the room size you pick, or the total you type in.",
"<strong>Doorways:</strong> about 3 ft each, our estimate for a 32 in door plus its casing. Change it in More options for wider openings.",
"<strong>Waste:</strong> 10% by default, 15% for many corners and 20% for a first DIY job.",
"<strong>Boards:</strong> the total divided by the board length (8, 12 or 16 ft, or 2.4, 3.05 or 4.2 m), rounded up.",
"<strong>Cost:</strong> MDF at $1 to $1.40 per linear foot, and $5.70 to $9 per linear foot installed. Prices vary by area and profile."])
h2("Skirting Board Calculator for the UK")
p(f"In the UK, baseboard is called skirting board, and it works the same way in meters. Wickes and B&amp;Q sell skirting in 2.4 m, 3.05 m and 4.2 m lengths and in heights such as 119, 144 and 169 mm, and Homebuilding &amp; Renovating notes that {ext(HB,'the most popular standard skirting board height is 145mm')}. Choose <em>Meters</em> in More options and the calculator uses UK board lengths and about 0.9 m per doorway.")
add(open('savebox.html').read())
h2("Baseboard Calculator FAQ")
h3("How much baseboard do I need for a 12 x 12 room?")
p("A 12 x 12 ft room has 48 ft of wall. Take off about 3 ft for one door to get 45 ft, then add 10% for waste: buy about 50 ft, or five 12 ft boards.")
h3("How do I calculate linear feet of baseboard?")
p("Measure each wall in feet and add them up, or use 2 x (length + width) for a rectangle. Subtract about 3 ft for each doorway, then add 10% for waste. The result is the linear feet to buy.")
h3("How much does baseboard cost per foot?")
p("MDF baseboard costs about $1 to $1.40 per linear foot and pine about $1.40 to $1.85. Professional installation, with materials, runs about $5.70 to $9 per linear foot.")
h3("Do you subtract doors when measuring for baseboard?")
p("Yes. Baseboard stops at each side of the door casing, so subtract the width of every doorway and open closet, about 3 ft for a standard interior door. Do not subtract windows unless they go down to the floor.")
h2("More Free Home Calculators")
p(f"Decorating the walls too? Our {a('wallpaper-calculator','wallpaper calculator')} works out how many rolls you need, our {a('picture-hanging-height-calculator','picture hanging height calculator')} shows where to put the nail and our {a('shelf-spacing-calculator','shelf spacing calculator')} helps you plan shelves.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script.*?</script>|<style.*?</style>|<svg.*?</svg>','',html))
print(len(html.encode()),'words',len(txt.split()),'kw',txt.lower().count('baseboard calculator'),txt.lower().count('baseboard'))
