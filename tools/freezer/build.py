import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={
"es":"https://www.energystar.gov/products/freezers",
"doe":"https://www.energy.gov/node/4821127",
"eia":"https://www.eia.gov/TOTALENERGY/data/monthly/pdf/sec9_11.pdf",
"usda":"https://usda.gov/media/press-releases/2013/05/23/usda-food-safety-tips-areas-affected-severe-storms-and-tornadoes",
"cr":"https://www.consumerreports.org/appliances/freezers/buying-guide",
"hd":"https://www.homedepot.com/c/ab/best-freezers-for-your-home/9ba683603be9fa5395fab9053d40619",
"ge":"https://www.ajmadison.com/cgi-bin/ajmadison/FCM7SKWW.html",
"fr":"https://www.ajmadison.com/cgi-bin/ajmadison/FFUE1326AW.html",
"clr":"https://pdf.lowes.com/productdocuments/94725213-1657-4e0f-a0e6-71aaf8f23f03/04094414.pdf",
"wp":"https://producthelp.whirlpool.com/Refrigeration/Freezers/Product_Info/Product_Assistance/How_to_Defrost_the_Freezer",
"cpsc":"https://www.cpsc.gov/Recalls/2000/cpsc-appliance-manufacturers-announce-voluntary-recall-initiative-for-old-chest"}
def SR(k,t): return ext(SRC[k],t)
P=0.1834
c_yr,u_yr=215*P,395*P

p(f"Choosing between a chest freezer and an upright freezer? A chest freezer wins on price and running costs, and an upright wins on floor space and organization. ENERGY STAR says a chest model is {SR('es','usually more energy efficient')} because the door opens from the top, and Consumer Reports says chest freezers cost less to buy. An upright fits a smaller footprint and keeps food on shelves where you can see it.")
lst(["<strong>Pick a chest freezer</strong> if you buy in bulk, have floor space in a basement or garage, and want the lowest running cost.",
"<strong>Pick an upright freezer</strong> if floor space is tight, you hate digging for food, or bending down is hard.",
"<strong>Either works</strong> as a small second freezer for a household of two."])
img(1)

h2("Chest Freezer vs Upright Freezer at a Glance")
table(["","Chest freezer","Upright freezer"],[
["Price (Consumer Reports)",SR('cr','about $170 to $1,200'),"about $450 to $2,100"],
["Energy use (ENERGY STAR example)",SR('es','about 215 kWh a year'),"about 395 kWh a year"],
["Yearly cost at 18.34¢/kWh (our estimate)",f"about ${c_yr:.0f}",f"about ${u_yr:.0f}"],
["Floor space, 22 cu ft","about 2 x 6 ft","about 2.5 x 2.5 ft"],
["Organization","Baskets and bins; items get buried","Shelves, drawers, door bins"],
["Defrosting","Most are manual","Many are frost-free"]])
diagram(open('z.svg').read(),f"A 7 cu ft chest takes more floor than a 13 cu ft upright, but an ENERGY STAR chest uses about ${c_yr*12:,.0f} of electricity over 12 years against about ${u_yr*12:,.0f} for an upright.")
p(f"The running cost estimates use ENERGY STAR's example energy figures and the June 2026 US average residential electricity price from the Energy Information Administration: {SR('eia','18.34 cents per kWh')}. ENERGY STAR's own figures of about $30 and $60 a year assume a lower electricity rate. Over the 12-year lifetime ENERGY STAR uses in its calculations, its example chest freezer saves roughly $400.")

h2("Chest Freezers: Best for Bulk Buying and Low Bills")
img(2)
p("<strong>Best for:</strong> large families, hunters and bulk shoppers, and anyone with space in a basement or garage.")
p(f"A chest freezer holds more for the money and lets less cold air escape when you open the lid. Consumer Reports notes a 22 cubic foot chest {SR('cr','takes up a 2x6-foot area')}, against a 2½ x 2½ foot area for an upright of the same size, and shelves and bins in uprights take up more space than in chest freezers, up to 20 percent. A 7 cu ft chest such as GE's FCM7SKWW measures about {SR('ge','37.5 x 21.75 inches')} and rises to about 53 inches with the lid open, so leave headroom above it.")
p(f"<strong>Avoid if:</strong> you want to find things quickly. Consumer Reports says chest freezers {SR('cr','can be harder to organize')} even with hanging baskets, and most need defrosting by hand. Whirlpool {SR('wp','advises defrosting')} when frost has built up to about 1/4 inch, and at least once a year. Sorting food into bins by type, with the newest at the bottom, makes it easier.")

