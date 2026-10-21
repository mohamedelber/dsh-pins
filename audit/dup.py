import re,glob,os,json,collections
from bs4 import BeautifulSoup
docs={}
for f in sorted(glob.glob('scout/site/*.html')):
    slug=os.path.basename(f)[:-5]
    s=open(f,encoding='utf-8',errors='ignore').read()
    so=BeautifulSoup(s,'lxml')
    c=so.select_one('.entry-content') or so.find('article')
    if not c: continue
    for x in c.find_all(['script','style','svg','figure','noscript']): x.decompose()
    for x in c.select('.dsh-calc,.dsh-emb,.dsh-save,.dsh-ai-note'): x.decompose()
    blocks=[b.get_text(' ',strip=True) for b in c.find_all(['p','li','h2','h3','td','th'])]
    heads=[h.get_text(' ',strip=True) for h in c.find_all(['h2','h3'])]
    docs[slug]=dict(blocks=blocks,heads=heads,text=' '.join(blocks),html=str(c))
print(len(docs),'pages with content')
# sentences repeated across pages
sent_docs=collections.defaultdict(set)
for slug,d in docs.items():
    for b in d['blocks']:
        for s in re.split(r'(?<=[.!?])\s+',b):
            n=re.sub(r'\s+',' ',s.lower()).strip(' .')
            if len(n.split())>=7: sent_docs[n].add(slug)
rep=sorted([(len(v),k,sorted(v)) for k,v in sent_docs.items() if len(v)>=3],reverse=True)
print('\n== sentences in 3+ pages:',len(rep))
for n,k,v in rep[:40]: print(n,'|',k[:150],'|',', '.join(v[:6]))
# template features
feat=collections.Counter()
for slug,d in docs.items():
    h=d['html']
    if 'Key Takeaways' in h: feat['Key Takeaways box']+=1
    if 'Quick Pick' in h: feat['Quick Pick']+=1
    if re.search(r'Time:</strong>',h): feat['Time/Cost/Difficulty line']+=1
    if any(x.startswith('Final Thoughts') for x in d['heads']): feat['Final Thoughts']+=1
    if any(re.search(r'FAQ|Frequently',x) for x in d['heads']): feat['FAQ']+=1
    if any(re.search(r'Mistakes',x) for x in d['heads']): feat['Mistakes h2']+=1
    if any(re.search(r'in \d+ Steps',x) for x in d['heads']): feat['N Steps h2']+=1
    if 'Quick answer:' in h: feat['Quick answer']+=1
print('\n== template features (of',len(docs),'):',dict(feat))
# repeated headings
hc=collections.Counter(h.lower() for d in docs.values() for h in set(d['heads']))
print('\n== headings in 3+ pages:',[(k,v) for k,v in hc.most_common(25) if v>=3])
# similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
sl=list(docs); X=TfidfVectorizer(stop_words='english',min_df=1,ngram_range=(1,2),sublinear_tf=True).fit_transform([docs[s]['text'] for s in sl])
S=cosine_similarity(X); pairs=[]
for i in range(len(sl)):
    for j in range(i+1,len(sl)):
        if S[i,j]>=0.35: pairs.append((round(S[i,j],2),sl[i],sl[j]))
print('\n== similar page pairs (cos>=0.35):')
for p in sorted(pairs,reverse=True)[:30]: print(p)
json.dump(dict(rep=[(n,k,v) for n,k,v in rep],pairs=sorted(pairs,reverse=True),feat=feat),open('audit/dup.json','w'),indent=1)
