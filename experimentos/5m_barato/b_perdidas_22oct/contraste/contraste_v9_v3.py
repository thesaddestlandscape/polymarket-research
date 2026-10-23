#!/usr/bin/env python3
"""contraste_v9_v3.py -- contraste de V9 y V3 segun prereg/PREREG_V9_V3.md (sha256 en PREREG_V9_V3.sha256). SOLO LECTURA de produccion.
Instrumentos: I1 B real (pos_anotado2.csv + ledger), I2 cinta (datos/sim), I3 simv2 (libro real), I4 poblacion (units / ms_units).
Salida: contraste/resultados.json, contraste/salida.txt (stdout), contraste/run_manifest.json.
Uso: nice -n 19 ionice -c3 python3 contraste_v9_v3.py   (ulimit -v 3000000)"""
import os, sys, json, glob, hashlib, time, datetime as dt
os.environ.setdefault('PYTHONDONTWRITEBYTECODE', '1'); sys.dont_write_bytecode = True
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__))
R = '/root/polymarket-research/experimentos/5m_barato'
SA = R + '/b_seleccion_adversa'; AN = R + '/b_perdidas_22oct/anatomia'; PRE = R + '/b_perdidas_22oct/prereg'
sys.path.insert(0, SA + '/scripts'); sys.path.insert(0, HERE)
import sa_sim                                   # solo run/load/dB; importa numpy/pandas
SEED = 20261022
EPS = 1e-9; TKV = 295 - 5 * np.arange(47)
T0 = time.time(); OUTS = []
def P(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); OUTS.append(s)
def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for ch in iter(lambda: f.read(1 << 20), b''): h.update(ch)
    return h.hexdigest()
# ---------------------------------------------------------------- verificacion del preregistro
okp = open(PRE + '/PREREG_V9_V3.sha256').read().split()[0] == sha(PRE + '/PREREG_V9_V3.md')
P('PREREG hash coincide:', okp)
if not okp: sys.exit('PREREG modificado: abortar')
INPUTS = {}
def reg(p): INPUTS[p.replace(R + '/', '')] = sha(p); return p
from v9v3_lib import *
import v9v3_lib as lib
def show(name, t):
    P(f"--- {name}: n={t['n']} vetados={t['nv']} ({t['share_veto']:.1%}) coste={t['cost']:.1f} coste_vetado={t['cost_v']:.1f} retiene {t['share_cost_kept']:.1%} del coste")
    f = lambda x: 'na' if x is None or (isinstance(x, float) and np.isnan(x)) else f'{x:+.3f}'
    P(f"    EV_todos {f(t['ev_all'])} | EV_retenido {f(t['ev_r'])} EV_vetado {f(t['ev_v'])} Delta {f(t['delta'])} | neto {t['net']:+.2f} (sin 2 mejores dias {t['net_sin2']:+.2f})")
    P(f"    IC90 Delta por dia ({t['ic90_dia_delta'][0]:+.3f},{t['ic90_dia_delta'][1]:+.3f}) por cierre ({t['ic90_cierre_delta'][0]:+.3f},{t['ic90_cierre_delta'][1]:+.3f}) n_cierres={t['n_cierres']} | IC90 neto por dia ({t['ic90_dia_net'][0]:+.2f},{t['ic90_dia_net'][1]:+.2f}) por cierre ({t['ic90_cierre_net'][0]:+.2f},{t['ic90_cierre_net'][1]:+.2f})")
    if 'placebo_estricto' in t: P(f"    placebo estricto: neto medio {t['placebo_estricto']['media']:+.2f} p95 {t['placebo_estricto']['p95']:+.2f} p={t['placebo_estricto']['p']:.4f} neto sobre placebo {t['placebo_estricto']['neto_sobre_placebo']:+.2f} | simple: media {t['placebo_simple']['media']:+.2f} p={t['placebo_simple']['p']:.4f}")
    P(f"    dias Delta>0: {t['dias_delta_pos']}/{t['dias']} | <=19-Oct: n={t['n_le19']} nv={t['nv_le19']} Delta {f(t['delta_le19'])} neto {('na' if t['net_le19'] is None else format(t['net_le19'], '+.2f'))}")
    P('    por dia: ' + ' '.join(f"{k[-5:]}:D{('na' if v['delta'] is None else format(v['delta'], '+.2f'))}/net{v['net']:+.1f}/v{v['nv']}" for k, v in t['por_dia'].items()))
