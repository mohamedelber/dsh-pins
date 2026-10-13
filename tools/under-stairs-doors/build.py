import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
BWF="https://www.bwf.org.uk/question-of-the-week/what-are-the-current-recommendations-for-the-rise-and-going-of-stairs/"
CAD="https://cadentgas.com/locating-your-meter-and-turning-off-the-gas"
CNC="https://www.cncbuildingcontrol.gov.uk/wp-content/uploads/2025/02/CNCD-051-Loft-Conversion-Easy-Guide-V1.2-1.pdf"
p("Good under stairs cupboard doors turn a dark, awkward triangle in the hallway into storage that looks as if it was always meant to be there. Because the space sits under a sloping staircase, a standard rectangular door rarely fits it well, so the best doors are cut to follow the slope.")
p("This guide covers how to measure the opening, the door styles that suit British hallways, from angled shaker doors and cottage ledged doors to sliding and hidden doors, how to make an under stairs cupboard door yourself, and the safety points to check before you start.")
img(1)
summary(["<strong>Quick answer:</strong> The best under stairs cupboard doors are made to measure, with top edges cut to the same angle as the stairs. Split a wide opening into two or three doors, hinge each one on a vertical edge, and keep any gas meter or fuse board inside easy to reach.",
"Measure the width, the height at both ends and the angle before you buy or build anything.",
"Sliding, hidden and painted doors change the look; ledged doors are the easiest to make yourself."],
"<strong>Time:</strong> a weekend to make and hang · <strong>Cost:</strong> £ (DIY) to £££ (made to measure) · <strong>Difficulty:</strong> Medium")
toc("under-stairs-cupboard-doors")
h2("How to Measure for Under Stairs Cupboard Doors")
p("Most under stairs openings have a tall end, a short end and a sloping top. Take these four measurements before you order doors or buy timber, and write them on a sketch of the opening.")
diagram(open('z.svg').read(),"How to measure for under stairs cupboard doors: the full width, the height at the tall end and the short end, and the angle of the slope.")
lst(["<strong>W, the full width:</strong> measure along the floor from the tall end to the short end of the opening.",
"<strong>H1, the tall end:</strong> measure from the floor to the underside of the stairs at the highest point.",
"<strong>H2, the short end:</strong> measure the height at the lowest point you want a door to cover.",
"<strong>The angle:</strong> copy it with a sliding bevel, or tape a sheet of cardboard in place and draw along the underside of the stairs to make a template."])
p(f"Measure the heights at both ends and in the middle, because floors and stairs are rarely perfectly level. For reference, the {ext(BWF,'British Woodworking Federation')} notes that under Approved Document K the maximum pitch of a private stair is 42°, so on a staircase built to current rules the slope you copy will be no steeper than that. Older stairs can differ, so always measure your own.")
p(f"Check what is inside before you plan the doors. A gas meter is often fitted under the stairs, and {ext(CAD,'Cadent')} explains that the emergency control valve is the red tap handle near the meter pipe, so plan a door that opens fully in front of it. Keep a fuse board just as easy to reach.")
h2("Can You Buy Ready-Made Under Stairs Cupboard Doors?")
p("Standard internal doors are rectangular, so they only fit the tall, square part of an under stairs opening. For the sloping part you need doors that are made to measure, cut down by a joiner, or made yourself. Many people fit one standard door at the tall end and panel the rest.")
h2("Quick Pick: Under Stairs Cupboard Doors by Situation")
table(["Your situation","Best ideas","Budget"],[
["Want it to look built in","#1, #3, #4","£££"],
["Cottage or period home","#2, #3","££"],
["Narrow hallway, little swing space","#5, #4","££"],
["Renting or on a tight budget","#7, #10","£"],
["Shoes, coats or a musty smell","#6, #8","££"]])
h2("How to Make an Under Stairs Cupboard Door in 7 Steps")
p("A ledged and braced door made from tongue and groove boards is the easiest door of this kind to build at home. These steps give the outline; a joiner can make the same door if you would rather not cut it yourself.")
lst(["<strong>Measure the opening.</strong> Take the width, both heights and the angle, as shown in the diagram above.",
"<strong>Make a cardboard template.</strong> Tape cardboard over the opening, draw along the frame and the slope, and cut it out to check the fit.",
"<strong>Choose how the door is built.</strong> Tongue and groove boards with ledges and a brace are simple; a flat MDF panel suits a painted, modern look.",
"<strong>Cut the angle.</strong> Transfer the slope from the template to the boards and cut slightly outside the line, then plane or sand to fit.",
"<strong>Allow a small gap.</strong> Trim the door so there is an even gap of about 2 to 3 mm all round, so it opens without rubbing.",
"<strong>Hang the door.</strong> Fit the hinges on a vertical edge, usually the taller one, which gives the hinges the most length. Use two or three hinges depending on the height.",
"<strong>Add a catch and handle, then paint.</strong> A magnetic catch or a thumb latch keeps the door closed; finish with paint or a hard-wearing wood finish."],True)
h2("Door Styles That Follow the Slope")
p("These ideas keep the clean line of the staircase. The top edge of every door runs parallel to the stairs, so the cupboard looks built in rather than added.")
h3("1. Angled Shaker Doors in a Row")
p(f"Splitting a long opening into two or three shaker doors, each with an angled top, is the classic look. Narrower doors are lighter, swing into less of the hallway and let you reach each section on its own: coats and the vacuum at the tall end, shoes in the middle and baskets at the low end. Our {a('under-stairs-storage-ideas','under stairs storage ideas')} show how to fit out each part.")
h3("2. A Ledged Cottage Door")
img(3)
p("A ledged and braced door made of vertical tongue and groove boards suits cottages, Victorian terraces and farmhouse-style hallways. Black T hinges and a thumb latch finish it, and it is the easiest style to make at home. Paint it a soft colour or leave the wood natural and oiled.")
h3("3. Panelled Doors That Match the Stairs")
p("If your staircase already has panelling on its side, copy the same panel size and moulding on the doors. The cupboard then disappears into the joinery, which works well in period homes where you want the hallway to look original.")
h3("4. Hidden Flush Doors")
img(2)
p(f"Flat, handleless doors painted the same colour as the walls show only thin shadow lines, so the cupboard almost vanishes. Push-to-open catches mean there are no handles to catch a bag or a shoulder in a narrow hallway. The same trick suits a {a('small-entryway-ideas','small entryway')} where furniture would feel crowded.")
h2("Space-Saving Door Options")
p("Not every hallway has room for a door to swing open. These options save space or skip the full door altogether.")
h3("5. A Sliding Door at the Tall End")
img(5)
p("A single sliding door on a top track works where the tall end of the space has a rectangular opening. The door slides along the wall instead of swinging into the hallway, so it suits narrow spaces. You need a clear stretch of wall beside the opening at least as wide as the door, and the sloping part beside it can be closed in with fixed panelling.")
h3("6. Doors at the Tall End, Drawers at the Low End")
p(f"The lowest part of the slope is awkward to reach through a door. Many built-in designs fit doors at the tall end and pull-out drawers at the low end, so the shoes or boxes at the back slide out to you. Our {a('under-stairs-shoe-storage','under stairs shoe storage')} guide shows how to split the space by height.")
h3("7. A Curtain Instead of a Door")
p("A linen curtain on a rod or ceiling track is the cheapest way to hide an open alcove under the stairs, and it needs no joinery. It suits renters, and it lets air move, which helps if you store shoes or coats. Choose a washable fabric and keep it clear of any fuse board or meter.")
h3("8. Vented or Slatted Doors")
p(f"Closed cupboards can trap moisture and smells, especially with damp coats and shoes inside. Slatted panels, a vented insert or a small gap at the bottom of the door let air in. They work well if your cupboard doubles as a {a('boot-room-ideas','boot room')} for wet wellies.")
h2("Colour and Hardware Ideas")
p("The finish decides whether the cupboard blends in or becomes a feature of the hallway.")
h3("9. Paint the Door a Bold Colour")
img(4)
p("A single under stairs door painted terracotta, deep green or navy turns a plain cupboard into a feature. It is a cheap change that works with a matching stair runner or front door. Use a hard-wearing eggshell or satin finish, because hallway doors get knocked and touched every day.")
h3("10. Match the Door to the Walls")
p("If your hallway is small, painting the doors, the panelling and the walls in one colour makes the space feel calmer and wider. Pale creams, warm whites and soft greys work well in a dark hallway with little daylight.")
h3("11. Choose Handles That Suit a Narrow Hallway")
p("Small round knobs, flush ring pulls or push-to-open catches sit close to the door and do not snag coats or bags. On a tall door, place the handle at a comfortable height on the opening side; on a short door at the low end, a small knob near the top edge is easiest to reach.")
h3("12. Light the Inside")
img(6)
p(f"An under stairs cupboard is dark at the back. A battery LED light that switches on when the door opens, or a short LED strip along the slope, helps you find things quickly. Plan the inside at the same time, with hooks at the tall end and shelves at the low end; our {a('diy-closet-shelves','DIY closet shelves')} guide and {a('shelf-spacing-calculator','shelf spacing calculator')} help with the layout.")
h2("Do Under Stairs Cupboard Doors Need to Be Fire Doors?")
p(f"In a typical two-storey house, not usually. It changes if your stairs form a protected escape route, for example after a loft conversion adds a third storey. One building control guide for loft conversions, from {ext(CNC,'CNC Building Control')}, says fire doors will be required to all habitable rooms and cupboards opening into the protected stairway. If you are planning a conversion, ask your building control body before choosing doors.")
h2("Common Under Stairs Cupboard Door Mistakes")
lst(["<strong>Measuring only once.</strong> Floors and stairs are rarely level, so measure both ends and the middle.",
"<strong>One huge door.</strong> A wide angled door is heavy and swings far into the hallway; two or three narrow doors are easier to use.",
"<strong>No gap around the door.</strong> Without a few millimetres of clearance it will stick when the paint goes on.",
"<strong>Blocking the gas meter or fuse board.</strong> Make sure the door opens fully in front of them.",
"<strong>Handles that stick out.</strong> In a narrow hallway they catch bags and shoulders.",
"<strong>A sealed cupboard full of damp coats.</strong> Leave room for air or use vented doors."])
h2("Under Stairs Cupboard Doors FAQ")
h3("What is the best door for an under stairs cupboard?")
p("For most homes, made-to-measure doors with angled tops that follow the stairs look the neatest. Split a long opening into two or three narrow doors. In a narrow hallway a sliding door at the tall end saves space, and on a budget a ledged door or a curtain is the cheapest option.")
h3("Can I put a normal door under the stairs?")
p("Yes, if the tall end of your under stairs space is high enough for a standard door. Fit it in a rectangular opening at the tall end and close in the sloping part with fixed panelling or a second, angled door. A standard door cannot fill the sloping part on its own.")
h3("Which side should an under stairs cupboard door be hinged?")
p("Hinge an angled door on a vertical edge, usually the taller one, which gives the hinges the most length. Think about how you will use the hallway: the door should open towards the free wall, not into the front door or the bottom step.")
h3("How do you stop an under stairs cupboard smelling musty?")
p("Let wet coats and shoes dry before you put them away, leave space so air can move, and use vented or slatted doors or a small gap at the bottom. Clear the cupboard out every few months, and look for signs of damp on the walls behind.")
h2("Final Thoughts")
p(f"The best under stairs cupboard doors follow the slope of the stairs, open easily in your hallway and keep the meter and fuse board within reach. Measure carefully, split long openings into narrow doors and pick a finish that blends in or stands out. For more ideas for the same space, see our {a('coat-closet-organization','coat closet organization')} and {a('downstairs-toilet-ideas','downstairs toilet ideas')} guides.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub('<[^>]+>',' ',re.sub(r'<svg.*?</svg>','',html,flags=re.S))
print(len(txt.split()),'words; kw',len(re.findall('under stairs cupboard door',txt,re.I)),'; ideas',len(re.findall(r'<h3 class="wp-block-heading">\d+\.',html)))
print(sorted(set(re.findall(r'dailyspacehacks\.com/([a-z0-9-]+)/',html))))
