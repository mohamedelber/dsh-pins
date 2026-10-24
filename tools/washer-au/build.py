import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={
"wels":"https://waterrating.gov.au/node/9",
"ch1":"https://www.choice.com.au/home-and-living/laundry-and-cleaning/washing-machines/articles/front-loading-washing-machines",
"ch2":"https://choice.com.au/home-and-living/laundry-and-cleaning/washing-machines/articles/best-washing-machine-for-saving-water",
"ch3":"https://www.choice.com.au/home-and-living/laundry-and-cleaning/washing-machines/articles/best-top-loaders-on-a-budget",
"ch4":"https://www.choice.com.au/home-and-living/laundry/washing-machines",
"ch5":"https://www.choice.com.au/home-and-living/laundry-and-cleaning/washing-machines/articles/washers-accessibility",
"calc":"https://calculator.energyrating.gov.au/WasherInformation.aspx",
"er":"https://energyrating.gov.au/node/50",
"eeca":"https://eeca.govt.nz/regulations/equipment-energy-efficiency/about-energy-rating-labels/clothes-washers",
"fp":"https://www.fisherpaykel.com/on/demandware.static/-/Sites-fpa-master-catalog/default/dw39c4dda3/GeneralFiles-FisherPaykelAU/FP-EnergyWater-en-WL9058G1-TopLoaderWashingMachine-0-431836A-NZ-AU.pdf",
"cb":"https://canstarblue.com.au/?p=73671",
"cbp":"https://www.canstarblue.com.au/appliances/cheap-washing-machines-whats-available/",
"ao":"https://www.appliancesonline.com.au/laundry-energy-and-water-efficiency/",
"aoi":"https://appliancesonline.com.au/academy/laundry/top-loader-washing-machines-agitator-or-impeller",
"aop":"https://www.appliancesonline.com.au/blog/raise-washing-machine-with-laundry-pedestal/",
"lid":"https://www.winnings.com.au/manuals/ak/1/1/e/a/11ea752093645c39f8597a83093f546dee7c2766_WA1068G2_Quick_Guide.pdf",
"lg":"https://www.lg.com/au/support/product-help/CT20088047-20153085543927",
"ar":"https://applianceretailer.com.au/?p=78733"}
def SR(k,t): return ext(SRC[k],t)
W=5*52
fw,tw=56*W,119*W
kwh=229; c=0.321; cost=kwh*c

p(f"Choosing between a front loader and a top loader comes down to running costs against speed and purchase price. A front loader uses far less water and spins clothes drier, and it fits under a benchtop, but it costs more and takes about twice as long per wash. A top loader is cheaper to buy, washes faster and suits a laundry with space above it, but it uses more water and energy over its life.")
lst(["<strong>Pick a front loader</strong> if you pay for water, wash often, want to stack a dryer or need the benchtop space.",
"<strong>Pick a top loader</strong> if your budget is tight, you want quick cycles, or bending to load is hard for you.",
"<strong>Either works</strong> for a household of one or two in a laundry with room for both."])
p(f"Australians have been switching. A 2024 Appliance Retailer report citing Oxford Economics found front loaders are now in {SR('ar','more Australian homes than top loaders')}, 53% against 44%.")
img(1)

h2("Front Loader vs Top Loader at a Glance")
table(["","Front loader","Top loader"],[
["Price (budget models)",SR('cbp','about A$500 to A$1,000+'),"about A$400 to A$800"],
["Water per normal cold wash (CHOICE tests)",SR('ch2','40 to 75 L'),"62 to 167 L"],
["Average cycle time","a bit over 2 hours","about 1 hour"],
["Fastest spin speed",SR('ao','up to 1,600 rpm'),"up to 1,100 rpm"],
["Under a benchtop or stacked","Yes","No, needs clear space above"],
["Loading","Bend down (a pedestal helps)","From above"],
["Care","Leave the door open, dry the seal","Fewer seal problems"]])
diagram(open('z.svg').read(),"Water use, cycle time, spin speed and the space each type of washer needs.")

