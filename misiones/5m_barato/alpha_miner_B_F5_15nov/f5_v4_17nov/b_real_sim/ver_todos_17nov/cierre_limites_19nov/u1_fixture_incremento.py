"""u1_fixture_incremento.py -- fixture de la regla R1 (bloqueo = INCREMENTO del nivel 1-L del complementario). Solo lectura, 0 ordenes.
Verdad on-chain: 202 rellenos reales B 20-23 Oct (tomador_202.pkl: tk_eq, tk_sz, tk_rem en ACCIONES, real_tm3 = sello exchange del print). L2 de bids: cola_vs_cruce/mk (20-22 Oct).
Poblacion: compra_comp (el tomador compra el COMPLEMENTARIO: su resto, si lo hay, queda en el bid del complementario a 1-tk_eq). rem_sh = tk_rem*tk_sz = acciones que NO casaron.
Pruebas: (a) hay un incremento positivo del nivel P=1-tk_eq con rx en [t3-50,t3+500] cuyo Delta = rem_sh (tol max(2%,0,05 acc)) -> la regla incremento aisla la orden en reposo del tomador;
 (b) mismo test en nivel +-1 tick y con ventana desplazada +-10/20/30 s (placebos) ; (c) factor cota = tamano total del nivel tras el evento / Delta (cuanto sobreestima el nivel entero)."""
import sys, numpy as np, pandas as pd
sys.path.insert(0, '../solo_observable_19nov'); import so1_traza as S
d = pd.read_pickle(S.BASE + 'tomador_202.pkl'); d['rem_sh'] = d.tk_rem * d.tk_sz
d = d[(d.tk_tipo == 'compra_comp') & (d.tk_rem > 0.01)]
rows = []; cache = {}
def incs(ser, t0, t1):
    if ser is None: return np.array([]), np.array([])
    t, s = ser; prev = np.concatenate([[0.0], s[:-1]]); m = (t >= t0) & (t <= t1)
    return (s[m] - prev[m]), s[m]
for r in d.itertuples():
    m = S.TOKM.get(str(r.tok))
    if m is None: continue
    import os
    fn = S.MK + f'{m[0]}_{m[1]}.gz'
    if not os.path.exists(fn): continue
    if fn not in cache:
        if len(cache) > 6: cache.pop(next(iter(cache)))
        cache[fn] = S.parse(fn)
    B = cache[fn]; comp = 'N' if m[2] == 'YES' else 'Y'; t3 = int(r.real_tm3); P = int(round((1.0 - float(r.tk_eq)) * 100)) * 10
    tol = max(0.02 * r.rem_sh, 0.05)
    def hit(p, sh):
        dl, lv = incs(B[comp].get(p), t3 + sh - 50, t3 + sh + 500); ok = np.where(np.abs(dl - r.rem_sh) <= tol)[0]
        return (len(ok) > 0), (float(lv[ok[0]] / dl[ok[0]]) if len(ok) else np.nan)
    h0, fac = hit(P, 0)
    pl_lv = [hit(P + o, 0)[0] for o in (-10, 10)]; pl_t = [hit(P, s)[0] for s in (-30000, -20000, -10000, 10000, 20000, 30000)]
    dl, _ = incs(B[comp].get(P), t3 - 50, t3 + 500)
    rows.append(dict(oid=r.oid, dia=r.dia, rem_sh=r.rem_sh, hit=h0, fac=fac, pl_nivel=np.mean(pl_lv), pl_t=np.mean(pl_t), pl_t_max=max(pl_t), n_inc_pos=int((dl > 0).sum())))
X = pd.DataFrame(rows)
print('n =', len(X), '(compra_comp, rem>1%, con L2 mk)')
print('hit exacto Delta=rem_sh en nivel 1-tk_eq: %.3f' % X.hit.mean(), '| placebo nivel+-1tick: %.3f' % X.pl_nivel.mean(), '| placebo ventana +-10/20/30 s: media %.3f max-por-shift(any) %.3f' % (X.pl_t.mean(), X.pl_t_max.mean()))
print('con incremento positivo cualquiera en ventana: %.3f' % (X.n_inc_pos > 0).mean())
f = X.fac.dropna(); print('factor cota (nivel total tras evento / Delta) cuando hit: n=%d mediana %.2f p90 %.2f' % (len(f), f.median(), f.quantile(.9)))
X.to_csv('out/u1_fixture_incremento.csv', index=False)
