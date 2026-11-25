#!/usr/bin/env python3
"""t2_dia_v4.py DIA [--smoke N] [--solo-hist] -- SPEC_F5_V4_17nov.md. UNA pasada (zcat | awk) de m5_registro_DIA (solo lectura) que produce:
 (1) cache/hist_D.npz  : histograma de d = rx-ex (recortado [-50,400] ms) por bin de 10 s de RX, de TODAS las filas q (tokens 5min de las 6 monedas, bid [0,03;0,45]) -> entrada de suelo_causal.tabla_clases;
 (2) cache/btc_pob_D.pkl.gz : poblacion de prints BTC (misma definicion que e2_dia_add3: banda q (0,10;0,30], ultimos 300 s, F5/bid/cat p35 y p60 con r_v3 = r_ex-19-1, t_dec = r_v3-l-3, estado q por RX<=t_dec), solo si D in los 35 dias decisivos y no --solo-hist.
 Idempotente: manifiesto cache/manifest_D.json (code sha + entrada size/mtime + conteos); COMPLETE valido (salidas existen y coinciden con el manifiesto) -> se salta. Escritura atomica (tmp + os.replace). Un assert fallido -> FAILED en el manifiesto (rc 1);
 desenlace < 0,995 del coste -> PENDING_DESENLACE (rc 3, la hist se conserva). Control: p5 de las ventanas alineadas de 10 min reproduce perfil_p5_10min de exp1/cache/pob_add3_D.json (paridad_p5). 0 ordenes, 0 EUR."""
import os, sys, gc, time, json, hashlib, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/exp1')
import numpy as np, pandas as pd
import suelo_causal as SC
from lib1 import *                                   # constantes congeladas, Q, t_dec, specs, epoca (lib1 asserta ADDENDUM1)
CACHE4 = HERE + '/cache/'; os.makedirs(CACHE4, exist_ok=True)
D = sys.argv[1]; SMOKE = int(sys.argv[sys.argv.index('--smoke') + 1]) if '--smoke' in sys.argv else 0; SOLO_HIST = '--solo-hist' in sys.argv
pre = CACHE4 + ('smoke_' if SMOKE else ''); MAN = pre + f'manifest_{D}.json'; HIST = pre + f'hist_{D}.npz'; POB = pre + f'btc_pob_{D}.pkl.gz'
DIAS_ADD3 = [x.strftime('%Y-%m-%d') for x in pd.date_range('2026-10-09', '2026-11-14') if x.strftime('%Y-%m-%d') not in ('2026-10-16', '2026-10-24')]; QUIERE_POB = (D in DIAS_ADD3) and not SOLO_HIST
CODE = '+'.join(hashlib.sha256(open(p, 'rb').read()).hexdigest()[:12] for p in (os.path.abspath(__file__), HERE + '/suelo_causal.py', EXP + 'lib1.py'))
fich = REG + f'm5_registro_{D}.csv.gz'; assert os.path.exists(fich), 'falta ' + fich
st = os.stat(fich); ENT = dict(fichero=fich, bytes=st.st_size, mtime=int(st.st_mtime))
def sha_arr(a): return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()[:16]
def valida(m):
    """COMPLETE valido: mismo codigo y entrada, salidas presentes y coherentes con el manifiesto."""
    if m.get('estado') != 'COMPLETE' or m.get('code') != CODE or m.get('entrada') != ENT or m.get('smoke') != SMOKE or m.get('quiere_pob') != QUIERE_POB: return False
    try:
        H = np.load(HIST)['H']; ok = H.shape == (SC.NBINS_DIA, SC.ND) and int(H.sum()) == m['hist_filas'] and sha_arr(H) == m['hist_sha']
        if QUIERE_POB: ok = ok and os.path.exists(POB) and len(pd.read_pickle(POB, compression='gzip')) == m['prints_btc']
        return bool(ok)
    except Exception: return False
if os.path.exists(MAN):
    m0 = json.load(open(MAN))
    if valida(m0): print(D, 'ya COMPLETE y valido (idempotente)'); sys.exit(0)
    print(D, 'manifiesto previo no valido/incompleto (estado', m0.get('estado'), '): se recalcula este dia')
