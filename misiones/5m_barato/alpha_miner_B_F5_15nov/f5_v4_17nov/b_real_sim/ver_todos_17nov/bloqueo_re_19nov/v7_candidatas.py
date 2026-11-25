"""v7_candidatas.py -- PREREG_V7 (53e9febb) paso 1: txs tomadoras PUBLICAS en el par de tokens de ordenes reales de B vivas (20-23 Oct).
Solo lectura. Prefiltro fisico: la tx toca liquidez con precio-equivalente-bid propio <= L+0,03 (si el limite cruza L y queda resto, consumio todo lo >= L).
Salida out/v7_cand.csv (tx,ts,oid,L,fill,dir,min_eq,n_tx_par) + out/v7_pares.json."""
import gzip, json, collections, csv
import pandas as pd
EXCH = '0xe111180000d2663c0091e4f400237545b87b996b'
O = pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv',
                usecols=['oid', 'tok', 'precio', 't_ini', 't_fin', 'dia', 'fill'], dtype={'tok': str})
O = O.dropna(subset=['t_ini', 't_fin'])
BT = set(O.tok)
def rows(fn):
    with gzip.open(fn, 'rt', errors='replace') as f:
        f.readline()
        for ln in f:
            c = ln.rstrip('\n').split(',')
            if len(c) < 13 or c[0] != 'F': continue
            yield c
DIAS = sorted(O.dia.unique()); comp = {}; out = []; ntot = collections.Counter()
for dia in DIAS:
    fn = f'/mnt/HC_Volume_106538179/keep_onchain_re_as_b/onchain_fills_{dia}.csv.gz'
    votes = collections.Counter(); cur = None; buf = []
    def flush_votes(buf):
        tk_ = {(c[9], c[8]) for c in buf}
        for t, s in tk_:
            if t in BT:
                for t2, s2 in tk_:
                    if t2 != t and s2 == s: votes[(t, t2)] += 1
    for c in rows(fn):
        if c[3] != cur:
            if buf: flush_votes(buf)
            cur = c[3]; buf = []
        buf.append(c)
    if buf: flush_votes(buf)
    for t in BT:
        if t in comp: continue
        cand = [(n, t2) for (a, t2), n in votes.items() if a == t]
        if cand: comp[t] = max(cand)[1]
    Od = O[O.dia == dia]; by = collections.defaultdict(list)
    for r in Od.itertuples(): by[r.tok].append((r.t_ini, r.t_fin, r.oid, r.precio, r.fill))
    pair_of = {}
    for t in by:
        pair_of[t] = t
        if t in comp: pair_of[comp[t]] = t
    def proc(buf):
        tkr = [c for c in buf if c[7] == EXCH]
        for tr in tkr:
            own = pair_of.get(tr[9])
            if own is None: continue
            # direccion: vende propio o compra comp (presiona la puja propia hacia abajo)
            if not ((tr[9] == own and tr[8] == '1') or (tr[9] != own and tr[8] == '0')): continue
            ts = float(tr[2]); eqs = []
            for c in buf:
                if c[7] == EXCH: continue
                try: ma = float(c[10]); ta = float(c[11])
                except ValueError: continue
                if ma <= 0 or ta <= 0: continue
                p = ma / ta if c[8] == '0' else ta / ma
                if c[9] == own: eqs.append(p)
                elif pair_of.get(c[9]) == own: eqs.append(1 - p)
            if not eqs: continue
            me = min(eqs); ntot[dia] += 1
            for (a, b, oid, L, fl) in by[own]:
                if a + 1 <= ts <= b + 3 and me <= L + 0.03 + 1e-9:
                    out.append((tr[3], ts, oid, L, fl, 'vende_propio' if tr[9] == own else 'compra_comp', round(me, 4), tr[5]))
    cur = None; buf = []
    for c in rows(fn):
        if c[3] != cur:
            if buf: proc(buf)
            cur = c[3]; buf = []
        buf.append(c)
    if buf: proc(buf)
    print(dia, 'comp', sum(t in comp for t in by), '/', len(by), '| tomadoras en direccion', ntot[dia], '| candidatas acum', len(out), flush=True)
with open('out/v7_cand.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['tx', 'ts', 'oid', 'L', 'fill', 'dir', 'min_eq', 'tk_hash']); w.writerows(out)
json.dump(comp, open('out/v7_pares.json', 'w'))
print('FIN candidatas', len(out), 'txs unicas', len({x[0] for x in out}), flush=True)
