# Oct 26 2026 (14:14): user rule "stay inside the site's niche" (storage, organisation, small spaces)
Supersedes the Oct 26 "strong keywords" table in backlog-2026-10-24b.md.
Dropped as off-niche: how to hang curtains, how to paint a room, full vs queen / twin vs twin xl / king vs queen bed, wall panelling ideas, living room / kitchen colour ideas, feature wall / accent wall ideas.
Already covered on site (skip): shoe/toy storage, mudroom, downstairs toilet, utility room, kitchen storage, pantry, small closet organization, fridge organization, coffee table decor, guest bedroom, small space storage (1084), how to fold clothes (1191: avoid "how to fold shirts").
Volumes: Google Ads via DataForSEO, Oct 26. KD from user's Semrush still needed.
| Slot | Keyword | Mkt | Vol | Fmt | Overlap |
|---|---|---|---|---|---|
| Mon Jan 11 | how to fold a fitted sheet | US | 33,100 (UK 2.9K) | F1 | low (1191, link 871 linen closet) |
| Thu Jan 14 | how to organize a closet | US | 5,400 | F1 | med (798, 688) → whole-closet step-by-step |
| Thu Jan 21 | konmari method | US | 4,400 | F1 | low (1061) |
| Thu Jan 28 | dresser vs chest of drawers | US | 2,900 | F3 | low |
| Mon Feb 1 | small kitchen ideas | US 18.1K / UK 12.1K | | F2 | low–med (1073 storage) |
| Thu Feb 4 | how to fold towels | US | 4,400 | F1 | low (1191) |
| Mon Feb 8 | small bedroom ideas | US/UK 9.9K | | F2 | med (881, 2229) → design/layout angle |
| Thu Feb 11 | TBD after Semrush (non-F2) | | | | |
| Mon Feb 15 | what colour goes with grey | UK | 2.9K KD25 | F2 | unchanged (already approved) |
| Thu Feb 18 | TBD after Semrush (non-F2) | | | | |
Reserves (in niche): garage organization ideas US 14.8K; kitchen island ideas US 12.1K (storage angle, island-size tool); small home office ideas US 4.4K; bedroom storage ideas UK 3.6K; blanket storage ideas US 2.4K; small dining room ideas US 2.4K.

## Already checked earlier (from SKILL notes; user says the whole list was checked before, results not saved here)
- small bedroom ideas US 9.9K KD15 (Oct 15), garage organization ideas US 14.8K KD19 (Oct 15), garage storage ideas US 18.1K KD16, fold towels 590 KD28 (Oct 17), small living room ideas UK 5.4K KD33 / US 14.8K KD45, built in closet ideas US 1.0K KD39.
- LESSON: every Semrush result the user sends must be written into this file the same day, so we never ask him to check a keyword twice.

## Duplicate check vs site focus keywords (Oct 26, 103 posts: rank_math_focus_keyword LIKE queries + all titles/slugs)
DROPPED as duplicates: garage organization ideas (= 3307 garage storage ideas), how to organize a closet (= 798 small closet organization + 688 closet clean out), bedroom storage ideas (= 881), how to fold towels (inside 1191; Semrush 590 KD28).
CLEAN (no focus keyword overlap): small kitchen ideas, dresser vs chest of drawers, konmari method (related 1061 declutter), small home office ideas (related 1048 desk org), small dining room ideas, blanket storage ideas (related 871), kitchen island ideas.
MEDIUM risk: small bedroom ideas (881 storage, 2229 box room → layout/design angle only), how to fold a fitted sheet (1191 has a sheets method → dedicated step-by-step).
RULE: before proposing any keyword, run wp_list_posts meta_key=rank_math_focus_keyword LIKE <word> (status any). Do not fire dozens of parallel wp_get_post_meta calls: the site returned 502s.
