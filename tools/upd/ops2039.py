from lib import *
from helpers import p,h2,h3,lst,table,img,a,ext
P=2039
IH=ext('https://www.idealhome.co.uk/utility-room/utility-room-ideas/small-utility-room-ideas-35169','Ideal Home')
HB=ext('https://www.heritagebuildgroup.co.uk/post/utility-room-ideas','Heritage Build Group')
BO=ext('https://www.bosch-home.co.uk/customer-service/get-support/installation-hub/washer-dryer-stacker-installation','Bosch')
ADF=ext('https://assets.publishing.service.gov.uk/media/61deba42d3bf7f054fcc243d/ADF1.pdf','Approved Document F')
MB=ext('https://www.mybuilder.com/extensions/price-guides/utility-room-cost','MyBuilder&#8217;s utility room cost guide')
def space():
    h3('How Much Space Does a Small Utility Room Need?')
    p('Less than you might think: a kitchen designer quoted by '+IH+' says a utility can fit into as little as 0.36 m² if you build upwards, about the footprint of one 60 cm machine with a second stacked on top, while the average utility room is about 2.5 to 5 m². Use these sizes as a starting point:')
    lst(['<strong>One wall of units:</strong> about 1.5 to 1.8 m of wall for the machines and a sink or worktop, plus about 1 m of clear floor in front so you can open the doors and load comfortably ('+HB+').',
     '<strong>Stacked machines:</strong> a column about 60 cm wide and at least 170 cm tall, because each machine is roughly 85 cm high before you add the stacking kit ('+BO+').',
     '<strong>A washer dryer only:</strong> one 60 cm space under a worktop, the smallest option if there is no room for two machines.'])
    h3('Long, Narrow Utility Rooms')
    img('u1')
    p('In a corridor-shaped utility, put the machines, sink and tall cupboard on one wall and keep the opposite side for shallow storage, such as slim open shelves or wall cupboards, so the walkway stays clear. '+HB+' suggests units on both walls only when the room is about 2 m wide. In anything narrower, open doors and drawers clash in the middle.')
after(P,'with a vent pipe that is not kinked, blocked or crushed.</p>\n<!-- /wp:paragraph -->',space)
rep(P,'show how to use the rest of the slope.</p>','show how to use the rest of the slope, and our '+a('under-stairs-cupboard-doors','under stairs cupboard doors')+' guide shows how to close it off neatly.</p>')
def loo():
    p('In a shared room, a washer dryer or a stacked pair behind a cupboard door keeps the space feeling like a cloakroom. Plan the extractor fan early. In England, '+ADF+' sets a minimum intermittent extract rate of 30 litres per second for a utility room, so check the fan&#8217;s rating before you buy.')
after(P,'covers the space a loo needs and the ventilation rules to check.</p>\n<!-- /wp:paragraph -->',loo)
rep(P,'Either way, follow the manual for the space it needs around it.</p>','Either way, follow the manual for the space it needs around it. If it smells of burning, leaves clothes hotter than usual or takes longer to dry, clean the filter and check the vent pipe straight away; if the problem continues, stop using it and have it checked by a qualified engineer.</p>')
def cost():
    h2('How Much Does a Small Utility Room Cost?')
    p('It depends on whether you refresh the room you have or build a new one. These typical UK prices come from '+MB+':')
    table(['Project','Typical cost'],[
     ['Paint and decorating','£100 to £300'],
     ['New units','£200 to £800'],
     ['New flooring','£500 to £1,000'],
     ['New lighting','from £100'],
     ['Small utility room conversion','£10,000 to £15,000'],
     ['Utility room extension','£7,500 to £25,000'],
     ['Garage conversion','£10,000 to £25,000'],
     ['Appliance upgrades','£1,000 to £3,000']])
    p('Costs rise quickly when water, waste or power has to be moved, so a refresh that keeps the machines where they are is by far the cheapest option.')
before(P,'<!-- wp:heading -->\n<h2 class="wp-block-heading">Easy Updates and Ideas on a Budget</h2>',cost)
rep(P,'can change the room for a fraction of the cost of a refit.</p>','can change the room for a fraction of the cost of a refit. Moving seasonal kit up into the loft frees shelf space too: see our '+a('loft-storage-ideas','loft storage ideas')+'.</p>')
def faq():
    h3('How much does it cost to build a utility room?')
    p('A refresh can cost a few hundred pounds: paint from about £100 and new units from £200. MyBuilder puts a small utility room conversion at about £10,000 to £15,000 and a utility room extension at £7,500 to £25,000. Moving water, waste or power adds the most to the bill.')
    h3('What usually goes in a utility room?')
    p('A washing machine and tumble dryer, or a washer dryer, a sink, a worktop for folding and a tall cupboard for the mop, broom, vacuum and ironing board. Most also have shelves for detergents and an airer for drying, and some house a spare fridge or freezer.')
    h3('What is a bootility room?')
    p('A bootility is a utility room that doubles as a boot room, usually by the back door. It combines the washing machine and sink with a bench, coat hooks, boot storage and a hard-wearing floor, so muddy kit and laundry are dealt with in one place before they reach the rest of the house.')
    h3('What is the smallest size for a utility room?')
    p('A kitchen designer quoted by Ideal Home has fitted working utilities into as little as 0.36 m² by building upwards, about the footprint of one 60 cm machine. A single run of units is easier to use: allow about 1.5 to 1.8 m of wall and about 1 m of clear floor in front.')
before(P,'<!-- wp:paragraph -->\n<p>If your utility room is also the way in from the garden,',faq)
save('ops2039.json')
