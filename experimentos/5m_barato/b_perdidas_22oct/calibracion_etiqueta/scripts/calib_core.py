#!/usr/bin/env python3
"""calib_core.py --dia D --modo B|P [--max-lineas N] : motor de relleno virtual (PREREG_CALIB). Pasivo, solo lectura del registro ms.
Modo B: repite las ordenes REALES de B del dia (5 etiquetas: R, L60, BB60, PE, P60) con 8 variantes (f in 0,.25,.5,1) x (barrido 0/1).
Modo P: vidas estaticas de poblacion (mismas claves/condiciones que f8_estructura/scripts/vpv_f8.py) con niveles off 0,1,2 y las 8 variantes; registra instante de relleno y F5 (log tamano ask propio a r-100 ms).
Reglas: print SELL del token a precio<=p o BUY del complementario a >=1-p (no dup) con recepcion en [ti,tf]; rellena cuando consumo>=f*Q+s (o 1er print que atraviesa el nivel si barrido=1)."""
import sys, gzip, json, os, argparse, collections, time, csv, math
ap = argparse.ArgumentParser(); ap.add_argument('--dia', required=True); ap.add_argument('--modo', required=True, choices=['B', 'P'])
ap.add_argument('--max-lineas', type=int, default=0); ap.add_argument('--out', default=None); ap.add_argument('--force', action='store_true'); a = ap.parse_args()
SRC = '/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz' % a.dia
OUTD = '/root/polymarket-research-datalogs/calibracion_etiqueta/'; os.makedirs(OUTD, exist_ok=True)
OUT = a.out or OUTD + ('cal_%s_%s.csv.gz' % (a.modo, a.dia))
if os.path.exists(OUT) and not a.force and not a.max_lineas: print('ya existe', OUT); sys.exit(0)
VARS = [(f, sw) for f in (0.0, 0.25, 0.5, 1.0) for sw in (0, 1)]; NV = len(VARS)
RHO = json.load(open(OUTD + 'rho.json')); RHOV = {0: 1.0, 1: RHO['1']['mediana'], 2: RHO['2']['mediana']}
ARR_MS, VIDA_MS, ACC = 150, 60_000, 5.0; PASO, LO, HI = 10_000, 0.10 - 1e-9, 0.30 + 1e-9
class O:
    __slots__ = ('tk', 'p', 's', 'Q', 'ti', 'tf', 'cons', 'fill', 'f5', 'f5b', 'meta')
    def __init__(s, tk, p, sz, Q, ti, tf, meta): s.tk, s.p, s.s, s.Q, s.ti, s.tf, s.cons, s.meta = tk, p, sz, Q, ti, tf, 0.0, meta; s.fill = [None] * NV; s.f5 = [float('nan')] * NV; s.f5b = [float('nan')] * NV
K = {}; COMP = {}; ords = collections.defaultdict(list); qh = {}; mdq = {}; mlast = {}; ultimo_t = {}; ult_col = {}; vidas = collections.defaultdict(list); cnt = collections.Counter()
def f5_at(tk, tau):
    d = qh.get(tk)
    if not d: return float('nan')
    for (t, bb, ba, bs, as_) in reversed(d):
        if t <= tau:
            if tau - t > 30_000 or bb >= ba: return float('nan')
            return math.log1p(as_)
    return float('nan')
def consume(o, now, sz, sweep):
    if now < o.ti or now > o.tf: return
    o.cons += sz
    for i, (f, sw) in enumerate(VARS):
        if o.fill[i] is None and ((sw and sweep) or o.cons >= f * o.Q + o.s - 1e-9):
            o.fill[i] = now; o.f5[i] = f5_at(o.tk, now - 100); o.f5b[i] = f5_at(o.tk, now - 250)
