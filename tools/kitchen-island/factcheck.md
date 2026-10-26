# Fact-check: Kitchen Island Ideas (UK)

Checked 26 Oct 2026 against the live pages. Each source was found with WebSearch, then fetched with WebFetch. Quotes below come back through the WebFetch summariser in quotation marks, and ambiguous ones were re-fetched. No AOL copies were used.

**Result: 0 MUST-FIX, 7 SHOULD-FIX, 7 MINOR.** No figure, price, product name or credited quote is plainly wrong. The problems are an invented dimension (The Range), an unsourced safety tip (locking castors), a quote framed with context it does not have (Proudfoot), an intro figure that sits below Wren's own guidance, and some unlinked or incomplete attributions.

Replacement script: `/tmp/claude-0/-home-claude/aa9f44c6-b1c7-520d-9978-96402d6712cc/scratchpad/ki_repl.py`. Run it as `python3 ki_repl.py <dir>`. It holds 14 replacements (F01 to F14). It checks that every old string occurs exactly once before writing anything, and it aborts on a second run. I tested it on a scratch copy only: `svg.py` and `build.py` both run (27,430 bytes; 1,914 words; keyword count still 3), and the new SVG footer fits (962 px wide in a 1200 px canvas). The repo files are unchanged.

---

## SHOULD-FIX

### F01: The intro's room width is below the cited brand's own figure (build.py)
- **Current:** `which means a fitted island usually wants a room around 4 metres wide.`
- **Problem:** The next section cites Wren's 1 m rule, but the same Wren page concludes the room must be wider than our "around 4 metres". Our 3.8 m and 4.3 m sums are right for their assumptions (a 60 cm island, or 90 cm with stools). Howard Miller of H. Miller Bros (Ideal Home) also gives "the room needs to be 4x4m minimum", so "around 4 m" is defensible as a floor, not as the norm.
- **Evidence:** https://www.wrenkitchens.com/blog/do-you-have-room-for-a-kitchen-island: "All in all your space needs to be 4.5 to 5 metres wide for a small kitchen island."
- **Replacement:** `which means a fitted island usually wants a room around 4 metres wide, though Wren says {SR('wren','your space needs to be 4.5 to 5 metres wide for a small kitchen island')}.`

### F02: The butcher's-block claim is unsourced (build.py)
- **Current:** `the minimum size of a kitchen island is 1000mm x 1000mm')}, though a butcher's block can be smaller.`
- **Problem:** Ideal Home's page does not mention butcher's blocks. The claim, and the diagram's "Butcher's block: from 60 cm", come from Tony Collier of Wickes in Homebuilding, which the prose never cites.
- **Evidence:** https://www.homebuilding.co.uk/advice/minimum-kitchen-island-size: Tony Collier, senior product manager at Wickes: "For example, a classic butcher's block can be as small as 600mm"
- **Replacement:** `the minimum size of a kitchen island is 1000mm x 1000mm')}, while Tony Collier of Wickes told Homebuilding that {SR('hbs','a classic butcher\'s block can be as small as 600mm')}.`

### F03: "Lock the castors" assumes a feature FÖRHÖJA is not listed with (build.py)
- **Current:** `Lock the castors when you chop, and roll it against a wall when you need the floor.`
- **Problem:** The sentence follows straight on from FÖRHÖJA, but IKEA's page lists no locking castors or brakes. It says only "This clever wheeled island rolls in to save the day." Telling readers to lock wheels they may not be able to lock, while chopping with a knife, is a safety point.
- **Evidence:** https://www.ikea.com/gb/en/p/-80035920/: no "lock", "brake" or "castor" line in the product details, materials or measurements.
- **Replacement:** `IKEA does not list locking castors, so brace it against a wall or worktop when you chop, and roll it aside when you need the floor.`

