# Fact-check: Small Ensuite Ideas (content.html, svg.py)

Checked 25 Oct 2026. Every source was found through WebSearch and then fetched in this session. The fetch tool goes through an extraction model, so quotes reported as verbatim are as close as that allows.

Severity counts: **must-fix 3 · should-fix 8 · minor 11**

---

## Issues

### MUST-FIX

**1. Three Birds' ensuite was a client's house, not their own**
- Current text (build.py / content.html): `in their own small ensuite`
- What's wrong: the post is filed under "HOUSE 9", and Bonnie writes about "her" house, meaning a client's ("Before we got our hands on this little ugly duckling of a house, she could only dream..."). It wasn't one of the Birds' own homes.
- Evidence: https://www.threebirdsrenovations.com/blog/smallensuites: "And speaking of the toilet, also from Reece, we chose an in-wall cistern to save space and showcase more of the tiles."
- Replace with: `in a small ensuite they renovated for a client (House 9)`

**2. "You can't hang towel rails or a cabinet" on a cavity slider wall: no source, and a source contradicts it**
- Current text: `Plan it before the walls go up: the cavity needs a stud-free section of wall the width of the door, so you can't hang towel rails or a cabinet on that stretch.`
- What's wrong: no source is given. A CS for Doors bathroom case study says the vanity and mirrored cupboards were fixed to the slider wall by "ordering additional nogs on one side of the pocket for fixing." CS Cavity Sliders also sells extra nogs on request. The claim is stated as an absolute, and it's wrong.
- Evidence: https://www.eboss.co.nz/ebossnow/cs-for-doors-cavity-slider-saves-space-bathroom-renovation ("ordering additional nogs on one side of the pocket for fixing"); https://archipro.com.au/product/wet-area-cavity-slider-cs-cavity-sliders-au ("Treated jambs, nogs and skirting blocks can be requested")
- Replace with: `Plan it before the walls go up: the door slides into a pocket in the wall about as wide as the door, and if you want a towel rail, vanity or cabinet on that stretch, order the unit with extra noggings for fixing.`

**3. Plumbing rough-in cost is for adding a new ensuite, not renovating one**
- Current text: `One Sydney cost guide puts ensuite renovations at $17,250–$34,500, with plumbing rough-in alone at $2,300 to $5,750, and premium jobs much higher. Keeping the wastes where they are is the biggest saving.` (link key `cost`, anchor `$17,250–$34,500` stays)
- What's wrong: on the page, "plumbing rough-in alone costs $2,300 to $5,750" sits in the section on adding a new ensuite. The $17,250–$34,500 range covers renovating an existing ensuite with budget fittings ($17,250–$24,150) through mid-range fittings ($24,150–$34,500). The premium band is given as a figure, so "much higher" can be precise. The source also doesn't say "keeping the wastes ... is the biggest saving". It says keeping the layout "avoids new plumbing and re-waterproofing - the biggest avoidable cost."
- Evidence: https://whatsthedamage.com.au/bathroom-renovation-cost-sydney/ensuites/ (October 2026): "$17,250 to $24,150 with budget fittings", "$24,150 to $34,500 at the mid-range in 2026", "sits in the $40,250 to $63,250 premium band", "plumbing rough-in alone costs $2,300 to $5,750" (new ensuite), "avoids new plumbing and re-waterproofing - the biggest avoidable cost"
- Replace with: `One Sydney cost guide puts renovating an existing ensuite at {SR('cost','$17,250–$34,500')} with budget to mid-range fittings, and premium jobs at $40,250 to $63,250 (October 2026 prices). Adding a new ensuite costs more: plumbing rough-in alone runs $2,300 to $5,750. Keeping the existing layout avoids new plumbing and re-waterproofing, which the same guide calls the biggest avoidable cost.`

### SHOULD-FIX

