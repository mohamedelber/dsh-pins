import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
ER="https://energyrating.gov.au/node/37"
FR="https://www.fire.nsw.gov.au/fire-safety/home-fire-safety/topics/home-fire-safety-checklist"
NCC="https://www.nccb.gov.au/ncc-navigator/waterproofing-houses"
p("The best European laundry ideas fit a full laundry, with a washing machine, a dryer and somewhere to fold, into a single cupboard that closes when you are done. They are popular in Australian apartments, townhouses and renovations because they free up the floor space a separate laundry room would take, and the doors hide the whole thing when guests come over.")
p("This guide explains what a European laundry is, the sizes you need for side-by-side and stacked layouts, a 6-step plan and 16 ideas for layouts, doors, storage, tubs and the practical details, such as dryer ventilation and waterproofing, that make a cupboard laundry work day to day.")
img(1)
summary(["<strong>Quick answer:</strong> A European laundry is a laundry hidden in a cupboard. Put the washer and dryer side by side under a benchtop (a cupboard about 1,200 to 1,300 mm wide) or stack them (about 700 mm wide), allow about 650 to 700 mm of depth, and choose a heat pump or condenser dryer, or duct a vented dryer outside.",
"Overhead cupboards, pull-out hampers and a slim shelf column add storage without widening the cupboard.",
"Use a licensed plumber and electrician for new taps, drains and power points."],
"<strong>Time:</strong> a weekend (flat pack) to a few weeks (custom joinery) · <strong>Cost:</strong> $ to $$$ · <strong>Difficulty:</strong> Medium")
toc("european-laundry-ideas")
h2("What Is a European Laundry?")
p(f"A European laundry, or European style laundry, is a compact laundry set inside a cupboard, usually behind bifold, sliding or hinged doors. It holds the same things as a laundry room, a washing machine, often a dryer, sometimes a small tub, with shelves above, but takes up only one stretch of wall in a hallway, kitchen or bathroom. In the US the same idea is often called a laundry closet; our {a('laundry-closet-ideas','laundry closet ideas')} show how it works there.")
h2("European Laundry Sizes")
p("Measure before you buy any joinery. The diagram shows the two most common layouts and the sizes they usually need.")
diagram(open('z.svg').read(),"European laundry sizes: side by side under a benchtop, or stacked on a stacking kit, with typical widths, heights and depth.")
p(f"Most front loaders and dryers are about 600 mm wide, but depths and heights vary between models, so copy the numbers from your appliances' installation guides, and leave room behind for the hoses and the power point. Our {a('washer-dryer-space-calculator','washer and dryer space calculator')} checks whether your machines will fit. The dryer type matters too: the Australian Government's {ext(ER,'Energy Rating')} site explains that vented dryers pump hot, humid air into the surrounding space and that the National Construction Code requires venting dryers to discharge to outside air, while condenser and heat pump dryers collect or drain the water instead.")
h2("Quick Pick: European Laundry Ideas by Space")
table(["Your space","Best ideas","Budget"],[
["Hallway cupboard about 1.2–1.7 m wide","#1, #6, #9","$$"],
["Narrow cupboard about 700 mm wide","#2, #12, #8","$$"],
["No room for two machines","#3, #11","$"],
["Open-plan kitchen","#4, #8, #10","$$$"],
["Living area or apartment","#7, #8, #15","$$"],
["Renting or tight budget","#3, #12, #14","$"]])
h2("How to Plan a European Laundry in 6 Steps")
lst(["<strong>Choose the spot.</strong> A hallway, kitchen or bathroom wall near existing water, drainage and power is cheapest to set up.",
"<strong>Choose your appliances first.</strong> Decide on side-by-side, stacked or a combo machine before you design the cupboard around them.",
"<strong>Check the dryer type.</strong> A vented dryer must be ducted outside; a heat pump or condenser dryer avoids that.",
"<strong>Measure width, height and depth.</strong> Allow for hoses, the power point and doors that open fully.",
"<strong>Plan the storage.</strong> Overhead cupboards, a hanging rail and hamper drawers keep the benchtop clear.",
"<strong>Book licensed trades.</strong> New taps, drains and power points are jobs for a licensed plumber and electrician."],True)
h2("Layout Ideas")
p("The layout decides how wide the cupboard has to be, so these European laundry ideas start there. Add doors and storage once the layout is fixed.")
h3("1. Washer and Dryer Side by Side Under a Benchtop")
p("Placing the two machines side by side under one benchtop, like the hallway laundry at the top of this guide, gives you a folding surface and room for overhead cupboards. It needs the widest cupboard, about 1,200 to 1,300 mm for two standard machines, but it is the easiest layout to use every day. Check the benchtop height clears the top of your tallest machine.")
h3("2. Stack the Dryer on the Washer")
img(2)
p("Stacking the dryer on top of the washer with a stacking kit cuts the width to about 700 mm, so a laundry can fit into a narrow linen cupboard. Use the kit made for your machines so the dryer sits securely, and keep the dryer controls within easy reach. A narrow column of shelves beside the stack holds towels and detergent.")
h3("3. One Washer-Dryer Combo")
p("If there is room for only one machine, a washer-dryer combo washes and dries in the same drum, so a single 600 mm space is enough. It suits small apartments and rentals. Combos dry smaller loads than a separate dryer, so they work best for small households.")
h3("4. A European Laundry in the Kitchen")
img(3)
p("Hiding the laundry behind a tall kitchen door uses the same water and drainage as the kitchen sink. Matching the laundry doors to the kitchen cabinetry makes it disappear, and a stacked pair takes the space of one tall pantry unit.")
h3("5. A Hallway or Bathroom Cupboard")
p(f"A hallway cupboard keeps the noise away from living areas, and a bathroom cupboard puts the machines right next to the dirty washing. If you are working with a top-loading washer, remember the lid needs clearance to open, so it cannot sit under a fixed benchtop; our {a('small-laundry-room-ideas-top-loading-washer','top loading washer guide')} explains how much space to leave.")
h2("Door Ideas")
p("Doors make a European laundry. They need to open wide enough to load the machines and close neatly over them.")
h3("6. Bifold Doors")
p("Bifold doors fold back to the sides and open the full width of the cupboard while taking up less floor in front than one wide hinged door. They suit hallways, where a single wide door would block the walkway.")
h3("7. Sliding Doors on a Top Track")
img(8)
p("Sliding doors need no space to swing at all, which makes them ideal for a laundry in a living area or a narrow hallway. The trade-off is that only half the cupboard is open at a time, so place the machines and the tub behind different doors.")
h3("8. Handleless Doors That Match the Walls")
img(7)
p("Floor-to-ceiling handleless doors painted the same colour as the walls, or a soft contrast like sage, hide the laundry completely. A slim vent grille at the top of the doors lets warm, damp air escape, which helps with any dryer.")
h2("Storage Ideas")
p("A cupboard laundry has little room, so the best storage-focused European laundry ideas go up the wall and into drawers.")
h3("9. Overhead Cupboards and a Hanging Rail")
img(6)
p("Overhead cupboards above the benchtop hold detergent refills, cleaning products and spare towels, and a hanging rail underneath lets shirts dry or wait on hangers. Keep laundry pods and chemicals on the highest shelf, out of reach of children.")
h3("10. Pull-Out Hamper Drawers")
img(5)
p(f"Wide pull-out drawers with fabric hampers sort darks and lights out of sight. They work beside a single machine or under the tub. Our {a('laundry-room-cabinet-ideas','laundry cabinet ideas')} show more ways to plan the joinery.")
h3("11. A Slim Pull-Out for Detergent or an Ironing Board")
p("A narrow pull-out, 150 to 200 mm wide, beside the machines holds detergent bottles, or a fold-out ironing board that slides away. It uses the gap that is often left over when the cupboard is wider than the appliances.")
h3("12. Open Shelves Beside a Stack")
p(f"With stacked machines, a column of open shelves beside them holds folded towels, baskets and the peg bag. Use baskets on the lower shelves so the cupboard looks tidy when the doors are open. Our {a('how-to-organize-a-laundry-room','laundry organisation guide')} explains where each item should go.")
h2("Tub, Benchtop and Practical Details")
h3("13. A Compact Laundry Tub")
img(4)
p("A compact stainless steel tub set into the benchtop is handy for soaking, hand washing and rinsing muddy shoes. It adds about 400 to 500 mm to the width of a side-by-side layout. A wall-mounted mixer tap or one on the benchtop keeps the bench easy to wipe.")
h3("14. A Benchtop for Folding")
p("Even a short benchtop over a single machine gives you somewhere to fold. Choose a moisture-resistant surface such as laminate, compact laminate or stone, and seal timber well if you love the look of oak.")
h3("15. Ventilation and the Right Dryer")
p(f"A closed cupboard traps heat and moisture. Choose a heat pump or condenser dryer, or have a vented dryer ducted to the outside, as Energy Rating explains the National Construction Code requires. Add a vent grille or leave the doors open while machines run. Fire and Rescue NSW's {ext(FR,'home fire safety checklist')} also advises cleaning the dryer's lint filter every time you use it.")
h3("16. Waterproofing, Power and a Leak Tray")
p(f"Laundries are wet areas under the National Construction Code, which covers waterproofing in {ext(NCC,'wet areas such as bathrooms and laundries')}, so plan the floor and walls with your builder or a licensed waterproofer. A washing machine leak tray under the machine adds protection in a timber-floored hallway, and new taps, drains and power points must be installed by licensed trades.")
h2("Before and After: A Hallway Laundry")
img(9)
p("Before, this hallway alcove holds a lone washing machine, an airer and piles of washing on the floor. After, bifold doors, a benchtop over a washer and dryer, overhead cupboards and a basket turn it into a European laundry that closes away. It uses four of the European laundry ideas above: the side-by-side layout, bifold doors, overhead cupboards and a folding benchtop.")
SAVE='https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fdailyspacehacks.com%2Feuropean-laundry-ideas%2F&media=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fmohamedelber%2Fdsh-pins%40main%2Fsrc%2Feuro-laundry%2Fpins%2Fpin-euro-laundry-5-checklist.jpg&description=European%20laundry%20size%20checklist%3A%204%20measurements%20before%20you%20build'
add('<!-- wp:html -->\n<div class="dsh-save" style="display:flex;flex-wrap:wrap;align-items:center;gap:24px;background:#F7F1E9;border:1px solid #E6DCCF;border-radius:16px;padding:24px;margin:2em 0;"><a href="'+SAVE+'" target="_blank" rel="noopener" style="flex:0 0 200px;max-width:200px;margin:0 auto;"><img src="https://dailyspacehacks.com/wp-content/uploads/2026/10/pin-euro-laundry-5-checklist.jpg" alt="European laundry size checklist: side by side, stacked, depth and dryer type" width="200" data-pin-media="https://cdn.jsdelivr.net/gh/mohamedelber/dsh-pins@main/src/euro-laundry/pins/pin-euro-laundry-5-checklist.jpg" style="width:200px;height:auto;border-radius:10px;display:block;"></a><div style="flex:1 1 260px;"><p style="font-weight:700;font-size:1.25em;margin:0 0 .4em;">Save the checklist</p><p style="margin:0 0 1em;">Pin these four measurements so they are on your phone when you talk to your cabinetmaker or shop for appliances.</p><a href="'+SAVE+'" target="_blank" rel="noopener" style="display:inline-block;background:#E60023;color:#fff;font-weight:700;text-decoration:none;padding:12px 22px;border-radius:999px;white-space:nowrap;line-height:1.2;">Save to Pinterest</a></div></div>\n<!-- /wp:html -->')
h2("Common European Laundry Mistakes")
lst(["<strong>Designing the cupboard before choosing the machines.</strong> Appliance sizes vary, so buy or measure them first.",
"<strong>Forgetting the depth.</strong> Hoses, taps and the power point need room behind the machines.",
"<strong>A vented dryer in a closed cupboard.</strong> Duct it outside or choose a heat pump or condenser dryer.",
"<strong>Doors that cannot open fully.</strong> Check doors clear the machine doors and the hallway.",
"<strong>No storage.</strong> Without overhead cupboards, detergent ends up on the floor.",
"<strong>DIY plumbing or electrics.</strong> Use licensed trades for new water, drainage and power."])
h2("European Laundry FAQ")
h3("What is a European laundry?")
p("A European laundry is a compact laundry hidden in a cupboard, usually with a washing machine, a dryer, shelves and sometimes a small tub, behind bifold, sliding or hinged doors. It takes up one wall instead of a whole room.")
h3("How deep does a European laundry need to be?")
p("Allow about 650 to 700 mm of depth for most front loaders, so there is room for the hoses, taps and power point behind the machine and for the doors to close in front. Check your appliances' installation guides, because depths vary between models.")
h3("How big is a European laundry?")
p("A side-by-side washer and dryer usually needs about 1,200 to 1,300 mm of width, or about 1,700 mm with a compact tub. Stacked machines need about 700 mm of width but about 1,800 mm of height. A single washer-dryer combo fits in about 600 mm.")
h3("Can you put a dryer in a European laundry?")
p("Yes. Heat pump and condenser dryers suit a cupboard because they collect or drain the water instead of blowing damp air out. A vented dryer needs to be ducted to the outside, and any dryer needs its lint filter cleaned after every load.")
h2("Final Thoughts")
p(f"The best European laundry ideas start with the appliances and the space, then add doors that suit the room and storage that goes up instead of out. Plan the depth, the dryer type and the trades before you order joinery, and the cupboard will work as well as a full laundry room. For more ideas, see our {a('small-laundry-room-ideas','small laundry room ideas')} and, for British homes, {a('small-utility-room-ideas','small utility room ideas')}.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub('<[^>]+>',' ',re.sub(r'<svg.*?</svg>','',html,flags=re.S))
print(len(txt.split()),'words; kw',len(re.findall('european laundry ideas',txt,re.I)),'eu laundry',len(re.findall('european laundry',txt,re.I)),'; ideas',len(re.findall(r'<h3 class="wp-block-heading">\d+\.',html)))
print(sorted(set(re.findall(r'dailyspacehacks\.com/([a-z0-9-]+)/',html))))
