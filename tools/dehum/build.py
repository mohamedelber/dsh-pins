import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={
"wd":"https://www.which.co.uk/news/article/can-you-use-a-dehumidifier-to-dry-laundry-aX79m5I0XFVm",
"wc":"https://www.which.co.uk/news/article/which-type-of-tumble-dryers-are-cheapest-to-run-aUOSv7x39Rdo",
"wb":"https://www.which.co.uk/reviews/tumble-dryers/article/how-to-buy-the-best-tumble-dryer-a2Xa42O3YWK7",
"wt":"https://www.which.co.uk/reviews/tumble-dryers/article/advice/energy-saving-tumble-drying-tips",
"meaco":"https://blog.meaco.com/when-to-buy-a-desiccant-dehumidifier-and-when-to-buy-a-compressor-dehumidifier",
"arete":"https://airconcentre.co.uk/products/meacodry-20l-arete-one-dehumidifier-white",
"man":"https://www.manchester.gov.uk/dampness",
"dorset":"https://www.dorsetcouncil.gov.uk/documents/35024/282001/How+to+prevent+damp+mould+and+condensation+in+your+home.pdf/52c52240-9d1b-39c5-4401-e665cc6e5a69",
"corn":"https://www.cornwall.gov.uk/fire-and-rescue-service/keeping-safe/fire-safety/fire-safety-at-home/washing-machines-and-tumble-dryers/",
"manual":"https://www.appliancesdirect.co.uk/PDFs/A1/DD8L-Zambezi_UserManual1.PDF"}
def SR(k,t): return ext(SRC[k],t)
LOADS=156
dh=round(0.26*2*LOADS,2)
tot_hp=round(350+54.32*5); tot_dh=round(234.90+dh*5); tot_c=round(220+138.91*5)

p(f"In the dehumidifier vs tumble dryer choice for drying clothes, a heat pump tumble dryer is usually cheaper per load and much faster than a dehumidifier, but a dehumidifier is cheaper to buy, takes up less space and also dries out a damp home. Which? tested both and found a dehumidifier {SR('wd','would still cost more and take longer')} than the most cost-effective tumble dryers. Over five years, though, our sums put a dehumidifier and airer within about £20 of a heat pump dryer.")
lst(["<strong>Choose a heat pump tumble dryer</strong> if you wash most days, need clothes dry in hours, and have room for one.",
"<strong>Choose a dehumidifier</strong> if you rent, have no space for a dryer, or also battle condensation and mould.",
"<strong>Avoid a new condenser dryer</strong> if running costs matter; it costs the most to run of the three."])
img(1)

h2("Dehumidifier vs Tumble Dryer at a Glance")
table(["","Dehumidifier + airer","Heat pump dryer","Condenser dryer"],[
["Cost per load",SR('wd','about 52p')+" (26p a litre, about 2 litres)","about 35p","about 89p"],
["Yearly running cost (3 loads a week)",f"about £{dh:.0f} (our estimate)",SR('wc','£54.32'),"£138.91"],
["Typical price to buy","£140 to £310","£327 to £1,699 (avg £727)",SR('wb','£220 to £529')],
["Drying time","Slower; Which? says it almost halves airer time","Hours","Hours"],
["Also dries the house","Yes","No","No"],
["Space","Small, moves room to room","Needs a dedicated spot","Needs a dedicated spot"]])
p("Tumble dryer running costs are from Which? at the October to December 2026 price cap of 26.32p per kWh. The dehumidifier cost per load uses Which?'s average of 26p per litre of water extracted.")

h2("What Five Years Actually Costs")
diagram(open('z.svg').read(),f"Estimated five-year cost: heat pump dryer about £{tot_hp}, dehumidifier and airer about £{tot_dh}, condenser dryer about £{tot_c}.")
p(f"To settle dehumidifier vs tumble dryer on cost, our estimate adds the price to buy to five years of running costs at three loads a week. A heat pump dryer at around £350, which Which? says is what {SR('wb','good heat pump dryers')} can cost, comes to about £{tot_hp}. A 20-litre compressor dehumidifier with a laundry mode, listed at {SR('arete','£234.90')}, plus 52p a load comes to about £{tot_dh}. A condenser dryer is cheapest to buy but about £{tot_c} over five years. Prices and energy rates will change, so use these as a guide.")

