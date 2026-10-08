#!/usr/bin/env python3
"""analisis_15m_v4_cosechador_pares.py -- MISIÓN 15M v4 (08-Oct): simulador del COSECHADOR DE PARES (la estructura que
gana on-chain: makers con escalera de pujas en YES y NO, coste de par 0,95-0,99, posición neta baja; ver
informes/m15v4_quien_gana_08oct.txt). Un par emparejado cobra 1 - (b_yes + b_no) gane quien gane: el objeto económico
NO es "una pata aguantada a resolución" (lo que midió V3).

Reglas CONGELADAS 08-Oct antes de ver resultados:
  - Mercados 15m con registro ms (caché m15_ms_cache: q = top del libro, t = operaciones con lado del TOMADOR).
  - Desde T=840 s hasta T_stop=60 s, cada PASO=2 s (reloj de RECEPCIÓN): mid del token YES (último q recibido); pujas
    deseadas en YES a mid_y - d y en NO a (1 - mid_y) - d para cada d de la ESCALERA, TAM acciones por nivel, en la
    rejilla de 0,01 hacia abajo. Alta y cancelación efectivas 100 ms después (hora del exchange ≈ recepción + 100 ms):
    durante ese hueco siguen vivas las órdenes viejas (riesgo de cotización rancia incluido).
  - Inventario: si las acciones SIN pareja de un lado superan TOPE, no se puja en ese lado (solo en el que empareja).
  - RELLENO CONSERVADOR: una puja a b en YES se llena entera si una operación en YES con tomador VENDEDOR imprime a
    precio < b, o una operación en NO con tomador COMPRADOR imprime a > 1 - b (cruce por acuñación). "Atravesar" el
    nivel implica que toda la cola a b se consumió: sin supuestos de posición en cola. Variante OPTIMISTA: <= b.
  - A T_stop se cancela todo; lo emparejado cobra 1 por par; lo suelto va a resolución (desenlace oficial).
  - Reembolso de maker ESTIMADO = 20 % de 0,07·p·(1-p) por acción rellenada (rebateRate de gamma; reparto real sin
    verificar): se reporta APARTE.
Salida: por escalera × variante × moneda × día: mercados, rellenos/mercado, % emparejado, coste medio del par, PnL
emparejado, PnL de la pata suelta, PnL/mercado, IC90 por días, + reembolso estimado.
Uso: (ulimit -v 5000000; nice -n 19 ionice -c3 python3 analisis_15m_v4_cosechador_pares.py [--cache DIR])
"""
import argparse
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

ESCALERAS = {"A_1c": (0.01,), "B_2-4c": (0.02, 0.04), "C_3-6c": (0.03, 0.06), "D_2-8c": (0.02, 0.04, 0.06, 0.08)}
TAM, TOPE, PASO_MS, LAT_MS, T_INI, T_STOP = 10.0, 30.0, 2000, 100, 840, 60
# v2 (08-Oct, CONGELADA antes de correr; Javi pidió "pujar NO según <= 1 - precio de YES - margen"): la pata que EMPAREJA
# no persigue al mid: se puja a min(precio de escalera, 1 - coste medio de la pata suelta - MARGEN). Variantes
# declaradas de antemano: MARGEN 0,03 y 0,05. Sin pata suelta, escalera sobre el mid en ambos lados (igual que v1).
MARGENES_V2 = (0.03, 0.05)


def rej(x):
    return np.floor(np.round(x * 100, 6)) / 100


