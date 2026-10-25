# Fact-check: First Apartment Checklist (Free Printable)

Checked 2026-10-25 against the live pages (WebSearch, then WebFetch). Files checked: content.html, build.py (source strings), checklist.py (53 items, the same list as in the PDF; count confirmed as 53 in 8 sections; the PDF is 2 pages, US Letter 612x792 pt with 46 pt margins, so "fits A4" holds).

Severity counts: must-fix 1, should-fix 6, minor 10.

"Text" is the exact visible string in content.html. Where the text comes from build.py, the matching source string is given as well (build.py uses `{SR('key','anchor')}`).

---

## Issues

### MUST-FIX

**1. The lead paint rule is stated as covering every pre-1978 rental, but studios are exempt**
- Text (content.html / build.py line 59): `If your building was built before 1978, your landlord must give you the EPA lead hazard pamphlet and {SR('lead','disclose any known information')} about lead-based paint.`
- What is wrong: The federal disclosure rule has exemptions. One of them is zero-bedroom units (studios, efficiencies, lofts), which are very common first apartments. Leases of 100 days or less, elderly or disability housing, and units certified lead-free are also exempt. "Your landlord must" is wrong for those renters.
- Evidence: https://www.epa.gov/lead/real-estate-disclosures-about-potential-lead-hazards lists the exemptions as "Zero-bedroom units, such as efficiencies, lofts, and dormitories" (unless a child under six lives there), "Leases of 100 days or less", and housing "tested ... and found lead-based paint free". The EPA fact sheet https://www.epa.gov/sites/production/files/documents/fs-discl.pdf says the same.
- Suggested replacement: `If your building was built before 1978, federal rules usually require your landlord to give you the EPA lead hazard pamphlet and {SR('lead','disclose any known information')} about lead-based paint before you sign (studios, leases of 100 days or less and certified lead-free units are exempt).`
- Checklist item (checklist.py) `Built before 1978? Get the lead paint disclosure` is acceptable as a prompt. Optional softer wording: `Built before 1978? Ask for the lead paint disclosure`.

### SHOULD-FIX

**2. The NAIC "$15 to $30 per month" figure is from 2015 and conflicts with the newer figure in the same sentence**
- Text (build.py line 56): `and puts renters insurance at an average of {SR('naic','between $15 and $30 per month')}; the Insurance Information Institute's national average for 2022 was {SR('iii','$171')} a year.`
- What is wrong: The NAIC page is dated Jan. 1, 2015. NAIC's own 2022 figure, published by Triple-I, is $171 a year, which is about $14 a month and below the "$15 to $30" range. Putting both numbers side by side as current averages contradicts itself. The $171 figure is accurate, and 2022 is still the latest year on the Triple-I page.
- Evidence: https://content.naic.org/article/consumer-insight-rent-protecting-your-belongings-renters-insurance quotes "The premiums for renters insurance average between $15 and $30 per month", and the page is dated "Jan. 1, 2015". https://www.iii.org/fact-statistic/facts-statistics-renters-insurance quotes "The average premiums for renters insurance in 2022 was $171." Its table runs from 2013 to 2022, and 2022 is the latest year. https://www.tdi.texas.gov/tips/renters-insurance.html quotes "The average renters policy in Texas costs about $20 a month."
- Suggested replacement: `The NAIC, the US association of state insurance regulators, warns that {SR('naic','your landlord\'s insurance doesn\'t cover your personal property')}. NAIC data put the national average premium at {SR('iii','$171')} a year in 2022 (about $14 a month), and the Texas Department of Insurance says {SR('tdi','about $20 a month')} is typical there.` Then keep the rest of the sentence ("It isn't required by law, but ...").

**3. "The Army's legal assistance office" is too broad an attribution**
- Text (build.py line 57): `The Army's legal assistance office advises you to`
- What is wrong: The article comes from one installation's office, not the Army as a whole. It was written in 2013 by Capt. Tanga Bernal of the Fort Rucker (now Fort Novosel) Office of the Staff Judge Advocate, Ala.
- Evidence: https://www.army.mil/article/102473/jag_5_tips_for_getting_security_deposits_back, by "Capt. Tanga Bernal", Fort Rucker Office of the Staff Judge Advocate, May 2, 2013. Both quotes are verbatim: "ask your landlord for a move-in inspection sheet" and "any and every small scratch or stain".
- Suggested replacement: `A legal assistance attorney at Fort Rucker's Office of the Staff Judge Advocate, writing on Army.mil, advises you to`

