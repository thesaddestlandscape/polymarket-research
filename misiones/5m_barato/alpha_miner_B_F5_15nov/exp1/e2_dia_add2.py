#!/usr/bin/env python3
"""e2_dia_add2.py DIA -- ADDENDUM2 §2: copia de e2_dia.py en la que SOLO cambia C3 (epoca por suelo medido por ventana de 10 min, no por constantes de timestamp) y los nombres de salida (*_add2). Solo para 2026-10-16 y 2026-10-24. Original: E2 (ADDENDUM1): extraccion de UN dia de m5_registro (una pasada zcat|awk; solo lectura) -> prints bid en banda con EX y RX, filas q (bid [0,03;0,45]) con rx y rx-ex,
barras de 1 min de Binance; features F5/bid/categoria por spec con r_v3 = r_ex - c - 1 (C2), t_dec = r_v3 + delta - l_ef - d_proc (C4), estado q por RX <= t_dec (C5), epoca por timestamp y assert de suelo (C3).
Salida idempotente: cache/pob_D.pkl.gz + cache/pob_D.json (estado COMPLETE) + cache/bn_D.csv + cache/k_D.csv. Un assert que falla aborta ESTE dia (rc 1) y queda FAILED en el manifiesto (C10).
Estados: COMPLETE | PENDING_DESENLACE (cobertura coste < 0,995; rc 3) | FAILED. --smoke N: solo las primeras N lineas del fichero, salida a cache/smoke_* (no toca la cache real)."""
import os, sys, gc, time, subprocess, hashlib; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib1 import *
D = sys.argv[1]; SMOKE = int(sys.argv[sys.argv.index('--smoke') + 1]) if '--smoke' in sys.argv else 0
PRIM = ('ETH', 'SOL', 'XRP'); COINS = 'ETH,SOL,XRP,BTC,DOGE,BNB'
pre = CACHE + ('smoke_' if SMOKE else '') + D + '_'; man_p = CACHE + ('smoke_' if SMOKE else '') + f'pob_add2_{D}.json'; OUTP = CACHE + ('smoke_' if SMOKE else '') + f'{D}_pob_add2.pkl.gz'
ADD2_SHA = open(AQ + 'ADDENDUM2_B_F5.sha256').read().split()[0]; assert hashlib.sha256(open(AQ + 'ADDENDUM2_B_F5.md', 'rb').read()).hexdigest() == ADD2_SHA, 'ADDENDUM2 modificado tras el sellado'
assert D in ('2026-10-16', '2026-10-24'), 'ADD2 solo se aplica a los dias FAILED-C3 (16-Oct y 24-Oct)'
CODE_SHA = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()[:16] + '+' + hashlib.sha256(open(EXP + 'lib1.py', 'rb').read()).hexdigest()[:16]
if os.path.exists(man_p) and not SMOKE:
    m0 = json.load(open(man_p))
    if m0.get('estado') == 'COMPLETE' and m0.get('code') == CODE_SHA and m0.get('addendum') == ADD2_SHA[:8] and os.path.exists(OUTP): print(D, 'ya COMPLETE (idempotente)'); sys.exit(0)
t0 = time.time(); man = dict(job='e2_dia_add2', dia=D, estado='RUNNING', code=CODE_SHA, addendum=ADD2_SHA[:8], addendum1=ADD_SHA[:8], regla_epoca='ADD2: suelo medido por ventana de 10 min', smoke=SMOKE, inicio=pd.Timestamp.utcnow().strftime('%FT%TZ'))
def guarda(): json.dump(man, open(man_p + '.tmp', 'w'), indent=1, default=str); os.replace(man_p + '.tmp', man_p)
def dia_ant(d): return (pd.Timestamp(d) - pd.Timedelta(days=1)).strftime('%Y-%m-%d')
def lee_k(p):
    K = {}
    if os.path.exists(p):
        for ln in open(p):
            c = ln.rstrip('\n').split(',')
            if len(c) > 7: K[c[2]] = (c[3], c[5], pd.Timestamp(c[6]).timestamp(), c[7])
    return K
