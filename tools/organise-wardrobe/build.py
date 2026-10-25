import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={"fci":"https://www.fcilondon.co.uk/blog/how-deep-should-built-in-wardrobes-be",
"fci2":"https://www.fcilondon.co.uk/blog/should-fitted-wardrobes-go-to-ceiling",
"ikpdf":"https://www.ikea.com/ie/en/files/pdf/69/0a/690a180e/pax__komplement.pdf",
"rev":"https://www.idealhome.co.uk/house-manual/storage-organisation/reverse-hanger-wardrobe-decluttering-trick",
"hoc":"https://www.houseofcolour.co.uk/blog/from-chaos-to-calm-the-ultimate-guide-to-organising-and-decluttering-your-wardrobe",
"ihw":"https://www.idealhome.co.uk/house-manual/storage-organisation/how-to-organise-your-wardrobe",
"wrap":"https://wrap.ngo/media-centre/press-releases/nations-wardrobes-hold-16-billion-items-unworn-clothes-people-open-new",
"ihs":"https://www.idealhome.co.uk/house-manual/storage-organisation/how-to-organise-a-small-wardrobe-with-lots-of-clothes",
"rn":"https://recyclenow.com/recycle-an-item/clothing-textiles",
"zws":"https://www.zerowastescotland.org.uk/resources/what-do-clothing-and-textiles",
"ikea":"https://www.ikea.com/gb/en/rooms/bedroom/how-to/how-to-organise-your-clothes-pub9c325b77/",
"ob":"https://www.oliverbonas.com/care-guides/fashion/knitwear",
"wh":"https://www.womanandhome.com/fashion/best-way-to-store-jumpers/",
"vel":"https://www.homesandgardens.com/solved/velvet-hangers",
"vs":"https://www.idealhome.co.uk/news/professional-organiser-hanger-size-tip-300676",
"km":"https://konmari.com/how-to-fold-clothes/",
"ff":"https://www.homesandgardens.com/life-design/file-folding-method",
"liv":"https://www.livingetc.com/advice/why-not-to-organize-a-closet-by-color",
"seas":"https://idealhome.co.uk/house-manual/storage-organisation/how-to-store-seasonal-clothes",
"eh":"https://www.english-heritage.org.uk/siteassets/home/learn/conservation/collections-advice--guidance/eh-top-tips-for-preventing-clothes-moth-infestations.pdf",
"eh2":"https://www.english-heritage.org.uk/siteassets/home/learn/conservation/collections-advice--guidance/clothes-moth-prevention-and-control-guideline.pdf",
"nhm":"https://www.nhm.ac.uk/take-part/identify-nature/common-insect-pest-species-in-homes/clothes-moths-identification-guide.html",
"which":"https://www.which.co.uk/news/article/how-to-get-rid-of-clothes-moths-adJHW5b1O1zT",
"tw":"https://www.timberwise.co.uk/blog/how-to-stop-damp-occurring-in-your-wardrobe/",
"hgd":"https://www.homesandgardens.com/solved/new-years-closet-decluttering-rules"}
def SR(k,t): return ext(SRC[k],t)

p(f"To organise clothes in a wardrobe, take everything out, keep only what you wear, then put it back by zone: the clothes you wear most at eye level, longer items on a high rail, shirts and folded trousers on a double rail, and knitwear folded on shelves. Swap to matching slim hangers, group each category by colour, and move out-of-season clothes into clean, breathable storage. The seven steps below take an afternoon for most wardrobes, and the diagram shows how much height each type of clothing needs.")
img(1)

h2("A Wardrobe, Organised by Height")
diagram(open('z.svg').read(),"An example 2 m wide wardrobe in three bays: double hanging, long hanging and shelves, with the space each type of clothing needs.")
p(f"Two numbers decide most layouts. For hanging, London wardrobe maker FCI says {SR('fci','the minimum depth required')} is 60 cm, and it recommends a single rail at 1800 mm and a lower double-hanging rail at about 900 mm. For drop, FCI allows {SR('fci2','90cm for skirts, shirts, and blouses')} and 150 cm for dresses, while IKEA's PAX planner suggests about {SR('ikpdf','100 cm for coats')}. If most of your clothes are shirts and folded trousers, a double rail nearly doubles the hanging space in the same width. Our {a('built-in-wardrobe-ideas','built in wardrobe ideas')} cover what to do if you are fitting a new one.")

