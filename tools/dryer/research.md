# Research: Heat pump vs condenser dryer (UK) — dailyspacehacks.com
Research date: 23 Oct 2026. All figures were taken from pages opened during this session (WebFetch). Prices are as seen on 23 Oct 2026.
Quotes are the exact wording that WebFetch returned. Where WebFetch paraphrased instead of quoting, the entry is marked (paraphrase). Uncertain items are marked **[UNCERTAIN]**.

Format: fact | number | exact quote | URL

---

## 1. Ofgem price cap (1 Oct – 31 Dec 2026)

| Fact | Number | Exact quote | URL |
|---|---|---|---|
| Electricity unit rate, Direct Debit, GB average (England, Scotland, Wales) | **26.32p/kWh** | "you will pay on average 26.32 pence per kilowatt hour (kWh)" | https://ofgem.gov.uk/news/changes-energy-price-cap-between-1-october-and-31-december-2026 |
| Electricity standing charge | **54.83p/day** | "The daily standing charge is 54.83 pence per day." | same |
| Confirmation from Ofgem's rates page | 26.32p / 54.83p | "26.32 pence per kWh" … "54.83 pence daily standing charge" | https://www.ofgem.gov.uk/node/176588/ |
| Change vs previous cap | +4% (typical dual fuel, DD) | "energy prices will go up by 4% for a typical household who use electricity and gas and pay by Direct Debit" | https://ofgem.gov.uk/news/changes-energy-price-cap-between-1-october-and-31-december-2026 |
| Which? uses the same rate | 26.32p | "Annual energy costs are based on the October 2026 energy price cap of 26.32p per kWh for electricity." | https://www.which.co.uk/news/article/the-tumble-dryer-ban-what-does-it-mean-for-you-alPRI3r8KXPx |

Note: the standing charge is paid regardless of the dryer, so leave it out of the per-cycle costs. Search snippets (Uswitch, MoneyToTheMasses; not opened) suggest a further rise is forecast for January 2027. **[UNCERTAIN: forecast, not checked]**

---

## 2. Energy label basis and specific models

### 2a. Label basis: 160 cycles (Reg. 392/2012, current GB label until 18 Jan 2027)

| Fact | Number | Exact quote | URL |
|---|---|---|---|
| Annual kWh on the old (A+++–D) label is based on 160 cycles at full and partial load | 160 cycles | "Energy consumption 'X' kWh per year, based on 160 drying cycles of the standard cotton programme at full and partial load" | https://www.legislation.gov.uk/eur/2012/392 |
| Same, on a manufacturer spec sheet | 160 | "482.0 kWh per year, based on 160 drying cycles of the standard cotton programme" | https://media3.bosch-home.com/Documents/specsheet/en-GB/WTA74200GB.pdf |
| 392/2012 is being revoked in GB | revoked 19 Jan 2027 | "Regulation revoked by S.I. 2026/318 reg. 19(b)" (pending-changes note on legislation.gov.uk) | https://www.legislation.gov.uk/eur/2012/392 |
| The new GB label (from 19 Jan 2027) shows kWh **per 100 cycles**, not per year, on an A–G scale | per 100 cycles | "weighted average energy consumption per 100 drying cycles in kWh, rounded to the nearest integer"; "scale of energy efficiency classes from A to G" | https://lawplayer.com/uk/act/uksi-2026-318 (third-party copy of S.I. 2026/318) |

**Caveat for the calculation:** label kWh ÷ 160 gives a *weighted average* cycle (a mix of full and half loads, plus standby), not a full load. For example, the Beko condenser uses 4.75 kWh on a full load but its label works out at 3.51 kWh per cycle.

### 2b. Old-label class thresholds (392/2012 Annex VI)

| Class | EEI | URL |
|---|---|---|
| A+++ | EEI < 24 | https://www.legislation.gov.uk/eur/2012/392/data.html |
| A++ | 24 ≤ EEI < 32 | same |
| A+ | 32 ≤ EEI < 42 | same |
| A | 42 ≤ EEI < 65 | same |
| B | 65 ≤ EEI < 76 | same |
| C | 76 ≤ EEI < 85 | same |
| D | 85 ≤ EEI | same |

- EEI = AEC ÷ standard AEC × 100. Standard AEC = 140 × capacity^0.8 for condensers. For vented dryers it is 140 × c^0.8 − (30 × Tt/60), so vented dryers are judged against a different baseline (paraphrase of Annex VII).
- Condensation efficiency classes: A >90%; B 80–90%; C 70–80%; down to G ≤40%. Source: same URL.
- **[UNCERTAIN]** The new A–G thresholds (Schedule 12 of S.I. 2026/318) could not be read; the page was truncated. The new EEI method is different, so an old "B" is not the same as a new "B".

### 2c. Model spec table (old A+++–D label unless noted)

