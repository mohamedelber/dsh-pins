
## 2026-10-26 Speed: delay GA (Site Kit gtag)
- Before (PSI mobile): article 83 / LCP 4.5s, calculator 80 / 4.9s, home 81 / 4.9s. Cause: gtag.js 180KB (Site Kit, handle google_gtagjs) in critical path.
- Test with Site Kit deactivated: article 98 / 2.2s, calculator 96 / 2.6s, home 94 / 3.0s. Site Kit reactivated same evening.
- Fix: WPCode PHP snippet "Delay Ga" (Run Everywhere, Active) filters script_loader_tag for google_gtagjs and loads gtag on first scroll/touch/mousemove/keydown/click or after 6s. Site Kit inline config untouched.
- LiteSpeed 7.1.3 has no "JS Delayed Includes" field; do not set Load JS Deferred=Delayed (would delay calculators).
- Verified: old tag gone, loader present, calculator inputs render. User PSI mobile after fix: 91.
- Next ideas: drop Bilbo Swash Caps preload (logo font), disable WP emoji, smaller card images on home, preload home hero bg, WebP.
