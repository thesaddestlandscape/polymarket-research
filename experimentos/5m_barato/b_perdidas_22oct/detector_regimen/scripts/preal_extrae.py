#!/usr/bin/env python3
"""preal_extrae.py - P-REAL (PREREG_PREAL sha 5a263d50...). Estado REAL del libro (bid/ask) y primer print de TOMADOR en la decision de cada ventana 5m.
Uso: python3 -I preal_extrae.py DIA [--src FICHERO ...] [--max-lineas N] [--salida DIR]
  DIA = YYYY-MM-DD (UTC, por apertura de ventana). Fuente por defecto: /mnt/HC_Volume_106538179/m5_registro/m5_registro_DIA.csv.gz
  (--src acepta tambien maker_ms_* crudos: mismo formato de filas k/q/t; el gz truncado se tolera y se anota).
Salida: DIR/ask_t0_DIA.csv.gz (default /root/polymarket-research-datalogs/preal/), una fila por (moneda, cierre, token) de marco 5min con apertura en DIA,
  y para cada objetivo j en {T120 lag0, T120 lag250, T120 lag1000, T180 lag0, T180 lag250, T180 lag1000}: bid, ask, bsz, asz, edad_ms (decision+lag - recepcion del ultimo q),
  pp (precio del primer print BUY de tomador con recepcion en [objetivo, objetivo+30 s]), ps (size), pd (retraso ms). missing = vacio, NUNCA 0.
No look-ahead: solo q/t con RECEPCION <= objetivo para el libro. Orden del fichero NO cronologico: se toma el maximo de recepcion <= objetivo.
Solo lectura de la fuente; escritura atomica; idempotente; lock fcntl. Sin red, sin imports del repo."""
import sys, os, gzip, io, json, fcntl, hashlib, datetime as dt, subprocess, bisect, zlib
COINS = {'BTC', 'ETH', 'SOL', 'XRP', 'BNB', 'DOGE'}
TS = [(120, 0), (120, 250), (120, 1000), (180, 0), (180, 250), (180, 1000)]
OFF = [t * 1000 + l for t, l in TS]          # ms desde la apertura
PWIN = 30000
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:12]
def lee_k(src):
    """tokens 5min: token(bytes) -> (coin, mid, cierre_s, lado). Pasada barata con gzip -dc | grep."""
    tm = {}
    p = subprocess.Popen(f"gzip -dc '{src}' 2>/dev/null | grep -a '^k,'", shell=True, stdout=subprocess.PIPE)
    for ln in p.stdout:
        f = ln.decode().rstrip('\n').split(',')
        if len(f) < 8 or f[4] != '5min' or f[3] not in COINS: continue
        try: cierre = int(dt.datetime.fromisoformat(f[6]).timestamp())
        except Exception: continue
        tm[f[2].encode()] = (f[3], f[5], cierre, f[7])
    p.wait(); return tm
def procesa(srcs, dia, maxl=0):
    d0 = int(dt.datetime.fromisoformat(dia).replace(tzinfo=dt.timezone.utc).timestamp()); d1 = d0 + 86400
    tmap = {}; trunc = []
    for s in srcs: tmap.update(lee_k(s))
    # solo tokens con apertura en el dia
    tmap = {k: v for k, v in tmap.items() if d0 <= v[2] - 300 < d1}
    ABS = {}                                   # token -> lista de objetivos absolutos (ms)
    ST = {}                                    # token -> [best_recv[j], bid, ask, bsz, asz] por objetivo ; print: [pbest_recv, price, size]
    for k, v in tmap.items():
        to = (v[2] - 300) * 1000; ABS[k] = [to + o for o in OFF]
        ST[k] = ([0] * 6, [None] * 6, [None] * 6, [None] * 6, [None] * 6, [0] * 6, [None] * 6, [None] * 6)
    nq = nt = nrows = 0; lo_rel = -600000; hi_rel = 181000
    for s in srcs:
        try:
            with gzip.open(s, 'rb') as f:
                for ln in io.BufferedReader(f, 1 << 22):
                    nrows += 1
                    if maxl and nrows > maxl: break
                    c = ln[0]
                    if c == 113:               # q: q,t_ms,token,bid,ask,bsz,asz,recv
                        j = ln.find(b',', 16)
                        tk = ln[16:j]; ab = ABS.get(tk)
                        if ab is None: continue
                        p = ln[j + 1:].rstrip(b'\n').split(b',')
                        try: rv = int(p[4])
                        except Exception: continue
                        if rv < ab[0] - 700000 or rv > ab[5]: continue
                        nq += 1; st = ST[tk]
                        try: b = float(p[0]) if p[0] else None; a = float(p[1]) if p[1] else None; bs = float(p[2]) if p[2] else None; as_ = float(p[3]) if p[3] else None
                        except Exception: continue
                        for jj in range(bisect.bisect_left(ab, rv), 6):
                            if rv > st[0][jj]: st[0][jj] = rv; st[1][jj] = b; st[2][jj] = a; st[3][jj] = bs; st[4][jj] = as_
                    elif c == 116:             # t: t,t_ms,token,price,side,size,recv
                        j = ln.find(b',', 16)
                        tk = ln[16:j]; ab = ABS.get(tk)
                        if ab is None: continue
                        p = ln[j + 1:].rstrip(b'\n').split(b',')
                        if len(p) < 4 or p[1] != b'BUY': continue
                        try: rv = int(p[3]); pr = float(p[0]); sz = float(p[2])
                        except Exception: continue
                        if rv < ab[0] or rv > ab[5] + PWIN: continue
                        nt += 1; st = ST[tk]
                        for jj in range(6):
                            if ab[jj] <= rv <= ab[jj] + PWIN and (st[5][jj] == 0 or rv < st[5][jj]): st[5][jj] = rv; st[6][jj] = pr; st[7][jj] = sz
        except (EOFError, zlib.error, OSError) as e:
            trunc.append((os.path.basename(s), type(e).__name__))
    return tmap, ABS, ST, dict(nrows=nrows, nq_usadas=nq, nt_usados=nt, truncados=trunc)
