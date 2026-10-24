import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={"bh":"https://balsamhill.com/storing-your-artificial-christmas-tree-instructions",
"bh2":"https://www.balsamhill.com/how-to-store-your-christmas-decorations",
"kc":"https://www.kingofchristmas.com/pages/tree-assembly-shaping-and-storage",
"ntc":"https://images.homedepot-static.com/catalog/pdfImages/ac/acc7fa34-739f-4a35-84d9-3e085469009b.pdf",
"nn":"https://www.nearlynatural.com/blogs/artificial-plants-and-trees-news/how-to-store-your-artificial-christmas-tree",
"rev":"https://reviewed.com/organization/features/how-store-artificial-christmas-tree",
"tt":"https://www.treetime.com/how-to-store-my-artificial-christmas-tree",
"ps":"https://www.publicstorage.com/blog/storage-tips/artificial-christmas-tree-storage.html",
"scr":"https://www.scrippsnews.com/dont-waste-your-money/dont-make-these-mistakes-taking-down-your-artificial-tree",
"hd1":"https://www.homedepot.com/p/Premium-Rolling-Red-Artificial-Tree-Storage-Bag-for-Trees-Up-to-7-5-ft-Tall-182107-S/319050334",
"hd2":"https://www.homedepot.com/p/TreeKeeper-Medium-Upright-Christmas-Tree-Storage-Bag-for-Trees-Up-to-7-5-ft-Tall-with-Rolling-Tree-Stand-TK-10105-RS/310520633",
"hs":"https://www.homeserve.com/en-us/blog/home-improvement/dangerous-attic-temperature-in-the-summer",
"uf":"https://journals.flvc.org/edis/article/download/116527/114711",
"msu":"https://extension.msstate.edu/newsletters/dawg-tracks-safety-talk/2021/controlling-mice-big-ole-rats",
"tg":"https://www.tomsguide.com/features/7-places-you-should-never-store-your-christmas-tree",
"nfpa":"https://portal.ct.gov/CFPC/_old/State-Fire-Administrator/General/NFPA-Offers-Tips-to-Keep-Holidays-Festive-and-Fire-Safe-this-Season",
"cpsc":"https://www.cpsc.gov/Newsroom/News-Releases/2011/CPSC-Gives-Consumers-a-Holiday-Home-Decorating-Safety-GuideTop-Tips-to-Prevent-Holiday-Decorating-Related-Fires-and-Injuries",
"ktvu":"https://www.ktvu.com/news/real-vs-fake-christmas-trees-what-to-buy-2025"}
def SR(k,t): return ext(SRC[k],t)

p(f"To store an artificial Christmas tree, unplug it and take off the decorations, dust it and let it dry, then take it apart from the top section down. Fold each section's branches up toward the pole, tie them loosely, and pack the sections in a storage bag with the stand in its own bag. Keep it somewhere cool and dry, such as an indoor closet, not a hot attic or a damp basement.")
p(f"Done this way, the tree comes out next December in the same shape it went in. Treated well, an artificial tree can last a long time: Balsam Hill's CEO told Scripps News that {SR('scr','proper care can help it last 10 years or more')}.")
img(1)

h2("Step 1: Unplug It, Undecorate It and Check the Lights")
p(f"Balsam Hill's first instruction is to {SR('bh','remove all décor and unplug the lights')} before you take the tree apart. On a pre-lit tree, now is the time to check the lights, while you can still see them working. Treetime suggests you {SR('tt','replace burned-out, broken, loose, or missing bulbs')} before the tree goes into storage. Look for damaged wires too: the Consumer Product Safety Commission says to check every set for broken or cracked sockets and frayed wires, and to {SR('cpsc','throw out damaged sets')}. Pack the spare bulbs and the instruction sheet with the tree so they are easy to find next year.")

h2("Step 2: Dust It and Let It Dry")
p(f"A tree that goes into a bag dusty or damp comes out musty. Nearly Natural, a maker of artificial trees, suggests you {SR('nn','use a soft cloth or microfiber duster to wipe each branch')}. Puleo, quoted by Reviewed, advises: {SR('rev','allow the tree to dry thoroughly before storing')}. If the tree stood near a humidifier or a door that let in snow, give it a day in a dry room first.")

h2("Step 3: Take It Apart From the Top Down")
p(f"Work in the reverse order you put it up. King of Christmas says to remove each section {SR('kc','starting from the top section and ending with the stand')}, and a National Tree Company manual notes that a twisting motion helps separate stiff sections. Most 6 to 8 foot trees come apart into three sections, according to Treetime; smaller trees have two, and trees of 9 feet and up have four or five. On a pre-lit tree, unplug the connectors between sections first and don't pull on the wires: King of Christmas asks you {SR('kc','not to use force or tug at the wires')}.")

