import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={
"cut":"https://cutmy.co.uk/ideas-advice/kitchen-unit-sizes",
"we":"https://www.worktop-express.co.uk/what-is-the-average-kitchen-worktop-height-and-depth/",
"nhs":"https://www.ouh.nhs.uk/media/lkonor55/115811kitchen.pdf",
"hsa":"https://hsa.ie/eng/education/managing_safety_and_health_in_schools/new_guidelines_files/manual-handling-no-13.pdf",
"rospa":"https://rospa.com/Keeping-Kids-Safe-Hub/Poisoning",
"gov":"https://www.gov.uk/understanding-food-labelling/best-before-and-use-by-dates",
"wrap":"https://wrap.ngo/media-centre/press-releases/urgent-action-needed-scale-tackle-food-waste-our-homes",
"mag":"https://www.magnet.co.uk/blog/kitchen-corner-unit-ideas/",
"utr":"https://www.ikea.com/gb/en/p/-20596787/",
"var":"https://www.ikea.com/gb/en/p/-80542961/",
"dun":"https://www.dunelm.com/product/joseph-joseph-set-of-3-pan-lid-holders-1000295274",
"ih":"https://www.idealhome.co.uk/kitchen/kitchen-ideas/how-to-organise-kitchen-cabinets-288669",
"kdw":"https://www.kitchendoorworkshop.co.uk/news/organise-your-kitchen-5-zones/"}
def SR(k,t): return ext(SRC[k],t)

p(f"To organise kitchen cupboards, empty one run of cupboards at a time, get rid of what you do not use, then put things back by height and by where you use them: everyday items between waist and shoulder height, heavy pans and appliances low down, and rarely used things on the top shelf. A shelf riser, a pan lid rack and a turntable fix most of the space problems, and the riser and lid holders below cost £7 and £12 at the time of writing.")
p("Doing it properly takes about an afternoon in a typical small UK kitchen. Start with the diagram: it shows the standard heights most British kitchens are built to, and which zone each kind of item belongs in.")
img(1)

h2("Where Everything Should Go")
p(f"Most UK kitchens follow the same basic sizes. The standard worktop is {SR('we','900mm')} high, base units are about 560mm deep, and wall units are about 300mm deep and hung with their {SR('cut','bottom edge 450-500mm above the worktop')}, according to the kitchen supplier cutmy.co.uk. That puts the lowest wall shelf at roughly 1,350 to 1,400 mm from the floor, which makes it the easiest wall shelf to reach.")
diagram(open('z.svg').read(),"Kitchen cupboard zones by height: everyday items in the middle, heavy items low, rarely used items high, cleaning products high or locked and away from food.")
p(f"The rule behind the zones is simple. An NHS occupational therapy leaflet advises people to {SR('nhs','store everyday items at waist or countertop level')}, and Ireland's Health and Safety Authority, in its workplace manual handling guidance, recommends keeping {SR('hsa','heavier items')} on middle shelves rather than on the floor or above shoulder height. Plates you use three times a day should never need a step stool.")

h2("Step 1: Empty One Run of Cupboards at a Time")
p("When you organise kitchen cupboards, do not empty the whole kitchen at once, or you will still be surrounded by saucepans at dinner time. Pick one run, such as the wall cupboards above the kettle, take everything out and wipe the shelves. Check the shelf pins while the cupboard is empty: moving an adjustable shelf up or down a few holes is often all you need to fit an extra row of mugs.")

h2("Step 2: Sort Into Groups and Let Go")
img(2)
p(f"Put everything on the worktop in groups: food, crockery, baking and roasting trays, gadgets, and a box for things to give away. Professional organiser Vicky Silverthorn told Ideal Home the point is to {SR('ih','see what you have, what you actually use')}. Duplicates, chipped mugs, the third garlic press and gadgets you have not touched for a year can go. Check dates on food as you sort. GOV.UK explains that a best before date is about quality, while a use by date means the food is {SR('gov','no longer safe to eat')} after it.")

h2("Step 3: Give Every Group a Home Near Where You Use It")
p(f"Zoning means storing things next to the job they are used for. Kitchen Door Workshop suggests you {SR('kdw','store your crockery and glassware close to your sink or dishwasher')}, and organiser Kathryn Lord told Ideal Home to keep herbs and spices near the hob. In a typical small kitchen that gives you four zones:")
lst(["<strong>Washing up:</strong> plates, bowls and glasses in the wall cupboard nearest the dishwasher or sink.",
"<strong>Cooking:</strong> pans, oils, utensils and spices next to the hob and oven.",
"<strong>Prep:</strong> chopping boards, knives, mixing bowls and scales by your longest stretch of worktop.",
"<strong>Drinks:</strong> mugs, tea, coffee and the sugar above or beside the kettle."])
p(f"For smaller items in the top drawers, our guide to {a('how-to-organize-kitchen-drawers','organising kitchen drawers')} shows how to divide cutlery and utensils.")

