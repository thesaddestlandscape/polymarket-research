#!/usr/bin/env python3
"""e1c_senales.py -- PREREG_E1C (sha 9b064af9...). Para cada orden REAL de B (20-22 Oct) calcula, en rejilla de 10 ms por RECEPCION, el primer instante
en que dispara cada una de las 33 configuraciones simples de F1-F6. Solo lectura. Salida: DL/e1_cancelacion_ms/senales.csv.gz (una fila por orden),
checkpoint por mercado (senales_parcial.jsonl, idempotente por clave act|mid), log con hora. Uso: nice -n 19 ionice -c3 python3 e1c_senales.py [--max N]"""
import os, sys, json, gzip, glob, hashlib, time, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.join(AQ, '..', '..')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_E1C.md'), 'rb').read()).hexdigest().startswith('9b064af90b24')
sys.path.insert(0, os.path.join(BASE, 'cola_posicion', 'scripts')); import d1_l2_motor as M
DLC = '/root/polymarket-research-datalogs/cola_posicion/'; OUT = '/root/polymarket-research-datalogs/e1_cancelacion_ms/'
CK = os.environ.get('E1C_CK', OUT + 'senales_parcial.jsonl'); LOG = OUT + 'e1c_senales.log'
LAT_CAN, LAG_PRINT, PASO = 60, 30, 10
def log(*a):
    with open(LOG, 'a') as f: f.write(time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()) + ' ' + ' '.join(map(str, a)) + '\n')
# ---- configs simples (F7 combos se forman en la evaluacion como OR de primeros disparos)
CFG = []
for W in (100, 300, 1000):
    for X in (1, 2, 3, 5): CFG.append(('BN', f'BN_W{W}_X{X}', W, X))
for W in (300, 1000):
    for d in (1, 2, 3): CFG.append(('KNIFE5', f'KN_W{W}_d{d}', W, d))
for g in (1, 2): CFG.append(('KNIFE5', f'GAP_g{g}', 0, g))
for W in (300, 1000):
    for c in (1, 2): CFG.append(('L15', f'L15_W{W}_c{c}', W, c))
for W in (200, 1000): CFG.append(('TRADE', f'TR_W{W}', W, 0))
for W in (300, 1000):
    for f in (50, 80): CFG.append(('DEPTH', f'DP_W{W}_f{f}', W, f))
CFG.append(('DEPTH', 'SOLO', 1000, 0))
for f in (50, 80): CFG.append(('DEPTH', f'AH_f{f}', 1000, f))
for A in (1, 2, 5, 10): CFG.append(('EDAD', f'ED_A{A}', A, 0))
assert len(CFG) == 37  # 37 simples (12+8+4+2+7+4); K_total 40 con 3 combos
# ---- Binance y 15m
def carga_bn():
    S = {}
    for f in sorted(glob.glob(OUT + 'maker_ms_*.x.gz')):
        A = pd.read_csv(f, header=None, names=['r', 'c', 'p'])
        for c, g in A.groupby('c'): S.setdefault(c, []).append(g[['r', 'p']].values)
    out = {}
    for c, l in S.items():
        a = np.concatenate(l); a = a[np.argsort(a[:, 0], kind='stable')]; out[c] = (a[:, 0].astype(np.int64), a[:, 1].astype(float))
    return out
def carga_15():
    K = {}; Q = {}
    for f in sorted(glob.glob(OUT + 'maker_ms_*.q2.gz')):   # v2: q con token (la v1 .q.gz guardaba la moneda: L15 vacio, bug corregido 24-Oct)
        with gzip.open(f, 'rt') as fh:
            for ln in fh:
                c = ln.rstrip('\n').split(',')
                if c[0] == 'k': K[c[1]] = (c[2], pd.Timestamp(c[4]).timestamp())
                elif c[0] == 'q':
                    try: r = int(c[1]); b = float(c[3]); a = float(c[4])
                    except ValueError: continue
                    if not (0 < b < a < 1): continue        # libro cruzado o lado vacio: descartado
                    Q.setdefault(c[2], []).append((r, (a + b) / 2))
    out = {}
    for tok, l in Q.items():
        if tok not in K: continue
        a = np.array(sorted(l)); out.setdefault(K[tok][0], []).append((K[tok][1], a[:, 0].astype(np.int64), a[:, 1]))
    return out
