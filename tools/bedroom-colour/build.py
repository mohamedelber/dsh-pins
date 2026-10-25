import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={"hgfb":"https://www.homesandgardens.com/interior-design/best-farrow-and-ball-paints-for-bedrooms",
"hgsage":"https://www.homesandgardens.com/interior-design/best-sage-green-paints",
"sofa":"https://blog.sofasandstuff.com/2025/03/11/curated-bedroom-colours-with-ruth-mottershead-of-little-greene/",
"ihgreen":"https://www.idealhome.co.uk/bedroom/bedroom-decor/best-green-paint-shades-for-a-bedroom",
"dbed":"https://www.dulux.co.uk/en/bedrooms",
"crown":"https://www.crownpaints.com/ie/inspiration-bedroom",
"hgolive":"https://www.homesandgardens.com/interior-design/best-olive-green-paint",
"liv25":"https://www.livingetc.com/spaces/interior-inspiration/bedroom-colour-ideas-25-paint-colours-with-impact-233940",
"sheer":"https://sheerluxe.com/home/farrow-ball%E2%80%99s-colour-expert-shows-us-round-her-home",
"hague":"https://www.homesandgardens.com/interior-design/decorating-with-Farrow-and-Ball-Hague-Blue",
"ihsch":"https://www.idealhome.co.uk/bedroom/bedroom-ideas/bedroom-colour-schemes-89813",
"livn":"https://www.livingetc.com/ideas/best-farrow-ball-paint-colors-for-north-facing-rooms",
"livsleep":"https://www.livingetc.com/ideas/best-paint-colors-for-sleep-in-bedroom",
"livw":"https://www.livingetc.com/advice/little-greene-choosing-perfect-white",
"brinjal":"https://www.farrow-ball.com/ie/the-chromologist/spotlight-on-brinjal",
"myl":"https://mylands.com/blogs/news/purple-paint-for-bedrooms",
"ihterra":"https://www.idealhome.co.uk/all-rooms/all-rooms-decor/how-to-decorate-with-terracotta",
"dasp":"https://www.dulux.co.uk/en/expert-help/dr-dulux-how-decorate-north-south-facing-rooms",
"dher":"https://duluxheritage.co.uk/en/inspiration/article/31/how-to-pick-the-right-heritage-shade",
"lrv":"https://www.homesandgardens.com/interior-design/what-is-light-reflective-value",
"fbs":"https://www.farrow-ball.com/ie/how-to-guide/how-to-sample",
"pshed":"https://www.thepaintshed.com/tips-advice/the-correct-way-to-test-and-use-paint-samples",
"drench":"https://www.idealhome.co.uk/all-rooms/colour-drenching-paint-trend",
"ceil":"https://www.livingetc.com/advice/paint-ceilings-and-walls-the-same-color",
"r603":"https://www.idealhome.co.uk/all-rooms/all-rooms-decor/60-30-10-rule",
"estate":"https://www.homesandgardens.com/interior-design/paint/estate-emulsion-vs-modern-emulsion",
"finish":"https://www.idealhome.co.uk/diy/what-paint-finish-is-best-for-walls-and-ceilings",
"netregs":"https://www.netregs.org.uk/environmental-topics/air-pollution/solvent-emissions/solvent-limits-in-paints-and-varnishes/",
"hse":"https://www.hse.gov.uk/construction/faq-paint.htm",
"dmatt":"https://www.dulux.co.uk/en/products/dulux-matt",
"travel":"https://www.travelodge.co.uk/blog/featured/bedroom-wall-colours",
"rest":"https://www.idealhome.co.uk/news/worst-colour-to-paint-a-bedroom-218092",
"nhs":"https://111.wales.nhs.uk/Insomnia/",
"sleepch":"https://thesleepcharity.org.uk/information-support/adults/sleep-hub/blue-light-and-sleep/",
"coty":"https://www.homesandgardens.com/decor/paint/dulux-colour-of-the-year-2027-soulful-sage",
"rhythm":"https://www.idealhome.co.uk/all-rooms/rhythm-of-blues-dulux-colours-of-the-year-2026",
"fbpop":"https://www.idealhome.co.uk/all-rooms/farrow-and-ball-most-popular-paint-colours-2026",
"lg26":"https://www.idealhome.co.uk/all-rooms/little-greene-26-new-paint-shades-2026-first-look"}
def SR(k,t): return ext(SRC[k],t)

