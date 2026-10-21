import urllib.request,os,re
H={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=40).read().decode('utf-8','ignore')
os.makedirs("scout/site",exist_ok=True)
urls=[]
for sm in ("post-sitemap.xml","page-sitemap.xml"):
    try: urls+=re.findall(r"<loc>(.*?)</loc>",get("https://dailyspacehacks.com/"+sm))
    except Exception as e: open("scout/site/_err.txt","a").write(sm+" "+repr(e)+"\n")
open("scout/site/_urls.txt","w").write("\n".join(urls))
for u in urls:
    slug=u.rstrip('/').split('/')[-1] or 'home'
    if 'dailyspacehacks.com/'==u.split('//')[1][-20:]: slug='home'
    try: open(f"scout/site/{slug}.html","w").write(get(u))
    except Exception as e: open("scout/site/_err.txt","a").write(u+" "+repr(e)+"\n")
