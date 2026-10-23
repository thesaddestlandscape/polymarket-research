#!/usr/bin/env python3
"""s4_eval.py -- evaluacion TEST 17..21 (una pasada) de lo congelado en DESC. PREREG sha 850d7101."""
import sys, json, os
import numpy as np, pandas as pd
from sklearn.metrics import roc_auc_score
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qlib import *
DL = '/root/polymarket-research-datalogs/q_techo/'; OUTD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
D = pd.read_pickle(DL + 'test_pred.pkl'); F1 = pd.read_pickle(DL + 'fase1.pkl'); fr = F1['frozen']
T = pd.read_pickle(DL + 'tab.pkl'); T = T[T.act.isin(COINS)].sort_values(['dia', 'ts']).reset_index(drop=True)
LOG = []
def P(*a):
    s = ' '.join(str(x) for x in a); LOG.append(s); print(s, flush=True)
fam = fr['fam'] or 'HGB'; m_p = fr['m'] if fr['fam'] else 0.02; qn = {'MAP': 'q_MAP', 'LOGIT': 'q_LOG', 'HGB': 'q_HGB'}[fam]
P(f'# Q-TECHO TEST 17-21 (n={len(D)}, EUR={D.c.sum():.0f}); regla primaria: familia {fam} m={m_p} ({"elegida en DESC" if fr["fam"] else "SIN candidata en DESC: descriptivo"}); prereg 850d7101')
cl = clus(D)
def r2flag(X): return (X.b15.notna() & (X.b15 <= X.a15.fillna(9)) & (X.lvl15 <= 0.03)).values
def r3flag(X): return r2flag(X) & (X.vol30ws.fillna(-1).values >= 26) & (X.hora.values >= 4)
def rep(nom, X, skip, ref=None, perm=True, extra=''):
    cl_ = clus(X); s = stats(X, skip); lo, hi = boot(-X.p.values * skip, cl_); elo, ehi = boot_ratio(X.p.values * ~skip, X.c.values * ~skip, cl_)
    pp = perm_cierre(X, skip)[0] if perm else np.nan
    dd = pd.Series(-X.p.values * skip).groupby(X.dia.values).sum(); best2 = dd.sort_values(ascending=False).index[:2]; sin2 = dd.drop(best2).sum()
    pc_ = {a: float(-X.p.values[skip & (X.act.values == a)].sum()) for a in COINS}
    evc = {a: round(float(X.p.values[~skip & (X.act.values == a)].sum() / max(X.c.values[~skip & (X.act.values == a)].sum(), 1e-9)), 3) for a in COINS}
    P(f'{nom}: skip {s["n_skip"]}/{s["n"]} ret {s["ret"]:.3f} | EV_all {s["ev_all"]:+.4f} EV_ret {s["ev_ret"]:+.4f} [{elo:+.3f},{ehi:+.3f}] EV_skip {s["ev_skip"]:+.4f} | dPnL {s["dpnl"]:+.1f} IC90cierre [{lo:+.1f},{hi:+.1f}] p_perm {pp:.4f} | dias+ {(dd>0).sum()}/{len(dd)} sin2mejores {sin2:+.1f} | haircut50 {s["dpnl"]/2:+.1f} | dPnL/moneda {{{", ".join(f"{k}:{v:+.1f}" for k,v in pc_.items())}}} EVret/moneda {evc} {extra}')
    return dict(s, ic=(lo, hi), p=pp, sin2=float(sin2), dias_pos=int((dd > 0).sum()), dias=int(len(dd)), por_moneda=pc_)
OUT = {}
# ---------------- G-Q1: prediccion
P('\n== G-Q1 prediccion (fuera de muestra, TEST 17-21): logloss/Brier medios, AUC; diferencias pareadas q - benchmark, IC90 por cierre (negativo = q mejor) ==')
y = D.gana_f.values
# indicador R3 como predictor: media de acierto por bandera (ajustada con dias < d)
r3 = r3flag(D); q_r3 = np.full(len(D), np.nan)
for d in sorted(D.dia.unique()):
    tr = T[T.dia < d]; f_tr = r3flag(tr); mk = (D.dia.values == d)
    for a in COINS:
        t_ = tr[(tr.act == a)]; ft = r3flag(t_); m1 = t_.gana_f.values[ft].mean(); m0 = t_.gana_f.values[~ft].mean()
        sel = mk & (D.act.values == a); q_r3[sel] = np.where(r3[sel], m1, m0)
