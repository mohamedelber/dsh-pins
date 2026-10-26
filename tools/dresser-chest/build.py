import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={"mw":"https://www.merriam-webster.com/dictionary/dresser",
"mwc":"https://www.merriam-webster.com/dictionary/chest%20of%20drawers",
"oxb":"https://www.oxfordlearnersdictionaries.com/us/definition/english/bureau",
"oxt":"https://www.oxfordlearnersdictionaries.com/us/definition/english/tallboy",
"oxd":"https://www.oxfordlearnersdictionaries.com/definition/english/dresser",
"brit":"https://www.britannica.com/topic/chest-of-drawers",
"lowboy":"https://www.dictionary.com/browse/lowboy",
"lowes":"https://www.lowes.com/n/buying-guide/chest-of-drawers-vs-dresser",
"wf":"https://www.wayfair.ca/sca/ideas-and-advice/rooms/dresser-dimensions-how-to-choose-the-right-one-T1079",
"col":"https://colemanfurniture.com/resources/buying-guides/dresser-dimensions-guide",
"ash":"https://blog.ashleyfurniture.com/?p=20289",
"skw":"https://www.ikea.com/us/en/p/-60561248",
"skt":"https://www.ikea.com/us/en/p/storklinta-6-drawer-dresser-dark-brown-oak-effect-anchor-unlock-function-70559278/",
"fgw":"https://www.ikea.com/us/en/p/-90627993/",
"fgt":"https://www.ikea.com/us/en/p/fagelfjaellet-6-drawer-dresser-black-oak-effect-30611645/",
"ikcat":"https://www.ikea.com/us/en/cat/dressers-storage-drawers-st004/",
"dims":"https://www.dimensions.com/element/dresser-chest-bedroom-clearances",
"hunk":"https://www.hunker.com/13412472/how-much-walking-space-should-be-around-bedroom-furniture",
"irc":"https://buildingcodetrainer.com/minimum-bedroom-size/",
"atc":"https://www.apartmenttherapy.com/dresser-in-a-bedroom-closet-36988327",
"rh":"https://www.realhomes.com/advice/where-to-put-a-dresser-in-a-small-bedroom",
"fr":"https://www.govinfo.gov/content/pkg/FR-2023-05-04/html/2023-08997.htm",
"itk":"https://www.intertek.com/products-retail/insight-bulletins/2023/sturdy-act-final-rule-published/",
"cpsc23":"https://www.cpsc.gov/s3fs-public/2023_Annual_Tip_Over_Report_Posted_2024Feb_FINAL_0.pdf",
"cpscnr":"https://www.cpsc.gov/Newsroom/News-Releases/2024/Ahead-of-Sundays-Game-CPSC-Reminds-Families-to-Tackle-the-Deadly-Hazard-of-TV-and-Furniture-Tip-Overs",
"cpsc22":"https://www.cpsc.gov/Newsroom/News-Releases/2022/CPSC-Injury-and-Fatality-Report-Shows-Despite-Some-Progress-Need-for-TV-and-Furniture-Tip-Over-Prevention-Remains-Strong",
"cpsc20":"https://www.cpsc.gov/Newsroom/News-Releases/2020/Latest-Anchor-It-Statistics-Show-Nearly-80-of-All-Furniture-TV-and-Appliance-Tip-Over-Fatalities-Involve-Children-5-Years-Old-and-Younger",
"cr":"https://www.consumerreports.org/child-safety/tv-tip-over-danger-to-children-a2119931225/",
"aap":"https://www.healthychildren.org/English/safety-prevention/at-home/Pages/Changing-Table-Safety.aspx",
"atd":"https://www.apartmenttherapy.com/expert-hacks-organizing-dresser-drawers-36976577"}
def SR(k,t): return ext(SRC[k],t)

p(f"A dresser is wide and low, with two or three columns of drawers and room for a mirror on top; a chest of drawers is tall and narrow, with one stacked column. Pick a dresser if you have a long wall and want a surface; pick a chest if floor space is tight. In a matched IKEA pair with the same six drawers and the same price, the tall chest uses half the floor for about 81% of the storage. Whichever you choose, anchor it to the wall: the CPSC says a chest, bureau or dresser was involved in {SR('cpsc23','36 percent (79 out of 217')} tip-over deaths it recorded from 2013 to mid-2023.")
img(1)