h2("Step 1: Empty It and Sort Into Four Piles")
p(f"Take everything out, so you can see the whole collection at once and clean the wardrobe while it is empty. House of Colour suggests four piles: {SR('hoc','Keep, Donate, Sell, and Repair/Alter')}. Professional organiser Hester Van Hien of Tidylicious told Ideal Home to {SR('ihw','start with a category that you find easy')}, as a warm-up. You probably own more than you wear: WRAP found the average UK adult's wardrobe holds 118 items, and {SR('wrap','one quarter (26% - 31 items) were unworn for at least a year')}.")
p(f"If you are unsure about something, House of Colour's rule is that {SR('hoc','if you haven\'t worn it in a year')}, you probably won't wear it again. The popular reverse hanger trick, where you turn every hanger backwards and flip each one after you wear it, shows what you reach for over several months, but author Helen Sanderson warns it can become {SR('rev','a way to avoid decluttering')}. Laura Price of The Home Organisation told Homes &amp; Gardens: {SR('hgd','I don\'t recommend holding onto clothes that no longer fit you')}.")

h2("Step 2: Pass On What You Don't Keep")
p(f"Don't let the donate pile go back in the wardrobe. Recycle Now says {SR('rn','around 49% of all unwanted textiles')} in the UK end up in the bin, even though there are {SR('rn','clothing and textile banks in supermarket and local car parks')}, and high street shops including Primark and M&amp;S have donation banks. Zero Waste Scotland asks you to {SR('zws','wash and dry clothes before donating')}, and to tie shoes together in pairs. Worn-out items can usually go in textile banks too, so check the bank's label. Our {a('declutter-checklist','declutter checklist')} covers the rest of the house.")

h2("Step 3: Plan Zones Before Anything Goes Back")
img(2)
p(f"Now decide where each category will live. The Declutter Hub told Ideal Home to {SR('ihw','place the clothes you use most where they\'re easiest to reach')}, which usually means between knee and head height. Use the top shelf for out-of-season clothes and the floor for shoes. Measure your hanging sections against the drops in the diagram: if your shirts need 90 cm and the space under the rail is 180 cm, you have room for a second rail. A hanging rail that clips onto the existing one is a quick way to test this before you pay for a fitted one.")
p(f"Keep everyday and year-round items in the main wardrobe, as The Declutter Hub suggests, and move anything else out of the way. Professional organiser Elizabeth Wickes told Ideal Home that {SR('ihs','most of us wear 20% of our clothing 80% of the time')}, so that 20% deserves the best spot.")

h2("Step 4: Decide What to Hang and What to Fold")
p(f"Hang anything that creases and fold anything that stretches. IKEA's UK guide says to {SR('ikea','hang blouses, tops, skirts, and jackets')} and to {SR('ikea','fold stretchy items like sweaters and knitted tops')}. Its trousers advice: hang tailored, silk and linen trousers, but {SR('ikea','fold heavier trousers like jeans or sweatpants')}. Oliver Bonas's care guide explains why: {SR('ob','hanging knitwear can cause it to stretch out')} or leave hanger marks. Heather Tingle told Woman &amp; Home that with heavy knits, {SR('wh','the weight of them can cause issues with stretching')}.")

h2("Step 5: Swap to Matching Slim Hangers")
p(f"Matching hangers make a rail look tidy and fit more in. The Declutter Hub's advice is to {SR('ihw','swap mismatched hangers for slim velvet ones')} where you can, and to keep wooden hangers for coats and suits. Homes &amp; Gardens notes that {SR('vel','velvet hangers take up less space')} than thicker wooden and plastic ones, though knits cling to velvet and can be hard to take off. Check the width too: professional organiser Vicky Silverthorn told Ideal Home that some velvet hangers with a bar {SR('vs','can often be too large for your clothing')}, especially in smaller sizes, and pull the shoulders out of shape. Belts can go on a hook or rolled in a drawer; see our {a('belt-storage-ideas','belt storage ideas')}.")

