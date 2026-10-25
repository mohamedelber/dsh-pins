# Fact-check: "Small Bathroom Ideas" (dailyspacehacks.com)

Checked 2026-10-26 against the live pages listed. Every URL below came back from a WebSearch in this session and was fetched with WebFetch. Code text comes from ICC-hosted documents, state adoptions of the IRC and code explainers (codes.iccsafe.org was not reachable).

The article is built from `build.py` (prose) and `svg.py` (diagram, written to `z.svg`). After any svg.py change, run svg.py and then build.py. Text strings below are copied exactly as they appear in build.py and svg.py. Where a link has to change, the SRC key is given.

Severity: **MUST-FIX** = wrong or misleading as published. **SHOULD-FIX** = a quote or attribution the page doesn't support, or a weak source for a code claim. **MINOR** = wording, precision, or a better source exists.

---

## Issues

### 1. MUST-FIX: The diagram's own layout breaks the code minimum it cites (toilet to vanity is 14 in)
- **Where:** `svg.py` line 27: `vx,vy=P(0,62)`. The `desc` text is `with its sink centerline 22 inches from the end wall`.
- **What's wrong:** The toilet centerline is drawn at y = 48 in (`tx,ty=P(0,48)`) and the vanity starts at y = 62 in. That puts the toilet centerline **14 in** from the side of the vanity. The IRC requires at least 15 in from a toilet's centerline to "any side wall, partition or vanity", and the panel on the right of the same diagram says "Toilet center to side: 15 in". The drawn toilet-to-sink spacing is also only 26 in center to center (48 in to 74 in), but the IRC requires at least 30 in between adjacent fixtures. The diagram shows a layout that fails inspection while presenting itself as the "measured" example.
- **Evidence:**
  - 2018 IRC P2705.1 item 5, as adopted by Oklahoma (no amendment to item 5): https://regulations.justia.com/states/oklahoma/title-748/chapter-20/subchapter-6/section-748-20-6-32 — "A water closet lavatory or bidet shall not be set closer than 15 inches (381 mm) from its center to any side wall, partition … or vanity or closer than 30 inches (762 mm) center-to-center between adjacent fixtures."
  - 2021 IRC paraphrase: https://buildingcodetrainer.com/minimum-toilet-clearances/ — "A toilet shall not be set closer than 15 inches from its center to any side wall, partition or vanity."
