import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={"wren":"https://www.wrenkitchens.com/blog/do-you-have-room-for-a-kitchen-island",
"wrens":"https://www.wrenkitchens.com/kitchen-design/small-kitchen-ideas/how-to-include-an-island-in-your-small-kitchen-design",
"lesm":"https://www.livingetc.com/amp/spaces/interior-inspiration/small-kitchen-island-ideas-240821",
"hbc":"https://www.homebuilding.co.uk/advice/minimum-amount-of-space-required-around-a-kitchen-island",
"hbs":"https://www.homebuilding.co.uk/advice/minimum-kitchen-island-size",
"ihs":"https://www.idealhome.co.uk/kitchen/kitchen-ideas/small-kitchen-island-ideas-296888",
"ihc":"https://www.idealhome.co.uk/kitchen/kitchen-advice/space-between-counter-and-island-299178",
"forh":"https://www.ikea.com/gb/en/p/-80035920/",
"torn":"https://www.ikea.com/gb/en/p/-40391657/",
"vad":"https://www.ikea.com/gb/en/p/-20359154/",
"dun":"https://www.dunelm.com/product/francis-kitchen-island-1000296337",
"range":"https://www.therange.co.uk/furniture/dining-room-furniture/kitchen-trolleys-and-islands-on-wheels/kitchen-island-with-drop-leaf",
"metod":"https://www.ikea.com/gb/en/p/-10205628/",
"diyk":"https://advice.diy-kitchens.com/customer-questions/design-island-feature/",
"pen":"https://www.livingetc.com/advice/peninsula-vs-island",
"maxi":"https://www.ikea.com/gb/en/p/metod-maximera-base-cb-2-frnts-2-low-1-md-1-hi-drw-white-upploev-matt-anthracite-s69493127",
"ihst":"https://www.idealhome.co.uk/kitchen/kitchen-decor/kitchen-island-storage-ideas",
"hgst":"https://www.homesandgardens.com/kitchens/kitchen-island-storage",
"hall":"https://www.ikea.com/gb/en/p/-s39308923",
"naked":"https://www.nakedkitchens.com/blog/the-kitchen-expert/breakfast-bars-and-stations-design-inspiration-and-expert-tips",
"dfs":"https://help.dfs.co.uk/hc/en-gb/articles/48709523371793-Barstools",
"niceic":"https://www.niceic.com/householders/kitchens-and-electrics-what-you-need-to-know/",
"adp":"https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/441872/BR_PDF_AD_P_2013.pdf",
"hbhob":"https://www.homebuilding.co.uk/advice/should-you-have-a-hob-on-a-kitchen-island",
"mjq":"https://www.myjobquote.co.uk/costs/moving-a-kitchen-sink",
"tala":"https://tala.co.uk/blogs/lighting-guide/how-high-should-pendant-lights-hang-over-a-kitchen-island",
"lec":"https://www.livingetc.com/advice/cost-of-a-kitchen-island",
"ihcost":"https://www.idealhome.co.uk/kitchen/how-much-does-a-kitchen-island-cost-304393"}
def SR(k,t): return ext(SRC[k],t)

p(f"The best kitchen island ideas for a small kitchen start with the walkway, not the worktop: you need about 1 metre of clear floor on every side, which means a fitted island usually wants a room around 4 metres wide. If you have less, a trolley on castors, a drop-leaf island, a slim 60 cm prep island or a peninsula gives you most of the benefit in less space. Whatever the size, make the island earn its place with deep pan drawers, a bin pull-out and shelves on the seating side. Below are 12 kitchen island ideas for UK homes, with real sizes, prices and the storage each one adds.")
img(1)

h2("Do You Have Room for a Kitchen Island?")
diagram(open('z.svg').read(),"With 60 cm units on both walls and 1 m walkways, a slim prep island needs a room about 3.8 m wide; one with stools needs about 4.3 m.")
p(f"Wren's {SR('wren','rule of thumb is a 1 metre clearance zone')} around an island, and Melissa Klink of Harvey Jones says {SR('lesm','the walkways around an island need to be at least 100cm wide')}. If two people cook at once, Homebuilding says {SR('hbc','a minimum clearance of 1.2m will allow multiple people to move around comfortably')}. As for the island itself, Lizzie Beesley of Magnet told Ideal Home that {SR('ihs','the minimum size of a kitchen island is 1000mm x 1000mm')}, though a butcher's block can be smaller. Our {a('kitchen-island-size-calculator','kitchen island size calculator')} works out what fits your room.")

