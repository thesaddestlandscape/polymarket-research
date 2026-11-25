#!/usr/bin/env python3
"""a1_virtual_b.py (ident_17nov, Tarea A H1a/H1b) -- SOLO LECTURA, 0 ordenes, 0 EUR. Uso: python3 -I a1_virtual_b.py DIA
Aplica la regla de colocacion REAL de B (H35 DEEP_PEG de experimento_maker_h47.py: funciones mils/en_banda/objetivo_h35/en_rejilla/tamano_orden
EXTRAIDAS POR AST del fichero del ejecutor, no copiadas; K ETH 2/SOL 1/XRP 1; cara = primera (YES, luego NO) con bid en rejilla y en banda desde
T=298 s; repega al cambiar el objetivo; tras cancelar espera ASENTAR 1,5 s (+50 ms bucle) antes de repujar; no coloca con T<=62 s; parada T=60 s;
un relleno CIERRA la puja) como ORDEN VIRTUAL sobre el registro ms (sa_ms/ms_D.npz via capt.Day, el MISMO lector y reloj que f3_evento_vacio.py).
RELOJ: libro y cinta en sa_ms (EX segun verif_v3). B observa en ex + suelo(lo 19,25 / hi 39,5 / indet 30 ms, clase por ventana de 10 min de
pob_add3_D.json) + 50 ms (bucle LOOP_S 0,1 s, media). Latencia de alta/cancelacion: paquete_l 13-Nov (pool sin BTC p50: alta 35, cancel 32 ms;
l_pool_vigente_13nov.json); variante de sensibilidad 'octB' = latencias medidas de B en su ledger (t_ini-t_dec p50 89, t_fuera-t_cancel_int p50 65).
EVENTO (definicion de f3 trasladada al mundo SIN orden): con la virtual viva a L y sin rellenar, el mejor bid REAL del token cara pasa de > L+0,005
a <= L+0,0049 (o desaparece) -> en el mundo de B el tope nuevo seria L (= evento del brazo B de f3 con P'=L). GOLPE = mismo criterio que f3:
print WS vendedor (tsd=0) en el token a <= L+0,0049 o comprador (tsd=1) en el complementario con 1-p <= L+0,0049; dt = primer golpe tras el evento.
Relleno virtual (para cerrar la puja): 'any' = primer golpe <= L dentro de la vida (cota alta de relleno, sin cola); 'no' = nunca cierra.
Mercados: 5m ETH/SOL/XRP. conB = mercado con alguna orden real de B (ordenes_b.csv, por token y complementario): sus eventos NO entran en el brazo
virtual principal (solo se usan para FIDELIDAD: cara, ordenes y eventos frente a los reales). Salida: A_ev_D.pkl, A_ord_D.pkl, A_fid_D.json."""
import os, sys, ast, json, math, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/capturabilidad_A_R1ws'); import capt
DL = '/root/polymarket-research-datalogs/'
SRC_B = '/root/polymarket-research-dev/experimento_maker_h47.py'
_src = open(SRC_B).read(); _ns = {'math': math, 'SIZE_MIN': 5, 'SIZE_MAX': 10}
for _n in ast.parse(_src).body:
    if isinstance(_n, ast.FunctionDef) and _n.name in ('mils', 'en_banda', 'objetivo_h35', 'en_rejilla', 'tamano_orden'):
        exec(compile(ast.get_source_segment(_src, _n), SRC_B, 'exec'), _ns)
