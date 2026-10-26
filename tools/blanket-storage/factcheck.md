# Fact-check: Blanket Storage Ideas (dailyspacehacks.com, publishes 21 Jan 2027)

- Checked: 26 Oct 2026, against live pages (WebSearch, then WebFetch). WebFetch summarises pages, so every quote below was requested verbatim. Where a page could not be fetched, this report says so.
- Scope: every claim, quote, attribution, product spec, price and figure in `build.py` and `svg.py`.
- Totals: **5 MUST-FIX, 4 SHOULD-FIX, 13 MINOR.**
- Testing: every replacement below was applied to a scratch copy. Each old string matched exactly once, and `svg.py` then `build.py` ran cleanly (27,368 bytes, 2,114 words, kw x3). Test script: `/tmp/claude-0/-home-claude/aa9f44c6-b1c7-520d-9978-96402d6712cc/scratchpad/fc_repl.py`.

## New SRC keys needed

Apply this edit to `build.py` once. It adds the keys used by M1, M2, S1 and S2.

Old:
```
SRC={"tgl"
```
New:
```
SRC={"cpsc14":"https://www.cpsc.gov/Newsroom/News-Releases/2014/CPSC-Warns-Consumers-of-the-Deadly-Dangers-of-Storage-and-Toy-Chests",
"cpsc18":"https://www.cpsc.gov/Newsroom/News-Releases/2018/CPSC-Urges-Consumers-to-Replace-or-Remove-Latches-Locks-on-Lane-and-Virginia-Maid-Cedar-Chests-14-Deaths-Reported",
"vt":"https://accomack.ext.vt.edu/content/dam/pubs_ext_vt_edu/3104/3104-1576/ENTO-471.pdf",
"bri":"https://www.target.com/p/-/A-94905415",
"tgl"
```

---

## MUST-FIX

### M1. The trunk "safety hinge" advice is misleading (build.py, idea 6)

Current:
```
If children use the room, choose a chest with a lid support or safety hinge that stops the lid slamming shut.
```

**Problem 1: the trunk we recommend has no lid support.** Readers will assume the trunk in the sentence before qualifies. It does not: its Target listing mentions no lid support, safety hinge or slow-close. The only lid line is "the hinged domed lid opens fully and stays open."
- Source: https://www.target.com/p/household-essentials-large-wooden-storage-trunk/-/A-93268477

**Problem 2: "safety hinge that stops the lid slamming shut" is not the CPSC guidance.** The CPSC asks for a lid support that holds the lid open in any position, and for ventilation holes. Its release does not mention hinges at all.
- Source: https://www.cpsc.gov/Newsroom/News-Releases/2014/CPSC-Warns-Consumers-of-the-Deadly-Dangers-of-Storage-and-Toy-Chests (March 5, 2014)
- "If the lid support does not keep the lid open in every position, you should remove the lid's support or replace it with a spring-loaded lid support that will keep the lid open in any position."
- "all toy chests should have ventilation holes that are not blocked by the floor or against the wall."

Replacement:
```
This listing does not mention a lid support. If children use the room, the CPSC advises {SR('cpsc14','a spring-loaded lid support that will keep the lid open in any position')} and says toy chests should have {SR('cpsc14','ventilation holes that are not blocked by the floor or against the wall')}.
```

### M2. The cedar chest idea leaves out a known suffocation hazard (build.py, idea 14)

The article recommends a "classic" cedar blanket chest. Many of these are hand-me-downs, and it says nothing about the auto-locking latches on Lane and Virginia Maid chests. CPSC reports 14 child deaths linked to those latches.
- Source: https://www.cpsc.gov/Newsroom/News-Releases/2018/CPSC-Urges-Consumers-to-Replace-or-Remove-Latches-Locks-on-Lane-and-Virginia-Maid-Cedar-Chests-14-Deaths-Reported (July 11, 2018)
- "Fourteen children have suffocated to death inside these cedar chests after becoming locked inside between 1977 and 2015."
- "The cedar chests were recalled because the chest's lid automatically locks when the lid is closed."
- "CPSC urges consumers to completely remove the locks from their recalled Lane and Virginia Maid brand chests to eliminate the hazard."
- "These chests are often handed down through families or purchased second-hand."

This replacement also softens "not protection" to "not full protection". UMD Extension says "Cedar chests, blocks, or closets also provide protection", and Pendleton says cedar "repel[s] moths, but don't fully protect against damage". See the cedar section of the OK list.