h2("Front Loaders: Best for Running Costs and Small Laundries")
img(2)
p(f"<strong>Best for:</strong> families who wash most days, households on water tanks or meters, small laundries where the machine must go under a benchtop, and anyone planning a stacked dryer.")
p(f"Water is the big win. CHOICE says front loaders can use {SR('ch1','up to 70% less water')} than an equivalent top loader, and the government's Energy Rating calculator says they use {SR('calc','about half the water of top loaders')}. Over a year of five washes a week, CHOICE's test averages of about 56 litres per front-loader wash and 119 litres per top-loader wash add up to roughly {fw:,} litres against {tw:,} litres, a difference of about {tw-fw:,} litres. Faster spinning also helps: CHOICE notes {SR('ch4','higher spin speeds extract more water from your clothes')}, so clothes dry sooner on the line or in a dryer.")
p(f"<strong>Avoid if:</strong> you need clothes washed in an hour, or bending is difficult. CHOICE says front loaders average a bit over two hours a cycle and some take up to five. Most pedestals raise the machine about 30 to 40 cm, and Appliances Online lists them from about {SR('aop','A$249')}. Use front-loader detergent, which CHOICE says contains a suds inhibitor.")
p(f"Planning a stacked pair? A condenser or heat pump dryer must be stacked on the washer itself (only vented dryers can be wall mounted), and some only stack on the same brand, so check before you buy. Our {a('washer-dryer-space-calculator','washer and dryer space calculator')} shows the space a stacked pair needs.")

h2("Top Loaders: Best for Budget and Speed")
img(3)
p(f"<strong>Best for:</strong> tight budgets, busy households that want a quick wash, and laundries with open space above the machine.")
p(f"Top loaders are cheaper up front. Canstar Blue puts budget top loaders at about A$400 to A$800, and the cheapest top loader in a CHOICE review cost A$399 (though CHOICE did not recommend it), while CHOICE says top loaders {SR('ch3','tend to top out at around $1500')} and front loaders can pass A$3,000. They are also quicker: Energy Rating notes top loaders {SR('er','tend to have shorter cycle times')}. If you choose one, an impeller model is usually {SR('aoi','gentler on your clothes than agitators')} and leaves more room in the drum.")
p(f"<strong>Avoid if:</strong> the machine has to go under a benchtop or you want to stack a dryer. The lid needs clear space above it: one Fisher &amp; Paykel top loader stands {SR('lid','1440 - 1470 mm')} high with the lid open. Running costs are higher too, as the next section shows.")

h2("What Each One Costs to Run")
p(f"The energy label shows estimated kWh per year, and the more stars, the cheaper it is to run. Compare machines of the same capacity. The figure on Australian and New Zealand labels assumes seven washes a week, {SR('eeca','calculated on a warm wash')} using the manufacturer's recommended settings, so washing in cold water costs much less. The water label shows a star rating and {SR('wels','litres per wash')}.")
p(f"To estimate a running cost, multiply the kWh figure by your electricity price. For example, a 9 kg Fisher &amp; Paykel top loader is labelled at {SR('fp','229 kWh a year')}; at Canstar Blue's average of 32.1c per kWh (2024 data), that is about A${cost:.0f} a year on warm washes. Canstar Blue's own comparison found yearly energy costs for washing machines {SR('cb','anywhere from $32 to $97')} based on three warm washes a week, with front loaders at the cheaper end.")

h2("Keep a Front Loader Fresh")
img(4)
p(f"The most common front-loader complaint is a musty smell. LG Australia advises that after each wash you {SR('lg','open the washing machine door and the detergent dispenser')} so the inside can dry, and wipe the door seal with a towel. CHOICE says manufacturers recommend keeping front loaders partly open for the same reason. If you have small children, keep the laundry door shut while the machine airs, and check the drum is empty before every wash.")

h2("Our Pick")
lst(["<strong>Family of four in a house:</strong> a front loader with a high water star rating. The water and energy savings add up fastest when you wash every day.",
"<strong>Small apartment laundry or European laundry:</strong> a front loader, because it fits under a benchtop or in a cupboard. See our "+a('european-laundry-ideas','European laundry ideas')+" and "+a('small-laundry-ideas','small laundry ideas')+".",
"<strong>Renter on a budget with a separate laundry:</strong> an impeller top loader, which costs less and washes fast.",
"<strong>Bad back or limited mobility:</strong> a top loader, or a front loader on a pedestal."])

h2("Decide in Five Questions")
lst(["Does the machine have to go under a benchtop or in a cupboard? <strong>Yes:</strong> front loader.",
"Do you want to stack a dryer on top? <strong>Yes:</strong> front loader.",
"Is your budget under about A$500? <strong>Yes:</strong> top loader.",
"Do you need a full wash in about an hour most days? <strong>Yes:</strong> top loader.",
"Do you pay for water or rely on a tank? <strong>Yes:</strong> front loader."],ordered=True)
p(f"Still choosing a dryer to go with it? Our {a('heat-pump-vs-condenser-dryer','heat pump vs condenser dryer guide')} compares the running costs. In the US, our {a('small-laundry-room-ideas-top-loading-washer','top-loading washer laundry ideas')} use American sizes.")
ai_note()
html='\n\n'.join(out)
html=re.sub(r'(\d+\.\d{2})\d+',r'\1',html)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('front loader vs top loader'),'kw')
