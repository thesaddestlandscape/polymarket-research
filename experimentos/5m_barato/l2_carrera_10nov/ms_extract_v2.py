#!/usr/bin/env python3
"""ms_extract_v2.py DIA [DIA...] -- extractor del registro ms con AMBOS RELOJES (version nueva; NO pisa b_seleccion_adversa/scripts/ms_extract.py ni sa_ms/).
Salida: <DL>sa_ms2/ms2_DIA.npz + ms2_DIA.manifest.json (atomicos, tmp+replace). Mismo filtro, mismo orden (k, t_ex) y mismas columnas que la v1, mas:
    q_t_ex  = sello del EXCHANGE (columna 2 de la fila q)           [= q_t de la v1, identico]
    q_t_rx  = RECEPCION local (ultima columna de la fila q, col 8)  [-1 si falta]
    t_t_ex  / t_t_rx idem para las filas t (recepcion = columna 7)
Ambos relativos a t0 (= medianoche UTC del dia - 1 h, como la v1). Reloj local = UTC (chrony: 0,2 ms de offset medido 11-Nov), reloj exchange = sello del CLOB.
Contrato de relojes: CONTRATO_RELOJES.md. Lee con zcat|grep (tolera gzip truncado). Un fichero a la vez; lanzar con nice -n 19 ionice -c3, ulimit -v 3000000, nunca 06-09Z.
Variables: SA2_COINS (def. ETH,SOL,XRP), SA2_OUT (directorio de salida; tests)."""
import sys, os, glob, subprocess, json, time, hashlib
import numpy as np, pandas as pd

DL = os.environ.get('SA2_DL', '/root/polymarket-research-datalogs/')
OUT = os.environ.get('SA2_OUT', DL + 'sa_ms2/')
COINS = tuple(os.environ.get('SA2_COINS', 'ETH,SOL,XRP').upper().split(','))
FORMATO = 'ms2.1'


def lines(f, pat):
    return subprocess.Popen(f"zcat '{f}' 2>/dev/null | grep -E '{pat}'", shell=True, stdout=subprocess.PIPE)


def parse_qt(ch, kind):
    """Devuelve (V, rx) de un chunk ya filtrado. q: V=[bid,ask,szb,sza], rx=c5.  t: V=[price,is_buy,size], rx=c4. rx -1 si ausente/ilegible."""
    if kind == 'q':
        V = np.stack([pd.to_numeric(ch[c], errors='coerce').values.astype(np.float32) for c in ['c1', 'c2', 'c3', 'c4']], 1)
        rx = pd.to_numeric(ch.c5, errors='coerce')
    else:
        V = np.stack([pd.to_numeric(ch.c1, errors='coerce').values, (ch.c2 == 'BUY').astype(float).values, pd.to_numeric(ch.c3, errors='coerce').values], 1).astype(np.float32)
        rx = pd.to_numeric(ch.c4, errors='coerce')
    return V, rx.fillna(-1).astype('int64').values


def cat(L, nv):
    """Concatena y ordena por (k, t_ex) estable (= v1). Devuelve t_ex, t_rx (int32 relativos a t0), k, V (lista de columnas float32). Memoria: columna a columna y liberando los trozos."""
    if not L:
        return np.zeros(0, np.int32), np.zeros(0, np.int32), np.zeros(0, np.int16), [np.zeros(0, np.float32) for _ in range(nv)]
    def col(i, j=None):
        a_ = np.concatenate([(x[i] if j is None else x[i][:, j]) for x in L])
        return a_
    t = col(0); k = col(2); o = np.lexsort((t, k)).astype(np.int32); k = k[o]; t = t[o]      # lexsort estable: mismo orden que la clave k*1e10+t de la v1; indices int32 (memoria)
    r = col(1)[o]
    V = []
    for j in range(nv):
        V.append(col(3, j)[o])
    L.clear(); del o
    return t, r, k, V


