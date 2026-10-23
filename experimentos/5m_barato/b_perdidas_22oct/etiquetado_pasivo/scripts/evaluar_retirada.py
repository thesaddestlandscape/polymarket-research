#!/usr/bin/env python3
"""evaluar_retirada.py -- PREREG_L1b parte B (H2'/H3). Solo lectura de retirada/ret_DIA.csv.gz. Backfill (forward=0) = DESCRIPTIVO; solo forward decide.
Delta2(tau)=EV(EXIT=1)-EV(EXIT=0) en prints E banda A, estratificado (moneda x cubo 0,05 x T3 x talla S(u-850)), ponderado por el coste de los EXIT=1. IC90 por CIERRE; placebo por permutacion de EXIT en estrato."""
import os, glob, hashlib, argparse
import numpy as np, pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get('L1B_RET_OUT', '/root/polymarket-research-datalogs/etiquetado_pasivo_B/retirada')
assert hashlib.sha256(open(os.path.join(HERE, '..', 'PREREG_L1b.md'), 'rb').read()).hexdigest().startswith('93cdda53'), 'PREREG_L1b.md modificado'
TAUS = (150, 200, 250, 300); NB = 2000; SEED = 20261023


def cargar():
    L = pd.concat([pd.read_csv(f, dtype={'mid': str, 'oid': str}) for f in sorted(glob.glob(os.path.join(OUT, 'ret_*.csv.gz')))], ignore_index=True)
    return L


def estratos(E, tau):
    T3 = np.where(E['T'] < 120, 0, np.where(E['T'] < 200, 1, 2)); s = E[f's{tau}'].values; S3 = np.where(s < 15, 0, np.where(s < 50, 1, 2))
    return (E.act.astype(str) + '|' + (E.q / 50).round().astype(int).astype(str) + '|' + pd.Series(T3, index=E.index).astype(str) + '|' + pd.Series(S3, index=E.index).astype(str)).values


def delta2(co, pn, ex, st):
    """sum_s w_s (EV1_s-EV0_s), w_s = coste de EXIT=1 en s, solo estratos con ambas clases."""
    num = 0.0; den = 0.0
    for s in np.unique(st):
        m = st == s; a = m & (ex == 1); b = m & (ex == 0)
        if not a.any() or not b.any() or co[a].sum() <= 0 or co[b].sum() <= 0: continue
        w = co[a].sum(); num += w * (pn[a].sum() / co[a].sum() - pn[b].sum() / co[b].sum()); den += w
    return num / den if den > 0 else np.nan


