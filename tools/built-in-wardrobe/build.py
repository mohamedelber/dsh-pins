import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={
"ob":"https://www.online-bedrooms.co.uk/blogs/be-inspired/how-to-build-fitted-wardrobe-in-alcove",
"ldc":"https://www.thelittledesigncorner.com/blog/wardrobe-design-tips",
"fci":"https://www.fcilondon.co.uk/blog/how-deep-should-built-in-wardrobes-be",
"haf":"https://www.hafele.co.uk/en/info/about-haefele/latest-news/how-to-measure-for-sliding-wardrobe-doors/185093",
"ham":"https://www.hammonds-uk.com/blogs/built-in-alcove-wardrobe-storage-ideas/",
"ih":"https://www.idealhome.co.uk/bedroom/fitted-wardrobe-ideas-245917",
"rh":"https://www.realhomes.com/advice/wardrobe-ideas",
"pax1":"https://www.ikea.com/gb/en/p/-10509125",
"pax2":"https://www.ikea.com/gb/en/p/-50509128",
"which":"https://www.which.co.uk/reviews/fitted-bedroom-furniture/article/how-much-do-fitted-wardrobes-cost-a4a121x9WUKu",
"mb":"https://www.mybuilder.com/carpentry-joinery/price-guides/fitted-wardrobes-cost",
"mjq":"https://www.myjobquote.co.uk/costs/installing-a-new-fitted-wardrobe"}
def SR(k,t): return ext(SRC[k],t)
WD=a('wardrobe-depth','wardrobe depth calculator')

p(f"The best built in wardrobe ideas start with one number: depth. Allow at least 600 mm from the wall if you want a hanging rail, and about 650 mm or more if you choose sliding doors. Get that right and a fitted wardrobe can fill an alcove, run wall to wall, tuck under the eaves or squeeze into a box room. Our {WD} checks your space in a few taps.")
p("Below are 10 built in wardrobe ideas for UK homes, each with the measurement that makes it work, plus a diagram of interior heights and what fitted wardrobes cost in 2026.")
img(1)

h2("1. Run It Floor to Ceiling, Wall to Wall")
p(f"Of all the built in wardrobe ideas here, a single run from wall to wall and floor to ceiling gives you the most storage for the floor space it takes, and it looks like part of the room rather than a piece of furniture. Fill the gap at the top with a filler panel so there is no dusty ledge. Keep hinged doors to about 600 mm wide each: FCI London warns that a hinged door {SR('fci','should not be wider than 60cm, or the hinges will be overloaded')}, so a 2 m run usually needs four doors.")

h2("2. Fit Alcove Wardrobes Either Side of the Chimney Breast")
img(2)
p(f"Many older British bedrooms have two recesses either side of a chimney breast, and they are made for fitted wardrobes. Walls are rarely straight, so measure carefully. Online Bedrooms suggests measuring the height {SR('ob','in 3 different places')} and using the tallest, measuring the width at three heights and using the smallest, rounding down to the nearest 50 mm and then taking off 100 mm for scribe panels that are trimmed to fit the wall. Ignore skirting and coving when you measure.")

h2("3. Use Shelves and Drawers in a Shallow Alcove")
p(f"If an alcove is less than 600 mm deep, a hanging rail running side to side will not fit without the wardrobe sticking out into the room; Hammonds notes a shallow alcove can leave {SR('ham','half a wardrobe extending into the room')}. Instead, fill it with shelves and drawers. Designer guides say shelves and drawers are normally finished to {SR('ldc','a depth of 450-500mm')}, so a shallow recess can still hold folded jumpers, bags and bedding.")

h2("4. Choose Sliding Doors for a Tight Bedroom")
img(5)
p(f"Sliding doors need no swing space, so they suit small bedrooms where the bed sits close to the wardrobe. The trade-off is depth: Häfele recommends {SR('haf','a minimum of 650mm for the wardrobe’s depth')} with sliding doors, and FCI London suggests 66 cm plus a running track of about 5 cm. FCI also says a sliding panel should not be wider than 120 cm. Check your room with our {WD}, and see more space savers in our {a('small-bedroom-storage-ideas','small bedroom storage ideas')}.")

h2("5. Build a Slim Wardrobe Into a Box Room")
p(f"In a box room, every centimetre counts. If you only need shelves for folded clothes, FCI London says a hinged wardrobe can be as shallow as 55 cm when you are not planning to hang anything, which leaves a little more floor for a single bed. A full-height cupboard beside the bed with a short rail at the top and shelves below gives a guest room real storage. Our {a('box-room-bedroom-ideas','box room bedroom ideas')} and {a('guest-bedroom-ideas','guest bedroom ideas')} show how to plan the rest of the room.")

h2("6. Turn the Eaves Into Wardrobe Space")
img(4)
p(f"In a loft conversion, the low wall under the slope is often wasted. Ideal Home quotes Sharps saying that {SR('ih','eaves can be turned into storage spaces')}: low drawers and cupboards fit under the slope, and a tall hanging section goes where the ceiling is highest. Made-to-measure eaves units cost more because every panel is cut to the angle, so get quotes early. For the rest of the loft, see our {a('loft-storage-ideas','loft storage ideas')}.")

h2("7. Light the Inside")
p(f"A deep fitted wardrobe can be dark, especially in an alcove. Real Homes suggests adding LED strip lighting to alcove wardrobes so you can see what you own. A strip under the top shelf or along the side panels, switched by the door, makes dark clothes much easier to find and works well on a timer or a door sensor.")

