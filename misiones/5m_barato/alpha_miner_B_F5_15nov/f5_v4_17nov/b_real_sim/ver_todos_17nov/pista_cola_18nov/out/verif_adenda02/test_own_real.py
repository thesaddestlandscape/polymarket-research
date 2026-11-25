"""ADENDA_02 punto 4: ejecuta VERBATIM el bloque on-chain de p1_dia.py (exclusion de wallet propia + marcado es_propio) con on-chain REAL de B 20-21 Oct (tx propias reales).
Tokens/comp de cola_vs_cruce/tokens.json (par YES/NO por market id). No hay dia con L2 libro5_ms Y tx propias EN BANDA: 13-Nov (Sonda B2/B3/B5) solo tiene 2 fills propios a p=0,01 (fuera de banda)."""
import json, collections, bisect, sys, numpy as np, pandas as pd
H = '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim/ver_todos_17nov/pista_cola_18nov/'
src = open(H + 'p1_dia.py').read()
a = src.index('# ---- on-chain del dia'); b = src.index('bidr = oc[oc.side == 0]')
blk = src[a:b].replace("f'/root/polymarket-research-datalogs/onchain_fills_{dd.date()}.csv.gz'", "f'/mnt/HC_Volume_106538179/keep_onchain_re_as_b/onchain_fills_{dd.date()}.csv.gz'")
tk = json.load(open('/root/polymarket-research-datalogs/cola_vs_cruce/tokens.json')); by = collections.defaultdict(dict)
for t, (act, mid, lado, e) in tk.items(): by[mid][lado] = t
comp = {}
for mid, d in by.items():
    if 'YES' in d and 'NO' in d: comp[d['YES']] = d['NO']; comp[d['NO']] = d['YES']
TK = set(comp); D = sys.argv[1]; d0 = pd.Timestamp(D)
import os; ns = dict(os=os, pd=pd, np=np, collections=collections, bisect=bisect, d0=d0, TK=TK, comp=comp, LO=0.10, HI=0.30 - 1e-9, EXC='0xe111180000d2663c0091e4f400237545b87b996b', OWN='0x659a40ff9920febc5a66836213040924343d297f')
exec(blk, ns)
oc, oc_own, own_tx, OWNI, OWNR, es = ns['oc'], ns['oc_own'], ns['own_tx'], ns['OWNI'], ns['OWNR'], ns['es_propio']
print('dia', D, 'OWNR', dict(OWNR), 'tx propias', len(own_tx))
print('PASS1 ninguna tx propia queda en oc:', not oc.tx.isin(own_tx).any(), '| filas excluidas en banda:', len(oc_own))
hit = miss = fa = 0; n = 0
for r in oc_own.itertuples():
    rx = r.ts_est * 1000 - 2331          # casado estimado (bloque - mediana 2,331 s)
    n += 1; hit += es(r.X, r.p, rx); fa += es(r.X, r.p, rx + 60000)
print('PASS2 es_propio(casado estimado)=True en %d/%d ; falso-control (+60 s) True en %d/%d' % (hit, n, fa, n))
# control negativo: filas NO propias en banda con el mismo nivel no deben marcarse fuera de ventana
sample = oc.sample(min(2000, len(oc)), random_state=1); print('PASS3 tasa es_propio en filas ajenas (rx=bloque-2331, nivel ajeno): %.4f (esperada ~ coincidencia de nivel+ventana)' % np.mean([es(r.X, r.p, r.ts_est * 1000 - 2331) for r in sample.itertuples()]))
