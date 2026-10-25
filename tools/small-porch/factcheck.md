# Fact-check: small porch ideas (dailyspacehacks.com)

Checked 25 Oct 2026 against live pages. Every source was found with WebSearch and then fetched. The files were not edited.
Severity counts: **2 must-fix, 5 should-fix, 11 minor.**

Paragraph text lives in `build.py`. Diagram text lives in `svg.py`, which generates `z.svg`. "Visible text" below is the rendered text, so you can find it with a string replace. Link changes give the `SR('key', ...)` call.

---

## MUST-FIX

### 1. The planning fee is badly out of date
- **Visible text:** `And if you do need planning permission, Homebuilding puts the application fee at £172 in England and £157 in Wales.`
- **build.py:** `{SR('hbpp','£172 in England and £157 in Wales')}`
- **Problem:** Homebuilding's article dates from 24 Jan 2023, and its figures were already stale then. England's householder fee rose from £172 to £206 in 2018. Today it is **£548** in England and **£585** in Wales.
- **Evidence:**
  - Planning Portal, householder consent: "Alterations to a single house - £548". https://www.planningportal.co.uk/planning/planning-applications/consent-types/householder-planning-consent
  - Ribble Valley fee table, from 1 April 2026: "Single dwellinghouse NOT INCLUDING FLATS £548". https://www.ribblevalley.gov.uk/downloads/file/4972/planning-application-fees-from-1-april-2026-table-
  - Welsh Government Fee Document: "a) Where the application relates to one dwellinghouse, £585", which takes effect 1 December 2025. https://www.gov.wales/sites/default/files/publications/2025-10/planning-application-fees-fee-document.pdf
  - Homebuilding (published 24 Jan 2023): "will cost around £172 in England and £157 in Wales". https://www.homebuilding.co.uk/advice/porch-planning-permission
- **Suggested replacement:** add two keys to `SRC`:
  - `"ppfee":"https://www.planningportal.co.uk/planning/planning-applications/consent-types/householder-planning-consent"`
  - `"walfee":"https://www.gov.wales/sites/default/files/publications/2025-10/planning-application-fees-fee-document.pdf"`

  Then use: `And if you do need planning permission, a householder application costs {SR('ppfee','£548 in England')} and {SR('walfee','£585 in Wales')} (2026 fees).`

  The `hbpp` key can then be dropped.

### 2. The text implies an open canopy escapes the 2 m highway rule
- **Visible text:** `Works best: terraces with the door close to the pavement, where the 2 m rule means an enclosed porch would need planning permission.` In build.py this is `<strong>Works best:</strong> terraces with the door close to the pavement, where the 2 m rule means an enclosed porch would need planning permission.`
- **Problem:** Readers will take this to mean a canopy needs no permission where an enclosed porch would. That is not safe advice. Planning Portal treats a porch canopy as permitted development only within the porch limits, which include the 2 m rule. Class D does not require a porch to be enclosed.
- **Evidence:**
  - Planning Portal FAQ, "Do I need planning permission to add a small wooden canopy over my front door?": "Adding a porch canopy is classed as permitted development … provided it meets the limits and conditions … Porches must meet the following limits: … no part of the porch would be within two metres of any boundary of the dwellinghouse and the highway." https://interactive.planningportal.co.uk/faqs/do-i-need-planning-permission-to-add-a-small-wooden-canopy-over-my-front-door
  - PlanWatch says that assuming a canopy needs no permission "is not a safe assumption" and that whether a small canopy crosses that line "is a matter for the council". https://planwatch.co.uk/guides/do-i-need-planning-permission-for-a-porch
- **Suggested replacement:** `<strong>Works best:</strong> when you want shelter at the door without losing light in the hall. Planning Portal applies the porch limits to canopies too (3 m², 3 m high, 2 m from a boundary with a highway), so if your door opens almost straight onto the pavement, check with your council before fitting even a canopy.`

