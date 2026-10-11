import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
WW="https://wheelsforwellbeing.org.uk/benches-and-seating-in-public-spaces/"
SK="https://www.southkesteven.gov.uk/housing/damp-mould-and-condensation-advice/how-can-i-reduce-damp-and-mould"
PP="https://www.planningportal.co.uk/permission/common-projects/extensions/building-regulations-ventilation"
p("Good boot room ideas stop mud, wet coats and muddy paws at the back door, before they reach the rest of the house. You do not need a big country kitchen to have one: a hallway corner, the space under the stairs, a tall cupboard or a glazed porch can all become a hard-working boot room.")
p("Below you will find a layout guide with the heights that work, a 6-step plan and 18 boot room ideas for small spaces, seating and storage, mud and wet weather, dogs and budgets, plus a before-and-after and the mistakes to avoid.")
img(1)
summary(["<strong>Quick answer:</strong> A boot room needs four zones: somewhere to wipe (a mat and a boot tray by the door), somewhere to sit (a bench about 45 to 48 cm high with baskets underneath), somewhere to hang (hooks at adult and child height) and somewhere to store (a shelf for hats and gloves). In a small home, fit these into a hallway nook, under the stairs, a tall cupboard or a porch.",
"Choose a floor that copes with mud and water, such as slate, quarry tiles or porcelain.",
"Hang wet coats with space around them and keep the room ventilated, rather than drying them on radiators."],
"<strong>Time:</strong> an afternoon for hooks and a bench, longer for built-in joinery · <strong>Cost:</strong> £ to £££ · <strong>Difficulty:</strong> Easy to moderate")
toc("boot-room-ideas")
h2("Boot Room Layout Guide: Zones and Heights")
p("Every boot room works best when you plan it in the order you use it: wipe your feet, sit down, take off boots, hang up your coat and put away hats and gloves. Measure the wall you have and mark these four zones before you buy anything.")
diagram(open('z.svg').read(),"Boot room layout guide: wipe by the door, sit on a bench 45 to 48 cm high, hang coats on hooks at adult and child height, and store hats and gloves on a shelf above.")
p(f"For the bench, UK seating guidance is a useful starting point: a {ext(WW,'Wheels for Wellbeing guide')} to public seating says most seats should be 470 to 480 mm high (citing Inclusive Mobility 2021) and gives a seat depth of 380 to 470 mm from the HSE. A boot room bench of about 45 to 48 cm high and 38 to 45 cm deep fits most adults. The hook heights and the 90 cm of clear floor are our own rule of thumb, so adjust them for your family.")
p(f"Wet coats bring a lot of moisture indoors. {ext(SK,'South Kesteven District Council')} advises drying clothes in a heated, well-ventilated room and not drying clothes on radiators, and it suggests leaving space for air to circulate behind large furniture. In a boot room, that means hooks with space between them, an open trickle vent or window, and no coats draped over the radiator.")
h2("Quick Pick: Boot Room Ideas by Space")
table(["Your space","Best ideas","Budget"],[
["Narrow hallway","#1, #7, #10","£"],
["Under the stairs","#2, #6, #9","££"],
["No spare room at all","#3, #4, #18","£–££"],
["Family with kids","#8, #9, #12","££"],
["Dog owners","#14, #16, #11","££–£££"]])
h2("How to Plan a Boot Room in 6 Steps")
lst(["<strong>Measure the space.</strong> Wall length, depth from the wall, ceiling height and where the door swings.",
"<strong>Mark the four zones.</strong> Wipe by the door, then sit, hang and store along the wall.",
"<strong>Choose the bench.</strong> About 45 to 48 cm high, with room for baskets or boots underneath.",
"<strong>Set the hooks.</strong> One row for adults and one lower row for children.",
"<strong>Sort the floor.</strong> A tough, wipeable floor, a coir mat and a boot tray for wet wellies.",
"<strong>Plan for wet weather.</strong> Ventilation, space between coats and somewhere for muddy boots to dry."],True)
h2("Small Boot Room Ideas")
p("These small boot room ideas work in homes with no spare room, because they borrow a corner, a cupboard or the porch.")
h3("1. Turn a Hallway Corner Into a Boot Nook")
img(2)
p(f"A shallow bench, a peg rail and a boot tray turn the end of a hallway into a mini boot room. Keep the bench around 35 cm deep in a narrow hall so there is still room to walk past. Our {a('small-entryway-ideas','small entryway ideas')} have more ways to organise a tight space by the door.")
h3("2. Use the Space Under the Stairs")
img(3)
p(f"The low end of the stairs is perfect for a bench and baskets, and the tall end takes coat hooks. If you only have a cupboard there, our {a('under-stairs-storage-ideas','under stairs storage ideas')} show how to fit pull-outs and shelves into the slope.")
h3("3. Hide It in a Tall Cupboard")
img(4)
p("A tall cupboard by the back door can hold coats, a shelf of baskets and a boot tray behind closed doors. It is the tidiest of all boot room ideas for small spaces, because the mess disappears when you shut the doors. Leave a gap at the bottom of the doors or add a vent so damp coats can breathe.")
h3("4. Make the Porch Work Harder")
img(5)
p("An enclosed porch is a natural boot room. A slim bench along one side, hooks on the wall and a slate tray for wellies keep the mud out of the house, and the glass lets in plenty of light.")
h3("5. Share the Space With the Utility Room")
p(f"If you have a utility room by the back door, give one wall to coats and boots. Our {a('small-utility-room-ideas','small utility room ideas')} show how to fit a washing machine, a sink and storage into a small room. If you are creating a new utility room with a washing machine and sink, the {ext(PP,'Planning Portal')} says it needs extract ventilation.")
h2("Boot Room Seating and Storage Ideas")
p("Storage is what turns a corner into a boot room. Aim to get everything off the floor except the boots that are drying.")
h3("6. Build a Bench With Baskets Underneath")
p("A bench gives you somewhere to sit and pull off muddy boots, and the space underneath holds baskets for shoes, dog towels and sports kit. Choose baskets that slide out easily and leave one slot open for the boots you wear every day.")
h3("7. Fit a Shaker Peg Rail")
p("A peg rail is one of the simplest boot room ideas and it suits a cottage look. Pegs hold coats, bags, scarves and dog leads, and a rail fixed into the studs or masonry spreads the weight of heavy wet coats.")
h3("8. Give Everyone Their Own Cubby")
img(6)
p("Open cubbies with one hook, one basket and a space for boots give each person their own spot, so nobody has to dig through a shared pile. Children find their own things more easily, and coats stop ending up on the floor.")
h3("9. Add a Shelf for Hats and Gloves")
p(f"A shelf above the hooks holds a basket per person for hats, gloves and scarves. Our {a('hat-storage-ideas','hat storage ideas')} cover ways to store caps and beanies without crushing them.")
h3("10. Use a Slim Shoe Cabinet for Clean Shoes")
p(f"Keep clean everyday shoes in a slim tilt-out cabinet and leave the boot tray for wet and muddy pairs. Let boots dry before they go into a closed cabinet. Our {a('shoe-storage-ideas','shoe storage ideas')} include cabinets that fit in very shallow spaces.")
h2("Practical Ideas for Mud and Wet Weather")
p("The best boot room ideas are practical first. These are the details that make cleaning up quick.")
h3("11. Choose a Floor That Copes With Mud")
img(7)
p("Slate, quarry tiles, brick-effect tiles and porcelain all shrug off mud and water and wipe clean quickly. Darker colours and textured surfaces hide dirt between cleans, and a matt or slip-resistant finish is safer when the floor is wet.")
h3("12. Put Down a Boot Tray and a Coir Mat")
p("A rubber or slate boot tray catches water and mud from wellies, and a coir mat at the door takes most of the dirt off shoes. Shake the mat outside and rinse the tray regularly so the mud does not spread.")
h3("13. Add a Welly Rack")
p("A simple welly rack keeps boots upright and in pairs, so they dry evenly and do not end up in a heap. Put it on the boot tray or on a hard floor near the door.")
h3("14. Fit a Sink for Muddy Boots and Paws")
img(8)
p("A deep Belfast sink set into a worktop is ideal for rinsing muddy boots, washing a dog's paws and soaking dirty kit. Put the tap directly over the basin and choose a worktop that can cope with water, then seal it well.")
h3("15. Give Wet Coats Room to Dry")
p("Do not cram wet coats together. Leave space between hooks, keep a window or trickle vent open and dry soaked clothes in a well-ventilated room rather than on a radiator. A boot room that stays damp will start to smell and can grow mould.")
h3("16. Set Up a Dog Station")
img(9)
p(f"A dog bed under the bench, hooks for the lead and towel, and a basket of toys and treats make walks easier. Keep a towel by the door so you can dry muddy paws before the dog runs through the house. Our {a('mudroom-ideas','mudroom ideas')} include more ideas for pets, and in the US this space is usually called a mudroom.")
h2("Boot Room Ideas on a Budget")
p("You do not need bespoke joinery. These boot room ideas on a budget use paint and flat-pack furniture.")
h3("17. Paint the Woodwork in a Wipeable Finish")
p("A sage green, deep blue or warm grey on the bench and panelling makes a boot room feel finished. Choose a durable, wipeable paint for the woodwork and walls so muddy marks clean off.")
h3("18. Build It From Flat-Pack Units")
p(f"Many people build their boot room from flat-pack kitchen or wardrobe units, often called an IKEA hack: wall cabinets laid on their side make a bench base, and a tall wardrobe becomes a coat cupboard. Add a solid wood seat, new handles and paint to make them look built in. Our {a('diy-floating-shelves','DIY floating shelves guide')} explains how to fix shelves securely to the wall.")
h2("Before and After: A Small Boot Room Makeover")
img(10)
p("In the before picture, coats are piled on the bench, wellies lie across the floor and loose shoes fill the space underneath. In the after picture, the same room has coats on the hooks, baskets under the bench and boots standing in pairs on a tray. Nothing was rebuilt: the change comes from giving every item a place.")
h2("Common Boot Room Mistakes")
lst(["<strong>No space to sit.</strong> Without a bench, people take off muddy boots standing up and mud goes everywhere.",
"<strong>Hooks too close together.</strong> Bulky coats overlap, stay damp and fall off.",
"<strong>A floor that stains.</strong> Unsealed wood, pale grout and carpet do not cope with mud.",
"<strong>Drying coats on radiators.</strong> Hang them with space around them in a ventilated room instead.",
"<strong>Wet boots in closed cupboards.</strong> Let them dry on a tray first.",
"<strong>Forgetting the children.</strong> Hooks they cannot reach mean coats on the floor."])
h2("Boot Room FAQ")
h3("What is a boot room?")
p("A boot room is a space by the back or side door where you take off muddy boots and wet coats before going into the rest of the house. In the US the same space is usually called a mudroom.")
h3("How small can a boot room be?")
p("A boot room can be as small as one wall or a tall cupboard. A bench, a row of hooks, a shelf and a boot tray fit along a short wall in a hallway, under the stairs or in a porch.")
h3("How high should a boot room bench be?")
p("UK guidance for public seating puts most seats at 47 to 48 cm high, so a boot room bench of about 45 to 48 cm high and 38 to 45 cm deep suits most adults. Go a little lower if young children will use it most.")
h3("What is the best floor for a boot room?")
p("A hard, water-resistant floor such as slate, quarry tiles, brick-effect tiles or porcelain, with a slip-resistant finish. Add a coir mat by the door and a boot tray for wet wellies.")
h2("Final Thoughts")
p("The best boot room ideas are simple: a place to wipe your feet, a bench to sit on, hooks at the right height and a shelf for the small things. Start with the space you have, whether that is a hallway corner, the stairs or the porch, and the mud will stay by the door.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub('<[^>]+>',' ',re.sub(r'<svg.*?</svg>','',html,flags=re.S))
print(len(txt.split()),'words; keyword',len(re.findall('boot room ideas',txt,re.I)),'; h3 ideas',len(re.findall(r'<h3 class="wp-block-heading">\d+\.',html)))
