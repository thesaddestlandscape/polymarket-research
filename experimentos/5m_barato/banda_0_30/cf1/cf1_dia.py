#!/usr/bin/env python3
"""cf1_dia.py - CF1 tal cual PREREG_CF1_CARRY_FAV_5M.md (sha256 d74fae893bf2630c...) + rejilla franja x bucket 0,05 (H3 enjambre 05-Nov).
Uso:  cf1_dia.py MAPA OUT KDIR      -> OUT/tokmap_union.json  (tokmap/*.k.json  U  filas k de m5_registro; nunca mapa_escala/tokens.json)
      cf1_dia.py D OUT [maxfilas]   -> OUT/dia_D.json (agregados con desenlace oficial aplicado + cobertura)
Relojes: solo on-chain (ts_est = bloque interpolado, error <1,5 s); ningun reloj WS. Desenlace oficial maker_ms_desenlaces_cache.json.
CF1: relleno maker = fila F con taker != exchange; dedup tx+log_index; compra equivalente (venta a q = compra del contrario a 1-q);
     grupo de casacion = filas entre filas M consecutivas por log_index; L = n de niveles (round(pc,3)) de rellenos maker del mismo
     lado economico estrictamente mas caros; TOP L=0, MID L=1, DEEP L>=2; contra MINT (tomador compra el complementario) / CRUCE
     (tomador vende el mismo token) / NA. Banda FAV pc en [0,70;0,99), CTRL [0,05;0,30); T=cierre-ts en (5;300]; fuera wallet dedicada.
Rejilla: rol T = fila M (orden tomadora entera, como tb.py), rol K = rellenos maker; modo lit = solo compras literales (como tb.py),
     modo eq = compras U ventas como compra del contrario; unidad mercado-lado por celda; tomador paga 0,07 p(1-p)/acc, maker rebate 20 %.
Desviaciones declaradas: niveles a 0,001; tx no contiguas se descartan y se cuentan; grupos sin fila M -> contra NA."""
import sys, os, gzip, csv, json, glob, collections, datetime as dt
V = '/mnt/HC_Volume_106538179'
if sys.argv[1] == 'MAPA':
    OUT, KD = sys.argv[2], sys.argv[3]; TK = {}; conf = 0; nk = 0
    for f in sorted(glob.glob(V + '/agentes_datos/mapa_infra/tokmap/*.k.json')):
        for t, v in json.load(open(f)).items():
            TK[t] = [v[0], v[1], str(v[2]), int(v[3]), v[4]]
    for f in sorted(glob.glob(KD + '/k*.csv')):
        for l in open(f):
            c = l.rstrip('\n').split(',')
            if len(c) < 8 or c[0] != 'k': continue
            v = [c[3], c[4], c[5], int(dt.datetime.fromisoformat(c[6]).timestamp()), c[7]]
            if c[2] in TK and TK[c[2]] != v: conf += 1
            TK[c[2]] = v; nk += 1
    json.dump(TK, open(OUT + '/tokmap_union.json.tmp', 'w')); os.replace(OUT + '/tokmap_union.json.tmp', OUT + '/tokmap_union.json')
    print('tokens', len(TK), 'filas_k', nk, 'conflictos_tokmap_vs_k', conf); sys.exit(0)

D, OUT = sys.argv[1], sys.argv[2]; MAXF = int(sys.argv[3]) if len(sys.argv) > 3 else 0
EX = '0xe111180000d2663c0091e4f400237545b87b996b'; DED = '0x659a40ff9920febc5a66836213040924343d297f'
WP, MP = '0xb0f85baa', '0x32ed2e54'
TK = json.load(open(OUT + '/tokmap_union.json'))
OC = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
OTH = {'YES': 'NO', 'NO': 'YES', 'Up': 'Down', 'Down': 'Up'}
def banda(e): return 'pre' if e < 0 else ('0-30' if e < 30 else ('30-120' if e < 120 else ('120-240' if e < 240 else '240-300')))
def tbin(T): return '(5,60]' if T <= 60 else ('(60,150]' if T <= 150 else '(150,300]')
def subb(pc):
    if pc < 0.30: return 'CTRL'
    return '0.70-0.80' if pc < 0.80 else ('0.80-0.90' if pc < 0.90 else ('0.90-0.95' if pc < 0.95 else '0.95-0.99'))
