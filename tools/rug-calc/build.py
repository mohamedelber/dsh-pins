import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
HD="https://contentgrid.homedepot-static.com/hdus/en_US/DTCCOMNEW/fetch/Global_Assets/PDFs/Selecting-Proper-Rug-Size.pdf"
FW="https://fibreworks.com/pages/custom-size-rug-guide"
RL="https://www.ruglove.co.uk/pages/rug-sizes"
p("What size rug do you need? This free <strong>rug size calculator</strong> works out the right rug for a living room, dining room, bedroom or hallway from a few quick measurements, and shows the closest standard size to buy.")
p("It works in feet and inches or centimeters and gives US sizes (like 8' x 10') or UK sizes (like 160 x 230 cm). A typical living room is filled in, so change the numbers to match your room and the result updates as you type.")
add('<!-- wp:html -->\n'+open('tool.html').read()+'\n<!-- /wp:html -->')

h2("How to Choose the Right Rug Size")
p(f"The most common mistake is a rug that is too small. According to the {ext(HD,'Home Depot rug size guide')}, the right size depends on how the furniture is arranged, not just on the size of the room. Measure the furniture group first, then check that the rug still leaves a border of bare floor to the walls.")
diagram(open('z.svg').read(),"Rug size rules by room: front legs on the rug in a living room, 24 to 36 in of rug past every side of a dining table, at least 24 in past each side of a bed and 4 to 6 in of floor around a hallway runner.")
lst(["<strong>Measure the room</strong> from wall to wall, and note doors, vents and fireplaces.",
"<strong>Measure the furniture group</strong>: the sofa, the dining table or the bed.",
"<strong>Choose the look</strong>: all legs on the rug, front legs only, or a smaller rug under a coffee table.",
"<strong>Mark it out with painter's tape</strong> and live with it for a day before you buy."],True)
img(1)

h2("Living Room Rug Size")
p(f"The {ext(HD,'Home Depot guide')} shows three ways to place a living room rug. Our rug size calculator gives you all three:")
table(["Layout","How it looks","Typical size"],
[["All legs on the rug","Every piece of seating sits on the rug, with about 12 to 18 in (30 to 46 cm) of floor to the walls","10' x 13' or larger (280 x 360 cm)"],
 ["Front legs on the rug","The rug tucks under the front legs of the sofa and chairs","8' x 10' or larger (200 x 290 cm)"],
 ["Coffee table only","A smaller rug under the coffee table, about as long as the sofa","At least 5' x 8' (160 x 230 cm)"]])
p("Front legs on the rug is the easiest choice in most rooms: it connects the sofa and chairs without needing a huge rug, and it suits a sofa that stands against a wall. In a small living room, a rug under the coffee table works, but it should still be at least 5' x 8' so it does not look like a doormat.")

h2("Dining Room Rug Size")
p(f"A dining rug must be large enough that chairs stay on it when you pull them out. The {ext(FW,'Fibreworks custom rug guide')} suggests measuring the table and adding 24 to 36 in (61 to 91 cm) to each side, with 30 in (76 cm) as the sweet spot and 36 in for large upholstered chairs. The rug size calculator uses the chair setting you choose.")
table(["Table size","Rug needed (30 in each side)","Standard size to buy"],
[["36 x 60 in (4 seats)","96 x 120 in","8' x 10'"],
 ["40 x 72 in (6 seats)","100 x 132 in","9' x 12'"],
 ["42 x 84 in (8 seats)","102 x 144 in","9' x 12' (snug) or 10' x 13'"],
 ["48 in round","108 in round","10' round, or a square rug"]])
img(2)

h2("Bedroom Rug Size")
p(f"In a bedroom, the rug should show on both sides of the bed and at the foot. The {ext(HD,'Home Depot guide')} recommends that it extend at least 24 in (61 cm) from the edges of the bed, and the {ext(FW,'Fibreworks guide')} suggests 30 to 36 in (76 to 91 cm) on each side and at the foot, with the rug under at least the lower two-thirds of the bed.")
table(["Bed","Rug under the lower two-thirds","Rug under the whole bed"],
[["Twin","7' 6\" x 9' 6\" (6' x 9' if space is tight)","8' x 10'"],
 ["Full","7' 6\" x 9' 6\" or 8' x 10'","9' x 12'"],
 ["Queen","8' x 10'","9' x 12'"],
 ["King","9' x 12'","9' x 12' or 10' x 13'"]])