h2("Dresser vs Chest of Drawers at a Glance")
table(["","Dresser","Chest of drawers"],[
["Shape","Wide and low, 2–3 drawer columns","Tall and narrow, 1 column"],
["Typical height",f"30–36 in ({SR('col','Coleman')})",f"44–60 in ({SR('lowes','Lowe\'s')})"],
["Typical width","50–70 in","24–38 in"],
["Depth","18–22 in","16–22 in"],
["Drawers","6–9","4–6"],
["Top surface","Large: mirror, lamp, tray","Small: lamp or plant"],
["Best for","Long walls, primary bedrooms","Small rooms, narrow walls, corners"],
["IKEA US price range","$69.99–$649.99 across both types",""]])
p("Ranges come from Coleman Furniture, Lowe's and Wayfair buying guides. Real products sit at both ends, so measure the piece you are buying, not the category.")

h2("Same Drawers, Different Shape: The Floor-Space Math")
diagram(open('z.svg').read(),"The same six drawers as a wide dresser and a tall chest: the chest takes half the floor and gives 81% of the storage.")
p(f"Buying guides give ranges, so we compared two real products that differ only in shape. IKEA's STORKLINTA 6-drawer comes as a wide unit, {SR('skw','55 1/8 x 18 7/8 x 29 1/2 inches')} with a listed {SR('skw','storage capacity 8.4 cu.ft')}, and as a tall unit of 27 1/2 x 18 7/8 x 47 1/4 inches with {SR('skt','storage capacity 6.8 cu.ft')}. Both cost $249.99 and use the same 24 x 15 3/4 inch drawers. Multiply width by depth and the wide one covers 7.2 square feet of floor, the tall one 3.6. That is 1.16 cubic feet of storage per square foot of floor for the dresser and 1.89 for the chest.")
p(f"A second pair says the same. IKEA's FÅGELFJÄLLET 6-drawer is {SR('fgw','63 x 20 1/8 x 30 3/4 inches')} and 9.1 cubic feet as a dresser, and 32 1/4 x 20 1/8 x 48 3/8 inches and {SR('fgt','7.6 cu.ft')} as a chest, so the chest uses 51% of the floor for 84% of the storage, and costs $70 less. Floor area is only half the story: you also need room to open the drawers. Wayfair recommends {SR('wf','36\" of clearance')} in front of a dresser, which turns the STORKLINTA pair into about 21 and 10.5 square feet of floor in use.")

h2("The Dresser: Best For, Avoid If")
img(2)
p(f"Merriam-Webster defines a dresser as {SR('mw','a chest of drawers or bureau with a mirror')}, and Ashley says its drawers are {SR('ash','organized horizontally into two or three columns')}. The wide top is the main reason to buy one: it holds a lamp, a tray and a mirror, and at 30 to 36 inches it sits at a comfortable height to stand at. Lowe's adds that a low piece suits a room with a low ceiling, because {SR('lowes','a dresser will help create the illusion of a larger room')}.")
lst(["<strong>Best for:</strong> a primary bedroom with a long, unbroken wall; couples who want one drawer column each; anyone who wants a dressing surface with a mirror.",
"<strong>Avoid if:</strong> the only free wall is under 5 feet, the room is narrow (a 20-inch-deep dresser plus 36 inches to open it needs almost 5 feet from the wall), or you planned to put a TV on top (see the safety section)."])

h2("The Chest of Drawers: Best For, Avoid If")
img(3)
p(f"A chest stacks its drawers in one column. Lowe's puts a typical chest {SR('lowes','between 44 and 60 inches tall and between 24 and 38 inches wide')}, and calls chests {SR('lowes','perfect for corners and small rooms')}. Very narrow ones exist: IKEA's STORKLINTA 5-drawer is {SR('ikcat','15 3/4 inches wide')}, small enough for the gap beside a door or window. A chest also fits inside many closets; Apartment Therapy notes that {SR('atc','closets are usually about 24 inches deep')}, while most chests and dressers are under 20.")
lst(["<strong>Best for:</strong> small bedrooms, a narrow wall between a window and a door, a closet, kids' rooms, and a second storage piece next to a dresser.",
"<strong>Avoid if:</strong> you want a surface to get ready at, or the top drawers would sit above a short person's eye level. The tallest chests reach 60 inches."])