def run(cmd, pf=True): r = subprocess.run(['bash'] + (['-o', 'pipefail'] if pf else []) + ['-c', cmd], capture_output=True, text=True); assert r.returncode == 0, 'subproceso: ' + r.stderr[-400:]
try:
    fich = REG + f'm5_registro_{D}.csv.gz'; assert os.path.exists(fich), 'falta ' + fich
    Dp = dia_ant(D); kp = CACHE + f'k_{Dp}.csv'
    if not os.path.exists(kp):        # tokens creados antes de medianoche: mapa k del dia anterior (una pasada ligera solo si falta; primer dia de la serie)
        fp = REG + f'm5_registro_{Dp}.csv.gz'
        if os.path.exists(fp): run(f"zcat {fp} | awk -F, '$1==\"k\" && $5==\"5min\"' > {kp}.tmp && mv {kp}.tmp {kp}")
    Kprev = lee_k(kp); ktok = pre + 'ktokprev.txt'; open(ktok, 'w').write('\n'.join(Kprev.keys()) + '\n')
    prog = r'''BEGIN{FS=","; split(COINS,cs,","); for(i in cs) C[cs[i]]=1}
FILENAME==KP{ if($1!="") K[$1]=1; next }
$1=="k" && $5=="5min" && ($4 in C) {K[$3]=1; print > KOUT; next}
$1=="t" && ($3 in K) {print $2","$3","$4","$5","$6","$7 > TOUT; next}
$1=="x" && ($3=="ETHUSDT"||$3=="SOLUSDT"||$3=="XRPUSDT") {m=int($2/60000); key=$3","m; if(!(key in O)){O[key]=$4;H[key]=$4;L[key]=$4}; if($4>H[key])H[key]=$4; if($4<L[key])L[key]=$4; Z[key]=$4; N[key]++; next}
$1=="q" && ($3 in K) && $4>=0.03 && $4<=0.45 {print $3","$8","$4","$5","$6","$7","($8-$2) | QCMD; next}
END{for(k in O) print k","O[k]","H[k]","L[k]","Z[k]","N[k] > XOUT}'''
    src = f"zcat {fich}" + (f" | head -n {SMOKE}" if SMOKE else '')
    cmd = (f"{src} | awk -v COINS={COINS} -v KP={ktok} -v KOUT={pre}k.csv -v TOUT={pre}t.csv -v XOUT={pre}bn.csv -v QCMD='gzip -c > {pre}q.tmp.gz' '{prog}' {ktok} -")
    run(cmd, pf=not SMOKE); os.replace(pre + 'q.tmp.gz', pre + 'q.gz') if os.path.exists(pre + 'q.tmp.gz') else open(pre + 'q.gz', 'wb').close()
    man['t_extraccion_s'] = round(time.time() - t0)
    K = dict(Kprev); K.update(lee_k(pre + 'k.csv')); K = {t: v for t, v in K.items() if v[0] in PRIM}
    if not SMOKE: os.replace(pre + 'k.csv', CACHE + f'add2_k_{D}.csv') if os.path.exists(pre + 'k.csv') else None
    T = pd.read_csv(pre + 't.csv', header=None, names=['r_ex', 'tok', 'p', 'side', 'acc', 'r_rx'], dtype={'tok': str, 'side': str}, na_values=['None'], on_bad_lines='skip')
    for c in ('r_ex', 'r_rx', 'p', 'acc'): T[c] = pd.to_numeric(T[c], errors='coerce')
    T = T.dropna(subset=['r_ex', 'r_rx', 'p', 'acc']); T['r_ex'] = T.r_ex.astype(np.int64); T['r_rx'] = T.r_rx.astype(np.int64); n_t0 = len(T); T = T.drop_duplicates(); n_dup = n_t0 - len(T)
    T = T[T.tok.isin(K)].copy(); T['coin'] = T.tok.map(lambda t: K[t][0]); T['mid'] = T.tok.map(lambda t: K[t][1]); T['fin'] = T.tok.map(lambda t: K[t][2]); T['lado'] = T.tok.map(lambda t: K[t][3])
    sell = T.side == 'SELL'; T['lado_m'] = np.where(sell, T.lado, np.where(T.lado == 'YES', 'NO', 'YES')); T['q'] = np.where(sell, T.p, 1 - T.p).round(3)
    F = T[(T.q > 0.10 + 1e-9) & (T.q <= 0.30 + 1e-9) & (T.r_ex / 1000 < T.fin) & (T.r_ex / 1000 >= T.fin - 300)].copy(); n_banda = len(F); del T; gc.collect()
    tokmap = {(v[1], v[3]): t for t, v in K.items()}; F['tokm'] = [tokmap.get((m, l)) for m, l in zip(F.mid, F.lado_m)]; F = F[F.tokm.notna()].copy()
    DES = {}
    for p in (DL + 'maker_ms_desenlaces_cache.json', DL + 'e1_cancelacion_ms/desenlaces_e1d.json', MIT + 'forward/desenlaces_fwd.json'):
        if os.path.exists(p): DES.update(json.load(open(p)))
    F['w'] = F.mid.map(DES); F['coste'] = F.q * F.acc; cob = 1 - F[F.w.isna()].coste.sum() / max(F.coste.sum(), 1e-9)
    man.update(prints_banda=int(n_banda), prints_con_token=int(len(F)), t_duplicados=int(n_dup), cobertura_desenlace_coste=round(float(cob), 5), mercados_sin_desenlace=int(F[F.w.isna()].mid.nunique()))
    if len(F) and cob < 0.995 and not SMOKE: man['estado'] = 'PENDING_DESENLACE'; guarda(); print(D, 'PENDING_DESENLACE', cob); sys.exit(3)
    F = F[F.w.notna()].copy(); assert F.w.isin(['YES', 'NO']).all(), 'C7: valores de desenlace'
    F['gana'] = (F.lado_m == F.w).astype(np.float32); F['pnl'] = ((F.gana - F.q) * F.acc).astype(np.float32); F['dia'] = D; F['hora'] = ((F.r_ex // 3600000) % 24).astype(np.int8); F['epoca'] = epoca(F.r_ex.values)
    # ---------------- filas q: histograma de rx-ex por ventana de 10 min (C3) + filas de los tokens con prints
    keep = set(F.tokm.unique().tolist()); codes = {t: i for i, t in enumerate(sorted(keep))}; day0 = ms(D + 'T00:00:00Z'); NB = 451; H = np.zeros((144, NB), np.int64); parts = []
    for ch in pd.read_csv(pre + 'q.gz', header=None, names=['tok', 'r', 'b', 'a', 'tb', 'ta', 'd'], chunksize=2_000_000, compression='gzip', na_values=['None'], on_bad_lines='skip',
                          dtype={'tok': str, 'r': np.int64, 'b': np.float32, 'a': np.float32, 'tb': np.float32, 'ta': np.float32, 'd': np.float32}):
        w = ((ch.r.values - day0) // 600000).astype(np.int64); dcl = (np.clip(ch.d.fillna(0).values, -50, 400) + 50).astype(np.int64); ok = (w >= 0) & (w < 144); H += np.bincount(w[ok] * NB + dcl[ok], minlength=144 * NB).reshape(144, NB)
        ch = ch[ch.tok.isin(keep)]; ch = ch.assign(id=ch.tok.map(codes).astype(np.int64)).drop(columns=['tok', 'd']); parts.append(ch)
    Qd = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame(columns=['id', 'r', 'b', 'a', 'tb', 'ta']); del parts; gc.collect()
    cum = np.cumsum(H, 1); tot = cum[:, -1]; p5 = np.where(tot >= 200, (cum >= np.maximum(1, (0.05 * tot)).astype(np.int64)[:, None]).argmax(1) - 50, np.nan)
    # ADD2 §2: epoca por SUELO MEDIDO por ventana de 10 min (sustituye al assert C3 con constantes por timestamp, que falla en este dia); indet se excluye y se cuenta
    cls = np.full(144, 'indet', dtype=object); fz = np.isfinite(p5); cls[fz & (np.abs(p5 - 19.25) <= 5)] = 'lo'; cls[fz & (np.abs(p5 - 39.5) <= 5)] = 'hi'
    w_pr = ((F.r_ex.values - day0) // 600000).astype(np.int64); dentro = (w_pr >= 0) & (w_pr < 144); wc = np.clip(w_pr, 0, 143); c_pr = np.where(dentro, cls[wc], 'indet').astype(object)
    ep_ts = epoca(F.r_ex.values).astype(object); cons = ((ep_ts == 'R0') & (c_pr == 'lo')) | ((ep_ts == 'R1') & (c_pr == 'hi')) | ((ep_ts == 'R2') & (c_pr == 'lo'))
    lab2 = np.where(c_pr == 'indet', 'indet', np.where(cons, ep_ts, ep_ts + c_pr)).astype(object)
    F['epoca_ts'] = ep_ts.astype(str); F['epoca'] = lab2.astype(str); F['p5w'] = np.where(dentro, p5[wc], np.nan).astype(np.float32); frac_indet = float(np.mean(lab2 == 'indet')) if len(lab2) else 1.0
    floor = dict(perfil_p5_10min=[None if not np.isfinite(x) else float(x) for x in p5], ventanas_por_clase={k: int((cls == k).sum()) for k in ('lo', 'hi', 'indet')}, prints_por_etiqueta={str(k): int(v) for k, v in zip(*np.unique(lab2.astype(str), return_counts=True))}, frac_indet=round(frac_indet, 5))
    assert frac_indet <= 0.20, f'ADD2-C3: {100 * frac_indet:.1f} % de prints sin clase de suelo (> 20 %)'
    man['C3_suelo_rx_menos_ex'] = floor; man['q_filas_tokens_con_prints'] = int(len(Qd)); man['q_filas_con_NaN_ask_o_tam'] = int(Qd[['a', 'tb', 'ta']].isna().any(axis=1).sum())
    QA = Q(Qd.id.values, Qd.r.values, Qd.b.values, Qd.a.values, Qd.tb.values, Qd.ta.values); fin_m = np.isfinite(QA.A) & np.isfinite(QA.TB) & np.isfinite(QA.TA)
    QO = Q.__new__(Q); QO.K, QO.R, QO.B, QO.A, QO.TB, QO.TA = (a[fin_m] for a in (QA.K, QA.R, QA.B, QA.A, QA.TB, QA.TA)); del Qd; gc.collect()
    ids = F.tokm.map(codes).astype(np.int64).values; out = {}; F = F.reset_index(drop=True)
    for (nm, c, l, dp, dm) in specs():
        tf = F.r_ex.values - c - 1; td = t_dec(tf, l, dp, dm); f5, bid, cat, _ = QA.feat(ids, td); out['F5_' + nm] = f5; out['bid_' + nm] = bid; out['cat_' + nm] = cat
    for nm, lag in (('o100', 100), ('o250', 250)):                       # definicion VIEJA (NO VALIDADA): tau = r_rx - lag con el estado sin filas de ask vacio (dropna), solo para reproducir +0,068/0/-0,145 y +0,132/+0,048/-0,033
        f5, bid, cat, _ = QO.feat(ids, F.r_rx.values - lag); out['F5_' + nm] = f5; out['bid_' + nm] = bid; out['cat_' + nm] = cat
    X = pd.DataFrame(out); P = pd.concat([F[['dia', 'coin', 'hora', 'fin', 'r_ex', 'r_rx', 'q', 'acc', 'gana', 'pnl', 'coste', 'epoca', 'mid', 'lado_m', 'epoca_ts', 'p5w']].assign(coste=lambda d: d.coste.astype(np.float32)), X], axis=1)
    assert not any(c in P.columns for c in ('t_fill', 'TOBp')), 'C2: columnas de sello viejo'
    P['fin'] = P.fin.astype(np.int64); P.to_pickle(OUTP, compression='gzip')
    man.update(estado='COMPLETE', fin=pd.Timestamp.utcnow().strftime('%FT%TZ'), duracion_s=round(time.time() - t0), prints=len(P), por_moneda=P.coin.value_counts().to_dict(), epoca=P.epoca.value_counts().to_dict(),
               cat_p60={CATN[k]: int((P['cat_p60'] == k).sum()) for k in range(4)}, cat_o100={CATN[k]: int((P['cat_o100'] == k).sum()) for k in range(4)}, valores_desenlace=sorted(set(DES.values()))[:5])
    guarda(); print(D, 'COMPLETE prints', len(P), 'cob', man['cobertura_desenlace_coste'], 'suelo', floor, 'cat_p60', man['cat_p60'], 's', man['duracion_s'])
    for s in ('t.csv', 'q.gz', 'ktokprev.txt'):
        if os.path.exists(pre + s): os.remove(pre + s)
    if os.path.exists(pre + 'bn.csv'): os.replace(pre + 'bn.csv', CACHE + ('smoke_' if SMOKE else '') + f'add2_bn_{D}.csv')
except AssertionError as e:
    man.update(estado='FAILED', error='ASSERT: ' + str(e)[:400]); guarda(); print(D, 'FAILED', man['error']); sys.exit(1)
except Exception as e:
    man.update(estado='FAILED', error=f'{type(e).__name__}: {str(e)[:400]}'); guarda(); print(D, 'FAILED', man['error']); raise
