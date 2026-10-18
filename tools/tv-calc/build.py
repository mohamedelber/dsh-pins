import re,json,math
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
CE="https://www.cepro.com/audio-video/how-high-should-a-tv-be-mounted/"
MM="https://www.mantelmount.com/blogs/news/the-science-behind-eye-level-tv-viewing"
CP="https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/AnchorItgov"
p("How high should you mount a TV? This free <strong>TV mounting height calculator</strong> gives you the answer in two taps: pick your TV size and where you sit, and it shows how high the center, bottom and top of the screen should be from the floor.")
p("It works in inches or centimeters, handles sofas, beds and standing spots, and warns you if a fireplace or piece of furniture forces the TV too high. Open <em>More options</em> to enter your own eye height and viewing distance, or the height for the wall bracket.")
add('<!-- wp:html -->\n'+open('tool.html').read()+'\n<!-- /wp:html -->')
h2("How High Should a TV Be Mounted?")
p(f"The simple rule is to put the center of the screen at the eye level of the person watching. Home technology trade site CE Pro {ext(CE,'recommends mounting a TV')} so the center is at eye level when you are seated, and gives about 42 inches (107 cm) from the floor to the center of the screen as a rule of thumb for a typical sofa. That is the starting point the calculator uses for the Sofa option.")
p(f"If the TV cannot sit at eye level, keep the angle small. CE Pro advises no more than 15 degrees of vertical angle to the viewer, and MantelMount's guide to {ext(MM,'eye-level TV viewing')} cites THX guidance to keep the vertical angle within 15 degrees of the center of the screen, treating it as a limit, not a target. The calculator checks this angle for you and turns red when it is exceeded.")
img(1)
h2("TV Height Chart for a Sofa")
p("This chart assumes a 16:9 TV with the center of the screen at 42 in (107 cm), a typical seated eye height on a sofa. Use it as a quick check, then use the calculator above for your own room.")
rows=[]
for d in [32,43,50,55,65,75,85]:
    h=d*9/math.sqrt(337); w=d*16/math.sqrt(337)
    rows.append([f'{d}"',f'{w:.0f} x {h:.0f} in ({w*2.54:.0f} x {h*2.54:.0f} cm)',f'{42-h/2:.0f} in ({(42-h/2)*2.54:.0f} cm)',f'{42+h/2:.0f} in ({(42+h/2)*2.54:.0f} cm)'])
table(["TV size","Screen (W x H)","Bottom edge","Top edge"],rows)
p("Bigger screens end up with the bottom edge lower, so check that a 75 or 85 inch TV still clears your media console. If it does not, raise it only as much as you need and check the angle in the calculator.")
h2("TV Height for a Bedroom")
img(2)
p(f"In bed you usually sit higher and lean back, so a bedroom TV often goes a little higher than in a living room. Eye heights in bed vary a lot with the bed and the pillows, so sit where you watch, measure from the floor to your eyes and enter it under More options. For the rest of the room, see our {a('small-bedroom-storage-ideas','small bedroom storage ideas')}.")
h2("Mounting a TV Above a Fireplace")
img(3)
p(f"A mantel usually forces the screen well above eye level, which is why CE Pro and MantelMount both point to pull-down or tilting mounts for this spot. Tick the fireplace box in the calculator, enter the lowest the bottom of the TV can go (the top of the mantel plus the clearance in your fireplace and TV manuals) and it shows the real viewing angle. If it is over 15 degrees, a pull-down mount, sitting further back or another wall will be more comfortable. Styling the mantel underneath? See our {a('christmas-mantel-decorating-ideas','Christmas mantel ideas')}.")
h2("How to Use the Calculator")
lst(["<strong>Pick your TV size.</strong> It is the diagonal, measured corner to corner, that the TV is sold by.",
"<strong>Pick where you sit.</strong> Sofa, low sofa, bed or standing fills in a typical eye height.",
"<strong>Read the answer.</strong> The center, bottom and top of the screen are measured from the floor.",
"<strong>Fine-tune if you like.</strong> Under More options, enter your own eye height, viewing distance, the mounting-hole height for the bracket and any fireplace limit.",
"<strong>Test before you drill.</strong> Tape a paper template the size of the screen to the wall and sit down to check it."],True)
h2("Mount It Safely")
p(f"A wall mount only works if it holds. Use a mount rated for your TV's weight and screen size, fix it into studs or with fixings meant for your wall type, and follow the TV and mount instructions. The U.S. Consumer Product Safety Commission's {ext(CP,'Anchor It campaign')} advises mounting flat-screen TVs to the wall or to furniture to stop them toppling over, and anchoring TVs that are not wall-mounted, especially in homes with young children.")
add(open('savebox.html').read())
h2("TV Mounting Height FAQ")
h3("How high should a TV be mounted from the floor?")
p("Mount the TV so the center of the screen is at the seated eye level of the main viewer, which is often around 42 inches (107 cm) from the floor for a standard sofa. A 55 inch TV centered there has its bottom edge about 29 inches up and its top edge about 55 inches up.")
h3("Where should the center of a TV be?")
p("The center of the screen should line up with your eyes when you sit where you usually watch. If that is not possible, keep the angle from your eyes up to the center of the screen under 15 degrees, which CE Pro and THX guidance treat as the limit for comfortable viewing.")
h3("Is a TV above a fireplace too high?")
p("Often, yes. A mantel usually pushes the center of the screen well above seated eye level, and the viewing angle can go past 15 degrees. Use the fireplace option in the calculator to check the real angle, and consider a pull-down mount, sitting further back or another wall.")
h3("How high should a TV be in a bedroom?")
p("A bedroom TV usually goes a little higher than a living room TV because you sit higher in bed. Sit up the way you normally watch, measure from the floor to your eyes and put the center of the screen at that height, or slightly above if you lean back on pillows.")
h2("More Planning Tools")
p(f"Planning the rest of the room? Try our {a('rug-size-calculator','rug size calculator')}, {a('curtain-size-calculator','curtain size calculator')} and {a('shelf-spacing-calculator','shelf spacing calculator')}, or get ideas for the console under the TV in our {a('coffee-table-decor','coffee table decor')} guide.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script.*?</script>|<style.*?</style>','',html))
print(len(html),'words',len(txt.split()),'kw',txt.lower().count('tv mounting height'),txt.lower().count('mount a tv'))
print(sorted(set(re.findall(r'dailyspacehacks\.com/([a-z0-9-]+)/',html))))
