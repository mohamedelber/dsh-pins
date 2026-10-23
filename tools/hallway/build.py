import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={
"adm":"https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/540330/BR_PDF_AD_M1_2015_with_2016_amendments_V3.pdf",
"fk":"https://firekills.campaign.gov.uk/escape",
"gm":"https://manchesterfire.gov.uk/your-safety/fire-safety/electrical/e-bikes-e-scooters-and-mobility-scooters",
"lfb":"https://www.london-fire.gov.uk/news/2014-news/londoners-warned-of-potential-fire-hazard-lurking-under-the-stairs",
"pp":"https://www.planningportal.co.uk/permission/common-projects/utilities/gas-safety",
"ikea":"https://www.ikea.com/gb/en/cat/shoe-cabinets-10456/",
"trones":"https://ikea.com/gb/en/p/trones-shoe-cabinet-storage-white-00397307",
"secure":"https://www.ikea.com/ie/en/ikea/secure-it/",
"stel":"https://www.stelrad.com/news-events/blog/do-radiator-covers-block-heat-what-you-actually-need-to-know/",
"ih":"https://www.idealhome.co.uk/house-manual/heating/home-decor-choices-increasing-my-heating-bills",
"hb":"https://www.homebuilding.co.uk/advice/how-to-build-understairs-storage",
"hbv":"https://www.homebuilding.co.uk/ideas/victorian-hallway-ideas",
"mb":"https://www.mybuilder.com/carpentry-joinery/price-guides/fitted-wardrobes-cost"}
def SR(k,t): return ext(SRC[k],t)

p(f"The best hallway storage ideas for a small UK home all follow one rule: keep the floor clear and build up the walls, never out into the walkway. In a typical narrow hall, a slim shoe cabinet less than 25 cm deep and a peg rail above it will clear most of the daily pile of shoes, coats and bags while still leaving room to walk past with the shopping.")
p("Below are 10 hallway storage ideas grouped by how wide your hall is, from tight terrace corridors under a metre wide to roomier entrance halls, plus the awkward spaces under the stairs and beside the door. First, a quick measurement tells you which ideas will actually fit.")
img(1)

h2("Measure First: How Much Depth Can You Spare?")
p(f"Before choosing from these hallway storage ideas, measure the width of your hall at skirting height, at its narrowest point, and take off the space you want to keep for walking. Our diagram uses 75 cm as a rule of thumb. That figure comes from Approved Document M, which for new homes says a short obstruction such as a radiator must not narrow a corridor {SR('adm','below a minimum 750mm width')}, and it asks for halls at least 900 mm wide in new homes built to its accessible M4(2) standard. Older houses do not have to meet it, but it is a sensible minimum for getting a pushchair or a laundry basket past.")
diagram(open('z.svg').read(),"Hallway storage depth budget: keep about 75 cm clear and the rest of the width is the depth you can use on one wall.")
p("Whatever is left over is your storage depth on one wall. Leave room for the front door to open fully, and do not count the space in front of a radiator. Put the deepest piece where the hall is widest, often near the stairs rather than right by the door.")

