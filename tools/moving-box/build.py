from helpers import *
import helpers
IMG={1:(2333,"moving-box-calculator-01-packed-boxes.jpg","Moving box calculator: stacks of sealed cardboard moving boxes in several sizes and a wardrobe box with shirts on hangers in a bright living room on moving day"),
2:(2335,"moving-box-calculator-02-box-sizes.jpg","Four sealed cardboard moving boxes lined up from small to extra-large on a wood floor, with flat boxes leaning against the wall")}
helpers.IMG=IMG
UH='https://www.uhaul.com/MovingSupplies/Boxes/Standard-Sized-Moving-Boxes/Small-Moving-Box?id=3245'
UHD='https://www.uhaul.com/MovingSupplies/Boxes/Double-Wall-Boxes/Dish-Barrel-Box?id=2573'
MP='https://www.movingplace.com/moving-advice/how-many-moving-boxes-do-i-need'
RF='https://www.redfin.com/blog/2016/03/moving-soon-this-guide-will-help-you-figure-out-how-many-boxes-you-need.html'

p("How many boxes do you need to move? This free <strong>moving box calculator</strong> estimates how many small, medium, large, wardrobe and dish boxes your home needs, room by room, plus the packing tape and paper to buy.")
p("Pick your home size, change the rooms to match yours and say how much stuff you own. A typical two-bedroom apartment is filled in, and the box list updates as you type, so you can copy it or print it before you shop.")
add('<!-- wp:html -->\n'+open('tool.html').read()+'\n<!-- /wp:html -->')

h2("How Many Moving Boxes Do I Need?")
p(f"Most homes need somewhere between 20 and 160 boxes, depending on the number of rooms and how much is in them. The moving supply guide at {ext(MP,'Moving Place')} gives these ranges for an average move, and our moving box calculator lands inside them for each home size:")
table(["Home size","Average move (Moving Place)","Our calculator, average stuff"],
[["Studio","20–30 boxes","25 boxes"],
 ["1-bedroom apartment","30–40 boxes","37 boxes"],
 ["2-bedroom apartment","50–60 boxes","50 boxes"],
 ["3-bedroom house","80–100 boxes","83 boxes"],
 ["4-bedroom house","100–125 boxes","114 boxes"],
 ["5+ bedroom house","130–160 boxes","136 boxes"]])
p(f"Light packers can need about a third fewer boxes, and homes with full closets, lots of books or a packed garage can need a third more. A quick rule from a packaging supplier quoted by {ext(RF,'Redfin')} is 10 to 15 boxes per room, and the same article cites a box seller's advice to buy about 10 percent more than your estimate, so a few spare boxes are always on hand for the last-minute items.")
img(1)

h2("Moving Box Sizes and What to Pack in Each")
p("Pack heavy items in small boxes and light items in large ones. A large box full of books is too heavy to lift safely and can split, while a small box of pillows wastes space. These are typical sizes for standard US moving boxes:")
diagram(open('z.svg').read(),"Moving box sizes: small boxes for heavy items like books and dishes, medium and large boxes for kitchen items, toys and bedding, extra-large boxes for light bulky things, a wardrobe box for hanging clothes and a double-wall dish pack for plates and glasses.")
table(["Box","Typical size","Volume","Best for"],
[["Small","16.4 x 12.6 x 12.6 in (42 x 32 x 32 cm)","1.5 cu ft","Books, dishes, canned food, tools"],
 ["Medium","18 x 18 x 16 in (46 x 46 x 41 cm)","3 cu ft","Kitchen items, toys, decor, shoes"],
 ["Large","18 x 18 x 24 in (46 x 46 x 61 cm)","4.5 cu ft","Bedding, towels, pillows, lampshades"],
 ["Extra-large","24 x 18 x 24 in (61 x 46 x 61 cm)","6 cu ft","Comforters, cushions, light bulky items"],
 ["Wardrobe","About 24 in (61 cm) wide","Varies","Clothes on hangers"],
 ["Dish pack","18 x 18 x 28 in (46 x 46 x 71 cm)","5.25 cu ft","Plates, glasses, china"]])