| Model | Type | Cap. | Rating | kWh/annum | H×W×D (cm) | Noise | Cotton full load | Price seen 23 Oct 2026 | URL |
|---|---|---|---|---|---|---|---|---|---|
| **Bosch Series 6 WQG24502GB** | Heat pump | 9 kg | A+++ | **193** | 84.2×59.8×61.3 | 61 dB(A) | not listed on Currys; sister model WQG245A0GB = 195 min | £649 (was £799, 23/09/26–20/10/26) | https://www.currys.co.uk/products/bosch-series-6-wqg24502gb-9-kg-heat-pump-tumble-dryer-white-10288375.html |
| Bosch WQG245A0GB (spec sheet) | Heat pump | 9 kg | A+++ | 193 | 84.2×59.8×61.3 | 61 dB(A) | 195 min | — | https://media3.bosch-home.com/Documents/specsheet/en-GB/WQG245A0GB.pdf |
| **Hisense 1Q DH1Q802BW2** | Heat pump | 8 kg | A++ | **235** | 84.5×59.5×55.0 | 64 dB(A) | 160 min (half 124) | £329 (was £349, 27/05/26–07/07/26) | https://www.currys.co.uk/products/hisense-1q-series-dh1q802bw2-8-kg-heat-pump-tumble-dryer-white-10279497.html |
| Samsung Series 5 DV90CGC0A0AEEU | Heat pump | 9 kg | A++ | 258 | 85×60×60 | 65 dB(A) | 210 min (half 145) | £629 (was £769, 19/08/26–22/09/26) | https://www.currys.co.uk/products/samsung-series-5-ai-energy-dv90cgc0a0aeeu-9-kg-heat-pump-tumble-dryer-white-10256928.html |
| Beko Pro BM3T3822W | Heat pump | 8 kg | A+ | 265 | 84.6×59.8×54.5 | 64 dB(A) | 199 min (half 125) | £314.97 | https://www.currys.co.uk/products/beko-pro-bm3t3822w-8-kg-heat-pump-tumble-dryer-white-10266315.html |
| Hotpoint C HSD 82M WW UK (PetHairCare) | Heat pump | 8 kg | A+ | 265 | 84.6×59.8×54.5 | 64 dB(A) | 209 min | £398.97 | https://www.currys.co.uk/products/hotpoint-pethaircare-c-hsd-82m-ww-uk-8-kg-heat-pump-tumble-dryer-white-10286246.html |
| **Beko DTKCE80021W** | Condenser | 8 kg | B | **561.1** | 84.6×59.7×56.8 | 66 dB(A) | 142 min (half 80) | £249 (was £269, 06/05/26–11/06/26) | https://www.currys.co.uk/products/beko-dtkce80021w-8-kg-condenser-tumble-dryer-white-10211744.html |
| Beko DTLCE80121W (EPREL fiche, same platform) | Condenser | 8 kg | B | 561.1 | — | 66 dB | 142 min; 4.75 kWh full, 2.53 kWh half; condensation eff. 81% | — | https://eprel.ec.europa.eu/fiches/tumbledriers/Fiche_762668_EN.pdf |
| **Indesit C YD C82 WWGL UK** | Condenser | 8 kg | B | **562** | 84.6×59.7×56.8 | 66 dB(A) | 142 min (half 80) | £259 | https://www.currys.co.uk/products/indesit-c-yd-c82-wwgl-uk-8-kg-condenser-tumble-dryer-white-10274212.html |
| Hotpoint C HD C92 WWGD UK | Condenser | 9 kg | B | 617 | 84.6×59.7×60.1 | 65 dB(A) | 149 min (half 84) | £299 (was £329, 27/05/26–16/06/26) | https://www.currys.co.uk/products/hotpoint-c-hd-c92-wwgd-uk-9-kg-condenser-tumble-dryer-white-10271702.html |
| **Bosch Series 4 WTA74200GB** (spec sheet) | Vented | 7 kg | C | **482.0** | 84.2×59.8×60.1 | 65 dB(A) | 128 min (half 77) | not found | https://media3.bosch-home.com/Documents/specsheet/en-GB/WTA74200GB.pdf |
| **Logik LVD7W18** | Vented | 7 kg | C | **520** | 84.0×59.5×55.0 | 69 dB(A) | 145 min (half 75) | £229 | https://www.currys.co.uk/products/logik-lvd7w18-7-kg-vented-tumble-dryer-white-10175587.html |
| Hotpoint H1D80WUK | Vented | 8 kg | C | not listed | 85×59.5×67 (Euronics) | 65 dB | 129 min (half 76) | see §10 | https://www.euronics.co.uk/p/HOTH1D80WUK |