Current:
```
Treat cedar as a bonus, not protection, and only store blankets that are clean.
```
Replacement:
```
Treat cedar as a bonus, not full protection, and only store blankets that are clean. If you own an older Lane or Virginia Maid cedar chest, check the latch: the CPSC says on recalled chests the {SR('cpsc18','lid automatically locks when the lid is closed')}, and it urges owners to remove the locks completely.
```

### M3. Apartment Therapy's writer does not use the lid rack on a shelf (build.py, idea 5)

Current:
```
For a creative fix, Apartment Therapy's writer uses {SR('atlid','the $7.99 IKEA VARIERA Stainless Steel Lid Organizer')} on a shelf to hold folded throws upright, like files.
```

The word "shelf" does not appear in the article. The writer (Meg Hemphill, Sep 26, 2026) puts the rack on the floor, in a deep drawer, or outside by her fire pit.
- Source: https://www.apartmenttherapy.com/lid-organizer-for-blanket-storage-idea-37691981
- "You can display the organizer on the floor to show off your cozy collection or tuck it away inside a deep drawer if you prefer a cleaner look."
- "I fold bulkier fleece throws and slide them across two lid spaces, while thinner throws fit neatly into one."

The quote and the $7.99 price are correct, and IKEA US also shows the VARIERA pot lid organizer at $7.99 (https://www.ikea.com/us/en/p/70154800/).

Replacement:
```
For a creative fix, Apartment Therapy's writer uses {SR('atlid','the $7.99 IKEA VARIERA Stainless Steel Lid Organizer')} on the floor or inside a deep drawer to hold folded throws in separate slots, like files.
```

### M4. "Takes only a few inches of floor" is wrong for a leaning ladder (build.py, idea 2)

Current:
```
A ladder shows off throws and takes only a few inches of floor.
```

Yamazaki, the one ladder in the article that gives a footprint, says its base sits 10 to 15 inches out from the wall.
- Source: https://theyamazakihome.com/products/tower-leaning-ladder-rack (FAQ)
- "The bottom of the ladder can stand from about 10 in to 15 in from the wall."

Replacement:
```
A ladder shows off throws on a small footprint, but a leaning one still sits out from the wall.
```

Companion edit, also tested. Current:
```
and Yamazaki's steel Tower ladder puts its rungs {SR('yam','8.25 inches')} apart.
```
Replacement:
```
and Yamazaki's steel Tower ladder puts its rungs {SR('yam','8.25 inches')} apart, with its base {SR('yam','from about 10 in to 15 in from the wall')}.
```

### M5. The ladder load figures overstate what ladders hold (build.py, idea 2, and svg.py)

The diagram says "17.6–20 lb load rating on the two blanket ladders we checked", and the desc says "blanket ladders are rated for 17.6 to 20 pounds". That leaves out the third ladder the article links, which is rated far lower, and one of the two figures it does use is ambiguous.

**The Yamazaki ladder is rated at 2.2 lb per bar.**
- Source: https://theyamazakihome.com/products/tower-leaning-ladder-rack
- "Each bar of the ladder supports 2.2 lbs / 1 kg."

**The VASAGLE listing contradicts itself on its 17.6 lb figure.** The description says "holds up to 17.6 lb per rung.", but the specs say "Total Max. Static Load Capacity: 17.6 lb (8 kg)". The ladder is also sold by a third party ("Sold & shipped by LEDREM", Target Plus), not by Target.
- Source: https://www.target.com/p/vasagle-blanket-ladder-decorative-farmhouse-for-the-living-room-5-tier-ladder-shelf-ladder-rack-for-storage-and-decor/-/A-1000114547

**The DecMode figure is correct:** "Max load, 20 lb."
- Source: https://www.walmart.com/ip/744497143

build.py. Current:
```
Ladders are not built for heavy loads: the VASAGLE ladder at Target is rated at {SR('vas','17.6 lb')}, so drape throws rather than stacking quilts.
```
Replacement:
```
Ladders are not built for heavy loads: Yamazaki says {SR('yam','each bar of the ladder supports 2.2 lbs')}, and the VASAGLE ladder sold through Target lists {SR('vas','17.6 lb')} (per rung in one place, in total in another), so drape throws rather than stacking quilts.
```

svg.py card. Current:
```
('17.6–20 lb','load rating on the two','blanket ladders we checked')
```
Replacement:
```
('2.2–20 lb','load limits listed on the','three ladders we checked')
```

svg.py desc. Current:
```
blanket ladders are rated for 17.6 to 20 pounds;
```
Replacement:
```
the three blanket ladders we checked list load limits from 2.2 pounds per bar to 20 pounds;
```

---

## SHOULD-FIX

### S1. The University of Florida "small larvae" claim could not be verified (build.py, idea 14)

Current:
```
and the University of Florida found cedar oil can kill only small larvae.
```

**The live page could not be read.** The SRC URL (https://edis.ifas.ufl.edu/publication/IG090/pdf) returns a 302 redirect to ask.ifas.ufl.edu, and fetching that was refused (PROVENANCE_REQUIRED).

**The archived copy does not contain the claim.** It is UF/IFAS ENY-223 "Clothes Moths and Plaster Bagworms", P.G. Koehler, Jan 1994, revised May 1999: https://journals.flvc.org/edis/article/download/138152/143332/271967. Its only cedar sentence is "Clothing bags, cedar closets, and cedar chests only provide protection when stored materials are free from infestation." It says nothing about cedar oil killing small larvae.

**"Found" also overclaims.** An extension factsheet is guidance, not a study.

A current extension source says the same thing verbatim: Virginia Cooperative Extension ENTO-471NP "Clothes Moths" (Dellinger & Day, Virginia Tech, revised Nov 19, 2021), https://accomack.ext.vt.edu/content/dam/pubs_ext_vt_edu/3104/3104-1576/ENTO-471.pdf: "Cedar oil kills small, but not full-grown larvae, but only until the oil dissipates."

Replacement (needs the new key `vt`):
```
and Virginia Cooperative Extension says {SR('vt','cedar oil kills small, but not full-grown larvae, but only until the oil dissipates')}.
```

### S2. The "6-inch fabric bag" has no source (build.py, idea 8, and svg.py)

The article and diagram say a 6-inch bag fits. The text has no link for it, and the diagram footer credits "Simplify".

The Simplify listing contradicts itself. The title says "SIMPLIFY 40 in. x 18 in. x 6 in. ... Under the Bed (2-Pack) Storage Bag". The spec table says "Product Height (in.) 12 in", "Product Width (in.) 24 in", "Product Depth (in.) 18 in", and Highlights say "Dimensions: 18" x 24" x 12"".
- Source: https://homedepot.com/p/SIMPLIFY-40-in-x-18-in-x-6-in-Beige-Non-Woven-Fabric-Under-the-Bed-2-Pack-Storage-Bag-25424-2PK-FEJ/314118725

A 12-inch-tall bag would not fit under either IKEA frame. Replace it with a product whose listing is consistent: Target's Underbed 3 Drawer Storage Unit - Brightroom, $40, "6.3in H x 45.67in W x 11.81in D", with the same figures in Specifications.
- Source: https://www.target.com/p/-/A-94905415

Alternatively, delete the 6-inch item from both files.

build.py. Current:
```
With about 8 inches to work with, a 6-inch fabric bag or Sterilite's wheeled box at {SR('ster','7 inches (H)')} will fit;
```
Replacement (needs the new key `bri`):
```
With about 8 inches to work with, Target's Brightroom under-bed drawer unit at {SR('bri','6.3 inches')} or Sterilite's wheeled box at {SR('ster','7 inches (H)')} will fit;
```

svg.py box. Current:
```
(92,6,'6 in bag','#E9DFD2')
```
Replacement:
```
(92,6.3,'6.3 in unit','#E9DFD2')
```

svg.py desc. Current:
```
A 6-inch fabric bag and a 7-inch wheeled box fit;
```
Replacement:
```
A 6.3-inch drawer unit and a 7-inch wheeled box fit;
```

svg.py footer. Current:
```
Sterilite, Simplify and Mainstays listings
```
Replacement:
```
Sterilite, Brightroom and Mainstays listings
```

### S3. Hunker said adhesive strips, not hooks, and IKEA's warning cuts against them (build.py, idea 3)

Current:
```
Hunker suggests adhesive hooks only for the thinnest throws.
```

Hunker talks about adhesive strips for mounting the rail itself, and the sentence has no link.
- Source: https://www.hunker.com/2259612/blanket-storage-idea-ikea-hultarp-rail/
- "you can also use adhesive strips to mount the rail on the wall ... but only if your throws are thin and lightweight, like those made from linen and bamboo."

IKEA's own page warns against anything less than a secure fixing.
- Source: https://www.ikea.com/us/en/p/hultarp-rail-black-20448773/
- "WARNING! Falling hazard – to reduce the risk of this product falling down, it must be securely anchored. Use suitable screws and plugs for your home."

Replacement:
```
Hunker says {SR('hunk','adhesive strips')} work only for thin, light throws, but IKEA warns the rail {SR('hult','must be securely anchored')}, so screws are the safer choice.
```

### S4. The wool part of the vacuum-bag advice has no source (build.py, idea 11)

Current:
```
Use vacuum bags for synthetic comforters and moves, not for long-term storage of down or wool.
```

Nothing in the section supports the wool claim. Ideal Home does say it, in an unattributed quote: "Natural fibres such as wool can become damaged when compressed so are better stored in sealed bags which aren't compressed."
- Source: https://www.idealhome.co.uk/house-manual/storage-organisation/should-you-use-vacuum-storage-bags-for-duvets

The same page supports the synthetics half of the sentence. Laura Haddy (APDO): "I would recommend using vacuum bags for synthetic duvets." Rex Isap (Happy Beds) says the same.

Replacement:
```
Ideal Home adds that {SR('ih','natural fibres such as wool can become damaged when compressed')}. Use vacuum bags for synthetic comforters and moves, not for long-term storage of down or wool.
```

---

## MINOR

### N1. Ottoman: "11.75 inches deep" is the height (build.py, idea 4)

The listing gives "Inner Storage Width: 28.4"", "Inner Storage Depth: 12.25"" and "Inner Storage Height: 11.75"". Calling 11.75 the depth clashes with the listing's own depth of 12.25.
- Source: https://www.target.com/p/lucinda-rectangle-storage-ottoman-linon/-/A-89851438

Current:
```
but its compartment is 28.4 x 12.25 inches and {SR('lin','11.75 inches')} deep,
```
Replacement:
```
but its compartment is 28.4 inches wide, 12.25 inches deep and {SR('lin','11.75 inches')} high,
```

### N2. Kelly Beutler was talking about a bulky quilt or blanket, not a comforter (build.py, idea 12)

In the article, "it" reads as the comforter, and the purpose given ("so rolls can stand in a basket") is not hers.
- Source: https://www.consumerreports.org/home-garden/sheets/the-easiest-way-to-store-bedding-a3985264822
- Her words: "If you've got a bulky quilt or blanket, try rolling it and tying it with a ribbon and then stack it with other rolled blankets."
- CR describes her as "a professional organizer and owner of The Joyful Sort in Columbus, Ohio".

Current:
```
Organizer Kelly Beutler told Consumer Reports to {SR('crb','try rolling it and tying it with a ribbon')}, so rolls can stand in a basket or stack on a shelf.
```
Replacement:
```
For a bulky quilt or blanket, organizer Kelly Beutler told Consumer Reports to {SR('crb','try rolling it and tying it with a ribbon')} and then stack it with other rolled blankets.
```

### N3. Shannon Krause's method is paraphrased inaccurately (build.py, idea 1)

She folds the blanket in half lengthwise twice, then rolls it from a short end.
- Source: https://www.homesandgardens.com/solved/how-to-store-blankets
- "Fold the blanket in half lengthwise so both halves are aligned. Repeat this so you have a small rectangle."
- "Start at one end (either of the shorter sides of your rectangle) and tightly roll the blanket."
- On fringe: "if your blanket has a fringe along the edge, try to tuck it inside the initial fold"
- The page gives her as "Professional Organizer of Tidy Nest".

Current:
```
To roll one neatly, organizer Shannon Krause of Tidy Nest folds it in half lengthwise and rolls it from one end, tucking any fringe inside the first fold so it does not get damaged.
```
Replacement:
```
To roll one neatly, organizer Shannon Krause of Tidy Nest folds it in half lengthwise twice, then rolls it tightly from one of the short ends; if it has a fringe, she tucks it inside the first fold so it does not get damaged.
```

### N4. The Living Spaces thin-comforter fold is described wrongly (build.py, idea 12)

The page folds each corner into the center, then folds in half. It does not fold in quarters.
- Source: https://www.livingspaces.com/inspiration/ideas-advice/how-tos/how-to-store-comforters
- "Pick up one corner and fold it into the center of the comforter, and repeat for the other three corners." ... "Then, fold the comforter at the center."

Current:
```
For a thinner one, Living Spaces suggests folding it in quarters, then in half.
```
Replacement:
```
For a thinner one, Living Spaces suggests folding each corner into the center, then folding it in half.
```

### N5. University of Florida: name the products, not "cedar and similar products" (build.py, list)

The source sentence is "Clothing bags, cedar closets, and cedar chests only provide protection when stored materials are free from infestation." This was verified on the archived FLVC copy. As noted in S1, the live EDIS URL redirects and could not be fetched, so re-check that the link resolves before publishing. The dry-cleaning line is also in the source: "Dry clean items such as woolen sweaters, before they are stored."

Current:
```
The University of Florida notes that cedar and similar products {SR('ufl','only provide protection when stored materials are free from infestation')}
```
Replacement:
```
The University of Florida notes that clothing bags, cedar closets and cedar chests {SR('ufl','only provide protection when stored materials are free from infestation')}
```

### N6. "Most experts" overgeneralises (build.py, intro)

The article rests this on a handful of sources, and they do not agree.
- Against vacuum-sealing down: Biggs (Ideal Home), Mattress Nerd ("vacuum-sealing can damage the down filling"), Tia Mellis (Livingetc), and Di Ter Avest ("be careful").
- For short-term use: Puffy says "While it is technically okay to vacuum seal a down comforter, it's essential to take precautions."
- For vacuum-sealing seasonal blankets: Julianna Melamed (H&G) recommends "a vacuum seal system".

Current:
```
Vacuum bags save space, but most experts say not to use them for down.
```
Replacement:
```
Vacuum bags save space, but most of the organizers we checked advise against them for down.
```

### N7. The Ziploc 75% claim comes from a retailer listing and has a condition attached (build.py, idea 11)

The claim is product copy on a Harris Teeter page, and it continues with a qualifier.
- Source: https://harristeeter.com/p/ziploc-space-bag-vacuum-seal-storage-bags/0003181070424
- "Volume can be reduced by up to 75% to triple your storage space, depending on the items placed in the bag;"

Current:
```
Ziploc says {SR('zip','volume can be reduced by up to 75%')}.
```
Replacement:
```
Ziploc's product copy says {SR('zip','volume can be reduced by up to 75%')}, depending on what is in the bag.
```

### N8. Mainstays risers: grammar (build.py, idea 8)

"bed risers like the Mainstays set lifts" mixes a plural subject with a singular verb. The figure is correct: "Lifts your bed by 5.25 inches to create immediate under-bed storage space". The riser's overall height is 6 in, so 5.25 in is the right figure for the gain.
- Source: https://www.walmart.com/ip/5405909905

Current:
```
For more room, bed risers like the Mainstays set {SR('riser','lifts your bed by 5.25 inches')}.
```
Replacement:
```
For more room, a set of Mainstays bed risers {SR('riser','lifts your bed by 5.25 inches')}.
```

### N9. Rachel-Elizabeth Mitchell needs her company and the outlet (build.py, idea 10)

Livingetc gives her only as "Rachel-Elizabeth Mitchell of Please Organise Me", with no job title. The quote is verbatim: "Try to store them by weight and avoid having anything on top of your down comforters."
- Source: https://livingetc.com/advice/blanket-storage-ideas

Current:
```
Don't pile things on top, either: organizer Rachel-Elizabeth Mitchell advises you
```
Replacement:
```
Don't pile things on top, either: Rachel-Elizabeth Mitchell of Please Organise Me told Livingetc to
```

### N10. Diagram: the SKUBB volume uses outside dimensions (svg.py)

IKEA lists the SKUBB case as "35 ½x20 ¾x7 ½"", which is its product size, not an inside size. The ottoman and bench figures are inside sizes.
- Source: https://www.ikea.com/us/en/p/skubb-storage-case-dark-gray-10591064/

Subtitle. Current:
```
Calculated from each product\'s listed inside size
```
Replacement:
```
From listed sizes: inside for ottoman and bench, outside for the case
```

### N11. Diagram desc: same issue as N10 (svg.py)

Current:
```
calculated from listed inside dimensions:
```
Replacement:
```
calculated from listed dimensions (inside for the ottoman and bench, outside for the soft case):
```

### N12. Diagram: Closet World says "usually", not "standard" (svg.py)

The source says "Builder shelving is usually fixed around 12 inches apart". It reserves "standard" for shelf depth: "A standard linen closet shelf runs 14 to 18 inches deep".
- Source: https://www.closetworld.com/blog/linen-closet-organization

Current:
```
folded duvet (standard: 12 in)
```
Replacement:
```
folded duvet (fixed: often 12 in)
```

### N13. The DecMode wall ladder is out of stock (build.py, idea 3)

The listing shows "Out of stock" ($71.51). The 20 lb rating is correct.
- Source: https://www.walmart.com/ip/744497143

Current:
```
one sold at Walmart is rated for {SR('dec','20 lb')}.
```
Replacement:
```
one listed at Walmart (out of stock when we checked) is rated for {SR('dec','20 lb')}.
```

### Notes (no text change required)

- **Trunk dimensions.** The Household Essentials listing contradicts itself. Highlights say "18.25" H x 29" W x 16.25" D", which is what the article uses. Specifications say "18.3 inches (H) x 16.5 inches (W)". The material is "MDF (Medium-Density Fiberboard)", although the product is named "wooden".
- **Sterilite link.** It points to a 12-pack ($359.43) "Sold & shipped by Spreetail". The 7" H spec is correct: "7 inches (H) x 18.75 inches (W) x 33.88 inches (D)". Consider linking a single-unit listing.
- **Unused key.** `osu` (Oregon State PNW606) is defined in SRC but never cited. If you want a third extension voice, it says: "While cedar chips or balls smell wonderful, they do nothing to repel clothes moths."
- **Consumer Reports paywall.** The CR "easiest way to store bedding" page shows the title "Your membership has expired", but the article text loaded and the quotes were confirmed. Some readers may hit the paywall.

---

## Verified OK

### Expert quotes and roles: Homes & Gardens, "how to store blankets"

Source: https://www.homesandgardens.com/solved/how-to-store-blankets (Ottilie Blackhall, 8 Sep 2025)

- **Janelle Lam**, "Professional Home Organizer and TV Personality": "If you have throw blankets, I recommend putting them in a decorative storage basket near where you use them, like your couch." Verbatim; "Professional organizer" is fine.
- **Artem Kropovinsky**, "Interior Design Expert and the Founder of Arsight Studios": "You can use ladder-style racks for a sophisticated presentation." Verbatim; "Designer" is fine.
- **Shannon Krause**, "Professional Organizer of Tidy Nest". Name and role OK; for the method wording see N3.
- **Julianna Melamed**, "Founder of Full Service Living": "Those are two places where blankets are sure to get musty and possibly even moldy." Verbatim. "Those" refers to "The basement and attic", so "Skip the attic and basement" is correct.

### Expert quotes and roles: Homes & Gardens, "how to store a comforter"

Source: https://www.homesandgardens.com/solved/how-to-store-a-comforter

- **Ben Soreff**, "Professional Organizer at House to Home Organizing": "Try and avoid using plastic, since our goal is always for the duvet to breathe." Verbatim.
- **Di Ter Avest**, "Professional Organizer and Founder of Diisorganized": "Fold it in thirds lengthwise, then fold it again into a compact square or roll it up." Verbatim.

### Expert quotes and roles: other outlets

- **Rachel-Elizabeth Mitchell** (Livingetc): the quote is verbatim. For the attribution wording see N9.
- **Amanda Biggs** (Ideal Home), "APDO's memberships director and founder of Professionally Organised": "I would not recommend using vacuum bags if you have feather bedding as compressing feather duvets can damage the feathers ..." Verbatim. Describing APDO as the UK's association of professional organizers is fair (APDO = Association of Professional Declutterers and Organisers; the page does not expand the acronym).
- **Jeffrey Phillip** (Consumer Reports), "of Jeffrey Phillip Organization and Design": "Bulkier, less frequently used items like extra blankets and pillows can go in soft-sided bins on an upper shelf or on the floor." Verbatim, and the "bulky items" paraphrase is fair. Source: https://www.consumerreports.org/home-organization/how-to-organize-your-linen-closet/ (Brooke Glassberg, Apr 7, 2022)
- **Consumer Reports**, in its own voice: "a bed should have two sheet sets—the one on it and a backup." Verbatim.
- **Brooklinen**: "Keep items rarely used—heated blankets, extra sheets for guests, beach towels, and tablecloths—on the topmost shelf ..." and "cap out your linens at three sets per bed or person." Both OK.

### Target products

- **Storied Home ladder**: $57.99; "72.5 Inches (H)"; "Number of Rungs: 5". Leaning ("can be easily placed against the wall"). OK.
- **VASAGLE ladder**: 17.6 lb appears. For the per-rung versus total ambiguity see M5.
- **Threshold Light Coiled Basket**: $45; "16.14in H x 18.1in W x 18.1in D", round. So "18.1 inches across" and "about 16 inches tall" are OK.
- **Linon Lucinda ottoman**: 32" W outside; inside 28.4 x 12.25 x 11.75 (for the wording see N1); $202.99; holds 200 lb.
- **HomePop tufted bench**: 40.0" W outside. Inside "37.75"W x 15.75"D x 9.75"H" comes from a HomePop "Brand expert" Q&A answer, so "its maker gives" is accurate. $127.99.
- **Household Essentials trunk**: $183.99; 18.25 x 29 x 16.25 per Highlights (see Notes).
- **Sterilite wheeled box**: 7" H OK (see Notes).

### Other retailers

- **Yamazaki**: "distance between runghs [sic] of 8.25 inches"; steel; $88.
- **Walmart DecMode**: wall-mounted, 6 rungs, "Max load, 20 lb".
- **Walmart Mainstays**: "Lifts your bed by 5.25 inches".

### IKEA

- **HULTARP**: "31 ½"", $12.99, "Screws for wall mounting sold separately."
- **MALM** (oak veneer, Queen): "Height under furniture 8 1/4"".
- **NEIDEN** (pine, Full): "Height under furniture 7 7/8"".
- **SKUBB**: 35 ½ x 20 ¾ x 7 ½", $12.99.
- **VARIERA**: $7.99, matching both IKEA US and Apartment Therapy.

### Numbers

- **Casper**: "A standard throw blanket is 50 inches wide by 60 inches tall".
- **Closet World**: "a folded duvet needs closer to 14 to 16 inches"; "Builder shelving is usually fixed around 12 inches apart". The article's "many fixed shelves are about 12 inches apart" is OK.
- **Ziploc**: "Volume can be reduced by up to 75%" (for wording see N7).
- **Puffy** (Puffy Editorial Team): "Aim to vacuum seal only for 3-6 months"; "Remove only enough air to reduce the bulk by half"; "Repeated vacuum sealing may cause the delicate feathers to break."; "Moisture trapped in a sealed bag can lead to mildew or mold." All OK.
- **Mattress Nerd**: "Having your comforter completely dry before storage is important". OK.
- **Living Spaces**: "cotton is an excellent choice for airflow". This supports the cotton bag advice.
- **Lowe's**: "add a small piece of rubber drawer liner or rubber pads to the bottom of the rails to keep them from sliding" and "Avoid using felt pads for this as they will not be as secure." OK.
- **USFA**: "Keep them at least three feet from things that can burn." OK.

### Cedar and moth sources

- **Clemson HGIC 2416** (Benson & Zungoli, updated Apr 23, 2020): "most types of cedar chests and closets are only marginally effective against fabric pests". OK. The page also says storing in cedar chests "is fine", and that cedar's benefit "lessens" over time. Saying cedar is not a moth cure is fair.
- **University of Maryland**: "Woolen articles should be cleaned and stored in sealed boxes." Verbatim. The same page says "Cedar chests, blocks, or closets also provide protection", which is why M2 softens "not protection" to "not full protection".
- **Pendleton**: "Air out, shake and refold your treasures every few months." and "Store blankets in plastic airtight boxes and bags that seal completely." This supports "Store wool sealed".

### Diagram arithmetic

- 28.4 x 12.25 x 11.75 = 4,087.8 cu in = 2.37 cu ft, which rounds to 2.4. OK.
- 37.75 x 15.75 x 9.75 = 5,797.0 cu in = 3.35 cu ft, which rounds to 3.4. OK.
- 35.5 x 20.75 x 7.5 = 5,524.7 cu in = 3.20 cu ft. OK, but these are outside dimensions (N10).
- 8 1/4 + 5 1/4 = 13 1/2. OK.
- The diagram correctly calls the 7 1/2" SKUBB tight under the 7 7/8" NEIDEN frame.
- The idea count is 14, matching "Below are 14 blanket storage ideas".

## Pages that could not be fetched

- **https://edis.ifas.ufl.edu/publication/IG090/pdf** redirects (302) to ask.ifas.ufl.edu, and fetching that was refused (PROVENANCE_REQUIRED). I verified against the archived FLVC copy of the same publication instead (S1, N5).
