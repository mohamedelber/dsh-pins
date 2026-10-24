import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
LOC="https://www.nedcc.org/assets/media/documents/Pres101/6_media_loc_c-cylinder_disc.pdf"
SRC={"loc":LOC,
"nara":"https://www.archives.gov/preservation/formats/audio-storage.html",
"gay":"https://info.gaylord.com/resources/best-practices-for-vinyl-records",
"naa":"https://www.naa.gov.au/information-management/storing-and-preserving-information/preserving-information/preserving-gramophone-discs",
"cci":"https://www.canada.ca/en/conservation-institute/services/preventive-conservation/guidelines-collections/caring-audio-video-data-recording-media.html",
"psap":"https://psap.library.illinois.edu/collection-id-guide/phonodisc",
"aic":"https://www.culturalheritage.org/discussion/record-albums",
"at":"https://www.audio-technica.com/en-us/support/audio-solutions-question-of-the-week-how-do-i-use-audio-technica-record-cleaning-products",
"dm":"https://support.discmakers.com/hc/en-us/articles/209637637-Vinyl-record-weights",
"kallax":"https://www.ikea.com/us/en/p/kallax-shelf-unit-black-brown-40311873/",
"eket":"https://www.ikea.com/us/en/p/eket-cabinet-white-70332124/"}
def SR(k,t): return ext(SRC[k],t)

p(f"To store vinyl records, stand them upright in their sleeves, never stacked flat, with enough support that they don't lean. Keep them somewhere steady, cool and dark: the Library of Congress recommends {SR('loc','65 to 70° F and 45 to 50% relative humidity')} for medium-term storage. Swap old paper inner sleeves for polyethylene ones and keep records out of the attic, the garage and the sun.")
p("That's the short version. The seven steps below cover what to do before a record goes on the shelf, how to choose furniture that can take the weight, and where in the house to put it.")
img(1)

h2("Step 1: Clean Each Record Before You Store It")
p(f"Dust that goes onto the shelf in the grooves stays there. Gaylord Archival, which makes conservation supplies, says {SR('gay','to clean a record both before and after playback')}. A dry carbon fiber brush is enough for most LPs; Audio-Technica says its anti-static brush is {SR('at','designed for dry cleaning records')} and shouldn't be used with liquid. Don't overdo it: the Canadian Conservation Institute warns that frequent or improper cleaning {SR('cci','may cause more problems')}. Hold records by the edge and the label only, as the Library of Congress advises; Gaylord notes that oils from your hands transfer into the grooves and attract dust.")

h2("Step 2: Replace Paper Inner Sleeves")
img(3)
p(f"Plain paper sleeves scuff the surface and shed fibers. The Library of Congress says most sleeves should be replaced with {SR('loc','a high density polyethylene')} sleeve, and the Canadian Conservation Institute recommends soft polyethylene sleeves inside the original jacket, while avoiding {SR('cci','PVC and acidic cardboard sleeves')}. If a sleeve feels sticky or tacky, swap it. Want to keep a printed original inner sleeve? Thin poly sleeves can go inside it, so you keep the artwork and still protect the disc.")

h2("Step 3: Take Off the Shrink Wrap")
p(f"Many collectors leave new records in their shrink wrap, but it is better to remove it. Gaylord says {SR('gay','the wrap can continue to shrink')}, which can damage the record, and a conservator on the American Institute for Conservation forum notes that {SR('aic','tight plastic wrapping may cause warping')}. If you want to protect the jacket, slide it into a loose clear outer sleeve instead.")

h2("Step 4: Stand Records Upright, Never Flat")
img(2)
p(f"This is the rule every archive agrees on. The Library of Congress says to keep discs {SR('loc','standing upright, on edge')} and not to lay any recording flat, and the National Archives says {SR('nara','do not stack discs on top of one another')}. Gaylord explains why: {SR('gay','to minimize warping')}, records should be stored vertically. Records that lean are almost as bad. The National Archives of Australia says boxes or dividers should give support {SR('naa','so that the discs do not lean over')}. Fill a part-empty shelf or crate with a bookend or a block so the last few stay straight.")

h2("Step 5: Add Dividers and Sort by Size")
p(f"For long runs of records, the Library of Congress recommends full-height and full-depth dividers {SR('loc','spaced 4 to 6 inches apart')}, and warns that shorter dividers may contribute to warping. It also says mixing discs of different diameters on one shelf can warp them, so keep 7-inch singles, 10-inch records and 12-inch LPs in separate sections. Gaylord agrees: {SR('gay','store records of the same size together')}. Pack them snugly but not crammed, so you can pull one out without forcing it.")

