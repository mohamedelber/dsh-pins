# Fact-check: "Dresser vs Chest of Drawers" (publishes 11 Jan 2027)

Checked 26 Oct 2026 against live pages. Every source was surfaced with WebSearch and then fetched with WebFetch. Quotes below are verbatim as the fetch returned them. Strings marked "Current" are copied exactly from `build.py` (line numbers given) or `svg.py`.

Totals: **3 MUST-FIX, 5 SHOULD-FIX, 13 MINOR.**

---

## MUST-FIX

### M1. "Same price" is false: the STORKLINTA pair compares a white dresser with a dark-brown chest

The wide link (`skw`) is the **white** unit and the tall link (`skt`) is the **dark-brown/oak effect** unit. When you compare the same colour, the tall chest is always cheaper:

| Colour | Wide 55 1/8 x 18 7/8 x 29 1/2 | Tall 27 1/2 x 18 7/8 x 47 1/4 |
|---|---|---|
| White | $249.99 (https://www.ikea.com/us/en/p/-60561248) | **$229.99** (https://www.ikea.com/us/en/p/-10559281/) |
| Dark-brown/oak effect | $279.99 (https://www.ikea.com/us/en/p/-50561244/) | $249.99 (https://www.ikea.com/us/en/p/storklinta-6-drawer-dresser-dark-brown-oak-effect-anchor-unlock-function-70559278/) |
| Oak effect | $279.99 (https://www.ikea.com/us/en/p/-00561246/) | $249.99 (https://www.ikea.com/us/en/p/storklinta-6-drawer-dresser-oak-effect-anchor-unlock-function-50559279/) |

Evidence: the white tall page gives the title "STORKLINTA 6-drawer dresser, white/anchor/unlock function, 27 1/2x18 7/8x47 1/4 "", the price "$229.99" and "Storage capacity6.8 cu.ft". The category page (https://www.ikea.com/us/en/cat/dressers-storage-drawers-st004/) agrees: "STORKLINTA 6-drawer dresser, white/anchor/unlock function, 27 1/2x18 7/8x47 1/4 "" - $229.99.

Recommended fix: change `SRC['skt']` to the white tall page so both links are white, then state the real prices. The chest also comes out cheaper, which matches the FÅGELFJÄLLET pair.

- **SRC (build.py line 16).** Current: `"skt":"https://www.ikea.com/us/en/p/storklinta-6-drawer-dresser-dark-brown-oak-effect-anchor-unlock-function-70559278/",`
  Replace: `"skt":"https://www.ikea.com/us/en/p/-10559281/",`
- **build.py line 36.** Current: `In a matched IKEA pair with the same six drawers and the same price, the tall chest uses half the floor for about 81% of the storage.`
  Replace: `In a matched IKEA pair with six drawers each, the tall chest uses half the floor for about 81% of the storage, and costs $20 less.`
- **build.py line 53.** Current: `Buying guides give ranges, so we compared two real products that differ only in shape.`
  Replace: `Buying guides give ranges, so we compared two real products from the same IKEA series, in the same white finish.`
- **build.py line 53.** Current: `and as a tall unit of 27 1/2 x 18 7/8 x 47 1/4 inches with {SR('skt','storage capacity 6.8 cu.ft')}. Both cost $249.99 and use the same 24 x 15 3/4 inch drawers.`
  Replace: `and as a tall unit of 27 1/2 x 18 7/8 x 47 1/4 inches with {SR('skt','storage capacity 6.8 cu.ft')}. The wide one costs $249.99 and the tall one $229.99. Both have six drawers with the same 24 x 15 3/4 inch inner footprint, but the tall unit's drawers are shallower from top to bottom.`
- **svg.py line 9.** Current: `IKEA STORKLINTA 6-drawer, wide and tall versions, same price, drawn to scale`
  Replace: `IKEA STORKLINTA 6-drawer in white, wide and tall versions, drawn to scale`
- **svg.py line 56.** Current: `('Tall chest (6 drawers)','3.6','6.8','1.89','$249.99',A)`
  Replace: `('Tall chest (6 drawers)','3.6','6.8','1.89','$229.99',A)`
- **svg.py line 3 (desc).** Current: `Two IKEA STORKLINTA 6-drawer units with the same drawers and price, drawn to scale.`
  Replace: `Two white IKEA STORKLINTA 6-drawer units, drawn to scale: the wide one costs $249.99 and the tall one $229.99.`

(If you would rather keep the dark-brown chest, link the dark-brown wide unit, https://www.ikea.com/us/en/p/-50561244/, at $279.99, and say the chest is $30 less. Either way the two links must be the same colour.)

Note: the white wide unit also shows "In-store only price: "$199.99"" with "Offer valid from Sep 8, 2026 until Dec 24, 2026". The offer ends before publication, so no change is needed, but recheck all prices in the week of publication.

### M2. "The same six drawers" contradicts the 81% figure

The drawers match only in inner width and depth ("Drawer width (inside) 24"" and "Drawer depth (inside) 15 3/4"" on both pages). They are not the same drawers. If they were, both units would hold the same volume. IKEA lists "Storage capacity 8.4 cu.ft" for the wide unit and "Storage capacity6.8 cu.ft" for the tall one. That works out to 1.40 cu ft per drawer against 1.13, so the tall unit's drawers are about 19% shorter inside. A reader who notices "same drawers" next to "81% of the storage" will see the conflict.

- **build.py line 52 (diagram caption).** Current: `The same six drawers as a wide dresser and a tall chest: the chest takes half the floor and gives 81% of the storage.`
  Replace: `Six drawers as a wide dresser and as a tall chest: the chest takes half the floor and gives 81% of the storage.`
- **build.py line 51 (H2).** Current: `Same Drawers, Different Shape: The Floor-Space Math`
  Replace: `Six Drawers, Two Shapes: The Floor-Space Math`
- **svg.py line 8.** Current: `Dresser vs Chest: Same Drawers, Different Shape`
  Replace: `Dresser vs Chest: Six Drawers, Two Shapes`
- **svg.py line 6 (title element).** Current: `Dresser vs chest of drawers: same drawers, different shape`
  Replace: `Dresser vs chest of drawers: six drawers, two shapes`
- **build.py line 36.** Already fixed in M1 ("with six drawers each").
- **build.py line 53.** Already fixed in M1 ("the same 24 x 15 3/4 inch inner footprint, but the tall unit's drawers are shallower").

### M3. STURDY applies to units *manufactured* after 1 Sept 2023, not to units *sold* since then

Evidence (https://www.govinfo.gov/content/pkg/FR-2023-05-04/html/2023-08997.htm): "All clothing storage units that are manufactured after September 1, 2023, are subject to the requirements of this part." Intertek (https://www.intertek.com/products-retail/insight-bulletins/2023/sturdy-act-final-rule-published/) says the same: "All clothing storage units manufactured after September 1, 2023, will be subject to the requirements of this part." A unit made earlier could still be sold new after that date.

- **build.py line 74.** Current: `Since September 1, 2023, new clothing storage units sold in the US must meet a federal stability standard under the STURDY Act.`
  Replace: `Clothing storage units manufactured after September 1, 2023 must meet a federal stability standard under the STURDY Act.`

---

## SHOULD-FIX

### S1. The IKEA US price range covers only the first 24 of 158 items

The category page says "Showing 24 of 158 results" (https://www.ikea.com/us/en/cat/dressers-storage-drawers-st004/). Among those 24, the dresser prices do run from $69.99 ("RAST 3-drawer dresser, pine, 24 3/8x26 3/4 "") to $649.99 ("STOREMOLLA 8-drawer dresser, gray-brown stained, 67 3/8x19 5/8x35 7/8 ""). But 134 items were not checked, and the cheapest item shown was "JONAXEL Storage combination" at $49.99. The range is also unlinked, and the chest cell is empty. Below, a split by shape using the 24 items shown:

- Wide units: RAST 6-drawer $129.99 to STOREMOLLA $649.99.
- Tall single-stack units: STORKLINTA 5-drawer and 4-drawer $179.99 to HEMNES 6-drawer $399.99.

- **build.py line 48.** Current: `["IKEA US price range","$69.99–$649.99 across both types",""]]`
  Replace: `["IKEA US examples (Oct 2026)",f"{SR('ikcat','$129.99–$649.99')} for 6- to 8-drawer wide units","$179.99–$399.99 for 4- to 6-drawer tall units"]]`
  (Recheck these prices in the publication week; IKEA prices change often.)

### S2. Several table rows have no source, and Wayfair is credited but never linked

The cell-level attributions that exist are correct:
- Coleman (https://colemanfurniture.com/resources/buying-guides/dresser-dimensions-guide): "Typical dimensions for horizontal dressers are approximately 30–36 inches high, 50–70 inches wide, and 18–22 inches deep." and "Vertical dressers generally measure 40–60 inches high, 24–40 inches wide, and 16–22 inches deep".
- Lowe's (https://www.lowes.com/n/buying-guide/chest-of-drawers-vs-dresser): "The dimensions for a chest of drawers are usually between 44 and 60 inches tall and between 24 and 38 inches wide." and "Chests of drawers are taller, narrower structures that feature between four and six drawers."
- Wayfair (https://www.wayfair.ca/sca/ideas-and-advice/rooms/dresser-dimensions-how-to-choose-the-right-one-T1079): "A standard dresser typically has anywhere between six and nine drawers."

The problem: the width, depth and drawer rows are unattributed, and those rows mix sources. The chest depth (16–22) is from Coleman, the chest width (24–38) is from Lowe's, and the dresser drawer count (6–9) is from Wayfair. Wayfair's own figures differ: "A standard dresser ranges from 30" – 50" tall, 35" – 58" wide" and "A standard chest is taller (44" – 60") and narrower (30" – 40" wide)". Attribute each cell.

- **build.py line 43.** Current: `["Typical width","50–70 in","24–38 in"],`
  Replace: `["Typical width","50–70 in (Coleman)","24–38 in (Lowe's)"],`
- **build.py line 44.** Current: `["Depth","18–22 in","16–22 in"],`
  Replace: `["Depth","18–22 in (Coleman)","16–22 in (Coleman)"],`
- **build.py line 45.** Current: `["Drawers","6–9","4–6"],`
  Replace: `["Drawers",f"6–9 ({SR('wf','Wayfair')})","4–6 (Lowe's)"],`
- **build.py line 49.** Current: `Ranges come from Coleman Furniture, Lowe's and Wayfair buying guides. Real products sit at both ends, so measure the piece you are buying, not the category.`
  Replace: `Ranges come from the Coleman Furniture, Lowe's and Wayfair buying guides, which do not agree exactly (Wayfair, for example, gives chests as 30–40 in wide). Real products sit at both ends, so measure the piece you are buying, not the category.`

### S3. The clearance source is Wayfair Canada; a US source says the same thing

No US version of the Wayfair guide appeared in two searches; only wayfair.ca results came back (T1079 and T2617). The figure itself is right: "We recommend having 36" of clearance between the front of your dresser and your bed or other piece of furniture". But a US article is better served by Coleman, a US retailer, which says: "Leave at least 36 inches of clearance in front of a dresser to allow drawers to open fully and maintain walkable space." The SVG already credits "Wayfair and Coleman", so it needs no change.

- **build.py line 54.** Current: `Wayfair recommends {SR('wf','36\" of clearance')} in front of a dresser, which turns the STORKLINTA pair into about 21 and 10.5 square feet of floor in use.`
  Replace: `Coleman Furniture says to {SR('col','leave at least 36 inches of clearance in front of a dresser')}, and Wayfair gives the same figure. That turns the STORKLINTA pair into about 21 and 10.5 square feet of floor in use.`

### S4. The Real Homes role is wrong: Lamonaca is called a "design expert", not an interior designer

Evidence (https://www.realhomes.com/advice/where-to-put-a-dresser-in-a-small-bedroom): ""In my opinion, the best place for a dresser in a small bedroom is inside the closet," says Alessia Lamonaca, a design expert and the owner of New Mode Home. "… A low-profile dresser fits nicely in most closets directly underneath a clothing rod."" The quote and the name are confirmed. The role is not.

- **build.py line 83.** Current: `Real Homes quotes interior designer Alessia Lamonaca: {SR('rh','a low-profile dresser fits nicely in most closets directly underneath a clothing rod')}.`
  Replace: `Real Homes quotes Alessia Lamonaca, a design expert and the owner of New Mode Home: {SR('rh','a low-profile dresser fits nicely in most closets directly underneath a clothing rod')}.`

### S5. Highboy: Britannica describes a double chest (chest-on-chest), not "a tall chest on legs"

Britannica (https://www.britannica.com/topic/chest-of-drawers): "Double chests, or chest-on-chests, once known as tallboys in England and highboys in America, were also made." Merriam-Webster (https://www.merriam-webster.com/dictionary/Highboy) is the source for the legs: "a tall chest of drawers with a legged base." Calling the two "the same piece" merges two different descriptions.

- **build.py line 69.** Current: `A highboy is a tall chest on legs, the same piece Britannica says was {SR('brit','once known as tallboys in England and highboys in America')}.`
  Replace (no new key): `A highboy is a tall chest of drawers, usually on legs; Britannica notes that double chests, or chest-on-chests, were {SR('brit','once known as tallboys in England and highboys in America')}.`
  Alternative (adds `"mwh":"https://www.merriam-webster.com/dictionary/highboy"` to SRC): `Merriam-Webster defines a highboy as {SR('mwh','a tall chest of drawers with a legged base')}; Britannica notes that double chests, or chest-on-chests, were {SR('brit','once known as tallboys in England and highboys in America')}.`

---

## MINOR

### m1. The intro's parenthesis never closes
The rendered text reads "involved in 36 percent (79 out of 217 tip-over deaths it recorded from 2013 to mid-2023." The verbatim source is "tip-over fatalities involving a chest, bureau, or dresser make up 36 percent (79 out of 217 fatalities)" (https://www.cpsc.gov/s3fs-public/2023_Annual_Tip_Over_Report_Posted_2024Feb_FINAL_0.pdf).
- **build.py line 36.** Current: `the CPSC says a chest, bureau or dresser was involved in {SR('cpsc23','36 percent (79 out of 217')} tip-over deaths it recorded from 2013 to mid-2023.`
  Replace: `the CPSC says a chest, bureau or dresser was involved in {SR('cpsc23','79 out of 217')} tip-over deaths it recorded from 2013 to mid-2023 (36 percent).`

### m2. "Children" in the CPSC report means under 18
The report gives "Of the 217 tip-over fatalities, 155 (71 percent) were children," and defines them as "children (younger than 18 years of age)".
- **build.py line 73.** Current: `71% of the victims were children, and a chest, bureau or dresser was involved in 79 of them.`
  Replace: `71% of the victims were children under 18, and a chest, bureau or dresser was involved in 79 of the deaths.`
  (This also fixes the ambiguity in "79 of them": the 79 is out of all 217 deaths, not out of the child deaths.)

### m3. 20 + 36 inches is 4 ft 8 in, not "almost 5 feet"
56 in is 4.67 ft.
- **build.py line 60.** Current: `(a 20-inch-deep dresser plus 36 inches to open it needs almost 5 feet from the wall)`
  Replace: `(a 20-inch-deep dresser plus 36 inches to open it needs about 4 feet 8 inches from the wall)`

### m4. Katrina Hassan's title is not on the linked page
The linked Apartment Therapy page (https://www.apartmenttherapy.com/expert-hacks-organizing-dresser-drawers-36976577) introduces her only as "Katrina Hassan of Spark Joy London" and gives no job title. Her APDO listing (https://apdo.co.uk/member/katrina-hassan.html) does support the title: "Spark Joy London - KonMari Consultant & Professional Oragniser" [sic]. So the claim is true, but the source you link does not show it. Separately, the article's "jeans lower down" is not in the source, which says to "reserve the bottom drawers for items you put on last."
- **build.py line 90.** Current: `Professional organizer Katrina Hassan's rule, in Apartment Therapy: {SR('atd','fill the top drawers with items you put on first')}, so underwear and socks go up top and jeans lower down, which also keeps heavier things low.`
  Replace: `Katrina Hassan of Spark Joy London, a KonMari consultant and professional organizer, gives this rule in Apartment Therapy: {SR('atd','fill the top drawers with items you put on first')}, such as underwear and socks, and keep the bottom drawers for what you put on last. That usually puts heavier things low.`

### m5. The British "dresser" claim has no source, and the wording goes beyond Oxford's
Oxford (https://www.oxfordlearnersdictionaries.com/definition/english/dresser) gives, under British English: "a large piece of wooden furniture with shelves in the top part and cupboards below". Neither "open" nor "for plates" appears. Merriam-Webster's older sense is "a cupboard to hold dishes and cooking utensils". The `oxd` key is already in SRC but never used.
- **build.py line 69.** Current: `And a British \"dresser\" is something else again: a cupboard with open shelves on top for plates.`
  Replace: `And a British \"dresser\" is something else again: {SR('oxd','a large piece of wooden furniture with shelves in the top part and cupboards below')}, traditionally used for dishes.`

### m6. The anti-tip device requirement has no link
Intertek: "CSU furniture products must also include an anti-tip device that meets the requirements of ASTM F3096." The `itk` key is already in SRC but never used.
- **build.py line 74.** Current: `Covered units must pass stability tests and come with an anti-tip device.`
  Replace: `Covered units must pass stability tests and {SR('itk','must also include an anti-tip device')}.`

### m7. The SVG suggests height alone triggers the rule; the scope has three criteria
Intertek: "Units must meet ALL three of the above criteria to fall within the scope of the rule." Both units do meet all three: package weights are 73 lb 7 oz + 56 lb 14 oz (tall) and 78 lb 4 oz + 2 x 33 lb 5 oz (wide), and capacities are 6.8 and 8.4 cu ft. Only the reasoning needs fixing.
- **svg.py line 32.** Current: `Both are over 27 in tall: the federal tip-over standard applies. Anchor both.`
  Replace: `Both are over 27 in, 30 lb and 3.2 cu ft: the federal standard applies. Anchor both.`
- **svg.py line 3 (desc).** Current: `Both are taller than 27 inches, so the federal tip-over standard applies and both should be anchored to the wall.`
  Replace: `Both are taller than 27 inches, heavier than 30 pounds and hold more than 3.2 cubic feet, so the federal tip-over standard applies and both should be anchored to the wall.`

### m8. The FÅGELFJÄLLET pair also mixes colours
`fgw` links the off-white wide unit ($349.99). `fgt` links the black oak tall unit ($279.99). The off-white tall unit has the same specs and price: "FÅGELFJÄLLET 6-drawer dresser, off-white, 32 1/4x20 1/8x48 3/8 "", "$279.99", "7.6 cu.ft" (https://www.ikea.com/us/en/p/-70627994/). So "$70 less" holds within one colour, but the links should match.
- **SRC (build.py line 18).** Current: `"fgt":"https://www.ikea.com/us/en/p/fagelfjaellet-6-drawer-dresser-black-oak-effect-30611645/",`
  Replace: `"fgt":"https://www.ikea.com/us/en/p/-70627994/",`

### m9. Apartment Therapy says "dressers", not "chests and dressers"
Source: "Closets are usually about 24 inches deep, and dressers usually clock in at less than 20 inches deep." (https://www.apartmenttherapy.com/dresser-in-a-bedroom-closet-36988327)
- **build.py line 64.** Current: `{SR('atc','closets are usually about 24 inches deep')}, while most chests and dressers are under 20.`
  Replace: `{SR('atc','closets are usually about 24 inches deep')}, while dressers usually measure less than 20; both STORKLINTA units are 18 7/8.`

### m10. "Saving 10 square feet" counts the drawer-opening zone
The footprint saving is 3.6 sq ft (7.2 − 3.6). The 10.5 sq ft saving includes the 36 in clear zone, which is usually also the walkway. The reader should know which figure this is.
- **build.py line 81.** Current: `in a room like that, saving 10 square feet of floor matters.`
  Replace: `in a room like that, saving about 10 square feet of floor, counting the space to open the drawers, matters.`

### m11. "The tallest chests reach 60 inches" overstates the guides
The guides give 60 in as the top of the *typical* range (Lowe's "between 44 and 60 inches tall"; Coleman "40–60 inches high"). They do not say no chest is taller.
- **build.py line 66.** Current: `The tallest chests reach 60 inches.`
  Replace: `Typical chests reach up to 60 inches.`

### m12. IKEA uses "chest of drawers" for the wide unit as well
The claim about the tall unit is accurate. Its title is "STORKLINTA 6-drawer dresser, … 27 1/2x18 7/8x47 1/4 "", and its description says "The chest of drawers comes with Anchor and Unlock…". But the wide unit's page uses exactly the same sentence: "The chest of drawers comes with Anchor and Unlock that helps to reduce the tip-over risk…". The stronger point is that IKEA uses both words for both shapes. This is optional.
- **build.py line 69.** Current: `IKEA US calls its 47-inch-tall single-column STORKLINTA a \"dresser\" in the title and a \"chest of drawers\" in the description, so go by the measurements.`
  Replace: `IKEA US titles both STORKLINTA 6-drawer units, the wide one and the 47-inch-tall single column, \"dresser\", yet its product copy calls each one a \"chest of drawers\", so go by the measurements.`

### m13. The IRC source is a secondary training site
buildingcodetrainer.com quotes the 2021 IRC correctly: "Habitable rooms shall have a floor area of not less than 70 square feet" (R304.1) and "Habitable rooms shall be not less than 7 feet in any horizontal dimension" (R304.2). It also notes kitchens are exempt. The claim is fine. If you want a primary source, link the ICC code text instead (I did not fetch it). No text change is needed.

---

## Verified OK

**Arithmetic**
- STORKLINTA footprints: 55 1/8 x 18 7/8 = 7.23 sq ft; 27 1/2 x 18 7/8 = 3.60 sq ft. So "7.2" and "3.6" are correct.
- Storage per sq ft: 8.4 / 7.226 = 1.16; 6.8 / 3.605 = 1.89.
- "Half the floor, 81% of the storage": 3.605 / 7.226 = 49.9% of the floor; 6.8 / 8.4 = 80.95%.
- FÅGELFJÄLLET: 32 1/4 x 20 1/8 against 63 x 20 1/8 is 51.2% of the floor. 7.6 / 9.1 = 83.5%, which rounds to 84%. $349.99 − $279.99 = $70.00.
- With 36 in of clearance: 55.125 x 54.875 / 144 = 21.0 sq ft; 27.5 x 54.875 / 144 = 10.48, so "10.5" is correct.

**IKEA specs (live US pages)**
- STORKLINTA 6-drawer wide (white): "55 1/8x18 7/8x29 1/2", "Storage capacity 8.4 cu.ft", inner drawer 24 x 15 3/4, pull-out 10 7/8, $249.99.
- STORKLINTA 6-drawer tall: 27 1/2 x 18 7/8 x 47 1/4, "Storage capacity6.8 cu.ft", inner drawer 24 x 15 3/4. Prices: $249.99 in dark brown, $229.99 in white (see M1).
- FÅGELFJÄLLET 6-drawer wide (off-white): "63x20 1/8x30 3/4", "Storage capacity 9.1 cu.ft", $349.99.
- FÅGELFJÄLLET 6-drawer tall: "32 1/4x20 1/8x48 3/8", "Storage capacity7.6 cu.ft", $279.99 (black oak and off-white).
- STORKLINTA 5-drawer: "15 3/4x18 7/8x47 1/4" on the category page.
- IKEA titles the tall STORKLINTA a "dresser" and its description calls it a "chest of drawers" (but see m12).
- The SVG draws the wide unit as 2 columns x 3 rows and the tall unit as 1 x 6. That matches 24 in drawers in a 55 1/8 in and a 27 1/2 in carcass.

**Definitions**
- Merriam-Webster sense 3 of dresser: "a chest of drawers or bureau with a mirror".
- Oxford, bureau: "(British English) a desk with drawers and usually a top that opens down…" and "(North American English) = chest of drawers".
- Oxford, tallboy: British English, with the North American equivalent given as highboy.
- Dictionary.com, lowboy (U.S. furniture sense): "a low chest of drawers on short legs, resembling the lower part of a highboy".
- Britannica's quote "once known as tallboys in England and highboys in America" is verbatim (but see S5 on how it is used).
- Ashley: "organized horizontally into two or three columns".

**Lowe's**
- "a dresser will help create the illusion of a larger room" (the sentence opens "In a smaller bedroom with lower ceilings").
- "Have a taller, slimmer construction that's perfect for corners and small rooms".
- "between 44 and 60 inches tall and between 24 and 38 inches wide".
- Chests have "between four and six drawers".

**Comparison table**
- Height 30–36 (Coleman) and 44–60 (Lowe's) are correctly attributed.
- The width, depth and drawer values match Coleman, Lowe's and Wayfair (see S2 for attribution).

**Space planning**
- Apartment Therapy: "Closets are usually about 24 inches deep".
- IRC, via buildingcodetrainer: 70 sq ft and 7 ft (2021 IRC R304.1/R304.2).

**CPSC figures**
- 2023 report: "Between January 1, 2013 and July 31, 2023 … 217 reports of product instability or tip-over-related fatalities"; "155 (71 percent) were children"; "36 percent (79 out of 217 fatalities)".
- Feb 2024 release: "a child being treated in an emergency department (ED-treated) every 53 minutes". The CPSC's Super Bowl LX release (5 Feb 2026, https://cpsc.gov/Newsroom/News-Releases/2026/CPSC-Urges-Fans-Anchor-TVs-and-Furniture-Before-Super-Bowl-LX) repeats the same 217, 71%, 17,800 and 53-minute figures. No newer annual report was cited, so the data is still current.

**CPSC quotes (2022 release)**
- "Anchor TVs and furniture, such as bookcases and dressers, securely to the wall."
- "Most anti-tip-over kits cost less than $20 and can be installed in fewer than 20 minutes." This is a quote from Chair Hoehn-Saric.
- "Store heavier items on lower shelves, or in lower drawers."
- "Avoid displaying or storing items, such as toys and remotes, where kids may be tempted to climb" supports the "Keep toys and remotes off the top" bullet.

**STURDY rule (Federal Register)**
- Effective "September 1, 2023".
- Scope: "27 in. (686 mm) or greater in height", "30 lb (13.6 kg) or greater in mass", "3.2 ft³ (90.6 dm³) or greater of enclosed storage volume".
- Stability tests: a clothing-load test, a 10 lb horizontal force, and a carpet-tilt test with 60 lb on an open drawer.
- "Older furniture is not covered" is consistent with the rule's "manufactured after September 1, 2023".
- 16 CFR part 1261 is cited in the SVG footer.
- Both STORKLINTA units exceed all three scope thresholds.

**Other quotes**
- Consumer Reports: "Avoid placing TVs on dressers and chests because children may be tempted to climb on the drawers…" (James K. Willcox, updated Feb 24, 2025).
- AAP (healthychildren.org, © AAP): "a 2-inch (5 cm) guardrail around all four sides" and "Never leave a child unattended on a dressing table, even for a moment, even if he is strapped." Note that the AAP does not mention dresser toppers; "only with a proper changing topper" is the article's own advice, which is fine.
- Apartment Therapy drawer tips:
  - Sangita Evans is introduced as "professional organizer Sangita Evans of Clear and Hear". Her quote "eliminate layers and file your clothing instead" is verbatim.
  - Rashelle Isip is introduced as "Professional organizer and productivity consultant Rashelle Isip of The Order Expert". Her quote "creating at least three to four sections in an extra-wide drawer" is verbatim.
  - Katrina Hassan's quote "Fill the top drawers with items you put on first" is verbatim (see m4 on her title).
- Real Homes: the Lamonaca quote is verbatim (see S4 on her role).