def day(d):
    os.makedirs(OUT, exist_ok=True)
    of = OUT + f'ms2_{d}.npz'
    if os.path.exists(of):
        print(d, 'ya', flush=True); return of
    t_ini = time.time()
    fs = sorted(glob.glob(DL + f'maker_ms_{d}_*.csv.gz'))
    if not fs: raise SystemExit(f'{d}: sin ficheros maker_ms')
    from datetime import date, timedelta
    dprev = (date.fromisoformat(d) - timedelta(1)).isoformat()
    tm = {}
    for f in sorted(glob.glob(DL + f'maker_ms_{dprev}_*.csv.gz')) + fs:      # mapa de tokens (filas k), incluye el dia anterior
        p = lines(f, '^k,')
        for ch in pd.read_csv(p.stdout, header=None, names=['tipo', 't', 'tok', 'act', 'marco', 'mid', 'fin', 'lado'], dtype=str, on_bad_lines='skip', chunksize=100000):
            ch = ch[ch.act.isin(COINS) & ch.marco.isin(['5min', '15min'])]
            for r in ch.itertuples(): tm[r.tok] = (r.act, r.marco, r.mid, r.fin, r.lado)
        p.wait()
    toks = sorted(tm); ti = {t: i for i, t in enumerate(toks)}
    finE = np.array([int(pd.Timestamp(tm[t][3]).timestamp() * 1000) for t in toks]); vida = np.array([330000 if tm[t][1] == '5min' else 1000000 for t in toks])
    LO = finE - vida; HI = finE + 10000
    Q = []; T = []; t0 = int(pd.Timestamp(d).timestamp() * 1000) - 3600000
    cnt = dict(q_parsed=0, q_kept=0, q_rx_missing=0, q_rx_lt_ex=0, t_parsed=0, t_kept=0, t_rx_missing=0, t_rx_lt_ex=0)
    for f in fs:
        for kind, store in (('q', Q), ('t', T)):
            p = lines(f, f'^{kind},')
            names = ['tipo', 't', 'tok', 'c1', 'c2', 'c3', 'c4', 'c5']
            for ch in pd.read_csv(p.stdout, header=None, names=names, dtype={'tok': str, 'c1': str, 'c2': str, 'c3': str, 'c4': str, 'c5': str}, on_bad_lines='skip', chunksize=500000):
                cnt[kind + '_parsed'] += len(ch)
                ch = ch[ch.tok.isin(ti)]
                if not len(ch): continue
                kk = ch.tok.map(ti).values.astype(np.int64); tabs = ch.t.astype('int64').values; keep = (tabs >= LO[kk]) & (tabs <= HI[kk])   # filtro por sello EXCHANGE (= v1)
                if not keep.any(): continue
                ch = ch[keep]; k = kk[keep].astype(np.int16); tex = tabs[keep]
                V, rx = parse_qt(ch, kind)
                cnt[kind + '_kept'] += len(tex); cnt[kind + '_rx_missing'] += int((rx < 0).sum()); cnt[kind + '_rx_lt_ex'] += int(((rx >= 0) & (rx < tex)).sum())
                store.append(((tex - t0).astype(np.int32), np.where(rx >= 0, rx - t0, -1).astype(np.int32), k, V))
            p.wait()
        print(d, f.split('_')[-1], 'q', sum(len(x[0]) for x in Q), 't', sum(len(x[0]) for x in T), flush=True)
    qt, qr, qk, qV = cat(Q, 4); tt, tr_, tk_, tV = cat(T, 3)
    tmp = of[:-4] + '.tmp.npz'
    np.savez_compressed(tmp, tokens=np.array(toks), tmap=np.array([tm[t] for t in toks]), t0=t0, q_t_ex=qt, q_t_rx=qr, q_k=qk, **{'q_v%d' % j: qV[j] for j in range(4)},
                        t_t_ex=tt, t_t_rx=tr_, t_k=tk_, t_pr=tV[0], t_sd=tV[1], t_sz=tV[2])
    os.replace(tmp, of)
    man = dict(formato=FORMATO, dia=d, t0=t0, coins=list(COINS), tokens=len(toks), q=len(qt), t=len(tt), contadores=cnt, inicio_utc=time.strftime('%FT%TZ', time.gmtime(t_ini)), fin_utc=time.strftime('%FT%TZ', time.gmtime()),
               segundos=round(time.time() - t_ini, 1), codigo_sha256=hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
               entradas=[dict(f=os.path.basename(f), bytes=os.path.getsize(f), mtime=int(os.path.getmtime(f))) for f in fs], estado='COMPLETE' if cnt['q_kept'] == len(qt) and cnt['t_kept'] == len(tt) else 'FAILED')
    json.dump(man, open(of[:-4] + '.manifest.json.tmp', 'w'), indent=1); os.replace(of[:-4] + '.manifest.json.tmp', of[:-4] + '.manifest.json')
    print(d, 'tokens', len(toks), 'q', len(qt), 't', len(tt), cnt, 'guardado', of, flush=True)
    return of


if __name__ == '__main__':
    for d in sys.argv[1:]: day(d)