p(f"The sizes come from {ext(UH,'U-Haul')}, which rates its small box for up to 65 lb (the box's strength limit, not a comfortable lifting weight) and recommends it for books, tools and canned food. Its double-walled {ext(UHD,'Dish Barrel box')} measures 18 x 18 x 28 in and is made for dishes, glassware and other fragile items, with a divider kit sold separately. Other stores sell slightly different sizes, so compare the dimensions rather than the names.")
img(2)

h2("How Many Boxes per Room")
p("Every room packs differently. Kitchens fill the most boxes for their size because of dishes, glasses and pantry food, while bathrooms need only a few. These are the average counts the moving box calculator uses before adjusting for how much you own:")
table(["Room","Small","Medium","Large and XL","Specialty"],
[["Main bedroom","3","4","4","2 wardrobe boxes"],
 ["Other bedroom","2","3","3","1 wardrobe box"],
 ["Living room","3","4","4","–"],
 ["Kitchen (2 bedrooms)","5","5","2","2 dish packs"],
 ["Dining room","2","2","1","1 dish pack"],
 ["Bathroom","2","1","–","–"],
 ["Home office","4","3","1","–"],
 ["Garage, basement or attic","3","4","6","–"]])
p(f"For hanging clothes, {ext(MP,'Moving Place')} suggests about one wardrobe box for every 2 feet (61 cm) of closet rail, and one or two dish packs per kitchen. Our own rule of thumb: if your garage, basement or attic is full, count it as two rooms. Our {a('how-to-declutter-your-home','guide to decluttering your home')} helps you cut the pile before you pack.")

h2("Packing Supplies Checklist")
p("Boxes are only half the shopping list. Buy these at the same time so packing day does not stop halfway:")
lst(["<strong>Packing tape.</strong> Wide 2 in (48 mm) tape and a tape gun. Plan on roughly one roll for every 15 boxes, because each box needs tape across the bottom and top seams.",
"<strong>Packing paper.</strong> Plain newsprint for wrapping dishes and glasses. Newspaper ink can rub off on plates.",
"<strong>Bubble wrap.</strong> One roll for lamps, frames, mirrors and electronics.",
"<strong>Markers and labels.</strong> Write the room and a short list of contents on two sides of every box, not the top, so you can read them when boxes are stacked.",
"<strong>Furniture pads or blankets.</strong> To protect furniture, mirrors and floors on moving day."])
add('<!-- wp:html -->\n<div class="dsh-save" style="display:flex;flex-wrap:wrap;align-items:center;gap:24px;background:#F7F1E9;border:1px solid #E6DCCF;border-radius:16px;padding:24px;margin:2em 0;"><a href="SAVEURL" target="_blank" rel="noopener" style="flex:0 0 200px;max-width:200px;margin:0 auto;"><img src="https://dailyspacehacks.com/wp-content/uploads/2026/10/moving-box-calculator-pin-01.jpg" alt="How many moving boxes do I need: a stack of cardboard moving boxes beside a wardrobe box with shirts on hangers" width="200" data-pin-media="https://cdn.jsdelivr.net/gh/mohamedelber/dsh-pins@main/src/moving-box/pins/moving-box-calculator-pin-01.jpg" style="width:200px;height:auto;border-radius:10px;display:block;"></a><div style="flex:1 1 260px;"><p style="font-weight:700;font-size:1.25em;margin:0 0 .4em;">Save the calculator</p><p style="margin:0 0 1em;">Pin it so the box list is on your phone when you shop for boxes and supplies.</p><a href="SAVEURL" target="_blank" rel="noopener" style="display:inline-block;background:#E60023;color:#fff;font-weight:700;text-decoration:none;padding:12px 22px;border-radius:999px;white-space:nowrap;line-height:1.2;">Save to Pinterest</a></div></div>\n<!-- /wp:html -->'.replace('SAVEURL','https://www.pinterest.com/pin/create/button/?url=https%3A%2F%2Fdailyspacehacks.com%2Fmoving-box-calculator%2F&amp;media=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fmohamedelber%2Fdsh-pins%40main%2Fsrc%2Fmoving-box%2Fpins%2Fmoving-box-calculator-pin-01.jpg&amp;description=Moving%20box%20calculator%3A%20how%20many%20moving%20boxes%20do%20I%20need%3F'))

