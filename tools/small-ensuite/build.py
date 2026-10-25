import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={"houzz1":"https://www.houzz.com.au/ideabooks/96027874/thumbs/7-key-things-to-establish-before-you-plan-an-ensuite",
"bl":"https://blueleafbath.com.au/blogs/blog-posts/standard-bathroom-sizes-dimensions",
"blv":"https://blueleafbath.com.au/blogs/blog-posts/bathroom-vanity-dimensions",
"bls":"https://blueleafbath.com.au/blogs/blog-posts/standard-shower-size",
"ncc104":"https://ncc.abcb.gov.au/editions/ncc-2022/adopted/housing-provisions/10-health-and-amenity/part-104-facilities",
"ncc102":"https://ncc.abcb.gov.au/editions/ncc-2022/adopted/housing-provisions/10-health-and-amenity/part-102-wet-area-waterproofing",
"nsw":"https://www.nsw.gov.au/business-and-economy/licences-and-credentials/building-and-trade-licences-and-registrations/waterproofing-work",
"qbcc":"https://qbcc.qld.gov.au/news/waterproofing-done-right",
"vbafan":"https://www.vba.vic.gov.au/news/news/2022/complaints-exhaust-fan-discharge1",
"cond":"https://cpd.nccb.gov.au/news/2022/improved-condensation-management-ncc-2022",
"wels":"https://waterrating.gov.au/node/8",
"basix":"https://www.planningportal.nsw.gov.au/basix-water/fixtures/showerheads",
"vbaplumb":"https://www.vba.vic.gov.au/consumers/home-renovation-essentials/engaging-plumber",
"ausgrid":"https://ausgrid.com.au/Your-safety/Safety-around-your-home/DIY-and-home-maintenance",
"zones":"https://www.nsw.gov.au/housing-and-construction/compliance-and-regulation/electricians/electrical-standards-rules-and-notes/switches-and-sockets-wet-areas",
"cost":"https://whatsthedamage.com.au/bathroom-renovation-cost-sydney/ensuites/",
"bhgcost":"https://www.bhg.com.au/how-much-does-a-cheap-bathroom-renovation-cost",
"houzz2":"https://www.houzz.com.au/ideabooks/136583044",
"bhg":"https://www.bhg.com.au/homes/renovating/ensuite-bathrooms/",
"tb":"https://www.threebirdsrenovations.com/blog/smallensuites",
"hb":"https://www.homebeautiful.com.au/bathroom-ideas/small-bathroom-design-ideas/",
"racv":"https://www.racv.com.au/royalauto/property/renovating/small-bathroom-renovation.html",
"bun":"https://www.bunnings.com.au/diy-advice/home-improvement/baths-showers-toilets/create-the-perfect-ensuite",
"tiles":"https://www.houzz.com.au/ideabooks/116118984/thumbs/how-do-i-choose-tiles-for-a-small-bathroom",
"tc":"https://tilecloud.com.au/blogs/news/bathroom-heights-placement-guide",
"rail":"https://racv.com.au/royalauto/property/renovating/are-heated-towel-rails-worth-it.html",
"cav":"https://tradecentre.idlvr.com.au/collections/cavity-units"}
def SR(k,t): return ext(SRC[k],t)

p(f"The best small ensuite ideas make a tight room feel bigger by keeping the floor clear and the sightlines open: a frameless glass shower, a wall-hung vanity and toilet, a recessed niche instead of a shower caddy, and a cavity sliding door so no floor is lost to a door swing. Most Australian ensuites are {SR('bl','between 3 and 5 m²')}, and architect Dominic Bagnato told Houzz that a shower, basin and toilet need {SR('houzz1','a minimum floor area of 3 square metres')}. Below are 10 ideas grouped by layout, shower, storage and finishes, with the NCC rules and costs that apply in Australia.")
img(1)

