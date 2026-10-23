import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={
"ofgem":"https://ofgem.gov.uk/news/changes-energy-price-cap-between-1-october-and-31-december-2026",
"which_ban":"https://www.which.co.uk/news/article/the-tumble-dryer-ban-what-does-it-mean-for-you-alPRI3r8KXPx",
"retra":"https://retra.co.uk/news/tumble-dryer-sales-restrictions-to-come-into-force-in-2027/",
"gov":"https://assets.publishing.service.gov.uk/media/6888ab90048fff613a4d5acd/raising-standards-for-household-tumble-dryers.pdf",
"lab392":"https://www.legislation.gov.uk/eur/2012/392",
"currys_tt":"https://www.currys.co.uk/techtalk/kitchen-and-home/laundry-advice/heat-pump-vs-condenser-tumble-dryers.html",
"beko_pros":"https://www.beko.co.uk/lifestyle/heat-pump-tumble-dryers-efficiency-pros-and-cons",
"beko_garage":"https://www.beko.co.uk/support/faqs/tumble-dryers/can-i-put-a-tumble-dryer-in-my-garage",
"which_garage":"https://www.which.co.uk/news/article/can-i-put-my-laundry-appliances-in-the-garage-a5ecl4S26lJk",
"beko_where":"https://www.beko.co.uk/support/faqs/tumble-dryers/where-can-you-put-a-tumble-dryer",
"hoover_man":"https://service.hoover.co.uk/media/giemhlfv/atd-c10tkex-31101120-instruction-manual-pdf.pdf",
"miele":"https://media.miele.com/downloads/5a/41/01_C7F12828AC5F1FE0979321FE0E875A41.pdf",
"beko_man":"https://www.manualslib.com/manual/3479434/Beko-Bm3t4724ww.html",
"hp_vent":"https://www.appliancesdirect.co.uk/PDFs/TVFS73BGP9_1_4542615_Original.pdf",
"hp_cond":"https://www.appliancesdirect.co.uk/PDFs/784670031H2D81WUK_1_9031943_Original.pdf?v=9",
"beko_damp":"https://www.beko.co.uk/support/faqs/tumble-dryers/do-heat-pump-dryers-cause-condensation",
"aeg_damp":"https://support.aeg.co.uk/support-articles/article/excessive-moisture-in-room-on-walls-and-windows-where-the-tumble-dryer-is-located",
"lfb":"https://london-fire.gov.uk/safety/the-home/electrical-items/whitegoods",
"humber":"https://humbersidefire.gov.uk/newsroom/news/important-fire-safety-warning-tumble-dryers",
"nwales":"https://www.northwalesfire.gov.wales/keeping-you-safe/at-home/looking-after-the-electrics/white-goods-safety/",
"hisense":"https://www.currys.co.uk/products/hisense-1q-series-dh1q802bw2-8-kg-heat-pump-tumble-dryer-white-10279497.html",
"bosch_hp":"https://www.currys.co.uk/products/bosch-series-6-wqg24502gb-9-kg-heat-pump-tumble-dryer-white-10288375.html",
"beko_cond":"https://www.currys.co.uk/products/beko-dtkce80021w-8-kg-condenser-tumble-dryer-white-10211744.html",
"bosch_vent":"https://media3.bosch-home.com/Documents/specsheet/en-GB/WTA74200GB.pdf",
"logik":"https://www.currys.co.uk/products/logik-lvd7w18-7-kg-vented-tumble-dryer-white-10175587.html",
"eprel":"https://eprel.ec.europa.eu/fiches/tumbledriers/Fiche_762668_EN.pdf"}
def SR(k,t): return ext(SRC[k],t)
RATE=26.32
M=[("Heat pump, 8 kg, A++ (Hisense DH1Q802BW2)",235,"hisense"),("Heat pump, 9 kg, A+++ (Bosch WQG24502GB)",193,"bosch_hp"),("Condenser, 8 kg, B (Beko DTKCE80021W)",561.1,"beko_cond"),("Vented, 7 kg, C (Bosch WTA74200GB)",482,"bosch_vent")]
def cost(k,n): return k/160*n*52*RATE/100
def gbp(x): return f"£{x:,.0f}"
hp,cd,vt=235,561.1,482
s2,s4,s7=[cost(cd,n)-cost(hp,n) for n in (2,4,7)]

