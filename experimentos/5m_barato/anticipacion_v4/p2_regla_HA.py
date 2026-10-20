#!/usr/bin/env python3
"""Paso 2 anticipacion_v4: simula la regla H-A (umbral laxo sobre margen que SUBE) sobre feat_D (r3_out, 13 dias 06-18 Oct, BTC).
VARIANTES FIJADAS ANTES DE MIRAR RESULTADOS (4 + baseline V4):
  A: m>=-0,05 y dm>=0,01      (dm = db15_1s - da5_1s = subida del margen en el ultimo 1 s)
  B: m>=-0,02 y dm>=0,01
  C: m>=-0,05 y dm>=0,01 y m_prev<-0,05 (cruce ascendente estricto)
  D: m>=0,00 y dm>=0,01
  V4: m>=0,05 (condicion 'sen' del vigia, 1er instante)
Entrada: 1ER instante por cierre que cumple (poblacion PRIMARIA, 1 por cierre); RE-ARMES: nuevos disparos >=2 s despues del anterior, max 3 (poblacion aparte).
Ejecucion: limite = ask5 del instante, tomador a +215 ms (ask real nivel 1 por recepcion, ask_e215<=limite, acc_e215 = min(objetivo, tamano nivel 1)).
EV ponderado por EUR; IC90 bootstrap por cierre y por dia; sin 2 mejores dias; Bonferroni x4 (cuantil 1,25 %); DESC 06-12 / TEST 13-18."""
import glob, gzip, numpy as np, pandas as pd
O = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/r3_out/'
F = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(O + 'feat_*.csv.gz'))], ignore_index=True)
F = F.drop_duplicates(['cierre', 't']).sort_values(['cierre', 't'])
n0 = len(F); F = F.dropna(subset=['gana']); print('filas', n0, 'con desenlace', len(F))
F['gana'] = F.gana.astype(bool)
F['dm'] = F.db15_1s - F.da5_1s; F['m_prev'] = F.m - F.dm
fee = lambda p: 0.07 * p * (1 - p)
VAR = {'A m>=-.05&dm>=.01': (F.m >= -0.05 - 1e-9) & (F.dm >= 0.01 - 1e-9),
       'B m>=-.02&dm>=.01': (F.m >= -0.02 - 1e-9) & (F.dm >= 0.01 - 1e-9),
       'C cruce -.05': (F.m >= -0.05 - 1e-9) & (F.dm >= 0.01 - 1e-9) & (F.m_prev < -0.05),
       'D m>=0&dm>=.01': (F.m >= 0 - 1e-9) & (F.dm >= 0.01 - 1e-9),
       'V4 m>=.05': F.sen.astype(bool)}
rng = np.random.default_rng(11)
def boot(df, key, q, n=4000):
    g = df.groupby(key)[['pnl', 'coste']].sum().values
    if len(g) < 3: return (np.nan, np.nan)
    ix = rng.integers(0, len(g), (n, len(g))); num = g[ix, 0].sum(1); den = g[ix, 1].sum(1); r = num[den > 0] / den[den > 0]
    return np.percentile(r, [q, 100 - q]).round(3)
def res(d, nom):
    if not len(d) or d.coste.sum() <= 0: print(f'  {nom:28s} n=0'); return None
    ev = d.pnl.sum() / d.coste.sum(); byd = d.groupby('dia')[['pnl', 'coste']].sum(); top = byd.pnl.sort_values(ascending=False).index[:2]
    r2 = d[~d.dia.isin(top)]; ev2 = r2.pnl.sum() / r2.coste.sum() if r2.coste.sum() > 0 else np.nan
    print(f'  {nom:28s} n={len(d):3d} dias={d.dia.nunique():2d} coste={d.coste.sum():6.1f} PnL={d.pnl.sum():+7.2f} EV={ev:+.3f} acierto={d.gana.mean():.2f} precio={ (d.p).mean():.2f} '
          f'IC90cierre={boot(d,"cierre",5)} IC90dia={boot(d,"dia",5)} | Bonf4 cierre inf={boot(d,"cierre",1.25)[0]} | sin2mejoresdias={ev2:+.3f} dias+={(byd.pnl>0).sum()}/{len(byd)}')
    return ev
def sim(mask, rearmes):
    d = F[mask].copy(); out = []
    for c, g in d.groupby('cierre'):
        last = None; k = 0
        for r in g.itertuples():
            if last is None or (rearmes and r.t - last >= 2000 and k < 4):
                if last is None or rearmes: out.append((r, k))
                last = r.t; k += 1
                if not rearmes: break
    rows = []
    for r, k in out:
        ok = r.acc_e215 > 0 and r.ask_e215 == r.ask_e215
        rows.append(dict(dia=r.dia, cierre=r.cierre, t=r.t, k=k, ejec=ok, p=r.ask_e215, acc=r.acc_e215 if ok else 0.0, gana=r.gana, m=r.m, ask=r.ask5, lim=r.ask5))
    x = pd.DataFrame(rows)
    return x
for nom, mk in VAR.items():
    print('\n=== ', nom)
    X = sim(mk, True)
    if not len(X): print('  sin disparos'); continue
    X['coste'] = X.acc * (X.p + fee(X.p)); X['pnl'] = X.acc * (X.gana.astype(float) - X.p - fee(X.p))
    E = X[X.ejec]; first = E[E.k == 0]; first_all = X[X.k == 0]
    print(f'  disparos 1a por cierre {len(first_all)} ejecutables a +215 ms {len(first)} ({100*len(first)/max(len(first_all),1):.0f} %) | re-armes disparados {int((X.k>0).sum())} ejec {int((E.k>0).sum())}')
    res(first, 'PRIMARIA 1a/cierre TODO'); 
    for per, ds in (('DESC 06-12', lambda s: s <= '2026-10-12'), ('TEST 13-18', lambda s: s >= '2026-10-13')):
        res(first[first.dia.map(ds)], 'PRIMARIA ' + per)
    res(E[E.k > 0], 'RE-ARMES (k>=1)')
    res(E, 'TODO (1a + re-armes)')
    # no rellenadas: acierto de las que se pierden
    nr = first_all[~first_all.ejec]
    print(f'  no ejecutables a +215: {len(nr)} acierto {nr.gana.mean() if len(nr) else float("nan"):.2f} (selecc. adversa si > ejecutadas {first.gana.mean() if len(first) else float("nan"):.2f})')
