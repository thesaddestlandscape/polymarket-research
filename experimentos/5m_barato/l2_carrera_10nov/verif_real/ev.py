import pandas as pd, numpy as np, subprocess, collections, tempfile, os
H = os.path.dirname(os.path.abspath(__file__)) + '/'
R = pd.read_pickle(H + 'out/R_all.pkl'); R['cl'] = R.dia + '_' + (R.t_ini // 300000).astype(str)
def pnl(q, L, g): return q * (g - L) + q * 0.2 * 0.07 * L * (1 - L)
R['pr'] = pnl(R.real_q, R.L, R.gana); R['cr'] = R.real_q * R.L; R['ps'] = pnl(R.BASE_f_q, R.L, R.gana); R['cs'] = R.BASE_f_q * R.L
def boot(df, p, c, n=2000, seed=1):
    cl = df.groupby('cl')[[p, c]].sum(); a = cl.values; rng = np.random.default_rng(seed); ev = []
    for _ in range(n):
        i = rng.integers(0, len(a), len(a)); s = a[i].sum(0); ev.append(s[0] / s[1] if s[1] > 0 else np.nan)
    return np.nanpercentile(ev, [5, 95]).round(3).tolist()
def line(nm, df, p, c):
    s = df[[p, c]].sum(); return f'{nm}: n_orden={len(df)} fills={int((df[c] > 0).sum())} pnl={s[p]:.2f} coste={s[c]:.2f} EV/E={(s[p] / s[c] if s[c] > 0 else float("nan")):.3f} IC90clu={boot(df, p, c) if s[c] > 0 else None} pnl/orden colocada={s[p] / len(df):.4f}'
print('== TODAS 20-23 Oct (incondicional: sin relleno = 0)'); print(line('REAL', R, 'pr', 'cr')); print(line('SIM BASE', R, 'ps', 'cs'))
sm = R[(R.BASE_f_q > 0) & (R.real_q > 0)]; print(line('comun REAL', sm, 'pr', 'cr')); print(line('comun SIM', sm, 'ps', 'cs'))
print(line('solo-real (FN)', R[(R.BASE_f_q <= 0) & (R.real_q > 0)], 'pr', 'cr')); print(line('solo-sim (FP)', R[(R.BASE_f_q > 0) & (R.real_q <= 0)], 'ps', 'cs'))
print('dias positivos real:', (R.groupby('dia').pr.sum() > 0).sum(), 'de', R.dia.nunique(), R.groupby('dia').pr.sum().round(2).to_dict(), '| sim', R.groupby('dia').ps.sum().round(2).to_dict())
# respaldo L2 (23-Oct): reduccion de nivel L en +-1500 ms de tf (sim) / del print propio (real)
W = R[R.dia == '2026-10-23'].copy(); toks = set(W.tok.dropna().unique()); tf_ = tempfile.NamedTemporaryFile('w', suffix='.tok', delete=False, dir=H + 'out'); tf_.write('\n'.join(toks) + '\n'); tf_.close()
cmd = f"zcat /root/polymarket-research-datalogs/calibracion_etiqueta/l2_b23_libro5.csv.gz | awk -F, -v tf={tf_.name} 'BEGIN{{while((getline l<tf)>0)t[l]}} ($1==\"d\"||$1==\"B\"||$1==\"G\")&&($3 in t)'"
BK = collections.defaultdict(dict); RED = collections.defaultdict(list)
for line_ in subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, text=True, bufsize=1 << 20).stdout:
    q = line_.rstrip('\n').split(','); tk = q[2]; rx = int(q[6])
    if q[0] == 'G': BK[tk].clear(); continue
    if q[0] == 'B':
        BK[tk] = {}
        if q[3]:
            for kv in q[3].split(';'): a, b = kv.split(':'); BK[tk][int(round(float(a) * 100))] = float(b)
        continue
    if q[3] != 'B': continue
    pr = int(round(float(q[4]) * 100)); sz = float(q[5]); old = BK[tk].get(pr)
    if old is not None and sz < old - 1e-9: RED[tk].append((rx, pr))
    if sz > 0: BK[tk][pr] = sz
    else: BK[tk].pop(pr, None)
os.unlink(tf_.name)
def has_l2(tok, L, t): return any(p == int(round(L * 100)) and abs(rx - t) <= 1500 for rx, p in RED.get(tok, []))
W['l2_sim'] = [has_l2(r.tok, r.L, r.BASE_f_tf) if r.BASE_f_q > 0 else None for r in W.itertuples()]
W['l2_real'] = [has_l2(r.tok, r.L, r.t_own_print) if r.real_q > 0 and r.t_own_print > 0 else None for r in W.itertuples()]
print('== 23-Oct con L2: sim fills', int((W.BASE_f_q > 0).sum()), 'con respaldo L2', int((W.l2_sim == True).sum()), 'sin', int((W.l2_sim == False).sum()), '| real fills', int((W.real_q > 0).sum()), 'con L2', int((W.l2_real == True).sum()), 'sin', int((W.l2_real == False).sum()))
for nm, m in (('SIM con L2', W.l2_sim == True), ('SIM sin L2', W.l2_sim == False)): print(line(nm, W[m], 'ps', 'cs'))
for nm, m in (('REAL con L2', W.l2_real == True), ('REAL sin L2', W.l2_real == False)): print(line(nm, W[m], 'pr', 'cr'))
print(line('23-Oct REAL todas', W, 'pr', 'cr')); print(line('23-Oct SIM todas', W, 'ps', 'cs'))
