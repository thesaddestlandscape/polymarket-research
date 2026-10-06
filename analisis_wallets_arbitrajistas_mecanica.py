#!/usr/bin/env python3
"""analisis_wallets_arbitrajistas_mecanica.py -- B2 paso 1 (cont.): mecánica de las wallets sobre el pickle de
analisis_wallets_arbitrajistas_forense.py.

Unidad = ORDEN TOMADORA de la wallet (fila on-chain tipo M: OrdersMatched; maker = dueño de la orden tomadora). Se
empareja con la operación del WS del CLOB (registro ms) del mismo token y tamaño total en [bloque-4 s, bloque] ->
hora del EXCHANGE en ms (OBSERVADO si el emparejamiento es único).
Para cada orden emparejada:
  t_aparece = primer cambio del top (hora del exchange) desde el que el mejor ask ya era <= precio de la orden, sin
    interrupción hasta el relleno; Δ = t_relleno - t_aparece. Δ < 150 ms con el retraso de tomador del exchange =>
    la orden se ENVIÓ antes de que el nivel fuese visible (COMPATIBLE con orden en vuelo; no demuestra el motivo).
  Línea base: el mismo Δ para TODAS las demás operaciones de compra de esos tokens.
Estructura: por mercado, acciones YES y NO compradas, precio medio, coste del conjunto completo con comisión y
desenlace oficial -> PnL "garantizado" (min(YES,NO) acciones) y "direccional" (el exceso de un lado), por separado.
Uso: --pkl <forense.pkl>
"""
import argparse
import bisect
import collections
import pickle
import statistics as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

EX = "0xe111180000d2663c0091e4f400237545b87b996b"


def fee(p):
    return 0.07 * p * (1 - p)


def ps(r):
    ma, ta = float(r["maker_amt"] or 0), float(r["taker_amt"] or 0)
    if not ma or not ta:
        return None, None
    return (ma / ta, ta) if r["side"] == "0" else (ta / ma, ma)


