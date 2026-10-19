import json, sys, collections, glob
S = sys.argv[1]
EXCH = '0xe111180000d2663c0091e4f400237545b87b996b'
tot_ws = tot_oc = 0
rows = []
for f in sorted(glob.glob(f'{S}/toks_*.json')):
    dia = f[-15:-5]
    toks = json.load(open(f))
    k5s = {v[0] for v in toks.values() if v[0]}
    ws = collections.Counter()
    for ln in open(f'{S}/qt5_{dia}.txt'):
        if ln.startswith('t,'):
            c = ln.split(',')
            if c[2] in k5s: ws[c[2]] += 1
    oc = collections.defaultdict(set)
    for ln in open(f'{S}/oc_{dia}.txt'):
        c = ln.split(',')
        if c[0] == 'F' and c[7] == EXCH and c[9] in k5s: oc[c[9]].add(c[3] + c[4])
    for k in k5s:
        rows.append((dia, k[:8], ws[k], len(oc[k])))
        tot_ws += ws[k]; tot_oc += len(oc[k])
print('WS trades (t rows, ambos lados) vs on-chain taker-fill rows (cualquier lado/ tomador=exchange):', tot_ws, tot_oc)
for r in rows[:40]: print(r)
# ratio por token y marcado de eventos
O = json.load(open(f'{S}/cron2_out.json'))
ratio = {}
for dia, k, w, o in rows: ratio[(dia, k)] = (w, o)
bad = 0; out = {}
for r in O:
    toks = json.load(open(f'{S}/toks_{r["dia"]}.json'))
    k = toks[r['event_id']][0][:8]
    w, o = ratio[(r['dia'], k)]
    ok = (o == 0) or (w / o >= 0.95)
    out[r['event_id']] = ok
    if not ok: bad += 1; print('WS incompleto', r['event_id'], w, o, r['cls215'][:1])
json.dump(out, open(f'{S}/ws_ok.json', 'w'))
print('eventos con feed de trades incompleto:', bad, '/', len(O))
