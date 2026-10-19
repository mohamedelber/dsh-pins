import re,json,math
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
DU="https://dunelm.com/info/buying-guides/how-to-measure-wallpaper"
PD="https://www.practicaldiy.com/decorating/wallpaper/wallpaper_quantity.php"
BV="https://www.bobvila.com/articles/how-to-measure-for-wallpaper/"
SW="https://www.selectedwallpapers.com/pages/european-rolls-vs-double-rolls"
FP="https://www.fabricsandpapers.com/blog/how-to-calculate-wallpaper-quantities"
BN="https://www.bunnings.com.au/wallpaper-trader-beach-people-wallpaper-roll-10-05m-x-61-5cm_p1069289"
FT=0.3048
def rolls(run,H,rep,rw=52,rl=10.05):
    drop=H+0.10+rep/100; d=math.ceil(run*100/rw-1e-4); dpr=math.floor(rl/drop+1e-4); return math.ceil(d/dpr)
p("How much wallpaper do you need? This free <strong>wallpaper calculator</strong> works it out drop by drop: it counts the drops (strips) your wall needs, how many drops you get from each roll once you allow for trimming and the pattern repeat, and turns that into the number of rolls to buy.")
p("Choose where you shop (UK, US, Canada or Australia), a feature wall or a whole room, then type the size and pick the pattern. It works in meters or feet, and under <em>More options</em> you can pick another roll size, a half-drop pattern or an exact pattern repeat.")
add('<!-- wp:html -->\n'+open('tool.html').read()+'\n<!-- /wp:html -->')
h2("How Many Rolls of Wallpaper Do I Need?")
p("These charts use standard rolls, 10 cm (4 in) of trim on every drop and the pattern repeat shown. They do not include the spare roll we recommend you add.")
rows=[]
for lab,run in [('Feature wall 2.5 m wide',2.5),('Feature wall 3 m wide',3),('Feature wall 4 m wide',4),('Feature wall 5 m wide',5),('Room 3 x 3 m',12),('Room 3 x 4 m',14),('Room 4 x 4 m',16),('Room 4 x 5 m',18)]:
    rows.append([lab,str(rolls(run,2.4,0)),str(rolls(run,2.4,64))])
table(["Walls 2.4 m high, 52 cm x 10.05 m rolls","Plain or no repeat","Large repeat (64 cm)"],rows)
rows=[]
for lab,run in [('Feature wall 10 ft wide',10),('Feature wall 12 ft wide',12),('Feature wall 14 ft wide',14),('Room 10 x 10 ft',40),('Room 10 x 12 ft',44),('Room 12 x 12 ft',48),('Room 12 x 14 ft',52)]:
    rows.append([lab,str(rolls(run*FT,8*FT,0,52.07,33*FT)),str(rolls(run*FT,8*FT,64,52.07,33*FT))])
