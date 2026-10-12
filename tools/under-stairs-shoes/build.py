import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
LFB="https://www.london-fire.gov.uk/news/2014-news/londoners-warned-of-potential-fire-hazard-lurking-under-the-stairs"
NFR="https://www.northumberlandfireandrescue.gov.uk/escape-planning"
p("Good under stairs shoe storage turns the pile of trainers by the front door into something you can actually walk past. In most British homes the stairs rise straight from the hallway, so the space underneath is the one spot near the door that is big enough to hold every pair, if you match the storage to the shape.")
p("This guide shows which storage fits the low, middle and tall parts of the space, a 6-step plan, and 16 under stairs shoe storage ideas, from pull-out drawers and built-in cubbies to cheap racks, shoes on wheels and ideas for small hallways, plus the safety checks most guides skip.")
img(1)
summary(["<strong>Quick answer:</strong> The best under stairs shoe storage uses the shape of the space: shallow drawers or cubbies for flat shoes at the low end, pull-out units with angled shelves for everyday pairs in the middle, and boots, wellies or a bench at the tall end. Keep shoes away from any fuse board and keep the hallway clear.",
"Pull-out units make the deep space usable, because the shoes at the back come out to you.",
"Let wet shoes and wellies dry on a tray before they go behind a closed door."],
"<strong>Time:</strong> an hour for racks, a weekend for built-in pull-outs · <strong>Cost:</strong> £ to £££ · <strong>Difficulty:</strong> Easy to hard")
toc("under-stairs-shoe-storage")
h2("Under Stairs Shoe Storage Planner")
p("The space under a straight staircase is a long triangle: very low at one end and tall at the other. Plan the storage by height, so every section holds the shoes that fit it.")
diagram(open('z.svg').read(),"Under stairs shoe storage planner: shallow drawers for trainers at the low end, pull-out units in the middle and boots or a bench at the tall end, with the fuse board kept clear.")
p(f"Two safety points matter under the stairs. Many fuse boards are fitted there, and {ext(LFB,'London Fire Brigade and Electrical Safety First')} advise making sure coats, shoes and other combustible items stored in those areas are placed well away from it. The hallway and stairs are also usually your way out in a fire, and {ext(NFR,'Northumberland Fire and Rescue Service')} advises making sure hallways and stairs are not blocked with clutter. Storage that closes neatly under the stairs helps with both.")
h2("What Is the Best Shoe Storage for Under the Stairs?")
p("For most homes, the best shoe storage for under the stairs is a set of pull-out units on runners, because they bring the shoes at the back out into the hallway. If you rent or want to spend less, open racks inside an under stairs cupboard or a crate on wheels do a similar job without building anything.")
h2("Quick Pick: Under Stairs Shoe Storage by Situation")
table(["Your situation","Best ideas","Budget"],[
["Open space, happy to build","#1, #2, #3","£££"],
["Existing cupboard or open alcove","#8, #9, #10","£"],
["Renting, no drilling","#6, #7, #8","£"],
["Family with lots of pairs","#4, #11, #13","££"],
["Muddy boots and wellies","#9, #15, #16","£"]])
h2("How to Plan Under Stairs Shoe Storage in 6 Steps")
lst(["<strong>Count your shoes.</strong> Only everyday pairs need to live here; store party shoes and out-of-season boots elsewhere.",
"<strong>Check what is already there.</strong> Look for a fuse board, meter, pipes or cables, and keep clear access to them.",
"<strong>Measure.</strong> The width of the stairs, the length of the space and the height at a few points along the slope.",
"<strong>Split it into zones.</strong> Low end for flat shoes, middle for most pairs, tall end for boots or a bench.",
"<strong>Choose the storage.</strong> Pull-outs or drawers if you can build, racks or crates if you cannot.",
"<strong>Plan for wet shoes.</strong> A boot tray and a little air flow stop smells and mould."],True)
h2("Pull-Out and Built-In Ideas")
p("Built-in storage uses every centimetre of the slope. These ideas cost more but look tidy and hold the most shoes.")
h3("1. Fit Pull-Out Shoe Units on Runners")
p("Tall pull-out units on heavy-duty runners are the classic answer. Each one slides out into the hallway like a drawer on its side, with shelves inside for shoes, so nothing gets lost at the back. Angled shelves with a small lip show more pairs at a glance. Use runners rated for the weight and fix the frame securely to the floor and wall.")
h3("2. Add Shallow Drawers at the Low End")
p("The lowest part of the slope is too short for a tall unit but perfect for one or two shallow drawers. They hold flat shoes, sliders and children's trainers. Full-extension runners let you see the back of the drawer.")
h3("3. Build Open Cubbies")
img(2)
p(f"Open cubbies are cheaper than pull-outs and quick to use: one pair per box, boots in the taller ones. They suit a hallway that people see, so keep them tidy and limit them to everyday shoes. Our {a('under-stairs-storage-ideas','under stairs storage ideas')} show more ways to use the slope.")
h3("4. Combine a Bench With Shoe Shelves")
img(3)
p(f"At the tall end, a built-in bench gives you somewhere to sit while you put shoes on, with open shelves underneath. Add a hook or two beside it for coats, kept away from any fuse board. It works like a mini {a('boot-room-ideas','boot room')} in the hallway.")
h3("5. Use Kitchen Base Units")
p("Flat-pack kitchen base units with deep drawers make a budget built-in. Fit them along the tall part of the space, add a worktop or wooden top, and use the drawers for shoes and the top for keys and post. Fix them to the wall so they cannot tip when a drawer is full and open.")
h2("Freestanding and Budget Ideas")
p("No building work needed. These ideas suit renters and anyone who wants storage this weekend.")
h3("6. Put Shoes on Wheels")
img(4)
p("A low wooden crate or tray on castors rolls out from under the stairs and back again. It is one of the cheapest under stairs shoe storage ideas and works well for trainers and school shoes. Choose castors that suit your floor and keep the crate low so it slides under the lowest steps.")
h3("7. Stand a Slim Tilt-Out Cabinet at the Tall End")
img(5)
p(f"A slim tilt-out cabinet holds shoes upright in flip-down compartments and takes up little floor space. Fix it to the wall with the fitting supplied, because tall slim cabinets can tip forward. Our {a('shoe-storage-ideas','shoe storage ideas')} include more slim cabinets for narrow hallways.")
h3("8. Use Tiered Racks in an Alcove or Cupboard")
img(6)
p("Whether the space under your stairs is an open alcove or an existing cupboard, simple tiered racks on the floor turn it into a shoe store. Put everyday pairs at the front and seasonal boots behind. In a cupboard, a battery LED light makes it easy to see.")
h3("9. Add a Boot Tray for Wellies")
p("Wet wellies and muddy trainers belong on a rubber or slate boot tray before they go anywhere else. Place it at the front of the cupboard or by the door, and move the boots onto a shelf once they are dry.")
h3("10. Use the Back of the Cupboard Door")
p("A slim over-door rack on the inside of the under stairs cupboard door holds slippers, flip-flops and kids' shoes. Check that the door still closes and does not hit the racks behind it.")
h2("Small Space and Family Ideas")
p("These ideas keep a busy hallway under control without extra furniture.")
h3("11. Give Each Person a Shelf or Cubby")
p("One shelf or cubby per person means everyone knows where their shoes go, and you can see at a glance whose trainers are missing. Label the front for younger children.")
h3("12. Keep Only Everyday Pairs Here")
p("Under the stairs works best for the shoes you wear every week. Move party shoes, walking boots and out-of-season pairs to a wardrobe or under the bed, and swap them at the start of each season.")
h3("13. Put Children's Shoes at the Low End")
p("The low end of the slope is the right height for children. Shallow drawers or cubbies there let them put their own shoes away and keep small pairs from getting buried under adult boots.")
h3("14. Label Drawers and Boxes")
p("Closed drawers and boxes hide clutter but also hide what is inside. A simple label on each front, such as trainers, school shoes or wellies, saves opening every drawer.")
h2("Keeping Shoes Fresh Under the Stairs")
p("A closed space under the stairs can trap moisture and smells. These two habits stop that.")
h3("15. Let Shoes Dry Before They Go Away")
p("Put wet shoes on a boot tray or rack in the open hallway until they are dry, then store them. Shoes that go away wet make the whole space smell musty.")
h3("16. Leave Room for Air")
p(f"Do not pack the space so tightly that air cannot move. Leave small gaps between pairs, and consider doors with vents or a small gap at the bottom. If you are planning a downstairs loo under the stairs instead, our {a('downstairs-toilet-ideas','downstairs toilet ideas')} cover the space you need.")
h2("Before and After: An Under Stairs Shoe Makeover")
img(7)
p("Before, the space under the stairs is a heap of unpaired shoes spilling into the hallway. After, sage pull-out units hold every pair out of sight, and the hallway is clear to walk through.")
h2("Common Under Stairs Shoe Storage Mistakes")
lst(["<strong>Piling shoes against the fuse board.</strong> Keep coats, shoes and other combustible items well away from it.",
"<strong>Blocking the hallway.</strong> Freestanding racks that stick out make the escape route harder to use.",
"<strong>Deep shelves with no pull-out.</strong> Shoes at the back are forgotten.",
"<strong>Wet shoes behind closed doors.</strong> They cause smells and mould.",
"<strong>Tall units not fixed to the wall.</strong> A full tilt-out cabinet or drawer unit can tip.",
"<strong>Storing every pair you own.</strong> Keep only everyday shoes here."])
h2("Under Stairs Shoe Storage FAQ")
h3("How do you store shoes under the stairs?")
p("Match the storage to the height: shallow drawers or cubbies for flat shoes at the low end, pull-out units with shelves in the middle and boots or a bench at the tall end. Keep only everyday pairs there and keep the space around any fuse board clear.")
h3("Are pull-out shoe drawers under the stairs worth it?")
p("Yes, if you can build or pay for them. Pull-outs bring the shoes at the back of the deep space out to you, so you can use the whole depth. On a tight budget, a crate on wheels or racks inside a cupboard gives a similar result for much less.")
h3("Is it safe to store shoes under the stairs?")
p("Yes, as long as shoes and coats are kept well away from any fuse board fitted there and the storage does not block the hallway or stairs. Fire services advise keeping escape routes clear, so choose storage that closes or sits neatly under the slope.")
h3("How do you stop shoes smelling under the stairs?")
p("Let shoes dry fully before you put them away, keep wet wellies on a boot tray, and leave small gaps so air can move. Vented doors or a gap at the bottom of the cupboard door also help, and clear out shoes you no longer wear.")
h2("Final Thoughts")
p(f"The best under stairs shoe storage follows the slope: low drawers for small shoes, pull-outs in the middle and boots or a bench at the tall end. Keep the fuse board clear and the hallway open, and the pile by the front door will finally disappear. For more hallway ideas, see our {a('small-entryway-ideas','small entryway ideas')} and {a('airing-cupboard-shelves','airing cupboard shelves')} guides.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub('<[^>]+>',' ',re.sub(r'<svg.*?</svg>','',html,flags=re.S))
print(len(txt.split()),'words; kw',len(re.findall('under stairs shoe storage',txt,re.I)),'; ideas',len(re.findall(r'<h3 class="wp-block-heading">\d+\.',html)))