h2("Small Kitchen Island Ideas")
h3("1. A Butcher's Trolley on Wheels")
img(2)
p(f"The cheapest island is one that moves. IKEA's FÖRHÖJA kitchen trolley is 100 cm long and 43 cm deep, costs {SR('forh','£129')}, and has two drawers plus open shelves with {SR('forh','space for 9 bottles on each shelf')}. Helen Parker of deVOL told Livingetc: {SR('lesm','there is something really quite pleasing about a movable piece of furniture')}. Lock the castors when you chop, and roll it against a wall when you need the floor.")
h3("2. A Freestanding Island With Shelves")
p(f"A ready-made island needs no fitting and comes with you when you move. IKEA's TORNVIKEN is {SR('torn','126x77 cm')} for £379, with open shelves underneath; its VADHOLMA comes in a large {SR('vad','126x79x90 cm')} version for £579; and Dunelm's Francis, at 123 x 75 cm and {SR('dun','£349')}, adds a drawer and twin cupboards. Stephanie Nix of Neptune told Livingetc that {SR('lesm','including a freestanding unit is the perfect solution if you have less room')}.")
h3("3. A Drop-Leaf Island")
p(f"A drop-leaf island gives you a breakfast bar only when you need one. The Range's rolling island with a drop leaf is 65 cm wide and 107 cm long with the leaf up, costs £139.95 and has a tilt-out cabinet that {SR('range','fits a 27L trash can')}, so it handles the bin as well.")
h3("4. A Slim Prep Island")
p(f"If you cannot fit a 90 cm deep island, go narrow. Darren Watts of Wren told Ideal Home that slimline islands are {SR('ihs','narrow, yet long, these islands are purely for cooking, storage or food preparation')}. IKEA's METOD base cabinet also comes in a {SR('metod','80x37x80 cm')} version (£45), and DIY Kitchens says {SR('diyk','the average depths (front to back) of our islands are either 600mm or 900mm')}. A 60 cm deep island is the same depth as a standard base unit, so it uses ordinary cabinets. Simon Ribchester of Beams adds that {SR('lesm','a narrower island still gives you extra prep space and storage')}.")
h3("5. A Peninsula Instead of an Island")
img(5)
p(f"A peninsula is joined to your run of units at one end, so it needs a walkway on only three sides. Wren says {SR('wrens','for small kitchens, a peninsula can be much more practical than an island')}, and designer Claire Garner told Livingetc: {SR('pen','because it connects to existing cabinetry, it takes up less floor space')}. It still gives you cupboards underneath and a breakfast bar on the outside.")