p(f"The best bedroom colour ideas start with the light, not the paint chart. In a north-facing bedroom, warm shades such as plaster pink, terracotta and warm white stop the room feeling cold; in a south-facing one, cooler greens and blues stay fresh. Soft sage green is the safest all-rounder, and Farrow &amp; Ball's Patrick O'Donnell says {SR('hgfb','green is the most natural colour family for the bedroom')}. Below are 14 bedroom colour ideas from paint-brand colour experts and designers, with named shades, plus how to test them before you commit.")
img(1)

h2("Start With Which Way Your Bedroom Faces")
diagram(open('z.svg').read(),"Window direction changes how paint looks: go warm in a north-facing bedroom, cooler in a south-facing one, and test east and west-facing rooms at the times you use them.")
p(f"Dulux puts it simply: {SR('dasp','the natural light a room receives has a huge effect on colour')}. Its advice is warm pinks and yellows for north-facing rooms and cooler shades for south-facing ones. Tash Bradley, Lick's director of interior design, explains that north-facing rooms {SR('lrv','receive cooler, bluish light, which can make colors appear darker')}. For east and west-facing rooms, Dulux Heritage says {SR('dher','it\'s all about the time of day and when you\'ll be using the space')}. Most of us use a bedroom early in the morning and at night, so judge colours at those times, under your own lamps.")
p(f"A paint's light reflectance value (LRV) tells you how much light it bounces back, on {SR('lrv','a scale from 0 to 100')}. A high LRV helps in a dim room, but Bradley adds that {SR('lrv','light needs to be present for the paint to reflect it')}. That is why designers often go darker, not paler, in a small, gloomy bedroom.")

h2("Greens")
h3("1. Soft Sage Green")
p(f"Sage is the colour most bedroom colour ideas come back to. Dulux named Soulful Sage its Colour of the Year 2027, and creative director Marianne Shillingford says {SR('coty','its soft, silvery quality brings a sense of lightness')}. O'Donnell suggests Farrow &amp; Ball Lichen {SR('hgsage','for a relaxing bedroom across both walls and woodwork')}, and Little Greene's Ruth Mottershead calls Little Greene Sage Green {SR('hgsage','a calming and sophisticated shade of green with a very soothing effect')}. On a budget, Crown's Mellow Sage is {SR('crown','a restorative pale sage green paint')}. Farrow &amp; Ball colour curator Joa Studholme painted her own main bedroom in French Gray, a soft green, to link it to the garden outside. Pair sage with white linen, oak and a rust-coloured throw, as in the illustration above.")
h3("2. Deep Forest or Olive Green")
p(f"Darker greens make a bedroom feel enclosed and calm rather than bright. Chelsea Clark of Lust Home says dark, rich greens {SR('ihgreen','bring depth to a room')}; Ideal Home suggests Dulux Everglade Forest, and Crown's Woodland Wanderer is {SR('crown','a rich, deep and calming green')}. For olive, designer Julia Baum says Farrow &amp; Ball Bancha {SR('hgolive','has a deep feel that creates a sense of calm in any space')}. Green also works in a {a('box-room-bedroom-ideas','box room bedroom')}, where a dark shade blurs the corners.")

h2("Blues")
h3("3. Soft, Changeable Blue")
p(f"Valspar's Lucy Steele says {SR('ihsch','blue is one of the colours most associated with calm')}. Pale blues shift with the light: Studholme says Farrow &amp; Ball Light Blue in her triple-aspect spare bedroom is {SR('sheer','positively blue in strong morning light')} and greyer later. Farrow &amp; Ball Lulworth Blue No. 89 and Dulux's 2026 colour Mellow Flow, {SR('rhythm','the perfect muted blue that calms and soothes')}, are softer options. In a south-facing room, Dulux also suggests the pale Nordic Sky.")
h3("4. Navy and Inky Blue")
p(f"Designer Alice Bettington says {SR('liv25','darker blues are a wonderful choice for bedrooms as they evoke the night sky')}. O'Donnell says Farrow &amp; Ball Hague Blue {SR('hague','works a treat in north-facing rooms')} because of its green undertone. Mottershead recommends Little Greene Royal Navy, saying deep shades {SR('sofa','create depth and intimacy')}, and Crown's Midnight Navy is the high-street version. Navy looks best painted everywhere, which is idea 13.")

