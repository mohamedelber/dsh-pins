# Fact-check: Feng Shui Bedroom (content.html)

Checked 2026-10-25. Each source below was found through WebSearch and then fetched with WebFetch. Quoted text is the visible text (build.py wraps anchors in `{SR('key','anchor')}`; the key is given where a link needs to change).

Severity: MUST-FIX = wrong attribution, wrong link or a false statement. SHOULD-FIX = breaks the editorial line or is misleading. MINOR = wording or precision.

## Issues

1. **MUST-FIX: the death-position quote links to the wrong Livingetc article (Step 2, paragraph 2)**
   - Current text: `Deflorian told Livingetc this is known as the death position in feng shui, linked to the custom of carrying the dead out feet first. If you can't move the bed, her fixes are a solid footboard or a bench at the end of the bed, a folding screen, a heavy curtain, or simply closing the door at night.` (anchor: `{SR('livdeath','this is known as the death position')}`)
   - What is wrong: the linked page (livingetc.com/advice/feng-shui-death-position) does not mention Rosanna Deflorian. The phrase "known as the death position" is not on it, and neither are the folding screen, heavy curtain or closing-the-door remedies. That page quotes Marie Diamond and Anjie Cho ("Also known as the 'coffin position'"). The Deflorian quote, the feet-first funeral explanation and all of these remedies are on the bed-layout article that Step 2 already cites (`livbed`). The research notes (rows 11 and 12) give the wrong URL.
   - Evidence: https://www.livingetc.com/advice/bed-feng-shui-layout quotes Deflorian: "this is known as the death position in" Feng Shui; "In funeral wakes, the deceased are placed with their feet towards the door"; "use a high footboard or bench, a folding screen, or a heavy curtain between the bed and the door"; "keep your bedroom door closed at night." https://www.livingetc.com/advice/feng-shui-death-position quotes only Marie Diamond ("Feng Shui master") and Anjie Cho. The words "Deflorian", "heavy curtain" and "folding screen" do not appear on it.
   - Fix: change `SR('livdeath', ...)` to `SR('livbed','this is known as the death position')`. Also change "a solid footboard" to "a high footboard" (her word). Suggested text: `Deflorian told Livingetc {SR('livbed','this is known as the death position')} in feng shui, linked to the custom of carrying the dead out feet first. If you can't move the bed, her fixes are a high footboard or a bench at the end of the bed, a folding screen, a heavy curtain, or simply closing the door at night.`

2. **MUST-FIX: Roynon's mirror rule links to a page that does not contain it (Step 5)**
   - Current text: `Roynon's rule is that a mirror never reflects the sleeper in bed` (anchor in build.py presumably `{SR('hgmir','a mirror never reflects the sleeper in bed')}`)
   - What is wrong: the linked Homes & Gardens mirrors article does not mention Suzanne Roynon, and the phrase "never reflects" is not on it. The page quotes Jessie Kim, Melissa Waite Stamps and Anna Lippett. The Roynon quote is in the Homes & Gardens article at the `hgcol` URL (title "9 Simple Feng Shui Bedroom Fixes to Invite Calm and Balanced Energy for Rest"), where she is quoted directly. Research notes row 22 gives the wrong URL.
   - Evidence: https://homesandgardens.com/interior-design/bedrooms/feng-shui-bedroom-colors: Suzanne Roynon, "Feng Shui consultant and interiors therapist": "The key Feng Shui aspects to consider are that a mirror never reflects the sleeper in bed." At https://homesandgardens.com/interior-design/where-should-mirrors-be-placed-in-a-bedroom-for-feng-shui, "Roynon" and "never reflects" are not found.
   - Fix: change the key to `SR('hgcol','a mirror never reflects the sleeper in bed')`. The Anna Lippett link to `hgmir` that follows is correct and stays.