Notes:
- Currys "was" prices often carry old date ranges (for example May–June 2026), so treat them as historical.
- **[NEW-LABEL WARNING]** On 23 Oct 2026 some retailer listings already show **new A–G letters** for heat pumps. Currys lists "BEKO Dry Guard BM3T3822NNW … Heat Pump … E" and "BEKO Pro Ironfinish B5T49251INW 9 kg Smart Heat Pump … B" (https://www.currys.co.uk/products/beko-pro-bm3t3833w-8-kg-heat-pump-tumble-dryer-white-10264594.html, which redirected to the listing). Appliances Direct lists Hotpoint CHSD84MWWUK heat pump as "C" (https://www.appliancesdirect.co.uk/p/chsd84mwwuk/hotpoint-chsd84mwwuk-freestanding-heat-pump-tumble-dryer). A heat pump showing "B"/"C"/"E" is on the new scale, so it cannot be compared directly with an old-scale "B" condenser. Readers will be confused by this, so explain it in the article.
- Typical rating bands per Hoover: "heat pump A+++ to A+, condenser B to C, vented C to D" (paraphrase). https://www.hoover-home.com/en_GB/blogs/news/choosing-the-right-tumble-dryer-heat-pump-vs-condenser-vs-vented

---

## 3. Savings claims (who says what)

| Who | Claim | Exact quote | URL |
|---|---|---|---|
| Currys TechTalk | up to 60% | heat pumps "use up to 60% less energy than a condenser dryer"; FAQ: "consume up to 50–60% less energy than condenser dryers" | https://www.currys.co.uk/techtalk/kitchen-and-home/laundry-advice/heat-pump-vs-condenser-tumble-dryers.html |
| Currys TechTalk | £209 vs £88/yr (2025 prices) | "a condenser dryer costs around £209 per year to run, while a heat pump dryer costs about £88 per year" | same |
| Beko | up to 50% | "can consume up to 50% less electricity than traditional vented or condenser models" | https://www.beko.co.uk/lifestyle/heat-pump-tumble-dryers-efficiency-pros-and-cons |
| Beko | up to £463/yr **[UNCERTAIN: basis not given, looks like a heavy-use marketing figure, do not use]** | "up to £463* per year in energy" | same |
| Hotpoint (AO meta description, ColdGuard 8 kg) | up to 77% | "using up to 77% less energy than B-class condenser dryers" | https://ao.com/product/chsd84mwwuk-hotpoint-coldguard-heat-pump-tumble-dryer-white-112801-126.aspx |
| Which? (Oct 2026 cap) | £54 vs £139/yr | "The average heat pump dryer we've tested costs £54 a year to run, compared to £139 annually for the average condenser." | https://www.which.co.uk/news/article/the-tumble-dryer-ban-what-does-it-mean-for-you-alPRI3r8KXPx |
| Which? | best heat pump £34/yr | most efficient tested "would add a mere £34 to your energy bills each year" | same |
| Which? | up to £1,200 over lifetime | "an average saving of up to £1,200 in your energy bills over that time" (10–15 year lifespan) | same |
| Which? (basis) | 3 loads/week | "We then calculate the annual running cost based on drying three cotton loads every week for a year." Vented: "around £140" | https://www.which.co.uk/reviews/tumble-dryers/article/how-to-buy-the-best-tumble-dryer-a2Xa42O3YWK7 |
| Which? | ~£85/yr saving | "around £85 a year compared to a condenser dryer"; "Energy costs can be half or even less" | https://www.which.co.uk/news/2021/03/why-heat-pump-tumble-dryers-cost-less-to-run-and-use-less-energy (page dated 01 Oct 2026) |
| UK Gov (DESNZ consultation, Jul 2025) | 564 vs 225 kWh/yr | condenser "564 kWh per year"; heat pump "225 kWh per year" | https://assets.publishing.service.gov.uk/media/6888ab90048fff613a4d5acd/raising-standards-for-household-tumble-dryers.pdf |
| UK Gov | ~£60 premium, payback ~2 yrs | upfront increase "around £60, on average"; payback "potentially within two years" | same |
| UK Gov | net £250 / £900 lifetime | net saving "£250" (12-yr life vs condenser, undiscounted); "£900" over 20-yr heat pump life (paraphrase) | same |
| AEG support | 561 vs 235 kWh | "the condenser model has an annual energy consumption of 561 kWh/annum" vs 235 kWh/annum for the heat pump (paraphrase) | https://support.aeg.co.uk/support-articles/article/how-long-does-a-full-load-dry-to-dry-take-in-a-dryer-heatpump-vs-condenser |

From the label figures in §2: Hisense A++ 235 vs Beko B 561.1 is **58% less**; Bosch A+++ 193 vs 561.1 is **66% less**; Beko A+ 265 vs 561.1 is **53% less**. So "up to 60%" holds for typical A++ models.

---

## 4. Drying temperatures and drying times

| Fact | Number | Exact quote | URL |
|---|---|---|---|
| Beko: condenser peak temperature | 70–75°C | "the maximum temperature reached in a condenser dryer is 70-75 °C" (heat pump ~50°C, paraphrase) | https://www.beko.co.uk/support/faqs/tumble-dryers/my-heat-pump-dryer-takes-long-time-to-dry-clothing |
| Currys: heat pump vs standard temperature | ~50°C vs 70–75°C | "running at a lower temperature - around 50°C instead of the standard 70–75°C" | https://www.currys.co.uk/techtalk/kitchen-and-home/laundry-advice/heat-pump-vs-condenser-tumble-dryers.html |
| Beko: drying times, 8 kg | 142 vs 197/209 min | "an 8kg condenser dryer typically requires 142 minutes for a cotton eco cycle"; A+ heat pump "takes about 209 minutes"; A++ "approximately 197 minutes" | https://www.beko.co.uk/lifestyle/heat-pump-tumble-dryers-efficiency-pros-and-cons |
| AEG: condenser vs heat pump | 145 vs 178 min | "The condenser model has an energy rating of B and a drying time of 145 minutes." Heat pump 178 min (paraphrase) | https://support.aeg.co.uk/support-articles/article/how-long-does-a-full-load-dry-to-dry-take-in-a-dryer-heatpump-vs-condenser |
| Currys FAQ | +20–30 min | "20–30 minutes extra per cycle compared to a condenser dryer" | https://www.currys.co.uk/techtalk/kitchen-and-home/laundry-advice/heat-pump-vs-condenser-tumble-dryers.html |
| Which? tests | almost 2× | "Heat pumps can often take almost twice as long to dry the same amount of clothing in our tests." | https://www.which.co.uk/news/article/the-tumble-dryer-ban-what-does-it-mean-for-you-alPRI3r8KXPx |
| Spec-sheet full-load times (§2c) | HP 160–210 min; condenser 142–149; vented 128–145 | see table | see table |

Claims about time differences vary a lot, from +20 min (Currys) to almost double (Which?). Label data from §2c gives roughly +15 to +65 min per full load.

---

## 5. Installation and space

| Fact | Number | Exact quote | URL |
|---|---|---|---|
| Heat pump in cupboard OK with airflow (Beko) | — | heat pump dryers can go in cupboards "as long as there's adequate space and airflow"; cupboard "is not ideal due to the lack of ventilation" (add vents or leave door open, paraphrase) | https://www.beko.co.uk/support/faqs/tumble-dryers/where-can-you-put-a-tumble-dryer |
| Condenser in cupboard (Beko) | — | "It's possible to place a condenser tumble dryer in a cupboard, but you must ensure proper ventilation." (louvred doors or leave door open, paraphrase) | https://www.beko.co.uk/support/faqs/tumble-dryers/where-can-you-put-a-condenser-tumble-dryer |
| Miele heat pump (en-GB manual): under worktop OK | — | "This tumble dryer is suitable for pushing under a worktop." Keep front intake and base gap clear: "The cool air intake at the front of the tumble dryer must not be blocked or covered." | https://media.miele.com/downloads/5a/41/01_C7F12828AC5F1FE0979321FE0E875A41.pdf |
| Hoover condenser manual: gap and lockable door | 12 mm | "There should be a gap of at least 12 mm between the machine and any obstrubtions." [sic]; "The appliance must not be installed behind a lockable door." | https://service.hoover.co.uk/media/giemhlfv/atd-c10tkex-31101120-instruction-manual-pdf.pdf |
| Hotpoint vented manual: under worktop gaps | 10 mm top / 15 mm sides | under a worktop keep 10 mm above and 15 mm at sides (paraphrase); "We do not recommend that the dryer is installed in a cupboard." | https://www.appliancesdirect.co.uk/PDFs/TVFS73BGP9_1_4542615_Original.pdf |
| Valberg heat pump (Belgian retailer manual, non-UK brand) **[weak source]**: built-in clearances | 25 mm top, 20 mm sides, 50 mm back | "25 mm at the top, 20 mm at the left and right sides and 50 mm at the back" | https://www.electrodepot.be/media/wysiwyg/page/notice/pdf/international/N10009318.pdf |
| Ambient temperature: Hoover condenser | 5–35°C | "the ambient room temperature must be between 5-35°C" | https://service.hoover.co.uk/media/giemhlfv/atd-c10tkex-31101120-instruction-manual-pdf.pdf |
| Ambient temperature: Hotpoint condenser (H2D81W) | 5–35°C | "The dryer must be installed in a room with a temperature ranging between 5°C and 35°C to ensure proper operation." | https://www.appliancesdirect.co.uk/PDFs/784670031H2D81WUK_1_9031943_Original.pdf?v=9 |
| Ambient temperature: Miele heat pump (GB) | 2–35°C | "The ambient room temperature should be between 2°C and 35°C." / "Do not install the tumble dryer in a room where there is a risk of frost occurring." | https://media.miele.com/downloads/5a/41/01_C7F12828AC5F1FE0979321FE0E875A41.pdf |
| Ambient temperature: Beko (all dryers) | not below 5°C | "Our tumble dryers should not be placed in an environment where the ambient temperature drops below 5°C." | https://www.beko.co.uk/support/faqs/tumble-dryers/can-i-put-a-tumble-dryer-in-my-garage |
| Which? on garages | 5–10°C typical; DryGuard/ColdGuard 0°C | Most brands "specify a minimum temperature anywhere between 5°C and 10°C"; Beko/Blomberg DryGuard "designed to perform in room temperatures as low as 0°C"; Hotpoint ColdGuard "designed to work efficiently in temperatures as low as 0°C"; heat pumps "require moderate room temperatures to function efficiently" | https://www.which.co.uk/news/article/can-i-put-my-laundry-appliances-in-the-garage-a5ecl4S26lJk (15 Oct 2026) |
| Which? on frost and warranty | — | "there are currently no dryers on the market that claim to work effectively at this temperature" (below freezing); out-of-spec use "will likely result in any claims on your warranty being denied" | same |
| Currys: cold garage slows drying | <10°C | "If your garage is unheated and drops below 10°C, you might notice slower performance." | https://www.currys.co.uk/techtalk/kitchen-and-home/laundry-advice/heat-pump-vs-condenser-tumble-dryers.html |
| Water tank vs drain hose (Miele HP) | — | "empty the condensate container after every drying programme"; "The condensed water can also be externally drained away via the drain hose at the back of the dryer." | https://media.miele.com/downloads/5a/41/01_C7F12828AC5F1FE0979321FE0E875A41.pdf |
| Water tank vs drain (Hoover condenser) | — | "the water can be discharged directly to a waste water drain pipe." | https://service.hoover.co.uk/media/giemhlfv/atd-c10tkex-31101120-instruction-manual-pdf.pdf |
| Drain hose height limit (Valberg) **[weak source]** | — | "The drain pipe shall not be higher than the dryer, otherwise the water cannot be drained." | https://www.electrodepot.be/media/wysiwyg/page/notice/pdf/international/N10009318.pdf |
| Stacking needs a kit (Hoover) | — | "a suitable stacking kit must be used according to the configuration of your appliance." | https://service.hoover.co.uk/media/giemhlfv/atd-c10tkex-31101120-instruction-manual-pdf.pdf |
| Stacking (Beko FAQ) | — | "A stacking kit is essential for stability and safety"; "Make sure your washer and dryer are compatible for stacking." | https://www.beko.co.uk/support/faqs/tumble-dryers/where-can-you-put-a-tumble-dryer |
| Stacking: dryer on top only, depth rules (Beko manual) | 60 cm TD needs WM ≥50 cm deep; 54 cm TD needs WM >45 cm | "Washing machine cannot be placed on top of the drying machine."; "60cm TD --> WM≥50cm / 54cm TD --> WM>45cm" | https://www.manualslib.com/manual/3479434/Beko-Bm3t4724ww.html |
| Stacking kits named (Bosch HP) | WTZ27400 / WTZ27410 | stacking kit with pull-out shelf WTZ27400; stacking kit WTZ27410 (paraphrase) | https://media3.bosch-home.com/Documents/specsheet/en-GB/WQG245A0GB.pdf |
| Miele stack | — | "The tumble dryer can be combined with a Miele washing machine in a washer-dryer stack." | https://media.miele.com/downloads/5a/41/01_C7F12828AC5F1FE0979321FE0E875A41.pdf |
| Vented: hose to outside, max length (Hotpoint) | 2.4 m | "The ventilation hose should not exceed a maximum length of 2.4 metres"; vent through a wall hole or partly open window, hose end pointing down; not into ducts used by gas or other fuel-burning appliances, and not into extractor-fan ducts (paraphrase) | https://www.appliancesdirect.co.uk/PDFs/TVFS73BGP9_1_4542615_Original.pdf |
| Vented needs outside access (Which?) | — | "The hose must be vented outside your property."; need to "feed through a window" | https://www.which.co.uk/reviews/tumble-dryers/article/how-to-buy-the-best-tumble-dryer-a2Xa42O3YWK7 |
| Vented: external wall/window (Hoover) | — | vented dryers "must be positioned against an external wall or window" | https://www.hoover-home.com/en_GB/blogs/news/choosing-the-right-tumble-dryer-heat-pump-vs-condenser-vs-vented |
| Only vented need an external vent (Beko) | — | "Only vented tumble dryers need an external vent to expel hot, moist air outside" | https://www.beko.co.uk/support/faqs/tumble-dryers/where-can-you-put-a-tumble-dryer |
| Currys install: services within 1.5 m | 1.5 m | water and electricity connections "within 1.5m of where you want your new machine to live" | https://www.currys.co.uk/products/hotpoint-c-hd-c92-wwgd-uk-9-kg-condenser-tumble-dryer-white-10271702.html |

Depth note for small spaces (from §2c): Beko/Hotpoint/Hisense 8 kg heat pumps are 54.5–55 cm deep. Bosch 9 kg is 61.3 cm (64.8 cm with door; Bosch spec sheet). Standard 60 cm-deep worktops are therefore fine, though door depth matters in narrow utility rooms.

---

## 6. Moisture and heat in the room

| Fact | Number | Exact quote | URL |
|---|---|---|---|
| Miele HP warms the room; needs ventilation | — | "The hot air that is blown out from the heat exchanger warms the room air."; "Permanent room ventilation during every drying programme." | https://media.miele.com/downloads/5a/41/01_C7F12828AC5F1FE0979321FE0E875A41.pdf |
| Beko: HP condensation risk | "moderate" | "the potential for condensation, especially in poorly ventilated spaces"; may "release warm, moist air back into the room"; "If possible, position your dryer in a room with windows or install an extractor fan to help move humid air outside." | https://www.beko.co.uk/support/faqs/tumble-dryers/do-heat-pump-dryers-cause-condensation |
| Beko: vented lowest condensation risk | — | vented has "the lowest risk of condensation as they expel moisture outside" | same |
| AEG: room size and seals | 10–12 m² | "Make sure then that the room is large enough (more than roughly 10-12 m2)."; "If the door seal is damaged, this can result in an unnecessarily large amount of moisture in the room." | https://support.aeg.co.uk/support-articles/article/excessive-moisture-in-room-on-walls-and-windows-where-the-tumble-dryer-is-located |
| Whitegoodshelp: condensers heat room, some moist air escapes | — | condenser dryers "still heat the air in the room during operation"; "allowing some moist air to escape into the room"; "Opening a window or door slightly during operation allows moist air to escape" | https://www.whitegoodshelp.co.uk/condenser-tumble-drier-causes-condensation/ |
| Condensation efficiency, i.e. how much water is captured | condenser 81%; Bosch HP 88% | Beko fiche: "Average condensation efficiency (C dry) 81 %"; Bosch WQG245A0GB: 88% average (class B; the spec sheet also says A in another place, an inconsistency) | https://eprel.ec.europa.eu/fiches/tumbledriers/Fiche_762668_EN.pdf ; https://media3.bosch-home.com/Documents/specsheet/en-GB/WQG245A0GB.pdf |
| Legal minimum condensation efficiency (new GB rules) | 80% | "the condensation efficiency of a condenser tumble dryer must not be lower than 80%" | https://lawplayer.com/uk/act/uksi-2026-318 |
| Hotpoint vented manual | — | "Make sure that the room in which the tumble dryer is installed is not damp, and that it is adequately ventilated." | https://www.appliancesdirect.co.uk/PDFs/TVFS73BGP9_1_4542615_Original.pdf |

Derived point (my inference, flag it as such in the article): a condenser at 81% efficiency lets about 19% of the water out into the room, and a heat pump at 88% about 12%. On a 4 kg partial load wrung to typical residual moisture this is a few hundred ml, so ventilate small rooms. **[UNCERTAIN: no exact volume calculated or sourced]**

---

## 7. Fire safety (UK)

| Fact | Exact quote | URL |
|---|---|---|
| LFB: clean filter every load | "Clean your tumble dryer filter after every load." | https://london-fire.gov.uk/safety/the-home/electrical-items/whitegoods |
| LFB: register appliances | "Always make sure new appliances are registered so that manufacturers can contact you in the event of any problems." | same |
| LFB: sockets | "Don't overload sockets with lots of energy-hungry appliances." | same |
| LFB (Feb 2025 incident news) | "Clean your tumble dryer filter after every load." / "If your white goods start making strange noises, don't ignore it." | https://www.london-fire.gov.uk/incidents/2025/february/firefighters-issue-white-goods-safety-reminder-following-fires-in-hackney-and-edmonton |
| Humberside FRS (15 Feb 2025) | "Clean the lint filter after every load to prevent dangerous build-up."; "Never overload your dryer."; "never leave your dryer running unattended or overnight."; "Never dry rags and materials that have been used to soak up flammable liquids."; vent pipe "free from kinks, blockages, or crushing" | https://humbersidefire.gov.uk/newsroom/news/important-fire-safety-warning-tumble-dryers |
| North Wales FRS | "Do not leave appliances running when you go out or go to bed."; "Register appliances at Register My Appliance and check for recalls." | https://www.northwalesfire.gov.wales/keeping-you-safe/at-home/looking-after-the-electrics/white-goods-safety/ |
| Hotpoint vented manual: cool-down | Do not switch off with warm items inside; if stopped early, remove and spread items so the heat can dissipate (paraphrase); "Clean the filter after each use." | https://www.appliancesdirect.co.uk/PDFs/TVFS73BGP9_1_4542615_Original.pdf |
| H&F council letter citing LFB (2016, older) | "Items should be removed from the dryer immediately after the cycle and shaken loose to assist cooling." | https://www.lbhf.gov.uk/sites/default/files/article_attachments/tumble-dryer-safety-advice-leader-letter-final.pdf |

**[NOT FOUND]** The Electrical Safety First tumble dryer page did not appear in search results, so no ESF quote was collected. Use LFB or the fire and rescue services above.

---

## 8. Regulation: what is being phased out (CONFIRMED vs NOT)

### Great Britain (England, Scotland, Wales): CONFIRMED
| Fact | Number/date | Exact quote | URL |
|---|---|---|---|
| Instrument | S.I. 2026/318, made 19 Mar 2026 | "The Ecodesign for Energy-Related Products and Energy Information (Household Tumble Dryers) Regulations 2026 (S.I. 2026/318)" | https://lawplayer.com/uk/act/uksi-2026-318 (third-party copy; legislation.gov.uk copy not opened) |
| Extent | GB only | regulations "extend to England and Wales and Scotland" | same |
| Ecodesign in force | 10 Apr 2026 | stage 1 in force 10 April 2026 (paraphrase) | same |
| EEI cap | ≤ 85 | EEI "must not be higher than 85" (Sch 2 para 2); ≤3 kg dryers exempt | same |
| Transition | to 18/19 Jan 2027 | dryers placed on the market 10 Apr 2026 – 19 Jan 2027 that comply with old 932/2012 are deemed compliant (reg 15, paraphrase) | same |
| New A–G label | in force 19 Jan 2027 (transitional labels from 19 Sep 2026) | "scale of energy efficiency classes from A to G" | same; dates also on https://www.tuv.com/regulations-and-standards/en/uk-ecodesign-regulations-2026-for-household-tumble-dryers.html |
| Effect: vented, condenser and gas leave the market | from 19 Jan 2027 | "new vented, condenser and gas-fired tumble dryers will no longer be allowed onto the Great Britain market"; "Heat pump tumble dryers that meet the new requirements will remain available." | https://retra.co.uk/news/tumble-dryer-sales-restrictions-to-come-into-force-in-2027/ (24 Aug 2026) |
| Existing owners and second-hand unaffected | — | "existing owners will not be required to replace conventional machines"; "Second-hand sales of existing vented and condenser machines will also remain permitted." | same |
| Which? | — | "most tumble dryers available to buy from 19 January 2027 will be heat pump models"; non-compliant stock placed before then "will continue to be available to buy until stocks have been depeleted" [sic]; "The ban does not affect washer-dryers" | https://www.which.co.uk/news/article/the-tumble-dryer-ban-what-does-it-mean-for-you-alPRI3r8KXPx (9 Jul 2026) |
| Gov consultation rationale | EEI 85 phases out non-HP | would phase out "inefficient gas-fired, air-vented, and condenser tumble dryers"; HP already "74% of models sold" (condenser ~20%, vented ~5%, gas 0.4%) | https://assets.publishing.service.gov.uk/media/6888ab90048fff613a4d5acd/raising-standards-for-household-tumble-dryers.pdf |
| Repairability | 10 years parts; 15 working days | spare parts "at least 10 years after placing on the market the last unit of the model concerned"; delivery within 15 working days (paraphrase) | https://lawplayer.com/uk/act/uksi-2026-318 |
| Whitegoodshelp framing | — | "This is a change to what can be sold as new, not a change to what can be owned, used, repaired, or traded second-hand." | https://www.whitegoodshelp.co.uk/?p=35694 |

### Northern Ireland and EU: CONFIRMED that EU rules apply; effect PARTLY INFERRED
| Fact | Exact quote | URL |
|---|---|---|
| EU 2023/2533 (ecodesign) and 2023/2534 (label) apply from 1 Jul 2025 | ecodesign provisions "will apply from 1 July 2025"; label "will apply from 1 July 2025" | https://assets.publishing.service.gov.uk/media/65ca1e8a9c5b7f000c951cea/9_February_2024_EM_C_23_7671_and_4741_-_Tumble_dryers.pdf |
| Apply in NI | "The Regulations will apply in NI in accordance with the Windsor Framework." | same |
| NI continues EU rules | NI "continues to apply EU ecodesign and energy labelling regulations" | https://assets.publishing.service.gov.uk/media/6888ab90048fff613a4d5acd/raising-standards-for-household-tumble-dryers.pdf |
| EU EEI cap is also 85 | "must not have an Energy Efficiency Index (EEI) higher than 85"; condensers "shall not be lower than 80%" | https://seai.ie/sites/default/files/2025-01/Notice%20for%20manufacturers%20importers%20-%20tumble%20dryers_0.pdf |
| Supporting sign | Currys lists the Beko DTKCE80021W condenser as "not available to customers in Northern Ireland." | https://www.currys.co.uk/products/beko-dtkce80021w-8-kg-condenser-tumble-dryer-white-10211744.html |

- **[UNCERTAIN]** No official source opened says explicitly that the EU rules ended conventional condenser and vented sales in NI or the EU. It is inferred from the same EEI ≤85 cap that the UK Government says phases them out in GB, and from the Currys NI restriction.
- **[CONFLICT]** Whitegoodshelp says NI's date is "approximately six months ahead of the GB date". 1 Jul 2025 vs 19 Jan 2027 is about 18 months, so do not repeat the "six months" claim.

---

## 9. Maintenance

| Fact | Exact quote | URL |
|---|---|---|
| Hotpoint condenser: filter every cycle, condenser monthly | "Cleaning the door filter after each cycle"; "Remove the condenser unit regularly (monthly)" | https://www.appliancesdirect.co.uk/PDFs/784670031H2D81WUK_1_9031943_Original.pdf?v=9 |
| Hoover condenser | "Clean the filter and empty the water container after every drying cycle."; "Regularly clean the condenser." | https://service.hoover.co.uk/media/giemhlfv/atd-c10tkex-31101120-instruction-manual-pdf.pdf |
| Beko HP: filters and evaporator | "make sure the filters and the evaporator are cleaned regularly", "ideally after every few cycles" | https://www.beko.co.uk/lifestyle/heat-pump-tumble-dryers-efficiency-pros-and-cons |
| Miele HP: fluff filters each cycle, plinth filter when indicated | fluff filters after each cycle; plinth filter when the light comes on or the running time "seems to be taking longer than usual" (paraphrase) | https://media.miele.com/downloads/5a/41/01_C7F12828AC5F1FE0979321FE0E875A41.pdf |
| Bosch HP: self-cleaning condenser | "Self-Cleaning Condenser: Automatic fluff-cleaning condenser." (Currys: cleans up to 4 times per cycle, paraphrase) | https://media3.bosch-home.com/Documents/specsheet/en-GB/WQG245A0GB.pdf ; https://www.currys.co.uk/products/bosch-series-6-wqg24502gb-9-kg-heat-pump-tumble-dryer-white-10288375.html |
| Beko "environment friendly filter" | "If you are using environment friendly filter, you are not required to clean the filter after every cycle." | https://www.manualslib.com/manual/3479434/Beko-Bm3t4724ww.html |
| Whitegoodshelp: HP downside | "can take slightly longer per cycle, and require the condenser system to be cleaned regularly." | https://www.whitegoodshelp.co.uk/?p=35694 |
| Lifespan: Which? | about 10–15 years (paraphrase, in the context of "up to £1,200" savings) | https://www.which.co.uk/news/article/the-tumble-dryer-ban-what-does-it-mean-for-you-alPRI3r8KXPx |
| Lifespan: Gov assumptions | condenser 12-year, heat pump 20-year lifetimes used in the cost-benefit analysis (paraphrase) **[assumption, not a guarantee]** | https://assets.publishing.service.gov.uk/media/6888ab90048fff613a4d5acd/raising-standards-for-household-tumble-dryers.pdf |
| Beko guarantee | "All our tumble dryers also come with a Beko 10-Year Parts Guarantee." | https://www.beko.co.uk/lifestyle/heat-pump-tumble-dryers-efficiency-pros-and-cons |

---

## 10. Prices seen 23 Oct 2026

**Cheap 8–9 kg condenser (old label B)**
- Beko DTKCE80021W 8 kg: **£249**, Currys. https://www.currys.co.uk/products/beko-dtkce80021w-8-kg-condenser-tumble-dryer-white-10211744.html
- Indesit C YD C82 WWGL UK 8 kg: **£259**, Currys. https://www.currys.co.uk/products/indesit-c-yd-c82-wwgl-uk-8-kg-condenser-tumble-dryer-white-10274212.html
- Logik LCD8W23 8 kg: **£259**, Currys listing.
- Hotpoint C HD C92 WWGD UK 9 kg: **£299**, Currys. https://www.currys.co.uk/products/hotpoint-c-hd-c92-wwgd-uk-9-kg-condenser-tumble-dryer-white-10271702.html

**Cheap 8–9 kg heat pump**
- Logik LHP8W26 8 kg A+: **£299**, Currys listing (kWh not checked).
- Beko Pro BM3T3822W 8 kg A+: **£314.97**, Currys. https://www.currys.co.uk/products/beko-pro-bm3t3822w-8-kg-heat-pump-tumble-dryer-white-10266315.html
- Hisense DH1Q802BW2 8 kg A++: **£329**, Currys. https://www.currys.co.uk/products/hisense-1q-series-dh1q802bw2-8-kg-heat-pump-tumble-dryer-white-10279497.html
- Hoover HBR 9N2X-80 9 kg A++: **£379**, Currys listing.
- (Premium: Bosch WQG24502GB 9 kg A+++ £649)

**Cheap vented (few left on sale)**
- Logik LVD7W18 7 kg C: **£229**, Currys, the only vented model on Currys' vented page. https://www.currys.co.uk/products/logik-lvd7w18-7-kg-vented-tumble-dryer-white-10175587.html ; listing https://www.currys.co.uk/deals-on-computing/computing-deal/vented-tumble-dryers
- Indesit CYDA81WWGLUK 8 kg: **£269**, Appliances Direct, marked "This product is no longer available." **[stale]** https://appliancesdirect.co.uk/p/78855866/1/cyda81wwgluk/indesit-788558661cyda81wwgluk--freestanding-vented-tumble-dryer
- Hotpoint H1D80WUK 8 kg C: about **£381**, Atlantic Electrics. Only instalments were shown: "£127.00" ×3 and "£95.25" ×4, so the total is derived. **[UNCERTAIN]** https://www.atlanticelectrics.co.uk/products/hotpoint-h1d80wuk-8kg-freestanding-air-vented-tumble-dryer-in-white
- electriq 7 kg vented: £199.97 via Amazon Marketplace (PriceSpy aggregate, not opened directly). **[weak]** https://pricespy.co.uk/s/vented-tumble-dryer-uk/

Which? price ranges: heat pumps "around £350, but they're more likely to cost around £500+"; condensers "start at around £220"; vented "can cost as little as £250" (table says £219). https://www.which.co.uk/reviews/tumble-dryers/article/how-to-buy-the-best-tumble-dryer-a2Xa42O3YWK7 . Which? (Jul 2026): average tested heat pump "just over £600". https://www.which.co.uk/news/article/the-tumble-dryer-ban-what-does-it-mean-for-you-alPRI3r8KXPx

**Cheapest-vs-cheapest premium:** Hisense A++ £329 vs Beko condenser £249 = **£80** (Gov estimate: about £60).

---

## 11. People Also Ask: answer notes

1. **Why are condenser dryers being phased out?** GB S.I. 2026/318 sets EEI ≤85. The UK Government says this phases out "inefficient gas-fired, air-vented, and condenser tumble dryers". From 19 Jan 2027 new stock must comply. Existing machines and second-hand sales are unaffected. NI has applied the EU equivalent (also EEI ≤85) since 1 Jul 2025. Heat pumps were already 74% of models sold (Gov).
2. **Downside of a heat pump?** Longer cycles: Beko gives 142 vs 197–209 min, and Which? says "almost twice as long" in some tests. Higher upfront price: about £60–80 more at the cheap end. Heavier (Beko). They need regular filter and heat-exchanger/evaporator cleaning. They work poorly in cold rooms (most need 5°C+; ColdGuard/DryGuard 0°C). They warm the room and release some moisture.
3. **Worth paying extra?** At 26.32p, a typical A++ (235 kWh) vs B condenser (561 kWh) saves about £56/yr at 2 loads/week, £112 at 4, and £195 at 7. An £80 premium pays back in about 17 months, 9 months or 5 months respectively. Which?: about £85/yr, up to £1,200 over the dryer's life. From Jan 2027 there is little choice in GB anyway.
4. **Heat pump in a cupboard?** Generally yes, if the cupboard has airflow (Beko). Keep the front air intake and base gap clear (Miele). Not behind a lockable door (Hoover/Hotpoint manuals). Leave gaps per the manual (e.g. 10–25 mm), add vents or louvred doors, or leave the door open while it runs. Use the drain hose if the tank is hard to reach.
5. **Do heat pump dryers cause damp?** They can a little. Beko rates the condensation risk as "moderate", and Miele says the exhaust "warms the room air" and the room needs "Permanent room ventilation". Condensation efficiency of 80–90% means 10–20% of the water escapes. Ventilate, use rooms over about 10–12 m² (AEG), keep filters and seals clean, and use a window or extractor fan. It is still far less moisture than drying on airers indoors (general knowledge, not sourced).

---

## 12. Running-cost table (computed)

Method: label kWh/annum ÷ 160 = kWh per (weighted) cycle; × cycles/week × 52 × **26.32p/kWh** (Ofgem, 1 Oct–31 Dec 2026, DD, GB average). This excludes the standing charge and assumes the rate holds all year. The cap changes quarterly.

| Model (type, cap, label) | kWh/annum | kWh/cycle | Cost/cycle | 2/wk (104 cycles) | 4/wk (208) | 7/wk (364) |
|---|---|---|---|---|---|---|
| Bosch WQG24502GB (HP, 9 kg, A+++) | 193 | 1.206 | 31.7p | £33.02 | £66.04 | £115.56 |
| **Hisense DH1Q802BW2 (HP, 8 kg, A++), typical HP** | 235 | 1.469 | 38.7p | **£40.20** | **£80.41** | **£140.71** |
| Beko BM3T3822W (HP, 8 kg, A+) | 265 | 1.656 | 43.6p | £45.34 | £90.67 | £158.68 |
| **Beko DTKCE80021W (condenser, 8 kg, B), typical condenser** | 561.1 | 3.507 | 92.3p | **£95.99** | **£191.99** | **£335.98** |
| Hotpoint C HD C92 WWGD (condenser, 9 kg, B) | 617 | 3.856 | 101.5p | £105.56 | £211.11 | £369.45 |
| **Bosch WTA74200GB (vented, 7 kg, C), typical vented** | 482 | 3.013 | 79.3p | **£82.46** | **£164.92** | **£288.61** |
| Logik LVD7W18 (vented, 7 kg, C) | 520 | 3.250 | 85.5p | £88.96 | £177.92 | £311.37 |

Annual difference, typical HP (Hisense 235) vs typical condenser (Beko 561.1):
- 2/wk: **£55.79**; 4/wk: **£111.58**; 7/wk: **£195.26**
- Payback on the £80 price gap (£329 vs £249): about 17 months / 9 months / 5 months.
- Best HP (Bosch 193) vs condenser: £62.97 / £125.95 / £220.41.

Typical HP vs typical vented (Bosch 482): £42.26 / £84.51 / £147.90 per year.

Cross-checks:
- At exactly 160 cycles/yr (label basis, about 3/wk) the Hisense HP costs £61.85/yr and the Beko condenser £147.68/yr. Which? gives £54 vs £139 at 3 loads/week (it uses its own test kWh), which is consistent.
- Full-load reality check: the Beko condenser uses 4.75 kWh on a full load, about **£1.25 per full load**, vs 92p "average" cycle. Full loads cost more than the table suggests.
- Vented dryers look cheaper per kWh than condensers here partly because 7 kg vs 8 kg capacity and the shorter cycle. Per kg dried, the gap narrows.