h2("Pinks, Whites and Warm Neutrals")
h3("5. Plaster Pink")
img(3)
p(f"O'Donnell's advice is direct: {SR('hgfb','pink is a colour for those poorly lit north-facing bedrooms')}. His pick, Farrow &amp; Ball Setting Plaster, is one Studholme uses in her own small third bedroom. Charlotte Cosby, Farrow &amp; Ball's creative director, calls it {SR('livn','perfect for enveloping north-facing spaces')}. Little Greene's earthier Split Pink and Lick Pink 02 are close alternatives; Bradley says Pink 02 {SR('livsleep','offers exactly what a bedroom should feel like')}.")
h3("6. Warm White")
p(f"White is not one colour. Mottershead says {SR('livw','warm whites work particularly well in north-facing rooms')}, while {SR('livw','cool whites can work well in south-facing rooms')}. For a bedroom she suggests the pink-tinged Little Greene China Clay or Rolling Fog – Pale. Crown's Fresh Coconut is {SR('crown','a delicate neutral, warm off white')}. Designer Katie Miller says Farrow &amp; Ball Shaded White {SR('hgfb','always looks different throughout the day')}, so sample it first.")
h3("7. Taupe, Stone and Mushroom")
p(f"If you are moving away from grey, warm neutrals are the obvious replacement. Ideal Home reports that {SR('fbpop','warm, characterful colours are driving sales in 2026')} at Farrow &amp; Ball, with Wimborne White its best seller and Mouse's Back among the risers. Designer Adam Knight chose the darker Oxford Stone for a bedroom, saying it promotes {SR('hgfb','rest, comfort, and calm')}. Little Greene's Masquerade is a lighter warm neutral Mottershead suggests for bedrooms.")

h2("Deep and Earthy Colours")
h3("8. Terracotta and Clay")
p(f"Cosby says Farrow &amp; Ball Red Earth is {SR('livn','the perfect shade for embracing a warmer color palette')} in a north-facing room. James Sirett of Fired Earth says {SR('ihterra','terracotta has a reassuring earthiness')}, but Annie Sloan warns that deep terracotta can look muddy in a dark north-facing room, so test a sample there. Terracotta also works lower down the wall (idea 14).")
h3("9. Aubergine and Plum")
p(f"Farrow &amp; Ball says {SR('brinjal','in bedrooms, Brinjal feels dramatic yet grounding')}; Brinjal No. 222 is a deep, wine-coloured purple. Mylands suggests its Plum Tree No. 283 behind the bed, saying {SR('myl','it\'s comforting and reassuring')}, and the paler, grey-lilac Lavender Garden No. 30 if a dark purple feels too much. Graham &amp; Brown's 2026 colour, Divine Damson, sits in the same family.")
h3("10. Deep Red")
p(f"Red sounds stimulating, but a dark, brown-based red can feel enclosing. Mottershead suggests Little Greene Baked Cherry for all-over bedroom schemes, {SR('sofa','creating that cosy, cocooning quality')}. Keep it to walls you see from bed, not the wall you face when you wake, if you find it too strong.")
h3("11. Soft Black")
p(f"O'Donnell says Farrow &amp; Ball Railings can be {SR('hgfb','a surprisingly successful option in a naturally poorly lit or small room')}. Andy Greenall of Paint &amp; Paper Library says {SR('liv25','black helps to create a calm, intimate ambience')}. Warm it up with wood, brass and soft white bedding.")
h3("12. Ochre Yellow, Used Carefully")
p(f"Yellow divides opinion. Mottershead suggests Little Greene Bassoon, an ochre, to {SR('sofa','help us feel uplifted, happy and energised')}. Colour psychologist Karen Haller, working with bed maker Rest Assured, told Ideal Home to {SR('rest','avoid yellow in the bedroom')}. If you love it, choose a muted ochre over a bright lemon, and try it on a headboard wall first.")

