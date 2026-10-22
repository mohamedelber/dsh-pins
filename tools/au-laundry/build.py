import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={
"ncc4":"https://cpd.nccb.gov.au/editions/ncc-2022/adopted/housing-provisions/10-health-and-amenity/part-104-facilities",
"sa":"https://dit.sa.gov.au/__data/assets/pdf_file/0004/497452/Advisory_Notice_04_18_-_Laundry_facilities_in_residential_buildings_-_September_2018.pdf",
"fp":"https://www.fisherpaykel.com/au/laundry/washing-machines/front-load/front-loader-washing-machine-7.5-kg-wh7560j2-93230.html",
"dry":"https://www.winnings.com.au/p/fisher-paykel-8kg-heat-pump-dryer-dh8060p1",
"haier":"https://www.haier.co.nz/on/demandware.static/-/Sites-haier-master-catalog/default/dwd05e4bf9/DesignPlanning-HaierNZ/Haier-SpecificationGuide-en-HWD9060MW1-HWD1060MW1-WasherDryer-0-90005091A-AU-NZ.pdf",
"tub":"https://tradelink.com.au/eureka-45l-standard-tub-cabinet-no-tap-hole-single-by-pass-068285/",
"bun":"https://www.bunnings.com.au/diy-advice/home-improvement/design-inspiration/laundry-sinks-cabinets-and-troughs-how-to-choose-the-right-one",
"er":"https://energyrating.gov.au/node/37",
"wp":"https://ncc.abcb.gov.au/editions/ncc-2022/adopted/housing-provisions/10-health-and-amenity/part-102-wet-area-waterproofing",
"vba":"https://www.vba.vic.gov.au/news/news/2022/victorians-breaking-plumbing-rules-fined-tens-of-thousands-of-dollars",
"ausgrid":"https://ausgrid.com.au/safety/safety-at-home/diy-and-home-maintenance",
"tb":"https://www.threebirdsrenovations.com/blog/how-much-does-a-laundry-renovation-cost",
"schn":"https://www.schn.health.nsw.gov.au/kids-health-hub/safety-and-injury-prevention/home/poisons",
"accc":"https://recalls.gov.au/laundrysafe"}
def SR(k,t): return ext(SRC[k],t)

p(f"Small laundry ideas work best when you plan in millimetres first and decorate second. In Australia the National Construction Code doesn't set a minimum laundry size, but it does require {SR('ncc4','at least one washtub and space in the same room for a washing machine')}, so even the tiniest laundry needs room for both. A stacked washer and dryer beside a slim tub can fit on about 1.15 m of wall.")
p(f"This guide takes you through a small laundry in seven steps: measuring, choosing a layout for your size, picking appliances, fitting a tub and benchtop, adding storage, checking the rules and storing chemicals safely. If your laundry hides in a cupboard, see our {a('european-laundry-ideas','European laundry ideas')}; for more styling ideas, see our {a('small-laundry-room-ideas','small laundry room ideas')}.")
img(1)

h2("Step 1: Measure the Space and Find the Services")
p("Measure the length of the wall you can use, the depth from that wall to the doorway or opposite wall, and the ceiling height if you want to stack. Then mark where the cold and hot taps, the drain and the powerpoint are: moving them is usually the biggest cost in a small laundry. Note which way the laundry door swings and whether it will hit an open machine door.")
p(f"Write down the size of the machines you already own, or plan to buy, before you look at cabinets. Our {a('washer-dryer-space-calculator','washer and dryer space calculator')} checks whether they will fit in the gap you have.")

h2("Step 2: Choose the Layout That Fits Your Size")
p("Most small Australian laundries fall into one of three plans. The diagram shows each one from above with typical sizes, and the table below adds two common alternatives.")
diagram(open('z.svg').read(),"Small laundry layouts in mm: a single wall with a stacked washer and dryer, machines side by side under a benchtop, and a galley with shelves opposite.")
table(["Layout","Best for","Wall run (approx.)","Depth to plan for*"],[
["Single wall, stacked machines + tub","Laundries of about 1–1.5 m²","1,150 mm","1,550 mm (650 + 900)"],
["Side by side under a benchtop","A wider alcove or room","1,750 mm","1,550 mm"],
["Galley with shelves opposite","Narrow walk-through laundries","1,150 mm or more","1,900 mm (650 + 900 + 350)"],
["Laundry in the bathroom","Homes with no separate laundry","Washer + its own tub","Shared floor space"],
["Garage or carport corner","Older homes and units","Any","Vent a vented dryer outside"]])
p("*Our planning guide, worked out from typical appliance sizes: allow about 625 mm of width per machine, 499 mm for a 45 L tub cabinet, 650 mm of depth for the machines and about 900 mm of standing room in front. These are not building rules, so measure your own appliances.")
img(2)
p(f"A laundry can also share a room. South Australia's building advisory notice says laundry facilities {SR('sa','are permitted in a bathroom or kitchen')}, but where the washing machine sits there, that area must also have a laundry tub: a basin or kitchen sink doesn't count. In a hallway or bathroom, our {a('laundry-closet-ideas','laundry closet ideas')} show how to close it off neatly.")
img(4)

