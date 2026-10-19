import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={"hg":"https://www.homesandgardens.com/interior-design/what-is-bohemian-style",
"dict":"https://www.dictionary.com/browse/bohemian",
"rug":"https://ruggable.com/en-CA/blogs/bedroom-and-bedside-rug-ideas-for-cozy-comfort",
"cit":"https://the-citizenry.com/blogs/design/rug-size-and-style-guide",
"heat":"https://www.cpsc.gov/Newsroom/News-Releases/2026/Keep-Warm-and-Safe-This-Winter-Tips-for-Using-Generators-Furnaces-and-Space-Heaters",
"ny":"https://www.dhses.ny.gov/earthquake",
"hd":"https://www.homedepot.com/c/ah/how-to-hang-a-picture/9ba683603be9fa5395fab9009928978",
"pothos":"https://www.aspca.org/pet-care/animal-poison-control/toxic-and-non-toxic-plants/golden-pothos",
"fig":"https://www.aspca.org/news/houseplant-safe-your-pets",
"fern":"https://www.aspca.org/node/4659",
"palm":"https://www.aspca.org/node/5217",
"lights":"https://www.cpsc.gov/Newsroom/News-Releases/2009/CPSC-Releases-Dos-and-Donts-of-Holiday-Decorating",
"esfi":"https://www.esfi.org/news/avoid-serious-electrical-and-fire-hazards-decorating-your-home-this-holiday-season/"}
def SR(k,t): return ext(SRC[k],t)
p("Boho bedroom ideas are all about a room that feels relaxed, warm and lived in: natural textures, layered textiles, plenty of plants and a mix of pieces that look collected over time. The best part is that a boho bedroom does not need a big budget. Most of the look comes from fabric, baskets and greenery.")
p("This guide covers what makes a bedroom boho, the rug rule that anchors the whole room, a 6-step plan and 20 boho bedroom ideas for the bed, walls, plants, lighting and small or rented rooms, with the safety notes that matter when you hang things over a bed.")
img(1)
summary(["<strong>Quick answer:</strong> Start with a calm base of white or cream bedding and warm walls. Layer textiles in terracotta, rust and sage, add natural materials like rattan, jute and wood, bring in a few plants and finish with warm, low lighting.",
"Anchor the bed with a big jute or wool rug: about 8 x 10 ft for a queen and 9 x 12 ft for a king.",
"Keep anything heavy away from the space above the bed, choose pet-safe plants if you have cats or dogs, and switch decorative lights off at bedtime."],
"<strong>Time:</strong> a weekend · <strong>Cost:</strong> about $100 to $500 · <strong>Difficulty:</strong> Easy")
toc("boho-bedroom-ideas")
h2("What Makes a Bedroom Boho?")
p(f"Boho is short for bohemian, a word that describes {SR('dict','a person who lives and acts free of regard for conventional rules')}, and the style follows the same spirit. As designer Kathy Kuo puts it, {SR('hg','bohemian design is less formal and more eclectic')} than most decor styles. In a bedroom, that usually comes down to five ingredients:")
lst(["<strong>Natural materials:</strong> rattan, cane, jute, linen, cotton and wood.",
"<strong>Layered textiles:</strong> throws, pillows and rugs in different textures.",
"<strong>Plants:</strong> a tall plant in a basket and a few smaller ones.",
"<strong>A warm, earthy palette:</strong> cream with terracotta, rust, sage and honey tones.",
"<strong>Collected pieces:</strong> handmade, vintage or thrifted finds that tell a story."])
p("You do not need all five at full volume. A calm base with two or three of them looks more grown-up than a room that tries to do everything.")
h2("The Rug Rule: What Size Rug Goes Under a Boho Bed?")
p(f"A large natural rug is what makes a boho bedroom feel finished. Ruggable recommends {SR('rug','18–24 inches of rug visible on each side and at the foot of the bed')} (The Citizenry suggests about two feet), which points to an {SR('cit','8 x 10 ft rug for a queen and 9 x 12 ft for a king')}, turned sideways under the bed.")
diagram(re.sub(r'(\d+\.\d{1,2})\d+',r'\1',open('z.svg').read()),"What size rug goes under the bed: an 8 x 10 ft rug for a queen and a 9 x 12 ft rug for a king, with 18 to 24 in or more showing, plus a simple boho color palette.")
table(["Bed","Rug size","Rug showing on each side","Tip"],[
["Queen (60 x 80 in)","8 x 10 ft","30 in","Turn the rug sideways, front legs of the nightstands on the rug"],
["King (76 x 80 in)","9 x 12 ft","34 in","Start the rug at or just under the headboard"],
["Any bed, smaller budget","Two runners or small rugs","Placed on each side","Layer a small hide-style or kilim-style rug on top"]])
p(f"Not sure what fits your floor? Our {a('rug-size-calculator','rug size calculator')} works it out from your room and bed size.")
h2("Quick Pick: Boho Bedroom Ideas by Situation")
table(["Your situation","Best ideas","Cost"],[
["Change the look this weekend","#2, #3, #4, #10","Low"],
["Small bedroom","#16, #17, #18","Low to medium"],
["Renting","#6, #13, #17, #19","Low"],
["Have cats or dogs","#12, #18","Low"],
["Want a bigger change","#1, #5, #8, #13","Medium"]])
h2("How to Create a Boho Bedroom in 6 Steps")
lst(["<strong>Clear and calm the base.</strong> Start with white or cream bedding and remove anything that does not fit the warm, natural look.",
"<strong>Pick a palette.</strong> Choose cream plus two or three earthy accents, such as terracotta, rust and sage.",
"<strong>Ground the bed.</strong> Add a big jute or wool rug sized to the bed.",
"<strong>Layer the textiles.</strong> Add a throw, three to five throw pillows in mixed textures and linen curtains.",
"<strong>Bring in nature.</strong> Add one tall plant, one or two small ones and a few rattan or wood pieces.",
"<strong>Light it warmly.</strong> Swap a harsh ceiling light for a woven pendant or lamps with warm-white bulbs."],True)
img(6)
h2("Boho Bed and Bedding Ideas")
h3("1. A Low Wood or Rattan Bed")
p("A low platform bed in light wood, or a headboard in rattan or cane, sets the relaxed tone right away. If you are keeping your current bed, a slipcovered or upholstered headboard in a natural fabric works too.")
h3("2. A White Linen Base")
p("White or cream linen bedding is the calm backdrop that lets everything else stand out. Linen looks best a little rumpled, so it suits the easy boho look and needs no ironing.")
h3("3. Layered Throws and Blankets")
img(4)
p("Fold a waffle blanket at the foot of the bed and drape a fringed or woven throw over one corner. Mixing textures, smooth with chunky or flat-weave with fringed, matters more than matching colors.")
h3("4. Mixed Throw Pillows in Earthy Tones")
p("Three to five throw pillows is plenty. Pick one solid, one textured and one pattern in your palette, and vary the sizes so the bed looks layered rather than crowded.")
h3("5. A Light Fabric Canopy")
img(3)
p(f"A gauzy canopy hung from a ceiling ring or rail makes the bed feel like a cozy nook. Fix the hook into a joist or use a ceiling anchor rated for the weight, and keep the fabric well away from lamps and heaters: the CPSC advises keeping portable heaters {SR('heat','at least three feet away from drapes, furniture, bedding')} and other things that can burn.")
h2("Boho Wall Ideas")
h3("6. A Macrame Wall Hanging")
img(2)
p("A cream macrame piece on a wooden dowel adds texture and softness to a bare wall. It is light, so a single hook or nail holds it, which also makes it a good choice for renters.")
h3("7. A Woven or Rattan Wall Piece Above the Bed")
p(f"Round rattan wall decor, woven baskets or a light textile are the classic boho choice for the wall above the bed. Keep it light: New York State emergency guidance says to {SR('ny','hang heavy items such as pictures and mirrors away from beds')}, and Home Depot recommends anchoring hooks {SR('hd','in a stud')} whatever the size of the frame.")
h3("8. A Small Gallery of Prints")
p(f"Group three to five prints with botanical or abstract earthy art in simple wood frames. Hang the center of the group at eye level; our {a('picture-hanging-height-calculator','picture hanging height calculator')} tells you where to put each nail.")
h3("9. Floating Shelves With Plants and Books")
p(f"A couple of shelves give you a place for small plants, a few books and a vintage find. See our guide to {a('diy-floating-shelves','DIY floating shelves')} for how to fix them safely into studs or the right anchors.")
h2("Boho Plant Ideas")
h3("10. A Tall Plant in a Woven Basket")
img(5)
p("One tall plant in the corner does more than several small ones. Set the pot on a saucer inside a woven basket so water does not damage the basket or the floor. If you have pets, check idea #12 first: the fiddle-leaf fig is mildly toxic to cats and dogs.")
h3("11. A Hanging Planter")
p("A trailing plant in a macrame or ceramic hanging planter fills an empty corner without taking floor space. Hang it from a ceiling hook rated for the weight of the pot, soil and water, and not directly over the bed.")
h3("12. Pet-Safe Plant Picks")
p(f"If you have cats or dogs, check every plant first. The ASPCA lists golden pothos as {SR('pothos','toxic to dogs and cats')}, and says the popular fiddle-leaf fig is {SR('fig','mildly toxic to dogs and cats')}. Safer choices include the {SR('fern','Boston fern')} and the {SR('palm','parlor palm')}, both listed by the ASPCA as non-toxic to dogs and cats.")
h2("Boho Lighting Ideas")
h3("13. A Woven Pendant Light")
p("A rattan or bamboo pendant casts soft, patterned light and is one of the quickest ways to make a room look boho. Renters can use a plug-in pendant kit hung from a ceiling hook.")
h3("14. Warm Lamps Instead of the Ceiling Light")
p("Use warm-white bulbs, around 2700K, in a table lamp or two. Low, warm light makes layered textiles and wood tones glow in the evening.")
h3("15. String Lights, Used Safely")
p(f"If you love string lights, the CPSC says to use lights {SR('lights','tested for safety by a nationally-recognized testing laboratory, such as UL')}, check them for frayed or bare wires, and turn them off when you go to bed or leave the house. ESFI gives the same advice: {SR('esfi','turn off all indoor and outdoor electrical decorations')} before leaving home or going to bed.")
h2("Boho Ideas for Small or Rented Bedrooms")
h3("16. A Pouf or Floor Cushion")
p(f"A woven pouf or floor cushion gives you a seat without the bulk of a chair, and it tucks under a console when you need the floor. For more space-saving ideas, see our {a('small-bedroom-storage-ideas','small bedroom storage ideas')}.")
h3("17. Linen Curtains Hung High and Wide")
p(f"Hang sheer or linen curtains close to the ceiling and a little wider than the window to make the room feel taller and brighter. Use our {a('curtain-size-calculator','curtain size calculator')} to get the width and length right.")
h3("18. A Rattan Mirror")
p("A round or arched mirror with a rattan frame bounces light around a small room. If you lean a floor mirror against the wall, secure it to the wall with an anti-tip strap so it is much less likely to tip.")
h3("19. Baskets as Storage")
p("Woven baskets look boho and hide the clutter: one for extra blankets at the foot of the bed, one for books by the nightstand and a lidded one for anything you would rather not see.")
h2("The Finishing Touch")
h3("20. One Collected, Vintage Piece")
p("A thrifted wooden stool, an old trunk or a handmade ceramic lamp gives the room character that a set from one store cannot. Then stop: leave some wall and floor space empty so the room still feels calm.")
add(open('savebox.html').read())
h2("Boho Bedroom Safety Tips")
lst([f"<strong>Nothing heavy over the bed:</strong> {SR('ny','hang heavy items such as pictures and mirrors away from beds')}, and use studs or anchors rated for the weight for anything you do hang.",
f"<strong>Fabric and heat:</strong> keep canopies, throws and curtains {SR('heat','at least three feet away')} from portable heaters.",
f"<strong>Decorative lights:</strong> choose UL- or ETL-listed lights and {SR('lights','turn off all holiday lights when you go to bed or leave the house')}, as the CPSC advises.",
f"<strong>Plants and pets:</strong> check each plant on the ASPCA list; {SR('pothos','golden pothos')} is toxic to cats and dogs.",
"<strong>Candles:</strong> boho rooms are full of fabric, so use flameless LED candles instead of real ones."])
h2("Common Boho Bedroom Mistakes")
lst(["<strong>Too many patterns.</strong> Keep to one or two patterns and let texture do the rest.",
"<strong>A rug that is too small.</strong> A small rug floating at the foot of the bed makes the room look unfinished.",
"<strong>Clutter instead of collected.</strong> Boho is relaxed, not messy; give every piece space.",
"<strong>Heavy decor above the bed.</strong> Keep that wall light and soft.",
"<strong>Cold lighting.</strong> Bright, cool-white bulbs flatten warm wood and textiles."])
h2("Boho Bedroom FAQ")
h3("What is a boho bedroom?")
p("A boho bedroom is a relaxed, eclectic room built on natural materials like rattan, jute, linen and wood, layered textiles, plants and a warm, earthy palette, with a few handmade or vintage pieces that make it feel personal.")
h3("How do I make my bedroom boho on a budget?")
p("Start with textiles: a white or cream duvet cover, a throw and a few pillows in terracotta, rust or sage. Add a plant in a basket, a macrame hanging and warm lighting. Thrift stores are a great source of baskets, frames and vintage pieces.")
h3("What colors are used in a boho bedroom?")
p("Most boho bedrooms use a calm base of cream, warm white or beige, with earthy accents like terracotta, rust, mustard, sage and olive, plus the honey tones of rattan and wood.")
h3("What size rug do I need for a boho bedroom?")
p("For a queen bed, an 8 x 10 ft rug turned sideways usually works; for a king, a 9 x 12 ft rug. Aim for about 18 to 24 inches or more of rug showing on each side and at the foot of the bed.")
h3("Can a small bedroom be boho?")
p("Yes. Keep the base light, use a woven pendant or wall lights instead of bulky lamps, hang curtains high, add one tall plant and choose a few textured pieces rather than lots of small decor.")
h2("Final Thoughts")
p("The best boho bedroom ideas start with a calm base and build up with texture: linen bedding, a big natural rug, a few plants and warm light. Add pieces slowly, keep the wall above the bed light and the room will feel relaxed, personal and easy to live in.")
p(f"Have family coming to stay? Our {a('guest-bedroom-ideas','guest bedroom ideas')} cover the essentials guests need, and our {a('room-divider-ideas','room divider ideas')} show how to carve out a cozy corner in a shared space.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<svg.*?</svg>','',html))
print(len(html.encode()),'words',len(txt.split()),'kw',txt.lower().count('boho bedroom ideas'),txt.lower().count('boho bedroom'),txt.lower().count('boho'))
print(sorted(set(re.findall(r'dailyspacehacks\.com/([a-z0-9-]+)/',html))))
for w in ['colour','organise','favourite','cushion']:
    if w in txt.lower(): print('UK',w)
