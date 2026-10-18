import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
FCI="https://www.fcilondon.co.uk/blog/how-deep-should-built-in-wardrobes-be"
DIM="https://www.dimensions.com/element/reach-in-closets"
HG="https://www.dimensions.com/element/ikea-bumerang-coat-hanger"
EM="https://shop.emuca.com/wardrobes/accessories/self/self-pull-out-wardrobe-rail-62106"
p("What is the right <strong>wardrobe depth</strong>? For hanging clothes on a normal side-to-side rail, plan about 60 cm (24 in) deep with hinged doors and about 71 cm (28 in) with sliding doors. This free calculator gives you the answer for your wardrobe in two taps and checks whether the space you have is deep enough.")
p("Pick the door type and what goes inside, and the depth appears straight away. Open <em>More options</em> to enter the depth of your alcove or wall, and it tells you whether a standard rail fits, whether it is tight, or whether you need a pull-out rail or shelves instead.")
add('<!-- wp:html -->\n'+open('tool.html').read()+'\n<!-- /wp:html -->')
h2("Standard Wardrobe Depth")
table(["Wardrobe","Depth to plan","Why"],[
["Hinged doors, hanging rail","60 cm (24 in)","Hangers about 46 cm wide plus room in front and behind"],
["Sliding doors, hanging rail","71 cm (28 in)","66 cm inside plus about 5 cm for the door track"],
["Open wardrobe or rail, no doors","60 cm (24 in)","Same hanging space, nothing to close"],
["Shelves and drawers only","55 cm (22 in)","No hanging rail, so it can be shallower"],
["Sliding doors, shelves only","60 cm (24 in)","55 cm plus about 5 cm for the track"],
["Absolute minimum for a side-on rail","about 51 cm (20 in) inside, about 56 cm with sliding doors","FCI advises 60 cm; below that a standard rail is a squeeze and clothes will touch the doors"],
["Pull-out (end-on) rail","from about 30 cm (12 in) inside","Clothes hang front to back"]])
p(f"These figures come mainly from two planning guides. London fitted-furniture maker FCI's guide to {ext(FCI,'how deep built-in wardrobes should be')} gives 600 mm for a hinged-door wardrobe, says anything under 60 cm means you cannot use a standard horizontal hanging rail, allows 55 cm if you are not hanging clothes, and recommends 660 mm plus a running track of about 50 mm for sliding doors. Dimensions.com's {ext(DIM,'reach-in closet guide')} recommends 24 in (61 cm) as a comfortable depth and says closets as shallow as 20 in (50.8 cm) can be used.")
img(1)
h2("Why Wardrobes Are About 60 cm Deep")
p(f"It comes down to the hanger. A standard adult hanger such as IKEA's Bumerang is 18 in (45.7 cm) wide according to {ext(HG,'Dimensions.com')}, and clothes on a side-to-side rail hang at that width. Add the thickness of the back panel and doors and a little air in front and behind so shirts are not crushed, and you arrive at about 60 cm outside. Bulky winter coats need a few centimetres more, so if your wardrobe holds mostly coats, go for the deeper end; FCI's luxury range is 650 to 680 mm.")
h2("Can a Wardrobe Be 50 cm Deep?")
p("Yes, but not with a normal side-to-side rail and standard hangers. At 50 cm outside, the inside is usually around 45 to 47 cm once the back panel and doors are taken off, which is about the width of the hanger itself, so clothes press against the doors and get creased. In a 50 cm wardrobe you have three better options:")
lst(["<strong>A pull-out rail.</strong> Clothes hang front to back on a rail that slides out. One made by fittings maker Emuca needs a {0} of just 302 mm.".format(ext(EM,'minimum inside depth')),
"<strong>Slim hangers and short clothes.</strong> Children's clothes and slim hangers can work on a side-on rail in a tight space.",
"<strong>Shelves and drawers.</strong> Use the shallow wardrobe for folded clothes and keep hanging clothes elsewhere."])
h2("Sliding or Hinged Doors?")
img(2)
p("Sliding doors save floor space in front of the wardrobe, which helps in a narrow bedroom, but the track takes about 5 cm of depth, so the wardrobe itself has to be deeper. Hinged doors need a clear arc of floor to swing open, roughly as wide as each door, but the wardrobe can be shallower. In a box room with the bed close to the wardrobe, measure the door swing before you choose.")
h2("Shallow Wardrobe and Alcove Ideas")
img(3)
p(f"If an alcove beside a chimney breast is only 30 to 45 cm deep, turn it into shelving for folded clothes, shoes and baskets, or fit a pull-out rail. Our {a('box-room-bedroom-ideas','box room bedroom ideas')} and {a('small-bedroom-storage-ideas','small bedroom storage ideas')} have more ways to fit storage into tight rooms, and our {a('loft-storage-ideas','loft storage ideas')} cover wardrobes under a sloping ceiling.")
h2("How to Measure for a Wardrobe")
lst(["<strong>Measure the depth</strong> from the back wall to where the front of the wardrobe can come, at skirting-board height and higher up. Use the smaller figure.",
"<strong>Check what is in the way:</strong> skirting boards, sockets, radiators, coving and window frames.",
"<strong>Measure the width and height</strong>, and the floor space in front for the doors to open.",
"<strong>Enter the depth</strong> under More options in the calculator to see what fits."],True)
add(open('savebox.html').read())
h2("Wardrobe Depth FAQ")
h3("What is the standard depth of a wardrobe?")
p("A standard wardrobe with hinged doors and a side-to-side hanging rail is about 60 cm (24 in) deep. With sliding doors, plan about 71 cm (28 in) because the door track takes extra depth. A wardrobe with only shelves and drawers can be about 55 cm (22 in) deep.")
h3("How deep does a wardrobe need to be for hangers?")
p("A standard adult hanger is about 46 cm (18 in) wide, so a wardrobe needs to be deeper than that inside for a side-on rail. Plan around 60 cm outside for comfortable hanging; Dimensions.com says closets as shallow as 51 cm (20 in) can work, but FCI warns anything under 60 cm rules out a standard rail.")
h3("Is 50 cm deep enough for a wardrobe?")
p("A 50 cm wardrobe is too shallow for a normal side-to-side rail with standard hangers, because the inside is barely wider than the hanger. It works well with a pull-out rail that hangs clothes front to back, with slim hangers for small clothes, or as shelving for folded clothes.")
h3("How deep is a sliding door wardrobe?")
p("Plan about 71 cm (28 in) for a sliding door wardrobe with a hanging rail: around 66 cm for the hanging space plus about 5 cm for the door track. If your space is shallower, hinged doors or an open wardrobe will give you more usable depth.")
h2("More Planning Tools")
p(f"Planning the whole bedroom? Try our {a('curtain-size-calculator','curtain size calculator')}, {a('rug-size-calculator','rug size calculator')} and {a('tv-mounting-height-calculator','TV mounting height calculator')}.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script.*?</script>|<style.*?</style>','',html))
print(len(html),'words',len(txt.split()),'kw',txt.lower().count('wardrobe depth'))
print(sorted(set(re.findall(r'dailyspacehacks\.com/([a-z0-9-]+)/',html))))
