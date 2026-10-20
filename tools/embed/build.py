import html, json, os
S = 'https://dailyspacehacks.com/'
# (main slug, page id, embed slug, title, short line, tool file, height)
T = [
 ('moving-checklist-printable', 0, 'moving-checklist', 'Printable Moving Checklist', 'A week-by-week moving checklist that readers can tick off and print.', '../moving-checklist/tool.html'),
 ('chandelier-size-calculator', 2987, 'chandelier-size', 'Chandelier Size Calculator', 'The right chandelier width and hanging height for any room, table or kitchen island.', '../chandelier-calc/tool.html'),
 ('dining-table-size-calculator', 0, 'dining-table', 'Dining Table Size Calculator', 'The right dining table size for 2 to 12 people, and the room it needs.', '../dining-table/tool.html'),
 ('picture-hanging-height-calculator', 0, 'picture-height', 'Picture Hanging Height Calculator', 'How high to hang a picture, with the exact nail height.', '../picture-height/tool.html'),
 ('christmas-tree-lights-calculator', 2617, 'christmas-tree-lights', 'Christmas Tree Lights Calculator', 'How many lights, ornaments and garland a tree needs.', '../xmas-lights/tool.html'),
 ('wallpaper-calculator', 2638, 'wallpaper-rolls', 'Wallpaper Calculator', 'How many rolls of wallpaper for a wall or a whole room.', '../wallpaper-calc/tool.html'),
 ('storage-unit-size-calculator', 2659, 'storage-unit-size', 'Storage Unit Size Calculator', 'The right storage unit size for a home or a car.', '../storage-unit/tool.html'),
 ('tv-mounting-height-calculator', 2549, 'tv-height', 'TV Mounting Height Calculator', 'How high to mount a TV for comfortable viewing.', '../tv-calc/tool.html'),
 ('wardrobe-depth', 2579, 'wardrobe-size', 'Wardrobe Depth Calculator', 'How deep a wardrobe needs to be for hanging clothes.', '../wardrobe-depth/tool.html'),
 ('rug-size-calculator', 2403, 'rug-size', 'Rug Size Calculator', 'The right rug size for a living room, dining room or bedroom.', '../rug-calc/tool.html'),
 ('curtain-size-calculator', 2257, 'curtain-size', 'Curtain Size Calculator', 'Curtain width and drop for any window.', '../curtain-calc/tool.html'),
 ('moving-box-calculator', 2337, 'moving-boxes', 'Moving Box Calculator', 'How many moving boxes of each size you need.', '../moving-box/tool.html'),
 ('shelf-spacing-calculator', 1890, 'shelf-spacing', 'Shelf Spacing Calculator', 'How far apart to put floating shelves.', 'src/shelf.html'),
 ('washer-dryer-space-calculator', 1295, 'washer-dryer-space', 'Washer and Dryer Space Calculator', 'Whether a washer and dryer fit, with clearances.', 'src/washer.html'),
]
H = json.load(open('heights.json')) if os.path.exists('heights.json') else {}

PAGE_CSS = """<style>
body.dsh-embed{background:#fff!important}
body.dsh-embed .site-header,body.dsh-embed .site-footer,body.dsh-embed .entry-header,body.dsh-embed .entry-footer,body.dsh-embed .comments-area,body.dsh-embed #kt-scroll-up,body.dsh-embed .kadence-scroll-up,body.dsh-embed .post-navigation{display:none!important}
body.dsh-embed .content-container,body.dsh-embed .site-container,body.dsh-embed .content-area,body.dsh-embed .content-wrap,body.dsh-embed .entry-content-wrap,body.dsh-embed .site-main,body.dsh-embed article.entry{margin:0!important;padding:0!important;max-width:none!important;box-shadow:none!important;background:transparent!important;border:0!important}
body.dsh-embed .entry-content{margin:0!important}
body.dsh-embed .entry-content>*{max-width:none!important}
body.dsh-embed .dsh-calc{margin:0!important}
body.dsh-embed .dsh-calc .viz svg{max-height:340px}
.dsh-ef{display:flex;flex-wrap:wrap;justify-content:space-between;gap:6px 12px;align-items:center;font-size:13px;color:#6E645C;padding:8px 4px 2px;line-height:1.4}
.dsh-ef a{color:#C85A32;font-weight:700;text-decoration:none}
.dsh-ef a:hover{text-decoration:underline}
</style>"""

def snippet(t):
    main, pid, es, title, line, f = t
    h = H.get(es, 760)
    return ('<iframe class="dsh-embed" src="%sembed-calculators/%s/" title="%s" width="100%%" height="%d" style="border:0;width:100%%;max-width:760px;display:block" loading="lazy"></iframe>\n'
            '<p style="font-size:13px;margin:6px 0 0"><a href="%s%s/">%s</a> by Daily Space Hacks</p>\n' + HOST) % (S, es, title, h, S, main, title)

RESIZE = "<script>(function(){var w=document.getElementById('dsh-ew'),last=0;function s(){if(!w)return;var h=Math.ceil(w.getBoundingClientRect().height)+4;if(h!==last){last=h;try{parent.postMessage({dshEmbed:1,h:h},'*')}catch(e){}}}if(window.ResizeObserver){new ResizeObserver(s).observe(w)}window.addEventListener('load',s);setInterval(s,1000);s()})();</script>"
HOST = "<script>window.addEventListener('message',function(e){if(e.origin!=='https://dailyspacehacks.com'||!e.data||!e.data.dshEmbed)return;document.querySelectorAll('iframe.dsh-embed').forEach(function(f){if(f.contentWindow===e.source)f.style.height=e.data.h+'px'})});</script>"