**4. The extinguisher advice leaves out the "alert others and call 911 first" conditions (safety)**
- Text (build.py line 62): `Learn the PASS steps: pull the pin, aim low at the base of the fire, squeeze the lever slowly and sweep from side to side, and only fight a small fire when you have a clear way out.`
- What is wrong: USFA says to use an extinguisher only when all six of its conditions are met. Besides "small and contained" and "clear escape route", these are: others have been alerted, the fire department has been called, you are physically able to use the extinguisher, and you are safe from toxic smoke. Otherwise it says to get out and call 911. Listing only two conditions understates the safety guidance.
- Evidence: https://usfa.fema.gov/prevention/home-fires/prepare-for-fire/fire-extinguishers/ asks "Is the fire small and contained in a single object ...?" and "Do I have a clear escape route?", plus questions on alerting others and calling the fire department. The page says to use an extinguisher only if every answer is yes, and otherwise to leave and call 911.
- Suggested replacement: `Learn the PASS steps: pull the pin, aim low at the base of the fire, squeeze the lever slowly and sweep from side to side. Only fight a fire that is small and contained, after everyone is alerted and 911 has been called, and when you have a clear way out; otherwise get out and call 911.`

**5. The 30% budget rule leaves out utilities (checklist item and article)**
- Checklist text (checklist.py and PDF): `Set a budget: rent at or under 30% of income`
- Article text (build.py line 59): `which is why the 30% rule is the usual guide for rent.`
- What is wrong: The cost-burden measure covers housing costs. For renters, standard data such as the census figures cited by Triple-I count rent plus utilities. "Rent at or under 30%" invites a first-time renter to budget the full 30% for rent and then pay utilities on top. The HUD source also says "policymakers consider" this threshold, and it criticises the rule. That's fine for a rule of thumb, but not for a hard limit.
- Evidence: https://www.huduser.gov/portal/node/7211 (HUD PD&R Edge, "Defining Housing Affordability", 14 Aug 2017; the same article as the archives.huduser.gov link) says: "policymakers consider households who spend more than 30 percent of income on housing costs to be housing cost burdened." https://www.iii.org/fact-statistic/facts-statistics-renters-insurance says: "The percent of renter occupied units spending more than 30 percent on rent and utilities in 2024 was 48.2 percent."
- Suggested replacement (checklist.py): `Set a budget: rent plus utilities at or under about 30% of income`
- Suggested replacement (build.py): `which is why keeping rent plus utilities at or under about 30% of your gross income is the usual rule of thumb.`

**6. The USFA extinguisher quote is reframed as a claim the page doesn't make**
- Text (build.py line 62): `the USFA says home extinguishers are usually {SR('fe','multipurpose fire extinguishers that cover Class A through Class C')}`
- What is wrong: The quoted words come from a sentence about what stores sell. They are not a statement about what home extinguishers usually are.
- Evidence: https://usfa.fema.gov/prevention/home-fires/prepare-for-fire/fire-extinguishers/ says: "Most home improvement stores carry multipurpose fire extinguishers that cover Class A through Class C." The preceding sentence says "A-B-C" models "can be used on most types of home fires."
- Suggested replacement: `the USFA notes that most home improvement stores carry {SR('fe','multipurpose fire extinguishers that cover Class A through Class C')}, which work on most home fires.`

**7. The Texas deposit deadline needs its condition**
- Text (build.py line 57): `and Texas {SR('tx','within 30 days')}, minus any deductions.`
- What is wrong: In Texas, the 30-day refund depends on the tenant giving a written forwarding address. First-time renters often miss this, so it is worth saying.
- Evidence: https://www.texasattorneygeneral.gov/consumer-protection/home-real-estate-and-travel/renters-rights says: "Under Texas law, you must give the landlord a forwarding address in order to receive your returned security deposit." It also says: "The landlord must return your deposit — less any amount deducted for damages — within 30 days." https://guides.sll.texas.gov/landlord-tenant-law/security-deposit-refunds cites Prop. Code 92.103 and 92.107.
- Suggested replacement: `and Texas {SR('tx','within 30 days')} once you give a forwarding address, minus any deductions. Check your own state's rules.`

### MINOR

**8. The University of Illinois office is named generically**
- Text (build.py line 59): `The University of Illinois off-campus housing office suggests`
- What is wrong: The office is called Off-Campus Community Living (OCCL), part of Student Affairs at the Urbana-Champaign campus.
- Evidence: https://occl.illinois.edu/housing/utilities-and-services is titled "Student Affairs Off-Campus Community Living" and says: "Call the public utility companies at least one month prior to your move-in date".
- Suggested replacement: `The University of Illinois Urbana-Champaign's Off-Campus Community Living office suggests`

**9. The EPA lists mattress encasements under control, not prevention**
- Text (build.py line 66): `Buy a mattress encasement too; the EPA lists encasements among its bed bug prevention steps.`
- Evidence: In https://www.epa.gov/sites/default/files/2014-02/documents/bed-bug-prevention-detection-control.pdf, "Install encasements on mattress and box spring." appears under Control (Physical Control Methods), not under Day-to-Day Prevention. This sentence also has no link.
- Suggested replacement: `Buy a mattress encasement too; the EPA lists {SR('bb','encasements on mattress and box spring')} among its bed bug control steps.`

