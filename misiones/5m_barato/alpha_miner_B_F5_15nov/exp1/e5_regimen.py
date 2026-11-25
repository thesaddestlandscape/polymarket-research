#!/usr/bin/env python3
"""E5 (ADDENDUM1 §3 E5): regimen por conductores (K = 4), descriptivo de la POBLACION censurada (prints tipo B, spec p60 = l_ef 60 ms; sens p35), todos los terciles; secundario: solo prints F5-bajo (G2) y solo T_rem > 60 s.
Unidad = (dia, bloque de 4 h UTC, moneda). Conductores (todos con informacion anterior al bloque): D1 = vol realizada 1-min de la moneda en los 30 min previos al bloque; D2 = idem 4 h previas; D3 = EV pond. EUR del bloque 4 h anterior (3 monedas juntas, tipo B);
D4 = EV pond. EUR historico del mismo slot horario en los 14 dias anteriores (>= 10 dias). Umbral = mediana movil de los 14 dias previos del propio conductor (>= 10 dias distintos disponibles). Viable: D1 <= med, D2 <= med, D3 >= med, D4 >= med (un conductor = una regla).
Metrica: dEV diario = EV(unidades viables) - EV(no viables) del dia (ponderado por EUR); dPnL = -pnl de las no viables. Walk-forward desde 2026-10-23. Gate (K = 4, placebo max-statistic p <= 0,0125): media diaria > 0, IC90 por dias inf > 0, >= 60 % de dias +.
Placebo: permutar la viabilidad dentro de (dia, moneda) entre las unidades evaluables (B=1000; claves independientes por conductor = conservador). Los 215 fills de B (4 dias, historial < 14 dias) se muestran viables/no viables SIN decidir. Solo lectura de caches; sin red."""
import os, sys, glob, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from popdata import *
t0 = time.time(); SPEC = 'p60'; EVAL0 = '2026-10-23'; COINS = ('ETH', 'SOL', 'XRP'); SYM = {'ETH': 'ETHUSDT', 'SOL': 'SOLUSDT', 'XRP': 'XRPUSDT'}
P, est = carga_pob(specs_keep=[SPEC, 'p35']); cobL, por = resumen_cobertura(est); COMPLETO = len(por.get('COMPLETE', [])) == len(est)
txt = [f'# E5 regimen por conductores (ADDENDUM1 sha {ADD_SHA[:8]}) -- POBLACION censurada, descriptivo; tipo B de {SPEC}; evaluacion walk-forward desde {EVAL0}'] + cobL + [f'Estado: {"COMPLETO" if COMPLETO else "PARTIAL"}; prints {len(P)}']
if len(P) == 0: txt.append('DATA_BLOCKED: sin caches de poblacion'); write(EXP + 'E5_regimen.txt', txt); estado_fase('E5', 'DATA_BLOCKED'); print('\n'.join(txt)); sys.exit(2)
# ---------------- barras de 1 min de Binance (cache/bn_D.csv de e2_dia)
partes = [pd.read_csv(p, header=None, names=['sym', 'min', 'o', 'h', 'l', 'z', 'n'], dtype={'sym': str}) for p in sorted(glob.glob(CACHE + 'bn_2026-*.csv'))]
if not partes: txt.append('DATA_BLOCKED: sin barras Binance (cache/bn_*.csv)'); write(EXP + 'E5_regimen.txt', txt); estado_fase('E5', 'DATA_BLOCKED'); print('\n'.join(txt)); sys.exit(2)
BN = pd.concat(partes, ignore_index=True); BN = BN.groupby(['sym', 'min'], sort=True).agg(z=('z', 'last'), n=('n', 'sum')).reset_index()
m_lo, m_hi = int(BN['min'].min()), int(BN['min'].max()); SV = {}
for c in COINS:
    b = BN[BN.sym == SYM[c]].set_index('min').z.reindex(np.arange(m_lo, m_hi + 1)).ffill(); lz = np.log(b.values.astype(float)); r = np.r_[0.0, np.diff(lz)]; r[~np.isfinite(r)] = 0.0
    SV[c] = (np.cumsum(r), np.cumsum(r * r), np.isfinite(lz))