h2("Storage Inside the Island")
h3("6. Build It From Base Units")
p(f"A fitted island is usually just kitchen base units set back to back. DIY Kitchens shows how a standard unit and a 300 mm shallow unit, plus doors, make a {SR('diyk','860mm + (2 x 20mm doors) = 900mm depth')} island: deep storage on the cooking side and shallow cupboards on the other. Finish the ends with end panels, and you have a fitted look from off-the-shelf units.")
h3("7. Deep Pan Drawers, Not Cupboards")
img(3)
p(f"Drawers beat cupboards in an island, because you can see everything from above. Dave Young of HUSK Kitchens told Ideal Home: {SR('ihst','we always recommend deep drawers with integrated storage systems')}. IKEA's METOD/MAXIMERA 80 cm drawer unit with two low, one medium and one high drawer costs {SR('maxi','£330')}. Anthony Earle of Artichoke told Homes &amp; Gardens that {SR('hgst','for deeper pan drawers, incorporating a slim internal drawer for lids is quite clever')}. Our guide to {a('how-to-organize-kitchen-drawers','organising kitchen drawers')} covers what goes where.")
h3("8. Hide the Bin in the Island")
p(f"The bin is the hardest thing to place in a small kitchen, and the island is often the best spot, close to the prep area. Fred Horlock of Neptune told Homes &amp; Gardens that {SR('hgst','concealed trash storage is a brilliant use of storage on the island')}. IKEA's HÅLLBAR waste-sorting insert, four 10-litre bins for a METOD drawer, costs {SR('hall','£41')}.")
h3("9. Use the Seating Side Too")
img(4)
p(f"The back of an island is often wasted. Caroline Levenson told Homes &amp; Gardens that it {SR('hgst','can be a great place for shallow storage')}, and Tom Howley suggests {SR('ihst','open shelving on which you can display your favourite pottery, cookery books')} and more. Keep everyday working storage on the cooking side and seasonal or rarely used things behind the stools.")
h3("10. Put the End Panel to Work")
p(f"The short end of an island can take a slim wine rack, a cookbook ledge or a rail. Melissa Klink of Harvey Jones suggests {SR('ihst','a hanging rail for hand towels and tea towels')}, and Homes &amp; Gardens notes that a single column can hold {SR('hgst','five to six bottles')}. Our {a('kitchen-storage-ideas','kitchen storage ideas')} have more ways to use narrow gaps.")

h2("Seating, Power and Light")
h3("11. A Breakfast Bar Overhang")
p(f"For stools, let the worktop overhang the seating side. Matt Baker of Harvey Jones told Ideal Home that {SR('ihc','you will need around 30cm of worktop overhang')}; much more than that needs legs or brackets, and DIY Kitchens says a 20 mm worktop can overhang only 250 mm unsupported. Naked Kitchens suggests you {SR('naked','allow at least 60cm per stool for comfort')}. At a standard 90 cm worktop, DFS recommends a counter stool with a 60 to 65 cm seat, and for a breakfast bar of {SR('dfs','around 100–110cm high')}, a 70 to 75 cm seat.")
h3("12. Power, a Hob or a Sink, With Care")
p(f"Sockets on an island are useful, but plan them early. NICEIC says {SR('niceic','all socket-outlets in kitchens must be protected by a residual current device (RCD)')}, and that sockets should be at least 30 cm from a sink. A new circuit is notifiable building work in England under {SR('adp','Approved Document P')}, so use a registered electrician. A hob is harder: on a small island Christopher Proudfoot warns {SR('hbhob','an overhead extractor may not be feasible, so a downdraft system might be necessary')}, and Emily Pickett of Kitchens by Holloways suggests you {SR('lesm','keep the top of a smaller island clear of sinks or hobs too')}. Moving a sink into an island costs about £800 to £1,100 on a timber floor and £1,100 to £1,600 on concrete, according to {SR('mjq','MyJobQuote')}.")
p(f"Light it with pendants: UK lighting maker Tala suggests hanging them {SR('tala','70–80cm (28–32 inches) above the countertop surface')}, about 60 to 75 cm apart. Our {a('chandelier-size-calculator','chandelier size calculator')} helps size the shades.")

h2("What a Kitchen Island Costs")
lst([f"<strong>Trolley or drop-leaf island:</strong> about £130 to £140 for the IKEA and The Range examples above.",
f"<strong>Freestanding island:</strong> £349 to £579 for the Dunelm and IKEA examples; Livingetc puts a non-bespoke timber or steel island at {SR('lec','around £500 to £1,500')}.",
f"<strong>Fitted island:</strong> Ideal Home says {SR('ihcost','somewhere between £1,000-£4,500')}, and bespoke islands {SR('ihcost','upwards of £5,000')}.",
"<strong>Extras:</strong> plumbing, electrics and extraction add to that, so get quotes before you commit."])

h2("If You Only Do One Thing")
p(f"Mark the island's outline on the floor with masking tape and live with it for a week. If you can open the dishwasher, the oven and the fridge and still walk past, it fits; if not, choose a trolley or a peninsula instead. Charlie Smallbone's advice to Livingetc says it best: {SR('lesm','and if you don\'t have the room, don\'t force it')}.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('kitchen island ideas'),'kw')
