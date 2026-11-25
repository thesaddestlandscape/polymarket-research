#!/usr/bin/env python3
"""b_policy_sim.py DIA [--policy R3|R2|R1] -- simulador de la POLITICA REAL de B (experimento_maker_h47.py escalon B/H35, CONTRATO_MEDICION_F5_B_v2 sec.1-2). Solo calculo, 0 ordenes, nada en data/.
Reloj: UTC epoch ms. DECIDE con la vista RX (K del motor: filas q por recepcion); la MECANICA DE RELLENO es la del motor v4 en EXCHANGE (engine_v4.fill_segment_v4, tm3). t_dec = rx + B_DEC_RX (supuesto 50);
alta efectiva t_arr = t_dec + B_D_ALTA + B_EX_ALTA (53+35); cancelacion efectiva = t_dec_cancel + B_D_CANC + B_EX_CANC (0+33). Funciones de decision (en_banda, objetivo_h35, en_rejilla, tamano_orden) y constantes: del .py del ejecutor por AST (ejecutor_puro.py).
NO modelado (declarado): presupuesto/N_MAX/rotacion de tandas, min_size del mercado, ws_viejo/tick_cambiado, efecto propio de nuestra orden en el libro (en 26-Oct+ no habia ordenes propias de B en el libro; en la realidad nuestra orden visible puede cambiar top()).
Politicas: R3 = B real (control, la que hizo B). R2 = B real + armado: cancelar cuando bid_rx(t)-L < 0,0099. R1 = poner/mantener solo si bid_rx(t)-L >= D_R1 (0,06). R1/R2 = REGLAS de fase 2: aqui sin validar.
Primer relleno cierra la puja (detectado en tf + B_DET_FILL ms; poll real 0,5 s); la cantidad se trunca en la cancelacion efectiva que sigue a la deteccion."""
import sys, os, json, time, hashlib, heapq, numpy as np, pandas as pd
T0 = time.time(); H = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, H)
import eng_v5 as EV, ejecutor_puro as EP
G, E4 = EV.G, EV.E4; NS, SHA_EJ = EP.carga()
en_banda, objetivo_h35, en_rejilla, tamano_orden = NS['en_banda'], NS['objetivo_h35'], NS['en_rejilla'], NS['tamano_orden']
KMON = NS['K_POR_MONEDA']; T_INI = NS['T_INI']; T_STOP = NS['T_STOP_DEF']; LOOP = int(NS['LOOP_S'] * 1000); ASENTAR = int(NS['ASENTAR_H47_S'] * 1000); MIN_ACC = int(NS['MIN_ENTRE_ACCIONES_S'] * 1000)
INVAL = int(NS['REQUOTE_INVALIDO_S'] * 1000); MAXV = NS['MAX_VIVAS']; MAXP = NS['MAX_ORDENES_PUJA']
def params(env=os.environ):
    return dict(policy=env.get('B_POLICY', 'R3'), dec_rx=int(env.get('B_DEC_RX', 50)), d_alta=int(env.get('B_D_ALTA', 53)), ex_alta=int(env.get('B_EX_ALTA', 35)), d_canc=int(env.get('B_D_CANC', 0)), ex_canc=int(env.get('B_EX_CANC', 33)),
                det_fill=int(env.get('B_DET_FILL', 250)), post_block=int(env.get('B_POST_BLOCK', 88)), canc_block=int(env.get('B_CANC_BLOCK', 61)), settle_extra=int(env.get('B_SETTLE_EXTRA', 200)), tick=int(env.get('B_TICK', 1)), d_r1=float(env.get('B_D_R1', 0.06)), arm=float(env.get('B_ARM', 0.0099)))
def tag_of(P): return P['policy'] + '_' + hashlib.sha256(json.dumps(P, sort_keys=True).encode()).hexdigest()[:8]

class Mkt:
    def __init__(s, mid, ku, kd, fin, coin, K):
        s.mid, s.ku, s.kd, s.fin, s.coin, s.kx = mid, ku, kd, fin, coin, KMON[coin]; s.o = None; s.cerrado = False; s.done = False; s.tok = None; s.t_accion = -10**15; s.settle_until = -10**15; s.fuera = None; s.n_ord = 0
        s.A = {}
        for k in (ku, kd):
            a, b = K.qb[k], K.qb[k + 1]; s.A[k] = (K.qt[a:b], K.v0[a:b].astype(float), K.v1[a:b].astype(float))
    def top(s, k, t):
        qt, v0, v1 = s.A[k]; j = int(np.searchsorted(qt, t, side='right')) - 1
        if j < 0: return None, None
        b, a = v0[j], v1[j]
        return (float(b) if np.isfinite(b) and b > 0 else None), (float(a) if np.isfinite(a) and a > 0 else None)

