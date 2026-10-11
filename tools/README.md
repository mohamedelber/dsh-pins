# dailyspacehacks build tools
- helpers.py: Gutenberg block helpers (p, h2, h3, img, lst, table, summary, toc, diagram, ai_note). Set U (uploads month) and IMG = {n: (media_id, file, alt)} before use.
- shot.js: renders z.svg to z.png (NODE_PATH=$(npm root -g) node shot.js).
- example-utility-room/: full build.py + svg.py + img.json of post 2039 (copy the pattern for new posts).
- ../pinh.py: pin templates pin_h, pin_i, pin_collage, pin_labels, pin_sq (fonts in ../fonts).
- ../gen/generate.py + .github/workflows/gen-images.yml: push gen/<job>.json -> GitHub Action makes images with OpenAI (secret OPENAI_API_KEY) into gen/out/<job>/.
- ../fetch/*.txt + .github/workflows/fetch-images.yml: list of image URLs -> Action downloads them into fetch/out/ (the cloud shell cannot reach dailyspacehacks.com).