**10. The bed bug paraphrase drops "and cleaned"**
- Text (build.py line 42): `the EPA says {SR('bb','do not bring second-hand furniture into your home')} until you have checked it thoroughly for bed bugs.`
- Evidence: The same EPA PDF says: "Do not bring second-hand furniture into your home unless you have thoroughly inspected and cleaned the items first."
- Suggested replacement: `... until you have thoroughly inspected and cleaned it.`

**11. The anti-tip kit claim drops "most"**
- Text (build.py line 64): `anti-tip kits {SR('cpsc','cost less than $20')} and take under 20 minutes.`
- Evidence: https://www.cpsc.gov/Newsroom/News-Releases/2023/Plans-to-Watch-the-Big-Game-on-the-Big-Screen-CPSC-Reminds-Families-to-Protect-Children-from-the-Deadly-Hazard-of-Toppling-TVs-and-Furniture says: "Most kits cost less than $20 and can be installed in fewer than 20 minutes."
- Suggested replacement: `most anti-tip kits {SR('cpsc','cost less than $20')} and take under 20 minutes to install.`

**12. The HUD wording says HUD when the source says "policymakers"**
- Text (build.py line 59): `On budget, HUD treats households that {SR('hud','spend more than 30 percent of income on housing costs')} as cost burdened,`
- Evidence: The HUD PD&R article (https://www.huduser.gov/portal/node/7211) says: "policymakers consider households who spend more than 30 percent of income on housing costs to be housing cost burdened". HUD does use this definition, so this is low risk.
- Suggested replacement: `On budget, HUD's research office notes that households that {SR('hud','spend more than 30 percent of income on housing costs')} are considered cost burdened,`

**13. The CO death statistic has no link**
- Text (build.py line 61): `and more than 150 people in the US die every year from accidental non-fire CO poisoning.`
- Evidence: https://www.usfa.fema.gov/prevention/life-safety-hazards/carbon-monoxide/ says: "More than 150 people in the United States die every year from accidental nonfire-related CO" (CPSC data). The claim is accurate but stated with no source.
- Suggested replacement: `and the USFA, citing CPSC data, says {SR('co','more than 150 people in the United States die every year')} from accidental non-fire CO poisoning.`

**14. "It isn't required by law" is stated generally but comes from Texas**
- Text (build.py line 56): `It isn't required by law, but the Texas Department of Insurance notes that`
- Evidence: https://www.tdi.texas.gov/tips/renters-insurance.html says: "Renters insurance isn't required by law." That is accurate for state law, but it is a Texas regulator's statement.
- Suggested replacement: `No state law requires it, the Texas Department of Insurance says, but it notes that ...` (or link the existing text to the TDI page).

**15. The extension cord item needs a short safety qualifier (checklist.py / PDF)**
- Text: `Surge protector and an extension cord`
- What is wrong: Nothing is incorrect, but first-time renters often use extension cords as permanent wiring, which is a fire risk.
- Evidence: https://esfi.org/extension-cord-safety says "an extension cord is a temporary solution and is not meant to be used as a long-term extension" and "Do not substitute extension cords for permanent wiring."
- Suggested replacement: `Surge protector and an extension cord (temporary use only)`. If space is tight in the PDF, keep the item and add the note to the article.

**16. The freezer temperature needs "or below" (checklist.py / PDF)**
- Text: `Check fridge 40°F or below, freezer 0°F`
- Evidence: https://www.foodsafety.gov/keep-food-safe/4-steps-to-food-safety says: "Your refrigerator should be set to 40°F (4°C) or below and your freezer to 0°F (-18°C) or below."
- Suggested replacement: `Check fridge 40°F or below, freezer 0°F or below`

**17. Some link URLs could not be checked directly (please click-test)**
The proxy blocks direct requests, and WebSearch did not return these exact URLs. The content was confirmed on equivalent URLs:
- `https://faq.usps.com/articles/FAQ/Change-of-Address-The-Basics`: content confirmed at https://faq.usps.com/articles/Knowledge/Change-of-Address-The-Basics (90 days before / 30 days after; "When the COA request is made online there is a $1.25 authentication fee."). Consider switching the link to the `/Knowledge/` path that search returns.
- `https://archives.huduser.gov/portal/pdredge/pdr-edge-featd-article-081417.html`: the same article is live at https://www.huduser.gov/portal/node/7211.
- `https://www.cdc.gov/hygiene/about/when-and-how-to-clean-and-disinfect-your-home.html`: the quote was confirmed on a mirror of that page: "To disinfect, use an EPA-registered disinfecting product or a stronger bleach solution."
- `https://www.energy.gov/sites/default/files/2022-08/energy-saver-guide-2022.pdf`: this PDF could not be fetched. The DOE Energy Saver Guide page confirms a 2022 edition exists, and the DOE lighting fact sheet (https://www.energy.gov/sites/default/files/2021-08/ES-EE%20Lighting_080921.pdf) says "LEDs use up to 90% less energy and last up to 25 times longer than incandescent bulbs." The claim is correct; the link needs a click-test.

---

## Verified claims (no change needed)

- 53 tick boxes in 8 sections, a two-page PDF, US Letter that fits A4 (pdfinfo: 2 pages, 612x792 pt, 46 pt margins). The article's checklist matches checklist.py and the PDF word for word.
- NAIC: "your landlord's insurance doesn't cover your personal property" (verbatim, content.naic.org).
- Triple-I: $171 national average for 2022 (iii.org; 2022 is the latest year shown).
- TDI: "Some landlords might require you to have a renters policy." and "Fill out a home inventory to know the value of your belongings ..." (both verbatim, tdi.texas.gov/tips/renters-insurance.html).
- Army.mil JAG article: "ask your landlord for a move-in inspection sheet", "any and every small scratch or stain", and the advice to take photos at move-in and move-out (verbatim).
- NY AG Tenants' Rights Guide: "the landlord must return the security deposit within 14 days of the tenant moving out" (verbatim).
- Texas AG: deposit returned "within 30 days" less deductions, and "The landlord must also provide smoke detectors." (verbatim).
- UIUC OCCL: "at least one month prior to your move-in date" (verbatim). The checklist's "about a month ahead" is consistent.
- USPS: COA can be filed "90 days before the effective date of your move", and the online fee is $1.25 (current FAQ). The checklist item "online fee $1.25" is correct.
- HUD 30% cost-burden threshold (huduser.gov "Defining Housing Affordability", 2017). The phrase "spend more than 30 percent of income on housing costs" is verbatim.
- EPA lead: pamphlet plus "Disclose any known information about the presence of lead-based paint ..." (verbatim; the exemptions are covered in issue 1).
- USFA smoke alarms: "Put smoke alarms inside and outside each bedroom and sleeping area.", "Put alarms on every level of the home.", "Test smoke alarms every month ...", "A smoke alarm with a dead or missing battery is the same as having no smoke alarm at all." (verbatim). The checklist item "Test every smoke alarm (inside and outside bedrooms)" is consistent.
- USFA CO: "Install CO alarms in a central location outside each separate sleeping area and on every level of your home." (verbatim). The checklist item "CO alarm outside each sleeping area and on every level" is consistent. The page recommends CO alarms for all homes, not only homes with fuel-burning appliances. "More than 150 ... die every year" is verified (issue 13 only adds a link).
- USFA PASS wording: "Pull the pin", "Aim low. Point the extinguisher at the base of the fire.", "Squeeze the lever slowly and evenly.", "Sweep the nozzle from side-to-side." "Multipurpose (ABC) fire extinguisher" in the checklist is consistent.
- USFA home checklist: "There is a fire escape plan that shows 2 ways out of every room." (verbatim).
- CPSC Anchor It (2024): "Anchor TVs and furniture, such as bookcases and dressers, securely to the wall." and "17,800 people annually are injured in these incidents" (ED-treated, 2020 to 2022). The 2026 CPSC Super Bowl LX release repeats 17,800 (2020 to 2022), so the figure is still current.
- FDA: "keep its temperature at 40 °F or below; the freezer should be at 0 °F." (verbatim).
- FoodSafety.gov chart: poultry 165°F (74°C).
- FoodSafety.gov 4 Steps: separate cutting boards for produce and for raw meat, poultry and seafood. "Use a food thermometer to be sure your food is safe." This supports the checklist's "two cutting boards (one for raw meat)" and "Food thermometer".
- Poison Control: "Ammonia should never be mixed with chlorine or bleach products." (verbatim).
- CDC: "use an EPA-registered disinfecting product" (verbatim). This supports the checklist's "EPA-registered disinfectant".
- Sleep Foundation: full "54” wide, 75” long", queen "60” wide, 80” long", and "leaving about 24 inches of space around each side of your bed" (verbatim).
- EPA bed bug PDF: the second-hand furniture warning (see issue 10 for wording) and encasements (see issue 9 for section).
- DOE: LEDs use up to 90% less energy than incandescent bulbs (DOE fact sheet; see issue 17 for the link).
- The remaining checklist items (lease, renters insurance, move-in inspection sheet, photos at move-in, breaker panel and water shut-off, landlord contacts, kitchen, bathroom, bedroom and cleaning basics) are ordinary, safe and accurate. The PDF footer "Check your lease and local rules" and the article's "Ask your landlord before drilling" cover landlord limits on anchoring and hanging.
