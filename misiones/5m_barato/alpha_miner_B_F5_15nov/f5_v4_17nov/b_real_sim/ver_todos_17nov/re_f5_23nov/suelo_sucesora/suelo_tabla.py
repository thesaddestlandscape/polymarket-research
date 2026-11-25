#!/usr/bin/env python3
"""suelo_tabla.py -- TABLA FIRMADA de suelo rx-ex por ventana de 5 min (CIERRE_LIMITES_SEC7_19nov.md, limite 4). Solo lectura de out/h_DIA.csv (generado por suelo_dia.sh desde m5_registro).
Filas q (bid 0,03-0,45, tokens 5min por moneda) con d=rx-ex en [-50,400] ms, bins de 10 s de RX.
 clase_estrato (ventana completa [w0,w0+300 s), SOLO estrato, mira al futuro del rasgo a drede): n<MIN_N -> sin_datos ; p5<=28 lo ; p5>=33 hi ; 28<p5<33 indet. p5 = menor d con cum >= max(1,trunc(0,05 n)).
 causal_w0 (RASGO, solo filas rx<w0): suelo_causal.clase_de_ventanas con [w0-600,w0-300) y [w0-300,w0) ; mixta->indet ; sin bins previos (primer dia sin dia anterior) -> sin_prev (missing != lo).
 dia valido (dia x moneda): n_ventanas(lo+hi+indet) >= 24 y n_lo/(n_lo+n_hi+n_indet) >= 0,5."""
import sys, os, glob, csv, hashlib, numpy as np, datetime as dt
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = HERE + 'out/'
sys.path.insert(0, '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov'); import suelo_causal as SC
MIN_N, LO_MAX, HI_MIN, N_VAL, FRAC = 100, 28, 33, 24, 0.5
COINS = ['BNB', 'BTC', 'DOGE', 'ETH', 'SOL', 'XRP']; ND = SC.ND
def carga(d):
    p = OUT + f'h_{d}.csv'
    if not os.path.exists(p) or not os.path.exists(OUT + f'h_{d}.done'): return None
    H = {c: np.zeros((8640, ND), np.int32) for c in COINS}
    with open(p) as f:
        for ln in f:
            c, b, dd, n = ln.split(','); 
            if c in H: H[c][int(b), int(dd) + 50] += int(n)
    return H
def prev(d): return (dt.date.fromisoformat(d) - dt.timedelta(days=1)).isoformat()
def p5(h):
    tot = int(h.sum())
    if tot <= 0: return np.nan, 0
    cum = np.cumsum(h); return float(np.argmax(cum >= max(1, int(0.05 * tot))) + SC.D_LO), tot
def main():
    dias = sorted(os.path.basename(p)[2:12] for p in glob.glob(OUT + 'h_*.done')); dias = [os.path.basename(p)[2:12] for p in sorted(glob.glob(OUT + 'h_*.done'))]
    filas = []; res = []
    for d in dias:
        H = carga(d); P = carga(prev(d)); day0 = int(dt.datetime.fromisoformat(d).replace(tzinfo=dt.timezone.utc).timestamp() * 1000)
        for c in COINS:
            h = H[c]; hp = P[c] if P is not None else None
            cnt = dict(lo=0, hi=0, indet=0, sin_datos=0)
            for w in range(288):                                   # ventana = bins [30 w, 30 w + 30)
                hw = h[30 * w:30 * w + 30].sum(0); pv, n = p5(hw)
                cl = 'sin_datos' if n < MIN_N else ('lo' if pv <= LO_MAX else ('hi' if pv >= HI_MIN else 'indet'))
                cnt[cl] += 1
                a, b = 30 * w - 60, 30 * w - 30
                def seg(x, y):                                     # bins [x,y) con indices negativos -> dia anterior
                    s = np.zeros(ND, np.int64)
                    for k in range(x, y):
                        if k >= 0: s += h[k]
                        elif hp is not None: s += hp[8640 + k]
                    return s
                if w < 2 and hp is None: causal, pp1, pp2 = 'sin_prev', np.nan, np.nan
                else:
                    h1, h2 = seg(a, b), seg(b, 30 * w); f, dg = SC.clase_de_ventanas(h1, h2); causal = 'indet' if f == 'mixta' else f; pp1, pp2 = dg['p5_1'], dg['p5_2']
                    if f == 'indet' and dg['tot'] == 0: causal = 'sin_datos'
                t0 = day0 + w * 300_000
                filas.append([d, c, t0, dt.datetime.fromtimestamp(t0 / 1000, dt.timezone.utc).strftime('%FT%TZ'), n, pv, cl, causal, pp1, pp2])
            ncl = cnt['lo'] + cnt['hi'] + cnt['indet']; frac = cnt['lo'] / ncl if ncl else float('nan')
            res.append([d, c, cnt['lo'], cnt['hi'], cnt['indet'], cnt['sin_datos'], ncl, round(frac, 4) if ncl else '', int(ncl >= N_VAL and ncl > 0 and frac >= FRAC)])
    T = HERE + 'tabla_suelo_ventanas_19nov.csv'; R = HERE + 'resumen_suelo_dia_19nov.csv'
    with open(T + '.tmp', 'w', newline='') as f:
        w = csv.writer(f, lineterminator='\n'); w.writerow(['dia', 'coin', 'w0_ms', 'w0_utc', 'n_filas', 'p5_ms', 'clase_estrato', 'causal_w0', 'p5_prev_h1', 'p5_prev_h2']); w.writerows(filas)
    os.replace(T + '.tmp', T)
    with open(R + '.tmp', 'w', newline='') as f:
        w = csv.writer(f, lineterminator='\n'); w.writerow(['dia', 'coin', 'n_lo', 'n_hi', 'n_indet', 'n_sin_datos', 'n_clasificadas', 'frac_lo', 'dia_valido']); w.writerows(res)
    os.replace(R + '.tmp', R)
    for p in (T, R): open(p.replace('.csv', '.sha256'), 'w').write(hashlib.sha256(open(p, 'rb').read()).hexdigest() + '  ' + os.path.basename(p) + '\n')
    print('dias', len(dias), 'filas', len(filas))
    por_dia = {}
    for r in res: por_dia.setdefault(r[0], []).append(r)
    for d, rr in por_dia.items(): print(d, ' '.join(f"{r[1]}:{r[7]}{'V' if r[8] else 'x'}" for r in rr))
if __name__ == '__main__': main()
