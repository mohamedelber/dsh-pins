# Fact-check: Bedroom Colour Ideas (publishes 25 Jan 2027)

Checked 26 Oct 2026 against live pages (WebSearch, then WebFetch). WebFetch passes pages through a summariser that caps quotes at about 125 characters. Where a quote below is marked "(truncated)", only the opening was returned word for word.

**Counts:** 5 MUST-FIX, 4 SHOULD-FIX, 11 MINOR.

---

## MUST-FIX

### 1. Studholme's French Gray main bedroom is out of date (idea 1)
**Current (build.py):**
`Farrow &amp; Ball colour curator Joa Studholme painted her own main bedroom in French Gray, a soft green, to link it to the garden outside.`

**Problem:** The only source is SheerLuxe, dated **07 October 2021**. Its words are narration, not a quote from Studholme: "With its doors opening straight onto the garden, the master bedroom is painted in a restful green…" (truncated). Farrow & Ball's own page on the same Somerset house after its renovation (13 Feb 2025) lists a different colour: "Primary Bedroom … Walls and ceiling: Stirabout No.300 in Dead Flat". French Gray does not appear on that page. The sentence reads as current fact, but it is four years old. It is also unlinked.
- https://sheerluxe.com/home/farrow-ball%E2%80%99s-colour-expert-shows-us-round-her-home
- https://www.farrow-ball.com/the-chromologist/inside-our-colour-curators-newly-renovated-somerset-home ("When choosing to extend her Somerset schoolhouse, Joa Studholme, Farrow & Ball Colour Curator, had a big decision to make.")

**Replacement:**
`When SheerLuxe toured her Somerset home in 2021, Farrow &amp; Ball colour curator Joa Studholme's garden-facing main bedroom was painted in French Gray, {SR('sheer','a restful green')}.`

### 2. Light Blue: wrongly attributed to Studholme, and out of date (idea 3)
**Current:**
`Pale blues shift with the light: Studholme says Farrow &amp; Ball Light Blue in her triple-aspect spare bedroom is {SR('sheer','positively blue in strong morning light')} and greyer later.`

**Problem:** First, this is not Studholme's quote. SheerLuxe is written in the third person by a journalist. The line is the writer's narration, with no quotation marks and no "she says": "…it's positively blue in strong morning light but becomes greyer as the evening progresses." Second, the house has since been renovated. The guest bedroom is now "Walls: Inchyra Blue No.289 in Dead Flat | Upper walls and ceiling: Light Blue No.22 in Dead Flat" (F&B, 13 Feb 2025). The present tense "is" is therefore wrong.

**Replacement:**
`Pale blues shift with the light: when SheerLuxe visited Studholme's home in 2021, it found Farrow &amp; Ball Light Blue in her triple-aspect second bedroom was {SR('sheer','positively blue in strong morning light')} but greyer by evening.`

Add to SRC: `"joa25":"https://www.farrow-ball.com/the-chromologist/inside-our-colour-curators-newly-renovated-somerset-home"` (needed for items 3 and 4).

### 3. Setting Plaster is no longer in her third bedroom (idea 5)
**Current:**
`His pick, Farrow &amp; Ball Setting Plaster, is one Studholme uses in her own small third bedroom.`

**Problem:** SheerLuxe (2021) says the third and smallest bedroom was "embraced by Setting Plaster". After the 2025 renovation, Farrow & Ball lists Setting Plaster only in the hallway: "Walls: Setting Plaster No.231 in Dead Flat". None of the three bedrooms now uses it. The present tense "uses" is wrong.

**Replacement (pick one):**
`His pick, Farrow &amp; Ball Setting Plaster, was the colour of Studholme's small third bedroom when SheerLuxe visited in 2021.`
or
`His pick, Farrow &amp; Ball Setting Plaster, is one Studholme uses at home, on the {SR('joa25','hallway')} walls of her renovated Somerset house.`

### 4. "One colour per bedroom" is no longer true of her home (idea 13)
**Current:**
`Studholme uses one colour per bedroom at home because most of them are so small.`

**Problem:** This is SheerLuxe narration from 2021: "Each bedroom uses only one colour, because most of them are so small." The 2025 F&B page shows that two of her three bedrooms now use two colours each. The guest bedroom has Inchyra Blue walls with Light Blue upper walls and ceiling. The Sap Green bedroom has "Walls and woodwork: Sap Green No.199 in Dead Flat | Ceiling: Pink Cup No.9801 in Dead Flat". Only the primary bedroom is a single colour: "Walls and ceiling: Stirabout No.300 in Dead Flat".

