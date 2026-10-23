#!/usr/bin/env python3
"""preal_analisis.py - P-REAL (PREREG_PREAL sha 5a263d50...). H1/H2/H3 con ASK/BID/PRINT reales + calibracion modelo->real + conversion de la proxy larga.
Uso: python3 -I preal_analisis.py [--desde D] [--hasta D] [--salida FICHERO]   (por defecto 2026-10-05..2026-10-21). Solo lectura de datalogs/preal, desenlaces cacheados y datos/*.csv.gz de R-TEND."""
import sys, os, json, glob, gzip, hashlib, numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); DAT = os.path.join(HERE, '..', 'datos'); D = '/root/polymarket-research-datalogs/preal'
assert hashlib.sha256(open(os.path.join(HERE, '..', 'PREREG_PREAL.md'), 'rb').read()).hexdigest().startswith('5a263d50'), 'PREREG_PREAL alterado'
RNG = np.random.default_rng(20261026); NB = 2000; NP = 1000; THR = 7.7; FEE = 0.07
PRIM = ['ETH', 'SOL', 'XRP']; REPL = ['BTC', 'BNB', 'DOGE']
args = sys.argv[1:]; desde = args[args.index('--desde') + 1] if '--desde' in args else '2026-10-05'; hasta = args[args.index('--hasta') + 1] if '--hasta' in args else '2026-10-21'
OUT = []
def P(*a): s = ' '.join(str(x) for x in a); OUT.append(s); print(s, flush=True)
def cost_ask(p): return p * (1 + FEE * (1 - p))
# ---------------------------------------------------------------- carga
def carga():
    fs = [f for f in sorted(glob.glob(f'{D}/ask_t0_*.csv.gz')) if desde <= os.path.basename(f)[7:17] <= hasta]; L = []
    for f in fs:
        x = pd.read_csv(f, dtype={'mid': str, 'cierre': np.int64}); L.append(x)
    X = pd.concat(L, ignore_index=True); X['tmin'] = X.cierre // 60 - 5; return X, [os.path.basename(f)[7:17] for f in fs]
def largo(X, T, lag):
    s = f'_{T}_{lag}'; cols = {k + s: k for k in ('bid', 'ask', 'bsz', 'asz', 'edad', 'pp', 'ps', 'pd')}
    Y = X[['dia', 'coin', 'mid', 'cierre', 'tmin', 'lado'] + list(cols)].rename(columns=cols)
    for k in ('bid', 'ask'): Y.loc[Y[k] <= 0, k] = np.nan                 # 0 en el registro = lado vacio -> missing
    Y.loc[Y.ask >= 1, 'ask'] = np.nan
    # vivo: algun token de la pareja con edad <=30 s ; cruzado: bid>ask
    e = Y.groupby(['coin', 'cierre']).edad.transform('min'); Y['vivo'] = e <= 30000
    Y['cruz'] = (Y.bid > Y.ask); Y['sgn'] = np.where(Y.lado == 'YES', 1.0, -1.0); return Y
def prep(Y, W, desen):
    Y = Y.merge(W, on=['coin', 'tmin'], how='left'); Y['out'] = Y.mid.map(desen)
    Y['gana'] = np.where(Y.out.isna(), np.nan, (Y.out == Y.lado).astype(float)); Y['rs'] = Y.sgn * Y.rpre_bar
    Y['cls'] = np.where(Y.rs >= THR, 'CON', np.where(Y.rs <= -THR, 'CONTRA', 'NEU')); Y.loc[Y.rpre_bar.isna(), 'cls'] = 'NA'; return Y
def precio_cols(U, kind):
    if kind == 'ask': p = U.ask; c = cost_ask(p)
    elif kind == 'bid': p = U.bid; c = p.copy()
    elif kind == 'print': p = U.pp; c = cost_ask(p)
    return p, c
# ---------------------------------------------------------------- estadistica
def ev(pnl, cost): return pnl.sum() / cost.sum() if len(pnl) and cost.sum() > 0 else np.nan
def agg_cl(U, key):   # sumas por cluster x clase
    g = U[U.cls.isin(['CON', 'CONTRA'])].groupby([key, 'cls']).agg(p=('pnl', 'sum'), c=('cst', 'sum')).unstack('cls').fillna(0); return g
