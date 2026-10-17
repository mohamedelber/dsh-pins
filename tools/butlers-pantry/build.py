import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
NK="https://kb.nkba.org/uploads/2022/05/Kitchen-Planning-Guidelines.pdf"
DM="https://www.dimensions.com/element/pantry-butler-open-u-shape-3-side"
MDH="https://www.health.mn.gov/people/foodsafety/store/store.html"
p("The best butler's pantry ideas give you a second, quieter work zone right next to the kitchen: somewhere to store serving dishes, prep food, make coffee and hide the mess when guests arrive. A butler's pantry can be a full walk-in room, a short passage between the kitchen and dining room or simply a converted closet.")
p("This guide explains what a butler's pantry is, the layouts and sizes that work, a 6-step plan and 16 ideas for layouts, small spaces, design details and storage, with sizes in inches and centimeters for homes in the US, Australia and beyond.")
img(1)
summary(["<strong>Quick answer:</strong> A butler's pantry is a small room or nook beside the kitchen with base cabinets, a countertop and storage above. A single-wall layout needs about 5 ft (1.5 m) of width, a galley with cabinets on both sides about 7.5 ft (2.3 m), so you keep at least a 36 in (91 cm) walkway or a 42 in (107 cm) work aisle.",
"Small homes can borrow the idea with a converted closet, a coffee station or a wall of tall cabinets.",
"Plan outlets, lighting and any sink before you order cabinets, and use a licensed electrician and plumber for new wiring and plumbing."],
"<strong>Time:</strong> a weekend (closet conversion) to several weeks (new room) · <strong>Cost:</strong> $ to $$$ · <strong>Difficulty:</strong> Medium to hard")
toc("butlers-pantry-ideas")

h2("What Is a Butler's Pantry?")
p("A butler's pantry is a service area between the kitchen and the dining room, or tucked behind the kitchen, with counter space and storage. Historically it held the household's china, glassware and silver. Today it is used for food storage, small appliances, a coffee or drinks station and extra prep space, and it keeps the main kitchen clear. In Australia, butler's pantries are a popular feature of new homes, and a larger one with a sink and dishwasher is sometimes called a scullery.")
table(["","Butler's pantry","Walk-in pantry","Scullery"],
[["Main job","Prep, serving and storage","Food storage","Messy prep and cleanup"],
 ["Counter space","Yes","Sometimes","Yes"],
 ["Sink","Optional","Rarely","Usually"],
 ["Typical spot","Between kitchen and dining room, or behind the kitchen","Off the kitchen","Behind the kitchen"]])
p(f"If you mainly need more shelves for food, a walk-in pantry may be enough, and our {a('pantry-organization-ideas','pantry organization ideas')} will help you set one up. Choose a butler's pantry when you also want counter space, appliances or a place to stage meals.")

h2("Butler's Pantry Layouts and Sizes")
p("The aisle decides how wide a butler's pantry has to be, so plan it first. The diagram shows the three most common layouts and the sizes they usually need.")
diagram(open('z.svg').read(),"Butler's pantry layouts and sizes: a single wall about 5 ft wide, a galley about 7.5 ft wide and an L-shape, each with 24 in deep base cabinets and a 36 to 42 in aisle.")
p(f"The {ext(NK,'NKBA Kitchen Planning Guidelines')} recommend a walkway of at least 36 in (91 cm) and a work aisle of at least 42 in (107 cm) for one cook or 48 in (122 cm) for two. A pass-through pantry you only walk through can use the narrower figure; a galley where you prep and open drawers and a dishwasher needs the wider one. Standard base cabinets are about 24 in (61 cm) deep, and {ext(DM,'Dimensions.com')} lists a typical butler's pantry counter depth of 25 to 26 in (64 to 66 cm) at a height of 36 in (91 cm).")

