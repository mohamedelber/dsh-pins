import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
HDB="https://www.homedepot.com/c/ab/recessed-lighting-buying-guide/9ba683603be9fa5395fab904f2192b8"
HDL="https://www.homedepot.com/c/ah/recessed-lighting-layout/9ba683603be9fa5395fab90c18f7401"
KIC="https://www.kichler.com/tips-guides/indoor-lighting-guide/downlight-recessed-placement-tips"
WAC="https://waclighting.com/blog/kitchen-lighting-guide/"
RLP="https://blog.recessedlighting.com/recessed-lighting-placement/"
RLN="https://blog.recessedlighting.com/how-many-recessed-lights/"
PH="https://www.philips-hue.com/en-us/explore-hue/faq/lamps/how-far-should-recessed-lights-be-from-the-wall"
LE="https://www.livingetc.com/advice/how-do-you-layout-recessed-lighting-top-designers-answer-your-questions"
LRC="https://www.lrc.rpi.edu/programs/lightingTransformation/residentialLighting/buildersguide/luminairesRecessed.asp"
PSU="https://courses.ems.psu.edu/egee102/node/2363"
DB="https://duttonbrown.com/blogs/news/how-much-light-do-you-need-for-your-space"
HUN="https://www.hunker.com/13412735/how-to-calculate-lumens-per-square-foot"
FEIT="https://www.feit.com/inspire/how-to-choose-the-right-color-light-temperature-for-your-bulb-or-fixture/"
TOH="https://www.thisoldhouse.com/lighting/how-to-insulate-around-recessed-led-fixtures"
HALO4="https://cooperlighting.com/global/brands/halo/1060027/hlb4sp-4-slim-canless-direct-mount/hlb4sp069fs1emwr"
HALO6="https://cooperlighting.com/global/brands/halo/1017823/hlb6s-6-slim-canless-direct-mount/hlb6s099401emwr"
UKSL="https://www.simplelighting.co.uk/blog/downlight-spacing-guide"
UKDL="https://www.downlights.co.uk/faq-how-many-downlights-do-i-need-for-my-kitchen-.html"
UKIP="https://www.lumination.co.uk/blogs/news/ip-ratings-for-bathroom-lights"
p("How many recessed lights do you need? Space them about half the ceiling height apart, so 4 ft apart on an 8 ft ceiling, and put the first light about half that distance from the walls, about 2 ft. A 12 x 14 ft room with an 8 ft ceiling takes about 9 recessed lights in 3 rows of 3. This free <strong>recessed lighting calculator</strong> works out the number, the spacing and how bright each light should be in two taps.")
p("Pick the room and its size. You get how many lights to install, how far apart, how far from the walls and the light size and lumens, with a ceiling plan you can copy. Open <em>More options</em> to type your exact room size, change the ceiling height, choose 4 in or 6 in lights or switch to meters.")
add('<!-- wp:html -->\n'+open('tool.html').read()+'\n<!-- /wp:html -->')
h2("Recessed Lighting Spacing Chart")
table(["Ceiling height","Space lights apart","First light from the wall"],[
["8 ft (2.4 m)","4 ft (1.2 m)","2 ft (0.6 m)"],
["9 ft (2.7 m)","4 ft 6 in (1.4 m)","2 ft 3 in (0.7 m)"],
["10 ft (3.0 m)","5 ft (1.5 m)","2 ft 6 in (0.8 m)"],
["12 ft (3.7 m)","6 ft (1.8 m)","3 ft (0.9 m)"]])
diagram(re.sub(r'(\d+\.\d{1,2})\d+',r'\1',open('z.svg').read()),"Recessed lighting spacing: lights about half the ceiling height apart (4 ft on an 8 ft ceiling) and the first light about half that from the wall (2 ft), so the cones of light meet evenly. The table shows the spacing for 8 to 12 ft ceilings and the lumens per square foot each room needs.")
h2("How Many Recessed Lights for Your Room Size")
table(["Room size","8 ft ceiling","9 ft ceiling","10 ft ceiling"],[
["10 x 10 ft","4 (2 rows of 2)","4 (2 rows of 2)","4 (2 rows of 2)"],
["12 x 10 ft","6 (2 rows of 3)","6 (2 rows of 3)","4 (2 rows of 2)"],
["12 x 12 ft","9 (3 rows of 3)","9 (3 rows of 3)","4 (2 rows of 2)"],
["14 x 12 ft","9 (3 rows of 3)","9 (3 rows of 3)","6 (2 rows of 3)"],
["16 x 14 ft","12 (3 rows of 4)","12 (3 rows of 4)","9 (3 rows of 3)"],
["20 x 16 ft","20 (4 rows of 5)","16 (4 rows of 4)","12 (3 rows of 4)"],
["12 x 4 ft hallway","3 (one row)","3 (one row)","2 (one row)"]])
p("The chart uses the half-the-ceiling-height rule and rounds to whole rows, so the real spacing can be up to about a foot wider or closer (a 12 x 12 ft room with a 10 ft ceiling gets lights 6 ft apart, not 5 ft). Brightness is the second half of the job: the calculator checks the lumens your room needs and suggests the light size to match.")
img(1)
h2("How Far Apart Should Recessed Lights Be?")
p(f"The most common rule is simple: Home Depot says to {ext(HDB,'divide the height of the ceiling by two to get the distance the lights should be from one another')}. So an 8 ft ceiling gets lights about 4 ft apart and a 10 ft ceiling about 5 ft apart. Kichler adds a limit: {ext(KIC,'but don’t go more than 6 feet apart, or you’ll lose the impact')}.")
p(f"For the walls, RecessedLighting.com says {ext(RLP,'the distance between your lights is always twice (2x) the distance from the wall to the first light')}. That puts the first light about 2 ft from the wall on an 8 ft ceiling. Fixed figures vary: Philips Hue's layout table gives {ext(PH,'1.5–2 ft (50–60 cm)')} from the wall for an 8 ft ceiling, while Home Depot suggests about 3 ft from the wall {ext(HDB,'to avoid creating shadows that make your ceilings look lower')}. Anything from about 1.5 to 3 ft works; the half-spacing rule keeps the light even.")
lst(["<strong>Measure the room</strong> and note the ceiling height.",
"<strong>Find the spacing:</strong> ceiling height divided by 2.",
"<strong>Count the lights per row:</strong> room length divided by the spacing, rounded to a whole number. Do the same for the width to get the number of rows.",
"<strong>Mark the first light</strong> half a spacing from each wall, then the rest at the full spacing.",
"<strong>Adjust around joists, vents and furniture</strong> by a few inches, keeping the rows straight."],ordered=True)
h2("How Many Recessed Lights Do I Need?")
p(f"The spacing rule gives the number of lights; brightness tells you how strong each one should be. Lighting retailer Dutton Brown says to {ext(DB,'multiply the square footage of your room by the number of foot-candles required for the space')}. A foot-candle is about one lumen per square foot, so a 168 sq ft living room at 15 lumens per sq ft needs about 2,520 lumens in total.")
table(["Room","Lumens per sq ft","Example: 12 x 14 ft room"],[
["Hallway","5 to 10","about 1,260 lumens"],
["Living room, bedroom","10 to 20","about 2,520 lumens"],
["Kitchen (general), dining room","30 to 40","about 5,880 lumens"],
["Home office","20 to 50","about 6,720 lumens"],
["Bathroom","20 to 50 (some guides say 70 to 80)","about 8,400 lumens"]])
p(f"The living, bedroom, kitchen, dining, office and bathroom ranges come from a Penn State course page based on guidance from {ext(PSU,'the Illuminating Engineering Society (IES)')}; the 5 to 10 hallway range is from Dutton Brown (Penn State gives 5 to 20). Sources disagree on bathrooms: IES-based tables give 20 to 50, while Hunker's rule of thumb is {ext(HUN,'70–80 lumens per square foot')}. The calculator uses 50 as a middle value and lets you pick <em>Brighter</em>. Real rooms lose some light to walls and trims, so a little extra and a dimmer is the safe choice. As RecessedLighting.com puts it, {ext(RLN,'Most often you’ll be better off installing brighter lights rather than more lights.')}")
h2("4 Inch vs 6 Inch Recessed Lights")
p(f"Home Depot notes that {ext(HDB,'6-inch fixtures are most common for general lighting purposes')}, while {ext(HDL,'3-inch/4-inch: The smallest sizes of housing, they are used mainly for small areas')}. Typical LED models give about 600 lumens for a 4 in light (Halo HLB4: {ext(HALO4,'600 lm (nominal)')}) and about 900 lumens for a 6 in light (Halo HLB6: {ext(HALO6,'900 lm (nominal)')}). Many brands also sell brighter versions.")
lst(["<strong>4 in lights:</strong> small rooms, bathrooms, hallways, kitchen task rows and accent lighting.",
"<strong>6 in lights:</strong> general light in living rooms, kitchens and large spaces.",
f"<strong>High ceilings:</strong> Kichler advises {ext(KIC,'For ceilings higher than 10ft, use 1000 lumens in your downlights to make sure light reaches the floor.')}"])
h2("Recessed Lighting in the Kitchen")
img(2)
p(f"In a kitchen, the row over the counters matters most. Libby Rawers of Sharp + Grey Interiors told Livingetc: {ext(LE,'Make sure recessed lighting is placed 12- 18 inches from a cabinet so that there aren’t any dark spots')}. Home Depot suggests {ext(HDL,'about 14 to 18 inches of space between the light cannisters and the cabinets')}. Light the rest of the kitchen with the normal grid, and add a row over the island or pendants above it.")
h2("Bedrooms, Bathrooms and Hallways")
img(3)
p("Bedrooms need soft light, so fewer or dimmer lights work, and lamps do the reading. Keep lights away from the spot right above your head when you lie in bed, and put them on a dimmer.")
img(4)
p(f"Bathrooms need more light. Over a shower or tub, use a light made for wet locations; Home Depot describes shower trim as {ext(HDB,'specifically designed for installation above the bathtub and in shower stalls')}. In the UK, bathroom zones set the rating: Lumination lists {ext(UKIP,'IP65 minimum')} directly above the bath or shower.")
img(5)
p("In a hallway, one centered row is usually enough. Use the same spacing rule along its length, and add a light at each doorway or turn.")
h2("Wall Washing and Accent Lights")
img(6)
p(f"To light a wall evenly, the rule flips. The Lighting Research Center says wall-wash lights {ext(LRC,'should be spaced as far from each other as they are from the wall')}, and warns that lights {ext(LRC,'mounted closer to the wall than 1 foot 6 inches produce harsh, scalloped patterns of light on the wall')}. For art, use adjustable gimbal lights and aim them about 30 degrees from straight down, the angle RecessedLighting.com calls {ext(RLP,'The optimal aiming angle to minimize glare')}.")
h2("Best Color Temperature for Recessed Lights")
p(f"WAC Lighting says: {ext(WAC,'For ambient lighting, consider a CCT between 2700K and 3000K.')} Feit Electric recommends {ext(FEIT,'2700K (Soft White) is the best color temperature for bedrooms')} and {ext(FEIT,'3000K to 4000K is the ideal range for kitchens')}. Keep the same color temperature in one room, and in open spaces that share a ceiling, so the light does not look patchy.")
h2("IC-Rated vs Non-IC Recessed Lights")
p(f"If there is insulation above the ceiling, you need IC-rated lights. The Lighting Research Center explains that {ext(LRC,'IC-rated luminaires are designed so insulation can cover and abut the luminaire')}. This Old House notes that {ext(TOH,'Non-IC-rated fixtures require a minimum of three inches of clearance from insulation')}. Many new canless LED lights are IC-rated; check the box. If you are not sure about the wiring, hire a licensed electrician.")
h2("How the Recessed Lighting Calculator Works")
lst(["<strong>Spacing:</strong> ceiling height divided by 2, capped at 6 ft.",
"<strong>Layout:</strong> the room length and width divided by the spacing, rounded to whole rows, with the first light half a spacing from each wall.",
"<strong>Brightness:</strong> room area times lumens per sq ft for the room type (hallway 7.5, living room and bedroom 15, kitchen and dining room 35, home office 40, bathroom 50), divided by the number of lights.",
"<strong>Light size:</strong> 4 in at about 650 lumens or 6 in at about 900 lumens, or a high-output 6 in light when the room needs more. Over 10 ft, it suggests at least 1,000 lumens.",
"<strong>Estimates:</strong> these are planning guidelines. Your joists, vents and furniture may move a light a few inches."])
h2("Downlight Spacing in the UK")
p(f"UK guides use the same rule in metres. Simple Lighting says: {ext(UKSL,'If your ceiling is 2.4 metres high, aim for downlights about 1.2 metres apart.')} and to {ext(UKSL,'place them about 60cm from the walls')}. For brightness, Downlights.co.uk says {ext(UKDL,'Kitchens require a minimum of 300 average lux')} and {ext(UKDL,'Living rooms and bathrooms require 150 average lux')}. Choose <em>Meters</em> in More options to get every result in metres.")
add(open('savebox.html').read())
h2("Recessed Lighting FAQ")
h3("How far apart should recessed lights be on an 8 ft ceiling?")
p("About 4 ft apart, with the first light about 2 ft from the walls. On a 9 ft ceiling, space them about 4 ft 6 in apart; on a 10 ft ceiling, about 5 ft.")
h3("How many recessed lights do I need for a 12 x 12 room?")
p("With an 8 or 9 ft ceiling, about 9 lights in 3 rows of 3, about 4 ft apart and 2 ft from the walls. With a 10 ft ceiling, 4 lights in 2 rows of 2, about 6 ft apart and 3 ft from the walls; a kitchen needs high-output lights.")
h3("How far should recessed lights be from the wall?")
p("About half the spacing between the lights, which is usually 2 to 3 ft. For wall washing, place them about 1.5 to 3 ft from the wall (never closer than 1.5 ft) and space them as far apart as they are from the wall.")
h3("Should I use 4 inch or 6 inch recessed lights?")
p("Use 6 in lights for general light in most rooms and 4 in lights for small rooms, bathrooms, hallways and task or accent lighting. What matters most is the lumens: about 600 to 650 for a typical 4 in light and about 900 for a 6 in light.")
h2("More Free Home Tools")
p(f"Lighting over a table or island? Our {a('chandelier-size-calculator','chandelier size calculator')} sizes the fixture and the hanging height. Planning a kitchen, try our {a('kitchen-island-size-calculator','kitchen island size calculator')}, and use our {a('picture-hanging-height-calculator','picture hanging height calculator')} for the art you want to light.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script.*?</script>|<style.*?</style>|<svg.*?</svg>','',html))
print(len(html.encode()),'words',len(txt.split()),'kw',txt.lower().count('recessed lighting calculator'),txt.lower().count('recessed light'))