**4. Concealed cisterns don't need "an access panel behind the flush plate"**
- Current text: `A concealed cistern needs a framed wall and an access panel behind the flush plate.`
- What's wrong: this is unsourced and misleading. The flush plate itself is the access point. You service the cistern by taking the plate off, and no separate panel is needed.
- Evidence: https://archived.habitusliving.com/products/geberit-concealed: "simply removing the mechanical flush plate provides enough room for repair or maintenance work" and "There is no need to rip tiles from the wall"; https://www.geberitnorthamerica.com/_assets/local-media/brochures/gna7247.pdf: "all working parts are easily accessed through the flush plate or cover plate", "The system fits in 2x4 or 2x6 walls."
- Replace with: `A concealed cistern sits inside a stud wall or a built-out false wall, and its working parts are reached by taking off the flush plate, so no tiles have to come off for a repair.`

**5. Bunnings' "30 per cent more" claim has no link and comes from an image caption**
- Current text: `Choose drawers over doors: Bunnings says drawers hold up to 30 per cent more than cupboards.`
- What's wrong: the claim is real, but it has no link. It's unattributed caption text on a Bunnings article from April 2019, not something Dan Gibney says. Linking it lets readers check it.
- Evidence: https://www.bunnings.com.au/diy-advice/home-improvement/baths-showers-toilets/create-the-perfect-ensuite (Apr 2019, image caption): "For storage, pick drawers, which hold up to 30 per cent more than cupboards."
- Replace with: `Choose drawers over doors: Bunnings says drawers {SR('bun','hold up to 30 per cent more than cupboards')}.`

**6. The 25 L/s link goes to a VBA page that lists roof-space discharge, which NCC 2022 doesn't allow**
- Current text: `the NCC calls for 25 L/s for a bathroom, discharged outside` (link key `vbafan`)
- What's wrong: the VBA news item quotes an older clause, including "(ii) to a roof space that is ventilated in accordance with Ventilation of roof spaces". NCC 2022 Housing Provisions 10.8.2(2) requires discharge "directly or via a shaft or duct to outdoor air" and has no roof-space option. "Discharged outside" is correct for NCC 2022, but the link contradicts it. Link the ABCB clause instead.
- Evidence: https://abcb.gov.au/editions/ncc-2022/adopted/housing-provisions/10-health-and-amenity/part-108-condensation-management: 10.8.2(1)(a) "25 L/s for a bathroom or sanitary compartment"; 10.8.2(2) "discharge directly or via a shaft or duct to outdoor air". https://www.vba.vic.gov.au/news/news/2022/complaints-exhaust-fan-discharge1: "(ii) to a roof space that is ventilated..."
- Replace with: set `SRC['vbafan']` to `https://abcb.gov.au/editions/ncc-2022/adopted/housing-provisions/10-health-and-amenity/part-108-condensation-management`, or add a new key `ncc108` with that URL and use `{SR('ncc108','25 L/s for a bathroom')}`. The text can stay the same.

**7. The Victorian Building Authority is now the Building and Plumbing Commission**
- Current text: `The Victorian Building Authority says to engage a licensed or registered plumber for plumbing work` (link key `vbaplumb`). In svg.py, the footer reads `Example only. Sources: NCC 2022 Housing Provisions, VBA, NSW Government (AS/NZS 3000 zones, waterproofing licence), QBCC, Blueleaf (sizes).`
- What's wrong: the BPC replaced the VBA on 1 July 2025. The same advice now sits on bpc.vic.gov.au, whose footer reads "Victorian Building Authority, trading as the Building and Plumbing Commission". The quote is word-for-word the same.
- Evidence: https://briq.com.au/blog/bpc-one-year-on-what-changed-for-victorian-builders: "It replaced the Victorian Building Authority"; https://www.bpc.vic.gov.au/home-owners/before-you-start-building/engaging-a-plumber: "Make sure you engage a licensed or registered plumber when you want plumbing work carried out."
- Replace with: `Victoria's Building and Plumbing Commission (formerly the VBA) says to {SR('vbaplumb','engage a licensed or registered plumber')} for plumbing work`, and set `SRC['vbaplumb']` to `https://www.bpc.vic.gov.au/home-owners/before-you-start-building/engaging-a-plumber`. In the svg.py footer, change `VBA,` to `Victorian BPC,`. If you make fix 6, the VBA is no longer a source for the diagram at all.