rows = []
if a.modo == 'B':
    B = [r for r in csv.DictReader(open(OUTD + 'ordenes_b.csv')) if r['dia'] == a.dia]
    for r in B:
        for k in ('precio', 'size', 't_ini', 't_fin', 'cie'): r[k] = float(r[k])
        for k in ('cola', 'bb', 'bs'): r[k] = float(r[k]) if r[k] not in ('', 'nan') else float('nan')
    B.sort(key=lambda r: r['t_ini'])
    pj = {}
    for r in B:
        ti, tf = int(r['t_ini'] * 1000), int(r['t_fin'] * 1000); cie = int(r['cie'] * 1000); cola = r['cola'] if r['cola'] == r['cola'] else 0.0
        m = dict(oid=r['oid'], puja=r['puja']); tok = r['tok']; p = r['precio']; sz = r['size']
        ords[tok].append(O(tok, p, sz, cola, ti, tf, dict(m, tag='R')))
        ords[tok].append(O(tok, p, sz, cola, ti, min(ti + VIDA_MS, cie - 2000), dict(m, tag='L60')))
        if r['bb'] == r['bb'] and r['bs'] == r['bs']: ords[tok].append(O(tok, round(r['bb'], 2), ACC, r['bs'], ti, min(ti + VIDA_MS, cie - 2000), dict(m, tag='BB60')))
        e = pj.setdefault(r['puja'], dict(tok=tok, p=p, s=sz, Q=cola, ti=ti, tf=tf, cie=cie))
        e['tf'] = max(e['tf'], tf)
    for k, e in pj.items():
        ords[e['tok']].append(O(e['tok'], e['p'], e['s'], e['Q'], e['ti'], e['tf'], dict(oid='', puja=k, tag='PE')))
        ords[e['tok']].append(O(e['tok'], e['p'], e['s'], e['Q'], e['ti'], min(e['ti'] + VIDA_MS, e['cie'] - 2000), dict(oid='', puja=k, tag='P60')))
    print('modo B: %d ordenes B, %d pujas, %d objetos' % (len(B), len(pj), sum(len(v) for v in ords.values())), flush=True)
def cerrar_vida(v, cens):
    coin, mk, cie, lado = K[v['tk']]
    r = [a.dia, mk, coin, lado, v['t0'], v['b'], v['Q0'], int(cens)]
    for oo in v['o']:
        for i in range(NV): r += ['' if oo.fill[i] is None else oo.fill[i] - v['t0'], '' if oo.fill[i] is None or oo.f5[i] != oo.f5[i] else round(oo.f5[i], 4), '' if oo.fill[i] is None or oo.f5b[i] != oo.f5b[i] else round(oo.f5b[i], 4)]
    rows.append(r)
def avanzar(tk, now):
    keep = []
    for v in vidas[tk]:
        if now > v['end'] + 1000:
            cerrar_vida(v, 0)
            for oo in v['o']:
                try: ords[tk].remove(oo)
                except ValueError: pass
                oc = COMP.get((K[tk][1], 'NO' if K[tk][3] == 'YES' else 'YES'))
        else: keep.append(v)
    vidas[tk] = keep
