#!/usr/bin/env python3
"""t4d_c2.py [LAT] (1d-C v2, 17-Nov, correcciones de Javi). Rellenos virtuales de B = G0 de passT_v4 con la LATENCIA REAL de alta (LAT_POST=LAT ms; paquete_l B2/B3/B5 13-Nov: alta ex-envio p50 38/34/35, p90 147/47/42; cancelacion ex-envio p50 34/32/32) en motor+gating+rasgos.
RASGOS (F5 p60, bid, tipo B = bid >= L+0,0099) en t_dec de COLOCACION (solo rx <= t_dec); convencion antigua tf-63 solo para medir su sesgo. METRICA PRINCIPAL = regla de B: tipo B (y variante tipo B & tercil bajo); G0 solo contexto.
RELOJ: tf = sello de EXCHANGE del relleno (~UTC local, chrony 2-4 ms); el detector decide por segundos locales con datos rx < segundo (causal). Estado aplicado a la hora local del relleno menos la latencia real de cancelacion Lc (33 ms p50; 111 p90 B2). Pruebas: desplazar el relleno +-1 s y +-d_hat (rx-ex medido por segundo en la segmentacion) y ver cuantas asignaciones lo/nolo cambian.
GATING: 'colocacion' = estado lo en el segundo de t_dec (la guarda permite colocar); 'continuo' = lo en todos los segundos desde t_dec hasta el relleno (cota conservadora: sin cancelar/reponer). Estados: detector adoptado (W12 C30 rho0,07 nmin5 H1, salida inmediata), p5 10 min, verdad d<30 ms.
EV = sum(pnl)/sum(coste) ponderado por EUR; IC90 por dias (t) del EV diario y bootstrap por bloques de dia (B=5000, semilla 20261118); dias necesarios = (1,645*sd/media)^2 del EV diario; sin 2 mejores dias."""
import os, sys, json, glob, numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import suelo_causal as SC, t4b_eval as T
from scipy import stats
LAT = sys.argv[1] if len(sys.argv) > 1 else '35'; C0 = 3.526360511779785; P = SC.ParamsDetector(12, 30, 0.07, 5, 1); LC = 33
def dhat(S):
    """rx-ex medido por segundo: p5 (centro de banda) de la ventana [s-30, s+30] de la segmentacion."""
    cen = np.array([9.0] + [10.5 + 2 * i for i in range(25)] + [60.0]); cs = np.cumsum(np.concatenate([np.zeros((1, S.shape[1]), np.int64), S.astype(np.int64)]), 0); s = np.arange(S.shape[0]); a = np.clip(s - 30, 0, S.shape[0]); b = np.clip(s + 31, 0, S.shape[0]); W = cs[b] - cs[a]; tot = W.sum(1)
    k = np.maximum(1, (0.05 * tot).astype(np.int64)); cum = np.cumsum(W, 1); i = (cum >= k[:, None]).argmax(1); d = cen[i]; d[tot < 20] = np.nan; return pd.Series(d).ffill().bfill().values
