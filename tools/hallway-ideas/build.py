import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={"adm":"https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/540330/BR_PDF_AD_M1_2015_with_2016_amendments_V3.pdf",
"cae":"https://cae.org.uk/our-services/housing-services/lifetime-homes/6-internal-doorways-and-hallways/",
"ox":"https://www.oxford.gov.uk/landlords-agents/private-housing-smoke-regulations",
"labc":"https://www.labc.co.uk/news/dos-and-donts-mains-powered-smoke-alarms-and-battery-alarms",
"dado":"https://www.idealhome.co.uk/all-rooms/hallway/hallway-dado-rail-trend",
"orac":"https://www.oracdecor.com/en/blog/post/how-to-design-timeless-wall-panelling",
"mb":"https://www.mybuilder.com/carpentry-joinery/price-guides/cost-to-install-wall-panelling",
"mjq":"https://www.myjobquote.co.uk/costs/installing-wall-panelling",
"wk":"https://www.wickes.co.uk/Cheshire-Mouldings-Shaker-Primed-Wall-Panel-Kit-1-2-x-1-2m/p/288212",
"dlx":"https://www.dulux.ie/en/change-starts-here/small-hallway-ideas",
"sfx":"https://www.screwfix.com/p/dulux-easycare-washable-tough-2-5ltr-pure-brilliant-white-matt-emulsion-paint/6823t",
"fb":"https://www.farrow-ball.com/paint/oval-room-blue/modern-emulsion",
"lg":"https://littlegreene.us/paint/finish/intelligent-eggshell",
"crown":"https://www.buildworld.co.uk/merchant/crown-clean-extreme-stain-resistant-scrubbable-matt-paint-various-colours-and-litres-available-bw-24930",
"ihp":"https://idealhome.co.uk/hallway/hallway-decor/hallway-paint-ideas",
"ihfb":"https://www.idealhome.co.uk/all-rooms/hallway/best-farrow-and-ball-paint-colours-for-a-hallway",
"hgza":"https://www.houseandgarden.co.za/interiors/try-these-practical-tips-when-painting-a-dark-hallway-f0dcba76-844e-4cd1-90c8-fbac512f4167",
"ihd":"https://www.idealhome.co.uk/hallway/hallway-decor/how-to-lighten-a-dark-hallway",
"tld":"https://www.tiffanylightingdirect.co.uk/pages/hallway-lighting-buying-guide",
"liv57":"https://www.livingetc.com/advice/picture-hanging-hack",
"fbox":"https://furniturebox.co.uk/blog/how-big-should-a-mirror-be",
"rs":"https://www.idealhome.co.uk/hallway/how-to-measure-for-a-stair-runner",
"ro":"https://www.rogeroates.com/measuring-guide/",
"rl":"https://ruglove.co.uk/blogs/rugs/how-to-measure-for-a-hallway-runner",
"st":"https://www.stelrad.com/news-events/blog/do-radiator-covers-block-heat-what-you-actually-need-to-know/",
"wfw":"https://www.woodfloorwarehouse.co.uk/advice-inspiration/faqs/the-best-flooring-for-hallways-in-uk-homes",
"tm":"https://www.tilemountain.co.uk/blog/pei-ratings-explained/",
"bc":"https://www.buildingconservation.com/articles/tiles/tiles.htm",
"sl":"https://sheerluxe.com/home/how-to-choose-a-colour-for-your-front-door",
"ihw":"https://idealhome.co.uk/hallway/hallway-ideas/hallway-wallpaper-ideas-210813",
"livs":"https://www.livingetc.com/ideas/small-hallway-ideas"}
def SR(k,t): return ext(SRC[k],t)

p(f"The best hallway ideas solve the same three problems: halls are narrow, often dark and take more knocks than any other room. If you only change one thing, make the walls tougher and lighter, or go boldly dark and own it, with a dado rail or panelling below to take the scuffs. Then fix the lighting, add a mirror and choose a floor that can cope with wet shoes. Below are 11 hallway decor ideas grouped by where they go, from the walls to the front door, with the heights, widths and UK prices that make each one work.")
img(1)

h2("A Hallway, Measured")
diagram(open('z.svg').read(),"Heights for a dado rail, wall lights and art, and what fits in an example 100 cm wide hall.")
p(f"Most of these ideas come down to a few numbers. Building Regulations guidance for accessible new homes says {SR('adm','the minimum clear width of every hall or landing is 900mm')}, and the Lifetime Homes standard allows a pinch point of 750 mm at {SR('cae','an obstruction such as a radiator')}. Older terraces can be tighter, so measure yours before buying furniture. In our 100 cm example, a 30 cm deep console would leave 70 cm, which is tight; a 20 to 25 cm shelf leaves more room to pass. Our {a('hallway-storage-ideas','hallway storage ideas')} cover slim shoe cabinets and peg rails for halls this narrow.")