### F04: The Range's dimension "with the leaf up" is not on the page (build.py)
- **Current:** `The Range's rolling island with a drop leaf is 65 cm wide and 107 cm long with the leaf up, costs £139.95`
- **Problem:** The page gives only "Width: 65cm", "Height: 90cm" and "Depth: 107cm". It gives no leaf-up or leaf-down size, so "with the leaf up" is inferred. The price (£139.95) and "fits a 27L trash can" are correct.
- **Evidence:** https://www.therange.co.uk/furniture/dining-room-furniture/kitchen-trolleys-and-islands-on-wheels/kitchen-island-with-drop-leaf: "Width: 65cm" / "Depth: 107cm" / "The tilt-out trash cabinet fits a 27L trash can (not included) for added convenience."
- **Replacement:** `The Range's rolling island with a drop leaf is listed at 65 cm wide and 107 cm deep (the page does not say whether that is with the leaf up), costs £139.95`

### F09: Overhang support is understated, and two claims are unlinked (build.py)
- **Current:** `; much more than that needs legs or brackets, and DIY Kitchens says a 20 mm worktop can overhang only 250 mm unsupported.`
- **Problem:** The source says any overhang beyond 30 cm needs support, not "much more". The Daval and DIY Kitchens claims also carry no links. The figures themselves are right.
- **Evidence:** https://www.idealhome.co.uk/kitchen/kitchen-advice/space-between-counter-and-island-299178: Simon Bodsworth, managing director at Daval Furniture: "If you want to incorporate a cantilevered worktop design that goes beyond 30cm, then you’ll need to introduce extra support like legs or metal brackets to share the load and meet safety requirements." https://advice.diy-kitchens.com/customer-questions/design-island-feature/: "With a 20mm worktop, the maximum unsupported overhang would be 250mm, with a 30mm the maximum would be 300mm."
- **Replacement:** `. Beyond that, Simon Bodsworth of Daval Furniture says {SR('ihc','you’ll need to introduce extra support like legs or metal brackets')}, and DIY Kitchens says that {SR('diyk','with a 20mm worktop, the maximum unsupported overhang would be 250mm')}.` The quote keeps the page's curly apostrophe.

### F10: Proudfoot's quote is framed as small-island advice, and his company is missing (build.py)
- **Current:** `A hob is harder: on a small island Christopher Proudfoot warns {SR('hbhob',`
- **Problem:** The quote is verbatim, but Homebuilding does not tie it to small islands; it is about island hobs in general. His company is also not named.
- **Evidence:** https://www.homebuilding.co.uk/advice/should-you-have-a-hob-on-a-kitchen-island: Christopher Proudfoot, owner and director at The White Kitchen Company: "An overhead extractor may not be feasible, so a downdraft system might be necessary, which can be more expensive."
- **Replacement:** `A hob is harder: Christopher Proudfoot of The White Kitchen Company told Homebuilding that with an island hob {SR('hbhob',`

### F14: The diagram footer omits Naked Kitchens (svg.py)
- **Current:** `Example widths are our own sums with 60 cm units. Sources: Wren, Harvey Jones, Magnet, Wickes, Homebuilding, DFS, Tala, NICEIC.`
- **Problem:** The "Per stool: 60 cm of worktop" row comes from Naked Kitchens, which the footer does not list. Every other row maps to a listed source:
  - Wren / Homebuilding: 1 m and 1.2 m
  - Homebuilding (Proudfoot, Davonport): 90 cm to 1.2 m behind stools
  - Magnet: 100 x 100
  - Wickes: 60 cm butcher's block
  - Homebuilding / DFS: 90 cm worktop
  - DFS: 100–110 cm bar
  - Harvey Jones: about 30 cm overhang
  - Tala: pendants
  - NICEIC: sockets

  I dropped "with 60 cm units" to keep the line width the same, since the subtitle and desc already state the 60 cm units.
- **Evidence:** https://www.nakedkitchens.com/blog/the-kitchen-expert/breakfast-bars-and-stations-design-inspiration-and-expert-tips: "Pro tip: allow at least 60cm per stool for comfort, even in small spaces."
- **Replacement:** `Example widths are our own sums. Sources: Wren, Harvey Jones, Magnet, Wickes, Homebuilding, Naked Kitchens, DFS, Tala, NICEIC.`

---

## MINOR

