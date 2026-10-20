from lib import *
import helpers as h
from helpers import p,h2,h3,lst,table,img,diagram,a,ext
P=788
rep(P,'These numbers come from a professional closet builder interviewed by','These numbers come from Scott Davis of storage maker ClosetMaid, interviewed by')
rep(P,'18 to 20 inches between shelves for small appliances and big items','18 to 20 inches between shelves for large items such as bags of potatoes')
rep(P,'If space is tight, 6 to 12 inch shelves work well for cans.','If space is tight, use shallow shelves: about 6 inches deep for spices and 10 to 12 inches up high.')
rep(P,'fill="#6E645C">small appliances, big items</text>','fill="#6E645C">large items, potato bags</text>')
rep(P,'text-anchor="middle">use 6 to 12 in shelves for cans</text>','text-anchor="middle">try 6 in deep shelves for spices</text>')
rep(P,'Spacing and depths based on advice from a professional closet builder. Adjust to the items you actually store.','Spacing and depths: ClosetMaid via The Kitchn; spice shelf depth: dimensions.com. Adjust to what you store.')
DIM=ext('https://www.dimensions.com/element/pantry-storage-depths','Dimensions.com')
def chart():
    h3('Pantry Shelf Measurements Chart')
    p('Two good sources give slightly different numbers, so here they are side by side. Use them as a range rather than a rule.')
    table(['Measurement','ClosetMaid (via The Kitchn)','Dimensions.com'],[
     ['Main shelf depth','16 to 20 in','14 to 16 in'],
     ['High shelf depth','about 12 in','10 to 12 in'],
     ['Spice shelf depth','not given','about 6 in'],
     ['Height for cans','6.5 to 7 in','6 to 10 in'],
     ['Height for cereal and general items','14 to 16 in','10 to 15 in'],
     ['Height for large or bulk items','18 to 20 in','16 to 18 in'],
     ['Bottom shelf off the floor','20 to 24 in','20 to 24 in'],
     ['Top shelf height','not given','about 84 in'],
     ['Space above the tallest item','at least 2 in','not given']])
    p('The two agree on the bottom shelf and differ a little on depth. Go deeper in a walk-in pantry full of bulk food, and shallower in a reach-in pantry, where anything behind the front row is easy to forget. '+DIM+' also puts the comfortable maximum reach at about 69 to 76 inches, so keep everyday food below that and use the very top shelf for backups.')
after(P,'and it works out the gaps for you.</p>\n<!-- /wp:paragraph -->',chart)
SVG=open('z.svg').read()
def layout():
    h3('Walk-In Pantry Layouts and Aisle Widths')
    p('Before you choose shelves, check that the walkway still works. '+DIM+' lists 36, 42 and 48 inches as typical walk-in pantry aisle widths, and 60 to 66 inches where a wheelchair needs to turn. Add the depth of the shelves on each shelved side, and you get the minimum width of the room.')
    diagram(SVG,'Walk-in pantry layouts: add the aisle to the shelf depth on each side to find how wide the room needs to be.')
    p('A U-shape gives the most storage but needs the widest room. A galley, with shelves on two facing walls, suits a long, narrow pantry. If your walk-in is under about 5 feet wide, shelves on one wall, or deep shelves on one side and shallow ones opposite, keep the aisle comfortable.')
after(P,'<h2 class="wp-block-heading">Walk-In Pantry Shelving Ideas</h2>\n<!-- /wp:heading -->',layout)
def wire():
    h3('How to Make Wire Pantry Shelves Work')
    img('p1')
    p('Many builder-grade pantries come with white wire shelves. You don&#8217;t have to rip them out; a few cheap fixes make them far easier to live with:')
    lst(['<strong>Add a shelf liner.</strong> A clear or solid liner cut to size gives jars and bottles a flat surface, so nothing tips through the gaps.',
     '<strong>Use risers and turntables.</strong> A step riser lifts the back row of cans into view, and a turntable stops oils and sauces getting lost in a corner.',
     '<strong>Group food in matching bins.</strong> Same-size bins sit flat across the wires and slide out like drawers.',
     '<strong>Put heavy jars on solid shelves.</strong> If you mix shelf types, keep wire for light boxes and bags, and use wood or laminate for glass jars and tins.'])
