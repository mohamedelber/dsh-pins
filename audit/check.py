import re,os,json,html
from bs4 import BeautifulSoup
urls=[l.strip() for l in open('fetch/audit-2.txt') if l.strip()]
valid=set(u.rstrip('/') for u in urls)
rows=[];issues=[]
def norm(h):
    h=h.split('#')[0].split('?')[0]
    return h.rstrip('/')
for u in urls:
    f='fetch/out/'+os.path.basename(u.rstrip('/')); s=open(f,encoding='utf-8',errors='ignore').read()
    soup=BeautifulSoup(s,'lxml')
    t=(soup.title.string or '').strip() if soup.title else ''
    md=soup.find('meta',attrs={'name':'description'}); md=md['content'] if md and md.has_attr('content') else ''
    rob=soup.find('meta',attrs={'name':'robots'}); rob=rob['content'] if rob and rob.has_attr('content') else ''
    can=soup.find('link',rel='canonical'); can=can['href'] if can else ''
    main=soup.find('article') or soup.find('main') or soup.body
    for x in main.find_all(['script','style','svg','nav','footer']): x.decompose()
    txt=main.get_text(' ',strip=True); wc=len(txt.split())
    h1=len(soup.find_all('h1'))
    imgs=main.find_all('img'); noalt=[i.get('src','')[-60:] for i in imgs if not (i.get('alt') or '').strip()]
    links=[a.get('href','') for a in (soup.find('article') or soup.body).find_all('a',href=True)]
    broken=[]
    for h in links:
        if h.startswith('https://dailyspacehacks.com/') or h.startswith('/'):
            n=norm(h if h.startswith('http') else 'https://dailyspacehacks.com'+h)
            if '/wp-content/' in n or '/category/' in n or '/author/' in n or n in ('https://dailyspacehacks.com',) : continue
            if n not in valid: broken.append(n)
    intl=len([h for h in links if 'dailyspacehacks.com' in h])
    ext=len([h for h in links if h.startswith('http') and 'dailyspacehacks.com' not in h and 'pinterest.com' not in h])
    rows.append(dict(url=u,title=t,tlen=len(t),desc_len=len(md),robots=rob,canon_ok=(norm(can)==norm(u)),words=wc,h1=h1,imgs=len(imgs),noalt=len(noalt),broken=sorted(set(broken)),internal=intl,external=ext))
json.dump(rows,open('audit/rows.json','w'),indent=1)
print('pages',len(rows))
for r in sorted(rows,key=lambda r:r['words']):
    flag=[]
    if r['words']<600: flag.append(f"THIN {r['words']}w")
    if not (120<=r['desc_len']<=165): flag.append(f"desc {r['desc_len']}")
    if r['tlen']>65: flag.append(f"title {r['tlen']}")
    if 'noindex' in r['robots']: flag.append('NOINDEX')
    if not r['canon_ok']: flag.append('canon')
    if r['h1']!=1: flag.append(f"h1={r['h1']}")
    if r['noalt']: flag.append(f"noalt {r['noalt']}")
    if r['broken']: flag.append('BROKEN '+','.join(b.replace('https://dailyspacehacks.com/','') for b in r['broken']))
    if flag: print(r['url'].replace('https://dailyspacehacks.com/','/'),'|',r['words'],'|','; '.join(flag))
ts={}
for r in rows: ts.setdefault(r['title'],[]).append(r['url'])
print('dup titles',[v for v in ts.values() if len(v)>1])
print('total words',sum(r['words'] for r in rows))