### F05: The Darren Watts sentence is garbled (build.py)
- **Current:** `slimline islands are {SR('ihs','narrow, yet long, these islands are purely for cooking, storage or food preparation')}.`
- **Problem:** The quote is verbatim, and Watts is Design Director at Wren Kitchens. But spliced in, it reads "slimline islands are narrow, yet long, these islands are…". It also cuts the key end of his sentence.
- **Evidence:** https://www.idealhome.co.uk/kitchen/kitchen-ideas/small-kitchen-island-ideas-296888: "Narrow, yet long, these islands are purely for cooking, storage or food preparation rather than an area for seating," says Darren Watts, Design Director, Wren Kitchens.
- **Replacement:** `slimline islands are {SR('ihs','purely for cooking, storage or food preparation rather than an area for seating')}.`

### F06: METOD 80x37 at £45 is a frame only, and the wording is ungrammatical (build.py)
- **Current:** `IKEA's METOD base cabinet also comes in a {SR('metod','80x37x80 cm')} version (£45)`
- **Problem:** £45 buys the bare frame. "also" refers back to a METOD mention that does not exist, and "a 80x37" should read "an".
- **Evidence:** https://www.ikea.com/gb/en/p/-10205628/: "METOD Base cabinet, white, 80x37x80 cm", £45; "Doors, drawers, worktop, shelves, hinges, plinths and cover panels sold separately."
- **Replacement:** `IKEA's METOD base cabinet frame comes in a shallow {SR('metod','80x37x80 cm')} size (£45, doors extra)`

### F07: HÅLLBAR is meant for a 60 cm drawer, not the 80 cm unit just mentioned (build.py)
- **Current:** `four 10-litre bins for a METOD drawer, costs {SR('hall','£41')}.`
- **Evidence:** https://www.ikea.com/gb/en/p/-s39308923: "HÅLLBAR Waste sorting solution, for METOD kitchen drawer ventilated/light grey, 40 l", £41, four 10 l bins. IKEA recommends mounting it in a MAXIMERA high drawer of 60 × 60 or 60 × 45 cm.
- **Replacement:** `four 10-litre bins that IKEA recommends for a 60 cm wide MAXIMERA high drawer, costs {SR('hall','£41')}.`

### F08: Caroline Levenson has no role (build.py)
- **Current:** `often wasted. Caroline Levenson told Homes &amp; Gardens`
- **Evidence:** https://www.homesandgardens.com/kitchens/kitchen-island-storage calls her "interior designer Caroline Levenson". Her quote is verbatim: "We see missed opportunities on the back side of the island, which can be a great place for shallow storage…"
- **Replacement:** `often wasted. Interior designer Caroline Levenson told Homes &amp; Gardens`

### F11: Tala's spacing applies to medium pendants (build.py)
- **Current:** `about 60 to 75 cm apart.`
- **Evidence:** https://tala.co.uk/blogs/lighting-guide/how-high-should-pendant-lights-hang-over-a-kitchen-island: "Space evenly along the island, typically 24–30 inches (60–75cm) apart for medium pendants". The page defines medium as 20–40 cm in diameter.
- **Replacement:** `about 60 to 75 cm apart for medium pendants.`

### F12: Charlie Smallbone has no company (build.py)
- **Current:** `Charlie Smallbone's advice to Livingetc says it best:`
- **Evidence:** https://www.livingetc.com/spaces/interior-inspiration/small-kitchen-island-ideas-240821: Charlie Smallbone, Founder, Ledbury Studio: "And if you don't have the room, don't force it."
- **Replacement:** `Charlie Smallbone, founder of Ledbury Studio, put it best to Livingetc:`

### F13: The diagram caption says "1 m walkways", but the stool layout uses 1.2 m (build.py)
- **Current:** `one with stools needs about 4.3 m.`
- **Replacement:** `one with stools and 1.2 m behind them needs about 4.3 m.`

### Notes with no change needed
- **"trash".** Fred Horlock's quote and The Range's listing both say "trash" (US usage). Both are verbatim, so leave them.
- **Emily Pickett.** Her quote opens with a caveat the article drops: "In an ideal world, if space and layout allow, you want to keep the top of a smaller island clear of sinks or hobs too". "Suggests" is fair as it stands.
- **Ideal Home's £1,000–£4,500** is for "an island unit". The "Fitted island" label is our framing. The page does not say whether worktop or fitting is included, so the article's "Extras" line covers it.
- **Prices drift.** Prices were checked on 26 Oct 2026 and the article publishes on 28 Jan 2027. Re-check the IKEA, Dunelm and The Range prices the week before publishing. Research notes that Dunelm's Francis was £249 in an Ideal Home piece in Sep 2026.

