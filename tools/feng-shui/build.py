import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={"brit":"https://www.britannica.com/art/fengshui",
"wiki":"https://en.wikipedia.org/wiki/Feng_shui",
"hgbag":"https://www.homesandgardens.com/life-design/feng-shui-energy-map",
"hgbed":"https://homesandgardens.com/interior-design/bedrooms/feng-shui-bed-placement",
"cho":"https://www.anjiecho.com/holistic-spaces-blog/feng-shui-for-your-bedroom",
"chopos":"https://www.anjiecho.com/holistic-spaces-blog/best-feng-shui-bed-position",
"chons":"https://anjiecho.com/holistic-spaces-blog/qa-sunday-feng-shui-do-you-really-need-two-nightstands?format=amp",
"livbed":"https://www.livingetc.com/advice/bed-feng-shui-layout",
"livdeath":"https://www.livingetc.com/advice/feng-shui-death-position",
"tg1":"https://www.tomsguide.com/news/feng-shui-and-sleep-expert-reveals-where-not-to-place-your-bed",
"tg2":"https://www.tomsguide.com/wellness/mattresses/if-your-bed-is-facing-any-of-these-things-experts-advise-moving-it-now-for-better-sleep",
"hav":"https://havenly.com/blog/feng-shui-bedroom",
"hgtv":"https://www.hgtv.com/decorating/bedrooms/feng-shui-your-bedroom-pictures",
"hgmir":"https://homesandgardens.com/interior-design/where-should-mirrors-be-placed-in-a-bedroom-for-feng-shui",
"livplant":"https://www.livingetc.com/advice/feng-shui-houseplant-decorating-mistakes",
"hgcol":"https://homesandgardens.com/interior-design/bedrooms/feng-shui-bedroom-colors",
"livcol":"https://livingetc.com/advice/feng-shui-bedroom-colors",
"hunkcol":"https://www.hunker.com/13769894/feng-shui-bedroom-colors-and-tips/",
"sfq":"https://www.sleepfoundation.org/mattress-sizes/queen-size-bed",
"hunk":"https://www.hunker.com/13412472/how-much-walking-space-should-be-around-bedroom-furniture",
"sft":"https://www.sleepfoundation.org/bedroom-environment/best-temperature-for-sleep",
"sfd":"https://www.sleepfoundation.org/bedroom-environment/making-your-room-dark",
"cdc":"https://www.cdc.gov/sleep/about/index.html"}
def SR(k,t): return ext(SRC[k],t)

p(f"A feng shui bedroom starts with the bed. Practitioners advise the commanding position, with the headboard against a solid wall and the door in view but not straight in line with your feet, then a clear floor and an empty space under the bed, mirrors that don't reflect you while you sleep, and soft, earthy colors. Feng shui is an {SR('brit','ancient Chinese practice of orienting significant sites, buildings')} and the objects in them; it is a tradition, and Wikipedia notes {SR('wiki','there is no empirical evidence that it is effective')}. So in the seven steps below, every rule is credited to the practitioner or publication that gives it, and we add the sleep-science and spacing numbers that make the same layout comfortable anyway.")
img(1)

h2("The Commanding Position, Measured")
diagram(open('z.svg').read(),"An example 12 x 12 ft bedroom with a queen bed in the commanding position, two layouts practitioners avoid, and how much floor a queen bed needs.")
p(f"Most feng shui bedroom advice is about where the bed goes, so it helps to check that your room can fit it. A queen mattress is {SR('sfq','60 x 80 inches')}, and the Sleep Foundation recommends {SR('sfq','at least 24 inches of space on the foot and either side')}. That means a queen needs about 108 x 104 inches (9 ft x 8 ft 8 in) of clear floor before you add nightstands or a dresser. In a smaller room, a full bed at 54 inches wide is the easier fit.")

h2("Step 1: Clear the Room, Including Under the Bed")
p(f"Most feng shui guides start with decluttering, and it is also the step that makes every other one easier. Los Angeles feng shui consultant Jayme Barrett told HGTV that {SR('hgtv','clutter under the bed has its own energy, which can disturb sleep')}, and Homes &amp; Gardens goes further, suggesting {SR('hgbed','nothing under the bed at all')} apart from a glass of water. HGTV's guide advises against even boxes of out-of-season clothes, so if a small room leaves you no choice, keep it to soft, closed boxes of bedding or clothes, not paperwork or things you are avoiding. Our {a('declutter-checklist','declutter checklist')} and {a('how-to-organize-your-room','how to organize your room')} guide make this step quicker.")

h2("Step 2: Put the Bed in the Commanding Position")
img(2)
p(f"Practitioners treat this as the main rule of a feng shui bedroom layout. Suzanne Roynon, a feng shui consultant, told Homes &amp; Gardens that you should {SR('hgbed','see the door from what we call \'the command position\'')}. Architect and feng shui consultant Anjie Cho puts it simply: you should {SR('cho','see the main entryway to the bedroom when you\'re sitting up')} in bed. Classical consultant Rosanna Deflorian adds the catch: place the bed where {SR('livbed','you can see the entrance without being directly in line with it')}, usually diagonally across from the door.")
p(f"Avoid having your feet point straight out of the door. Deflorian told Livingetc {SR('livbed','this is known as the death position')} in feng shui, linked to the custom of carrying the dead out feet first. If you can't move the bed, her fixes are a high footboard or a bench at the end of the bed, a folding screen, a heavy curtain, or simply closing the door at night.")