after(P,'and wood shelves where they show.</p>\n<!-- /wp:paragraph -->',wire)
def cleat():
    h3('Step by Step: Build Cleat Pantry Shelves')
    lst(['<strong>Mark the shelf lines.</strong> Use the measurements chart above to set each height, then draw a level line on the back and side walls and mark every stud.',
     '<strong>Fix the cleats.</strong> Cut 1x2 or 1x3 strips to length and screw them along each line, into at least two studs per strip.',
     '<strong>Cut the shelves.</strong> Use 3/4 in plywood or pine boards cut to the depth you chose. Where two shelves meet in a corner, overlap them or add a short cleat underneath to carry both.',
     '<strong>Stiffen long shelves.</strong> Glue and nail a 1x2 strip to the front edge. It hides the plywood layers and helps stop the shelf sagging under jars and cans.',
     '<strong>Finish before loading.</strong> Fill the screw holes, caulk the joints, then prime and paint with a durable semi-gloss or enamel so spills wipe off. Let the paint cure before you load the shelves.'],ordered=True)
after(P,'explains how to find studs and choose the right fasteners.</p>\n<!-- /wp:paragraph -->',cleat)
def light():
    h2('Lighting and Doors for Pantry Shelves')
    img('p2')
    p('Light makes deep shelves much easier to use. LED strips fixed under the front edge of each shelf light the shelf below without glare, and battery motion-sensor lights are an easy fix for a closet pantry with no wiring. For hard-wired lights or a new outlet, hire an electrician.')
    p('The door matters too. A sliding, pocket or barn door doesn&#8217;t swing into the pantry, so it leaves room for shelves on every wall. A hinged door is the one to keep if you want a rack on the back of it, like idea #6.')
before(P,'<!-- wp:heading -->\n<h2 class="wp-block-heading">How to Plan Pantry Shelves in 5 Steps</h2>',light)
rep(P,'<li><strong>Unsealed wood.</strong> Spills soak in and stain unless the shelves are painted or sealed.</li>\n<!-- /wp:list-item -->','<li><strong>Unsealed wood.</strong> Spills soak in and stain unless the shelves are painted or sealed.</li>\n<!-- /wp:list-item -->\n\n<!-- wp:list-item -->\n<li><strong>No light.</strong> A dark pantry hides the back of every shelf. Add LED strips or a motion-sensor light.</li>\n<!-- /wp:list-item -->')
rep(P,'<p>A common recommendation is 16 to 20 inches for main shelves and around 12 inches for the top shelf. Shallow shelves only a few inches deep work well for cans and spices.</p>','<p>Main pantry shelves are usually 14 to 20 inches deep: Dimensions.com gives 14 to 16 inches and ClosetMaid&#8217;s Scott Davis 16 to 20 inches. Keep high shelves around 10 to 12 inches and spice shelves about 6 inches, and choose the shallower end in a reach-in pantry so food doesn&#8217;t hide at the back.</p>')
def faq():
    h3('What is the best shelving for a pantry?')
    p('For most homes, adjustable shelving is the best choice, because you can move each shelf to fit what you store. Sealed wood or laminate gives a flat, solid surface for jars, while wire is cheaper and airier but needs a liner for small items. Keep eye-level shelves shallow enough that nothing hides.')
    h3('How wide should a walk-in pantry be?')
    p('Allow at least 36 inches of clear aisle, or 42 to 48 inches for a roomier walk-in, then add the shelf depth on each shelved side. With 16 inch shelves on two facing walls, the room needs to be about 68 inches wide; with shelves on one wall only, about 52 inches.')
    h3('How high should the top pantry shelf be?')
    p('Dimensions.com puts a typical top pantry shelf around 84 inches from the floor, but most people can only reach about 69 to 76 inches without a step. Use the top shelf for backups and rarely used items, keep a step stool nearby and store heavy things low.')
before(P,'<!-- wp:paragraph -->\n<p>Planning open shelves on a wall instead?',faq)
rep(P,'\n\n<!-- wp:paragraph -->\n<p>Want shelving with a sink, a coffee station and glass-front cabinets too? See our <a href="https://dailyspacehacks.com/butlers-pantry-ideas/">butler\'s pantry ideas</a> for layouts and sizes that fit any home.</p>\n<!-- /wp:paragraph -->','')
rep(P,'<p>A slim door rack holds spices, small jars and packets,','<p>A slim door rack holds '+a('spice-cabinet-organization','spices')+', small jars and packets,')
rep(P,'Plywood is strong and budget-friendly. Add','Plywood is strong and budget-friendly, and it is the same material we use in our '+a('diy-closet-shelves','DIY closet shelves')+'. Add')
rep(P,'a pull-out cabinet or shelves in another spot can work.','a pull-out cabinet or '+a('storage-ideas-for-small-spaces','shelves in another spot')+' can work.')
rep(P,'Get the shelves right first, and organizing the pantry becomes much easier.</p>','Get the shelves right first, and organizing the pantry becomes much easier. For the rest of the room, see our '+a('kitchen-storage-ideas','kitchen storage ideas')+'.</p>')
save('ops788.json')
