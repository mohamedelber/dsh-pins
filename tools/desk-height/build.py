import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
CU="https://ergo.human.cornell.edu/ergoguide.html"
CS="https://ergo.human.cornell.edu/CUESitStand.html"
CK="https://ergo.human.cornell.edu/cuchildcomp.html"
OP="https://www.osha.gov/etools/computer-workstations/positions"
OD="https://www.osha.gov/etools/computer-workstations/components/desks"
OM="https://www.osha.gov/etools/computer-workstations/components/monitors"
HSE="https://www.hse.gov.uk/msd/dse/good-posture.htm"
MY="https://www.mayoclinic.org/healthy-lifestyle/adult-health/in-depth/office-ergonomics/art-20046169"
EW="https://ergoweb.com/29-inch-desk-height-revisited/"
BC="https://www.bellevuecollege.edu/wp-content/uploads/sites/395/2020/06/Standing-Desk-Setup.pdf"
AU="https://www.autonomous.ai/en-GB/desk-height-calculator"
UC="https://uhs.berkeley.edu/sites/default/files/uc_task_chair_requirements_1.pdf"
IC="https://www.inchcalculator.com/desk-height-calculator/"
FX="https://flexispot.co.uk/blog/how-to-choose-the-ideal-desk-height-buying-guide"
p("What is the right desk height? Your desk, or at least your keyboard, should sit at your elbow height, so your elbows bend at about 90 degrees and your forearms are level. For most adults that means about 23 to 30 in (58 to 76 cm) for a sitting desk and about 36 to 47 in (91 to 119 cm) for a standing desk. This free <strong>desk height calculator</strong> works out your numbers in two taps.")
p("Pick your height and choose sitting or standing. You get the desk height, the chair seat height and where the top of your screen should be, with a simple side view. Open <em>More options</em> to type your exact height, switch to centimeters or enter your own elbow height for the most accurate result.")
add('<!-- wp:html -->\n'+open('tool.html').read()+'\n<!-- /wp:html -->')
h2("Desk Height Chart by Your Height")
table(["Your height","Sitting desk","Chair seat","Standing desk"],[
["5 ft 0 in (152 cm)","22.5 to 24.5 in (57 to 62 cm)","13.5 to 15.5 in","35.5 to 37.5 in (90 to 95 cm)"],
["5 ft 4 in (163 cm)","23.5 to 25.5 in (60 to 65 cm)","15.5 to 17.5 in","37.5 to 39.5 in (95 to 100 cm)"],
["5 ft 8 in (173 cm)","25.5 to 27.5 in (65 to 70 cm)","16.5 to 18.5 in","40.5 to 42.5 in (103 to 108 cm)"],
["6 ft 0 in (183 cm)","26.5 to 28.5 in (67 to 72 cm)","17.5 to 19.5 in","43 to 45 in (109 to 114 cm)"],
["6 ft 4 in (193 cm)","28.5 to 30.5 in (72 to 77 cm)","19.5 to 21.5 in","45.5 to 47.5 in (116 to 121 cm)"]])
p(f"The chart includes about 1 in for normal shoes. The sitting values follow the {ext(IC,'Inch Calculator desk height table')}, which aligns the desk with your elbows while seated, and the standing values follow the Autonomous height chart. No official body sets a desk height by person height, so treat these as starting points and fine-tune with your own elbow height.")
diagram(re.sub(r'(\d+\.\d{1,2})\d+',r'\1',open('z.svg').read()),"The right desk height: the desk or keyboard at elbow height with the elbows at about 90 degrees, feet flat and thighs level, and the top of the screen at eye level about an arm's length away. The table shows sitting and standing desk heights by person height.")
h2("How to Find Your Perfect Desk Height")
img(3)
lst(["<strong>Set the chair first.</strong> Raise or lower it until your feet rest flat on the floor and your thighs are about level.",
"<strong>Bend your elbows to about 90 degrees</strong> with your shoulders relaxed, and measure from the floor to the underside of your forearm. That is your elbow height.",
"<strong>Put the keyboard at or just below that height.</strong> If the desk is fixed and too high, raise the chair and add a footrest, or use a keyboard tray.",
"<strong>Set the screen</strong> so the top is at or slightly below eye level, about an arm's length away."],ordered=True)
p(f"The UK Health and Safety Executive recommends a {ext(HSE,'keyboard just below elbow height')}, and OSHA says {ext(OP,'elbows stay in close to the body and are bent between 90 and 120 degrees')}. For your legs, Mayo Clinic advises: {ext(MY,'adjust the height of the chair so that your feet rest flat on the floor')}.")
h2("What Is the Standard Desk Height?")
img(1)
p(f"Most desks are 28 to 30 in (71 to 76 cm) tall. Cornell University's ergonomics guide puts a typical desk {ext(CU,'between 28”-30” above the floor (suitable for most adults)')}, but Ergoweb points out that {ext(EW,'29 inches actually represents a one-size-fits-all, significant compromise')}. For shorter people a standard desk is often too high, which pushes the shoulders up. OSHA's fix: {ext(OD,'if the work surface cannot be lowered, raise the chair to accommodate the user')}, then add a footrest so your feet still rest flat.")
h2("Standing Desk Height")
img(2)
p(f"A standing desk follows the same rule: {ext(BC,'table height approximately at standing elbow height')}. Autonomous puts most adults {ext(AU,'between 38 and 46 inches (97 to 117 cm)')} when standing; shorter and taller people fall outside that range, so check your own elbow height. Set the height wearing the shoes you usually work in.")
p(f"Standing all day is not the goal either. Cornell's research suggests a simple rhythm: sit for 20 minutes, {ext(CS,'then every 20 minutes stand for 8 minutes AND MOVE for 2 minutes')}. On a sit-stand desk, save your sitting and standing heights as presets so switching takes one tap.")
h2("Chair Height")
p(f"A good office chair adjusts to your desk, not the other way round. The ANSI/HFES office standard, summarized by the University of California, says the {ext(UC,'seat height is adjustable at least 4.5 inches within the range of 15 - 22 inches from the floor')}. Once your feet are flat, HSE suggests a {ext(HSE,'gap of 2-3 cm between front of seat bottom and back of knee')}.")
h2("Monitor Height and Distance")
img(6)
p(f"OSHA says {ext(OM,'the top of the monitor should be at or slightly below eye level')}, and Mayo Clinic adds that {ext(MY,'the monitor should be no closer to you than 20 inches (about 50 centimeters)')}, about an arm's length away. If you wear bifocals, lower the screen another 1 to 2 in so you do not tilt your head back. Laptops sit too low for long sessions: put them on a stand and use a separate keyboard and mouse.")
h2("Desks for Small Spaces and Kids")
img(4)
p("In a small room, a wall-mounted or floating desk lets you choose the exact height, because you set the brackets yourself. Mount it at your seated elbow height minus the thickness of the keyboard, and keep at least 20 in of leg room underneath.")
img(5)
p(f"Children need the same posture, just smaller. Cornell notes that {ext(CK,'young children need a chair that raises them to the correct height for computer use')} and something stable for their feet. Height-adjustable kids' desks and chairs can grow with them; use the calculator with your child's height and check their elbows.")
h2("How the Desk Height Calculator Works")
lst(["<strong>Sitting desk:</strong> seated elbow height by person height, based on the Inch Calculator table, with about 1 in added for shoes.",
"<strong>Standing desk:</strong> standing elbow height by person height, based on the Autonomous chart.",
"<strong>Chair seat:</strong> the seat height that keeps your feet flat and thighs level.",
"<strong>Top of screen:</strong> your eye height, estimated from average body proportions. This is our own estimate.",
"<strong>Your elbow height:</strong> if you enter it, the calculator uses it instead of the estimate, which is the most accurate way."])
h2("Desk Height in cm (UK)")
p(f"In the UK and Europe, most desks are about 72 to 76 cm tall; FlexiSpot UK notes that {ext(FX,'a standard desk height falls within the range of 28 to 30 inches (71-76cm)')}. HSE's display screen guidance uses the same body-based rules as the US, so choose <em>Centimeters</em> in More options to get every result in cm.")
add(open('savebox.html').read())
h2("Desk Height FAQ")
h3("What is the standard desk height?")
p("Most desks are 28 to 30 in (71 to 76 cm) tall. That suits taller people best; shorter people usually need to raise their chair and add a footrest, or use a keyboard tray.")
h3("What desk height do I need if I am 5 ft 4 in?")
p("At about 5 ft 4 in (163 cm), a sitting desk or keyboard about 23.5 to 25.5 in (60 to 65 cm) high and a chair seat about 15.5 to 17.5 in high suit most people. A standing desk should be about 37.5 to 39.5 in (95 to 100 cm).")
h3("How high should a standing desk be?")
p("Set it at your standing elbow height, so your elbows bend at about 90 degrees with relaxed shoulders. For most adults that is about 38 to 46 in (97 to 117 cm), measured with your work shoes on.")
h3("Should my elbows be level with the desk?")
p("Yes. Your keyboard should be at or just below elbow height, with your forearms roughly level with the floor and your wrists straight.")
h2("More Free Home Tools")
p(f"Setting up a home office? See our {a('desk-organization-ideas','desk organization ideas')}, plan shelves above the desk with our {a('shelf-spacing-calculator','shelf spacing calculator')}, and use our {a('picture-hanging-height-calculator','picture hanging height calculator')} for the art on the wall.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script.*?</script>|<style.*?</style>|<svg.*?</svg>','',html))
print(len(html.encode()),'words',len(txt.split()),'kw',txt.lower().count('desk height calculator'),txt.lower().count('desk height'))