**8. The WELS saving is for a family of four, priced at 2014–15 water rates**
- Current text: `The government's WELS scheme says a 3-star shower that flows at 9L/min will save 70kL and $210 a year compared with an old 15 L/min head.` (key `wels`)
- What's wrong: the figure is for "this family of four", at 8 minutes per shower each a day, priced at "$2.99/kL (the national average price reported in the 2014–15 ... Water Account)". The article leaves out the household and states a dated dollar figure as if it were current.
- Evidence: https://waterrating.gov.au/node/8: "For this family of four, replacing their shower that flows at 15L/min with a new:" … "3-star shower that flows at 9L/min will save 70kL and $210 each year on their water bills."
- Replace with: `The government's WELS scheme says that for a family of four, swapping a 15 L/min shower for a 3-star shower {SR('wels','that flows at 9L/min will save 70kL and $210')} a year, though the dollar figure uses 2014–15 water prices.`

**9. The WELS star rating is national, not a NSW rule**
- Current text: `In NSW, a showerhead of not more than 7.5 litres per minute is rated WELS 4 stars.` (key `basix`)
- What's wrong: WELS ratings come from the national standard (AS/NZS 6400). The NSW BASIX page only explains them. "In NSW" reads as if the rating were state-specific. The page also attaches a spray-force and coverage condition to the rating.
- Evidence: https://www.planningportal.nsw.gov.au/basix-water/fixtures/showerheads: "A showerhead with a nominal flowrate of not more than 7.5 litres per minute is rated WELS 4 stars" (cites AS6400:2016)
- Replace with: `Under the national WELS standard, as the NSW Planning Portal explains, a showerhead with a flow of {SR('basix','not more than 7.5 litres per minute is rated WELS 4 stars')}.`

**10. Kate Bath's quote doesn't support "keep colour to one wall"**
- Current text: `If you want colour, keep it to one wall: Kate Bath of Blue Tea Kitchens and Bathrooms used wall tiles sparingly, to make the room feel larger.` (key `hb`)
- What's wrong: Kate Bath is correctly named. She's quoted in the body text ("Kate Bath, interior designer at Blue Tea Kitchens and Bathrooms"), not in a photo credit. But the bathroom she describes is white, and she says nothing about colour on one wall. It's a family bathroom, not an ensuite.
- Evidence: https://www.homebeautiful.com.au/bathroom-ideas/small-bathroom-design-ideas/ (29 May 2025): "I used wall tiles sparingly, to make the room feel larger."
- Replace with: `Go easy on wall tiles too: interior designer Kate Bath of Blue Tea Kitchens and Bathrooms told Home Beautiful she {SR('hb','used wall tiles sparingly, to make the room feel larger')} in a small family bathroom.`

**11. "None of them needs the plumbing moved" overstates it**
- Current text: `Together they free up the most floor and light, and none of them needs the plumbing moved.`
- What's wrong: this is unsourced and too absolute. A frameless screen and a cavity slider don't touch the plumbing. But replacing a floor-standing vanity with a wall-hung one often means moving the waste and water points up into the wall. Running one floor tile into the shower usually means regrading and re-waterproofing the shower floor. (This is general trade knowledge; I found no single source for it.)
- Replace with: `Together they free up the most floor and light, and none of them needs the toilet or shower moved.`

### MINOR

