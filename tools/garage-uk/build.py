import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={
"hb":"https://www.homebuilding.co.uk/advice/garage-size",
"rac":"https://hub.1stcentralinsurance.com/?p=4455",
"hse":"https://www.hse.gov.uk/fireandexplosion/petrol-storage-club-association.htm",
"nfcc":"https://nfcc.org.uk/wp-content/uploads/2023/09/NFCC_Guidance_E-bikes_and_Scooters_.pdf",
"lfb":"https://www.london-fire.gov.uk/safety/e-bikes-and-e-scooters/how-to-charge-e-bikes-and-e-scooters-safely/",
"bror":"https://www.ikea.com/gb/en/p/bror-shelving-unit-black-s39272655/",
"sfp":"https://www.screwfix.com/p/essentials-5-tier-plastic-garage-shelving-unit-1200mm-x-400mm-x-1850mm/740VM",
"sfs":"https://www.screwfix.com/p/rb-boss-fastlok-udl-galv-5-tier-metal-garage-shelving-unit-1200mm-x-450mm-x-1800mm/773tw",
"gpo":"https://www.garagepride.co.uk/blog/post/overhead-garage-storage",
"gpb":"https://www.garagepride.co.uk/blog/post/garage-bike-rack",
"bar":"https://www.barratthomes.co.uk/Help--support/Outside-your-home/Your-garage/",
"paint":"https://www.homebuilding.co.uk/paint/does-paint-freeze",
"crp":"https://communityrepaint.org.uk/news_and_stories/how-should-i-store-my-leftover-paint/",
"nid":"https://nidirect.gov.uk/articles/keeping-children-safe-poisonous-substances",
"police":"https://www.avonandsomerset.police.uk/crime-prevention-advice/home-protection/garage-or-shed-security/",
"harrow":"https://www.harrow.gov.uk/downloads/file/32472/Guidance_Notes_fire_safety_in_dwelling_houses.pdf"}
def SR(k,t): return ext(SRC[k],t)

p(f"The best garage storage ideas get everything off the floor and onto the walls: sturdy shelving with lidded boxes down one side, bikes and garden tools hung on the other, and a pegboard above a bench at the back. Do that and even a cluttered single garage can usually hold the family's kit with a clear path down the middle.")
p(f"First, be realistic about the car. Homebuilding says most UK single garages are {SR('hb','around 2.4m wide by 4.9m long')}, while a family car such as a Ford Focus is about 2 metres wide including mirrors, and you need 80 to 100 cm on each side to open the doors. That is why so many British garages end up as storerooms. The 10 ideas below are grouped by wall, with prices and the safety rules that matter in a garage.")
img(1)

h2("Will a Car and Storage Both Fit?")
diagram(open('z.svg').read(),"In a typical 2.4 x 4.9 m single garage, a 2 m wide car leaves room only for a shallow rack at the back. Without a car, the whole garage can be used for storage.")
p(f"If you do want to park inside, keep storage to the back wall and above the bonnet, and leave the sides clear. If the garage is a storeroom, use the plan on the right: deep shelving on one long wall, bikes and tools on the other, and a bench at the back. For a garage that is becoming a den instead, see our {a('garage-man-cave-ideas','garage man cave ideas')}.")

h2("Garage Storage Ideas for the Side Walls")
h3("1. Choose Shelving Rated for the Load")
img(2)
p(f"Freestanding shelving does most of the work in a garage. Check the load per shelf, not just the price. At the time of writing, Screwfix lists a five-tier plastic unit at £49.99 rated at {SR('sfp','60 kg per shelf')}, and a galvanised steel five-tier unit at £85.99 rated at 450 kg per shelf, which Screwfix says {SR('sfs','must be securely attached to the wall')}. IKEA's BROR unit (85 x 55 x 110 cm) was £80 on offer at the time of writing, down from £95, and IKEA says it {SR('bror','must be securely anchored')}. Fix every tall unit to the wall, and keep the heaviest things on the lowest shelves.")
h3("2. Put Everything in Matching Lidded Boxes")
p(f"Garages get damp. Barratt Homes tells buyers a garage should be {SR('bar','only used for things that would be unaffected by wet conditions')}, so cardboard boxes are a poor choice. Clear plastic boxes with lids keep out dust and damp, stack neatly on shelves and let you see what is inside. Keep the bottom shelf a few centimetres off the floor so air can move underneath. Our guide to {a('christmas-decoration-storage','storing Christmas decorations')} shows how to pack seasonal boxes.")
h3("3. Hang Bikes Vertically")
img(3)
p(f"Bikes take up floor space for most of the year. Hanging them by the front wheel on wall hooks means each one needs only about {SR('gpb','30cm of wall width per bike')}, according to GaragePride. E-bikes often weigh 20 to 30 kg, so GaragePride suggests a rack rated to at least 40 kg per bike, fixed into solid wall or timber studs. For security, Avon and Somerset Police advise you to {SR('police','use a ground anchor')} so bikes cannot be easily removed. See our {a('storage-ideas-for-small-spaces','storage ideas for small spaces')} for more wall-mounted solutions.")
h3("4. Give Garden Tools a Wall Rail")
img(5)
p("Long-handled tools fall over when they lean in a corner. A wall rail with a clip for each tool keeps spades, rakes and brooms upright and off the floor, with the heads at the top so nobody steps on a rake. A wall bracket for the hose and a shelf for gloves, seeds and twine complete the gardening corner.")