h2("A Small Ensuite, Measured")
diagram(open('z.svg').read(),"An example 1.8 x 2.0 m ensuite with a 900 mm shower, a wall-hung vanity, a cavity slider, and the NCC rules for waterproofing, ventilation and the toilet door.")
p(f"Our example is 1.8 x 2.0 m, or 3.6 m², the size Blueleaf gives for {SR('bl','a compact ensuite')} with a toilet, vanity and 900 x 900 mm shower. Two NCC rules shape every small layout. If a toilet is in a fully enclosed room, its door has to slide, open outwards or lift off {SR('ncc104','unless there is a clear space of at least 1.2 m')} between the pan and the doorway, which is why cavity sliders are so common in ensuites. And in the shower, walls must be waterproofed {SR('ncc102','not less than 1800 mm above the floor substrate')}, with the whole shower floor waterproof.")

h2("Layout")
h3("1. Put Everything on One Wall")
p(f"Plumbing is the expensive part of any ensuite. Laura Merlin of Origin Bathrooms told Houzz that {SR('houzz2','placing the basin, toilet and shower along one wall')} keeps a small room open, and interior designer Kia Howat told Better Homes and Gardens that {SR('bhgcost','maintaining the placement of your existing toilet, shower and vanity waste locations')} saves money in a renovation. In a narrow room, Bagnato notes that {SR('houzz1','if the room is narrow (1 metre or less)')}, a shower-only layout may be the realistic choice.")
h3("2. A Cavity Sliding Door")
img(4)
p(f"A hinged door needs clear floor to swing into, which a small ensuite rarely has. Cavity slider units are sold in widths from 620 to 920 mm, such as a {SR('cav','720 x 90 mm cavity sliding door unit')}, and the door slides into the wall. It also solves the NCC toilet-door rule above. Plan it before the walls go up: the cavity needs a stud-free section of wall the width of the door, so you can't hang towel rails or a cabinet on that stretch.")
p("<strong>Works best:</strong> ensuites opening off a bedroom with a clear wall beside the doorway. <strong>Skip it:</strong> if the only wall beside the door holds plumbing or switches.")
h3("3. Toilet Out of the Line of Sight")
p(f"Designer Sophie Bowers of Strutt Studios told Better Homes and Gardens that {SR('bhg','by placing a toilet near the doorway, your focus will be drawn')} to the rest of the room, not the loo. Designer Kate Walker told RACV that {SR('racv','entering front-on to your vanity creates more circulation space')}. If you can, put the toilet behind the door's line of sight and the vanity or shower opposite the entry.")

h2("The Shower")
h3("4. Frameless Glass and One Floor Tile")
p(f"Bunnings' bathroom buyer Dan Gibney warns that {SR('bun','doors and frames on showers in small spaces can create a closed-in feel')}, and RACV Trades' Andy Anderson says {SR('racv','a clear glass frame allows you to take the whole room in')}. Run the same floor tile into the shower so the room reads as one space. If you go without a screen, the NCC requires a waterstop at a {SR('ncc102','minimum horizontal distance of 1500 mm from the shower rose')}. Blueleaf calls 900 x 900 mm the {SR('bls','standard shower size in Australia')}.")
h3("5. A Recessed Niche, Not a Caddy")
img(2)
p(f"Architect Kirsten Johnstone told Houzz to {SR('houzz2','include a shower ledge or recessed alcove')}. Tile Cloud suggests the base of a niche sits {SR('tc','900mm to 1100mm from FFL')} (finished floor level), and Blueleaf puts the inside height at 150 to 300 mm. A niche needs a stud-free wall cavity or a nib wall, and it must be waterproofed with the rest of the shower, so plan it with your builder before framing.")
h3("6. A Water-Efficient Showerhead")
p(f"The government's WELS scheme says a 3-star shower {SR('wels','that flows at 9L/min will save 70kL and $210')} a year compared with an old 15 L/min head. In NSW, a showerhead of {SR('basix','not more than 7.5 litres per minute is rated WELS 4 stars')}. A rail shower with a hand-held head, as in our photo, also makes cleaning the glass easier.")

