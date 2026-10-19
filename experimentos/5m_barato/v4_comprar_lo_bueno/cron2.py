#!/usr/bin/env python3
"""Cronología y precursores por señal V4 (B1_5m) a partir de los extractos de extrae.py. Solo lectura.
Relojes: rx = recepción local (decisión), ex = exchange (identificar quién/cuándo), E = hora de evento de Binance (SOLO para identificar
quién reacciona a qué; nunca para decidir). Salida: SCR/ext/cron2_out.json
Uso: python3 cron2.py SCR/ext [todos]   (todos = incluye re-arms)"""
import csv, glob, json, sys, bisect, collections
from datetime import datetime, timezone
D = '/root/polymarket-research-datalogs/'
S = sys.argv[1]
TODOS = len(sys.argv) > 2 and sys.argv[2] == 'todos'
EXCH = '0xe111180000d2663c0091e4f400237545b87b996b'
des = json.load(open(D + 'maker_ms_desenlaces_cache.json'))
cong = int(datetime.fromisoformat('2026-10-06T12:00:00+00:00').timestamp() * 1000)
E = []
for f in sorted(glob.glob(D + 'vigia_5m_barato/eventos_*.csv')):
    E += list(csv.DictReader(open(f)))
prim = [e for e in E if e['regla'] == 'B1_5m' and (TODOS or e['es_primero'] == '1') and int(e['t_deteccion']) >= cong]
SIM = {'BTC': 'BTCUSDT', 'ETH': 'ETHUSDT', 'SOL': 'SOLUSDT', 'XRP': 'XRPUSDT', 'DOGE': 'DOGEUSDT', 'BNB': 'BNBUSDT'}
def fl(x): return None if x in ('', 'None') else float(x)
def fee(p): return 0.07 * p * (1 - p)

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
    k = lambda r: (r[0], r[1])
    return {a: sorted(v, key=k) for a, v in q.items()}, {a: sorted(v, key=k) for a, v in t.items()}

def idx_le(keys, v):  # último índice con keys[i] <= v
    return bisect.bisect_right(keys, v) - 1

