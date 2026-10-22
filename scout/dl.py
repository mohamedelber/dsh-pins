# download free Unsplash photos listed in scout/urls.txt via the images CDN
import os,re,urllib.request
os.makedirs('scout/real',exist_ok=True)
for u in open('scout/urls.txt'):
    u=u.strip()
    m=re.search(r'(photo-\d{13}-[0-9a-f]+)',u)
    if not m: continue
    p='scout/real/'+m.group(1)+'.jpg'
    if os.path.exists(p): continue
    try:
        r=urllib.request.urlopen(urllib.request.Request('https://images.unsplash.com/'+m.group(1)+'?w=1600&q=85&fm=jpg',headers={'User-Agent':'Mozilla/5.0'}),timeout=40)
        open(p,'wb').write(r.read()); print('ok',p)
    except Exception as e: print('fail',u,e)