---

## SHOULD-FIX

### 3. Approved Document K is guidance, not law, and safety glass is not the only option
- **Visible text:** `Approved Document K requires safety glass in critical locations.`
- **Problem:** The legal requirement is K4 of Schedule 1 to the Building Regulations. Approved Document K is the guidance that explains it. That guidance also allows robust or small panes, or permanent protection, not only safety glass.
- **Evidence:** The Lancaster leaflet (issued 1 April 2013, citing ADK) lists three ways to comply: "Break safely" (laminated or toughened), "Robust or small panes", or "Permanent protection". https://lancaster.gov.uk/assets/attach/1343/Leaflet-4-Safety-Glass-Where-is-it-needed.pdf
- **Suggested replacement:** `Under the Building Regulations (Part K, explained in Approved Document K), glazing in "critical locations" must break safely, be robust or be protected, which in a porch usually means toughened or laminated safety glass.`

### 4. Door side panels: the 1500 mm height limit is missing (article and diagram)
- **Visible text (article):** `glazing within 300 mm of the edge of a door, and other glazing within 800 mm of the floor.`
- **Visible text (diagram, svg.py line 67):** `• within 300 mm of a door edge`
- **Problem:** Side panels within 300 mm of a door edge only need safety glazing up to 1500 mm above the floor. As written, the text implies the whole panel at any height.
- **Evidence:** Lancaster: "Glazing adjacent to doors – wholly or partially within 300mm of the edge of a door" and "also wholly or partially within 1500mm from floor level". Eden Council's page says the same. https://eden.gov.uk/planning-and-building/building-control/building-control-guidance-notes/safety-glazing
- **Suggested replacement:**
  - Article: `glazing within 300 mm of the edge of a door (again up to 1500 mm from the floor), and other glazing within 800 mm of the floor.`
  - Diagram: `• within 300 mm of a door edge, below 1500 mm`

### 5. Part P: the notifiable-work rule given is England-only, and Wales is stricter
- **Visible text:** `According to the IET, adding a light to an existing circuit is not notifiable, but the installation of a new circuit is, so use a registered electrician who can certify the work.`
- **Problem:** The article covers Wales elsewhere, but this rule only applies in England. In Wales, garden lighting and outside sockets are still notifiable.
- **Evidence:**
  - IET FAQ: on 31 July 2014 "the Welsh Building Regulations were amended, diverging from those used in England". The England examples are "The installation of a new circuit", while "adding a lighting or power point to an existing circuit" is non-notifiable. https://electrical.theiet.org/bs-7671/building-regulations/part-p-england-and-wales/frequently-asked-questions/
  - Electrical Competent Person: the Wales notifiable list includes, "Outside the dwelling: … garden lighting … a socket-outlet". https://www.electricalcompetentperson.co.uk/building-regulations-explained/
- **Suggested replacement:** `In England, according to the IET, adding a light to an existing circuit is not notifiable, but {SR('iet','the installation of a new circuit')} is; in Wales, outdoor lighting work is notifiable too. Either way, a registered electrician can certify the work.`

### 6. The bench sentence mixes up the porch's dimensions
- **Visible text:** `at the shallow end, a 40 cm bench fits even in our 1.4 m deep example.`
- **Problem:** In the diagram, the bench runs along a 1.4 m side wall. Its 40 cm depth comes out of the 1.8 m internal width, not the 1.4 m depth. The arithmetic itself is right: 1.8 − 0.4 leaves 1.4 m across to the hook wall, and about 1 m once coats are hanging. The sentence just links the wrong dimension.
- **Suggested replacement:** `at the shallow end, a 40 cm deep, 1 m long bench fits along one 1.4 m side wall of our example and still leaves about 1.4 m of floor across to the hooks.`