h2("Quick Pick: Butler's Pantry Ideas by Space")
table(["Your space","Best ideas","Budget"],[
["Passage between kitchen and dining room","#1, #11, #13","$$"],
["Spare room or large alcove","#2, #4, #9","$$$"],
["Small, square room","#3, #9, #14","$$$"],
["Kitchen closet","#5, #8, #15","$"],
["No room to spare","#6, #7, #16","$$"],
["Tight budget","#5, #7, #15","$"]])

h2("How to Plan a Butler's Pantry in 6 Steps")
lst(["<strong>Decide its job.</strong> Storage, prep, a coffee bar, a serving station or a place to hide dishes? The answer decides whether you need a sink, outlets or just shelves.",
"<strong>Pick the spot.</strong> Next to the kitchen works best, ideally between the kitchen and dining room, or behind the kitchen.",
"<strong>Measure the aisle first.</strong> Keep at least 36 in (91 cm) to walk through and 42 in (107 cm) where you will work.",
"<strong>Plan power, water and light.</strong> Mark outlets for every appliance, any sink and the lighting before you design the cabinets.",
"<strong>Choose cabinets and storage.</strong> Drawers below, shelves or glass cabinets above, and a tall unit for brooms or bulk food.",
"<strong>Book licensed trades.</strong> New circuits, outlets and plumbing are jobs for a licensed electrician and plumber, and may need a permit."],True)

h2("Butler's Pantry Layout Ideas")
p("Start with the shape of the space. These four layouts cover most homes, from a short passage to a full walk-in room.")
h3("1. A Single-Wall Pass-Through")
p("The classic butler's pantry is one run of cabinets in the short passage between the kitchen and the dining room. It needs only about 5 ft (1.5 m) of width, gives you a landing spot for serving dishes and keeps platters, glasses and table linens exactly where you set the table. Open shelves above keep it light, like the pantry below.")
img(2)
h3("2. A Galley Butler's Pantry")
p("Cabinets on both walls, like the pantry at the top of this guide, double the storage and counter space. Allow about 7.5 ft (2.3 m) of width so you can stand at one counter and still open the drawers on the other side. Use one side for food and appliances and the other for dishes and glassware.")
h3("3. An L-Shaped Pantry With a Corner Sink")
p("In a small, square room, an L-shape wraps cabinets around two walls and leaves the rest open. The corner is a natural home for a prep sink or a coffee machine, with clear counter on both sides for setting things down.")
img(3)
h3("4. A Walk-In Butler's Pantry")
p(f"If you have a spare room, combine both pantry types: floor-to-ceiling shelves for food on the side walls and a counter with base cabinets for appliances on the back wall. This walk-in butler's pantry holds bulk food and the stand mixer in one place. Our {a('pantry-shelving-ideas','pantry shelving ideas')} and the {a('shelf-spacing-calculator','shelf spacing calculator')} help you set the shelf heights.")
img(4)

h2("Small Butler's Pantry Ideas")
p("No spare room? These small butler's pantry ideas give you the same zones in a closet, an alcove or a single wall.")
h3("5. Convert a Kitchen Closet")
p("A closet near the kitchen can become a mini butler's pantry. Remove the shelves at counter height, fit a countertop about 24 in (61 cm) deep, add shelves above and drawers or baskets below. Bifold or pocket doors open the full width and close over everything when guests arrive.")
img(5)
h3("6. Hide It Behind Tall Cabinet Doors")
p(f"A wall of tall cabinets in the kitchen can hide a shallow counter, shelves and outlets behind doors that fold or slide back into pockets. Open them while you cook and close them when you are done. Plan it like any other cabinet run with our guide to {a('how-to-organize-kitchen-cabinets','organizing kitchen cabinets')}.")
h3("7. Use Open Shelves Instead of Upper Cabinets")
p("Open shelves cost less than upper cabinets and make a narrow pantry feel wider. Keep the everyday dishes and glasses at eye level and the rarely used platters on top. Shelves about 12 in (30 cm) deep hold most plates without things getting lost at the back.")
h3("8. Make It a Coffee and Breakfast Station")
p("If you have only a few feet of wall, give it one job. A coffee and breakfast station with the machine, mugs, cereal and a small fridge below keeps the morning rush out of the main kitchen. Put an outlet right above the counter so no cords cross the work surface.")
img(8)

