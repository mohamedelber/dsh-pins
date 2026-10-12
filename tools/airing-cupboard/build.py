import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
VI="https://www.viessmann.co.uk/heating-advice/what-is-an-airing-cupboard"
EST="https://energysavingtrust.org.uk/advice/insulating-tanks-pipes-and-radiators/"
CW="https://www.cheshirewestandchester.gov.uk/asset-library/housing-gas-safety-leaflet.pdf"
p("The right airing cupboard shelves turn a warm, cluttered cupboard into the best linen store in the house. Most British airing cupboards were built around a hot water cylinder, with a couple of wobbly shelves squeezed in above it, so towels end up in piles and the bedding you need is always at the bottom.")
p("This guide shows what to store where, how to fit slatted shelves safely around a cylinder or boiler, and 16 airing cupboard storage ideas for towels, bedding sets, small cupboards and rented homes, plus the mistakes to avoid.")
img(1)
summary(["<strong>Quick answer:</strong> The best airing cupboard shelves are slatted wooden shelves fixed on battens to the walls, starting above the hot water cylinder so the cylinder, pipes and valves stay easy to reach. Keep towels and bedding you use every week in the middle, spares on the top shelf, and never cover the slats or pack the cupboard so tightly that air cannot move.",
"Use the shelf just above the cylinder to finish off items that are only slightly damp, never soaking wet ones.",
"Keep paint, aerosols and cleaning products out of any cupboard with a gas boiler."],
"<strong>Time:</strong> an hour to reorganise, a morning to fit new shelves · <strong>Cost:</strong> £ to ££ · <strong>Difficulty:</strong> Easy to moderate")
toc("airing-cupboard-shelves")
h2("Airing Cupboard Shelves Layout Guide")
p("Plan your airing cupboard from the bottom up. The cylinder and its pipes come first, then a warm shelf for airing, then everyday towels and bedding, and finally the top shelf for things you rarely need.")
diagram(open('z.svg').read(),"Airing cupboard shelves guide: keep the cylinder area clear, use the warm shelf for airing, keep everyday towels in the middle and spare duvets on top.")
p(f"An airing cupboard is mainly where the hot water tank is kept, as heating maker {ext(VI,'Viessmann')} explains, and the warmth makes it a good place for towels, bedding and clothes after washing. Viessmann also advises not putting soaking wet items in the cupboard, not overfilling it so fabrics can breathe, and not covering slatted shelves with a board, because that interrupts the air flow. If your cylinder needs a jacket, the {ext(EST,'Energy Saving Trust')} says it should be at least 80 mm thick.")
h2("What Can You Store in an Airing Cupboard?")
p("An airing cupboard is ideal for towels, bed linen, duvets, pillows and clothes that need a final airing after washing. Avoid storing anything flammable, such as paint, aerosols or cleaning products, especially if a gas boiler shares the cupboard, and keep food and paperwork somewhere cooler.")
p(f"Gas boilers need extra care. A {ext(CW,'gas safety leaflet from Cheshire West and Chester Council')} warns that keeping flammable materials close to gas lines can increase the risk of fire, and that gas cupboards need to be easily accessible for maintenance, inspection and emergencies. If your boiler is in the airing cupboard, leave the space around it clear and check the boiler manual for the clearances it needs.")
h2("Quick Pick: Airing Cupboard Ideas by Problem")
table(["Your problem","Best ideas","Budget"],[
["Wobbly or missing shelves","#1, #2, #3","£–££"],
["Boiler or cylinder in the way","#3, #4, #16","£"],
["Renting, no drilling","#5, #11","£"],
["Bedding always in a muddle","#7, #8, #9","£"],
["Damp or musty smell","#13, #14, #15","£"]])
h2("How to Fit Airing Cupboard Shelves in 6 Steps")
lst(["<strong>Empty the cupboard.</strong> Take everything out and check for leaks, damp patches or a dripping valve before you add shelves.",
"<strong>Note what must stay reachable.</strong> The cylinder, pipes, valves, the immersion heater switch and any boiler controls.",
"<strong>Measure.</strong> Width, depth and height, and the height of the top of the cylinder.",
"<strong>Choose slatted shelves.</strong> Planed timber slats with small gaps let warm air rise through the stacks.",
"<strong>Fix battens to the walls.</strong> Screw timber battens to the side and back walls, level, then rest or screw the slatted shelves on top.",
"<strong>Load it by zone.</strong> Airing shelf just above the cylinder, everyday towels in the middle, spares on top."],True)
h2("Airing Cupboard Shelf Ideas")
p("These airing cupboard shelf ideas give you more storage without blocking the warmth or the parts a plumber needs to reach.")
h3("1. Fit Slatted Pine Shelves")
img(2)
p("Slatted shelves are the classic choice for a reason. Warm air from the cylinder rises through the gaps, so towels stay fresh, and the slats are cheap to make from planed pine. Leave a small gap between each slat and sand the edges so they do not snag your linen.")
h3("2. Run Battens Around Three Walls")
p(f"Screwing battens to the back and both side walls makes a shelf that is supported on three sides and will not sag under a pile of towels. Use a level and screw into solid wall or studs. Our {a('diy-closet-shelves','DIY closet shelves guide')} explains cleat shelves step by step.")
h3("3. Start the Shelves Above the Cylinder")
p("The lowest shelf should sit above the top of the cylinder, not around it. That keeps the pipes, valves and immersion heater switch easy to reach and leaves a clear space for a plumber to work. Cut a notch in the back slats only where a pipe has to pass, rather than boxing the pipes in.")
h3("4. Plan Shelves Around a Boiler With Care")
p("If a combi or system boiler hangs in the cupboard, keep shelves well away from it and from its flue, pipes and controls. Boiler manuals list the service clearances needed around the case, so check yours before you fit anything, and leave the area under the boiler empty.")
h3("5. Use a Freestanding Slatted Unit")
img(6)
p("Renting, or not allowed to drill? A freestanding slatted shelving unit gives you the same airy storage and moves with you. Choose one narrow enough to leave a clear gap on each side and keep it away from the cylinder and pipes.")
h3("6. Go Floor to Ceiling After a Combi Swap")
img(4)
p("Many homes lose their hot water cylinder when a combi boiler is fitted, which leaves an empty cupboard on the landing. Fill it with evenly spaced slatted shelves from floor to ceiling and it becomes a proper linen cupboard. It will not be as warm as before, so keep the slats and leave room for air.")
h2("Airing Cupboard Storage Ideas")
p("Once the shelves are in, these airing cupboard storage ideas keep everything easy to find.")
h3("7. Store Bedding Sets Inside a Pillowcase")
img(3)
p(f"Fold a duvet cover and fitted sheet, then slip them inside one of the matching pillowcases. Each set becomes one neat bundle, so you never hunt for the right pillowcase again. Our guide on {a('how-to-fold-clothes-to-save-space','how to fold clothes to save space')} shows the folds that keep stacks tidy.")
h3("8. Give Each Shelf One Job")
p("Towels on one shelf, bedding on the next, spare pillows on top. When every shelf has a single job, the cupboard stays tidy because everyone knows where things go back.")
h3("9. Roll Hand Towels and Flannels")
p("Small towels and flannels topple off a stack. Roll them and stand them in an open basket so you can grab one without pulling the rest out. Open baskets also let air reach the fabric.")
h3("10. Keep Spare Duvets in Cotton Bags")
p("Bulky spare duvets and pillows belong on the top shelf in breathable cotton bags, which keep dust off while letting the filling breathe. Avoid sealing them in plastic in a warm cupboard.")
h3("11. Use the Back of the Door")
img(5)
p(f"A shallow rack on the inside of the door holds rolled hand towels, spare toilet rolls or a lint roller. Check the rack does not hit the shelves when the door closes. For a larger linen store, see our guide to {a("linen-closet-organization","organising a linen store")}.")
h3("12. Sort by Room or by Person")
p("In a busy home, give each bedroom or each person a stack: one for the main bedroom, one for the children and one for guests. It makes changing beds much quicker.")
h2("Airing and Warmth Ideas")
p("An airing cupboard is warm, but it only works well if air can move and the heat is not wasted.")
h3("13. Finish Off Slightly Damp Items")
p("The shelf just above the cylinder is the warmest. Use it to finish off towels or clothes that are only slightly damp after the tumble dryer or washing line. Soaking wet washing adds moisture to the cupboard and can leave it smelling musty.")
h3("14. Never Cover the Slats")
p("It is tempting to lay a board over slatted shelves to stop small items falling through. Use a basket instead, because a solid board blocks the warm air that keeps the linen fresh.")
h3("15. Leave Room for Air to Move")
p("A cupboard packed to the door has no air flow. Leave a little space between stacks and at the back of each shelf. If the cupboard smells damp, take everything out, look for a leak and air it with the door open.")
h3("16. Insulate the Cylinder")
p(f"An uninsulated cylinder heats the cupboard but wastes energy. If yours has no factory foam or the jacket is thin, the {ext(EST,'Energy Saving Trust')} recommends a jacket at least 80 mm thick. The cupboard will still be warm enough to air linen.")
h2("Common Airing Cupboard Mistakes")
lst(["<strong>Boxing in pipes and valves.</strong> A plumber needs to reach them quickly if something leaks.",
"<strong>Solid shelves or boards over slats.</strong> They stop warm air rising through the linen.",
"<strong>Soaking wet washing.</strong> It adds moisture and can make the cupboard smell musty.",
"<strong>Storing flammable items.</strong> Paint, aerosols and cleaning products do not belong in a warm cupboard or near a gas boiler.",
"<strong>Overfilling every shelf.</strong> Packed linen cannot breathe.",
"<strong>Ignoring drips.</strong> A small leak from a valve or the cylinder can damage floors and ceilings below."])
h2("Airing Cupboard FAQ")
h3("Should airing cupboard shelves be slatted?")
p("Yes. Slatted shelves let warm air from the hot water cylinder rise through your towels and bedding, which keeps them dry and fresh. Solid shelves block that air flow, so if small items fall through the gaps, use an open basket rather than covering the slats with a board.")
h3("How far apart should airing cupboard shelves be?")
p(f"About 30 to 35 cm between shelves suits stacks of towels and folded bedding, and a little more on the top shelf for duvets and pillows. This is our rule of thumb, so measure your tallest stack first. Our {a('shelf-spacing-calculator','shelf spacing calculator')} works out the gaps for you.")
h3("Can you put shelves around a boiler?")
p("You can fit shelves in a cupboard with a boiler, but keep them away from the boiler case, flue, pipes and controls, and leave the space below it empty. Check your boiler manual for the service clearances, and never store flammable items in a cupboard with a gas boiler.")
h3("Can you store towels next to a hot water cylinder?")
p("Yes, towels and bedding are exactly what an airing cupboard is for. Keep them on shelves above or beside the cylinder rather than piled against it, so the cylinder, pipes and valves stay easy to reach and air can move around the linen.")
h2("Final Thoughts")
p(f"Good airing cupboard shelves are simple: slatted, fixed on battens, starting above the cylinder and loaded by zone. Keep the pipes reachable, the slats uncovered and the shelves not too full, and your towels and bedding will always come out warm and fresh. For more UK storage ideas, see our {a('boot-room-ideas','boot room ideas')} and {a('small-utility-room-ideas','small utility room ideas')}.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub('<[^>]+>',' ',re.sub(r'<svg.*?</svg>','',html,flags=re.S))
print(len(txt.split()),'words; kw',len(re.findall('airing cupboard shelves',txt,re.I)),'; ideas',len(re.findall(r'<h3 class="wp-block-heading">\d+\.',html)))
