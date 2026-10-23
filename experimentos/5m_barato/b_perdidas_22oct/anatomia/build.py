#!/usr/bin/env python3
"""build.py -- dataset de anatomia de perdidas de B (H47-B real). SOLO LECTURA de produccion.
Unidad = posicion (mercado, lado) de posiciones.csv (tanda_B no vacia; PnL on-chain). Rasgos del ledger
experimento_h47_B_ledger.jsonl (puja_post / puja_fin / mercado_fin.trades_propios) + Chainlink RTDS (chainlink_D.csv,
source=chainlink, hora de RECEPCION para rasgos previos) + twap60 oficial polybolt (refs) + Binance bookTicker (datalogs).
Tambien escribe las pujas NO rellenadas con desenlace (placebo/contrafactico). Salida: pos.csv, pujas.csv en este dir."""
import json, csv, os, sys, bisect, datetime as dt, collections
import numpy as np, pandas as pd, requests
OUT = os.path.dirname(os.path.abspath(__file__))
R = '/root/polymarket-research'; DL = '/root/polymarket-research-datalogs'
LED = DL + '/experimento_h47_B_ledger.jsonl'
DIAS = ['2026-10-20', '2026-10-21', '2026-10-22']
COINS = ['BTC', 'ETH', 'SOL', 'XRP']
# ---------- ledger
first, fin, mfin = {}, {}, {}
for l in open(LED):
    try: r = json.loads(l)
    except Exception: continue
    if not r.get('real'): continue
    t = r.get('tipo')
    if t == 'puja_post' and r.get('escalon') == 'B': first.setdefault((r['slug'], r['lado']), r)
    elif t == 'puja_fin' and r.get('escalon') == 'B': fin[(r['slug'], r['lado'])] = r
    elif t == 'mercado_fin' and r.get('escalon') == 'B': mfin[r['slug']] = r
# ---------- desenlaces (copia local de la cache de b_postmortem + gamma read-only para lo que falte)
CL = OUT + '/des_cache.json'
des = json.load(open(CL)) if os.path.exists(CL) else {}
src = R + '/experimentos/5m_barato/b_seleccion_adversa/datos/b_des_cache.json'
if os.path.exists(src):
    for k, v in json.load(open(src)).items(): des.setdefault(k, v)
falta = sorted({k[0] for k in fin} - {k for k, v in des.items() if v})
ses = requests.Session()
for i in range(0, len(falta), 40):
    try:
        rs = ses.get('https://gamma-api.polymarket.com/markets', timeout=25, params=[('slug', s) for s in falta[i:i+40]] + [('closed', 'true'), ('limit', '40')]).json()
    except Exception as e:
        print('gamma', e, file=sys.stderr); continue
    for m in rs:
        pr = m.get('outcomePrices'); pr = json.loads(pr) if isinstance(pr, str) else pr
        if m.get('closed') and pr: des[m['slug']] = 'YES' if float(pr[0]) >= .999 else ('NO' if float(pr[1]) >= .999 else None)
json.dump(des, open(CL, 'w'))
# ---------- precios
def load_cl():
    d = {c: ([], [], []) for c in COINS}
    for D in DIAS:
        with open(f'{R}/data/prices/chainlink_{D}.csv') as f:
            rd = csv.reader(f); next(rd)
            for ts, a, p, wms, s in rd:
                if s != 'chainlink' or a not in d: continue
                rx = dt.datetime.fromisoformat(ts).timestamp()
                d[a][0].append(rx); d[a][1].append(int(wms) / 1000); d[a][2].append(float(p))
    o = {}
    for a, (rx, ws, p) in d.items():
        rx, ws, p = map(np.array, (rx, ws, p)); i = np.argsort(rx, kind='stable'); j = np.argsort(ws, kind='stable')
        o[a] = dict(rx=rx[i], prx=p[i], ws=ws[j], pws=p[j])
    return o