t_ini = time.time(); n = 0
with gzip.open(SRC, 'rt', errors='replace') as f:
    try:
        for line in f:
            n += 1
            if a.max_lineas and n > a.max_lineas: break
            ty = line[0]
            if ty == 'x': continue
            c = line.rstrip('\n').split(',')
            if ty == 'k':
                if len(c) >= 8 and c[4] == '5min':
                    try: cie = int(time.mktime(time.strptime(c[6][:19], '%Y-%m-%d %H:%M:%S')) - time.timezone) * 1000
                    except Exception: continue
                    K[c[2]] = (c[3], c[5], cie, c[7]); COMP[(c[5], c[7])] = c[2]
                continue
            if ty not in ('q', 't') or len(c) < 7 or c[2] not in K: continue
            tk = c[2]
            try: now = int(c[7]) if ty == 'q' else int(c[6])
            except (ValueError, IndexError): continue
            coin, mk, cie, lado = K[tk]
            if a.modo == 'P' and tk in ultimo_t and now < ultimo_t[tk] - 60_000:
                for v in vidas[tk]:
                    cerrar_vida(v, 1)
                    for oo in v['o']: ords[tk].remove(oo) if oo in ords[tk] else None
                vidas[tk] = []; ult_col.pop(tk, None)
            ultimo_t[tk] = now
            if mk in mlast and now < mlast[mk] - 60_000: mdq[mk] = collections.deque(); mlast[mk] = now
            else: mlast[mk] = max(mlast.get(mk, 0), now)
            if ty == 't':
                try: p = float(c[3]); sz = float(c[5])
                except ValueError: continue
                sd = c[4]; d = mdq.get(mk)
                if d is None: d = mdq[mk] = collections.deque()
                while d and d[0][0] < now - 150_000: d.popleft()
                dup = False; sz4 = round(sz, 4)
                for (t2, tok2, p2, sz2) in d:
                    if now - t2 <= 300 and tok2 != tk and round(sz2, 4) == sz4 and abs(p2 + p - 1) < 1e-9: dup = True; break
                d.append((now, tk, p, sz)); cnt['prints'] += 1; cnt['dup'] += dup
                if dup: continue
                if sd == 'SELL':
                    for o in ords.get(tk, ()):
                        if p <= o.p + 1e-9: consume(o, now, sz, p < o.p - 1e-9)
                else:
                    otro = COMP.get((mk, 'NO' if lado == 'YES' else 'YES'))
                    if otro:
                        for o in ords.get(otro, ()):
                            if p >= 1 - o.p - 1e-9: consume(o, now, sz, p > 1 - o.p + 1e-9)
                continue
            try: bb, ba, bs, as_ = float(c[3]), float(c[4]), float(c[5]), float(c[6])
            except ValueError: continue
            d = qh.get(tk)
            if d is None: d = qh[tk] = collections.deque()
            d.append((now, bb, ba, bs, as_))
            while d and d[0][0] < now - 31_000: d.popleft()
            if a.modo != 'P': continue
            if bb >= ba: continue
            avanzar(tk, now)
            T = (cie - now) / 1000.0
            if coin in ('ETH', 'SOL', 'XRP', 'BTC', 'DOGE', 'BNB') and LO <= bb <= HI and 60 <= T <= 300 and now - ult_col.get(tk, -10**15) >= PASO:
                b = round(bb, 2); end = min(now + VIDA_MS, cie - 2000); lst = []
                for off in (0, 1, 2):
                    oo = O(tk, round(b - off / 100.0, 2), ACC, RHOV[off] * bs, now + ARR_MS, end, dict(off=off)); ords[tk].append(oo); lst.append(oo)
                vidas[tk].append(dict(tk=tk, t0=now, b=b, Q0=bs, end=end, o=lst)); ult_col[tk] = now
    except EOFError: print('AVISO: gz truncado tras %d lineas' % n)
if a.modo == 'P':
    for tk in list(vidas):
        for v in vidas[tk]: cerrar_vida(v, 1)
    hdr = ['dia', 'mercado', 'coin', 'lado', 't0_recv_ms', 'b', 'Q0', 'censurada'] + ['o%d_v%d_%s' % (off, i, k) for off in (0, 1, 2) for i in range(NV) for k in ('ft', 'f5', 'f5b')]
else:
    for lst in ords.values():
        for o in lst:
            m = o.meta; rows.append([a.dia, m['tag'], m['oid'], m['puja'], o.p, o.s, o.Q, o.ti, o.tf, round(o.cons, 3)] + [x for i in range(NV) for x in ('' if o.fill[i] is None else o.fill[i], '' if o.fill[i] is None or o.f5[i] != o.f5[i] else round(o.f5[i], 4))])
    hdr = ['dia', 'tag', 'oid', 'puja', 'p', 's', 'Q', 'ti', 'tf', 'cons'] + ['v%d_%s' % (i, k) for i in range(NV) for k in ('ft', 'f5')]
with gzip.open(OUT + '.tmp', 'wt', newline='') as fo:
    w = csv.writer(fo); w.writerow(hdr); w.writerows(rows)
os.replace(OUT + '.tmp', OUT)
print('dia %s modo %s lineas %d filas %d prints %d dup %d seg %.0f -> %s' % (a.dia, a.modo, n, len(rows), cnt['prints'], cnt['dup'], time.time() - t_ini, OUT))