h2("Step 6: Group by Category, Then Colour, and File-Fold Drawers")
img(3)
p(f"Silverthorn's order is simple: {SR('ihw','hang clothes in categories')}, then within each one by sleeve length and colour. Professional organiser Cher Casey told Livingetc the same, and warned that {SR('liv','a rainbow organization can look beautiful')} but is often hard to keep up. Grouping by category first means you can see at once how many black trousers you own.")
p(f"In drawers, fold T-shirts and light knits into rectangles and stand them on end. The KonMari method is about {SR('km','folding clothes neatly and standing them up vertically')}, so you can see everything at once, and Homes &amp; Gardens found file folding {SR('ff','allows us to see exactly what we have')} in one glance, though thick jumpers were too bulky for it. Silverthorn's practical rule: {SR('ihw','fold to a standard you can keep up')}.")
img(4)
p(f"On shelves, keep stacks short so they don't topple: IKEA allows about {SR('ikpdf','30 cm for 10 pairs of folded sweaters')}, which suits shelves 30 to 40 cm apart. Clear shelf dividers hold the stacks upright, and professional organiser Shannon Murphy told Ideal Home to {SR('ihw','use fabric storage boxes or baskets')} for smaller items such as scarves and swimwear.")

h2("Step 7: Store Off-Season Clothes Away From Moths and Damp")
img(5)
p(f"Swap clothes twice a year. Simon Glanville of A Place for Everything told Ideal Home that {SR('seas','it\'s pretty cold by October in the UK')}, so knitwear comes out then, and heavy coats can go away in late March. Store everything clean: English Heritage says to {SR('eh','always ensure clothing is clean')} before it goes into a wardrobe, because the Natural History Museum notes that moths {SR('nhm','prefer low light levels and dirty fabrics')}. Craig Hoareau of A Tidy Mind London advises you to {SR('seas','avoid cardboard boxes as these attract pests')}; use lidded plastic boxes or breathable cotton bags. Vacuum bags save space for bulky synthetics, but Heather Tingle warns {SR('wh','don\'t put cashmere in any vacuum packaging')}.")
p(f"Keep checking for moths: English Heritage suggests you {SR('eh','shake items hanging up inside your wardrobe at least once a month')} and vacuum the wardrobe floor. Which? says pheromone traps {SR('which','won\'t eradicate an infestation')}; they only show you have one. If you find larvae, English Heritage's guideline is to bag the item and freeze it at -18°C {SR('eh2','for at least two weeks')}, then leave it in the bag for 24 hours as it warms up. To stop damp, Timberwise suggests you {SR('tw','make sure that the wardrobe is not overfilled')}, put clothes away fully dry and move the wardrobe slightly away from a cold outside wall.")

h2("Mistakes That Undo the Work")
lst(["<strong>Buying organisers first.</strong> Declutter and measure before you buy boxes or dividers, or you'll be organising clothes you don't wear.",
"<strong>Overfilling the rail.</strong> A packed rail creases clothes and traps damp; if hangers don't slide, take something out.",
f"<strong>Forgetting the one-in, one-out habit.</strong> Shannon Krause told Homes &amp; Gardens to {SR('hgd','consider incorporating exercises like the one-in, one-out method')} through the year, so the wardrobe stays at the size you've just made it.",
f"<strong>Shoes on top of clothes.</strong> IKEA's planner says a shoe rack should never go above clothes. Keep shoes at the bottom, and see our {a('shoe-storage-ideas','shoe storage ideas')} if they don't fit."])

h2("Do This First")
lst(["Take everything out and make four piles: keep, donate, sell, repair.",
"Bag the donations and put them in the car today.",
"Measure your rails and shelves, and add a second rail if shirts leave space below.",
"Fold knits, hang what creases, and switch to one type of slim hanger.",
"Put this season's most-worn clothes at eye level and pack the rest away clean."],ordered=True)
p(f"That is how to organise clothes in a wardrobe so it stays that way. For the rest of the bedroom, our {a('how-to-declutter-your-home','how to declutter your home')} guide uses the same four-pile method room by room.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('organise clothes in a wardrobe'),'kw')
