#!/usr/bin/env python3
"""cal_run.py -- PREREG_E1_CALIBRACION (sha 001c130d...). Corre e1q_sim (importado SIN modificar) sobre los mercados MEDIR donde B real hizo puja,
rejilla lat_can x alloc con settle=0, repost=1500 (codigo real de B). Salida datos/cal_sim.csv. Solo lectura de produccion."""
import os, sys, json, hashlib, bisect, glob, collections
os.environ['E1Q_FASE'] = 'MEDIR'
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_E1_CALIBRACION.md'), 'rb').read()).hexdigest().startswith('001c130d2e5a1d73')
CV = os.path.join(AQ, '../../cola_vs_cruce/scripts'); sys.path.insert(0, CV)
import numpy as np, pandas as pd
import e1q_sim as S
LAST = {}
_orig = S.vida_orden
def _w(lvl, NT, L, o, t_live, t_end, size, alloc='prop'):
    res = _orig(lvl, NT, L, o, t_live, t_end, size, alloc)
    if res: LAST['tl'] = t_live
    return res
S.vida_orden = _w
CV_D = os.path.join(CV, '..', 'datos')
T = pd.concat([pd.read_csv(os.path.join(CV_D, f'tok_2026-10-{d}.csv'), dtype={'mid': str}) for d in (20, 21, 22)]).drop_duplicates(['act', 'mid'])
slug2mid = {(r.act, int(r.fin)): r.mid for r in T.itertuples()}
# pujas reales de B (ledger)
LED = '/root/polymarket-research-datalogs/experimento_h47_B_ledger.jsonl'
pj = {}; tard = collections.Counter()
for l in open(LED):
    try: d = json.loads(l)
    except Exception: continue
    if not d.get('real'): continue
    if d.get('tipo') == 'puja_fin':
        coin, _, _, st = d['slug'].split('-'); m = slug2mid.get((coin.upper(), int(st) + 300))
        if m: pj[m] = dict(mid=m, act=coin.upper(), fin=int(st) + 300, real_lado='Y' if d['lado'] == 'YES' else 'N', rf_a=int(bool(d.get('rellenos'))),
                           n_ord=d.get('n_ordenes'), fin_puja=d.get('fin_puja'), slug=d['slug'])
    elif d.get('tipo') == 'relleno_tardio': tard[d['slug']] += 1
for v in pj.values(): v['rf_tardio'] = int(tard.get(v['slug'], 0) > 0)
R = pd.DataFrame(pj.values())
bc = pd.read_csv(os.path.join(CV_D, 'b_clase.csv'), dtype={'mid': str}).drop_duplicates(['tx', 'c'])
R['rf_chain'] = R.apply(lambda r: int(((bc.mid == r.mid) & (bc.lado == ('YES' if r.real_lado == 'Y' else 'NO'))).any()), axis=1)
R['rf_union'] = ((R.rf_a + R.rf_tardio + R.rf_chain) > 0).astype(int)
R['dia'] = pd.to_datetime(R.fin, unit='s').dt.strftime('%Y-%m-%d')
R.to_csv(os.path.join(D, 'cal_real_pujas.csv'), index=False)
print('pujas reales', len(R), 'rf_a', R.rf_a.sum(), 'rf_chain', R.rf_chain.sum(), 'rf_tardio', R.rf_tardio.sum(), 'union', R.rf_union.sum(), flush=True)
# simulador
TOK = json.load(open(S.SRC + 'tokens.json')); mk = {}
for t, v in TOK.items():
    if v[0] in ('ETH', 'SOL', 'XRP'): mk[(v[0], str(v[1]))] = float(v[3])
CELLS = [(lc, al) for lc in (65, 150, 280, 450) for al in ('prop', 'lo', 'hi')]
rows = []; nmiss = collections.Counter(); n = 0
for _, r in R.iterrows():
    key = (r.act, r.mid); fin = int(r.fin)
    if key not in mk: nmiss['sin_token'] += 1; continue
    if not (S.FIN_MIN <= fin <= S.FIN_MAX): nmiss['fuera_rango_MEDIR'] += 1; continue
    path = S.SRC + f'mk/{r.act}_{r.mid}.gz'
    if not os.path.exists(path): nmiss['sin_fichero'] += 1; continue
    w = S.DES.get(r.mid)
    if w is None: nmiss['sin_desenlace'] += 1; continue
    gi = bisect.bisect_left(S.GALL, (fin - 305) * 1000)
    if gi < len(S.GALL) and S.GALL[gi] <= (fin - 60) * 1000: nmiss['hueco_global'] += 1; continue
    ev = S.load(path)
    if not ev: nmiss['vacio'] += 1; continue
    TT, TV, lvl, NT, roto = S.prepara(ev, fin)
    if roto: nmiss['hueco_token'] += 1; continue
    g = (fin * 1000 - np.arange(S.T_HI * 1000, S.T_LO * 1000 - 1, -S.STEP)).astype(np.int64)
    L = None
    for t in g:
        for LL in ('Y', 'N'):
            b = S.top_at(TT, TV, LL, t)
            if 110 < b <= 300: L = LL; break
        if L: break
    if L is None: nmiss['sin_banda_en_sim'] += 1; continue
    k = 2 if r.act == 'ETH' else 1; gana = int((w == 'YES') == (L == 'Y'))
    for (lc, al) in CELLS:
        LAST.clear()
        res = S.politica(TT, TV, lvl, NT, fin, L, k, settle=0, repost=1500, lat_can=lc, alloc=al)
        rr, acc, tipo, o, npost = res
        cl = S.clase(NT, L, rr, o, tipo) if rr is not None else None
        rows.append(dict(mid=r.mid, act=r.act, fin=fin, dia=r.dia, lado_sim=L, gana=gana, lat_can=lc, alloc=al, fill=int(rr is not None), acc=acc,
                         p=(o / 1000.0 if o else np.nan), r=rr, tl=LAST.get('tl') if rr is not None else None, tipo=tipo, clase=cl, npost=npost))
    n += 1
    if n % 50 == 0: print(n, dict(nmiss), flush=True)
pd.DataFrame(rows).to_csv(os.path.join(D, 'cal_sim.csv'), index=False)
print('FIN mercados', n, 'excluidos', dict(nmiss), flush=True)
