"""F8 EXPLORATORY (pedido chief 25-Oct, fuera del PREREG): ¿separan los rasgos de estructura (precio/T/moneda/hora) los rellenos que RECIBE B de los de la poblacion?
Descomposicion de la brecha EV por EUR (rellenos, pnl ponderado por EUR, fee maker 0, sin rebate):
  [poblacion: todas las vidas virtuales rellenas pes, ETH/SOL/XRP, mismos dias] -> [vidas virtuales EMPAREJADAS con las ordenes de B (misma moneda, cierre, lado, |dt|<=5 s)] -> [B real].
  tramo 1 (poblacion -> emparejadas) = momento/estructura en que B arma; tramo 2 (emparejadas -> B real) = ejecucion/cola (lo que la estructura NO explica).
Ademas: post-estratificacion de la poblacion a la distribucion de B en (moneda x b 0,05 x T 60s) -> cuanto de la brecha explica la estructura P0 pura."""
import gzip, glob, json, numpy as np, pandas as pd
DL = '/root/polymarket-research-datalogs/'; rng = np.random.default_rng(7)
V = pd.read_parquet(DL + 'f8_estructura/tabla.parquet').drop_duplicates(['mercado', 'lado', 't0_recv_ms'])
V = V[(V.censurada == 0) & V.coin.isin(['ETH', 'SOL', 'XRP'])].copy(); V = V[~((V.relleno_pes == 1) & V.gana.isna())]
V['dia'] = pd.to_datetime(V.t0_recv_ms, unit='ms', utc=True).dt.strftime('%Y-%m-%d'); V['c'] = 5.0 * V.b
V['y'] = np.where(V.relleno_pes == 1, V.pnl_5acc_si_relleno.astype(float), 0.0); V['t0s'] = V.t0_recv_ms / 1000.0
B = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(DL + 'etiquetado_pasivo_B/etiquetado_B_2026-10-2*.csv.gz'))], ignore_index=True)
B = B[(B.unidad == 'orden') & B.coin.isin(['ETH', 'SOL', 'XRP']) & (B.resuelto == 1)].copy()
B['cierre'] = B.fin_s.astype(np.int64); B['t0s'] = B.t0.astype(float); B['lado'] = B.lado.astype(str)
B['fill'] = (B.acc_llena.fillna(0) > 0).astype(int); B['costeB'] = B.acc_llena.fillna(0) * B.precio; B['yB'] = B.acc_llena.fillna(0) * (B.gana_lado - B.precio)
dias = sorted(set(B.dia)); print('dias B', dias, 'ordenes', len(B), 'rellenas', B.fill.sum())
# emparejar: mejor vida (misma moneda,cierre,lado) con |dt|<=5 s
Vi = V[['coin', 'cierre', 'lado', 't0s', 'b', 'T_s', 'relleno_pes', 'y', 'c', 'dia']].copy().sort_values('t0s')
Vi['k'] = Vi.coin.astype(str) + '|' + Vi.cierre.astype(str) + '|' + Vi.lado
B['k'] = B.coin.astype(str) + '|' + B.cierre.astype(str) + '|' + B.lado
g = {k: (x.t0s.values, x.index.values) for k, x in Vi.groupby('k')}
mi = np.full(len(B), -1); 
for i, (k, t) in enumerate(zip(B.k.values, B.t0s.values)):
    if k in g:
        ts, ix = g[k]; j = np.searchsorted(ts, t); cand = [q for q in (j - 1, j) if 0 <= q < len(ts) and abs(ts[q] - t) <= 5]
        if cand: q = min(cand, key=lambda q: abs(ts[q] - t)); mi[i] = ix[q]
B['mi'] = mi; Bm = B[B.mi >= 0].copy(); print('emparejadas', len(Bm), 'de', len(B))
M = Vi.loc[Bm.mi.values].reset_index(drop=True); Bm = Bm.reset_index(drop=True)
Vp = Vi[Vi.dia.isin(dias)]
def ev(y, c): return float(y.sum() / c.sum()) if c.sum() > 0 else None
fp = Vp.relleno_pes == 1; fm = M.relleno_pes == 1
R = {'n_ordenes_B': int(len(B)), 'n_emparejadas': int(len(Bm)), 'dias': dias,
     'poblacion': {'n_vidas': int(len(Vp)), 'n_rellenas': int(fp.sum()), 'p_relleno': float(fp.mean()), 'EV_relleno': ev(Vp.y[fp], Vp.c[fp])},
     'emparejadas_virtual': {'n': int(len(M)), 'n_rellenas': int(fm.sum()), 'p_relleno': float(fm.mean()), 'EV_relleno': ev(M.y[fm], M.c[fm])},
     'B_real_emparejadas': {'n': int(len(Bm)), 'n_rellenas': int(Bm.fill.sum()), 'p_relleno': float(Bm.fill.mean()), 'EV_relleno': ev(Bm.yB, Bm.costeB)},
     'B_real_todas': {'n': int(len(B)), 'n_rellenas': int(B.fill.sum()), 'p_relleno': float(B.fill.mean()), 'EV_relleno': ev(B.yB, B.costeB)}}