table(["Walls 8 ft high, 20.5 in x 33 ft rolls","Plain or no repeat","Large repeat (25 in)"],rows)
p("Notice the difference between the two charts. A 2.4 m wall plus trim is 2.5 m per drop, so a 10.05 m roll gives exactly four drops. An 8 ft wall plus 4 in of trim is about 8 ft 4 in, and four of those need just over 33 ft, so a 33 ft roll gives only three full drops. On 8 ft walls, a pattern repeat often costs you nothing extra.")
img(1)
h2("How to Calculate Wallpaper Needed")
p(f"It uses the strip method from Bob Vila's guide on {ext(BV,'how to measure for wallpaper')}, instead of dividing the wall area by the roll area. Area alone ignores the paper you waste at the top and bottom of every drop.")
lst(["<strong>Drops needed</strong> = the width to cover (one wall, or the distance all the way around the room) divided by the roll width, rounded up.",
f"<strong>Length of each drop</strong> = wall height + 10 cm (4 in) for trimming + the pattern repeat. The trim follows Selected Wallpapers, whose calculator allows {ext(SW,'about 2 in (5 cm) on all sides')}.",
"<strong>Drops per roll</strong> = roll length divided by the drop length, rounded down. A leftover piece shorter than a full drop is waste.",
"<strong>Rolls</strong> = drops needed divided by drops per roll, rounded up. We add one spare roll on top."],True)
p(f"The results match the figures in Dunelm's {ext(DU,'wallpaper measuring guide')}: with standard 52 cm x 10.05 m rolls and walls about 2.4 m high, a wallpaper with no repeat gives four drops per roll, and a repeat of up to 64 cm gives three.")
h2("How to Measure for Wallpaper")
lst(["<strong>Measure the width.</strong> For a feature wall, measure from corner to corner. For a whole room, measure all the way around, including chimney breasts and other projections, as Practical DIY advises.",
"<strong>Measure the height</strong> from the top of the skirting board (baseboard) to the ceiling or coving, in a few places. Use the tallest figure.",
"<strong>Do not take off doors and windows.</strong> Bob Vila's guide says not to deduct them. Practical DIY only subtracts very large windows or areas that will not be papered.",
"<strong>Read the label</strong> for the roll width, roll length and pattern repeat, and enter them under More options if they are not standard."],True)
img(2)
h2("Wallpaper Calculator With Pattern Repeat")
p(f"The pattern repeat is the height after which the design starts again. To line the pattern up across the seams, each drop has to start at the same point in the design, so you lose up to one repeat of paper on every drop. Practical DIY notes that, generally, {ext(PD,'the larger the vertical repeat, the more rolls you will need')}, because the waste is greater.")
p("Plain papers, textured papers and designs labeled free match have no repeat to line up. Even a small repeat of around 27 cm (10.6 in) can cost you a whole drop per roll on 2.4 m walls, and large repeats of 53 or 64 cm (21 to 25 in) waste more on taller walls. On a big room, that adds several rolls.")
p(f"<strong>Half-drop patterns</strong> need more paper again. With a half drop, every other drop starts half a repeat lower, so the motifs step diagonally across the wall. Fabrics &amp; Papers' guide to {ext(FP,'calculating wallpaper quantities')} says to add a pattern repeat for each drop apart from the first, and for a half drop to add half of the total pattern repeat again. Our calculator allows one and a half repeats on every drop for a half drop, which also covers the first drop. Choose <em>Half drop</em> under More options; the match type is printed on the label.")
h2("Wallpaper Roll Sizes")
table(["Roll","Width","Length","Covers about"],[
["Standard UK roll","52 cm (20.5 in)","10.05 m (33 ft)","5.2 m² (56 sq ft)"],
["European roll","53 cm (20.9 in)","10 m (32.8 ft)","5.3 m² (57 sq ft)"],
["Some Australian brands","61.5 cm (24.2 in)","10.05 m (33 ft)","6.2 m² (66 sq ft)"],
["US double roll","20.5 to 27 in","27 to 33 ft","56 to 70 sq ft"],
["US single roll","20.5 to 27 in","13.5 to 16.5 ft","28 to 35 sq ft"]])
p(f"Sizes come from Practical DIY (standard UK roll) and {ext(SW,'Selected Wallpapers')} (European and US rolls). Selected Wallpapers notes that one European roll is roughly one American double roll. In Australia, Bunnings lists {ext(BN,'Wallpaper Trader rolls at 10.05 m x 61.5 cm')}, wider than the UK standard, so always copy the roll size from the label. Before you order, check whether the price and the label refer to a single or a double roll.")
img(3)
h2("Before You Buy")
lst(["<strong>Buy one spare roll</strong>, or two for a large repeat on a big room. Bob Vila suggests one or two more rolls than you think you need, and Practical DIY adds a couple for large repeats.",
"<strong>Check the batch number</strong> on every roll. Practical DIY advises buying only rolls with the same batch or lot number to ensure color matching, and Dunelm recommends buying extra for complex rooms to ensure batch continuity.",
"<strong>Keep the spare</strong> with its label. It is useful for repairs later."])
add(open('savebox.html').read())
h2("Wallpaper Calculator FAQ")
h3("How many rolls of wallpaper do I need for a feature wall?")
p(f"A feature wall 3 m (about 10 ft) wide and 2.4 m (8 ft) high needs 2 standard rolls with no pattern repeat: six drops, four drops per roll on a 2.4 m wall. A 4 m wall with a large repeat needs 3. Add one spare roll from the same batch.")
h3("How many rolls of wallpaper for a 12 x 12 room?")
p("A 12 x 12 ft room with 8 ft walls needs about 10 standard 20.5 in x 33 ft rolls: 48 ft of wall all the way around is 29 drops, and each roll gives three drops once you allow for trimming. Buy 11 to have a spare. Doors and windows are not taken off.")
h3("How many drops do you get from a roll of wallpaper?")
p("A standard 10.05 m roll gives four drops on a wall about 2.4 m high with no pattern repeat, and three drops with a repeat of up to 64 cm. On taller walls or with a large repeat you may only get two or three drops per roll.")
h3("How do you calculate half drop wallpaper?")
p("Work out the length of each drop as usual (wall height plus about 10 cm or 4 in for trimming), then add one and a half pattern repeats instead of one. Divide the roll length by that drop length to get the drops per roll, and divide the drops you need by that number. Choose Half drop in the calculator to do it for you.")
h3("Should I subtract doors and windows when measuring for wallpaper?")
p("Usually not. You still need drops above and below doors and windows, and cutting around them wastes paper. Measure the full wall and only subtract very large openings, such as a wide patio door or a wall of windows.")
h2("More Room Planning Tools")
p(f"Decorating a bedroom? Our {a('box-room-bedroom-ideas','box room bedroom ideas')} and {a('small-bedroom-storage-ideas','small bedroom storage ideas')} help you plan the rest, and wallpaper is one of the easiest ways to dress up a small {a('powder-room-decor-ideas','powder room')} or {a('downstairs-toilet-ideas','downstairs toilet')}. For soft furnishings, try our {a('curtain-size-calculator','curtain size calculator')} and {a('rug-size-calculator','rug size calculator')}.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script.*?</script>|<style.*?</style>','',html))
print(len(html),'words',len(txt.split()),'kw',txt.lower().count('wallpaper calculator'))
for w in ['colour','metre','centimetre','organise']:
    if w in txt.lower(): print('UK word',w)
