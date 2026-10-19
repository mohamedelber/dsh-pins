import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
AT="https://www.apartmenttherapy.com/faqs-how-high-to-hang-art-229727"
BV="https://www.bobvila.com/articles/how-high-to-hang-pictures/"
LE="https://www.livingetc.com/advice/picture-hanging-hack"
LF="https://www.livingetc.com/advice/how-high-to-hang-art-above-furniture"
HU="https://www.hunker.com/12003406/height-to-hang-a-picture-over-a-sofa/"
RO="https://rossettiart.com/blogs/news/over-bed-wall-art"
UG="https://ugallery.com/blogs/articles/how-high-should-i-hang-art"
CM=2.54
def q(x): return ('%g' % (round(x*4)/4))
p("How high should you hang pictures? On an open wall, hang them so the center of the picture sits about 57 inches (145 cm) from the floor, roughly average eye level. This free <strong>picture hanging height calculator</strong> turns that rule into the one number you need: exactly where to put the nail.")
p("Pick where the picture goes, tap the frame height and the nail height appears. It also works above a sofa, bed, console or mantel, where the gap above the furniture matters more than eye level. Open <em>More options</em> for picture wire, an exact frame size or your own furniture height.")
add('<!-- wp:html -->\n'+open('tool.html').read()+'\n<!-- /wp:html -->')
h2("Picture Hanging Height Chart")
p("Nail heights from the floor for a picture on an open wall, with the center of the picture at 57 in (145 cm). A sawtooth hanger or D-rings usually sit about 1 in (2.5 cm) below the top of the frame; tight picture wire often sits about 3 in (7.5 cm) below it. Measure your own frame for an exact answer.")
rows=[]
for h,hc in [(12,30),(16,40),(20,50),(24,60),(30,75),(36,90)]:
    rows.append([f"{h} in ({hc} cm)", f"{q(57+h/2-1)} in ({round((57+hc/2.54/2-1)*2.54)} cm)", f"{q(57+h/2-3)} in ({round((57+hc/2.54/2-3)*2.54)} cm)"])