def last_val(tarr, varr, t):
    i = np.searchsorted(tarr, t, 'right') - 1
    v = np.where(i >= 0, varr[np.maximum(i, 0)], np.nan); return v
def main():
    mx = int(sys.argv[sys.argv.index('--max') + 1]) if '--max' in sys.argv else None
    O = json.load(open(DLC + 'ordenes_b.json')); TOK = {}
    for l in open(DLC + 'snap/ledger_B.jsonl'):
        d = json.loads(l)
        if d.get('tipo') == 'intencion_post': TOK[d['oid']] = d['tok']
    Lb = pd.read_csv(os.path.join(BASE, 'cola_posicion', 'datos', 'b_l2.csv')).set_index('oid')
    iso = lambda s: int(pd.Timestamp(s).timestamp() * 1000)
    BN = carga_bn(); F15 = carga_15(); log('BN', {k: len(v[0]) for k, v in BN.items()}, '15m', {k: len(v) for k, v in F15.items()})
    hecho = set()
    if os.path.exists(CK):
        for l in open(CK):
            try: hecho.add(json.loads(l)['key'])
            except Exception: pass                           # linea corrupta (corte a mitad): se recalcula ese mercado
    por = {}
    for o in O:
        t = TOK.get(o['oid'])
        if t is None or t not in M.TM: continue
        act, mid, lado, fin = M.TM[t]; por.setdefault((act, mid), []).append((o, 'Y' if lado == 'YES' else 'N', fin))
    keys = sorted(por); log('mercados', len(keys), 'ya hechos', len(hecho))
    n = 0
    for (act, mid) in keys:
        key = f'{act}|{mid}'
        if key in hecho: continue
        n += 1
        if mx and n > mx: break
        path = M.MK + f'{act}_{mid}.gz'; rows = []
        if not os.path.exists(path):
            for o, L, fin in por[(act, mid)]: rows.append(dict(oid=o['oid'], estado='sin_l2'))
        else:
            lvn, prn, tp, ap = M.carga(path)
            for o, L, fin in por[(act, mid)]:
                rows.append(una(o, L, fin, act, lvn, tp, ap, Lb, iso, BN, F15))
        with open(CK, 'a') as f: f.write(json.dumps(dict(key=key, rows=rows)) + '\n')
    log('fin bucle, nuevos', n)
