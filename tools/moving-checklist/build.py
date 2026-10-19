import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
PDF=json.load(open('pdf.json'))['url']
FM1="https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/ReadytoMoveBrochure_2022Update.pdf"
FM2="https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/Protect_Your_Move_Brochure.pdf"
HH="https://www.hireahelper.com/advice/how-far-in-advance-should-you-book-movers/"
USPS="https://faq.usps.com/articles/Knowledge/Change-of-Address-The-Basics"
RM="https://www.royalmail.com/d8/help/redirection"
IRS="https://www.irs.gov/pub/irs-access/f8822_accessible.pdf"
UV="https://unitedvanlines.com/moving-tips/moving-checklists/first-night-box"
CA="https://www.citizensadvice.org.uk/consumer/energy/energy-supply/moving-home-your-energy-supply/moving-home-dealing-with-your-energy-supply/"
VOTE="https://www.usa.gov/change-voter-registration"
DVLA="https://www.gov.uk/change-address-driving-licence"
HMRC="https://www.gov.uk/tell-hmrc-change-address"
PDSA="https://pdsa.org.uk/what-we-do/blog/moving-house-with-pets"
p("A good <strong>moving checklist printable</strong> turns one huge job into small weekly ones. Start about 8 weeks before moving day: book movers and declutter first, forward your mail and switch the utilities about 4 weeks out, pack an essentials box in moving week, and take meter readings on the day itself.")
p("This free checklist does the planning for you in two taps: pick how long you have until you move and whether you rent or own, and it builds your list in the right order, with catch-up tasks at the top if you are starting late. Add your moving date under <em>More options</em> to put a date on every step, tick tasks as you go, then print it or download the free two-page PDF.")
add('<!-- wp:html -->\n'+open('tool.html').read().replace("var PDF='';","var PDF='"+PDF+"';")+'\n<!-- /wp:html -->')
add('<!-- wp:html -->\n<div class="dsh-dl" style="display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px;background:#EEF3EC;border:1px solid #D5E0D0;border-radius:16px;padding:20px 24px;margin:2em 0"><div style="flex:1 1 260px"><p style="margin:0 0 4px;font-weight:700;font-size:1.1rem;color:#342E2A">Free printable moving checklist (PDF)</p><p style="margin:0;color:#6E645C;font-size:.95rem">Two pages: week-by-week tasks, a who-to-tell list and space for notes. US Letter, fits A4.</p></div><a href="'+PDF+'" target="_blank" rel="noopener" style="background:#C85A32;color:#fff;border-radius:999px;padding:12px 22px;font-weight:700;text-decoration:none;white-space:nowrap">Download the PDF</a></div>\n<!-- /wp:html -->')
img(1)
h2("Moving Checklist Timeline at a Glance")
table(["When","Main jobs"],[
["8 weeks before","Set the date and budget, get quotes from movers or book a van, declutter, give notice if you rent"],
["6 weeks before","Order boxes, measure furniture, use up food, pack things you rarely use"],
["4 weeks before","Forward your mail, book the utilities switch, update your address, pack room by room"],
["2 weeks before","Confirm the movers, plan parking, refill prescriptions, take furniture apart"],
["Moving week","Pack the essentials box and a bag for a few days, clean as you go"],
["Moving day","Meter readings and photos, last walk-through, check every box arrived"],
["First week after","Unpack the kitchen and bathroom, test the alarms, update your license and voter registration"]])
p("Short on time? The checklist moves the tasks you have missed into a <em>Start now</em> list and drops the nice-to-haves, such as using up the freezer, so you only see what still matters.")
h2("8 to 6 Weeks Before Moving: Book Movers and Declutter")
p(f"Booking early gives you a choice of dates and prices. HireAHelper suggests booking movers {ext(HH,'roughly 4 to 8 weeks before your move')}, and earlier in the peak season from May to September. For a move to another US state, the FMCSA's {ext(FM1,'Ready to Move brochure')} advises getting estimates from at least three movers or brokers and checking that the mover has a USDOT number. Its {ext(FM2,'Protect Your Move brochure')} lists a demand for cash or a large deposit before the move as a red flag.")
p(f"Declutter before you pack, not after: every box you do not move saves packing time and money. Our guide on {a('how-to-declutter-your-home','how to declutter your home')} goes room by room, and the {a('moving-box-calculator','moving box calculator')} tells you how many boxes to order once you know what is going.")
h2("4 Weeks Before Moving: Forward Your Mail and Switch Utilities")
lst([f"<strong>US mail:</strong> USPS lets you submit a change of address {ext(USPS,'up to 90 days before')} your move. Online, there is a $1.25 identity check fee; allow 7 to 10 business days for it to start. First-Class Mail is forwarded for 12 months.",
f"<strong>UK post:</strong> Royal Mail needs {ext(RM,'at least five working days')} to set up Redirection and suggests applying about three weeks before you move. You can redirect post for three, six or twelve months.",
f"<strong>Taxes:</strong> in the US, you can tell the IRS about a new address with {ext(IRS,'Form 8822')}. In the UK, HMRC asks you to {ext(HMRC,'wait until you have moved')} before telling it your new address, so that task sits in the first week.",
"<strong>Utilities:</strong> book the switch of electricity, gas, water and internet for both homes now, so nothing is cut off on the day and you are not paying for the old home after you leave."])
img(2)
h2("Moving Week: Pack an Essentials Box")
p(f"United Van Lines recommends a {ext(UV,'first-night box')}, so you have the basics at hand before the rest is unpacked. Pack it last, label it clearly and take it in the car with you:")
lst(["Bedding and a towel for each person","Phone chargers and a power bank","Toilet paper, soap and toiletries","Medicine and prescriptions","A kettle, mugs, snacks and a few plates","A box cutter, a small tool kit and trash bags","Clothes for the next day"])
img(3)
h2("Moving Day Checklist")
p(f"Citizens Advice recommends you {ext(CA,'read your meters on the day you move out')} and again on the day you move in, and give the readings to the supplier. A photo of each meter shows the date too. If you rent, photograph every room after cleaning; those photos help if there is a dispute about the deposit. Do a last walk-through of every cupboard, the attic or loft, the garage and the shed before you lock up.")
p("Keep documents, keys, medicine and valuables with you rather than in the van. At the new home, check that every box and piece of furniture has arrived before the movers leave, and note any damage.")
h2("First Week in Your New Home")
lst([f"<strong>Update official records.</strong> In the US, you must {ext(VOTE,'update your voter registration')} when you move, and the deadline for a new driver's license varies by state. In the UK, changing the address on your driving licence with {ext(DVLA,'DVLA is free')}, and you can be fined up to £1,000 if you do not.",
"<strong>Safety first.</strong> Test the smoke and carbon monoxide alarms, and find the main water shutoff and the breaker panel or fuse box before you need them.",
f"<strong>Pets.</strong> PDSA suggests giving your pet one quiet room on moving day and telling the {ext(PDSA,'microchip company')} your new address and contact details.",
"<strong>Unpack in order.</strong> Kitchen and bathroom first, then bedrooms, then everything else."])
h2("How This Moving Checklist Works")
lst(["<strong>Two taps:</strong> how long until you move and whether you rent or own. Renters get deposit tasks; owners get closing or completion and lock tasks.",
"<strong>Starting late:</strong> tasks from earlier weeks move into a <em>Start now</em> list at the top, and optional ones are left out.",
"<strong>More options:</strong> a moving date puts a date on every step; kids, pets, long distance and how you move add or remove tasks; the country switch shows US or UK wording, such as USPS or Royal Mail.",
"<strong>Your ticks</strong> are saved only in your own browser. Nothing is sent to us.",
"<strong>The weeks</strong> are a common moving timeline, not a rule: if a task suits your move better earlier or later, do it then."])
add(open('savebox.html').read())
h2("Moving Checklist FAQ")
h3("How far in advance should you start planning a move?")
p("Start about 8 weeks before moving day. That gives you time to compare at least three movers, declutter and give notice on a rental. In the busy May to September season, book movers even earlier. If you have less time, start with the urgent tasks: movers, mail forwarding and utilities.")
h3("What should I do 2 weeks before moving?")
p("Two weeks before moving, confirm the date, time and both addresses with the movers or the rental company, plan parking at both homes, refill prescriptions, return borrowed items and take apart furniture you can do without. Keep the screws in a labeled bag taped to each piece.")
h3("What is the first thing to do when you move?")
p("Set the moving date and budget, then book movers or a van, because good dates fill up first. Next, give notice if you rent, then declutter before you buy boxes. On arrival, the first jobs are meter readings, making the beds and unpacking the essentials box.")
h3("Who do I need to tell when I move?")
p("Tell the post office, your bank and card providers, employer, doctor and dentist, insurers, phone and internet provider, subscriptions, school, the tax office and the driving license authority, and update your voter registration. The free PDF has a who-to-tell list you can tick off.")
h2("More Moving Tools")
p(f"Work out how many boxes to buy with our {a('moving-box-calculator','moving box calculator')}, and if your dates do not line up, our {a('storage-unit-size-calculator','storage unit size calculator')} shows what size unit you need. Before you pack, our {a('closet-clean-out','closet clean-out')} guide and tips on {a('how-to-fold-clothes-to-save-space','how to fold clothes to save space')} cut the number of boxes, and once you arrive, start with {a('how-to-organize-kitchen-cabinets','how to organize kitchen cabinets')}.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script.*?</script>|<style.*?</style>','',html))
print(len(html),'words',len(txt.split()),'kw',txt.lower().count('moving checklist'))
for w in ['colour','organise','personalise']:
    if w in txt.lower(): print('UK word',w)