table(["Frame height","Nail with sawtooth or D-rings","Nail with picture wire"],rows)
p(f"The 57 in rule comes from galleries: Apartment Therapy explains that {ext(AT,'57 inches represents the average human eye height')} and is used as a standard in many galleries and museums. Some designers go a little higher; in Livingetc, an art advisor recommends {ext(LE,'about 60 inches (150 cm) to the center')}, and the article calls 57 to 60 in (145 to 152 cm) a good starting point.")
h2("How the Picture Hanging Height Calculator Works")
lst(["<strong>Open wall:</strong> nail height = 57 in (or 60 in) + half the frame height &minus; the distance from the top of the frame to the hanger. This is the method in Apartment Therapy's guide; Bob Vila adds that hanging hardware can sit anywhere from half an inch to three inches below the top of the frame.",
"<strong>Above furniture:</strong> the bottom of the frame goes a set gap above the furniture, and the nail goes one frame height higher, minus the hanger distance. The gap starts at 8 in (20 cm), or 9 in (23 cm) above a headboard, and you can change it.",
"<strong>Typical furniture heights</strong> are our own starting points: a sofa back about 34 in (86 cm), a headboard 48 in (122 cm), a console 32 in (81 cm) and a mantel 54 in (137 cm). Measure yours and enter them under More options for an exact result.",
"<strong>Very tall frames</strong> on an open wall are kept at least 12 in (30 cm) off the floor, and the calculator warns you when the top of the frame gets close to a standard 8 ft (244 cm) ceiling."])
h2("How High to Hang Pictures Above Furniture")
table(["Where","Gap between furniture and frame","Source"],[
["Above a sofa","4 to 10 in (10 to 25 cm)","Hunker; Livingetc gives 6 to 12 in"],
["Above a bed","8 to 10 in (20 to 25 cm) above the headboard","Rossetti Art"],
["Above a mantel","6 to 12 in (15 to 30 cm)","UGallery"],
["Above a console or sideboard","6 to 12 in (15 to 30 cm)","UGallery (large pieces over furniture)"]])
img(1)
p(f"Hunker's guide to {ext(HU,'hanging a picture over a sofa')} suggests 4 to 8 inches above the couch, with some designers leaving 8 to 10 inches, and art no more than two-thirds the width of the furniture. Rossetti Art suggests {ext(RO,'8 to 10 inches above a headboard')} and art about two-thirds of the headboard width, and UGallery suggests {ext(UG,'6 to 12 inches above a mantel')}. In {ext(LF,'Livingetc')}, an art advisor puts the lowest point of the art about 6 to 12 inches above the furniture.")
img(3)
h2("How to Hang a Picture at the Right Height")
lst(["<strong>Measure the frame</strong> from top to bottom, then measure from the top of the frame down to the hanger. For picture wire, pull the wire up tight first.",
"<strong>Get the nail height</strong> from the calculator above.",
"<strong>Mark the wall.</strong> Measure up from the floor (not from the baseboard) and mark the height on a strip of painter's tape. Mark the center of the wall or the furniture too.",
"<strong>Check the wall</strong> for hidden pipes and cables before you drill, and pick a hook or anchor rated for the weight of the frame.",
"<strong>Hang and level.</strong> For a wide frame, use two hooks at the same height so it stays straight."],True)
h2("Gallery Walls and Groups of Pictures")
p(f"Apartment Therapy suggests treating a group or gallery wall as one giant picture and hanging its center piece at 57 in (145 cm). Over furniture, use the same gap as for a single piece. Leave 2 to 3 in (5 to 8 cm) between frames, as Hunker suggests; UGallery puts medium pieces 2 to 3 in apart and smaller pieces 1.5 to 2 in apart. Lay the frames out on the floor or tape paper cutouts to the wall before you drill.")
img(2)
add(open('savebox.html').read())
h2("Picture Hanging FAQ")
h3("How high should pictures be hung on a wall?")
p("Hang pictures so their center sits about 57 to 60 inches (145 to 152 cm) from the floor, which is roughly average eye level and the standard many galleries use. For a 20 in frame with a hanger 1 in below the top, that puts the nail about 66 in (168 cm) from the floor.")
h3("How high should a picture be hung above a couch?")
p("Leave about 4 to 10 inches (10 to 25 cm) between the top of the sofa back and the bottom of the frame, so the art and the sofa read as one group. Choose art about two-thirds as wide as the sofa, and keep it centered over the sofa rather than over the wall.")
h3("How high should art be above a bed?")
p("Hang art about 8 to 10 inches (20 to 25 cm) above the top of the headboard, and choose a piece about two-thirds as wide as the headboard. Use secure hooks rated for the weight, and avoid heavy glass frames above where you sleep.")
h3("What is the 57 inch rule for hanging pictures?")
p("The 57 inch rule says to hang art so its center is 57 inches (145 cm) from the floor, about average eye height. Measure your frame, halve its height, add it to 57 and subtract the distance from the top of the frame to the hanger: that gives the nail height.")
h2("More Wall Planning Tools")
p(f"Mounting a screen too? Our {a('tv-mounting-height-calculator','TV mounting height calculator')} uses the same eye-level idea, and our {a('shelf-spacing-calculator','shelf spacing calculator')} plans floating shelves. For ideas on what to hang, see our {a('kitchen-wall-decor-ideas','kitchen wall decor ideas')}, {a('powder-room-decor-ideas','powder room decor ideas')} and {a('christmas-mantel-decorating-ideas','Christmas mantel decorating ideas')}, and finish the room with our {a('curtain-size-calculator','curtain size calculator')} and {a('rug-size-calculator','rug size calculator')}.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<script.*?</script>|<style.*?</style>','',html))
print(len(html),'words',len(txt.split()),'kw',txt.lower().count('hang'),txt.lower().count('picture hanging height'))
for w in ['colour','metre','organise']:
    if w in txt.lower(): print('UK word',w)
