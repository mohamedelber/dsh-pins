# Fact-check: Small Dining Room Ideas (publishes 14 Jan 2027)

Checked 26 Oct 2026 against live pages. Every source was found with WebSearch and then read with WebFetch. WebFetch summarises pages, so I asked for verbatim sentences each time. Quotes below are what came back as exact text. Raw curl fetches are blocked by the proxy policy (403 on CONNECT), so I could not diff against raw HTML.

All replacement strings below were applied to a scratch copy of build.py/svg.py: each `old` string occurs exactly once, and `python3 svg.py && python3 build.py` runs cleanly afterwards. build.py and svg.py in the repo were not edited.

**Counts:** 2 MUST-FIX, 7 SHOULD-FIX, 12 MINOR.

---

## MUST-FIX

### M1. Table width: the diagram's 80 cm table for four contradicts its own planning table and the prose

- **Current (svg.py, line 45):** `("Table for four","120 cm long, at least 90 wide")`
- **Current (build.py, line 41):** `A narrow table, 80 cm rather than 90 cm, also works if you only ever sit on one side or at the ends.`
- **Problem:** The worked example in the same image is a 120 x 80 cm table with chairs on both long sides. The planning row next to it says a table for four must be "at least 90 wide", and the prose says 80 cm only works for one-sided seating. No source supports the one-side/ends claim. Oak Furnitureland (https://www.oakfurnitureland.co.uk/blog/your-dining-room-measurement-guide/) says only: "If you are working with a smaller space, bear in mind that your table should be no narrower than 90cm to allow for comfortable place settings." It gives no condition about seating on one side. The page "does not mention an 80 cm wide table" and "does not discuss one-sided seating". IKEA GB sells ÅLHULT at "120x80 cm" (£99) and "120/170x80 cm" (£149) (https://www.ikea.com/gb/en/cat/dining-tables-21825), so 80 cm is a normal width for four.
- **Replacement (svg.py):** `("Table for four","120 cm long, 80–90 cm wide")`
- **Replacement (build.py):** `An 80 cm wide table, like the one in our diagram, is a common size for four; go up to 90 cm if you want more room for place settings and serving dishes.`
- (Alternative: redraw the example at 120 x 90. That gives 270 x 240 cm, 270 x 205 cm with the banquette, still a 35 cm saving. It would also mean changing the caption, the line 35 prose and the "2.7 x 2.3 m" label.)

### M2. "Round Table on a Pedestal": both example products stand on legs, not a pedestal

- **Current (build.py, line 39):** `The John Lewis Iona, for example, is 100 cm across and {SR('jl','offers seating for up to 4 diners')}; IKEA's VIHALS round table is 107 cm and costs £59.`
- **Problem:** The heading and the Snowden quote recommend a central pedestal, and both "examples" are legged tables. On the John Lewis page (https://www.johnlewis.com/john-lewis-iona-4-seater-round-dining-table/oak/p3765224): "Splayed, rounded legs ensure a sturdy base." VIHALS round 107 cm uses a "VIHALS underframe, 74x74x73 cm" with "Leg/ Side rail: Steel" (IKEA product spec, https://mgmt.ikea.gr/en/products/vihals-table-107-cm/49589970/). The IKEA GB listing confirms "VIHALS table … 107 cm … £59" but gives no base type. The VIHALS £59 price is also unlinked.
- **Replacement:** `The John Lewis Iona, for example, is 100 cm across and {SR('jl','offers seating for up to 4 diners')}, and IKEA's VIHALS round table is 107 cm and costs {SR('ikt','£59')}. Both stand on legs rather than a pedestal, so check where the legs fall before you choose chairs.`
- (Or swap in a true pedestal product after checking its product page. The GB listing shows ROSENTORP extendable round, 110/155 cm, £349, captioned as pedestal, but I did not open its product page.)

---

## SHOULD-FIX

### S1. Oak Furnitureland's 90 cm rule is credited with a condition it does not state

- **Current (line 34):** `Oak Furnitureland says {SR('ofl','your table should be no narrower than 90cm')} if people sit on both sides.`
- **Problem:** The source sentence is "If you are working with a smaller space, bear in mind that your table should be no narrower than 90cm to allow for comfortable place settings." It does not mention "both sides". https://www.oakfurnitureland.co.uk/blog/your-dining-room-measurement-guide/
- **Replacement:** `Oak Furnitureland says that in a smaller space {SR('ofl','your table should be no narrower than 90cm')} to allow for comfortable place settings, though plenty of 120 cm tables, such as IKEA's ÅLHULT, are 80 cm wide.`

### S2. Banquette cost: £600–£1,200 is the source's price for an unupholstered bench

- **Current (line 51):** `A UK builders' guide puts a carpenter-built banquette at £600 to £1,200.`
- **Problem:** Bookabuilder lists "Carpenter built bench without upholstery, £600 to £1,200" and "Fully upholstered bespoke banquette, £1,200 to £3,000 depending on size and fabrics". The figure is also unlinked. https://www.bookabuilderuk.com/blog/small-dining-room-ideas
- **Replacement:** `A UK builders' guide puts a {SR('bab','carpenter built bench without upholstery')} at £600 to £1,200, and a fully upholstered bespoke banquette at £1,200 to £3,000.`

### S3. Dunelm Montreal bench has no source link

- **Current (line 55):** `Dunelm's Montreal two-seater bench, for example, has a seat 122 cm wide and 48 cm high.`
- **Evidence:** The figures are correct. The product page gives "Montreal 2 Seater Dining Bench, Faux Leather, 133cm", "Seat: H 48cm x W 122cm x D 45cm", "H 82cm x W 133cm x D 63cm", £249. https://www.dunelm.com/product/montreal-2-seater-dining-bench-faux-leather-133cm-1000189679
- **New key:** `"mon":"https://www.dunelm.com/product/montreal-2-seater-dining-bench-faux-leather-133cm-1000189679"`
- **Replacement:** `Dunelm's {SR('mon','Montreal 2 Seater Dining Bench')}, for example, has a seat 122 cm wide and 48 cm high (£249).`

### S4. Pendant spacing of 60–80 cm is unsourced, and Tala does not give it

- **Current (line 64):** `For a long table, use two smaller pendants about 60 to 80 cm apart.`
- **Problem:** Tala's page gives no spacing figure, only "longer tables benefit from two or more smaller pendants spaced evenly". The figure comes from the Bookabuilder lighting page: "Usually 600 mm to 800 mm between fittings works well." and "Measure between the centres of each pendant rather than between the outside edges." https://www.bookabuilderuk.com/blog/dining-room-lighting-ideas (key `babl` is defined in SRC but never used).
- **Replacement:** `For a long table, use two smaller pendants; a UK builders' guide says {SR('babl','600 mm to 800 mm between fittings works well')}, measured between the centres.`

### S5. The IKEA rug rule is unlinked, and the only source found is IKEA Switzerland

- **Current (line 66):** `and IKEA suggests 60 to 70 cm.`
- **Problem:** No link is given (key `ikrug` is unused). The source is IKEA Switzerland ("Choosing the right dining table rug - IKEA Switzerland"): "As a rule, the rug should preferably be larger than your dining table by 60-70 centimetres on both sides." https://www.ikea.com/ch/en/rooms/dining/how-to/how-to-choose-a-rug-for-your-dining-table-pub69273980/ . No IKEA GB version came up in searches. The same article ID shows up only for CH, AU and SG. I tried the GB path https://www.ikea.com/gb/en/rooms/dining/how-to/how-to-choose-a-rug-for-your-dining-table-pub69273980/ but the fetch was blocked (PROVENANCE_REQUIRED, permission not answered), so it is **unverified and should not be used**.
- **Replacement (link it):** `and IKEA's rug guide suggests {SR('ikrug','60-70 centimetres on both sides')}.`
- **Or (UK-only sourcing):** delete ` and IKEA suggests 60 to 70 cm` and rely on Oak Furnitureland, which is already cited in the same sentence.

### S6. London Housing Design Guide figure is from a 2010 interim edition but is presented as current

- **Current (line 70):** `Under the London Housing Design Guide, the {SR('ldg','minimum combined floor area of living, dining and kitchen spaces')} for a two-person home is just 23 m²`
- **Evidence:** The anchor matches the table header verbatim, apart from the capital M: "Minimum combined floor area of living, dining and kitchen spaces (sq m)". The figure is right: "2 person | 23" (also 3p 25, 4p 27, 5p 29, 6p 31). Standard 4.4.1 reads "The following combined floor areas for living / kitchen / dining space should be met:". The document is the *London Housing Design Guide, Interim Edition*, London Development Agency, August 2010. https://www.london.gov.uk/media/8395/download . "Under the…" implies a standard still in force. I did not confirm that later London guidance keeps it.
- **Replacement:** `The 2010 London Housing Design Guide set the {SR('ldg','minimum combined floor area of living, dining and kitchen spaces')} for a two-person home at just 23 m²`

### S7. "Wide carver chairs" and walk-behind figures are given without links

These are correct but unsourced in the prose. I've ranked them below S1–S6 because the figures are right.

- **Current (line 41):** `Wide carver chairs with arms need 10 to 15 cm more per person, so`
  - Source: "Wide carver chairs can add 100 to 150 millimetres per person." (Bookabuilder)
  - **Replacement:** `A UK builders' guide notes that {SR('bab','wide carver chairs can add 100 to 150 millimetres per person')}, so`
- **Current (line 34):** `If people need to walk behind a seated diner, allow about 100 to 110 cm.`
  - Source: "Where people need to pass behind seated diners, aim for around 1,000 to 1,100 millimetres." (Bookabuilder)
  - **Replacement:** `If people need to walk behind a seated diner, the builders' guide says to {SR('bab','aim for around 1,000 to 1,100 millimetres')}.`

---

## MINOR

### m1. YouGov: "usually" is not in the source, and there is a better UK-specific page
- **Current (line 70):** `a YouGov poll found that only {SR('yg','45%')} of Britons usually eat dinner at a dining table, against 42% who eat on the sofa or in an armchair.`
- The source says "Fewer than half of Britons (45%) say they eat their dinner at a dining table" and "Brits are by far the most likely to say they eat dinner on a sofa or armchair, with 42% saying so" (https://yougov.com/en-gb/articles/50383-…, 5 Sep 2024). The question wording is not published on the page. The UK-only companion article has the same figures: "fewer than half of Britons (45%) say they eat their dinner at a dining table" and "42% of the public saying they have dinner on the sofa or an armchair". https://yougov.com/en-gb/articles/50382-britons-are-as-likely-to-eat-dinner-on-the-sofa-as-they-are-at-a-dining-table
- **New key (optional):** `"yguk":"https://yougov.com/en-gb/articles/50382-britons-are-as-likely-to-eat-dinner-on-the-sofa-as-they-are-at-a-dining-table"`
- **Replacement:** `a YouGov poll found that only {SR('yguk','45%')} of Britons say they eat their dinner at a dining table, against 42% who have dinner on the sofa or an armchair.` (or keep `'yg'`, since both pages carry the figures)

### m2. Skills and Employment Survey sentence: "do so" has nothing to refer to
- **Current (line 72):** `The Skills and Employment Survey found that {SR('sur','a quarter of workers do so (27%) in spaces intended for other purposes')}, such as the kitchen or dining room, when they work from home.`
- The source is accurate. It reads "When working at home, a quarter of workers do so (27%) in spaces intended for other purposes such as the kitchen or dining room" (no comma before "such"). The figure is a share of people working at home, from the Skills and Employment Survey 2024 (n=5,469, released 2 Apr 2025). Lifted out of that sentence, "do so" refers to nothing. https://www.surrey.ac.uk/news/bringing-work-home-dining-room-tables-among-places-doubling-office-desks-half-workers
- **Replacement:** `The 2024 Skills and Employment Survey found that 27% of people who work from home do it in {SR('sur','spaces intended for other purposes such as the kitchen or dining room')}.`

### m3. Jamie Blake paraphrase: "normally need" should be "a minimum"
- **Current (line 51):** `you normally need about 90 cm behind chairs, but you can`
- Source: "allow about 90cm between a chair and the next piece of furniture or wall, minimum" (same sentence as the verified 30 cm quote). https://www.homesandgardens.com/ideas/banquette-seating-ideas
- **Replacement:** `you should allow about 90 cm between a chair and the wall as a minimum, but you can`

### m4. Christian Bense's "extra metre" is about an open-plan room
- **Current (line 51):** `Interior designer Christian Bense told SheerLuxe that a fixed banquette {SR('sl','effectively buys you an extra metre in the room')}.`
- Source context: "Building in a banquette seat and permanently fixing the location of the dining table in an open-plan room…" then "It effectively buys you an extra metre in the room, if not more…". https://sheerluxe.com/home/interior-design/experts-guide-banquette-seating (22 Oct 2025; "interior designer Christian Bense", no company named). The page doesn't label each answer with a speaker; his authorship comes from the standfirst.
- **Replacement:** `Interior designer Christian Bense told SheerLuxe that building in a banquette in an open-plan room {SR('sl','effectively buys you an extra metre in the room')}.`

### m5. La Redoute 90 cm is unlinked
- **Current (line 34):** `and La Redoute suggests 90 cm.`
- Source: "As a general guide, leave at least 90cm between the edge of the table and the nearest wall or piece of furniture." https://www.laredoute.co.uk/content/how-to-choose-the-right-dining-table-size-for-your-space/
- **Replacement:** `and La Redoute suggests {SR('lr','at least 90cm between the edge of the table and the nearest wall')}.`

### m6. The 80–120 cm in front of drawers is Oak Furnitureland's figure, not Bookabuilder's, and is unlinked
- **Current (line 60):** `Leave 80 to 120 cm in front of drawers so you can open them with the chairs in place.`
- Source: "When planning your layout, allow 80 to 120cm of space in front of drawers and dressers, so they can open comfortably…" The source doesn't mention chairs. Bookabuilder has no such figure.
- **Replacement:** `Oak Furnitureland says to {SR('ofl','allow 80 to 120cm of space in front of drawers and dressers')} so they can open comfortably.`

### m7. HAUGA £99 is unlinked
- **Current (line 46):** `The freestanding HAUGA drop-leaf goes from 55 to 109 cm long for £99,`
- IKEA GB listing: "HAUGA drop-leaf table … 55/82/109x74 cm … £99".
- **Replacement:** `The freestanding HAUGA drop-leaf goes from 55 to 109 cm long for {SR('ikt','£99')},`

### m8. Pendant height: svg says 70–90, prose says 75–90 (Tala)
- **Current (svg.py, line 46):** `("Pendant height","70–90 cm above the table top")`. The desc also has `pendant 70 to 90 cm above the table`.
- 70–90 is supported by Bookabuilder ("The bottom of a pendant is commonly positioned around 700 to 900 millimetres above the tabletop"). But Tala ("Dining table: 75–90cm above table surface"), Bookabuilder's lighting page ("roughly 750 mm to 900 mm") and Oak Furnitureland ("75 to 85cm") all start at 75. Optional harmonisation:
- **Replacement:** `("Pendant height","75–90 cm above the table top")` and `pendant 75 to 90 cm above the table`

### m9. Diagram footer credits Blakes London, but no figure in the diagram comes from Blakes
- **Current (svg.py, line 53):** `Blakes London via Homes &amp; Gardens. Check your own room and chairs before you buy.`
- The 40 cm table-to-wall figure on the banquette plan is the author's arithmetic (a 50 cm seat with a 10 cm overlap, based on Bookabuilder's "table overlap of around 75 to 100 millimetres" and "seat depth of 450 to 500 millimetres"). It is not Jamie Blake's 30 cm. This is harmless. Optional: `Homes &amp; Gardens. Check your own room and chairs before you buy.`

### m10. Clare Gaskin apostrophe
- The source uses a curly apostrophe: "We’re big fans of drawers, rather than lid-style lift up bench storage." build.py has `we\'re`. This is typographic only. Optional: `{SR('hgb','we’re big fans of drawers, rather than lid-style lift up bench storage')}`

### m11. Prices will be 11 weeks old at publication
- The prices are correct as of 26 Oct 2026: VIHALS round £59, ÅLHULT ext £149, VIHALS ext £99, NORBERG £39, HAUGA £99, Georgi £199, Montreal £249. BESTÅ is now £190 ("previously £235"), but the article gives no BESTÅ price. Iona is £374.25 and Clifford £321, neither quoted. The John Lewis and Dunelm pages showed no clear stock status. Re-check all prices before 14 Jan 2027.

### m12. Housekeeping
- These SRC keys are unused: `lth`, `ihm`, `ihs`, `ndss`. `babl` and `ikrug` become used if S4 and S5 are applied.
- The H&G banquette article is dated 21 May 2021 and shows no update date. The quotes are still live and correct.

---

## Verified OK (verbatim on the live page, right person and role)

**Ideal Home** (https://www.idealhome.co.uk/dining-room/small-dining-room-ideas-35006, updated 24 Oct 2025, Jennifer Ebert). The page capitalises the first word of each quote.
- Rebecca Snowden, interior style advisor, Furniture and Choice: "Round tables with a central pedestal are perfect due to their smaller footprint" ✔
- Rebecca Snowden: "Utilise wall space like installing floating shelves for added storage" ✔
- Adam Brown, director, The Painted Furniture Company: "…we think the flexibility of an extending table is crucial." ✔
- Kris Manalo, head of product, Atkin and Thyme: "Adding bench seating rather than chairs is a way to save space in a small dining room" ✔
- Magdalena Gierasinska, head of product and displays, Barker and Stonehouse: "A well-placed mirror can also work wonders to create the illusion of space." ✔
- Lucy Mather, interiors expert, Arighi Bianchi: "Light or neutral colours usually work best in a small room as they make the space feel larger" ✔

**Homes & Gardens**
- Jamie Blake, creative director, Blakes London: "reduce that down to as little as 30cm if the seat fits directly onto the wall" ✔ (banquette-seating-ideas)
- Clare Gaskin, interior designer (no company named): "We’re big fans of drawers, rather than lid-style lift up bench storage." ✔
- Amy Hicks, Lead Designer, Blakes London: "Placing a rug under the dining table helps to zone the dining area" ✔ (dining-room-layout-ideas)

**SheerLuxe:** Christian Bense, interior designer: "It effectively buys you an extra metre in the room, if not more…" ✔ (see m4 for context)

**IKEA GB** (https://www.ikea.com/gb/en/cat/dining-tables-21825 and product pages)
- "For that, it is estimated that each seat needs 60 centimetres in width." ✔ "…you need one that is at least 120 centimetres long." ✔
- VIHALS table, round, 107 cm, £59 ✔. ÅLHULT extendable 120/170x80 cm £149 ✔. VIHALS extendable 120/180x74 cm £99 ✔. HAUGA drop-leaf 55/82/109x74 cm £99 ✔
- NORBERG "Wall-mounted drop-leaf table, white, 74x60 cm", £39, "Seats 2." ✔
- BESTÅ combination "120x42x74 cm", depth 42 cm ✔

**John Lewis Iona:** "H75 x Dia.100cm", "This round dining table offers seating for up to 4 diners." ✔ (but legged, see M2)

**Dunelm**
- Clifford 2-4 Seater Drop Leaf: "H 78cm x W 41-152cm x D 90cm", "comfortably seats up to four people" ✔. The price (£321) is not stated in the article, which is fine.
- Montreal: seat "W 122cm", "H 48cm" ✔ (see S3)
- Georgi Slim 2 Door Sideboard: "H 90cm x W 82cm x D 30cm", £199 ✔

**Bookabuilder** (https://www.bookabuilderuk.com/blog/small-dining-room-ideas)
- "A clearance of 600 millimetres from the table edge to a wall is a tight minimum where a chair only needs to be pulled out." ✔
- "Allow at least 600 millimetres between the table edge and a wall for a chair, although 750 millimetres is more comfortable." ✔ (supports svg "60 tight, 75 comfortable")
- 1,000–1,100 mm to pass behind ✔. "A 900 to 1,000 millimetre diameter table normally seats four." ✔ "700 to 800 millimetres is better for two people" ✔
- "A finished seat height of about 450 millimetres works with a standard 750 millimetre dining table." ✔ Seat depth 450–500 mm ✔. 600 mm bench per adult ✔
- "Aim for units between 300 and 400 millimetres deep…" ✔. Pendant "700 to 900 millimetres above the tabletop" ✔ (svg)

**Oak Furnitureland:** "A minimum of 75cm of space around the dining table for seating and movement" ✔. "…no narrower than 90cm…" ✔ (see S1). "…ensure you leave at least 60cm on each side of the table…" ✔. The 80–120 cm drawers figure is OFL's ✔ (see m6)

**La Redoute:** 90 cm to wall ✔. Chart "120cm | 4 people", "180cm | 6 people" ✔

**Tala:** "Dining table: 75–90cm above table surface" ✔. "Pendant diameter should be about 1/2 to 2/3 the width of the table" ✔. Worked example: 1/2 to 2/3 of 80 cm = 40–53 cm, so "a 40 to 50 cm shade" ✔

**London Housing Design Guide:** anchor wording matches the table header. 2 person = 23 m² ✔ (see S6 on dating)

**YouGov:** 45% dining table, 42% sofa or armchair ✔ (see m1). **Skills and Employment Survey:** 27% ✔ (see m2)

**IKEA rug rule:** "larger than your dining table by 60-70 centimetres on both sides" ✔ on the IKEA Switzerland page. No GB page was found (see S5)

**Diagram arithmetic (svg.py)**
- Chairs round: (120 + 75 + 75) x (80 + 75 + 75) = 270 x 230 cm ✔, labelled "2.7 x 2.3 m" ✔, caption ✔, line 35 prose ✔
- Banquette: 50 cm seat − 10 cm overlap = table edge 40 cm from wall. Depth 40 + 80 + 75 = 195 cm, so 270 x 195 cm ✔, "2.7 x 1.95 m" ✔. Saving 230 − 195 = 35 cm ✔. A 10 cm overlap is at the top of Bookabuilder's 75–100 mm range, and a 50 cm seat is within its 450–500 mm range ✔
- These planning rows match their sources: per diner 60 cm (IKEA) ✔; round 70–80 = 2, 90–100 = 4 (Bookabuilder) ✔; table to wall 60 tight / 75 comfortable ✔; walk behind 100–110 ✔; banquette 45 high, 45–50 deep ✔; pendant width 1/2–2/3 (Tala) ✔; rug +60 cm each side (OFL) ✔; sideboard 30–40 (Bookabuilder) ✔, with "not 42+" referring to BESTÅ 42 cm ✔. The exceptions are "Table for four" (M1) and pendant height (m8).
