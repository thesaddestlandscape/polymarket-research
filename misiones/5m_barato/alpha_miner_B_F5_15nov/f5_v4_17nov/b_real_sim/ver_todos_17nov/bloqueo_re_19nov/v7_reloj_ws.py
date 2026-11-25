"""v7_reloj_ws.py -- ADENDA A3: reloj fino (rx de la T del WS) para candidatas V7 con mk (ETH/SOL/XRP 20-22 Oct). Solo lectura."""
import sys, os, gzip, csv, collections
sys.path.insert(0, '../solo_observable_19nov'); import so1_traza as S
C = list(csv.DictReader(open('out/v7_cand.csv')))
import pandas as pd
O = pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv', usecols=['oid', 'tok'], dtype={'tok': str}).set_index('oid').tok.to_dict()
by = collections.defaultdict(list)
for r in C:
    m = S.TOKM.get(str(O.get(r['oid'])))
    if m: by[S.MK + f'{m[0]}_{m[1]}.gz'].append((r, 'Y' if m[2] == 'YES' else 'N'))
out = []; st = collections.Counter(sin_mk=len(C) - sum(len(v) for v in by.values()))
for fn, lst in by.items():
    if not os.path.exists(fn): st['sin_fichero'] += len(lst); continue
    T = []
    with gzip.open(fn, 'rt', errors='replace') as f:
        for ln in f:
            c = ln.rstrip('\n').split(',')
            if len(c) >= 6 and c[1] == 'T':
                try: T.append((int(c[2]) / 1000, c[0], float(c[4])))
                except ValueError: pass
    for r, own in lst:
        ts = float(r['ts']); me = float(r['min_eq'])
        mt = [t for t, sd, p in T if ts - 3.1 <= t <= ts - 1.4 and ((sd == own and abs(p - me) <= 0.005) or (sd != own and abs(p - (1 - me)) <= 0.005))]
        if not mt: st['sin_T'] += 1; continue
        if max(mt) - min(mt) > 0.3: st['ambigua'] += 1; continue
        st['ok'] += 1; out.append(dict(r, ts_ws=min(mt)))
pd.DataFrame(out).to_csv('out/v7_cand_ws.csv', index=False); print(dict(st))