RES = {}
rng = np.random.default_rng(SEED)
# ================================================================ I2 cinta (V9)
P('\n==================== I2 CINTA (datos/sim, 9-21 Oct) -- V9')
files = sorted(glob.glob(SA + '/datos/sim/sim_*.npz')); [reg(f) for f in files]
D2 = sa_sim.load(SA + '/datos/sim'); Rr = sa_sim.run(D2, delta=sa_sim.dB(D2), mode='cons')
Rr['side'] = D2['side']
f2 = Rr[Rr.filled].copy(); f2['pnl'] = 5 * (f2.win.astype(float) - f2.p); f2['cost'] = 5 * f2.p; f2['cierre'] = f2.fin.astype(np.int64)
q = Rr[Rr.quoted]; P(f"mercados {len(Rr)} cotizados {len(q)} rellenos {len(f2)} (tasa {len(f2)/len(q):.3f}) dias {f2.dia.nunique()} EV base {f2.pnl.sum()/f2.cost.sum():+.3f} acierto relleno {f2.win.mean():.3f}")
RES['I2_base'] = dict(mercados=len(Rr), cotizados=int(len(q)), rellenos=int(len(f2)), ev=float(f2.pnl.sum() / f2.cost.sum()), dias=sorted(f2.dia.unique().tolist()))
f2['grp'] = f2.cierre.astype(str) + '_' + f2.side.astype(str)
for dk, lab in ((2, 'primario k>=k1+2 (gap>=5 s)'), (1, 'secundario k>=k1+1')):
    f2['veto'] = lib.veto_steps(f2.grp.values, f2.k.values, dk)
    t = summarize('I2', f2[['dia', 'cierre', 'pnl', 'cost', 'veto', 'grp']].assign(grp=f2.grp.values), 'grp', rng); show(f'I2 V9 {lab}', t); RES[f'I2_V9_dk{dk}'] = t
# ================================================================ I3 simv2 (V3 y V9)
P('\n==================== I3 SIMV2 libro real (17-21 Oct) -- V3 y V9')
zs = sorted(glob.glob(SA + '/datos/simv2/simv2_*.npz')); [reg(f) for f in zs]
Z = [np.load(f, allow_pickle=True) for f in zs]; D3 = {k: np.concatenate([z[k] for z in Z]) for k in Z[0].files}; M = len(D3['mkt'])
spr = np.round((D3['ba'].astype(float) - D3['bb'].astype(float)), 2)
p3 = D3['p']; valid0 = np.isfinite(p3); win3 = D3['win'].astype(bool); ar = np.arange(M)
def run3(gate=None, sel=None):
    valid = valid0.copy()
    if gate is not None: valid &= gate
    if sel is not None: valid &= sel[:, None]
    fill = valid & (D3['minpc'] < p3 - EPS); kf = fill.argmax(1); filled = fill.any(1); quoted = valid.any(1)
    pf = np.where(filled, p3[ar, kf], np.nan)
    return filled, kf, pf, quoted
filled0, kf0, pf0, quoted0 = run3()
ix = np.flatnonzero(filled0); F3 = pd.DataFrame(dict(dia=D3['dia'][ix], act=D3['act'][ix], cierre=D3['fin'][ix].astype(np.int64), side=D3['side'][ix], k=kf0[ix], p=pf0[ix], win=win3[ix], spread=spr[ix, kf0[ix]]))
F3['pnl'] = 5 * (F3.win.astype(float) - F3.p); F3['cost'] = 5 * F3.p
P(f"mercados {M} cotizados {int(quoted0.sum())} rellenos {len(F3)} (tasa {len(F3)/quoted0.sum():.3f}) EV base {F3.pnl.sum()/F3.cost.sum():+.3f}  [referencia del informe SA para replicar: EV -0,146, tasa 0,76]  spread NaN en el paso de relleno: {int(F3.spread.isna().sum())}")
RES['I3_base'] = dict(mercados=int(M), cotizados=int(quoted0.sum()), rellenos=int(len(F3)), ev=float(F3.pnl.sum() / F3.cost.sum()), spread_nan_en_relleno=int(F3.spread.isna().sum()))
# ---- V9 sobre I3
F3['grp'] = F3.cierre.astype(str) + '_' + F3.side.astype(str)
for dk, lab in ((2, 'primario k>=k1+2'), (1, 'secundario k>=k1+1')):
    F3['veto'] = lib.veto_steps(F3.grp.values, F3.k.values, dk)
    t = summarize('I3', F3[['dia', 'cierre', 'pnl', 'cost', 'veto', 'grp']], 'grp', rng); show(f'I3 V9 {lab}', t); RES[f'I3_V9_dk{dk}'] = t
