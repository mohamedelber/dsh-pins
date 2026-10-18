import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
CC="https://www.christmascentral.com/how-to-decorate-your-christmas-tree/"
WF="https://www.wayfair.com/sca/ideas-and-advice/guides/how-to-put-lights-on-a-christmas-tree-T8505"
GG="https://www.gatesgardencentre.co.uk/how-many-christmas-lights-do-i-need/"
AN="https://www.angi.com/articles/how-to-calculate-christmas-lights-needed.htm"
BH="https://balsamhill.co.uk/christmas-tree-decorations-ultimate-guide"
LE="https://www.livingetc.com/advice/how-to-hang-a-garland-on-a-christmas-tree"
US="https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/holiday/"
p("How many lights does a Christmas tree need? The usual rule is about 100 lights per foot of tree height, so a 7 ft tree needs around 700 lights, and 150 or even 200 per foot if you like a fuller, brighter look. This <strong>Christmas tree lights calculator</strong> works it out for your tree in two taps, and tells you how many strands to buy.")
p("Pick your tree height and the look you want. You also get a full shopping list: how many ornaments, how much garland and how much ribbon. Open <em>More options</em> for a slim or pencil tree, a different strand size or an exact height in feet or centimetres.")
add('<!-- wp:html -->\n'+open('tool.html').read()+'\n<!-- /wp:html -->')
h2("Christmas Tree Lights Chart")
rows=[]
for h in [4,5,6,6.5,7,7.5,8,9,10,12]:
    hs=(str(h).rstrip('0').rstrip('.') if isinstance(h,float) else str(h))
    rows.append([f"{hs} ft ({round(h*30.48)} cm)",f"{round(h*100):,}",f"{round(h*150):,}",f"{round(h*200):,}"])
table(["Tree height","Classic (100 per ft)","Full (150 per ft)","Extra bright (200 per ft)"],rows)
p(f"The 100-per-foot rule is the one you will see most often. Christmas Central says {ext(CC,'decorators typically recommend 100 mini lights for every foot')} of tree height, and Wayfair's {ext(WF,'guide to putting lights on a Christmas tree')} uses the same rule, rising to 150 per foot for an especially full tree. UK garden centre Gates gives a range of {ext(GG,'100 to 150 lights per foot')}, and Angi suggests up to {ext(AN,'200 per foot for high-powered brightness')}. Round up to whole strands, and if you are between two sizes, buy the bigger number: spare lights are easier than a gap.")
img(1)
h2("How the Calculator Works")
lst([f"<strong>Lights</strong> = tree height in feet x 100, 150 or 200, rounded to the nearest 10.",
"<strong>Strands</strong> = lights divided by the lights per strand on the box (100 by default), rounded up.",
f"<strong>Ornaments:</strong> Christmas Central recommends {ext(CC,'10 to 15 standard ornaments per foot')} for trees under 9 ft and 12 to 20 per foot for taller trees.",
f"<strong>Garland:</strong> about 9 ft of garland for every foot of a large tree, less on a small one (Christmas Central), and up to 10 ft per foot for a layered look ({ext(LE,'Livingetc')}). The calculator uses 9 ft per foot from 6 ft up and 7 ft per foot below that.",
f"<strong>Ribbon:</strong> Balsam Hill's {ext(BH,'tree decorating guide')} suggests at least 3 yards (about 2.7 m) per foot of tree.",
"<strong>Slim and pencil trees:</strong> they have far less branch surface, so we scale everything by 0.7 and 0.5. This is our own estimate, not a rule from the guides above."])
h2("How to Put Lights on a Christmas Tree")
lst(["<strong>Test every strand first.</strong> Plug each set in on the floor, so you find dead bulbs before they are on the tree.",
"<strong>Start at the bottom, near the socket.</strong> That way the plug end reaches the wall without an extension lead across the room.",
"<strong>Work deep, then out.</strong> Run the lights along each branch from the trunk to the tip and back. Lights near the trunk make the tree glow from inside.",
"<strong>Work in sections.</strong> Wayfair suggests a vertical method: picture the tree as three or four triangles from top to bottom and light one at a time. A loose spiral with about 3 inches between loops is quicker.",
"<strong>Step back and squint.</strong> Dark patches show up clearly. Move a few lights before you add ornaments."],True)
img(2)
p(f"Do not wrap the wire tightly around single branches. Wayfair notes that real branches can droop under heavy strands, so lightweight LED sets are kinder to a real tree.")
h2("Lights for Small, Slim and Tabletop Trees")
img(3)
p(f"A 4 ft tree still needs about 400 lights for the classic look, which surprises many people. Battery micro lights avoid a cable across the floor, and the thin wire disappears into small branches. A slim or pencil tree fits a narrow corner but has fewer, shorter branches, so you need fewer lights; switch the shape in <em>More options</em> to see the difference. For other small-space holiday ideas, see our {a('christmas-mantel-decorating-ideas','Christmas mantel decorating ideas')} and {a('coffee-table-decor','coffee table decor ideas')}.")
h2("Christmas Light Safety")
p(f"The U.S. Fire Administration's {ext(US,'holiday fire safety advice')} is short and practical:")
lst(["Read the manufacturer's instructions for the number of light strands you can connect.",
"Inspect holiday lights every year before you put them up, and throw away strands with frayed or pinched wires.",
"Keep the tree at least 3 feet (about 90 cm) from heat sources like fireplaces, radiators, space heaters, candles and heat vents, and keep it clear of exits."])
p("Wayfair adds that you should always turn off the lights on a real tree before you go to sleep or leave the house. Doing the same with an artificial tree costs nothing and is a good habit.")
add(open('savebox.html').read())
h2("Christmas Tree Lights FAQ")
h3("How many lights do I need for a 7 ft Christmas tree?")
p("A 7 ft tree needs about 700 lights for a classic look, using the rule of 100 lights per foot. For a fuller look use about 1,050 lights (150 per foot), and for an extra bright tree about 1,400 (200 per foot). That is 7, 11 or 14 strands of 100.")
h3("How many lights do I need for a 6 ft Christmas tree?")
p("Plan about 600 lights for a 6 ft tree, or 900 for a fuller look. With 100-light strands that is 6 or 9 sets. A slim 6 ft tree needs fewer, around 420 for the classic look, because it has less branch surface.")
h3("How many lights for a 7.5 ft tree?")
p("A 7.5 ft tree needs about 750 lights for the classic 100-per-foot look, about 1,130 for a full look and about 1,500 for extra bright. Most 7.5 ft pre-lit trees fall somewhere in this range, so check the box before you add more.")
h3("How many ornaments and how much garland do I need?")
p("For a 7 ft tree, plan 70 to 105 standard ornaments (10 to 15 per foot), about 63 ft (19 m) of garland and at least 21 yards (19 m) of ribbon. The calculator above works these out for any tree height.")
h2("More Holiday Guides")
p(f"When the season is over, our {a('christmas-decoration-storage','Christmas decoration storage ideas')} help you pack the lights so they do not tangle. Setting the table? See our {a('christmas-table-decoration-ideas','Christmas table decoration ideas')}, and for wrapping, our {a('gift-wrap-storage-ideas','gift wrap storage ideas')}. Planning the room around the tree? Try our {a('rug-size-calculator','rug size calculator')}.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script.*?</script>|<style.*?</style>','',html))
print(len(html),'words',len(txt.split()),'kw',txt.lower().count('christmas tree lights'))
print(sorted(set(re.findall(r'dailyspacehacks\.com/([a-z0-9-]+)/',html))))
