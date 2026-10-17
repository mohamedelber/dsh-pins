import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
FSIS="https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/leftovers-and-food-safety"
HH="https://www.health.harvard.edu/healthy-aging-and-longevity/microwaving-food-in-plastic-dangerous-or-not"
p("Learning how to organize Tupperware comes down to one simple idea: every container needs a matching lid and a fixed place. Most food storage cabinets fail for the same reasons. There are too many mismatched pieces, the lids are loose in a pile, and nothing is sorted by shape, so one pull brings the whole stack down.")
p("This guide gives you a simple drawer and cabinet map, a 6-step clean-out and 15 Tupperware organization ideas for drawers, cabinets and lids, plus what to throw out and how many containers you really need. We say \"Tupperware\" the way most people do, for any plastic or glass food storage containers, whatever the brand.")
img(1)
summary(["<strong>Quick answer:</strong> Take everything out, match every base to a lid and recycle the orphans. Nest the bases by shape, largest at the bottom, and file the lids upright in a divider or rack, sorted by size. Keep one everyday set with lids on at the front, and keep only as many containers as your drawer or shelf holds.",
"Lids stored upright, like files, are the biggest single fix.",
"Replace cracked, warped or badly scratched containers and keep takeout tubs out of the microwave."],
"<strong>Time:</strong> 30 to 60 minutes · <strong>Cost:</strong> free to about $40 · <strong>Difficulty:</strong> Easy")
toc("how-to-organize-tupperware")
h2("The Container Drawer Map")
p("The simplest way to organize Tupperware is to give every type of piece its own zone. Whether you use a deep drawer or a cabinet shelf, the same five zones work. Lids go in an upright file at the back, nested bases sit in the middle by shape, and the everyday containers you grab most often sit at the front with their lids already on.")
diagram(open('z.svg').read(),"The container drawer map: lids filed upright at the back, rectangles, squares and rounds nested in the middle, and an everyday set with lids on at the front.")
p(f"Good organization also makes leftovers safer. The USDA's {ext(FSIS,'leftovers and food safety guide')} says to refrigerate leftovers within 2 hours, divide large amounts into shallow containers, and keep leftovers in the fridge for 3 to 4 days or in the freezer for 3 to 4 months. A few shallow containers in sizes you can find quickly make that much easier than a cupboard of mismatched tubs.")
h2("Quick Pick: Tupperware Organization Ideas by Space")
table(["Your space","Best ideas","Cost"],[
["Deep kitchen drawer","#1, #2, #3","Free to medium"],
["Lower cabinet shelf","#5, #6, #8","Low"],
["Deep cabinet, hard to reach","#7, #6","Medium"],
["Lids everywhere","#5, #10, #12","Free to low"],
["Too many containers","#13, #14, #15","Free"],
["Renters, no drilling","#1, #4, #6, #10","Low"]])
h2("How to Organize Tupperware in 6 Steps")
lst(["<strong>Empty everything.</strong> Take every container and lid out of the cabinets, drawers, dishwasher and the back of the fridge, and put them on the counter.",
"<strong>Do the match test.</strong> Snap a lid onto every base. Anything without a partner goes in a donate, recycle or reuse pile.",
"<strong>Remove damaged pieces.</strong> Set aside containers that are cracked, warped, badly stained or scratched, or that no longer seal.",
"<strong>Pick one home.</strong> Choose a drawer or cabinet near the dishwasher or prep area, and keep all food storage there.",
"<strong>Sort by shape and nest.</strong> Group rectangles, squares and rounds, then nest each group from largest to smallest.",
"<strong>File the lids.</strong> Stand the lids upright in a divider or rack, largest at one end, and keep the everyday set at the front with lids on."],True)
img(6)
p(f"If your cabinet is crowded with more than food containers, start with our guide on {a('how-to-organize-kitchen-cabinets','how to organize kitchen cabinets')} so the containers end up in the right zone of the kitchen.")
h2("Tupperware Organization Ideas for Drawers")
p("A deep drawer is the easiest place to store food containers, because you see everything from above and nothing falls out when you open it.")
h3("1. Nest Containers by Shape in a Deep Drawer")
p("Put each shape family in its own section: rectangles together, squares together and rounds together, each nested from largest to smallest. Two short stacks side by side are easier to use than one tall tower, and you can see at a glance which size is free. This one change makes the rest of the Tupperware organization ideas much easier.")
h3("2. A Pegboard Drawer System")
img(5)
p("A pegboard base with movable wooden pegs turns a deep drawer into compartments that you can change as your containers change. Set one compartment for nested bases, one for lids on edge and one for rounds. The pegs stop stacks from sliding when you open and close the drawer.")
h3("3. A Slim Lid Divider at the Back")
p("A narrow wooden or acrylic divider along the back of the drawer holds the lids upright like files. Sort them from largest to smallest so the right lid is easy to find. If your drawer is too shallow for lids to stand, lay them flat in a single row behind the bases instead.")
h3("4. Adjustable Drawer Dividers")
p(f"Spring-loaded bamboo dividers fit most drawer widths without screws, so they suit renters. Run one or two across the drawer to separate lids from bases and keep stacks from tipping. Our ideas for {a('how-to-organize-kitchen-drawers','organizing kitchen drawers')} show more ways to use them.")
h2("Tupperware Organizer Ideas for Cabinets")
p("If you have no free drawer, here is how to organize Tupperware in a cabinet: a lower shelf works well. The trick is to make the back of the shelf easy to reach.")
h3("5. A File-Style Lid Rack")
img(2)
p("A wire or bamboo lid rack, the kind sold as a Tupperware lid organizer or pot lid rack, holds flat lids upright on the cabinet floor. Put it at one side of the shelf and the nested bases beside it, so a lid and its base are always within one reach.")
h3("6. Clear Bins by Use")
img(4)
p("Clear bins with handles turn a deep shelf into drawers. Use one bin for small lunch containers, one for medium nested containers and one for lids. Pull the whole bin forward, take what you need and slide it back.")
h3("7. A Pull-Out Cabinet Organizer")
p(f"For a deep base cabinet, a pull-out basket or sliding shelf brings the back of the cabinet to you. Measure the cabinet opening and the hinge side before you buy, because the door and hinges reduce the usable width. Our {a('kitchen-storage-ideas','kitchen storage ideas')} include more ways to use deep cabinets.")
h3("8. A Shelf Riser to Double the Space")
p(f"A wire shelf riser adds a second level inside a tall cabinet. Store light, everyday containers on top and heavier glass on the bottom. If you want to add a real shelf instead, our {a('shelf-spacing-calculator','shelf spacing calculator')} helps you plan the gap between shelves.")
h2("How to Organize Tupperware Lids")
p("Lids cause most of the mess, because they are flat, slippery and come in more sizes than the bases. These ideas keep them under control.")
h3("9. Switch to One Matching Set")
img(3)
p("The most effective way to organize Tupperware lids is to need fewer of them. A matching set in two or three sizes, where many bases share the same lid, cuts the number of lids you have to sort. Glass containers with snap lids are a popular choice because they stack well with the lids on.")
h3("10. A Magazine File or a Dish Rack")
p("A plain magazine file or a small dish drying rack works as a cheap lid organizer. Put it on its side in a cabinet or upright in a deep drawer, and slot the lids in by size.")
h3("11. A Lid Holder on the Cabinet Door")
p("A shallow lid holder on the inside of a cabinet door frees up the shelf. Check that it clears the shelf edges when the door closes, keep only light plastic lids on it, and use adhesive strips if you cannot drill.")
h3("12. Store the Everyday Set With Lids On")
p("For the four to six containers you use every day for lunches and leftovers, keep the lids on. They take more space but save time, and they are the first thing you reach for. Store the rest of the collection nested, with lids filed separately.")
h2("Keep Your Container Collection Small")
p("Organizers help, but the real reason a container cabinet overflows is having too many pieces. These ideas keep the collection to a size that fits.")
h3("13. Keep Only What Fits")
p(f"Decide how much space food storage gets, one drawer or one shelf, and keep only what fits there. When you buy a new set, let an old one go. Our guide on {a('how-to-declutter-your-home','how to declutter your home')} uses the same container rule for every room.")
h3("14. Move Takeout Tubs Out of the Food Cabinet")
p(f"Takeout tubs and margarine tubs are handy for crafts and screws, but they are not made for reheating. {ext(HH,'Harvard Health')} notes that most takeout containers and plastic tubs or jars made to hold margarine are not microwave-safe, and that old, scratched or cracked containers may leach more plasticizers. Move them to the garage or craft box, or recycle them.")
h3("15. Count What You Really Use")
p(f"Most homes need enough containers for about three or four days of leftovers and lunches, since the USDA says leftovers keep 3 to 4 days in the fridge. Add a few freezer containers and a couple of large ones for batch cooking. Anything beyond that usually sits unused. For the fridge side, see our {a('fridge-organization','fridge organization')} guide.")
add(open('savebox.html').read())
h2("Common Tupperware Organization Mistakes")
lst(["<strong>Buying organizers first.</strong> Do the match test and clear out the extras before you buy a rack or bins.",
"<strong>Stacking lids flat in a pile.</strong> Flat piles slide and hide the size you need; file them upright.",
"<strong>Mixing shapes in one stack.</strong> Rounds and rectangles do not nest together and topple.",
"<strong>Keeping takeout tubs with good containers.</strong> They take space and are not meant for the microwave.",
"<strong>Storing containers far from where you use them.</strong> Keep them near the dishwasher or prep area so they get put away."])
h2("Tupperware Organization FAQ")
h3("What is the best way to store Tupperware?")
p("The best way to store Tupperware is to nest the bases by shape, largest at the bottom, and file the lids upright in a divider or rack, sorted by size. Keep the containers you use every day at the front with their lids on, and keep the whole collection in one drawer or cabinet near the dishwasher.")
h3("Should you store Tupperware with lids on or off?")
p("Store most containers with the lids off: nested bases and upright lids take much less space. Keep the lids on only for a small everyday set that you grab for lunches and leftovers. Matching glass sets that stack well can also be stored with the lids on if you have the room.")
h3("What Tupperware should I throw out?")
p(f"Let go of containers without a matching lid, and those that are cracked, warped, badly stained or no longer seal. {ext(HH,'Harvard Health')} notes that old, scratched or cracked containers, or ones that have been microwaved many times, may leach more plasticizers, so replace them or keep them for non-food storage.")
h3("How do you organize Tupperware in a cabinet?")
p("To organize Tupperware in a cabinet, put a lid rack at one side of a lower shelf and the nested bases beside it, or use clear bins with handles so you can pull the back of the shelf forward. In a deep cabinet, a pull-out basket brings everything within reach.")
h3("How many food storage containers do you need?")
p("Most homes do well with enough containers for three or four days of leftovers and lunches, plus a few freezer and batch-cooking sizes. The easier rule is to keep only what fits in your chosen drawer or shelf.")
h2("Final Thoughts")
p("Knowing how to organize Tupperware is less about buying organizers and more about a few simple rules. Once every base has a lid, every shape has a section and the lids stand upright, a food storage cabinet stays tidy with almost no effort. Start with the match test, set up the five zones and keep only what fits.")
p(f"Ready for the rest of the kitchen? See our {a('pantry-organization-ideas','pantry organization ideas')}, tackle the {a('junk-drawer-organizer','junk drawer')} next, and save this guide on Pinterest for later.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<svg.*?</svg>','',html))
print(len(html),'words',len(txt.split()),'kw',txt.lower().count('organize tupperware'),'tw org',txt.lower().count('tupperware organization'))
print(sorted(set(re.findall(r'dailyspacehacks\.com/([a-z0-9-]+)/',html))))
