import helpers as h, json, os
IMGJ='img.json'
h.IMG={k:tuple(v) for k,v in (json.load(open(IMGJ)).items() if os.path.exists(IMGJ) else [])}
def grab(fn):
    h.out.clear(); fn(); r='\n\n'.join(h.out); h.out.clear(); return r
OPS=[]
def after(pid,search,fn): OPS.append([pid,search,search+'\n\n'+grab(fn)])
def before(pid,search,fn): OPS.append([pid,search,grab(fn)+'\n\n'+search])
def rep(pid,search,new): OPS.append([pid,search,new])
def save(name):
    json.dump(OPS,open(name,'w'),indent=1,ensure_ascii=False)
    for pid,s,r in OPS: assert '&&' not in r
    print(name,len(OPS),'ops, +%d bytes'%sum(len(r.encode())-len(s.encode()) for _,s,r in OPS))