h2("Butler's Pantry Design Ideas")
p("These butler's pantry design ideas make the space work harder once the layout is fixed.")
h3("9. Add a Prep Sink")
p(f"A small prep sink lets you wash fruit, fill a kettle or rinse glasses without crossing the kitchen. The {ext(NK,'NKBA guidelines')} recommend a landing area of at least 24 in (61 cm) on one side of a sink and at least 18 in (46 cm) on the other, so leave counter space on both sides. A new sink needs a water supply and drain, so plan it with a licensed plumber.")
h3("10. Add a Dishwasher Drawer")
p("A single dishwasher drawer next to the pantry sink handles glasses and serving dishes after a party, so the main dishwasher is free for everyday loads. The NKBA guidelines suggest placing the nearest edge of a primary dishwasher within 36 in (91 cm) of the sink, and the same idea makes a second one easier to load.")
h3("11. Choose Glass-Front Upper Cabinets")
p("Glass doors show off glassware and serving pieces, keep the dust off and make a small pantry look deeper. They work best for things you keep tidy, so put the mismatched mugs behind solid doors.")
img(6)
h3("12. Pick the Right Door")
p("A pocket door or sliding barn door saves the swing space a hinged door needs, which matters in a narrow passage. A pass-through pantry between the kitchen and dining room often needs no door at all.")
h3("13. Light the Counter")
p("Butler's pantries are often windowless. Add ceiling lights for the aisle and LED strips under the shelves or upper cabinets so the counter is not in your own shadow. Lights inside glass cabinets add a soft glow in the evening.")

h2("Butler's Pantry Storage Ideas")
h3("14. Swap Base Doors for Deep Drawers")
p(f"Full-extension drawers bring everything to you, so nothing gets lost at the back of a deep cabinet. Use them for food in clear containers, pots and heavy small appliances. Our guide to {a('how-to-organize-kitchen-drawers','organizing kitchen drawers')} shows how to divide them.")
img(7)
h3("15. Organize in Zones")
p(f"Give each section one job: baking, breakfast, snacks, drinks, serving and entertaining. Clear containers show when you are running low, and the oldest food goes to the front. If your pantry has deep shelves, see our tips on {a('how-to-organize-a-pantry-with-deep-shelves','organizing a pantry with deep shelves')}. Keep cleaning products away from food: the {ext(MDH,'Minnesota Department of Health')} advises not storing foods near household cleaning products and chemicals.")
h3("16. Give Appliances a Home With Power")
p(f"The mixer, air fryer, toaster and blender take over a kitchen counter. Store them in the butler's pantry on the counter or in a lower cabinet beside an outlet, so they are ready to use without being carried around. The NKBA guidelines note that the electrical code requires GFCI (ground-fault circuit-interrupter) protection on all receptacles serving countertop surfaces, and they should not be installed face-up in the countertop. Our {a('kitchen-storage-ideas','kitchen storage ideas')} have more ways to clear the counter.")