h2("Step 4: Put Heavy Things Low")
img(3)
p(f"Saucepans, casserole dishes, the slow cooker and bags of potatoes belong in the base cupboards or deep drawers. Nest saucepans by size and stand frying pans or lids upright so you can lift one out without moving the rest. A set of three {SR('dun','pan lid holders costs £12 at Dunelm')} and can be fixed inside a cupboard door or a deep drawer; measure the gap between the door and the shelves before you fit anything to a door, so it still closes. If plastic tubs are the problem, our guide on {a('how-to-organize-tupperware','how to organise food containers')} sorts out the lids.")

h2("Step 5: Double the Height of Your Shelves")
p(f"Most cupboard shelves waste the space above a single stack of plates. A shelf riser creates a second level, so bowls sit above the plates instead of on top of them. IKEA UK lists a VARIERA {SR('var','shelf insert for £7')} at 45.5 x 29 x 16 cm. Measure the inside depth of your wall cupboards first: standard units are about 300mm deep from the outside, so a 29 cm insert may not fit. IKEA sells smaller sizes too, so check the depth before you buy. Tins can go on a stepped riser so you can read every label at once.")

h2("Step 6: Fix the Corner Cupboard")
img(4)
p(f"Blind corner cupboards are where things get lost. The cheapest fix is a turntable on the shelf, which brings bottles and jars from the back to the front with a spin. If you are willing to spend more, Magnet explains the options: carousels, Le Mans units with two kidney-shaped shelves that glide out, and magic corners that pull the back shelves forward, with carousel baskets that {SR('mag','typically')} take up to 25 kg each. As a price guide, IKEA's UTRUSTA corner carousel is {SR('utr','£90')} and fits IKEA's own METOD 88 x 60 cm corner base unit. For deep shelves and tall food cupboards, see our guide to {a('how-to-organize-a-pantry-with-deep-shelves','organising a pantry with deep shelves')}.")

h2("Step 7: Keep Food in Date and Cleaning Products Apart")
p(f"Put new food behind the old so the oldest gets used first. It matters more than it sounds: WRAP estimates, using 2021 data, that food waste {SR('wrap','costs a four-person household around £1,000 per year')}. Clear, square containers for pasta, rice and cereal save space and show you when you are running low; our {a('pantry-organization-ideas','pantry organisation ideas')} have more ways to store dry food.")
p(f"Cleaning products do not belong next to food. RoSPA advises keeping household chemicals, including laundry capsules, {SR('rospa','out of the sight and reach of children')}, ideally high up in a locked cupboard, and always in their original containers. If you have space, move them out of the kitchen altogether; our {a('small-utility-room-ideas','small utility room ideas')} show where they can go instead.")

h2("The Result")
img(5)
p("This illustration shows the steps above applied to two wall cupboards: the mugs are in one row, dry food is in matching jars, and shelf risers put the bowls above the plates.")

h2("If Your Kitchen Is Different")
lst(["<strong>No wall cupboards:</strong> use open shelves for everyday plates and glasses, and keep the base cupboards for everything else.",
"<strong>Renting:</strong> shelf risers, turntables and freestanding lid racks all go in without screws.",
"<strong>Very small kitchen:</strong> move rarely used items, such as the roasting tin or party glasses, to another room, and use the walls; our "+a('kitchen-storage-ideas','kitchen storage ideas')+" and "+a('kitchen-counter-organization','worktop organisation tips')+" help.",
"<strong>In the US?</strong> Our guide to "+a('how-to-organize-kitchen-cabinets','organizing kitchen cabinets')+" uses American sizes."])

h2("Kitchen Cupboard Questions")
h3("What is the best way to organise kitchen cupboards?")
p("The best way to organise kitchen cupboards is to store things by how often you use them and where you use them. Keep everyday items between waist and shoulder height near the sink, hob or kettle, heavy pans in base cupboards, and rarely used things on the top shelf. Then add shelf risers and a turntable so nothing is hidden behind something else.")
h3("What should not be stored in kitchen cupboards?")
p("Keep cleaning chemicals and laundry capsules away from food, ideally high up in a locked cupboard if children visit. Do not store heavy items above shoulder height. Food that says keep refrigerated after opening belongs in the fridge, which GOV.UK says should be at 5°C or below, not back in the cupboard.")
h3("How do I organise a kitchen with no space?")
p("Start by removing anything you use less than once a month and storing it elsewhere. Then use height: shelf risers in wall cupboards, lids on a rack, pans nested by size. A turntable in a corner cupboard and hooks under a shelf add space without building anything.")
ai_note()
html='\n\n'.join(out)
html=re.sub(r'(\d+\.\d{2})\d+',r'\1',html)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('organise kitchen cupboards'),'kw')
