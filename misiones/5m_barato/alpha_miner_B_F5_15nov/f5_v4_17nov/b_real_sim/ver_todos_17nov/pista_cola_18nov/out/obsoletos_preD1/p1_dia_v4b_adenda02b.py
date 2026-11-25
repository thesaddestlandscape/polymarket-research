#!/usr/bin/env python3
"""p1_dia.py v2 (ADENDA_01_18nov: D-1 y fixes 2-5) (RE-B-COLA-CANCELA, 18-Nov, MECANISMO, NO EV). Prereg PREREG_PISTA_COLA_18nov.md (sha 654a655d...).
Por dia D y moneda: replay L2 de libro5_ms (reloj RECEPCION), eventos = clusters de T en bids (X,p) 0,10-0,30, candidatos placebo
en los mismos niveles, rasgos por ventana, disparo de las 7 variantes, union con on-chain (hueco a), salto Binance (hueco c).
Salida: out/p1_<coin>_<D>.pkl (idempotente: si existe, sale). Uso: p1_dia.py D [coin=btc]"""
import sys, os, gzip, json, bisect, random, collections, subprocess, heapq, glob, time, pickle
import numpy as np, pandas as pd
D = sys.argv[1]; COIN = sys.argv[2] if len(sys.argv) > 2 else 'btc'
H0 = os.path.dirname(os.path.abspath(__file__)); OUT = f'{H0}/out/p1_{COIN}_{D}{os.environ.get("PISTA_SUF","")}.pkl'
os.makedirs(f'{H0}/out', exist_ok=True)
if os.path.exists(OUT): print('ya existe', OUT); sys.exit(0)
random.seed(int(D.replace('-', ''))); T0 = time.time()   # ADENDA fix 2: semilla reproducible (hash(str) varia entre procesos)
EXC = '0xe111180000d2663c0091e4f400237545b87b996b'; OWN = '0x659a40ff9920febc5a66836213040924343d297f'   # wallet dedicada (contrato §9)
SYM = {'btc': 'BTCUSDT', 'eth': 'ETHUSDT', 'sol': 'SOLUSDT', 'xrp': 'XRPUSDT'}[COIN]
LO, HI = 0.10, 0.30 - 1e-9
log = lambda *a: print(f'[{time.time()-T0:7.0f}s]', *a, flush=True)
# ---- tokens
d0 = pd.Timestamp(D)
comp, END, SGN = {}, {}, {}      # SGN: signo ESTRUCTURAL del token frente al spot (rol 'tok' = Up = +1, 'comp' = Down = -1; verificado en sonda1_barridos outcome_tok)
for dd in (d0 - pd.Timedelta(days=1), d0, d0 + pd.Timedelta(days=1)):
    fn = f'/root/polymarket-research-datalogs/sonda1/pasivo/sonda1_fotos_l2_{dd.date()}.csv.gz'
    if not os.path.exists(fn): continue
    rows = collections.defaultdict(dict)
    for ch in pd.read_csv(fn, usecols=['slug', 'token', 'rol'], dtype=str, chunksize=300000):
        ch = ch[ch.slug.str.startswith(f'{COIN}-updown-5m')].drop_duplicates(['slug', 'rol'])
        for r in ch.itertuples(): rows[r.slug][r.rol] = r.token
    for s_, t in rows.items():
        if 'tok' in t and 'comp' in t:
            comp[t['tok']] = t['comp']; comp[t['comp']] = t['tok']; SGN[t['tok']] = 1; SGN[t['comp']] = -1; e = (int(s_.rsplit('-', 1)[1]) + 300) * 1000
            END[t['tok']] = e; END[t['comp']] = e
