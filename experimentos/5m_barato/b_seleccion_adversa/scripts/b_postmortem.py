#!/usr/bin/env python3
"""b_postmortem.py [--ledger RUTA] [--hasta ISO] [--min-n 15] -- postmortem RE-EJECUTABLE por celdas de las pujas/rellenos REALES de B (H47-B) desde el ledger
experimento_h47_B_ledger.jsonl + desenlace oficial gamma (cache datos/b_des_cache.json). Solo lectura; no toca B.
Unidad = puja (mercado, lado). Por celda (moneda, T de relleno, banda de precio, hora UTC, cola, spread, dia, tanda de repegs): pujas, rellenos, tasa,
acierto relleno vs no relleno (seleccion adversa), EV ponderado por EUR (sum pnl / sum coste), IC90 bootstrap por MERCADO, EV sin las 2 mejores posiciones,
y p familiar (max-estadistico por permutacion de pujas entre celdas) de la diferencia celda-vs-resto. n<min-n => 'no concluye'. Si existen las unidades de
poblacion (datos/units) compara B con la poblacion en la misma celda. Salidas: stdout + datos/b_postmortem_<n>pujas.json."""
import sys, os, json, time, glob, argparse, requests
import numpy as np, pandas as pd
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ap = argparse.ArgumentParser(); ap.add_argument('--ledger', default='/root/polymarket-research-datalogs/experimento_h47_B_ledger.jsonl'); ap.add_argument('--hasta', default=None)
ap.add_argument('--min-n', type=int, default=15); ap.add_argument('--perms', type=int, default=2000); a = ap.parse_args()
CACHE = B + '/datos/b_des_cache.json'; des = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
first = {}; fin = {}; cfg = None
for l in open(a.ledger):
    try: r = json.loads(l)
    except Exception: continue
    if not r.get('real') or r.get('escalon') != 'B': continue
    if a.hasta and r.get('ts', '') > a.hasta: continue
    t = r.get('tipo')
    if t == 'puja_post': first.setdefault((r['slug'], r['lado']), r)
    elif t == 'puja_fin' and not r.get('interrumpida'): fin[(r['slug'], r['lado'])] = r      # un parcial de salida no es un cierre: el mercado queda fuera hasta tener el completo/reconstruido
slugs = sorted({k[0] for k in fin} - set(des))
ses = requests.Session()
for i in range(0, len(slugs), 40):
    for closed in ('true', 'false'):
        try: rs = ses.get('https://gamma-api.polymarket.com/markets', timeout=25, params=[('slug', s) for s in slugs[i:i + 40]] + [('closed', closed), ('limit', '40')]).json()
        except Exception as e: print('gamma', e, file=sys.stderr); continue
        for m in rs:
            pr = m.get('outcomePrices'); pr = json.loads(pr) if isinstance(pr, str) else pr
            if m.get('closed') and pr: des[m['slug']] = 'YES' if float(pr[0]) >= 0.999 else ('NO' if float(pr[1]) >= 0.999 else None)
json.dump(des, open(CACHE, 'w'))
def nm(v):
    v = [x for x in v if x is not None]
    return float(np.mean(v)) if v else np.nan
rows = []
for (slug, lado), f in fin.items():
    p0 = first.get((slug, lado), {}); st = int(slug.rsplit('-', 1)[1]); finm = st + 300; d = des.get(slug)
    rl = f.get('rellenos') or []; acc = sum(x['acc'] for x in rl); coste = sum(x['acc'] * x['precio'] for x in rl)
    bids = (p0.get('libro') or {}).get('bids') or [[np.nan, np.nan]]; asks = (p0.get('libro') or {}).get('asks') or [[np.nan, np.nan]]
    tf = nm([finm - x['t_deteccion'] if x.get('t_deteccion') else None for x in rl]); t0 = p0.get('t_dec', np.nan)
    win = np.nan if d is None else float(d == lado)
    rows.append(dict(slug=slug, coin=f['coin'].upper(), lado=lado, k=f['k'], n_ord=f['n_ordenes'], fin_puja=f['fin_puja'], filled=bool(rl), acc=acc, coste=coste, precio=(coste / acc if acc else np.nan),
                     p_post=p0.get('precio', np.nan), cola=p0.get('cola', np.nan), T0=p0.get('T', np.nan), T_fill=tf, spread0=asks[0][0] - bids[0][0], bidsz0=bids[0][1],
                     espera=nm([x.get('espera_s') for x in rl]), mo5=nm([x.get('markout_5s') for x in rl]),
                     mo30=nm([x.get('markout_30s') for x in rl]), win=win,
                     t_dec=t0, hora=(pd.to_datetime(finm - 150, unit='s').hour), dia=str(pd.to_datetime(finm - 150, unit='s').date()), fin=finm))
D = pd.DataFrame(rows).sort_values('fin').reset_index(drop=True); D['cum_n'] = np.arange(len(D))
n = len(D); print(f'B real: {n} pujas ({D.slug.nunique()} mercados), rellenas {int(D.filled.sum())} ({D.filled.mean():.3f}), sin desenlace {int(D.win.isna().sum())}')
D['c'] = D.coste; D['p'] = D.acc * D.win - D.coste
Fd = D[D.filled & D.win.notna()].copy()
Ud = D[~D.filled & D.win.notna()]
def boot(df, key='slug', nb=3000, seed=1):
    g = df.groupby(key)[['p', 'c']].sum()
    if len(g) < 2: return np.nan, np.nan
    r = np.random.default_rng(seed); i = r.integers(0, len(g), (nb, len(g))); e = g.p.values[i].sum(1) / np.maximum(g.c.values[i].sum(1), 1e-9); return np.quantile(e, .05), np.quantile(e, .95)