h2("Walls and Colour")
h3("1. Light, Washable Paint")
p(f"In a narrow hall with little daylight, pale walls are the safe choice. Interior designer Sonnaz Nooranvary told Ideal Home that {SR('ihp','light colours help to create an illusion of space')}. The finish matters as much as the colour: Dulux notes that {SR('dlx','hallways are high-traffic areas')}, and recommends its Easycare Washable &amp; Tough range for hallway walls. At Screwfix, a 2.5 litre tin of the matt costs {SR('sfx','£24.99')}. For a more designer look, Farrow &amp; Ball's {SR('fb','Modern Emulsion')} is a wipeable matt with 7% sheen, and Crown Clean Extreme is rated {SR('crown','Class 1 for scrubbing')} (ISO 11998).")
p("<strong>Works best:</strong> small halls with one window or none. <strong>Skip it:</strong> if the hall faces north and white turns grey; a warm off-white or soft sand is kinder.")
h3("2. Two-Tone Walls Below a Dado Rail")
p(f"Splitting the wall with a dado rail puts the toughest colour where hands, bags and buggies hit it. Cathryn Sanders of Earthborn Paints suggests you {SR('ihp','consider painting the lower half of the wall in a dark shade')}, with a lighter colour above. Handyman Violeta Stoyanova of Fantastic Handyman told Ideal Home that a dado rail is {SR('dado','generally best placed at about one third of the wall height')}, which typically works out at around 85 to 100 cm from the floor, and closer to 85 cm in a hall with a low ceiling. Use an eggshell or satinwood below the rail: Little Greene says its Intelligent Eggshell {SR('lg','will give tremendous service')} in high-traffic areas.")
h3("3. A Dark Colour Drench")
img(3)
p(f"If your hall gets almost no daylight, you can stop fighting it. Interior designer Nicola Harding told House &amp; Garden she would {SR('hgza','always paint the space with the lowest light level in a dark colour')}. Patrick O'Donnell of Farrow &amp; Ball says {SR('ihfb','dark colours are a wonderful backdrop for pictures')}, so a deep green or navy hall is a good place for a gallery wall. Paint the skirting, doors and even the radiator the same colour; Anna Elkington of Melody Maison says {SR('ihd','painting your trim and wall the same colour')} helps a corridor look taller.")
p("<strong>Works best:</strong> halls with no window and good artificial light. <strong>Skip it:</strong> if you can't add wall lights, as a dark hall lit by one ceiling bulb feels gloomy.")
h3("4. A Painted or Papered Ceiling")
p(f"The ceiling is the one surface in a hall that nobody scuffs. Vicky Yardley of Victory Colours suggests you {SR('ihp','use a bold colour on the ceiling')} to draw the eye upwards, and Christina Nielsen told Livingetc that she likes {SR('livs','to wallpaper the ceiling')} as well as the walls. A small pattern on the ceiling and plain walls below is a good way to try pattern in a rented home's hall, as long as your landlord agrees.")

h2("Panelling, Wallpaper and Tiles")
h3("5. Picture-Frame Panelling")
img(2)
p(f"Picture-frame panelling makes a plain new-build hall look like a period home. Orac Decor advises you to {SR('orac','maintain a 3 - 7 cm gap around each panel')} so the boxes look balanced. If you do it yourself, Wickes sells a 1.2 x 1.2 m primed MDF shaker kit with {SR('wk','6 x 1.2m MDF strips')} for £10. MyBuilder puts fitted panelling at {SR('mb','£50-£100 per square metre')}, and MyJobQuote says panelling a full hall, stairs and landing typically costs {SR('mjq','£500 to £1,200')} and takes two to four days. Our {a('wainscoting-calculator','wainscoting calculator')} works out the box sizes for your wall, and the {a('board-and-batten-calculator','board and batten calculator')} does the same for a simpler batten look.")
p("<strong>Works best:</strong> halls with a dado rail or a long, plain wall. <strong>Skip it:</strong> on walls with lots of doors and switches, where boxes get cut up.")
h3("6. Wallpaper Above Panelling")
img(5)
p(f"Wallpaper adds pattern without taking up any floor space. Chelsea Clark of Lucie Annabel says {SR('ihw','a dado rail can serve as a stylish divide between wallpaper and paint')}: tongue-and-groove or painted panelling below, paper above. She also recommends washable wallpapers in halls because they are easy to keep clean. Fiona Howard, a wallpaper designer, says {SR('ihw','stripes are wonderful in a hallway')}. Our {a('wallpaper-calculator','wallpaper calculator')} tells you how many rolls you need for the area above the rail.")
h3("7. Restore Original Victorian Tiles")
p(f"If you lift an old carpet and find geometric tiles, keep them. Building Conservation says that {SR('bc','by the 1890s')} tiled hall floors had become an essential feature of terraced houses, and a fine hall floor could have around 4,000 tiles. The good news is that around {SR('bc','9 out of 10 are generally repairable')}. A specialist can clean, replace missing tiles and re-bed loose ones, so get a quote for repair before you pay for a new floor.")

