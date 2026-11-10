import pandas as pd, numpy as np, glob, subprocess, tempfile, collections, os
H = os.path.dirname(os.path.abspath(__file__)) + '/'
R = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H + 'out/V_*.pkl'))], ignore_index=True); R = R[R['cov'] == 'ok'].copy()
BF = pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str}, usecols=['oid', 'tok', 't_cancel_int']); R = R.merge(BF, on='oid', how='left'); R['t_cx'] = np.where(R.t_cancel_int.notna(), (R.t_cancel_int * 1000).fillna(0).astype('int64'), R.t_fuera)
R['vida'] = (R.t_fuera - R.t_ini) / 1000
# ---- E_comp / E_self (print WS): primer print en vida -> ya en R (t_comp, t_self); tf-like = t-63
def stats(x, name, mask):
    x = x[mask]; return f'{name}: n={len(x)}'
real = R[R.real_fill == 1]
print('REALES n', len(real), 'con print comp (>=1-L) en vida+250ms', int((real.t_comp > 0).sum()), 'self sale<=L', int((real.t_self > 0).sum()), 'cualquiera', int((real.t_prn_any > 0).sum()))
ra = real[real.t_own_print > 0]
print('anclas propias emparejadas (print WS del tx propio) n', len(ra), 'src', ra.own_src.value_counts().to_dict())
d1 = (ra.t_comp - ra.t_own_print)[ra.t_comp > 0]; print('E_comp(primer print comp en vida) - print propio: n', len(d1), d1.describe(percentiles=[.05,.25,.5,.75,.95]).round(0).to_dict(), 'exacto<=100ms', round(float((d1.abs() <= 100).mean()), 3), '<=200', round(float((d1.abs() <= 200).mean()), 3))
d2 = (ra.t_prn_any - ra.t_own_print)[ra.t_prn_any > 0]; print('E_any - print propio: n', len(d2), 'exacto<=100ms', round(float((d2.abs() <= 100).mean()), 3), 'mediana', float(d2.median()))
# real: el relleno cae dentro de la vida? hora de fill real (print propio) en [t_ini,t_fuera]
print('print propio dentro de vida [t_ini,t_fuera+250]', round(float(((ra.t_own_print >= ra.t_ini) & (ra.t_own_print <= ra.t_fuera + 250)).mean()), 3), 'n', len(ra))
# precision por evento: P(real fill | evento en vida)
for col, nm in (('t_comp', 'E_comp'), ('t_self', 'E_self'), ('t_prn_any', 'E_any')):
    m = R[col] > 0; print(nm, 'ordenes con evento', int(m.sum()), 'de ellas rellenadas', int(R[m].real_fill.sum()), 'P(fill|evento)', round(float(R[m].real_fill.mean()), 3), '| sin evento', int((~m).sum()), 'rellenadas', int(R[~m].real_fill.sum()))
# ---- L2 (solo 23-Oct 04:36-09:15Z, calibracion_etiqueta/l2_b23_libro5.csv.gz) -> reducciones de nivel L
W = R[R.dia == '2026-10-23']; toks = set(W.tok.unique()); tf_ = tempfile.NamedTemporaryFile('w', suffix='.tok', delete=False, dir=H + 'out'); tf_.write('\n'.join(toks) + '\n'); tf_.close()
cmd = f"zcat /root/polymarket-research-datalogs/calibracion_etiqueta/l2_b23_libro5.csv.gz | awk -F, -v tf={tf_.name} 'BEGIN{{while((getline l<tf)>0)t[l]}} ($1==\"d\"||$1==\"B\"||$1==\"G\")&&($3 in t)'"
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, text=True, bufsize=1 << 20)
BK = collections.defaultdict(dict); RED = collections.defaultdict(list); rxmin = None; rxmax = None; nrows = 0
for line in p.stdout:
    q = line.rstrip('\n').split(','); nrows += 1; tk = q[2]; rx = int(q[6]); rxmin = rx if rxmin is None else min(rxmin, rx); rxmax = rx if rxmax is None else max(rxmax, rx)
    if q[0] == 'G':
        BK[tk].clear(); continue
    if q[0] == 'B':
        BK[tk] = {}
        if q[3]:
            for kv in q[3].split(';'):
                a, b = kv.split(':'); BK[tk][int(round(float(a) * 100))] = float(b)
        continue
    if q[3] != 'B': continue
    pr = int(round(float(q[4]) * 100)); sz = float(q[5]); old = BK[tk].get(pr)
    if old is not None and sz < old - 1e-9: RED[tk].append((rx, pr, old, sz))
    if sz > 0: BK[tk][pr] = sz
    else: BK[tk].pop(pr, None)
os.unlink(tf_.name)
print('L2 filas', nrows, 'rx rango', pd.to_datetime(rxmin, unit='ms'), pd.to_datetime(rxmax, unit='ms'))
W = W[(W.t_ini >= rxmin) & (W.t_fuera <= rxmax)].copy(); print('ordenes 23-Oct dentro del rango L2', len(W), 'reales', int(W.real_fill.sum()))
def first_red(r):
    ev = [x for x in RED.get(r.tok, []) if x[1] == int(round(r.L * 100)) and r.t_ini < x[0] <= r.t_cx]
    return ev[0][0] if ev else -1
W['t_l2'] = W.apply(first_red, axis=1)
wr = W[W.real_fill == 1]
print('L2 reducciones de L: reales con evento', int((wr.t_l2 > 0).sum()), 'de', len(wr), '| ordenes con evento', int((W.t_l2 > 0).sum()), 'rellenadas', int(W[W.t_l2 > 0].real_fill.sum()), 'P(fill|evento)', round(float(W[W.t_l2 > 0].real_fill.mean()), 3))
wra = wr[wr.t_own_print > 0]; dl = (wra.t_l2 - wra.t_own_print)[wra.t_l2 > 0]
print('E_L2 - print propio (n=%d):' % len(dl), dl.describe(percentiles=[.05,.25,.5,.75,.95]).round(0).to_dict() if len(dl) else '')
W['hib'] = np.where(W.t_l2 > 0, W.t_l2, np.where(W.t_comp > 0, W.t_comp - 63, -1)); wh = W[(W.real_fill == 1)]
print('HIBRIDO (L2 si hay, si no print comp-63) cobertura reales', int((wh.hib > 0).sum()), 'de', len(wh), 'desde L2', int((wh.t_l2 > 0).sum()), 'desde comp', int(((wh.t_l2 <= 0) & (wh.t_comp > 0)).sum()))
wha = wh[(wh.t_own_print > 0) & (wh.hib > 0)]; dh = wha.hib - (wha.t_own_print - 63)
print('hibrido - (print propio-63): n', len(dh), dh.describe(percentiles=[.05,.25,.5,.75,.95]).round(0).to_dict())
for nm, m in (('L2', wha.t_l2 > 0), ('comp', (wha.t_l2 <= 0) & (wha.t_comp > 0))):
    x = dh[m]; print('  tramo', nm, 'n', len(x), 'med', float(x.median()) if len(x) else None, '|d|<=50ms', round(float((x.abs() <= 50).mean()), 3) if len(x) else None, '<=100', round(float((x.abs() <= 100).mean()), 3) if len(x) else None, '<=200', round(float((x.abs() <= 200).mean()), 3) if len(x) else None)
R.to_pickle(H + 'out/R_all.pkl')
