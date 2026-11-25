#!/usr/bin/env python3
"""COPIA VERSIONADA F5-V4 (17-Nov): own_D de verif_real/out_v4, salidas en f5_v4_17nov/ (exp1/ intacto). E1 (ADDENDUM1_B_F5): B real 20-23 Oct con sello v3 (tm3 de own_D.pkl, C1) y F5(l_ef) a t_dec = tm3 + delta - l_ef - d_proc (C4); tabla viejo (t_fill libro5) vs v3; sens d_proc/delta; solo-`sig` y
estabilidad de etiqueta por rama (C6); incondicional por orden (C8); placebo e inversion (C9). Asserts abortan (C10). Escribe exp1/E1_B_real_v3.{txt,json} y exp1/B_fills_v3.pkl. nice 19; <0,5 GB; ~20 s."""
import os, sys; sys.path.insert(0, '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/exp1'); HERE4 = os.path.dirname(os.path.abspath(__file__)) + '/'
from lib1 import *
OWN = L2 + 'verif_real/out_v4/own_2026-10-%d.pkl'
F = pd.read_pickle(AQ + 'B_fills.pkl'); O = pd.read_pickle(AQ + 'B_ordenes.pkl')
own = pd.concat([pd.read_pickle(OWN % d) for d in (20, 21, 22, 23)], ignore_index=True)
assert not own.duplicated(['tx', 'token_id']).any(), 'own_D duplicado'
M = F.merge(own[['tx', 'token_id', 'tm3', 'rama']], left_on=['tx', 'tok_x'], right_on=['tx', 'token_id'], how='left', validate='many_to_one').drop(columns='token_id')
assert len(M) == 215 and M.tm3.notna().all(), f'C1 join {len(M)} {int(M.tm3.notna().sum())}'
cnt = M.rama.value_counts().to_dict(); assert cnt == {'sig': 163, 'amb': 24, 'sinev': 17, 'nosig': 6, 'guard': 5}, cnt
M['tm3'] = M.tm3.astype('int64'); M = M.rename(columns={'t_fill': 't_fill_OLD'})                       # el sello viejo NO se usa en ningun calculo v3 (C1)
dd = (M.tm3 - M.t_fill_OLD).values; p5, p50, p95 = np.percentile(dd, [5, 50, 95]); assert abs(p50 + 68) <= 5, f'C10 p50 {p50}'
M['epoca'] = epoca(M.tm3.values); assert (M.epoca == 'R1').all(), 'C3: B real debe ser 100 % R1'
assert M.gana.notna().all() and (M.gana.isin([0, 1])).all(), 'C7: gana'
M['pnl'] = M['size'] * (M.gana - M.precio); M['coste'] = M['size'] * M.precio
txt = [f'# E1 B real con sello v3 (ADDENDUM1 sha {ADD_SHA[:8]}); 215 fills, {M.mkt_lado.nunique()} unidades mercado-lado, {M.cierre.nunique()} cierres, dias {sorted(M.dia.unique())}; epoca 100 % R1',
       f'C1 OK: join own_D 215/215; ramas {cnt}. C10: tm3 - t_fill(libro5 viejo) p5/p50/p95 = {p5:.0f}/{p50:.0f}/{p95:.0f} ms (|d|>50 ms en {100*np.mean(np.abs(dd) > 50):.1f} % de los fills; integridad: -236/-68/-58)',
       f'Cobertura desenlace C7: gana notna 215/215 = 1,000. EV pond. total {ev(M.pnl, M.coste):+.4f}; PnL {M.pnl.sum():+.2f} EUR sobre {M.coste.sum():.2f} EUR.']
# ---------------- features F5(l) a t_dec con tm3
SB = [s for s in specs() if not s[0].startswith('c')]          # c (poblacion) no aplica: tm3 ya es el sello
X = pd.DataFrame(index=M.index); NANI = {}; QD = {}
for d, g in M.groupby('dia'):
    Qd, nn = leeq(MIT + f'q_{d}.gz', set(g.tid.unique())); QD[d] = Q(Qd.id.values, Qd.r.values, Qd.b.values, Qd.a.values, Qd.tb.values, Qd.ta.values)
    NANI[d] = dict(filas_q_tokens_de_B=int(len(Qd)), filas_con_ask_o_tamano_vacio=nn)
    for (nm, c, l, dp, dm) in SB:
        f5, bid, cat, _ = QD[d].feat(g.tid.values, t_dec(g.tm3.values, l, dp, dm))
        for k, v in (('F5_', f5), ('bid_', bid), ('cat_', cat)): X.loc[g.index, k + nm] = v
