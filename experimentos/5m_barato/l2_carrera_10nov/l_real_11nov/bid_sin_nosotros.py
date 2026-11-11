#!/usr/bin/env python3
"""bid_sin_nosotros.py -- como se ve el libro PUBLICO con NUESTRA orden dentro y regla causal bid_otros_rx = bid - nuestra cantidad viva en L. SOLO LECTURA (0 ordenes, 0 red).
Datos: B real 20-23 Oct (ordenes_b.csv; `t_call0` envio LOC, `post_ms` RTT del POST => la orden estaba YA ACEPTADA antes de `t_call0+post_ms`; `t_cancel_int` envio del DELETE; `t_fuera` retorno del DELETE =>
la orden YA NO esta tras `t_fuera`) cruzado con filas q (top del libro: ex, bid, ask, szb, sza, rx) de m5_registro (mismo reloj que usa el motor). Cache de filas q en datalogs (fuera de git).
REGLA (causal, feed + estado propio):   para un mensaje q (rx, ex, bid, szb) y nuestra orden viva en nivel L con cantidad restante r (r = size - size_matched):
   estado 'incluida'  <=> ex_msg > t_ack_loc + 5 ms (el exchange ya la habia aceptado antes de ese mensaje; 5 ms = incertidumbre de reloj, CAUSA_SUELO 2.2) Y ex_msg < t_cancel_send + 30 ms (antes de la salida efectiva mas rapida medida, p10 derivado 34 ms).
   bid_otros(msg) = bid si bid > L (nada nuestro por encima) ; (L, szb - r) si bid == L y 'incluida' ; bid si bid == L y NO incluida (ventana ambigua: no disparar con szb) ; bid < L con la orden 'incluida' => mensaje INVALIDO (fail-closed: no disparar, contar).
   DISPARO CXB: 'bid_otros < L' <=> (bid < L sin orden propia) O (bid == L, 'incluida' y szb - r <= 0,011).
Validaciones (solo ordenes SIN relleno, acc_llena == 0, para no necesitar la hora del relleno): (V1) inclusion: en la ventana cierta no hay filas bid < L ni szb < r - 0,011 ; (V2) estado al cancelar -> primera fila tras `t_fuera`
(bid<L si el disparo valia; szb baja en r si habia otros); (V3) la regla ingenua sobre el feed crudo (bid<L) NUNCA dispara con la orden dentro (recall 0 por construccion).
Salida: out/bid_sin_nosotros.json + stdout. nice 19, ulimit 2 GB."""
import os, sys, json, subprocess
import numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = H + 'out/'; os.makedirs(OUT, exist_ok=True)
CACHE = '/root/polymarket-research-datalogs/l_real_11nov/cacheq/'; os.makedirs(CACHE, exist_ok=True)
DL = '/root/polymarket-research-datalogs/'; EPS = 0.011; T_CLK = 5; T_EFF_MIN = 30
DIAS = ['2026-10-20', '2026-10-21', '2026-10-22', '2026-10-23']


def extrae(d, toks):
    f = CACHE + f'bq_{d}.csv'
    if os.path.exists(f): return f
    tf = CACHE + f'tok_{d}.txt'; open(tf, 'w').write('\n'.join(sorted(toks)) + '\n')
    cmd = f"zcat /mnt/HC_Volume_106538179/m5_registro/m5_registro_{d}.csv.gz | awk -F, -v tf={tf} 'BEGIN{{while((getline l<tf)>0)t[l]}} $1==\"q\"&&($3 in t)' > {f}.tmp && mv {f}.tmp {f}"
    subprocess.run(['nice', '-n', '19', 'ionice', '-c3', 'bash', '-c', 'ulimit -v 2000000; ' + cmd], check=True); return f


def carga_q(f):
    Q = pd.read_csv(f, header=None, names=['tipo', 'ex', 'tok', 'bid', 'ask', 'szb', 'sza', 'rx'], dtype=str, na_values=['None', ''])
    Q = Q[Q.tipo == 'q'].dropna(subset=['ex', 'rx']).copy(); Q['ex'] = Q.ex.astype('int64'); Q['rx'] = Q.rx.astype('int64')
    for c in ('bid', 'ask', 'szb', 'sza'): Q[c] = pd.to_numeric(Q[c], errors='coerce')
    return {t: g.sort_values(['rx', 'ex']).reset_index(drop=True) for t, g in Q.groupby('tok')}


