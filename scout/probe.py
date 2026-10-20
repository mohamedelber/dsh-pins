import urllib.request,os
H={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36","Accept-Language":"en-US,en;q=0.9"}
os.makedirs("scout/out",exist_ok=True)
for name,u in [("search","https://unsplash.com/s/photos/bathroom-storage?order_by=latest"),("photo","https://unsplash.com/photos/hairbrushes-and-clips-in-storage-basket-jt7SEU8Yin4"),("pexels","https://www.pexels.com/search/bathroom%20storage/")]:
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30).read()
        open(f"scout/out/{name}.html","wb").write(r); print(name,len(r))
    except Exception as e:
        open(f"scout/out/{name}.err","w").write(repr(e))
