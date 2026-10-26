import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={"bab":"https://www.bookabuilderuk.com/blog/small-dining-room-ideas",
"babl":"https://www.bookabuilderuk.com/blog/dining-room-lighting-ideas",
"ofl":"https://www.oakfurnitureland.co.uk/blog/your-dining-room-measurement-guide/",
"lr":"https://www.laredoute.co.uk/content/how-to-choose-the-right-dining-table-size-for-your-space/",
"hgb":"https://www.homesandgardens.com/ideas/banquette-seating-ideas",
"lth":"https://cae.org.uk/our-services/housing-services/lifetime-homes/7-circulation-space/",
"ikt":"https://www.ikea.com/gb/en/cat/dining-tables-21825",
"nor":"https://www.ikea.com/gb/en/p/-30180504/",
"jl":"https://www.johnlewis.com/john-lewis-iona-4-seater-round-dining-table/oak/p3765224",
"dun":"https://dunelm.com/product/clifford-2-4-seater-drop-leaf-dining-table-1000247241",
"ih":"https://www.idealhome.co.uk/dining-room/small-dining-room-ideas-35006",
"ihm":"https://www.idealhome.co.uk/dining-room/dining-room-decor/small-dining-room-mirror-ideas",
"ihs":"https://www.idealhome.co.uk/dining-room/dining-room-storage-ideas-187432",
"sl":"https://sheerluxe.com/home/interior-design/experts-guide-banquette-seating",
"ndss":"https://www.essexdesignguide.co.uk/design-details/internal-design-details/nationally-described-space-standards/",
"ldg":"https://www.london.gov.uk/media/8395/download",
"yg":"https://yougov.com/en-gb/articles/50383-far-more-britons-eat-dinner-on-the-sofa-than-in-other-western-countries",
"tala":"https://tala.co.uk/blogs/lighting-guide/what-size-pendant-light-do-i-need",
"ikrug":"https://www.ikea.com/ch/en/rooms/dining/how-to/how-to-choose-a-rug-for-your-dining-table-pub69273980/",
"hgl":"https://www.homesandgardens.com/dining-rooms/dining-room-layout-ideas",
"geo":"https://www.dunelm.com/product/georgi-slim-2-door-sideboard-1000296196",
"besta":"https://www.ikea.com/gb/en/p/-s59508049/",
"sur":"https://www.surrey.ac.uk/news/bringing-work-home-dining-room-tables-among-places-doubling-office-desks-half-workers"}
def SR(k,t): return ext(SRC[k],t)

p(f"The best small dining room ideas start with a tape measure: allow 60 cm of table edge per person, keep at least 75 cm between the table and the wall so chairs can pull out, and choose a table that shrinks when you are not using it. A round pedestal table, a banquette along one wall, a drop-leaf or extending table and a slim sideboard all win back floor. Below are 12 small dining room ideas for UK homes, with the measurements that make them work and real products with prices.")
img(1)

h2("Small Dining Room Measurements to Plan Around")
diagram(open('z.svg').read(),"A table for four needs a space about 2.7 x 2.3 m with chairs all round, or 2.7 x 1.95 m with a banquette along one wall.")
p(f"Retailers agree on the basics. IKEA says {SR('ikt','each seat needs 60 centimetres in width')}, so a table for four should be at least 120 cm long, and Oak Furnitureland says {SR('ofl','your table should be no narrower than 90cm')} if people sit on both sides. For space around the table, a UK builders' guide calls 60 cm from table edge to wall {SR('bab','a tight minimum')}, Oak Furnitureland recommends {SR('ofl','a minimum of 75cm of space around the dining table')}, and La Redoute suggests 90 cm. If people need to walk behind a seated diner, allow about 100 to 110 cm.")
p(f"Our worked example in the diagram uses a 120 x 80 cm table with 75 cm all round: that is a 2.7 x 2.3 m dining area. For the size that fits your room, try our {a('dining-table-size-calculator','dining table size calculator')}.")

h2("Tables That Fit")
h3("1. Choose a Round Table on a Pedestal")
p(f"A round table has no corners to walk around, and a single central leg leaves room for knees and chairs. Rebecca Snowden of Furniture and Choice told Ideal Home that {SR('ih','round tables with a central pedestal are perfect due to their smaller footprint')}. As a guide, a table {SR('bab','900 to 1,000 millimetre')} across seats four and 70 to 80 cm seats two. The John Lewis Iona, for example, is 100 cm across and {SR('jl','offers seating for up to 4 diners')}; IKEA's VIHALS round table is 107 cm and costs £59.")
h3("2. Size a Rectangular Table at 60 cm a Head")
p(f"La Redoute's chart puts a {SR('lr','120cm')} table at four people and 180 cm at six. Wide carver chairs with arms need 10 to 15 cm more per person, so in a small room, armless chairs that tuck fully under the table save the most space. A narrow table, 80 cm rather than 90 cm, also works if you only ever sit on one side or at the ends.")
h3("3. Buy for Four, Extend for Six")
p(f"If you host a few times a year, pay for the extra seats only when you use them. Adam Brown of The Painted Furniture Company told Ideal Home that {SR('ih','the flexibility of an extending table is crucial')}. IKEA's ÅLHULT extends from 120 to 170 cm for {SR('ikt','£149')}, and its VIHALS from 120 to 180 cm for £99. Store the leaf where you can reach it, or you will never use it.")
h3("4. Fold It Away: Drop-Leaf and Wall-Mounted Tables")
img(3)
p(f"In a kitchen or a studio flat, a table that folds flat against the wall is the biggest saving of all. IKEA's NORBERG wall-mounted drop-leaf table is 74 x 60 cm when it is up, {SR('nor','seats 2')} and costs £39. The freestanding HAUGA drop-leaf goes from 55 to 109 cm long for £99, and Dunelm's Clifford is just 41 cm wide with both leaves down, opening to 152 cm and {SR('dun','comfortably seats up to four people')}. Our {a('studio-apartment-ideas','studio apartment ideas')} show where a fold-down table fits in one room.")