### 7. The Energy Saving Trust figure comes from a 2021 page
- **Visible text:** `The Energy Saving Trust says draught-proofing windows and doors could save you around £30 a year`
- **Problem:** The linked page was last updated 21 Dec 2021, before the energy price rises. A newer EST page (updated 20 May 2026) gives "around £55 a year in Great Britain". That figure is for windows, floors and doors in older homes, so its scope differs slightly.
- **Evidence:**
  - "could save you around £30 a year", based on a gas-heated semi; published and updated December 2021. https://energysavingtrust.org.uk/how-to-draught-proof-your-windows-and-doors/?loc=international
  - "could save you around £55 a year in Great Britain (GB)". https://energysavingtrust.org.uk/cutting-out-draughts-older-homes
- **Suggested replacement (choose one):**
  - Keep the link and date the figure: `The Energy Saving Trust's 2021 guide says draught-proofing windows and doors {SR('est','could save you around £30 a year')}`
  - Or add a key `"est2":"https://energysavingtrust.org.uk/cutting-out-draughts-older-homes"` and write: `The Energy Saving Trust says draught-proofing windows, doors and floors {SR('est2','could save you around £55 a year')} in an older home.`

  The letterbox and keyhole advice can stay on the `est` link.

---

## MINOR

### 8. Grammar in the MyBuilder canopy price
- **Visible text:** `MyBuilder puts open canopy porches at £2,000 and £4,000 including installation`
- **Fix:** `{SR('mb','£2,000 to £4,000')}`

### 9. The £95 canopy is a retail price, not a fitted price
- **Visible text:** `A simple polycarbonate door canopy starts from £95`
- **Evidence:** "A simple polycarbonate door canopy with contemporary wall brackets can be purchased online at many retailers from £95." https://www.homebuilding.co.uk/advice/porch-costs
- **Fix:** `A simple polycarbonate door canopy {SR('hbc','can be bought online from £95')} to fit yourself`

### 10. "Homebuilding's experts" is vague; name the expert
- **Visible text:** `and Homebuilding's experts say an open porch won't provide the same thermal buffer as an enclosed one.`
- **Evidence:** The line is Alexandra Hull's (MD, Back to Front Exterior Design), quoted on https://www.homebuilding.co.uk/rooms/hallway/is-my-porch-making-my-home-colder
- **Fix:** `and Alexandra Hull of Back to Front Exterior Design told Homebuilding that an open porch {SR('cold','won\'t provide the same thermal buffer')} as an enclosed one.`

### 11. The reason given for Mottershead's advice is paraphrased loosely
- **Visible text:** `which makes a small entrance look more substantial.`
- **Evidence:** Ideal Home says the effect "draws the eye past the door's framework, making the entrance appear larger". https://idealhome.co.uk/renovation/exterior/small-front-porch-ideas
- **Fix:** `which she says makes the entrance appear larger.`

### 12. Assaf's depth figure and its context
- **Visible text:** `with a depth of about 1 to 1.5 m.`
- **Evidence:** "it should extend to the front by at least 1m to 1.5m". She was describing a porch "just to protect the door", that is a canopy-type porch. https://www.idealhome.co.uk/renovation/exterior/what-is-the-ideal-porch-size
- **Fix:** `and project at least 1 to 1.5 m.` Optionally, move this sentence to idea 1 (canopy).

### 13. Class D: the exclusions are incomplete and the instrument is misnamed
- **Visible text:** `These rules come from Class D of the planning regulations, they do not apply to flats or maisonettes, and Wales has the`
- **Problem:** D.1(a) also excludes houses created by change of use under Part 3 (Classes G, M, MA, N, P, PA, Q). D.1(e) excludes new dwellings built under Part 20. The instrument is an Order, not "regulations".
- **Evidence:** https://legislation.gov.uk/uksi/2015/596/schedule/2/part/1/crossheading/class-d-porches, which says "the dwellinghouse is built under Part 20 of this Schedule". Planning Portal also lists converted houses and Part 20 homes as excluded.
- **Fix:** `These rules come from {SR('leg','Class D')} of the General Permitted Development Order 2015. They do not apply to flats or maisonettes, or to homes created under certain change-of-use or new-build permitted development rights, and Wales has the`

  The diagram `<desc>` could add "or homes converted under permitted development". This is optional.

