import sys, numpy as np
from scipy import stats
sys.argv = ['x']
import r5
D = ['2026-10-%02d' % d for d in range(5, 28)]
R = np.stack([np.load('simout/r_%s.npz' % d)['R'] for d in D])
FLOW = 266344.0
ia = list(range(0, 21)); iv = [21, 22]; i1 = list(range(0, 11)); i2 = list(range(11, 21))
labs = [r5.vlabel(v) for v in range(456)]
def ic(r):
    r = np.asarray(r, float); r = r[np.isfinite(r)]
    if len(r) < 2: return (float('nan'),) * 3 + (0, len(r))
    m = r.mean(); h = stats.t.ppf(0.95, len(r) - 1) * r.std(ddof=1) / np.sqrt(len(r))
    return m, m - h, m + h, int((r > 0).sum()), len(r)
def st(v, ni, idx):
    c = R[idx, v, ni, 1]; p = R[idx, v, ni, 2]; t = R[idx, v, ni, 0]; e = R[idx, v, ni, 3]
    r = np.where(c > 0, p / np.maximum(c, 1e-12), np.nan)
    return p.sum() / max(c.sum(), 1e-12), ic(r), e.mean(), t.mean(), p.mean()
print('== 1. VARIANTES: v057 = elegida prerregistrada en IS; el resto = 7 mejores OOS descriptivas (POST-HOC, solo diagnostico). EV/E bruto de comision, pesado por EUR; dias 05-25 (21)')
print('variante | N | EV agregado | dia medio [IC90 por dias] dias+ | ejec/dia acc/dia cuota%S800-BTC pnl EUR/anio | DEV 26-27 EV/E por dia')
for v in (57, 211, 258, 252, 260, 228, 254, 234):
    for ni, N in ((0, 5), (2, 20), (3, 50)):
        ev, (m, lo, hi, pp, n), e, t, pn = st(v, ni, ia)
        dv = R[iv, v, ni, 2] / np.maximum(R[iv, v, ni, 1], 1e-12)
        print('v%03d %-44s N=%2d | %+.3f | %+.3f [%+.3f,%+.3f] %d/%d | %4.0f %6.0f %5.2f%% %+7.0f | %s' % (v, labs[v][:44], N, ev, m, lo, hi, pp, n, e, t, 100 * t / FLOW, pn * 365, ' '.join('%+.2f' % x for x in dv)))
gate = ((R[i1, :, 2, 1] > 0).mean(0) >= 0.8) & (R[i1, :, 2, 3].mean(0) >= 100)
def evp(idx): return R[idx, :, 2, 2].sum(0) / np.maximum(R[idx, :, 2, 1].sum(0), 1e-12)
eI, eO, eD = evp(i1), evp(i2), evp(iv)
S = lambda f: np.array([f(l) for l in labs])
isS = S(lambda l: l.startswith('S ')); isA = S(lambda l: l.startswith('SIEMPRE'))
print('\n== 2. SUBFAMILIAS: EV agregado medio a N=20 de las variantes y %% con EV>0, por tramo (IS 05-15 | OOS 16-25 | DEV 26-27)')
rows = [('todas las S de la compuerta', gate & isS), ('S th400', gate & isS & S(lambda l: 'th400' in l)), ('S th800', gate & isS & S(lambda l: 'th800' in l)), ('S th1600', gate & isS & S(lambda l: 'th1600' in l)),
        ('S T60-290', gate & isS & S(lambda l: 'T60-290' in l)), ('S T120-240', gate & isS & S(lambda l: 'T120-240' in l)),
        ('S th800 T120-240', gate & isS & S(lambda l: 'th800' in l and 'T120-240' in l)), ('S th800 T60-290', gate & isS & S(lambda l: 'th800' in l and 'T60-290' in l)),
        ('S TD0', gate & isS & S(lambda l: ' TD0 ' in l)), ('S TD1', gate & isS & S(lambda l: ' TD1 ' in l)),
        ('S d+0.01 (cola 0)', gate & isS & S(lambda l: 'd+0.01' in l)), ('S d+0.00 (cola visible)', gate & isS & S(lambda l: 'd+0.00' in l)), ('S d-0.01 (solo travesia)', gate & isS & S(lambda l: 'd-0.01' in l)),
        ('S b0.10', gate & isS & S(lambda l: 'b0.10' in l)), ('S b0.20', gate & isS & S(lambda l: 'b0.20' in l)), ('SIEMPRE (sin S, sin compuerta)', isA)]
for name, m in rows:
    if m.sum() == 0: print('%-34s n=0' % name); continue
    print('%-34s n=%3d | EV medio %+.3f %+.3f %+.3f | EV>0: %5.1f %% %5.1f %% %5.1f %%' % (name, m.sum(), eI[m].mean(), eO[m].mean(), eD[m].mean(), 100 * (eI[m] > 0).mean(), 100 * (eO[m] > 0).mean(), 100 * (eD[m] > 0).mean()))
a800 = [0.381, 0.0, 0.090, 0.129, 0.078, 0.255, 0.089, -0.231, -0.110, -0.030, 0.374, 0.187]
d0625 = [-0.008, 0.595, -0.235, -0.078, 0.258, -0.024, 0.186, 0.297, 0.381, 0.0, 0.090, 0.129, 0.078, 0.255, 0.089, -0.231, -0.110, -0.030, 0.374, 0.187]
print('\n== 3. S800 todas las monedas, dEV/E diario (tabla s1 de salida_suite_final.txt, redondeado a 3 decimales)')
for nm, a in (('14-25 Oct = walk-forward con S800 fijo SIN los dias 26-27', a800), ('06-25 Oct (20 dias, sin los 2 de descubrimiento)', d0625), ('06-08 Oct (frescos, 3 dias)', d0625[:3])):
    m, lo, hi, pp, n = ic(a); print('   %-60s media %+.3f IC90[%+.3f,%+.3f] dias+ %d/%d' % (nm, m, lo, hi, pp, n))