# post-estratificacion de la poblacion a la estructura de B (moneda x b x T)
def st(d, bcol, tcol): return d.coin.astype(str) + '|' + (np.round(d[bcol] * 20) / 20).astype(str) + '|' + (d[tcol] // 60).astype(int).astype(str)
Vp = Vp.assign(s=st(Vp, 'b', 'T_s')); Bs = B.assign(b=B.precio, s=None); Bs['s'] = st(Bs, 'b', 'T_s')
# peso por celda = coste de B relleno en la celda / coste de poblacion rellena en la celda
wB = Bs[Bs.fill == 1].groupby('s').costeB.sum(); wP = Vp[Vp.relleno_pes == 1].groupby('s').c.sum(); ev_cell = Vp[Vp.relleno_pes == 1].groupby('s').apply(lambda x: x.y.sum() / x.c.sum(), include_groups=False)
cells = wB.index.intersection(ev_cell.index); cov = float(wB[cells].sum() / wB.sum())
R['post_estratificado_P0'] = {'EV_poblacion_con_estructura_de_B': float((ev_cell[cells] * wB[cells]).sum() / wB[cells].sum()), 'cobertura_eur_B_en_celdas_con_poblacion': cov, 'n_celdas': int(len(cells))}
# IC90 por cierre/dia de las diferencias
def boot(f, key_p, nb=2000):
    ks = np.unique(key_p); out = []
    return None
R['por_dia'] = {d: {'EV_pob': ev(Vp[(Vp.dia == d) & (Vp.relleno_pes == 1)].y, Vp[(Vp.dia == d) & (Vp.relleno_pes == 1)].c),
                    'EV_B': ev(B[(B.dia == d)].yB, B[(B.dia == d)].costeB), 'n_B_fill': int(B[B.dia == d].fill.sum())} for d in dias}
# IC90 de EV_B - EV_pob por cierre (bootstrap de cierres: B)
cb = B.groupby('cierre')[['yB', 'costeB']].sum(); sub = []
cp = Vp[Vp.relleno_pes == 1].groupby('cierre')[['y', 'c']].sum()
cl = np.array(sorted(set(cb.index) | set(cp.index))); cbb = cb.reindex(cl).fillna(0).values; cpp = cp.reindex(cl).fillna(0).values
dif = []
for _ in range(3000):
    ix = rng.integers(0, len(cl), len(cl)); b = cbb[ix].sum(0); p = cpp[ix].sum(0); dif.append(b[0] / max(b[1], 1e-9) - p[0] / max(p[1], 1e-9))
R['EV_B_menos_EV_pob_IC90_cierre'] = [float(np.percentile(dif, 5)), float(np.percentile(dif, 95))]
json.dump(R, open('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f8_estructura/datos/f8_b_vs_poblacion.json', 'w'), indent=1, default=float)
print(json.dumps(R, indent=1, default=float))

# --- parte 2: ¿separan los scores P0/P1/P2 (walk-forward, cortes del TRAIN) los rellenos de B de los de la poblacion? (descriptivo, n pequeno)
S = pd.read_parquet(DL + 'f8_estructura/f8_scores.parquet'); R2 = {}
Vp2 = V[V.dia.isin(dias)]
for m in ('P0', 'P1', 'P2'):
    s = S[S.modelo == m].set_index('idx'); s = s[~s.index.duplicated()]
    P = Vp2.join(s[['score', 'cut30']], how='inner'); P['flag'] = P.score >= P.cut30
    Mx = Bm.assign(idx=Bm.mi.values).set_index('idx').join(s[['score', 'cut30']], how='inner'); Mx['flag'] = Mx.score >= Mx.cut30
    pf = P[P.relleno_pes == 1]
    R2[m] = {'flag_rate_vidas_poblacion': float(P.flag.mean()), 'flag_rate_vidas_emparejadas_B': float(Mx.flag.mean()), 'flag_rate_rellenos_virtuales_pob': float(pf.flag.mean()),
             'flag_rate_rellenos_REALES_B': float(Mx[Mx.fill == 1].flag.mean()), 'n_rellenos_B': int((Mx.fill == 1).sum()),
             'score_medio_pob_rellenas': float(pf.score.mean()), 'score_medio_B_rellenas': float(Mx[Mx.fill == 1].score.mean()), 'score_medio_B_no_rellenas': float(Mx[Mx.fill == 0].score.mean()),
             'EV_B_real_flag': ev(Mx[(Mx.fill == 1) & Mx.flag].yB, Mx[(Mx.fill == 1) & Mx.flag].costeB), 'EV_B_real_noflag': ev(Mx[(Mx.fill == 1) & ~Mx.flag].yB, Mx[(Mx.fill == 1) & ~Mx.flag].costeB),
             'n_B_fill_flag': int(((Mx.fill == 1) & Mx.flag).sum()), 'n_B_fill_noflag': int(((Mx.fill == 1) & ~Mx.flag).sum()),
             'p_relleno_B_real_flag': float(Mx[Mx.flag].fill.mean()), 'p_relleno_B_real_noflag': float(Mx[~Mx.flag].fill.mean()),
             'EV_virtual_pob_flag': ev(pf[pf.flag].y, pf[pf.flag].c), 'EV_virtual_pob_noflag': ev(pf[~pf.flag].y, pf[~pf.flag].c)}
R2['precio_B_menos_b_vida_emparejada'] = {'media': float((Bm.precio - M.b).mean()), 'frac_igual': float(((Bm.precio - M.b).abs() < 0.005).mean()), 'dt_s_medio': float((Bm.t0s - M.t0s).abs().mean())}
json.dump(R2, open('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f8_estructura/datos/f8_b_vs_poblacion_scores.json', 'w'), indent=1, default=float)
print(json.dumps(R2, indent=1, default=float))
