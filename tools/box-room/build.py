import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
NDSS="https://www.gov.uk/government/publications/technical-housing-standards-nationally-described-space-standard/technical-housing-standards-nationally-described-space-standard"
NHSB="https://frimley-healthiertogether.nhs.uk/parentscarers/keeping-your-child-safe/accidents-and-injuries-keeping-your-child-safe-home"
NHSC="https://www.nhs.uk/conditions/baby/first-aid-and-safety/safety/baby-and-toddler-safety/"
p("The best box room bedroom ideas start with one honest fact: the room is small, so every piece has to earn its place. In many British homes the box room is the third bedroom, often tucked over the stairs, and it is usually just big enough for a single bed, a slim wardrobe and a bit of floor.")
p("This guide shows a simple box room layout with real sizes, which beds fit, a 6-step plan and 18 box room bedroom ideas for beds, the stair bulkhead, storage, home offices, nurseries and guest rooms, plus the mistakes that make a small room feel even smaller.")
img(1)
summary(["<strong>Quick answer:</strong> To make a box room work, put a single bed (90 x 190 cm) with drawers along the long wall, keep about 60 cm free to walk, build storage up the walls and over the stair bulkhead, and use wall lights and pale colours so the floor and walls stay clear.",
"A mid-sleeper or high sleeper frees the floor for a desk; a daybed turns an office into a guest room.",
"Check with a joiner before you build over a stair bulkhead."],
"<strong>Time:</strong> a weekend for most ideas · <strong>Cost:</strong> £ to £££ · <strong>Difficulty:</strong> Easy to medium")
toc("box-room-bedroom-ideas")
h2("What Is a Box Room?")
p("A box room is the smallest bedroom in a British house, often above the stairs or over the front door. Many are around 2 to 2.5 metres on each side, and some have a bulkhead, a raised box in the floor over the top of the staircase. Most fit a single bed and little else, so layout matters.")
h2("Box Room Layout Guide")
p("Start with a plan before you buy anything. The diagram below shows a typical box room with a single bed, a walkway and a wardrobe on the bulkhead.")
diagram(open('z.svg').read(),"Box room layout guide: a single bed along the long wall, a 60 cm walkway, a wardrobe over the stair bulkhead and room for the door to open.")
p(f"For comparison, the {ext(NDSS,'Nationally Described Space Standard')} for new homes in England asks for a single bedroom to have a floor area of at least 7.5 m² and to be at least 2.15 m wide. The standard applies to new dwellings, not existing homes, and many older box rooms are smaller, which is why the ideas below focus on beds and storage that use height instead of floor.")
h2("Which Bed Fits a Box Room?")
p("The bed decides the whole layout. These are common UK mattress sizes and how each one works in a small room.")
table(["Bed","Mattress size","Best for"],[
["Small single","75 x 190 cm","Very narrow rooms, children"],
["Single","90 x 190 cm","Most box rooms"],
["Small double","120 x 190 cm","Rooms about 2.4 m wide or more"],
["Cabin or storage bed","Single size","Storage underneath"],
["Mid-sleeper or high sleeper","Single size","A desk or play space underneath"],
["Daybed","Single size","Offices and guest rooms"]])
h2("Quick Pick: Box Room Bedroom Ideas by Use")
table(["How you use the room","Best ideas","Budget"],[
["Child's bedroom","#1, #2, #3","££"],
["Teen bedroom with a desk","#2, #10, #11","££"],
["Home office and guest room","#4, #5, #16","££"],
["Nursery","#15, #12, #17","£"],
["Room with a stair bulkhead","#7, #8","££"],
["Dressing room","#9, #14","£££"]])
h2("How to Plan a Box Room in 6 Steps")
lst(["<strong>Decide what the room is for.</strong> A bedroom, office, nursery or dressing room each needs different furniture.",
"<strong>Measure the room and the door swing.</strong> Note the window, radiator, sockets and any bulkhead.",
"<strong>Choose the bed first.</strong> A single along the long wall leaves the most floor.",
"<strong>Keep a clear walkway.</strong> Aim for about 60 cm beside the bed so you can get in and dress.",
"<strong>Go up, not out.</strong> Use wall shelves, tall wardrobes and storage over the bulkhead.",
"<strong>Light and colour last.</strong> Wall lights and pale, matching colours make the room feel calmer."],True)
h2("Space-Saving Beds")
p("Most box room bedroom ideas start with the bed, because it takes up most of the floor. Choose one that does a second job.")
h3("1. A Single Bed With Drawers Underneath")
p("A storage bed or cabin bed with deep drawers holds bedding, clothes or toys in the space that is usually wasted under a bed. Check the drawers can open fully without hitting the wall or the door, and that there is room to stand in front of them.")
h3("2. A Mid-Sleeper or High Sleeper With a Desk")
img(2)
p(f"Raising the mattress frees the floor for a desk, a chair or a reading nook, which is ideal for older children and teens. Choose a bed with a guard rail on all sides and a ladder fixed to the frame, and check there is enough headroom above the mattress. For bunk beds, NHS advice shared by {ext(NHSB,'Frimley Healthier Together')} is not to let children under six sleep in the top bunk, as they can easily fall out, and the same caution makes sense for any high bed.")
h3("3. A Cabin Bed for Younger Children")
p(f"A low cabin bed with drawers or a small pull-out desk gives young children storage without the height of a high sleeper. It also leaves the top of the bed low enough to make in the morning. Our {a("toy-storage-ideas","toy storage ideas")} help with the rest of a child\'s room.")
h3("4. A Daybed for an Office or Guest Room")
img(4)
p(f"A daybed looks like a sofa during the day and works as a single bed when guests stay. Choose one with drawers or a pull-out trundle, and pair it with a slim desk under the window. Our {a('desk-organization-ideas','desk organization ideas')} help keep a small work area tidy.")
h3("5. A Fold-Down Wall Bed")
p("A wall bed folds up into a cabinet, so the room becomes an office or play space during the day. It needs a solid wall and must be fixed exactly as the maker says, so this is a job for a fitter if you are not confident.")
h3("6. Push the Bed Into a Corner")
p("Placing a single bed in a corner, against two walls, leaves one larger open area instead of two narrow strips. Add a cushion or a padded headboard along the wall side so it works as a daybed too.")
h2("Using the Stair Bulkhead")
p("Many box rooms have a bulkhead, the raised box in the floor over the top of the stairs. It is awkward, but it can be useful.")
h3("7. Build a Wardrobe Over the Bulkhead")
img(3)
p("A fitted wardrobe built on top of the bulkhead turns dead space into hanging space. Bulkheads are often a light timber frame over the stairs, so ask a joiner whether yours can take the weight, and keep the wardrobe on its own frame or fixed to the walls rather than resting heavy loads on the bulkhead itself.")
h3("8. Turn the Bulkhead Into a Shelf or Desk")
p("If a wardrobe is too much, a simple top over the bulkhead makes a display shelf, a bedside surface or a small desk. Keep it light, and avoid using the bulkhead as a step or a seat unless a joiner has confirmed it is strong enough.")
h2("Storage That Uses the Walls")
p("When the floor is full, the walls are your storage. These ideas keep things off the floor and the room feeling open.")
h3("9. A Floor-to-Ceiling Built-In Wardrobe")
img(5)
p("A built-in wardrobe that runs to the ceiling holds far more than a freestanding one of the same width, and it looks like part of the room. Painting it the same colour as the walls, or a soft contrast like sage, keeps it calm. Aim for about 55 to 60 cm of inside depth for hangers.")
h3("10. Shelves Above the Bed or Desk")
p(f"Two or three wall shelves above the bed or desk hold books and baskets without using any floor. Fix them securely into the wall and keep heavy items off the shelf directly above where you sleep. Our {a('diy-floating-shelves','DIY floating shelves')} guide shows how to fit them.")
h3("11. Wall Lights Instead of Bedside Lamps")
p("Plug-in or wired wall lights free up the bedside surface, so a small floating shelf can replace a bedside table. That leaves more floor beside the bed, which matters in a narrow room.")
h3("12. Hooks and Rails on the Back of the Door")
p("An over-door rail or a row of hooks holds dressing gowns, tomorrow's outfit or bags. Check the door still opens fully and closes without catching.")
h3("13. Under-Bed Boxes for Bedding")
p(f"If the bed has no drawers, low boxes with lids keep spare bedding and out-of-season clothes dust-free. Our {a('small-bedroom-storage-ideas','small bedroom storage ideas')} include more ways to use the space under and around the bed.")
h2("Other Ways to Use a Box Room")
p("A box room does not have to be a bedroom. These uses suit the small size well.")
h3("14. A Small Dressing Room")
p("If the other bedrooms are short on storage, turning the box room into a dressing room with rails, shelves and a mirror can free space everywhere else. Open rails and shelves feel lighter than heavy wardrobes in a small room.")
h3("15. A Calm Nursery")
img(6)
p(f"A box room makes a cosy nursery next to the main bedroom. Keep the cot away from the window and keep blind or curtain cords tied up and out of reach; the {ext(NHSC,'NHS')} warns that unsecured blind and curtain cords can quickly wrap around a baby or toddler's neck. Keep the cot clear of pillows, bumpers and soft toys.")
h3("16. A Home Office That Doubles as a Guest Room")
p(f"A desk under the window and a daybed or sofa bed along the wall give you a workspace most days and a guest room when you need it. Store the guest bedding in drawers under the daybed. Our {a('how-to-organize-your-room','how to organize your room')} guide helps you set up simple zones.")
h2("Colour and Decor Ideas")
h3("17. Pale, Matching Colours")
p("Painting the walls, ceiling and woodwork in the same pale colour, or close shades of it, softens the edges of the room so it feels less boxy. Warm whites, creams and soft greens work well in rooms with little daylight.")
h3("18. A Mirror That Reflects the Window")
p("A mirror placed where it catches light from the window brightens a small room and makes it feel deeper. Fix larger mirrors securely to the wall, especially in a child's room.")
h2("Before and After: A Box Room Makeover")
img(7)
p("This makeover uses three of the box room bedroom ideas above. Before, the box room is a dumping ground for boxes, laundry and the ironing board. After, a single bed with drawers, two shelves and a wall light turn it into a calm bedroom, with everything else stored under the bed.")
h2("Common Box Room Mistakes")
lst(["<strong>Buying a bed that is too big.</strong> A small double can leave no room to walk or open drawers.",
"<strong>Furniture on every wall.</strong> Keep at least one wall mostly clear.",
"<strong>Ignoring the door swing.</strong> Check the door opens fully past the bed and wardrobe.",
"<strong>Loading the stair bulkhead.</strong> Ask a joiner before you build on it or stand on it.",
"<strong>Dark, heavy colours everywhere.</strong> They can make a room with little daylight feel smaller.",
"<strong>Letting it become a junk room.</strong> Give every stored item a box, a shelf or a drawer."])
h2("Box Room FAQ")
h3("Can you fit a double bed in a box room?")
p("Sometimes, but it is usually a squeeze. A small double (120 x 190 cm) can work in a room about 2.4 m wide or more, but you may lose the walkway and space for drawers. In most box rooms a single bed, a cabin bed or a high sleeper works better.")
h3("How big is a box room in the UK?")
p("There is no fixed size. Many box rooms are around 2 to 2.5 metres on each side. For new homes in England, the Nationally Described Space Standard asks for single bedrooms of at least 7.5 m² and 2.15 m wide, and many older box rooms are smaller than that.")
h3("How do you make a box room look bigger?")
p("Keep the floor as clear as possible, use a bed with storage underneath, build storage up the walls, choose pale matching colours and add a mirror that reflects the window. Wall lights and floating shelves instead of bedside tables also help.")
h3("What can you do with the bulkhead in a box room?")
p("You can build a wardrobe, shelf or small desk over it, or simply leave it as a surface for baskets. Bulkheads are often a light timber frame over the stairs, so ask a joiner before adding weight, and do not use it as a step or seat unless it has been checked.")
h2("Final Thoughts")
p(f"The best box room bedroom ideas use height instead of floor: a bed with storage or a high sleeper, shelves and wardrobes up the walls and smart use of the stair bulkhead. Pick one clear purpose for the room, plan the layout first and keep at least one wall calm. If your house has other awkward spaces, see our {a('under-stairs-storage-ideas','under stairs storage ideas')} and {a('airing-cupboard-shelves','airing cupboard shelves')} guides.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub('<[^>]+>',' ',re.sub(r'<svg.*?</svg>','',html,flags=re.S))
print(len(txt.split()),'words; kw',len(re.findall('box room bedroom ideas',txt,re.I)),'box room',len(re.findall('box room',txt,re.I)),'; ideas',len(re.findall(r'<h3 class="wp-block-heading">\d+\.',html)))
print(sorted(set(re.findall(r'dailyspacehacks\.com/([a-z0-9-]+)/',html))))