# ---- V3 particion (rellenos del base cuyo paso de relleno tiene spread > 0,02)
F3['veto'] = (F3.spread > 0.025).values; F3['grp3'] = F3.dia + '_' + F3.act
t = summarize('I3', F3[['dia', 'cierre', 'pnl', 'cost', 'veto', 'grp3']], 'grp3', rng); show('I3 V3 particion por relleno (spread en el paso de relleno > 0,02)', t); RES['I3_V3_particion'] = t
# ---- V3 re-simulado con puerta por paso
gate_step = np.where(np.isfinite(spr), spr <= 0.025, True)       # spread NaN: no se puede evaluar -> NO se veta (contado)
nan_cells = int((valid0 & ~np.isfinite(spr)).sum())
fG, kG, pG, qG = run3(gate=gate_step)
def tot(filled, pf):
    return float((5 * (win3[filled].astype(float) - pf[filled])).sum()), float((5 * pf[filled]).sum())
pnl0, c0 = tot(filled0, pf0); pnlG, cG = tot(fG, pG)
P(f"RE-SIM V3 puerta por paso: cotizados {int(qG.sum())} (base {int(quoted0.sum())}) rellenos {int(fG.sum())} (base {int(filled0.sum())}) | PnL {pnlG:+.2f} vs base {pnl0:+.2f} => cambio {pnlG-pnl0:+.2f} EUR | EV {pnlG/cG:+.3f} vs {pnl0/c0:+.3f} | celdas con spread NaN (no vetadas): {nan_cells}")
# placebo del re-sim: barajar las filas de spread entre mercados del mismo (dia, moneda)
grp_ix = pd.Series(range(M)).groupby([D3['dia'], D3['act']]).apply(lambda s: s.values).tolist()
plc = np.empty(REPS_P); prng = np.random.default_rng(SEED + 1)
for r in range(REPS_P):
    perm = np.arange(M)
    for gi in grp_ix: perm[gi] = prng.permutation(gi)
    gt = np.where(np.isfinite(spr[perm]), spr[perm] <= 0.025, True)
    fp, kp, pp_, qp = run3(gate=gt); plc[r] = tot(fp, pp_)[0] - pnl0
real_ch = pnlG - pnl0
RES['I3_V3_resim'] = dict(cotizados=int(qG.sum()), rellenos=int(fG.sum()), pnl_puerta=pnlG, pnl_base=pnl0, cambio=real_ch, ev_puerta=pnlG / cG, ev_base=pnl0 / c0, placebo_media=float(plc.mean()), placebo_p95=float(np.quantile(plc, .95)), p_placebo=float((np.sum(plc >= real_ch - 1e-9) + 1) / (REPS_P + 1)), spread_nan=nan_cells)
P(f"    placebo (filas de spread barajadas por dia-moneda): cambio medio {plc.mean():+.2f} p95 {np.quantile(plc,.95):+.2f}  p(placebo>=real)={RES['I3_V3_resim']['p_placebo']:.4f}  cambio sobre placebo {real_ch-plc.mean():+.2f}")
dias3 = sorted(set(D3['dia'].tolist())); rows = []
for d_ in dias3:
    m = D3['dia'] == d_; rows.append((d_, tot(filled0 & m, pf0)[0], tot(fG & m, pG)[0], int((filled0 & m).sum()), int((fG & m).sum())))