def embed_page(t):
    main, pid, es, title, line, f = t
    tool = open(f).read().strip()
    foot = ('<div class="dsh-ef"><span>Free tool by <a href="%s?utm_source=embed&amp;utm_medium=referral" target="_blank" rel="noopener">Daily Space Hacks</a></span>'
            '<a href="%s%s/?utm_source=embed&amp;utm_medium=referral" target="_blank" rel="noopener">%s &rarr;</a></div>') % (S, S, main, 'Full guide and free PDF' if 'checklist' in main else 'Full guide and charts')
    return '<!-- wp:html -->\n' + PAGE_CSS + '\n<div id="dsh-ew">\n' + tool + '\n' + foot + '\n</div>\n' + RESIZE + '\n<!-- /wp:html -->'

COPY = "var c=this.parentNode.parentNode.querySelector('code'),b=this,d=function(){b.textContent='Copied';b.classList.add('ok');setTimeout(function(){b.textContent='Copy code';b.classList.remove('ok')},2200)};if(navigator.clipboard){navigator.clipboard.writeText(c.textContent).then(d)}else{var r=document.createRange();r.selectNodeContents(c);var w=getSelection();w.removeAllRanges();w.addRange(r);document.execCommand('copy');d()}"

def button(t, hub=False):
    main, pid, es, title, line, f = t
    nn = 'checklist' if 'checklist' in main else 'calculator'
    code = html.escape(snippet(t), quote=False)
    extra = '' if hub else '<a class="eal" href="%sembed-calculators/">All free calculators to embed</a>' % S
    return ('<div class="dsh-emb"><details><summary><span class="eic" aria-hidden="true">&lt;/&gt;</span>'
            '<span class="etx"><b>Embed this '+nn+'</b><small>Free for your blog or website</small></span><span class="ech" aria-hidden="true"></span></summary>'
            '<div class="ebd"><p>Copy the code and paste it into an HTML block on your site. It is free to use; please keep the credit link under the '+nn+'.</p>'
            '<pre><code>%s</code></pre>'
            '<div class="eac"><button type="button" class="ecp" onclick="%s">Copy code</button>'
            '<a class="epv" href="%sembed-calculators/%s/" target="_blank" rel="noopener nofollow">Preview</a>%s</div></div></details></div>') % (code, COPY, S, es, extra)

os.makedirs('out', exist_ok=True)
for t in T:
    es = t[2]
    open('out/page-%s.html' % es, 'w').write(embed_page(t))
    open('out/btn-%s.html' % es, 'w').write('<!-- wp:html -->\n' + button(t) + '\n<!-- /wp:html -->')
    open('out/hubbtn-%s.html' % es, 'w').write(button(t, True))
json.dump([t[:5] for t in T], open('out/tools.json', 'w'), indent=0)
print('ok', len(T))

# hub page /embed/
def p(x): return '<!-- wp:paragraph -->\n<p>%s</p>\n<!-- /wp:paragraph -->' % x
def h2(x): return '<!-- wp:heading -->\n<h2 class="wp-block-heading">%s</h2>\n<!-- /wp:heading -->' % x
def h3(x): return '<!-- wp:heading {"level":3} -->\n<h3 class="wp-block-heading">%s</h3>\n<!-- /wp:heading -->' % x
hub = [p('Run a home, interiors, moving or DIY blog? You can add any of our free home calculators to your own website. Each one works inside your page, in inches or centimeters, and gives your readers an instant answer without leaving your site.'),
 p('The calculators are free to use on blogs and websites. All we ask is that you keep the small credit link under the calculator, which is already part of the code.'),
 h2('How to Add a Calculator to Your Site'),
 '<!-- wp:list {"ordered":true} -->\n<ol class="wp-block-list"><!-- wp:list-item -->\n<li>Open <strong>Embed this calculator</strong> under the tool you want and press <strong>Copy code</strong>.</li>\n<!-- /wp:list-item -->\n<!-- wp:list-item -->\n<li>In WordPress, add a <strong>Custom HTML</strong> block where you want the calculator. On other platforms, use the HTML or embed option.</li>\n<!-- /wp:list-item -->\n<!-- wp:list-item -->\n<li>Paste the code and publish. The calculator adapts to the width of your page.</li>\n<!-- /wp:list-item --></ol>\n<!-- /wp:list -->',
 h2('Free Calculators You Can Embed')]
for t in T:
    hub.append(h3(t[3]))
    hub.append(p('%s <a href="%s%s/">Try the %s</a>.' % (t[4], S, t[0], t[3].replace('TV','TV').lower().replace('tv ','TV ').replace('christmas','Christmas'))))
    hub.append('<!-- wp:html -->\n' + button(t, True) + '\n<!-- /wp:html -->')
hub += [h2('Terms of Use'),
 p('You may embed the calculators on any website that is legal and family-friendly. Please do not remove or hide the credit link, change the results or present the tool as your own. The results are planning estimates; readers should always check measurements and follow product instructions. We may update the calculators at any time, and embedded versions update automatically.'),
 p('Questions or a calculator you would like us to build? <a href="%scontact/">Contact us</a>.' % S)]
open('out/hub.html','w').write('\n\n'.join(hub))
print('hub', len('\n\n'.join(hub)))