mils, en_banda, objetivo_h35, en_rejilla, tamano_orden = (_ns[k] for k in ('mils', 'en_banda', 'objetivo_h35', 'en_rejilla', 'tamano_orden'))
K = {'ETH': 2, 'SOL': 1, 'XRP': 1}
T_INI, T_STOP, T_NOPLACE = 298000, 60000, 62000
ASENTAR, LOOP, MIN_ACC, REQ_INV = 1500, 50, 100, 2000
LAT = {'pl': (35, 32), 'octB': (89, 65)}             # (alta, cancel) ms
VARS = [('pl', 'any'), ('pl', 'no'), ('octB', 'any')]
SUELO_MS = {'lo': 19.25, 'hi': 39.5, 'indet': 30.0}
d = sys.argv[1]
d0 = int(pd.Timestamp(d, tz='UTC').timestamp() * 1000)
def clase_p5(v):
    if v is None or not np.isfinite(v): return 'indet'
    if abs(v - 19.25) <= 5: return 'lo'
    if abs(v - 39.5) <= 5: return 'hi'
    return 'indet'
pa = '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/exp1/cache/' + f'pob_add3_{d}.json'
CL = ['indet'] * 144
if os.path.exists(pa):
    j = json.load(open(pa))
    if j.get('estado') == 'COMPLETE': CL = [clase_p5(None if v is None else float(v)) for v in j['C3_suelo_rx_menos_ex']['perfil_p5_10min']]