h2("Hallway Storage Ideas for a Very Narrow Hall (Under 1 Metre)")
h3("1. Hang a Peg Rail at Two Heights")
img(2)
p(f"In the narrowest halls, wall hooks take almost no depth at all, so they come first. A Shaker-style peg rail at about shoulder height holds coats and bags, and a second, lower rail lets children hang their own things, which speeds up school mornings. Hang one item per peg so the rail does not turn into a lumpy pile that sticks out into the hall. For the smaller things that drift onto the pegs, our {a('hat-storage-ideas','hat storage ideas')} and {a('backpack-storage-ideas','backpack storage ideas')} can help.")
h3("2. Choose a Slim Tip-Out Shoe Cabinet")
p(f"Tip-out shoe cabinets store shoes at an angle, so they can be very shallow. At the time of writing, IKEA UK lists its STÄLL four-compartment cabinet at {SR('ikea','96 x 17 x 90 cm')} for £99 and a GULLABERG version 22 cm deep for £79, while {SR('trones','TRONES units are 18 cm deep')} and sold in pairs. Anything up to about 22 cm deep fits the depth budget of a 1 metre hall. Fix tall or tip-out cabinets to the wall: IKEA says securing furniture to the wall is {SR('secure','the best way to help prevent furniture tip-over accidents')}. For more shapes and sizes see our {a('shoe-storage-ideas','shoe storage ideas')}.")
img(6)
p("The before and after above shows the difference those first two ideas make in the same hall: the shoe pile goes into a slim cabinet, and the heap of coats, bags and scarves comes down to a couple of coats on the peg rail.")
h3("3. Add a High Shelf for Things You Rarely Need")
p(f"The wall above head height is the most wasted space in a narrow hall. A single sturdy shelf above the front door or along one wall at about 2 to 2.1 metres takes spare hats, gloves and light bulbs out of the way without eating into the walkway. Keep it to light, soft items in boxes or baskets so nothing heavy falls on anyone. Our {a('shelf-spacing-calculator','shelf spacing calculator')} helps you set the gaps if you add more than one.")
h3("4. Pair a Mirror With a Small Key Shelf")
p(f"A mirror by the door is useful for the last check before you leave, and Homebuilding and Renovating calls mirrors {SR('hbv','a classic design trick')} for making narrow hallways feel wider and brighter. A small shelf or ledge under it, about 10 cm deep, catches keys, post and sunglasses. It is worth a thought for safety too: the government's Fire Kills campaign advises keeping door and window keys in a safe but accessible place near the exit, so you are not hunting for them in a fire. Our {a('picture-hanging-height-calculator','picture hanging height calculator')} shows where to hang the mirror.")

h2("Ideas for a Standard Hallway (About 1 to 1.2 Metres)")
h3("5. Sit Down on a Storage Bench")
img(3)
p(f"Once your hall is about 1.2 metres wide, a bench becomes possible, and it makes taking boots off much easier. Look for open cubbies or a lift-up seat underneath, and keep the depth to about 40 to 45 cm so you still keep your 75 cm walkway. Wet boots dry better on an open shelf or a tray than shut inside a box. If you have a little more space, our {a('boot-room-ideas','boot room ideas')} show how to turn a bench and hooks into a proper drop zone.")
h3("6. Use a Slim Console With Baskets Underneath")
p(f"A slim console table with a drawer gives the post, keys and dog leads a home, and the space underneath fits two or three baskets for gloves, scarves or shoes. IKEA BISSA shoe cabinets around 28 cm deep, which IKEA UK lists at {SR('ikea','49 x 28 x 93 cm')}, do the same job with doors and suit a hall about 1.1 metres wide. Keep the top clear of everything except a dish and a lamp, or it fills up within a week. Our {a('entryway-table-decor','hall table styling guide')} has a simple formula for styling it.")
h3("7. Work Around the Radiator, Not Over It")
p(f"Many British hallways have a radiator, and it is tempting to box it in to get a shelf. Be careful with the design: Stelrad, citing the Energy Saving Trust, says a poorly designed radiator cover {SR('stel','can reduce heat output by as much as 20 to 30%')}, while a well-designed one may lose around 5 to 10%. It recommends leaving 30 to 50 mm of space around the radiator inside a cover. For large furniture, Ideal Home quotes The Radiator Centre advising {SR('ih','at least 20–30 centimetres')} between a radiator and large pieces. A simple shelf mounted above the radiator, with an open front, keeps the heat flowing and still gives you a ledge for gloves to warm through.")

