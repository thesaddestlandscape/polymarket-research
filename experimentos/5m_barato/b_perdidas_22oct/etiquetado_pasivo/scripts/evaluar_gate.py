#!/usr/bin/env python3
"""evaluar_gate.py -- aplica el gate de ../PREREG_L1.md a las etiquetas L1. Solo lectura. Uso: evaluar_gate.py [--sens]
Imprime SIEMPRE: dias forward (>=2026-10-23) contados, n por clase y estado de cada condicion. Dias 20-22 = descriptivo (ya vistos en W1)."""
import os, sys, glob, hashlib, argparse
import numpy as np, pandas as pd

OUT = os.environ.get('L1_OUT', '/root/polymarket-research-datalogs/etiquetado_pasivo_B')
FWD = '2026-10-23'; UMBRAL = 7.7
HERE = os.path.dirname(os.path.abspath(__file__))
assert hashlib.sha256(open(os.path.join(HERE, '..', 'PREREG_L1.md'), 'rb').read()).hexdigest().startswith('643c9e97'), 'PREREG_L1.md modificado'


def cargar():
    L = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(os.path.join(OUT, 'etiquetado_B_*.csv.gz')))], ignore_index=True)
    P = L[(L.unidad == 'posicion') & (L.resuelto == 1) & L.pnl.notna() & L.coste.notna()].copy()
    P['grupo'] = np.where(P.h_w1 == 1, 1, np.where(P.clase_rpre.isin(['a_favor', 'en_contra']), 0, -1))   # -1 = neutra/missing: fuera
    return P[P.grupo >= 0]


def ev(g): return g.pnl.sum() / g.coste.sum() if len(g) and g.coste.sum() > 0 else np.nan


def delta_ic(P, nb=2000, seed=7):
    """IC90 de EV(h1)-EV(h0) por bootstrap de CIERRES (fin_s)."""
    rng = np.random.default_rng(seed); fins = P.fin_s.unique(); idx = {f: np.where(P.fin_s.values == f)[0] for f in fins}
    g = P.grupo.values; pn = P.pnl.values; co = P.coste.values; out = []
    for _ in range(nb):
        sel = np.concatenate([idx[f] for f in rng.choice(fins, len(fins))])
        a = sel[g[sel] == 1]; b = sel[g[sel] == 0]
        if len(a) and len(b) and co[a].sum() > 0 and co[b].sum() > 0: out.append(pn[a].sum() / co[a].sum() - pn[b].sum() / co[b].sum())
    return np.percentile(out, [5, 95]) if out else (np.nan, np.nan)


def placebo(P, nb=2000, seed=11):
    """Quitar al azar la misma fraccion de coste dentro de dia x moneda x lado x cubo precio 0,05: p de que el PnL retenido real >= placebo (una cola)."""
    rng = np.random.default_rng(seed); P = P.assign(cubo=(P.precio / 0.05).round().astype(int))
    real_ret = P[P.grupo == 0].pnl.sum(); strata = [g for _, g in P.groupby(['dia', 'coin', 'lado', 'cubo'])]; sims = []
    for _ in range(nb):
        ret = 0.0
        for g in strata:
            k = int((g.grupo == 1).sum())
            if k == 0: ret += g.pnl.sum(); continue
            quita = rng.choice(len(g), k, replace=False); m = np.ones(len(g), bool); m[quita] = False; ret += g.pnl.values[m].sum()
        sims.append(ret)
    sims = np.array(sims); return real_ret, float(sims.mean()), float((sims >= real_ret).mean())


def bloque(P, titulo):
    h1, h0 = P[P.grupo == 1], P[P.grupo == 0]
    print(f'--- {titulo}: dias={P.dia.nunique()} posiciones={len(P)} h_w1=1 n={len(h1)} coste={h1.coste.sum():.2f} | h_w1=0 n={len(h0)} coste={h0.coste.sum():.2f}')
    if len(h1) == 0 or len(h0) == 0: print('   sin ambas clases'); return None
    d = ev(h1) - ev(h0); lo, hi = delta_ic(P); rr, pm, pp = placebo(P)
    dias = P.groupby('dia').apply(lambda g: (ev(g[g.grupo == 1]), ev(g[g.grupo == 0])), include_groups=False)
    ambos = [(a, b) for a, b in dias if np.isfinite(a) and np.isfinite(b)]
    frac = np.mean([a < b for a, b in ambos]) if ambos else np.nan
    pdia = P.groupby('dia').pnl.sum().sort_values(ascending=False); Q = P[~P.dia.isin(pdia.index[:2])]
    d2 = ev(Q[Q.grupo == 1]) - ev(Q[Q.grupo == 0]) if len(pdia) > 2 else np.nan
    print(f'   EV h1={ev(h1):+.3f} h0={ev(h0):+.3f} Delta={d:+.3f} IC90 cierre=({lo:+.3f},{hi:+.3f}) [{P.fin_s.nunique()} cierres]')
    print(f'   PnL h1={h1.pnl.sum():+.2f} h0={h0.pnl.sum():+.2f} total={P.pnl.sum():+.2f}; PnL retenido (h0) {rr:+.2f} vs placebo medio {pm:+.2f} p={pp:.3f}')
    print(f'   Delta sin 2 mejores dias={d2:+.3f}; dias con ambas clases={len(ambos)}, fraccion con Delta<0={frac:.2f}')
    return dict(n1=len(h1), n0=len(h0), delta=d, lo=lo, hi=hi, pl_p=pp, pnl1=h1.pnl.sum(), d2=d2, frac=frac, dias=P.dia.nunique())


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--sens', action='store_true'); a = ap.parse_args()
    P = cargar(); F = P[P.dia >= FWD]
    bloque(P, 'TODO el backfill (20-22 Oct visto en W1: DESCRIPTIVO, NO decide)')
    r = bloque(F, f'FORWARD >= {FWD} (decide)') if len(F) else print('--- FORWARD: 0 posiciones resueltas con etiqueta (B parado o sin datos)')
    nd = F.dia.nunique()
    print(f'\nGATE: dias forward con posiciones resueltas = {nd}/10 ; n(h_w1=1) = {int((F.grupo == 1).sum())}/40')
    if r is None or nd < 10 or r['n1'] < 40: print('ESTADO: NO EVALUABLE (faltan dias y/o n). No cambiar B.'); return
    ok = [('Delta<0 e IC90 cierre sup<0', r['hi'] < 0), ('PnL(h1)<0 y placebo p<0,05', r['pnl1'] < 0 and r['pl_p'] < 0.05), ('sin 2 mejores dias mismo signo', r['d2'] < 0), ('>=60 % dias Delta<0', r['frac'] >= 0.6)]
    for k, v in ok: print(f'  [{"OK" if v else "NO"}] {k}')
    refut = r['delta'] >= 0 or r['lo'] <= 0 <= r['hi'] or r['pnl1'] >= 0
    print('ESTADO:', 'ELEGIBLE para disenar variante B (requiere /code-review + OK Javi)' if all(v for _, v in ok) else ('REFUTADA' if refut else 'NO CUMPLE (inconcluso)'))
    if a.sens: print('(sensibilidad r900/umbrales: pendiente de pedir; no decide)')


if __name__ == '__main__': main()
