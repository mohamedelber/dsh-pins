import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
RF="https://www.raymourflanigan.com/blog/expertise/guides/dining-table-size-guide"
DM="https://dimensions.com/element/dining-room-clearances"
CM=2.54
RECT={2:[[30,30],[30,36]],4:[[36,48],[36,60]],6:[[36,60],[40,72]],8:[[36,84],[40,96]],10:[[40,96],[42,108]],12:[[42,120],[44,132]]}
ROUND={2:[30,36],4:[36,44],6:[44,54],8:[54,60],10:[60,72],12:[72,84]}
def c5(x): return int(round(x*CM/5)*5)
def rs(t): return f"{t[0]} x {t[1]} in ({c5(t[0])} x {c5(t[1])} cm)"
def ft(x):
    f=int(x//12); i=round(x-f*12)
    if i==12: f+=1; i=0
    return f"{f} ft"+(f" {i} in" if i else "")
p("What size dining table do you need? Allow about 24 inches (61 cm) of table edge for each person, and leave at least 36 inches (91 cm) between the table and the walls so chairs can slide back. A table for six is usually about 36 to 40 inches wide and 60 to 72 inches long (90 to 100 x 150 to 185 cm).")
p("This free <strong>dining table size calculator</strong> works it out for you in two taps: choose how many people and the table shape, and it gives the comfortable size, the smallest size that still works and the room you need. Open <em>More options</em> to check whether a table fits your room.")
add('<!-- wp:html -->\n'+open('tool.html').read()+'\n<!-- /wp:html -->')
h2("Dining Table Size Chart")
rows=[]
for n in [2,4,6,8,10,12]:
    mn,cf=RECT[n]; r=ROUND[n]
    rows.append([str(n), rs(cf), f"{r[0]} to {r[1]} in ({c5(r[0])} to {c5(r[1])} cm)", f"{ft(cf[0]+72)} x {ft(cf[1]+72)}"])
table(["People","Rectangle (comfortable)","Round (diameter)","Room for a rectangle, 36 in all around"],rows)
p(f"The sizes follow the typical ranges in Raymour &amp; Flanigan's {ext(RF,'dining table size guide')}: rectangular tables about 60 to 72 inches long for 4 to 6 people, 84 inches for 6 to 8 and 96 inches for 8 to 10, and round tables 36 to 44 inches across for up to 4 people, 44 to 54 inches for 4 to 6 and 54 to 60 inches for 6 to 8. The guide gives no rectangle sizes for 2 or 12 people or round sizes for 10 or more, and our 108 in table for 10 is roomier than its 96 in, so those sizes are our own estimates.")
img(1)
h2("How the Dining Table Size Calculator Works")
lst([f"<strong>Space per person.</strong> Dimensions.com gives a {ext(DM,'place setting width')} of at least 24 in (61 cm) per person and 30 in (76 cm) for the most comfortable spacing. For rectangles, the smallest size allows about 24 in per person and the comfortable size more; round and square sizes follow Raymour &amp; Flanigan's ranges where it gives them.",
"<strong>End seats.</strong> For 6 or more people at a rectangle, the calculator assumes one person at each end. Without end seats, add about 24 in (61 cm) to the length.",
"<strong>Room size</strong> = the table plus the space you choose on every side: 36 in (91 cm) as the usual minimum, 42 to 48 in (107 to 122 cm) for a busy room or large chairs, or 60 in (152 cm) for wheelchair access.",
"<strong>Wide chairs or armchairs</strong> add about 12 in (30 cm) to the length of a rectangle and 6 in (15 cm) to a round or square table. This is our own rule of thumb.",
"<strong>Checking your room:</strong> the calculator takes the space around the table off both room measurements and compares what is left with the table. If even the smallest size does not fit, it shows the largest table your room can take."])
h2("How Much Space Do You Need Around a Dining Table?")
table(["Space from table edge to wall","Works for"],[
["36 in (91 cm)","Everyday use: chairs slide back and people can sit down"],
["42 to 48 in (107 to 122 cm)","Walking behind seated people, high-traffic rooms, large chairs"],
["54 to 60 in (137 to 152 cm)","Wheelchair access"]])
p(f"Raymour &amp; Flanigan recommends {ext(RF,'at least 36 inches from the table edge to walls or furniture')} for daily use and 42 to 48 inches for high-traffic areas or larger chairs. Dimensions.com puts the total clearance, a seated zone plus a walkway, at {ext(DM,'36 to 60 inches (91 to 152 cm)')} and accessible clearance at 54 to 60 inches (137 to 152 cm).")
img(2)
h2("Round, Square or Rectangular Table?")
lst(["<strong>Round tables</strong> suit small rooms and square rooms, have no corners to bump into and make conversation easy. Above about 60 in (152 cm) across, the center gets hard to reach.",
"<strong>Square tables</strong> work best for 4 people, or 8 on a large table. For 6 people, a rectangle usually uses the space better.",
"<strong>Rectangular tables</strong> fit long, narrow rooms and seat the most people. An extending table can seat extra guests and stay compact every day.",
"<strong>Benches</strong> slide fully under the table, so they save space in a tight room, and children can squeeze in."])
h2("Before You Buy a Dining Table")
lst(["<strong>Tape it out.</strong> Mark the table size on the floor with painter's tape, put the chairs around it and walk around it for a day.",
"<strong>Check the legs.</strong> Legs at the corners leave the long sides free; a pedestal base fits more chairs around a round table.",
"<strong>Measure the way in.</strong> Make sure the table fits through the doors, hallway and stairs to the dining room.",
f"<strong>Plan the rug.</strong> A rug under the table should be big enough that chairs stay on it when pulled out. Our {a('rug-size-calculator','rug size calculator')} works it out."],True)
img(3)
add(open('savebox.html').read())
h2("Dining Table Size FAQ")
h3("What size dining table seats 6?")
p("A rectangular table about 36 to 40 inches wide and 60 to 72 inches long (90 to 100 x 150 to 185 cm) seats six, with one person at each end. A round table for six is about 44 to 54 inches (110 to 135 cm) across. Leave 36 inches (91 cm) around it.")
h3("How much room do you need for a dining table?")
p("Add at least 36 inches (91 cm) to every side of the table, or 42 to 48 inches (107 to 122 cm) if people walk behind the chairs. A 40 x 72 inch table therefore needs a dining area of about 9 ft 4 in x 12 ft (2.8 x 3.7 m).")
h3("What size round table seats 4?")
p("A round table 36 to 44 inches (90 to 110 cm) across seats four people. Choose the larger size if you like room for serving dishes, and leave at least 36 inches (91 cm) around it, so the dining area needs to be about 9 ft to 9 ft 8 in (2.7 to 2.9 m) square.")
h3("How many people fit at an 8 ft table?")
p("An 8 ft (96 inch, about 245 cm) rectangular table seats 8 people comfortably, with three on each side and one at each end, and can squeeze in 10 with narrower spacing. Raymour & Flanigan lists 96 inch tables for 8 to 10 people.".replace("&","&amp;"))
h2("More Room Planning Tools")
p(f"Planning the whole room? Size the rug with our {a('rug-size-calculator','rug size calculator')} and hang art at the right height with our {a('picture-hanging-height-calculator','picture hanging height calculator')}. For the table itself, see our {a('christmas-table-decoration-ideas','Christmas table decoration ideas')}, and for an open-plan space try our {a('room-divider-ideas','room divider ideas')}. Short on storage near the table? Our {a('kitchen-storage-ideas','kitchen storage ideas')} help.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script.*?</script>|<style.*?</style>','',html))
print(len(html),'words',len(txt.split()),'kw',txt.lower().count('dining table size'))
for w in ['colour','metre','organise']:
    if w in txt.lower(): print('UK word',w)
