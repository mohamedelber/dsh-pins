import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={"tgl":"https://www.target.com/p/storied-home-rustic-blanket-ladder-black/-/A-91789113",
"vas":"https://www.target.com/p/vasagle-blanket-ladder-decorative-farmhouse-for-the-living-room-5-tier-ladder-shelf-ladder-rack-for-storage-and-decor/-/A-1000114547",
"yam":"https://theyamazakihome.com/products/tower-leaning-ladder-rack",
"dec":"https://www.walmart.com/ip/744497143",
"lowes":"https://www.lowes.com/n/how-to/how-to-build-a-blanket-ladder",
"bask":"https://www.target.com/p/light-coiled-basket-threshold-8482/-/A-94685969",
"casp":"https://casper.com/blog/throw-blanket-size/",
"lin":"https://www.target.com/p/lucinda-rectangle-storage-ottoman-linon/-/A-89851438",
"hp":"https://www.target.com/p/tufted-storage-bench-homepop/-/A-15406613",
"hult":"https://www.ikea.com/us/en/p/hultarp-rail-black-20448773/",
"hunk":"https://www.hunker.com/2259612/blanket-storage-idea-ikea-hultarp-rail/",
"atlid":"https://www.apartmenttherapy.com/lid-organizer-for-blanket-storage-idea-37691981",
"hgb":"https://www.homesandgardens.com/solved/how-to-store-blankets",
"hgc":"https://www.homesandgardens.com/solved/how-to-store-a-comforter",
"malm":"https://www.ikea.com/us/en/p/malm-bed-frame-s39574403",
"neid":"https://www.ikea.com/us/en/catalog/products/80395248",
"skubb":"https://www.ikea.com/us/en/p/skubb-storage-case-dark-gray-10591064/",
"ster":"https://www.target.com/p/sterilite-56-qt-wheeled-under-bed-storage-container-plastic-bin/-/A-1010824823",
"riser":"https://www.walmart.com/ip/5405909905",
"trunk":"https://www.target.com/p/household-essentials-large-wooden-storage-trunk/-/A-93268477",
"cw":"https://www.closetworld.com/blog/linen-closet-organization",
"brook":"https://www.brooklinen.com/blogs/brookliving/how-to-organize-a-linen-closet",
"crl":"https://www.consumerreports.org/home-organization/how-to-organize-your-linen-closet/",
"crb":"https://www.consumerreports.org/home-garden/sheets/the-easiest-way-to-store-bedding-a3985264822",
"liv":"https://www.livingetc.com/advice/blanket-storage-ideas",
"zip":"https://www.harristeeter.com/p/ziploc-space-bag-vacuum-seal-storage-bags/0003181070424",
"puffy":"https://puffy.com/blogs/best-sleep/can-you-vacuum-seal-a-down-comforter",
"ih":"https://www.idealhome.co.uk/house-manual/storage-organisation/should-you-use-vacuum-storage-bags-for-duvets",
"ls":"https://www.livingspaces.com/inspiration/ideas-advice/how-tos/how-to-store-comforters",
"mn":"https://www.mattressnerd.com/how-to-store-a-comforter/",
"ufl":"https://edis.ifas.ufl.edu/publication/IG090/pdf",
"clem":"https://hgic.clemson.edu/factsheet/controlling-fabric-pests/",
"osu":"https://extension.oregonstate.edu/sites/extd8/files/catalog/auto/PNW606.pdf",
"umd":"https://extension.umd.edu/resource/clothes-moths",
"pend":"https://www.pendleton-usa.com/blog/caring-for-pendleton-wool-washing-dry-cleaning-and-more/",
"usfa":"https://www.usfa.fema.gov/downloads/pdf/publications/portable_heater_fire_safety_flyer.pdf"}
def SR(k,t): return ext(SRC[k],t)

p(f"The best blanket storage ideas depend on the blanket. Keep the throws you use every day within reach of the couch, in a big basket, on a leaning ladder or inside a storage ottoman. Put bulky comforters and spare blankets out of sight, under the bed, in a bench at the foot of it or on the top shelf of a closet, in breathable cotton bags. Vacuum bags save space, but most experts say not to use them for down. Below are 14 blanket storage ideas with real product sizes, the measurements to check first and how to keep stored blankets fresh.")
img(1)

