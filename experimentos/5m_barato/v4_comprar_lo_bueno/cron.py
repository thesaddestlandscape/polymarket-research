#!/usr/bin/env python3
"""Cronología por señal V4 OOS. Lee los extractos de extrae.py (SCR/ext). Reloj: rx = recepción local (ms), ex = exchange (ms)."""
import csv, glob, json, sys, bisect, collections, statistics as st
from datetime import datetime, timezone
D = '/root/polymarket-research-datalogs/'
S = sys.argv[1]
EXCH = '0xe111180000d2663c0091e4f400237545b87b996b'
des = json.load(open(D + 'maker_ms_desenlaces_cache.json'))
cong = int(datetime.fromisoformat('2026-10-06T12:00:00+00:00').timestamp() * 1000)
E = []
for f in sorted(glob.glob(D + 'vigia_5m_barato/eventos_*.csv')):
    E += list(csv.DictReader(open(f)))
prim = [e for e in E if e['regla'] == 'B1_5m' and e['es_primero'] == '1' and int(e['t_deteccion']) >= cong]
SIM = {'BTC': 'BTCUSDT', 'ETH': 'ETHUSDT', 'SOL': 'SOLUSDT', 'XRP': 'XRPUSDT', 'DOGE': 'DOGEUSDT', 'BNB': 'BNBUSDT'}
def fee(p): return 0.07 * p * (1 - p)
def fl(x): return None if x in ('', 'None') else float(x)

def load_qt(path, tokset):
    q, t = collections.defaultdict(set), collections.defaultdict(set)
    for ln in open(path):
        c = ln.rstrip('\n').split(',')
        if c[0] == 'q' and c[2] in tokset:
            try: q[c[2]].add((int(c[7]), int(c[1]), fl(c[3]), fl(c[4]), fl(c[5]) or 0.0, fl(c[6]) or 0.0))  # rx, ex, bid, ask, bsz, asz
            except Exception: pass
        elif c[0] == 't' and c[2] in tokset:
            try: t[c[2]].add((int(c[6]), int(c[1]), float(c[3]), c[4], float(c[5])))  # rx, ex, price, side, size
            except Exception: pass
    return {k: sorted(v, key=lambda r: (r[0], r[1])) for k, v in q.items()}, {k: sorted(v, key=lambda r: (r[0], r[1])) for k, v in t.items()}

def rows_event(dia):
    toks = json.load(open(f'{S}/toks_{dia}.json'))
    ts = {t for v in toks.values() for t in v if t}
    q5, t5 = load_qt(f'{S}/qt5_{dia}.txt', ts)
    q15, _ = load_qt(f'{S}/qt15_{dia}.txt', ts)
    X = collections.defaultdict(list)
    for ln in open(f'{S}/x_{dia}.txt'):
        c = ln.split(',')
        try: X[c[2]].append((int(c[7]), float(c[3]), int(c[5])))
        except Exception: pass
    for k in X: X[k].sort()
    oc = []
    for ln in open(f'{S}/oc_{dia}.txt'):
        c = ln.rstrip('\n').split(',')
        if c[0] == 'F' and len(c) >= 13: oc.append(c)
    return toks, q5, t5, q15, X, oc

def last_before(Q, t_rx, strict=False):
    ts = [r[0] for r in Q]
    i = (bisect.bisect_left(ts, t_rx) if strict else bisect.bisect_right(ts, t_rx)) - 1
    return (Q[i] if i >= 0 else None), i