---

## Verified OK

**Quotes and attributions** (all verbatim and correctly credited):
- **Melissa Klink, Head of Design, Harvey Jones** (Livingetc): "As a rule, the walkways around an island need to be at least 100cm wide…"
- **Melissa Klink, Harvey Jones** (Ideal Home storage page): "Another practical addition to the island is a hanging rail for hand towels and tea towels". The page gives no role, and the article gives none.
- **Lizzie Beesley, Head of Design, Magnet** (Ideal Home): "The minimum size of a kitchen island is 1000mm x 1000mm"
- **Helen Parker, Creative director, deVOL** (Livingetc): "There is something really quite pleasing about a movable piece of furniture;"
- **Stephanie Nix, Kitchen Designer, Neptune** (Livingetc): "Including a freestanding unit is the perfect solution if you have less room to play with". The anchor's trim at "less room" does not change the meaning.
- **Darren Watts, Design Director, Wren Kitchens** (Ideal Home): verbatim. Only the splice is an issue (F05).
- **Simon Ribchester, Head of Design, Beams** (Livingetc): "A narrower island still gives you extra prep space and storage, without eating up your floor area,"
- **Claire Garner, Founder, Claire Garner Design Studio** (Livingetc, 7 Jun 2025): "Because it connects to existing cabinetry, it takes up less floor space…"
- **Dave Young, founder, HUSK Kitchens** (Ideal Home): "…we always recommend deep drawers with integrated storage systems,"
- **Anthony Earle, Creative designer, Artichoke** (Homes & Gardens): "For deeper pan drawers, incorporating a slim internal drawer for lids is quite clever"
- **Fred Horlock, Design director, Neptune** (Homes & Gardens): "Concealed trash storage is a brilliant use of storage on the island"
- **Caroline Levenson** (Homes & Gardens): verbatim. Only her role is missing (F08).
- **Tom Howley, creative design director, Tom Howley** (Ideal Home): "…open shelving on which you can display your favourite pottery, cookery books or pieces of art"
- **Matt Baker, kitchen designer, Harvey Jones** (Ideal Home): "you will need around 30cm of worktop overhang"
- **Christopher Proudfoot** (Homebuilding): verbatim. Only the framing is an issue (F10).
- **Emily Pickett, Design consultant, Kitchens by Holloways** (Livingetc): verbatim.
- **Charlie Smallbone, Founder, Ledbury Studio** (Livingetc): "And if you don't have the room, don't force it."
- **Wren:**
  - "Generally the rule of thumb is a 1 metre clearance zone." (blog, 5 Mar 2021)
  - "For small kitchens, a peninsula can be much more practical than an island." (small-kitchen design page)
- **Homebuilding's 1.2 m figure is in the article's own voice**, so "Homebuilding says" is the right credit: "a minimum clearance of 1.2m will allow multiple people to move around comfortably". It is not a named designer's quote. The 90 cm behind stools is Christopher Proudfoot's; the 1.2 m behind seating is Richard Davonport's.
- **Homes & Gardens' "five to six bottles"** is in the article's voice, so "Homes & Gardens notes" is right.