### 14. The Building Conservation attribution could be more precise
- **Visible text:** `Building Conservation warns that exterior tiling should never be sealed.`
- **Evidence:** The article is by Peter Thompson, Restoration Consultant, Original Features. "exterior tiling should never be sealed, as it can reduce the frost resistance of the tiles." https://buildingconservation.com/articles/tiles/tiles.htm
- **Fix:** `restoration consultant Peter Thompson warns on BuildingConservation.com that {SR('bc','exterior tiling should never be sealed')}, because sealing can reduce its frost resistance.`

### 15. Superlatives and generalisations with no source
These are editorial opinion. Soften or keep them as clearly your view.
- `Porch floors get wet, so grip matters more than anywhere else in the house.` This overclaims: bathrooms are wetter. Try `…so grip matters as much as in a bathroom.`
- `Most small porches are mostly glass, so this matters.` No source. Try `Many small porches are largely glazed, so this matters.`
- `A bench is the most useful thing in a porch` and `the one that makes the biggest difference`. These are acceptable as opinion. You could say "In our view…" or leave them.

### 16. Security advice reads as a requirement
- **Visible text:** `If your porch has its own lockable outer door, the same standards apply to it.`
- **Problem:** These are recommendations from a community safety guide, not mandatory standards.
- **Fix:** `If your porch has its own lockable outer door, it's worth fitting it to the same standard.`

### 17. Diagram: the door swing isn't drawn, and the hook side is tight
- **Problem:** At 220 px/m, the outer door is 0.84 m wide, placed 0.48 m from the bench wall. The hooks sit 0.6–1.15 m back from the front wall on the opposite side.
  - If the door opens inwards and is hinged on the hook side, the open leaf sits about 0.48 m from that wall and reaches 0.84 m in, so it would hit hanging coats.
  - If it is hinged on the bench side, the leaf clears the bench front by about 8 cm.
  - The 60 x 85 cm mat sits under the swing, so it needs to be thin (Mats4U makes this point about clearance).
  - Overall it fits, but only with the door hinged on the bench side or opening outwards.
- **Fix:** Add a dashed swing arc on the bench side, or a short note in the desc: "outer door hinged on the bench side". Alternatively, move the hooks back towards the house wall.

### 18. Diagram: the 10 cm wall assumption is optimistic for a brick porch
- **Problem:** About 10 cm suits half-brick dwarf walls with uPVC or timber frames. A cavity-wall brick porch (about 27–30 cm) would leave roughly 1.45 x 1.2 m ≈ 1.75 m² inside. The diagram is labelled "Example only", so this is optional.
- **Fix:** One clause in the paragraph: `(thicker cavity walls would leave closer to 1.8 m²)`.

---

## Verified OK

**Permitted development and the diagram (England and Wales)**
- Planning Portal Class D summary: "the ground floor area (measured externally) would not exceed three square metres", "no part would be more than three metres above ground level" and "no part of the porch is within two metres of any boundary that fronts a highway". Flats and maisonettes are excluded, and so are areas with a "planning condition, Article 4 Direction or other restriction".
- Legislation, Class D.1(b)–(d): 3 m² measured externally, 3 m, and "within 2 metres of any boundary of the curtilage of the dwellinghouse with a highway". D.1(d) was substituted in 2020. The article's "fronts a highway" paraphrase is fine.
- "Highway (a road or public path)" in the diagram matches the technical guidance definition: "a public right of way such as a public road, public footpath and bridleway".
- Wales has the same 3 m², 3 m and 2 m limits, excludes flats and maisonettes, and can lose these rights by condition or Article 4 direction (gov.wales). "Wales has the same limits" is correct.
- Camden: "If your house is a listed building you must apply for listed building consent to add a porch." The quote is accurate.
- Diagram arithmetic: 2.0 x 1.5 = 3.0 m². Taking two 10 cm side walls and one 10 cm front wall (no wall against the house) gives 1.8 x 1.4 = 2.52 m² ≈ 2.5 m². The SVG scale (440 px = 2.0 m) draws the interior, bench (0.4 x 1.0 m), mat (0.85 x 0.6 m) and doors (0.84 m) to the stated sizes.