p(f"In the heat pump vs condenser dryer choice, a heat pump dryer is the better buy for most UK homes: at the current price cap a typical heat pump model costs about {gbp(cost(hp,4))} a year to run at four loads a week, against about {gbp(cost(cd,4))} for a typical condenser. A condenser is cheaper to buy and dries faster, but from 19 January 2027 new condenser and vented dryers can no longer be placed on the market in Great Britain, so the choice is closing anyway.")
p("Here is the short verdict:")
lst([f"<strong>Pick a heat pump dryer</strong> if you dry more than once or twice a week, if the dryer lives in a cupboard or small flat, or if you want it to last into the 2030s.",
 "<strong>Pick a condenser dryer</strong> only if you dry rarely, need the shortest cycles and can find one in stock before shops sell out.",
 "<strong>Pick a vented dryer</strong> only if it can sit against an outside wall or window and you use it occasionally: it is cheap, but it pushes hot, damp air outside through a hose."])
img(1)

h2("Heat Pump vs Condenser vs Vented Dryer at a Glance")
p("The table uses real models on sale at Currys on 23 October 2026 and their energy-label figures. Running costs use Ofgem’s electricity unit rate for October to December 2026.")
table(["","Heat pump","Condenser","Vented"],[
 ["Cheapest 8 kg price we saw","£329 (A++)","£249 (B)","£229 (7 kg, C)"],
 ["Label energy use (kWh a year)","193–265","561–617","482–520"],
 ["Running cost, 4 loads a week",gbp(cost(hp,4)),gbp(cost(cd,4)),gbp(cost(vt,4))],
 ["Full cotton load","about 160–210 min","about 142–149 min","about 128–145 min"],
 ["Drying temperature","about 50°C","70–75°C","70–75°C"],
 ["Needs an outside vent","No","No","Yes"],
 ["Where the water goes","Tank or drain hose","Tank or drain hose","Outside, as damp air"],
 ["Warmth and damp in the room","Some","More","Very little (if vented outside)"],
 ["New ones sold in GB after 18 Jan 2027","Yes","No (until stock runs out)","No (until stock runs out)"]])
p("Prices change weekly, and the cheapest models are not always the most efficient within each type, so treat the price row as a guide.")

h2("Is a Heat Pump Dryer Worth Paying Extra For?")
p(f"Yes, for almost everyone who uses a dryer every week. Ofgem’s cap for 1 October to 31 December 2026 is {SR('ofgem','26.32p per kWh')} for electricity paid by direct debit. The old energy label gives each dryer’s yearly use {SR('lab392','based on 160 drying cycles')} at full and partial loads, so dividing by 160 gives an average cost per cycle. We used that method for four real dryers:")
rows=[]
for n,k,src in M:
    rows.append([SR(src,n),f"{k/160*RATE:.0f}p"]+[gbp(cost(k,x)) for x in (2,4,7)])
table(["Dryer (energy label)","Per load","2 loads a week","4 loads a week","7 loads a week"],rows)
p(f"Against the Beko condenser, the Hisense heat pump saves about {gbp(s2)} a year at two loads a week, {gbp(s4)} at four and {gbp(s7)} at seven. With an £80 price gap between the two, it pays for itself in roughly 17, 9 or 5 months. Which? reaches a similar answer from its own tests: the average heat pump it tested {SR('which_ban','costs £54 a year to run')}, against £139 for the average condenser, at three loads a week.")
p("Two caveats. The label figure is an average of full and half loads, so a full load costs more: Beko’s fiche for a matching condenser lists 4.75 kWh, about £1.25, for a full cotton load. And the price cap changes every three months, so your own bill will move with it.")