P('    por dia (PnL base -> puerta, n base -> n puerta): ' + ' '.join(f"{d_[-5:]}:{a:+.1f}->{b:+.1f}({n0}->{n1})" for d_, a, b, n0, n1 in rows))
RES['I3_V3_resim']['por_dia'] = {d_: dict(base=a, puerta=b, n0=n0, n1=n1) for d_, a, b, n0, n1 in rows}
# puerta de mercado (secundario)
first_valid = valid0.argmax(1); sp_first = spr[ar, first_valid]; selm = np.where(np.isfinite(sp_first), sp_first <= 0.025, True) & valid0.any(1)
fM, kM, pM, qM = run3(sel=selm); pnlM, cM = tot(fM, pM)
P(f"RE-SIM V3 puerta de MERCADO (spread en la 1a cotizacion): mercados cotizados {int(qM.sum())}/{int(quoted0.sum())} rellenos {int(fM.sum())} PnL {pnlM:+.2f} vs {pnl0:+.2f} (cambio {pnlM-pnl0:+.2f}) EV {pnlM/cM:+.3f}")
RES['I3_V3_mercado'] = dict(cotizados=int(qM.sum()), rellenos=int(fM.sum()), pnl=pnlM, cambio=pnlM - pnl0, ev=pnlM / cM)
# efecto sobre las NO rellenadas (poblacion de pujas completa): acierto de cotizadas por tramo de spread al cotizar (primer paso valido)
qm = valid0.any(1); spf = sp_first[qm]; wq = win3[qm]; pq = p3[ar, first_valid][qm]; fq = filled0[qm]
for lab, m in (('spread<=0,02', spf <= 0.025), ('spread>0,02', spf > 0.025)):
    P(f"    pujas (cotizadas) {lab}: n={int(m.sum())} rellenan {fq[m].mean():.3f} acierto de todas {wq[m].mean():.3f} acierto rellenadas {wq[m & fq].mean():.3f} no rellenadas {wq[m & ~fq].mean():.3f} EV_si_siempre_rellena {((wq[m].astype(float)-pq[m]).sum()/pq[m].sum()):+.3f}")
# ================================================================ I4 poblacion units (V9)
P('\n==================== I4 POBLACION units (9-21 Oct) -- V9 (decisor = maker)')
uf = sorted(glob.glob(SA + '/datos/units/units_*.pkl')); [reg(f) for f in uf]
U = pd.concat([pd.read_pickle(f)[['dia', 'maker', 'mkt', 'lado_c', 'act', 'c', 'p', 'fin', 'ts', 'gana']] for f in uf], ignore_index=True)
U['cierre'] = U.fin.astype(np.int64); U = U.rename(columns={'c': 'cost', 'p': 'pnl'}); U['grp'] = U.maker + '_' + U.cierre.astype(str) + '_' + U.lado_c
P(f"unidades {len(U)} EUR {U.cost.sum():.0f} dias {U.dia.nunique()} EV {U.pnl.sum()/U.cost.sum():+.3f} makers {U.maker.nunique()} grupos {U.grp.nunique()} ts NaN {int(U.ts.isna().sum())}")
U = U[U.ts.notna()].copy(); U['t1'] = U.groupby('grp').ts.transform('min'); U['gap'] = U.ts - U.t1
sz = U.groupby('grp').grp.transform('size'); P(f"grupos con >=2 unidades (otras monedas, mismo maker/cierre/lado): {int((U.groupby('grp').size()>=2).sum())} ; unidades en ellos {int((sz>=2).sum())}")
RES['I4_base'] = dict(unidades=int(len(U)), eur=float(U.cost.sum()), ev=float(U.pnl.sum() / U.cost.sum()), grupos_multi=int((U.groupby('grp').size() >= 2).sum()))
Ucl = U[['dia', 'cierre', 'pnl', 'cost', 'grp']].copy()
for L in (3.0, 1.0, 5.0):
    veto = lib.veto_time(U.grp.values, U.ts.values, L)
    t = summarize('I4', Ucl.assign(veto=veto), 'grp', rng, reps=(REPS_P if L == 3.0 else 500)); show(f'I4 V9 L={L:g} s{" (PRIMARIO)" if L==3.0 else " (sens.)"}', t); RES[f'I4_V9_L{L:g}'] = t
    gp = U.gap[(sz >= 2) & (U.gap > 0)]
    if L == 3.0: P(f"    gaps (s) de unidades posteriores al 1o: n={len(gp)} p10/25/50/75/90 {np.quantile(gp,[.1,.25,.5,.75,.9]).round(2).tolist()}")