3. **MUST-FIX: the beam advice is credited to Roynon but is Tom's Guide's own unattributed text, and the sloped-ceiling rule is stated as fact (Step 3, paragraph 2)**
   - Current text: `Practitioners also dislike beams or a low, sloped ceiling over the bed. In a Tom's Guide article produced with a mattress brand, Roynon suggests moving the bed out from under overhead beams; if the ceiling slopes, put the bed under the highest part of the room, which also gives you more headroom when you sit up.`
   - What is wrong: (a) In the Tom's Guide article, the beams section ("3. Your bed is under exposed beams") and the sloping-ceiling section have no speaker. They are the article's own text, not Roynon's. None of the Roynon quotes in the piece is about beams. (b) "put the bed under the highest part of the room" is a placement rule given as an instruction with no attribution, which breaks the editorial line. (c) "Practitioners also dislike" names no practitioner. (d) "produced with a mattress brand" is accurate but vague. The disclosure says it is a paid partnership with Nectar Sleep, and readers should be told that plainly.
   - Evidence: https://www.tomsguide.com/wellness/mattresses/if-your-bed-is-facing-any-of-these-things-experts-advise-moving-it-now-for-better-sleep: "Tom's Guide created this content as part of a paid partnership with Nectar Sleep." Unattributed text: "When overhead beams cross the bed, to Feng Shui, this may cause pain or reduced function..." and "it's best to position your bed and the bedhead or headboard in the highest part of the room." Roynon ("Feng Shui and interiors therapy expert") is quoted on the command position, mirrors and mirrored wardrobes, not on beams.
   - Suggested replacement: `Tom's Guide also advises against sleeping under beams or a low, sloped ceiling. In an article written as a paid partnership with mattress brand Nectar Sleep, it suggests moving the bed out from under {SR('tg2','overhead beams')} and, under a sloping ceiling, placing the bed and headboard in the highest part of the room, which also gives you more headroom when you sit up.`

4. **SHOULD-FIX: the intro gives the rules as plain instructions, with no attribution**
   - Current text: `A feng shui bedroom starts with the bed. Put it in the commanding position, with the headboard against a solid wall and the door in view but not straight in line with your feet. Then clear the floor and the space under the bed, keep mirrors from reflecting you while you sleep, and choose soft, earthy colors.`
   - What is wrong: these are placement and energy rules written as facts or commands. The attribution only comes later ("every rule is credited to the practitioner who gives it"). This paragraph is also the one most likely to be shown as a search snippet on its own.
   - Suggested replacement: `Feng shui practitioners start a bedroom with the bed. They advise the commanding position, with the headboard against a solid wall and the door in view but not straight in line with your feet, then a clear floor and an empty space under the bed, mirrors that don't reflect you while you sleep, and soft, earthy colors.`

