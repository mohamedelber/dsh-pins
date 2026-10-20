import urllib.request,os
H={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
os.makedirs("scout/out",exist_ok=True)
u="https://images.unsplash.com/photo-1788346905555-f1066e4ac431?fm=jpg&q=70&w=600"
try:
    r=urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30).read()
    open("scout/out/cdn-test.jpg","wb").write(r); print(len(r))
except Exception as e:
    open("scout/out/cdn.err","w").write(repr(e))