def simular_mercado(qy, ty, tn, fin_ms, escalera, optimista, margen=None):
    """qy: (tr, bb, ba) del YES ordenado por tr. ty/tn: (te, p, side_tomador(1=compra), sz) de YES y NO por te.
    Devuelve (acc_yes, coste_yes, acc_no, coste_no, n_rellenos, rebate)."""
    tr, bb, ba = qy
    inv = {"Y": [0.0, 0.0], "N": [0.0, 0.0]}          # acciones, coste
    n_rell = 0
    reb = 0.0
    vivas = []                                         # (lado, precio, acc_restantes, te_desde, te_hasta)
    t0 = fin_ms - T_INI * 1000
    pasos = np.arange(t0, fin_ms - T_STOP * 1000, PASO_MS)
    for k, ts in enumerate(pasos):
        j = np.searchsorted(tr, ts, side="right") - 1
        if j < 0 or not (bb[j] > 0 and ba[j] > 0 and ba[j] > bb[j]):
            continue
        mid = (bb[j] + ba[j]) / 2
        efec = ts + LAT_MS
        hasta = (pasos[k + 1] if k + 1 < len(pasos) else fin_ms - T_STOP * 1000) + LAT_MS
        # las vivas del paso anterior acaban en efec (cancelación); se crean las nuevas desde efec
        vivas = [(l, p, a, d, min(h, efec)) for (l, p, a, d, h) in vivas]
        sy = inv["Y"][0] - inv["N"][0]
        nuevas = []
        tope_y = tope_n = None                             # v2: precio máximo de la pata que empareja
        if margen is not None and sy > 1e-9:               # sobra YES -> NO anclado al coste medio del YES suelto
            tope_n = rej(1 - inv["Y"][1] / inv["Y"][0] - margen)
        elif margen is not None and sy < -1e-9:
            tope_y = rej(1 - inv["N"][1] / inv["N"][0] - margen)
        for d in escalera:
            py, pn = rej(mid - d), rej(1 - mid - d)
            if tope_y is not None:
                py = min(py, tope_y)
            if tope_n is not None:
                pn = min(pn, tope_n)
            if sy < TOPE and 0.01 <= py <= 0.98:
                nuevas.append(["Y", py, TAM, efec, hasta])
            if -sy < TOPE and 0.01 <= pn <= 0.98:
                nuevas.append(["N", pn, TAM, efec, hasta])
        ordenes = [list(v) for v in vivas] + nuevas
        # rellenos en la ventana de cada orden
        for o in ordenes:
            lado, p, a, desde, h = o
            if a <= 0 or h <= desde:
                continue
            for (T_, pr_, sd_, own) in ((ty, None, None, True), (tn, None, None, False)):
                te, pp, sd, sz = T_
                i0, i1 = np.searchsorted(te, desde), np.searchsorted(te, h)
                if i1 <= i0:
                    continue
                if (lado == "Y") == own:               # mismo token: tomador VENDE a precio < p
                    m = (sd[i0:i1] == 0) & ((pp[i0:i1] < p - 1e-9) if not optimista else (pp[i0:i1] <= p + 1e-9))
                else:                                  # token contrario: tomador COMPRA a > 1 - p (acuñación)
                    m = (sd[i0:i1] == 1) & ((pp[i0:i1] > 1 - p + 1e-9) if not optimista else (pp[i0:i1] >= 1 - p - 1e-9))
                if m.any():
                    inv[lado][0] += a
                    inv[lado][1] += a * p
                    reb += 0.2 * 0.07 * p * (1 - p) * a
                    n_rell += 1
                    o[2] = 0.0
                    break
        vivas = [tuple(o) for o in ordenes if o[2] > 0]
    return inv["Y"][0], inv["Y"][1], inv["N"][0], inv["N"][1], n_rell, reb


# v3 (08-Oct, CONGELADA antes de ver PnL; política EXTRAÍDA de los rellenos on-chain de 5 cosechadores en BTC 05-06,
# informes/m15v4_politica_bots_pares_08oct.txt): ambos lados en el MEJOR BID de cada token y 1c por debajo, TAM3
# acciones por nivel; recotización cada 2 s SIN perder la cola (si el precio deseado no cambia, la orden se queda);
# sin anclaje ni sesgo; deja de pujar el lado que sobra solo si el desequilibrio supera TOPE3; para a T_STOP3.
# Relleno: en el mejor bid con MODELO DE COLA (cola delante = tamaño visible del nivel al entrar; la consumen las
# operaciones a ese precio en el token -tomador vende- o en el contrario -tomador compra a 1 - p, acuñación-; las
# cancelaciones de delante NO nos adelantan: conservador); por debajo del mejor bid, solo si se ATRAVIESA el nivel.
TAM3, TOPE3, T_STOP3, NIVELES3 = 10.0, 300.0, 90, (0.0, 0.01)


# v4 (08-Oct, CONGELADA antes de correr; Javi: "antes, más simulación"): réplica de UN solo bot, 0x81c935ef, con
# parámetros medidos en sus rellenos BTC 05-06 (informes/m15v4_politica_bots_pares_08oct.txt): solo el mejor bid
# (57 % de sus rellenos), 12 acciones (tamaño mediano 11,5), tope de desequilibrio 60 (max|I| P90 66), lado que sobra
# con tamaño 12·(1 - |I|/60) (su P(empareja) sube 0,60 -> 0,75 con |I|), de T=870 s a T=90 s (1er/último relleno
# P50 860/92 s). Mismo modelo de cola que v3.
V4 = {"niveles": (0.0,), "tam": 12.0, "tope": 60.0, "sesgo": True, "t_ini": 870, "t_stop": 90}


