
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