D['q_R3'] = q_r3; mid5 = D.mid5.values; has_mid = np.isfinite(mid5)
P('cobertura mid5', has_mid.mean().round(4))
for nm in ['q_MAP', 'q_LOG', 'q_HGB', 'q_LOGF', 'q_HGBF', 'q_R3']:
    q = D[nm].values; ll = lossd(y, q, np.full(len(y), 0.5), 'll') * 0
    llm = -(y * np.log(np.clip(q, 1e-3, 1 - 1e-3)) + (1 - y) * np.log(1 - np.clip(q, 1e-3, 1 - 1e-3))).mean(); br = ((q - y) ** 2).mean()
    P(f'  {nm}: logloss {llm:.5f} Brier {br:.5f} AUC {roc_auc_score(y, q):.4f}')
pcv = D.pc.values; P(f'  precio pc: logloss {-(y*np.log(pcv)+(1-y)*np.log(1-pcv)).mean():.5f} Brier {((pcv-y)**2).mean():.5f} AUC {roc_auc_score(y, pcv):.4f}')
qm = np.clip(mid5, 0.01, 0.99); mm = has_mid
P(f'  mid5 (n={mm.sum()}): logloss {-(y[mm]*np.log(qm[mm])+(1-y[mm])*np.log(1-qm[mm])).mean():.5f} Brier {((qm[mm]-y[mm])**2).mean():.5f} AUC {roc_auc_score(y[mm], mid5[mm]):.4f}')
for nm in ['q_MAP', 'q_LOG', 'q_HGB', 'q_LOGF', 'q_HGBF']:
    for bn, b in [('mid5', qm), ('pc', pcv), ('MAP', D.q_MAP.values), ('R3-ind', D.q_R3.values)]:
        if bn == 'MAP' and nm == 'q_MAP': continue
        ok = np.isfinite(b) & np.isfinite(D[nm].values) & (has_mid if bn == 'mid5' else True)
        X = D[ok]; c_ = clus(X)
        for kind in ('ll', 'br'):
            v = lossd(y[ok], D[nm].values[ok], b[ok], 'll' if kind == 'll' else 'br'); mu, lo, hi = ic_mean(v, c_)
            P(f'  {nm} vs {bn} {kind}: dif media {mu:+.5f} IC90 cierre [{lo:+.5f},{hi:+.5f}] n={ok.sum()} {"<- q MEJOR" if hi<0 else ("<- q peor" if lo>0 else "")}')
# fiabilidad
q = D[qn].values; dec = pd.qcut(q, 10, duplicates='drop'); rel = pd.DataFrame(dict(q=q, y=y, pc=D.pc.values, p=D.p.values, c=D.c.values)).groupby(dec, observed=True).agg(n=('y', 'size'), q=('q', 'mean'), hit=('y', 'mean'), pc=('pc', 'mean'), ev=('p', 'sum'), c=('c', 'sum')); rel['ev'] = rel.ev / rel.c
P('\n== fiabilidad del q primario por decil (q, acierto real, pc medio, EV/EUR del decil) ==\n' + rel[['n', 'q', 'hit', 'pc', 'ev']].round(4).to_string())
edge = D[qn].values - D.pc.values; de = pd.qcut(edge, 10, duplicates='drop'); r2_ = pd.DataFrame(dict(e=edge, p=D.p.values, c=D.c.values)).groupby(de, observed=True).agg(e=('e', 'mean'), p=('p', 'sum'), c=('c', 'sum')); r2_['ev'] = r2_.p / r2_.c
P('== EV/EUR por decil de edge (q-pc) del q primario (monotonia = ordena) ==\n' + r2_[['e', 'ev']].round(4).T.to_string())
# ---------------- G-Q2/3: reglas
P('\n== G-Q2 reglas en TEST (dPnL = -PnL de las saltadas; EV ponderado por EUR; precio = relleno real del maker) ==')
res = {}
skp = D.pc.values > D[qn].values - m_p; res['primaria'] = rep(f'PRIMARIA {fam} m={m_p}', D, skp)
# inversion: misma cantidad de EUR por la cola alta del edge
def inv_skip(X, qv, frac_eur):
    e = qv - X.pc.values; o = np.argsort(-e); cum = np.cumsum(X.c.values[o]); n = np.searchsorted(cum, frac_eur * X.c.sum()); sk = np.zeros(len(X), bool); sk[o[:n]] = True; return sk
