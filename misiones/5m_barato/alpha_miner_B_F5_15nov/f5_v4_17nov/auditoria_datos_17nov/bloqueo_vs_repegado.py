#!/usr/bin/env python3
"""Solo lectura. Cruza bloqueos del ledger real de B (20-23 Oct) con ordenes/puja. Intervalo de bloqueo = [ts del evento bloqueo_*, siguiente intencion_post real) (el ledger solo registra la TRANSICION a bloqueado: _log_bloqueo experimento_pares_cola_15m.py:839-842)."""
import json, collections, numpy as np, pandas as pd, datetime as dt
DL = '/root/polymarket-research-datalogs/'; ts = lambda s: dt.datetime.fromisoformat(s).timestamp()
ev = []; 
for ln in open(DL + 'experimento_h47_B_ledger.jsonl'):
    try: e = json.loads(ln)
    except Exception: continue
    if e.get('real') is False: continue
    ev.append((ts(e['ts']), e.get('tipo'))) if e.get('ts') and e.get('tipo') in ('bloqueo_suelo_saldo', 'bloqueo_coste_orden', 'bloqueo_suelo_no_fijado', 'bloqueo_saldo_ilegible', 'bloqueo_alza_saldo_sin_confirmar', 'bloqueo_tamano', 'bloqueo_min_size_mercado', 'intencion_post', 'config') else None
ev.sort(); O = pd.read_csv(DL + 'calibracion_etiqueta/ordenes_b.csv'); t0, t1 = O.t_dec.min() - 3600, O.t_dec.max() + 3600
ev = [x for x in ev if t0 <= x[0] <= t1]; print('tipos', collections.Counter(x[1] for x in ev))
posts = np.array([x[0] for x in ev if x[1] == 'intencion_post']); iv = []
for t, tp in ev:
    if tp.startswith('bloqueo'):
        j = np.searchsorted(posts, t, side='right'); iv.append((t, posts[j] if j < len(posts) else t, tp))
iv = pd.DataFrame(iv, columns=['a', 'b', 'tipo']); iv['dur'] = iv.b - iv.a
print('bloqueos', len(iv), 'duracion s p10/p50/p90/max', iv.dur.quantile([.1, .5, .9]).round(1).tolist(), round(iv.dur.max(), 1), 'suma s', round(iv.dur.sum()), 'por tipo', iv.groupby('tipo').dur.agg(['size', 'sum']).round(0).to_dict())
# fusionar intervalos (union)
iv = iv.sort_values('a'); U = []; 
for a, b in zip(iv.a, iv.b):
    if U and a <= U[-1][1]: U[-1][1] = max(U[-1][1], b)
    else: U.append([a, b])
U = np.array(U); print('union s', round((U[:, 1] - U[:, 0]).sum()), 'en', len(U), 'tramos; tiempo B vivo (ventanas de puja) s', None)
def ovl(a, b):
    if len(U) == 0: return 0.0
    return float(np.clip(np.minimum(U[:, 1], b) - np.maximum(U[:, 0], a), 0, None).sum())
O = O.sort_values(['puja', 't_dec']); G = O.groupby('puja').agg(n=('oid', 'size'), a=('t_dec', 'min'), b=('t_cancel_int', 'max'), fill=('fill', 'max'), coin=('coin', 'first'), dia=('dia', 'first'), T0=('T', 'max'), Tm=('T', 'min'))
G['dur'] = G.b - G.a; G['blk'] = [ovl(a, b) for a, b in zip(G.a, G.b)]; G['con_blq'] = G.blk > 0
# gaps entre ordenes consecutivas y su solape con bloqueo
O['prev_c'] = O.groupby('puja').t_cancel_int.shift(); O['gap'] = O.t_dec - O.prev_c; O['gap_blk'] = [ovl(a, b) if pd.notna(a) else np.nan for a, b in zip(O.prev_c, O.t_dec)]
def r(x): return round(float(x), 2)
print('REAL pujas', len(G), 'ord/puja', r(G.n.mean()), 'sin relleno', r(G.n[G.fill == 0].mean()), 'con relleno', r(G.n[G.fill == 1].mean()))
for nm, g in (('SIN bloqueo en su vida', G[~G.con_blq]), ('CON bloqueo en su vida', G[G.con_blq])):
    s = g[g.fill == 0]; print(nm, 'pujas', len(g), 'ord/puja', r(g.n.mean()), '| sin relleno', len(s), r(s.n.mean()), '| duracion s', r(s.dur.mean()), '| ord por 100 s vivos (sin relleno)', r(100 * s.n.sum() / s.dur.sum()), '| frac. del puja bloqueado', r((g.blk.sum() / g.dur.sum())))
gp = O.dropna(subset=['gap']); print('gaps entre ordenes: n', len(gp), 'mediana', r(gp.gap.median()), '| con solape de bloqueo', int((gp.gap_blk > 0).sum()), 'mediana', r(gp[gp.gap_blk > 0].gap.median()), 'suma s', r(gp[gp.gap_blk > 0].gap.sum()), '| sin', r(gp[gp.gap_blk == 0].gap.median()), 'suma s', r(gp[gp.gap_blk == 0].gap.sum()))
print('vida orden (t_dec->t_cancel_int) mediana: con bloqueo', r((O.t_cancel_int - O.t_dec)[O.puja.isin(G.index[G.con_blq])].median()), 'sin', r((O.t_cancel_int - O.t_dec)[O.puja.isin(G.index[~G.con_blq])].median()))
# ajuste: quitar el tiempo bloqueado -> ordenes equivalentes por puja
s = G[G.fill == 0]; print('sin relleno: tasa ord/s vivo no bloqueado', r(s.n.sum() / (s.dur - s.blk).sum()), '; ord/puja de 238 s a esa tasa', r(238 * s.n.sum() / (s.dur - s.blk).sum()))
print('por dia ord/puja', G.groupby('dia').n.mean().round(1).to_dict(), 'frac pujas con bloqueo', G.groupby('dia').con_blq.mean().round(2).to_dict())
print('por moneda ord/puja', G.groupby('coin').n.mean().round(1).to_dict())
G.to_csv('bloqueo_vs_repegado_pujas.csv'); iv.to_csv('bloqueo_intervalos.csv', index=False)