h2("Step 6: Use Furniture That Can Take the Weight")
diagram(open('z.svg').read(),"Records should stand upright with full-height dividers; a full 13-inch cube of LPs can weigh around 38 to 49 pounds by our estimate.")
p(f"Records are heavy. The Library of Congress says {SR('loc','LPs average between 35 and 45 pounds per shelf-foot')}, and that the weight concentrates along the middle of a shelf, which is where shelves sag. A standard LP weighs about {SR('dm','140 grams')} according to pressing plant Disc Makers, and 180-gram pressings are heavier still. That matters with cube shelving. IKEA lists a KALLAX shelf at {SR('kallax','Max load/shelf 29 lb')}, while a full 13-inch cube of LPs would weigh roughly 38 to 49 pounds by our estimate. Many collectors use KALLAX anyway, but check the rated load, don't cram every cube with heavy pressings, and anchor tall units to the wall.")
p(f"Check the depth too. A 12-inch LP jacket is a little over 12 inches square, so shelves need at least 13 inches of clear depth. IKEA's small EKET cabinet, for example, is only {SR('eket','9 7/8\"')} deep, so LPs would stick out. Our {a('shelf-spacing-calculator','shelf spacing calculator')} helps you set heights, and if you are building your own, our {a('diy-floating-shelves','DIY floating shelves')} guide covers fixings; for records, choose a bracketed or cabinet shelf rated for the weight.")
img(4)
p(f"Short on space? A sturdy wooden crate on a sideboard holds a few dozen records near the turntable, and the rest can live in a closet on an inside wall. Our {a('storage-ideas-for-small-spaces','storage ideas for small spaces')} have more ways to find room, and a cube unit can even double as a divider, as in our {a('room-divider-ideas','room divider ideas')}.")

h2("Step 7: Pick a Cool, Dry, Dark Spot")
p(f"Temperature and humidity swings do more damage than any shelf. The National Archives suggests keeping audio recordings {SR('nara','within the ranges of 55-70 degrees Fahrenheit and 30-55% relative humidity')}, and the Library of Congress figure of 65 to 70°F and 45 to 50% humidity fits a normal living room or bedroom. Steady conditions matter more than hitting an exact number.")
lst([f"<strong>Avoid the attic and garage.</strong> The National Archives says to avoid {SR('nara','an attic or garage')} because their climate is unregulated.",
f"<strong>Basements are a maybe.</strong> The National Archives notes they are often cooler and steadier, but says to choose another floor if yours floods, and to keep records off the floor.",
f"<strong>Keep out of the sun and away from heat.</strong> The National Archives of Australia warns that {SR('naa','vinyl discs will readily buckle')} if exposed to heat or sunlight, so don't store them by a radiator, a heating vent or a sunny window, or leave them in a parked car.",
f"<strong>Watch the damp.</strong> The Canadian Conservation Institute says that {SR('cci','at high RH, mould is a concern')} for all recording media."])

h2("78s and Singles Need Extra Care")
p(f"Old 78 rpm records are made of shellac, not vinyl. The University of Illinois preservation program describes them as {SR('psap','rigid and brittle')}, and the Library of Congress notes 78s are even heavier than LPs. Give them their own shelf, upright with good support, and don't use LP cleaning fluid on them: Audio-Technica says its LP fluid is not for shellac 78s. Keep 7-inch singles in a box or crate sized for them, rather than lost between LPs.")

h2("Storing Vinyl: Quick Answers")
h3("Is it bad to store vinyl records at an angle?")
p("Yes, if they lean for long. Records that sit at an angle put uneven pressure on the discs, and archives such as the National Archives of Australia recommend dividers or boxes that keep them from leaning. A slight lean in a crate you flip through every day is less of a worry than a half-empty shelf left for months.")
h3("Should you keep the plastic on vinyl records?")
p("Take off the original shrink wrap, because it can keep shrinking and warp the record. To protect the jacket, use a loose outer sleeve instead.")
p(f"Before you sort a big collection, our {a('how-to-declutter-your-home','guide to decluttering your home')} can help you decide what stays, and our {a('bookshelf-decor-ideas','bookshelf decor ideas')} show how to style the top of a record shelf.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('store vinyl records')+html.lower().count('storing vinyl'),'kw')
