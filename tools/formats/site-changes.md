
## 2026-10-26 Speed: delay GA (Site Kit gtag)
- Before (PSI mobile): article 83 / LCP 4.5s, calculator 80 / 4.9s, home 81 / 4.9s. Cause: gtag.js 180KB (Site Kit, handle google_gtagjs) in critical path.
- Test with Site Kit deactivated: article 98 / 2.2s, calculator 96 / 2.6s, home 94 / 3.0s. Site Kit reactivated same evening.
- Fix: WPCode PHP snippet "Delay Ga" (Run Everywhere, Active) filters script_loader_tag for google_gtagjs and loads gtag on first scroll/touch/mousemove/keydown/click or after 6s. Site Kit inline config untouched.
- LiteSpeed 7.1.3 has no "JS Delayed Includes" field; do not set Load JS Deferred=Delayed (would delay calculators).
- Verified: old tag gone, loader present, calculator inputs render. User PSI mobile after fix: 91.
- Next ideas: drop Bilbo Swash Caps preload (logo font), disable WP emoji, smaller card images on home, preload home hero bg, WebP.

## 2026-10-26 Speed 2 + homepage SEO
- WPCode PHP snippet "Speed 2" (user added): preload home hero webp (fetchpriority high, front page only) + remove WP emoji. Verified: 1 image preload, 0 emoji scripts on home.
- Home page 105: Rank Math title "Small Space Organization Ideas That Work - Daily Space Hacks" (was "Home - Daily Space Hacks"); OG/Twitter image = hero 1480 webp 1200x675 (was 2021/04/Home-712x1024.jpeg); featured_media 1480 (not displayed on page, checked).
- Skipped on purpose: Kadence font preload (would drop Merriweather preload too), home room images (below fold, lazy), WebP via QUIC.cloud (later).

