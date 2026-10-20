from lib import *
import helpers
img=lambda n: helpers.img(n)
from helpers import p,h2,h3,lst,table,a,ext
P=1286
WP=ext('https://www.whirlpool.com/blog/washers-and-dryers/laundry-sizing-guide.html','Whirlpool')
RTA=ext('https://blog.rtacabinetstore.com/cabinets-for-laundry/','RTA Cabinet Store&#8217;s laundry cabinet guide')
def sizes():
    h3('Washer and Dryer Sizes at a Glance')
    table(['Machine','Width','Height','Depth'],[
     ['Front-load washer or dryer','about 27 in','about 39 in','32 to 34 in'],
     ['Top-load washer','about 27 in','42 to 44 in, plus about 2 ft for the lid','27 to 28 in'],
     ['Stacked front-load pair','about 27 in','about 78 in','32 to 34 in'],
     ['Compact machines','about 24 in','33 to 36 in','24 to 26 in']])
    p('Add the gaps on top of these sizes: about 1 in at each side and 6 in behind. A side-by-side pair of full-size machines needs a space at least 56 in wide, Whirlpool says, before any cabinets. Sizes vary by model, so check the install guide of the machines you own.')
after(P,'6 in behind the machines for hoses and venting.</p>\n<!-- /wp:paragraph -->',sizes)
def high():
    h3('How High to Hang Laundry Room Wall Cabinets')
    p('Measured from the floor to the bottom of the wall cabinet, these are the heights we work to:')
    lst(['<strong>Over front-loaders with a counter:</strong> the machines are about 39 in tall, the gap about 1 in and the counter 1 to 1.5 in thick, so the counter top sits near 41 in. Add the usual 15 to 18 in kitchen gap, and the cabinets start about 56 to 60 in from the floor.',
     '<strong>Over a top-loader:</strong> the washer is 42 to 44 in tall and the lid needs about 24 in, so the bottom of the cabinet should be at least 66 to 68 in from the floor. Open the lid fully and measure, because lids differ.',
     '<strong>Over a stacked pair:</strong> about 78 in of machines leaves roughly 18 in below an 8 ft (96 in) ceiling. After a small gap, that fits a cabinet about 14 to 16 in tall.'])
    p('These are our own working numbers, built from the '+WP+' sizes above and standard kitchen spacing, not a building code. Before you fix anything, check that the cabinet doors clear the machine doors and that, except above a stacked pair, you can reach the lowest shelf without a step stool.')
after(P,'closing it tightly after use.</p>\n<!-- /wp:paragraph -->',high)
rep(P,'<p>Most laundry rooms use the same cabinet boxes as kitchens:','<p>Most laundry rooms use the same cabinet boxes as kitchens (our '+a('kitchen-storage-ideas','kitchen storage ideas')+' show more ways to use them):')
def cost():
    h3('What a Full Laundry Cabinet Project Costs')
    p(RTA+' gives a sample budget for an 8 x 10 ft laundry room: about $1,500 to $3,000 for cabinets, $800 to $2,000 for installation and plumbing, and $300 to $1,000 for extras such as a sink or pull-outs, or roughly $2,500 to $6,000 in total. The Bob Vila guide was last updated in 2023, so expect current prices to be somewhat higher.')
    h2('Best Materials and Hardware for a Damp Room')
    p('A laundry room sees steam, spills and the odd leaking hose, so the materials matter more than in most rooms:')
    lst(['<strong>Cabinet boxes:</strong> plywood holds up better to humidity than particleboard. If you buy particleboard or MDF boxes, seal every cut edge.',
     '<strong>Doors and finish:</strong> solid wood or painted MDF doors with a tough satin or semi-gloss paint that wipes clean.',
     '<strong>Counters:</strong> quartz and laminate shrug off water and detergent. Butcher block looks warm but needs sealing, especially around a sink.',
     '<strong>Hardware:</strong> soft-close hinges, full-extension slides for hampers and drawers.'])