M = pd.concat([M, X], axis=1)
for nm, *_ in SB: M['ter_' + nm] = lab(M['F5_' + nm].values)
txt += ['', f'C5 (dropna): filas q con ask/tamano vacio por dia (el extractor viejo las descartaba y conservaba el estado anterior): {NANI}',
        'Categorias de estado en el primario p60: ' + str({CATN[k]: int((M['cat_p60'] == k).sum()) for k in range(4)}) + ' (NaN = categoria `nan`, no se descarta)']
def unidades(M, col):
    Ms = M.sort_values(['tm3', 'logidx_fill']); first = Ms.drop_duplicates('mkt_lado', keep='first').set_index('mkt_lado')        # primer fill (incluye NaN: sin skipna)
    agg = Ms.groupby('mkt_lado').agg(pnl=('pnl', 'sum'), coste=('coste', 'sum')); U = agg.join(first[['dia', 'coin', 'cierre', 'rama', col]]); U['cl'] = U.cierre; U['ter'] = lab(U[col].values); return U.reset_index()
RES = {}
def bloque(nombre, U, placebo=False):
    L, o = resumen(U, nombre); g, lo, hi, sd = boot_grad(U); o['grad_bajo_alto'] = dict(g=g, ic90=(lo, hi), sd=sd, n_req_unidades=n_req(len(U), g, sd))
    L.append(f'   gradiente bajo-alto = {g:+.3f}  IC90 cierre ({lo:+.3f},{hi:+.3f})  n_unidades requeridas para IC90>0 con este efecto: {o["grad_bajo_alto"]["n_req_unidades"]:.0f}')
    if placebo:
        P = placebo_multi(U, ['G1', 'G2'], ['dia'], B=2000)
        for r in ('G1', 'G2'): L.append(f'   placebo {r} (permutar tercil dentro de dia, 2000): DeltaEV obs {P[r][0]:+.3f}, media placebo {P[r][2]:+.3f}, p={P[r][1]:.3f}'); o[r]['placebo_p'] = P[r][1]
    txt.extend(L); RES[nombre] = o; return o
txt += ['', '# TABLA viejo (sello libro5 t_fill, F5 a t_fill-100/250) vs v3 (tm3, F5 a tm3+delta-l_ef-d_proc; delta=0, d_proc=3)']
bloque('OLD F5@t_fill-100 (NO VALIDADO)', unidades(M, 'F5_100')); bloque('OLD F5@t_fill-250 (NO VALIDADO)', unidades(M, 'F5_250'))
for l in LS: bloque(f'v3 l_ef={l} (todas las ramas)', unidades(M, f'F5_p{l}'), placebo=(l in (35, 60)))
txt += ['', '# Sensibilidades DESCRIPTIVAS (no deciden): d_proc 10/30 y delta -suelo/+suelo (l_ef 35 y 60)']
for l in (35, 60):
    for nm, et in ((f'd10_{l}', 'd_proc=10'), (f'd30_{l}', 'd_proc=30'), (f'dm_{l}', 'delta=-suelo(39,5)'), (f'dp_{l}', 'delta=+suelo (NO decide)')): bloque(f'v3 l_ef={l} {et}', unidades(M, 'F5_' + nm))
txt += ['', '# C6: solo rama `sig` (n=163 fills)']
Ms = M[M.rama == 'sig']
for l in (35, 60): bloque(f'v3 l_ef={l} SOLO sig', unidades(Ms, f'F5_p{l}'))
# estabilidad de etiqueta (operacionalizacion de C6 fijada al implementar, antes de ver resultados): perturbar tm3 por rama y contar cambios de tercil en l_ef=60
PERT = {'sig': (-5, 5), 'amb': (-57, 3), 'nosig': (-57, 3), 'guard': (-57, 3), 'sinev': (-750, 750)}
base = M['ter_p60'].values; ch = np.zeros(len(M), bool)
for d, g in M.groupby('dia'):
    for rama, sh in PERT.items():
        gr = g[g.rama == rama]
        for s in sh:
            if len(gr) == 0: continue
            f5, _, _, _ = QD[d].feat(gr.tid.values, t_dec(gr.tm3.values + s, 60, 3, 0)); ch[M.index.get_indexer(gr.index)] |= (lab(f5) != base[M.index.get_indexer(gr.index)])