def fmt(x): return '' if x is None else repr(x)
def escribe(dia, tmap, ABS, ST, meta, srcs, salida):
    os.makedirs(salida, exist_ok=True); out = f'{salida}/ask_t0_{dia}.csv.gz'; tmp = out + '.tmp'
    cols = ['dia', 'coin', 'mid', 'cierre', 'lado']
    for t, l in TS: cols += [f'{x}_{t}_{l}' for x in ('bid', 'ask', 'bsz', 'asz', 'edad', 'pp', 'ps', 'pd')]
    with gzip.open(tmp, 'wt') as w:
        w.write(','.join(cols) + '\n')
        for k, v in sorted(tmap.items(), key=lambda kv: (kv[1][2], kv[1][0], kv[1][3])):
            st = ST[k]; ab = ABS[k]; r = [dia, v[0], v[1], str(v[2]), v[3]]
            for j in range(6):
                edad = (ab[j] - st[0][j]) if st[0][j] else None
                pd_ = (st[5][j] - ab[j]) if st[5][j] else None
                r += [fmt(st[1][j]), fmt(st[2][j]), fmt(st[3][j]), fmt(st[4][j]), fmt(edad), fmt(st[6][j]), fmt(st[7][j]), fmt(pd_)]
            w.write(','.join(r) + '\n')
    os.replace(tmp, out)
    man = dict(dia=dia, fuentes=[os.path.basename(s) for s in srcs], tokens_5min=len(tmap), codigo_sha12=sha(__file__), prereg='5a263d50', **meta,
               generado=dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'))
    json.dump(man, open(f'{salida}/ask_t0_{dia}.manifest.json', 'w'), indent=1); return out, man
def main():
    a = sys.argv[1:]; 
    if not a: print(__doc__); sys.exit(1)
    dia = a[0]; srcs = []; maxl = 0; salida = '/root/polymarket-research-datalogs/preal'; i = 1
    while i < len(a):
        if a[i] == '--src': i += 1; srcs.append(a[i])
        elif a[i] == '--max-lineas': i += 1; maxl = int(a[i])
        elif a[i] == '--salida': i += 1; salida = a[i]
        i += 1
    if not srcs: srcs = [f'/mnt/HC_Volume_106538179/m5_registro/m5_registro_{dia}.csv.gz']
    for s in srcs:
        if not os.path.exists(s): print('NO existe', s); sys.exit(2)
    os.makedirs(salida, exist_ok=True); lk = open(f'{salida}/.lock', 'w'); fcntl.flock(lk, fcntl.LOCK_EX | fcntl.LOCK_NB)
    out0 = f'{salida}/ask_t0_{dia}.csv.gz'
    if os.path.exists(out0) and not maxl and '--forzar' not in a: print('ya existe (idempotente)', out0); return
    tmap, ABS, ST, meta = procesa(srcs, dia, maxl); out, man = escribe(dia, tmap, ABS, ST, meta, srcs, salida); print(json.dumps(man))
if __name__ == '__main__': main()
