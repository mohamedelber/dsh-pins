import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={"sq":"https://squote.app/knowledge/carpentry/alcove-cupboard-and-shelving-installation",
"liv":"https://www.livingetc.com/advice/how-deep-should-bookshelves-be",
"bab":"https://www.bookabuilderuk.com/blog/arched-alcove-ideas-shelving-paint-colours",
"hbr":"https://www.homebuilding.co.uk/rooms/living-room/living-room-alcove-ideas",
"hun":"https://www.hunker.com/13403530/what-is-the-average-space-between-shelves-on-a-bookshelf",
"hg1":"https://homesandgardens.com/solved/how-to-install-shelves-in-an-alcove",
"hg2":"https://homesandgardens.com/interior-design/alcove-shelf-ideas",
"mb":"https://www.mybuilder.com/questions/v/68823/what-s-the-thinnest-an-alcove-bookshelf-be",
"pd":"https://www.practicaldiy.com/carpentry/shelving/shelving-alcove.php",
"w120":"https://www.wickes.co.uk/Floating-Shelf-Pair---Supporting-Rod-120x12mm-thick/p/249892",
"w140":"https://www.wickes.co.uk/Floating-Shelf-Supporting-Bracket-Pair---140-x-14mm/p/249893",
"wts":"https://www.wickes.co.uk/Twin-Slot-Antique-Brass-Shelving-Bracket---320mm/p/249769",
"we":"https://worktop-express.co.uk/oak-solid-wood-floating-shelf-900mm-x-200mm-x-30mm",
"uh":"https://ultimatehandyman.co.uk/how-to/k9q",
"pe":"https://professional-electrician.com/?p=17329",
"hbw":"https://www.homebuilding.co.uk/advice/how-to-avoid-drilling-into-wires",
"bosch":"https://www.bosch-diy.com/gb/en/all-about-diy/drill-more-safely",
"red":"https://www.redbridge.gov.uk/planning-and-building/building-control/chimney-breasts-removal",
"sw":"https://www.stoveworlduk.co.uk/wood-burner-distance-from-combustible-materials-explained",
"or":"https://www.officereality.co.uk/blog/what-is-the-average-desk-height",
"fci":"https://fcilondon.co.uk/blog/how-deep-should-built-in-wardrobes-be",
"b40":"https://www.ikea.com/gb/en/p/billy-bookcase-blue-40594928/",
"b80":"https://www.ikea.com/gb/en/p/-00263850/",
"b106":"https://www.ikea.com/gb/en/p/-30263844/",
"sb":"https://www.diy.com/departments/scaffold-board-l-2-4m-w-0-23m-t-38mm-pack-of-3/5022652847289_BQ.prd",
"livi":"https://www.livingetc.com/ideas/alcove-shelving-ideas",
"sl":"https://www.simplelighting.co.uk/blog/how-to-calculate-power-requirements-for-led-strip-lights/"}
def SR(k,t): return ext(SRC[k],t)

p(f"The best alcove shelving ideas make the most of the recesses either side of a chimney breast without fighting their odd sizes. For most homes, the winner is a low cupboard with three or four shelves above it: closed storage for clutter, open shelves for books. If your budget is small, oak floating shelves or simple shelves on battens look almost as good for a fraction of the cost. Alcoves in pre-1930s UK terraces and semis are {SR('sq','typically 300–450mm')} deep, but yours may differ, so measure first; the ideas below are grouped by budget, with the sizes that make each one work.")
img(1)

h2("Alcove Shelving, Measured")
diagram(open('z.svg').read(),"An example 100 cm alcove with a cupboard below and shelves about 30 cm apart, and how shelf depths compare with a typical 300–450 mm alcove.")
p(f"Three numbers matter most. For depth, interior designer Noz Nozawa, quoted by Livingetc, suggests at least 9 inches (about 23 cm) for novels and {SR('liv','a nice middle-ground is 12')} inches (about 30 cm) for a mix of books and objects. For spacing, {SR('hun','Hunker')} puts the average gap between bookshelves at 8 to 12 inches (about 20 to 30 cm). For span, the UK trade guide {SR('sq','Squote')} says 18 mm MDF sags visibly at around 600 to 700 mm under a moderate load, and nearer 500 to 600 mm under books, so in a wider alcove use 25 mm boards and a support in the middle, or battens along the back. Our {a('shelf-spacing-calculator','shelf spacing calculator')} works out the gaps for your alcove's height.")