**12. The 150 mm vanity-wall rule only applies when the basin is within 75 mm of the wall (diagram and desc)**
- Current text (svg.py): `• Vanity wall: 150 mm above the basin`. In the desc: `the wall behind a vanity water resistant 150 mm above the basin`
- Evidence: https://ncc.abcb.gov.au/editions/ncc-2022/adopted/housing-provisions/10-health-and-amenity/part-102-wet-area-waterproofing: "Walls must be water resistant to a height of not less than 150 mm above the vessel" … "where the vessel is within 75 mm of a wall"
- Replace with: `• Basin within 75 mm of wall: 150 mm up` and, in the desc, `the wall behind a basin within 75 mm of it water resistant to 150 mm above the basin`

**13. The trigger for the 10-minute run-on is "no natural ventilation", not "no window"**
- Current text (svg.py): `• No window? 10-minute fan run-on`
- What's wrong: 10.8.2(4) applies when the room isn't naturally ventilated under 10.6.2(a) and the fan doesn't run continuously. A small or fixed window doesn't count as natural ventilation. The fan must also be interlocked with the light. The body text ("a room without enough outdoor air") is fine.
- Evidence: ABCB 10.8 page (link in item 6): "continues to operate for 10 minutes after the light switch is turned off"; https://cpd.nccb.gov.au/news/2022/improved-condensation-management-ncc-2022: "which don't have sufficient access to outdoor air ... must be controlled to turn on when the lights in the room are turned on."
- Replace with: `• Not naturally ventilated? 10-min run-on`

**14. Bagnato wrote the Houzz piece himself (2018), and his narrow-room advice is "no bath"**
- Current text: `architect Dominic Bagnato told Houzz that a shower, basin and toilet need` and `a shower-only layout may be the realistic choice.`
- What's wrong: Bagnato is the article's author, a Houzz contributor writing on 28 Jan 2018 (Bagnato Architecture & Interiors), so "told Houzz" is wrong. In a narrow room he says to skip the bathtub and install only a shower. "Shower-only layout" could be read as no toilet or basin.
- Evidence: https://www.houzz.com.au/ideabooks/96027874/thumbs/7-key-things-to-establish-before-you-plan-an-ensuite: "To comfortably accommodate a shower, basin and toilet, you will need a minimum floor area of 3 square metres." and "If space is particularly tight or if the room is narrow (1 metre or less) or has a sloping roof," (the sentence goes on to advise a shower instead of a bath)
- Replace with: `architect Dominic Bagnato, writing for Houzz, says a shower, basin and toilet need`, and `it's best to skip the bath and fit a shower only.`

**15. Bowers' title, and two paraphrases that drift from what she said**
- Current text: `Designer Sophie Bowers of Strutt Studios told Better Homes and Gardens that by placing a toilet near the doorway, your focus will be drawn to the rest of the room, not the loo.` Also: `in a small ensuite, because they add storage without taking floor space.`
- Evidence: https://www.bhg.com.au/homes/renovating/ensuite-bathrooms/: she's described as "managing director of Sydney-based interior architecture and design firm, Strutt Studios". "By placing a toilet near the doorway, your focus will be drawn to the more decorative elements such as the basin and vanity..." "The opportunity for storage is usually limited, so mirrored shaving cabinets are an excellent solution to maximise light and add storage without cluttering the room."
- Replace with: `Sophie Bowers, managing director of Sydney design firm Strutt Studios, told Better Homes and Gardens that {SR('bhg','by placing a toilet near the doorway, your focus will be drawn')} to the more decorative elements, such as the basin and vanity.` For the second sentence: `in a small ensuite, because they maximise light and add storage without cluttering the room.`

**16. Christie Wood doesn't give "fewer visible lines" as her reason for matching grout**
- Current text: `and that she always recommends matching the grout to the tile so there are fewer visible lines.`
- Evidence: https://www.houzz.com.au/ideabooks/116118984/thumbs/how-do-i-choose-tiles-for-a-small-bathroom: "I always recommend matching the colour of the grout to the tile," followed by "unless you want to highlight the shape or layout of the tiles."
- Replace with: `and that she always recommends matching the grout colour to the tile unless you want to highlight the tiles' shape or layout.`