h2("Garage Storage Ideas for the Back Wall")
h3("5. Build a Workbench With a Pegboard Above")
img(4)
p(f"A pegboard turns the wall above a bench into tool storage you can see at a glance. Hang each tool on its own hook and draw round it with a marker if you want everyone to put things back in the same place. Small jars or tubs on a narrow shelf hold screws and wall plugs. If you only have room for a narrow bench, a fold-down one saves floor space; our {a('diy-floating-shelves','floating shelves guide')} covers fixing shelves to a wall.")
h3("6. Use the Space Above a Parked Car")
p(f"If you park inside, the back wall above the bonnet can still take a shallow shelf or wall rack. Ceiling racks are another option, but be careful: GaragePride says overhead racks {SR('gpo','must be fixed into the ceiling joists')}, not plasterboard, and typical racks are rated for about 100 to 250 kg in total. They also need enough headroom (GaragePride suggests 2.1 m) to clear the car. Garage roof structures are not always designed for extra weight, so check with a builder or structural engineer before loading the ceiling.")

h2("Keep It Safe")
h3("7. Store Paint and Chemicals Properly")
p(f"Paint does not like cold garages. Paint expert James Knighton, quoted by Homebuilding, advises storing it {SR('paint','somewhere dry, frost-free and temperature-stable')}, ideally between 5 and 20°C, and Community RePaint suggests avoiding the shed or garage if it drops below freezing. Keep chemicals in their {SR('nid','original, labelled containers')} on a high shelf, as nidirect advises, and lock the garage if children could get in.")
h3("8. Follow the Petrol Rules")
p(f"The Health and Safety Executive says you can keep {SR('hse','up to 30 litres of petrol at home')} without notifying your local Petroleum Enforcement Authority, in plastic containers of up to 10 litres or metal ones of up to 20 litres. If the store is not in the open air, HSE says it needs {SR('hse','a direct exit to the open air and ventilation')} to that exit. Petrol must not be kept in living accommodation, so an integral garage needs care: keep cans away from any heat source and from the door into the house.")
h3("9. Charge E-Bikes and Scooters Safely")
p(f"Many people store e-bikes and e-scooters in the garage. The National Fire Chiefs Council recommends {SR('nfcc','heat alarms rather than smoke detectors')} in garages and advises against charging batteries while you are asleep or away. The London Fire Brigade also says to fit an alarm where you charge and to use the correct charger. If your garage is attached to the house, the door between them should be a self-closing fire door; council guidance based on the Building Regulations describes an {SR('harrow','FD30S (E30Sa) self-closing fire door')} with smoke seals. Many older homes do not have one, so check yours and never prop it open.")

h2("Keep It Tidy")
h3("10. Do a Twice-Yearly Clear-Out")
img(6)
p(f"This before and after illustration shows what clearing the floor can do for a single garage. The hardest part is deciding what to keep, so empty one wall at a time, sort into keep, sell, donate and tip, and only buy storage once you know what is left. Our {a('how-to-declutter-your-home','decluttering guide')} walks through the process, and a quick tidy every spring and autumn stops the pile coming back.")

h2("If You Only Do One Thing")
p(f"Of all these garage storage ideas, getting the floor clear matters most. A fixed shelving unit, a few lidded boxes and two bike hooks will make more difference than any other change, and the shelving prices above show it need not cost much. Then add a pegboard and garden tool rail as you go. If your garage is also your laundry, our {a('small-utility-room-ideas','small utility room ideas')} show how to plan a washer and dryer in a small space.")
ai_note()
html='\n\n'.join(out)
html=re.sub(r'(\d+\.\d{2})\d+',r'\1',html)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('garage storage ideas'),'kw')
