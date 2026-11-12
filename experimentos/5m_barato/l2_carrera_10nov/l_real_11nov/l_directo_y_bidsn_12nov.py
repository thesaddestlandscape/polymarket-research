#!/usr/bin/env python3
"""l_directo_y_bidsn_12nov.py [--dias D1 D2 ..] [--max-ordenes N] -- C y E del paquete 12-Nov. SOLO LECTURA (0 ordenes, 0 red).
C  (l directo gratis): (1) INVENTARIO de anclas de canal de USUARIO (hora del exchange) en TODO el historico de cancel_evid (30-Oct..05-Nov: el canal solo registro eventos el 04-Nov);
   (2) anclas INDIRECTAS con el feed publico (RX, no hora de exchange) en B real 20-23 Oct (ordenes_b.csv + cache de filas q de los tokens de B): primera fila posterior al envio del DELETE donde la cantidad del bid en L baja
   EXACTAMENTE nuestra cantidad restante r (o el bid cae por debajo de L cuando solo estaba la nuestra), candidato UNICO en [t_envio-5 ms, t_fuera+300 ms] => rx_visto - t_envio_DELETE. l_estimado = ese valor - lag_feed (rx-ex de la fila, mediana;
   y con el lag del canal de usuario 17 ms) para comparar con RTT_DELETE-22,5. No son anclas del exchange: son una COTA (el feed publico llega ~17 ms tras el exchange).
E  («bid sin nosotros»): reproduce 454/522 y mide (a) donde estan los fallos (nuestra orden aun visible / llegan otros / otro), (b) precision con r = size - acc_llena en ordenes con relleno PARCIAL (relleno on-chain anterior al DELETE por ts_est),
   (c) precision por edad de la ultima fila y umbrales fijados a priori {100,300,1000} ms. Las reglas/umbrales son DIAGNOSTICO (no se ajusta ninguna regla con datos fuera de TRAIN)."""
import os, sys, json, glob, gzip, collections, argparse
import numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = H + 'out/'; DL = '/root/polymarket-research-datalogs/'; CACHE = DL + 'l_real_11nov/cacheq/'; EPS = 0.011; T_CLK = 5
RESCALE = 1792630711.0                                          # 2026-10-22T09:58:31Z
RNG = np.random.default_rng(20261112)


def pct(v):
    v = np.asarray([x for x in v if x is not None and np.isfinite(x)], float)
    if len(v) == 0: return dict(n=0)
    r = dict(n=int(len(v)), p10=float(np.percentile(v, 10)), p50=float(np.median(v)), p90=float(np.percentile(v, 90)), min=float(v.min()), max=float(v.max()))
    if len(v) >= 5:
        s = v[RNG.integers(0, len(v), (2000, len(v)))]; r['p50_ic90'] = [float(np.percentile(np.median(s, 1), 5)), float(np.percentile(np.median(s, 1), 95))]
    return r


def inventario_usuario():
    inv = dict(ficheros={}, anclas_directas=dict(alta=0, cancelacion=0))
    for f in sorted(glob.glob(DL + 'sonda1/cancel_evid/cancel_evid_*.jsonl*')):
        op = gzip.open if f.endswith('.gz') else open; c = collections.Counter(); ult = {}
        for l in op(f, 'rt'):
            try: e = json.loads(l)
            except ValueError: continue
            k = e.get('k'); c[k + (':' + str(e.get('tipo')) if k == 'user_order' and e.get('mine') else '')] += 1
            if k == 'latido': ult = e
        inv['ficheros'][os.path.basename(f)] = dict(eventos=dict(c), ws_msgs_ultimo_latido=ult.get('ws_msgs'), ws_conex_ultimo_latido=ult.get('ws_conex'))
        inv['anclas_directas']['alta'] += c.get('user_order:PLACEMENT', 0); inv['anclas_directas']['cancelacion'] += c.get('user_order:CANCELLATION', 0)
    inv['nota'] = 'solo el 04-Nov tiene eventos de canal de usuario (ws_msgs>0): 9 PLACEMENT / 4 CANCELLATION propios; 03-Nov y 05-Nov: canal sin mensajes (sin ordenes). B (20-23 Oct) y Sonda 30-Oct..03-Nov anteceden al registro: no hay mas anclas de exchange gratis.'
    return inv


def carga_cache(d, toks):
    f = CACHE + f'bq_{d}.csv'
    Q = pd.read_csv(f, header=None, names=['tipo', 'ex', 'tok', 'bid', 'ask', 'szb', 'sza', 'rx'], dtype=str, na_values=['None', ''], usecols=[0, 1, 2, 3, 5, 7])
    Q = Q[Q.tipo == 'q'].dropna(subset=['ex', 'rx']); Q = Q[Q.tok.isin(toks)].copy()
    Q['ex'] = Q.ex.astype('int64'); Q['rx'] = Q.rx.astype('int64'); Q['bid'] = pd.to_numeric(Q.bid, errors='coerce'); Q['szb'] = pd.to_numeric(Q.szb, errors='coerce'); Q = Q.drop(columns=['tipo'])
    out = {}
    for t, g in Q.groupby('tok'):
        g = g.sort_values(['rx', 'ex'], kind='stable').drop_duplicates(['rx', 'ex', 'bid', 'szb']); out[t] = (g.rx.values, g.ex.values, g.bid.values, g.szb.values)
    del Q; return out


