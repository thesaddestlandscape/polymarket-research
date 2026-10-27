#!/usr/bin/env python3
"""forward_a1.py -- wrapper diario IDEMPOTENTE del forward pasivo de A1/F5 (mitigar_as_25oct). Solo lectura; sin dinero real; sin tocar PREREG_A1 ni los scripts originales.
REGLA CONGELADA: regla_congelada.json (cortes/terciles del TRAIN 06-08 Oct). Diseno y gate: PREREG_FWD.md (sha en PREREG_FWD.sha256).
Uso:  python3 -I forward_a1.py todo            # procesa los dias nuevos elegibles >= 24-Oct y reagrega (lo que hace el cron)
      python3 -I forward_a1.py dia YYYY-MM-DD   # fuerza un dia (p. ej. validacion)
      python3 -I forward_a1.py agrega           # solo regenera forward_diario.csv y RESUMEN.md desde las caches
Entorno (tests): FWD_REG (dir de m5_registro), FWD_DL (cache/datalogs), FWD_OUT (salida), FWD_DESDE, FWD_DES (json extra de desenlaces), FWD_NOGAMMA=1, FWD_NOCHECKPRE=1 (validar un dia pre-congelacion).
Contrato: run_manifest.json por dia (hash de codigo/regla, parametros, hashes de entrada, estado, cobertura); cache atomica por dia (prints_D.pkl) = checkpoint;
forward_diario.csv se REGENERA desde todas las caches (no se anexa => sin duplicados posibles). Estados por dia: COMPLETE | PENDING_DESENLACE | BLOCKED | FAILED."""
import os, sys, io, gc, glob, gzip, json, time, hashlib, subprocess, numpy as np, pandas as pd
from scipy import stats
AQ = os.path.dirname(os.path.abspath(__file__))
REG = os.environ.get('FWD_REG', '/mnt/HC_Volume_106538179/m5_registro')
DL = os.environ.get('FWD_DL', '/root/polymarket-research-datalogs/mitigar_as_25oct/forward') + '/'
OUT = os.environ.get('FWD_OUT', AQ) + '/'
DESDE = os.environ.get('FWD_DESDE', '2026-10-24')
DES_CACHE = '/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'
DES_EXTRA = os.path.join(AQ, '../salida/datos/desenlaces_extra.json')   # puede no existir: opcional
COINS = ('ETH', 'SOL', 'XRP', 'BTC', 'DOGE', 'BNB'); PRIM = ('ETH', 'SOL', 'XRP'); REPL = ('BTC', 'DOGE', 'BNB')
SH = np.int64(1) << np.int64(41)
VERSION = 'fwd_a1_v1'
os.makedirs(DL, exist_ok=True)
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def ahora(): return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
def log(*a):
    s = ahora() + ' ' + ' '.join(map(str, a)); print(s, flush=True)
    with open(DL + 'forward.log', 'a') as f: f.write(s + '\n')
def atomic_json(p, o):
    t = p + '.tmp'; json.dump(o, open(t, 'w'), indent=1, default=str); os.replace(t, p)
def check_prereg():
    if os.environ.get('FWD_NOCHECKPRE'): return
    h = open(os.path.join(AQ, 'PREREG_FWD.sha256')).read().split()[0]
    assert sha(os.path.join(AQ, 'PREREG_FWD.md')) == h, 'PREREG_FWD.md no coincide con su sha256: abortar'
RULE_P = os.path.join(AQ, 'regla_congelada.json')
RULE = json.load(open(RULE_P)); C0, C1 = RULE['cortes_F5_terciles_train']; F2E = np.array(RULE['F2_deciles_train'])
assert RULE['tercil_marcado'] == 2   # marcar F5 > C1
CODE_SHA = sha(os.path.abspath(__file__)); RULE_SHA = sha(RULE_P)