h2("Measure Before You Buy")
diagram(open('z.svg').read(),"Check the clearance under your bed, the inside size of an ottoman or bench, and the gap between closet shelves before you buy storage.")
p(f"Most blanket storage fails because it is too small or does not fit the space. A standard throw is {SR('casp','50 inches wide by 60 inches tall')}, so a basket needs to be big enough to hold one or two rolled up. Under a bed, the gap is often smaller than you think: IKEA lists {SR('malm','8 1/4\"')} under its MALM frame and {SR('neid','7 7/8\"')} under its NEIDEN. On a shelf, Closet World says a folded duvet {SR('cw','needs closer to 14 to 16 inches')} of height, while many fixed shelves are about 12 inches apart.")

h2("Couch and Living Room Blanket Storage Ideas")
h3("1. A Big Basket by the Sofa")
p(f"A basket is the easiest place to drop a throw. Professional organizer Janelle Lam recommends {SR('hgb','putting them in a decorative storage basket near where you use them')}. Go big: Target's Threshold coiled basket is {SR('bask','18.1 inches')} across and about 16 inches tall, enough for two or three rolled throws. To roll one neatly, organizer Shannon Krause of Tidy Nest folds it in half lengthwise and rolls it from one end, tucking any fringe inside the first fold so it does not get damaged.")
h3("2. A Leaning Blanket Ladder")
img(2)
p(f"A ladder shows off throws and takes only a few inches of floor. Designer Artem Kropovinsky suggests {SR('hgb','ladder-style racks for a sophisticated presentation')}. Target's Storied Home ladder is {SR('tgl','72.5 inches tall')} with five rungs for $57.99, and Yamazaki's steel Tower ladder puts its rungs {SR('yam','8.25 inches')} apart. Ladders are not built for heavy loads: the VASAGLE ladder at Target is rated at {SR('vas','17.6 lb')}, so drape throws rather than stacking quilts. If the ladder slides on a hard floor, Lowe's suggests rubber pads under the feet; {SR('lowes','avoid using felt pads for this')}.")
h3("3. A Wall Rail or Wall-Mounted Ladder")
p(f"If there is no floor to spare, go up the wall. IKEA's HULTARP rail is {SR('hult','31 1/2 inches')} long for $12.99, enough for a folded throw or two, and a wall-mounted ladder works the same way: one sold at Walmart is rated for {SR('dec','20 lb')}. Screw rails into a stud or use proper wall anchors, and note that IKEA sells the screws separately. Hunker suggests adhesive hooks only for the thinnest throws.")
h3("4. A Storage Ottoman")
p(f"An ottoman hides blankets and gives you a footrest. Check the inside, not the outside: the Linon Lucinda ottoman at Target is 32 inches wide outside, but its compartment is 28.4 x 12.25 inches and {SR('lin','11.75 inches')} deep, about 2.4 cubic feet. That holds two or three folded throws.")
h3("5. A Pot-Lid Rack, Reused")
p(f"For a creative fix, Apartment Therapy's writer uses {SR('atlid','the $7.99 IKEA VARIERA Stainless Steel Lid Organizer')} on a shelf to hold folded throws upright, like files. It is cheap and keeps each blanket separate.")
h3("6. A Trunk That Doubles as a Coffee Table")
p(f"A lidded trunk can be a coffee table, a side table or a bench. Target's Household Essentials large wooden trunk is {SR('trunk','18.25\" H x 29\" W x 16.25\" D')} ($183.99). If children use the room, choose a chest with a lid support or safety hinge that stops the lid slamming shut.")