def bid_otros(bid, szb, ex_ms, L, r, t_ack_ms, t_cancel_ms):
    """Regla causal (funcion pura, la usa el dry-run/ejecutor). Devuelve (estado, bid_otros_precio, size_otros) con estado in {'sin_orden','incluida','ambigua','invalido'}.
    Si la orden propia esta incluida y bid==L: otros = szb - r (<=EPS => 'otros por debajo de L': precio None)."""
    if not (np.isfinite(bid) and np.isfinite(szb)): return 'invalido', None, None
    if bid > L + 1e-9: return 'sin_orden', bid, szb                                  # nada nuestro por encima del mejor bid
    inc = (ex_ms > t_ack_ms + T_CLK) and (t_cancel_ms is None or ex_ms < t_cancel_ms + T_EFF_MIN)
    if bid < L - 1e-9: return ('invalido', None, None) if inc else ('sin_orden', bid, szb)       # con la orden dentro el mejor bid visible nunca esta por debajo de L
    if not inc:
        amb = (ex_ms >= t_ack_ms - 0) and not (t_cancel_ms is not None and ex_ms >= t_cancel_ms + 200)   # entre envio-aceptacion y salida: no sabemos si incluye nuestra cantidad
        return ('ambigua' if amb else 'sin_orden'), bid, szb
    so = szb - r
    if so < -EPS: return 'invalido', None, None                                       # szb menor que nuestra cantidad: la orden NO esta en el feed (o r mal)
    return 'incluida', (None if so <= EPS else bid), max(so, 0.0)


def main():
    O = pd.read_csv(DL + 'calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str}); O = O[O.acc_llena == 0].copy()
    S = dict(n_ordenes_sin_relleno=int(len(O)), filas_ventana_cierta=0, filas_bid_menor_L=0, filas_szb_menor_r=0, filas_bid_igual_L=0, filas_disparo=0, ordenes_con_disparo=0,
             estado_final=dict(n=0, fire=0, fire_bid_below_after=0, fire_other=0, nofire_others=0, nofire_szb_drop_exact=0, nofire_bid_above=0, nofire_bid_above_stays=0), detalle=[])
    ordenes_usadas = 0
    for d in DIAS:
        g = O[O.dia == d]
        Qd = carga_q(extrae(d, set(g.tok)))
        for r in g.itertuples():
            q = Qd.get(r.tok)
            if q is None: continue
            L = r.precio; size = r.size; t_ack = int((r.t_call0 + r.post_ms / 1000.0) * 1000)
            tcs = r.t_cancel_int if r.t_cancel_int == r.t_cancel_int else None
            if tcs is None or r.t_fuera != r.t_fuera: continue
            tcs = int(tcs * 1000); tfu = int(r.t_fuera * 1000)
            w = q[(q.ex > t_ack + T_CLK) & (q.ex < tcs + T_EFF_MIN)]
            if len(w) == 0: continue
            ordenes_usadas += 1; S['filas_ventana_cierta'] += len(w)
            S['filas_bid_menor_L'] += int((w.bid < L - 1e-9).sum()); top = w[(w.bid - L).abs() < 1e-9]; S['filas_bid_igual_L'] += len(top); S['filas_szb_menor_r'] += int((top.szb < size - EPS).sum())
            fire = top[(top.szb - size) <= EPS]; S['filas_disparo'] += len(fire); S['ordenes_con_disparo'] += int(len(fire) > 0)
            # estado al cancelar: ultima fila con ex <= tcs + T_EFF_MIN dentro de la ventana, y primera fila despues del retorno del DELETE (orden ya fuera, cierto)
            pre = w.iloc[-1]; post = q[q.ex > tfu + T_CLK]
            if len(post) == 0 or (post.ex.iloc[0] - tfu) > 3000: continue
            post = post.iloc[0]; E = S['estado_final']; E['n'] += 1
            if abs(pre.bid - L) < 1e-9:
                if pre.szb - size <= EPS:
                    E['fire'] += 1
                    if post.bid < L - 1e-9: E['fire_bid_below_after'] += 1
                    else: E['fire_other'] += 1; S['detalle'].append(dict(oid=r.oid[:10], L=L, pre=(float(pre.bid), float(pre.szb)), post=(float(post.bid), float(post.szb)), dt_post_ms=int(post.ex - tfu)))
                else:
                    E['nofire_others'] += 1
                    if abs(post.bid - L) < 1e-9 and abs((pre.szb - post.szb) - size) <= EPS: E['nofire_szb_drop_exact'] += 1
            elif pre.bid > L:
                E['nofire_bid_above'] += 1; E['nofire_bid_above_stays'] += int(post.bid > L - 1e-9)
    S['ordenes_usadas'] = ordenes_usadas
    # V3: regla ingenua (bid<L en el feed crudo) con la orden dentro: filas de disparo reales de la regla propia que la ingenua NO ve
    S['ingenua_dispara_con_orden_dentro'] = S['filas_bid_menor_L']
    json.dump(S, open(OUT + 'bid_sin_nosotros.json', 'w'), indent=1)
    E = S['estado_final']
    print({k: v for k, v in S.items() if k not in ('detalle', 'estado_final')}); print(E)
    if E['fire']: print('PRECISION de la regla en el estado al cancelar: P(bid<L tras la salida | regla dice otros<L) = %d/%d = %.3f' % (E['fire_bid_below_after'], E['fire'], E['fire_bid_below_after'] / E['fire']))
    if E['nofire_others']: print('con otros presentes (szb-r>0): tras la salida szb baja EXACTAMENTE r en %d/%d = %.3f' % (E['nofire_szb_drop_exact'], E['nofire_others'], E['nofire_szb_drop_exact'] / E['nofire_others']))
    for x in S['detalle'][:15]: print('  fire sin bid<L tras salida:', x)


if __name__ == '__main__': main()