after(P,'get quotes for anything custom.</p>\n<!-- /wp:paragraph -->',cost)
def store():
    h2('What to Store in Each Laundry Cabinet')
    table(['Cabinet','What goes in it','Tip'],[
     ['High wall cabinet','Detergent, pods, bleach, stain removers','Add a lock if children visit'],
     ['Other wall cabinets','Dryer sheets, spare lint filters, refills','Group refills in one bin'],
     ['Base cabinet or drawers','Hampers, sewing kit, lint rollers, rags','No chemicals in low drawers'],
     ['Tall cabinet','Broom, mop, vacuum, ironing board','Clips keep handles upright'],
     ['Sink base','Bucket, brushes, a soaking tub','A waterproof mat catches drips'],
     ['Open shelf','Folded towels, baskets','Matching baskets look calm']])
    p('Leave at least 36 in of clear floor in front of the cabinets and machines so their doors open fully, as '+RTA+' recommends. '+WP+' suggests about 4 ft in front of a front-loader for loading.')
after(P,'class="wp-image-1285"/></figure>\n<!-- /wp:image -->',store)
rep(P,'and a sink base with doors leaves room for a bucket and spare sponges.</p>','and a sink base with doors leaves room for a bucket and spare sponges. A drop-in sink is the easiest to fit into a laminate counter, while an undermount sink suits quartz or stone; if you skip the cabinet, a wall-mounted or freestanding utility sink does the same job.</p>')
rep(P,'screw the hooks into the frame of the door, not just the thin center panel.</p>','screw the hooks into the frame of the door, not just the thin center panel. If no door is wide enough, a pull-out ironing board that folds into a drawer does the same job.</p>')
rep(P,'narrow shelves down one side hold sprays and cloths.','narrow shelves down one side hold sprays and cloths (our '+a('shelf-spacing-calculator','shelf spacing calculator')+' sets the gaps).')
def bonus():
    h2('Bonus Ideas: Hidden Machines and a Mini Mudroom')
    h3('Hide the washer and dryer behind cabinet doors')
    img('l1')
    p('Paneled or bi-fold doors turn the washer and dryer into one more cabinet, which is ideal when the laundry is part of a kitchen or hallway. Size the opening from the machine sizes above plus the side and back gaps, check that the cabinet doors open fully past the machine doors, and leave room for the hoses and dryer vent. Heat and moisture need a way out, so check your dryer&#8217;s install guide for closet airflow, and consider louvered doors or a gap above them. Our '+a('european-laundry-ideas','European laundry ideas')+' show more machines tucked behind doors.')
    h3('Turn one end of the laundry wall into a mini mudroom')
    p('If the laundry room is also the way in from the garage or backyard, give one end a bench, a row of hooks and open cubbies for shoes and bags, with a tall cabinet for coats. A wipeable floor and a basket for each person keep it tidy. Our '+a('mudroom-ideas','mudroom ideas')+' cover benches, hooks and boot storage in more detail.')
    h2('Laundry Cabinet Colors and Styles')
    img('l2')
    p('Two-tone cabinets are an easy way to make a plain laundry room look designed: navy, deep green or wood base cabinets with white or cream uppers keep the top of the room light. In a small room, light colors are the safer choice; dark cabinets work best when the walls, counter and floor stay light.')
    p('Shaker doors suit a classic or farmhouse look, while flat slab doors look more modern and are easier to wipe down. Brass or black pulls finish either style. For paint colors, wall art and finishing touches, see our '+a('laundry-room-decor-ideas','laundry room decor ideas')+'.')
after(P,'check that the boxes are not swollen from water.</p>\n<!-- /wp:paragraph -->',bonus)
def faq():
    h3('How much does it cost to add cabinets to a laundry room?')
    p('Cabinets alone run from about $250 to $2,000, with countertops another $300 to $1,400, according to Bob Vila&#8217;s guide (updated 2023). A fuller project for an 8 x 10 ft room, with installation, plumbing and extras such as a sink, is about $2,500 to $6,000 in RTA Cabinet Store&#8217;s sample budget.')
    h3('Can you put a washer and dryer in a closet with cabinets?')
    p('Yes, if the closet fits the machines plus their gaps: about 1 in at each side and 6 in behind. A stacked front-load pair is about 27 in wide and 78 in tall, so a shallow cabinet can go above it. Check the dryer&#8217;s install guide for closet airflow and venting before you close it in.')
    h3('What is the best layout for laundry room cabinets?')
    p('For most rooms, a single wall works best: machines side by side under a counter, a tall cabinet at one end and wall cabinets above. Leave about 36 in of clear floor in front, and keep detergent in a high, locked cabinet. In a narrow room, stack the machines and use the freed wall for base cabinets.')
after(P,'and keep one high, lockable cabinet for detergent.</p>\n<!-- /wp:paragraph -->',faq)
save('ops1286.json')
