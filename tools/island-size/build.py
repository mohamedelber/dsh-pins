import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
NK="https://kb.nkba.org/uploads/2022/05/Kitchen-Planning-Guidelines.pdf"
BV="https://www.bobvila.com/articles/kitchen-island-size.md"
FX="https://fixr.com/articles/kitchen-island-dimensions"
TOH="https://www.thisoldhouse.com/kitchens/21016275/how-to-size-a-kitchen-island"
JLC="https://www.jlconline.com/remodeling/guidlines-for-kitchen-island-functionality"
WR="https://www.wrenkitchens.com/blog/do-you-have-room-for-a-kitchen-island"
HB="https://www.homebuilding.co.uk/advice/kitchen-island-sizes"
p("What size kitchen island do you need? Start with the space around it: keep a 42 in work aisle between the island and your counters (48 in if two people cook) and at least 36 in walkways elsewhere. Most kitchens need about 13 ft of width before an island fits, and the average island is about 40 x 80 in. This free <strong>kitchen island size calculator</strong> finds the biggest island that fits your kitchen in two taps.")
p("Pick your kitchen size and where the cabinets are. You get the largest island that keeps safe walkways, how many stools fit and a top view of the layout. Open <em>More options</em> to type your exact measurements, plan for two cooks, switch to bar height or use meters.")
add('<!-- wp:html -->\n'+open('tool.html').read()+'\n<!-- /wp:html -->')
h2("Kitchen Island Size Chart")
table(["Kitchen","Cabinets on one wall","L-shaped cabinets","U-shaped cabinets"],[
["10 x 12 ft","no island, try a cart","no island, try a cart","no island, try a cart"],
["12 x 14 ft","8 ft x 40 in, no side seats","5 ft x 40 in, no side seats","no island"],
["14 x 16 ft","10 ft x 48 in, 5 stools","7 ft x 48 in, 3 stools","4 ft 6 in x 48 in, 2 stools"],
["16 x 20 ft","10 ft x 48 in, 5 stools","10 ft x 48 in, 5 stools","8 ft 6 in x 48 in, 4 stools"]])
p("The chart uses a 42 in work aisle, 25 in deep cabinets, 36 in walkways at open ends and 44 in behind the stools. Your own walls, doors and windows may change the result, so use the calculator with your exact measurements.")
img(1)
h2("Kitchen Island Clearance: Aisles and Walkways")
diagram(re.sub(r'(\d+\.\d{1,2})\d+',r'\1',open('z.svg').read()),"Kitchen island clearances: a 42 to 48 in work aisle between the island and the cabinets, 36 in walkways, 24 in of counter per stool, a 15 in overhang for knee space and 44 in behind the stools so people can walk past.")
p(f"The National Kitchen &amp; Bath Association (NKBA) says {ext(NK,'the width of a work aisle should be at least 42″ (1067 mm) for one cook and at least 48″ (1219 mm) for multiple cooks')}, and that {ext(NK,'the width of a walkway should be at least 36″ (914 mm)')}. A work aisle is the space in front of the sink, range or fridge; a walkway is where people only pass through.")
img(4)
h2("Minimum Kitchen Island Size")
img(2)
p(f"Bob Vila says that {ext(BV,'at a minimum, your built-in kitchen island size will need to be four feet by two feet')}, and warns that {ext(BV,'if your kitchen is less than 13 feet wide, it is unlikely that a built-in island will be possible')}. Fixr gives a floor-area check: {ext(FX,'if your kitchen is at least 150 square feet, you should be able to fit an island')}.")
p("A 2 x 4 ft island works as an extra prep surface, but it is too narrow for seating. If you want stools on one side, plan on about 36 to 42 in of depth.")
h2("Average Kitchen Island Size")
p(f"Fixr notes that {ext(FX,'the typical kitchen island dimensions are 40 inches wide by 80 inches long')}, or about 1 x 2 m. Designers also use a simple rule of thumb: Fixr says {ext(FX,'most islands look best when they take up around 10% of the total kitchen square footage')}. This is a style guide, not an NKBA rule, and the calculator shows your percentage so you can judge for yourself.")
table(["Island","Size","Good for"],[
["Small","24 x 48 in (2 x 4 ft)","extra prep space, no seating"],
["Medium","36 x 72 in (3 x 6 ft)","prep and 2 stools on the end or side"],
["Average","40 x 80 in","prep and 3 stools"],
["Large","48 x 96 in (4 x 8 ft) and up","prep, a sink or cooktop and 4 stools"]])
h2("Kitchen Island Seating: How Much Space per Stool?")
img(3)
p(f"The NKBA recommends a knee space 24 in wide for each seat, and JLC confirms that {ext(JLC,'the NKBA guidelines recommend that each seat be 24 inches wide')}. How deep the knee space should be depends on the counter height:")
table(["Counter height","Width per seat","Knee space"],[
["30 in (table)","24 in","18 in"],
["36 in (counter)","24 in","15 in"],
["42 in (bar)","24 in","12 in"]])
p(f"Behind the stools, NKBA says to {ext(NK,'allow 32″ (813 mm) of clearance from the counter/table edge to any wall or other obstruction behind the seating area')}, at least 36 in for someone to edge past and at least 44 in for someone to walk past. Our calculator uses 44 in so the kitchen still works when the stools are full.")
h2("How Much Overhang for Island Seating?")
p(f"This Old House recommends {ext(TOH,'a minimum overhang of 15 inches for standard-height counters and a 12-inch overhang for bar-height counters')}. Overhangs past about 10 to 12 in usually need brackets or corbels; the limit depends on the countertop material and thickness, so check with your countertop maker.")
h2("Island With a Sink or Cooktop")
img(5)
p(f"An island with a sink or cooktop needs more length and depth. Bob Vila suggests about 7 ft for an island with either one, and {ext(BV,'at least nine feet long')} for both. For a cooktop, NKBA says {ext(NK,'the countertop should also extend a minimum of 9″ (229 mm) behind the cooking surface')}, so nobody at the stools sits right next to a hot pan.")
h2("Small Kitchen? Try a Cart or a Peninsula")
img(6)
p("If the calculator says a fixed island will not fit, a rolling cart about 2 x 3 ft gives you extra prep space and moves out of the way when you need the floor. A peninsula, joined to the end of your counters, needs a walkway on only three sides and often fits where an island does not.")
h2("How the Kitchen Island Size Calculator Works")
lst(["<strong>Cabinets:</strong> 25 in deep (24 in base cabinets plus the countertop edge), along one, two or three walls.",
"<strong>Work aisle:</strong> 42 in for one cook or 48 in for two in front of every run of cabinets, and 36 in at open ends.",
"<strong>Seating:</strong> stools on one long side when the island can be at least 24 in plus the knee space deep and still leave 44 in behind the stools.",
"<strong>Size:</strong> the biggest island that fits, up to 48 in deep and 10 ft long. The 10 ft cap is our own choice, because longer tops often need a seam.",
"<strong>Rule of thumb:</strong> we show how much of the floor the island covers, compared with the 10% guide."])
p("These are planning guidelines, not building codes. Check door swings, appliance doors and windows before you build.")
h2("Kitchen Island Size in the UK")
p(f"UK designers work in metres but use similar numbers. Wren says that {ext(WR,'generally the rule of thumb is a 1 metre clearance zone')} around the island, and Homebuilding &amp; Renovating notes that {ext(HB,'the practical minimum size for an island is 1m x 1m')}. For the average, Wren says {ext(WR,'the average size of an island is 1 by 2 metres')}. UK sources disagree on room width: some say a 4.2 m wide room is enough, others say 4.5 to 5 m. Choose <em>Meters</em> in More options to use the calculator in metric.")
add(open('savebox.html').read())
h2("Kitchen Island Size FAQ")
h3("How much space do you need around a kitchen island?")
p("Leave at least 42 in between the island and the counters for one cook, 48 in for two, and at least 36 in anywhere people only walk past. Behind island stools, allow about 44 in so people can walk behind someone sitting down.")
h3("What is the minimum kitchen size for an island?")
p("Most guides say a kitchen should be at least about 13 ft wide, or about 150 sq ft, for a built-in island. In a narrower kitchen, a cart or a peninsula usually works better.")
h3("How big should a kitchen island be for 4 stools?")
p("Allow 24 in of counter per stool, so 4 stools need an island about 8 ft long. With a 15 in overhang for knee space, plan on about 42 to 48 in of depth.")
h3("What is a good size for a kitchen island?")
p("About 40 x 80 in is the average, and 36 x 72 in suits many medium kitchens. The best size is the biggest one that still leaves 42 to 48 in work aisles and 36 in walkways.")
h2("More Kitchen and Dining Tools")
p(f"Lighting the island? Our {a('chandelier-size-calculator','chandelier size calculator')} shows how many pendants to hang and how far apart. For the dining area, try our {a('dining-table-size-calculator','dining table size calculator')}, and see our {a('kitchen-storage-ideas','kitchen storage ideas')} for the cabinets around your island.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script.*?</script>|<style.*?</style>|<svg.*?</svg>','',html))
print(len(html.encode()),'words',len(txt.split()),'kw',txt.lower().count('kitchen island size calculator'),txt.lower().count('island'))