p("Stop the rug just short of the nightstands so they stand level on the floor. If the room is too small for a large rug, a runner on each side of the bed is a good alternative.")
img(3)

h2("Hallway Runner Size")
p(f"For a hallway, the {ext(FW,'Fibreworks guide')} recommends leaving about 4 to 6 in (10 to 15 cm) of floor between the runner and each wall and each end of the hallway. Fibreworks says a 30 in (76 cm) wide runner suits most hallways; common US lengths are 8, 10 and 12 ft. For a long hallway, use two runners in a row or order a custom length, and keep the runner clear of doors so they can open.")

h2("Standard Rug Sizes")
p(f"Rug sizes are not quite the same in the US and the UK. These are common sizes from the {ext(HD,'Home Depot guide')} and the UK retailer {ext(RL,'Rug Love')}. Exact sizes vary by brand, so check the label.")
table(["US size","In cm","Nearest UK size"],
[["3' x 5'","91 x 152 cm","80 x 150 cm"],
 ["4' x 6'","122 x 183 cm","120 x 170 cm"],
 ["5' x 8'","152 x 244 cm","160 x 230 cm"],
 ["8' x 10'","244 x 305 cm","200 x 290 cm"],
 ["9' x 12'","274 x 366 cm","280 x 360 cm"],
 ["10' x 13'","305 x 396 cm","280 x 360 cm or custom"]])

h2("Rug Size FAQ")
h3("What size rug do I need for my living room?")
p("For most living rooms, an 8' x 10' rug (or 200 x 290 cm in the UK) lets the front legs of the sofa and chairs rest on it. In a large room, go up to 9' x 12' or 10' x 13' so every leg fits, and keep about 12 to 18 in (30 to 46 cm) of floor showing to the walls.")
h3("How do you calculate rug size for a room?")
p("Measure the room and subtract 12 to 18 in (30 to 46 cm) from each side to leave a border of floor; that is the largest rug for an all-legs-on look. Then check the furniture: the rug should be a little longer than the sofa, or 24 to 36 in (61 to 91 cm) bigger than the dining table on every side. The rug size calculator above does both checks for you.")
h3("What size rug goes under a queen bed?")
p("An 8' x 10' rug laid crosswise under the lower two-thirds of a queen bed leaves about 30 in (76 cm) of rug on each side. For a rug under the whole bed, or in a bigger room, choose 9' x 12'.")
h3("Is it better to have a rug too big or too small?")
p("Slightly too big is usually better. A rug that is too small makes furniture look like it is floating and the room feel smaller. Just keep a border of bare floor around the edges so the rug does not run wall to wall.")

h2("More Planning Tools")
p(f"Planning the rest of the room? Try our {a('curtain-size-calculator','curtain size calculator')} for the windows, the {a('moving-box-calculator','moving box calculator')} if you are moving, and our ideas for {a('small-bedroom-storage-ideas','small bedroom storage')} and {a('room-divider-ideas','dividing a room without a wall')}.")
add('<!-- wp:paragraph {"className":"dsh-ai-note","fontSize":"small"} -->\n<p class="dsh-ai-note has-small-font-size"><em>How this tool was made: built with the help of AI tools, tested in the browser and published by Mohamed Elber. Results are planning estimates based on rug sizing guides from home and rug retailers; standard sizes vary by brand. Images are AI-generated illustrations. See our <a href="https://dailyspacehacks.com/editorial-policy/">Editorial Policy</a>.</em></p>\n<!-- /wp:paragraph -->')
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script>.*?</script>|<style>.*?</style>|<svg.*?</svg>','',html))
print(len(html),'words',len(txt.split()),'kw',txt.lower().count('rug size calculator'))
print(sorted(set(re.findall(r'dailyspacehacks\.com/([a-z0-9-]+)/',html))))
