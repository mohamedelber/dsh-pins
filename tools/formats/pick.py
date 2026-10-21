import csv,sys,collections
allowed=sys.argv[1:] or ['F1','F2','F3','F4','F5']
rows=[r for r in csv.DictReader(open(__file__.replace('pick.py','log.csv'))) if r['format']!='LEGACY']
last=rows[-1]['format'] if rows else None
recent=collections.Counter(r['format'] for r in rows[-5:])
cands=[f for f in allowed if f!=last] or allowed
best=sorted(cands,key=lambda f:(recent[f],allowed.index(f)))
print('last:',last,'| recent:',dict(recent),'| choose:',best[0],'| order:',best)