def run_day(d, P, E=None):
    if E is None: E, info = EV.build(d)
    else: info = {}
    D, K = E.D, E.K; pol = P['policy']; LA = P['d_alta'] + P['ex_alta']; LC = P['d_canc'] + P['ex_canc']; DET = P['det_fill']; DEC = P['dec_rx']
    cov = dict(tokens_5m=0, mercados=0, skip={}); byid = {}
    for k in E.ks:
        s = E.sane(k)
        if s != 'ok': cov['skip'][s] = cov['skip'].get(s, 0) + 1; continue
        if G.capt_outcome(E, k) is None: cov['skip']['sin_desenlace'] = cov['skip'].get('sin_desenlace', 0) + 1; continue
        byid.setdefault(D.mid[k], {})[D.lado[k]] = k
    mkts = []
    for mid, v in byid.items():
        if 'YES' in v and 'NO' in v: mkts.append(Mkt(mid, v['YES'], v['NO'], int(D.fin[v['YES']]), str(D.act[v['YES']]).lower(), K))
        else: cov['skip']['sin_par'] = cov['skip'].get('sin_par', 0) + 1
    cov['mercados'] = len(mkts); ORD = []; ACT = []       # ACT: ordenes que ocupan cupo (dict con 'rel')
    def evtimes(m):
        t = np.concatenate([m.A[m.ku][0], m.A[m.kd][0]]) + DEC; lo = (m.fin - 300) * 1000; hi = int((m.fin - T_STOP) * 1000) + 1000
        return np.unique(t[(t >= lo) & (t <= hi)])
    EVT = {id(m): evtimes(m) for m in mkts}; heap = []
    for i, m in enumerate(mkts): heapq.heappush(heap, (int((m.fin - T_INI) * 1000) + DEC, i))
    def settle(m, o, t_end):
        """fin de la orden: relleno acumulado hasta la cancelacion efectiva t_end (EX); el primer relleno cierra la puja."""
        o['t_end'] = int(t_end); q = 0.0; tf = None
        if o['tf1'] is not None and o['tf1'] <= t_end:
            q, tf, _ = E.run_segment(o['k'], o['L'], o['t_arr'], int(t_end), o['size'], 'BASE')
            if not E4.es_fill(q): q, tf = 0.0, None
        o['q'] = float(q); o['tf'] = int(tf) if tf is not None else -1
        if q > 0: m.cerrado = True
    def cancela(m, t, motivo):
        o = m.o; t_det = None
        if o['tf1'] is not None and motivo == 'relleno': pass
        settle(m, o, t + LC); o['motivo_fin'] = motivo; o['t_cancel_dec'] = int(t); o['rel'] = t + ASENTAR + P['settle_extra']; m.settle_until = t + ASENTAR + P['settle_extra']; m.t_accion = t; m.o = None; busy[0] = max(busy[0], t) + P['canc_block']
    busy = [0]   # hilo unico del ejecutor real: post (post_ms p50 88) y cancel (cancel_lat p50 61) BLOQUEAN el bucle de todos los mercados (ledger B 20-23 Oct)
    def ocupados(t): return sum(1 for x in ACT if x['rel'] > t)
    def paso(m, t):
        T = m.fin - t / 1000.0
        if P['tick'] and T > T_STOP and any(((lambda b_a: (b_a[0] is not None and b_a[0] >= 0.96) or (b_a[1] is not None and b_a[1] <= 0.04))(m.top(k_, t))) for k_ in (m.ku, m.kd)):
            if m.o is not None: cancela(m, t, 'tick_cambiado')     # tick_size_change del WS (precio >0,96 / <0,04): el ejecutor real cierra el mercado para siempre
            m.done = True; return
        if T <= T_STOP:
            if m.o is not None: cancela(m, t, 't_stop')
            m.done = True; return
        o = m.o
        if o is not None and o['tf1'] is not None and t >= o['tf1'] + DET:        # relleno detectado (poll): cierra la puja y cancela el resto
            m.cerrado = True; cancela(m, t, 'relleno'); return
        if m.cerrado: return
        tok = m.tok
        if tok is None:
            for k in (m.ku, m.kd):
                b, a = m.top(k, t)
                if b is not None and a is not None and en_rejilla(b) and en_banda(b, a): tok = k; break
        if tok is None: return
        b, a = m.top(tok, t); valido = b is not None and a is not None and b < a and en_rejilla(b)
        objetivo = objetivo_h35(b, a, m.kx) if valido and en_banda(b, a) else None
        if o is not None:
            if not valido:
                m.fuera = m.fuera if m.fuera is not None else t
                if t - m.fuera >= INVAL: m.fuera = None; cancela(m, t, 'libro_invalido')
                return
            m.fuera = None
            if t - m.t_accion < MIN_ACC: return
            if pol == 'R2' and b - o['L'] < P['arm'] - 1e-9: cancela(m, t, 'armado'); return
            if pol == 'R1' and b - o['L'] < P['d_r1'] - 1e-9: cancela(m, t, 'R1_dist'); return
            if objetivo is None or abs(objetivo - o['L']) > 1e-9: cancela(m, t, 'repega' if objetivo is not None else 'cancela_banda')
            return
        if objetivo is None or m.settle_until > t or t - m.t_accion < MIN_ACC: return
        if pol == 'R1' and b - objetivo < P['d_r1'] - 1e-9: return
        if ocupados(t) >= MAXV or m.n_ord >= MAXP: return
        if m.fin * 1000 - t <= (T_STOP + 2) * 1000: return
        size = tamano_orden(objetivo, 5, 1.0)
        if size is None: return
        m.tok = tok; k = tok; t_arr = t + LA; t_hard = int(m.fin * 1000 - T_STOP * 1000 + LC + 1000)
        q, tf, _ = E.run_segment(k, objetivo, t_arr, t_hard, size, 'BASE')
        o = dict(mid=m.mid, coin=m.coin, k=k, lado=str(D.lado[k]), L=float(objetivo), size=float(size), t_dec=int(t), t_arr=int(t_arr), T_dec=float(T), n_ord=m.n_ord, bid_dec=float(b), ask_dec=float(a),
                 tf1=(int(tf) if E4.es_fill(q) else None), fin=m.fin, gana=float(G.capt_outcome(E, k)), rel=10**18)
        m.n_ord += 1; m.o = o; m.t_accion = t; m.fuera = None; ORD.append(o); ACT.append(o); busy[0] = t + P['post_block']
    nev = 0
    while heap:
        t, i = heapq.heappop(heap); m = mkts[i]
        if m.done: continue
        if t < busy[0]: heapq.heappush(heap, (busy[0], i)); continue
        paso(m, t); nev += 1
        if m.done: continue
        cands = []; ev = EVT[id(m)]; j = int(np.searchsorted(ev, t, side='right'))
        if j < len(ev): cands.append(int(ev[j]))
        cands.append(int((m.fin - T_STOP) * 1000) + DEC)
        if m.settle_until > t: cands.append(int(m.settle_until))
        if m.fuera is not None: cands.append(int(m.fuera + INVAL))
        if m.o is not None and m.o['tf1'] is not None: cands.append(int(m.o['tf1'] + DET))
        if m.o is None and m.t_accion + MIN_ACC > t: cands.append(int(m.t_accion + MIN_ACC))
        nt = min(max(c, t + LOOP) for c in cands if c > t); heapq.heappush(heap, (nt, i))
    for m in mkts:
        if m.o is not None: settle(m, m.o, int(m.fin * 1000 - T_STOP * 1000 + LC)); m.o['motivo_fin'] = 'fin_forzado'
    R = pd.DataFrame(ORD)
    if len(R): R['cost'] = R.q * R.L; R['pnl'] = R.q * (R.gana - R.L)
    cov.update(eventos=nev, ordenes=len(R), ordenes_rellenas=int((R.q > 0).sum()) if len(R) else 0, mercados_con_orden=int(R.mid.nunique()) if len(R) else 0, info_motor=info, seg=round(time.time() - T0, 1))
    return R, cov

