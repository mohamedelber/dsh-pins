import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
RC="https://www.rentcafe.com/storage-units/size-guide/"
UH="https://www.uhaul.com/Tips/Storage/What-Size-Storage-Unit-Do-I-Need-31025/"
BY="https://www.bigyellow.co.uk/staines-self-storage-units"
PS="https://www.publicstorage.com/blog/public-storage/what-size-storage-unit-do-you-need-for-a-car-2026-size-and-pricing-guide.html"
p("What size storage unit do I need? As a rough guide, a studio fits in a 5 x 10 ft unit, a one or two bedroom home in a 10 x 10, a three bedroom house in a 10 x 15 and a four bedroom house in a 10 x 20. This free <strong>storage unit size calculator</strong> picks the right size for you in two taps, in US unit sizes or the square feet UK stores use.")
p("Choose what you are storing and whether it is everything or about half. Open <em>More options</em> if you want a walk-in aisle so you can reach things easily, or to switch between US and UK sizes. Renting a size too big wastes money every month; too small and you end up paying for a second unit.")
add('<!-- wp:html -->\n'+open('tool.html').read()+'\n<!-- /wp:html -->')
h2("Storage Unit Size Chart")
table(["US unit","Area","What it holds","UK stores"],[
["5 x 5 ft","25 sq ft","A few boxes and small items, such as a desk and chair; about a small closet","25 sq ft: about a small garden shed"],
["5 x 10 ft","50 sq ft","The contents of a studio apartment","50 sq ft: a standard studio flat, about a transit van load"],
["10 x 10 ft","100 sq ft","A one or two bedroom apartment; about a regular bedroom","75 sq ft for a large 1 bedroom; 100 sq ft for a standard 2 bedroom flat or house"],
["10 x 15 ft","150 sq ft","A two or three bedroom home; about a master bedroom","125 to 150 sq ft for a 3 bedroom house"],
["10 x 20 ft","200 sq ft","A three bedroom home, or one car; about a one-car garage","200 sq ft for a large 4 bedroom house"],
["10 x 30 ft","300 sq ft","Big homes with several bedrooms; about a double garage","250 to 300 sq ft for a 5 bedroom house"]])
p(f"The US sizes and what they hold come from RentCafe's {ext(RC,'storage unit size guide')}, cross-checked with U-Haul's guide to {ext(UH,'what size storage unit you need')}, which says a 5 x 10 suits a studio or one bedroom apartment and a 10 x 20 holds up to four bedrooms' worth. The UK column uses Big Yellow's {ext(BY,'room size guide')}, which sells rooms by square feet rather than by width and depth.")
img(1)
h2("How the Storage Unit Size Calculator Works")
lst(["It matches your home size to the guides above: a few boxes 25 sq ft, a studio 50, one bedroom 75 to 100, two bedrooms 100, three bedrooms 150, four bedrooms 200 and five or more 300 sq ft.",
"<strong>About half</strong> moves you one size down, for example when the big furniture stays behind or goes with you.",
"<strong>A walk-in aisle</strong> moves you one size up. This is our own rule of thumb: an aisle down the middle costs floor space but lets you reach the back without unpacking the front.",
"For US users it shows the nearest standard unit (5 x 5, 5 x 10, 10 x 10, 10 x 15, 10 x 20 or 10 x 30). UK users see the square feet that stores such as Big Yellow sell."])
p("These guides assume a sensibly packed unit. If you own large furniture, a piano or lots of garden equipment, go one size up. If you are mainly storing boxes, you can often go one size down.")
h2("What Size Storage Unit for a Car?")
p(f"Public Storage's {ext(PS,'guide to storing a car')} suggests a 20 ft space for a sedan or standard-size car and a 16 ft space for a small car, and describes a 10 x 20 ft unit as roughly the size of a small one-car garage. For an SUV, van or truck, it says to measure first. Before you book, measure the car's length, its width including mirrors and its height, compare them with the unit and its door opening, and check that the facility allows a vehicle in that unit.")
img(2)
h2("How to Pack a Storage Unit to Fit More")
lst(["<strong>Use boxes of the same size.</strong> They stack into stable columns and waste less space. Our "+a('moving-box-calculator','moving box calculator')+" tells you how many you need.",
"<strong>Take furniture apart.</strong> Remove table legs and bed frames, and stand mattresses and sofas on end where they are stable.",
"<strong>Heavy at the bottom, light on top.</strong> Put books and kitchen boxes low and bedding and lampshades high.",
"<strong>Keep what you need near the door.</strong> Seasonal items and paperwork go at the front, things you will not need for months at the back.",
"<strong>Write a list.</strong> Number every box and keep a list on your phone of what is in each one."],True)
img(3)
h2("Rent a Smaller Unit: Declutter First")
p(f"Every item you sell, donate or recycle before you move is one you do not pay to store month after month. Start with our guide on {a('how-to-declutter-your-home','how to declutter your home')}. If you only need room for seasonal things, the space you already have may be enough: see our {a('loft-storage-ideas','loft storage ideas')}, {a('under-stairs-storage-ideas','under stairs storage ideas')} and {a('christmas-decoration-storage','Christmas decoration storage ideas')}.")
add(open('savebox.html').read())
h2("Storage Unit Size FAQ")
h3("What size storage unit do I need for a 2 bedroom apartment?")
p("A 10 x 10 ft unit (100 sq ft) holds the contents of a typical one or two bedroom apartment, according to RentCafe. Big Yellow in the UK suggests 100 sq ft for a standard two bedroom flat or house. A large two bedroom home with a lot of furniture may need a 10 x 15.")
h3("What size storage unit do I need for a 3 bedroom house?")
p("Plan a 10 x 15 ft unit (150 sq ft) for a typical three bedroom house, or a 10 x 20 ft unit (200 sq ft) for a large one. RentCafe says a 10 x 20 can easily hold a three bedroom home, and Big Yellow suggests 125 to 150 sq ft.")
h3("What size storage unit for a 1 bedroom apartment?")
p("A 5 x 10 ft unit can work for a small one bedroom apartment, as U-Haul suggests, but a 10 x 10 ft unit gives room for a bed, sofa and appliances without packing it to the ceiling. In the UK, Big Yellow suggests about 75 sq ft for a large one bedroom home.")
h3("How big is a 10 x 10 storage unit?")
p("A 10 x 10 storage unit has 100 sq ft (about 9.3 m²) of floor space, about the size of a regular bedroom. It typically holds the contents of a one or two bedroom apartment, including a bed, sofa, dresser and boxes.")
h2("More Moving and Storage Tools")
p(f"Moving house too? Our {a('moving-box-calculator','moving box calculator')} works out how many boxes you need, and our {a('storage-ideas-for-small-spaces','storage ideas for small spaces')} help you fit everything into your new home.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script.*?</script>|<style.*?</style>','',html))
print(len(html),'words',len(txt.split()),'kw',txt.lower().count('storage unit'))
