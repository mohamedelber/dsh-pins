# Fact-check: How to Organise Clothes in a Wardrobe: 7 Steps

Checked 25 Oct 2026 against live pages (WebSearch, then WebFetch). Every quoted anchor was checked for wording and speaker. No quote is misattributed and no quoted anchor is missing from its linked page. The issues below are about added detail, unsourced claims and numbers.

Severity: **MUST** = fix before publishing; **SHOULD** = inaccurate or overstated, fix; **MINOR** = optional polish.

Text locations: "content.html" means the published HTML. The same string is in build.py (paragraph f-strings) unless the issue says svg.py.

## Issues

1. **MUST: unsourced IKEA shoe-rack claim, and the source is misnamed**
   - Current text: `IKEA's planner says a shoe rack should never go above clothes.`
   - Problem: there is no link. The claim is not in the PAX/KOMPLEMENT PDF (ie or gb), which only says "Plan 33 cm for a pull-out shoe shelf". It is on IKEA's "step-by-step: find your perfect clothes storage system" page, which is a guide, not "the planner". There is an IKEA GB copy of that page.
   - Evidence: https://www.ikea.com/gb/en/rooms/bedroom/how-to/step-by-step-find-your-perfect-clothes-storage-system-pubf9da8ed0/ says "Shoe rack – 33 cm (allow more space for boots; never place above clothes)". The research notes cited the Hong Kong copy (ikea.com.hk), which has the same wording.
   - Fix: add `"ikss":"https://www.ikea.com/gb/en/rooms/bedroom/how-to/step-by-step-find-your-perfect-clothes-storage-system-pubf9da8ed0/"` to SRC, then replace the sentence with:
     `IKEA's clothes storage guide says to allow 33 cm for a shoe rack and {SR('ikss','never place above clothes')}.`

2. **SHOULD: "a double rail nearly doubles the hanging space" has no source**
   - Current text: `If most of your clothes are shirts and folded trousers, a double rail nearly doubles the hanging space in the same width.`
   - Problem: no source. The only nearby figure ("almost doubled", Ideal Home small-wardrobe article) is an editor testing cascading hooks, not double rails. The research notes call it an unverified marketing-style claim. The statement is only true as arithmetic: two rails give twice the rail length.
   - Fix (plain arithmetic, needs no source): `If most of your clothes are shirts and trousers, two rails one above the other give you twice the rail length in the same width.`