def ev(p, c): return float(p / c) if c > 0 else float('nan')
def sec(ms, day0): return np.clip((np.asarray(ms, np.int64) - day0) // 1000, 0, 86399)
def gate(F, st, day0, modo, shift_ms=0, lc=LC, dh=None):
    td = F.t_dec.values.astype(np.int64) + shift_ms; tf = F.tf.values.astype(np.int64) + shift_ms - lc
    if dh is not None: tf = tf + dh[sec(F.tf.values, day0)].astype(np.int64)
    if modo == 'coloc': return st[sec(td, day0)]
    c = np.concatenate([[0], np.cumsum(~st)]); a = sec(td, day0); b = sec(tf, day0); return (c[np.maximum(b, a) + 1] - c[a]) == 0
def agrega_dias(rows):
    a = np.array(rows, float)                                 # filas: (pnl, coste) por dia
    return a
def resumen(nm, per_dia, n):
    p = np.array([x[0] for x in per_dia]); c = np.array([x[1] for x in per_dia]); ok = c > 0; ev_d = p[ok] / c[ok]; s = (p.sum(), c.sum())
    rng = np.random.default_rng(20261118); idx = np.where(ok)[0]; bs = []
    for _ in range(5000):
        j = rng.choice(idx, len(idx)); bs.append(ev(p[j].sum(), c[j].sum()))
    bs = np.array(bs); t = ''
    if ok.sum() >= 3:
        se = ev_d.std(ddof=1) / np.sqrt(ok.sum()); lo = ev_d.mean() - stats.t.ppf(.95, ok.sum() - 1) * se; hi = ev_d.mean() + stats.t.ppf(.95, ok.sum() - 1) * se; sd = ev_d.std(ddof=1)
        nreq = (1.645 * sd / ev_d.mean()) ** 2 if ev_d.mean() > 0 else float('nan'); s2 = np.sort(p[ok] / c[ok])[:-2].mean() if ok.sum() > 3 else float('nan')
        t = f"EV diario medio {ev_d.mean():+.3f} IC90 dias ({lo:+.3f},{hi:+.3f}) [{ok.sum()} dias, dias+ {(ev_d > 0).sum()}], sin 2 mejores dias {s2:+.3f}, dias necesarios para IC90>0 {'n/a (EV<=0)' if not np.isfinite(nreq) else f'~{nreq:.0f}'}"
    return f"{nm:<46} n={n:>5} {s[1]:>7.0f} EUR EV pond. {ev(*s):+.3f} (boot bloques-dia IC90 {np.percentile(bs, 5):+.3f},{np.percentile(bs, 95):+.3f}) | {t}"
if __name__ == '__main__':
    fs = sorted(glob.glob(HERE + f'/cache/bfill{LAT}_2026-*.pkl')); days = [os.path.basename(f)[-14:-4] for f in fs]; SUF = ''
    REF = sys.argv[2] if len(sys.argv) > 2 else None
    if REF: days = [d for d in days if os.path.exists(HERE + f'/cache/bfill{REF}_{d}.pkl')]
    days = [d for d in days if json.load(open(HERE + f'/cache/bfill{LAT}_man_{d}.json')).get('estado') == 'COMPLETE' and os.path.exists(HERE + f'/cache/seg_{d}.npz')]
    L = [f'# T4d-C2 B virtual LAT={LAT} ms; dias {len(days)} ({days[0]}..{days[-1]})']
    Fs = {d: pd.read_pickle(HERE + f'/cache/bfill{LAT}_{d}.pkl') for d in days}; Ds = {d: T.Dia(d) for d in days}; ST = {d: SC.estado_lo(SC.lo_crudo(Ds[d].S, P), P) for d in days}; DH = {d: dhat(Ds[d].S) for d in days}; D0 = {d: int(pd.Timestamp(d + 'T00:00:00Z').value // 10**6) for d in days}
    tot = pd.concat(Fs.values()); L.append(f"G0 (contexto) n={len(tot)} {tot.cost.sum():.0f} EUR EV {ev(tot.pnl.sum(), tot.cost.sum()):+.3f}; F5 ok en t_dec {int((tot.cat_p60 == 0).sum())}; tipoB(t_dec) n={int(tot.tipoB.sum())}; tipoB(tf-63) n={int(tot.tipoB_old.sum())}; d_hat mediana {np.nanmedian(np.concatenate(list(DH.values()))):.1f} ms")
    reglas = {'REGLA B: tipo B (primaria)': lambda F: F.tipoB & (F.cat_p60 == 0), 'tipo B & tercil bajo': lambda F: F.tipoB & (F.cat_p60 == 0) & (F.F5_p60 <= C0), 'tercil bajo (sin tipo B)': lambda F: (F.cat_p60 == 0) & (F.F5_p60 <= C0), 'G0 todos (contexto)': lambda F: np.ones(len(F), bool)}
    estados = {'detector adoptado': lambda d: ST[d], 'p5 10 min': lambda d: Ds[d].st_p5, 'verdad d<30': lambda d: Ds[d].vs == 1}
    for rn, rf in reglas.items():
        L.append(f'## {rn}')
        sel = {d: rf(Fs[d]) for d in days}; per_all = [(float(Fs[d].pnl[sel[d]].sum()), float(Fs[d].cost[sel[d]].sum())) for d in days]; L.append(resumen('  sin guarda (todos los dias)', per_all, int(sum(s.sum() for s in sel.values()))))
        for en, ef in estados.items():
            for modo in ('coloc', 'cont'):
                lo = []; no = []; nl = nn = 0
                for d in days:
                    F = Fs[d][sel[d]]
                    if len(F) == 0: lo.append((0., 0.)); no.append((0., 0.)); continue
                    g = gate(F, ef(d), D0[d], modo); lo.append((float(F.pnl[g].sum()), float(F.cost[g].sum()))); no.append((float(F.pnl[~g].sum()), float(F.cost[~g].sum()))); nl += int(g.sum()); nn += int((~g).sum())
                L.append(resumen(f'  {en} [{modo}] LO', lo, nl)); L.append(resumen(f'  {en} [{modo}] NOLO', no, nn))
    # --- RELOJ: sensibilidad de la asignacion lo/nolo (regla principal, detector adoptado, 'coloc' y 'cont')
    L.append('## RELOJ: % de rellenos (regla B tipo B) cuya asignacion lo/nolo cambia al mover el relleno'); F5r = {d: Fs[d][reglas['REGLA B: tipo B (primaria)'](Fs[d])] for d in days}; ntot = sum(len(F) for F in F5r.values())
    for modo in ('coloc', 'cont'):
        for nm, kw in (('+1 s', dict(shift_ms=1000)), ('-1 s', dict(shift_ms=-1000)), ('+d_hat (rx-ex medido)', dict(dh=True)), ('Lc=111 ms (p90 B2)', dict(lc=111)), ('Lc=0', dict(lc=0))):
            ch = 0
            for d in days:
                F = F5r[d]
                if len(F) == 0: continue
                a = gate(F, ST[d], D0[d], modo); b = gate(F, ST[d], D0[d], modo, shift_ms=kw.get('shift_ms', 0), lc=kw.get('lc', LC), dh=DH[d] if kw.get('dh') else None); ch += int((a != b).sum())
            L.append(f'  [{modo}] {nm:<24} cambian {ch}/{ntot} ({100 * ch / max(ntot, 1):.2f} %)')
    ntr = 0
    for d in days:
        F = F5r[d]; tr = np.where(np.diff(ST[d].astype(int)) != 0)[0] + 1; s = sec(F.tf.values, D0[d]); ntr += int(sum(np.any(np.abs(tr - x) <= 60) for x in s)) if len(tr) else 0
    L.append(f'  (fills de la regla a <=60 s de una transicion del detector: {ntr}/{ntot}; los que importan para esta prueba)')
    for modo in ('coloc', 'cont'):
        rl = [0, 0., 0.]; rh = [0, 0., 0.]
        for d in days:
            F = F5r[d]
            if len(F) == 0: continue
            g = gate(F, ST[d], D0[d], modo); tv = Ds[d].vs[sec(F.t_dec.values, D0[d])]
            for tg, m in ((rl, ~g & (tv == 1)), (rh, g & (tv == 0))): tg[0] += int(m.sum()); tg[1] += float(F.cost.values[m].sum()); tg[2] += float(F.pnl.values[m].sum())
        L.append(f'  [{modo}] regla B: OPORTUNIDAD PERDIDA (guarda nolo, verdad lo en t_dec) n={rl[0]} {rl[1]:.1f} EUR pnl {rl[2]:+.1f} | EXPOSICION (guarda lo, verdad hi) n={rh[0]} {rh[1]:.1f} EUR pnl {rh[2]:+.1f}')
    # --- DECISION: sesgo de la convencion antigua (tf-63) frente a t_dec
    L.append('## DECISION: convencion antigua (rasgos en tf-63) vs t_dec de colocacion (todos los dias)')
    a = tot.tipoB_old & (tot.cat_old == 0); b = tot.tipoB & (tot.cat_p60 == 0); L.append(f"  tipo B: antigua n={int(a.sum())} ({tot.cost[a].sum():.0f} EUR, EV {ev(tot.pnl[a].sum(), tot.cost[a].sum()):+.3f}) | t_dec n={int(b.sum())} ({tot.cost[b].sum():.0f} EUR, EV {ev(tot.pnl[b].sum(), tot.cost[b].sum()):+.3f}) | en ambas {int((a & b).sum())}; solo antigua {int((a & ~b).sum())} (EV {ev(tot.pnl[a & ~b].sum(), tot.cost[a & ~b].sum()):+.3f}); solo t_dec {int((~a & b).sum())} (EV {ev(tot.pnl[~a & b].sum(), tot.cost[~a & b].sum()):+.3f})")
    ra = (tot.cat_old == 0) & (tot.F5_old <= C0); rb = (tot.cat_p60 == 0) & (tot.F5_p60 <= C0); L.append(f"  tercil bajo: antigua n={int(ra.sum())} EV {ev(tot.pnl[ra].sum(), tot.cost[ra].sum()):+.3f} | t_dec n={int(rb.sum())} EV {ev(tot.pnl[rb].sum(), tot.cost[rb].sum()):+.3f} | concordancia de etiqueta {100 * np.mean(ra == rb):.1f} %")
    open(HERE + f'/T4d_C2_{LAT}' + (f'_vs{REF}' if REF else '') + '.txt', 'w').write('\n'.join(L) + '\n'); print('\n'.join(x[:620] for x in L))