**Replacement:**
`In her renovated Somerset home, Studholme takes Farrow &amp; Ball Stirabout over the walls and ceiling of the main bedroom, and Sap Green over the {SR('joa25','walls and woodwork')} of another.`

### 5. Divine Damson is out of date and is a red, not a plum (idea 9)
**Current:**
`Graham &amp; Brown's 2026 colour, Divine Damson, sits in the same family.`

**Problem:** (a) Ideal Home describes Divine Damson as a red: "a rich and juicy red" and "a dark cherry red", with "hints of mulberry and garnet". It does not call it purple or plum, and the article never links it to bedrooms (https://www.idealhome.co.uk/all-rooms/graham-brown-colour-of-the-year-2026-divine-damson, 17 Sep 2025). (b) By 25 Jan 2027 it is last year's pick. Ideal Home, 3 Sep 2026: "Last night, Graham & Brown revealed Rose Earth as its colour of the year for 2027", described as "a warm, earthy pink shade with subtle brown undertones". H&G's 2027 round-up (22 Sep 2026) also confirms Graham & Brown "Rose Earth".
- https://www.idealhome.co.uk/all-rooms/graham-and-brown-colour-of-the-year-2027-rose-earth
- https://www.homesandgardens.com/decor/paint/colors-of-the-year-2027

**Replacement:** delete the sentence from idea 9, and add this to the end of the idea 5 (Plaster Pink) paragraph:
` Graham &amp; Brown's Colour of the Year 2027, Rose Earth, is {SR('gb27','a warm, earthy pink shade with subtle brown undertones')}.`
Add to SRC: `"gb27":"https://www.idealhome.co.uk/all-rooms/graham-and-brown-colour-of-the-year-2027-rose-earth"`

---

## SHOULD-FIX

### 6. China Clay and Rolling Fog are not suggested "for a bedroom" (idea 6)
**Current:**
`For a bedroom she suggests the pink-tinged Little Greene China Clay or Rolling Fog – Pale.`

**Problem:** Livingetc (8 Nov 2022, a **Sponsored** piece) says: "A tinge of pink can also make whites feel warmer, creating an inviting atmosphere," Ruth adds. "China Clay and Rolling Fog – Pale are great options here." There is no bedroom context, and neither colour is called "pink-tinged" directly.
https://www.livingetc.com/advice/little-greene-choosing-perfect-white

**Replacement:**
`She adds that {SR('livw','a tinge of pink can also make whites feel warmer')}, naming Little Greene China Clay and Rolling Fog – Pale.`

### 7. Charlotte Cosby's title (idea 5)
**Current:**
`Charlotte Cosby, Farrow &amp; Ball's creative director, calls it`

**Problem:** The Livingetc page does say "creative director at Farrow & Ball". Two other pages give her title as Head of Creative:
- Homes & Gardens: "Charlotte Cosby, Head of Creative at Farrow & Ball" (https://homesandgardens.com/interior-design/paint/estate-emulsion-vs-modern-emulsion)
- Tala: "Head of Creative at colour experts Farrow & Ball" (https://tala.co.uk/blogs/journal/at-work-with-charlotte-cosby-farrow-ball)

**Replacement:**
`Charlotte Cosby, Farrow &amp; Ball's head of creative, calls it`

### 8. Sleep surveys: no dates given (sleep section)
**Current:**
`a Travelodge survey of 2,000 British homes found {SR('travel','58% of Britons with a blue wall colour reported waking up feeling happy')}, and Rest Assured's research put soft green as the most restful.`

**Problem:** The Travelodge page has no date. Its full sentence is "In fact, 58% of Britons with a blue wall colour reported waking up feeling happy and refreshed." Ideal Home reported the same study on 21 Feb 2017: "The study of 2,000 British homes for Travelodge hotels…" (https://www.idealhome.co.uk/news/paint-your-bedroom-blue-to-sleep-better-42905). The Rest Assured research is from 27 Feb 2019 ("Soft green topped the poll as the most restful and relaxing colour") and gives no sample size. Readers should know these are 8 to 10-year-old PR polls. The page's framing ("There is no proven sleep colour… Treat them as opinion polls") is good and should stay.

**Replacement:**
`an undated Travelodge survey of 2,000 British homes (reported in 2017) found {SR('travel','58% of Britons with a blue wall colour reported waking up feeling happy')}, and Rest Assured's 2019 research put soft green as the most restful.`

### 9. Mellow Flow quote is Ideal Home's wording, and "2026 colour" needs context for a 2027 reader (idea 3)
**Current:**
`Farrow &amp; Ball Lulworth Blue No. 89 and Dulux's 2026 colour Mellow Flow, {SR('rhythm','the perfect muted blue that calms and soothes')}, are softer options.`

**Problem:** "It's light and soft, the perfect muted blue that calms and soothes." is the Ideal Home writer's own description, not Dulux's (https://www.idealhome.co.uk/all-rooms/rhythm-of-blues-dulux-colours-of-the-year-2026, 9 Sep 2025). Mellow Flow was one of three 2026 colours (Mellow Flow, Free Groove, Slow Swing). By January 2027, Dulux's current colour is Soulful Sage.

**Replacement:**
`Farrow &amp; Ball Lulworth Blue No. 89 and Mellow Flow, one of Dulux's three 2026 Colours of the Year, which Ideal Home calls {SR('rhythm','the perfect muted blue that calms and soothes')}, are softer options.`

---

## MINOR

### 10. Diagram: east-facing light is not described as "warm" in the sources (svg.py)
**Current:** `["Bright, warm light in the","morning, cooler after midday"]`

Farrow & Ball says east-facing rooms enjoy "the most sun in the morning and cooler, muted light in the evening" (https://www.farrow-ball.com/ie/how-to-guide/how-light-affects-colour). Dulux Heritage says "natural light spills in during the morning… the room will feel cooler in the evenings." Neither says warm, and neither says midday.

**Replacement:** `["Most sun in the morning, then","cooler, muted light later"]`

The west card ("Cooler mornings, then warm golden light in the evening") and the south card are supported. F&B: "Light in west facing spaces is cooler in the morning and brighter in the afternoon"; "south facing rooms can be filled with warm light from dawn until dusk". Dulux Heritage: "Your room will feel cooler in the morning and brighter in the evening".

### 11. Mouse's Back is "topping the charts", not "among the risers" (idea 7)
**Current:** `with Wimborne White its best seller and Mouse's Back among the risers.`

Ideal Home: Mouse's Back "is another brown shade that's topping the charts at the moment". The "significant rise" refers to browns in general.

**Replacement:** `with Wimborne White its best seller and the brown Mouse's Back also topping the charts.`

### 12. Red Earth quote is about a living room (idea 8)
**Current:** `{SR('livn','the perfect shade for embracing a warmer color palette')} in a north-facing room.`

Source: "Red Earth is the perfect shade for embracing a warmer color palette in a north-facing living room".

**Replacement:** `{SR('livn','the perfect shade for embracing a warmer color palette')} in a north-facing living room, and the same logic applies to a bedroom.`

### 13. Karen Haller's description (idea 12)
**Current:** `Colour psychologist Karen Haller, working with bed maker Rest Assured, told Ideal Home to {SR('rest','avoid yellow in the bedroom')}.`

Ideal Home calls her only "the UK's leading colour expert". It reports research Rest Assured "conducted … alongside" her, so she did not necessarily speak to Ideal Home herself.

**Replacement:** `Colour expert Karen Haller, who worked with bed maker Rest Assured on its 2019 research, says to {SR('rest','avoid yellow in the bedroom')}.`

### 14. Farrow & Ball sampling link goes to the Irish site
**Current:** `"fbs":"https://www.farrow-ball.com/ie/how-to-guide/how-to-sample",`

The UK page has the same wording: "Apply two coats of your sample onto thick paper or card — the bigger the better — and let it dry." and "Check your samples over the course of a day or two to see how the colour looks in different lights."

**Replacement:** add `"fbsuk":"https://www.farrow-ball.com/how-to-guide/how-to-sample"` and change both `SR('fbs',` calls to `SR('fbsuk',`. Changing the URL on the existing `fbs` key does the same job.

### 15. Crown and Brinjal links go to Irish pages
`crown` (https://www.crownpaints.com/ie/inspiration-bedroom) is titled "IE Inspiration - Bedroom". `brinjal` is on farrow-ball.com/ie/. All quotes on both pages check out, but I could not find a UK equivalent of either. Leave as is, or mention in an editor's note that UK stock and prices may differ.

### 16. Paint arithmetic: "roughly the walls" overstates the match
**Current:** `So a 5-litre tin gives two coats on up to about 35 m², roughly the walls of a 3.5 m square bedroom with a 2.4 m ceiling once the door and window are taken off.`

The maths: 5 L × 14 m²/L = 70 m² for one coat, so 35 m² for two coats. That is correct, but it is a best case ("Up to 14m2/litre", https://dulux.co.uk/en/products/dulux-matt). The walls come to 4 × 3.5 × 2.4 = 33.6 m². Taking off a standard door (about 0.76 × 1.98 m) and a 1.2 × 1.2 m window leaves about 30.7 m². So the walls are about 31 m², not 35.

**Replacement:** `So a 5-litre tin gives two coats on up to about 35 m² at best-case coverage, enough for the roughly 31 m² of wall in a 3.5 m square bedroom with a 2.4 m ceiling once a door and window are taken off.`

### 17. "Matt … hides uneven walls" has no source
**Current:** `Matt or flat emulsion hides uneven walls.`

The linked Ideal Home finish article doesn't say this. Its only point on hiding marks is about satin ("a satin finish can help to disguise those knocks and scrapes a bit better"). The claim is common trade knowledge, so a softer wording is enough.

**Replacement:** `Matt or flat emulsion is more forgiving of uneven walls than a sheen finish.`

### 18. Paint Shed tip is unlinked
**Current:** `The Paint Shed suggests A5 or bigger and moving the card around the room.`

The `pshed` key is defined but unused. Source: "painting your sample colour onto paper, ideally A5 or bigger" and "position the sample around the room at various times of the day".

**Replacement:** `The Paint Shed suggests {SR('pshed','ideally A5 or bigger')} and moving the card around the room.`

### 19. Unused SRC keys
`dbed`, `sleepch` and `lg26` are defined but never used (`pshed` too, see item 18). This is harmless, but remove them or use them.

### 20. Lavender Garden "if a dark purple feels too much" is the writer's own framing
Mylands does not present Lavender Garden No. 30 as a paler alternative. The page simply lists it first and calls it "a grey-lilac colour" that "makes a wonderfully serene ambience in a bedroom". This is acceptable as editorial advice, and no change is needed. If you want it sourced, the replacement is:
`and the paler, grey-lilac Lavender Garden No. 30, which Mylands says {SR('myl','makes a wonderfully serene ambience in a bedroom')}.`

### Note on quote spellings
Bradley's and Cosby's quotes use US spellings ("colors", "color palette") because the source pages are written in US English. They are verbatim, so keep them as they are.

---

## Verified OK

**Experts, quotes and titles**
- **Patrick O'Donnell** (H&G calls him "Brand Ambassador at Farrow & Ball"), all verbatim:
  - "Green is the most natural colour family for the bedroom due to the affinity with calm and restfulness."
  - "Pink is a colour for those poorly lit north-facing bedrooms."
  - Setting Plaster is his pick.
  - "a surprisingly successful option in a naturally poorly lit or small room", about Railings.
  - Lichen "for a relaxing bedroom across both walls and woodwork".
  - "Our ever-popular Hague Blue works a treat in north-facing rooms because of the underlying green note" (truncated).
- **Ruth Mottershead** (Creative Director, Little Greene):
  - "It is a calming and sophisticated shade of green with a very soothing effect" (Sage Green).
  - Royal Navy: "They create depth and intimacy…"
  - Baked Cherry: "creating that cosy, cocooning quality", and "particularly when used in an all-over scheme".
  - Bassoon: "help us feel uplifted, happy and energised".
  - Masquerade: "the perfect colour for bringing warmth", with "soft, warm tones" and a "gentle blush hue", listed under neutrals for bedrooms.
  - "Warm whites work particularly well in north-facing rooms" (truncated).
  - "Cool whites can work well in south-facing rooms where the light is warmer…"
  - Split Pink: "a wonderfully warm pink hue".
- **Tash Bradley** (H&G: "Director of Interior Design at Lick and color psychologist"):
  - "These tend to receive cooler, bluish light, which can make colors appear darker."
  - "LRV is measured on a scale from 0 to 100…"
  - "light needs to be present for the paint to reflect it."
  - "Lick's Pink 02 offers exactly what a bedroom should feel like - a space for you to switch off and truly wind down."
  - "take one colour and paint everything in that room in the same one colour"
  - "you don't notice the edges of the room."
- **Marianne Shillingford** (H&G: "Creative Director and Colour Expert at Dulux"): "…its soft, silvery quality brings a sense of lightness while retaining that reassuring connection to the natural world." Dulux Colour of the Year 2027 = Soulful Sage (H&G, 8 Sep 2026; also H&G's 2027 round-up).
- **Chelsea Clark** (head of marketing, Lust Home): "…dark, rich greens are a great choice to bring depth to a room". Dulux Everglade Forest is named by Ideal Home ("forest green like the Dulux Everglade Forest at B&Q").
- **Julia Baum** (Julia Baum Interiors) on Bancha: "It has a deep feel that creates a sense of calm in any space."
- **Lucy Steele** ("Valspar's paint & interiors expert"): "Blue is one of the colours most associated with calm".
- **Alice Bettington** (Golden Interior Design): "Darker blues are a wonderful choice for bedrooms as they evoke the night sky."
- **Andy Greenall** (Head of Design, Paint & Paper Library): "Black helps to create a calm, intimate ambience".
- **Katie Miller** (Baile Interiors): "…always looks different throughout the day." (Shaded White)
- **Adam Knight** (Nefarious Design): Oxford Stone, "promoting rest, comfort, and calm".
- **Charlotte Cosby** on Setting Plaster: "perfect for enveloping north-facing spaces". (Her title is item 7.)
- **James Sirett** (head of product, Fired Earth): "Terracotta has a reassuring earthiness…"
- **Annie Sloan**: "Avoid a deep shade in a darker north-facing room; the nuances will be lost and it could look a little muddy."
- **Lizzie Green** (interior designer): "…hugely effective in making a space feel bigger", about colour drenching in a small room.
- **60-30-10 rule, all three quotes:**
  - Ben Thomson (Manager, Promain): "allocating 60% of a room's colour to the dominant hue"
  - Sarah Lloyd (Interiors & Paint Specialist, Valspar): "soft furnishings such as throws, pillows, artwork and accessories", about the 10% accent
  - Emma Deterding (Kelling Designs): "There are no hard and fast rules"
- **Claire Garner** (director, Claire Garner Design Studio): "My go-to paint finish for walls and ceilings is always matt".
- **Joa Studholme's title**, "colour curator", is correct.

**Paint colours and numbers**
- Crown descriptions are verbatim:
  - Mellow Sage: "A restorative pale sage green paint"
  - Woodland Wanderer: "A rich, deep and calming green"
  - Fresh Coconut: "A delicate neutral, warm off white"
  - Midnight Navy: "A luxurious, dark navy blue paint"
- Lulworth Blue **No. 89**: Ideal Home lists "Farrow & Ball Estate Lulworth Blue No.89" and says it is "the perfect blue shade for a bedroom".
- Dulux **Nordic Sky** is in the south-facing "Colours to try" list. Dulux recommends "warmer shades like pink, gold and yellow tones" for north-facing rooms and "cool shades such as blue, green and violet" for south-facing ones. Its line "The natural light a room receives has a huge effect on colour." is verbatim.
- Dulux Heritage: "For east and west facing rooms, it's all about the time of day and when you'll be using the space."
- Mellow Flow two-thirds example: the caption reads "A bedroom with two thirds of the walls painted in Dulux's Mellow Flow blue shade and the top in a neutral off-white".
- Farrow & Ball: "Warm, characterful colours are driving sales in 2026" (O'Donnell, Ideal Home, 25 May 2026). Wimborne White "has taken the top spot… overtaking All White".
- Brinjal **No. 222**: "In bedrooms, Brinjal feels dramatic yet grounding." It is a "wine-like tone" that "sits somewhere between purple and red".
- Mylands **Plum Tree No.283**: "As a bedroom wall colour, it's comforting and reassuring." The photo shows it "behind the bed". **Lavender Garden No.30** is "a grey-lilac colour".

**Paint finishes, coverage and safety**
- Estate Emulsion "just 2 per cent" sheen and "wipeable but not washable". Modern Emulsion is "7 per cent", and Cosby calls it "washable, scuff-proof".
- Dulux Matt "Up to 14m2/litre", 2 coats, sold in 5 L tins. The 35 m² arithmetic is correct (see item 16 for the wall area).
- NetRegs: interior matt walls and ceilings (gloss ≤25 at 60°) are limited to 30 g/l "when the product is ready to use", under the VOC in Paints… Regulations 2012.
- HSE: "If indoors open doors and windows." The page is aimed at construction work, but the advice applies at home too.
- Farrow & Ball sampling: two coats on card, "the bigger the better", "Check your samples over the course of a day or two", and close the curtains and turn on a lamp for rooms used in the evening.

**Sleep and light**
- Travelodge: 2,000 British homes, 58%. Rest Assured: soft green was "most restful". (Dates are item 8.)
- NHS 111 Wales: "make sure your bedroom is dark and quiet - use thick curtains…"; "do not watch television or use devices… right before going to bed"; "the bright light makes you more awake". The page says nothing about wall colour, so "There is no proven sleep colour" is a fair summary.
- Diagram: the north card ("cool, bluish light… colours look darker"), the south card ("warm, bright light most of the day"), the west card, the LRV 0 to 100 scale and the 60-30-10 split all match their sources.