if __name__ == '__main__':
    d = sys.argv[1]; P = params(); TAG = tag_of(P); OUT = H + f'out_sim/{TAG}/'; os.makedirs(OUT, exist_ok=True)
    mf = OUT + f'manifest_{d}.json'
    if os.path.exists(mf) and json.load(open(mf)).get('status') == 'COMPLETE': print('ya', TAG, d); sys.exit(0)
    json.dump(dict(job=f'b_policy_sim {d} {TAG}', status='RUNNING', params=P, sha256_ejecutor=SHA_EJ, sha256_sim=hashlib.sha256(open(__file__, 'rb').read()).hexdigest(), t_ini=time.time()), open(mf, 'w'))
    try:
        R, cov = run_day(d, P)
        R.to_pickle(OUT + f'ordenes_{d}.pkl.tmp'); os.replace(OUT + f'ordenes_{d}.pkl.tmp', OUT + f'ordenes_{d}.pkl')
        json.dump(dict(job=f'b_policy_sim {d} {TAG}', status='COMPLETE', params=P, sha256_ejecutor=SHA_EJ, sha256_sim=hashlib.sha256(open(__file__, 'rb').read()).hexdigest(), cobertura=cov, t_fin=time.time()), open(mf + '.tmp', 'w')); os.replace(mf + '.tmp', mf)
        print('ok', d, TAG, json.dumps(cov, default=str))
    except Exception as ex:
        json.dump(dict(job=f'b_policy_sim {d} {TAG}', status='FAILED', err=repr(ex)), open(mf, 'w')); raise