out = []
for dia in sorted({datetime.fromtimestamp(int(e['t_deteccion']) / 1000, timezone.utc).date().isoformat() for e in prim}):
    try: toks, q5, t5, q15, X, oc = rows_event(dia)
    except FileNotFoundError: continue
    Ed = [e for e in prim if datetime.fromtimestamp(int(e['t_deteccion']) / 1000, timezone.utc).date().isoformat() == dia]
    for e in Ed:
        k5, k15 = toks[e['event_id']]
        r = dict(event_id=e['event_id'], dia=dia, moneda=e['moneda'], lado=e['lado'], cierre=int(e['cierre']), t0=int(e['t_deteccion']),
                 ask0=float(e['ask_compra_t0']), bid15_0=float(e['bid_otro_t0']), plim=float(e['p_limite']), cls215=e['L215_clase'],
                 cls150=e['L150_clase'], cls250=e['L250_clase'], resto=float(e['resto_s']))
        r['gana'] = (des[e['market_compra']] == 'YES') == (e['lado'] == 'Up')
        Q5, T5, Q15 = q5.get(k5, []), t5.get(k5, []), q15.get(k15, [])
        r['n_q5'], r['n_q15'], r['n_t5'] = len(Q5), len(Q15), len(T5)
        t0 = r['t0']
        if not Q5 or not Q15: out.append(r); continue
        # fila trigger: q con rx == t0 en cada pata
        a5 = [x for x in Q5 if x[0] == t0]; a15 = [x for x in Q15 if x[0] == t0]
        p5, _ = last_before(Q5, t0, strict=True); p15, _ = last_before(Q15, t0, strict=True)
        trig = []
        if a5 and p5 and (a5[-1][3] != p5[3]): trig.append('5m_ask')
        if a15 and p15 and (a15[-1][2] != p15[2]): trig.append('15m_bid')
        if a5 and not any(t == '5m_ask' for t in trig): pass
        r['trigger'] = '+'.join(trig) if trig else ('5m_otro' if a5 and not a15 else '15m_otro' if a15 and not a5 else 'desconocido')
        # tiempos exchange del trigger
        tex5 = a5[-1][1] if a5 else None; tex15 = a15[-1][1] if a15 else None
        r['t_trig_ex'] = max([x for x in (tex5 if '5m_ask' in trig else None, tex15 if '15m_bid' in trig else None) if x] or [tex5 or tex15 or t0])
        r['feed_ms'] = t0 - r['t_trig_ex']
        # estado previo: ask5 y bid15 antes
        r['ask5_prev'] = p5[3] if p5 else None; r['bid15_prev'] = p15[2] if p15 else None
        r['ask5_prev_sz'] = p5[5] if p5 else None
        # edad del precio previo del lado que NO cambia
        def edad(Q, k, t):
            i = bisect.bisect_right([x[0] for x in Q], t) - 1
            if i < 0: return None
            v = Q[i][k]
            j = i
            while j > 0 and Q[j - 1][k] == v: j -= 1
            return t - Q[j][0]
        r['edad_ask5_ms'] = edad(Q5, 3, t0 - 1) if False else None
        # ask0 / tamaño en t0
        q0, _ = last_before(Q5, t0)
        r['ask0_sz'] = q0[5] if q0 else None
        # consumo: BUY a precio <= plim con rx > t0-3000
        cons = [x for x in T5 if x[3] == 'BUY' and x[2] <= r['plim'] + 1e-9 and r['t_trig_ex'] - 3000 <= x[1]]
        # trades en nivel ask0
        c_ev = [x for x in cons if x[1] >= r['t_trig_ex'] - 200]
        r['cons_ex_trig_ms'] = (c_ev[0][1] - r['t_trig_ex']) if c_ev else None
        r['cons_rx_t0_ms'] = (c_ev[0][0] - t0) if c_ev else None
        r['cons_pre_200ms'] = len([x for x in cons if x[1] < r['t_trig_ex'] - 0 and x[1] >= r['t_trig_ex'] - 3000])
        r['cons_precio'] = c_ev[0][2] if c_ev else None
        r['cons_sz'] = c_ev[0][4] if c_ev else None
        # desaparición: primera q rx > t0 con ask > plim o None
        g = next((x for x in Q5 if x[0] > t0 and (x[3] is None or x[3] > r['plim'] + 1e-9)), None)
        r['gone_rx_t0_ms'] = (g[0] - t0) if g else None
        r['gone_ex_trig_ms'] = (g[1] - r['t_trig_ex']) if g else None
        # q intermedias entre t0 y gone
        r['q5_changes_before_gone'] = len([x for x in Q5 if t0 < x[0] <= (g[0] if g else t0 + 3000)])
        # tamaño visible antes de gone y trades
        if g:
            pg, _ = last_before(Q5, g[0], strict=True)
            r['pre_gone_sz'] = pg[5] if pg else None
            trs = [x for x in T5 if x[3] == 'BUY' and x[2] <= r['plim'] + 1e-9 and r['t_trig_ex'] - 300 <= x[1] <= g[1] + 120]
            r['trades_sz_hasta_gone'] = round(sum(x[4] for x in trs), 3)
            r['trades_n_hasta_gone'] = len(trs)
        # bid15 tras t0
        for L in (100, 215, 355):
            qq, _ = last_before(Q15, t0 + L)
            r[f'bid15_t0+{L}'] = qq[2] if qq else None
        # Binance
        xs = X.get(SIM[e['moneda']], [])
        xt = [x[0] for x in xs]
        sgn = 1 if e['lado'] == 'Up' else -1
        def px(t):
            j = bisect.bisect_right(xt, t) - 1
            return xs[j][1] if j >= 0 else None
        p0 = px(t0)
        for w in (500, 1000, 3000, 10000):
            pw = px(t0 - w)
            r[f'bin_{w}'] = round(sgn * (p0 / pw - 1) * 1e4, 3) if p0 and pw else None
        # primer cruce de +0.5 bp orientado en los 5 s previos a t0
        base = px(t0 - 5000)
        prec = None
        if base:
            for tr_, p_, _m in xs:
                if t0 - 5000 <= tr_ <= t0 and sgn * (p_ / base - 1) * 1e4 >= 0.5:
                    prec = tr_ - t0; break
        r['bin_prec_ms'] = prec
        # on-chain wallet del consumo
        r['wallet'] = None
        if c_ev:
            tr = c_ev[0]
            best = None
            for c in oc:
                if c[9] != k5 or c[7] != EXCH or c[8] != '0': continue
                ts_ = float(c[2]); 
                if not (tr[1] / 1000 - 1 <= ts_ <= tr[1] / 1000 + 6): continue
                try: pr_ = float(c[10]) / float(c[11]); acc = float(c[11])
                except Exception: continue
                if abs(pr_ - tr[2]) > 0.006: continue
                d_ = abs(acc - tr[4])
                if best is None or d_ < best[0]: best = (d_, c[6].lower(), pr_, acc, c[3], ts_)
            if best: r['wallet'], r['w_precio'], r['w_acc'], r['w_tx'], r['w_block_ts'] = best[1], round(best[2], 4), round(best[3], 2), best[4], best[5]
        out.append(r)
    print(dia, len(Ed), flush=True)
json.dump(out, open(f'{S}/cron_out.json', 'w'))
print(len(out))
