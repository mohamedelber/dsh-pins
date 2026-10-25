import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={"toh":"https://www.thisoldhouse.com/bathrooms/small-bathroom-remodel-cost",
"tohl":"https://www.thisoldhouse.com/bathrooms/how-to-make-a-small-bathroom-look-larger",
"tohm":"https://www.thisoldhouse.com/bathrooms/5-ways-mosaic-tile-makes-a-small-bath-look-big",
"tohw":"https://www.thisoldhouse.com/walls/don-t-be-afraid-to-wallpaper-your-powder-room",
"bv":"https://bobvila.com/articles/15445-the-basics-of-bathroom-design",
"bvp":"https://www.bobvila.com/articles/installing-a-pocket-door.md",
"bvt":"https://www.bobvila.com/articles/tiny-bathroom-ideas.md",
"blk":"https://www.blockrenovation.com/guides/5x7-bathroom-floor-plans-layouts-fixture-guide",
"blkm":"https://www.blockrenovation.com/guides/design/minimum-bathroom-size-maximize-small-space",
"code":"https://buildingcodetrainer.com/minimum-shower-size/",
"houzz":"https://www.houzz.com/magazine/12-ways-to-make-any-bathroom-look-bigger-stsetivw-vs~84997339",
"houzzl":"https://www.houzz.com/magazine/how-to-choose-your-bathroom-vanity-lighting-stsetivw-vs~94643748",
"sch":"https://www.schluter.com/schluter-us/en_US/curbing-the-curb",
"at":"https://www.apartmenttherapy.com/things-making-bathroom-feel-smaller-36864237",
"hgtv":"https://www.hgtv.com/decorating/bathrooms/small-bathroom-design-pictures",
"crd":"https://www.crddesignbuild.com/blog/bathroom-wallpaper/",
"gold":"https://goldenlighting.com/blogs/the-golden-edit/bathroom-sconce-placement-2",
"tile":"https://www.tilebar.com/learn/large-format-wall-tiles-trends-designs-installations/",
"hvi":"https://www.hvi.org/resources/publications/bathroom-exhaust-fans/",
"hvi2":"https://hvi.org/resources/publications/bathroom-ventilation/",
"epa":"https://www.epa.gov/watersense/residential-toilets",
"epas":"https://www.epa.gov/sites/default/files/2017-01/documents/ws-products-factsheet-showerheads.pdf",
"esfi":"https://www.esfi.org/ground-fault-circuit-interrupters-what-if-gfcis-did-not-exist/",
"cvv":"https://www.jlconline.com//cost-vs-value/2025",
"ha":"https://www.homeadvisor.com/cost/bathrooms/small-bathrooms-and-half-baths",
"pro":"https://www.probuilder.com/products/kitchen-baths/article/55226747/pros-and-cons-wall-hung-toilets",
"vent":"https://buildingcodetrainer.com/bathroom-ventilation/",
"scald":"https://www.law.cornell.edu/regulations/south-carolina/R-8-1243"}
def SR(k,t): return ext(SRC[k],t)

p(f"The best small bathroom ideas work with the room's size instead of fighting it: keep the plumbing on one wall, swap a swinging door for a pocket door, use a floating vanity and clear glass so you can see more floor, and choose large tiles, light colors and good side lighting. This Old House says {SR('toh','a small bathroom typically measures 5-by-8 feet or 6-by-6 feet')}, so every inch counts. Below are 12 small bathroom ideas grouped by layout, shower and tub, walls and light, with the code minimums and costs to plan around.")
img(1)

h2("A 5 x 8 Bathroom, Measured")
diagram(open('z.svg').read(),"An example 5 x 8 ft bathroom with a tub, one plumbing wall and a pocket door, plus code minimums compared with NKBA recommendations.")
p(f"Two sets of numbers matter. Building codes set the minimum: the code allows {SR('bv','a minimum of 21 inches')} of clear space in front of a toilet or sink and a toilet centerline 15 inches from a side wall. The National Kitchen &amp; Bath Association (NKBA) recommends more for comfort: {SR('bv','a 30-inch clearance')} in front of each fixture and 18 inches to the toilet centerline. In a 5-foot-wide room, a {SR('blk','60 inches long by 30 to 32 inches wide')} alcove tub fits wall to wall, which is why so many small bathrooms are exactly that width.")