tasa = float(ch.mean()); por_rama = {r: (round(float(ch[(M.rama == r).values].mean()), 3), int((M.rama == r).sum())) for r in PERT}
txt += ['', f'C6 estabilidad de etiqueta (l_ef=60; tm3 perturbado: sig +-5 ms; amb/nosig/guard -57/+3 ms (d_ex p95 76 ms vs c~19); sinev +-750 ms): fills con tercil distinto = {100*tasa:.1f} % del total (criterio: >20 % => INSUFFICIENT); por rama (tasa, n): {por_rama}',
        'Cruce tercil viejo F5@t_fill-100 vs v3 l_ef=35 (fills): ' + pd.crosstab(M.ter_100, M.ter_p35).to_string().replace('\n', ' | '), 'Cruce viejo F5@t_fill-100 vs v3 l_ef=100: ' + pd.crosstab(M.ter_100, M.ter_p100).to_string().replace('\n', ' | ')]
RES['C6'] = dict(tasa_cambio=tasa, por_rama=por_rama, criterio_insufficient=bool(tasa > 0.20))
# por dia (primario l_ef=60)
U = unidades(M, 'F5_p60'); by = U.groupby('dia').apply(lambda d: pd.Series({'n': len(d), 'EV_todo': ev(d.pnl, d.coste), 'EV_bajo': ev(d.pnl[d.ter == 'bajo'], d.coste[d.ter == 'bajo']), 'EV_medio': ev(d.pnl[d.ter == 'medio'], d.coste[d.ter == 'medio']), 'EV_alto': ev(d.pnl[d.ter == 'alto'], d.coste[d.ter == 'alto'])}), include_groups=False)
txt += ['', '# Por dia (v3 l_ef=60, EV pond.):', by.round(3).to_string()]
gd = (by.EV_bajo - by.EV_alto).dropna(); RES['dias_bajo_menos_alto_p60'] = dict(pos=int((gd > 0).sum()), n=int(len(gd)), vals=gd.round(3).to_dict())
# ---------------- incondicional por orden (C8): 3.796 ordenes, coste_pot = size*precio de TODAS
O['exp'] = O['size'] * O.precio; O['pnl'] = O.pnl.fillna(0.0).astype(float); O['coste'] = O.coste.fillna(0.0).astype(float)
assert O.exp.sum() >= O.coste.sum() - 1e-9, 'C8: sum(coste_pot) < sum(coste_relleno)'
t = O.groupby('ter_post').agg(ordenes=('oid', 'size'), rellenadas=('relleno', 'sum'), coste=('coste', 'sum'), pnl=('pnl', 'sum'), exposicion=('exp', 'sum')); t['P_fill'] = t.rellenadas / t.ordenes
t['EV_pond_relleno'] = t.pnl / t.coste; t['EV_incond_por_EUR_expuesto'] = t.pnl / t.exposicion; t['pnl_por_orden'] = t.pnl / t.ordenes
txt += ['', f'# C8 incondicional por orden ({len(O)} ordenes; sum coste_pot {O.exp.sum():.1f} >= sum coste_relleno {O.coste.sum():.1f}): F5_post (ledger, en la decision de colocacion; NO depende del sello del fill)', t.round(4).to_string(),
        f'Total: P(fill) {O.relleno.mean():.4f}; EV|fill pond. {O.pnl.sum()/O.coste.sum():+.4f}; EV incondicional por EUR expuesto {O.pnl.sum()/O.exp.sum():+.4f}; P(fill) x EV|fill = {O.relleno.mean()*O.pnl.sum()/O.coste.sum():+.5f}']
RES['incondicional'] = dict(total_exposicion=float(O.exp.sum()), coste_relleno=float(O.coste.sum()), pnl=float(O.pnl.sum()), p_fill=float(O.relleno.mean()), tabla=t.round(5).reset_index().to_dict('records'))
write(HERE4 + 'E1_B_real_v4.txt', txt); json.dump(RES, open(HERE4 + 'E1_B_real_v4.json', 'w'), default=float, indent=1); M.to_pickle(HERE4 + 'B_fills_v4.pkl')
pass
print('\n'.join(txt))