# latencia por coste vetado en I4
vet_all = U[(sz >= 2) & (U.gap > 0)]
RES['I4_latencia'] = {f'cost_share_gap_ge_{L:g}': float(vet_all[vet_all.gap >= L].cost.sum() / vet_all.cost.sum()) for L in (0.5, 1.0, 3.0, 5.0)}
P('I4 latencia (cuota de coste de unidades posteriores con gap>=L):', RES['I4_latencia'])
# ================================================================ I4b poblacion con libro (V3)
P('\n==================== I4b POBLACION ms_units (17-21 Oct) -- V3')
mf = reg(SA + '/datos/ms_units.pkl'); MU = pd.read_pickle(mf)[['dia', 'maker', 'mkt', 'act', 'c', 'p', 'fin', 'spread']].rename(columns={'c': 'cost', 'p': 'pnl'})
MU['cierre'] = MU.fin.astype(np.int64); nanm = int(MU.spread.isna().sum()); MU = MU[MU.spread.notna()].copy()
MU['spread'] = MU.spread.round(2); MU['veto'] = MU.spread > 0.025; MU['grp3'] = MU.dia + '_' + MU.act
P(f"unidades con spread {len(MU)} (excluidas por spread NaN: {nanm}) EV {MU.pnl.sum()/MU.cost.sum():+.3f}")
t = summarize('I4b', MU[['dia', 'cierre', 'pnl', 'cost', 'veto', 'grp3']], 'grp3', rng); show('I4b V3 particion (spread en el relleno > 0,02)', t); RES['I4b_V3'] = t; RES['I4b_V3']['spread_nan_excluidas'] = nanm
# ================================================================ I1 B real (descriptivo / in-sample)
P('\n==================== I1 B REAL on-chain (DESCRIPTIVO, ORIGEN de las reglas, 20-22 Oct)')
pf_ = reg(AN + '/pos_anotado2.csv'); B1 = pd.read_csv(pf_)
B1['cierre'] = B1.fin.astype(np.int64); B1 = B1.rename(columns={'coste': 'cost', 'pnl': 'pnl'})
P(f"posiciones {len(B1)} (en ledger {int(B1.en_ledger.sum())}, SIN puja_fin {int((~B1.en_ledger).sum())}) PnL {B1.pnl.sum():+.2f} EV {B1.pnl.sum()/B1.cost.sum():+.3f}")
B1['grp'] = B1.cierre.astype(str) + '_' + B1.lado
B1 = B1.sort_values('t_fill'); B1['t1'] = B1.groupby('grp').t_fill.transform('min'); B1['gap'] = B1.t_fill - B1.t1; szb = B1.groupby('grp').grp.transform('size')
for L in (1.0, 0.5, 3.0):
    # el 1o = el de menor t_fill; vetados = los demas con gap >= L (L=0: reproduce el informe)
    veto = lib.veto_time(B1.grp.values, B1.t_fill.values, L)
    t = summarize('I1', B1[['dia', 'cierre', 'pnl', 'cost', 'grp']].assign(veto=veto), 'grp', rng, reps=(REPS_P if L == 1.0 else 500)); show(f'I1 V9 L={L:g} s{" (PRIMARIO)" if L==1.0 else " (sens.)"}', t); RES[f'I1_V9_L{L:g}'] = t