**Building Regulations**
- Planning Portal: "at ground level and under 30 square metres in floor area is normally exempt". The front door "must remain in place", and "glazing and any fixed electrical installations comply".
- DCLG circular letter, 30 July 2013 (R J Ledsome): "The building's heating system must not be extended into the conservatory or porch." This is correctly described as government guidance.
- The safety-glass figures (doors below 1500 mm, 300 mm from a door edge, other glazing below 800 mm) match the Lancaster leaflet and Eden Council, apart from the side-panel height limit in #4.

**Costs**
- MyJobQuote build-a-porch (updated 01/10/26): about £4,500 for 3 m² including labour, brick £5,500–£8,000, uPVC £2,800–£5,200.
- MyBuilder (updated 21/10/2026): about £4,500 for a standard 3 m² porch, small brick £7,500–£12,500, open canopy £2,000–£4,000 installed, builds "between one and three weeks".
- MyJobQuote oak canopy (updated 28/09/26): small canopy £800–£2,000, fitted in 1–2 days.
- Homebuilding: polycarbonate canopy from £95 (see #9 for wording).

**Expert quotes** (each said by the named person on the linked page)
- Rebecca Foster (Homebuilding): "The porch needs to work in proportion with the house".
- David Gray (Corston Architectural Detail): "We would advise having warm white lighting in the porch".
- Jake Vincett (Heritage Build Group): "Don't try to heat the porch…".
- Elizabeth Assaf (Urban Front):
  - "treat the porch as an unheated buffer zone" (Homebuilding)
  - "at least 500mm on each side" (Ideal Home)
- Chloe Barrow (Laura James): both bench and cabinet quotes.
- Danielle Le Vaillant (Cox & Cox): the mirror quote.
- Ruth Mottershead (Little Greene, creative director): "Consider painting both the door and surrounding frame in one shade". The Little Greene blog has "Ruth", the Creative Director, saying "Avoid selecting bright white shades…" and recommending darker tones for a townhouse.
- Genevieve Hurley (interior designer, H&G): "opt for a high gloss finish".
- Rohan Blacker (founder, Pooky, H&G): the spotlights quote.
- Teresa Buck (The Cotswold Company), Eloise Street (The London Tile Co.) and Lucy Mather (Arighi Bianchi), all in Ideal Home's front-porch-ideas: all three quotes are accurate.

**Products, materials and safety**
- Mats4U: "at least 80% of your doorway's width", step on it at least twice, door clearance.
- First Mats: "The most common size is 60cm x 85cm" for standard single doors.
- Wayfair UK: bench height 45–50 cm and "depth is between 38cm and 50cm".
- Walls and Floors: "R10 frequently appears on tiles intended for general residential…" and "Many outdoor … tiles carry an R11 classification".
- Porcelain Superstore: "water absorption rate of less than 0.5%".
- NICEIC: "rated IP44 or higher", plus automatic daylight and movement controls (citing Part L).
- Security guide (North Worcestershire Community Safety Partnership, hosted by Redditch BC): three-star TS007 cylinders, BS3621 mortice deadlock, letterbox deflector.
- EST letterbox flap or brush and keyhole cover advice.

**Structure and links**
- There are 11 ideas in three groups (1–3, 4–8, 9–11), as the intro says.
- All external links resolve to the cited pages.