**Products** (IKEA GB, Dunelm and The Range, all checked 26 Oct 2026):
- **FÖRHÖJA:** "FÖRHÖJA Kitchen trolley, birch, 100x43 cm", £129, 90 cm high. "Open storage with space for 9 bottles on each shelf." The materials list includes a drawer, and a review confirms "2 drawers", so two drawers is OK.
- **TORNVIKEN:** "TORNVIKEN Kitchen island, off-white/oak, 126x77 cm", £379, with shelves and no drawers.
- **VADHOLMA:** "VADHOLMA Kitchen island, black/oak, 126x79x90 cm", £579. "Large" is fair, since a 79x63x90 version exists on IKEA GB.
- **Dunelm Francis:** £349, no was/now price. H90 x W123.3 x D74.8 cm (rounds to 123 x 75). One soft-close drawer, "Twin cupboard storage" and open shelves.
- **The Range drop-leaf island:** £139.95, 65 cm wide, tilt-out cabinet for a 27L bin. Only "with the leaf up" is unsupported (F04).
- **METOD frame:** 80x37x80 cm, £45 (frame only, F06).
- **METOD/MAXIMERA:** "Base cb 2 frnts/2 low/1 md/1 hi drw … 80x60 cm", £330, four drawers: two low, one medium, one high.
- **HÅLLBAR:** £41, four 10 l bins, 40 l in total.

**DIY Kitchens:**
- "The average depths (front to back) of our islands are either 600mm or 900mm"
- "560mm+300mm does = 860mm" and "860mm + (2 x 20mm doors) = 900mm depth"
- 20 mm worktop: 250 mm maximum unsupported overhang

**Seating:**
- **Naked Kitchens** (brand voice): "allow at least 60cm per stool for comfort, even in small spaces"
- **DFS:** "Kitchen counters (around 90cm high): Seat height of 60–65cm." and "Breakfast bars (around 100–110cm high): Seat height of 70–75cm." So DFS does tie the 60–65 cm seat to a worktop of about 90 cm, and the article's wording is right.

**Electrics:**
- **NICEIC:** "All socket-outlets in kitchens must be protected by a residual current device (RCD)". On sinks: "it's recommended that socket-outlets are placed at least 30cm horizontally away from sinks". That is a recommendation, so "should" is fine.
- **Approved Document P** (2013 edition, still the current edition per the Planning Portal): notifiable work includes "the installation of a new circuit". It is "for use in England", so "in England" is right.
- **"So use a registered electrician"** is fair advice. NICEIC says "The safest, easiest, and least expensive option is to choose a CPS-registered electrician". AD P also allows notifying a building control body, so this is advice rather than law, and the article does not present it as law.

**Sink, lighting and costs:**
- **MyJobQuote** (updated 7 Oct 2026):
  - "Move into an island (timber / suspended floor) | £800–£1,100"
  - "Move into an island (concrete / screed floor, waste channel cut) | £1,100–£1,600"
- **Tala** is a UK company (Tala Energy Ltd, London showroom): "70–80cm (28–32 inches) above the countertop surface". The 60–75 cm spacing is for medium pendants (F11).
- **Livingetc** (10 Jun 2025, article voice): "Expect around £500 to £1,500 for a non-bespoke timber or steel island that can be assembled in place."
- **Ideal Home** (updated 22 Apr 2025, article voice): "an island unit that comes in somewhere between £1,000-£4,500" and "upwards of £5,000 for something special" (bespoke).
- **Trolley/drop-leaf £130–£140 and freestanding £349–£579** match the product prices above.

**Diagram:**
- Slim island: 60+100+60+100+60 = 380 cm, so "about 3.8 m" is correct.
- Island with stools: 60+100+(60+30)+120+60 = 430 cm, so "about 4.3 m" is correct.
- **"A trolley 43 cm deep"** is correct (FÖRHÖJA, 43 cm).
- **Planning numbers:**
  - 1 m walkway; 1.2 m for two cooks or a main route (Homebuilding; Wickes's "900mm or 1200mm for a main thoroughfare")
  - 90 cm to 1.2 m behind stools (Proudfoot / Davonport)
  - About 100 x 100 cm smallest island (Magnet)
  - Butcher's block from 60 cm (Wickes)
  - Worktop 90 cm ("The minimum recommended height for an island is 900mm", Homebuilding; DFS "around 90cm")
  - Breakfast bar 100–110 cm (DFS; Homebuilding's 1060 mm sits inside it)
  - About 30 cm overhang, more needs support (Harvey Jones / Daval)
  - 60 cm per stool (Naked Kitchens)
  - Pendants 70–80 cm (Tala)
  - Sockets 30 cm from a sink plus RCD (NICEIC)

  All are supported. The only footer gap is Naked Kitchens (F14).