TK = set(comp); tokfile = f'{H0}/out/.tok_{COIN}_{D}.txt'; open(tokfile, 'w').write('\n'.join(TK) + '\n')
log('tokens', len(TK))
# ---- Binance (m5_registro x, c[7]=recepcion)
bx, bp = [], []
for dd in (d0, d0 + pd.Timedelta(days=1)):
    fn = f'/mnt/HC_Volume_106538179/m5_registro/m5_registro_{dd.date()}.csv.gz'
    if not os.path.exists(fn): continue
    pr = subprocess.Popen(f"zcat {fn} 2>/dev/null | grep -F ',{SYM},' | grep '^x,'", shell=True, stdout=subprocess.PIPE, text=True)
    for l in pr.stdout:
        p = l.split(','); bx.append(int(p[7])); bp.append(float(p[3]))
o = np.argsort(bx, kind='stable'); bx = np.array(bx, dtype=np.int64)[o]; bp = np.array(bp)[o]
log('binance', len(bx))
def bprice(t):
    i = np.searchsorted(bx, t, 'right') - 1
    return bp[i] if i >= 0 and t - bx[i] < 5000 else np.nan
# ---- on-chain del dia (y vecino para cubrir bordes)
oc = []; own_tx = set(); OWNR = collections.Counter()
for dd in (d0, d0 + pd.Timedelta(days=1)):
    fn = f'/root/polymarket-research-datalogs/onchain_fills_{dd.date()}.csv.gz'
    if not os.path.exists(fn): continue
    for ch in pd.read_csv(fn, usecols=['tipo', 'ts_est', 'tx', 'log_index', 'order_hash', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt'],
                          dtype={'token_id': str, 'taker': str, 'maker': str, 'tx': str, 'order_hash': str}, chunksize=500000):
        ch = ch[(ch.tipo == 'F') & ch.token_id.isin(TK) & (ch.ts_est < (d0 + pd.Timedelta(days=1, minutes=15)).timestamp())]
        om = (ch.maker.str.lower() == OWN) | (ch.taker.str.lower() == OWN)     # ADENDA fix 5: maker o tomador = nuestra wallet
        if om.any(): own_tx.update(ch.tx[om]); OWNR['filas_propias'] += int(om.sum())
        ch = ch[ch.taker.str.lower() != EXC]
        if len(ch): oc.append(ch.drop(columns=['tipo', 'taker']))
oc = pd.concat(oc) if oc else pd.DataFrame()
for c_ in ('token_id', 'maker', 'tx', 'order_hash'): oc[c_] = oc[c_].astype(object)
oc = oc.reset_index(drop=True)
oc['px'] = np.where(oc.side == 0, oc.maker_amt / oc.taker_amt, oc.taker_amt / oc.maker_amt)
oc['sh'] = np.where(oc.side == 0, oc.taker_amt, oc.maker_amt)
oc['X'] = [t if sd == 0 else comp[t] for t, sd in zip(oc.token_id, oc.side)]           # nivel bid de X equivalente
oc['p'] = np.where(oc.side == 0, oc.px, 1 - oc.px).round(2)
oc = oc[(oc.p >= LO) & (oc.p < 0.30 - 1e-9) & ((oc.side == 0) | (oc.px.round(2) > 0.5))]
# ADENDA fix 5: se EXCLUYE toda tx en la que nuestra wallet es maker o tomador (n_mk, mk, union, universo); los clusters libro5_ms que casan con una tx
# propia por (X,p) y ventana de bloque quedan MARCADOS (own=True) y p3 los excluye
oc_own = oc[oc.tx.isin(own_tx)]; oc = oc[~oc.tx.isin(own_tx)]
OWNI = collections.defaultdict(list)
for r in oc_own.itertuples(): OWNI[(r.X, r.p)].append(r.ts_est * 1000)
for k in OWNI: OWNI[k].sort()
OWNR['tx_propias'] = len(own_tx); OWNR['filas_propias_en_banda'] = len(oc_own)
def es_propio(X, p, rx):
    L = OWNI.get((X, p))
    if not L: return False
    i = bisect.bisect_left(L, rx + 800); return i < len(L) and L[i] <= rx + 4500
bidr = oc[oc.side == 0]
AG = bidr.groupby(['tx', 'X', 'p']).agg(ts=('ts_est', 'first'), n_mk=('order_hash', 'nunique'), sh_bid=('sh', 'sum'), li=('log_index', 'min'),
                                       mk=('maker', lambda s: tuple(sorted(set(s))))).reset_index()
ask_c = oc[oc.side == 1].groupby(['tx', 'X', 'p']).sh.sum().rename('sh_ask')
AG = AG.merge(ask_c, on=['tx', 'X', 'p'], how='left').fillna({'sh_ask': 0.0}); AG['sh_tot'] = AG.sh_bid + AG.sh_ask
AGI = collections.defaultdict(list)       # (X,p) -> [(ts_ms, sh_bid, sh_tot, idx)]
for i, r in enumerate(AG.itertuples()): AGI[(r.X, r.p)].append((r.ts * 1000, r.sh_bid, r.sh_tot, i))
for k in AGI: AGI[k].sort()
ROW = collections.defaultdict(list)       # fila individual (s5): (X,p) -> [(ts_ms, sh, idx_agg)]
agi = {(r.tx, r.X, r.p): i for i, r in enumerate(AG[['tx', 'X', 'p']].itertuples())}
for r in bidr.itertuples(): ROW[(r.X, r.p)].append((r.ts_est * 1000, r.sh, agi[(r.tx, r.X, r.p)]))
for k in ROW: ROW[k].sort()
log('onchain agregados', len(AG), 'filas bid', len(bidr))
def join(X, p, rx, sz, shift=0):
    """devuelve (metodo, idx_agg, n_cand). Ventana ts_bloque - rx en [800,4500] (+shift)."""
    a, b = rx + 800 + shift, rx + 4500 + shift
    tol = lambda x: abs(x - sz) <= max(1e-3, 1e-4 * sz)
    L = AGI.get((X, p), []); i = bisect.bisect_left(L, (a,)); c1 = []; c2 = []
    while i < len(L) and L[i][0] <= b:
        if tol(L[i][1]): c1.append(L[i][3])
        elif tol(L[i][2]): c2.append(L[i][3])
        i += 1
    if c1: return 'agg_bid', c1[0], len(c1)
    if c2: return 'agg_bid_ask', c2[0], len(c2)
    R = ROW.get((X, p), []); i = bisect.bisect_left(R, (a,)); c3 = []
    while i < len(R) and R[i][0] <= b:
        if tol(R[i][1]): c3.append(R[i][2])
        i += 1
    if c3: return 'fila', c3[0], len(c3)
    return None, None, 0
# ---- suelo: histograma rx-ex de d por ventana de 5 min
SU = collections.defaultdict(lambda: np.zeros(3001, dtype=np.int64))
def clase_suelo(w):
    h = SU.get(w)
    if h is None or h.sum() < 200: return 'indet', np.nan, np.nan
    c = np.cumsum(h); n = c[-1]; p1 = int(np.searchsorted(c, 0.01 * n)); p95 = int(np.searchsorted(c, 0.95 * n))
    return ('lo' if p1 <= 28 else 'hi' if p1 >= 33 else 'indet'), p1, p95
# ---- replay
class St:
    __slots__ = ('lv', 'Hr', 'Hs', 'chg', 'T', 'tb')
    def __init__(s): s.lv = {}; s.Hr = collections.defaultdict(list); s.Hs = collections.defaultdict(list); s.chg = []; s.T = []; s.tb = None   # tb = recepcion del 1.er B en vida activa
def setlv(st, px, s, r, rec=True):
    old = st.lv.get(px, 0.0)
    if not rec:
        if s > 0: st.lv[px] = s
        else: st.lv.pop(px, None)
        return
    if s == old and st.Hr[px]: return
    st.Hr[px].append(r); st.Hs[px].append(s); st.chg.append((r, px, s - old))
    if s > 0: st.lv[px] = s
    else: st.lv.pop(px, None)
def size_at(st, px, t):
    """tamano del nivel bid px en t. Nivel sin historia anterior a t: 0.0 si t >= tb (el 1.er B ya lo habria registrado si existiera: nivel genuinamente vacio),
    None (= dato FALTANTE, NaN aguas abajo) solo si t < tb. (ADENDA: antes None en ambos casos y p3 lo contaba como 0)."""
    h = st.Hr.get(px)
    if h:
        i = bisect.bisect_right(h, t) - 1
        if i >= 0: return st.Hs[px][i]
    return 0.0 if (st.tb is not None and t >= st.tb) else None
MI = set(); EV, PL, JN = [], [], collections.Counter(); OCN = collections.Counter(); seen = set(); cover = []
NPL = int(os.environ.get('PISTA_NPL', '8')); BAD = collections.Counter()
TAUS = {'V1': (300, .5), 'V2': (150, .5), 'V3': (1000, .5), 'V4': (300, .25)}
ev_szs = {}; NPOOL = int(os.environ.get('PISTA_NPOOL', '400'))
RNG2 = random.Random(int(D.replace('-', '')) + 1); SZP = []     # control dec_eq_S: tamanos de OTRO cluster (misma regla de coincidencia)
def eq_sz(x, szs): return any(abs(x - z) <= max(0.01, 0.01 * z) for z in szs)
def proc_pair(sts, tok):
    c = comp[tok]; end = END[tok]
    for X in (tok, c):
        stX = sts.get(X); stC = sts.get(comp[X])
        if stX is None: continue
        # prints mapeados a nivel bid de X
        P = collections.defaultdict(list); PA = []   # (X,px)->[(rx,sz,ex,ty)] ; all (rx,px,sz)
        for (r, ex, px, sd, sz) in stX.T:
            if sd == 'SELL': P[px].append((r, sz, ex, 'dir')); PA.append((r, px, sz))
        if stC:
            for (r, ex, px, sd, sz) in stC.T:
                if sd == 'BUY': q = round(1 - px, 2); P[q].append((r, sz, ex, 'mint')); PA.append((r, q, sz))
        PA.sort(); par = [x[0] for x in PA]
        # ADENDA fix 3: signo ESTRUCTURAL (Up=+1 / Down=-1), sin mirar prints futuros (antes: correlacion con TODOS los prints del mercado = look-ahead)
        sg = SGN[X]
        chg = sorted(stX.chg); chr_ = [x[0] for x in chg]
        cum = {}
        for px, L in P.items():
            L.sort(); cum[px] = ([x[0] for x in L], np.concatenate([[0], np.cumsum([x[1] for x in L])]))
        def printed(px, a, b):
            if px not in cum: return 0.0
            r, cs = cum[px]; return cs[bisect.bisect_right(r, b)] - cs[bisect.bisect_right(r, a)]
        def repeg(px, a, b):
            """masa de caidas en px en (a,b] que reaparece >=90% en otro nivel bid del mismo token en +-5 ms"""
            tot = 0.0; i = bisect.bisect_right(chr_, a)
            while i < len(chg) and chg[i][0] <= b:
                r, q, dl = chg[i]
                if q == px and dl < 0:
                    j = bisect.bisect_left(chr_, r - 5)
                    while j < len(chg) and chg[j][0] <= r + 5:
                        if chg[j][1] != px and chg[j][2] >= 0.9 * (-dl): tot += -dl; break
                        j += 1
                i += 1
            return tot
        def better(p_, t):
            return sum((size_at(stX, q, t) or 0.0) for q in list(stX.Hr) if q > p_ + 1e-9 and q < 0.5)
        def pbetter(p_, a, b):
            i = bisect.bisect_right(par, a); s = 0.0
            while i < len(PA) and PA[i][0] <= b:
                if PA[i][1] > p_ + 1e-9: s += PA[i][2]
                i += 1
            return s
        def matched(a, b, szs, pred):
            """ADENDA D-1: masa de caidas de nivel en (a,b] (pred sobre el precio del nivel) cuyo tamano ~ S o ~ algun T del MISMO cluster: son la propia
            casacion (el `d` llega hasta ~200 ms antes que su print T), cuentan como IMPRESAS, no como cancelacion."""
            if not szs: return 0.0
            tot = 0.0; i = bisect.bisect_right(chr_, a)
            while i < len(chg) and chg[i][0] <= b:
                r, q, dl = chg[i]
                if dl < 0 and pred(q) and eq_sz(-dl, szs): tot += -dl
                i += 1
            return tot
        def canc(px, a, b, szs=None):
            qa, qb = size_at(stX, px, a), size_at(stX, px, b)
            if qa is None or qb is None: return None, None, None
            raw = max(0.0, qa - qb - printed(px, a, b) - matched(a, b, szs, lambda q: q == px)); rp = repeg(px, a, b) if raw > 0 else 0.0
            return qa, max(0.0, raw - rp), (qb == 0 and qa > 0)
        def first_fire(px, t, var, lo_, hi_, szs=None):
            if var in TAUS:
                tau, th = TAUS[var]; i = bisect.bisect_left(chr_, lo_ - tau); cand = {lo_, hi_}
                while i < len(chg) and chg[i][0] <= hi_:
                    if chg[i][1] == px:
                        cand.add(chg[i][0]); cand.add(chg[i][0] + tau)
                    i += 1
                for te in sorted(x for x in cand if lo_ <= x <= hi_):
                    qa, cm, _ = canc(px, te - tau, te, szs)
                    if qa and qa > 0 and cm >= th * qa - 1e-9: return te
                return None
            if var == 'V5':
                tau = 300; i = bisect.bisect_left(chr_, lo_ - tau); cand = {lo_, hi_}
                while i < len(chg) and chg[i][0] <= hi_:
                    if chg[i][1] > px + 1e-9: cand.add(chg[i][0]); cand.add(chg[i][0] + tau)
                    i += 1
                for te in sorted(x for x in cand if lo_ <= x <= hi_):
                    ma, mb = better(px, te - tau), better(px, te)
                    if ma > 0 and max(0.0, ma - mb - pbetter(px, te - tau, te) - matched(te - tau, te, szs, lambda q: q > px + 1e-9)) >= 0.5 * ma - 1e-9: return te
                return None
            if var == 'V6':
                if sg == 0: return None
                i0, i1 = np.searchsorted(bx, lo_, 'left'), np.searchsorted(bx, hi_, 'right')
                for i in range(i0, i1):
                    p0 = bprice(bx[i] - 300)
                    if p0 == p0 and sg * (bp[i] / p0 - 1) <= -1e-4: return int(bx[i])
                return None
        def feats(px, t, szs=None):
            q150 = size_at(stX, px, t - 150)
            if q150 is None: return None
            w5 = t // 300000; cl, p1, p95 = clase_suelo(w5)
            o = dict(q150=q150, ttc=end - t, suelo=cl, su_p1=p1, su_p95=p95, sg=sg)
            o['act'] = sum(1 for (r, q, dl) in chg[bisect.bisect_left(chr_, t - 1000):bisect.bisect_left(chr_, t - 50)] if q == px)
            o['act2'] = sum(1 for (r, q, dl) in chg[bisect.bisect_left(chr_, t - 3000):bisect.bisect_left(chr_, t - 1000)] if q == px)
            b1, b0 = bprice(t - 50), bprice(t - 5050); o['r5'] = (b1 / b0 - 1) * sg if (b1 == b1 and b0 == b0 and sg) else np.nan
            o['absr5'] = abs(b1 / b0 - 1) if (b1 == b1 and b0 == b0) else np.nan
            for nm, (a, b) in {'W1': (-1000, -300), 'W2': (-300, -150), 'W3': (-150, -50), 'WA': (-1000, -50)}.items():
                qa, cm, sal = canc(px, t + a, t + b, szs)
                o[nm + '_q'] = qa; o[nm + '_c'] = cm; o[nm + '_sal'] = sal
                qa0, cm0, _ = canc(px, t + a, t + b, None); o[nm + '_c0'] = cm0           # legado (sin D-1), solo diagnostico
            # sensibilidad ADENDA: ventanas que terminan en -250 ms (la caida de la propia casacion llega hasta ~-200 ms)
            for nm, (a, b) in {'S250_WA': (-1000, -250), 'S250_W3': (-400, -250)}.items():
                qa, cm, sal = canc(px, t + a, t + b, szs); o[nm + '_q'] = qa; o[nm + '_c'] = cm
            o['bet1000'] = better(px, t - 1000); o['bet150'] = better(px, t - 150)
            dl50 = t - 20 - 53; dl90 = t - 20 - ((p95 if p95 == p95 else 40) + 147)
            for v in ('V1', 'V2', 'V3', 'V4', 'V5', 'V6'):
                o['f_' + v] = first_fire(px, t, v, t - 1000, dl50, szs)
            o['f_V7'] = min([x for x in (o['f_V1'], o['f_V5']) if x is not None], default=None)
            o['f_V1_0'] = first_fire(px, t, 'V1', t - 1000, dl50, None)                       # legado (sin D-1), solo diagnostico
            for v in ('V1', 'V2', 'V3', 'V4', 'V5'): o['f_' + v + '_e250'] = first_fire(px, t, v, t - 1000, t - 250, szs)
            o['f_V7_e250'] = min([x for x in (o['f_V1_e250'], o['f_V5_e250']) if x is not None], default=None)
            o['dl50'] = dl50; o['dl90'] = dl90
            # inicio de evaporacion (1.a caida no impresa NI igual a la propia casacion en [t-1000,t-50)) y 1.er salto Binance >=1bp contra
            ev0 = None; i = bisect.bisect_left(chr_, t - 1000); prev = t - 1000
            while i < len(chg) and chg[i][0] < t - 50:
                r, q, dl = chg[i]
                if q == px:
                    if dl < 0 and -dl > printed(px, prev, r) + 1e-9 and not (szs and eq_sz(-dl, szs)): ev0 = r; break
                    prev = r
                i += 1
            o['evap0'] = ev0; o['bn0'] = first_fire(px, t, 'V6', t - 1000, t - 50)
            return o
        for px, L in P.items():
            if not (LO <= px < HI): continue
            cls = []
            for (r, sz, ex, ty) in L:
                if cls and r - cls[-1]['t1'] < 300: cls[-1]['t1'] = r; cls[-1]['S'] += sz; cls[-1]['rows'].append((r, sz, ty))
                else: cls.append(dict(t0=r, t1=r, S=sz, ty=ty, ex=ex, rows=[(r, sz, ty)]))
            for cl in cls: cl['szs'] = sorted({cl['S']} | {x[1] for x in cl['rows']})
            n_ev0 = len(EV)
            for k_, cl in enumerate(cls):
                key = (X, px, cl['ex'])
                if key in seen: continue
                seen.add(key)
                szs = cl['szs']
                f = feats(px, cl['t0'], szs)
                if f is None: JN['ev_sin_estado'] += 1; continue
                # union on-chain (1.a fila T del cluster) + falsos con desplazamiento
                r0, sz0, ty0 = cl['rows'][0]; m, idx, nc = join(X, px, r0, sz0)
                JN['T1_tot'] += 1; JN['T1_' + str(m)] += 1; JN['T1_unico'] += (nc == 1)
                for sh in (-60000, 60000): JN[f'T1_falso_{sh}'] += join(X, px, r0, sz0, sh)[0] is not None
                for (rr, ss, tt) in cl['rows']:
                    JN['Trow_tot'] += 1; jj = join(X, px, rr, ss); JN['Trow_ok'] += jj[0] is not None
                    if jj[1] is not None: MI.add(jj[1])
                win = chg[bisect.bisect_left(chr_, cl['t0'] - 1000):bisect.bisect_left(chr_, cl['t0'] - 50)]
                f['dec_eq_S'] = any(q == px and dl < 0 and eq_sz(-dl, szs) for (r, q, dl) in win)    # diagnostico D-1: hay caida ~S/T en (-1000,-50)
                zc = SZP[RNG2.randrange(len(SZP))] if SZP else None
                f['dec_eq_S_ctrl'] = (any(q == px and dl < 0 and eq_sz(-dl, zc) for (r, q, dl) in win) if zc else None)   # control: tamanos de OTRO cluster
                SZP.append(szs)
                ev_szs[f"{D}|{X[-10:]}|{px}|{cl['t0']}"] = szs
                f.update(dict(evid=f"{D}|{X[-10:]}|{px}|{cl['t0']}", X=X, p=px, t=cl['t0'], S=cl['S'], ty=cl['ty'], nT=len(cl['rows']), end=end, D=D, coin=COIN, jm=m, jnc=nc, own=es_propio(X, px, r0),
                              n_mk=int(AG.n_mk.iat[idx]) if idx is not None else np.nan, mk=AG.mk.iat[idx] if idx is not None else None,
                              prevpr=printed(px, cl['t0'] - 1000, cl['t0'] - 1)))
                EV.append(f)
            # ADENDA_02 (punto 2): placebo EMPAREJADO POR EVENTO con calibre (caliper) en el MISMO mercado y nivel (X,px), otro instante.
            # Pool barato (q150, act, ttc) de NPOOL instantes uniformes con Q(t-150)>0 y sin T +-1 s; cada evento toma hasta NPL del pool que cumplan el calibre:
            # C1: act in [0,7a-1 ; 1,3a+1], q150/q150_ev in [0,7 ; 1,43], |dttc|<=60 s ; C2: act +-(0,5a+2), q ratio [0,5 ; 2], |dttc|<=120 s ; si ninguno: sin pareja.
            hr = stX.Hr.get(px); evs = EV[n_ev0:]
            if not hr or not evs or stX.tb is None: continue
            a0, a1 = stX.tb + 150, end
            if a1 <= a0: continue
            def cheap_act(t): return sum(1 for (r, q, dl) in chg[bisect.bisect_left(chr_, t - 3000):bisect.bisect_left(chr_, t - 1000)] if q == px)   # act2: PRE-ventana
            pool = []
            for _ in range(NPOOL):
                t = random.randint(a0, a1)
                if printed(px, t - 1000, t + 1000) > 0: continue
                q = size_at(stX, px, t - 150)
                if not q or q <= 0: continue
                q0 = size_at(stX, px, t - 1000)
                if q0 is None or q0 <= 0: continue
                pool.append((t, q0, cheap_act(t), end - t))
            usedp = set()
            for ev in evs:
                ea, eq, et = ev['act2'], ev['WA_q'], ev['ttc']
                if eq is None or eq != eq or not eq > 0: continue
                sel = []; lvl = None
                for L_, (fa, fb, qlo, qhi, dt) in (('C1', (0.7, 1.3, 0.7, 1.43, 60000)), ('C2', (0.5, 1.5, 0.5, 2.0, 120000))):
                    sl = 1 if L_ == 'C1' else 2
                    c_ = [k for k, (t, q, a_, tt) in enumerate(pool) if k not in usedp and (ea * fa - sl) <= a_ <= (ea * fb + sl) and qlo <= q / eq <= qhi and abs(tt - et) <= dt]
                    if c_: sel = random.sample(c_, min(NPL, len(c_))); lvl = L_; break
                for k in sel:
                    usedp.add(k); t = pool[k][0]
                    f = feats(px, t, ev_szs.get(ev['evid']))
                    if f is None: continue
                    f.update(dict(X=X, p=px, t=t, D=D, coin=COIN, end=end, evid=ev['evid'], cal=lvl)); PL.append(f)
def run_file(fn):
    sts = {}; hp = []; known = set(); last = 0; t_first = None
    cmd = f"zcat {fn} 2>/dev/null | grep -F -f {tokfile}"
    pr = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, text=True, bufsize=1 << 20)
    for n, l in enumerate(pr.stdout):
        p = l.rstrip('\n').split(','); t = p[0]
        if t not in ('B', 'd', 'T'): continue
        if len(p) < 8 or p[2] not in END: BAD['linea_corta_o_token'] += 1; continue
        tk = p[2]
        try: r = int(p[6]); int(p[1])
        except ValueError: BAD['ts_malo'] += 1; continue
        if t_first is None: t_first = r
        last = r
        if r > END[tk] + 120000: continue                     # mercado ya cerrado y procesado
        rec = r >= END[tk] - 420000                           # historia solo en la vida activa (5 min + 2 min previos)
        st = sts.get(tk)
        if st is None:
            st = sts[tk] = St()
            if tk not in known: known.add(tk); heapq.heappush(hp, (END[tk], tk))
        try:
          if t == 'd':
            if p[3] != 'B': continue
            px = round(float(p[4]), 2)
            if px >= 0.5: continue
            SU[r // 300000][min(3000, max(0, r - int(p[1])))] += 1
            setlv(st, px, float(p[5]), r, rec)
          elif t == 'B':
            if rec and st.tb is None: st.tb = r
            b = {}
            if p[3]:
                for x in p[3].split(';'):
                    if x:
                        a_, s_ = x.split(':'); q = round(float(a_), 2)
                        if q < 0.5: b[q] = float(s_)
            for q in list(st.lv):
                if q not in b: setlv(st, q, 0.0, r, rec)
            for q, s_ in b.items(): setlv(st, q, s_, r, rec)
          elif rec:
            st.T.append((r, int(p[1]), round(float(p[3]), 2), p[4], float(p[5])))
        except (ValueError, IndexError):
            BAD['campo_malo'] += 1; continue
        if n % 300000 == 0:
            while hp and hp[0][0] + 120000 < last:
                e, tk2 = heapq.heappop(hp)
                if tk2 in sts and comp[tk2] in sts or tk2 in sts:
                    pair = {x: sts.pop(x) for x in (tk2, comp[tk2]) if x in sts}
                    if pair: proc_pair(pair, tk2)
    pr.wait()
    for tk2 in list(sts):
        if tk2 in sts:
            pair = {x: sts.pop(x) for x in (tk2, comp[tk2]) if x in sts}; proc_pair(pair, tk2)
    if t_first: cover.append((t_first, last))
EVD, PLD = [], []
files = sorted(glob.glob(os.environ.get('PISTA_FILES') or f'/mnt/HC_Volume_106538179/libro5_ms_prot/libro5_ms_{D}_*.csv.gz'), key=lambda f_: (os.path.getmtime(f_), f_))
for fn in files:
    log('fichero', os.path.basename(fn)); run_file(fn); log('eventos', len(EV), 'placebo', len(PL), 'lineas_malas', dict(BAD))
    EVD.append(pd.DataFrame(EV)); PLD.append(pd.DataFrame(PL)); EV.clear(); PL.clear()
# tasa de union centrada en on-chain (agregados (tx,X,p) con casado dentro de la cobertura)
for r in AG.itertuples():
    ts = r.ts * 1000
    if any(a + 5000 <= ts - 2300 <= b - 5000 for a, b in cover): OCN['agg_en_cobertura'] += 1; OCN['agg_n_mk1'] += (r.n_mk == 1); OCN['agg_unidos'] += (r.Index in MI); OCN['agg_unidos_nmk1'] += (r.Index in MI and r.n_mk == 1)
pickle.dump(dict(EV=pd.concat(EVD, ignore_index=True), PL=pd.concat(PLD, ignore_index=True), BAD=dict(BAD), JN=dict(JN), OCN=dict(OCN), OWNR=dict(OWNR), version='p1_v3_ADENDA02', cover=cover, files=files, D=D, coin=COIN,
                 suelo={int(w): clase_suelo(w) for w in SU}), open(OUT + '.tmp', 'wb'))
os.replace(OUT + '.tmp', OUT); log('FIN', OUT, sum(map(len, EVD)), sum(map(len, PLD)), dict(JN), dict(BAD))
