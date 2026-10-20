import urllib.request,os,json
H={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
C=[("bath","gBH886ZlZQ8","1790926154404-b4755d4affaa"),("bath","MJwXQ6YKt74","1790926153591-bef8549eea66"),("bath","fpkl3E_NUjI","1790926155299-007c6f17c1d1"),
("bath","olIn1pY5uWs","1791140841982-8d34b95ddea5"),("bath","ylz9ErZovyI","1790926154787-c7cd631e342c"),("store","jt7SEU8Yin4","1791714762207-09d9720186ab"),
("store","uzj-dkm0JJs","1791002598903-834d7c1be8d6"),("store","G3I9Jjx2mQI","1791986139555-6bf5aa4a2e88"),("store","WhcksC0iaUA","1790926153560-9984cf61d308"),
("store","5JETkmRSH1I","1791739915508-0ce17fd8017e"),("xmas","-9dKh4rOtyA","1792036727825-8cb15cda7f6b"),("xmas","QOIJPJSfL2g","1792477014335-6edd356d028e"),
("xmas","rVXYfmDWRvU","1792287213947-0ef504a6b262"),("xmas","HDAsstipHcM","1792287213921-3288323c0708")]
os.makedirs("scout/out/prev",exist_ok=True)
for g,pid,ph in C:
    u=f"https://images.unsplash.com/photo-{ph}?fm=jpg&q=70&w=600"
    try:
        open(f"scout/out/prev/{g}_{pid}.jpg","wb").write(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30).read())
    except Exception as e: print(pid,e)