# ---------------------------------------------------------------- extraccion (una pasada por fichero; solo lectura)
def dia_ant(D): return (pd.Timestamp(D) - pd.Timedelta(days=1)).strftime('%Y-%m-%d')
def midnight_ms(D): return int(pd.Timestamp(D, tz='UTC').timestamp() * 1000)
def extrae_dia(D, fich, kprev):
    """Una pasada: k (5min, 6 monedas) -> kD.csv; t de tokens conocidos -> tD.csv; q de tokens 5min bid [0,03;0,45] -> qD.gz; cola de q (ultimos 120 s del dia) -> tail."""
    pre = DL + f'{D}_'
    fin_dia = midnight_ms(D) + 86400000 - 120000
    prog = r'''BEGIN{FS=","; split(COINS,cs,","); for(i in cs) C[cs[i]]=1}
FILENAME==KP{ if($1!="") K[$1]=1; next }
$1=="k" && $5=="5min" && ($4 in C) {K[$3]=1; print > KOUT; next}
$1=="t" && ($3 in K) {print $2","$3","$4","$5","$6","$7 > TOUT; next}
$1=="x" && ($3=="ETHUSDT"||$3=="SOLUSDT"||$3=="XRPUSDT") {print substr($3,1,3)","$8","$4 | XCMD; next}
$1=="q" && ($3 in K) && $4>=0.03 && $4<=0.45 {l=$3","$8","$4","$5","$6","$7; print l | QCMD; if($8>=FIN) print l | TCMD}'''
    kp = DL + f'ktok_prev_{D}.txt'
    with open(kp, 'w') as f:
        for t in kprev: f.write(t + '\n')
    cmd = (f"zcat {fich} | awk -v COINS={','.join(COINS)} -v KP={kp} -v KOUT={pre}k.csv -v TOUT={pre}t.csv -v FIN={fin_dia} "
           f"-v XCMD='gzip -c > {pre}x.tmp.gz' -v QCMD='gzip -c > {pre}q.tmp.gz' -v TCMD='gzip -c > {pre}tail.tmp.gz' '{prog}' {kp} -")
    t0 = time.time(); r = subprocess.run(['bash', '-o', 'pipefail', '-c', cmd], capture_output=True, text=True)
    if r.returncode != 0: raise RuntimeError('extraccion fallo: ' + r.stderr[-400:])
    for f in ('q', 'tail', 'x'):
        if os.path.exists(pre + f + '.tmp.gz'): os.replace(pre + f + '.tmp.gz', pre + f + '.gz')
        else: gzip.open(pre + f + '.gz', 'wb').close()
    os.remove(kp); log(D, 'extraido en', round(time.time() - t0), 's')
def lee_k(p):
    K = {}
    if os.path.exists(p):
        for ln in open(p):
            c = ln.rstrip('\n').split(',')
            K[c[2]] = (c[3], c[5], pd.Timestamp(c[6]).timestamp(), c[7])
    return K