**17. The cavity slider width range comes from one supplier, but reads as true of all of them**
- Current text: `Cavity slider units are sold in widths from 620 to 920 mm, such as a`
- What's wrong: 620–920 mm is the range in one retailer's listing. Other makers differ: CS for Doors offers standard sizes of 610–910 mm and custom sizes up to 1000 mm.
- Evidence: https://tradecentre.idlvr.com.au/collections/cavity-units (widths 620, 720, 770, 820, 870 and 920 mm; "720 x 90 mm Cavity Sliding Door Unit - Flush Jamb"); https://www.eboss.co.nz/ebossnow/cs-for-doors-cavity-slider-saves-space-bathroom-renovation ("1980mm high x 610-910mm wide")
- Replace with: `One supplier lists cavity slider units in widths from 620 to 920 mm, such as a`

**18. The QBCC figure needs its year**
- Current text: `the QBCC says bathroom home warranty claims averaged almost $25,000 in rectification costs`
- Evidence: https://www.qbcc.qld.gov.au/news/waterproofing-done-right (24 Feb 2026): "Each residential bathroom claim finalised under the Queensland Home Warranty Scheme during the 2024–25 financial year" … "averaged almost $25,000 in rectification costs"
- Replace with: `the QBCC says bathroom claims finalised under its home warranty scheme in 2024–25 averaged almost $25,000 in rectification costs`. The anchor text inside the link stays the same.

**19. The NCC wording is "readily removable", not "lift off"**
- Current text (body): `its door has to slide, open outwards or lift off`
- Evidence: https://www.nccb.gov.au/news/2019/construction-sanitary-compartments: "open outwards or slide" or "be readily removable from the outside of the compartment"; NCC 2022 10.4.2: "unless there is a clear space of at least 1.2 m, measured in accordance with Figure 10.4.2, between the closet pan ... and the doorway."
- Replace with: `its door has to open outwards, slide or be readily removable from outside (usually with lift-off hinges)`. The diagram's shorthand, "door slides, opens out or lifts off", is acceptable as it is.

**20. "Plumbing is the expensive part of any ensuite" has no source**
- Current text: `Plumbing is the expensive part of any ensuite.`
- What's wrong: the Houzz quote from Merlin that follows is about circulation space, not cost. Her full line is "keeps circulation space on the opposite side of the room".
- Replace with: `Moving plumbing is one of the biggest costs in an ensuite renovation.` Optionally link it with `SR('cost', ...)`, which supports "avoids new plumbing and re-waterproofing - the biggest avoidable cost".

**21. The niche framing claim has no source**
- Current text: `A niche needs a stud-free wall cavity or a nib wall`
- What's wrong: this is stated as a requirement but no source is given. In practice a niche is set between studs, with noggings, or built into a nib wall.
- Replace with: `A niche is usually built between wall studs or into a nib wall`

**22. The NSW licence threshold leaves out what the $5,000 covers**
- Current text: `In NSW you need a contractor licence for waterproofing work valued at more than $5,000`
- Evidence: https://www.nsw.gov.au/business-and-economy/licences-and-credentials/building-and-trade-licences-and-registrations/waterproofing-work: "valued at more than $5000 in labour and materials (including GST)"
- Replace with: add ` in labour and materials (including GST)` after the link.

---

## Verified claims (no change needed)