out = []
dias = sorted({datetime.fromtimestamp(int(e['t_deteccion']) / 1000, timezone.utc).date().isoformat() for e in prim})
for dia in dias:
    try: toks = json.load(open(f'{S}/toks_{dia}.json'))
    except FileNotFoundError: continue
    Ed = [e for e in prim if datetime.fromtimestamp(int(e['t_deteccion']) / 1000, timezone.utc).date().isoformat() == dia]
    ts = {t for v in toks.values() for t in v if t}
    q5, t5 = load_qt(f'{S}/qt5_{dia}.txt', ts)
    q15, t15 = load_qt(f'{S}/qt15_{dia}.txt', ts)
    X = collections.defaultdict(list)
    for ln in open(f'{S}/x_{dia}.txt'):
        c = ln.split(',')
        try: X[c[2]].append((int(c[6]), float(c[3]), int(c[7])))   # E, precio, rx
        except Exception: pass
    for k in X: X[k].sort()
    oc = [c for c in (ln.rstrip('\n').split(',') for ln in open(f'{S}/oc_{dia}.txt')) if c[0] == 'F' and len(c) >= 13]
    for e in Ed:
        eid = e['event_id']
        base_id = eid.rsplit('_', 1)[0] + '_1'
        if eid in toks: k5, k15 = toks[eid]
        elif base_id in toks: k5, k15 = toks[base_id]
        else: continue
        r = dict(event_id=eid, dia=dia, moneda=e['moneda'], lado=e['lado'], cierre=int(e['cierre']), es_primero=int(e['es_primero']),
                 t0=int(e['t_deteccion']), ask0=float(e['ask_compra_t0']), bid15_0=float(e['bid_otro_t0']), plim=float(e['p_limite']),
                 cls150=e['L150_clase'], cls215=e['L215_clase'], cls250=e['L250_clase'], resto=float(e['resto_s']),
                 acc215=float(e['L215_acciones'] or 0), p215=fl(e['L215_precio']))
        r['gana'] = (des.get(e['market_compra']) == 'YES') == (e['lado'] == 'Up') if e['market_compra'] in des else None
        Q5, T5, Q15, T15 = q5.get(k5, []), t5.get(k5, []), q15.get(k15, []), t15.get(k15, [])
        r['n_q5'], r['n_q15'] = len(Q5), len(Q15)
        t0 = r['t0']
        if not Q5 or not Q15: out.append(r); continue
        rx5 = [x[0] for x in Q5]; rx15 = [x[0] for x in Q15]
        a5 = [x for x in Q5 if x[0] == t0]; a15 = [x for x in Q15 if x[0] == t0]
        i5 = bisect.bisect_left(rx5, t0) - 1; i15 = bisect.bisect_left(rx15, t0) - 1   # estrictamente antes
        p5 = Q5[i5] if i5 >= 0 else None; p15 = Q15[i15] if i15 >= 0 else None
        trig = []
        if a5 and p5 and a5[-1][3] != p5[3]: trig.append('5m_ask')
        if a15 and p15 and a15[-1][2] != p15[2]: trig.append('15m_bid')
        r['trigger'] = '+'.join(trig) if trig else 'otro'
        # reloj exchange del trigger
        exs = []
        if '5m_ask' in trig: exs.append(a5[-1][1])
        if '15m_bid' in trig: exs.append(a15[-1][1])
        if not exs: exs = [x[-1][1] for x in (a5, a15) if x] or [t0]
        r['t_trig_ex'] = max(exs); T = r['t_trig_ex']
        r['feed_ms'] = t0 - T
        r['ask5_prev'] = p5[3] if p5 else None; r['bid15_prev'] = p15[2] if p15 else None
        r['ask5_prev_sz'] = p5[5] if p5 else None
        r['bid5_t0'] = (a5[-1][2] if a5 else (p5[2] if p5 else None))
        # tamaño y precio vigente del ask a t0
        j5 = idx_le(rx5, t0)
        r['ask0_sz'] = Q5[j5][5] if j5 >= 0 else None
        r['bid5_sz_t0'] = Q5[j5][4] if j5 >= 0 else None
        # edad de ask5 y de bid15 inmediatamente antes de t0 (tiempo desde el último cambio de precio)
        def edad(Q, rx, col, i, t):
            if i < 0: return None
            v = Q[i][col]; j = i
            while j > 0 and Q[j - 1][col] == v: j -= 1
            return t - Q[j][0]
        r['edad_ask5_prev'] = edad(Q5, rx5, 3, i5, t0)
        r['edad_bid15_prev'] = edad(Q15, rx15, 2, i15, t0)
        # actividad 15m previa
        for w in (1000, 5000):
            r[f'n_bid15_chg_{w}'] = sum(1 for k in range(max(0, i15 - 400), i15 + 1) if Q15[k][0] >= t0 - w and k > 0 and Q15[k][2] != Q15[k - 1][2])
            r[f'n_ask5_chg_{w}'] = sum(1 for k in range(max(0, i5 - 400), i5 + 1) if Q5[k][0] >= t0 - w and k > 0 and Q5[k][3] != Q5[k - 1][3])
        r['bid15_ask15_t0'] = Q15[idx_le(rx15, t0)][3] if idx_le(rx15, t0) >= 0 else None
        # trayectoria bid15 previa: valor 250/500/1000/3000 ms antes de t0 (recepción)
        for w in (250, 500, 1000, 3000):
            j = idx_le(rx15, t0 - w); r[f'bid15_m{w}'] = Q15[j][2] if j >= 0 else None
        # trades 15m y 5m en la ventana previa (rx)
        r['t5_prev1s'] = sum(1 for x in T5 if t0 - 1000 <= x[0] < t0)
        r['t15_prev1s'] = sum(1 for x in T15 if t0 - 1000 <= x[0] < t0)

        # inicio latente de la condición (ignorando t_ini=C-300+1,5 s): retrocede desde t0 mientras margen>=0,05 con el último q de cada pata
        def marg(t):
            a = idx_le(rx5, t); b = idx_le(rx15, t)
            if a < 0 or b < 0: return None
            ask, bid = Q5[a][3], Q15[b][2]
            if ask is None or bid is None: return None
            return round(bid - ask - fee(ask), 4)
        ts_all = sorted({x[0] for x in Q5 if t0 - 8000 <= x[0] <= t0} | {x[0] for x in Q15 if t0 - 8000 <= x[0] <= t0})
        start = t0
        for tt in reversed([t for t in ts_all if t <= t0]):
            m = marg(tt)
            if m is not None and m >= 0.05: start = tt
            else: break
        r['run_start_vs_t0_ms'] = start - t0
        r['t_open_rx'] = (r['cierre'] - 300) * 1000
        r['t0_desde_apertura_ms'] = t0 - r['t_open_rx']
        r['start_desde_apertura_ms'] = start - r['t_open_rx']

        # H23 maker pre-posicionado (simulación optimista: toca = llena, sin cola): puja de compra en t0-1000 al bid vigente ('join') o ask-1c ('mejora')
        jb = idx_le(rx5, t0 - 1000)
        if jb >= 0 and Q5[jb][2] is not None:
            for nom, pb in (('join', Q5[jb][2]), ('mejora', round((Q5[jb][3] - 0.01) if Q5[jb][3] is not None else 0, 2))):
                if pb is None or pb <= 0: continue
                sells = [x for x in T5 if x[3] == 'SELL' and x[2] <= pb + 1e-9 and t0 - 1000 <= x[0]]
                for W in (2000, 10000, 60000):
                    f_ = next((x for x in sells if x[0] <= t0 + W), None)
                    r[f'mk_{nom}_{W}'] = None if f_ is None else dict(precio=pb, dt=f_[0] - t0)

        r['gap_prev_q5_ms'] = (t0 - Q5[i5][0]) if i5 >= 0 else None
        r['gap_prev_q15_ms'] = (t0 - Q15[i15][0]) if i15 >= 0 else None
        # mayor hueco entre filas q consecutivas de cada pata en los 120 s previos a t0
        for nom, QQ, ii in (('5', Q5, i5), ('15', Q15, i15)):
            mg = 0; k = ii
            while k > 0 and QQ[k][0] >= t0 - 120000:
                mg = max(mg, QQ[k][0] - QQ[k - 1][0]); k -= 1
            r[f'max_gap_q{nom}_120s'] = mg
        # consumo del nivel: BUY a precio <= plim con ex >= T - 300 (incluye lo ya en curso), y separado: despues del trigger
        trs = [x for x in T5 if x[3] == 'BUY' and x[2] <= r['plim'] + 1e-9]
        pre = [x for x in trs if T - 3000 <= x[1] < T]
        post = [x for x in trs if x[1] >= T]
        r['cons_pre_n'] = len(pre); r['cons_pre_sz'] = round(sum(x[4] for x in pre), 2)
        r['cons_ex_trig_ms'] = (post[0][1] - T) if post else None
        r['cons_rx_t0_ms'] = (post[0][0] - t0) if post else None
        r['cons_precio'] = post[0][2] if post else None; r['cons_sz'] = post[0][4] if post else None
        # desaparición: primera q con rx>t0, ask>plim o sin ask
        g = next((x for x in Q5 if x[0] > t0 and (x[3] is None or x[3] > r['plim'] + 1e-9)), None)
        r['gone_rx_t0_ms'] = (g[0] - t0) if g else None
        r['gone_ex_trig_ms'] = (g[1] - T) if g else None
        # q intermedias que reducen el tamaño del nivel (ask0) antes de gone
        if g:
            ig = bisect.bisect_left(rx5, g[0]) - 1
            r['sz_pre_gone'] = Q5[ig][5]
            tw = [x for x in T5 if x[3] == 'BUY' and x[2] <= r['plim'] + 1e-9 and T <= x[1] <= g[1] + 100]
            r['trades_sz_T_gone'] = round(sum(x[4] for x in tw), 2)
            r['trades_n_T_gone'] = len(tw)
            # ¿hay operaciones SELL (que no son compra del lado) en la ventana? (informativo)
        # bid15 posterior (diagnóstico: solo visible tras t0)
        for L in (100, 215, 355, 1000):
            j = idx_le(rx15, t0 + L); r[f'bid15_p{L}'] = Q15[j][2] if j >= 0 else None
        # mid5 posterior
        for L in (215, 1000, 5000):
            j = idx_le(rx5, t0 + L); r[f'ask5_p{L}'] = Q5[j][3] if j >= 0 else None; r[f'bid5_p{L}'] = Q5[j][2] if j >= 0 else None
        # Binance en reloj E
        xs = X.get(SIM[e['moneda']], [])
        xe = [x[0] for x in xs]; sgn = 1 if e['lado'] == 'Up' else -1
        def pxE(t):
            j = idx_le(xe, t); return xs[j][1] if j >= 0 else None
        for w in (250, 500, 1000, 3000):
            a, b = pxE(T), pxE(T - w)
            r[f'binE_R{w}'] = round(sgn * (a / b - 1) * 1e4, 3) if a and b else None
        a, b = pxE(T + 500), pxE(T)
        r['binE_fwd500'] = round(sgn * (a / b - 1) * 1e4, 3) if a and b else None
        a, b = pxE(T + 2000), pxE(T)
        r['binE_fwd2000'] = round(sgn * (a / b - 1) * 1e4, 3) if a and b else None
        # inicio del movimiento (E): primer instante en [T-3000, T+300] con retorno orientado acumulado >= 1 bp respecto a T-3000
        base = pxE(T - 3000); onset = None; peak = None
        if base:
            for Ee, p_, _rx in xs:
                if T - 3000 <= Ee <= T + 300 and sgn * (p_ / base - 1) * 1e4 >= 1.0:
                    onset = Ee - T; break
        r['binE_onset_vs_trig_ms'] = onset
        # Binance visible para NOSOTROS (rx) antes de t0
        xr = sorted((x[2], x[1]) for x in xs); xrr = [x[0] for x in xr]
        def pxR(t):
            j = idx_le(xrr, t); return xr[j][1] if j >= 0 else None
        a, b = pxR(t0), pxR(t0 - 1000)
        r['binR_R1000'] = round(sgn * (a / b - 1) * 1e4, 3) if a and b else None
        a, b = pxR(t0), pxR(t0 - 250)
        r['binR_R250'] = round(sgn * (a / b - 1) * 1e4, 3) if a and b else None
        # wallet que consumió
        r['wallet'] = None
        if post:
            tr = post[0]; best = None
            for c in oc:
                if c[9] != k5 or c[7] != EXCH or c[8] != '0': continue
                ts_ = float(c[2])
                if not (tr[1] / 1000 - 1 <= ts_ <= tr[1] / 1000 + 6): continue
                try: pr_ = float(c[10]) / float(c[11]); acc = float(c[11])
                except Exception: continue
                if abs(pr_ - tr[2]) > 0.006: continue
                d_ = abs(acc - tr[4]) + 0.1 * abs(ts_ - (tr[1] / 1000 + 2.4))
                if best is None or d_ < best[0]: best = (d_, c[6].lower(), pr_, acc, c[3], ts_)
            if best: r['wallet'], r['w_precio'], r['w_acc'], r['w_tx'], r['w_block_ts'] = best[1], round(best[2], 4), round(best[3], 2), best[4], best[5]
            if best:
                mk = collections.Counter()
                for c in oc:
                    if c[3] == best[4] and c[0] == 'F' and c[7] != EXCH and c[6].lower() != best[1]:
                        mk[(c[6].lower(), c[8])] += 1
                r['w_makers_tx'] = [list(k) for k in mk]
        out.append(r)
    print(dia, len(Ed), flush=True)
json.dump(out, open(f'{S}/cron2_out{"_todos" if TODOS else ""}.json', 'w'))
print(len(out))