h2("Use the Awkward Spaces")
h3("8. Fill the Space Under the Stairs")
img(4)
p(f"If your stairs rise from the hall, the triangle underneath is worth planning carefully, because it is often the biggest storage space you have. Pull-out units that follow the slope, tall at one end and short at the other, keep coats, shoes and the hoover reachable without crawling into a dark cupboard. Homebuilding and Renovating says a carpenter-built version costs {SR('hb','around a minimum of £600')} for an average-sized space, and around £2,000 or more for a more complex design. Check what is already there first: gas meters and fuse boards often live under the stairs, and you must not {SR('pp','restrict adequate access to the emergency control')} of a gas meter. The London Fire Brigade warned in 2014 to keep coats, shoes and other things that burn {SR('lfb','well away')} from fuse boards. See our {a('under-stairs-storage-ideas','under stairs storage ideas')}, {a('under-stairs-shoe-storage','under stairs shoe storage')} and {a('under-stairs-cupboard-doors','under stairs cupboard doors')} for layouts.")
h3("9. Build a Cupboard Into an Alcove")
img(5)
p(f"Many terraced and semi-detached houses have a small recess beside the front door or the stairs. A floor-to-ceiling cupboard there hides coats, the vacuum and bags behind closed doors, which instantly makes a hall look calmer. Prices vary a lot; as a guide, MyBuilder puts mid-range fitted wardrobes at about {SR('mb','£400 to £800 per linear metre')}, though basic fitted wardrobes start from around £1,000, and a hall cupboard is likely to cost something similar. Our {a('built-in-wardrobe-ideas','built-in wardrobe ideas')} explain how to measure an alcove and plan the inside.")
h3("10. Rotate Coats and Shoes With the Seasons")
p(f"The cheapest of all hallway storage ideas is to store less in the hall. Keep only what each person wears this season, roughly one coat and two pairs of shoes each, and move the rest to a wardrobe or the loft in vacuum bags or boxes. Twice a year, swap them over. Our {a('loft-storage-ideas','loft storage ideas')} cover what is safe to store up there, and our {a('how-to-declutter-your-home','decluttering guide')} helps you decide what to let go.")

h2("Keep Your Way Out Clear")
p(f"A hallway is usually your escape route in a fire, so storage should never block it. The Fire Kills campaign tells households not to let {SR('fk','clutter, furniture or belongings block doors, hallways or windows')}. E-bikes and e-scooters are a particular risk: Greater Manchester Fire and Rescue Service says to {SR('gm','never charge or store')} them in hallways. If you live in a flat, keep shared corridors and stairways clear as well.")

h2("If You Only Do One Thing")
p(f"Measure your hall, work out your depth budget and buy the slimmest shoe storage that fits, with a peg rail above it. Of all the hallway storage ideas here, those two changes clear the floor fastest, which is what makes a small hall feel bigger. If you are in the US or reading about an entry rather than a hall, our {a('small-entryway-ideas','small entryway ideas')} cover the same problem with American sizes.")

h2("Hallway Storage Questions")
h3("Where should I store shoes in a narrow hallway?")
p("Use a tip-out shoe cabinet, because it stores shoes at an angle and can be very shallow. IKEA UK lists models from 17 to 22 cm deep, which fit a hall about one metre wide while keeping roughly 75 cm clear to walk. Fix it to the wall, and keep wet boots on a tray by the door.")
h3("What can I put in a small hallway?")
p("In a small hallway, choose things that are shallow or high: wall hooks or a peg rail, a slim shoe cabinet, a high shelf for rarely used items, and a mirror with a small key ledge. From about 1.1 metres wide a slim console fits, and from about 1.2 metres a storage bench.")
h3("How wide does a hallway need to be?")
p("There is no single rule for existing homes. For new accessible homes, Approved Document M asks for halls at least 900 mm wide and never narrower than 750 mm at a short obstruction such as a radiator. Keeping about 75 cm clear is a good guide when you add storage to an older hall.")
ai_note()
html='\n\n'.join(out)
html=re.sub(r'(\d+\.\d{2})\d+',r'\1',html)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('hallway storage ideas'),'kw')
