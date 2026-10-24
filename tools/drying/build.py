import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={
"gsa1":"https://gsamediacentre.co.uk/research-highlights-health-and-economic/",
"gsa2":"https://gsamediacentre.co.uk/media-release-think-before-you-hang/",
"tand":"https://www.tandridge.gov.uk/condensation",
"nhs":"https://www.nhs.uk/CHQ/Pages/Can-damp-and-mould-affect-my-health.aspx",
"nhsht":"https://www.healthiertogether.nhs.uk/new-parent-and-baby/damp-and-mould",
"skdc":"https://www.southkesteven.gov.uk/housing/damp-mould-and-condensation-advice/how-can-i-reduce-damp-and-mould",
"gw":"https://www.groundwork.org.uk/resources/drying-your-clothes/",
"shrop":"https://www.shropshirefire.gov.uk/news/portable-heaters-fire-warning/",
"ofgem":"https://ofgem.gov.uk/news/changes-energy-price-cap-between-1-october-and-31-december-2026",
"dun":"https://www.dunelm.com/product/3-tier-heated-airer-1000292620",
"meaco":"https://www.meaco.com/products/meaco-12l-low-energy-dehumidifier-and-air-purifier",
"which":"https://www.which.co.uk/news/article/can-you-use-a-dehumidifier-to-dry-laundry-aX79m5I0XFVm",
"wgh":"https://www.whitegoodshelp.co.uk/washing-machine-spin-speed-efficiency/",
"leeds":"https://leeds.gov.uk/housing/council-housing-information-for-tenants/damp-mould-and-condensation",
"ash":"https://www.ashfield.gov.uk/media/s0jfhksl/a-tenants-guide-to-damp-condensation-and-mould.pdf",
"dorset":"https://www.dorsetcouncil.gov.uk/documents/35024/282001/How+to+prevent+damp+mould+and+condensation+in+your+home.pdf/52c52240-9d1b-39c5-4401-e665cc6e5a69",
"lofti":"https://www.lakeland.co.uk/23727/the-lofti-aluminium-ceiling-pulley-indoor-clothes-airer-7m",
"elm":"https://www.elmbridge.gov.uk/housing/damp-condensation-and-mould/awaabs-law-guidance-tenants"}
def SR(k,t): return ext(SRC[k],t)
P=26.32
airer=round(0.3*6*P)

p(f"To dry clothes indoors without damp, spin them as fast as your machine allows, hang them on an airer in a small room with the door shut and a window slightly open or the extractor fan on, and keep them off the radiators. A dehumidifier or a heated airer speeds things up when the weather is cold and wet. Done this way, you keep condensation and mould to a minimum.")
p(f"The reason it matters is the water. Research from the Mackintosh School of Architecture found that {SR('gsa1','the average load of washing will release around 2 litres of moisture')} into your home, and that drying on airers by radiators in a poorly ventilated room can account for up to a third of the moisture in the air. Here is how to keep that water out of your walls.")
img(1)

h2("Step 1: Spin It Fast")
p(f"The less water you start with, the faster clothes dry. Groundwork, an environmental charity, advises you to {SR('gw','use the highest spin cycle you can')}. Manufacturer data reported by Whitegoods Help suggests a 6 kg cotton load spun at 1,400 rpm keeps about 49% of its moisture, against about 55% at 1,000 rpm, though figures vary between machines. Check the care labels for delicates, but for towels, sheets and cottons, use the fastest spin.")

h2("Step 2: Pick the Right Room")
p(f"Dry washing in one room and shut the door, so the moist air does not spread through the house. Leeds City Council suggests you {SR('leeds','leave a window opened slightly and close the door')}, and Tandridge District Council suggests using an airer in the bathroom with the door closed. A bathroom or utility room with an extractor fan is ideal; Ashfield District Council says to dry clothes with {SR('ash','the extractor fan on or window slightly open')}. Avoid drying washing in bedrooms. If you have a utility room, our {a('small-utility-room-ideas','small utility room ideas')} show how to fit a drying rack in.")