- **Suggested fix (option A, a single change):** In svg.py, change `vx,vy=P(0,62)` to `vx,vy=P(0,66)`. The vanity then runs from 66 to 90 in, so the toilet centerline is 18 in from the vanity (meets both code and NKBA), sink-to-toilet is 30 in center to center, the sink centerline is 18 in from the end wall (code 15 in; NKBA's 20 in is not met), and there is still 39 in clear in front. I checked the label positions and nothing collides. Then change the desc text from `with its sink centerline 22 inches from the end wall` to `with its sink centerline 18 inches from the end wall and 30 inches from the toilet centerline`. Also add `The vanity starts 18 inches from the toilet centerline.` after `so all the plumbing is on one wall.`
  - Option B, which meets NKBA at the sink instead: toilet at 46 in (16 in from the tub, so code is met but NKBA is not), vanity from 64 to 88 in, sink at 76 in (20 in from the end wall). Option A keeps the "18 in to centerline" callout that's already drawn, so it's simpler.

### 2. MUST-FIX: The Janelle Hughes quote is used to argue the opposite of what she said
- **Current text:** `But small rooms can also take color: designer Janelle Hughes told Apartment Therapy that {SR('at','in smaller spaces, you really have to use color as your friend')}.` (Visible: "But small rooms can also take color: designer Janelle Hughes told Apartment Therapy that in smaller spaces, you really have to use color as your friend.")
- **What's wrong:** On the source page the quote sits in the "dark wall colors" section. There, Hughes advises **lighter** colors for a small bathroom without a window. The article uses it to say small rooms can take bold color. Also, she is identified as co-owner of KJ Design & Mortar Styling, and the headline calls her a home stager, not a designer.
- **Evidence:** https://www.apartmenttherapy.com/things-making-bathroom-feel-smaller-36864237 — "In smaller spaces, you really have to use color as your friend," given as advice to stick to lighter colors in a windowless small bathroom.
- **Suggested replacement:** `Home stager Janelle Hughes of KJ Design &amp; Mortar Styling agrees for windowless baths, telling Apartment Therapy that {SR('at','in smaller spaces, you really have to use color as your friend')}, which for her means lighter shades. Small rooms can still take one bold move:` Then continue with the Melissa Miranda sentence (see #15).

### 3. SHOULD-FIX: Code minimums are sourced to Bob Vila, and Bob Vila doesn't say "centerline"
- **Current text (build.py, the paragraph under the diagram):** `Building codes set the minimum: the code allows {SR('bv','a minimum of 21 inches')} of clear space in front of a toilet or sink and a toilet centerline 15 inches from a side wall.`
- **Diagram footer (svg.py line 50):** `Sources: Bob Vila (NKBA and code figures), HVI (fans), EPA WaterSense, NEC 210.8 (GFCI), IRC P2708 (showers).`
- **What's wrong:** Bob Vila is a secondary source for code. Its 15-in toilet figure is "Codes allow a minimum distance of 15 inches" and doesn't say it is measured from the centerline. The real requirement is IRC R307.1/Figure R307.1 together with P2705.1 item 5, which includes "or vanity". That wording matters for #1.
- **Evidence:** https://bobvila.com/articles/15445-the-basics-of-bathroom-design — "The building code allows for a minimum of 21 inches." / "Codes allow a minimum distance of 15 inches." Better: https://buildingcodetrainer.com/minimum-toilet-clearances/ (2021 IRC, R307.1/P2705.1) — "A toilet shall not be set closer than 15 inches from its center to any side wall, partition or vanity."
- **Suggested fix:** Add `"wc":"https://buildingcodetrainer.com/minimum-toilet-clearances/"` to SRC. Then write: `Building codes set the minimum: the IRC allows 21 inches of clear space in front of a toilet or sink and says {SR('wc','a toilet shall not be set closer than 15 inches from its center to any side wall, partition or vanity')}.` In the svg.py footer, change `Bob Vila (NKBA and code figures)` to `IRC R307.1 and P2705.1 (code), NKBA via Bob Vila` (or drop "HVI (fans)" if the line gets too long).

### 4. SHOULD-FIX: Schluter doesn't say linear drains let you use large tiles
- **Current text:** `and that linear drains let the shower floor pitch in one direction, so you can use large tiles.`
- **What's wrong:** The page says linear drains let the floor pitch in one direction. It says nothing about large tiles. That part is the writer's inference, attributed to Schluter.
- **Evidence:** https://www.schluter.com/schluter-us/en_US/curbing-the-curb — "Linear drains let the shower floor pitch in one direction". The page has no mention of large tiles.
- **Suggested replacement:** `and that linear drains let the shower floor pitch in one direction. A single-plane slope is what makes large floor tiles practical in a shower.` This keeps the claim as our own and doesn't attribute it to Schluter. Or simply end after "one direction".

### 5. SHOULD-FIX: Tom Silva didn't say "cheap" pocket doors
- **Current text:** `Buy good hardware: This Old House's Tom Silva warns that on cheap pocket doors, {SR('tohl','often, a screw falls out or the door comes off the track')}.`
- **What's wrong:** The source never uses "cheap", "inexpensive" or "old". Silva is talking about pocket-door hardware in general, and he recommends newer nylon-wheeled hardware.
- **Evidence:** https://www.thisoldhouse.com/bathrooms/how-to-make-a-small-bathroom-look-larger — "This Old House contractor Tom Silva has long championed pocket doors for tight spaces, though he cautions about hardware quality: "Often, a screw falls out or the door comes off the track," he says." / "Tom recommends investing in newer nylon-wheeled hardware systems".
- **Suggested replacement:** `Buy good hardware: This Old House contractor Tom Silva warns that with poor pocket-door hardware, {SR('tohl','often, a screw falls out or the door comes off the track')}, and recommends newer nylon-wheeled systems.`

### 6. SHOULD-FIX: Lynn Kirincich is presented as This Old House staff
- **Current text:** `This Old House's Lynn Kirincich says {SR('tohl','stopping the shower wall short and topping it with glass')} keeps an open feel.`
- **What's wrong:** The page identifies her as "Lynn Kirincich of Wayne, N.J.", a homeowner sharing her experience. She isn't a This Old House staffer or expert.
- **Evidence:** https://www.thisoldhouse.com/bathrooms/how-to-make-a-small-bathroom-look-larger — "Stopping the shower wall short and topping it with glass preserves an open feel in the space."
- **Suggested replacement:** `Homeowner Lynn Kirincich of Wayne, N.J., told This Old House that {SR('tohl','stopping the shower wall short and topping it with glass')} preserves an open feel.`

### 7. SHOULD-FIX: The Gina Shaw quote drops "perhaps"
- **Current text:** `Gina Shaw of York Wallcoverings told This Old House that wallpaper is {SR('tohw','the single most dramatic statement you can make in a small space')}.`
- **What's wrong:** She hedged. Dropping "perhaps" makes the claim absolute.
- **Evidence:** https://www.thisoldhouse.com/walls/don-t-be-afraid-to-wallpaper-your-powder-room — "Wallpaper offers perhaps the single most dramatic statement you can make in a small space," she says.
- **Suggested replacement:** `Gina Shaw of York Wallcoverings told This Old House that wallpaper offers perhaps {SR('tohw','the single most dramatic statement you can make in a small space')}.`

### 8. SHOULD-FIX: The EPA sentence is garbled and leaves out the basis for the 13,000 gallons
- **Current text:** `The EPA's WaterSense label means {SR('epa','toilets to use 1.28 gallons per flush or less')}, which saves a household nearly 13,000 gallons a year,`
- **What's wrong:** "The label means toilets to use…" isn't grammatical. The EPA page says "Design improvements have allowed toilets to use 1.28 gallons per flush or less", and WaterSense labels toilets at that level. The 13,000-gallon figure is the savings for an average family that **replaces old, inefficient toilets**. It isn't a property of the label itself.
- **Evidence:** https://www.epa.gov/watersense/residential-toilets — "Design improvements have allowed toilets to use 1.28 gallons per flush or less" / "that's nearly 13,000 gallons of water savings for your home every year".
- **Suggested replacement:** `WaterSense-labeled toilets use 1.28 gallons per flush or less (the EPA notes that design improvements have allowed {SR('epa','toilets to use 1.28 gallons per flush or less')}), and replacing older toilets with them saves an average family nearly 13,000 gallons a year,`. A shorter version: `WaterSense toilets use 1.28 gallons per flush or less; EPA says replacing old toilets with them saves an average family {SR('epa','nearly 13,000 gallons of water')} a year,`. If the anchor changes, check it against the page wording ("nearly 13,000 gallons of water savings").

### 9. SHOULD-FIX: The wall-hung toilet claim ("thicker wall") is unsourced and not always true
- **Current text:** `It needs a thicker wall or a frame to carry the tank and bowl, so it is easiest to add in a full remodel.`
- **What's wrong:** The cited Pro Builder piece describes an adjustable-height frame bolted to the studs and floor, and says installation means breaking into the wall. Geberit makes carriers for both 2x4 and 2x6 walls, so a thicker wall isn't required. The sentence carries no link.
- **Evidence:** https://www.probuilder.com/products/kitchen-baths/article/55226747/pros-and-cons-wall-hung-toilets — an "adjustable-height frame" that is "bolted to the wall studs and the floor"; installation "is more involved because contractors need to break into the wall". https://learn.geberitnorthamerica.com/blog/wall-hung-bathroom-fixture-installation-demystified — "the steel-framed toilet carrier system that holds the water tank and all the mechanical parts" / requirements depend on "stud depth (2x4 or 2x6)" / for retrofits, "plan to modify the drain-waste-vent layout to accommodate the carrier system."
- **Suggested replacement:** `It needs a steel in-wall carrier that holds the tank and carries the bowl, and the drain usually has to be rerouted, so it is easiest to add in a full remodel.` Optionally link "steel in-wall carrier" to the Geberit page (new SRC key, e.g. `"geb"`).

### 10. SHOULD-FIX: The niche "insulation" reason is unsourced, and an expert source gives a different reason
- **Current text:** `Plan it before the walls are tiled, on an interior wall, and keep it out of an exterior wall where insulation needs the space.`
- **What's wrong:** No link is given. The sentence also says the same thing twice ("on an interior wall" and "out of an exterior wall"). A kitchen and bath designer writing in Fine Homebuilding gives the reason as protecting the water and vapor barriers, not making room for insulation.
- **Evidence:** Mary Jo Peterson, CKD, CBD, "Preventing Moisture Problems in Bathrooms", *Fine Homebuilding*, Fall/Winter 2002 (hosted by GreenBuildingAdvisor): https://images.greenbuildingadvisor.com/app/uploads/2021/10/25190610/Preventing-Moisture-Problems-in-Bathrooms.pdf — "I never design these niches to be set into an exterior wall." / "Soap and shampoo cubbies must not compromise the water or vapor barriers."
- **Suggested replacement:** `Plan it before the walls are tiled, and put it on an interior wall: bath designer Mary Jo Peterson writes in Fine Homebuilding that she {SR('niche','never design[s] these niches to be set into an exterior wall')}, because a niche must not compromise the water or vapor barrier.` Add SRC key `"niche"` pointing to the PDF above. Or skip the quote and just write `put it on an interior wall, where it won't cut into the exterior wall's insulation and vapor barrier.`

### 11. SHOULD-FIX: The anti-scald rule is cited "under the IRC" to a South Carolina regulation
- **Current text:** `New shower valves must limit hot water to {SR('scald','120°F')} under the IRC to prevent scalds.` (SRC key `scald` = https://www.law.cornell.edu/regulations/south-carolina/R-8-1243)
- **What's wrong:** The 120°F limit is right, but the link goes to South Carolina's codified regulation (S.C. Code Regs. 8-1243, titled "IRC P2708.4"), which is a state adoption and not the model IRC. The subsection number also changes between editions: one 2018 IRC index lists shower anti-scald valves under P2708.3 (https://www.jaspector.com/codes/irc-2018/ch27-plumbing-fixtures/). The article doesn't give a subsection number, so leave it that way.
- **Evidence:** https://www.law.cornell.edu/regulations/south-carolina/R-8-1243 — "Shower and tub/shower combination valves required by this section shall be equipped with a means to limit the maximum setting of the valve to 120°F (49°C)". ICC's own Building Safety Journal (https://www.iccsafe.org/building-safety-journal/bsj-technical/week-three-building-safety-month-event-covers-hot-water-safety/) confirms the matching 120°F limit for tub valves (P2713.3) and refers to P2708.4 for tub/shower valves.
- **Suggested replacement:** `Shower and tub/shower valves must be pressure-balance or thermostatic types that limit the maximum setting to 120°F, a rule from the IRC that states adopt, as in {SR('scald','South Carolina\'s code')}.` Or keep the current sentence but change the anchor to `limit the maximum setting to 120°F` and add "(as adopted in South Carolina)". In the svg.py "Also check" list, `Shower valve: anti-scald, max 120°F` is fine.

### 12. SHOULD-FIX: The diagram's "Door width: NKBA 32 in" is a clear-opening figure, not a door width
- **Current text (svg.py rows):** `("Door width","—","32 in")`
- **What's wrong:** NKBA's 32 in is the **clear opening**. Bob Vila says the door itself should therefore be at least 34 in, unless it is a pocket door. Labeled as "door width" next to a "32 in pocket door", the row tells readers a 32-in swinging door meets NKBA, which it doesn't. (The "—" under Code is fine: the IRC sets no bathroom door width.)
- **Evidence:** https://www.bobvila.com/articles/15445-the-basics-of-bathroom-design.md — "a bathroom door opening should be at least 32 inches wide when measured from the open door to the opposite stop." / "That means the door itself should be at least 34 inches wide".
- **Suggested replacement:** `("Door clear opening","—","32 in")`.

### 13. SHOULD-FIX: Block Renovation doesn't call Layout 1 "the cheapest"
- **Current text:** `and it is the cheapest to build because the drain and supply lines share one wall.`
- **What's wrong:** The source makes a softer claim.
- **Evidence:** https://www.blockrenovation.com/guides/5x7-bathroom-floor-plans-layouts-fixture-guide — "contractors will quote it most competitively because every wet fixture shares one plumbing wall." Also: "keeping fixtures on the same walls is meaningfully cheaper."
- **Suggested replacement:** `and Block says contractors quote it most competitively because every wet fixture shares one plumbing wall.`

### 14. MINOR: Hughes's mirror quote gets a reason she didn't give, and her title is off
- **Current text:** `Hughes suggests {SR('at','a really large round mirror above your vanity')} to bounce light around.`
- **What's wrong:** She gives the large mirror as an example of a bold mirror choice. She doesn't say it bounces light.
- **Evidence:** https://www.apartmenttherapy.com/things-making-bathroom-feel-smaller-36864237 — "You can do a really large round mirror above your vanity".
- **Suggested replacement:** `Hughes suggests going big with {SR('at','a really large round mirror above your vanity')}; a bigger mirror also bounces more light around.`

### 15. MINOR: Melissa Miranda isn't HGTV staff
- **Current text:** `HGTV's Melissa Miranda says {SR('hgtv','powder rooms are usually where I really go all out')},`
- **Evidence:** https://www.hgtv.com/decorating/bathrooms/small-bathroom-design-pictures — she is identified as an interior designer. "Powder rooms are usually where I really go all out, break all the rules…"
- **Suggested replacement:** `Interior designer Melissa Miranda told HGTV that {SR('hgtv','powder rooms are usually where I really go all out')},`

### 16. MINOR: The pocket-door limitation is overstated
- **Current text:** `and you can't use one where pipes or wires run through the wall.`
- **Evidence:** https://www.bobvila.com/articles/installing-a-pocket-door.md — a wall is a poor candidate if "Pipes or electrical wires run through it." Rerouting them "add[s] to the installation cost."
- **Suggested replacement:** `and a wall with pipes or wires in it is a poor candidate unless you pay to reroute them.`

### 17. MINOR: Sconce height has no clear referent, and the sources disagree
- **Current text:** `the American Lighting Association, via Houzz, recommends {SR('houzzl','mounting them 65 to 70 inches from the floor')} and 28 to 30 inches apart.`
- **What's wrong:** "them" has no antecedent in our sentence (on the source page it refers to sconces). Rick Kovac of Golden Lighting, who is cited in the next sentence, gives 60 to 66 in to the fixture's center. Houzz also adds that the 28 to 30 in spacing "depends on the size of the room".
- **Evidence:** https://www.houzz.com/magazine/how-to-choose-your-bathroom-vanity-lighting-stsetivw-vs~94643748 — "The American Lighting Association recommends mounting them 65 to 70 inches from the floor as a general rule." https://goldenlighting.com/blogs/the-golden-edit/bathroom-sconce-placement-2 — "Mount side sconces at 60 to 66 inches from the finished floor to the center of the fixture."
- **Suggested replacement:** `the American Lighting Association, via Houzz, recommends mounting sconces {SR('houzzl','65 to 70 inches from the floor')} as a general rule and 28 to 30 inches apart (Golden Lighting puts the fixture center a little lower, at 60 to 66 inches).`

### 18. MINOR: The color temperature advice gives only one side of a disagreement
- **Current text:** `Rick Kovac of Golden Lighting suggests {SR('gold','a warm 2700K to 3000K color temperature')}.`
- **Note:** The quote and attribution are correct (Kovac is COO, and the full phrase is "aim for a CRI of 90 or higher at a warm 2700K to 3000K"). But This Old House, which the same paragraph cites, recommends "cool white bulbs (around 3,000K–4,000K)" (https://www.thisoldhouse.com/bathrooms/how-to-make-a-small-bathroom-look-larger). Optionally add `and a CRI of 90 or higher`. You could also note that 3000K is where the two recommendations overlap.

### 19. MINOR: The Cost vs Value link has a double slash
- **SRC key `cvv`:** `https://www.jlconline.com//cost-vs-value/2025` should be `https://www.jlconline.com/cost-vs-value/2025/`.
- The figures are verified (see below). The 2026 report isn't out: jlconline's year selector stops at 2025 (checked 2026-10-26).

### 20. MINOR: The ESFi wording implies causation and leaves out the date range
- **Current text:** `ESFi credits GFCIs with an {SR('esfi','81% drop in electrocutions')} since they were first required in bathrooms in 1975.`
- **Evidence:** https://www.esfi.org/ground-fault-circuit-interrupters-what-if-gfcis-did-not-exist/ — "81% drop in electrocutions since the introduction of GFCI protection in bathrooms in 1975 and 2024" and "first introduced in the bathrooms of homes as required by the 1975 edition of the National Electrical Code".
- **Suggested replacement:** `ESFi reports an {SR('esfi','81% drop in electrocutions')} between 1975, when GFCIs were first required in bathrooms, and 2024.` The text says "Bathroom outlets must be GFCI protected" without a link. It's correct (NEC 210.8(A)(1), which covers all 125 to 250 V receptacles in bathrooms since the 2020 NEC; https://iaeimagazine.org/electrical-fundamentals/nec-requirements-for-gfci-protection-section-210-8). Consider linking it.

### 21. MINOR: The diagram says shower walls are "water-resistant", but code says "nonabsorbent", and R307.2 isn't credited
- **Current text (svg.py):** `"Shower walls: water-resistant to 6 ft"`
- **Evidence:** IRC R307.2 (Richland WA handout): https://www.richlandwa.gov/home/showpublisheddocument/17279/638864566397300000 — "Bathtub and shower floors and walls above bathtubs with installed shower heads and in shower compartments shall be finished with a nonabsorbent surface. Such wall surfaces shall extend to a height of not less than 6 feet above the floor."
- **Suggested replacement:** `"Tub/shower walls: nonabsorbent to 6 ft"`. Add `IRC R307.2` to the footer sources.

### 22. MINOR: The mosaic tile description doesn't match the source
- **Current text:** `Stacking narrow tiles vertically has the opposite trick; This Old House notes a vertical pattern {SR('tohm','draws the eye upward, making the ceiling appear higher')}.`
- **What's wrong:** The source talks about rectangular **mosaic** tiles stacked vertically. "Opposite trick" doesn't fit, because large tiles and vertical stacking aren't opposites.
- **Evidence:** https://www.thisoldhouse.com/bathrooms/5-ways-mosaic-tile-makes-a-small-bath-look-big — "stacking rectangular tiles vertically is a great option." / "This technique draws the eye upward, making the ceiling appear higher."
- **Suggested replacement:** `Small tiles can work too: This Old House says stacking rectangular mosaic tiles vertically {SR('tohm','draws the eye upward, making the ceiling appear higher')}.`

### 23. MINOR: Unsourced claim about why small baths are 5 ft wide
- **Current text:** `alcove tub fits wall to wall, which is why so many small bathrooms are exactly that width.`
- **Suggested replacement:** `alcove tub fits wall to wall, which is why 5 feet is such a common width for a small full bath.` This keeps it as reasoning rather than stated fact. Note that This Old House gives 5x8 and 6x6 as typical, so not all small baths are 5 ft wide.

### 24. MINOR: "Blocks half the room" overstates the source
- **Current text:** `A shower curtain blocks half the room from view.`
- **Evidence:** The Houzz page says a curtain acts as a visual wall even when open (https://www.houzz.com/magazine/12-ways-to-make-any-bathroom-look-bigger-stsetivw-vs~84997339).
- **Suggested replacement:** `A shower curtain acts as a visual wall, even when it's open.`

### 25. MINOR: Unsourced claim about the swinging glass door
- **Current text:** `A single fixed panel is simplest: a swinging glass door needs floor to open into.`
- **Note:** This is plainly true, and a source exists if you want one: JLC, "Fighting for Inches" (Lena Savage, April 1, 1996), https://www.jlconline.com/how-to/plumbing/fighting-for-inches-a-guide-to-small-bathroom-design_o/ — "But in reality, it's the swing of the shower door that eats up the space." Optional: `a swinging glass door needs floor to open into; as JLC put it, {SR('jlc','it's the swing of the shower door that eats up the space')}.`

### 26. MINOR: The company name and date for the Pro Builder quote
- **Current text:** `Peter Christofferson of Chicago Faucet says`
- **Evidence:** https://www.probuilder.com/products/kitchen-baths/article/55226747/pros-and-cons-wall-hung-toilets (Oct. 26, 2018) — "marketing services manager for the Chicago Faucet Company". Both quotes are verbatim.
- **Suggested replacement:** `Peter Christofferson of the Chicago Faucet Company told Pro Builder` (optional).

### 27. MINOR: The pocket drawn in the diagram runs alongside the tub
- **Where:** `svg.py` line 33, `dx,dy=P(60,58)`. The pocket is drawn from y ≈ 26.7 to 58.7 in, and the tub occupies y = 0 to 30 in on the same wall.
- **What's wrong:** About 3 in of the pocket sits behind the tub's tiled end wall and flange. Bob Vila says a 32-in pocket door needs 66 in of wall, and the wall beyond the tub is exactly 66 in (30 to 96). Moving the door to the far end (`P(60,62)`, so the door runs 62 to 94 and the pocket 30 to 62) keeps the pocket clear of the tub. Purely illustrative, and optional.

### 28. MINOR: Code figures for the shower and fan come from a 2018-IRC explainer
- `{SR('code','not less than 900 square inches')}`, `{SR('code','no less than 24 inches')}` and `{SR('vent','air from an exhaust fan must discharge directly to the outside')}` all come from buildingcodetrainer.com, which quotes the **2018** IRC. The wording is verbatim and matches the current requirements, so this is acceptable. "Directly" is buildingcodetrainer's word, not the code's (M1501.1: discharged to the outdoors, not into an attic, soffit, ridge vent or crawl space). Optionally note "(2018 IRC)". The P2708.1 exception, which allows a 25 in minimum dimension when the compartment is at least 1,300 sq in, is left out. That's fine for a general guide.

---

## Verified claims (no change needed)

- **This Old House sizes:** "A small bathroom typically measures 5-by-8 feet or 6-by-6 feet." (thisoldhouse.com/bathrooms/small-bathroom-remodel-cost, updated 06/08/2026). The diagram's 40 sq ft for 5x8 is simple arithmetic.
- **Bob Vila clearances:** "The building code allows for a minimum of 21 inches." / "NKBA designers recommend a 30-inch clearance between the front edge of a fixture" / NKBA toilet 18 in, code 15 in / shower 36x36 recommended, 30x30 code / NKBA lavatory centerline 20 in to wall, and "Code is a minimum of 15 inches (with 4 inches from the edge of a pedestal sink to the wall)."
- **"Sink center to wall: code 15 in" is a real code figure.** 2018 IRC P2705.1 item 5 lists lavatories along with water closets: "A water closet lavatory or bidet shall not be set closer than 15 inches … from its center to any side wall, partition or vanity" (Oklahoma's adopted text, item 5 not amended). Caveat: North Carolina's residential code interpretation says NC sets no lavatory sidewall limit (ncosfm.gov). Cite the IRC rather than Bob Vila (see #3).
- **NKBA numbers, independent confirmation:** Supply House Times (2008, excerpted from NKBA's *Bath Planning*): toilet "at least 18 inches on center from the nearest wall or obstacle"; lavatory "20 inches" to a wall or tall obstruction; "30 inches of clearance in front of the lavatory"; shower "at least 36 inches x 36 inches" (https://supplyht.com/articles/92491-nkba-placement-of-bath-fixtures). Hunker: NKBA entry door "at least 32 inches wide".
- **Block Renovation:** "Standard alcove tubs are 60 inches long by 30 to 32 inches wide." / "Layout 1: Shower, toilet, and sink on one wall" / "A standard vanity is 21 to 22 inches deep." / shallow vanity "16 to 18 inches deep gives back three or four inches of floor space."
- **Bob Vila pocket door:** "recovers at least 10 square feet of floor space around the door"; a 32-inch door needs "at least 66 inches of linear wall space."
- **Houzz (12 ways):** "the peek of flooring underneath makes the area feel a notch more open" (floating vanity); "The entire square footage of the room will be visible at once…" (glass instead of a curtain).
- **Bob Vila tiny bathrooms:** "A corner sink opens up this tiny bathroom, giving the rest of the off-camera space room to breathe."
- **Pro Builder:** "They also allow easy access to the floor under the bowl for cleaning." / "This setup allows the height to be completely customized," Christofferson explains. The tank sits inside the wall.
- **Schluter:** "create a seamless look in the bathroom, making it look and feel bigger"; "improved accessibility to everyone from the very young to the very old"; "Linear drains let the shower floor pitch in one direction."
- **IRC P2708.1 (via buildingcodetrainer, 2018 IRC):** "not less than 900 square inches of interior cross-sectional area" and "not less than 30 inches in minimum dimension". The 24 in clearance in front of a shower opening is confirmed there and by NC OSFM (2018 NC Residential Code: "24 inches in front of its full width").
- **IRC R307.1:** 21 in clearance in front of the water closet and lavatory (NC OSFM). "Fixtures shall be spaced in accordance with Figure R307.1" (Casa Grande AZ).
- **IRC R307.2:** nonabsorbent tub and shower walls to at least 6 ft above the floor (Richland WA). Only the wording needs adjusting (#21).
- **IRC M1501.1 / M1505.4.4 (via buildingcodetrainer, 2018 IRC):** exhaust "must discharge directly to the outside and not into attics…"; "minimum exhaust rate of 50 cfm intermittent or 20 cfm continuous." This matches the diagram's 50 CFM minimum.
- **HVI:** "For most bathrooms this works out to one CFM per square foot of bathroom area." / "A 50 CFM rating is recommended as a minimum for bathrooms 50 sq. ft. and smaller." / "the fan should be rated at 1.0 sones or less." HVI ventilation page: "HVI recommends that the fan be left on for 20 minutes after use of the bathroom."
- **HGTV:** "installing an extra-tall curtain close to the ceiling"; "use the same tiles or finishes for the niche that are featured on the surrounding walls"; Miranda: "you can get away with using higher priced materials as you need so little of them."
- **TileBar:** "tile with at least one edge measuring 12 inches or more"; "Fewer grout lines reduce interruptions, making smaller bathrooms feel more open and cohesive."
- **This Old House (look larger):** "Use large-format tiles to minimize grout lines" (the article's own tip); Debbie Zimmer, color expert at the Paint Quality Institute: "Lighter hues can open up a small space."; Francesca Bettridge, lighting designer with Cline, Bettridge, Bernstein: "Never shine a light on the mirror."
- **CRD Design Build:** "Low-moisture bathrooms (like powder rooms without a shower or tub) are ideal candidates for wallpaper." / "Use vinyl-coated, moisture-resistant wallpaper specifically designed for high-humidity environments."
- **Golden Lighting:** byline "Written by Rick Kovac, COO of Golden Lighting"; "a warm 2700K to 3000K color temperature."
- **HomeAdvisor:** "Remodeling a small bathroom costs an average of $6,500"; "most projects cost between $1,500 and $15,000" (updated Jun 20, 2026; page labeled 2025 data).
- **Cost vs Value 2025 (JLC national):** midrange bath remodel job cost $26,138, resale value $20,915, 80% recouped. No 2026 report has been published (the jlconline year selector ends at 2025).
- **EPA WaterSense showerheads:** "must demonstrate that they use no more than 2.0 gpm" (standard is 2.5 gpm). The diagram's "Toilet: WaterSense 1.28 gal per flush" and "Showerhead: WaterSense 2.0 gal per min" are correct.
- **ESFi:** 81% drop and the 1975 NEC bathroom requirement are confirmed (wording in #20).
- **NEC 210.8(A)(1):** bathroom receptacles require GFCI protection (IAEI). The diagram's "Outlets: GFCI protected" is correct.
- **Anti-scald 120°F:** the limit is correct (wording and source in #11).
- **Diagram geometry, apart from #1 and #27:** the room is 60x96 in (40 sq ft). The tub is 60x30 in. The toilet centerline is 18 in from the tub (48 - 30). The toilet bowl front is at 28 in, leaving 32 in clear to the opposite wall. The vanity is 21 in deep, leaving 39 in clear. The sink centerline is currently 22 in from the end wall (96 - 74), so the current desc matches the current drawing. The pocket door is 32 in on the long wall. All labels match the drawn dimensions.
- **Internal links and structure:** 12 numbered ideas, as the intro says.
