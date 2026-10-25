import re
S="https://dailyspacehacks.com/"
U=S+"wp-content/uploads/2026/10/"
out=[]
def add(x): out.append(x)
def a(slug,t): return f'<a href="{S}{slug}/">{t}</a>'
def ext(u,t): return f'<a href="{u}" target="_blank" rel="noopener">{t}</a>'
def p(t): add(f'<!-- wp:paragraph -->\n<p>{t}</p>\n<!-- /wp:paragraph -->')
def h2(t): add(f'<!-- wp:heading -->\n<h2 class="wp-block-heading">{t}</h2>\n<!-- /wp:heading -->')
def h3(t): add(f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->')
def img(n):
    i,f,al=IMG[n]
    add(f'<!-- wp:image {{"id":{i},"sizeSlug":"full","linkDestination":"none"}} -->\n<figure class="wp-block-image size-full"><img src="{U}{f}" alt="{al}" class="wp-image-{i}"/></figure>\n<!-- /wp:image -->')
def lst(items,ordered=False):
    tag='ol' if ordered else 'ul'
    attr=' {"ordered":true}' if ordered else ''
    li='\n'.join(f'<!-- wp:list-item -->\n<li>{x}</li>\n<!-- /wp:list-item -->' for x in items)
    add(f'<!-- wp:list{attr} -->\n<{tag} class="wp-block-list">{li}</{tag}>\n<!-- /wp:list -->')
def table(head,rows):
    th=''.join(f'<th>{h}</th>' for h in head)
    tr=''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)
    add(f'<!-- wp:table -->\n<figure class="wp-block-table"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->')
def summary(items,line):
    li='\n'.join(f'<!-- wp:list-item -->\n<li>{x}</li>\n<!-- /wp:list-item -->' for x in items)
    add('<!-- wp:group {"className":"dsh-summary","style":{"color":{"background":"#EEF3EC"},"spacing":{"padding":{"top":"20px","bottom":"20px","left":"24px","right":"24px"}},"border":{"radius":"12px","left":{"color":"#8FA689","width":"5px"}}},"layout":{"type":"constrained"}} -->\n<div class="wp-block-group dsh-summary has-background" style="border-radius:12px;border-left-color:#8FA689;border-left-width:5px;background-color:#EEF3EC;padding-top:20px;padding-right:24px;padding-bottom:20px;padding-left:24px"><!-- wp:paragraph -->\n<p><strong>Key Takeaways</strong></p>\n<!-- /wp:paragraph -->\n<!-- wp:list -->\n<ul class="wp-block-list">'+li+'</ul>\n<!-- /wp:list -->\n<!-- wp:paragraph -->\n<p>'+line+'</p>\n<!-- /wp:paragraph -->\n</div>\n<!-- /wp:group -->')
def toc(uid): add('<!-- wp:kadence/tableofcontents {"uniqueID":"_toc'+uid+'","allowedHeaders":[{"h1":false,"h2":true,"h3":true,"h4":false,"h5":false,"h6":false}],"enableToggle":true,"startClosed":true} /-->')
def diagram(svg,cap): add('<!-- wp:html -->\n<figure class="dsh-diagram">'+svg.replace('\n','')+'<figcaption>'+cap+'</figcaption></figure>\n<!-- /wp:html -->')
def ai_note(): add('<!-- wp:paragraph {"className":"dsh-ai-note","fontSize":"small"} -->\n<p class="dsh-ai-note has-small-font-size"><em>How this guide was made: researched and written with the help of AI tools, fact-checked against trusted sources and published by Mohamed Elber. Images are AI-generated illustrations. See our <a href="https://dailyspacehacks.com/editorial-policy/">Editorial Policy</a>.</em></p>\n<!-- /wp:paragraph -->')