CHK='https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fdailyspacehacks.com%2Fbutlers-pantry-ideas%2F&amp;media=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fmohamedelber%2Fdsh-pins%40main%2Fsrc%2Fbutlers-pantry%2Fpins%2Fpin-butlers-pantry-5-checklist.jpg&amp;description=Butler%27s%20pantry%20planning%20checklist%3A%20aisle%2C%20cabinets%2C%20outlets%20and%20sink'
add('<!-- wp:html -->\n<div class="dsh-save" style="display:flex;flex-wrap:wrap;align-items:center;gap:24px;background:#F7F1E9;border:1px solid #E6DCCF;border-radius:16px;padding:24px;margin:2em 0;"><a href="'+CHK+'" target="_blank" rel="noopener" style="flex:0 0 200px;max-width:200px;margin:0 auto;"><img src="https://dailyspacehacks.com/wp-content/uploads/2026/10/pin-butlers-pantry-5-checklist.jpg" alt="Butler\'s pantry planning checklist: aisle width, cabinet depths, outlets and sink" width="200" data-pin-media="https://cdn.jsdelivr.net/gh/mohamedelber/dsh-pins@main/src/butlers-pantry/pins/pin-butlers-pantry-5-checklist.jpg" style="width:200px;height:auto;border-radius:10px;display:block;"></a><div style="flex:1 1 260px;"><p style="font-weight:700;font-size:1.25em;margin:0 0 .4em;">Save the checklist</p><p style="margin:0 0 1em;">Pin these measurements so they are on your phone when you talk to your cabinetmaker or plan the pantry.</p><a href="'+CHK+'" target="_blank" rel="noopener" style="display:inline-block;background:#E60023;color:#fff;font-weight:700;text-decoration:none;padding:12px 22px;border-radius:999px;white-space:nowrap;line-height:1.2;">Save to Pinterest</a></div></div>\n<!-- /wp:html -->')

h2("Common Butler's Pantry Mistakes")
lst(["<strong>Making the aisle too narrow.</strong> Below 36 in (91 cm), two people cannot pass and drawers block the way. Plan the aisle before the cabinets.",
"<strong>Too few outlets.</strong> A pantry full of appliances needs outlets along the counter, not one at the end of the run.",
"<strong>Upper storage nobody can reach.</strong> Keep everyday items between hip and eye height and use the top shelves for things you need once a year.",
"<strong>Mixing food and cleaning products.</strong> Store detergents and sprays in their own cabinet, away from food.",
"<strong>Forgetting the light.</strong> A dark pantry is hard to use. Plan ceiling and under-shelf lighting from the start."])

h2("Butler's Pantry FAQ")
h3("What is the difference between a butler's pantry and a walk-in pantry?")
p("A walk-in pantry is mainly for storing food. A butler's pantry adds counter space and often appliances or a sink, so you can prep, make drinks and stage meals there, not just store things.")
h3("How big should a butler's pantry be?")
p("A single-wall butler's pantry needs about 5 ft (1.5 m) of width: 24 in (61 cm) for the cabinets and a walkway of at least 36 in (91 cm). A galley with cabinets on both sides needs about 7.5 ft (2.3 m). The length can be as short as one cabinet run.")
h3("Does a butler's pantry need a sink?")
p("No. Many butler's pantries are storage and serving areas without water. A sink is useful if you prep or wash glasses there, but it adds the cost of a water supply and drain.")
h3("Is a butler's pantry the same as a scullery?")
p("Not quite. In Australia, the names are often used for the same room, but a scullery usually means a working back kitchen with a sink and dishwasher for the messy jobs, while a butler's pantry is often more about storage, serving and small appliances.")

h2("Final Thoughts")
p(f"The best butler's pantry ideas start with the job you want the space to do and an aisle wide enough to do it. Whether you build a walk-in room, a pass-through or a converted closet, plan the power, light and storage first and the pantry will keep your main kitchen clear for years. For more ideas, see our {a('kitchen-counter-organization','kitchen counter organization')} tips, our {a('spice-cabinet-organization','spice cabinet organization')} guide and, for Australian homes, our {a('european-laundry-ideas','European laundry ideas')}.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub('<[^>]+>',' ',re.sub(r'<svg.*?</svg>','',html,flags=re.S))
print(len(txt.split()),'words; kw',len(re.findall("butler's pantry ideas",txt,re.I)),'bp',len(re.findall("butler's pantr",txt,re.I)),'; ideas',len(re.findall(r'<h3 class="wp-block-heading">\d+\.',html)))
print(sorted(set(re.findall(r'dailyspacehacks\.com/([a-z0-9-]+)/',html))))
