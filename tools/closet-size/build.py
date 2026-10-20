import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
CC="https://www.californiaclosets.com/blog/ideal-walk-in-closet-size/"
HG="https://homeguide.com/articles/walk-in-closet-dimensions"
DIM="https://www.dimensions.com/element/double-sided-walk-in-closets"
TOH1="https://www.thisoldhouse.com/closets/closet-organization-guide"
TOH2="https://www.thisoldhouse.com/closets/cut-the-clutter-with-proper-closet-organization"
LE="https://www.livingetc.com/advice/closet-dimensions"
HUN="https://www.hunker.com/13413647/what-is-the-proper-height-for-closet-rods-shelves/"
BV="https://www.bobvila.com/articles/closet-rod-height/"
FCI1="https://fcilondon.co.uk/blog/minimum-size-for-walk-in-wardrobe"
FCI3="https://fcilondon.co.uk/blog/average-width-walk-in-wardrobe"
p("What is the right walk-in closet size? Most walk-in closets need at least 5 x 5 ft, a closet with clothes on two facing walls needs about 7 ft of width, and a typical walk-in for one or two people is about 6.5 to 7 ft wide by 10 ft deep. This free <strong>walk-in closet size</strong> calculator works out the size for your layout and wardrobe in two taps.")
p("Pick a layout, then how much you hang. You get a comfortable size, the tight minimum, the length of hanging rod and a simple floor plan, in feet and meters. Open <em>More options</em> to enter your own closet measurements and see which layout fits.")
add('<!-- wp:html -->\n'+open('tool.html').read()+'\n<!-- /wp:html -->')
h2("Walk-In Closet Size Chart")
table(["Closet","Size","Area","What fits"],[
["Absolute minimum","4 x 4 ft","16 sq ft","One short rod, tight to use"],
["Small","5 x 5 ft","25 sq ft","Clothes on one wall with a walkway"],
["Average, one person","6.5 x 8 ft","52 sq ft","Clothes on two walls"],
["Average, two people","7 x 10 ft","70 sq ft","Two walls or a U-shape"],
["Large","10 x 10 ft","100 sq ft","U-shape, room for a small island"],
["Luxury","10 x 12 ft and up","120+ sq ft","Island, seating, full-length mirror"]])
p(f"California Closets says {ext(CC,'the minimum viable size for a walk-in closet is about 4’ x 4’')}, but HomeGuide notes that {ext(HG,'most designers recommend no smaller than 5 by 5 feet (25 square feet) for practical daily use')}. For a typical home, HomeGuide puts the standard walk-in at {ext(HG,'approximately 6.5 to 7 feet wide by 10 feet deep')}. These are industry rules of thumb, not official averages.")
img(1)
h2("Minimum Walk-In Closet Size by Layout")
p("The width of a walk-in closet comes from two numbers: about 24 in of depth for each wall of hanging clothes, and a walkway of 24 in (tight) to 36 in (comfortable). Add them up and you get the width each layout needs.")
diagram(re.sub(r'(\d+\.\d{1,2})\d+',r'\1',open('z.svg').read()),"Walk-in closet sizes by layout: 24 in for each wall of clothes plus a 36 in walkway. One wall needs 5 ft, two walls or a U-shape need 7 ft, an L-shape starts at 5 x 5 ft and a closet with an island needs about 12 x 12 ft.")
table(["Layout","Tight minimum","Comfortable","How it adds up"],[
["One wall","4 ft wide","5 ft wide","24 in clothes + walkway"],
["Two walls","6 ft wide","7 ft wide","24 in + walkway + 24 in"],
["L-shape","4 x 4 ft","5 x 5 ft","walkway in front of both walls"],
["U-shape","6 ft wide","7 ft wide","same width as two walls, plus a back wall"],
["With an island","10 x 10 ft","12 x 12 ft","walkway on every side of the island"]])
p(f"This Old House says walk-ins {ext(TOH1,'should be at least 6 feet wide to allow for a 2-foot aisle and 2 feet of hanging space on either side')}, and Dimensions.com gives {ext(DIM,'7’ (213 cm) for two sets of comfortable hanger rods')}. For a U-shape, HomeGuide says such closets {ext(HG,'require at least 7 feet wide and 10 feet deep')}.")
h3("One-Wall Walk-In Closet")
img(2)
p("A one-wall closet keeps every rod, shelf and drawer on a single wall. It is the best choice for a narrow space, a deep reach-in closet you want to walk into, or a corner of a bedroom. At 5 ft wide you get 24 in for clothes and a comfortable 36 in walkway.")
h3("Two-Wall (Double-Sided) Walk-In Closet")
img(3)
p("Clothes on two facing walls give you twice the hanging space in the same length. Plan on 7 ft of width; at 6 ft the walkway shrinks to 24 in, which works for one person but feels tight. A 7 x 10 ft two-wall closet holds about 20 ft of single rod.")
h3("L-Shaped Walk-In Closet")
img(4)
p("An L-shape uses two walls that meet in a corner and leaves open floor for a stool or a small rug. Corners are hard to reach, so put shelves or a corner unit there instead of two rods that run into each other.")
h3("Walk-In Closet With an Island")
img(5)
p(f"An island adds drawers and a folding surface, but it needs space on every side. California Closets says that with a center island {ext(CC,'you’ll want at least 36” of clearance on all sides')}, and suggests an island layout in {ext(CC,'larger areas (10’ x 10’ or more)')}. With 36 in walkways all around, plan about 12 x 12 ft.")
h2("Average Walk-In Closet Size")
p(f"There is no official national figure, but closet companies agree on a range. Architect Matthew Coates, quoted by Livingetc, says {ext(LE,'a medium walk-in closet usually ranges from 40-70 square feet')} and {ext(LE,'a large walk-in closet can be 100 square feet or more')}. In practice, a closet for one person is often about 6.5 x 8 ft, and a shared main-bedroom closet about 7 x 10 ft.")
h2("Walk-In Closet Dimensions: Depth, Walkway and Rod Height")
table(["What","Standard size","Notes"],[
["Hanging depth","24 in (61 cm)","20 in works at a squeeze"],
["Shelves","12 to 16 in deep","12 to 14 in for shoes"],
["Drawers","18 to 24 in deep","for folded clothes"],
["Walkway","24 in minimum","30 to 36 in is comfortable"],
["Around an island","36 in","on every side"],
["Single rod","66 in high","for shirts, dresses and coats"],
["Double hang","about 80 to 82 in and 40 in","two rods, one above the other"],
["Long hang","50 to 60 in of clear drop","dresses and long coats"]])
p(f"HomeGuide says {ext(HG,'walkway clearance should be at least 24 inches, though 30 to 36 inches is more comfortable')}. For double hang, Bob Vila suggests you {ext(BV,'mount the top rod 81¾ inches above the floor and the lower rod 40½ inches above the floor')}, and This Old House notes that {ext(TOH2,'long dresses and coats require 50 to 60 inches of hanging space')}.")
img(6)
h2("How Much Hanging Space Do You Need?")
p(f"A common rule is to {ext(HUN,'provide 4 feet of closet rod space per person using the closet')}, but that is a bare minimum. Hunker suggests {ext(HUN,'about 2 1/2 inches of rod space per apparel item')}, so 40 shirts, trousers and dresses need about 8 ft of rod, and coats need more. Count what you hang today, add some room to grow, and use double hang for shorter clothes to fit almost twice as much on the same wall.")
h2("How the Walk-In Closet Size Calculator Works")
lst(["<strong>Width:</strong> 24 in for each wall of hanging clothes (22 in if you choose it) plus your walkway. The comfortable size uses a 36 in walkway, the tight minimum 24 in.",
"<strong>Length:</strong> long enough for the hanging rod you need, and at least 4 ft. Corners in L-shaped and U-shaped closets lose about 24 in of rod each.",
"<strong>Hanging rod:</strong> about 2.5 in per hanging item, so Small is about 25 items (5 ft), Average about 40 (8 ft), Large about 60 (12 ft) and Two people about 75 (16 ft). These groups are our own estimates.",
"<strong>Drawers and shoes:</strong> we add 2 to 4 ft of wall for drawers and shoe shelves, depending on your wardrobe. Shelves above the rods need no extra wall. This is our own estimate.",
"<strong>Double hang:</strong> we assume most clothes can go on two rods and a few need long hang, so the wall needed drops to about 60 percent. This is our own estimate.",
"<strong>Island:</strong> a 24 x 48 in island with your walkway on every side."])
p("The sizes are planning guides from closet designers, not building codes. Check door swings, windows and light switches before you build.")
h2("Walk-In Wardrobe Size in Meters")
p(f"In the UK, the same rules apply in metric. FCI London says {ext(FCI1,'the minimum depth for wardrobe carcassing with a standard hanging rail is 60cm internally')}, and suggests a walk-in wardrobe of {ext(FCI1,'at least 1.5m x 1.5m for one person, or 2m x 3m for a shared space')}. For layouts, it says {ext(FCI3,'double-sided walk-in wardrobes require a minimum width of 1.8 to 2.6m')}, and that {ext(FCI3,'U-shaped layouts are slightly larger at a minimum width of 2.1m')}. Our calculator shows every result in meters too.")
add(open('savebox.html').read())
h2("Walk-In Closet Size FAQ")
h3("What is the minimum size for a walk-in closet?")
p("About 4 x 4 ft is the smallest walk-in closet, but 5 x 5 ft is more practical: it gives you 24 in for clothes on one wall plus a 36 in walkway. With clothes on two facing walls, you need at least 6 ft of width, and 7 ft is comfortable.")
h3("What is the average size of a walk-in closet?")
p("Most walk-in closets are about 6.5 to 7 ft wide and 8 to 10 ft long, or about 50 to 70 sq ft. A large primary closet is 100 sq ft or more.")
h3("Is a 5 x 5 walk-in closet too small?")
p("No, not for one person with a modest wardrobe. In an L-shape, a 5 x 5 ft closet gives about 8 ft of wall for rods and drawers, and double hang fits almost twice as many shirts and trousers on the same wall.")
h3("How wide should a walk-in closet be for two sides?")
p("Plan on 7 ft: 24 in of hanging depth on each side and a 36 in walkway. At 6 ft the walkway is only 24 in, which works but feels tight.")
h2("More Closet Planning Tools")
p(f"Planning a reach-in instead? Our {a('wardrobe-depth','wardrobe depth calculator')} checks how deep it needs to be. For layouts and storage tricks, see our {a('small-walk-in-closet-ideas','small walk-in closet ideas')} and {a('small-closet-organization-ideas','small closet organization ideas')}.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script.*?</script>|<style.*?</style>|<svg.*?</svg>','',html))
print(len(html.encode()),'words',len(txt.split()),'kw',txt.lower().count('walk-in closet size'),txt.lower().count('walk-in closet'))