t0 = time.time(); man = dict(job='t2_dia_v4', dia=D, estado='RUNNING', code=CODE, entrada=ENT, smoke=SMOKE, quiere_pob=QUIERE_POB, spec_sha=open(HERE + '/SPEC_F5_V4_17nov.sha256').read().split()[0][:12], inicio=pd.Timestamp.now('UTC').strftime('%FT%TZ'))
def guarda(): json.dump(man, open(MAN + '.tmp', 'w'), indent=1, default=str); os.replace(MAN + '.tmp', MAN)
def dia_ant(d): return (pd.Timestamp(d) - pd.Timedelta(days=1)).strftime('%Y-%m-%d')
def lee_k(p):
    K = {}
    if os.path.exists(p):
        for ln in open(p):
            c = ln.rstrip('\n').split(',')
            if len(c) > 7: K[c[2]] = (c[3], c[5], pd.Timestamp(c[6]).timestamp(), c[7])
    return K
def run(cmd, pf=True): r = subprocess.run(['bash'] + (['-o', 'pipefail'] if pf else []) + ['-c', cmd], capture_output=True, text=True); assert r.returncode == 0, 'subproceso: ' + r.stderr[-400:]
guarda()
try:
    Dp = dia_ant(D); kp = [p for p in (EXP + f'cache/add3_k_{Dp}.csv', EXP + f'cache/k_{Dp}.csv') if os.path.exists(p)]
    if not kp:                                        # mapa k del dia anterior (tokens creados antes de medianoche); una pasada ligera solo si falta
        fp = REG + f'm5_registro_{Dp}.csv.gz'; kq = CACHE4 + f'k_{Dp}.csv'
        if os.path.exists(fp): run(f"zcat {fp} | awk -F, '$1==\"k\" && $5==\"5min\"' > {kq}.tmp && mv {kq}.tmp {kq}"); kp = [kq]
    Kprev = lee_k(kp[0]) if kp else {}; man['k_prev'] = kp[0] if kp else None; man['k_prev_tokens'] = len(Kprev)
    tag = pre + f'_{D}_'; open(tag + 'kall.txt', 'w').write('\n'.join(Kprev.keys()) + '\n'); open(tag + 'kbtc.txt', 'w').write('\n'.join(t for t, v in Kprev.items() if v[0] == 'BTC') + '\n')
    day0 = ms(D + 'T00:00:00Z'); day1 = day0 + 86_400_000
    prog = r'''BEGIN{FS=","; split(COINS,cs,","); for(i in cs) C[cs[i]]=1}
FILENAME==KPF{ if($1!="") K[$1]=1; next }
FILENAME==KBF{ if($1!="") KB[$1]=1; next }
$1=="k" && $5=="5min" && ($4 in C) {K[$3]=1; if($4=="BTC") KB[$3]=1; print > KOUT; next}
$1=="t" && ($3 in KB) {print $2","$3","$4","$5","$6","$7 > TOUT; next}
$1=="q" && ($3 in K) && $4>=0.03 && $4<=0.45 { rx=$8; if(rx>=D0 && rx<D1){ d=rx-$2; if(d<-50)d=-50; else if(d>400)d=400; H[int((rx-D0)/10000)*1000+d+50]++ }
   if(($3 in KB) && !SOLOH) print $3","$8","$4","$5","$6","$7","($8-$2) | QCMD; next}
END{for(k in H) print k","H[k] > HOUT}'''
    src = f"zcat {fich}" + (f" | head -n {SMOKE}" if SMOKE else '')
    cmd = (f"{src} | awk -v COINS=ETH,SOL,XRP,BTC,DOGE,BNB -v KPF={tag}kall.txt -v KBF={tag}kbtc.txt -v D0={day0} -v D1={day1} -v SOLOH={1 if not QUIERE_POB else 0} "
           f"-v KOUT={tag}k.csv -v TOUT={tag}t.csv -v HOUT={tag}h.csv -v QCMD='gzip -c > {tag}q.tmp.gz' '{prog}' {tag}kall.txt {tag}kbtc.txt -")
    run(cmd, pf=not SMOKE)
    for f in ('k.csv', 't.csv', 'h.csv'): open(tag + f, 'a').close()
    man['t_extraccion_s'] = round(time.time() - t0)
    hh = pd.read_csv(tag + 'h.csv', header=None, names=['key', 'n'], dtype=np.int64) if os.path.getsize(tag + 'h.csv') else pd.DataFrame({'key': [], 'n': []}, dtype=np.int64)
    H = np.zeros((SC.NBINS_DIA, SC.ND), np.int32)
    if len(hh): b, dd = hh.key.values // 1000, hh.key.values % 1000; assert (dd >= 0).all() and (dd < SC.ND).all() and (b >= 0).all() and (b < SC.NBINS_DIA).all(), 'hist: indices fuera de rango'; H[b, dd] = hh.n.values
    man.update(hist_filas=int(H.sum()), hist_sha=sha_arr(H), hist_bins_con_datos=int((H.sum(1) > 0).sum()))
    # paridad con ADD3: p5 de ventanas ALINEADAS de 10 min (60 bins) vs perfil_p5_10min (solo ventanas con tot >= 200)
    pm = EXP + f'cache/pob_add3_{D}.json'
    if os.path.exists(pm) and not SMOKE:
        ref = json.load(open(pm))['C3_suelo_rx_menos_ex']['perfil_p5_10min']; mal = []
        for w in range(144):
            p, t = SC.p5_de(H[60 * w:60 * w + 60].sum(0)); p = p if t >= 200 else None; r = ref[w]
            if (p is None) != (r is None) or (p is not None and abs(p - r) > 1e-9): mal.append((w, p, r))
        man['paridad_p5'] = dict(ventanas=144, difieren=len(mal), ejemplos=mal[:5], ref=pm)
    else: man['paridad_p5'] = 'NA (sin manifiesto ADD3 de ese dia o smoke)'
    np.savez_compressed(HIST + '.tmp.npz', H=H); os.replace(HIST + '.tmp.npz', HIST)
    if QUIERE_POB:
        os.replace(tag + 'q.tmp.gz', tag + 'q.gz') if os.path.exists(tag + 'q.tmp.gz') else open(tag + 'q.gz', 'wb').close()
        K = dict(Kprev); K.update(lee_k(tag + 'k.csv')); K = {t: v for t, v in K.items() if v[0] == 'BTC'}
        T = pd.read_csv(tag + 't.csv', header=None, names=['r_ex', 'tok', 'p', 'side', 'acc', 'r_rx'], dtype={'tok': str, 'side': str}, na_values=['None'], on_bad_lines='skip')
        for c in ('r_ex', 'r_rx', 'p', 'acc'): T[c] = pd.to_numeric(T[c], errors='coerce')
        T = T.dropna(subset=['r_ex', 'r_rx', 'p', 'acc']); T['r_ex'] = T.r_ex.astype(np.int64); T['r_rx'] = T.r_rx.astype(np.int64); n_t0 = len(T); T = T.drop_duplicates(); n_dup = n_t0 - len(T)
        cod, uq = pd.factorize(T.tok); info = [K.get(u) for u in uq]; val = np.array([i is not None for i in info]); T = T[val[cod]].copy(); cod = cod[val[cod]]                       # mapa por token unico (no por fila): poca RAM
        T['coin'] = 'BTC'; T['mid'] = np.array([i[1] if i else '' for i in info], object)[cod]; T['fin'] = np.array([i[2] if i else np.nan for i in info], float)[cod]; T['lado'] = np.array([i[3] if i else '' for i in info], object)[cod]; del cod
        sell = T.side == 'SELL'; T['lado_m'] = np.where(sell, T.lado, np.where(T.lado == 'YES', 'NO', 'YES')); T['q'] = np.where(sell, T.p, 1 - T.p).round(3)
        F = T[(T.q > 0.10 + 1e-9) & (T.q <= 0.30 + 1e-9) & (T.r_ex / 1000 < T.fin) & (T.r_ex / 1000 >= T.fin - 300)].copy(); n_banda = len(F); del T; gc.collect()
        tokmap = {(v[1], v[3]): t for t, v in K.items()}; F['tokm'] = [tokmap.get((m, l)) for m, l in zip(F.mid, F.lado_m)]; n_sin_tok = int(F.tokm.isna().sum()); F = F[F.tokm.notna()].copy()
        DES = {}
        for p in (DL + 'maker_ms_desenlaces_cache.json', DL + 'e1_cancelacion_ms/desenlaces_e1d.json', MIT + 'forward/desenlaces_fwd.json'):
            if os.path.exists(p): DES.update(json.load(open(p)))
        F['w'] = F.mid.map(DES); F['coste'] = F.q * F.acc; cob = 1 - F[F.w.isna()].coste.sum() / max(F.coste.sum(), 1e-9)
        man.update(prints_banda=int(n_banda), prints_banda_sin_token_par=n_sin_tok, prints_con_token=int(len(F)), t_duplicados=int(n_dup), cobertura_desenlace_coste=round(float(cob), 5), mercados_sin_desenlace=int(F[F.w.isna()].mid.nunique()), mercados_total=int(F.mid.nunique()))
        if len(F) and cob < 0.995 and not SMOKE: man.update(estado='PENDING_DESENLACE', hist_ok=True, valores_desenlace_sin=sorted(F[F.w.isna()].mid.unique().tolist())[:20]); guarda(); print(D, 'PENDING_DESENLACE', cob); sys.exit(3)
        F = F[F.w.notna()].copy(); assert F.w.isin(['YES', 'NO']).all(), 'C7: valores de desenlace'
        F['gana'] = (F.lado_m == F.w).astype(np.float32); F['pnl'] = ((F.gana - F.q) * F.acc).astype(np.float32); F['dia'] = D; F['hora'] = ((F.r_ex // 3600000) % 24).astype(np.int8); F['epoca_ts'] = epoca(F.r_ex.values)
        keep = set(F.tokm.unique().tolist()); codes = {t: i for i, t in enumerate(sorted(keep))}; parts = []
        for ch in pd.read_csv(tag + 'q.gz', header=None, names=['tok', 'r', 'b', 'a', 'tb', 'ta', 'd'], chunksize=2_000_000, compression='gzip', na_values=['None'], on_bad_lines='skip',
                              dtype={'tok': str, 'r': np.int64, 'b': np.float32, 'a': np.float32, 'tb': np.float32, 'ta': np.float32, 'd': np.float32}):
            ch = ch[ch.tok.isin(keep)]; parts.append(ch.assign(id=ch.tok.map(codes).astype(np.int64)).drop(columns=['tok', 'd']))
        Qd = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame(columns=['id', 'r', 'b', 'a', 'tb', 'ta']); del parts; gc.collect()
        man['q_filas_tokens_con_prints'] = int(len(Qd)); QA = Q(Qd.id.values, Qd.r.values, Qd.b.values, Qd.a.values, Qd.tb.values, Qd.ta.values); del Qd; gc.collect()
        ids = F.tokm.map(codes).astype(np.int64).values; out = {}; F = F.reset_index(drop=True)
        for (nm, c, l, dp, dm) in specs():
            if nm not in ('p35', 'p60'): continue
            tf = F.r_ex.values - c - 1; td = t_dec(tf, l, dp, dm); f5, bid, cat, _ = QA.feat(ids, td); out['F5_' + nm] = f5; out['bid_' + nm] = bid; out['cat_' + nm] = cat
        P = pd.concat([F[['dia', 'coin', 'hora', 'fin', 'r_ex', 'r_rx', 'q', 'acc', 'gana', 'pnl', 'coste', 'epoca_ts', 'mid', 'lado_m']].assign(coste=lambda d: d.coste.astype(np.float32)), pd.DataFrame(out)], axis=1)
        P['fin'] = P.fin.astype(np.int64); P.to_pickle(POB + '.tmp', compression='gzip'); os.replace(POB + '.tmp', POB)
        man.update(prints_btc=int(len(P)), cat_p60={CATN[k]: int((P['cat_p60'] == k).sum()) for k in range(4)})
        for s in ('q.gz', 'q.tmp.gz'):
            if os.path.exists(tag + s): os.remove(tag + s)
    man.update(estado='COMPLETE', fin=pd.Timestamp.now('UTC').strftime('%FT%TZ'), duracion_s=round(time.time() - t0)); guarda()
    print(D, 'COMPLETE hist_filas', man['hist_filas'], 'paridad_p5', (man['paridad_p5'] if isinstance(man['paridad_p5'], str) else man['paridad_p5']['difieren']), 'prints_btc', man.get('prints_btc'), 'cob', man.get('cobertura_desenlace_coste'), 's', man['duracion_s'])
    for s in ('t.csv', 'k.csv', 'h.csv', 'kall.txt', 'kbtc.txt'):
        if os.path.exists(tag + s): os.remove(tag + s)
except AssertionError as e:
    man.update(estado='FAILED', error='ASSERT: ' + str(e)[:400]); guarda(); print(D, 'FAILED', man['error']); sys.exit(1)
except Exception as e:
    man.update(estado='FAILED', error=f'{type(e).__name__}: {str(e)[:400]}'); guarda(); print(D, 'FAILED', man['error']); raise
