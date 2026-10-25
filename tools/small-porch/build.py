import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={"pp":"https://www.planningportal.co.uk/permission/common-projects/porches",
"leg":"https://legislation.gov.uk/uksi/2015/596/schedule/2/part/1/crossheading/class-d-porches",
"cam":"https://camden.gov.uk/porches-planning-permission",
"ppfee":"https://www.planningportal.co.uk/planning/planning-applications/consent-types/householder-planning-consent",
"walfee":"https://www.gov.wales/sites/default/files/publications/2025-10/planning-application-fees-fee-document.pdf",
"est2":"https://energysavingtrust.org.uk/cutting-out-draughts-older-homes",
"wal":"https://www.gov.wales/planning-permission-porches",
"ppbr":"https://www.planningportal.co.uk/permission/common-projects/porches/building-regulations/",
"circ":"https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/248652/130507_-_Circular_Letter_conservatories_and_porches_final.pdf",
"lan":"https://lancaster.gov.uk/assets/attach/1343/Leaflet-4-Safety-Glass-Where-is-it-needed.pdf",
"mjq":"https://www.myjobquote.co.uk/costs/build-a-porch",
"mb":"https://www.mybuilder.com/extensions/price-guides/porch-extension-cost",
"oak":"https://www.myjobquote.co.uk/costs/oak-porch-canopy",
"hbc":"https://www.homebuilding.co.uk/advice/porch-costs",
"size":"https://www.idealhome.co.uk/renovation/exterior/what-is-the-ideal-porch-size",
"mats":"https://mats4u.co.uk/blogs/guides/essential-guide-how-to-choose-the-right-size-door-mat",
"fm":"https://www.firstmats.co.uk/blogs/buying-guides/entrance-mat-sizing-guide",
"way":"https://www.wayfair.co.uk/sca/ideas-and-advice/guides/what-is-the-standard-bench-height-and-other-useful-dimensions-to-know-T9802",
"wf":"https://www.wallsandfloors.co.uk/blog/r-ratings-explained-r9-r10-r11-r12-r13-non-slip-tile-ratings/",
"ps":"https://www.porcelainsuperstore.co.uk/blogs/help-advice/can-i-use-porcelain-tiles-outside",
"ihf":"https://www.idealhome.co.uk/renovation/exterior/front-porch-ideas",
"bc":"https://buildingconservation.com/articles/tiles/tiles.htm",
"nic":"https://niceic.com/householders/gardens-and-electrics-what-you-need-to-know",
"iet":"https://electrical.theiet.org/bs-7671/building-regulations/part-p-england-and-wales/frequently-asked-questions/",
"hbi":"https://www.homebuilding.co.uk/ideas/small-porch-ideas",
"ihs":"https://idealhome.co.uk/renovation/exterior/small-front-porch-ideas",
"lg":"https://littlegreene.com/blog/selecting-a-front-door-shade-with-ruth",
"hg":"https://www.homesandgardens.com/ideas/small-front-porch-ideas",
"cold":"https://www.homebuilding.co.uk/rooms/hallway/is-my-porch-making-my-home-colder",
"est":"https://energysavingtrust.org.uk/how-to-draught-proof-your-windows-and-doors/?loc=international",
"sec":"https://www.redditchbc.gov.uk/media/oqoblytk/home-security-guide.pdf"}
def SR(k,t): return ext(SRC[k],t)

p(f"The best small porch ideas keep the floor clear: a slim bench with shoes underneath, hooks on the wall, a big doormat and good light. If you are building one, a porch of up to 3 m² usually needs no planning permission in England, and an open canopy is the cheapest way to get shelter by the front door. Below are 11 ideas in three groups, from building a new porch to making a tiny one work inside and dressing the front door, with the UK sizes, rules and costs behind each one.")
img(1)

h2("A Small Porch, Measured")
diagram(open('z.svg').read(),"An example 2.0 x 1.5 m porch: 3 m² outside, about 2.5 m² inside, with the planning, Building Regulations and safety glass checks.")
p(f"Under permitted development in England, a porch is allowed without a planning application if the ground floor area {SR('pp','(measured externally) would not exceed three square metres')}, no part is more than 3 m high and no part is within 2 m of a boundary that fronts a highway. These rules come from {SR('leg','Class D')} of the General Permitted Development Order 2015. They do not apply to flats or maisonettes, or to homes created under certain change-of-use or new-build permitted development rights, and Wales has the {SR('wal','same three-square-metre limit')}. Because the 3 m² is measured outside, the walls eat into it: in our example, a 2.0 x 1.5 m porch with walls about 10 cm thick leaves roughly 1.8 x 1.4 m, or 2.5 m², inside (thicker cavity walls would leave closer to 1.8 m²). That is enough for a bench on one side, hooks on the other and a doormat in between.")