veto0 = ((szb >= 2) & (B1.gap > 0)).values
P(f"I1 V9 L=0 (reproduccion del informe): vetados {int(veto0.sum())} neto {-B1.pnl[veto0].sum():+.2f} (informe: 75 / +10.99)")
vet = B1[(szb >= 2) & (B1.gap > 0)]
gp = vet.gap; P(f"    gaps de los posteriores al 1o: n={len(gp)} p10/25/50/75/90 {np.quantile(gp,[.1,.25,.5,.75,.9]).round(2).tolist()}  cuota del coste con gap>=0,5/1/3 s: " + '/'.join(f"{vet[vet.gap >= L].cost.sum()/vet.cost.sum():.3f}" for L in (0.5, 1.0, 3.0)) + f" | fuente de t: {vet.src_t.value_counts().to_dict()}")
RES['I1_latencia'] = {f'cost_share_gap_ge_{L:g}': float(vet[vet.gap >= L].cost.sum() / vet.cost.sum()) for L in (0.5, 1.0, 3.0)}
RES['I1_latencia']['gaps_q'] = np.quantile(gp, [.1, .25, .5, .75, .9]).round(3).tolist()
# V3 en B real
B1['spr'] = B1.spread_post.round(2); nmiss = int(B1.spr.isna().sum()); P(f"V3 B real: spread_post NaN {nmiss} (de ellas SIN puja_fin: {int((B1.spr.isna() & ~B1.en_ledger).sum())})")
for lab, rule in (('excluidas', None), ('missing=no vetada', False), ('missing=vetada', True)):
    d_ = B1.copy()
    if rule is None: d_ = d_[d_.spr.notna()]; veto = (d_.spr > 0.025).values
    else: veto = np.where(d_.spr.isna(), rule, d_.spr > 0.025)
    d_ = d_.assign(grp3=d_.dia.astype(str))
    t = summarize('I1', d_[['dia', 'cierre', 'pnl', 'cost', 'grp3']].assign(veto=veto), 'grp3', rng, reps=(REPS_P if rule is None else 500)); show(f'I1 V3 ({lab})', t); RES[f'I1_V3_{lab}'] = t
# pujas B real (275): V3 y V9 sobre la poblacion de pujas
P('\n--- I1 POBLACION DE PUJAS (275 pujas del ledger con desenlace gamma)')
pj = pd.read_csv(AN + '/pujas.csv'); led = {}
for l in open('/root/polymarket-research-datalogs/experimento_h47_B_ledger.jsonl'):
    try: r = json.loads(l)
    except Exception: continue
    if r.get('real') and r.get('tipo') == 'puja_post' and r.get('escalon') == 'B': led.setdefault((r['slug'], r['lado']), r)
def spr_led(s, l):
    r = led.get((s, l)); lib = (r or {}).get('libro') or {}; b, a = lib.get('bids'), lib.get('asks')
    return round(a[0][0] - b[0][0], 2) if b and a else np.nan
pj['spr'] = [spr_led(s, l) for s, l in zip(pj.slug, pj.lado)]
P(f"pujas {len(pj)} rellenas {int(pj.relleno.sum())} con desenlace {int(pj.gana.notna().sum())} spread NaN {int(pj.spr.isna().sum())}")
pjv = pj[pj.gana.notna() & pj.spr.notna()].copy()
for lab, m in (('spread<=0,02', pjv.spr <= 0.025), ('spread>0,02', pjv.spr > 0.025)):
    g = pjv[m]; P(f"    {lab}: pujas {len(g)} rellenan {g.relleno.mean():.3f} acierto rellenas {g[g.relleno].gana.mean():.3f} (n={int(g.relleno.sum())}) no rellenas {g[~g.relleno].gana.mean():.3f} (n={int((~g.relleno).sum())}) EV_si_siempre_rellena {((g.gana - g.p_post).sum()/g.p_post.sum()):+.3f}")
RES['I1_pujas'] = {lab: dict(n=int(m.sum()), relleno=float(pjv[m].relleno.mean()), acierto_rellenas=float(pjv[m & pjv.relleno].gana.mean()), acierto_no=float(pjv[m & ~pjv.relleno].gana.mean())) for lab, m in (('le002', pjv.spr <= 0.025), ('gt002', pjv.spr > 0.025))}
pj['grp'] = pj.fin.astype(str) + '_' + pj.lado
mg = pj.groupby('grp').size(); P(f"V9 sobre pujas: cierres-lado con >=2 pujas {int((mg>=2).sum())}; pujas en ellos {int(mg[mg>=2].sum())}")
# ================================================================ VEREDICTOS (gate del prereg, seccion 4)
P('\n==================== VEREDICTOS segun gate preregistrado')
def gv9(t, nd, lat_ok):
    g = {}
    g['G1'] = bool(t['delta'] is not None and t['delta'] > 0 and t['ic90_dia_delta'][0] > 0)
    g['G2'] = bool(t['ic90_cierre_delta'][0] > 0)
    pe = t.get('placebo_estricto'); g['G3'] = bool(pe and pe['neto_sobre_placebo'] > 0 and pe['p'] <= 0.05)
    g['G4'] = bool(t['dias_delta_pos'] >= 9 and t['net_sin2'] > 0)
    g['G5'] = bool(t['delta_le19'] is not None and t['delta_le19'] > 0)
    g['G6'] = bool(lat_ok)
    return g