h2("8. Hack IKEA PAX Into a Built-In Look")
p(f"IKEA PAX frames are a popular base for a budget fitted wardrobe. At the time of writing, a {SR('pax1','100x58x236 cm PAX frame costs £90')}, and the 236 cm frame needs a ceiling of at least 237 cm to stand it up, or 240 cm with sliding doors. A {SR('pax2','50x58x201 cm frame costs £70')} and suits lower ceilings. Doors and interiors are sold separately, and IKEA says the frame must be fixed to the wall. Add filler panels to the walls and ceiling and paint them to match for a built-in finish. If you like making things yourself, our {a('diy-closet-shelves','DIY shelving guide')} covers the basics.")

h2("9. Plan the Interior: Long Hang, Double Hang and Drawers")
p("Most built in wardrobe ideas succeed or fail on the interior, so plan it inside out: decide what you hang and fold, then choose the doors. The diagram shows a typical 2 m layout with three bays.")
diagram(open('z.svg').read(),"Built-in wardrobe interior heights: a long-hanging bay, a double-hanging bay and a drawer and shelf bay, with typical heights in mm.")
p(f"Allow {SR('ldc','about 1900mm (H) for long hanging space')} and about 950 mm for short hanging, according to The Little Design Corner. FCI London recommends a single rail at about 1,800 mm (up to 1,900 mm), a lower rail at about 900 mm for double hanging, and 350 to 400 mm between shelves. A drawer bank finished at around 900 to 1,100 mm high doubles as a shelf for a watch tray. Keep shelves adjustable so the layout can change with you.")
img(3)
p(f"Fold knitwear rather than hanging it, using our guide to {a('how-to-fold-clothes-to-save-space','folding clothes to save space')}, and give small things a home with our {a('belt-storage-ideas','belt storage ideas')} and {a('shoe-storage-ideas','shoe storage ideas')}.")

h2("10. Make a Walk-Through Dressing Area")
p(f"If the room is long enough, wardrobes on one or both sides of a short corridor make a dressing area without building a separate room. Leave at least 900 mm of walkway, which is the minimum FCI London gives for a walk-in wardrobe aisle. A mirror on the end wall and a small bench make it feel finished. Our {a('small-walk-in-closet-ideas','small walk-in wardrobe ideas')} have more layouts.")

h2("What Do Built-In Wardrobes Cost in the UK?")
p("Whichever of these built in wardrobe ideas you choose, prices vary with size, doors, interiors and where you live, so treat these as starting points and get at least three quotes.")
table(["Option","Typical price","Source"],[
["DIY flatpack, 3 doors","£500 (standard) to £900 (high quality)",SR('which','Which?, August 2026')],
["Modular, professionally installed","about £2,900 (3 doors), £4,900 (4 doors)","Which?, August 2026"],
["Bespoke","£1,500 to £7,000 (3 doors), £3,900 to £10,000 (4 doors)","Which?, August 2026"],
["Mid-range fitted, per linear metre","£400 to £800 a metre",SR('mb','MyBuilder, October 2026')],
["Fitted with shelves and rails","£1,400 (2 doors), £2,100 (3 doors), £2,800 (4 doors)",SR('mjq','MyJobQuote, October 2026')],
["Sliding doors with shelves and rails","about £2,350","MyJobQuote, October 2026"]])
p("MyJobQuote puts a joiner at about £20 to £25 an hour and says a fitted wardrobe takes between one and nine days to install. Moving sockets or lights inside the wardrobe space adds to the cost, so plan the electrics before the joiner arrives.")

h2("Built In Wardrobe FAQ")
h3("How deep should a built-in wardrobe be?")
p("Allow at least 600 mm from the wall for a hanging rail. Online Bedrooms recommends 600 mm because the back panel and the doors each take about 18 mm. Sliding doors need more room: Häfele recommends at least 650 mm. Shelves-only wardrobes can be shallower, from about 55 cm.")
h3("Is it cheaper to build a wardrobe or buy one?")
p("Building one yourself is usually cheapest. Which? lists DIY flatpack three-door wardrobes from about £500, against about £2,900 for a modular one professionally installed. MyJobQuote says a joiner typically charges £20 to £25 an hour. IKEA PAX frames start at £70, but doors and interiors cost extra.")
h3("What height should a wardrobe rail be?")
p("For long dresses and coats, a rail at about 1,800 to 1,900 mm works for most people. For double hanging, FCI London puts the lower rail at about 900 mm, which leaves roughly 1,000 mm for each row of shirts. Keep the top rail within easy reach of the shortest person using it.")
h3("How do I measure an alcove for a fitted wardrobe?")
p("Measure the height in three places and use the tallest, and the width at three heights and use the smallest. Round down to the nearest 50 mm, then take off 100 mm for scribe panels, which are trimmed to fit uneven walls. Ignore skirting boards and coving when you measure.")

h2("Before You Call a Joiner")
lst(["Clear out first, so you design for what you keep: our "+a('closet-clean-out','wardrobe clear-out guide')+" walks you through it.",
"List what you hang long, hang short and fold, and count your shoes.",
"Measure depth, width and height in several places, and note sockets, radiators and skirting.",
"Decide on hinged or sliding doors before you order, because the depth depends on it."])
p("Get those four things right and any of these built in wardrobe ideas will give you storage that fits the room and lasts for years.")
ai_note()
html='\n\n'.join(out)
html=re.sub(r'(\d+\.\d{2})\d+',r'\1',html)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words')
