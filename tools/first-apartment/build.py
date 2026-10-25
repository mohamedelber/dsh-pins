import re,json
exec(open('helpers.py').read())
exec(open('checklist.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
PDF=json.load(open('pdf.json'))['url']
SRC={"sa":"https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/smoke-alarms/",
"co":"https://www.usfa.fema.gov/prevention/life-safety-hazards/carbon-monoxide/",
"fe":"https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/fire-extinguishers/",
"usfa":"https://www.usfa.fema.gov/downloads/fief/up_in_smoke_home_checklist.pdf",
"ready":"https://www.ready.gov/kit",
"naic":"https://content.naic.org/article/consumer-insight-rent-protecting-your-belongings-renters-insurance",
"iii":"https://www.iii.org/fact-statistic/facts-statistics-renters-insurance",
"tdi":"https://www.tdi.texas.gov/tips/renters-insurance.html",
"jag":"https://www.army.mil/article/102473/jag_5_tips_for_getting_security_deposits_back",
"ill":"https://occl.illinois.edu/rights-and-responsibilities/responsibilities",
"illu":"https://occl.illinois.edu/housing/utilities-and-services",
"ny":"https://ag.ny.gov/sites/default/files/tenants_rights.pdf",
"tx":"https://www.texasattorneygeneral.gov/consumer-protection/home-real-estate-and-travel/renters-rights",
"usps":"https://faq.usps.com/articles/FAQ/Change-of-Address-The-Basics",
"lead":"https://www.epa.gov/lead/real-estate-disclosures-about-potential-lead-hazards",
"hud":"https://archives.huduser.gov/portal/pdredge/pdr-edge-featd-article-081417.html",
"temps":"https://www.foodsafety.gov/food-safety-charts/safe-minimum-internal-temperatures",
"fda":"https://www.fda.gov/food/buy-store-serve-safe-food/refrigerator-thermometers-cold-facts-about-food-safety",
"four":"https://www.foodsafety.gov/keep-food-safe/4-steps-to-food-safety",
"poison":"https://www.poison.org/articles/spring-cleaning",
"cdc":"https://www.cdc.gov/hygiene/about/when-and-how-to-clean-and-disinfect-your-home.html",
"anchor":"https://www.anchorit.gov/2024/02/08/ahead-of-sundays-game-cpsc-reminds-families-to-tackle-the-deadly-hazard-of-tv-and-furniture-tip-overs/",
"cpsc":"https://www.cpsc.gov/Newsroom/News-Releases/2023/Plans-to-Watch-the-Big-Game-on-the-Big-Screen-CPSC-Reminds-Families-to-Protect-Children-from-the-Deadly-Hazard-of-Toppling-TVs-and-Furniture",
"sleep":"https://www.sleepfoundation.org/mattress-sizes",
"bb":"https://www.epa.gov/sites/default/files/2014-02/documents/bed-bug-prevention-detection-control.pdf",
"doe":"https://www.energy.gov/sites/default/files/2022-08/energy-saver-guide-2022.pdf"}
def SR(k,t): return ext(SRC[k],t)

p(f"A first apartment checklist should tell you two things: what to buy, and when you actually need it. This one covers every room in 53 tick boxes, from the lease and renters insurance to pots, towels and a plunger, and tags each item <em>Before</em> (before moving day), <em>Day 1</em> (for your first night), <em>Week 1</em> or <em>Later</em>. Buy the Day 1 items first and the rest as your budget allows; most of the Later list can be borrowed or bought secondhand.")
p(f"Print the two-page PDF and tick items off as you go. If you are still packing, our {a('moving-checklist-printable','printable moving checklist')} covers the move itself; this list starts when you get the keys.")
add('<!-- wp:html -->\n<div class="dsh-dl" style="display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px;background:#EEF3EC;border:1px solid #D5E0D0;border-radius:16px;padding:20px 24px;margin:2em 0"><div style="flex:1 1 260px"><p style="margin:0 0 4px;font-weight:700;font-size:1.1rem;color:#342E2A">Free printable first apartment checklist (PDF)</p><p style="margin:0;color:#6E645C;font-size:.95rem">Two pages: 8 sections, 53 tick boxes tagged Before, Day 1, Week 1 or Later, plus shopping tips. US Letter, fits A4.</p></div><a href="'+PDF+'" target="_blank" rel="noopener" style="background:#C85A32;color:#fff;border-radius:999px;padding:12px 22px;font-weight:700;text-decoration:none;white-space:nowrap">Download the PDF</a></div>\n<!-- /wp:html -->')
img(1)

h2("Before You Shop")
lst(["<strong>Measure first.</strong> Doorways, stairs and the bedroom, before you buy a bed or a sofa.",
"<strong>Day 1 items first.</strong> Your first night needs light, a bed, a towel, toilet paper and something to eat off.",
f"<strong>Borrow or buy used for the Later list,</strong> but inspect secondhand furniture first: the EPA says {SR('bb','do not bring second-hand furniture into your home')} until you have checked it thoroughly for bed bugs.",
f"<strong>Keep receipts and photos</strong> of what you buy; the Texas Department of Insurance suggests you {SR('tdi','fill out a home inventory')} so you know what your belongings are worth if you need to claim."])

h2("The First Apartment Checklist, Room by Room")
p("Each item ends with when you need it. Your lease comes first: some apartments already include a fridge, blinds or a smoke alarm, and some landlords have rules about what you can hang or install.")
for room,items in ROOMS:
    h3(room)
    lst([f"{t} <em>({g})</em>" for t,g in items])
    if room=="Safety and tools": img(4)
    if room=="Kitchen": img(2)
    if room=="Bathroom": img(3)

h2("Why These Items Are on the List")
h3("Renters insurance and the move-in inspection")
p(f"The NAIC, the US association of state insurance regulators, warns that {SR('naic','your landlord\'s insurance doesn\'t cover your personal property')}, and puts renters insurance at an average of {SR('naic','between $15 and $30 per month')}; the Insurance Information Institute's national average for 2022 was {SR('iii','$171')} a year. It isn't required by law, but the Texas Department of Insurance notes that {SR('tdi','some landlords might require you to have a renters policy')}, so check your lease.")
p(f"Your security deposit depends on proving what was already wrong. The Army's legal assistance office advises you to {SR('jag','ask your landlord for a move-in inspection sheet')}, note {SR('jag','any and every small scratch or stain')} and take photos when you move in and out. Deposit deadlines vary by state: New York requires landlords to return it {SR('ny','within 14 days')} and Texas {SR('tx','within 30 days')}, minus any deductions.")
h3("Utilities, mail and the budget")
p(f"The University of Illinois off-campus housing office suggests calling utility companies {SR('illu','at least one month prior to your move-in date')}. The USPS lets you file a change of address {SR('usps','90 days before the effective date of your move')}, with a {SR('usps','$1.25 authentication fee')} online. On budget, HUD treats households that {SR('hud','spend more than 30 percent of income on housing costs')} as cost burdened, which is why the 30% rule is the usual guide for rent. If your building was built before 1978, your landlord must give you the EPA lead hazard pamphlet and {SR('lead','disclose any known information')} about lead-based paint.")
h3("Smoke alarms, CO alarms and a fire extinguisher")
p(f"On your first day, test every smoke alarm. The US Fire Administration says to {SR('sa','put smoke alarms inside and outside each bedroom')} and on every level, to {SR('sa','test smoke alarms every month')} and that a dead or missing battery is the same as having no alarm. In some states the landlord must provide them; the Texas Attorney General notes that {SR('tx','the landlord must also provide smoke detectors')}. Carbon monoxide alarms belong {SR('co','outside each separate sleeping area and on every level')}, and more than 150 people in the US die every year from accidental non-fire CO poisoning.")
p(f"For a fire extinguisher, the USFA says home extinguishers are usually {SR('fe','multipurpose fire extinguishers that cover Class A through Class C')}. Learn the PASS steps: pull the pin, aim low at the base of the fire, squeeze the lever slowly and sweep from side to side, and only fight a small fire when you have a clear way out. While you are at it, plan {SR('usfa','2 ways out of every room')}.")
h3("Anchors, kitchen safety and cleaning")
p(f"The CPSC's Anchor It campaign says to {SR('anchor','anchor TVs and furniture, such as bookcases and dressers')}, and reports that {SR('anchor','17,800 people annually are injured')} in tip-overs; anti-tip kits {SR('cpsc','cost less than $20')} and take under 20 minutes. Ask your landlord before drilling. In the kitchen, the FDA says to keep the fridge {SR('fda','at 40 °F or below; the freezer should be at 0 °F')}, which is why a fridge thermometer is on the list, and FoodSafety.gov's chart puts poultry at {SR('temps','165°F')}. Use {SR('four','separate cutting boards')} for raw meat and produce. When you clean, Poison Control warns that {SR('poison','ammonia should never be mixed with chlorine or bleach products')}, and the CDC says to {SR('cdc','use an EPA-registered disinfecting product')} where you need to disinfect.")
h3("The right size bed")
p(f"A mattress is the biggest Day 1 purchase, so measure the room first. The Sleep Foundation lists a full at {SR('sleep','54” wide, 75” long')} and a queen at 60 by 80 inches, and suggests {SR('sleep','leaving about 24 inches of space around each side of your bed')}. Buy a mattress encasement too; the EPA lists encasements among its bed bug prevention steps.")

h2("Make It Feel Like Home")
p(f"Once the Day 1 and Week 1 items are done, the rest is the fun part. Our {a('studio-apartment-ideas','studio apartment ideas')} help you lay out one room, our {a('small-apartment-living-room-ideas','small apartment living room ideas')} cover seating and rugs, and the {a('rug-size-calculator','rug size calculator')} saves you from buying one that's too small. Swap any old bulbs for LEDs: the Department of Energy says they use {SR('doe','up to 90% less energy')} than incandescent bulbs.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('first apartment checklist'),'kw')