h2("Why New Condenser and Vented Dryers Are Leaving UK Shops")
p(f"New ecodesign rules for Great Britain (S.I. 2026/318) set an energy limit that only heat pump models meet. From 19 January 2027, {SR('retra','new vented, condenser and gas-fired tumble dryers will no longer be allowed')} onto the GB market, according to the retail trade body RETRA. The government’s own impact work says heat pumps were already {SR('gov','74% of models sold')}, with condensers about 20% and vented about 5%.")
lst(["<strong>You do not have to replace a working dryer.</strong> Existing machines can be used, repaired and sold second-hand.",
 "<strong>Shops can sell the stock they already hold.</strong> Which? says older models placed on the market before the deadline stay on sale until stocks run out.",
 "<strong>Washer-dryers are not affected</strong> by these tumble dryer rules, according to Which?.",
 "<strong>Northern Ireland follows the EU rules</strong>, which set the same energy limit from 1 July 2025."])
p("Expect confusion over labels. A new A to G label, showing kWh per 100 cycles, replaces the old A+++ scale. Some retailers already show heat pump dryers with new-scale letters such as B, C or E, which are not comparable with an old-scale B condenser. Compare the kWh figures, not the letters.")

h2("Heat Pump Dryer: Best For and Avoid If")
img(6)
p(f"A heat pump dryer reuses its warm air through a closed loop, so it dries at a lower temperature: about 50°C instead of the 70–75°C of a standard dryer, {SR('currys_tt','according to Currys')}. That is gentler on fabrics and the reason it uses roughly half the energy.")
lst(["<strong>Best for:</strong> families, anyone drying three or more loads a week, flats with no outside wall, cupboards and utility rooms where you want less heat.",
 f"<strong>Avoid if:</strong> you need fast turnarounds. Beko quotes about {SR('beko_pros','142 minutes')} for an 8 kg condenser cotton cycle against roughly 197 to 209 minutes for its heat pumps, and Which? found some heat pumps take almost twice as long.",
 f"<strong>Watch the room temperature.</strong> Beko says its dryers {SR('beko_garage','should not be placed')} where the temperature drops below 5°C, and Which? notes most brands set a minimum of {SR('which_garage','5°C to 10°C')}. For a cold garage, look for models designed for 0°C, such as Hotpoint ColdGuard or Beko and Blomberg DryGuard."])
p("Heat pump dryers also need a little more care: as well as the door filter after every load, Beko advises cleaning the filters and the evaporator regularly. Some models, such as the Bosch WQG24502GB, have a self-cleaning condenser.")

h2("Condenser Dryer: Best For and Avoid If")
img(4)
p("A condenser dryer heats air with an element, then cools it to turn the moisture into water, which collects in a tank or runs away through a drain hose. No vent is needed, which is why it became the standard choice for British flats and utility cupboards.")
lst(["<strong>Best for:</strong> occasional use (one load a week or less), when the lower price matters more than the running cost, and when you want a cycle well under two and a half hours.",
 f"<strong>Avoid if:</strong> you dry most days. At seven loads a week the Beko condenser costs about {gbp(cost(cd,7))} a year, against {gbp(cost(hp,7))} for the Hisense heat pump.",
 f"<strong>Expect some warm, damp air.</strong> Beko’s condenser fiche lists a condensation efficiency of {SR('eprel','81%')}, so part of the water still leaves as humid air. Empty the tank after every cycle, and clean the condenser unit: Hotpoint’s manual says {SR('hp_cond','monthly')}."])

h2("Vented Dryer: Best For and Avoid If")
img(5)
p(f"A vented dryer blows hot, moist air straight outside through a flexible hose, so it adds the least damp to the room but must stand by an outside wall or window. Hotpoint’s installation guide says the hose {SR('hp_vent','should not exceed 2.4 metres')}, and it must not go into an extractor fan duct or a flue for a gas or other fuel-burning appliance.")
lst(["<strong>Best for:</strong> a garage or utility room with a wall vent already in place, and light use.",
 "<strong>Avoid if:</strong> the dryer would sit in an inside cupboard, or if you would have to push the hose through an open window in winter.",
 "<strong>Price and choice:</strong> very few vented models are still on sale; the Logik LVD7W18 at £229 was the only one on Currys’ vented page when we checked."])

