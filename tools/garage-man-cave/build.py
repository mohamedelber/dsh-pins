import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={"cdc":"https://archive.cdc.gov/www_cdc_gov/media/releases/2021/p0217-winter-safety-tips.html",
"cdc2":"https://www.cdc.gov/natural-disasters/psa-toolkit/prevent-carbon-monoxide-poisoning.html",
"irc":"https://www.law.cornell.edu/regulations/south-carolina/R-8-1206",
"wa":"https://mybuildingpermit.com/sites/default/files/TS_06_Residential_Garage_Separation_2021_IRC_Final_0.pdf",
"gfci":"https://www.ecmweb.com/national-electrical-code/qa/article/20900093/code-qa-gfci-protection-requirements-in-a-dwelling-unit-garage",
"heat":"https://www7.mississauga.ca/documents/fire/2018/Portable_space_heater_safety_tips_NFPA.pdf",
"unv":"https://www.cpsc.gov/Newsroom/News-Releases/2012/CPSC-Issues-Warnings-On-Use-Of-Space-Heaters-Offers-Eight-Point-Safety-Checklist",
"gas":"https://www.mass.gov/service-details/gasoline-safety",
"lehi":"https://www.lehi-ut.gov/departments/fire-department/fire-prevention/home-fuel-storage-limits/",
"permit":"https://kirklandwa.gov/Government/Departments/Development-Services-Center/Do-you-need-a-permit/Garage-Conversions",
"tv":"https://www.soundandvision.com/content/screen-size-and-seating-distance",
"doe":"https://www.energy.gov/node/1265581",
"door":"https://basc.pnnl.gov/diy-guides/insulate-and-weatherstrip-garage-door"}
def SR(k,t): return ext(SRC[k],t)
p("The best garage man cave ideas turn a cold, cluttered garage into the room everyone wants to hang out in: a comfortable sofa, a big screen, a small bar and a place for the tools you still need. Because a garage already has space, a door to the outside and often its own power, it is one of the easiest rooms in the house to transform.")
p("This guide gives you a simple zone plan for a two-car garage, the permit and safety basics to check first, a 7-step plan and 18 man cave ideas for a garage, covering comfort, entertainment, the bar, storage and style. Most ideas work in a one-car garage too, and many need no building work at all.")
img(1)
summary(["<strong>Quick answer:</strong> Clear the garage, insulate it and sort out heating, then split it into zones: a lounge with a sofa and TV, a small bar, a game table and one storage wall for tools. Finish the floor with sealed concrete, tiles and a big rug, and add warm, layered lighting.",
"Check your city's permit rules before you turn a garage into living space, and keep the fire-rated door to the house.",
"Never run a car or engine inside, install a CO alarm and use GFCI-protected outlets."],
"<strong>Time:</strong> a weekend to a few weeks · <strong>Cost:</strong> about $500 to $5,000+ · <strong>Difficulty:</strong> Easy to moderate")
toc("garage-man-cave-ideas")
h2("Before You Start: Permits and Safety Basics")
p(f"A garage hangout with a sofa and a rug is usually just furniture, but a full conversion into living space is building work. The City of Kirkland, Washington, for example, says a garage conversion {SR('permit','requires a building permit, and may require electrical, mechanical and plumbing permits')} as well, and that heating, insulation, smoke and carbon monoxide alarms must meet code. Some cities also require you to keep off-street parking, so call your local building department first.")
lst([f"<strong>Keep the door to the house fire-rated.</strong> The International Residential Code calls for {SR('irc','solid wood doors not less than 1 3/8 inches')} thick, solid or honeycomb-core steel doors of the same thickness, or 20-minute fire-rated doors between a garage and the house. The 2021 IRC also requires the door to be self-closing and self-latching, though some states amend this.",
f"<strong>Keep the fire barrier.</strong> The code also requires {SR('wa','not less than 1/2-inch gypsum board')} on the garage side of walls and ceilings separating it from the house and attic (5/8-inch Type X on the ceiling if there are rooms above), so don't strip it out to add paneling; put any wood finish on top of it.",
f"<strong>No engines inside.</strong> The CDC warns: {SR('cdc','never run a car or truck inside a garage attached to your house, even if you leave the garage door open')}.",
f"<strong>Use GFCI outlets.</strong> Under the National Electrical Code, {SR('gfci','GFCI protection is required for all 15A and 20A, 125V receptacles in garages')}. Have a licensed electrician add circuits for a TV, fridge or heater."])
h2("The Garage Man Cave Zone Plan")
p("The easiest way to plan a man cave is to give every activity its own zone, with clear walkways between them. Here is an example layout for a standard 20 x 20 ft two-car garage.")
diagram(re.sub(r'(\d+\.\d{1,2})\d+',r'\1',open('z.svg').read()),"The garage man cave zone plan: a lounge, a bar, a game table, a storage wall and a clear path from the house door in a 20 x 20 ft two-car garage.")
table(["Zone","What goes there","Space to allow (our estimate)"],[
["A. Lounge","Sofa, rug, TV, side table","About 10 x 12 ft"],
["B. Bar","Counter, 2 stools, small fridge","About 2 ft deep plus 3 ft for stools"],
["C. Game table","Card or game table and chairs","About 10 x 10 ft with chairs pulled out"],
["D. Storage wall","Workbench, pegboard, cabinets","About 2 ft deep along one wall"],
["E. Path","Walkway from the house door","At least 36 in wide"]])
p("These sizes are our own planning estimates, not code minimums. In a one-car garage, drop the game table and put the bar along the back wall.")
h2("Quick Pick: Garage Man Cave Ideas by Situation")
table(["Your situation","Best ideas","Cost"],[
["Small budget","#3, #6, #10, #16","Low"],
["One-car garage","#6, #10, #13, #18","Low to medium"],
["Cold winters or hot summers","#1, #2, #4","Medium to high"],
["Still need to park or work on the car","#13, #14, #18","Low to medium"],
["Big game days","#6, #7, #10, #11","Medium"]])
h2("How to Turn a Garage Into a Man Cave in 7 Steps")
lst(["<strong>Clear everything out.</strong> Sort what stays, what moves to storage and what goes.",
"<strong>Check the rules.</strong> Ask your building department about permits, and your HOA or lease about any limits.",
"<strong>Fix the shell.</strong> Seal gaps, insulate walls and the garage door, and plan heating and cooling.",
"<strong>Sort the power.</strong> Have an electrician add GFCI-protected outlets and circuits where the TV, bar and heater will go.",
"<strong>Finish the floor.</strong> Clean and seal the concrete, then add tiles or a big rug in the lounge zone.",
"<strong>Set up the zones.</strong> Lounge first, then bar, games and a storage wall, keeping a 36 in path.",
"<strong>Add the finishing touches.</strong> Lighting, an accent wall, art and a few comfortable extras."],True)
img(6)
h2("Comfort Basics: Insulation, Floors and Climate")
h3("1. Insulate the Walls")
p(f"Insulation is what turns a garage into a room you want to sit in. The U.S. Department of Energy recommends that you {SR('doe','insulate all exterior walls, including walls between living spaces and unheated garages')}. If the walls are open studs, insulate them and cover them with drywall, keeping the gypsum board on any wall shared with the house.")
h3("2. Insulate and Seal the Garage Door")
p(f"The garage door is the biggest weak spot. A guide from the Department of Energy's Building America program recommends that you {SR('door','install garage door insulation to help maintain moderate temperatures')}, and new weatherstripping along the bottom and sides stops drafts.")
h3("3. Upgrade the Floor")
p(f"Clean and seal the concrete, or use an epoxy floor coating, then lay interlocking rubber or foam tiles in the lounge zone and a large rug on top. A rug defines the seating area and softens the sound; our {a('rug-size-calculator','rug size calculator')} helps you pick one that fits the sofa and chairs.")
h3("4. Heating and Cooling That Is Safe")
img(5)
p(f"A ductless mini-split heat pump is the most comfortable year-round option and needs a professional install. If you use a portable electric space heater, NFPA advice is to {SR('heat','keep the heater at least 3 feet away from anything that can burn')}, plug it straight into a wall outlet and turn it off when you leave. The CPSC warns that {SR('unv','unvented heaters, which burn natural gas, liquified petroleum and other fuels pose the greatest threat')}, so skip fuel-burning heaters in a closed garage.")
h3("5. Layered Lighting")
p("Replace a single bare bulb with layers: bright ceiling lights for the work zone, pendants over the bar and game table, and lamps in the lounge. Warm-white bulbs make concrete and metal feel far more inviting at night.")
h2("Lounge and Entertainment Ideas")
h3("6. A Real Sofa on a Big Rug")
p("A comfortable sofa or a pair of recliners on a large rug is the heart of the room. Place it so you face the TV on a side wall, and keep the walkway from the house door clear.")
h3("7. A TV Wall at the Right Size and Height")
p(f"Mount the TV on the side wall opposite the sofa, not on the garage door. For screen size, Sound & Vision notes that SMPTE guidance gives {SR('tv','a minimum viewing angle of 30 degrees')} as a starting point. Our {a('tv-mounting-height-calculator','TV mounting height calculator')} tells you how high to hang it for your seating.")
h3("8. A Game Table or Compact Pool Table")
img(3)
p("A card table with four chairs fits almost any garage; a pool table needs much more room because of the cue length, so check the maker's room-size chart before you buy. Hang a pendant light over the table, and add a wall rack for cues or games.")
h3("9. Sound That Stays In")
p("Concrete and bare walls echo. A large rug, a fabric sofa, curtains over any windows and a few fabric acoustic panels make movies and music sound better and cut the echo; insulating the shared wall and weatherstripping the house door keeps noise from the rest of the house.")
h2("Bar Ideas for a Garage Man Cave")
h3("10. A Simple Bar Counter")
img(2)
p("A wooden counter along one wall with two stools gives you a bar, even without plumbing; add a small sink only if a plumber can tie it in. Add open shelves above for glasses and mugs, and leave about 3 ft behind the stools so people can walk past.")
h3("11. A Fridge on Its Own Outlet")
p("A small fridge keeps drinks cold for game day. Plug it into its own GFCI-protected outlet (required in garages; check now and then that it hasn't tripped) rather than an extension cord, choose a garage-ready model if the space isn't climate-controlled, and leave the gap around it that the manual asks for so it can vent heat.")
h3("12. A Coffee and Snack Station")
p("Not every man cave needs a bar. A coffee maker, a kettle and a basket of snacks on the same counter make the room useful in the morning too.")
h2("Garage Man Cave Storage Ideas")
h3("13. One Storage Wall With a Workbench")
img(4)
p(f"Keep the tools, but put them all on one wall: a workbench, a pegboard above it and closed cabinets on each side. Closed doors hide the clutter from the lounge. Our {a('shelf-spacing-calculator','shelf spacing calculator')} helps you plan shelves at useful heights.")
h3("14. Overhead Storage Racks")
p(f"Ceiling racks hold seasonal bins clear of the garage door track and opener, or above the storage wall. Fix them into the ceiling joists exactly as the manufacturer says and stay under the stated weight limit. Too much to keep? Our {a('storage-unit-size-calculator','storage unit size calculator')} shows what size unit you would need.")
h3("15. Safe Storage for Fuel and Chemicals")
p(f"Keep gasoline, paint and chemicals out of the lounge zone. Massachusetts fire officials advise: {SR('gas','if you need to carry or store gasoline, use an approved container')}, store it away from living areas and keep it away from pilot lights. Some towns limit how much fuel you can keep; Lehi, Utah, for example, allows {SR('lehi','no more than 10 gallons')} in an attached garage, so check your local rule.")
h2("Garage Man Cave Style Ideas")
h3("16. A Wood Slat Accent Wall")
p("A wall of vertical wood slats behind the TV adds warmth and hides the cables in the gaps. It is a weekend project and looks great with gray concrete and leather.")
h3("17. Pick One Theme")
p(f"Sports, vintage garage, music or a favorite team: one theme ties the room together. Frame a few prints or memorabilia instead of covering every wall, and use our {a('picture-hanging-height-calculator','picture hanging height calculator')} to hang them at the right height.")
h3("18. Keep It Flexible")
p(f"If you still need to park or work in the garage, put the sofa and rug on one side, use furniture you can move, and keep the bar and storage along the walls. A big declutter first makes it all fit; our guide on {a('how-to-declutter-your-home','how to declutter your home')} walks you through it.")
add(open('savebox.html').read())
h2("Garage Man Cave Safety Tips")
lst([f"<strong>Carbon monoxide:</strong> the CDC says to {SR('cdc2','install a battery-operated CO detector in your home')}; put one near the door to the house and never run a car, generator or other engine in the garage.",
"<strong>Smoke alarm:</strong> install one rated for the space (use a heat alarm instead if you still park in the garage) and test it monthly.",
f"<strong>Heaters:</strong> {SR('heat','keep the heater at least 3 feet away from anything that can burn')}, never use an extension cord and turn it off when you leave or go to bed.",
"<strong>Electrical:</strong> use GFCI-protected outlets and a licensed electrician for new circuits; don't overload a single outlet.",
"<strong>Fire-rated door:</strong> keep the door to the house closed and never prop it open."])
h2("Common Garage Man Cave Mistakes")
lst(["<strong>Skipping insulation.</strong> The room ends up too cold to use in winter and too hot in summer.",
"<strong>Mounting the TV on the garage door.</strong> Use a solid side wall.",
"<strong>Leaving tools everywhere.</strong> One closed storage wall keeps the lounge feeling like a room.",
"<strong>Removing the fire barrier.</strong> Keep the gypsum board and the fire-rated door to the house.",
"<strong>Ignoring permits.</strong> A full conversion without a permit can cause problems when you sell."])
h2("Garage Man Cave FAQ")
h3("How do you turn a garage into a man cave?")
p("Clear the garage, check permit rules, insulate the walls and door, and plan safe heating. Then add GFCI-protected outlets, finish the floor with sealed concrete, tiles and a rug, and set up zones: a lounge, a bar, a game table and one storage wall.")
h3("How much does a garage man cave cost?")
p("A simple setup with a used sofa, rug, TV and lighting can start at about $500. Insulation, a mini-split, flooring and electrical work push a full conversion into the thousands, and costs vary a lot by area and by how much you do yourself.")
h3("Do I need a permit for a garage man cave?")
p("Adding furniture usually does not need a permit, but converting a garage into living space often does, along with electrical or mechanical permits. Rules vary by city, so check with your local building department before you start.")
h3("How do you heat a garage man cave?")
p("A ductless mini-split heat pump is the most efficient year-round choice. A portable electric heater works for short sessions if you keep it 3 feet from anything that can burn, plug it into a wall outlet and turn it off when you leave.")
h3("Can a one-car garage be a man cave?")
p("Yes. Put a sofa and TV on one side, a slim bar or coffee counter on the back wall and tools on a single storage wall. Skip the game table, use a big rug to define the lounge and choose furniture you can move.")
h2("Final Thoughts")
p("The best garage man cave ideas start with the basics: a warm, insulated room, safe power and heat, and clear zones for relaxing, drinks, games and tools. Get those right, add a big rug, warm light and one theme, and your garage becomes the favorite room in the house.")
p(f"Need more space ideas? Our {a('storage-ideas-for-small-spaces','storage ideas for small spaces')} help you clear the clutter first, and our {a('diy-floating-shelves','DIY floating shelves')} guide is perfect for a bar or display wall.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<svg.*?</svg>','',html))
print(len(html.encode()),'words',len(txt.split()),'kw',txt.lower().count('garage man cave ideas'),txt.lower().count('man cave'))
print(sorted(set(re.findall(r'dailyspacehacks\.com/([a-z0-9-]+)/',html))))
for w in ['colour','organise','favourite','cushion','metre']:
    if w in txt.lower(): print('UK',w)