def simular_v3(qy, qn, ty, tn, fin_ms, niveles=None, tam=None, tope=None, sesgo=False, t_ini=None, t_stop=None):
    """qy/qn: dict con vistas del libro: por RECEPCIÓN (tr, bb_tr) para decidir y por EXCHANGE (te, bb_te, bs_te)
    para la cola al entrar. ty/tn: (te, p, side, sz) por te."""
    niveles = NIVELES3 if niveles is None else niveles
    tam = TAM3 if tam is None else tam
    tope = TOPE3 if tope is None else tope
    inv = {"Y": [0.0, 0.0], "N": [0.0, 0.0]}
    n_rell, reb = 0, 0.0
    max_abs_i = 0.0
    ordenes = {}                                       # (lado, precio) -> dict(rest, desde, cola, ultimo_te)
    t0 = fin_ms - (T_INI if t_ini is None else t_ini) * 1000
    t_fin = fin_ms - (T_STOP3 if t_stop is None else t_stop) * 1000
    libro = {"Y": qy, "N": qn}
    trades = {"Y": (ty, tn), "N": (tn, ty)}           # (mismo token, token contrario)

    def avanzar(o, lado, p, hasta):
        """Procesa operaciones (o["ultimo_te"], hasta] contra la orden; devuelve acciones rellenadas."""
        mismo, contra = trades[lado]
        lleno = 0.0
        ev = []
        te, pp, sd, sz = mismo
        i0, i1 = np.searchsorted(te, o["ultimo_te"], side="right"), np.searchsorted(te, hasta, side="right")
        for k in range(i0, i1):
            if sd[k] == 0:
                ev.append((te[k], pp[k], sz[k]))
        te, pp, sd, sz = contra
        i0, i1 = np.searchsorted(te, o["ultimo_te"], side="right"), np.searchsorted(te, hasta, side="right")
        for k in range(i0, i1):
            if sd[k] == 1:
                ev.append((te[k], round(1 - pp[k], 4), sz[k]))
        ev.sort()
        for _, px, q in ev:
            if o["rest"] <= 0:
                break
            if px < p - 1e-9:                           # atraviesa: todo lo nuestro se llena
                lleno += o["rest"]
                o["rest"] = 0.0
            elif abs(px - p) < 1e-9 and o["cola"] is not None:
                o["cola"] -= q
                if o["cola"] < 0:
                    f = min(o["rest"], -o["cola"])
                    lleno += f
                    o["rest"] -= f
                    o["cola"] = 0.0
        o["ultimo_te"] = hasta
        return lleno

    for ts in np.arange(t0, t_fin, PASO_MS):
        efec = ts + LAT_MS
        # 1) liquidar hasta efec las órdenes vivas
        for (lado, p), o in list(ordenes.items()):
            f = avanzar(o, lado, p, efec)
            if f > 0:
                inv[lado][0] += f
                inv[lado][1] += f * p
                reb += 0.2 * 0.07 * p * (1 - p) * f
                n_rell += 1
            if o["rest"] <= 0:
                del ordenes[(lado, p)]
        # 2) precios deseados con el libro VISTO (recepción <= ts)
        sy = inv["Y"][0] - inv["N"][0]
        max_abs_i = max(max_abs_i, abs(sy))
        deseadas = {}
        for lado in ("Y", "N"):
            L_ = libro[lado]
            tr_, bb_ = L_["tr"], L_["bb_tr"]
            j = np.searchsorted(tr_, ts, side="right") - 1
            if j < 0 or not (0.01 <= bb_[j] <= 0.98):
                continue
            sobra = (lado == "Y" and sy > 0) or (lado == "N" and sy < 0)
            if sobra and abs(sy) >= tope:
                continue
            t_orden = tam * (1 - abs(sy) / tope) if (sesgo and sobra) else tam
            if t_orden < 1:
                continue
            for d in niveles:
                pr = round(float(bb_[j]) - d, 2)
                if pr >= 0.01:
                    deseadas[(lado, pr)] = t_orden
        # 3) cancelar las que ya no se desean (efectivo en efec); alta de las nuevas con su cola
        for k in list(ordenes):
            if k not in deseadas:
                del ordenes[k]
        for (lado, pr), t_orden in deseadas.items():
            if (lado, pr) in ordenes:
                continue                               # se queda: conserva su posición en la cola
            L_ = libro[lado]
            j = np.searchsorted(L_["te"], efec, side="right") - 1  # libro en el exchange al entrar
            cola = float(L_["bs_te"][j]) if j >= 0 and abs(float(L_["bb_te"][j]) - pr) < 1e-9 else None
            ordenes[(lado, pr)] = {"rest": t_orden, "cola": cola, "ultimo_te": efec}
    # último tramo hasta la parada
    for (lado, p), o in list(ordenes.items()):
        f = avanzar(o, lado, p, t_fin + LAT_MS)
        if f > 0:
            inv[lado][0] += f
            inv[lado][1] += f * p
            reb += 0.2 * 0.07 * p * (1 - p) * f
            n_rell += 1
    simular_v3.max_abs_i = max_abs_i
    return inv["Y"][0], inv["Y"][1], inv["N"][0], inv["N"][1], n_rell, reb


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default="/root/polymarket-research-datalogs/m15_ms_cache")
    ap.add_argument("--salida", default="informes/m15v4_cosechador_pares_08oct.txt")
    ap.add_argument("--activos", default="", help="p. ej. BTC (vacío = todas)")
    ap.add_argument("--escaleras", default="", help="p. ej. B_2-4c,C_3-6c (vacío = todas)")
    ap.add_argument("--solo-conservador", action="store_true")
    ap.add_argument("--solo-optimista", action="store_true")
    ap.add_argument("--version", default="v1", choices=["v1", "v2", "v3", "v4"])
    a = ap.parse_args()
    os.environ["M15_CACHE_DIR"] = a.cache
    from m15_ms_cache import cargar
    C = cargar()
    q, T = C["q"], C["t"]
    toks = C["tokens"]
    bq = np.searchsorted(q["tok"], np.arange(len(toks) + 1))
    o = np.lexsort((T["te"], T["tok"]))
    T = {k: v[o] for k, v in T.items()}
    bt = np.searchsorted(T["tok"], np.arange(len(toks) + 1))
    merc = {}
    for i, (tk, act, mid, fin, lado) in enumerate(toks):
        merc.setdefault(str(mid), {"act": act, "fin": int(fin)})[lado] = i
    des = desenlaces(set(merc))
    filas = []
    for mid, m in merc.items():
        if "YES" not in m or "NO" not in m or mid not in des:
            continue
        if a.activos and m["act"] not in a.activos.split(","):
            continue
        iy, inn = m["YES"], m["NO"]
        a0, a1 = bq[iy], bq[iy + 1]
        if a1 - a0 < 50:
            continue
        o2 = np.argsort(q["tr"][a0:a1], kind="stable")
        qy = (q["tr"][a0:a1][o2], q["bb"][a0:a1][o2].astype(float), q["ba"][a0:a1][o2].astype(float))
        ty = tuple(T[k][bt[iy]:bt[iy + 1]] for k in ("te", "p", "side", "sz"))
        tn = tuple(T[k][bt[inn]:bt[inn + 1]] for k in ("te", "p", "side", "sz"))
        fin_ms = m["fin"] * 1000
        if qy[0][0] > fin_ms - T_INI * 1000 + 60_000 or qy[0][-1] < fin_ms - T_STOP * 1000:
            continue                                   # registro sin cobertura del ciclo
        gana_y = des[mid] == "YES"
        dia = pd.Timestamp(m["fin"], unit="s").strftime("%Y-%m-%d")
        if a.version in ("v3", "v4"):
            b0, b1 = bq[inn], bq[inn + 1]
            if b1 - b0 < 50:
                continue

            def vistas(c0, c1):
                otr = np.argsort(q["tr"][c0:c1], kind="stable")
                ote = np.argsort(q["te"][c0:c1], kind="stable")
                return {"tr": q["tr"][c0:c1][otr], "bb_tr": q["bb"][c0:c1][otr].astype(float),
                        "te": q["te"][c0:c1][ote], "bb_te": q["bb"][c0:c1][ote].astype(float),
                        "bs_te": q["bs"][c0:c1][ote].astype(float)}
            qy3, qn3 = vistas(a0, a1), vistas(b0, b1)
            ay, cy, an, cn, nr, reb = simular_v3(qy3, qn3, ty, tn, fin_ms, **(V4 if a.version == "v4" else {}))
            par = min(ay, an)
            cpy, cpn = (cy / ay if ay else 0), (cn / an if an else 0)
            pnl_par = par * (1 - cpy - cpn) if par else 0.0
            pnl_suelta = (ay - par) * ((1.0 if gana_y else 0.0) - cpy) + (an - par) * ((0.0 if gana_y else 1.0) - cpn)
            filas.append({"mkt": mid, "act": m["act"], "dia": dia, "esc": "v3_extraida" if a.version == "v3" else "v4_replica_81c9",
                          "var": "cola", "max_abs_i": simular_v3.max_abs_i, "i_final_frac": abs(ay - an) / max(1e-9, ay + an),
                          "rell": nr, "acc": ay + an, "par": par, "coste_par": (cpy + cpn) if par else np.nan,
                          "pnl_par": pnl_par, "pnl_suelta": pnl_suelta, "pnl": pnl_par + pnl_suelta, "reb": reb,
                          "inv_usdc": cy + cn})
            continue
        for nom0, esc in ESCALERAS.items():
            if a.escaleras and nom0 not in a.escaleras.split(","):
                continue
            for mg in ((None,) if a.version == "v1" else MARGENES_V2):
              nom = nom0 if mg is None else f"{nom0}_v2m{int(round(mg * 100))}"
              for opt in ((False,) if a.solo_conservador else (True,) if a.solo_optimista else (False, True)):
                ay, cy, an, cn, nr, reb = simular_mercado(qy, ty, tn, fin_ms, esc, opt, mg)
                par = min(ay, an)
                cpy, cpn = (cy / ay if ay else 0), (cn / an if an else 0)
                pnl_par = par * (1 - cpy - cpn) if par else 0.0
                suelta_y, suelta_n = ay - par, an - par
                pnl_suelta = suelta_y * ((1.0 if gana_y else 0.0) - cpy) + suelta_n * ((0.0 if gana_y else 1.0) - cpn)
                filas.append({"mkt": mid, "act": m["act"], "dia": dia, "esc": nom, "var": "optimista" if opt else "conservador",
                              "rell": nr, "acc": ay + an, "par": par, "coste_par": (cpy + cpn) if par else np.nan,
                              "pnl_par": pnl_par, "pnl_suelta": pnl_suelta, "pnl": pnl_par + pnl_suelta, "reb": reb,
                              "inv_usdc": cy + cn})
    R = pd.DataFrame(filas)
    lin = []

    def L(s=""):
        print(s, flush=True)
        lin.append(s)
    L(f"Cosechador de pares — {R.mkt.nunique()} mercados 15m, días {sorted(R.dia.unique())}; TAM {TAM}, TOPE {TOPE}, paso {PASO_MS} ms, latencia {LAT_MS} ms, T {T_INI}->{T_STOP} s")
    rng = np.random.default_rng(3)
    for (esc, var), g in R.groupby(["esc", "var"]):
        L(f"\n== {esc} {var} ==")
        for act, h in [("TODAS", g)] + list(g.groupby("act")):
            dm = h.groupby("dia").pnl.mean()
            bs = [rng.choice(dm.values, len(dm)).mean() for _ in range(1000)] if len(dm) > 1 else [np.nan]
            frac = 2 * h.par.sum() / max(1e-9, h.acc.sum())
            L(f"  {act:5s} merc={len(h):4d} rell/merc={h.rell.mean():5.1f} acc/merc={h.acc.mean():6.1f} emparejado={frac:.2f} "
              f"coste_par={np.nansum(h.coste_par * h.par) / max(1e-9, h.par.sum()):.4f} PnL_par/merc={h.pnl_par.mean():+.3f} "
              f"PnL_suelta/merc={h.pnl_suelta.mean():+.3f} PnL/merc={h.pnl.mean():+.3f} (días {', '.join(f'{v:+.2f}' for v in dm.values)}) "
              f"IC90d=({np.nanpercentile(bs, 5):+.2f},{np.nanpercentile(bs, 95):+.2f}) reb/merc={h.reb.mean():.3f} "
              f"capital/merc={h.inv_usdc.mean():.1f}"
              + (f" | max|I| P50 {h.max_abs_i.median():.0f} P90 {h.max_abs_i.quantile(.9):.0f}; |I| final/acc P50 {h.i_final_frac.median():.3f}; "
                 f"rell/merc P50 {h.rell.median():.0f}; acc/merc P50 {h.acc.median():.0f}; PnL/merc P10 {h.pnl.quantile(.1):+.1f} P90 {h.pnl.quantile(.9):+.1f}"
                 if "max_abs_i" in h else ""))
    Path(a.salida).write_text("\n".join(lin) + "\n")
    R.to_parquet(Path(a.cache) / ("v4_cosechador_pares" + (f"_{a.version}" if a.version != "v1" else "") + (f"_{a.activos}" if a.activos else "") + ("_opt" if a.solo_optimista else "") + ".parquet"))


if __name__ == "__main__":
    main()