h2("Dehumidifier: Best for Small Homes and Damp")
img(2)
p(f"<strong>Best for:</strong> flats and rentals with no room or venting for a dryer, homes with condensation, and anyone who dries washing on airers already.")
p(f"A dehumidifier does two jobs. Which? found it {SR('wd','almost halved the drying time')} compared with an airer alone in the same room, and it also pulled around two litres of water out of the air. Manchester City Council says drying clothes indoors {SR('man','can add 10 - 15 litres of water a week')}, and that a dehumidifier helps reduce moisture. Dorset Council puts normal indoor humidity at around 40 to 55%, with the risk rising above 60%.")
p(f"Pick the right type. Meaco says a desiccant dehumidifier is better {SR('meaco','for temperatures below 10°C')}, such as an unheated utility room or garage, while compressor models are generally cheaper to run in a heated home. Which? advises keeping the unit at least 20cm from walls or furniture, and Meaco's manual says to place it on a {SR('manual','flat stable surface')} with the air vents clear.")
p(f"<strong>Avoid if:</strong> you need a full load dry in a couple of hours, or you dry several loads a day. Our guide on {a('how-to-dry-clothes-indoors','how to dry clothes indoors')} covers the rest of the routine.")

h2("Heat Pump Tumble Dryer: Best for Speed and Running Costs")
img(3)
p(f"<strong>Best for:</strong> families, people with no outdoor drying space, and anyone who wants towels dry the same evening.")
p(f"A heat pump dryer is the cheapest tumble dryer to run. Which? puts it at about £54.32 a year for three loads a week at the current price cap, against about £139 for condenser and vented models. It costs more to buy: Which? lists heat pump dryers from £327 to £1,699. From 19 January 2027, new vented, condenser and gas dryers can no longer be placed on the market in Great Britain, so heat pump dryers will be the main choice for new machines. Our {a('heat-pump-vs-condenser-dryer','heat pump vs condenser dryer guide')} explains the rule and the running costs in detail.")
p(f"<strong>Avoid if:</strong> you have no space, or you rent and cannot install one. Look after it safely: Cornwall Fire and Rescue advises you to {SR('corn','clean the filter in your dryer after every use')} and never leave it running overnight.")

h2("Our Pick")
lst([f"<strong>Family, daily washing, a utility room:</strong> a heat pump tumble dryer. See our {a('small-utility-room-ideas','small utility room ideas')} for where it fits.",
"<strong>One or two people in a flat:</strong> a compressor dehumidifier with a laundry mode and a good airer.",
"<strong>Damp, mould or an unheated room:</strong> a dehumidifier, desiccant if the room is below about 10°C.",
"<strong>Already own a condenser dryer:</strong> keep using it; the GB rule only affects new machines being sold."])

h2("Decide in Five Questions")
lst(["Do you dry more than four loads a week? <strong>Yes:</strong> heat pump dryer.",
"Do you have condensation or mould in winter? <strong>Yes:</strong> dehumidifier.",
"Is there no space or venting for a dryer? <strong>Yes:</strong> dehumidifier.",
"Do you need clothes dry in a few hours? <strong>Yes:</strong> heat pump dryer.",
"Is your budget under about £250? <strong>Yes:</strong> dehumidifier."],ordered=True)
p(f"Short of room for an airer? Our {a('laundry-closet-ideas','laundry closet ideas')} and {a('airing-cupboard-shelves','airing cupboard shelves')} show where drying space can hide.")
ai_note()
html='\n\n'.join(out)
html=re.sub(r'(\d+\.\d{2})\d+',r'\1',html)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('dehumidifier vs tumble dryer'),'kw',dh,tot_hp,tot_dh,tot_c)
