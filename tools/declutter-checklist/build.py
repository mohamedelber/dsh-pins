import re,json
exec(open('helpers.py').read())
exec(open('checklist.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
PDF=json.load(open('pdf.json'))['url']
SRC={"ill":"https://extension.illinois.edu/media/8723/download",
"flush":"https://www.fda.gov/drugs/disposal-unused-medicines-what-you-should-know/drug-disposal-fdas-flush-list-certain-medicines/",
"ny":"https://trafficsafety.ny.gov/used-child-safety-seats-checklist",
"fda":"https://www.fda.gov/consumers/consumer-updates/where-and-how-dispose-unused-medicines",
"dea":"https://www.dea.gov/press-releases/2026/10/19/dea-hosts-31st-national-prescription-drug-take-back-day-saturday-october",
"cos":"https://www.fda.gov/cosmetics/resources-consumers-cosmetics/cosmetics-safety-qa-shelf-life",
"mayo":"https://www.mayoclinic.org/healthy-lifestyle/consumer-health/expert-answers/sauna/faq-20057957",
"fsis":"https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/food-product-dating",
"li":"https://epa.gov/recycle/used-lithium-ion-batteries",
"el":"https://www.epa.gov/recycle/electronics-donation-and-recycling",
"ftc":"https://consumer.ftc.gov/articles/how-remove-your-personal-information-you-get-rid-your-phone",
"hhw":"https://www.epa.gov/large-scale-residential-demolition/household-hazardous-waste-and-demolition",
"irs":"https://irs.gov/businesses/small-businesses-self-employed/how-long-should-i-keep-records",
"shred":"https://www.consumer.ftc.gov/sites/default/files/articles/pdf/pdf-0014-identity-theft.pdf",
"tex":"https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/textiles-material-specific-data",
"crib":"https://www.cpsc.gov/onsafety/2011/06/the-new-crib-standard-questions-and-answers",
"nhtsa":"https://www.nhtsa.gov/car-seat-use-after-crash",
"usfa":"https://usfa.fema.gov/gallery/pictographs/pictograph28.html"}
def SR(k,t): return ext(SRC[k],t)

p(f"A declutter checklist works best when it is short enough to finish and clear about where everything goes. This one covers the whole house room by room, from the pantry to the garage, and gives every item a tag: donate, recycle, trash, take-back, hazardous waste, shred or keep. Work through it in short sessions: University of Illinois Extension describes a {SR('ill','5–15 minutes at different times during the day')} approach, which is easier to stick to than one exhausting weekend.")
p(f"Print the two-page PDF, tick items as you go and use the notes box for local drop-off sites. For the bigger picture, such as how to decide what to keep and how to stop clutter coming back, see our {a('how-to-declutter-your-home','room-by-room guide to decluttering your home')}.")
add('<!-- wp:html -->\n<div class="dsh-dl" style="display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px;background:#EEF3EC;border:1px solid #D5E0D0;border-radius:16px;padding:20px 24px;margin:2em 0"><div style="flex:1 1 260px"><p style="margin:0 0 4px;font-weight:700;font-size:1.1rem;color:#342E2A">Free printable declutter checklist (PDF)</p><p style="margin:0;color:#6E645C;font-size:.95rem">Two pages: 7 rooms, 44 tick boxes with a where-it-goes tag, tips and a notes box. US Letter, fits A4.</p></div><a href="'+PDF+'" target="_blank" rel="noopener" style="background:#C85A32;color:#fff;border-radius:999px;padding:12px 22px;font-weight:700;text-decoration:none;white-space:nowrap">Download the PDF</a></div>\n<!-- /wp:html -->')
img(1)
h2("Before You Start")
lst(["<strong>Set a timer.</strong> Five to 15 minutes on one shelf or drawer is enough for a session.",
"<strong>Grab four boxes:</strong> donate, recycle, trash and put-away, so nothing gets sorted twice.",
"<strong>Work top to bottom</strong> in each room, and finish one spot before you start the next.",
"<strong>Get it out the same day.</strong> Put donations in the car and recycling by the door before you stop."])
h2("The Declutter Checklist, Room by Room")
p("Each line ends with where the item goes. Rules for recycling and hazardous waste vary by town, so check your local guidance for the drop-off points near you.")
for room,items in ROOMS:
    h3(room)
    lst([f"{t} <em>({g.lower()})</em>" for t,g in items])
img(2)
h2("Where It Goes: The Rules Worth Knowing")
h3("Medicines: take-back first")
p(f"The FDA says a drug take-back program is {SR('fda','the best way to dispose of most types of expired, unwanted or unused medicines')}. The DEA counts {SR('dea','more than 15,300 pharmacies, hospitals, and businesses')} that take them year-round, as well as twice-yearly National Prescription Drug Take Back Days. If there is no take-back option, the FDA says to mix medicines with something undesirable such as used coffee grounds, dirt or cat litter, seal it in a bag or container, put it in the trash and scratch your details off the packaging. Only flush medicines that are on the {SR('flush','FDA flush list')}.")
h3("Makeup, sunscreen and food")
p(f"Cosmetics don't need an expiration date by law, but the FDA notes that {SR('cos','some industry experts recommend replacing mascara 3 months after purchase')}, and it says to throw out eye makeup you were using when you had an eye infection. Sunscreen is required to keep its original strength for at least three years, according to {SR('mayo','Mayo Clinic')}, which says to throw out any that is past its date. In the pantry, a \"Best if Used By\" date {SR('fsis','indicates when a product will be of best flavor or quality')}, not when it becomes unsafe, so check the food itself before you throw it away.")
h3("Electronics and batteries")
p(f"The EPA says lithium-ion batteries {SR('li','should NOT go in household garbage or recycling bins')}, because they can start fires. Take them to a battery drop-off or household hazardous waste site, with the terminals taped or each battery in its own bag. Before you recycle or donate a phone or laptop, the EPA says to {SR('el','delete all personal information')}, and the FTC's three steps for a phone are to back it up, remove the SIM card and {SR('ftc','restore or reset it')}.")
h3("Paint, chemicals and cleaners")
p(f"Old paint, solvents, pesticides, motor oil and drain openers are household hazardous waste. The EPA recommends that you not pour them down the drain, on the ground or into storm sewers, and that you use {SR('hhw','HHW collection programs rather than discarding the HHW in the trash')}. Many towns run collection days or a permanent drop-off site.")
h3("Clothes and textiles")
p(f"Donate what is clean and wearable, and look for a textile recycling drop-off for the rest. It adds up: the EPA says {SR('tex','landfills received 11.3 million tons')} of textiles in 2018.")
h3("Cribs and car seats: don't pass them on")
p(f"The CPSC says you {SR('crib','should not resell, donate or give away a crib that does not meet')} the federal standard that took effect on June 28, 2011, which rules out drop-side cribs; take an old crib apart before you throw it away. For car seats, NHTSA recommends {SR('nhtsa','that car seats be replaced following a moderate or severe crash')}, and many seats also have an {SR('ny','expiration date')} printed on the seat or in the manual. If you are not sure of a seat's history, don't donate it.")
h2("What Not to Throw Out")
p(f"Paperwork is where decluttering can go wrong. The IRS says to {SR('irs','keep records for 3 years')} in most cases, but 6 years if you didn't report income you should have, 7 years if you claimed a loss from worthless securities or a bad debt, and indefinitely if you didn't file a return. Keep records for a property, such as your purchase and home improvement receipts, until the limitations period ends for the year you sell it. When papers do go, the FTC advises you to {SR('shred','shred all documents that show personal, financial, and medical information')}.")
p(f"While you are in each room, check the smoke alarms too. The U.S. Fire Administration says to {SR('usfa','replace smoke alarms when they are 10 years old')}.")
h2("Keep It Clear")
p(f"Once a room is done, give what is left a home. Our {a('storage-ideas-for-small-spaces','storage ideas for small spaces')} help in tight rooms, our {a('coat-closet-organization','coat closet organization')} ideas tame the entry, and if you are decluttering before a move, our {a('moving-checklist-printable','printable moving checklist')} picks up where this one ends.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('declutter checklist'),'kw')
