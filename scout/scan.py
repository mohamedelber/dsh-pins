import json, urllib.request, urllib.parse, os, time
Q=["under sink organization","bathroom cabinet organization","bathroom storage","bathroom shelves","organized pantry","pantry shelves","kitchen organization","toy storage","lego","kids playroom storage","closet organization","laundry room","entryway","christmas table","christmas decorations storage","over toilet shelf"]
SINCE="2026-10-01"
H={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36","Accept":"application/json"}
os.makedirs("scout/out",exist_ok=True)
res={}
LOG=open("scout/out/log.txt","w")
def log(*a): print(*a); LOG.write(" ".join(map(str,a))+"\n"); LOG.flush()
for q in Q:
    for page in (1,2,3):
        u="https://unsplash.com/napi/search/photos?"+urllib.parse.urlencode({"query":q,"order_by":"latest","per_page":30,"page":page})
        try:
            d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=30))
        except Exception as e:
            log("fail",q,page,repr(e)); break
        rs=d.get("results",[])
        log(q,page,"n=",len(rs),"total=",d.get("total"),[ (p.get("created_at") or "")[:10]+("P" if (p.get("premium") or p.get("plus")) else "") for p in rs[:8]])
        old=0
        for p in rs:
            c=(p.get("created_at") or "")[:10]
            if c<SINCE: old+=1; continue
            if p.get("premium") or p.get("plus"): continue
            pid=p["id"]
            if pid in res: res[pid]["queries"].append(q); continue
            res[pid]={"id":pid,"created":c,"w":p.get("width"),"h":p.get("height"),"alt":p.get("alt_description") or p.get("description"),
                "user":(p.get("user") or {}).get("name"),"page":(p.get("links") or {}).get("html"),"raw":(p.get("urls") or {}).get("raw"),
                "likes":p.get("likes"),"queries":[q]}
        if old==len(rs) or not rs: break
        time.sleep(1)
for pid,r in res.items():
    try:
        urllib.request.urlretrieve(r["raw"]+"&w=400&q=70&fm=jpg", f"scout/out/{pid}.jpg")
    except Exception as e: print("dl fail",pid,e)
json.dump(sorted(res.values(),key=lambda r:r["created"],reverse=True),open("scout/out/index.json","w"),indent=1)
log(len(res),"photos")