def szb(c): return '<5' if c < 5 else ('5-25' if c < 25 else ('25-100' if c < 100 else '>=100'))
G = collections.defaultdict(lambda: [0., 0., 0]); AG = collections.defaultdict(lambda: [0., 0., 0., 0])
CL = collections.defaultdict(lambda: [0., 0.]); UN = collections.defaultdict(lambda: [0., 0.])
COVG = collections.defaultdict(lambda: [0., 0.]); COVC = collections.defaultdict(lambda: [0., 0.]); ST = collections.Counter()

def gadd(role, coin, mkt, lab, sd, p, sh, usd, e, win):
    bd = banda(e)
    for mode in (('lit', 'eq') if sd == '0' else ('eq',)):
        if sd == '0': pp, ll, ww, cost = p, lab, win, usd
        else: pp = 1. - p; ll = OTH[lab]; ww = 1 - win; cost = sh * pp
        fee = 0.07 * pp * (1. - pp) * sh
        pnl = sh * ww - cost + (-fee if role == 'T' else 0.2 * fee)
        b = min(int(pp * 20 + 1e-9), 19)
        for bb in (bd, 'ALL'):
            x = G[(role, mode, coin, bb, b, mkt, ll)]; x[0] += pnl; x[1] += cost; x[2] += 1

def grupo(g, ts):
    M = g[-1] if g[-1][1] == 'M' else None
    ST['grupos'] += 1
    if M is None: ST['grupos_sin_M'] += 1
    if M is not None and M[2] != DED:
        _, _, tw, _, sd, tok, ma, ta = M
        sh, usd = (ta, ma) if sd == '0' else (ma, ta)
        i = TK.get(tok)
        if sh > 0 and i is None: ST['usd_sin_mapa_T'] += usd
        elif sh > 0 and i[1] == '5min':
            coin, fr, mkt, close, lab = i; o = OC.get(mkt)
            COVG[coin][1] += usd
            if o is not None:
                COVG[coin][0] += usd; gadd('T', coin, mkt, lab, sd, usd / sh, sh, usd, ts - (close - 300), 1 if o == lab else 0)
    fl = []
    for r in g:
        if r[1] != 'F' or r[3] == EX: continue
        _, _, mw, tw, sd, tok, ma, ta = r
        sh, usd = (ta, ma) if sd == '0' else (ma, ta)
        if sh <= 0: continue
        i = TK.get(tok)
        if i is None: ST['usd_sin_mapa_K'] += usd; continue
        coin, fr, mkt, close, lab = i
        if fr != '5min': continue
        p = usd / sh; o = OC.get(mkt); win = None if o is None else (1 if o == lab else 0)
        COVG[coin][1] += usd
        if win is not None:
            COVG[coin][0] += usd
            if mw != DED: gadd('K', coin, mkt, lab, sd, p, sh, usd, ts - (close - 300), win)
        if sd == '0': pc, el, we = p, lab, win
        else: pc, el, we = 1. - p, OTH[lab], (None if win is None else 1 - win)
        fl.append((mkt, el, round(pc, 3), pc, sh, we, coin, close, mw))
    if not fl: return
    lv = collections.defaultdict(set)
    for f in fl: lv[(f[0], f[1])].add(f[2])
    if len(lv) > 1: ST['grupos_multilado'] += 1
    it = TK.get(M[5]) if M is not None else None
    for mkt, el, pr, pc, sh, we, coin, close, mw in fl:
        T = close - ts
        if not (5 < T <= 300): continue
        if 0.70 <= pc < 0.99: bc = 'FAV'
        elif 0.05 <= pc < 0.30: bc = 'CTRL'
        else: continue
        if mw == DED: ST['rellenos_dedicada_excl'] += 1; continue
        cost = sh * pc; COVC[coin][1] += cost
        if we is None: continue
        COVC[coin][0] += cost
        L = sum(1 for q in lv[(mkt, el)] if q > pr)
        cls = 'TOP' if L == 0 else ('MID' if L == 1 else 'DEEP')
        if it is None or it[2] != mkt: ct = 'NA'
        elif M[4] == '0' and it[4] != el: ct = 'MINT'
        elif M[4] == '1' and it[4] == el: ct = 'CRUCE'
        else: ct = 'NA'
        pnl = sh * (we - pc); reb = 0.014 * pc * (1. - pc) * sh; sb = subb(pc)
        wm = 'W' if mw.startswith(WP) else ('MM' if mw.startswith(MP) else 'O')
        a = AG[(bc, coin, sb, cls, ct, tbin(T), szb(cost), wm)]; a[0] += pnl; a[1] += cost; a[2] += reb; a[3] += 1
        u = UN[(bc, coin, sb, cls, mkt, el)]; u[0] += pnl; u[1] += cost
        if bc == 'FAV':
            x = CL[('A_' + cls, close, coin)]; x[0] += pnl; x[1] += cost
            if coin == 'BTC' and pc >= 0.90:
                x = CL[('B_' + cls, close, coin)]; x[0] += pnl; x[1] += cost