h2("Step 4: Fold the Branches Up and Tie Each Section")
img(2)
p(f"Branches fold up toward the pole, the way the tree arrived. Balsam Hill says to compress the foliage with both hands before detaching each section, then {SR('bh','tie a ribbon or cord around the section')} so it stays compact. Don't overdo it. Treetime warns that {SR('tt','over-compressing branches')} makes next year's shaping harder, and pre-lit trees need extra care so bulbs don't snap. If your lights are separate strings, Public Storage advises: {SR('ps','avoid wrapping cords tightly around branches')}. Wind them around a piece of card instead.")

h2("Step 5: Pack It in a Bag, Not the Old Box")
p(f"The cardboard box the tree came in is almost impossible to close again, and Balsam Hill says such boxes are {SR('bh2','bound to deteriorate over time')}. Balsam Hill says storage bags offer better protection against heat, humidity and pests, and a rolling one is easier to move. Before you buy, check the bag against your tree and your closet:")
lst([f"<strong>Rolling duffel bags</strong> hold a tree taken apart. A Home Depot listing for a bag for trees up to 7.5 feet gives {SR('hd1','H 51 in, W 15.5 in, D 23.5 in')}.",
f"<strong>Upright bags</strong> zip over the tree while it is still assembled, but they are big: a TreeKeeper bag for trees up to 7.5 feet measures {SR('hd2','H 89 in, W 50 in, D 30 in')}.",
"<strong>Big trees</strong> can go in two bags. Balsam Hill suggests putting the odd-numbered sections in one and the even-numbered sections in the other, so neither bag gets too heavy."])
diagram(open('z.svg').read(),"A duffel bag on end needs the least floor space; an upright bag keeps the tree assembled but needs about 89 inches of height.")
p(f"Put the largest section in first, as King of Christmas suggests, and don't force the zip. Balsam Hill's CEO told Scripps News: {SR('scr','don\'t smash it in so tight that it puts stress on the wires')}. Keep the stand and its bolt in a separate small bag so the metal doesn't crush the branches.")

h2("Step 6: Choose a Cool, Dry Spot")
img(3)
p(f"Where you keep the tree matters as much as how you pack it. A National Tree Company manual says to store it {SR('ntc','in a cool, dry location protected from sunlight')}, and Nearly Natural says to avoid damp basements and hot attics, because heat can cause lights to fail or branches to lose their shape. HomeServe says an attic {SR('hs','can reach 150 degrees Fahrenheit')} in summer. Balsam Hill notes that damage from excessive heat or humidity in storage is not covered by its warranty.")
lst([f"<strong>Best:</strong> an indoor closet. Tom's Guide calls it {SR('tg','the ideal environment to store your tree')}. Stand the bag on end at the back, on a low shelf or platform off the floor.",
f"<strong>Basement:</strong> only if it is dry. The University of Florida extension advises keeping indoor humidity {SR('uf','below 60% relative humidity')}, ideally 30 to 50%.",
f"<strong>Garage or shed:</strong> watch for mice. Mississippi State University Extension says rodents {SR('msu','will gnaw on wiring of any kind')}, which is bad news for a pre-lit tree."])
img(4)
p(f"If a closet is too small, look at the space under the stairs or at the back of a coat closet. Our {a('under-stairs-storage-ideas','under stairs storage ideas')} and {a('coat-closet-organization','coat closet organization')} guides show how to make room, and our {a('christmas-decoration-storage','Christmas decoration storage')} ideas cover the ornaments, lights and wreaths.")

h2("Step 7: Next Year, Fluff and Check Before You Plug In")
p(f"When the tree comes out, assemble it and shape the branches from the bottom up. King of Christmas says to separate and shape each tip {SR('kc','beginning from the bottom')}, starting with the inner tips. Before you switch the lights on, follow the National Fire Protection Association's advice to {SR('nfpa','replace any string of lights with worn or broken cords')} or loose bulb connections, and connect no more than three strands of mini string sets. When it is time to buy a new tree, the NFPA says to choose one labeled, certified or identified by the manufacturer as fire retardant. Our {a('christmas-tree-lights-calculator','Christmas tree lights calculator')} works out how many lights a tree needs.")

h2("Storing an Artificial Tree: Quick Answers")
h3("Is it better to store a Christmas tree in a box or a bag?")
p("A bag. Cardboard boxes break down, are hard to close once the branches have been fluffed, and let in damp and pests. A zippered storage bag with handles or wheels protects the tree better and is easier to carry.")
h3("How long does an artificial Christmas tree last?")
p(f"Owners keep an artificial tree for {SR('ktvu','an average of 10 years')}, according to the American Christmas Tree Association figures reported by KTVU. Pre-lit trees may last a little less, because the lights wear out first.")
h3("How can I store a Christmas tree without a box?")
p("Fold and tie each section, then wrap it in an old sheet or put it in a heavy-duty bag, and keep the stand separate. Store it on end at the back of a closet, off the floor and away from heat.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('store an artificial christmas tree')+html.lower().count('storing an artificial'),'kw')