def una(o, L, fin, act, lvn, tp, ap, Lb, iso, BN, F15):
    oid = o['oid']; q = M.mills(o['precio']); size = o['size']; Opp = 'N' if L == 'Y' else 'Y'
    r = dict(oid=oid, act=act, L=L, q=q, dia=o['ts_post'][:10], fin=fin, size=size)
    tc = int(o.get('t_call0', 0) * 1000)
    if not tc: r['estado'] = 'sin_tcall'; return r
    isf = oid in Lb.index
    arr = int(Lb.loc[oid].t_arr) if (isf and not pd.isna(Lb.loc[oid].get('t_arr', np.nan))) else tc + 122
    if isf:
        tpz = Lb.loc[oid].get('t_print', np.nan)
        if pd.isna(tpz): r['estado'] = 'relleno_sin_print'; return r
        end = int(tpz); tmax = end - LAG_PRINT - LAT_CAN
    else:
        if o.get('t_fuera'): end = iso(o['t_fuera'])
        elif o.get('t_cancel_int'): end = iso(o['t_cancel_int']) + 65
        else: r['estado'] = 'sin_fin'; return r
        tmax = end - LAT_CAN
    r.update(estado='ok', relleno=int(isf), arr=arr, end=end, vida=end - arr)
    if tmax < arr: return r                                    # no hay instante util para cancelar
    g = np.arange(arr, tmax + 1, PASO, dtype=np.int64)
    def otros(t):
        e = lvn.get((L, q))
        v = np.zeros(len(t)) if e is None else last_val(e[0], e[1], t)
        v = np.nan_to_num(v); own = (t >= arr) & (t <= end); return np.maximum(v - np.where(own, size, 0.0), 0.0)
    bL = last_val(*tp[L], g); bO = last_val(*tp[Opp], g)
    ok_libro = ~((bL > 0) & (bO > 0) & (bL + bO > 1000))         # descartar libro cruzado
    def ask(t):
        b = last_val(*tp[Opp], t); return np.where(b > 0, 1000 - b, np.nan)
    first = {}
    def put(name, mask):
        idx = np.flatnonzero(mask); first[name] = int(g[idx[0]]) if len(idx) else -1
    # F1 BN
    s = BN.get(act)
    for fam, name, W, X in CFG:
        if fam == 'BN':
            if s is None: first[name] = -2; continue
            p1 = last_val(s[0], s[1], g); p0 = last_val(s[0], s[1], g - W); ret = (p1 / p0 - 1) * 1e4
            if 'bn_stale' not in r:
                ia = np.searchsorted(s[0], g, 'right') - 1; age = np.where(ia >= 0, g - s[0][np.maximum(ia, 0)], 10**9); r['bn_stale'] = float((age > 2000).mean())
            put(name, (ret <= -X) if L == 'Y' else (ret >= X))
    a1 = ask(g)
    for fam, name, W, X in CFG:
        if fam == 'KNIFE5':
            if W: a0 = ask(g - W); put(name, ok_libro & ((a0 - a1) >= X * 10))
            else: put(name, ok_libro & ((a1 - q) <= X * 10))
    # F3 L15
    lst = F15.get(act)
    for fam, name, W, X in CFG:
        if fam != 'L15': continue
        if not lst: first[name] = -2; continue
        m1 = np.full(len(g), np.nan); m0 = np.full(len(g), np.nan)
        for cier, ta, va in lst:
            sel = (g / 1000 > cier - 900) & (g / 1000 <= cier)
            if sel.any(): m1[sel] = last_val(ta, va, g[sel]); m0[sel] = last_val(ta, va, g[sel] - W)
        dm = (m1 - m0) * 100
        if 'l15_nan' not in r: r['l15_nan'] = float(np.isnan(m1).mean())
        put(name, (dm <= -X) if L == 'Y' else (dm >= X))
    # F4 TRADE: prints que golpean bids de L a nivel > q
    P = ap[L]
    if len(P):
        tr = P[P[:, 1] > q][:, 0].astype(np.int64)
        for fam, name, W, X in CFG:
            if fam == 'TRADE':
                c1 = np.searchsorted(tr, g, 'right'); c0 = np.searchsorted(tr, g - W, 'right'); put(name, (c1 - c0) > 0)
    else:
        for fam, name, W, X in CFG:
            if fam == 'TRADE': first[name] = -1
    # F5 DEPTH
    o1 = otros(g)
    for fam, name, W, X in CFG:
        if fam != 'DEPTH': continue
        if name == 'SOLO': put(name, ok_libro & (o1 <= 0.5) & (otros(g - 1000) >= 5)); continue
        if name.startswith('DP'):
            o0 = otros(g - W); put(name, ok_libro & (o0 >= 5) & (o1 <= (1 - X / 100) * o0)); continue
    lv = [k for k in lvn if k[0] == L and k[1] > q]
    def ahead(t):
        v = np.zeros(len(t))
        for k in lv: v += np.nan_to_num(last_val(lvn[k][0], lvn[k][1], t))
        return v
    if lv:
        h1 = ahead(g); h0 = ahead(g - 1000)
        for f in (50, 80): put(f'AH_f{f}', ok_libro & (h0 >= 5) & (h1 <= (1 - f / 100) * h0))
    else:
        for f in (50, 80): first[f'AH_f{f}'] = -1
    for fam, name, A, X in CFG:
        if fam == 'EDAD': put(name, (g - arr) >= A * 1000)
    r.update({k: v for k, v in first.items()}); return r
if __name__ == '__main__':
    log('arranque', sys.argv); main()
    rows = []
    for l in open(CK):
        try: rows += json.loads(l)['rows']
        except Exception: continue
    D = pd.DataFrame(rows).drop_duplicates('oid', keep='last'); D.to_csv(CK.replace('_parcial.jsonl', '.csv.gz'), index=False); log('escrito', len(D), 'ordenes')