h2("Layout")
h3("1. Keep the Plumbing on One Wall")
p(f"Block Renovation's first layout for a 5 x 7 bathroom is {SR('blk','shower, toilet, and sink on one wall')}, and it is the cheapest to build because the drain and supply lines share one wall. It also leaves the opposite wall free for a door, towel bars or a tall cabinet. If your plumbing is already on one wall, keeping it there avoids the cost of moving drains.")
h3("2. A Pocket Door Instead of a Swinging Door")
img(5)
p(f"A swinging door needs clear floor on one side. Bob Vila says a pocket door {SR('bvp','recovers at least 10 square feet of floor space around the door')}, but a 32-inch door needs {SR('bvp','at least 66 inches of linear wall space')}, and you can't use one where pipes or wires run through the wall. Buy good hardware: This Old House's Tom Silva warns that on cheap pocket doors, {SR('tohl','often, a screw falls out or the door comes off the track')}.")
h3("3. A Shallower or Floating Vanity")
p(f"Block Renovation notes that {SR('blk','a standard vanity is 21 to 22 inches deep')}, while a shallow vanity of 16 to 18 inches can win back a few inches of clear floor. Mounting it on the wall helps too: Houzz points out that {SR('houzz','the peek of flooring underneath makes the area feel a notch more open')}. In a very small half bath, a wall-mounted or corner sink is enough; Bob Vila shows how {SR('bvt','a corner sink opens up this tiny bathroom')}. Our {a('small-bathroom-storage-ideas','small bathroom storage ideas')} cover where everything goes once the vanity shrinks.")
img(3)
h3("4. A Wall-Hung Toilet")
p(f"A wall-hung toilet hides the tank inside the wall. Pro Builder notes it gives {SR('pro','easy access to the floor under the bowl for cleaning')}, and Peter Christofferson of Chicago Faucet says {SR('pro','this setup allows the height to be completely customized')}. It needs a thicker wall or a frame to carry the tank and bowl, so it is easiest to add in a full remodel.")

h2("Shower and Tub")
h3("5. A Curbless Shower With One Floor Tile")
img(2)
p(f"Taking away the curb lets one floor tile run from the door into the shower. Schluter says curbless showers {SR('sch','create a seamless look in the bathroom, making it look and feel bigger')}, and that linear drains let the shower floor pitch in one direction, so you can use large tiles. They also offer {SR('sch','improved accessibility to everyone from the very young to the very old')}. The code minimum is a shower of {SR('code','not less than 900 square inches')} and at least 30 inches in each direction; the NKBA recommends 36 x 36 inches if you have room.")
h3("6. Clear Glass, Not a Curtain")
p(f"A shower curtain blocks half the room from view. Houzz says that with clear glass, {SR('houzz','the entire square footage of the room will be visible at once')}. A single fixed panel is simplest: a swinging glass door needs floor to open into. Over a tub, a half panel works; This Old House's Lynn Kirincich says {SR('tohl','stopping the shower wall short and topping it with glass')} keeps an open feel. If you keep a curtain, HGTV suggests {SR('hgtv','installing an extra-tall curtain close to the ceiling')} so the room looks taller.")
h3("7. A Niche Instead of a Caddy")
p(f"A recessed niche keeps bottles off the shower floor and out of sight. HGTV recommends using the {SR('hgtv','same tiles or finishes for the niche that are featured on the surrounding walls')} so it blends in. Plan it before the walls are tiled, on an interior wall, and keep it out of an exterior wall where insulation needs the space. The IRC also asks for clear floor in front of the shower opening of {SR('code','no less than 24 inches')}.")