h2("Upright Freezers: Best for Small Spaces and Easy Access")
img(3)
p("<strong>Best for:</strong> kitchens, laundry rooms and apartments, and anyone who wants food at eye level.")
p(f"An upright freezer works like a refrigerator: shelves, drawers and door bins keep everything in sight. Frigidaire's 13 cu ft frost-free upright is {SR('fr','27.75 inches wide')} and designed to run in temperatures from 0°F to 110°F. Many uprights are frost-free, which is convenient, but ENERGY STAR says {SR('es','manual defrost freezers use half the energy')} of automatic defrost models, and uprights use more electricity overall.")
p(f"<strong>Avoid if:</strong> running costs come first, or you store large, awkward items such as whole turkeys. If you need more kitchen space for the overflow, our {a('kitchen-storage-ideas','kitchen storage ideas')} and {a('pantry-organization-ideas','pantry organization ideas')} can help.")

h2("How to Size and Place Either One")
lst([f"<strong>Size:</strong> Home Depot suggests {SR('hd','2.5 to 3 cubic feet of space per person')}, so about 12 cu ft for a family of four.",
f"<strong>Space:</strong> leave room for air. A Frigidaire chest freezer spec sheet asks for {SR('clr','3\" minimum clearance on all sides')} and ENERGY STAR says to leave a few inches between the freezer and the wall.",
f"<strong>Temperature:</strong> set it to 0°F. The Department of Energy says a freezer {SR('doe','should be set at 0 degrees Fahrenheit')}.",
f"<strong>Garage:</strong> ENERGY STAR recommends keeping a freezer indoors unless your climate is mild. If it must go in a garage, choose a model rated for garage temperatures and {SR('cr','check the range on the spec sheet')}."])

h2("Power Outages and Safety")
p(f"A full freezer holds its cold longer. The USDA says {SR('usda','a full freezer will keep its temperature for about 48 hours')}, or about 24 hours if half full. Keep the freezer door closed as much as possible. If you have an old latch-style chest freezer (made roughly 1945 to 1970) you no longer use, the Consumer Product Safety Commission has warned that children have suffocated in them and advises people to {SR('cpsc','properly dispose of these non-working freezers immediately or disable the latch')} if disposal is impossible.")

h2("Our Pick")
lst(["<strong>Family of four with a basement:</strong> a 12 to 15 cu ft chest freezer with baskets and bins.",
"<strong>Apartment or small kitchen:</strong> a compact upright, which needs the least floor space.",
"<strong>Garage:</strong> whichever type you choose, buy a garage-ready model.",
"<strong>Bad back:</strong> an upright, so most food is on shelves you can reach without leaning into a deep chest."])

h2("Decide in Five Questions")
lst(["Do you have a 6-foot stretch of floor for a large freezer? <strong>No:</strong> upright.",
"Do you buy meat or produce in bulk? <strong>Yes:</strong> chest.",
"Is the lowest electric bill your top priority? <strong>Yes:</strong> chest.",
"Do you open the freezer several times a day? <strong>Yes:</strong> upright.",
"Will it live in a garage? <strong>Yes:</strong> either, but garage-rated."],ordered=True)
p(f"Planning a utility space around it? Our {a('small-laundry-room-ideas','small laundry room ideas')} and {a('garage-storage-ideas','garage storage ideas')} show how to fit a freezer in.")
ai_note()
html='\n\n'.join(out)
html=re.sub(r'(\d+\.\d{2})\d+',r'\1',html)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('chest freezer vs upright freezer'),'kw')