txt.append(f'Barras Binance 1 min: minutos {m_lo}..{m_hi} ({(m_hi - m_lo) / 1440:.1f} dias), filas {len(BN)}; huecos rellenados con el ultimo cierre (retorno 0)')
def vol(c, a, b):
    """desviacion tipica de los retornos de 1 min en los minutos [a, b); NaN si no hay serie completa en la ventana."""
    if a < m_lo + 1 or b > m_hi + 1: return np.nan
    S1, S2, ok = SV[c]; i, j = a - m_lo, b - m_lo
    if not ok[i - 1:j].all(): return np.nan
    n = j - i; mu = (S1[j - 1] - S1[i - 1]) / n; return float(np.sqrt(max((S2[j - 1] - S2[i - 1]) / n - mu * mu, 0.0)))
# ---------------- unidades (dia, bloque, moneda) con pnl/coste de prints tipo B
q = P.q.values.astype(float); b60 = P['bid_' + SPEC].values.astype(float); tB = np.isfinite(b60) & ((b60 - q) >= 0.0099 - 1e-12); ter60 = ter(P['F5_' + SPEC].values)
dias_u = sorted(P.dia.unique()); di = {d: i for i, d in enumerate(dias_u)}; dpos = np.array([di[d] for d in P.dia.to_numpy(dtype=object)]); blk = (P.hora.values.astype(int) // 4); cn = P.coin.to_numpy(dtype=object); trem = P.fin.values.astype(np.int64) - P.r_ex.values / 1000.0
pnl = P.pnl.values.astype(float); co = P.coste.values.astype(float); ND = len(dias_u)
def agrega(m):
    d = pd.DataFrame({'d': dpos[m], 'b': blk[m], 'c': cn[m], 'p': pnl[m], 'k': co[m]}); g = d.groupby(['d', 'b', 'c']).agg(p=('p', 'sum'), k=('k', 'sum'), n=('p', 'size')); return g
U_all = agrega(tB); U_t60 = agrega(tB & (trem > 60)); U_bajo = agrega(tB & (ter60 == 'bajo'))
# EV por (dia, bloque) con las 3 monedas juntas (tipo B, todo T) para D3/D4
bp = np.zeros((ND, 6)); bk = np.zeros((ND, 6)); bnn = np.zeros((ND, 6))
for (d, b, c), r in U_all.iterrows(): bp[d, b] += r.p; bk[d, b] += r.k; bnn[d, b] += r.n
def d3(d, b):
    dd, bb = (d, b - 1) if b > 0 else (d - 1, 5)
    return (bp[dd, bb] / bk[dd, bb]) if dd >= 0 and bnn[dd, bb] >= 30 and bk[dd, bb] > 0 else np.nan
def d4(d, b):
    lo = max(0, d - 14); w = [x for x in range(lo, d) if bnn[x, b] > 0]
    return (sum(bp[x, b] for x in w) / sum(bk[x, b] for x in w)) if len(w) >= 10 and sum(bk[x, b] for x in w) > 0 else np.nan
day0 = {d: ms(d + 'T00:00:00Z') for d in dias_u}
TAB = {}
for d in dias_u:
    for b in range(6):
        s = (day0[d] + b * 4 * 3600000) // 60000
        for c in COINS: TAB[(di[d], b, c)] = [vol(c, s - 30, s), vol(c, s - 240, s), d3(di[d], b), d4(di[d], b)]
T = pd.DataFrame.from_dict(TAB, orient='index', columns=['D1', 'D2', 'D3', 'D4']); T.index = pd.MultiIndex.from_tuples(T.index, names=['d', 'b', 'c'])
def med_mov(col, by_coin):
    """mediana movil de los 14 dias previos (>= 10 dias distintos con el conductor definido); devuelve Serie indexada como T."""
    out = pd.Series(np.nan, index=T.index)
    for d in range(ND):
        win = T[(T.index.get_level_values('d') >= d - 14) & (T.index.get_level_values('d') < d) & T[col].notna()]
        if by_coin:
            for c in COINS:
                w = win[win.index.get_level_values('c') == c]
                if w.index.get_level_values('d').nunique() >= 10: out[(out.index.get_level_values('d') == d) & (out.index.get_level_values('c') == c)] = float(w[col].median())
        else:
            w = win[win.index.get_level_values('c') == 'ETH']                    # D3/D4 son comunes a las 3 monedas: una sola copia por bloque
            if w.index.get_level_values('d').nunique() >= 10: out[out.index.get_level_values('d') == d] = float(w[col].median())
    return out
MED = {'D1': med_mov('D1', True), 'D2': med_mov('D2', True), 'D3': med_mov('D3', False), 'D4': med_mov('D4', False)}
FLAG = pd.DataFrame(index=T.index); FLAG['v1'] = np.where(T.D1.notna() & MED['D1'].notna(), (T.D1 <= MED['D1']).astype(float), np.nan); FLAG['v2'] = np.where(T.D2.notna() & MED['D2'].notna(), (T.D2 <= MED['D2']).astype(float), np.nan)
FLAG['v3'] = np.where(T.D3.notna() & MED['D3'].notna(), (T.D3 >= MED['D3']).astype(float), np.nan); FLAG['v4'] = np.where(T.D4.notna() & MED['D4'].notna(), (T.D4 >= MED['D4']).astype(float), np.nan)
txt.append('Unidades (dia, bloque 4 h, moneda) con conductor evaluable (todas las fechas): ' + ', '.join(f'v{k}: {int(FLAG[f"v{k}"].notna().sum())}' for k in (1, 2, 3, 4)) + f' de {len(FLAG)} | primer dia evaluable por conductor: ' + ', '.join(f'v{k}: {dias_u[int(FLAG[FLAG[f"v{k}"].notna()].index.get_level_values("d").min())] if FLAG[f"v{k}"].notna().any() else "n/d"}' for k in (1, 2, 3, 4)))
# ---------------- evaluacion por conductor
def eval_units(U, tag, B=1000, seed=20261115):
    X = FLAG.join(U, how='left').fillna({'p': 0.0, 'k': 0.0, 'n': 0}); dn = X.index.get_level_values('d').values; i0 = min([i for d_, i in di.items() if d_ >= EVAL0], default=0); sel_d = dn >= i0; res = {}; rng = np.random.default_rng(seed); dist = {}; setup = {}
    for k in (1, 2, 3, 4):
        f = X[f'v{k}'].values; ok = np.isfinite(f) & sel_d & (X.k.values > 0); setup[k] = dict(ok=ok, f=f[ok] > 0.5, p=X.p.values[ok], c=X.k.values[ok], d=dn[ok], g=pd.factorize(pd.MultiIndex.from_arrays([dn[ok], X.index.get_level_values('c').values[ok]]))[0])
    def stat(a, fl):
        nd = ND; sv = np.bincount(a['d'][fl], a['p'][fl], nd); cv = np.bincount(a['d'][fl], a['c'][fl], nd); sn = np.bincount(a['d'][~fl], a['p'][~fl], nd); cn_ = np.bincount(a['d'][~fl], a['c'][~fl], nd)
        g = np.full(nd, np.nan); okd = (cv > 0) & (cn_ > 0); g[okd] = sv[okd] / cv[okd] - sn[okd] / cn_[okd]; return g
    for k in (1, 2, 3, 4):
        a = setup[k]
        if len(a['p']) == 0: res[k] = dict(n_unidades=0); continue
        g = stat(a, a['f']); d_ = g[np.isfinite(g)]; lo, p_t, mu = t_ic(d_) if len(d_) >= 3 else (np.nan, np.nan, np.nan); fl = a['f']
        evv = a['p'][fl].sum() / max(a['c'][fl].sum(), 1e-9); evn = a['p'][~fl].sum() / max(a['c'][~fl].sum(), 1e-9); evt = a['p'].sum() / a['c'].sum()
        res[k] = dict(n_unidades=int(len(a['p'])), frac_viables=float(fl.mean()), frac_coste_viable=float(a['c'][fl].sum() / a['c'].sum()), n_dias=int(len(d_)), media_dia=float(mu), ic90_dias_inf=float(lo), p_t=float(p_t), dias_pos=int((d_ > 0).sum()), frac_dias_pos=float((d_ > 0).mean()) if len(d_) else np.nan,
                      sin2mejores=float(np.sort(d_)[:-2].mean()) if len(d_) > 2 else np.nan, ev_viables=float(evv), ev_no_viables=float(evn), ev_todo=float(evt), dEV_pooled=float(evv - evn), dPnL_evitar_no_viables=float(-a['p'][~fl].sum()), dEV_retenido_vs_todo=float(evv - evt), serie=dict(zip([dias_u[i] for i in np.flatnonzero(np.isfinite(g))], np.round(g[np.isfinite(g)], 3).tolist())))
    ords = {k: np.argsort(setup[k]['g'], kind='stable') for k in (1, 2, 3, 4) if len(setup[k]['p'])}
    for k in ords: dist[k] = np.empty(B)
    for b in range(B):
        for k in ords:
            a = setup[k]; ordr = np.lexsort((rng.random(len(a['p'])), a['g'])); fp = np.empty(len(a['p']), bool); fp[ords[k]] = a['f'][ordr]; g = stat(dict(a, f=fp), fp); dist[k][b] = np.nanmean(g) if np.isfinite(g).any() else np.nan
    mx = np.nanmax(np.vstack([dist[k] for k in ords]), axis=0) if ords else np.array([np.nan])
    for k in ords:
        r = res[k]; r['p_placebo_celda'] = float(np.nanmean(dist[k] >= r['media_dia'] - 1e-12)); r['p_placebo_maxstat'] = float(np.nanmean(mx >= r['media_dia'] - 1e-12)); r['placebo_media'] = float(np.nanmean(dist[k]))
        r['cumple_gate'] = bool(r['media_dia'] > 0 and r['ic90_dias_inf'] > 0 and r['frac_dias_pos'] >= 0.6 and r['p_placebo_maxstat'] <= 0.0125)
        r['etiqueta'] = 'VALIDADA-poblacion (potenciador descriptivo, censurado)' if r['cumple_gate'] else ('EXPLORATORIA' if (r['media_dia'] > 0 and r['frac_dias_pos'] >= 0.5) else 'INSUFFICIENT (media <= 0 o < 50 % dias +; no refuta: poblacion censurada)')
    return res
NM = {1: 'D1 vol 30 min <= mediana', 2: 'D2 vol 4 h <= mediana', 3: 'D3 EV bloque previo >= mediana', 4: 'D4 EV mismo slot 14 d >= mediana'}; RES = {}
for tag, U in (('PRIMARIO tipo B, todo T, todos los terciles', U_all), ('secundario: tipo B, T_rem > 60 s (ventana de B)', U_t60), ('secundario: tipo B, solo F5 bajo (G2)', U_bajo)):
    R = eval_units(U, tag); RES[tag] = R; txt += ['', f'## {tag}']
    for k in (1, 2, 3, 4):
        r = R[k]
        if r.get('n_unidades', 0) == 0: txt.append(f'{NM[k]}: sin unidades evaluables'); continue
        txt.append(f"{NM[k]}: {r['n_unidades']} unidades ({100*r['frac_viables']:.0f} % viables, {100*r['frac_coste_viable']:.0f} % del coste) | {r['n_dias']} dias | dEV diario medio {r['media_dia']:+.3f} IC90 dias inf {r['ic90_dias_inf']:+.3f} (p_t {r['p_t']:.3f}) | dias+ {r['dias_pos']}/{r['n_dias']} ({100*r['frac_dias_pos']:.0f} %) | sin 2 mejores {r['sin2mejores']:+.3f} | EV viables {r['ev_viables']:+.3f} vs no viables {r['ev_no_viables']:+.3f} (todo {r['ev_todo']:+.3f}) | dEV agrupado {r['dEV_pooled']:+.3f} | dPnL poblacion al evitar no viables {r['dPnL_evitar_no_viables']:+.0f} EUR | placebo celda p {r['p_placebo_celda']:.3f} maxstat p {r['p_placebo_maxstat']:.4f} -> {r['etiqueta']}")
# ---------------- B real (215 fills, 4 dias) viable / no viable: DESCRIPTIVO (historial < 14 dias para D3/D4)
Bf = pd.read_pickle(EXP + 'B_fills_v3.pkl'); tt = pd.to_datetime(Bf.tm3.values, unit='ms', utc=True); Bf['d_utc'] = tt.strftime('%Y-%m-%d'); Bf['b_utc'] = (tt.hour // 4).values; txt += ['', '## B real (215 fills, 20-23 Oct; bloque por tm3 UTC): viables / no viables por conductor (DESCRIPTIVO; sin decidir)']
for k in (1, 2, 3, 4):
    fl = []
    for r in Bf.itertuples():
        key = (di.get(r.d_utc, -1), r.b_utc, r.coin); fl.append(FLAG[f'v{k}'].get(key, np.nan) if key in FLAG.index else np.nan)
    fl = np.array(fl, float); okm = np.isfinite(fl); v = okm & (fl > 0.5); nv = okm & (fl < 0.5)
    ev_ = lambda m: (Bf.pnl.values[m].sum() / Bf.coste.values[m].sum()) if m.sum() and Bf.coste.values[m].sum() > 0 else np.nan
    txt.append(f"{NM[k]}: fills evaluables {int(okm.sum())}/215 | viables {int(v.sum())} (EV pond. {ev_(v):+.3f}, pnl {Bf.pnl.values[v].sum():+.2f}) | no viables {int(nv.sum())} (EV pond. {ev_(nv):+.3f}, pnl {Bf.pnl.values[nv].sum():+.2f}) | sin dato {int((~okm).sum())}"); RES.setdefault('B_real', {})[k] = dict(eval=int(okm.sum()), viables=int(v.sum()), ev_v=ev_(v), pnl_v=float(Bf.pnl.values[v].sum()), no_viables=int(nv.sum()), ev_nv=ev_(nv), pnl_nv=float(Bf.pnl.values[nv].sum()))
prim = RES['PRIMARIO tipo B, todo T, todos los terciles']; nc = sum(1 for k in prim if prim[k].get('cumple_gate'))
txt += ['', f"RESUMEN: {nc}/4 conductores cumplen el gate en el PRIMARIO; " + '; '.join(f"{NM[k]} -> {prim[k].get('etiqueta', 'sin datos')}" for k in (1, 2, 3, 4)) + ('' if COMPLETO else ' | PARTIAL: faltan dias de poblacion'),
        f'Tiempo {time.time() - t0:.0f} s. Limites: poblacion censurada (fills ajenos), conductor D4 solo evaluable desde ~29-Oct (necesita 10 dias de historia del propio conductor), 215 fills de B = 4 dias R1 (descriptivo), unidades parciales de bloque en dias FAILED.']
write(EXP + 'E5_regimen.txt', txt); json.dump(RES, open(EXP + 'E5_regimen.json', 'w'), default=float, indent=1); estado_fase('E5', 'COMPLETE' if COMPLETO else 'PARTIAL', conductores_ok=nc); print('\n'.join(txt))
