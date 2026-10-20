import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
VC="https://www.visualcomfort.com/inspiration/how-to-pick-the-right-chandelier-size-for-your-room/"
LP="https://lampsplus.com/chandeliers/"
KO="https://resources.kohler.com/webassets/kpna/brochures/KohlerLighting_QuickTipsGuide.pdf"
GL="https://goldenlighting.com/blogs/the-golden-edit/chandelier-size-calculator"
GH="https://goldenlighting.com/blogs/the-golden-edit/dining-room-light-height-2"
GF="https://goldenlighting.com/blogs/the-golden-edit/lighting-for-entrance-foyers-2"
HD="https://www.homedepot.com/c/ah/how-to-hang-a-chandelier/9ba683603be9fa5395fab9011d07599f"
LT="https://www.lightopia.com/kitchen-island-pendant-lighting-guide"
EC="https://www.ecmweb.com/national-electrical-code/qa/article/20899505/code-qa-outlet-boxes-used-to-support-luminaires"
p("What size chandelier do I need? Add the length and width of the room in feet, and the total is the chandelier's diameter in inches: a 12 x 14 ft room suits a chandelier about 26 in wide. Over a dining table, the rule changes: pick a fixture about half to two thirds as wide as the table. This free <strong>chandelier size calculator</strong> does the math for you in two taps.")
p("Choose the room, then its size or your table. Open <em>More options</em> to set your ceiling height or type exact measurements. You get the chandelier width, how tall the fixture should be and how high to hang it, plus a simple side view and tips for long tables, foyers and kitchen islands.")
add('<!-- wp:html -->\n'+open('tool.html').read()+'\n<!-- /wp:html -->')
h2("Chandelier Size Chart by Room Size")
table(["Room size","Chandelier width","Room size","Chandelier width"],[
["10 x 10 ft","about 20 in","14 x 14 ft","about 28 in"],
["10 x 12 ft","about 22 in","14 x 16 ft","about 30 in"],
["12 x 12 ft","about 24 in","16 x 18 ft","about 34 in"],
["12 x 14 ft","about 26 in","16 x 20 ft","about 36 in"]])
p(f"The rule is used across the lighting industry. Visual Comfort puts it simply: {ext(VC,'the width and length in feet equals the ideal chandelier diameter in inches')}, and Lamps Plus and Kohler give the same method. Golden Lighting treats the result as {ext(GL,'the fixture’s minimum diameter in inches')}, so in a room with tall ceilings you can go a little bigger.")
img(1)
h2("Chandelier Size for a Dining Table")
p(f"Over a table, the table matters more than the room. Visual Comfort suggests {ext(VC,'a fixture with a diameter that’s one half to two thirds the width of your table')}, while Kohler says {ext(KO,'the ideal diameter for the chandelier is 12\" less than the width of the table')}. Our calculator uses whichever is smaller, so the chandelier never overhangs the edges.")
table(["Table","Chandelier width","Bottom above the table (8 ft ceiling)"],[
["36 in wide (4 seats)","18 to 24 in","30 to 36 in"],
["40 in wide (6 seats)","20 to 27 in","30 to 36 in"],
["42 in wide (8 seats)","21 to 28 in","30 to 36 in"],
["48 in round","24 to 32 in","30 to 36 in"],
["60 in round","30 to 40 in","30 to 36 in"]])
p(f"For hanging height, Golden Lighting says to {ext(GH,'hang the fixture 30 to 36 inches above the tabletop as the standard starting point on an 8-foot ceiling')}, and to add roughly 3 in of drop for every extra foot of ceiling. Home Depot gives the same 30 to 36 in range. On a long rectangular table, a linear chandelier or two smaller fixtures spread the light better than one round chandelier.")
img(6)
h2("How Tall Should a Chandelier Be?")
p(f"For the height of the fixture itself, Lamps Plus says to {ext(LP,'multiply your ceiling height by 2.5–3')}, which gives the height in inches. Kohler uses a slightly lower 2 to 2.5, so treat the numbers below as a comfortable range rather than a strict rule.")
table(["Ceiling height","Fixture height","Bottom above a dining table"],[
["8 ft","20 to 24 in","30 to 36 in"],
["9 ft","23 to 27 in","33 to 39 in"],
["10 ft","25 to 30 in","36 to 42 in"],
["12 ft","30 to 36 in","42 to 48 in"]])
p("In a living room, bedroom or hallway where people walk underneath, the bottom of the chandelier should be at least 7 ft above the floor. On an 8 ft ceiling that leaves only about 12 in, so choose a flush or semi-flush fixture, or hang the chandelier over a table where nobody walks.")
h2("How the Chandelier Size Calculator Works")
lst(["<strong>Living room, bedroom and foyer:</strong> room length + room width in feet = chandelier width in inches. The bottom stays at least 7 ft above the floor.",
"<strong>Dining room:</strong> the width is half to two thirds of the table width, and never more than the table width minus 12 in. The bottom hangs 30 to 36 in above the table on an 8 ft ceiling, plus 3 in for every extra foot.",
"<strong>Kitchen island:</strong> pendants about 30 in apart, center to center, with each end pendant at least 6 in in from the end of the island and the bottoms 30 to 36 in above the counter. The maximum pendant width is our own estimate to leave a gap between shades.",
"<strong>Fixture height:</strong> 2.5 to 3 in per foot of ceiling height. If that will not fit above 7 ft, the calculator suggests a flush or semi-flush fixture instead."])
p("These rules are design guidelines from lighting makers and retailers, not building codes. Use them as a starting point, then trust your eye: a bold statement piece can go bigger, a delicate one smaller.")
h2("Foyer and Entryway Chandelier Size")
img(2)
p(f"Use the same room rule for a foyer. Kohler says to {ext(KO,"leave at least 7' between the floor and the base of the fixture")}. In a two-story foyer, Golden Lighting suggests you {ext(GF,'align with the second-floor landing')}, so the chandelier looks right from upstairs as well as from the front door.")
h2("Living Room and Bedroom Chandeliers")
img(3)
p("In a living room, center the chandelier in the room or over the main seating area, and keep the bottom at least 7 ft above the floor. In a bedroom, many people hang a small chandelier over the foot of the bed or the middle of the room rather than right above the pillows.")
img(5)
h2("Kitchen Island Pendant Spacing")
img(4)
p(f"Lightopia's guide says to {ext(LT,'hang pendants 30 to 36 inches above the countertop')} and to {ext(LT,'space pendants 24 to 30 inches apart, measured from the center of one fixture to the center of the next')}, leaving at least 6 in from the end of the island to the center of the first pendant. As a rough guide, a 6 ft island takes 3 pendants and an 8 ft island takes 3 to 4.")
h2("Chandelier Safety and Installation")
lst([f"<strong>Weight:</strong> under the National Electrical Code, as explained by EC&amp;M, {ext(EC,'outlet boxes for luminaires can support a luminaire that weighs up to 50 lb')}; a heavier fixture needs a box listed for its weight or separate support.",
f"<strong>Box rating:</strong> Home Depot notes that {ext(HD,'most ceiling boxes can hold 50 pounds to 75 pounds')}, so check the box before you buy a heavy chandelier.",
"<strong>Electrician:</strong> turn off the power at the breaker, and hire a licensed electrician if you need a new box, a brace or new wiring.",
"<strong>Headroom:</strong> keep at least 7 ft under any fixture where people walk."])
add(open('savebox.html').read())
h2("Chandelier Size FAQ")
h3("How do I know what size chandelier I need?")
p("Add the room's length and width in feet; the total is a good chandelier diameter in inches. A 12 x 14 ft room suits about 26 in. Over a dining table, choose a chandelier half to two thirds as wide as the table, and at least 12 in narrower than it.")
h3("How high should a chandelier hang over a dining table?")
p("Hang the bottom of the chandelier 30 to 36 in above the tabletop on an 8 ft ceiling, and add about 3 in for each extra foot of ceiling height. On a 10 ft ceiling, that means about 36 to 42 in above the table.")
h3("Can a chandelier be too big for a room?")
p("Yes. A chandelier much wider than the room rule, or wider than the table minus 12 in, crowds the space and can hit people standing up from the table. If you love a large piece, raise it a little and keep plenty of space around it.")
h3("What size chandelier for an 8 ft ceiling?")
p("For a fixture over a table, aim for about 20 to 24 in tall. Where people walk underneath, the bottom must stay at least 7 ft above the floor, which leaves about 12 in, so a flush or semi-flush chandelier works best.")
h2("More Free Room Tools")
p(f"Planning the whole dining room? Our {a('dining-table-size-calculator','dining table size calculator')} shows what table fits your room, our {a('rug-size-calculator','rug size calculator')} sizes the rug underneath and our {a('picture-hanging-height-calculator','picture hanging height calculator')} helps you hang art at the right height.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script.*?</script>|<style.*?</style>','',html))
print(len(html.encode()),'words',len(txt.split()),'kw',txt.lower().count('chandelier size calculator'),txt.lower().count('chandelier'))
