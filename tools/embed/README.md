# Embed calculators (Oct 18)
- Hub page 2683 /embed-calculators/ (indexed). Child embed pages (noindex, Kadence header/footer off, body class dsh-embed):
  2685 christmas-tree-lights, 2692 wallpaper-rolls, 2693 storage-unit-size, 2694 tv-height, 2695 wardrobe-size,
  2696 rug-size, 2697 curtain-size, 2698 moving-boxes, 2699 shelf-spacing, 2700 washer-dryer-space.
- build.py makes out/page-*.html (embed page content), out/btn-*.html (button block inserted after the first <!-- /wp:html --> of each tool page), out/hub.html.
- Embed pages post their height (postMessage {dshEmbed,h}); the snippet's script resizes iframe.dsh-embed. heights.json = fallback heights.
- Button CSS lives in Additional CSS (.dsh-emb). Test: push tools/embed/test/host.html -> embed-test workflow screenshots each iframe.
- When a tool changes, update BOTH the tool page and its embed page. New tool: run build.py, create child page under 2683, add button + hub section.