h2("Under £100: Simple DIY Alcove Shelves")
h3("1. Oak Floating Shelves on Hidden Brackets")
img(2)
p(f"Floating shelves keep an alcove light and modern. A 900 x 200 x 30 mm solid oak shelf from Worktop Express costs £39 each, so two shelves stay well under £100, but the retailer warns that {SR('we','they should not be fitted to plasterboard')} or internal walls, so check that your alcove walls are solid masonry first. If you make your own, Wickes' 140 mm hidden bracket pair costs £4.50 and is rated for {SR('w140','up to 50kg per pair')}, for shelves at least 30 mm thick and up to 300 mm deep, spaced no more than 500 mm apart on brick. Our {a('diy-floating-shelves','DIY floating shelves')} guide covers the fitting.")
p("<strong>Works best:</strong> alcoves up to about a metre wide with solid walls. <strong>Skip it:</strong> for heavy rows of hardbacks, which are better on battens.")
h3("2. Shelves on Battens, Three Sides")
p(f"The traditional way to shelve an alcove is to fix a timber batten to the back wall and both side walls, then rest the shelf on top. Practical DIY suggests ordinary {SR('pd','planed timber, 50x18mm')}, for the battens, with the side battens cut about 38 mm shorter than the shelf depth so they're hidden from the front. Space the fixings no more than about 450 mm apart for light loads and no more than 300 mm for heavy ones, using screws that go at least 38 mm into the wall. Because the shelf is held on three sides, this is the strongest cheap option for books.")
p(f"<strong>Tip:</strong> Archer Furniture, a furniture maker answering on MyBuilder, says {SR('mb','heavy books are best toward the ends')} of alcove shelves, not in the middle, where shelves sag.")
h3("3. Adjustable Twin-Slot Shelving")
p(f"If your books keep changing, twin-slot uprights let you move shelves without drilling new holes; if you rent, check your tenancy first. Wickes' 320 mm twin-slot bracket costs £4.50 (uprights are sold separately) and has a {SR('wts','maximum weight loading of 24kg per bracket')}, with shelves up to 450 mm deep. Paint the uprights the wall colour and they almost disappear.")
p("<strong>Works best:</strong> home offices and kids' rooms. <strong>Skip it:</strong> if you want a built-in look.")
h3("4. Scaffold Board Shelves")
p(f"Chunky, rustic and cheap, scaffold boards are about 38 mm thick, so they don't sag easily. B&amp;Q sells them in packs of three at {SR('sb','2.4m x 22.5cm x 38mm')}, so one board makes two shelves for a 1 m alcove. Sand them well and seal them before use, and fix them on battens or heavy-duty brackets.")

h2("£100 to £500: Smarter Shelving and Lighting")
h3("5. An IKEA BILLY Hack")
p(f"IKEA's BILLY is 28 cm deep, which fits most alcoves. Two narrow {SR('b40','40x28x202 cm')} bookcases (£50 each) can fill a 90 cm alcove, or a wide 80 cm version costs £55. For a cupboard-below look, use the low {SR('b106','80x28x106 cm')} BILLY (£35) as a base with shelves or a second unit above, then fill the gaps at the sides and top with painted timber so it looks built in. Anchor every unit to the wall, as IKEA instructs.")
h3("6. Lit Shelves Against a Dark Back Wall")
img(6)
p(f"Painting the back of an alcove a deep colour turns ordinary shelves into a display. Livingetc says {SR('livi','dark paint works well in alcoves')} because it makes the colours of the objects in front stand out. Add low-voltage LED strips under each shelf: Bookabuilder suggests warm white around 2700K to 3000K for living spaces, and puts the cost of supplied and fitted shelf lighting at £80 to £200 per alcove, not counting any electrical upgrades. Most strips run at 12 V or 24 V, and Simple Lighting advises you to {SR('sl','match the driver\'s output voltage')} to the strip. Have an electrician wire anything that isn't plug-in.")
h3("7. A Drinks or Display Alcove")
p(f"An alcove in a dining room makes a neat built-in bar. Builder Samuel Anton, quoted by {SR('hbr','Homebuilding &amp; Renovating')}, gives minimums of 300 to 350 mm deep, with around 300 mm between shelves for bottles and 200 to 250 mm for glasses. A ready-made base cupboard below hides spare bottles and the shelves above show off glassware.")