h2("Walls, Color and Light")
h3("8. Large Tiles, Few Grout Lines")
p(f"TileBar defines large-format tile as {SR('tile','tile with at least one edge measuring 12 inches or more')}, and says fewer grout lines make small bathrooms feel more open. This Old House agrees: {SR('tohl','use large-format tiles to minimize grout lines')}. Stacking narrow tiles vertically has the opposite trick; This Old House notes a vertical pattern {SR('tohm','draws the eye upward, making the ceiling appear higher')}.")
h3("9. Light Colors, or One Bold Move")
p(f"Debbie Zimmer of the Paint Quality Institute told This Old House that {SR('tohl','lighter hues can open up a small space')}. But small rooms can also take color: designer Janelle Hughes told Apartment Therapy that {SR('at','in smaller spaces, you really have to use color as your friend')}. HGTV's Melissa Miranda says {SR('hgtv','powder rooms are usually where I really go all out')}, because you need so little material that you can afford a better one.")
h3("10. Wallpaper in a Powder Room")
img(4)
p(f"Gina Shaw of York Wallcoverings told This Old House that wallpaper is {SR('tohw','the single most dramatic statement you can make in a small space')}. It works best where there is no shower: CRD Design Build says half baths {SR('crd','are ideal candidates for wallpaper')}, and in a full bath you should {SR('crd','use vinyl-coated, moisture-resistant wallpaper')}. Our {a('powder-room-decor-ideas','powder room decor ideas')} have more.")
h3("11. A Bigger Mirror and Side Lighting")
p(f"Hughes suggests {SR('at','a really large round mirror above your vanity')} to bounce light around. Light the face from the sides, not only from above: the American Lighting Association, via Houzz, recommends {SR('houzzl','mounting them 65 to 70 inches from the floor')} and 28 to 30 inches apart. Rick Kovac of Golden Lighting suggests {SR('gold','a warm 2700K to 3000K color temperature')}. Lighting designer Francesca Bettridge's rule, in This Old House: {SR('tohl','never shine a light on the mirror')}.")
h3("12. A Quiet Fan That Actually Clears Steam")
p(f"Small bathrooms steam up fast. HVI says fan size {SR('hvi','works out to one CFM per square foot of bathroom area')}, with 50 CFM as the minimum for a bathroom of up to 50 square feet, and a fan rated at {SR('hvi','1.0 sones or less')} for quiet running. HVI also suggests the {SR('hvi2','fan be left on for 20 minutes after use')}. The IRC says {SR('vent','air from an exhaust fan must discharge directly to the outside')}, not into the attic.")

h2("Before You Remodel")
lst([f"<strong>Budget.</strong> HomeAdvisor says {SR('ha','remodeling a small bathroom costs an average of $6,500')}, with most projects between $1,500 and $15,000. The 2025 Cost vs. Value report puts a midrange bathroom remodel at {SR('cvv','$26,138')}, with 80% of the cost recouped at resale.",
f"<strong>Water.</strong> The EPA's WaterSense label means {SR('epa','toilets to use 1.28 gallons per flush or less')}, which saves a household nearly 13,000 gallons a year, and WaterSense showerheads use {SR('epas','no more than 2.0 gpm')}.",
f"<strong>Safety.</strong> Bathroom outlets must be GFCI protected; ESFi credits GFCIs with an {SR('esfi','81% drop in electrocutions')} since they were first required in bathrooms in 1975. New shower valves must limit hot water to {SR('scald','120°F')} under the IRC to prevent scalds.",
f"<strong>Related ideas.</strong> Our {a('bathroom-wall-decor-ideas','bathroom wall decor ideas')}, {a('medicine-cabinet-organization','medicine cabinet organization')} tips and, for Australian readers, {a('small-ensuite-ideas','small ensuite ideas')} take these further."])

h2("If You Only Do One Thing")
p("Of all these small bathroom ideas, the one that changes a room most for the least money is light: a larger mirror with a sconce on each side, warm bulbs and a fan that clears the steam. If you are remodeling, add a floating vanity and clear glass, and keep the plumbing where it is.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('small bathroom ideas'),'kw')
