import json, glob, time, urllib.request, urllib.parse
SP='/tmp/claude-0/-root-polymarket-research/cbc315b0-0ee3-4fbb-b193-997ca0900993/scratchpad/act/'
sl=set()
for f in glob.glob(SP+'act_*.json'):
    for x in json.load(open(f)):
        if x['type']=='TRADE' and x.get('slug'): sl.add(x['slug'])
sl=sorted(sl); res={}
for i in range(0,len(sl),40):
    q=urllib.parse.urlencode([('closed','true'),('limit','100')]+[('slug',s) for s in sl[i:i+40]])
    try: d=json.load(urllib.request.urlopen(urllib.request.Request('https://gamma-api.polymarket.com/markets?'+q,headers={'User-Agent':'research-readonly'}),timeout=30))
    except Exception as e: print('err',i,e); continue
    for x in d:
        op=json.loads(x.get('outcomePrices') or '[]')
        res[x['slug']]=op
    time.sleep(0.3)
json.dump(res,open(SP+'resol.json','w')); print('slugs',len(sl),'resueltos',len(res),'con 1/0',sum(1 for v in res.values() if v in (['1','0'],['0','1'])))
