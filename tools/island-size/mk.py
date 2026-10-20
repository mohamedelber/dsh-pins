s=open('style.txt').read();b=open('body.html').read()
t='<div id="dsh-is" class="dsh-calc">\n'+s+'\n'+b+'</div>\n'
import re
js=t[t.find('<script>'):]
bad=[m.group(0) for m in re.finditer(r'<[a-zA-Z]',js) if not re.match(r'<(svg|rect|line|text|li|/)',js[m.start():m.start()+5])]
assert '&' not in js and ']]>' not in js, 'amp'
print('suspicious <letter:',bad[:10])
open('tool.html','w').write(t)