# ---------------------------------------------------------------- desenlaces
def desenlaces(mids):
    D = json.load(open(DES_CACHE))
    if os.path.exists(DES_EXTRA): D.update(json.load(open(DES_EXTRA)))
    ex = os.environ.get('FWD_DES')
    if ex and os.path.exists(ex): D.update(json.load(open(ex)))
    P = DL + 'desenlaces_fwd.json'; loc = json.load(open(P)) if os.path.exists(P) else {}
    pend = sorted(m for m in mids if m not in D and m not in loc)
    if pend and not os.environ.get('FWD_NOGAMMA'):
        import requests
        s = requests.Session()
        for k in range(0, len(pend), 40):
            try:
                for m in s.get('https://gamma-api.polymarket.com/markets', timeout=20, params=[('id', x) for x in pend[k:k + 40]] + [('closed', 'true'), ('limit', '40')]).json() or []:
                    pr = m.get('outcomePrices'); pr = json.loads(pr) if isinstance(pr, str) else pr
                    if pr and float(pr[0]) >= 0.999: loc[str(m['id'])] = 'YES'
                    elif pr and float(pr[1]) >= 0.999: loc[str(m['id'])] = 'NO'
            except Exception as e: log('gamma lote', k // 40, type(e).__name__)
            time.sleep(0.25)
        atomic_json(P, loc)
    D.update(loc); return D

# ---------------------------------------------------------------- rasgos (copia FIEL de a1_rasgos.py: estado() y F1..F8; tau = r-100 ms, 250 ms, control)
def leeq(path, keep):
    out = []
    for ch in pd.read_csv(path, header=None, names=['id', 'r', 'b', 'a', 'tb', 'ta'], chunksize=2_000_000, compression='gzip',
                          dtype={'id': str, 'r': np.int64, 'b': np.float32, 'a': np.float32, 'tb': np.float32, 'ta': np.float32}, on_bad_lines='skip'):
        out.append(ch[ch.id.isin(keep)].dropna())
    return pd.concat(out, ignore_index=True) if out else pd.DataFrame(columns=['id', 'r', 'b', 'a', 'tb', 'ta'])
def estado(K, R, ids, t):
    k = ids * SH + t; i = np.searchsorted(K, k, 'right') - 1; ok = (i >= 0); i = np.maximum(i, 0)
    ok &= ((K[i] // SH) == ids) & ((t - R[i]) <= 30000)
    return i, ok
def rasgos(F, Q, seed):
    """F: rellenos con columnas r, fin, tid (int). Q: filas q (id int, r, b, a, tb, ta). Devuelve F con F1..F8, bid y variantes _250 y _c."""
    K = Q.id.values.astype(np.int64) * SH + Q.r.values; o = np.lexsort((Q.ta.values, Q.tb.values, Q.a.values, Q.b.values, K)); K = K[o]
    R = Q.r.values[o]; B = Q.b.values[o]; A = Q.a.values[o]; TB = Q.tb.values[o]; TA = Q.ta.values[o]; IDs = Q.id.values.astype(np.int64)[o]
    u = np.ones(len(K), bool); u[1:] = (K[1:] != K[:-1]) | (B[1:] != B[:-1]) | (A[1:] != A[:-1]) | (TB[1:] != TB[:-1]) | (TA[1:] != TA[:-1])
    K, R, B, A, TB, TA, IDs = K[u], R[u], B[u], A[u], TB[u], TA[u], IDs[u]
    chg = np.ones(len(K), bool); chg[1:] = (IDs[1:] != IDs[:-1]) | (B[1:] != B[:-1]) | (A[1:] != A[:-1])
    LC = np.maximum.accumulate(np.where(chg, K, 0)) - IDs * SH
    ids = F.tid.values.astype(np.int64); rng = np.random.default_rng(seed)
    rc = F.r.values - rng.integers(5000, 30001, len(F)); res = {}
    for tag, base, lag in (('', F.r.values, 100), ('_250', F.r.values, 250), ('_c', rc, 100)):
        tau = base - lag
        i1, ok1 = estado(K, R, ids, tau); i0, ok0 = estado(K, R, ids, tau - 2000)
        ok1 &= (ids >= 0) & (B[i1] < A[i1]); ok0 &= ok1
        mid1 = (B[i1] + A[i1]) / 2; mid0 = (B[i0] + A[i0]) / 2
        pos0 = np.searchsorted(K, ids * SH + (tau - 2000), 'right')
        res['F1' + tag] = np.where(ok1, A[i1] - B[i1], np.nan)
        res['F2' + tag] = np.where(ok1, TB[i1] / np.maximum(TB[i1] + TA[i1], 1e-9), np.nan)
        res['F3' + tag] = np.where(ok0, np.log1p(TB[i1]) - np.log1p(TB[i0]), np.nan)
        res['F4' + tag] = np.where(ok0, mid1 - mid0, np.nan)
        res['F5' + tag] = np.where(ok1, np.log1p(TA[i1]), np.nan)
        res['F6' + tag] = np.where(ok1, (i1 + 1 - pos0).astype(float), np.nan)
        res['F7' + tag] = np.where(ok1, (tau - LC[i1]).astype(float), np.nan)
        res['F8' + tag] = F.fin.values - base / 1000.0
        res['bid' + tag] = np.where(ok1, B[i1], np.nan)
    F = F.copy()
    for k, v in res.items(): F[k] = v
    return F

# ---------------------------------------------------------------- ventanas R1 (copia de e1d_pob.py: vol() sobre rejilla de 10 s, ultimo precio con recepcion <= g) + control de huecos
def lv(ta, va, t):
    i = np.searchsorted(ta, t, 'right') - 1; return np.where(i >= 0, va[np.maximum(i, 0)], np.nan)
def lee_x(D, Dp):
    X = pd.read_csv(DL + f'{D}_x.gz', header=None, names=['c', 'r', 'p'], compression='gzip', on_bad_lines='skip') if os.path.getsize(DL + f'{D}_x.gz') > 0 else pd.DataFrame(columns=['c', 'r', 'p'])
    tp = DL + f'xtail_{Dp}.pkl'
    if not os.path.exists(tp):
        fp = f'{REG}/m5_registro_{Dp}.csv.gz'; fin_p = midnight_ms(D) - 3700000
        if os.path.exists(fp):
            subprocess.run(['bash', '-o', 'pipefail', '-c', f"zcat {fp} | awk -F, -v FIN={fin_p} '$1==\"x\" && ($3==\"ETHUSDT\"||$3==\"SOLUSDT\"||$3==\"XRPUSDT\") && $8>=FIN {{print substr($3,1,3)\",\"$8\",\"$4}}' > {tp}.csv"], check=True)
            pd.read_csv(tp + '.csv', header=None, names=['c', 'r', 'p']).to_pickle(tp); os.remove(tp + '.csv')
    P = pd.read_pickle(tp) if os.path.exists(tp) else pd.DataFrame(columns=['c', 'r', 'p'])
    X = pd.concat([P, X], ignore_index=True); X['r'] = X.r.astype(np.int64); X['p'] = X.p.astype(float)
    return X
def ventanas(D, K):
    Dp = dia_ant(D); X = lee_x(D, Dp); W = []
    A = {}
    for c in PRIM:
        a = X[X.c == c].sort_values('r', kind='stable'); A[c] = (a.r.values, a.p.values)
    mx = X.r.max() if len(X) else 0; X[X.r >= mx - 3700000].to_pickle(DL + f'xtail_{D}.pkl')
    seen = {}
    for t, v in K.items():
        if v[0] in PRIM: seen[(v[0], v[1])] = v[2]
    for (coin, mid), fin in seen.items():
        if pd.Timestamp(fin, unit='s').strftime('%Y-%m-%d') != D: continue
        ta, pa = A[coin]; t0 = int((fin - 300) * 1000)
        if not len(ta): W.append(dict(coin=coin, mid=mid, fin=fin, dia=D, R1=np.nan, gap_frac=np.nan)); continue
        g = np.arange(t0 - 900000, t0 + 1, 10000); p = lv(ta, pa, g); r = np.diff(np.log(p))
        i = np.searchsorted(ta, g, 'right') - 1; age = np.where(i >= 0, g - ta[np.maximum(i, 0)], 10 ** 9)
        W.append(dict(coin=coin, mid=mid, fin=fin, dia=D, R1=float(np.nanstd(r) * 1e4) if np.isfinite(r).sum() > 5 else np.nan, gap_frac=float((age > 10000).mean())))
    return pd.DataFrame(W, columns=['coin', 'mid', 'fin', 'dia', 'R1', 'gap_frac'])

# ---------------------------------------------------------------- un dia: rellenos poblacionales (copia de la logica de e1d_pob.py sin Binance) + rasgos
def procesa_dia(D, forzar=False):
    mp = DL + f'prints_{D}.pkl'; mf = DL + f'manifest_{D}.json'
    if os.path.exists(mp) and os.path.exists(mf) and os.path.exists(DL + f'ventanas_{D}.pkl') and not forzar:
        m = json.load(open(mf))
        if m.get('estado') == 'COMPLETE' and m.get('code_sha256') == CODE_SHA and m.get('regla_sha256') == RULE_SHA:
            try:
                n = len(pd.read_pickle(mp))
                if n == m['cobertura']['prints_guardados']: log(D, 'ya COMPLETE y valido (idempotente): omito'); return 'COMPLETE'
            except Exception as e: log(D, 'cache corrupta, se reconstruye:', type(e).__name__)
    fich = f'{REG}/m5_registro_{D}.csv.gz'
    man = dict(job='forward_a1', version=VERSION, dia=D, inicio=ahora(), estado='RUNNING', code_sha256=CODE_SHA, regla_sha256=RULE_SHA,
               prereg_sha256=(sha(os.path.join(AQ, 'PREREG_FWD.md')) if os.path.exists(os.path.join(AQ, 'PREREG_FWD.md')) else None),
               parametros=dict(banda_q='(0,10;0,30]', ventana_s=300, tau_ms=100, estado_max_s=30, monedas=COINS, rellenos='print t por recepcion c[6]; SELL->bid de s; BUY->bid de opuesto 1-p'),
               entrada=dict(fichero=fich, bytes=os.path.getsize(fich) if os.path.exists(fich) else None, mtime=(time.strftime('%FT%TZ', time.gmtime(os.path.getmtime(fich))) if os.path.exists(fich) else None)))
    atomic_json(mf, man)
    try:
        if not os.path.exists(fich): raise FileNotFoundError(fich)
        # mapa k del dia anterior (cache) para tokens creados antes de medianoche
        Dp = dia_ant(D); kp_file = DL + f'{Dp}_k.csv'
        if not os.path.exists(kp_file):    # k de D-1: una pasada ligera solo si no esta (primer dia de la serie)
            fp = f'{REG}/m5_registro_{Dp}.csv.gz'
            if os.path.exists(fp):
                subprocess.run(['bash', '-o', 'pipefail', '-c', f"zcat {fp} | awk -F, '$1==\"k\" && $5==\"5min\"' > {kp_file}.tmp && mv {kp_file}.tmp {kp_file}"], check=True)
        Kprev = lee_k(kp_file)
        extrae_dia(D, fich, set(Kprev.keys()))
        K = dict(Kprev); K.update(lee_k(DL + f'{D}_k.csv'))
        K = {t: v for t, v in K.items() if v[0] in COINS}
        T = pd.read_csv(DL + f'{D}_t.csv', header=None, names=['r', 'tok', 'p', 'side', 'acc', 'rr'], dtype={'tok': str}, on_bad_lines='skip')
        T['r'] = pd.to_numeric(T.rr, errors='coerce'); T = T.dropna(subset=['r', 'p', 'acc']); T['r'] = T.r.astype(np.int64)
        T = T[['r', 'tok', 'p', 'side', 'acc']]; n_t0 = len(T); T = T.drop_duplicates(); n_dup = n_t0 - len(T); T = T[T.tok.isin(K)].copy()
        T['coin'] = T.tok.map(lambda t: K[t][0]); T['mid'] = T.tok.map(lambda t: K[t][1]); T['fin'] = T.tok.map(lambda t: K[t][2]); T['lado'] = T.tok.map(lambda t: K[t][3])
        sell = T.side == 'SELL'
        T['lado_m'] = np.where(sell, T.lado, np.where(T.lado == 'YES', 'NO', 'YES')); T['q'] = np.where(sell, T.p, 1 - T.p).round(3)
        F = T[(T.q > 0.10 + 1e-9) & (T.q <= 0.30 + 1e-9) & (T.r / 1000 < T.fin) & (T.r / 1000 >= T.fin - 300)].copy()
        n_fill_all = len(F)
        DES = desenlaces(set(F.mid.unique()))
        F['w'] = F.mid.map(DES); F['coste'] = F.q * F.acc
        sin_des = F[F.w.isna()]; cob_coste = 1 - sin_des.coste.sum() / max(F.coste.sum(), 1e-9)
        faltan = {c: round(float(g.coste.sum()), 2) for c, g in sin_des.groupby('coin')}
        if cob_coste < 0.995:
            man.update(estado='PENDING_DESENLACE', fin=ahora(), cobertura=dict(rellenos_banda=n_fill_all, rellenos_sin_desenlace=int(len(sin_des)), cobertura_desenlace_coste=round(cob_coste, 5), coste_sin_desenlace_por_moneda=faltan))
            atomic_json(mf, man); log(D, 'PENDING_DESENLACE cobertura coste', round(cob_coste, 4)); return 'PENDING_DESENLACE'
        F = F[F.w.notna()].copy()
        F['gana'] = (F.lado_m == F.w).astype(float); F['pnl'] = (F.gana - F.q) * F.acc
        F['dia'] = D; F['hora'] = ((F.r // 3600000) % 24).astype(int)
        # ids de token del maker y filas q (dia + cola del anterior)
        tid = {}
        for t, v in K.items(): tid[(v[1], v[3])] = t
        F['tokm'] = [tid.get((m, l), None) for m, l in zip(F.mid, F.lado_m)]
        F = F[F.tokm.notna()].copy(); keep = set(F.tokm.unique().tolist())
        Q = leeq(DL + f'{D}_q.gz', keep)
        tp = DL + f'{Dp}_tail.gz'
        if not os.path.exists(tp):
            fp = f'{REG}/m5_registro_{Dp}.csv.gz'; man['aviso_cola'] = 'cola del dia anterior extraida del fichero D-1'
            if os.path.exists(fp):
                fin_p = midnight_ms(D) - 120000
                subprocess.run(['bash', '-o', 'pipefail', '-c', f"zcat {fp} | awk -F, -v FIN={fin_p} '$1==\"q\" && $4>=0.03 && $4<=0.45 && $8>=FIN {{print $3\",\"$8\",\"$4\",\"$5\",\"$6\",\"$7}}' | gzip -c > {tp}.tmp && mv {tp}.tmp {tp}"], check=True)
        if os.path.exists(tp):
            P = leeq(tp, keep); t0 = midnight_ms(D) - 120000; Q = pd.concat([P[P.r >= t0], Q], ignore_index=True)
        codes = {t: i for i, t in enumerate(sorted(keep))}
        Q['id'] = Q.id.map(codes).astype(np.int64); F['tid'] = F.tokm.map(codes).astype(np.int64)
        F = rasgos(F.reset_index(drop=True), Q, int(D.replace('-', '')))
        F = F.drop(columns=['w', 'tokm', 'tok', 'p', 'side', 'lado'], errors='ignore')
        V = ventanas(D, K); tv = DL + f'ventanas_{D}.pkl.tmp'; V.to_pickle(tv); os.replace(tv, DL + f'ventanas_{D}.pkl')
        tmp = mp + '.tmp'; F.to_pickle(tmp); os.replace(tmp, mp)
        man.update(estado='COMPLETE', fin=ahora(), cobertura=dict(
            t_rows_conocidos=int(len(T)), rellenos_banda=n_fill_all, rellenos_sin_desenlace=int(len(sin_des)), cobertura_desenlace_coste=round(cob_coste, 5),
            prints_guardados=int(len(F)), por_moneda={c: int(n) for c, n in F.coin.value_counts().items()}, F5_valido=round(float(np.isfinite(F.F5).mean()), 4),
            t_filas_leidas=int(n_t0), t_duplicados_exactos_descartados=int(n_dup), tokens_mapa=len(K), filas_q_usadas=int(len(Q)), ventanas_R1=int(len(V)), ventanas_R1_por_moneda={c: int(n) for c, n in V.coin.value_counts().items()}, ventanas_R1_sin_valor=int(V.R1.isna().sum())))
        atomic_json(mf, man); log(D, 'COMPLETE prints', len(F), 'F5 valido', man['cobertura']['F5_valido']); gc.collect()
        for s in ('q', 't', 'x'):
            for suf in ('.csv' if s == 't' else '.gz',):
                p = DL + f'{D}_{s}{suf}'
                if os.path.exists(p) and not os.environ.get('FWD_KEEPQ'): os.remove(p)
        return 'COMPLETE'
    except Exception as e:
        man.update(estado='FAILED', fin=ahora(), error=f'{type(e).__name__}: {e}'); atomic_json(mf, man); log(D, 'FAILED', man['error']); return 'FAILED'

# ---------------------------------------------------------------- evaluacion diaria por grupo/variante
def cell_f2(F2): return np.where(np.isfinite(F2), np.searchsorted(F2E, np.nan_to_num(F2), 'right'), -1)
def exc_global(pnl, coste, m):
    fd = coste[m].sum() / max(coste.sum(), 1e-12); return fd * pnl.sum() - pnl[m].sum(), fd
def evalua_dia(X, D, grupo, monedas):
    G = X[X.coin.isin(monedas)]; rows = []; cier = []
    if not len(G): return rows, cier
    F5 = G.F5.values; pnl = G.pnl.values; co = G.coste.values
    m = np.isfinite(F5) & (F5 > C1); m2 = np.isfinite(G.F5_250.values) & (G.F5_250.values > C1)
    mi = np.isfinite(F5) & (F5 > C0) & (F5 <= C1)      # INVERSION congelada: tercil medio (el de mayor EV en el train 06-08)
    e, fd = exc_global(pnl, co, m); ei, _ = exc_global(pnl, co, mi); e250, _ = exc_global(pnl, co, m2)
    # control: instantes r-U[5,30] s con bid en banda (0,10;0,30]
    vc = G.F5_c.values; bc = G.bid_c.values; okc = np.isfinite(vc) & (bc > 0.10) & (bc <= 0.30)
    ev_all = pnl.sum() / max(co.sum(), 1e-12)
    ev_m = pnl[m].sum() / max(co[m].sum(), 1e-12) if m.any() else np.nan; ev_r = pnl[~m].sum() / max(co[~m].sum(), 1e-12)
    base = dict(dia=D, grupo=grupo, n=len(G), coste=co.sum(), pnl=pnl.sum(), ev_all=ev_all)
    rows.append(dict(base, variante='global', exceso=e, frac_eur=fd, n_marc=int(m.sum()), coste_marc=co[m].sum(), pnl_marc=pnl[m].sum(), ev_marc=ev_m, ev_ret=ev_r,
                     exceso_inv=ei, exceso_tau250=e250, tasa_disparo_prerelleno=float(m[np.isfinite(F5)].mean()) if np.isfinite(F5).any() else np.nan,
                     tasa_disparo_control=float((vc[okc] > C1).mean()) if okc.any() else np.nan, F5_valido=float(np.isfinite(F5).mean())))
    # base F2 decil x moneda x hora (placebo estratificado dentro del dia)
    cell = pd.Series(cell_f2(G.F2.values).astype(str)) + '|' + pd.Series(G.coin.values) + '|' + pd.Series(G.hora.values.astype(str))
    df = pd.DataFrame({'c': cell.values, 'pnl': pnl, 'co': co, 'm': m}); es = 0.0; fm = 0.0
    for _, g in df.groupby('c'):
        cs = g.co.sum()
        if cs <= 0: continue
        f = g.co[g.m].sum() / cs; es += f * g.pnl.sum() - g.pnl[g.m].sum()
    rows.append(dict(base, variante='base_F2xmonedaxhora', exceso=es, frac_eur=fd, n_marc=int(m.sum()), coste_marc=co[m].sum(), pnl_marc=pnl[m].sum(), ev_marc=ev_m, ev_ret=ev_r))
    # por nivel de armado: bajo el mejor bid (tipo B) / al mejor bid
    q = G.q.values; bid = G.bid.values
    for nom, sel in (('nivel_bajo_mejor_bid', np.isfinite(bid) & (q < bid - 0.005)), ('nivel_al_mejor_bid', np.isfinite(bid) & (np.abs(q - bid) < 0.005))):
        if sel.sum() == 0: continue
        pn, cs_, ms = pnl[sel], co[sel], m[sel]; es_, fs = exc_global(pn, cs_, ms)
        rows.append(dict(base, n=int(sel.sum()), coste=cs_.sum(), pnl=pn.sum(), ev_all=pn.sum() / cs_.sum(), variante=nom, exceso=es_, frac_eur=fs, n_marc=int(ms.sum()), coste_marc=cs_[ms].sum(),
                         pnl_marc=pn[ms].sum(), ev_marc=pn[ms].sum() / max(cs_[ms].sum(), 1e-12) if ms.any() else np.nan, ev_ret=pn[~ms].sum() / max(cs_[~ms].sum(), 1e-12)))
    # cierres (cluster) para el bootstrap: variante global
    g2 = pd.DataFrame({'fin': G.fin.values, 'e': fd * pnl - np.where(m, pnl, 0)}).groupby('fin').e.sum()
    cier = [dict(dia=D, grupo=grupo, fin=float(k), e=float(v)) for k, v in g2.items()]
    return rows, cier

GRUPOS = [('ALL3_ETH_SOL_XRP', PRIM), ('REPLICA3_BTC_DOGE_BNB', REPL)] + [(c, (c,)) for c in COINS]
def agrega():
    mans = sorted(glob.glob(DL + 'manifest_*.json')); filas = []; cier = []; estados = {}
    for mf in mans:
        m = json.load(open(mf)); D = m['dia']; estados[D] = m
        if m.get('estado') != 'COMPLETE' or D < DESDE: continue
        mp = DL + f'prints_{D}.pkl'
        if not os.path.exists(mp): estados[D]['estado'] = 'FAILED(cache ausente)'; continue
        X = pd.read_pickle(mp)
        for g, mons in GRUPOS:
            r, c = evalua_dia(X, D, g, mons); filas += r; cier += c
    T = pd.DataFrame(filas)
    if len(T): T = T.sort_values(['grupo', 'variante', 'dia']).reset_index(drop=True)
    tmp = OUT + 'forward_diario.csv.tmp'; T.to_csv(tmp, index=False, float_format='%.6g'); os.replace(tmp, OUT + 'forward_diario.csv')
    C = pd.DataFrame(cier); tmpc = DL + 'forward_cierres.csv.tmp'; C.to_csv(tmpc, index=False); os.replace(tmpc, DL + 'forward_cierres.csv')
    resumen(T, C, estados); return T

def tstats(e):
    e = np.asarray(e, float); n = len(e)
    if n < 2: return dict(n=n, suma=float(e.sum()), lo=np.nan, hi=np.nan, p=np.nan, sin2=np.nan, pos=int((e > 0).sum()))
    se = e.std(ddof=1) / np.sqrt(n); t = e.mean() / se if se > 0 else np.nan; h = stats.t.ppf(0.95, n - 1) * se
    return dict(n=n, suma=float(e.sum()), lo=float(e.mean() - h), hi=float(e.mean() + h), p=float(1 - stats.t.cdf(t, n - 1)) if se > 0 else np.nan,
                sin2=float(np.sort(e)[:-2].sum()) if n > 2 else np.nan, pos=int((e > 0).sum()))
def resumen(T, C, estados):
    L = ['# RESUMEN forward A1/F5 (mitigar_as_25oct) -- generado ' + ahora(), '',
         'Pasivo, solo lectura, 0 EUR validados. Regla congelada (`regla_congelada.json`, TRAIN 06-08 Oct): marcar F5 = log1p(tamano ask propio a r-100 ms) > %.4f. Prereg `PREREG_FWD.md`.' % C1, '']
    ok = sorted(d for d, m in estados.items() if m.get('estado') == 'COMPLETE' and d >= DESDE)
    L.append(f'Dias COMPLETE acumulados: **{len(ok)}** ({", ".join(ok) if ok else "ninguno"}). Gate PREREG_A1 exige >=10 dias nuevos.')
    otros = {d: m.get('estado') for d, m in estados.items() if m.get('estado') != 'COMPLETE' and d >= DESDE}
    if otros: L.append('Dias NO completos: ' + ', '.join(f'{d}={s}' for d, s in sorted(otros.items())))
    L.append('')
    if not len(T): L.append('Sin datos aun.'); open(OUT + 'RESUMEN.md', 'w').write('\n'.join(L) + '\n'); return
    L += ['## Cobertura por dia (manifiestos)', '| dia | estado | rellenos banda | prints | cobertura desenlace (coste) | F5 valido | por moneda |', '|---|---|---|---|---|---|---|']
    for d in ok:
        c = estados[d]['cobertura']; L.append(f"| {d} | COMPLETE | {c['rellenos_banda']} | {c['prints_guardados']} | {c['cobertura_desenlace_coste']} | {c['F5_valido']} | {c['por_moneda']} |")
    L += ['', '## Acumulado por grupo y variante (EXCESO en USD vs placebo; IC90 y p por dias, t de una cola)',
          '| grupo | variante | dias | exceso acum. | IC90 dias | p | sin 2 mejores | dias + | inversion acum. | tau250 acum. | EV marc. | EV ret. | EV total |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
    for g, _ in GRUPOS:
        for v in ('global', 'base_F2xmonedaxhora', 'nivel_bajo_mejor_bid', 'nivel_al_mejor_bid'):
            S = T[(T.grupo == g) & (T.variante == v)]
            if not len(S): continue
            s = tstats(S.exceso.values); inv = S.exceso_inv.sum() if v == 'global' else np.nan; t250 = S.exceso_tau250.sum() if v == 'global' else np.nan
            evm = S.pnl_marc.sum() / S.coste_marc.sum() if S.coste_marc.sum() > 0 else np.nan
            rc = S.coste.sum() - S.coste_marc.sum(); evr = (S.pnl.sum() - S.pnl_marc.sum()) / rc if rc > 0 else np.nan
            L.append(f"| {g} | {v} | {s['n']} | {s['suma']:.0f} | ({s['lo']:.0f}, {s['hi']:.0f})/dia | {s['p']:.4f} | {s['sin2']:.0f} | {s['pos']}/{s['n']} | {inv:.0f} | {t250:.0f} | {evm:.3f} | {evr:.3f} | {S.pnl.sum() / S.coste.sum():.3f} |")
    L += ['', '## Por dia, grupo ALL3 (ETH/SOL/XRP), variante global', '| dia | n | coste | EV total | exceso | frac EUR marcada | EV marc. | EV ret. | inversion | tau250 | disparo control / pre-relleno |', '|---|---|---|---|---|---|---|---|---|---|---|']
    for _, r in T[(T.grupo == 'ALL3_ETH_SOL_XRP') & (T.variante == 'global')].iterrows():
        L.append(f"| {r.dia} | {int(r.n)} | {r.coste:.0f} | {r.ev_all:.3f} | {r.exceso:.0f} | {r.frac_eur:.2f} | {r.ev_marc:.3f} | {r.ev_ret:.3f} | {r.exceso_inv:.0f} | {r.exceso_tau250:.0f} | {r.tasa_disparo_control:.2f} / {r.tasa_disparo_prerelleno:.2f} |")
    # gate
    S = T[(T.grupo == 'ALL3_ETH_SOL_XRP') & (T.variante == 'global')]; n = len(S)
    L += ['', '## Gate PREREG_A1 adaptado al forward (ver PREREG_FWD.md), grupo ALL3 / global']
    if n < 2: L.append(f'Dias {n}/10: EN CURSO, sin veredicto.')
    else:
        s = tstats(S.exceso.values); cl = C[C.grupo == 'ALL3_ETH_SOL_XRP']; rng = np.random.default_rng(20261026); v = cl.e.values
        bs = [v[rng.integers(0, len(v), len(v))].sum() for _ in range(1000)] if len(v) else [np.nan]
        dd = (S.ev_ret - S.ev_all).values; sd = tstats(dd); Sb = T[(T.grupo == 'ALL3_ETH_SOL_XRP') & (T.variante == 'base_F2xmonedaxhora')]; sb = tstats(Sb.exceso.values)
        g = {'1_exceso>0 e IC90 dias inferior>0': s['suma'] > 0 and s['lo'] > 0, '2_p<0,05 (hipotesis unica)': s['p'] < 0.05, '2b_p<0,05/8 (estricto, informativo)': s['p'] < 0.05 / 8,
             '3_sin 2 mejores dias>0': s['sin2'] > 0, '4_inversion<0': S.exceso_inv.sum() < 0, '5_dias+ >= 2/3': s['pos'] >= np.ceil(2 * n / 3),
             '6_IC90 cierre inferior>0': float(np.nanquantile(bs, 0.05)) > 0, '7_EV ret - total, IC90 dias inferior>0': sd['lo'] > 0,
             'RT_base F2xmonedaxhora exceso>0 e IC90 inferior>0': sb['suma'] > 0 and sb['lo'] > 0}
        for k, vv in g.items(): L.append(f"- {k}: {'SI' if vv else 'no'}")
        nucleo = [k for k in g if k[0] in '1234567' and k != '2b_p<0,05/8 (estricto, informativo)']
        L.append(f"- IC90 cierre (bootstrap 1000, semilla 20261026): ({np.nanquantile(bs, .05):.0f}, {np.nanquantile(bs, .95):.0f}); EV ret - total IC90 dias ({sd['lo']:.4f}, {sd['hi']:.4f})")
        if n < 10: L.append(f'**Dias {n}/10: EN CURSO (lo anterior es descriptivo, NO veredicto).**')
        else: L.append('**VEREDICTO forward: ' + ('PASA 7/7 + base RT (CONFIRMADO-forward en poblacion; NO es capacidad de B)' if all(g[k] for k in nucleo) and g['RT_base F2xmonedaxhora exceso>0 e IC90 inferior>0'] else 'NO PASA (ver cuales fallan)') + '**')
    L += ['', 'Limites: unidad = print poblacional (no orden con cola); placebo sustractivo; EUR validados 0; exige reaccion <=100-150 ms desde recepcion + cancelacion 60 ms (sin medir con ordenes propias).', '']
    open(OUT + 'RESUMEN.md', 'w').write('\n'.join(L))

def elegibles():
    hoy = pd.Timestamp.now(tz='UTC').normalize(); out = []
    for f in sorted(glob.glob(f'{REG}/m5_registro_2026-??-??.csv.gz')):
        D = os.path.basename(f)[12:22]
        if D < DESDE or pd.Timestamp(D, tz='UTC') >= hoy: continue
        # fichero cerrado: modificado hace >30 min y escrito tras el fin del dia
        if time.time() - os.path.getmtime(f) < 1800 or os.path.getmtime(f) < midnight_ms(D) / 1000 + 86400: continue
        out.append(D)
    return out

if __name__ == '__main__':
    check_prereg(); modo = sys.argv[1] if len(sys.argv) > 1 else 'todo'
    if modo == 'dia': procesa_dia(sys.argv[2], forzar='--forzar' in sys.argv); agrega()
    elif modo == 'agrega': agrega()
    else:
        res = {D: procesa_dia(D) for D in elegibles()}; log('resultado', res); agrega()
        if any(v == 'FAILED' for v in res.values()): sys.exit(3)