h2("Ways to Use Colour in a Bedroom")
h3("13. Colour Drench the Whole Room")
img(2)
p(f"Colour drenching means you {SR('drench','take one colour and paint everything in that room in the same one colour')}: walls, ceiling, skirting, doors and window frames. Bradley says the result is that {SR('drench','you don\'t notice the edges of the room')}. Studholme uses one colour per bedroom at home because most of them are so small. Use a flat or low-sheen eggshell on the woodwork so it reads as one colour. Designer Lizzie Green says drenching is {SR('ceil','hugely effective in making a space feel bigger')}.")
h3("14. Two-Tone Walls")
img(4)
p(f"Painting the lower part of the wall in a deeper colour grounds the bed and makes the ceiling feel higher. One Dulux example shown by Ideal Home paints roughly the bottom two-thirds of the wall in Mellow Flow and the top third off-white. Keep the line straight with low-tack masking tape, and set it just above the headboard or at picture-rail height. Panelling does the same job: our {a('wainscoting-calculator','wainscoting calculator')} and {a('board-and-batten-calculator','board and batten calculator')} work out the spacing.")
p(f"To pull a bedroom colour scheme together, use the 60-30-10 rule. Ben Thomson of Promain describes it as {SR('r603','allocating 60% of a room\'s colour to the dominant hue')}, 30% to a secondary colour and 10% to an accent, which Valspar's Sarah Lloyd says goes into {SR('r603','soft furnishings such as throws, pillows, artwork and accessories')}. Interior designer Emma Deterding stresses {SR('r603','there are no hard and fast rules')}.")

h2("How to Test and Paint")
img(5)
lst([f"<strong>Sample big.</strong> Farrow &amp; Ball says to paint two coats of sample pot on card, {SR('fbs','the bigger the better')}, and {SR('fbs','check your samples over the course of a day or two')}. For a bedroom, close the curtains and look at them under a lamp too. The Paint Shed suggests A5 or bigger and moving the card around the room.",
f"<strong>Pick a finish.</strong> Matt or flat emulsion hides uneven walls. Farrow &amp; Ball Estate Emulsion has a 2% sheen and is {SR('estate','wipeable but not washable')}; Modern Emulsion (7%) is tougher. Designer Claire Garner says {SR('finish','my go-to paint finish for walls and ceilings is always matt')}.",
f"<strong>Buy enough.</strong> Dulux Matt covers {SR('dmatt','up to 14m2/litre')} per coat, and most colour changes need two coats. So a 5-litre tin gives two coats on up to about 35 m², roughly the walls of a 3.5 m square bedroom with a 2.4 m ceiling once the door and window are taken off. Measure yours.",
f"<strong>Ventilate.</strong> UK rules limit matt interior wall paint to {SR('netregs','30 g/l')} of VOCs (solvents) when ready to use. The HSE's advice is simple: {SR('hse','if indoors open doors and windows')}. Paint early in the day so the room can air before you sleep in it.",
f"<strong>Wallpaper instead?</strong> Our {a('wallpaper-calculator','wallpaper calculator')} works out how many rolls a feature wall needs."])

h2("What Is the Best Bedroom Colour for Sleep?")
p(f"There is no proven sleep colour. The most quoted figures come from commercial surveys, not trials: a Travelodge survey of 2,000 British homes found {SR('travel','58% of Britons with a blue wall colour reported waking up feeling happy')}, and Rest Assured's research put soft green as the most restful. Treat them as opinion polls. NHS advice for better sleep is to {SR('nhs','make sure your bedroom is dark and quiet')} and to avoid screens before bed, because {SR('nhs','the bright light makes you more awake')}. So choose a colour you find calming, add blackout lining and warm bedside lamps, and the paint will do its part. Our {a('small-bedroom-storage-ideas','small bedroom storage ideas')} help with the clutter that keeps many of us awake.")

h2("If You Only Do One Thing")
p("Buy three sample pots before you buy any paint: one warm, one cool and one deep shade from the ideas above. Paint each on a large card, look at them first thing in the morning and again at night under your lamps, and choose the one you still like on day two.")
ai_note()
html='\n\n'.join(out)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('bedroom colour ideas'),'kw')
