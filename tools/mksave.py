import sys,urllib.parse as u
def mk(slug,pinfile,wpfile,desc,alt,line,out,title='Save the cheat sheet'):
    url='https://dailyspacehacks.com/%s/'%slug
    med='https://cdn.jsdelivr.net/gh/mohamedelber/dsh-pins@main/pins-N/%s'%pinfile
    pin='https://www.pinterest.com/pin/create/button/?url=%s&media=%s&description=%s'%(u.quote(url,safe=''),u.quote(med,safe=''),u.quote(desc,safe=''))
    h=f'''<!-- wp:html -->
<div class="dsh-save" style="display:flex;flex-wrap:wrap;align-items:center;gap:24px;background:#F7F1E9;border:1px solid #E6DCCF;border-radius:16px;padding:24px;margin:2em 0;"><a href="{pin}" target="_blank" rel="noopener" style="flex:0 0 200px;max-width:200px;margin:0 auto;"><img src="https://dailyspacehacks.com/wp-content/uploads/2026/10/{wpfile}" alt="{alt}" width="200" data-pin-media="{med}" style="width:200px;height:auto;border-radius:10px;display:block;"></a><div style="flex:1 1 260px;"><p style="font-weight:700;font-size:1.25em;margin:0 0 .4em;">{title}</p><p style="margin:0 0 1em;">{line}</p><a href="{pin}" target="_blank" rel="noopener" style="display:inline-block;background:#E60023;color:#fff;font-weight:700;text-decoration:none;padding:12px 22px;border-radius:999px;white-space:nowrap;line-height:1.2;">Save to Pinterest</a></div></div>
<!-- /wp:html -->'''
    open(out,'w').write(h)