def clase_t(t):
    i = int((t - d0) // 600000); return CL[i] if 0 <= i < 144 else 'indet'
O = pd.read_csv(DL + 'calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str}, usecols=['oid', 'tok', 'dia', 'slug', 'precio', 'size', 't_dec', 't_ini', 't_cancel_int', 't_fuera', 'puja', 'fill', 'n_orden'])
BTOK = set(O.tok.astype(str))
D = capt.Day(d)
def golpes(k):
    ht, hp = [], []
    aa, bb = D.tb[k], D.tb[k + 1]; m = D.tsd[aa:bb] == 0; ht.append(D.tt[aa:bb][m]); hp.append(D.tp[aa:bb][m].astype(float))
    kc = D.comp(k)
    if kc is not None:
        aa, bb = D.tb[kc], D.tb[kc + 1]; m = D.tsd[aa:bb] == 1; ht.append(D.tt[aa:bb][m]); hp.append(1 - D.tp[aa:bb][m].astype(float))
    ht = np.concatenate(ht).astype(np.int64); hp = np.concatenate(hp); o = np.argsort(ht, kind='stable'); return ht[o], hp[o]
def first_golpe(ht, hp, t0, t1, L):
    """primer golpe <= L+0,0049 en (t0, t1] -> tiempo o None"""
    i0 = np.searchsorted(ht, t0, side='right'); i1 = np.searchsorted(ht, t1, side='right')
    c = np.where(hp[i0:i1] <= L + 0.0049)[0]
    return int(ht[i0 + c[0]]) if len(c) else None
def quotes(k):
    a, b = D.qb[k], D.qb[k + 1]
    return D.qt[a:b].astype(np.int64), np.round(D.v0[a:b].astype(float), 4), np.round(D.v1[a:b].astype(float), 4), D.v2[a:b].astype(float)
def obj(bid, ask, k):
    if not (np.isfinite(bid) and np.isfinite(ask)) or bid <= 0 or ask <= 0 or bid >= ask or not en_rejilla(bid) or not en_banda(bid, ask): return None
    return objetivo_h35(bid, ask, k)
def valido(bid, ask):
    return bool(np.isfinite(bid) and np.isfinite(ask) and bid > 0 and ask > 0 and bid < ask and en_rejilla(bid))
def dobs(t): return SUELO_MS[clase_t(t)] + LOOP
def maquina(kf, kk, fin, qt, v0, v1, i0, ht, hp, lat, close):
    """devuelve lista de ordenes virtuales dict(L, t_dec, t_ini, t_c, t_fuera, fill_t, motivo)"""
    la, lc = LAT[lat]; t_stop = fin - T_STOP; t_nopl = fin - T_NOPLACE
    out = []; live = None; next_ok = -1; prev = None; inv_since = None; closed = False
    def terminar(t_c, motivo):
        nonlocal live, closed
        o = live; o['t_c'] = t_c; o['t_fuera'] = t_c + lc; o['motivo'] = motivo; o['fill_t'] = None
        if close == 'any':
            g = first_golpe(ht, hp, o['t_ini'], o['t_fuera'], o['L'])
            if g is not None and g >= o['t_ini']: o['fill_t'] = g; o['t_fuera'] = g; closed = True
        out.append(o); live = None
    for i in range(i0, len(qt)):
        to = int(qt[i] + dobs(qt[i])); bid, ask = v0[i], v1[i]
        if live is None and prev is not None and prev[1] is not None and prev[0] < next_ok <= to and next_ok < t_nopl and next_ok < t_stop:
            live = dict(L=prev[1], t_dec=next_ok, t_ini=next_ok + la)
        if live is not None and inv_since is not None and to >= inv_since + REQ_INV and inv_since + REQ_INV < t_stop:
            tc = inv_since + REQ_INV; terminar(tc, 'invalido'); inv_since = None; next_ok = tc + ASENTAR + LOOP
            if closed: break
        if to >= t_stop: break
        tg = obj(bid, ask, kk)
        if live is not None:
            if not valido(bid, ask):
                inv_since = inv_since if inv_since is not None else to
            else:
                inv_since = None
                if tg is None or abs(tg - live['L']) > 1e-9:
                    tc = max(to, live['t_dec'] + MIN_ACC); terminar(tc, 'repega' if tg is not None else 'banda'); next_ok = tc + ASENTAR + LOOP
                    if closed: break
        if live is None and not closed and tg is not None and to >= next_ok and to < t_nopl:
            live = dict(L=tg, t_dec=to, t_ini=to + la); inv_since = None
        prev = (to, tg)
    if live is not None and not closed:
        terminar(min(max(t_stop, live['t_dec'] + MIN_ACC), fin), 't_stop')
    return out
rows_ev, rows_ord = [], []
mids = {}
for k in range(len(D.toks)):
    if D.marco[k] == '5min' and D.act[k] in K: mids.setdefault(D.mid[k], {})[D.lado[k]] = k
nB = nV = 0
for mid, sides in mids.items():
    if 'YES' not in sides or 'NO' not in sides: continue
    kY, kN = sides['YES'], sides['NO']; coin = D.act[kY]; kk = K[coin]; fin = int(D.fin[kY]) * 1000
    if fin - T_INI < d0 - 300000 or fin > d0 + 86400000 + 300000: continue
    conB = str(D.toks[kY]) in BTOK or str(D.toks[kN]) in BTOK
    Q = {s: quotes(k) for s, k in (('YES', kY), ('NO', kN))}
    # cara: primera (en tiempo de observacion) con bid en rejilla y en banda desde T=298; empate -> YES (orden de elegir_cara)
    t_start = fin - T_INI; best = None
    for s in ('YES', 'NO'):
        qt, v0, v1, _ = Q[s]
        if not len(qt): continue
        j0 = max(0, np.searchsorted(qt, t_start, side='right') - 1)
        for i in range(j0, len(qt)):
            to = max(int(qt[i] + dobs(qt[i])), t_start)
            if to >= fin - T_NOPLACE: break
            if obj(v0[i], v1[i], kk) is not None:
                if best is None or to < best[0]: best = (to, s, i)
                break
    if best is None: continue
    s = best[1]; kf = sides[s]; qt, v0, v1, v2 = Q[s]; i0 = best[2]; ht, hp = golpes(kf)
    if qt[i0] < t_start: qt = qt.copy(); qt[i0] = t_start - int(dobs(t_start))      # estado vigente al abrir la puja: decide en T=298
    for lat, close in VARS:
        ords = maquina(kf, kk, fin, qt, v0, v1, i0, ht, hp, lat, close)
        var = f'{lat}_{close}'
        for no, o in enumerate(ords):
            L = o['L']; a = np.searchsorted(qt, o['t_ini'], side='left'); b = np.searchsorted(qt, o['t_fuera'], side='right')
            rows_ord.append(dict(dia=d, mid=mid, coin=coin, k=kf, lado=s, fin=fin // 1000, conB=conB, var=var, n=no, **{x: o[x] for x in ('L', 't_dec', 't_ini', 't_c', 't_fuera', 'fill_t', 'motivo')}))
            for jj in range(max(a, i0 + 1), b):
                p0, p1 = v0[jj - 1], v0[jj]
                if not (np.isfinite(p0) and p0 > L + 0.005): continue
                if np.isfinite(p1) and p1 > 0 and p1 > L + 0.0049: continue
                t = int(qt[jj])
                if o['fill_t'] is not None and t >= o['fill_t']: continue
                g = first_golpe(ht, hp, t, t + 3000, L); dt = float(g - t) if g is not None else np.inf
                otros = float(v2[jj]) if (np.isfinite(p1) and abs(p1 - L) < 0.0049) else 0.0
                rows_ev.append(dict(dia=d, mid=mid, coin=coin, k=kf, fin=fin // 1000, conB=conB, var=var, n=no, t=t, T=(fin - t) / 1000.0, L=L,
                                    p_prev=float(p0), p_new=(float(p1) if np.isfinite(p1) else np.nan), otros_L=otros, size_b=tamano_orden(L, 5, 1.0),
                                    suelo=clase_t(t), dt=dt, hora=int(((t - d0) // 3600000) % 24)))
    nB += conB; nV += (not conB)
EV = pd.DataFrame(rows_ev); OR = pd.DataFrame(rows_ord)
EV.to_pickle(H + f'A_ev_{d}.pkl'); OR.to_pickle(H + f'A_ord_{d}.pkl')
# ---- fidelidad en mercados conB: ordenes virtuales (pl_any) vs ordenes reales del ledger (t_dec LOC s -> ms; precio)
fid = dict(dia=d, mercados_conB=int(nB), mercados_sinB=int(nV), clases_suelo={c: CL.count(c) for c in ('lo', 'hi', 'indet')})
Od = O[O.dia == d].copy()
if len(Od) and len(OR):
    V = OR[(OR.conB) & (OR['var'] == 'pl_any')]
    tokk = {str(D.toks[k]): k for k in set(V.k)}
    Od['k'] = Od.tok.map(lambda x: D.tokidx.get(str(x)))
    caras_reales = Od.groupby('puja').k.first(); caras_v = set(V.k)
    fid['pujas_reales'] = int(len(caras_reales)); fid['pujas_con_cara_virtual_igual'] = int(caras_reales.isin(caras_v).sum())
    m = 0; dts = []
    for r in Od.itertuples():
        if r.k is None or (isinstance(r.k, float) and np.isnan(r.k)): continue
        c = V[(V.k == int(r.k)) & (np.abs(V.L - r.precio) < 0.005)]
        if len(c):
            x = np.abs(c.t_dec.values - r.t_dec * 1000); dts.append(float(x.min())); m += int(x.min() <= 500)
    fid['ordenes_reales'] = int(len(Od)); fid['reales_con_virtual_mismoL_500ms'] = m
    fid['dt_dec_min_p50_ms'] = float(np.median(dts)) if dts else None
    fid['ordenes_virtuales_conB'] = int(len(V))
# ---- control de reproduccion del golpe de f3: recalcula dt del brazo B de fn_16nov/eventos_D.pkl con golpes()/first_golpe() de aqui
fe = H + '../fn_16nov/' + f'eventos_{d}.pkl'
if os.path.exists(fe):
    EB = pd.read_pickle(fe); EB = EB[EB.brazo == 'B']; cache = {}; ok = n = 0
    for r in EB.itertuples():
        if r.k not in cache: cache[r.k] = golpes(r.k)
        g = first_golpe(*cache[r.k], r.t, r.t + 3000, r.P); dt = float(g - r.t) if g is not None else np.inf
        n += 1; ok += int((dt == r.dt) or (not np.isfinite(dt) and (not np.isfinite(r.dt) or r.dt > 3000)) or (np.isfinite(dt) and dt <= 3000 and abs(dt - r.dt) < 1e-6))
    fid['repro_dt_f3_brazoB'] = dict(n=n, iguales=ok)
# ---- Tarea B: alinear las ordenes tomadoras de las wallets W de este dia (b1_ordenes.pkl) con la cinta WS y el libro ms del token MAKER de la 1a pata
fo = H + 'b1_ordenes.pkl'
if os.path.exists(fo):
    OD = pd.read_pickle(fo); OD = OD[OD.dia == d]; rt = []
    for r in OD.itertuples():
        k = D.tokidx.get(str(r.tok_m0))
        if k is None: rt.append(dict(tx=r.tx, wallet=r.wallet, al='sin_token')); continue
        t1 = int(r.ts * 1000) + 500; t0_ = t1 - 8500; tc = []
        for kq, pq in ((k, r.p_m0), (D.tokidx.get(str(r.tokX)), (1 - r.p_m0) if str(r.tokX) != str(r.tok_m0) else r.p_m0)):
            if kq is None: continue
            a, b = D.tb[kq], D.tb[kq + 1]; tt = D.tt[a:b]
            i0 = np.searchsorted(tt, t0_, side='left'); i1 = np.searchsorted(tt, t1, side='right')
            pr = D.tp[a + i0:a + i1].astype(float); sz = D.tsz[a + i0:a + i1].astype(float)
            c = np.where((np.abs(pr - pq) < 0.0051) & (np.abs(sz - r.sh_m0) <= 0.01 + 1e-3 * r.sh_m0))[0]
            tc += list(tt[i0 + c].astype(np.int64))
        if not len(tc): rt.append(dict(tx=r.tx, wallet=r.wallet, al='sin_print')); continue
        tc = np.array(tc); tp_ = int(tc[np.argmin(np.abs(tc - (int(r.ts * 1000) - 2400)))])
        qa, qb_ = D.qb[k], D.qb[k + 1]; qt = D.qt[qa:qb_].astype(np.int64); j = np.searchsorted(qt, tp_ - 1, side='right') - 1
        if j < 0: rt.append(dict(tx=r.tx, wallet=r.wallet, al='sin_libro')); continue
        lado_v = D.v0 if r.side_m0 == 0 else D.v1; lado_s = D.v2 if r.side_m0 == 0 else D.v3
        top = round(float(lado_v[qa + j]), 4); tsz = float(lado_s[qa + j])
        jj = j
        while jj > 0 and abs(float(lado_v[qa + jj - 1]) - top) < 0.0049: jj -= 1
        prev = float(lado_v[qa + jj - 1]) if jj > 0 else np.nan
        mejor_vs_top_c = round((top - r.p_m0) * 100 if r.side_m0 == 0 else (r.p_m0 - top) * 100, 2)   # >0: la 1a pata esta PEOR que el tope visto (mas profunda)
        cayo = bool(np.isfinite(prev) and ((prev > top + 0.0049) if r.side_m0 == 0 else (prev < top - 0.0049)))
        rt.append(dict(tx=r.tx, wallet=r.wallet, al='ok', t_print=tp_, d_bloque_ms=int(r.ts * 1000) - tp_, top=top, top_sz=tsz, mejor_vs_top_c=mejor_vs_top_c,
                       edad_top_ms=int(tp_ - qt[jj]), top_por_caida=cayo, sh_vs_topsz=(r.sh / tsz if tsz > 0 else np.nan)))
    pd.DataFrame(rt).to_pickle(H + f'B_al_{d}.pkl'); fid['tareaB_alineadas'] = int(sum(1 for x in rt if x.get('al') == 'ok')); fid['tareaB_ordenes'] = len(rt)
json.dump(fid, open(H + f'A_fid_{d}.json', 'w'), indent=1, default=str); print(json.dumps(fid, default=str))
print('eventos', len(EV), EV.groupby(['conB', 'var']).size().to_dict() if len(EV) else {}, flush=True)