h2("Step 3: Back the Bed With a Wall and a Headboard")
p(f"Next, check what is behind your head. Cho recommends {SR('cho','a solid headboard that\'s securely attached to your bed')}, ideally upholstered or wood, and says to {SR('chopos','make sure you\'re supported by a solid wall')}. Sarah McAllister of The Feng Shui Agency told Tom's Guide: {SR('tg1','Try not to place a bed beneath a window')}. On Havenly, Cho also warns against the habit of people who {SR('hav','push their bed up against the wall or into a corner')}, so leave a way in on both sides.")
p(f"Tom's Guide also advises against sleeping under beams or a low, sloped ceiling. In an article written as a paid partnership with mattress brand Nectar Sleep, it suggests moving the bed out from under {SR('tg2','overhead beams')} and, under a sloping ceiling, placing the bed and headboard in the highest part of the room, which also gives you more headroom when you sit up.")

h2("Step 4: Leave Space on Both Sides, With Two Nightstands")
img(3)
p(f"A bed with space and a nightstand on each side looks balanced, and it is easier for two people to use. Cho says two nightstands {SR('chons','don\'t have to match, but ideally, they should be similar in size')}. Homes &amp; Gardens suggests open space {SR('hgbed','around 18 inches, on either side')} of the bed; the Sleep Foundation's 24 inches is more comfortable if you have room. Keep the path in clear too: Hunker says {SR('hunk','three feet of clearance is essential from the doorway')} to the nearest furniture. If you are single and hoping for a partner, Terah Kathryn Collins, founder of the Western School of Feng Shui, told HGTV to {SR('hgtv','decorate your bedroom as if a partner is already there')}, and HGTV suggests matching nightstands and lamps on both sides.")

h2("Step 5: Move or Cover Mirrors")
img(4)
p(f"Mirrors are one of the most common questions about a feng shui bedroom. Roynon's rule is that {SR('hgcol','a mirror never reflects the sleeper in bed')}, and holistic designer Anna Lippett says mirrors amplify energy, so {SR('hgmir','avoid positioning opposite the bed')}. A mirrored wardrobe door is the usual problem. If you can't move it, Collins suggests you {SR('hgtv','treat them like windows and hang curtains in front of them')}. There is one exception: if your bed can't face the door, Cho suggests placing a mirror so that {SR('cho','you can see the reflection of the door from your bed')}.")

h2("Step 6: Choose Soft, Earthy Colors")
p(f"Practitioners choose feng shui bedroom colors for calm. Roynon recommends {SR('hgcol','earthy and softer tones')}, and Cho told Livingetc to {SR('livcol','avoid bright green or bright blue')} in a bedroom, and also charcoal grey. Certified feng shui expert Laura Cerrano suggests you {SR('hunkcol','use the Five Elements Theory')} to choose a scheme. In Hunker's version, earth is beige, cream and soft brown; metal is white and metallics; water is blue and black; wood is green; and fire is red and orange, best kept to small accents. Pick one main element for the walls and bedding, then add a little of another in cushions or art.")

h2("Step 7: Keep Work and Screens Out, and the Room Dark and Cool")
p(f"Barrett told HGTV the bedroom is {SR('hgtv','a place where you need to turn off the stresses of the day')}, so move the desk out if you can and hide a TV in a cabinet with doors. Sleep health guidance agrees on the basics. The CDC recommends {SR('cdc','keeping your bedroom quiet, relaxing, and at a cool temperature')}, and the Sleep Foundation puts the best temperature at {SR('sft','approximately 65 degrees Fahrenheit')}. It also explains that {SR('sfd','in response to darkness, the pineal gland begins to produce melatonin')}, and suggests putting phones and tablets away at least 30 minutes before bed.")
p(f"For the finishing touches, HGTV suggests hanging calm, uplifting art opposite the bed, and Barrett would keep family photos elsewhere; our {a('picture-hanging-height-calculator','picture hanging height calculator')} shows how high to hang it. Practitioners disagree about plants: Cho says {SR('hav','plants can bring kindness and growth')}, while feng shui master Marie Diamond says they can {SR('livplant','disrupt restful Yin energy')} and suggests silk plants or botanical art instead. If you like plants, one or two near the window, not beside your head, is a sensible middle way.")

h2("If Your Bedroom Is Different")
lst([f"<strong>Small room or box room.</strong> If the bed has to go against a side wall, keep the headboard on the solid wall and add a lamp on the open side; Cho prefers space on both sides, so treat this as a compromise. Our {a('box-room-bedroom-ideas','box room bedroom ideas')} cover layouts for very small rooms.",
"<strong>The door is right beside the bed.</strong> Following Deflorian's advice, turn the bed so the door is diagonal from it, even if that means a smaller nightstand on one side.",
"<strong>The only solid wall faces the door.</strong> Put a bench or a high footboard at the end of the bed, or follow Deflorian's other fixes: a screen, a heavy curtain, or closing the door at night.",
f"<strong>A guest room.</strong> The same rules work for visitors; see our {a('guest-bedroom-ideas','guest bedroom ideas')} for the essentials."])

h2("Do This First")
lst(["Clear the floor and empty the space under the bed.",
"Move the bed so you can see the door without your feet pointing at it.",
"Check for a solid wall behind your head, not a window.",
"Turn or cover any mirror that shows you in bed.",
"Take out the desk, the laundry pile and the TV if you can."],ordered=True)
p(f"Those five changes cost little or nothing and give you the calm, balanced room that feng shui bedroom rules aim for. Once the layout works, our {a('boho-bedroom-ideas','boho bedroom ideas')} have soft, earthy styling ideas to finish it.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('feng shui bedroom'),'kw')
