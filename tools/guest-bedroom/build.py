import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={"dim":"https://www.dimensions.com/element/queen-bedroom-layouts",
"mat":"https://www.sleepfoundation.org/mattress-information/mattress-sizes",
"smoke":"https://www.villageofpennyan.gov/uploads/1/2/3/8/123892065/nfpa-smoke-alarms.pdf",
"co":"https://www.cpsc.gov/s3fs-public/Quarter_Pg_CO_Alarms_10-22-14.pdf",
"egress":"https://billingsmt.gov/DocumentCenter/View/4693",
"temp":"https://www.sleepfoundation.org/bedroom-environment/best-temperature-for-sleep",
"sheets":"https://www.sleepfoundation.org/bedding-information/how-often-should-you-wash-your-sheets"}
def SR(k,t): return ext(SRC[k],t)
p("The best guest bedroom ideas make visitors feel at home from the moment they put their bag down: a comfortable bed, a light by the pillow, somewhere to unpack and a few small touches that say you thought about them. You do not need a big room or a big budget, just a plan.")
p("This guide shows you what size bed fits your spare room, a 6-step setup and 18 guest bedroom ideas for essentials, small rooms, guest room offices and decor. Many of them use things you already own, and every idea works in a small guest bedroom.")
img(1)
summary(["<strong>Quick answer:</strong> Start with the best bed the room can take, with at least 30 in of walking space around it. Add a nightstand with a lamp, a water carafe and a charger, a luggage rack with fresh towels, and some empty closet space. Finish with blackout curtains, an extra blanket and a calm color palette.",
"In a small room, a full, twin or daybed often works better than a squeezed-in queen.",
"Install a smoke alarm inside the guest room, and check that the window opens wide enough to serve as an escape route if you are turning another room into a bedroom."],
"<strong>Time:</strong> a weekend · <strong>Cost:</strong> about $50 to $300 if you already have a bed · <strong>Difficulty:</strong> Easy")
toc("guest-bedroom-ideas")
h2("What Size Bed Fits Your Guest Room?")
p(f"The bed decides everything else, so start there. Standard US mattress sizes, as listed by the Sleep Foundation, are {SR('mat','38 x 75 in for a twin')}, 54 x 75 in for a full, 60 x 80 in for a queen and 76 x 80 in for a king. Dimensions.com recommends {SR('dim','minimum clearances of 30 inches')} around a queen bed, and 36 inches for comfort.")
diagram(re.sub(r'(\d+\.\d{1,2})\d+',r'\1',open('z.svg').read()),"What bed fits your guest room: the smallest room for a twin, full, queen or king bed with 30 in of walking space on both sides and at the foot.")
table(["Bed","Mattress size","Smallest room (30 in around)","Best for"],[
["Twin","38 x 75 in","8 ft 2 in x 8 ft 9 in","One guest, kids, small rooms"],
["Full","54 x 75 in","9 ft 6 in x 8 ft 9 in","One adult, or a couple for a night or two"],
["Queen","60 x 80 in","10 ft x 9 ft 2 in","Couples, most guest rooms"],
["King","76 x 80 in","11 ft 4 in x 9 ft 2 in","Large rooms, frequent couples"]])
p("These room sizes are our own calculation: the mattress plus 30 in on both sides and at the foot, with the headboard against a wall. They leave out the nightstand, which is why Dimensions.com puts a queen bedroom at roughly 106 sq ft. Pushing one side of the bed against a wall saves 30 in of width, which is often the best trick in a small guest bedroom.")
h2("Quick Pick: Guest Bedroom Ideas by Situation")
table(["Your situation","Best ideas","Cost"],[
["Guests arrive this weekend","#2, #4, #5, #17","Free to low"],
["Very small spare room","#7, #8, #9","Low to medium"],
["Room is also your office","#10, #11","Medium"],
["Guests stay for a week or more","#5, #6, #18","Low"],
["Want a hotel feel","#3, #4, #12, #13","Medium"]])
h2("How to Set Up a Guest Bedroom in 6 Steps")
lst(["<strong>Clear the room.</strong> Move out boxes, exercise gear and anything you store there, or give it one closed cabinet.",
"<strong>Choose and place the bed.</strong> Use the size chart above, and keep 30 in of walking space where guests get in and out.",
"<strong>Add the essentials:</strong> a nightstand or shelf on each side used, a lamp, a place to unpack and a mirror.",
"<strong>Make up the bed</strong> with clean sheets, two kinds of pillows and an extra blanket at the foot.",
"<strong>Stock the small things:</strong> towels, water, a charger, tissues and the Wi-Fi password.",
"<strong>Sleep in it yourself for one night.</strong> You will notice the squeaky bed, the light that leaks in and the missing hook."],True)
img(6)
h2("Guest Bedroom Essentials")
p("These six ideas cover what every guest needs. Get them right and the room works, even before you add any decor.")
h3("1. A Comfortable Mattress and a Protector")
p("Guests remember a bad mattress more than anything else. If the guest bed is an old one, a 2 to 3 inch mattress topper is a cheaper fix than a new mattress. Add a waterproof mattress protector so the mattress stays clean between visits.")
h3("2. Two Kinds of Pillows")
p("Put out one firm and one soft pillow per guest, so side sleepers and back sleepers can both get comfortable. Keep a spare pillow and pillowcase in the closet.")
h3("3. Layered Bedding and an Extra Blanket")
p(f"Crisp sheets, a duvet or quilt, and a folded blanket at the foot let guests adjust to the temperature. The Sleep Foundation suggests that about {SR('temp','65 degrees Fahrenheit')} is best for sleep, so a light duvet plus a blanket covers most nights. Wash the sheets after every visit; the Sleep Foundation says most people should {SR('sheets','wash their sheets once per week')} anyway.")
h3("4. A Nightstand With a Lamp, Water and a Charger")
img(5)
p("A nightstand on each side used gives guests a place for glasses, a phone and a book. Add a lamp they can switch on from bed, a carafe of water with a glass, and a phone charger plugged in and ready, so they do not have to search for an outlet.")
h3("5. A Luggage Rack and Fresh Towels")
img(2)
p("A folding luggage rack keeps the suitcase off the floor and the bed. Set a stack of towels on it or at the foot of the bed: a bath towel, a hand towel and a washcloth per guest, so nobody has to ask.")
h3("6. Empty Closet Space and Hangers")
img(4)
p(f"Leave part of the closet empty, with eight to ten matching hangers and one clear drawer or shelf. For longer stays, this is the difference between living out of a suitcase and settling in. If your linen closet needs a reset to make room, see our {a('linen-closet-organization','linen closet organization')} guide.")
h2("Small Guest Bedroom Ideas")
p(f"A small spare room can still be a lovely guest bedroom. Our {a('box-room-bedroom-ideas','tiny bedroom ideas')} go further for the tiniest rooms.")
h3("7. A Daybed or Trundle Bed")
p("A daybed works as a sofa during the day and a twin bed at night, and a trundle underneath turns it into two beds for kids or friends. It takes far less floor space than a full or queen.")
h3("8. Wall Lights Instead of Lamps")
p("Plug-in wall sconces free up the nightstand, or let you swap it for a narrow shelf. Mount them so the shade sits a little above shoulder height when you sit up in bed.")
h3("9. Storage Under the Bed")
p(f"A bed with drawers, or low bins on wheels, holds spare bedding and out-of-season clothes without taking floor space. Keep one drawer empty for guests. Our {a('small-bedroom-storage-ideas','small bedroom storage ideas')} have more ways to fit storage in.")
h2("Guest Room and Office Ideas")
p("If the guest room is also your home office most of the year, choose pieces that switch roles quickly.")
h3("10. A Daybed and Desk Combo")
img(3)
p("Put a daybed along one wall and a desk under the window, and the room works as an office every day and a guest room when you need it. Clear the desk and give guests one drawer when they arrive.")
h3("11. A Murphy Bed or Sofa Bed")
p("A wall bed or a good sofa bed gives back the whole floor for work. A wall bed must be installed securely to the wall following the manufacturer's instructions; with a sofa bed, test the mattress before you buy and leave enough room in front to unfold it.")
h2("Guest Bedroom Decor Ideas")
p("Guest room decor should feel calm and welcoming rather than personal, like a good hotel with a little more warmth.")
h3("12. A Calm, Neutral Palette")
p("White or cream bedding, one soft accent color like sage or terracotta, and natural wood suit almost every guest. Keep family photos and collections to a minimum so the room feels like theirs for a few nights.")
h3("13. Blackout Curtains")
p(f"Guests sleep in unfamiliar rooms, often in a different time zone. The Sleep Foundation notes that {SR('temp','a dark, quiet bedroom will help you set your body clock')}, so lined or blackout curtains are worth it. Our {a('curtain-size-calculator','curtain size calculator')} tells you the size to buy.")
h3("14. A Mirror and a Few Pieces of Art")
p(f"A full-length mirror is something guests always look for. Add one or two calm pieces of art at the right height; our {a('picture-hanging-height-calculator','picture hanging height calculator')} works out where to put the nail.")
h3("15. A Soft Rug by the Bed")
p(f"A rug by the bed is the first thing guests step on in the morning. Choose one big enough to reach both sides of the bed, and use our {a('rug-size-calculator','rug size calculator')} to pick the size.")
h3("16. Plants or Fresh Greenery")
p("A small plant or a few stems of eucalyptus on the nightstand make the room feel cared for. Eucalyptus has a strong scent, so swap it for low-scent greenery if a guest has allergies or asthma.")
h2("Thoughtful Touches Guests Remember")
h3("17. A Welcome Card With the Wi-Fi Password")
p("A small framed card with the Wi-Fi name and password, your house routines and the time breakfast usually happens saves your guests from asking.")
h3("18. A Basket of Small Essentials")
p("A basket or tray with a spare toothbrush, toothpaste, travel-size toiletries, earplugs, a sleep mask and a few snacks covers the things guests most often forget.")
add(open('savebox.html').read())
h2("Guest Bedroom Safety Tips")
lst([f"<strong>Smoke alarms:</strong> NFPA guidance says {SR('smoke','smoke alarms should be installed inside every sleeping room')}, outside each separate sleeping area and on every level. Test the guest room alarm before visitors arrive.",
f"<strong>Carbon monoxide alarms:</strong> the CPSC advises installing CO alarms {SR('co','in a central location outside each separate sleeping area')}, and on every level of the home.",
f"<strong>Escape window:</strong> if you are turning an office or basement room into a bedroom, check the building code. The International Residential Code, as quoted by the City of Billings, requires an emergency escape opening with {SR('egress','a minimum net clear opening of 5.7 square feet')} (5 sq ft at grade floor), at least 24 in high and 20 in wide, with a sill no higher than 44 inches; local rules vary.",
"<strong>Clear path:</strong> keep the way from the bed to the door clear, and leave a small night light in the hallway for guests who do not know the house."])
h2("Common Guest Bedroom Mistakes")
lst(["<strong>Using the guest room as storage.</strong> Guests notice boxes and the exercise bike; give stored things one closed cabinet.",
"<strong>A bed that is too big for the room.</strong> A queen with no space to walk around feels worse than a comfortable full.",
"<strong>No light by the bed.</strong> Guests should not have to cross a dark room to switch off the ceiling light.",
"<strong>No space to unpack.</strong> Clear some hangers and a drawer before they arrive.",
"<strong>Never sleeping in it yourself.</strong> One night in the guest bed shows you what needs fixing."])
h2("Guest Bedroom FAQ")
h3("What do you need in a guest bedroom?")
p("A guest bedroom needs a comfortable bed with clean sheets and two kinds of pillows, a nightstand with a lamp, somewhere to put a suitcase, towels, a mirror and some empty closet space. Small extras like water, a charger, the Wi-Fi password and a spare toothbrush make guests feel welcome.")
h3("What size bed is best for a guest room?")
p("A queen suits most guest rooms and couples, but it needs a room about 10 by 9 feet with 30 inches to walk around. In a smaller room, a full or a twin, or a daybed with a trundle, leaves more space and is often more comfortable for guests.")
h3("How do you make a small guest room feel bigger?")
p("Push one side of the bed against a wall, use wall lights instead of large nightstands, store things under the bed, and keep the palette light and calm. A mirror opposite the window and curtains hung high and wide also make a small room feel larger.")
h3("Can a guest room be an office too?")
p("Yes. A daybed or sofa bed along one wall and a desk under the window let the room work as an office every day and a guest room when needed. Clear the desk and a drawer for guests, and keep work papers in a closed cabinet.")
h3("How do you make a guest room feel like a hotel?")
p("Use crisp white bedding, extra pillows, a folded throw, a luggage rack, a stack of fresh towels and blackout curtains. Add a lamp by the bed, water and glasses on the nightstand, and a small basket of toiletries.")
h2("Final Thoughts")
p("The best guest bedroom ideas are simple: the right size bed, light and water within reach, somewhere to unpack and a few small touches. Set the room up once, sleep in it yourself and keep a basket of essentials ready, and every visit becomes easy to host.")
p(f"Short on space? Our {a('room-divider-ideas','room divider ideas')} show how to carve a guest corner out of a bigger room, and our {a('studio-apartment-ideas','studio apartment ideas')} cover making one room work for everything.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<svg.*?</svg>','',html))
print(len(html),'words',len(txt.split()),'kw',txt.lower().count('guest bedroom ideas'),txt.lower().count('guest bedroom'),txt.lower().count('guest room'))
print(sorted(set(re.findall(r'dailyspacehacks\.com/([a-z0-9-]+)/',html))))
for w in ['colour','organise','favourite','cushion']:
    if w in txt.lower(): print('UK',w)
