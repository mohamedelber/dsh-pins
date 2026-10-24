import re,json
exec(open('helpers.py').read())
IMG={int(k):tuple(v) for k,v in json.load(open('img.json')).items()}
SRC={
"sc":"https://healthwell.eani.org.uk/node/5449",
"nhs":"https://www.royalberkshire.nhs.uk/media/qowjobz5/sleep-hygiene_dec23.pdf",
"ih_bulb":"https://idealhome.co.uk/all-rooms/how-to-choose-the-right-light-bulb-warmth",
"est":"https://energysavingtrust.org.uk/energy-saving-budget?loc=wales",
"lfb":"https://london-fire.gov.uk/safety/the-home/electrical-items/electric-blankets",
"warw":"https://www.warwickshire.gov.uk/news/article/4828/firefighters-issue-festive-electrical-safety-advice-",
"dwf":"https://www.dwfire.org.uk/news/warning-on-candle-safety-after-bedroom-fire",
"swb":"https://swanseabay.nhs.wales/news/swansea-bay-health-news/burns-patients-stark-warning-about-the-potential-dangers-of-hot-water-bottles/",
"fbc":"https://www.finebedding.co.uk/blogs/news/what-tog-duvet",
"rug":"https://www.idealhome.co.uk/all-rooms/bedroom/bedroom-rug-rules",
"rugg":"https://ruggable.co.uk/blogs/what-size-rug-should-I-get-for-under-my-bed",
"tand":"https://www.tandridge.gov.uk/condensation",
"paint":"https://www.idealhome.co.uk/bedroom/bedroom-decor/small-bedroom-paint-ideas"}
def SR(k,t): return ext(SRC[k],t)

p(f"The best cosy bedroom ideas work on three things at once: warmth you can feel, light that is soft and low, and texture you want to touch. Swap the ceiling light for two warm lamps, layer the bed, put a big rug underneath and close lined curtains at night, and even a small, chilly box room starts to feel like a retreat.")
p(f"Cosy should also mean comfortable to sleep in. The Sleep Charity puts {SR('sc','an ideal bedroom temperature')} at around 16 to 18°C, so the aim is a room that feels warm without being stuffy. The 10 ideas below are grouped into light, layers, warmth and the finishing touches, with the measurements that matter.")
img(1)

h2("A Cosy Small Bedroom, Measured")
diagram(open('z.svg').read(),"An example cosy layout for a small UK double bedroom: warm lamps on both sides, a rug showing about 55 cm each side of the bed, a clear radiator and the wardrobe on an inside wall.")

h2("Light: Cosy Bedroom Ideas for the Evening")
h3("1. Swap the Ceiling Light for Two Low Lamps")
img(2)
p(f"Nothing kills a cosy feeling like one bright bulb in the middle of the ceiling. Use a lamp on each side of the bed and a wall light for reading. Ideal Home describes warm white bulbs of {SR('ih_bulb','2700K-3000K')} as ideal for a snug space. An NHS sleep leaflet also suggests you {SR('nhs','dim lights during the evening')}, so a lamp with a dimmer or a low-wattage bulb does two jobs.")
h3("2. Keep Screens and Standby Lights Out")
p(f"Small lights matter more than you might think. The Sleep Charity warns that {SR('sc','even small amounts of light')} from an alarm clock or a TV standby button can disturb sleep, and suggests a red night light if you need one. Charge phones outside the bedroom, or face them down, and cover bright LEDs.")

h2("Layers: Bedding and Textiles")
h3("3. Choose the Right Tog for the Season")
img(3)
p(f"A thick duvet is the quickest way to feel warm, but too heavy and you will wake up hot. The Fine Bedding Company suggests 4.5 tog for summer, 7 to 10.5 for spring and autumn, and {SR('fbc','13.5 tog')} for winter. A four-seasons duvet, which clips a 4.5 and a 9 tog together, lets you change through the year without buying three.")
h3("4. Layer Throws and Cushions in Different Textures")
p("Cosy is mostly texture. Put a waffle or wool blanket across the foot of the bed, a chunky knitted throw on top, and three or four cushions in different fabrics such as linen, velvet and bouclé. Keep the colours close together, for example oatmeal, sage and caramel, so the bed looks layered rather than busy. Fold extra blankets into a basket so they are easy to grab on cold nights.")
h3("5. Put a Big Rug Under the Bed")
p(f"Stepping onto a soft rug in the morning makes a bare-floored room feel warmer straight away. Helen Ashmore, head of design at Laura Ashley, told Ideal Home a bedroom rug should {SR('rug','extend at least 45-60cm beyond the sides and foot of the bed')}. For a standard UK double, Ruggable suggests {SR('rugg','a 185x275 cm or 245x305 cm rug')}; the larger size gives you that 45 to 60 cm on each side. Our {a('rug-size-calculator','rug size calculator')} works it out for other beds.")

