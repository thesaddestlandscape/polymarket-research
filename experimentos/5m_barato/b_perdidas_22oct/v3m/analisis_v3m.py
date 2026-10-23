#!/usr/bin/env python3
"""analisis_v3m.py -- contraste PREREG_V3_PUERTA_v2 (sha256 en prereg_v2/PREREG_V3_PUERTA_v2.sha256): H-V (vetar mercados con
spread de la 1.a cotizacion > 0,02) y H-F (favorables: spread_puerta = 0,01) en I5 (simv3m 09-16 Oct) e I6 (poblacion con puerta).
Secundarios: R0 (17-21), I6 17-21, sensibilidades. Solo lectura. Salida: v3m/resultados_v3m.json, v3m/salida_v3m.txt."""
import os, sys, json, glob, hashlib
os.environ.setdefault('PYTHONDONTWRITEBYTECODE', '1'); sys.dont_write_bytecode = True
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); B = '/root/polymarket-research/experimentos/5m_barato'
PRE = B + '/b_perdidas_22oct/prereg_v2/PREREG_V3_PUERTA_v2'; V = '/root/polymarket-research-datalogs/v3m_puerta/'
sys.path.insert(0, B + '/b_perdidas_22oct/contraste'); import v9v3_lib as lib
SEED = 20261023; REPS = 2000; ALFA = 0.05 / 4; TK = 295 - 5 * np.arange(47)
OUT = []
def P(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); OUT.append(s)
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
ok = open(PRE + '.sha256').read().split()[0] == sha(PRE + '.md'); P('PREREG v2 hash coincide:', ok)
if not ok: sys.exit('PREREG modificado')
OOS = [f'2026-10-{d:02d}' for d in range(9, 17)]; DISC = [f'2026-10-{d:02d}' for d in range(17, 22)]
INPUTS = {}
# ------------------------------------------------------------------ mercados (I5) desde simv3m
def mercados(days, src='v3m'):
    rows = []; cover = {}
    for d in days:
        f = (V + f'simv3m_{d}.npz') if src == 'v3m' else (B + f'/b_seleccion_adversa/datos/simv2/simv2_{d}.npz')
        INPUTS[f] = sha(f); z = np.load(f, allow_pickle=True); M = len(z['mkt']); ar = np.arange(M)
        p = z['p']; valid = np.isfinite(p); quoted = valid.any(1); kq = valid.argmax(1)
        spr = np.round(z['ba'].astype(float) - z['bb'].astype(float), 2); s1 = spr[ar, kq]
        fill = valid & (z['minpc'] < p - 1e-9); filled = fill.any(1); kf = fill.argmax(1); pf = np.where(filled, p[ar, kf], np.nan)
        df = pd.DataFrame(dict(dia=z['dia'], act=z['act'], mkt=z['mkt'].astype(np.int64), fin=z['fin'].astype(np.int64), side=z['side'], win=z['win'].astype(bool),
                               quoted=quoted, kq=kq, s1=s1, t_puerta=z['fin'].astype(float) - TK[kq], filled=filled, kf=kf, pf=pf))
        rows.append(df); cover[d] = dict(simulados=int(M), cotizados=int(quoted.sum()), frac_864=round(M / 864, 4), s1_nan=int((quoted & ~np.isfinite(s1)).sum()))
    D = pd.concat(rows, ignore_index=True)
    # higiene (desviacion declarada): un mercado que cierra justo tras medianoche aparece en 2 ficheros de dia; se conserva la fila del dia
    # de su ventana (fecha UTC de cierre-300 s). Afecta a <=1 mercado por tramo; se reporta cuantos.
    dwin = pd.to_datetime(D.fin - 300, unit='s', utc=True).dt.strftime('%Y-%m-%d'); dup = D.mkt.duplicated(keep=False)
    ndup = int(dup.sum()); D = D[~dup | (D.dia == dwin)].drop_duplicates('mkt', keep='first'); cover['_duplicados_eliminados'] = ndup - int(dup.sum() and 0)
    D = D[D.quoted].copy()
    D['veto'] = D.s1 > 0.025; D['fav'] = D.s1 <= 0.015
    D['estrato'] = D.dia + '_' + D.act + '_' + ((D.fin % 86400) // 21600).astype(str); D['cierre'] = D.fin
    return D, cover
# ------------------------------------------------------------------ placebo por etiqueta de MERCADO dentro de estrato
def perm_labels(lab, strat, rng):
    so = np.argsort(strat, kind='stable'); o = np.lexsort((rng.random(len(lab)), strat)); new = np.empty_like(lab); new[so] = lab[o]; return new
def stats(pnl, cost, v, dia, days):
    pv = pnl[v].sum(); cv = cost[v].sum(); pr = pnl[~v].sum(); cr = cost[~v].sum()
    d = (pr / cr - pv / cv) if cv > 0 and cr > 0 else np.nan
    nd = np.array([-pnl[v & (dia == x)].sum() for x in days])
    return d, -pv, nd
def evaluar(name, U, mk, lab_col, days, reps=REPS, rng=None):
    """U: filas (rellenos o unidades) con dia, cierre, mkt, pnl, cost. mk: mercados con estrato y etiqueta lab_col (True = 'vetado').
    Devuelve dict con estadisticos, IC y placebo por etiqueta de mercado."""
    U = U.copy(); lab = mk.set_index('mkt')[lab_col]; U['veto'] = U.mkt.map(lab).astype(bool).values
    t = lib.summarize(name, U[['dia', 'cierre', 'pnl', 'cost', 'veto']], None, rng, reps=0)
    # delta sin 2 mejores dias de Delta
    pdd = {k: v['delta'] for k, v in t['por_dia'].items() if v['delta'] is not None}
    best2 = sorted(pdd, key=lambda k: -pdd[k])[:2]; Ux = U[~U.dia.isin(best2)]
    t['delta_sin2'] = float(Ux[~Ux.veto].pnl.sum() / Ux[~Ux.veto].cost.sum() - Ux[Ux.veto].pnl.sum() / Ux[Ux.veto].cost.sum()) if Ux.veto.any() else None
    # placebo
    mlab = mk[lab_col].values.astype(bool); strat = pd.factorize(mk.estrato)[0]; pos = U.mkt.map(pd.Series(np.arange(len(mk)), index=mk.mkt.values)).values
    pnl, cost, dia = U.pnl.values, U.cost.values, U.dia.values
    d0, n0, nd0 = stats(pnl, cost, U.veto.values, dia, days)
    PD = np.empty(reps); PN = np.empty(reps); PND = np.empty((reps, len(days)))
    for r in range(reps):
        nl = perm_labels(mlab, strat, rng); v = nl[pos]; PD[r], PN[r], PND[r] = stats(pnl, cost, v, dia, days)
    t['placebo'] = dict(delta_media=float(np.nanmean(PD)), p_delta=float((np.sum(PD >= d0 - 1e-12) + 1) / (reps + 1)), neto_media=float(PN.mean()), p_neto=float((np.sum(PN >= n0 - 1e-9) + 1) / (reps + 1)),
                        neto_sobre_placebo=float(n0 - PN.mean()))
    best2n = np.argsort(-nd0)[:2]; keep = np.setdiff1d(np.arange(len(days)), best2n)
    t['placebo']['neto_sobre_placebo_sin2'] = float(nd0[keep].sum() - PND[:, keep].sum(1).mean())
    t['n_mercados_vetados'] = int(U[U.veto].mkt.nunique()); t['n_mercados'] = int(U.mkt.nunique())
    return t
def show(name, t):
    f = lambda x: 'na' if x is None or (isinstance(x, float) and np.isnan(x)) else f'{x:+.3f}'
    P(f"--- {name}: n={t['n']} vetados={t['nv']} ({t['share_veto']:.1%}) en {t['n_mercados_vetados']}/{t['n_mercados']} mercados | retiene {t['share_cost_kept']:.1%} EUR")
    P(f"    EV base {f(t['ev_all'])} | EV retenido {f(t['ev_r'])} | EV vetado {f(t['ev_v'])} | Delta {f(t['delta'])} (sin 2 mejores dias {f(t['delta_sin2'])}) | neto {t['net']:+.2f} EUR")
    P(f"    IC90 Delta dia ({t['ic90_dia_delta'][0]:+.3f},{t['ic90_dia_delta'][1]:+.3f}) cierre ({t['ic90_cierre_delta'][0]:+.3f},{t['ic90_cierre_delta'][1]:+.3f}) n_cierres={t['n_cierres']} | IC90 neto dia ({t['ic90_dia_net'][0]:+.1f},{t['ic90_dia_net'][1]:+.1f})")
    pl = t['placebo']; P(f"    placebo (etiqueta de mercado barajada en dia-moneda-6h): Delta medio {pl['delta_media']:+.3f} p={pl['p_delta']:.4f} | neto medio {pl['neto_media']:+.1f} p={pl['p_neto']:.4f} | neto-placebo {pl['neto_sobre_placebo']:+.1f} (sin 2 mejores dias {pl['neto_sobre_placebo_sin2']:+.1f})")
    P(f"    dias Delta>0: {t['dias_delta_pos']}/{t['dias']} | por dia: " + ' '.join(f"{k[-5:]}:D{('na' if v['delta'] is None else format(v['delta'], '+.2f'))}/net{v['net']:+.1f}/v{v['nv']}/n{v['n']}" for k, v in t['por_dia'].items()))
def i5_fills(D):
    F = D[D.filled].copy(); F['pnl'] = 5 * (F.win.astype(float) - F.pf); F['cost'] = 5 * F.pf; return F
def ev_abs(F, rng):
    a = F.groupby('dia')[['pnl', 'cost']].sum().values; c = F.groupby('cierre')[['pnl', 'cost']].sum().values
    def b(a):
        idx = rng.integers(0, len(a), (REPS, len(a))); s = a[idx].sum(1); q = s[:, 0] / s[:, 1]; return float(np.quantile(q, .05)), float(np.quantile(q, .95))
    return dict(n=int(len(F)), ev=float(F.pnl.sum() / F.cost.sum()), ic90_dia=b(a), ic90_cierre=b(c), dias=int(F.dia.nunique()))
RES = {}; rng = np.random.default_rng(SEED)
# ================================================================== R0 (17-21): simv3m vs simv2 original
P('\n===== R0 reproduccion 17-21 Oct'); RES['R0_celdas'] = json.load(open(HERE + '/r0_check.json'))
for d, v in RES['R0_celdas'].items(): P(' ', d, v)
for src in ('orig', 'v3m'):
    Dd, _ = mercados(DISC, src); Fd = i5_fills(Dd)
    t = evaluar(f'R0 {src}', Fd, Dd, 'veto', DISC, reps=500, rng=rng); show(f'I3/R0 puerta de mercado 17-21 ({src})', t); RES[f'R0_{src}'] = t
# ================================================================== I5 primario 09-16
P('\n===== I5 simv3m OOS 09-16 Oct (PRIMARIO)')
D5, cov5 = mercados(OOS); RES['I5_cobertura'] = cov5; P('cobertura:', cov5)
F5 = i5_fills(D5); P(f"mercados cotizados {len(D5)} rellenos {len(F5)} (tasa {len(F5)/len(D5):.3f}) EV base {F5.pnl.sum()/F5.cost.sum():+.3f}; vetados {int(D5.veto.sum())} mercados ({D5.veto.mean():.1%}); favorables {int(D5.fav.sum())} ({D5.fav.mean():.1%}); s1 NaN {int(D5.s1.isna().sum())}")
P('    distribucion spread_puerta (mercados):', D5.s1.round(2).value_counts().sort_index().head(12).to_dict())
t = evaluar('I5 H-V', F5, D5, 'veto', OOS, rng=rng); show('I5 H-V (vetar puerta > 0,02)', t); RES['I5_HV'] = t
# cambio de PnL re-simulado (= particion: la puerta es de mercado) y EV retenido vs base
RES['I5_HV']['euros'] = dict(cambio_pnl=float(-F5[F5.mkt.isin(D5[D5.veto].mkt)].pnl.sum()), ev_base=t['ev_all'], ev_retenido=t['ev_r'])
D5['nofav'] = ~D5.fav
t = evaluar('I5 H-F', F5, D5, 'nofav', OOS, rng=rng); show('I5 H-F (DeltaF = EV(favorables=0,01) - EV(resto))', t); RES['I5_HF'] = t
RES['I5_HF']['ev_favorables'] = ev_abs(F5[F5.mkt.isin(D5[D5.fav].mkt)], rng); P('    EV favorables absoluto:', RES['I5_HF']['ev_favorables'])
# acierto y relleno por grupo (pujas cotizadas)
for lab, m in (('puerta<=0,02', ~D5.veto), ('puerta>0,02', D5.veto), ('puerta=0,01', D5.fav)):
    g = D5[m]; P(f"    cotizadas {lab}: n={len(g)} rellenan {g.filled.mean():.3f} acierto todas {g.win.mean():.3f} acierto rellenadas {g[g.filled].win.mean():.3f} no rellenadas {g[~g.filled].win.mean():.3f}")
# por moneda (sensibilidad)
for a in ('ETH', 'SOL', 'XRP'):
    Fa = F5[F5.act == a]; v = Fa.mkt.isin(D5[D5.veto].mkt)
    if v.any() and (~v).any(): P(f"    I5 {a}: n={len(Fa)} vetados {int(v.sum())} Delta {Fa[~v].pnl.sum()/Fa[~v].cost.sum() - Fa[v].pnl.sum()/Fa[v].cost.sum():+.3f} neto {-Fa[v].pnl.sum():+.1f}")
# ================================================================== I6 poblacion con puerta
P('\n===== I6 poblacion (otros makers) con etiqueta de puerta de MERCADO')
def poblacion(days, D, restr_t=True, mismo_lado=True):
    uf = [B + f'/b_seleccion_adversa/datos/units/units_{d}.pkl' for d in days]
    for f in uf: INPUTS[f] = sha(f)
    U = pd.concat([pd.read_pickle(f)[['dia', 'maker', 'mkt', 'lado_c', 'act', 'c', 'p', 'fin', 'ts', 'gana']] for f in uf], ignore_index=True)
    n0 = len(U); U = U[U.gana.notna()]; n_des = len(U)
    m = D.set_index('mkt'); U = U[U.mkt.isin(m.index)].copy(); n_mk = len(U)
    side = U.mkt.map(m.side); tp = U.mkt.map(m.t_puerta)
    if mismo_lado: U = U[(U.lado_c == 'YES') == (side > 0)]
    n_lado = len(U)
    if restr_t: U = U[U.ts - 2.4 >= U.mkt.map(m.t_puerta)]
    U = U.rename(columns={'p': 'pnl', 'c': 'cost'}); U['cierre'] = U.fin.astype(np.int64)
    return U, dict(unidades=n0, con_desenlace=n_des, en_mercado_con_puerta=n_mk, mismo_lado=n_lado, tras_t_puerta=len(U))
U6, c6 = poblacion(OOS, D5); RES['I6_cobertura'] = c6; P('filtros I6 09-16:', c6, '| EV', round(U6.pnl.sum() / U6.cost.sum(), 4), 'makers', U6.maker.nunique())
t = evaluar('I6 H-V', U6, D5, 'veto', OOS, rng=rng); show('I6 H-V 09-16 (PRIMARIO)', t); RES['I6_HV'] = t
t = evaluar('I6 H-F', U6, D5, 'nofav', OOS, rng=rng); show('I6 H-F 09-16 (DeltaF)', t); RES['I6_HF'] = t
# secundarios
P('\n===== SECUNDARIOS (no deciden)')
Dd, _ = mercados(DISC); Dd['nofav'] = ~Dd.fav
U6d, c6d = poblacion(DISC, Dd); P('filtros I6 17-21:', c6d)
t = evaluar('I6 H-V 17-21', U6d, Dd, 'veto', DISC, reps=500, rng=rng); show('I6 H-V 17-21 (solapado con descubrimiento)', t); RES['I6_HV_17_21'] = t
U6s, _ = poblacion(OOS, D5, restr_t=False); t = evaluar('I6 sens', U6s, D5, 'veto', OOS, reps=500, rng=rng); show('I6 H-V 09-16 sin restriccion de hora', t); RES['I6_HV_sin_t'] = t
U6b, _ = poblacion(OOS, D5, restr_t=False, mismo_lado=False); t = evaluar('I6 sens2', U6b, D5, 'veto', OOS, reps=500, rng=rng); show('I6 H-V 09-16 ambos lados, sin hora', t); RES['I6_HV_ambos'] = t
D13, _ = mercados(OOS + DISC); F13 = i5_fills(D13); t = evaluar('I5 13d', F13, D13, 'veto', OOS + DISC, reps=500, rng=rng); show('I5+I3 13 dias (09-21) H-V', t); RES['I5_HV_13d'] = t
# ================================================================== GATES
P('\n===== GATES (PREREG v2 §4-§5)')
def gHV(t, inst):
    g = {}; pl = t['placebo']
    g['G1'] = bool(t['delta'] > 0 and t['ic90_dia_delta'][0] > 0); g['G2'] = bool(t['ic90_cierre_delta'][0] > 0)
    g['G3'] = bool(pl['p_delta'] <= ALFA and pl['p_neto'] <= ALFA and pl['neto_sobre_placebo'] > 0)
    g['G4'] = bool(t['dias_delta_pos'] >= 6 and (t['delta_sin2'] or -1) > 0 and pl['neto_sobre_placebo_sin2'] > 0)
    g['G5'] = bool(t['share_veto'] <= 0.5 and t['share_cost_kept'] >= 0.4)
    g['G6'] = bool((t['n'] >= 2000 and t['nv'] >= 300) if inst == 'I5' else (t['n'] >= 5000 and t['nv'] >= 500 and t['n_mercados_vetados'] >= 300))
    if inst == 'I5': g['G7'] = bool(t['euros']['cambio_pnl'] > 0 and t['ev_r'] > t['ev_all'])
    return g
g5, g6 = gHV(RES['I5_HV'], 'I5'), gHV(RES['I6_HV'], 'I6')
ref = any(t['delta'] <= 0 or t['ic90_dia_delta'][1] < 0 for t in (RES['I5_HV'], RES['I6_HV'])) or RES['I5_HV']['placebo']['neto_sobre_placebo'] <= 0
r0ok = all(v['frac_comunes'] >= .99 and v['celdas_p_iguales'] >= .99 and v['mercados_mismo_spread_puerta'] >= .99 and v['celdas_minpc_iguales'] >= .99 for v in RES['R0_celdas'].values()) and abs(RES['R0_v3m']['delta'] - 0.129) <= 0.01
cov_ok = all(v['frac_864'] >= 0.9 for k, v in cov5.items() if not k.startswith('_'))
hv = 'DATA_BLOCKED' if not r0ok else ('CONFIRMADA' if all(g5.values()) and all(g6.values()) else ('REFUTADA' if ref else 'NO CONCLUYENTE'))
tF5, tF6 = RES['I5_HF'], RES['I6_HF']; evf = tF5['ev_favorables']
gF = dict(I5_ev_fav_pos=bool(evf['ev'] > 0 and evf['ic90_dia'][0] > 0 and evf['ic90_cierre'][0] > 0), I5_deltaF=bool(tF5['delta'] > 0 and tF5['placebo']['p_delta'] <= ALFA),
          I6_deltaF=bool(tF6['delta'] > 0 and tF6['ic90_dia_delta'][0] > 0), n=bool(evf['n'] >= 300 and tF6['nv'] < tF6['n'] and (tF6['n'] - tF6['nv']) >= 1000))
refF = tF5['delta'] <= 0 or tF6['delta'] <= 0 or evf['ic90_dia'][1] < 0
hf = 'DATA_BLOCKED' if not r0ok else ('CONFIRMADA' if all(gF.values()) else ('REFUTADA' if refF else 'NO CONCLUYENTE'))
RES['VEREDICTOS'] = dict(R0_ok=r0ok, cobertura_ok=cov_ok, HV=dict(I5=g5, I6=g6, veredicto=hv), HF=dict(gates=gF, veredicto=hf), alfa=ALFA)
P(json.dumps(RES['VEREDICTOS'], indent=1, default=lambda o: (o.item() if hasattr(o, 'item') else str(o))))
json.dump(RES, open(HERE + '/resultados_v3m.json', 'w'), indent=1, default=lambda o: (None if (isinstance(o, float) and np.isnan(o)) else (o.item() if hasattr(o, 'item') else str(o))))
json.dump(dict(script_sha256=sha(__file__), prereg_sha256=open(PRE + '.sha256').read().split()[0], seed=SEED, reps=REPS, alfa=ALFA, inputs=INPUTS, status='COMPLETE'), open(HERE + '/run_manifest_v3m.json', 'w'), indent=1)
open(HERE + '/salida_v3m.txt', 'w').write('\n'.join(OUT) + '\n')
