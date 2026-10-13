#!/usr/bin/env python3
"""analisis_15m_v5_sim_barato_reposicion.py -- MISIÓN 15M v5 (13-Oct): ¿una puja PROPIA que se repone en el lado barato de
BTC 15m captura el EV ponderado por volumen de H15-BARATO-REPOSICION-V1? (días del registro ya vistos: EXPLORACIÓN de
capturabilidad, no validación; la validación es el forward del vigía desde 13-Oct).

Política (fijada antes de correr): cada PASO=2 s (reloj de RECEPCIÓN), para cada token (YES y NO) con T restante en
(60, 600] s y mejor bid visto en [0,10, 0,40): una puja de TAM=5 acciones en el MEJOR bid. Si el mejor bid cambia, se mueve
(pierde la cola). Tras un relleno se repone en el siguiente paso. Tope de inventario por token y mercado: TOPE acciones
(variantes inf, 100, 25). Alta/cancelación efectivas LAT=100 ms después.
Relleno (modelo de simular_v3 de analisis_15m_v4_cosechador_pares.py): VENTAS tomadoras del token o COMPRAS tomadoras
del contrario (acuñación, precio 1-p); por debajo de nuestro precio = atraviesa (llena entera); a nuestro precio consume
primero la cola que teníamos delante al entrar. Cotas: CONSERVADORA (cola delante = tamaño visible del nivel al entrar;
las cancelaciones de delante no nos adelantan) y OPTIMISTA (cola 0: siempre primeros).
PnL a resolución (desenlace oficial), maker sin comisión; reembolso estimado (20 % de 0,07·p·(1-p)) aparte.
Uso: M15_CACHE_DIR=... (ulimit -v 3500000; nice -n 19 python3 analisis_15m_v5_sim_barato_reposicion.py)
"""
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

TAM, PASO_MS, LAT_MS = 5.0, 2000, 100
T_HI, T_LO, P_LO, P_HI = 600, 60, 0.10, 0.40
TOPES = (float("inf"), 100.0, 25.0)
INF = Path(__file__).resolve().parent / "informes" / "m15v5_sim_barato_reposicion_13oct.txt"


def simular(lib, trades, fin_ms, tope, optimista):
    """lib[l] = dict(tr, bb_tr, te, bb_te, bs_te); trades[l] = (mismo token, contrario) con (te, p, side, sz).
    Devuelve {l: [acc, coste, n_rellenos, reb]}."""
    inv = {l: [0.0, 0.0, 0, 0.0] for l in ("Y", "N")}
    ordenes = {}                                       # l -> dict(p, rest, cola, ultimo_te)

    def avanzar(l, o, hasta):
        mismo, contra = trades[l]
        ev = []
        te, pp, sd, sz = mismo
        for k in range(np.searchsorted(te, o["ultimo_te"], side="right"), np.searchsorted(te, hasta, side="right")):
            if sd[k] == 0:
                ev.append((te[k], pp[k], sz[k]))
        te, pp, sd, sz = contra
        for k in range(np.searchsorted(te, o["ultimo_te"], side="right"), np.searchsorted(te, hasta, side="right")):
            if sd[k] == 1:
                ev.append((te[k], round(1 - float(pp[k]), 4), sz[k]))
        ev.sort()
        lleno = 0.0
        for _, px, q in ev:
            if o["rest"] <= 0:
                break
            if px < o["p"] - 1e-9:
                lleno += o["rest"]
                o["rest"] = 0.0
            elif abs(px - o["p"]) < 1e-9:
                o["cola"] -= q
                if o["cola"] < 0:
                    f = min(o["rest"], -o["cola"])
                    lleno += f
                    o["rest"] -= f
                    o["cola"] = 0.0
        o["ultimo_te"] = hasta
        return lleno

    t0, t1 = fin_ms - T_HI * 1000, fin_ms - T_LO * 1000
    for ts in np.arange(t0, t1, PASO_MS):
        efec = ts + LAT_MS
        for l, o in list(ordenes.items()):
            f = avanzar(l, o, efec)
            if f > 0:
                inv[l][0] += f
                inv[l][1] += f * o["p"]
                inv[l][2] += 1
                inv[l][3] += 0.2 * 0.07 * o["p"] * (1 - o["p"]) * f
            if o["rest"] <= 0:
                del ordenes[l]
        for l in ("Y", "N"):
            L_ = lib[l]
            j = np.searchsorted(L_["tr"], ts, side="right") - 1
            bb = float(L_["bb_tr"][j]) if j >= 0 else np.nan
            quiero = (P_LO <= bb < P_HI) and inv[l][0] + TAM <= tope + 1e-9
            o = ordenes.get(l)
            if o is not None and (not quiero or abs(o["p"] - round(bb, 2)) > 1e-9):
                del ordenes[l]                         # cancelación (efectiva en efec: ya liquidado hasta efec)
                o = None
            if quiero and o is None:
                pr = round(bb, 2)
                k = np.searchsorted(L_["te"], efec, side="right") - 1
                cola = 0.0 if optimista else (float(L_["bs_te"][k]) if k >= 0 and abs(float(L_["bb_te"][k]) - pr) < 1e-9 else 0.0)
                ordenes[l] = {"p": pr, "rest": TAM, "cola": cola, "ultimo_te": efec}
    for l, o in list(ordenes.items()):
        f = avanzar(l, o, t1 + LAT_MS)
        if f > 0:
            inv[l][0] += f
            inv[l][1] += f * o["p"]
            inv[l][2] += 1
            inv[l][3] += 0.2 * 0.07 * o["p"] * (1 - o["p"]) * f
    return inv