def bloque(E, C, tau, titulo, nb=NB):
    k = E[(E[f'ok{tau}'] == 1)].copy(); k = k[k.pnl_h.notna() & (k.resuelto == 1)]
    if len(k) < 50 or k[f'ex{tau}'].nunique() < 2: print(f'  tau={tau}: n={len(k)} insuficiente'); return None
    co = k.coste_h.values; pn = k.pnl_h.values; ex = k[f'ex{tau}'].values.astype(int); st = estratos(k, tau); d = delta2(co, pn, ex, st)
    ev = lambda m: pn[m].sum() / co[m].sum() if m.any() and co[m].sum() > 0 else np.nan
    # IC90 por cierre (bootstrap de `fin`)
    fins, inv = np.unique(k.fin.values, return_inverse=True); rng = np.random.default_rng(SEED); idx = [np.where(inv == i)[0] for i in range(len(fins))]; bs = []
    for _ in range(nb):
        sel = np.concatenate([idx[i] for i in rng.integers(0, len(fins), len(fins))]); bs.append(delta2(co[sel], pn[sel], ex[sel], st[sel]))
    lo, hi = np.nanpercentile(bs, [5, 95])
    # placebo: permutar EXIT dentro de estrato
    cnt = 0; ids = {s: np.where(st == s)[0] for s in np.unique(st)}
    for _ in range(nb):
        e2 = ex.copy()
        for s, ii in ids.items(): e2[ii] = ex[rng.permutation(ii)]
        cnt += delta2(co, pn, e2, st) <= d
    pplac = (cnt + 1) / (nb + 1)
    # por dia y sin 2 mejores dias
    k['d'] = k.dia; dd = {}
    for dia, g in k.groupby('d'):
        i = g.index.values; m = k.index.isin(i); dd[dia] = delta2(co[m], pn[m], ex[m], st[m])
    pdia = k.groupby('d').pnl_h.sum().sort_values(ascending=False); q = ~k.d.isin(pdia.index[:2]).values
    d2 = delta2(co[q], pn[q], ex[q], st[q]) if len(pdia) > 2 else np.nan
    dv = [v for v in dd.values() if np.isfinite(v)]; frac = np.mean([v < 0 for v in dv]) if dv else np.nan
    # H3: evitados / conservados
    avo = ex == 1; kept = ~avo
    print(f'  tau={tau:>3}: n={len(k)} (EXIT=1 {int(avo.sum())}, {co[avo].sum() / co.sum():.1%} del coste) | Delta2={d:+.3f} IC90 cierre=({lo:+.3f},{hi:+.3f}) [{len(fins)} cierres] placebo p={pplac:.3f} | '
          f'sin2mejoresdias={d2:+.3f} dias Delta<0={frac:.2f} ({len(dv)} dias) | EV evitados={ev(avo):+.3f} conservados={ev(kept):+.3f} todos={ev(np.ones(len(co), bool)):+.3f}')
    c = C[C[f'ok{tau}'] == 1]; pe = k[f'ex{tau}'].mean(); pc = c[f'ex{tau}'].mean() if len(c) else np.nan
    print(f'          H1: P(EXIT|E)={pe:.3f} vs P(EXIT|C)={pc:.3f} (n C={len(c)}) -> E-C={pe - pc:+.3f}')
    return dict(tau=tau, n=len(k), delta=d, lo=lo, hi=hi, p=pplac, d2=d2, frac=frac, dias=len(dv), vol1=co[avo].sum() / co.sum())


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--banda', default='A'); a = ap.parse_args()
    L = cargar(); E = L[(L.grp == 'E') & (L.banda == a.banda)]; C = L[(L.grp == 'C') & (L.banda == a.banda)]
    print(f'filas: E={len(E)} C={len(C)} (banda {a.banda}); dias={sorted(L.dia.unique())}; sin desenlace E: {int((E.resuelto != 1).sum())}')
    for nom, fw in (('BACKFILL 20-22 Oct (forward=0, DESCRIPTIVO; los tau 150/300 ya los vio S1)', 0), ('FORWARD >= 2026-10-23 (decide)', 1)):
        e = E[E.forward == fw]; c = C[C.forward == fw]
        print(f'\n--- {nom}: dias={e.dia.nunique()} prints={len(e)}')
        if len(e) == 0: print('  sin filas todavia'); continue
        R = {t: bloque(e, c, t, nom) for t in TAUS}
        if fw == 1:
            nd = e.dia.nunique(); r2, r25 = R.get(200), R.get(250)
            print(f'\nGATE L1b-B: dias forward = {nd}/10')
            if nd < 10 or not r2 or not r25: print('ESTADO: NO EVALUABLE'); continue
            ok = all(r['hi'] < 0 and r['p'] < 0.05 and r['frac'] >= 0.6 and r['d2'] < 0 and r['vol1'] <= 0.30 for r in (r2, r25))
            ref = any(r['delta'] >= 0 or r['lo'] <= 0 <= r['hi'] for r in (r2, r25))
            print('ESTADO:', 'ACCIONABLE (disenar prereg de cancelar; requiere /code-review + OK Javi)' if ok else ('REFUTADA' if ref else 'INCONCLUSO'))
    B = L[L.grp.isin(['BF', 'BR'])]
    if len(B):
        print('\n--- ORDENES DE B (descriptivo, n pequeno, NO decide)')
        for g, x in B.groupby('grp'):
            print(f'  {g}: n={len(x)} dias={x.dia.nunique()} ' + ' '.join(f'ok{t}={int((x[f"ok{t}"] == 1).sum())}/ex{t}={x[x[f"ok{t}"] == 1][f"ex{t}"].mean():.2f}' for t in TAUS))


if __name__ == '__main__':
    main()
