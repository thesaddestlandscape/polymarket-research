#!/usr/bin/env python3
"""l2_triggers_v2.py MODO DIA -- COPIA de l2_triggers.py (no se edita el original) sobre out_v2/g0_fills_<modo>_<D>.pkl -> out_v2/trg_<modo>_<D>.pkl.
RELOJ: el libro L2 (libro5_b40) se ordena y compara en RECEPCION (rx, seq). tf: legacy/rx = tf tal cual (como el original); causal = tf es EXCHANGE -> para comparar con eventos rx se usa tf_rx = tf_rxb (recepcion de la caida L1, si existe) o tf + DELTA_RX_EX (p50 calibrado, ETIQUETADO) -- solo afecta a la ventana [t_dec-3000, tf+1000] y a tl2.
Paso 2 (solo lectura de datos; sin PnL de politicas): por relleno G0 y por config del DISENO.md, hora de RECEPCION del primer disparo del libro L2 (libro5_b40)
entre t_dec y tf, mas validez y diagnosticos de reloj. Uso: nice -n 19 ionice -c3 python3 -I l2_triggers.py DIA  -> out/trg_<DIA>.pkl (idempotente).
Libro: se reconstruye por token (B reemplaza, d fija el tamano del nivel; 0 borra), orden de llegada (rx, seq). 'Mejor bid visible' = max nivel <= 0,40 (bids >0,40 no visibles)."""
import sys, os, subprocess, tempfile, collections, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'
modo, d = sys.argv[1], sys.argv[2]; OUT = H + f'out_v2/trg_{modo}_{d}.pkl'; DELTA_RX_EX = int(os.environ.get('DELTA_RX_EX', '19'))
if os.path.exists(OUT): print('ya', d); sys.exit(0)
F = pd.read_pickle(H + f'out_v2/g0_fills_{modo}_{d}.pkl'); F = F[F.dia == d].reset_index(drop=True)
F['tf_orig'] = F.tf
if modo == 'causal': F['tf'] = np.where(F.tf_rxb > 0, F.tf_rxb, F.tf + DELTA_RX_EX)   # tf EXCHANGE -> RECEPCION (explicito)
CFG = [('D', x) for x in (-1, 0, 1, 2, 3, 5)] + [('V', x) for x in (2, 3, 5)] + [('S', x) for x in (0, 50, 200)]   # delta/d en centimos, theta en acciones
NC = len(CFG); LAM_PLACE = 68
SRC = f'/mnt/HC_Volume_106538179/libro5_b40/libro5_b40_{d}.csv.gz'
toks = set(F.token.unique())
tf_ = tempfile.NamedTemporaryFile('w', suffix='.tok', delete=False, dir=H + 'out'); tf_.write('\n'.join(toks) + '\n'); tf_.close()
by = collections.defaultdict(list)
for i, r in F.iterrows(): by[r.token].append(i)
st = {i: dict(init=False, bad=None, trig=np.full(NC, -1, np.int64), static=np.zeros(NC, bool), bbdec=np.nan, nev=0, tl2=-1) for i in range(len(F))}
tdec = F.t_dec.values.astype(np.int64); tfl = F.tf.values.astype(np.int64); Lc = np.rint(F.L.values * 100).astype(int)
BK = {}; DIRTY = {}; HIST = {}
def best(bk): return max(bk) if bk else -1
for tk in toks: BK[tk] = {}; DIRTY[tk] = True; HIST[tk] = collections.deque()    # dirty hasta el primer B
def depth(bk, L, hi): return sum(s for p, s in bk.items() if L < p <= hi)
def evalD(bk, i, ev_rx, dyn):
    """evalua D y S (estado actual) -> actualiza trig; static si no dyn."""
    L = Lc[i]; bb = best(bk); s = st[i]
    if bb < 0: return
    for c, (fam, x) in enumerate(CFG):
        if s['trig'][c] >= 0: continue
        if fam == 'D': ok = bb <= L + x
        elif fam == 'S': ok = depth(bk, L, L + 5) <= x + 1e-9
        else: continue
        if ok: s['trig'][c] = ev_rx if dyn else tdec[i]; s['static'][c] = not dyn