def t_aparece(libro, t_f, precio):
    """Instante (exchange) desde el que el mejor ask es <= precio sin interrupción hasta t_f. None si no se sabe."""
    if not libro:
        return None
    ts = [x[0] for x in libro]
    i = bisect.bisect_right(ts, t_f - 1) - 1      # estado justo antes del relleno
    if i < 0:
        return None
    if libro[i][2] is None or libro[i][2] > precio + 1e-9:
        return None                               # el top visible no estaba a ese precio: no se puede atribuir
    j = i
    while j > 0 and libro[j - 1][2] is not None and libro[j - 1][2] <= precio + 1e-9:
        j -= 1
    if j == 0:
        return None                               # ya estaba antes del inicio de lo grabado
    return libro[j][0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pkl", required=True)
    a = ap.parse_args()
    d = pickle.load(open(a.pkl, "rb"))
    rel, meta, trades, libro, W = d["rel"], d["meta"], d["trades"], d["libro"], d["W"]
    des = desenlaces({meta[r["token_id"]][2] for r in rel if r["token_id"] in meta})
    usados = set()
    for w in W:
        M = [r for r in rel if r["tipo"] == "M" and r["maker"].lower() == w]
        deltas, emp = [], 0
        for r in M:
            p, sh = ps(r)
            if p is None:
                continue
            tb = float(r["ts_est"]) * 1000
            c = [x for x in trades.get(r["token_id"], []) if tb - 4000 <= x[0] <= tb + 500 and
                 abs(x[3] - sh) <= max(0.01 * sh, 0.011) and x[2] == ("BUY" if r["side"] == "0" else "SELL")]
            if len(c) != 1:
                continue
            emp += 1
            usados.add((r["token_id"], c[0][0]))
            ta = t_aparece(libro.get(r["token_id"], []), c[0][0], c[0][1])
            if ta is not None:
                deltas.append(c[0][0] - ta)
        print(f"\n=== {w[:10]} === órdenes tomadoras {len(M)}, con hora ms {emp}, con aparición del nivel medible {len(deltas)}")
        if deltas:
            q = sorted(deltas)
            f = lambda p_: q[min(len(q) - 1, int(len(q) * p_))]
            print(f"  Δ relleno - aparición del nivel (ms, reloj del exchange): P10 {f(.1)} P25 {f(.25)} P50 {f(.5)} "
                  f"P75 {f(.75)} P90 {f(.9)} | <150 ms: {sum(x < 150 for x in q) / len(q):.0%} | <50 ms: "
                  f"{sum(x < 50 for x in q) / len(q):.0%}")
        # estructura por mercado
        merc = collections.defaultdict(lambda: {"YES": [0.0, 0.0, 0.0], "NO": [0.0, 0.0, 0.0]})
        for r in rel:
            if r["token_id"] not in meta:
                continue
            soy_tomador = r["tipo"] == "M" and r["maker"].lower() == w
            soy_maker = r["tipo"] == "F" and r["maker"].lower() == w and r["taker"].lower() not in (EX, "")
            if not (soy_tomador or soy_maker):
                continue
            p, sh = ps(r)
            if p is None or r["side"] != "0":
                continue
            mo, marco, mid, cie, lado = meta[r["token_id"]]
            x = merc[(mo, marco, mid, cie)][lado]
            x[0] += sh
            x[1] += sh * p
            x[2] += sh * fee(p) if soy_tomador else 0.0
        gar, direc, n_ambos, costes = 0.0, 0.0, 0, []
        for (mo, marco, mid, cie), v in merc.items():
            y, n = v["YES"], v["NO"]
            res = des.get(mid)
            if y[0] and n[0]:
                n_ambos += 1
                pm_y, pm_n = y[1] / y[0], n[1] / n[0]
                fy, fn = y[2] / y[0], n[2] / n[0]
                cs = min(y[0], n[0])
                coste_set = pm_y + pm_n + fy + fn
                costes.append(coste_set)
                gar += cs * (1 - coste_set)
                exceso, lado_ex = (y[0] - cs, "YES") if y[0] > n[0] else (n[0] - cs, "NO")
                pm, fe = (pm_y, fy) if lado_ex == "YES" else (pm_n, fn)
                if res and exceso:
                    direc += exceso * ((1.0 if res == lado_ex else 0.0) - pm - fe)
            else:
                lado_ex = "YES" if y[0] else "NO"
                z = y if y[0] else n
                if res and z[0]:
                    direc += z[0] * ((1.0 if res == lado_ex else 0.0)) - z[1] - z[2]
        print(f"  mercados {len(merc)}, con YES y NO {n_ambos} | coste del conjunto completo (YES+NO+comisión) "
              f"P10/P50/P90 {sorted(costes)[len(costes) // 10] if costes else 0:.3f}/"
              f"{st.median(costes) if costes else 0:.3f}/{sorted(costes)[int(len(costes) * .9)] if costes else 0:.3f}")
        print(f"  PnL GARANTIZADO (conjuntos completos) {gar:+.2f} $ | PnL DIRECCIONAL (exceso de un lado, desenlace "
              f"oficial) {direc:+.2f} $")
        # pares anidados 5m/15m mismo cierre
        cierres = collections.defaultdict(set)
        for (mo, marco, mid, cie), v in merc.items():
            for lado in ("YES", "NO"):
                if v[lado][0]:
                    cierres[(mo, cie)].add((marco, lado))
        nested = [k for k, v in cierres.items() if any(x[0] == "5min" for x in v) and any(x[0] == "15min" for x in v)]
        print(f"  cierres con 5m y 15m comprados: {len(nested)} -> {[(k[0], k[1], sorted(cierres[k])) for k in nested][:6]}")
    # línea base: todas las compras de esos tokens que no son de las wallets
    base = []
    for tok, tr in trades.items():
        lb = libro.get(tok, [])
        for x in tr:
            if x[2] != "BUY" or (tok, x[0]) in usados:
                continue
            ta = t_aparece(lb, x[0], x[1])
            if ta is not None:
                base.append(x[0] - ta)
    if base:
        q = sorted(base)
        f = lambda p_: q[min(len(q) - 1, int(len(q) * p_))]
        print(f"\nLÍNEA BASE (resto de compras en los mismos tokens, n={len(q)}): Δ P10 {f(.1)} P25 {f(.25)} P50 {f(.5)} "
              f"P75 {f(.75)} P90 {f(.9)} | <150 ms: {sum(x < 150 for x in q) / len(q):.0%} | <50 ms: "
              f"{sum(x < 50 for x in q) / len(q):.0%}")


if __name__ == "__main__":
    main()