h2("Step 3: Use an Airer, Not the Radiator")
img(2)
p(f"It is tempting to drape clothes over a warm radiator, but South Kesteven District Council's advice is simple: {SR('skdc','do not dry clothes on radiators')}. Groundwork says drying clothes on a radiator blocks airflow, so it takes more energy to heat the room. Never put clothes on a portable heater either; Shropshire Fire and Rescue says of portable heaters: {SR('shrop','don\'t dry clothes on them')}. Use a freestanding airer instead, and keep it clear of the radiator.")

h2("Step 4: Give Clothes Space")
p(f"Air needs to move around each item. Hang shirts and dresses on hangers from the airer's top rail, fold towels over a single bar rather than double, and leave a gap between items. If floor space is tight, a ceiling pulley airer lifts the washing out of the way; Lakeland's Lofti model gives {SR('lofti','up to 6.7 metres of drying room')}. Our {a('airing-cupboard-shelves','airing cupboard shelves')} guide covers finishing items off in a warm cupboard.")

h2("Step 5: Keep Air Moving")
p(f"Ventilation is what stops the moisture settling as condensation. NHS Healthier Together advises that if you have nowhere else to dry clothes, you should {SR('nhsht','open a window')}. Keep trickle vents open and wipe any condensation off the windows each morning. Moisture that has nowhere to go ends up as mould, and the NHS says moulds produce allergens and irritants and {SR('nhs','can also cause asthma attacks')}.")

h2("Step 6: Speed It Up When It Is Cold")
img(3)
p(f"In cold, damp weather, a small appliance can speed up drying. A dehumidifier pulls water out of the air as the clothes dry; Which? found it almost halved drying time in its test and costs on average {SR('which','26p per litre of water extracted')}, so about 52p for a load that releases 2 litres. Many models have a laundry mode, such as Meaco's 12-litre compressor dehumidifier, which uses {SR('meaco','157W')}. A heated airer is the other option: Dunelm's three-tier model is {SR('dun','300W')}, so six hours at the Ofgem price cap of {SR('ofgem','26.32 pence per kilowatt hour')} costs about {airer}p by our estimate.")
diagram(open('z.svg').read(),f"Estimated cost to dry one load indoors: from nothing on an airer by an open window to about 89p in a condenser tumble dryer.")
p(f"As the chart shows, a heat pump tumble dryer, at about 35p a load according to Which?, is cheaper than either the heated airer or the dehumidifier. Which? says a dehumidifier {SR('which','would still cost more and take longer')} than the cheapest tumble dryers. If you are choosing a dryer, our {a('heat-pump-vs-condenser-dryer','heat pump vs condenser dryer guide')} compares running costs.")

h2("Step 7: Check the Humidity")
p(f"A cheap digital hygrometer shows whether your drying routine is working. Dorset Council says indoor humidity is {SR('dorset','normally around 40-55%')}, and that the risk of condensation rises above 60%. If the reading stays high while washing is drying, open the window wider, run the fan longer or move the airer to a smaller room.")

h2("If You Rent")
p(f"Damp caused by a building fault is your landlord's job to fix, and ventilating well helps prevent condensation. In England, Awaab's Law has set deadlines for social landlords to deal with damp and mould since October 2025, though Elmbridge Borough Council notes it {SR('elm','only applies to social housing tenants')}, not private renters. Keep a record of any damp, and report it in writing.")

h2("Drying Clothes Indoors: Quick Answers")
h3("Is it bad to dry clothes indoors?")
p("Not if you control the moisture. A load releases about 2 litres of water, so drying in one room with the door shut and a window open, an extractor fan or a dehumidifier keeps it from causing condensation and mould. Problems start when washing dries slowly in a closed, unventilated room, especially a bedroom.")
h3("What is the cheapest way to dry clothes indoors?")
p(f"An ordinary airer near an open window costs nothing to run but is slow in winter. If you need speed, a heat pump tumble dryer costs about 35p a load according to Which?, less than a heated airer used for six hours (about {airer}p by our estimate) or a dehumidifier (about 52p).")
h3("Can I dry clothes on a radiator?")
p("It is best not to. Councils advise against it, and Groundwork says it blocks the heat, so heating the room takes more energy. Use an airer near the radiator instead, and never put clothes on a portable heater, which Shropshire Fire and Rescue warns against.")
ai_note()
html='\n\n'.join(out)
html=re.sub(r'(\d+\.\d{2})\d+',r'\1',html)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('dry clothes indoors')+html.lower().count('drying clothes indoors'),'kw')