h2("Light, Mirrors and Art")
h3("8. Layered Lighting")
p(f"One ceiling light makes a hall look like a corridor. UK retailer Tiffany Lighting Direct suggests hanging wall lights {SR('tld','around 170cm to 180cm')} from the floor, using warm white bulbs of 2700K to 3000K, and leaving at least 2.1 m of clearance under a pendant. In a long, narrow hall, Dominic Walsh of Off the Grain suggests you {SR('ihd','consider installing multiple spotlights')} down its length; our {a('recessed-lighting-calculator','recessed lighting calculator')} works out how many you need and how far apart. Keep new lights clear of the smoke alarm: LABC advises mounting alarms {SR('labc','300mm away from walls and light fittings')}. Any new wired light needs a qualified electrician.")
h3("9. A Statement Mirror")
p(f"A mirror is the quickest way to make a narrow hall feel wider. Vicki Foster of ScS says {SR('ihd','mirrors are the master of giving the illusion of space')}. Go bigger than you think: Furniturebox suggests a statement mirror {SR('fbox','should be at least half the size of the wall')} it hangs on, with some clear space around the frame. Hang it opposite or next to a window or a wall light so it bounces light along the hall, not at a blank wall. A round mirror over a slim shelf softens a hall full of straight lines.")
h3("10. A Gallery Wall Up the Stairs")
img(4)
p(f"Stairs give you a tall, empty wall that is perfect for framed prints. Interior designer Jason Wickens, quoted by Livingetc, recommends {SR('liv57','placing the center of the artwork 57 inches [145cm] from the floor')}. On a staircase, keep that 145 cm centre line above each step's nose so the frames rise with the stairs. Our {a('picture-hanging-height-calculator','picture hanging height calculator')} works out where to put the hook. Use matching frames in a dark hall to stop it looking busy.")

h2("Floors, Stairs and the Front Door")
h3("11. A Tough Floor, a Runner and a Front Door to Match")
p(f"Hall floors take wet shoes and grit every day. Wood Floor Warehouse says that if you want one answer, {SR('wfw','LVT is it')}: look for a wear layer of at least 0.55 mm. If you prefer laminate, AC4 is the rating for a busy hall, and engineered wood needs a lacquer finish rather than oil. For tiles, Tile Mountain says PEI 3 is {SR('tm','suited for all residential')} areas. Soften the floor with a runner that leaves {SR('rl','a 10-13 cm gap')} between its edges and the walls; our {a('rug-size-calculator','rug size calculator')} helps with the length.")
p(f"On the stairs, Daniel Prendergast of The Rug Seller told Ideal Home that {SR('rs','it\'s usual to leave about 10 centimetres')} of bare tread on either side of a runner, and Roger Oates sets {SR('ro','a minimum margin of 5cm')}. Finally, look at the front door from the inside and out. Katharine Paravicini of Sarah Delaney Designs uses Farrow &amp; Ball because {SR('sl','they do an exterior eggshell paint finish')}, and suggests asking whether your house is brick or rendered before choosing a colour.")

h2("Before You Start")
lst([f"<strong>Radiators.</strong> Painting a hall radiator the wall colour hides it for free. If you add a cover, Stelrad says a well-designed one might reduce heat output by {SR('st','around 5 to 10 %')}, while a poorly designed solid cover can cut it by 20 to 30% or more. Leave 30 to 50 mm of clearance at the sides and keep at least 40 to 50% of the front open.",
f"<strong>Smoke alarms.</strong> In England, landlords must fit {SR('ox','a working smoke alarm on each storey')} of a rented home. LABC also recommends an alarm {SR('labc','within 3m of the door to every bedroom')}, so a landing is a common spot. Don't paint or paper over an alarm.",
f"<strong>Clear width.</strong> Keep a clear path along the hall after adding furniture and rugs, especially near the front door. If the hall is under a metre wide, choose wall-hung shelves and hooks, or {a('under-stairs-storage-ideas','under stairs storage')}, instead of freestanding pieces.",
f"<strong>Small spaces.</strong> If your front door opens straight into a room, our {a('small-entryway-ideas','small entryway ideas')} and {a('boot-room-ideas','boot room ideas')} have layouts for very tight spaces."])

h2("If You Only Do One Thing")
p("Of all these hallway ideas, start with the walls. Choose a paint that you can wipe and pick a colour for how much light your hall actually gets: pale and warm if it has a window, dark and drenched if it doesn't. Add a dado rail or panelling to take the knocks, then a mirror and a second light source. Those three changes cost less than a new floor and make the biggest difference to how your hallway feels when you open the door.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('hallway ideas'),'kw')