def proc(rows, ts):
    rows.sort(key=lambda r: r[0]); g = []; last = None
    for r in rows:
        if r[0] == last: ST['dup_tx_li'] += 1; continue
        last = r[0]; g.append(r)
        if r[1] == 'M': grupo(g, ts); g = []
    if g: grupo(g, ts)

seen = set(); cur = None; buf = []; ts = 0.; skip = False; n = 0
with gzip.open(f'{V}/m5_onchain/m5_onchain_{D}.csv.gz', 'rt', newline='') as f:
    rd = csv.reader(f); h = next(rd)
    assert h[:12] == ['tipo', 'bloque', 'ts_est', 'tx', 'log_index', 'order_hash', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt'], h
    for c in rd:
        n += 1
        if MAXF and n > MAXF: break
        if c[3] != cur:
            if buf and not skip: proc(buf, ts)
            if cur is not None: seen.add(cur)
            cur = c[3]; buf = []; ts = float(c[2]); skip = cur in seen
            if skip: ST['tx_no_contiguas'] += 1
        if skip: ST['filas_tx_no_contiguas'] += 1; continue
        buf.append((int(c[4]), c[0], c[6].lower(), c[7].lower(), c[8], c[9], float(c[10] or 0), float(c[11] or 0)))
    if buf and not skip: proc(buf, ts)
ST['filas'] = n
grid = collections.defaultdict(lambda: [0., 0., 0, 0, 0.])
for (role, mode, coin, bb, b, mkt, ll), (p, c, nf) in G.items():
    x = grid[f'{role}|{mode}|{coin}|{bb}|{b}']; x[0] += p; x[1] += c; x[2] += 1; x[3] += nf; x[4] += (p / c if c > 0 else 0.)
res = {'dia': D, 'maxfilas': MAXF, 'st': dict(ST), 'covg': COVG, 'covc': COVC, 'grid': grid,
       'ag': {'|'.join(k): v for k, v in AG.items()},
       'cl': {f'{k[0]}|{k[1]}|{k[2]}': v for k, v in CL.items()},
       'un': [[k[0], k[1], k[2], k[3], round(v[0], 4), round(v[1], 4)] for k, v in UN.items()]}
json.dump(res, open(f'{OUT}/dia_{D}.json.tmp', 'w')); os.replace(f'{OUT}/dia_{D}.json.tmp', f'{OUT}/dia_{D}.json')
print(D, dict(ST), flush=True)