## 2026-10-27 Google docs review
- Oct 26 UGC spam guidance: embed pages /embed-calculators/*/ are noindex, search pages noindex, robots.txt blocks only /wp-admin/ → compliant. Minor: embed pages appear in on-site search results.
- Oct 1 gen-AI guidance (using-gen-ai-content): fact-check now also covers metadata (SEO title, meta description, alt text, schema). New article images get IPTC DigitalSourceType=trainedAlgorithmicMedia XMP via tools/blurfix.py fix(ai=True). Pins NOT tagged (Pinterest "AI modified" label). WP resized sub-sizes may drop XMP; original keeps it. Old images unchanged.

## 2026-10-27 Post 2186 under-stairs-cupboard-doors (user-approved exception to the Nov 3 no-edit rule)
- Replaced the short "Can You Buy Ready-Made…" section with "Where to Buy Under Stairs Cupboard Doors (and What They Cost)": 4 UK suppliers table (Wittswood £234.49, Doors Sincerely MDF 12-14 days, Doors Galore flush £425.46 / panelled ~£1,020-£1,970 / FD30 £671.34, Jewson up to 1050x2150) + 5 buyer checks (measurements, finish, ironmongery, no cooling-off for made to measure, fitting £80-£160 / carpenter £180-£320/day). Fact-checked: 26 claims, 2 fixes applied (tools/under-stairs-doors-buy/factcheck.md).
- Rank Math title "Under Stairs Cupboard Doors: 12 Ideas, Prices & Where to Buy"; new meta description. H1, slug, rest of article unchanged. Live page verified.
- Nov 3 measurement: treat 2186 as edited on Oct 27 (separate from the untouched pages). Recheck prices on monthly price sweeps.
- Same day: added Key Takeaways bullet "Buying one: … about £235 for a solid oak ledged door; see where to buy…" linking to #where-to-buy (anchor added to the buying H2). Verified live. No other edits planned on 2186 before Nov 3.

## 2026-10-27 GSC "Fonctionnalités d'IA générative" (beta) report is available for the site
- airing-cupboard-shelves, 28 days: 124 AI-feature impressions (AI Overviews + AI Mode) vs 872 total Web impressions in Performance (15 clicks) → ~14%. AI impressions started ~Oct 14, peak 22/day Oct 19.
- Earlier estimate "~1% AI" (conversational queries only) was too low: AI Overview impressions on normal queries are not visible in query text. Use this report for the real share; site-wide figure still needed (remove the page filter).
- 15 clicks vs 3 visible in query table: the rest are anonymized queries (privacy); page totals are complete.
- Site-wide AI report (28 days to ~Oct 25): 1,680 AI-feature impressions, 82 pages. Total Web impressions same window ≈ 10,556 (GSC daily sums Sep 28–Oct 25) → AI ≈ 16%, regular ≈ 84%. AI daily: ~50/day early Oct → 110–130/day late Oct.
  Top AI pages: laundry-closet-ideas 227, diy-closet-shelves 171, under-stairs-storage-ideas 162, hat-storage-ideas 138, airing-cupboard-shelves 124, under-stairs-cupboard-doors 119, purse-storage-ideas 70, wardrobe-depth 55, how-to-fold-clothes 52, toy-storage-ideas 33.
  Note: laundry-closet, under-stairs-storage, diy-closet-shelves rank ~25-35 organically but are cited often by AI.
  Nov 3 measurement: report AI impressions separately from total (export this report for Oct 27–Nov 2 vs previous 7 days).

## 2026-10-27 'Home images' WPCode snippet live
- wp_calculate_image_sizes filter for the 9 homepage room images → sizes '(max-width: 600px) 45vw, 230px'. Verified in the browser: the first 3 now download the 300x300 files (11–14 KB instead of 60–120 KB).
- PSI (user screenshots): homepage mobile 95, desktop 100. Before the speed work: mobile 81.

## 2026-10-28 GSC week check (Oct 26-27 complete-ish)
- Oct 26: 5 clicks / 1,035 impr / pos 18.6. Oct 27: 5 clicks / 1,559 impr / pos 12.3, BUT 821 of them = query "how to organize toilet" on bathroom-organization-ideas (Brazil 611, Russia 184, pos 3.5-8.5, 0 clicks) → anomaly (bot/rank-tracker or AI-mode noise); real Oct 27 ≈ 738. Exclude from the Nov 3 comparison.
- Pages Oct 26-28: airing-cupboard 3 clicks pos 8.0; under-stairs-cupboard-doors 180 impr pos 8.9 1 click (new title from Oct 27 not yet visible); color-coded-closet 65 impr pos 8.3 1 click; diy-closet-shelves pos 17.3 (was 25); wallpaper calc 55 impr pos 9.4 0 clicks.

## 2026-10-28 Accessibility contrast fixes (PSI flagged)
- Home 105: 'Start Here' Kadence button background #c85a32 → #a6481f (white text ~5.9:1; was ~4.2:1).
- Additional CSS (append, revision 3465): `.entry-content p a:not([class]), .entry-content li a:not([class]) {color:#A6481F}` hover #7E3415 — body text links sitewide (≥4.5:1 on white and #F7F1E9). Revert = remove those 2 lines.
- Site cache purged; LiteSpeed combined CSS hash changed. Verify with PSI accessibility (user).
- Round 2 (PSI still flagged the Free Tools grid): home 105 inline CSS .dsh-tools .tg #C85A32 → #A6481F, .tg.s #5E7D57 → #4F6B49, span.go #C85A32 → #A6481F; Additional CSS: latest-post dates #999 → #6E645C (rev 3469). Still #C85A32 as text elsewhere: .dsh-emb .epv/.eal on tool pages (check later).

## 2026-10-28 — Site rendered unstyled (fixed)
- Cause: after contrast edits + purges, cached HTML referenced LiteSpeed combined CSS `80142d78...css?ver=a1b13` which returned 404 → no styles.
- Fix: wp_clear_cache scope=site include_cdn=true → new ver=3e556 returns 200 on /, /under-stairs-cupboard-doors/, /wallpaper-calculator/. Verified Merriweather font, bg rgb(239,239,245), links #A6481F.
- Lesson: after any CSS change (Additional CSS / inline CSS), do ONE site purge with include_cdn, then verify the litespeed/css link returns 200. Don't purge URLs separately right after.

## 2026-10-28 — Full index check (GSC URL Inspection, 106 URLs)
- 103/106 indexed (all tools pages + homepage + 79 posts). Canonicals all match.
- Not yet: boho-bedroom-ideas (pub Oct 27, unknown), guest-bedroom-ideas (Oct 26, unknown), studio-apartment-ideas (Oct 25, discovered-not-indexed). All linked from home + /blog/ + in sitemap → normal for 1–3 day old posts. User to request indexing manually.
- wallpaper-calculator confirmed in page-sitemap.xml and indexed (pending item closed).
- 27 posts scheduled through 2027-01-28.

## 2026-10-28 — Link audit
- Broken internal links: 0 (111 pages, 146 internal URLs checked). External (737) not checked (CORS).
- Weak inbound (in-content links from other pages):
  0 stuffed-animal-storage-ideas | 1 boho-bedroom-ideas, studio-apartment-ideas, heat-pump-vs-condenser-dryer, small-laundry-ideas, built-in-wardrobe-ideas, bookshelf-decor-ideas, laundry-room-decor-ideas, medicine-cabinet-organization | 2 guest-bedroom-ideas, fridge-organization
- Proposed (awaiting approval): add 1 contextual link per source page.
- Watch for cannibalization on Nov 3: small-laundry-ideas vs small-laundry-room-ideas.
- APPLIED 2026-10-28 11:10 (user approved "ابدا"): 10 contextual links, 1 per source, via wp_replace_in_post max 1. URL purge only. All verified live, CSS 200.
  1006 toy-storage → stuffed-animal-storage ("stuffed animals")
  881 small-bedroom-storage → boho-bedroom (appended sentence)
  1084 storage-ideas-for-small-spaces → studio-apartment ("studio apartment")
  2039 small-utility-room → heat-pump-vs-condenser-dryer (appended sentence)
  1384 laundry-closet → small-laundry-ideas (appended sentence)
  745 small-walk-in-closet → built-in-wardrobe ("built-in look")
  1614 coffee-table-decor → bookshelf-decor (appended sentence)
  705 how-to-organize-a-laundry-room → laundry-room-decor (appended sentence)
  613 small-bathroom-storage → medicine-cabinet-organization (appended sentence)
  2229 box-room-bedroom → guest-bedroom ("guest room")
  Nov 3 note: these 10 source pages had a tiny edit on Oct 28 — not a content change.
