import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={
"silva":"https://www.silvawardrobeco.com.au/resources/how-much-space-do-you-need-for-a-walk-in-wardrobe",
"tnt":"https://www.tntwardrobes.com.au/walk-in-robe-layout-guide/",
"kf":"https://kitchenfox.com.au/blog/walk-in-wardrobe-design-layouts/",
"hz1":"https://www.houzz.com.au/magazine/expert-eye-how-to-squeeze-in-a-walk-in-wardrobe-stsetivw-vs~79140125",
"hz2":"https://www.houzz.com.au/magazine/an-insiders-guide-to-walk-in-wardrobe-measurements-stsetivw-vs~74725564",
"air":"https://www.airtasker.com/tradesman/built-in-wardrobe/price/built-in-wardrobe-cost/",
"pax1":"https://www.ikea.com/au/en/p/pax-2-wardrobe-frames-dark-grey-s89600131/",
"pax2":"https://www.ikea.com/au/en/p/pax-2-wardrobe-frames-dark-grey-s99600135/",
"bun":"https://www.bunnings.com.au/flexi-storage-white-1-hang-rail-2-shelf-walk-in-wardrobe-unit_p2583987",
"nsw":"https://www.nsw.gov.au/legal-and-justice/consumer-rights-and-protection/safety/electrical-safety/avoiding-electrical-accidents",
"esv":"https://www.energysafe.vic.gov.au/electrical-ddiy-dont-do-it-yourself",
"sah":"https://www.sahealth.sa.gov.au/wps/wcm/connect/Public+Content/SA+Health+Internet/Public+health/Living+conditions+and+sanitation/Mould+in+the+house",
"wa":"https://wa.gov.au/system/files/2023-07/preventing_dampness_mould.pdf",
"accc":"https://www.productsafety.gov.au/about-us/product-safety-news/news/toppling-furniture-and-televisions-anchor-them-and-save-a-child%E2%80%99s-life",
"stroud":"https://www.stroudhomes.com.au/five-quick-questions-about-walk-in-robes-wir"}
def SR(k,t): return ext(SRC[k],t)

p(f"The best walk in robe ideas start with one decision: width. A walk-in robe with hanging on one side needs a room about 1.5 metres wide, and one with robes on both sides needs about 2.1 metres, because each run of hanging is about 600 mm deep and you want around 900 mm to walk between them. Get the layout right for your space and every other idea, from shoe towers to LED strips, slots in around it.")
p(f"In Australian floor plans you will often see it shortened to WIR, which Stroud Homes notes is {SR('stroud','simply short for walk-in robe')}. The 10 walk in robe ideas below are grouped into layouts, the inside of the robe and finishing touches, with costs at the end.")
img(1)

h2("Which Walk-In Robe Layout Fits Your Room?")
diagram(open('z.svg').read(),"Walk-in robe layouts from above: single-sided about 1,500 mm wide, galley about 2,100 mm, L-shape in a 2,400 x 1,800 mm room, U-shape 2,400 to 2,600 mm or more.")
p(f"Silva Wardrobe Co describes 900 to 1000 mm of walkway as {SR('silva','everyday comfort')}, with 800 mm as the absolute minimum between facing units. If two people will use the robe at the same time, TNT Wardrobes suggests 1100 to 1200 mm.")

h2("Walk In Robe Layout Ideas")
h3("1. Run Robes Down Both Sides in a Galley")
p(f"A galley, with hanging on both long walls, gives the most storage for a narrow room. TNT Wardrobes says two opposing hanging runs {SR('tnt','need a room width of roughly 2,100 mm')}. Put long hanging on one side and double hanging with shelves and drawers on the other, as in the robe above, so each side does a different job.")
h3("2. Go Single-Sided in a Narrow Space")
p(f"If the room is only about 1.5 metres wide, put everything on one wall and keep the other wall clear, perhaps for a full-length mirror. A single-sided robe is also the easiest to fit with flat-pack units, because every unit sits against the same wall. Our {a('walk-in-closet-size','walk-in closet size guide')} works through the maths for other room sizes.")
h3("3. Use an L-Shape for a Corner")
img(2)
p(f"An L-shape wraps robes around two walls and leaves the rest of the floor open, which suits a square room or a corner of a large bedroom. Kitchenfox, an Adelaide cabinetmaker, gives about 2,400 x 1,800 mm as a minimum room for this layout. The corner itself is awkward to reach, so use it for shelves of folded clothes rather than hanging.")
h3("4. Plan a Walk-Through Robe Carefully")
p(f"A walk-through robe is one where the robe {SR('kf','forms a corridor between bedroom and ensuite')}. It saves a separate hallway, but your clothes sit next to a steamy bathroom. SA Health advises keeping {SR('sah','cupboards and bedrooms uncluttered and well ventilated')} to prevent mould, so make sure the ensuite has a working exhaust fan and keep the door closed while you shower.")