def load_twap():
    d = collections.defaultdict(dict)
    for D in DIAS:
        with open(f'{R}/data/prices/polybolt_{D}.csv') as f:
            rd = csv.reader(f); next(rd)
            for ts, a, can, v, ems, sn, s in rd:
                if can != 'twap60' or s != 'chainlink' or a not in COINS: continue
                d[a][int(ems) // 1000] = float(v)
    return d
BADBN = [0]
def load_bn():
    d = {c: ([], []) for c in COINS}
    for D in DIAS:
        with open(f'{DL}/binance_bookticker_{D}.csv') as f:
            rd = csv.reader(f); next(rd)
            for row in rd:
                try:
                    if row[1] in d: t_ = int(row[0]) / 1000; p_ = float(row[4]); d[row[1]][0].append(t_); d[row[1]][1].append(p_)
                except (ValueError, IndexError): BADBN[0] += 1
    o = {}
    for a, (t, p) in d.items():
        t, p = np.array(t), np.array(p); i = np.argsort(t, kind='stable'); o[a] = (t[i], p[i])
    return o
CLD = load_cl(); TW = load_twap(); BN = load_bn()
print('filas bookTicker corruptas', BADBN[0], file=sys.stderr); print('precios cargados', {a: len(CLD[a]['rx']) for a in COINS}, {a: len(BN[a][0]) for a in COINS}, file=sys.stderr)
def at(t_arr, p_arr, t):  # ultimo valor con t_arr <= t
    i = np.searchsorted(t_arr, t, side='right') - 1
    return float(p_arr[i]) if i >= 0 and t - t_arr[i] < 30 else np.nan
def cl_rx(a, t): return at(CLD[a]['rx'], CLD[a]['prx'], t)
def cl_ws(a, t): return at(CLD[a]['ws'], CLD[a]['pws'], t)
def bn(a, t): return at(BN[a][0], BN[a][1], t)
def tw(a, e):
    for k in (0, -1, 1, -2, 2):
        if e + k in TW[a]: return TW[a][e + k]
    return np.nan
def sig(lado): return 1.0 if lado == 'YES' else -1.0
def bps(x, y): return (y / x - 1) * 1e4 if x and y and x == x and y == y else np.nan
def feats(slug, lado, coin, tf):
    """rasgos de precio en el instante tf (hora de relleno). Signo + = a favor de nuestro lado."""
    st = int(slug.rsplit('-', 1)[1]); A = coin.upper(); s = sig(lado)
    ref = tw(A, st); refc = tw(A, st + 300)
    o = dict(ref_open=ref, ref_close=refc, up_wins_twap=(np.nan if ref != ref or refc != refc else float(refc >= ref)))
    sp = cl_rx(A, tf)
    o['dist_ref_bps'] = s * bps(ref, sp)                      # posicion del spot vs ref de apertura (recepcion, observable)
    o['mov_pre30_cl'] = s * bps(cl_rx(A, tf - 30), sp)        # movimiento 30 s antes del relleno
    o['mov_pre10_cl'] = s * bps(cl_rx(A, tf - 10), sp)
    o['mov_post10_cl'] = s * bps(cl_ws(A, tf), cl_ws(A, tf + 10))   # POST-relleno (no accionable, descriptivo)
    o['mov_post30_cl'] = s * bps(cl_ws(A, tf), cl_ws(A, tf + 30))
    o['mov_post_cierre_cl'] = s * bps(cl_ws(A, tf), refc)     # spot al relleno -> twap de cierre
    o['bn_pre30'] = s * bps(bn(A, tf - 30), bn(A, tf)); o['bn_pre5'] = s * bps(bn(A, tf - 5), bn(A, tf))
    o['bn_post5'] = s * bps(bn(A, tf), bn(A, tf + 5)); o['bn_post30'] = s * bps(bn(A, tf), bn(A, tf + 30))
    o['btc_pre30'] = s * bps(bn('BTC', tf - 30), bn('BTC', tf)); o['btc_post30'] = s * bps(bn('BTC', tf), bn('BTC', tf + 30))
    o['btc_post_cierre'] = s * bps(cl_ws('BTC', tf), cl_ws('BTC', st + 300))
    # volatilidad realizada 60 s previa (bps, desv. de retornos 1 s en recepcion)
    t0 = np.searchsorted(CLD[A]['rx'], tf - 60); t1 = np.searchsorted(CLD[A]['rx'], tf)
    pp = CLD[A]['prx'][t0:t1]
    o['vol60_bps'] = float(np.std(np.diff(np.log(pp))) * 1e4 * np.sqrt(60)) if len(pp) > 10 else np.nan
    return o
# ---------- posiciones
P = pd.read_csv(R + '/experimentos/5m_barato/contabilidad_wallet_dedicada/posiciones.csv', dtype=str)
P = P[P.tanda_B.notna() & (P.tanda_B != '')].copy()
rows = []
for _, p in P.iterrows():
    lado = 'YES' if p.outcome == 'Up' else 'NO'; slug = p.mercado; st = int(slug.rsplit('-', 1)[1]); coin = slug.split('-')[0]
    pf = fin.get((slug, lado)); pp = first.get((slug, lado), {}); mf = mfin.get(slug, {})
    tp = ((mf.get('trades_propios') or {}).get(lado)) or []
    tms = [int(x['match_time']) for x in tp if x.get('match_time')]
    rl = (pf or {}).get('rellenos') or []
    tdet = [x['t_deteccion'] for x in rl if x.get('t_deteccion')]
    tf = min(tdet) if tdet else (min(tms) if tms else dt.datetime.fromisoformat(p.fecha_primer_fill_utc.replace('Z', '+00:00')).timestamp())
    src_t = 'ledger_det' if tdet else ('trades_propios' if tms else 'onchain_bloque')
    r0 = rl[0] if rl else {}
    lib = (pp.get('libro') or {}); bids = lib.get('bids') or [[np.nan, np.nan]]; asks = lib.get('asks') or [[np.nan, np.nan]]
    d = dict(slug=slug, coin=coin.upper(), lado=lado, outcome=p.outcome, tanda=int(p.tanda_B), acc=float(p.acciones), coste=float(p.coste), precio=float(p.precio_medio),
             pnl=float(p.pnl_realizado), estado=p.estado, gana=float(p.estado == 'liquidada_ganada'), n_filas_onchain=int(p.n_filas),
             t_fill=tf, src_t=src_t, T_rest=st + 300 - tf, t_desde_open=tf - st, fin=st + 300, hora=int(dt.datetime.utcfromtimestamp(tf).hour),
             dia=dt.datetime.utcfromtimestamp(tf).strftime('%Y-%m-%d'), en_ledger=pf is not None,
             n_ordenes=(pf or {}).get('n_ordenes', np.nan), fin_puja=(pf or {}).get('fin_puja'), tardio=bool((pf or {}).get('rellenos_tardios')),
             tras_cancel=r0.get('tras_cancel'), espera_s=r0.get('espera_s', np.nan), cola_fill=r0.get('cola', np.nan), mid0=r0.get('mid0', np.nan),
             mo5=r0.get('markout_5s', np.nan), mo30=r0.get('markout_30s', np.nan), mo120=r0.get('markout_120s', np.nan),
             p_post=pp.get('precio', np.nan), T_post=pp.get('T', np.nan), cola_post=pp.get('cola', np.nan), spread_post=asks[0][0] - bids[0][0], bidsz_post=bids[0][1],
             des_gamma=des.get(slug))
    d.update(feats(slug, lado, coin, tf)); rows.append(d)
D = pd.DataFrame(rows).sort_values('t_fill'); D.to_csv(OUT + '/pos.csv', index=False)
# ---------- pujas (todas, rellenas o no) con desenlace
pr = []
for (slug, lado), f in fin.items():
    st = int(slug.rsplit('-', 1)[1]); pp = first.get((slug, lado), {}); d = des.get(slug)
    pr.append(dict(slug=slug, lado=lado, coin=f['coin'].upper(), relleno=bool(f.get('rellenos')) or bool(f.get('rellenos_tardios')), p_post=pp.get('precio', np.nan), T_post=pp.get('T', np.nan),
                   t_post=pp.get('t_dec', np.nan), hora=int(dt.datetime.utcfromtimestamp(st + 150).hour), dia=dt.datetime.utcfromtimestamp(st + 150).strftime('%Y-%m-%d'), fin=st + 300,
                   n_ordenes=f.get('n_ordenes'), fin_puja=f.get('fin_puja'), gana=(np.nan if not d else float(d == lado)),
                   **{k: v for k, v in feats(slug, lado, f['coin'], pp.get('t_dec', st + 5)).items() if k in ('dist_ref_bps', 'mov_pre30_cl', 'vol60_bps', 'bn_pre30', 'btc_pre30', 'up_wins_twap')}))
pd.DataFrame(pr).sort_values('fin').to_csv(OUT + '/pujas.csv', index=False)
print('pos', len(D), 'en_ledger', int(D.en_ledger.sum()), 'src_t', D.src_t.value_counts().to_dict(), 'pujas', len(pr), file=sys.stderr)