h2("Seating That Saves Space")
h3("5. Build a Banquette Along the Wall")
img(2)
p(f"Chairs need room to pull out; a fixed bench does not. Jamie Blake of Blakes London told Homes &amp; Gardens that you normally need about 90 cm behind chairs, but you can {SR('hgb','reduce that down to as little as 30cm if the seat fits directly onto the wall')}. Interior designer Christian Bense told SheerLuxe that a fixed banquette {SR('sl','effectively buys you an extra metre in the room')}. For comfort, aim for {SR('bab','a finished seat height of about 450 millimetres')} with a standard 75 cm table, a seat 45 to 50 cm deep and 60 cm of bench per adult. A UK builders' guide puts a carpenter-built banquette at £600 to £1,200.")
h3("6. Put Drawers Under the Bench")
p(f"A built-in bench is also storage. Interior designer Clare Gaskin told Homes &amp; Gardens: {SR('hgb','we\'re big fans of drawers, rather than lid-style lift up bench storage')}, because you do not have to clear the seat to get at what is inside. Keep table linen, candles and the spare table leaf there.")
h3("7. Swap Chairs on One Side for a Bench")
p(f"Even without building anything, a loose bench that slides right under the table takes less room than two chairs. Kris Manalo of Atkin and Thyme told Ideal Home that {SR('ih','adding bench seating rather than chairs is a way to save space')}. Dunelm's Montreal two-seater bench, for example, has a seat 122 cm wide and 48 cm high.")

h2("Storage, Light and Making It Feel Bigger")
h3("8. Choose a Slim Sideboard")
img(4)
p(f"A UK builders' guide suggests you {SR('bab','aim for units between 300 and 400 millimetres deep')} in a small dining room. That is a real saving: Dunelm's Georgi slim sideboard is {SR('geo','D 30cm')} (£199), while a standard IKEA BESTÅ combination is {SR('besta','42')} cm deep. Leave 80 to 120 cm in front of drawers so you can open them with the chairs in place. Our {a('storage-ideas-for-small-spaces','storage ideas for small spaces')} have more shallow options.")
h3("9. Go Up the Walls")
p(f"Floating shelves or a ladder shelf hold glasses, cookbooks and serving dishes without any floor at all. Rebecca Snowden suggests you {SR('ih','utilise wall space like installing floating shelves')}. Our guide to {a('diy-floating-shelves','DIY floating shelves')} shows how to fit them, and our {a('shelf-decor-ideas','shelf decor ideas')} help them look tidy rather than crowded.")
h3("10. Hang One Pendant, Low and the Right Size")
p(f"A pendant over the table marks out the dining area and keeps the floor and table clear of lamps. UK lighting maker Tala suggests hanging it {SR('tala','75–90cm above table surface')}, and says the {SR('tala','pendant diameter should be about 1/2 to 2/3 the width of the table')}, so a 40 to 50 cm shade suits an 80 cm wide table. For a long table, use two smaller pendants about 60 to 80 cm apart. Our {a('chandelier-size-calculator','chandelier size calculator')} works for pendants too.")
h3("11. Use a Rug, a Mirror and Light Walls")
p(f"A rug under the table should be big enough that the chairs stay on it when they are pulled out: Oak Furnitureland says to {SR('ofl','leave at least 60cm on each side of the table')}, and IKEA suggests 60 to 70 cm. Our {a('rug-size-calculator','rug size calculator')} does the sum. Magdalena Gierasinska of Barker and Stonehouse told Ideal Home that {SR('ih','a well-placed mirror can also work wonders to create the illusion of space')}; hang it opposite or beside a window so it reflects daylight. For walls, Lucy Mather of Arighi Bianchi says {SR('ih','light or neutral colours usually work best in a small room')}.")

h2("Small Living and Dining Room Ideas")
img(5)
p(f"Many UK homes do not have a separate dining room. Under the London Housing Design Guide, the {SR('ldg','minimum combined floor area of living, dining and kitchen spaces')} for a two-person home is just 23 m², and a YouGov poll found that only {SR('yg','45%')} of Britons usually eat dinner at a dining table, against 42% who eat on the sofa or in an armchair. If your table shares a room, give it its own zone: Amy Hicks of Blakes London told Homes &amp; Gardens that {SR('hgl','placing a rug under the dining table helps to zone the dining area')}. A pendant over the table and a sofa with its back to the dining space do the same job. Our {a('room-divider-ideas','room divider ideas')} go further.")
h3("12. Make the Table Work Twice")
p(f"A dining table is often the desk too. The Skills and Employment Survey found that {SR('sur','a quarter of workers do so (27%) in spaces intended for other purposes')}, such as the kitchen or dining room, when they work from home. Keep a box or a drawer in the sideboard for the laptop and papers, so the table can be cleared for dinner in a minute.")

h2("If You Only Do One Thing")
p("Measure from the table edge to the wall on every side. If any side is under 60 cm, a different table shape or a banquette on that side will help more than any decor change. Then light the table with one low pendant.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('small dining room ideas'),'kw')