h2("Building a Small Porch")
h3("1. An Open Canopy Porch")
img(4)
p(f"If you only want shelter while you find your keys, a canopy over the front door costs far less than an enclosed porch. A simple polycarbonate door canopy {SR('hbc','can be bought online from £95')} to fit yourself, a small oak canopy costs {SR('oak','£800 to £2,000')} and takes one to two days to fit, and MyBuilder puts open canopy porches at {SR('mb','£2,000 to £4,000')} including installation. Homebuilding's Rebecca Foster notes that {SR('hbi','the porch needs to work in proportion with the house')}, so a slim canopy on brackets suits a narrow Victorian terrace better than a deep one.")
p(f"<strong>Works best:</strong> when you want shelter at the door without losing light in the hall. Planning Portal applies the porch limits to canopies too (3 m², 3 m high, 2 m from a boundary with a highway), so if your door opens almost straight onto the pavement, check with your council before fitting even a canopy. <strong>Skip it:</strong> if you want somewhere to leave wet coats and muddy boots; an open porch won't keep them dry or keep the cold out, and Alexandra Hull of Back to Front Exterior Design told Homebuilding that an open porch {SR('cold','won\'t provide the same thermal buffer')} as an enclosed one.")
h3("2. A Brick and Glass Porch")
img(2)
p(f"An enclosed porch gives you a buffer between the street and the hall, and space for coats and shoes. MyJobQuote and MyBuilder both put a typical 3 m² porch at around {SR('mjq','£4,500')}. For brick, MyJobQuote quotes {SR('mjq','between £5,500 and £8,000')} and MyBuilder {SR('mb','£7,500 to £12,500')}; a uPVC porch is cheaper, from {SR('mjq','£2,800 to £5,200')} on MyJobQuote's figures. Most builds take {SR('mb','between one and three weeks')}. Elizabeth Assaf of Urban Front told Ideal Home that even a porch built just to protect the door should extend {SR('size','at least 500mm on each side')} of it and project at least 1 to 1.5 m.")
p(f"<strong>Before you build:</strong> a ground-level porch under 30 m² is {SR('ppbr','normally exempt')} from Building Regulations, but only if the front door between the house and the porch stays in place, the glazing and any fixed wiring still comply, and the government's guidance says {SR('circ','the building\'s heating system must not be extended')} into it. If your home is listed, Camden Council warns {SR('cam','you must apply for listed building consent')}. And if you do need planning permission, a householder application costs {SR('ppfee','£548 in England')} and {SR('walfee','£585 in Wales')} (2026 fees).")
h3("3. Safety Glass in the Right Places")
p(f"Many small porches are largely glazed, so this matters. Under the Building Regulations (Part K, explained in Approved Document K), glazing in &#8220;critical locations&#8221; must break safely, be robust or be protected, which in a porch usually means toughened or laminated safety glass. Lancaster City Council's guide lists {SR('lan','glazing in doors')} within 1500 mm of the floor, glazing within 300 mm of the edge of a door (again up to 1500 mm from the floor), and other glazing within 800 mm of the floor. Frosted or patterned safety glass in the lower panels also gives privacy without blocking light. Ask your installer to confirm the glass is marked as toughened or laminated.")