- Blueleaf: "Most Australian ensuites sit between 3 and 5 m²", and "A compact ensuite at around 1.8 x 2.0 m (3.6 m²) fits a toilet, vanity and 900 x 900 mm shower". This supports the intro, the diagram subtitle, the "3.6 m²: within the 3 to 5 m²" note and the paragraph under the diagram.
- Blueleaf: "Standard shower size in Australia is 900x900mm."; "Ensuite: 600–900mm wide, 460–500mm deep"; "Slimline depth (under 460mm) suits powder rooms, narrow ensuites..."; niche "Height: 150-300mm".
- Tile Cloud: "Base of niche: 900mm to 1100mm from FFL".
- NCC 2022 10.2.2: "The walls of the shower area must be waterproof not less than 1800 mm above the floor substrate"; "The floor of the shower area must be waterproof, including any hob or step-down"; waterstop "a minimum horizontal distance of 1500 mm from the shower rose". The diagram's Part 10.2 lines are correct, apart from the 150 mm caveat in item 12.
- NCC 2022 10.4.2 (Construction of sanitary compartments): the clause number in the diagram is right, and the 1.2 m clear-space wording matches. In the diagram, the pan is about 450 mm from the doorway, so "under 1.2 m" is consistent and the slider is justified.
- NCC 2022 10.8.2: 25 L/s for a bathroom; discharge to outdoor air; light interlock and 10-minute run-on (ABCB pages).
- AS/NZS 3000 zones (NSW Government summary): switches are "Not permitted" in Zones 0 and 1; Zone 2 is "a 0.6 m semicircle outside the door" or "a 0.6 m-wide band beside the barrier". The diagram line is correct.
- Licensing: NSW requires a contractor licence for waterproofing over $5,000. The QBCC has a waterproofing licence class ("Apply, install and repair waterproofing, including surface preparation..."). Victoria requires a licensed or registered plumber (BPC). Ausgrid: "DIY electrical is not only dangerous, it's illegal." The diagram's "Licensed plumber and electrician" line is fine.
- Houzz (136583044): Kirsten Johnstone, architect: "Do wall-mount your vanity and toilet pan" (reason: "makes your ensuite look larger, plus it's easier to clean"), "Do include a shower ledge or recessed alcove", and "I prefer to locate skylights to capture southern light" (first person, in her section). Laura Merlin, interior designer at Origin Bathrooms: "Placing the basin, toilet and shower along one wall keeps circulation space...". Ari Zorlu, managing director of Paco Jaanson: "Do opt for neutrals for longevity".
- Houzz tiles: Christie Wood, strategic designer at Beaumont Tiles: "Slab tiles of 800x1,600 millimetres and above are a brilliant choice for walls in small bathrooms."
- BHG cost article (2018): Kia Howat, interior designer at GIA Bathrooms and Kitchens: "Maintaining the placement of your existing toilet, shower and vanity waste locations".
- RACV small bathroom article: Kate Walker (designer, KWD): "Entering front-on to your vanity creates more circulation space". Andy Anderson (RACV Trades Training Manager): "A clear glass frame allows you to take the whole room in..." and "A skylight is a fairly inexpensive way to attract natural light".
- RACV heated towel rails (2 June 2025), Kieran Davies, Head of RACV Trades: a 200 W rail "running all day" at "35 cents per kilowatt-hour" costs "around $1.68". The arithmetic checks out (0.2 kW x 24 h x $0.35 = $1.68).
- Bunnings (Apr 2019), Dan Gibney, Bunnings bathroom buyer, in the body text: "Doors and frames on showers in small spaces can create a closed-in feel."; "Opt for a wall-hung vanity and a concealed cistern"; "Large tiles in cool colours will bounce light around the room". This covers "Bunnings suggests...", which is acceptable.
- Three Birds: the in-wall cistern quote is exact. Only the "their own" framing is wrong (item 1).
- Home Beautiful: Kate Bath is a real speaker named in the body text, not a photo credit. Only the framing is wrong (item 10).
- QBCC: "averaged almost $25,000 in rectification costs" is exact.
- Whatsthedamage: $17,250–$34,500 for Sydney ensuite renovations (October 2026) is exact.
- Cavity unit: "720 x 90 mm Cavity Sliding Door Unit - Flush Jamb" is listed.
- Diagram geometry in svg.py: shower 900 x 900, vanity 600 x 460, 720 mm slider on the bottom wall with its pocket on clear wall, room 1.8 x 2.0 m. All match the desc and labels.
- Structure: there are 10 numbered ideas under Layout, Shower, Storage and Finishes, as the intro says.
