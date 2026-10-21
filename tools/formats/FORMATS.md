# DailySpaceHacks article formats (adopted Oct 21, 2026)

Five formats replace the single fixed template used for posts up to Oct 20.
Selection rule:
1. INTENT FIRST: before writing, check the live top 10 (DataForSEO serp_organic_live_advanced) and classify what Google rewards
   (list of ideas / how-to steps / comparison / checklist-printable / personal project). Only formats that match are allowed.
2. ROTATION SECOND: among the allowed formats, never repeat the format of the previous post; prefer the one used least in the
   last 5 posts (`python3 pick.py F1 F3` prints the best choice from log.csv).
3. Log every new post in log.csv (date, post_id, slug, keyword, format, market).

Universal quality layer (every format, non-negotiable):
- A direct answer to the main question within the first 120 words (AI features quote these).
- At least one ORIGINAL element: our own diagram, measurement table, calculator link or worked example.
- Verified external sources (only what the source literally says), US or UK conventions, safety notes where relevant.
- 4+ natural internal links; AI disclosure line; independent fact-check + image QA before publishing.
- First-hand note from Mohamed ONLY if he actually did it (never invent experience).
Banned as defaults (use only when they truly help): Key Takeaways box with "Quick answer", Time/Cost/Difficulty line,
Quick Pick table, "Final Thoughts" heading, fixed 4-5 FAQ block, Save-to-Pinterest box in every post.

---------------------------------------------------------------------------------------------------------------------
## F1. Step-by-step guide  (intent: "how to ...", "how do I ...", fix/build/install)
Length 1,000-1,800 words. Title pattern: "How to X (in N Steps)" or "How to X Without Y".
Structure (pick ONE opening):
- a) 2-sentence answer + "What you need" box (tools/materials with sizes) → steps
- b) the problem in one paragraph + a measured diagram → steps
Steps: 5-9 numbered H2 or H3 steps, each = action + exact measurement/why + photo or diagram where it helps.
Then 1-2 of: "If your X is different" (variations), "Mistakes that cost time", "How long it lasts / maintenance".
Ending options: "Do this first" summary list / "When to call a pro" / short FAQ (max 3, only real PAA questions).
Images: 1 hero + 2-4 step images (or one process diagram). Pin: step strip or before/after.
Examples: how to organize under bathroom sink; how to create an airing cupboard without a boiler; how to hang a pegboard.

## F2. Short ideas list  (intent: "... ideas", inspiration)
Length 1,200-2,000 words. 8-12 ideas (NOT 16-20). Title: "N X Ideas That ..." / "X Ideas for Small Spaces".
Structure: 1 paragraph intro with the best idea named up front → grouped ideas (by budget / by room size / by style —
vary the grouping axis per post) → each idea 80-150 words with a concrete detail (size, price band, where it works,
where it fails). Optional: "How to choose" mini-section OR a comparison strip — not both.
Ending options: "If you only do one thing" / "Mix and match" combos / nothing (end on the last idea + links).
Images: hero + 4-6 idea images. Pin: cozy collage (current pin template).

## F3. Comparison + recommendation  (intent: "X vs Y", "best type of", "which ... should I")
Length 1,000-1,600 words. Title: "X vs Y: Which Is Better for Z?" / "Best X for Small Spaces: N Types Compared".
Structure: verdict first (who should pick what, 3 lines) → comparison TABLE (price, size, durability, renter-friendly,
install effort) → one section per option (best for / avoid if / real numbers) → "Our pick for…" by scenario.
Ending: decision checklist (3-5 yes/no questions). No idea count in the title.
Images: hero (both options side by side) + 1 per option. Pin: side-by-side "X or Y?" design.
Examples: wire vs wood pantry shelves; vented vs condenser dryer for a utility cupboard; tension rod vs mounted shelf.

## F4. Real project diary  (requires Mohamed's own photos — never fake)
Length 800-1,500 words. Title: "How I Organized My X (Before and After)" / "We Tidied a Messy X in One Afternoon".
Structure: the real before photo + the problem → what we used (with actual cost) → steps with real photos →
after photo → what worked / what we would change → link to the matching ideas or how-to post.
First person ("I"/"we") is allowed ONLY here. Images: real photos only (AI images forbidden in this format).
Pin: real before/after.

## F5. Checklist / printable  (intent: plan, prepare, "checklist", seasonal prep)
Length 600-1,200 words + a printable PDF (reportlab, see tools/moving-checklist/mkpdf.py) or an on-page interactive checklist.
Title: "X Checklist (Free Printable)". Structure: who it is for + when to start → the checklist grouped by time or area →
short notes only where an item needs a measurement/safety note → download box → 2-4 related links.
Images: hero + printable preview. Pin: the checklist page itself (saves well).
Examples: guest-ready home checklist for the holidays; Christmas decoration packing checklist; small-flat move-in checklist.

---------------------------------------------------------------------------------------------------------------------
## Variation inside a format (avoid a new fingerprint)
- Rotate the opening (answer-first / problem-first / number-first), the closing heading
  (e.g. "Where to start", "The short version", "Before you buy", "If you only do one thing", or no closing heading),
  heading style (questions vs statements), and where the diagram sits.
- Change the grouping axis of ideas (budget, room size, style, renter vs owner).
- Lengths vary with the topic; never pad to a word count.