si = inv_skip(D, D[qn].values, 1 - res['primaria']['ret']); res['inversion'] = rep('  inversion (saltar cola ALTA del edge, mismo EUR)', D, si, perm=False)
# otras familias en rejilla (descriptivo)
P('-- rejilla completa de familias x m en TEST (DESCRIPTIVA, multiplicidad declarada) --')
for nm in ['q_MAP', 'q_LOG', 'q_HGB', 'q_LOGF', 'q_HGBF']:
    for m in MGRID:
        sk = D.pc.values > D[nm].values - m; s = stats(D, sk); lo, hi = boot(-D.p.values * sk, cl)
        P(f'   {nm:7s} m={m:.2f}: skip {s["n_skip"]:5d} ret {s["ret"]:.3f} EV_ret {s["ev_ret"]:+.4f} EV_skip {s["ev_skip"]:+.4f} dPnL {s["dpnl"]:+8.1f} IC90 [{lo:+.1f},{hi:+.1f}]')
# MAP con su m de DESC
mm_ = [s for s in F1['sel'] if s['fam'] == 'MAP' and s['ret'] >= 0.25 and s['ev_ret'] > s['ev_all']]
if mm_ and fam != 'MAP':
    mb = max(mm_, key=lambda s: s['dpnl'])['m']; res['H-MAP'] = rep(f'H-MAP (techo por tramo, m={mb} de DESC)', D, D.pc.values > D.q_MAP.values - mb)
# Binance
thr = fr['r60thr']; sk60 = (D.r60f.values <= D.act.map(thr).values) & D.r60f.notna().values; res['H-r60'] = rep('H-r60 (saltar r60f <= p20 DESC por moneda)', D, sk60)
res['R0'] = rep('R0 (saltar CON rpre_s>=7,7)', D, (D.CON.values == 1))
P('-- lineas base R2/R3 (elegidas con 17-21: EN MUESTRA aqui; ver DESC-OOS abajo) --')
res['R2'] = rep('R2 (retener lvl15<=0,03)', D, ~r2flag(D)); res['R3'] = rep('R3 (R2 & vol30ws>=26 & hora>=4)', D, ~r3flag(D))
# G-Q3
P('\n== G-Q3: contra R0 y R3 ==')
a = -D.p.values * skp; b = -D.p.values * (D.CON.values == 1); lo, hi = boot(a - b, cl); P(f'dPnL(primaria) - dPnL(R0): {(a-b).sum():+.1f} IC90 cierre [{lo:+.1f},{hi:+.1f}]')
b = -D.p.values * sk60; lo, hi = boot(a - b, cl); P(f'dPnL(primaria) - dPnL(R_r60): {(a-b).sum():+.1f} IC90 cierre [{lo:+.1f},{hi:+.1f}]')
retR3 = res['R3']['ret']; sk_eq = inv_skip(D, -(D[qn].values - D.pc.values), 1 - retR3)   # saltar los de MENOR edge hasta retener igual que R3
res['q_igual_ret_R3'] = rep(f'q-top-edge a retencion igualada con R3 ({retR3:.3f})', D, sk_eq)
b = -D.p.values * (~r3flag(D)); a2 = -D.p.values * sk_eq; lo, hi = boot(a2 - b, cl); P(f'dPnL(q a retencion R3) - dPnL(R3): {(a2-b).sum():+.1f} IC90 cierre [{lo:+.1f},{hi:+.1f}]')
# incremento dentro de R3
inR3 = r3flag(D); X3 = D[inR3].reset_index(drop=True); res['dentro_R3'] = rep(f'q-cap DENTRO de R3 (retenidas por R3: {inR3.sum()})', X3, X3.pc.values > X3[qn].values - m_p)
notR3 = ~inR3; X0 = D[notR3].reset_index(drop=True); rep(f'q-cap FUERA de R3 ({notR3.sum()})', X0, X0.pc.values > X0[qn].values - m_p)
# DESC-OOS de R2/R3
P('\n== R2/R3 en 09-16 (OOS genuino para ellas; vol30ws mio ~15 % menor: umbral 26 aproximado) ==')
Dd = T[T.dia <= '2026-10-16'].reset_index(drop=True)
rep('R2 09-16', Dd, ~r2flag(Dd)); rep('R3 09-16', Dd, ~r3flag(Dd)); rep('R0 09-16', Dd, Dd.CON.values == 1)
json.dump(res, open(OUTD + '/q_techo_fase34.json', 'w'), default=float)
open(OUTD + '/q_techo_fase34.txt', 'w').write('\n'.join(LOG))
