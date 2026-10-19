import json, sys, csv, glob, random
S = sys.argv[1]
D = '/root/polymarket-research-datalogs/'
O = json.load(open(f'{S}/cron2_out.json'))
ev = {}
for f in sorted(glob.glob(D + 'vigia_5m_barato/eventos_*.csv')):
    for e in csv.DictReader(open(f)): ev[e['event_id']] = e
for r in O:
    r['hueco'] = (r.get('gap_prev_q5_ms') or 0) > 60000 or (r.get('gap_prev_q15_ms') or 0) > 60000
    r['ej'] = r['acc215'] > 0
    e = ev[r['event_id']]
    def f(k):
        v = e.get(k); return None if v in (None, '', 'None') else float(v)
    for k in ('o_bid_sz', 'o_spread', 'c_spread', 'c_edad_ask_ms', 'o_cambios_1s', 'c_cambios_1s', 'c_trades_1s', 'o_trades_1s', 'c_cancel_1s', 'margen_neto', 'c_ask_sz', 'c_bid_sz'):
        r[k] = f(k)
    r['jump15'] = None if r.get('bid15_prev') is None else r['bid15_0'] - r['bid15_prev']
feats = ['jump15', 'o_bid_sz', 'o_spread', 'c_spread', 'c_edad_ask_ms', 'o_cambios_1s', 'c_cambios_1s', 'c_trades_1s', 'o_trades_1s', 'c_cancel_1s', 'margen_neto', 'c_ask_sz', 'c_bid_sz', 'ask0', 'bid15_0', 'resto', 'binR_R1000', 'binR_R250', 'edad_bid15_prev', 'n_bid15_chg_1000', 'cons_pre_n']
def auc(pos, neg):
    c = 0.0
    for a in pos:
        for b in neg: c += 1.0 if a > b else 0.5 if a == b else 0.0
    return c / (len(pos) * len(neg))
def maxdev(rows, lab):
    best = 0; bn = None
    for k in feats:
        pos = [r[k] for r in rows if lab(r) and r.get(k) is not None]; neg = [r[k] for r in rows if not lab(r) and r.get(k) is not None]
        if len(pos) < 3 or len(neg) < 3: continue
        a = auc(pos, neg)
        if abs(a - .5) > best: best = abs(a - .5); bn = k
    return best, bn
rng = random.Random(1)
for nom, rows, lab in (('gana | 53 sin huecos', [r for r in O if not r['hueco']], lambda r: r['gana']), ('gana | 23 ejecutables sin huecos', [r for r in O if not r['hueco'] and r['ej']], lambda r: r['gana']), ('noejecutable | 53', [r for r in O if not r['hueco']], lambda r: not r['ej'])):
    obs, bn = maxdev(rows, lab)
    ge = 0; n = 400
    labs = [lab(r) for r in rows]
    for _ in range(n):
        sh = labs[:]; rng.shuffle(sh)
        for r, s in zip(rows, sh): r['_s'] = s
        m, _ = maxdev(rows, lambda r: r['_s'])
        if m >= obs: ge += 1
    print(f'{nom}: max|AUC-0,5| observado {obs:.3f} ({bn}); p(max-estadístico, 21 rasgos) = {(ge+1)/(n+1):.3f}')
