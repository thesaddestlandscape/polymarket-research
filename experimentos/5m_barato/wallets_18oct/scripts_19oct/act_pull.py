import json, sys, time, urllib.request, datetime as dt
W="0xc387c2a40d389f17b723b6bba9b18b7dbd2de4f4"
OUT='/tmp/claude-0/-root-polymarket-research/cbc315b0-0ee3-4fbb-b193-997ca0900993/scratchpad/act/'
for d in sys.argv[1:]:
    s=int(dt.datetime.fromisoformat(d+'T00:00:00+00:00').timestamp()); e=s+86400
    allr=[]; off=0
    while True:
        u=f"https://data-api.polymarket.com/activity?user={W}&limit=500&offset={off}&start={s}&end={e}"
        try: r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'research-readonly'}),timeout=30))
        except Exception as ex: print(d,'error',off,ex); break
        if not isinstance(r,list) or not r: break
        allr+=r; off+=500; time.sleep(0.4)
        if off>20000: print('tope offset'); break
    json.dump(allr,open(OUT+f'act_{d}.json','w')); print(d,len(allr),flush=True)