3. **SHOULD: the Step 3 worked example leaves no clearance and contradicts the diagram**
   - Current text: `if your shirts need 90 cm and the space under the rail is 180 cm, you have room for a second rail.`
   - Problem: 2 × 90 cm = 180 cm. That leaves 0 cm for the lower rail, the hanger hooks and floor clearance, and shirts on a 90 cm lower rail would touch the floor. The article's own diagram needs the upper rail at about 2 m (198 cm) to make double hanging work. The only drops in the sources are FCI's 90 cm for shirts and IKEA's 80 cm for blouses and 60–70 cm for hanging trousers.
   - Evidence: FCI (https://www.fcilondon.co.uk/blog/should-fitted-wardrobes-go-to-ceiling): "90cm for skirts, shirts, and blouses". IKEA PDF: "Plan appr. 60–70 cm for hanging trousers."
   - Fix: `if you have about 2 m below the top rail, there is room for two tiers of shirts at 90 cm each; with about 1.8 m, put shirts on the top rail and trousers (60 to 70 cm) on the lower one.`

4. **SHOULD: the diagram `<desc>` says folded trousers need 90 cm, which contradicts the key and the sources** (svg.py `desc`, also in content.html)
   - Current text: `so each tier has room for shirts and folded trousers, which need about 90 cm.`
   - Problem: the diagram's own key says "Trousers, hung 60-70 cm", which matches IKEA. Also, at 90 cm the lower tier has no clearance for a 90 cm shirt (see issue 3). The drawing itself puts shirts on top (about 88 cm long) and trousers below (about 72 cm). The lower-rail height (90 cm), upper rail (198 cm, which is ~2 m), shelf (205 cm), single rail (180 cm) and shelves (35 cm apart) all check out on the drawing at 2.75 px/cm.
   - Fix: `so the upper tier takes shirts (about 90 cm) and the lower tier takes folded trousers (60 to 70 cm).`

5. **SHOULD: Shannon Murphy is credited with examples she did not give**
   - Current text: `professional organiser Shannon Murphy told Ideal Home to <a ...>use fabric storage boxes or baskets</a> for smaller items such as scarves and swimwear.` (in build.py: `{SR('ihw','use fabric storage boxes or baskets')} for smaller items such as scarves and swimwear.`)
   - Problem: neither "scarves" nor "swimwear" appears anywhere on the Ideal Home page. Her point is about stopping piles toppling, and she adds a warning about wicker.
   - Evidence: https://www.idealhome.co.uk/house-manual/storage-organisation/how-to-organise-your-wardrobe: "Use fabric storage boxes or baskets for shelves to contain smaller items and prevent piles from toppling over." / "Avoid wicker as it can snag fabrics."
   - Fix: `{SR('ihw','use fabric storage boxes or baskets')} for smaller items so piles don't topple, and to avoid wicker, which can snag fabrics.`

6. **SHOULD: Craig Hoareau's advice is extended to cotton bags, which he does not mention**
   - Current text: `avoid cardboard boxes as these attract pests</a>; use lidded plastic boxes or breathable cotton bags.`
   - Problem: Hoareau says to use sealed plastic boxes or bags (he names the Really Useful Box) and says vacuum bags are "a great alternative". He does not mention cotton bags. As written, the cotton-bag advice reads as his.
   - Evidence: https://www.idealhome.co.uk/house-manual/storage-organisation/how-to-store-seasonal-clothes: "Avoid cardboard boxes as these attract pests and do not offer the same protection as a sealed plastic box/bag."
   - Fix: `avoid cardboard boxes as these attract pests</a> and use lidded plastic boxes instead. Breathable cotton bags also work for clean woollens.` If the cotton-bag line stays, it is unsourced; the research only has Hayden Hill, a cotton-bag seller.

7. **SHOULD: Which? is understated on pheromone traps**
   - Current text: `won't eradicate an infestation</a>; they only show you have one.`
   - Problem: Which? says the traps help to monitor, locate and reduce flying adult moths. "Only show you have one" goes beyond what it says. Which? adds that you still need to deal with eggs and larvae.
   - Evidence: https://www.which.co.uk/news/article/how-to-get-rid-of-clothes-moths-adJHW5b1O1zT (12 Aug 2026): "although these won't eradicate an infestation" … "they can play a part in helping to monitor, locate and reduce flying adult moth numbers" … "you will still need to break the breeding cycle".
   - Fix: `won't eradicate an infestation</a>, though they help you spot and track moths; you still have to deal with the eggs and larvae.`

8. **SHOULD: the internal link claims "the same four-pile method", but that guide uses different piles**
   - Current text: `guide uses the same four-pile method room by room.`
   - Problem: dailyspacehacks.com/how-to-declutter-your-home (local copy at scout/site/how-to-declutter-your-home.html) uses a four-box method with the piles "keep, donate or sell, trash or recycle, relocate". This article's piles are keep, donate, sell, repair.
   - Fix: `guide uses a similar four-box method room by room.`

9. **MINOR: Hester Van Hien's title**
   - Current text: `Professional organiser Hester Van Hien of Tidylicious`
   - Ideal Home calls her a "Home Decluttering and Organising Consultant, Tidylicious".
   - Fix: `Decluttering and organising consultant Hester Van Hien of Tidylicious`

10. **MINOR: Cher Casey did not say "the same" as Silverthorn**
    - Current text: `Professional organiser Cher Casey told Livingetc the same, and warned that`
    - She says "Organize by category first, then arrange each category by color" and does not mention sleeve length (https://www.livingetc.com/advice/why-not-to-organize-a-closet-by-color). She is quoted by the writer Amiya Baratan, so "told Livingetc" is correct.
    - Fix: `Professional organiser Cher Casey told Livingetc to sort by category first and colour second, and warned that`

11. **MINOR: a KonMari gloss is not on the linked page**
    - Current text: `standing them up vertically</a>, so you can see everything at once, and`
    - The KonMari page says upright storage prevents creasing and saves space. It does not mention seeing everything at once; that point is supported by the next source (Homes & Gardens).
    - Fix: `standing them up vertically</a>, which saves space and stops creasing, and`

12. **MINOR: Timberwise does not mention an outside wall**
    - Current text: `move the wardrobe slightly away from a cold outside wall.`
    - Timberwise says "you can slightly move the wardrobe away from the wall" and talks generally about "a cold surface at the back of your wardrobe".
    - Fix: `move the wardrobe slightly away from the wall, especially a cold one.`

13. **MINOR: the WRAP figures are from 2022**
    - Current text: `WRAP found the average UK adult's wardrobe holds 118 items`
    - The press release is dated 7 Oct 2022. The figures are correct ("the average UK adult has 118 items of clothing in their wardrobes"; "one quarter (26% - 31 items) were unworn for at least a year").
    - Fix: `WRAP found in 2022 that the average UK adult's wardrobe holds 118 items`

14. **MINOR: a 30 cm stack does not fit a 30 cm shelf gap**
    - Current text: `which suits shelves 30 to 40 cm apart.`
    - IKEA's 30 cm stack of 10 jumpers would fill a 30 cm gap exactly. FCI gives 300 mm as the minimum shelf spacing and 350–400 mm as recommended. The diagram's shelves are 35 cm apart, so it is fine.
    - Optional fix: `which suits shelves 35 to 40 cm apart.` If you change this, also change the diagram label `Shelves 30-40 cm apart` (svg.py) and `shelves 30 to 40 cm apart` in the desc. Leaving 30–40 is defensible because it matches FCI's minimum-to-recommended range.

15. **MINOR: the upper rail at ~2 m is above FCI's range**
    - FCI's single-rail heights are 1750 / 1800 / 1900 mm (minimum / recommended / luxury). The diagram's upper rail at 198 cm is above the luxury figure and out of easy reach for many people. It is correctly labelled "our worked example", so no change is required.
    - Option: add a line to Step 3 or the desc such as `a pull-down rail helps if the top rail is out of reach.`

16. **MINOR: a UK IKEA source is available for the PAX figures** (key `ikpdf`)
    - The Ireland PDF loads and has all the quoted figures. A GB copy has the same wording ("Plan appr. 100 cm for coats." / "Plan appr. 30 cm for 10 pairs of folded sweaters.").
    - Option: `"ikpdf":"https://www.ikea.com/gb/en/files/pdf/51/8d/518da651/1-pax_komplement_buying_guide_a4-final.pdf"`
    - Also "IKEA's PAX planner" is really the PAX & KOMPLEMENT buying guide. Option: change `IKEA's PAX planner suggests` to `IKEA's PAX buying guide suggests`.

17. **MINOR: the NHM link could not be confirmed** (key `nhm`)
    - The quote "Clothes moths prefer low light levels and dirty fabrics, such as carpets and rugs" was confirmed on the wifi.nhm.ac.uk mirror at the same path. The www.nhm.ac.uk URL itself could not be loaded here (the permission request timed out). Check that it resolves before publishing.

18. **MINOR (optional): House of Colour says not to empty everything at once**
    - Step 1 says "Take everything out", next to the House of Colour piles. House of Colour itself advises "Don't dump everything on the bed at once." This is not attributed to House of Colour, so it is not wrong; just be aware.

19. **MINOR (optional): vacuum bags framed only as space-savers**
    - The English Heritage top-tips PDF that the article already cites calls vacuum bags "particularly good" for protecting stored items from pests and damp. Hoareau says the same for bulky coats.
    - Option: change `Vacuum bags save space for bulky synthetics, but` to `Vacuum bags save space and keep moths out, but`

20. **MINOR: "take an afternoon for most wardrobes" is unsourced**
    - It is a soft estimate, which is fine for a how-to. Optionally say `about an afternoon`.

## Verified claims (wording and attribution checked on the live page)

- FCI depth page: "the minimum depth required to ensure functional storage for your clothing is 60cm". Single rail 1750/1800/1900 mm and lower double rail 850/900/950 mm (minimum / recommended / luxury). Shelf spacing 300 / 350–400 / 400–450 mm. The article's "single rail at 1800 mm" and "lower double-hanging rail at about 900 mm" are correct.
- FCI ceiling page: "Allow 105cm of vertical space for suits; 150cm for dresses and 90cm for skirts, shirts, and blouses." Also says the top band is for "off-season pieces", which supports "top shelf for out-of-season clothes".
- IKEA PAX PDF (ie): 100 cm for coats, 60–70 cm for hanging trousers, 25 cm for 10 folded t-shirts, 30 cm for 10 pairs of folded sweaters. All match the article and the diagram key.
- House of Colour: "Keep, Donate, Sell, and Repair/Alter"; "if you haven't worn it in a year, you probably won't wear it again" (said about everyday items).
- Ideal Home wardrobe article (updated 28 Aug 2025):
  - Hester Van Hien (Tidylicious): "Start with a category that you find easy, as a warm up."
  - The Declutter Hub (Ingrid Jansen and Lesley Spellman): "Place the clothes you use most where they're easiest to reach."; "Keep everyday and year-round items in your main wardrobe."; "Swap mismatched hangers for slim velvet ones where possible."; "wooden hangers are best for coats and suits".
  - Vicky Silverthorn (You Need a Vicky): "Hang clothes in categories, then within that, by sleeve length and colour…"; "Fold to a standard you can keep up".
  - Shannon Murphy (Simpl Living Co): "Use fabric storage boxes or baskets…".
  - Every one of these is attributed to the right person.
- The article's "clear shelf dividers" line is supported by Ideal Home's section "Invest in shelf separators".
- WRAP press release (7 Oct 2022): 118 items; "one quarter (26% - 31 items) were unworn for at least a year".
- Ideal Home reverse-hanger article: Hayley Forster gives the "several months" timescale. Helen Sanderson, "author of The Secret Life of Clutter", says "it can be a way to avoid decluttering".
- Homes & Gardens decluttering rules: Laura Price (The Home Organisation): "I don't recommend holding onto clothes that no longer fit you". Shannon Krause (Tidy Nest): "consider incorporating exercises like the one-in, one-out method throughout the year".
- Recycle Now: "around 49% of all unwanted textiles gets thrown in the rubbish bin each year"; "clothing and textile banks in supermarket and local car parks"; "Primark and M&S offer clothing donation banks in-store".
- Zero Waste Scotland (www URL loads): "Wash and dry clothes before donating"; "Shoes should be paired and secured with string or a rubber band"; textile banks "accept all unwanted textiles, not just good quality". This supports the article's worn-out-items line.
- Ideal Home small wardrobe article: Elizabeth Wickes (The Lifestyle Organiser): "Most of us wear 20% of our clothing 80% of the time".
- IKEA GB clothes guide: "Hang blouses, tops, skirts, and jackets"; "fold stretchy items like sweaters and knitted tops"; hang tailored, silk and linen trousers; "fold heavier trousers like jeans or sweatpants".
- Oliver Bonas: "hanging knitwear can cause it to stretch out or develop hanger marks".
- Woman & Home: Heather Tingle (professional organiser, APDO member) said both "the weight of them can cause issues with stretching" and "Don't put cashmere in any vacuum packaging, as this can damage the fibres". She is correctly credited for both, not Rachael Wood.
- Homes & Gardens velvet hangers: the writer says "Velvet hangers take up less space than thicker wooden and plastic hangers". The point that knits cling to velvet comes from Jennifer Q. Williams. "Homes & Gardens notes" is fine.
- Ideal Home hanger news (Jan 2022): Silverthorn says velvet hangers "with a bar across" "can often be too large for your clothing" and cause "nasty pulls on the shoulders". She says smaller hangers suit about a size 6–10.
- Livingetc: Cher Casey, professional organiser: "A rainbow organization can look beautiful, but it's often difficult to maintain".
- KonMari: "By folding clothes neatly and standing them up vertically".
- Homes & Gardens file folding (writer's own test): "allows us to see exactly what we have in one glance"; "jumpers and sweaters were simply too thick for this file folding".
- Ideal Home seasonal clothes: Simon Glanville (MD, A Place for Everything): "It's pretty cold by October in the UK…"; heavy coats away "in late March". Craig Hoareau (A Tidy Mind London): "Avoid cardboard boxes as these attract pests".
- English Heritage top tips PDF (Dee Lauder, May 2021): "Always ensure clothing is clean when storing in wardrobes…"; "take out and shake items hanging up inside your wardrobe at least once a month"; "Regularly vacuum around the bottom of wardrobes and any shelves".
- English Heritage control guideline PDF, freezing: "placed in plastic bags and exposed to -18°C for at least two weeks"; "do not remove items from the bag for at least 24 hours to prevent condensation problems".
  - The article's freezing advice is accurate, and freezing kills adults, eggs and larvae.
  - The article correctly avoids NHM's odd "-8°C for several days".
  - Which? also gives -18°C.
- NHM (mirror): "Clothes moths prefer low light levels and dirty fabrics".
- Which? (12 Aug 2026, current): traps "won't eradicate an infestation".
- Timberwise: "make sure that the wardrobe is not overfilled with clothes"; "let the clothes fully dry before putting them into the wardrobe". Packed wardrobes stop air circulating, which supports the "Overfilling the rail" mistake.
- Diagram: the internal geometry is consistent at 2.75 px/cm.
  - Wardrobe 220 × 200 cm.
  - Lower rail 90 cm; upper rail 198 cm (~2 m); top shelf 205 cm; single rail 180 cm.
  - Shelves at 75/110/145/180 cm, so 35 cm apart. Drawers 25–72 cm.
  - Key values (60 cm depth, 90 cm shirts, 150 cm dresses, 100 cm coats, 60–70 cm trousers, 30 cm / 25 cm folded stacks) all match FCI and IKEA.
  - Credit line ("Upper rail height and layout: our worked example") is honest.
  - The only diagram text issue is the desc sentence in issue 4 (plus optional issue 14).