def main():
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

    def vistas(i):
        c0, c1 = bq[i], bq[i + 1]
        otr = np.argsort(q["tr"][c0:c1], kind="stable")
        ote = np.argsort(q["te"][c0:c1], kind="stable")
        return {"tr": q["tr"][c0:c1][otr], "bb_tr": q["bb"][c0:c1][otr].astype(float),
                "te": q["te"][c0:c1][ote], "bb_te": q["bb"][c0:c1][ote].astype(float), "bs_te": q["bs"][c0:c1][ote].astype(float)}

    filas = []
    for mid, m in merc.items():
        if "YES" not in m or "NO" not in m or mid not in des or m["act"] != "BTC":
            continue
        iy, inn = m["YES"], m["NO"]
        if bq[iy + 1] - bq[iy] < 50 or bq[inn + 1] - bq[inn] < 50:
            continue
        fin_ms = m["fin"] * 1000
        ly, ln = vistas(iy), vistas(inn)
        if ly["tr"][0] > fin_ms - T_HI * 1000 or ly["tr"][-1] < fin_ms - T_LO * 1000:
            continue
        ty = tuple(T[k][bt[iy]:bt[iy + 1]] for k in ("te", "p", "side", "sz"))
        tn = tuple(T[k][bt[inn]:bt[inn + 1]] for k in ("te", "p", "side", "sz"))
        lib, trades = {"Y": ly, "N": ln}, {"Y": (ty, tn), "N": (tn, ty)}
        dia = pd.Timestamp(m["fin"], unit="s").strftime("%Y-%m-%d")
        for tope in TOPES:
            for opt in (False, True):
                inv = simular(lib, trades, fin_ms, tope, opt)
                for l, (acc, coste, nr, reb) in inv.items():
                    if acc <= 0:
                        continue
                    gana = (l == "Y") == (des[mid] == "YES")
                    filas.append({"mkt": mid, "dia": dia, "lado": l, "tope": tope, "cota": "optimista" if opt else "conservadora",
                                  "acc": acc, "coste": coste, "n": nr, "gana": gana, "pnl": acc * gana - coste, "reb": reb})
    R = pd.DataFrame(filas)
    lin = []

    def L(s=""):
        print(s, flush=True)
        lin.append(s)
    nm = len({mid for mid, m in merc.items() if m["act"] == "BTC"})
    L(f"Puja barata que se repone BTC 15m — días {sorted(R.dia.unique())}, mercados BTC en caché {nm}; TAM {TAM}, T ({T_LO},{T_HI}], "
      f"bid [{P_LO},{P_HI})")
    rng = np.random.default_rng(5)
    for (tope, cota), g in R.groupby(["tope", "cota"]):
        i = rng.integers(0, len(g), size=(2000, len(g)))
        bs = g.pnl.values[i].sum(1) / g.coste.values[i].sum(1)
        dd = g.groupby("dia").agg(p=("pnl", "sum"), e=("coste", "sum"))
        merc_pnl = g.groupby("mkt").pnl.sum()
        L(f"  tope {tope:>5} {cota:12s} unidades {len(g):4d} | EV/€ {g.pnl.sum() / g.coste.sum():+.4f} IC90 ({np.quantile(bs, .05):+.4f},"
          f"{np.quantile(bs, .95):+.4f}) | PnL/merc {merc_pnl.sum() / nm:+.3f} $ (+reemb {(merc_pnl.sum() + g.reb.sum()) / nm:+.3f}) | "
          f"rellenos/unidad si gana {g[g.gana].n.mean():.1f} si pierde {g[~g.gana].n.mean():.1f} | acc/unidad P50 {g.acc.median():.0f} "
          f"| P(gana) {g.gana.mean():.3f} precio {g.coste.sum() / g.acc.sum():.3f} | días " + " ".join(f"{d[5:]}:{r.p / r.e:+.3f}" for d, r in dd.iterrows()))
    INF.write_text("\n".join(lin) + "\n")
    L(f"\n→ {INF}")


if __name__ == "__main__":
    main()