h2("Bureau, Highboy, Lowboy, Tallboy: What the Names Mean")
p(f"The names overlap, and US and UK English use them differently. In North American English a bureau is simply a chest of drawers, but in British English it is {SR('oxb','a desk with drawers')}. A highboy is a tall chest on legs, the same piece Britannica says was {SR('brit','once known as tallboys in England and highboys in America')}. A lowboy is {SR('lowboy','a low chest of drawers on short legs')}. And a British \"dresser\" is something else again: a cupboard with open shelves on top for plates. Retailers blur the terms too: IKEA US calls its 47-inch-tall single-column STORKLINTA a \"dresser\" in the title and a \"chest of drawers\" in the description, so go by the measurements.")

h2("Whichever You Pick, Anchor It")
img(4)
p(f"Tall or wide, drawer units can tip when a child climbs the open drawers. The CPSC recorded {SR('cpsc23','217 reports of product instability or tip-over-related fatalities')} from January 2013 to July 2023; 71% of the victims were children, and a chest, bureau or dresser was involved in 79 of them. The agency says a child is treated in an emergency department {SR('cpscnr','every 53 minutes')} for a tip-over injury.")
p(f"Since September 1, 2023, new clothing storage units sold in the US must meet a federal stability standard under the STURDY Act. It covers units {SR('fr','27 in. (686 mm) or greater in height')} that weigh 30 pounds or more and hold at least 3.2 cubic feet, so both of our STORKLINTA examples are covered. Covered units must pass stability tests and come with an anti-tip device. Older furniture is not covered, so anchor it too.")
lst([f"<strong>Use the kit.</strong> The CPSC says to {SR('cpsc22','anchor TVs and furniture, such as bookcases and dressers, securely to the wall')}. It adds that most kits cost less than $20.",
f"<strong>Load it low.</strong> CPSC advice: {SR('cpsc22','store heavier items on lower shelves, or in lower drawers')}.",
f"<strong>No TV on top.</strong> Consumer Reports' advice is to {SR('cr','avoid placing TVs on dressers and chests')}; use a TV stand or wall mount instead.",
"<strong>Keep toys and remotes off the top</strong>, so children are not tempted to climb."])

h2("Our Pick for Each Room")
lst([f"<strong>Small bedroom:</strong> a chest. Under the International Residential Code, a habitable room can be as small as {SR('irc','70 square feet')} and 7 feet across; in a room like that, saving 10 square feet of floor matters. Our {a('box-room-bedroom-ideas','box room bedroom ideas')} show what else fits.",
"<strong>Primary bedroom with a long wall:</strong> a dresser, with a mirror above, opposite or beside the bed.",
f"<strong>Closet:</strong> a low chest or narrow dresser. Real Homes quotes interior designer Alessia Lamonaca: {SR('rh','a low-profile dresser fits nicely in most closets directly underneath a clothing rod')}. See our {a('small-closet-organization-ideas','small closet organization ideas')}.",
f"<strong>Nursery:</strong> a dresser can double as a changing table only with a proper changing topper. The AAP recommends {SR('aap','a 2-inch (5 cm) guardrail around all four sides')}, and says never to leave a baby on it, even for a moment. Anchor the dresser first.",
"<strong>Shared kids' room:</strong> one chest per child saves floor space and avoids arguments about whose drawer is whose.",
f"<strong>Studio or first apartment:</strong> a chest by the closet and the bed as your seat. Our {a('studio-apartment-ideas','studio apartment ideas')} cover the rest of the layout."])

h2("How to Organize the Drawers")
img(5)
p(f"Professional organizer Katrina Hassan's rule, in Apartment Therapy: {SR('atd','fill the top drawers with items you put on first')}, so underwear and socks go up top and jeans lower down, which also keeps heavier things low. Sangita Evans suggests you {SR('atd','eliminate layers and file your clothing instead')}, standing folded clothes on edge so you can see everything. In a wide dresser drawer, Rashelle Isip recommends {SR('atd','creating at least three to four sections')} with dividers. Our guide to {a('how-to-fold-clothes-to-save-space','folding clothes to save space')} shows the folds, and our {a('small-bedroom-storage-ideas','small bedroom storage ideas')} cover what goes where else.")

h2("Decision Checklist")
lst(["Is there a free wall at least 5 feet long, with about 3 feet clear in front? If yes, a dresser fits.",
"Is floor space your biggest problem? If yes, choose a chest.",
"Do you want a surface with a mirror to get ready at? If yes, choose a dresser.",
"Will it go in a closet, a corner or beside a door? If yes, choose a chest.",
"Are there young children in the home? Either works, but anchor it the day it arrives."],ordered=True)
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('dresser vs chest of drawers'),'kw')