h2("Bedroom and Closet Storage for Comforters and Bulky Blankets")
h3("7. A Storage Bench at the Foot of the Bed")
img(3)
p(f"A bench at the end of the bed holds the extra blanket you add on cold nights. HomePop's tufted storage bench at Target is 40 inches wide, and its maker gives the inside as {SR('hp','37.75\"W x 15.75\"D x 9.75\"H')}, about 3.4 cubic feet, enough for a folded comforter. Our {a('small-bedroom-storage-ideas','small bedroom storage ideas')} cover other spots in a tight bedroom.")
h3("8. Under-Bed Boxes That Actually Fit")
img(4)
p(f"Measure from the floor to the lowest part of the frame. With about 8 inches to work with, a 6-inch fabric bag or Sterilite's wheeled box at {SR('ster','7 inches (H)')} will fit; IKEA's SKUBB case is {SR('skubb','7 1/2 inches')} tall, which is tight under a 7 7/8-inch frame. For more room, bed risers like the Mainstays set {SR('riser','lifts your bed by 5.25 inches')}. Lidded boxes or zipped bags keep dust off.")
h3("9. The Top Shelf of the Linen Closet")
img(5)
p(f"Brooklinen's advice is to {SR('brook','keep items rarely used')}, such as heated blankets and extra guest sheets, on the topmost shelf. Organizer Jeffrey Phillip told Consumer Reports to put bulky items {SR('crl','in soft-sided bins on an upper shelf or on the floor')}. If you can adjust the shelves, set one gap at 14 to 16 inches for comforters. Our {a('linen-closet-organization','linen closet organization')} guide has a full shelf plan.")
h3("10. Breathable Cotton Bags for Comforters and Down")
p(f"Professional organizer Ben Soreff of House to Home Organizing says to {SR('hgc','try and avoid using plastic, since our goal is always for the duvet to breathe')}. A cotton storage bag, or a spare duvet cover, keeps dust off and lets moisture out. Don't pile things on top, either: organizer Rachel-Elizabeth Mitchell advises you {SR('liv','avoid having anything on top of your down comforters')}.")
h3("11. Vacuum Bags, for Synthetics and Short Stays")
p(f"Vacuum bags do save space. Ziploc says {SR('zip','volume can be reduced by up to 75%')}. But compression is hard on natural fills. Puffy, a bedding maker, warns that {SR('puffy','repeated vacuum sealing may cause the delicate feathers to break')}, and suggests sealing down only part way, for 3 to 6 months at most. Amanda Biggs of APDO, the UK's association of professional organizers, told Ideal Home: {SR('ih','I would not recommend using vacuum bags if you have feather bedding')}. Use vacuum bags for synthetic comforters and moves, not for long-term storage of down or wool.")
h3("12. Fold It to Fit the Space")
p(f"Organizer Di Ter Avest's method for a comforter is to {SR('hgc','fold it in thirds lengthwise, then fold it again into a compact square')}. For a thinner one, Living Spaces suggests folding it in quarters, then in half. Organizer Kelly Beutler told Consumer Reports to {SR('crb','try rolling it and tying it with a ribbon')}, so rolls can stand in a basket or stack on a shelf. Our guide to {a('how-to-fold-clothes-to-save-space','folding clothes to save space')} uses the same file-fold idea for drawers.")
h3("13. Keep Fewer Blankets")
p(f"The easiest storage is less to store. Consumer Reports' rule of thumb is that {SR('crl','a bed should have two sheet sets')}: the one on it and a backup, and Brooklinen suggests capping linens at three sets per bed. Apply the same idea to blankets: one for each bed and one or two throws for the sofa. Donate the rest, or offer old ones to an animal shelter. Our guide on {a('how-to-declutter-your-home','how to declutter your home')} covers the rest of the house.")
h3("14. A Cedar Chest, With Realistic Expectations")
p(f"A blanket chest is a classic way to store bedding, and a cedar lining smells good. But extension services say it is not a moth cure: Clemson University says {SR('clem','most types of cedar chests and closets are only marginally effective')}, and the University of Florida found cedar oil can kill only small larvae. Treat cedar as a bonus, not protection, and only store blankets that are clean.")

h2("Before You Store: Clean, Dry and Away From Heat")
lst([f"<strong>Wash or clean first.</strong> The University of Florida notes that cedar and similar products {SR('ufl','only provide protection when stored materials are free from infestation')}, and it advises dry-cleaning wool before storage.",
f"<strong>Make sure it is completely dry.</strong> Mattress Nerd puts it simply: {SR('mn','having your comforter completely dry before storage is important')}. Puffy warns that {SR('puffy','moisture trapped in a sealed bag can lead to mildew or mold')}.",
f"<strong>Store wool sealed.</strong> For moths, the University of Maryland says {SR('umd','woolen articles should be cleaned and stored in sealed boxes')}, and Pendleton suggests airing and refolding wool blankets {SR('pend','every few months')}. Down and cotton are better in breathable bags.",
f"<strong>Skip the attic and basement.</strong> Julianna Melamed of Full Service Living warns that {SR('hgb','those are two places where blankets are sure to get musty')}.",
f"<strong>Keep them away from heaters.</strong> The U.S. Fire Administration says to keep space heaters {SR('usfa','at least three feet from things that can burn')}, so a blanket basket should not sit next to one."])

h2("If You Only Do One Thing")
p("Split your blankets in two: everyday throws in one big basket by the couch, and everything else clean, dry and in breathable bags on a high shelf or under the bed. Measure the space before you buy the container.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('blanket storage ideas'),'kw')