cmd = f"zcat {SRC} | awk -F, -v tf={tf_.name} 'BEGIN{{while((getline l<tf)>0)t[l]}} ($1==\"d\"||$1==\"B\"||$1==\"G\")&&($3 in t)'"
p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, text=True, bufsize=1 << 20)
nrows = 0
for line in p.stdout:
    q = line.rstrip('\n').split(','); nrows += 1
    tk = q[2]; rx = int(q[6]); fl = by[tk]; typ = q[0]; bk = BK[tk]
    if typ == 'G':
        if q[3] in ('caida', 'traspaso', 'arranque'):
            bk.clear(); DIRTY[tk] = True
            for i in fl:
                if tdec[i] - 3000 <= rx <= tfl[i] + 1000 and st[i]['bad'] is None: st[i]['bad'] = 'hueco_G'
        continue
    # activar rellenos: antes de aplicar el evento, estado estatico en el primer evento con rx > t_dec
    for i in fl:
        s = st[i]
        if not s['init'] and rx > tdec[i] and rx <= tfl[i] + 1000:
            s['init'] = True
            if DIRTY[tk] or not bk: s['bad'] = s['bad'] or ('sin_libro' if not bk else 'sucio')
            else: s['bbdec'] = best(bk) / 100.0; evalD(bk, i, rx, False)
    if typ == 'B':
        bk.clear()
        if q[3]:
            for kv in q[3].split(';'):
                a, b = kv.split(':'); bk[int(round(float(a) * 100))] = float(b)
        DIRTY[tk] = False; old = None
    else:
        pr = int(round(float(q[4]) * 100)); sz = float(q[5]); old = bk.get(pr, 0.0)
        if sz > 0: bk[pr] = sz
        else: bk.pop(pr, None)
    bb = best(bk); h = HIST[tk]; h.append((rx, bb))
    while h and h[0][0] < rx - 500: h.popleft()
    if DIRTY[tk]: continue
    mx = max((b for _, b in h), default=-1)
    for i in fl:
        s = st[i]
        if not s['init'] or rx <= tdec[i] or rx > tfl[i]:
            if s['init'] and old is not None and abs(rx - tfl[i]) <= 1500 and pr == Lc[i] and sz < old and (s['tl2'] < 0 or abs(rx - tfl[i]) < abs(s['tl2'] - tfl[i])): s['tl2'] = rx
            continue
        s['nev'] += 1; L = Lc[i]
        evalD(bk, i, rx, True)
        if bb >= 0:
            for c, (fam, x) in enumerate(CFG):
                if fam == 'V' and s['trig'][c] < 0 and mx - bb >= x and bb <= L + 10: s['trig'][c] = rx
        if old is not None and abs(rx - tfl[i]) <= 1500 and pr == Lc[i] and sz < old and (s['tl2'] < 0 or abs(rx - tfl[i]) < abs(s['tl2'] - tfl[i])): s['tl2'] = rx
p.wait(); os.unlink(tf_.name)
rows = []
for i, r in F.iterrows():
    s = st[i]; bad = s['bad'] or (None if s['init'] else 'sin_eventos')
    rows.append(dict(dia=d, k=r.k, L=r.L, tf=r.tf_orig, tf_cmp=r.tf, token=r.token, bad=bad, bbdec=s['bbdec'], nev=s['nev'], tl2=s['tl2'], **{f'tr_{fam}{x}': int(s['trig'][c]) for c, (fam, x) in enumerate(CFG)},
                     **{f'st_{fam}{x}': bool(s['static'][c]) for c, (fam, x) in enumerate(CFG) if fam != 'V'}))
R = pd.DataFrame(rows); R.to_pickle(OUT + '.tmp'); os.replace(OUT + '.tmp', OUT)
print(modo, d, 'filas L2', nrows, 'fills', len(R), 'bad', R.bad.value_counts(dropna=False).to_dict())