h2("Bespoke: Built-In Alcove Storage")
h3("8. Cupboards Below, Shelves Above")
img(3)
p(f"This is the classic for good reason. Designer Tom Rutt of TR Studio told Homes &amp; Gardens that making {SR('hg2','the lower shelving deeper')} created practical internal storage, with shallower open shelves above. Bookabuilder puts bespoke alcove joinery at {SR('bab','between £1,200 and £3,000 per side')}, depending on materials and finish, and built-in timber shelving alone at £150 to £400 per alcove, depending on the number of shelves and finish. Paint the units the same colour as the walls for a calm, built-in look, or a contrast colour to make them a feature.")
h3("9. An Alcove Desk")
img(4)
p(f"A spare bedroom alcove is often exactly the right width for a desk. Fit a solid worktop wall to wall on battens, with one or two shelves above. UK office furniture sellers put standard desk height at {SR('or','between 69cm and 71cm')}, and our {a('desk-height-calculator','desk height calculator')} adjusts that for your own height. Keep the shelves above the desk shallow so you don't hit your head when you stand up.")
h3("10. An Alcove Wardrobe")
img(5)
p(f"In a bedroom, an alcove can hold a fitted wardrobe, but check the depth first. FCI London says the {SR('fci','standard answer is 600mm minimum')} for a hanging rail, with 650 to 680 mm ideal. Most alcoves are shallower than that, so an alcove wardrobe usually stands forward of the chimney breast. If you don't want that, use the alcove for folded clothes on shelves behind doors, which needs less depth. Our {a('built-in-wardrobe-ideas','built in wardrobe ideas')} have UK measurements for every type.")

h2("Before You Drill")
lst([f"<strong>Find the cables.</strong> Wiring regulations guidance says cables can run {SR('pe','within 150mm from the top of the wall')} and from corners, and horizontally or vertically in line with sockets and switches, so don't drill directly above, below or beside them. Older wiring doesn't always follow these rules, so check the whole area. Bosch notes that {SR('bosch','a cable must have a current')} to be picked up by a detector, so scan with the power on, then switch it off at the consumer unit before you drill.",
f"<strong>Know your wall.</strong> Brick takes plugs and screws; on a stud or lath and plaster wall, fix heavy shelving into the timber studs, as {SR('uh','Ultimate Handyman')} advises.",
f"<strong>Leave the chimney breast alone.</strong> Redbridge Council says removing all or part of one needs {SR('red','an application to Building Control')}, and damaging the brickwork between flues can let carbon monoxide in from a neighbour's flue.",
f"<strong>Keep timber clear of a stove.</strong> Stove World UK says the safe distance to combustible materials such as a wooden bookshelf {SR('sw','can be anywhere between 300-600mm+')}, depending on the stove's output, so check the manufacturer's figure and ask a HETAS-registered installer."])

h2("How Deep Should Alcove Shelves Be?")
p(f"Whichever of these alcove shelving ideas you choose, the depth rule is the same. For books, 200 to 250 mm; for media or storage, 300 to 400 mm, according to Bookabuilder. Older UK alcoves are typically 300 to 450 mm deep, so a 250 to 300 mm shelf sits a little back from the face of the chimney breast and looks neat. Once your shelves are up, our {a('shelf-decor-ideas','shelf decor ideas')} and {a('bookshelf-decor-ideas','bookshelf decor ideas')} show how to style them without clutter.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('alcove shelving ideas'),'kw')