def delta_cl(U, key, extra=None, nb=NB):
    """Delta = EV(CON)-EV(CONTRA); IC90 bootstrap de clusters. extra: funcion(U)->mask para sub-poblacion (p.ej. R==TREND)."""
    g = agg_cl(U, key); 
    for c in ('CON', 'CONTRA'):
        for v in ('p', 'c'):
            if (v, c) not in g.columns: g[(v, c)] = 0.0
    a = g[[('p', 'CON'), ('c', 'CON'), ('p', 'CONTRA'), ('c', 'CONTRA')]].values; n = len(a)
    if n < 2: return np.nan, (np.nan, np.nan), np.nan, n
    base = a.sum(0); D0 = base[0] / base[1] - base[2] / base[3]; bs = np.empty(nb)
    for i in range(nb):
        s = a[RNG.integers(0, n, n)].sum(0); bs[i] = s[0] / s[1] - s[2] / s[3]
    return D0, tuple(np.nanpercentile(bs, [5, 95])), (bs >= 0).mean(), n
def placebo_delta(U, nperm=NP):
    """Permuta CON/CONTRA dentro de dia x moneda x cubo ask 0,05 ; devuelve (Delta_obs, p una cola Delta_perm<=obs)."""
    V = U[U.cls.isin(['CON', 'CONTRA'])].copy(); V['st'] = (V.dia.astype(str) + V.coin + (V.ask * 20).astype(int).astype(str)).astype('category').cat.codes
    V = V.sort_values('st'); st = V.st.values; con = (V.cls == 'CON').values; p = V.pnl.values; c = V.cst.values
    d0 = p[con].sum() / c[con].sum() - p[~con].sum() / c[~con].sum(); out = np.empty(nperm)
    for i in range(nperm):
        idx = np.lexsort((RNG.random(len(st)), st)); L = con[idx]; out[i] = p[L].sum() / c[L].sum() - p[~L].sum() / c[~L].sum()
    return d0, (out <= d0).mean(), out.mean()
def delta_pop(U): 
    a = U[U.cls == 'CON']; b = U[U.cls == 'CONTRA']; return ev(a.pnl, a.cst) - ev(b.pnl, b.cst)
def por_dia_delta(U):
    r = {}
    for d, g in U.groupby('dia'):
        a = g[g.cls == 'CON']; b = g[g.cls == 'CONTRA']
        if len(a) >= 5 and len(b) >= 5: r[d] = ev(a.pnl, a.cst) - ev(b.pnl, b.cst)
    return pd.Series(r)
def informe_h1(U, titulo, completo=False):
    U = U[U.cls.isin(['CON', 'CONTRA'])]
    if len(U) < 40: P(f'  {titulo}: n={len(U)} (<40)'); return None
    d0, ic_c, pc, ncl = delta_cl(U, 'cierre'); d0d, ic_d, pd_, nd = delta_cl(U, 'dia')
    nCON = (U.cls == 'CON').sum(); nCTR = (U.cls == 'CONTRA').sum()
    eC = ev(U[U.cls == 'CON'].pnl, U[U.cls == 'CON'].cst); eK = ev(U[U.cls == 'CONTRA'].pnl, U[U.cls == 'CONTRA'].cst)
    s = f'  {titulo}: n CON {nCON} CONTRA {nCTR} (cierres {ncl}, dias {nd}) EV(CON) {eC:+.3f} EV(CONTRA) {eK:+.3f} Delta {d0:+.3f} IC90cierre ({ic_c[0]:+.3f},{ic_c[1]:+.3f}) IC90dia ({ic_d[0]:+.3f},{ic_d[1]:+.3f})'
    res = dict(delta=d0, ic_cierre=ic_c, ic_dia=ic_d)
    if completo:
        dd = por_dia_delta(U); pdn = (dd < 0).mean() if len(dd) else np.nan; w2 = dd.sort_values().index[:2]
        sin2 = delta_pop(U[~U.dia.isin(w2)]); pl = placebo_delta(U)
        s += f'\n     placebo p {pl[1]:.3f} (media perm {pl[2]:+.3f}); dias Delta<0 {int((dd < 0).sum())}/{len(dd)} ({100 * pdn:.0f} %); sin 2 dias mas negativos {sin2:+.3f}'
        ok = (d0 < 0) and (ic_c[1] < 0) and (pl[1] < 0.05) and (pdn >= 0.6) and (sin2 < 0); parcial = (d0 < 0) and (ic_c[1] < 0)
        res.update(placebo_p=pl[1], frac_dias=pdn, sin2=sin2, veredicto='SOSTENIDA' if (ok and ic_d[1] < 0) else ('SOSTENIDA (solo por cierre; IC90 por dia incluye 0)' if ok else ('PARCIAL' if parcial else 'NO SOSTENIDA')))
        s += f'\n     VEREDICTO H1-REAL: {res["veredicto"]}'
    P(s); return res
