#!/usr/bin/env python3
"""eng_v5.py -- construye el motor del dia (DayEngV4, modo causal, sello tm3, dedupe) EXACTAMENTE como el bloque STAMP=v3 / ENG=dd de passT_v4.py (L2/passT_v4.py l.20-58; ese fichero es un script y no se puede importar,
asi que el bloque se replica aqui; test_sim.py comprueba que reproduce los rellenos de los segmentos G0 de out_v4/SEGT_v3dd). Reutiliza engine_v4/engine_clock/stamp_v3 por import. Solo lectura, 0 ordenes."""
import sys, json, glob, numpy as np, pandas as pd
L2 = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/'; P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
sys.path.insert(0, L2); sys.path.insert(0, P2 + 'escalera_B')
import engine as G, engine_v4 as E4, stamp_v3 as ST
PB = P2 + 'precursores_barrido/out/'; TXD = '/mnt/HC_Volume_106538179/libro5_tx/'
def build(d):
    tape = pd.read_pickle(PB + f'tape_{d}.pkl'); bad = {tuple(x) for x in json.load(open(PB + f'bad_{d}.json'))['bad']}
    E = E4.DayEngV4(d, 'chain', tape, bad, modo='causal', dedupe=True); D = E.D
    fr = []
    for dd_ in [(pd.Timestamp(d) + pd.Timedelta(days=i)).strftime('%Y-%m-%d') for i in (-1, 0, 1)]:
        for f_ in sorted(glob.glob(TXD + f'libro5_tx_{dd_}_*.csv.gz')): fr.append(pd.read_csv(f_, header=None, names=['t_ev', 'token', 'tx', 'recv'], dtype={'token': str, 'tx': str}))
    TEV = pd.concat(fr, ignore_index=True).groupby('tx').t_ev.min() if fr else pd.Series(dtype='int64'); del fr
    tp = tape.assign(k=tape.token_id.map(D.tokidx)); tp = tp[tp.k.notna()].copy(); tp['k'] = tp.k.astype(int)
    tp['pr3'] = tp.price.round(3); ev = tp.groupby(['k', 'tx']).agg(t=('t_ws_ms', 'min'), pmin=('price', 'min'), pmax=('pr3', 'max'), S=('sh', 'sum'), npr=('pr3', 'nunique')).reset_index(); tp = tp.drop(columns=['pr3'])
    evk = ev.k.values; evt = ev.t.values.astype(np.int64); evp = ev.pmin.values
    tev_ = ev.tx.map(TEV).values; tev_abs = np.where(np.isfinite(tev_), np.nan_to_num(tev_, nan=-1.0), -1.0).astype(np.int64)
    tm, RAMA, ROW, DEX, C_EPOCA, NEX = ST.stamp_events(D.qt, D.v0, D.v2, D.qb, evk, tev_abs, ev.pmax.values, evp, ev.S.values, ev.npr.values)
    sinev = RAMA == 'sinev'; tm = np.where(sinev, evt - 63, tm); ev['tm'] = tm; ev['rama'] = RAMA
    tp = tp.merge(ev[['k', 'tx', 'tm']], on=['k', 'tx'], how='left'); tp['t_ws_ms'] = tp.tm.astype(np.int64)
    E.tape = G.Tape('chain', D, tp.drop(columns=['k', 'tm']))
    return E, dict(c_epoca=int(C_EPOCA), ramas={r: int((RAMA == r).sum()) for r in set(RAMA)})