h2("Step 3: Pick Appliances That Fit")
p(f"Most full-size machines are 600 mm wide. A 7.5 kg Fisher &amp; Paykel front loader, for example, is {SR('fp','850mm high, 600mm wide and 590mm deep')}, while a matching 8 kg heat pump dryer is 645 mm deep and the retailer recommends {SR('dry','allowing an extra 150mm in depth for hoses and connections')}. Front loaders can be stacked with the dryer on a stacking kit made for your models; top loaders can't, because the lid opens upwards.")
p(f"Remember the doors. Haier's {SR('haier','planning guide')} gives an overall depth of 1,062 mm for one of its washer dryers with the door open, and a minimum cavity width of 625 mm. A combined washer dryer is the smallest option of all: one 600 mm machine that washes and dries.")
p(f"In a closed or windowless laundry, a heat pump dryer is the easiest choice. Energy Rating says vented dryers {SR('er','pump hot, humid air into the surrounding space')}, while heat pump dryers are much more energy efficient because they capture and reuse their heat.")

h2("Step 4: Fit a Tub and a Benchtop")
p(f"The tub is the part people try to skip in a tiny laundry, but the code requires one. A standard 45 L tub cabinet is {SR('tub','499mm')} wide, and Bunnings lists slimmer options, including a 16-litre mini tub {SR('bun','at just 300mm wide')} and a 310 mm-wide 25-litre square sink. A tub set flush into a benchtop over the machines gives you a folding surface and a single easy-to-wipe top.")
p("Leave a small gap between the top of the machines and the underside of the benchtop so they don't vibrate against it, and keep wall cabinets high enough that you can lean over the tub without hitting your head.")

h2("Step 5: Go Vertical With Storage")
img(3)
p(f"Floor space is what a small laundry lacks, so build up. Overhead cupboards hold refills and spare towels, a slim pull-out between the machines or beside the tub holds bottles, and a short hanging rail under the cupboards lets shirts dry on hangers. In a galley laundry, shallow open shelves of about 350 mm on the opposite wall keep the walkway clear. Our {a('laundry-room-cabinet-ideas','laundry cabinet ideas')} and guide to {a('how-to-organize-a-laundry-room','organising a laundry')} show what goes where; if towels overflow, move them to the {a('linen-closet-organization','linen cupboard')}.")

h2("Step 6: Check the Rules and Book the Trades")
p(f"Laundries are wet areas. Under the NCC Housing Provisions, {SR('wp','the floor of the room must be water resistant')}, the wall/floor junctions must be water resistant, and the wall behind the washing machine must be water resistant to at least 75 mm above and 75 mm each side of the tap outlets. If the laundry has a floor waste, the floor and junctions must be waterproof.")
p(f"A vented dryer must be ducted to outdoor air; condenser and heat pump dryers don't need a duct. New taps, drains and waste pipes are jobs for a licensed plumber: in Victoria, the building authority reported that people who broke plumbing rules were {SR('vba','fined tens of thousands of dollars')}. Moving or adding powerpoints needs a licensed electrician, and Ausgrid warns that {SR('ausgrid','DIY electrical is not only dangerous, it’s illegal')}.")
p(f"As a rough budget, Three Birds Renovations puts a small laundry renovation at about {SR('tb','$5,000 – $10,000')}, with mid-range jobs at $10,000 to $18,000 (July 2025). Prices vary by state and by how much plumbing moves, so get several quotes.")

h2("Step 7: Store Chemicals Safely")
p(f"Detergents and capsules are a real risk for children in a small laundry where everything is within reach. NSW children's health advice is to store poisons {SR('schn','at least 1.5 metres off the ground in a child-resistant locked cupboard')}, in their original containers. The ACCC says to {SR('accc','store laundry capsules up high, out of reach and sight of children')}. If anything is swallowed, call the Poisons Information Centre on 13 11 26.")
p(f"If your laundry is in the garage or by the back door, a bench, hooks and a boot tray can turn it into a drop zone too: see our {a('mudroom-ideas','mudroom ideas')}, or for British-style homes our {a('small-utility-room-ideas','small utility room ideas')}.")

h2("Small Laundry FAQ")
h3("What is the minimum size for a laundry in Australia?")
p("The NCC sets no minimum room size, but it does require at least one washtub and space in the same room for a washing machine. A 600 mm washer next to a 499 mm tub cabinet fits on about 1.1 m of wall, plus roughly 900 mm of standing room in front.")
h3("Can a laundry go in a bathroom?")
p("Yes. South Australia's advisory notice says laundry facilities are permitted in a bathroom or kitchen. A washbasin doesn't count as the laundry tub, so if the washing machine goes in the bathroom, a separate tub is needed there too. Moving water or waste pipes is work for a licensed plumber.")
h3("What should you not store in the laundry?")
p("Don't keep detergents, capsules or chemicals at child height. NSW children's health advice is to store poisons at least 1.5 metres off the ground in a child-resistant locked cupboard, in their original containers. If anything is swallowed, call the Poisons Information Centre on 13 11 26.")
h3("Do I need to vent a dryer in a small laundry?")
p("Only if it is a vented dryer. The NCC requires vented dryers to be ducted directly to outdoor air; condenser and heat pump dryers don't need a duct. Energy Rating says heat pump models are much more energy efficient, which suits closed, windowless laundries.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words; kw',html.lower().count('small laundry'))