5. **SHOULD-FIX: the intro says every rule is credited, but some are not**
   - Current text: `So in the seven steps below, every rule is credited to the practitioner who gives it`
   - What is wrong: several rules come from publications' own editorial text, not from a practitioner: Homes & Gardens on "nothing under the bed" and "18 inches", and Tom's Guide on beams and slopes (see #3). The "If Your Bedroom Is Different" bullets are not credited at all (see #6).
   - Suggested replacement: `So in the seven steps below, every rule is credited to the practitioner or publication that gives it`

6. **SHOULD-FIX: a placement rule in "If Your Bedroom Is Different" has no attribution**
   - Current text: `Turn the bed so the door is diagonal from it, even if that means a smaller nightstand on one side.`
   - What is wrong: a feng shui placement rule stated as an instruction. It is Deflorian's diagonal rule (Livingetc).
   - Evidence: https://www.livingetc.com/advice/bed-feng-shui-layout, Deflorian: "I recommend arranging the bed diagonally to the door so you have a clear view of the entrance."
   - Suggested replacement: `Following Deflorian's advice, turn the bed so the door is diagonal from it, even if that means a smaller nightstand on one side.`
   - Related, lower priority: `If the bed has to go against a side wall, keep the headboard on the solid wall and add a lamp on the open side.` Cho (Havenly) warns against pushing a bed against a wall. Consider adding: `(Cho prefers space on both sides, so treat this as a compromise)`.

7. **SHOULD-FIX: the under-bed storage advice contradicts the HGTV source cited in the previous sentence (Step 1)**
   - Current text: `If you need under-bed storage in a small room, keep it to soft, closed boxes of bedding or out-of-season clothes, not paperwork or things you are avoiding.`
   - What is wrong: the HGTV piece cited just before this sentence specifically warns against storing out-of-season clothes under the bed. As written, readers may think the sources allow it.
   - Evidence: https://www.hgtv.com/decorating/bedrooms/feng-shui-your-bedroom-pictures, editorial: don't "use the space under your bed to store boxes of out-of-season clothes."
   - Suggested replacement: `HGTV's guide advises against even boxes of out-of-season clothes, so if a small room leaves you no choice, keep it to soft, closed boxes of bedding or clothes, not paperwork or things you are avoiding.`

8. **MINOR: Barrett is credited with the HGTV editorial advice on where to hang art (Step 7, paragraph 2)**
   - Current text: `Barrett suggests hanging calm, uplifting art opposite the bed and keeping family photos elsewhere`
   - What is wrong: "on the wall opposite your bed" is HGTV's editorial voice ("practitioners recommend..."). Barrett's own words are that the last thing you see before sleep should be uplifting, and that family photos belong elsewhere. Those two points are correctly hers.
   - Evidence: HGTV: "hanging your favorite piece of art on the wall opposite your bed" (editorial); Barrett: "The last thing you see before you go to sleep and the first thing you see when you open your eyes..."; "You can have pictures of your parents and your kids all over the rest of the house."
   - Suggested replacement: `For the finishing touches, HGTV suggests hanging calm, uplifting art opposite the bed, and Barrett would keep family photos elsewhere`

9. **MINOR: the "pairs of lamps and nightstands" advice is HGTV's, not Collins's (Step 4)**
   - Current text: `Terah Kathryn Collins of the Western School of Feng Shui told HGTV to decorate your bedroom as if a partner is already there, with pairs of lamps and nightstands.`
   - What is wrong: the quote is Collins's. The "nightstands and lamps on both sides" line comes straight after it in HGTV's editorial voice. Collins's related words are that one nightstand "is very symbolic of solitude." (Collins is the founder of the Western School of Feng Shui, so "of" is acceptable.)
   - Suggested replacement: `Terah Kathryn Collins, founder of the Western School of Feng Shui, told HGTV to decorate your bedroom as if a partner is already there, and HGTV suggests matching nightstands and lamps on both sides.`

10. **MINOR: "very dark charcoal" (Step 6)**
    - Current text: `and also very dark charcoal`
    - Evidence: https://livingetc.com/advice/feng-shui-bedroom-colors, Cho: "charcoal grey should be avoided."
    - Suggested replacement: `and also charcoal grey`

11. **MINOR: Marie Diamond's suggested alternative is slightly narrowed (Step 7, paragraph 2)**
    - Current text: `and suggests botanical prints instead`
    - Evidence: https://www.livingetc.com/advice/feng-shui-houseplant-decorating-mistakes, Diamond: "using silk plants or decorating with botanical art."
    - Suggested replacement: `and suggests silk plants or botanical art instead`

12. **MINOR: framing sentences state the tradition's priorities as fact**
    - `This is the main rule of a feng shui bedroom layout.` Suggest: `Practitioners treat this as the main rule of a feng shui bedroom layout.`
    - `Mirrors are the most common question about a feng shui bedroom.` This superlative is unsupported. Suggest: `Mirrors are one of the most common questions about a feng shui bedroom.`
    - `Feng shui bedroom colors are about calm.` Suggest: `Practitioners choose feng shui bedroom colors for calm.`

13. **MINOR: "Sleep researchers agree" (Step 7)**
    - Current text: `Sleep researchers agree on the basics.`
    - What is wrong: the CDC and the Sleep Foundation are health organisations publishing guidance, not researchers reporting findings.
    - Suggested replacement: `Sleep health guidance agrees on the basics.`

14. **MINOR: the CDC link uses a legacy URL**
    - Current link: https://www.cdc.gov/sleep/about_sleep/sleep_hygiene.html (key `cdc`). The page still serves, but its canonical URL is now https://www.cdc.gov/sleep/about/index.html. The quote is confirmed: "Keeping your bedroom quiet, relaxing, and at a cool temperature." Update the key to the canonical URL.

15. **MINOR: "cost nothing" (closing paragraph)**
    - Current text: `Those five changes cost nothing`
    - What is wrong: item 5 (moving a desk or TV out) may cost something. Suggest: `Those five changes cost little or nothing`.

## Verified OK

- Britannica: "ancient Chinese practice of orienting significant sites, buildings, and the spaces and objects within them" (https://www.britannica.com/art/fengshui).
- Wikipedia: "...although there is no empirical evidence that it is effective" (https://en.wikipedia.org/wiki/Feng_shui).
- Sleep Foundation: queen 60 x 80 in ("A queen size mattress is 60 inches wide by 80 inches long"), full 54 x 75 in, and "Try to allow for at least 24 inches of space on the foot and either side of the bed." "Recommends" is a fair word for "try to allow".
- Arithmetic: 60 + 24 + 24 = 108 in wide; 80 + 24 = 104 in long; 108 in = 9 ft; 104 in = 8 ft 8 in. Correct in the text, the SVG and the `<desc>`.
- SVG plan geometry, at a scale of 3.4 px per inch in a 144 x 144 in room: bed 272 x 204 px = 80 x 60 in. Clearances: 30 in (head side), 54 in (other side), 64 in (foot). These add up: 30 + 60 + 54 = 144 and 80 + 64 = 144. All are at least 24 in, as the desc claims. The door (32 in) is on the wall beyond the foot of the bed, diagonal to it and not in line with the feet. The window is on the foot wall, so the headboard is not under it. The door swing does not hit the bed, and there are more than 36 in clear inside the door (Hunker).
- SVG "layouts practitioners avoid" panels match their labels: feet in line with the door; headboard under a window.
- SVG credit line: Cho, Deflorian (Livingetc) and McAllister (Tom's Guide) are correct sources for the commanding-position, diagonal and window rules.
- Hunker (Melanie Aves): "Three feet of clearance is essential from the doorway to the nearest furniture." It also gives 2 ft around the bed, which agrees with the 24 in figure.
- Jayme Barrett, "Los Angeles feng shui consultant" (HGTV): "clutter under the bed has its own energy, which can disturb sleep"; "The bedroom is a place where you need to turn off the stresses of the day."
- Homes & Gardens editorial: "nothing under the bed at all, other than a glass of water" and "ideally around 18 inches, on either side of the bed." Both are correctly credited to Homes & Gardens, not to a practitioner.
- Suzanne Roynon, "Feng Shui consultant and interiors therapist" (Homes & Gardens bed placement): "Ideally, you would be able to see the door from what we call 'the command position'."
- Anjie Cho, architect and feng shui expert: "see the main entryway to the bedroom when you're sitting up against the headboard" (a fair paraphrase as "sitting up in bed"); "solid headboard that's securely attached to your bed"; "upholstered or wood"; "make sure you're supported by a solid wall"; and "you can see the reflection of the door from your bed," given as the fix when the bed can't see the door.
- Rosanna Deflorian, classical feng shui consultant (More Than Intuition), Livingetc: "you can see the entrance without being directly in line with it"; recommends diagonal placement.
- Sarah McAllister, The Feng Shui Agency (Tom's Guide news article, no sponsorship disclosed): "Try not to place a bed beneath a window, especially if the window is right behind your head."
- Cho on Havenly: "A lot of people push their bed up against the wall or into a corner..."; "plants can bring kindness and growth to your bedroom."
- Cho, nightstands: "They don't have to match, but ideally, they should be similar in size."
- Collins (HGTV): "Treat them like windows and hang curtains in front of them," said of mirrored closet doors.
- Anna Lippett, holistic designer (Homes & Gardens mirrors article): "They reflect and amplify energy so avoid positioning opposite the bed..."
- Roynon (Homes & Gardens): "Calming gentle colors are superb in a bedroom, with earthy and softer tones..."
- Cho (Livingetc): "avoid bright green or bright blue."
- Laura Cerrano, certified feng shui expert (Hunker): "use The Five Elements Theory to help select the color scheme." The element colours match Hunker: earth beige/cream/soft brown; metal white/metallics; water blue/black; wood green; fire red/orange, limited to accents.
- Marie Diamond, feng shui master (Livingetc): plants "can disrupt restful Yin energy with too much upward, active movement."
- Sleep Foundation: "approximately 65 degrees Fahrenheit (18.3 degrees Celsius)"; "In response to darkness, the pineal gland begins to produce melatonin."; "put your cell phone, laptop, and tablet away at least 30 minutes before bed."
- CDC quote confirmed (see #14 for the URL).
- No health or luck claim is stated as fact. Barrett's "can disturb sleep" and Lippett's "amplify energy" are both attributed.
- The internal dailyspacehacks.com links were not checked; the sandbox blocked those fetches.
