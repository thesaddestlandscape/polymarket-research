#!/usr/bin/env python3
"""s4_analisis.py -- PREREG_W2 (sha 7b3c5e4c…). P1 cuota CON, P2 lado contrario/mercado, P4 descomposicion. Salida w2_btc/an_w2.txt
Entradas w2_btc/feats_btc_M.csv.gz (s3) y w2_btc/fills_btc_all.csv.gz (s2). nice/ionice, ulimit -v 3000000, >=09:00Z."""
import os, sys, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); OUT = '/root/polymarket-research-datalogs/w2_btc'
assert hashlib.sha256(open(os.path.join(AQ, '..', 'PREREG_W2.md'), 'rb').read()).hexdigest().startswith('7b3c5e4c')
rng = np.random.default_rng(20261023); NPERM = int(os.environ.get('NPERM', 1000)); out = []
def P(*a): out.append(' '.join(str(x) for x in a)); print(out[-1], flush=True)
W21 = '0x21f4c1a1'; CTRL = ['0xaa1a4f31', '0x41e2e1cc']
IND = ['r300', 'r60', 'r900', 'rop', 'rpre', 'b15', 'f60']
F = pd.read_csv(os.path.join(OUT, 'feats_btc_M.csv.gz'), dtype={'wallet': str}, usecols=['dia', 'ts', 'wallet', 'mid', 'fin', 'lado_ef', 'px_ef', 'acc', 'des', 'T', 'r60', 'r300', 'r900', 'rop', 'rpre', 'b15', 'f60', 'mid5_t0', 'mid5_f'])
for c in ['r60', 'r300', 'r900', 'rop', 'rpre', 'b15', 'f60', 'mid5_t0', 'mid5_f', 'ts']: F[c] = F[c].astype(np.float32) if c != 'ts' else F[c]
F['gana'] = (F.lado_ef == F.des).astype(np.float32); F['coste'] = F.acc * F.px_ef; F['pnl'] = F.acc * (F.gana - F.px_ef)
F['per'] = np.where(F.dia <= '2026-10-19', 'DESC', 'TEST'); F['pxb'] = (F.px_ef / 0.1).astype(np.int8); F['pxb5'] = (F.px_ef / 0.05).astype(np.int8); F['Tb'] = (F['T'] // 60).clip(0, 4).astype(np.int8)
for c in IND: F['s_' + c] = np.where(np.isnan(F[c]) | (F[c] == 0), np.nan, (F[c] > 0).astype(float)).astype(np.float32)
isW = F.wallet.str.startswith(W21).values; Wd = F[isW].copy(); Od = F[~isW]; del F; import gc; gc.collect(); F = Od; Fall = pd.concat([Od, Wd], ignore_index=True)
P(f'Fills M BTC 5m px_ef 0,1-0,9 17-21 Oct: {len(F)}; wallets {F.wallet.nunique()}; wallet {W21}: {len(Wd)} fills, {Wd.mid.nunique()} mercados, acc medio {Wd.acc.mean():.2f}, px_ef medio {Wd.px_ef.mean():.3f}, EV {Wd.pnl.sum()/Wd.coste.sum():+.4f}; otros n {len(Od)} EV {Od.pnl.sum()/Od.coste.sum():+.4f}')
P('cobertura indicadores wallet:', Wd[IND].notna().mean().round(3).to_dict()); P('cobertura por dia (r300, rpre, b15):'); P(Wd.groupby('dia')[['r300', 'rpre', 'b15']].agg(lambda x: x.notna().mean()).round(3).to_string())
def ci_ratio(num, den, cl, nb=1000):
    d = pd.DataFrame({'n': num, 'd': den, 'c': cl}).dropna(); g = d.groupby('c')[['n', 'd']].sum(); a, b = g.n.values, g.d.values; m = len(g)
    if m < 5: return (np.nan, np.nan)
    r = np.empty(nb)
    for i in range(nb):
        j = rng.integers(0, m, m); r[i] = a[j].sum() / max(b[j].sum(), 1e-12)
    return tuple(np.percentile(r, [5, 95]))
def expected(Wsub, Osub, s):
    """cuota CON esperada: otros makers en el mismo (mid, pxb)."""
    g = Osub.groupby(['mid', 'pxb'])[s].agg(['sum', 'count']); key = pd.MultiIndex.from_frame(Wsub[['mid', 'pxb']])
    gs = g['sum'].reindex(key).values; gc = g['count'].reindex(key).values
    return np.where(gc > 0, gs / np.where(gc > 0, gc, 1), np.nan)
# ---------------- P1
def p1(wallet_prefix, label, placebo=False):
    Wx = Fall[Fall.wallet.str.startswith(wallet_prefix)]; Ox = Fall[~Fall.wallet.str.startswith(wallet_prefix)]
    P(f'\n===== P1 cuota CON: {label} ({wallet_prefix}): fills {len(Wx)}, mercados {Wx.mid.nunique()}')
    rows = []; res = {}
    for c in IND:
        s = 's_' + c; r = {'ind': c}
        for per in ('DESC', 'TEST'):
            w = Wx[Wx.per == per]; o = Ox[Ox.per == per]; e = expected(w, o, s); dif = w[s].values - e; ok = ~np.isnan(dif)
            lo, hi = ci_ratio(dif[ok], np.ones(ok.sum()), w.fin.values[ok]) if ok.sum() > 50 else (np.nan, np.nan)
            wt = w.acc.values[ok]; difw = (dif[ok] * wt).sum() / wt.sum() if ok.sum() else np.nan
            r[f'cw_{per}'] = np.nanmean(w[s]); r[f'exp_{per}'] = np.nanmean(e[ok]) if ok.sum() else np.nan; r[f'dif_{per}'] = np.nanmean(dif); r[f'ic_{per}'] = f'({lo*100:+.1f},{hi*100:+.1f})pp'; r[f'difW_{per}'] = difw; r[f'n_{per}'] = int(ok.sum())
        rows.append(r); res[c] = r['dif_TEST'] * np.sign(r['dif_DESC'] if r['dif_DESC'] == r['dif_DESC'] else 1)
    T = pd.DataFrame(rows); P(T.round(3).to_string(index=False))
    if not placebo: return T
    # placebo: reasignar la etiqueta wallet a fills de otros makers con el mismo n por (mid,pxb) (con reemplazo, leave-one-out) -- TEST
    w = Wx[Wx.per == 'TEST']; o = Ox[Ox.per == 'TEST'].copy(); o['g'] = o.groupby(['mid', 'pxb']).ngroup(); o = o.sort_values('g').reset_index(drop=True)
    cnt = o.groupby('g').size(); start = np.concatenate([[0], np.cumsum(cnt.values)[:-1]]); startS = pd.Series(start, index=cnt.index); cntS = cnt
    gw = pd.MultiIndex.from_frame(w[['mid', 'pxb']]); gmap = o.drop_duplicates('g').set_index(['mid', 'pxb']).g
    gi = gmap.reindex(gw).values; okg = ~np.isnan(gi); gi = gi[okg].astype(int); st = startS.reindex(gi).values; cn = cntS.reindex(gi).values
    obs = {c: float(T.loc[T.ind == c, 'dif_TEST'].iloc[0]) for c in IND}; sgn = {c: np.sign(float(T.loc[T.ind == c, 'dif_DESC'].iloc[0])) or 1.0 for c in IND}
    S = {}; C = {}
    for c in IND:
        s = o['s_' + c].values; okc = ~np.isnan(s); g = o.g.values
        S[c] = (np.bincount(g[okc], weights=s[okc], minlength=len(cnt)), np.bincount(g[okc], minlength=len(cnt)).astype(float), s)
    M = np.empty((NPERM, len(IND)))
    for p in range(NPERM):
        pos = (st + np.floor(rng.random(len(st)) * cn)).astype(int)
        for j, c in enumerate(IND):
            gs, gc, s = S[c]; sd = s[pos]; ok = ~np.isnan(sd); g_ = gi
            exp = (gs[g_] - np.where(ok, sd, 0)) / np.where(gc[g_] - ok > 0, gc[g_] - ok, np.nan)
            M[p, j] = np.nanmean((sd - exp)[ok])
    for j, c in enumerate(IND):
        pc = (M[:, j] * sgn[c] >= obs[c] * sgn[c]).mean()
        pm = (np.max(M * np.array([sgn[k] for k in IND]), axis=1) >= obs[c] * sgn[c]).mean()
        P(f'  placebo TEST {c}: obs {obs[c]*100:+.2f} pp, placebo medio {M[:, j].mean()*100:+.2f} (sd {M[:, j].std()*100:.2f}); p una cola (sentido DESC) {pc:.3f}; p max-estadistico {pm:.3f}')
    return T
p1(W21, 'WALLET', placebo=True)
for w in CTRL: p1(w, 'CONTROL')
# resumen por dia (r300 y rpre): cuota CON wallet vs esperada
P('\n== P1 por dia (dif cuota CON wallet - esperada, pp)')
for c in ('r300', 'rpre', 'r900'):
    s = 's_' + c; vals = []
    for d, w in Wd.groupby('dia'):
        o = Od[Od.dia == d]; e = expected(w, o, s); dif = w[s].values - e; vals.append(f'{d[5:]}: {np.nanmean(dif)*100:+.1f}')
    P('  ' + c + ': ' + ' | '.join(vals))
# ---------------- P2: tamano y lado a nivel mercado
P('\n===== P2 tamano de fill / nº fills por (mercado,lado) segun CON/CONTRA (wallet vs otros)')
for c in ('r300', 'rpre', 'rop'):
    s = 's_' + c
    for nm, D in (('wallet', Wd), ('otros', Od)):
        a = D[D[s] == 1]; b = D[D[s] == 0]
        nfa = a.groupby(['mid', 'lado_ef']).size().mean(); nfb = b.groupby(['mid', 'lado_ef']).size().mean()
        P(f'  {c} {nm}: acc medio CON {a.acc.mean():.2f} CONTRA {b.acc.mean():.2f} | n fills por (mercado,lado) CON {nfa:.1f} CONTRA {nfb:.1f} | n CON {len(a)} CONTRA {len(b)}')
# mercado: cuota de acciones en el lado a favor de la tendencia previa
def mkt_table(D):
    D = D.dropna(subset=['rpre']); D = D.assign(up=D.rpre * np.where(D.lado_ef == 'YES', 1, -1))
    g = D.groupby('mid'); m = g.agg(fin=('fin', 'first'), dia=('dia', 'first'), up=('up', 'median'))
    q = D.pivot_table(index='mid', columns='lado_ef', values='acc', aggfunc='sum', fill_value=0)
    for c in ('YES', 'NO'):
        if c not in q: q[c] = 0.0
    m = m.join(q); m['Q'] = m.YES + m.NO; m['shareUp'] = m.YES / m.Q; return m[m.Q > 0]
Mw = mkt_table(Wd); Mo = mkt_table(Od)
Mw = Mw.join(Mo[['shareUp']].rename(columns={'shareUp': 'shareUp_o'}), how='left')
Mw = Mw[(Mw.up != 0) & Mw.shareUp_o.notna()]
Mw['con_w'] = np.where(Mw.up > 0, Mw.shareUp, 1 - Mw.shareUp); Mw['con_o'] = np.where(Mw.up > 0, Mw.shareUp_o, 1 - Mw.shareUp_o); Mw['dif'] = Mw.con_w - Mw.con_o
Mw['per'] = np.where(Mw.dia <= '2026-10-19', 'DESC', 'TEST')
P(f'\n===== P2 mercado: parte de acciones en el lado A FAVOR de la tendencia previa (rpre) -- wallet vs el resto de makers del MISMO mercado; n mercados {len(Mw)}')
for per in ('DESC', 'TEST'):
    x = Mw[Mw.per == per]; lo, hi = ci_ratio(x['dif'].values, np.ones(len(x)), x.fin.values)
    P(f'  {per}: n {len(x)} cuota CON wallet {x.con_w.mean():.3f} otros {x.con_o.mean():.3f} dif {x["dif"].mean()*100:+.2f} pp IC90 cierre ({lo*100:+.1f},{hi*100:+.1f})')
# placebo: permutar signo de tendencia entre mercados del mismo dia (rompe la relacion lado-tendencia)
x = Mw[Mw.per == 'TEST']; obs = x['dif'].mean(); pm = []
for p in range(NPERM):
    up = x.groupby('dia')['up'].transform(lambda v: rng.permutation(v.values)).values
    cw = np.where(up > 0, x.shareUp, 1 - x.shareUp); co = np.where(up > 0, x.shareUp_o, 1 - x.shareUp_o); pm.append((cw - co).mean())
pm = np.array(pm); P(f'  placebo TEST (tendencia permutada dentro del dia): obs {obs*100:+.2f} pp, placebo {pm.mean()*100:+.2f} (sd {pm.std()*100:.2f}), p dos colas {(np.abs(pm - pm.mean()) >= abs(obs - pm.mean())).mean():.3f}')
# lado del residuo
Q = Wd.pivot_table(index='mid', columns='lado_ef', values='acc', aggfunc='sum', fill_value=0)
for c in ('YES', 'NO'):
    if c not in Q: Q[c] = 0.0
Q['heavy'] = np.where(Q.YES >= Q.NO, 'YES', 'NO'); Q['rf'] = (Q.YES - Q.NO).abs() / (Q.YES + Q.NO)
U = Mw[['up', 'fin', 'dia']].join(Q[['heavy', 'rf']], how='inner'); U['res_con'] = np.where(((U.up > 0) & (U.heavy == 'YES')) | ((U.up < 0) & (U.heavy == 'NO')), 1.0, 0.0)
for per, sel in (('DESC', U.dia <= '2026-10-19'), ('TEST', U.dia >= '2026-10-20')):
    x = U[sel]; lo, hi = ci_ratio(x.res_con.values, np.ones(len(x)), x.fin.values); P(f'  lado del residuo A FAVOR de la tendencia previa ({per}): {x.res_con.mean():.3f} (n {len(x)}) IC90 cierre ({lo:.3f},{hi:.3f}); ponderado por res_frac {np.average(x.res_con, weights=x.rf.values + 1e-9):.3f}')
# ---------------- P4: ledger wallet-mercado (todos los roles) y descomposicion
P('\n(b) PRECIO/COLA: edge frente al mid del token (c por acc; >0 = compra por debajo del mid) y EV/€ en exceso sobre otros makers de los mismos estratos (dia x Tb x px_ef 0,05)')
for ed in ('mid5_f', 'mid5_t0'):
    Wd['edge'] = (Wd[ed].astype(float) - Wd.px_ef) * 100; Od['edge'] = (Od[ed].astype(float) - Od.px_ef) * 100
    for per in ('DESC', 'TEST'):
        w = Wd[Wd.per == per]; o = Od[Od.per == per]
        go = o.groupby(['dia', 'Tb', 'pxb5']).agg(e=('edge', 'mean'), pn=('pnl', 'sum'), co=('coste', 'sum')); k = pd.MultiIndex.from_frame(w[['dia', 'Tb', 'pxb5']])
        e_exp = go.e.reindex(k).values; ev_exp = (go.pn / go.co).reindex(k).values
        d_edge = (w.edge.values - e_exp); okk = ~np.isnan(d_edge); l1, h1 = ci_ratio(d_edge[okk], np.ones(okk.sum()), w.fin.values[okk])
        ex = w.pnl.values - w.coste.values * ev_exp; ok2 = ~np.isnan(ev_exp); l2, h2 = ci_ratio(ex[ok2], w.coste.values[ok2], w.fin.values[ok2])
        P(f'  [{ed}] {per}: n fills {int(okk.sum())} edge wallet {np.nanmean(w.edge):+.2f}c, esperado {np.nanmean(e_exp):+.2f}c, dif {np.nanmean(d_edge):+.2f}c IC90 cierre ({l1:+.2f},{h1:+.2f}) | EV wallet {w.pnl.sum()/w.coste.sum():+.4f}, exceso EV/€ vs estratos {ex[ok2].sum()/w.coste.values[ok2].sum():+.4f} IC90 ({l2:+.4f},{h2:+.4f})')
del Od, F, Wd; gc.collect()
open(os.path.join(OUT, 'an_w2.txt'), 'w').write('\n'.join(out) + '\n')