def fills_antes(O):
    """acc_llena por orden y, si existe, ts_est del ultimo fill on-chain (join por order_hash == oid). Devuelve dict oid -> ts_est_max o None."""
    f = DL + 'calibracion_etiqueta/b_fills_onchain.csv'; B = pd.read_csv(f); B = B[B.tipo == 'F']; B['order_hash'] = B.order_hash.astype(str)
    m = B.groupby('order_hash').ts_est.max().to_dict(); return {o: m.get(o) for o in O.oid}, int(O.oid.isin(set(B.order_hash)).sum())


def evalua(O, dia, Q, fts, st):
    """Por orden con DELETE conocido: (1) ancla rx de cancelacion visible; (2) estado de la regla 'bid sin nosotros' al cancelar y tras la salida."""
    A = []; R = []
    for r in O.itertuples():
        q = Q.get(r.tok)
        if q is None or r.t_cancel_int != r.t_cancel_int: st['sin_q_o_sin_delete'] += 1; continue
        rx, ex, bid, szb = q; L = float(r.precio); size = float(r.size); acc = float(r.acc_llena); parcial = 0 < acc < size - 1e-9
        tcs = int(r.t_cancel_int * 1000); tfu = int(r.t_fuera * 1000)
        if acc >= size - 1e-9: st['llena_entera_no_cancela'] += 1; continue
        if acc > 0:
            ft = fts.get(r.oid)
            if ft is None or ft != ft or ft > r.t_cancel_int: st['parcial_sin_hora_fill_anterior'] += 1; continue          # relleno posterior al DELETE o sin hora: r ambiguo -> fuera
            rr = size - acc; st['parcial_con_fill_anterior'] += 1
        else: rr = size
        i0 = int(np.searchsorted(rx, tcs - T_CLK, side='left')); i1 = int(np.searchsorted(rx, tfu + 300, side='right'))
        if i0 == 0 or i1 <= i0: st['sin_filas_ventana'] += 1; continue
        pb, ps = bid[i0 - 1], szb[i0 - 1]
        if not (np.isfinite(pb) and abs(pb - L) < 1e-9): st['no_top_en_L_al_cancelar'] += 1
        # ---- (1) ancla rx: filas consecutivas en la ventana; candidato = fila j cuyo paso desde la anterior (bid==L) baja szb exactamente rr, o bid<L con szb previo ~ rr
        cand = []
        for j in range(i0, i1):
            b0, s0, b1, s1 = bid[j - 1], szb[j - 1], bid[j], szb[j]
            if not (np.isfinite(b0) and abs(b0 - L) < 1e-9): continue
            if np.isfinite(b1) and abs(b1 - L) < 1e-9 and abs((s0 - s1) - rr) <= EPS: cand.append(j)
            elif np.isfinite(b1) and b1 < L - 1e-9 and abs(s0 - rr) <= EPS: cand.append(j)
        if len(cand) == 1 and tcs - T_CLK <= rx[cand[0]] <= tfu + 300:
            j = cand[0]; A.append(dict(oid=r.oid, dia=dia, epoca='pre' if r.t_call0 < RESCALE else 'post', rx_menos_envio=float(rx[j] - tcs), rx_menos_fuera=float(rx[j] - tfu), lag_fila=float(rx[j] - ex[j]), solo_nosotros=int(abs(s0 - rr) <= EPS), parcial=int(parcial)))
            st['ancla_unica'] += 1
        else: st['ancla_no_unica' if len(cand) > 1 else 'ancla_sin_candidato'] += 1
        # ---- (2) regla bid sin nosotros: estado 'incluida' en la ultima fila antes del cancelar (ex <= tcs+30) y estado tras la salida (primera fila con ex > tfu+T_CLK)
        t_ack = int((r.t_call0 + r.post_ms / 1000.0) * 1000); w = np.where((ex > t_ack + T_CLK) & (ex < tcs + 30))[0]
        if len(w) == 0: continue
        jp = w[np.argmax(rx[w])] if False else w[-1]; pre_b, pre_s, pre_rx = bid[jp], szb[jp], rx[jp]
        post_ix = np.where(ex > tfu + T_CLK)[0]
        if len(post_ix) == 0 or ex[post_ix[0]] - tfu > 3000: continue
        jq = post_ix[0]; post_b, post_s = bid[jq], szb[jq]; edad = float(tcs - pre_rx)
        fire = bool(np.isfinite(pre_b) and abs(pre_b - L) < 1e-9 and (pre_s - rr) <= EPS); R.append(dict(oid=r.oid, dia=dia, parcial=int(parcial), fire=fire, pre_s=float(pre_s), rr=rr, edad_ms=edad, bid_post_bajo=bool(post_b < L - 1e-9),
                                                                                         visible_aun=bool(abs(post_b - L) < 1e-9 and post_s >= pre_s - EPS), otros_llegan=bool(abs(post_b - L) < 1e-9 and post_s > (pre_s - rr) + EPS and post_s < pre_s - EPS) or bool(post_b > L + 1e-9), dt_post=int(ex[jq] - tfu),
                                                                                         bid_pre_top=bool(np.isfinite(pre_b) and abs(pre_b - L) < 1e-9)))
    return A, R


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--dias', nargs='*', default=['2026-10-20', '2026-10-21', '2026-10-22', '2026-10-23']); ap.add_argument('--max-ordenes', type=int, default=0); a = ap.parse_args(); os.makedirs(OUT, exist_ok=True)
    res = dict(inventario_usuario=inventario_usuario()); O = pd.read_csv(DL + 'calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str}); fts, n_join = fills_antes(O); res['join_fills_onchain'] = dict(ordenes=len(O), con_hash_en_b_fills=n_join)
    st = collections.Counter(); A = []; R = []
    for d in a.dias:
        g = O[O.dia == d]
        if a.max_ordenes: g = g.head(a.max_ordenes)
        Q = carga_cache(d, set(g.tok)); a_, r_ = evalua(g, d, Q, fts, st); A += a_; R += r_; del Q; print('dia', d, 'ordenes', len(g), 'anclas', len(a_), 'estados', len(r_), flush=True)
    A = pd.DataFrame(A); R = pd.DataFrame(R); res['contadores'] = dict(st)
    if len(A):
        res['ancla_rx_cancel_B'] = dict(todas=pct(A.rx_menos_envio), rx_menos_fuera=pct(A.rx_menos_fuera), lag_fila_rx_menos_ex=pct(A.lag_fila), pre_rescale=pct(A[A.epoca == 'pre'].rx_menos_envio), post_rescale=pct(A[A.epoca == 'post'].rx_menos_envio),
                                       solo_nosotros=pct(A[A.solo_nosotros == 1].rx_menos_envio), con_otros=pct(A[A.solo_nosotros == 0].rx_menos_envio), parciales=pct(A[A.parcial == 1].rx_menos_envio))
        lag17 = 17.0; res['l_estimado_desde_feed'] = dict(menos_lag_usuario_17ms=pct(A.rx_menos_envio - lag17), menos_lag_fila_mediana=pct(A.rx_menos_envio - float(A.lag_fila.median())), nota='cota: rx_publico - envio - lag; compara con RTT_DELETE-22,5 (p50 64-22,5=41,5 en B post-Rescale)')
    if len(R):
        F = R[R.fire]; n = len(F); res['bid_sin_nosotros'] = dict(estados=len(R), fire=n, precision_bid_post_bajo=int(F.bid_post_bajo.sum()), precision=round(float(F.bid_post_bajo.mean()), 4) if n else None)
        fl = F[~F.bid_post_bajo]; res['bid_sin_nosotros']['fallos'] = dict(n=len(fl), nuestra_orden_aun_visible=int(fl.visible_aun.sum()), llegan_otros=int(fl.otros_llegan.sum()), otro=int(len(fl) - fl.visible_aun.sum() - fl.otros_llegan.sum()), dt_post_mediana=float(fl.dt_post.median()) if len(fl) else None)
        for nm, sub in (('sin_parcial', R[R.parcial == 0]), ('parcial_r_igual_size_menos_acc', R[R.parcial == 1])):
            f = sub[sub.fire]; res['bid_sin_nosotros'][nm] = dict(estados=len(sub), fire=len(f), precision=round(float(f.bid_post_bajo.mean()), 4) if len(f) else None, ic90_wilson=None)
            if len(f):
                p = f.bid_post_bajo.mean(); nn = len(f); z = 1.645; c = (p + z * z / (2 * nn)) / (1 + z * z / nn); h = z * np.sqrt(p * (1 - p) / nn + z * z / (4 * nn * nn)) / (1 + z * z / nn); res['bid_sin_nosotros'][nm]['ic90_wilson'] = [round(float(c - h), 3), round(float(c + h), 3)]
        res['bid_sin_nosotros']['por_edad_ultima_fila'] = {}
        for lim in (100, 300, 1000, 10 ** 9):                      # umbrales fijados a priori; edad = t_envio_DELETE - rx de la ultima fila antes del cancelar
            f = F[F.edad_ms <= lim]; res['bid_sin_nosotros']['por_edad_ultima_fila'][str(lim)] = dict(fire=len(f), precision=round(float(f.bid_post_bajo.mean()), 4) if len(f) else None, cobertura_de_fire=round(len(f) / max(n, 1), 3))
        res['bid_sin_nosotros']['por_L_bandas'] = 'ver ordenes_b.csv (no desagregado aqui: n por banda <40 con fire)'
    json.dump(res, open(OUT + 'l_directo_y_bidsn_12nov.json', 'w'), indent=1, default=str)
    if len(A): A.to_csv(OUT + 'anclas_rx_cancel_B.csv', index=False)
    print(json.dumps({k: v for k, v in res.items() if k != 'inventario_usuario'}, indent=1, default=str)[:6000]); print(json.dumps(res['inventario_usuario'], indent=1)[:1800])


if __name__ == '__main__': main()