h2("Storage")
h3("7. A Wall-Hung Vanity With Drawers")
img(3)
p(f"Johnstone's advice is to {SR('houzz2','wall-mount your vanity and toilet pan')}, so you can see and clean the floor underneath. For depth, Blueleaf gives {SR('blv','ensuite: 600–900mm wide, 460–500mm deep')}, and a slimline vanity under 460 mm suits narrow rooms. Choose drawers over doors: Bunnings says drawers hold up to 30 per cent more than cupboards. An LED strip under the vanity makes a good night light.")
h3("8. A Shaving Cabinet and an In-Wall Cistern")
p(f"Bowers says {SR('bhg','mirrored shaving cabinets are an excellent solution')} in a small ensuite, because they add storage without taking floor space. Three Birds Renovations chose {SR('tb','an in-wall cistern to save space and showcase more of the tiles')} in their own small ensuite, and Bunnings' Gibney suggests you {SR('bun','opt for a wall-hung vanity and a concealed cistern')}. A concealed cistern needs a framed wall and an access panel behind the flush plate.")

h2("Finishes")
h3("9. Large Tiles, Matching Grout and Light Colours")
img(5)
p(f"Christie Wood of Beaumont Tiles told Houzz that {SR('tiles','slab tiles of 800x1,600 millimetres and above are a brilliant choice')} for walls, and that she always recommends matching the grout to the tile so there are fewer visible lines. Bunnings suggests large tiles in cool colours to bounce light around, and Ari Zorlu of Paco Jaanson says {SR('houzz2','opt for neutrals for longevity')}. If you want colour, keep it to one wall: Kate Bath of Blue Tea Kitchens and Bathrooms {SR('hb','used wall tiles sparingly, to make the room feel larger')}.")
h3("10. A Skylight and a Proper Exhaust Fan")
p(f"Many ensuites have no window. Anderson says {SR('racv','a skylight is a fairly inexpensive way to attract natural light')}, and Johnstone prefers to {SR('houzz2','locate skylights to capture southern light')} where possible. You still need extraction: the NCC calls for {SR('vbafan','25 L/s for a bathroom')}, discharged outside, and since NCC 2022 a fan in a room without enough outdoor air must {SR('cond','continue to operate for 10 minutes')} after the light goes off. A heated towel rail helps towels dry; RACV puts a 200 W rail running all day at {SR('rail','around $1.68')} a day at 35c/kWh.")

h2("Before You Renovate")
lst([f"<strong>Use licensed trades.</strong> The Victorian Building Authority says to {SR('vbaplumb','engage a licensed or registered plumber')} for plumbing work, and Ausgrid warns that {SR('ausgrid','DIY electrical is not only dangerous, it\'s illegal')}. Electrical zones around the shower and basin limit where switches and power points can go.",
f"<strong>Get waterproofing right.</strong> In NSW you need a contractor licence for waterproofing work {SR('nsw','valued at more than $5,000')}, and in Queensland the QBCC says bathroom home warranty claims {SR('qbcc','averaged almost $25,000 in rectification costs')}.",
f"<strong>Budget.</strong> One Sydney cost guide puts ensuite renovations at {SR('cost','$17,250–$34,500')}, with plumbing rough-in alone at $2,300 to $5,750, and premium jobs much higher. Keeping the wastes where they are is the biggest saving.",
f"<strong>Related ideas.</strong> Our {a('small-bathroom-storage-ideas','small bathroom storage ideas')} and {a('bathroom-wall-decor-ideas','bathroom wall decor ideas')} help once the build is done, and our {a('walk-in-robe-ideas','walk in robe ideas')} cover the other half of a master suite."])

h2("Mix and Match")
p("If your budget covers only three of these small ensuite ideas, choose a frameless screen with one floor tile throughout, a wall-hung vanity with drawers, and a cavity slider. Together they free up the most floor and light, and none of them needs the plumbing moved.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('small ensuite ideas'),'kw')