h2("Inside the Robe")
h3("5. Make Some Sections Shallow")
p(f"Not everything needs a full 600 mm. Hanging needs about {SR('silva','520 to 550 mm of internal depth')}, but a designer quoted by Houzz Australia says shoe and drawer units {SR('hz1','work perfectly fine between 300 to 380 millimetres deep')}. In a tight galley, using shallow shelves on one side can turn an uncomfortable walkway into a usable one. Houzz notes shelving is commonly 450 mm deep.")
h3("6. Double Up the Hanging")
p(f"Most shirts, skirts and folded trousers are less than a metre long, so two rails stacked in one bay hold twice as much as one. Kitchenfox suggests {SR('kf','top at 1,800mm, bottom at 900mm')} for double hanging, and a single rail at about 1,800 mm for long dresses and coats. Keep one bay of long hanging and make the rest double. Folding knitwear instead of hanging it saves more space; see our guide to {a('how-to-fold-clothes-to-save-space','folding clothes to save space')}.")
img(6)
p("This before and after illustration shows the same robe crammed and then sorted: clothes off the floor, one style of hanger and folded stacks on the shelves. Most of the change comes from clearing out first, which our "+a('closet-clean-out','wardrobe clean-out guide')+" walks through.")
h3("7. Build a Shoe Tower")
img(3)
p(f"Shoes waste space when they are piled on the robe floor. A tower of shallow shelves, one pair per shelf, keeps them visible and off the walkway. Houzz Australia suggests spacing shoe shelves {SR('hz2','220 to 260 mm')} apart, which suits most flat shoes; leave a few taller gaps for ankle boots. More ideas are in our {a('shoe-storage-ideas','shoe storage ideas')}.")
h3("8. Add a Shallow Drawer for Accessories")
img(5)
p(f"Belts, scarves, sunglasses and jewellery get lost on shelves. One shallow drawer with dividers keeps them in sight. If you are adding a freestanding chest of drawers or a tall unit rather than built-in joinery, fix it to the wall: the ACCC tells households to {SR('accc','secure furniture and TVs using furniture straps, angle braces or anchors screwed into walls')}. Our {a('jewelry-storage-ideas','jewellery storage ideas')} and {a('belt-storage-ideas','belt storage ideas')} have more ways to organise small things.")

h2("Finishing Touches")
h3("9. Light It With LED Strips")
img(4)
p(f"A walk-in robe often has no window, and a single ceiling light leaves the shelves in shadow. LED strips under each shelf and above each rail make colours easier to see, and Kitchenfox recommends warm 3,000K light. Battery or plug-in sensor strips need no wiring. Anything hard-wired must be done by a licensed electrician: NSW Government advice says {SR('nsw','by law any electrical installation work must be done by a licensed electrician')}, and Energy Safe Victoria warns that unqualified electrical work is {SR('esv','illegal')}.")
h3("10. Start With Flat-Pack and Upgrade Later")
p(f"Custom joinery looks best but costs the most. Flat-pack systems let you start smaller and add pieces later. At the time of writing, IKEA Australia lists two PAX frames 200 x 58 x 201 cm for {SR('pax1','A$460')}, or {SR('pax2','A$480')} in the 236 cm height, with doors and interiors extra. Bunnings sells a Flexi Storage walk-in unit with one rail and two shelves, 606 x 2000 x 480 mm, for {SR('bun','A$199')}. Keep damp gear out of any robe: WA Government guidance on mould says to make sure {SR('wa','damp footwear and clothes are not put away in wardrobes')}.")

h2("What Does a Walk-In Robe Cost in Australia?")
p("Whichever walk in robe ideas you choose, prices vary a lot with size, finish and city, so treat these as rough guides and get several quotes.")
table(["Option","Typical price","Source"],[
["Flat-pack frames (IKEA PAX, 2 frames)","A$460 to A$480 before doors and interiors",SR('pax1','IKEA Australia')],
["Flat-pack walk-in unit (Bunnings Flexi Storage)","A$199 per unit",SR('bun','Bunnings')],
["DIY wardrobe kits","A$500 to A$2,000",SR('air','Airtasker')],
["Custom single-wall walk-in robe","A$4,000 to A$9,000 (Adelaide)",SR('kf','Kitchenfox')],
["Custom galley walk-in robe","A$9,000 to A$16,000 (Adelaide)","Kitchenfox"],
["Custom walk-through robe","A$14,000 to A$25,000 (Adelaide)","Kitchenfox"]])
p("Airtasker quotes higher figures for fully custom walk-in robes, from about A$20,000 and sometimes over A$30,000, so the gap between quotes can be large.")

h2("Mix and Match")
p("Most walk in robe ideas work best in combination. Three that suit common Australian homes:")
lst(["<strong>Small budget, narrow room:</strong> single-sided flat-pack units, double hanging, a shoe tower at the end and plug-in LED strips.",
"<strong>Family robe for two:</strong> a galley with 1100 to 1200 mm between sides, his-and-hers halves and one shared drawer bank.",
"<strong>Walk-through to the ensuite:</strong> shallow shelves on one side to keep the corridor wide, closed drawers rather than open shelves, and a strong exhaust fan in the bathroom."])
p(f"If you are in the UK or US, our {a('built-in-wardrobe-ideas','built-in wardrobe ideas')} and {a('small-walk-in-closet-ideas','small walk-in closet ideas')} cover the same ground with local sizes.")
ai_note()
html='\n\n'.join(out)
html=re.sub(r'(\d+\.\d{2})\d+',r'\1',html)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('walk in robe ideas')+html.lower().count('walk-in robe ideas'),'kw')