# ---------------------------------------------------------------- main
def main():
    desen = json.load(open(f'{D}/desenl_cache.json'))
    W = pd.read_csv(os.path.join(DAT, 'ventanas_bookticker.csv.gz'), usecols=['coin', 'tmin', 'rpre', 'R', 'D', 'COH'])
    et = [pd.read_csv(f, usecols=['coin', 'tmin', 'rpre', 'R', 'D', 'COH']) for f in sorted(glob.glob('/root/polymarket-research-datalogs/regimen_5m/etiquetas/regimen_*.csv.gz'))]
    W = pd.concat([W] + et, ignore_index=True).drop_duplicates(['coin', 'tmin'], keep='first').rename(columns={'rpre': 'rpre_bar'})
    X, dias = carga(); P(f'# P-REAL analisis (prereg 5a263d50) dias {dias[0]}..{dias[-1]} ({len(dias)} dias con extraccion); ventanas-token {len(X)}')
    # cobertura (seccion 6)
    Y = prep(largo(X, 180, 250), W, desen)
    cob = Y.groupby('dia').agg(tokens=('mid', 'size'), vivo=('vivo', 'mean'), ask_ok=('ask', lambda s: s.notna().mean()), cruz=('cruz', 'mean'), con_desenlace=('gana', lambda s: s.notna().mean()), edad_p50=('edad', 'median'), edad_p90=('edad', lambda s: s.quantile(0.9)), con_print=('pp', lambda s: s.notna().mean()))
    P('\n## Cobertura por dia (T=180, lag 250; fraccion sobre tokens 5min listados)'); P(cob.round(3).to_string())
    P(f'cobertura de desenlace oficial global {Y.gana.notna().mean():.4f}; ventanas sin estado vivo {(~Y.vivo).mean():.3f}; libros cruzados {Y.cruz.mean():.4f}')
    def U1(Y, coins, kind='ask', lo=0.10, hi=0.30, band='ask'):
        p, c = precio_cols(Y, kind); b = Y[band] if band in Y else Y.ask
        m = Y.coin.isin(coins) & Y.vivo & ~Y.cruz & Y.ask.notna() & b.ge(lo) & b.lt(hi) & Y.gana.notna() & Y.cls.isin(['CON', 'CONTRA', 'NEU']) & p.notna()
        U = Y[m].copy(); U['cst'] = c[m]; U['pnl'] = U.gana - U.cst; return U
    U = U1(Y, PRIM); P(f'\n## U1 primaria (ask en [0,10,0,30), ETH/SOL/XRP, T=180 lag 250): n {len(U)}, dias {U.dia.nunique()}, cierres {U.cierre.nunique()}, coste {U.cst.sum():.0f}, PnL {U.pnl.sum():+.1f}, EV/EUR {ev(U.pnl, U.cst):+.4f}, CON {int((U.cls=="CON").sum())} CONTRA {int((U.cls=="CONTRA").sum())} NEU {int((U.cls=="NEU").sum())}; ask medio {U.ask.mean():.3f}')
    P('\n## H1-REAL (primaria)'); r1 = informe_h1(U, 'ASK tomador, ETH/SOL/XRP', completo=True)
    dd_ = U[U.cls.isin(['CON', 'CONTRA'])].groupby('dia').apply(lambda g: pd.Series(dict(nCON=(g.cls == 'CON').sum(), nCTR=(g.cls == 'CONTRA').sum(), EV_CON=ev(g[g.cls == 'CON'].pnl, g[g.cls == 'CON'].cst), EV_CTR=ev(g[g.cls == 'CONTRA'].pnl, g[g.cls == 'CONTRA'].cst), EV_todas=ev(g.pnl, g.cst))), include_groups=False); dd_['Delta'] = dd_.EV_CON - dd_.EV_CTR
    P('  por dia (descriptivo):'); P(dd_.round(3).to_string())
    # H2
    P('\n## H2-REAL interaccion (U1)'); Ur = U[U.R.isin(['TREND', 'REVERT', 'MIXTO']) & U.cls.isin(['CON', 'CONTRA'])]
    for cl in ('TREND', 'MIXTO', 'REVERT'): informe_h1(Ur[Ur.R == cl], f'Delta | R={cl}')
    def inter(Ud, key, nb=NB):
        out = {}
        for cl in ('TREND', 'REVERT'):
            g = agg_cl(Ud[Ud.R == cl], key); out[cl] = g.reindex(columns=pd.MultiIndex.from_product([['p', 'c'], ['CON', 'CONTRA']])).fillna(0)
        idx = sorted(set(out['TREND'].index) | set(out['REVERT'].index)); A = {k: out[k].reindex(idx).fillna(0).values[:, [0, 2, 1, 3]] for k in out}   # p_con,c_con,p_ctr,c_ctr  (orden: p CON, p CONTRA, c CON, c CONTRA -> reorden)
        A = {k: np.column_stack([out[k].reindex(idx).fillna(0)[('p', 'CON')], out[k].reindex(idx).fillna(0)[('c', 'CON')], out[k].reindex(idx).fillna(0)[('p', 'CONTRA')], out[k].reindex(idx).fillna(0)[('c', 'CONTRA')]]) for k in out}
        def f(sel): 
            t = A['TREND'][sel].sum(0); r = A['REVERT'][sel].sum(0); return (t[0] / t[1] - t[2] / t[3]) - (r[0] / r[1] - r[2] / r[3])
        n = len(idx); i0 = f(slice(None)); bs = np.array([f(RNG.integers(0, n, n)) for _ in range(nb)]); return i0, np.nanpercentile(bs, [5, 95]), 2 * min((bs <= 0).mean(), (bs >= 0).mean()), n
    if len(Ur) > 100:
        for key in ('cierre', 'dia'):
            i0, ic, p2, n = inter(Ur, key); P(f'  I_R = Delta(TREND)-Delta(REVERT): {i0:+.3f} IC90 por {key} ({ic[0]:+.3f},{ic[1]:+.3f}) p2 {p2:.3f} (clusters {n})' + ('   -> ' + ('CONSISTENTE' if ic[1] < 0 and key == 'cierre' else 'no concluyente') if key == 'cierre' else ''))
    # H3
    P('\n## H3-REAL reglas congeladas (PnL por accion de las unidades SALTADAS; dP = -Sum pnl saltadas; x5 acc entre parentesis)')
    Uc = U[U.cls == 'CON']
    for nom, m in (('R0 CON>=7,7', Uc.index == Uc.index), ('R1 CON & TREND', (Uc.R == 'TREND').values), ('R2 CON & TREND|MIXTO', Uc.R.isin(['TREND', 'MIXTO']).values)):
        S = Uc[m]
        if len(S) < 20: P(f'  {nom}: n {len(S)} (<20)'); continue
        dP = -S.pnl.sum(); g = S.groupby('cierre').pnl.sum().values; bs = np.array([-g[RNG.integers(0, len(g), len(g))].sum() for _ in range(NB)])
        dd = -S.groupby('dia').pnl.sum(); best2 = dd.sort_values(ascending=False).index[:2]; sin2 = dd.drop(best2).sum()
        V = Uc.copy(); V['st'] = (V.dia.astype(str) + V.coin + (V.ask * 20).astype(int).astype(str)).astype('category').cat.codes; skm = pd.Series(m, index=Uc.index) if not isinstance(m, pd.Series) else m
        cnt = V[skm.values].groupby('st').size().to_dict(); ix = V.groupby('st').indices; pn = V.pnl.values
        pl = np.array([-sum(pn[RNG.choice(ix[s], k, replace=False)].sum() for s, k in cnt.items()) for _ in range(500)])
        P(f'  {nom}: n saltadas {len(S)} coste {S.cst.sum():.0f} EV saltadas {ev(S.pnl, S.cst):+.3f} dP {dP:+.1f} (x5: {5*dP:+.0f}) IC90cierre ({np.percentile(bs,5):+.1f},{np.percentile(bs,95):+.1f}) placebo media {pl.mean():+.1f} p {(pl >= dP).mean():.3f} dias dP>0 {int((dd > 0).sum())}/{len(dd)} sin 2 mejores dias {sin2:+.1f}')
    # replicas
    P('\n## Replicas (no decisorias): Delta [IC90 cierre]')
    for c in PRIM + REPL: informe_h1(U1(Y, [c]), f'moneda {c}')
    informe_h1(U1(Y, REPL), 'replicas BTC/BNB/DOGE agrupadas', completo=True)
    informe_h1(U1(Y, PRIM + REPL), 'las 6 monedas', completo=False)
    Uh = U; informe_h1(Uh[Uh.dia <= '2026-10-13'], 'mitad A (05-13)'); informe_h1(Uh[Uh.dia >= '2026-10-14'], 'mitad B (14-21)')
    for lo, hi in ((0.10, 0.15), (0.15, 0.20), (0.20, 0.25), (0.25, 0.30)): informe_h1(U1(Y, PRIM, lo=lo, hi=hi), f'ask [{lo:.2f},{hi:.2f})')
    for T, lag in ((180, 0), (180, 1000), (120, 250), (120, 0), (120, 1000)):
        Z = prep(largo(X, T, lag), W, desen); informe_h1(U1(Z, PRIM), f'T={T} lag={lag} ask')
    informe_h1(U1(Y, PRIM, kind='bid'), 'precio = BID (cota optimista de pujar en reposo, sin condicionar al relleno)')
    Up_ = U1(Y, PRIM, kind='print'); P(f'  PRINT (primer BUY de tomador en [dec+250ms, +30 s]; unidades U1 con print): n {len(Up_)} de {len(U)} ({100*len(Up_)/max(len(U),1):.0f} %)')
    informe_h1(Up_, 'precio = PRINT tomador, banda definida por ASK')
    # sesgo print vs ask
    if len(Up_):
        dlt = Up_.pp - Up_.ask; P(f'  sesgo print-ask: media {dlt.mean():+.4f}, p50 {dlt.median():+.4f}, p90 {dlt.quantile(.9):+.4f}, retraso del print p50 {Up_.pd.median():.0f} ms; print>=ask-0,01 en {100*(Up_.pp>=Up_.ask-0.01).mean():.0f} %, print<=bid+0,01 en {100*(Up_.pp<=Up_.bid+0.01).mean():.0f} % (auditoria interna: BUY=tomador => debe ir cerca del ask)')
        sc = Up_.copy(); sc['dif'] = (sc.pp - sc.ask); P(f'  EV a precio PRINT {ev(Up_.pnl, Up_.cst):+.4f} vs EV al ask de las mismas unidades {ev(Up_.gana - cost_ask(Up_.ask), cost_ask(Up_.ask)):+.4f}')
    # ------------------------------------------------ calibracion C1/C2
    P('\n## C1 calibracion modelo q -> ask real (U2: unidades del proxy con estado real; T=180, lag 250)')
    pan = pd.read_csv(os.path.join(DAT, 'panel_bookticker.csv.gz'), usecols=['coin', 'tmin', 'T', 'q', 'lado_up', 'win_proxy', 'rpre', 'R']); pan = pan[(pan['T'] == 180) & pan.coin.isin(PRIM)]
    pan['lado'] = np.where(pan.lado_up, 'YES', 'NO'); M = pan.merge(Y[['coin', 'tmin', 'lado', 'dia', 'cierre', 'mid', 'bid', 'ask', 'vivo', 'cruz', 'gana', 'cls']], on=['coin', 'tmin', 'lado'], how='inner')
    M = M[M.vivo & ~M.cruz & M.ask.notna() & M.gana.notna() & M.dia.between(desde, hasta)].copy()
    M['cst'] = cost_ask(M.ask); M['pnl_r'] = M.gana - M.cst; M['qb'] = pd.cut(M.q, [0.10, 0.15, 0.20, 0.25, 0.30], right=False)
    M['cl2'] = np.where(M.cls.isin(['CON', 'CONTRA']), M.cls, 'NEU')
    P(f'  U2 n {len(M)} dias {M.dia.nunique()}  acuerdo proxy Binance vs oficial {(M.win_proxy == M.gana).mean():.3f}')
    t = M.groupby(['qb', 'cl2'], observed=True).apply(lambda g: pd.Series(dict(n=len(g), q=g.q.mean(), ask=g.ask.mean(), bid=g.bid.mean(), acierto=g.gana.mean(), EV_modelo=(g.gana - g.q).sum() / g.q.sum(), EV_ask_real=g.pnl_r.sum() / g.cst.sum())), include_groups=False)
    P(t.round(3).to_string())
    tt = M.groupby('qb', observed=True).apply(lambda g: pd.Series(dict(n=len(g), q=g.q.mean(), ask=g.ask.mean(), desvio_ask_menos_q=(g.ask - g.q).mean(), acierto=g.gana.mean(), EV_modelo=(g.gana - g.q).sum() / g.q.sum(), EV_ask=g.pnl_r.sum() / g.cst.sum())), include_groups=False); P('  por tramo de q:'); P(tt.round(3).to_string())
    # C2: Delta modelo vs real en las mismas unidades
    Mc = M[M.cl2.isin(['CON', 'CONTRA'])].copy(); Mc['cls'] = Mc.cl2
    Mm = Mc.copy(); Mm['cst'] = Mm.q; Mm['pnl'] = Mm.gana - Mm.q; Mr = Mc.copy(); Mr['pnl'] = Mr.pnl_r
    dm = delta_pop(Mm); dr = delta_pop(Mr); g = pd.concat([Mm.groupby(['cierre', 'cls']).agg(pm=('pnl', 'sum'), cm=('cst', 'sum')), Mr.groupby(['cierre', 'cls']).agg(pr=('pnl', 'sum'), cr=('cst', 'sum'))], axis=1).unstack('cls').fillna(0)
    A = np.column_stack([g[(k, c)].values for k in ('pm', 'cm', 'pr', 'cr') for c in ('CON', 'CONTRA')]); n = len(A); bs = []
    for _ in range(NB):
        s = A[RNG.integers(0, n, n)].sum(0); bs.append((s[4] / s[6] - s[5] / s[7]) - (s[0] / s[2] - s[1] / s[3]))
    P(f'  C2 mismas unidades: Delta a precio de MODELO {dm:+.3f}; Delta al ASK real {dr:+.3f}; diferencia (real-modelo) {dr-dm:+.3f} IC90 cierre ({np.percentile(bs,5):+.3f},{np.percentile(bs,95):+.3f}); n CON {int((Mc.cls=="CON").sum())} CONTRA {int((Mc.cls=="CONTRA").sum())}')
    # ------------------------------------------------ C3 conversion proxy larga
    P('\n## C3 (EXPLORATORIO) proxy 2025 (349 d) convertida a coste al ask real con c_hat(tramo q, clase)')
    sd = pd.read_csv(os.path.join(DAT, 'panel_y2025.csv.gz'), usecols=['coin', 'tmin', 'T', 'q', 'lado_up', 'win_proxy', 'rpre', 'dia', 'R']); sd = sd[(sd['T'] == 180) & sd.coin.isin(PRIM) & sd.q.between(0.10, 0.2999999)].copy()
    sd['rs'] = np.where(sd.lado_up, sd.rpre, -sd.rpre); sd['cls'] = np.where(sd.rs >= THR, 'CON', np.where(sd.rs <= -THR, 'CONTRA', 'NEU')); sd['qb'] = pd.cut(sd.q, [0.10, 0.15, 0.20, 0.25, 0.30], right=False)
    QB = {iv: i for i, iv in enumerate(sd.qb.cat.categories)}; sd = sd[sd.cls.isin(['CON', 'CONTRA'])].copy()
    sq = sd.qb.cat.codes.values.astype(int); sc_ = (sd.cls == 'CONTRA').values.astype(int); swin = sd.win_proxy.values; sR = sd.R.values
    sdia = pd.factorize(sd.dia)[0]; nds = sdia.max() + 1
    mq = pd.Categorical(M.qb, categories=sd.qb.cat.categories).codes.astype(int); mc = (M.cl2 == 'CONTRA').values.astype(int); mcl = M.cl2.values; mcst = M.cst.values; mdia = pd.factorize(M.dia)[0]; ndm = mdia.max() + 1
    def chat(w):                                   # w: peso por dia de U2 -> c_hat[4,2] (celda con n>=20, si no media del tramo)
        W_ = w[mdia]; out = np.full((4, 2), np.nan)
        for qi in range(4):
            mq_ = (mq == qi); den = (W_ * mq_).sum(); tr = (W_ * mq_ * mcst).sum() / den if den > 0 else np.nan
            for ci, nm in enumerate(('CON', 'CONTRA')):
                sel = mq_ & (mcl == nm); n_ = (W_ * sel).sum(); out[qi, ci] = (W_ * sel * mcst).sum() / n_ if n_ >= 20 else tr
        return out
    def deltas(ch, w):
        cst = ch[sq, sc_]; pnl = swin - cst; W_ = w[sdia] * np.isfinite(cst); out = {}
        def d_(m): 
            a = m & (sc_ == 0); b = m & (sc_ == 1); return (W_ * a * pnl).sum() / (W_ * a * cst).sum() - (W_ * b * pnl).sum() / (W_ * b * cst).sum()
        return d_(np.ones(len(sq), bool)), d_(sR == 'TREND') - d_(sR == 'REVERT')
    c0 = chat(np.ones(ndm)); d_est, I_est = deltas(c0, np.ones(nds)); d_mod = (lambda a, b: (swin[a] - sd.q.values[a]).sum() / sd.q.values[a].sum() - (swin[b] - sd.q.values[b]).sum() / sd.q.values[b].sum())(sc_ == 0, sc_ == 1)
    bs = []; bsI = []
    for _ in range(1000):
        ch = chat(np.bincount(RNG.integers(0, ndm, ndm), minlength=ndm).astype(float)); a_, b_ = deltas(ch, np.bincount(RNG.integers(0, nds, nds), minlength=nds).astype(float)); bs.append(a_); bsI.append(b_)
    P('  c_hat (coste medio al ask con fee, U2) por tramo de q x clase [CON, CONTRA]: ' + '; '.join(f'{k}: {c0[i, 0]:.3f}/{c0[i, 1]:.3f}' for k, i in QB.items()))
    P(f'  S_D unidades CON/CONTRA {len(sd)} (dias {nds}): Delta a precio de MODELO {d_mod:+.3f} (R-TEND: -0,076); Delta a coste al ask real ESTIMADO {d_est:+.3f} IC90 doble bootstrap dias S_D x dias U2 ({np.percentile(bs,5):+.3f},{np.percentile(bs,95):+.3f}) [1000 rem.]')
    P(f'  I_R estimado (TREND-REVERT) {I_est:+.3f} IC90 ({np.nanpercentile(bsI,5):+.3f},{np.nanpercentile(bsI,95):+.3f}); Delta(win_proxy) usa acierto Binance, no oficial (acuerdo 97,6 % en S_B)')
    if '--forward' in args:
        nd_ = U.dia.nunique(); nco = int((U.cls == 'CON').sum()); P(f'\n## GATE FORWARD: dias nuevos {nd_}/10, n(CON) {nco}/300, veredicto H1 {r1["veredicto"] if r1 else "n/d"} -> ' + ('EVALUABLE' if nd_ >= 10 and nco >= 300 else 'NO EVALUABLE todavia'))
    sal = args[args.index('--salida') + 1] if '--salida' in args else os.path.join(HERE, '..', 'datos', 'preal_resultados.txt')
    open(sal, 'w').write('\n'.join(OUT))
if __name__ == '__main__': main()