h2("Inside a Small Porch")
h3("4. A Bench With Shoes Underneath")
img(3)
p(f"A bench is the most useful thing in a porch: somewhere to sit and pull boots on, with shoes tucked underneath. Chloe Barrow of Laura James suggests you {SR('ihs','opt for multi-functional storage like a bench')} topped with a cushion, and advises you to {SR('ihs','avoid filling it with a cabinet')} or floor-to-ceiling storage that makes a small porch feel cramped. Wayfair UK gives a standard bench height of 45 to 50 cm and a {SR('way','depth of between 38cm and 50cm')}; at the shallow end, a 40 cm deep, 1 m long bench fits along one 1.4 m side wall of our example and still leaves about 1.4 m of floor across to the hooks. Our {a('shoe-storage-ideas','shoe storage ideas')} have more slim options.")
h3("5. Hooks, Not a Coat Stand")
p(f"In a porch under 2 m wide, a coat stand takes up floor you need for the door to swing. Wall hooks or a peg rail leave the floor clear. Teresa Buck of The Cotswold Company told Ideal Home that {SR('ihf','storage to neatly hide away shoes and coats really is key')}. Keep hooks on the wall opposite the bench, add a lower row for children, and keep only this season's coats out; the rest can go in the {a('hallway-storage-ideas','hallway storage')} or a wardrobe.")
h3("6. A Doormat That Actually Fits")
p(f"A doormat that is too small does very little. UK mat seller Mats4U suggests {SR('mats','a mat that covers at least 80% of your doorway\'s width')}, long enough to step on twice, and with enough clearance for the door to swing over it. First Mats says 60 x 85 cm is {SR('fm','the most common size')} for a standard single door. In a porch, put a coir mat inside the outer door and a washable one inside the front door, so dirt is caught twice before it reaches the hall.")
h3("7. A Floor That Copes With Wet Shoes")
p(f"Porch floors get wet, so grip matters as much as in a bathroom. Walls and Floors explains that {SR('wf','R10 frequently appears')} on tiles for homes, while many outdoor tiles carry R11. Porcelain is a good choice for an unheated porch because it absorbs {SR('ps','less than 0.5%')} water, and Eloise Street of The London Tile Co. told Ideal Home that {SR('ihf','vitrified porcelain is an excellent choice')} because it is unaffected by changes in temperature. If you have an original Victorian tiled path or step, restoration consultant Peter Thompson warns on BuildingConservation.com that {SR('bc','exterior tiling should never be sealed')}, because sealing can reduce its frost resistance.")
h3("8. A Mirror and Warm Light")
img(5)
p(f"A small porch can feel like a cupboard, so use light to open it up. Danielle Le Vaillant of Cox &amp; Cox says a mirror {SR('ihs','reflects the light, creating an open and airy space')}, and David Gray of Corston told Homebuilding: {SR('hbi','We would advise having warm white lighting in the porch')}. Rohan Blacker of Pooky suggests you {SR('hg','use spotlights to highlight dark corners')}. A shelf under the window is a good place for a few pots of geraniums or herbs, as long as the porch gets daylight and doesn't freeze.")
p(f"<strong>Skip it:</strong> heating. Jake Vincett of Heritage Build Group told Homebuilding: {SR('cold','Don\'t try to heat the porch')}, because you'll just be wasting money. Elizabeth Assaf suggests you treat it as an unheated buffer zone instead.")

h2("Outside the Porch")
h3("9. A Front Door Colour That Fits the House")
p(f"The front door is the first thing visitors see. Ruth Mottershead of Little Greene suggests you {SR('ihs','consider painting both the door and surrounding frame in one shade')}, which she says makes the entrance appear larger. On Little Greene's own blog she advises you to {SR('lg','avoid selecting bright white shades')} that may be too harsh on the eye, and suggests darker tones for townhouses. Genevieve Hurley told Homes &amp; Gardens to {SR('hg','opt for a high gloss finish')} on the front door, whatever the colour.")
h3("10. Outdoor Lighting That Is Safe and Secure")
p(f"A light by the door helps you find your keys and puts off intruders. NICEIC advises outdoor lights {SR('nic','rated IP44 or higher')}, with automatic controls that switch off in response to daylight and movement. In England, according to the IET, adding a light to an existing circuit is not notifiable, but {SR('iet','the installation of a new circuit')} is; in Wales, outdoor lighting work is notifiable too. Either way, a registered electrician can certify the work. Lucy Mather of Arighi Bianchi told Ideal Home that porch lighting is {SR('ihf','also brilliant as an added security measure')}.")
h3("11. Draughts and Security at the Front Door")
p(f"A porch already shelters the front door, so finish the job on the door itself. The Energy Saving Trust says draught-proofing windows, doors and floors {SR('est2','could save you around £55 a year')} in an older home, and its door guide suggests {SR('est','a letterbox flap or brush')} and a keyhole cover. A council home security guide recommends {SR('sec','three-star TS007 rated cylinders')}, a mortice deadlock to BS 3621 and a letterbox guard so nobody can reach in. If your porch has its own lockable outer door, it's worth fitting it to the same standard.")

h2("If You Only Do One Thing")
p(f"Clear the floor. Of all these small porch ideas, the one that makes the biggest difference is moving everything off the floor and onto hooks, a bench and one big doormat. If you are starting from scratch, check the 3 m², 3 m and 2 m rules before you talk to a builder. For the rest of the entrance, our {a('hallway-ideas','hallway ideas')}, {a('small-entryway-ideas','small entryway ideas')} and {a('boot-room-ideas','boot room ideas')} carry the same approach into the house.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('small porch ideas'),'kw')