h2("Warmth: Keep the Heat In")
h3("6. Hang Lined Curtains and Close Them at Night")
img(4)
p(f"Heavy, lined curtains block draughts and make a room feel enclosed and calm. The Energy Saving Trust says {SR('est','closing blinds and curtains at night')} can limit heat loss, but warns against letting curtains cover radiators, which sends the heat out of the window. Hang the pole wider and higher than the window and let the curtains stop beside a radiator, not over it. Our {a('curtain-size-calculator','curtain size calculator')} gives the drop and width.")
h3("7. Seal the Draughts")
p(f"Gaps around windows and doors make a room feel cold even when the heating is on. The Energy Saving Trust puts the potential saving from draught-proofing at {SR('est','£40 a year')}, and self-adhesive strips are a quick DIY job. A fabric draught excluder along the bottom of the bedroom door helps too.")
h3("8. Warm the Bed Safely")
p(f"Hot water bottles and electric blankets are cosy, but both need care. An NHS burns centre advises that you {SR('swb','replace your hot water bottle every two years')}, fill it no more than two thirds and use a cover. The London Fire Brigade says to replace electric blankets at least every 10 years, never use one together with a hot water bottle, and {SR('lfb','unplug blankets before you get into bed')} unless the blanket is designed to stay on all night.")

h2("Finishing Touches")
h3("9. Paint the Walls a Warm, Muted Colour")
p(f"White walls can feel cold in a north-facing British bedroom. Justyna Korczynska, senior designer at Crown, told Ideal Home that {SR('paint','darker muted shades are good for creating a cosy and cocooning space')}, and a Benjamin Moore colour expert suggests shades with a yellow or red undertone. Warm terracotta, mushroom or deep sage all work. If painting is not an option, a fabric headboard does a similar job.")
h3("10. Make a Small Reading Corner")
img(5)
p(f"A small armchair, a floor lamp and a side table for a mug turn a spare corner into the cosiest spot in the room. Keep it simple: one chair, one light and one throw. Our {a('small-bedroom-storage-ideas','small bedroom storage ideas')} help free up the space, and our {a('box-room-bedroom-ideas','box room bedroom ideas')} show what fits in the smallest rooms.")

h2("Keep It Cosy and Safe")
p(f"Two common habits work against a cosy, healthy bedroom. First, avoid drying washing in the bedroom: Tandridge District Council says {SR('tand','do not dry washing on radiators')} and explains that drying clothes indoors adds a lot of moisture, which leads to condensation and mould. Second, take care with lights. Warwickshire fire service advises that {SR('warw','all fairy lights are switched off')} before going to bed, and Dorset and Wiltshire Fire and Rescue says to make sure candles are {SR('dwf','out completely at night')}. Battery-powered flameless candles give the same glow without the risk.")

h2("Where to Start")
img(6)
p("This before and after illustration shows how much warmth, light and texture change the same small bedroom.")
p(f"Of all these cosy bedroom ideas, if you only change one thing, change the light: two warm lamps instead of the ceiling bulb will make more difference than any new bedding. Then add a rug and a throw, close the curtains at dusk, and keep the room at around 16 to 18°C. For a room that also has to work for visitors, our {a('guest-bedroom-ideas','guest bedroom ideas')} and {a('boho-bedroom-ideas','boho bedroom ideas')} have more ways to layer a bedroom.")
ai_note()
html='\n\n'.join(out)
html=re.sub(r'(\d+\.\d{2})\d+',r'\1',html)
open('content.html','w').write(html)
print(len(html.encode()),'bytes;',len(re.sub('<[^>]+>',' ',html).split()),'words;',html.lower().count('cosy bedroom ideas'),'kw')
