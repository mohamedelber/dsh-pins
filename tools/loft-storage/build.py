import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
PP="https://www.planningportal.co.uk/permission/common-projects/loft-conversion/is-building-regulations-approval-needed-for-a-loft-conversion"
WH="https://www.which.co.uk/reviews/insulation/article/how-to-buy-loft-insulation"
NT="https://www.northtyneside.gov.uk/boarding-out-loft-storage"
LOC="https://www.loc.gov/preservation/care/paper.html"
p("Good loft storage ideas turn the space above your ceiling into somewhere you can actually find things again, instead of a dark tangle of boxes balanced on the joists. In most British homes the loft is the biggest storage space you have, but it only works if it is boarded properly, kept dry and organised by how often you need each item.")
p("This guide shows how to board a loft for storage without squashing the insulation, a 6-step plan and 16 loft storage ideas for boarded lofts, loft conversions, eaves and small lofts, with the safety points to check first.")
img(1)
summary(["<strong>Quick answer:</strong> Board a walkway on raised loft legs so the insulation stays at full depth, store light items in identical clear lidded boxes, keep the things you need every year nearest the hatch and leave the eaves and vents clear. In a loft conversion, use eaves drawers, eaves cupboards and shelves that follow the slope.",
"Only store light items such as suitcases, decorations and bedding unless a structural engineer or building control has confirmed the joists can take more.",
"Keep paper, photos and anything sensitive to heat or damp somewhere else."],
"<strong>Time:</strong> a weekend to sort and box up · <strong>Cost:</strong> low if the loft is already boarded; raised boarding is a bigger DIY job · <strong>Difficulty:</strong> Moderate")
toc("loft-storage")
h2("How to Board a Loft for Storage Safely")
p("Before you add a single box, check how the loft is built. Most loft floors are just ceiling joists with insulation between them, designed to hold up the ceiling below, not a floor full of storage.")
diagram(re.sub(r'(?<=[ "M,\-a-z])(\d+\.\d)\d+',r'\1',open('z.svg').read()),"How to board a loft for storage: loft legs stand on the joists and lift the boards above the insulation, which stays at about 270 mm, with gaps left at the eaves so air keeps flowing.")
p(f"Which? {ext(WH,'recommends 270 mm of mineral wool loft insulation')} and warns that squashing it under boards reduces how well it works. It suggests raising the floor level so the full depth fits beneath, and loft legs are a common way to do this. North Tyneside Council's {ext(NT,'rules for tenants boarding out a loft')} set three useful conditions: boarding should not compress the insulation, it should not block the ventilation the loft needs to avoid condensation, and it should leave flues alone. Its scheme also allows boarding only for light storage, such as suitcases and Christmas decorations.")
p(f"If you plan to use the loft as a room, the rules change. The Planning Portal explains that {ext(PP,'building regulations approval is required to convert a loft into a liveable space')}, and that existing joists are usually not designed for significant extra weight, so even boarding for storage can need approval. Check with your local council or building control before a big boarding job.")
h2("Quick Pick: Loft Storage Ideas by Loft")
table(["Your loft","Best ideas","Cost"],[
["Unboarded loft","#1, #5, #14","Low to medium"],
["Boarded loft","#2, #3, #4","Low"],
["Loft conversion bedroom","#9, #11, #12","Medium"],
["Eaves space","#9, #10, #11","Low to medium"],
["Small or awkward loft","#4, #14, #15","Free to low"],
["Seasonal items","#4, #8, #16","Free to low"]])
h2("How to Organise a Loft in 6 Steps")
lst(["<strong>Clear a landing space.</strong> Bring everything down to a spare room or landing so you can see what you have.",
"<strong>Declutter.</strong> Donate, sell or recycle what nobody has used in the last few years.",
"<strong>Check the floor.</strong> Make sure you have a safe walkway of boards on the joists, raised above the insulation.",
"<strong>Box it up.</strong> Use identical clear lidded boxes, one category per box, and label the ends.",
"<strong>Zone by use.</strong> Things you need every year go nearest the hatch; rarely used items go furthest away.",
"<strong>Keep a list.</strong> Note what is in each box on your phone so you only go up when you need to."],True)
img(6)
p(f"If the job feels too big, start with our guide on {a('how-to-declutter-your-home','how to declutter your home')} and tackle the loft last, once you know what is worth keeping.")
h2("Loft Storage Ideas for Boarded Lofts")
h3("1. Raise the Boards on Loft Legs")
p("Loft legs are plastic or metal stilts that screw onto the joists and hold the boards above the insulation, so you get a storage floor without squashing it. They are a popular way to board a loft that already has a full 270 mm of insulation. Keep the boarded area to a central walkway and leave the edges near the eaves clear.")
h3("2. Use Identical Clear Lidded Boxes")
p("Matching clear boxes stack neatly, keep out dust and let you see what is inside with a torch. Lids also help keep out insects. Choose a size you can carry up a loft ladder with one hand free, and avoid open cardboard boxes, which soften in damp air.")
h3("3. Add Low Shelving Between the Rafters")
img(3)
p(f"A low, freestanding shelving unit on the boards doubles your storage without stacking boxes four high. Keep it below the slope of the roof, put the heaviest boxes on the bottom shelf and leave a gap behind it so air can move. Our {a('diy-closet-shelves','DIY shelves guide')} shows simple builds you can adapt.")
h3("4. Zone the Loft by How Often You Need Things")
p(f"Put the things you fetch every year, such as Christmas decorations and suitcases, closest to the hatch. Keep rarely used items like keepsakes and spare bedding further back. For the festive boxes, our {a('christmas-decoration-storage','Christmas decoration storage')} ideas help you pack them well.")
h3("5. Keep a Clear Central Walkway")
p("A straight path of boards from the hatch to the far end means you never have to step between joists, where a foot can go straight through the plasterboard ceiling below. Store boxes either side of the walkway, never on it.")
h3("6. Light It Properly")
p("Poor light makes slips more likely. A battery LED lantern or a rechargeable light is the simple fix; a fixed light switched from the landing should be fitted by a qualified electrician. North Tyneside Council does not allow sockets in tenants' boarded lofts. Any new wiring should be done by a qualified electrician, and make sure boards and insulation never cover existing cables or junction boxes.")
h3("7. Fit a Proper Loft Ladder")
p("Carrying boxes up a stepladder is the riskiest part of using a loft. A folding loft ladder with a handrail makes access safer and quicker. If you need a new hatch, check current building regulations first, as the council guidance points out.")
h3("8. Protect What You Store From Heat and Damp")
p(f"Lofts get hot in summer and cold and damp in winter. The Library of Congress {ext(LOC,'advises against storing paper in attics and basements')}, so keep photos, documents and keepsakes in the house. Store bedding and soft toys in sealed bags inside boxes, and keep candles, paint and electronics out of the loft altogether.")
h2("Loft Conversion and Eaves Storage Ideas")
p("A converted loft has the same awkward slopes but more chances for built-in storage. These ideas use the low spaces under the roof that are too short to stand in.")
h3("9. Build Drawers Into the Eaves")
img(2)
p(f"Pull-out drawers set into the low knee wall turn dead space under the slope into a chest of drawers that takes up no floor space. They suit loft bedrooms where a wardrobe will not fit. See our {a('box-room-bedroom-ideas','box room bedroom ideas')} for other ways to make a small bedroom work.")
h3("10. Line Eaves Cupboards With Boxes")
img(4)
p("Behind a small door, the triangular eaves space is ideal for suitcases and seasonal items. Put the tallest boxes at the front and the smallest at the back where the roof gets low, and add a battery puck light so you can see in.")
h3("11. Fit Shelves That Follow the Slope")
img(5)
p("Built-in shelves that step down with the roof line use every centimetre of a sloping wall on a loft landing or in a bedroom. Keep heavy books on the lower shelves and display pieces at the top.")
h3("12. Choose a Bed With Storage")
p(f"In a loft bedroom, an ottoman or drawer bed holds bedding and out-of-season clothes without using wall space you do not have. Our {a('small-bedroom-storage-ideas','small bedroom storage ideas')} cover the best styles.")
h3("13. Put Wardrobes Where the Ceiling Is Highest")
p("Long coats need roughly 1.5 to 1.7 m of hanging height, so measure first and place a wardrobe or open rail under the ridge and use the low sides for drawers and baskets.")
h2("Small Loft and Rented Home Ideas")
h3("14. Board Just the Area by the Hatch")
p(f"If you rent or your loft is small, you do not need to board all of it. A few raised boards around the hatch give you space for lightweight boxes; ask your landlord before fixing anything. For more space-saving ideas inside the home, try our {a('under-stairs-storage-ideas','under stairs storage ideas')} and {a('airing-cupboard-shelves','airing cupboard shelves')}.")
h3("15. Use Vacuum Bags for Bulky Soft Items")
p("Duvets, pillows and winter coats take up most of a small loft. Vacuum bags shrink them to a fraction of the size (avoid long-term compression for down and wool); put the bags inside a lidded box so they do not get punctured.")
h3("16. Do a Yearly Loft Check")
p(f"Once a year, ideally when you bring the Christmas boxes down, check for damp patches, droppings or damage and pass on anything you no longer need. If you are moving soon, our {a('moving-box-calculator','moving box calculator')} helps you plan the boxes.")
add(open('savebox.html').read())
h2("Common Loft Mistakes")
lst(["<strong>Laying boards straight on top of insulation.</strong> Squashed insulation keeps your home less warm.",
"<strong>Overloading the joists.</strong> Ceiling joists are not a floor; keep storage light.",
"<strong>Blocking the eaves.</strong> Boxes against the eaves can stop air flowing and lead to condensation.",
"<strong>Storing paper and photos up there.</strong> Heat and damp damage them; keep them in the house.",
"<strong>Using open cardboard boxes.</strong> They soften, collapse and let in insects.",
"<strong>Stepping between the joists.</strong> Stay on the boards so you do not go through the ceiling."])
h2("Loft FAQ")
h3("Can you put boards on top of loft insulation?")
p("You should not lay boards directly on top of loft insulation, because squashing it reduces how well it insulates. Instead, fit loft legs or a raised floor on the joists so the boards sit above the insulation, which Which? recommends at 270 mm for mineral wool, and leave the eaves clear for ventilation.")
h3("Do you need building regulations to board a loft?")
p("The Planning Portal says loft joists are usually not designed for significant extra weight, so boarding over them for storage may need building regulations approval. Converting a loft into a room always needs approval, so check with building control before you start.")
h3("What should you not store in a loft?")
p("Avoid storing photos, documents, paper keepsakes, candles, paint, aerosols, electronics and anything heavy in the loft. Heat, cold and damp damage paper and electronics, and heavy items can overload the ceiling joists. Keep the loft for light, robust items such as suitcases, bedding in sealed bags and seasonal decorations.")
h3("How do you organise a small loft?")
p("Board a walkway by the hatch on raised loft legs, use identical clear lidded boxes and keep a list of what is in each box. Store the items you need every year nearest the hatch and rarely used things further back, and use vacuum bags to shrink bulky bedding.")
h2("Final Thoughts")
p("The best loft storage ideas start with a safe floor: raised boards, full-depth insulation and clear eaves. After that, matching boxes, simple zones and a yearly check keep the loft useful instead of a place where things disappear.")
p(f"Making room in the rest of the house? See our {a('box-room-bedroom-ideas','box room ideas')}, {a('under-stairs-storage-ideas','under stairs storage')} and {a('boot-room-ideas','boot room ideas')}, and save this guide on Pinterest for your next loft clear-out.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
txt=re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<svg.*?</svg>','',html))
print(len(html),'words',len(txt.split()),'kw',txt.lower().count('loft storage'))
print(sorted(set(re.findall(r'dailyspacehacks\.com/([a-z0-9-]+)/',html))))
for w in ['organize','color','center','favorite','closet','apartment']:
    if w in txt.lower(): print('US word:',w)