h2("Fitting a Dryer in a Small Utility Room or Cupboard")
diagram(open('z.svg').read(),"Where each tumble dryer can go: under a worktop, stacked on a washer with a kit, in a ventilated cupboard with a drain hose, or vented through an outside wall.")
p(f"Space, not just running cost, often decides which dryer works. Heat pump and condenser dryers can go in a cupboard {SR('beko_where','as long as there’s adequate space and airflow')}, says Beko. Hoover’s condenser manual asks for {SR('hoover_man','a gap of at least 12 mm')} around the machine and says it must not be installed behind a lockable door. Miele’s heat pump manual adds that the cool air intake at the front {SR('miele','must not be blocked or covered')}.")
img(2)
lst(["<strong>Check the depth.</strong> Many 8 kg heat pumps are only 54.5 to 55 cm deep, while some 9 kg models are about 61 cm, plus the door. Our "+a('washer-dryer-space-calculator','washer and dryer space calculator')+" checks whether two machines fit your gap.",
 f"<strong>Stack with the right kit.</strong> The dryer always goes on top. Beko’s manual says a washing machine {SR('beko_man','cannot be placed on top of the drying machine')} and gives minimum washer depths for each dryer depth.",
 "<strong>Use the drain hose</strong> when the tank would be awkward to reach, for example in a stack or a tall cupboard: Hoover’s manual says the water can be discharged directly to a waste water drain pipe.",
 f"<strong>Let the damp out.</strong> Beko advises a room with a window or {SR('beko_damp','an extractor fan')} for heat pump dryers, and AEG suggests a room larger than {SR('aeg_damp','roughly 10-12 m2')}. In a small cupboard, add vents or leave the door open while it runs."])
p("For layout ideas around the machines, see our "+a('small-utility-room-ideas','small utility room ideas')+" and "+a('laundry-closet-ideas','laundry closet ideas')+". If you still air-dry some clothes, our "+a('airing-cupboard-shelves','airing cupboard shelves')+" guide shows how to use the warm space above the cylinder.")

h2("Safety and Care for Any Tumble Dryer")
img(3)
p(f"Whichever type you choose, the fire services give the same advice. London Fire Brigade says to {SR('lfb','clean your tumble dryer filter after every load')} and to register new appliances so the maker can contact you about recalls. Humberside Fire and Rescue warns {SR('humber','never leave your dryer running unattended or overnight')} and never to overload it, and North Wales Fire and Rescue advises checking for recalls through {SR('nwales','Register My Appliance')}.")

h2("Our Pick for Your Home")
p("Here is how the heat pump vs condenser dryer choice plays out in different homes:")
lst(["<strong>Small flat with no outside wall:</strong> an 8 kg heat pump with a drain hose, about 55 cm deep.",
 f"<strong>Family drying every day:</strong> an A++ or A+++ heat pump; the saving over a condenser is close to {gbp(s7)} a year at seven loads a week.",
 "<strong>One load a week or less:</strong> a condenser still makes sense while stock lasts, or skip the dryer and use a heated airer.",
 "<strong>Cold garage or outbuilding:</strong> a heat pump designed to run at 0°C, or keep the space above the maker’s minimum temperature.",
 "<strong>Speed matters most:</strong> a condenser or vented model is quicker, but you are buying a type that is leaving the market."])
p("Once the dryer is in, our guide to "+a('how-to-organize-a-laundry-room','organising a laundry room')+" shows where baskets, detergent and folding space work best.")

h2("Quick Decision Checklist")
p("Answer yes or no:")
lst(["Do you dry three or more loads most weeks? Yes points to a heat pump.",
 "Will the dryer sit in a cupboard, flat or room without an outside wall? Yes rules out vented.",
 "Will the room drop below 5°C in winter? Yes means a cold-rated heat pump or a different spot.",
 "Do you need loads dry in under two and a half hours? Yes favours a condenser, while you can still buy one.",
 "Do you want spare parts and a model that is still sold new in 2027? Yes points to a heat pump."],ordered=True)
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub('<[^>]+>',' ',html)
print(len(html.encode()),'bytes;',len(txt.split()),'words; kw',html.lower().count('heat pump vs condenser dryer'), 'hp', html.lower().count('heat pump'))
print(f"savings {s2:.2f} {s4:.2f} {s7:.2f}; costs", [round(cost(k,4),2) for _,k,_ in M])