V = {}
lat1 = RES['I1_latencia']['cost_share_gap_ge_1'] >= 0.75; lat4 = RES['I4_latencia']['cost_share_gap_ge_3'] >= 0.75
gI2 = gv9(RES['I2_V9_dk2'], 13, lat1 and lat4); gI4 = gv9(RES['I4_V9_L3'], 13, lat1 and lat4)
i3ok = bool(RES['I3_V9_dk2']['delta'] is not None and RES['I3_V9_dk2']['delta'] > 0)
neg9 = any(((x['delta'] is None) or x['delta'] <= 0 or x['ic90_dia_delta'][1] < 0) for x in (RES['I2_V9_dk2'], RES['I4_V9_L3']))
pos9 = all(gI2.values()) and all(gI4.values()) and i3ok
V['V9'] = dict(I2=gI2, I4=gI4, I3_delta_pos=i3ok, latencia_I1=lat1, latencia_I4=lat4, veredicto=('POSITIVO' if pos9 else ('NEGATIVO' if neg9 else 'NO CONCLUYE')))
def gv3(t, resim=None):
    g = {}
    # Delta de V3 = EV(retenido spread<=0,02) - EV(vetado spread>0,02): es t['delta'] (ev_r - ev_v)
    g['G1'] = bool(t['delta'] is not None and t['delta'] > 0 and t['ic90_dia_delta'][0] > 0)
    g['G2'] = bool(t['ic90_cierre_delta'][0] > 0)
    pe = t.get('placebo_estricto'); g3 = bool(pe and pe['neto_sobre_placebo'] > 0 and pe['p'] <= 0.05)
    if resim is not None: g3 = g3 and bool(resim['cambio'] > 0 and resim['p_placebo'] <= 0.05)
    g['G3'] = g3
    g['G4'] = bool(t['dias_delta_pos'] >= 4 and t['net_sin2'] > 0 and t['delta_le19'] is not None and t['delta_le19'] > 0)
    g['G5'] = bool(t['share_veto'] <= 0.5 and t['share_cost_kept'] >= 0.4)
    return g
g3a = gv3(RES['I3_V3_particion'], RES['I3_V3_resim']); g3b = gv3(RES['I4b_V3'])
same = bool(RES['I3_V3_particion']['delta'] is not None and RES['I4b_V3']['delta'] is not None and np.sign(RES['I3_V3_particion']['delta']) == np.sign(RES['I4b_V3']['delta']))
pos3 = all(g3a.values()) and all(g3b.values()) and same
neg3 = any(((x['delta'] is None) or x['delta'] <= 0 or x['ic90_dia_delta'][1] < 0) for x in (RES['I3_V3_particion'], RES['I4b_V3']))
V['V3'] = dict(I3=g3a, I4b=g3b, G6_mismo_signo=same, veredicto=('POSITIVO' if pos3 else ('NEGATIVO' if neg3 else 'NO CONCLUYE')))
RES['VEREDICTOS'] = V
P(json.dumps(V, indent=1, ensure_ascii=False))
# ================================================================ salida
json.dump(RES, open(HERE + '/resultados.json', 'w'), indent=1, default=lambda o: (None if (isinstance(o, float) and np.isnan(o)) else (o.item() if hasattr(o, 'item') else str(o))))
open(HERE + '/salida.txt', 'w').write('\n'.join(OUTS) + '\n')
man = dict(job='contraste_v9_v3', script=sha(__file__)[:16], script_sha256=sha(__file__), prereg_sha256=open(PRE + '/PREREG_V9_V3.sha256').read().split()[0], params=dict(REPS_B=REPS_B, REPS_P=REPS_P, SEED=SEED),
           inputs=INPUTS, inicio=dt.datetime.fromtimestamp(T0, dt.timezone.utc).isoformat(), fin=dt.datetime.now(dt.timezone.utc).isoformat(), status='COMPLETE', veredictos={k: v['veredicto'] for k, v in V.items()},
           reproducir='cd /root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/contraste && (ulimit -v 3000000; nice -n 19 ionice -c3 python3 contraste_v9_v3.py)')
json.dump(man, open(HERE + '/run_manifest.json', 'w'), indent=1)
P('FIN', round(time.time() - T0, 1), 's')