def cell(df, nm):
    f = df[df.filled & df.win.notna()]; u = df[~df.filled & df.win.notna()]
    if not len(f): return dict(celda=nm, pujas=len(df), rellenos=0, tasa=np.nan)
    ev = f.p.sum() / f.c.sum(); lo, hi = boot(f); s2 = f.sort_values('p', ascending=False).iloc[2:]
    return dict(celda=nm, pujas=len(df), rellenos=len(f), tasa=len(f) / len(df), win_f=f.win.mean(), win_nf=(u.win.mean() if len(u) else np.nan), precio=f.c.sum() / f.acc.sum(), EV=ev, lo=lo, hi=hi,
                EV_sin2=(s2.p.sum() / s2.c.sum() if len(s2) else np.nan), eur=f.c.sum(), mo5=f.mo5.mean(), concluye=len(f) >= a.min_n)
for _c in ('Tb','pb','hb','colab','spb','rep'): pass
Fd['Tb'] = pd.cut(Fd.T_fill, [0, 60, 120, 180, 240, 301]).astype(str); Fd['pb'] = pd.cut(Fd.precio, [0.09, 0.15, 0.20, 0.25, 0.31]).astype(str); Fd['hb'] = (Fd.hora // 4 * 4).astype(str)
Fd['colab'] = pd.cut(Fd.cola, [-1, 20, 60, 150, 1e9]).astype(str); Fd['spb'] = pd.cut(Fd.spread0, [-1, 0.021, 0.041, 1]).astype(str); Fd['rep'] = pd.cut(Fd.n_ord, [0, 1, 4, 10, 1e9]).astype(str)
D['Tb0'] = pd.cut(D.T0, [0, 120, 240, 301]).astype(str)
cells = []
tot = cell(D, 'TOTAL'); cells.append(tot)
for dim in ['coin', 'dia', 'hb', 'Tb', 'pb', 'colab', 'spb', 'rep']:
    for v, g in Fd.groupby(dim):
        ids = set(g.slug + g.lado); sub = D[(D.slug + D.lado).isin(ids) | (~D.filled)] if dim in ('coin',) else g
        cells.append(cell(g if dim != 'coin' else D[D.coin == v], f'{dim}={v}'))
# max-estadistico celda vs resto sobre rellenos (permutacion de etiquetas de celda no vale; permutamos desenlaces entre rellenos)
names = [c['celda'] for c in cells[1:] if c.get('rellenos', 0) >= a.min_n]
def cellmask(nm):
    dim, v = nm.split('=', 1); return (Fd[dim].astype(str) == v).values
M = np.array([cellmask(nm) for nm in names]) if names else np.zeros((0, len(Fd)), bool)
def tstats(pn, c, M):
    out = []
    for m in M:
        g1p, g1c, g0p, g0c = pn[m].sum(), c[m].sum(), pn[~m].sum(), c[~m].sum()
        if m.sum() < 2 or (~m).sum() < 2 or g1c <= 0 or g0c <= 0: out.append(0.0); continue
        e1, e0 = g1p / g1c, g0p / g0c; v1 = ((pn[m] - e1 * c[m]) ** 2).sum() / g1c ** 2; v0 = ((pn[~m] - e0 * c[~m]) ** 2).sum() / g0c ** 2; out.append((e1 - e0) / np.sqrt(v1 + v0 + 1e-12))
    return np.array(out)
pn, cc = Fd.p.values, Fd.c.values; t0 = tstats(pn, cc, M) if len(M) else np.array([]); rng = np.random.default_rng(3); mx = []
for _ in range(a.perms if len(M) else 0):
    j = rng.permutation(len(pn)); tt = tstats(pn[j], cc[j], M); mx.append(np.abs(tt).max())
pfw = {nm: (1 + np.sum(np.array(mx) >= abs(t))) / (len(mx) + 1) for nm, t in zip(names, t0)} if mx else {}
pd.set_option('display.width', 250); pd.set_option('display.max_rows', 200)
T = pd.DataFrame(cells); T['p_fw_vs_resto'] = T.celda.map(pfw)
print(T.round(3).to_string(index=False))
f = Fd
print('\nSELECCION ADVERSA a nivel de puja: acierto relleno %.3f (precio %.3f) vs no relleno %.3f (n=%d); markout 5 s mediana %.3f' % (f.win.mean(), f.c.sum() / f.acc.sum(), Ud.win.mean() if len(Ud) else np.nan, len(Ud), f.mo5.median()))
s = f.sort_values('p', ascending=False)
print('PnL %.2f  EV %.3f  sin las 2 mejores posiciones %.3f  (mejores: %s)' % (f.p.sum(), f.p.sum() / f.c.sum(), s.iloc[2:].p.sum() / s.iloc[2:].c.sum(), [round(x, 2) for x in s.p.head(3)]))
print('Dias independientes:', f.dia.nunique(), ' pnl por dia:', f.groupby('dia').p.sum().round(2).to_dict())
print('Regla de lectura: una celda solo es "potenciable"/"eliminable" si concluye (n>=%d), p_fw_vs_resto<0.10 y mantiene el signo en la mitad cronologica posterior; todo lo demas es EXPLORATORY.' % a.min_n)
h = len(f) // 2; print('Mitades cronologicas EV: 1a %.3f  2a %.3f' % (f.iloc[:h].p.sum() / f.iloc[:h].c.sum(), f.iloc[h:].p.sum() / f.iloc[h:].c.sum()))
T.to_json(B + f'/datos/b_postmortem_{n}pujas.json', orient='records', indent=1)