h2("How to Use Fewer Moving Boxes")
lst(["<strong>Declutter first.</strong> Every item you donate is one you do not have to wrap, carry and unpack. Start with closets using our {}.".format(a('closet-clean-out','closet clean-out checklist')),
"<strong>Pack soft things in what you already own.</strong> Suitcases, duffel bags and laundry baskets hold clothes, towels and bedding.",
"<strong>Leave light items in drawers.</strong> Many movers let you leave clothes in dresser drawers if the dresser is not too heavy to carry. Ask your mover first.",
"<strong>Use wardrobe boxes for hanging clothes.</strong> They hold clothes on their hangers, so you skip folding and the closet is ready to fill on day one.",
"<strong>Eat down the pantry and freezer.</strong> Plan meals for the last two weeks so there is less food to pack."])
p(f"Once you arrive, unpack the kitchen and bedrooms first. Our guides on {a('how-to-organize-kitchen-cabinets','how to organize kitchen cabinets')} and {a('small-closet-organization-ideas','small closet organization ideas')} help you set up the new place, and our {a('storage-ideas-for-small-spaces','storage ideas for small spaces')} are useful if you are moving somewhere smaller.")

h2("Moving Box FAQ")
h3("How many boxes do I need for a 1-bedroom apartment?")
p("Plan on about 30 to 40 boxes for an average 1-bedroom apartment, or 20 to 30 if you own very little. That is usually around 12 small, 13 medium, 9 large or extra-large, 2 wardrobe boxes and 1 dish pack.")
h3("How many boxes do I need for a 2-bedroom apartment?")
p("An average 2-bedroom apartment needs about 50 to 60 boxes. Light packers can manage with about 40, and a home with lots of books, toys or a storage unit can need 65 to 75.")
h3("How many boxes do I need for a 3-bedroom house?")
p("A 3-bedroom house with a garage typically needs about 80 to 100 boxes. Garages, basements and attics vary the most, so look inside them before you buy.")
h3("How many wardrobe boxes do I need?")
p(f"A common rule of thumb from {ext(MP,'Moving Place')} is about one wardrobe box for every 2 feet (61 cm) of closet rail. Fold what you can into regular boxes and keep wardrobe boxes for shirts, dresses and coats that crease.")
h3("Where can I get moving boxes?")
p("You can buy new boxes from moving truck rental companies, home improvement stores and online, or look for used boxes through local buy-and-sell groups and neighbors who just moved. Check used boxes for damp, crushed corners and pests before you pack them.")

h2("More Planning Tools")
p(f"Planning the new place? Try our {a('curtain-size-calculator','curtain size calculator')} for new windows, the {a('washer-dryer-space-calculator','washer and dryer space calculator')} to check that your machines fit, and the {a('shelf-spacing-calculator','shelf spacing calculator')} for closets and pantries.")
add('<!-- wp:paragraph {"className":"dsh-ai-note","fontSize":"small"} -->\n<p class="dsh-ai-note has-small-font-size"><em>How this tool was made: built with the help of AI tools, tested in the browser and published by Mohamed Elber. Results are planning estimates based on box-count ranges published by moving supply companies; box sizes vary by store. Images are AI-generated illustrations. See our <a href="https://dailyspacehacks.com/editorial-policy/">Editorial Policy</a>.</em></p>\n<!-- /wp:paragraph -->')
html='\n\n'.join(helpers.out)
open('content.html','w').write(html)
import re
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script>.*?</script>|<style>.*?</style>|<svg.*?</svg>','',html))
print(len(html),'words',len(txt.split()),'kw',html.lower().count('moving box calculator'),'how many boxes',txt.lower().count('how many'))
