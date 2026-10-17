#!/usr/bin/env python3
"""H26 -- DIAGNÓSTICO DE LA CALIBRACIÓN del simulador maker banda (17-Oct): ¿comparamos el mismo objeto?
SOLO LECTURA sobre las cachés del simulador (unidades_D, pob_fills_D, universo_D). Sin red, sin órdenes, sin m5_registro.

Motivo: la calibración del simulador (analisis_5m_maker_banda_simulador.calibracion) comparó la población on-chain H5M "final de la
cola" (EV de la unidad con TODOS sus rellenos, ~105 por unidad, 77 % del volumen en unidades de >500 acciones) con UNA puja nuestra de
5 acciones. Eso no es el mismo objeto. Aquí se construye el objeto comparable: de la población, las PRIMERAS K acciones de cada unidad
(mercado, lado) por orden de reloj de cadena (T descendente = más temprano), K = tamaño de la puja simulada (5, 25, 50). Prorrata dentro
del relleno que cruza K. Es POST HOC (no estaba en el diseño fijado el 16-Oct): el criterio original se informa tal cual y este es un
diagnóstico, no un veredicto de PASA preregistrado; hace falta OK del chief para usarlo como criterio.

Salidas (en --out, por defecto la carpeta de la calibración): diag_calibracion_objeto.txt / .json.
Uso: nice -n 19 ionice -c3 python3 analisis_5m_maker_banda_calibracion_objeto.py [--out DIR] [--dias D1,D2,D3]
"""
import argparse
import gzip
import json
import os
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path("/root/polymarket-research-datalogs/m5barato_mision/h26_sim_calibracion")
DIAS = ["2026-10-05", "2026-10-06", "2026-10-07"]
MOTORES = ("JOIN|C0|CONS|5", "JOIN|C0|OPT|5")
TOL = 0.05
MONEDAS = ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")


def primeras_k(P, k):
    """P: rellenos de la población (columnas dia, mkt, lado_c, T, acc, coste, gana, cola?). -> DataFrame por unidad (dia, mkt, lado) con
    las primeras k acciones por orden temporal de cadena (T descendente; empates en el orden de entrada, estable): acc_k, coste_k, pnl_k.
    El relleno que cruza k se toma a prorrata (acciones y coste). Unidades con menos de k acciones: se toman enteras (acc_k < k)."""
    Q = P.sort_values(["dia", "mkt", "lado_c", "T"], ascending=[True, True, True, False], kind="stable").reset_index(drop=True)
    cum0 = Q.groupby(["dia", "mkt", "lado_c"], sort=False).acc.cumsum() - Q.acc
    tk = np.clip(np.minimum(k, cum0 + Q.acc) - cum0, 0.0, None)
    coste = np.where(Q.acc > 0, tk / Q.acc * Q.coste, 0.0)
    pnl = np.where(Q.gana == 1, tk, 0.0) - coste
    X = pd.DataFrame({"dia": Q.dia, "mkt": Q.mkt, "lado": Q.lado_c, "act": Q.act, "acc_k": tk, "coste_k": coste, "pnl_k": pnl})
    U = X.groupby(["dia", "mkt", "lado"], sort=False).agg(act=("act", "first"), acc_k=("acc_k", "sum"), coste_k=("coste_k", "sum"),
                                                          pnl_k=("pnl_k", "sum")).reset_index()
    return U[U.coste_k > 0]


def ev_pool(pnl, coste):
    c = float(np.sum(coste))
    return float(np.sum(pnl) / c) if c > 0 else float("nan")


def ev_medio(pnl, coste):
    pnl, coste = np.asarray(pnl, float), np.asarray(coste, float)
    return float(np.mean(pnl / coste)) if len(pnl) else float("nan")


def tabla_2x2(universo, pobU, simU):
    """universo: DataFrame (dia, mkt, lado) de unidades de mercados completos; pobU: unidades de la población (dia, mkt, lado, ...);
    simU: unidades del simulador de UN motor (dia, mkt, lado, lleno, norders). -> DataFrame con pop (bool) y sim ('rellena' |
    'cotiza_sin_relleno' | 'nunca_cotiza'). 'missing' no es 0: nunca_cotiza es una categoría propia."""
    A = universo.merge(pobU, on=["dia", "mkt", "lado"], how="left", indicator="_p")
    A["pop"] = A["_p"] == "both"
    A = A.drop(columns="_p").merge(simU, on=["dia", "mkt", "lado"], how="left")
    A["sim"] = np.where(A.norders.isna(), "nunca_cotiza", np.where(A.lleno.fillna(0) > 0, "rellena", "cotiza_sin_relleno"))
    return A


def veredicto_objeto(ev_pop_k, ev_cons, ev_opt, tol=TOL):
    """Mismo haz que el criterio original [min(CONS,OPT)-tol, max(CONS,OPT)+tol], pero con el objeto comparable (población primeras K)."""
    if any(x != x for x in (ev_pop_k, ev_cons, ev_opt)):
        return {"estado": "SIN_DATOS"}
    lo, hi = min(ev_cons, ev_opt) - tol, max(ev_cons, ev_opt) + tol
    return {"estado": "PASA_OBJETO_COMPARABLE" if lo <= ev_pop_k <= hi else "NO_REPRODUCE_OBJETO_COMPARABLE", "haz": [lo, hi],
            "ev_poblacion_primeras_k": ev_pop_k, "ev_cons": ev_cons, "ev_opt": ev_opt, "tol": tol, "post_hoc": True}


def cargar(out, dias):
    U, P, uni = [], [], []
    for d in dias:
        u = pd.read_csv(out / f"unidades_{d}.csv.gz", dtype={"mkt": str, "des": str})
        U.append(u[u.completo == 1])
        p = pd.read_csv(out / f"pob_fills_{d}.csv.gz", dtype={"mkt": str}).assign(dia=d)
        P.append(p)
        with gzip.open(out / f"universo_{d}.csv.gz", "rt") as fh:
            for ln in fh:
                for lado in ("YES", "NO"):
                    uni.append((d, ln.strip(), lado))
    U = pd.concat(U, ignore_index=True)
    P = pd.concat(P, ignore_index=True)
    P["gana"] = (P.lado_c == P.des).astype(int)
    return U, P, pd.DataFrame(uni, columns=["dia", "mkt", "lado"])


def informe(out, dias):
    U, P, uni = cargar(out, dias)
    L, res = [], {}
    L.append(f"H26 calibración: diagnóstico del OBJETO comparado | días {dias} | cachés {out}")
    L.append("Población = réplica del vigía H5M restringida a mercados completos (cada unidad = TODOS los rellenos on-chain de todos los makers).")
    # --- 1. población: de unidad completa a primeras K acciones
    L.append("\n== 1. EV de la población según cuánto volumen de la unidad se cuenta (pooled = ponderado por coste; media = media de unidades) ==")
    L.append("  K              | todas las filas                     | solo 'final de la cola' (rango por tx/nivel)")
    ctrl = {}
    for k in (5, 25, 50, 1e12):
        a, f = primeras_k(P, k), primeras_k(P[P.cola == "final"], k)
        ctrl[k] = (a, f)
        nm = "todo" if k >= 1e11 else f"{k:g}"
        L.append(f"  {nm:14} | pool {ev_pool(a.pnl_k, a.coste_k):+.4f} media {ev_medio(a.pnl_k, a.coste_k):+.4f} n {len(a):5d} | "
                 f"pool {ev_pool(f.pnl_k, f.coste_k):+.4f} media {ev_medio(f.pnl_k, f.coste_k):+.4f} n {len(f):5d}")
        res[f"pob_k{nm}"] = {"todas_pool": ev_pool(a.pnl_k, a.coste_k), "final_pool": ev_pool(f.pnl_k, f.coste_k), "n": len(a), "n_final": len(f)}
    L.append("  Por tramo de volumen acumulado de la unidad (todas las filas): EV del tramo")
    Q = P.sort_values(["dia", "mkt", "lado_c", "T"], ascending=[True, True, True, False], kind="stable").reset_index(drop=True)
    cum0 = Q.groupby(["dia", "mkt", "lado_c"], sort=False).acc.cumsum() - Q.acc
    edges = [0, 5, 25, 50, 100, 200, 500, 1e12]
    for lo, hi in zip(edges[:-1], edges[1:]):
        tk = np.clip(np.minimum(hi, cum0 + Q.acc) - np.maximum(lo, cum0), 0.0, None)
        c = tk / Q.acc * Q.coste
        pn = np.where(Q.gana == 1, tk, 0.0) - c
        L.append(f"    acciones {lo:g}-{'inf' if hi > 1e11 else format(hi, 'g'):>5}: volumen {tk.sum():12.0f} ({tk.sum() / Q.acc.sum():5.1%}) precio {c.sum() / tk.sum():.3f} "
                 f"EV {pn.sum() / c.sum():+.4f}")
    # --- 2. simulador frente al objeto comparable
    L.append("\n== 2. SIMULADOR (una puja de K acciones, JOIN+C0) frente a la población 'primeras K acciones' (mismos mercados completos y días) ==")
    for k in (5, 25, 50):
        for cola in ("CONS", "OPT"):
            if cola == "OPT" and k != 5:
                continue
            S = U[U.motor == f"JOIN|C0|{cola}|{k}"]
            S = S[S.lleno > 0]
            a, f = ctrl[k]
            L.append(f"  K={k:2d} {cola}: sim pool {ev_pool(S.pnl, S.coste):+.4f} media {ev_medio(S.pnl, S.coste):+.4f} n {len(S):5d} | "
                     f"pob primeras-K pool {ev_pool(a.pnl_k, a.coste_k):+.4f} (n {len(a)}), final {ev_pool(f.pnl_k, f.coste_k):+.4f} (n {len(f)})")
    cons = U[(U.motor == MOTORES[0]) & (U.lleno > 0)]
    opt = U[(U.motor == MOTORES[1]) & (U.lleno > 0)]
    ev_c, ev_o = ev_pool(cons.pnl, cons.coste), ev_pool(opt.pnl, opt.coste)
    v = veredicto_objeto(ev_pool(ctrl[5][1].pnl_k, ctrl[5][1].coste_k), ev_c, ev_o)
    res["veredicto_objeto_comparable"] = v
    L.append(f"  VEREDICTO (POST HOC, mismo haz que el original, población 'final' primeras 5 acc): {v['estado']}"
             + (f" | población {v['ev_poblacion_primeras_k']:+.4f} en [{v['haz'][0]:+.4f}, {v['haz'][1]:+.4f}]" if "haz" in v else ""))
    L.append("  Por día (pool): población primeras-5 / sim CONS 5")
    a5 = ctrl[5][0]
    for d in dias:
        x, s = a5[a5.dia == d], cons[cons.dia == d]
        L.append(f"    {d}: pob {ev_pool(x.pnl_k, x.coste_k):+.4f} (n {len(x)}) | sim {ev_pool(s.pnl, s.coste):+.4f} (n {len(s)})")
    L.append("  Por moneda (pool): población primeras-5 / sim CONS 5")
    for c in MONEDAS:
        x, s = a5[a5.act == c], cons[cons.act == c]
        L.append(f"    {c:5}: pob {ev_pool(x.pnl_k, x.coste_k):+.4f} (n {len(x)}) | sim {ev_pool(s.pnl, s.coste):+.4f} (n {len(s)})")
    # --- 3. tabla 2x2 por unidad
    PU = P.groupby(["dia", "mkt", "lado_c"], sort=False).agg(act=("act", "first"), pnl_p=("pnl", "sum"), coste_p=("coste", "sum")).reset_index() \
        .rename(columns={"lado_c": "lado"})
    PU = PU.merge(ctrl[5][0][["dia", "mkt", "lado", "pnl_k", "coste_k"]], on=["dia", "mkt", "lado"], how="left")
    for mot in MOTORES:
        S = U[U.motor == mot][["dia", "mkt", "lado", "act", "norders", "lleno", "pnl", "coste"]].rename(
            columns={"act": "act_s", "pnl": "pnl_s", "coste": "coste_s"})
        A = tabla_2x2(uni, PU, S)
        A["act"] = A.act.fillna(A.act_s)
        L.append(f"\n== 3. 2x2 por unidad (mercado-lado) -- {mot} (universo {len(A)} unidades de mercados completos) ==")
        L.append("  pob sí/no x sim rellena/cotiza sin relleno/nunca cotiza: n | EV pob unidad completa | EV pob primeras-5 | EV sim")
        for (pp, ss), g in A.groupby(["pop", "sim"]):
            t = f"  pob={'sí' if pp else 'no':2} sim={ss:19} n {len(g):5d}"
            if pp:
                t += f" | EVpob {ev_pool(g.pnl_p, g.coste_p):+.4f}"
                gk = g[g.coste_k.notna()]
                t += f" | EVpob5 {ev_pool(gk.pnl_k, gk.coste_k):+.4f}"
            if ss == "rellena":
                t += f" | EVsim {ev_pool(g.pnl_s, g.coste_s):+.4f}"
            L.append(t)
        res[f"celdas_{mot}"] = {f"{'pob' if pp else 'nopob'}|{ss}": int(len(g)) for (pp, ss), g in A.groupby(["pop", "sim"])}
        L.append("  Por moneda: A=pob&sim rellena | B=pob&sim no rellena | C=no pob&sim rellena | D=ninguno")
        for c in MONEDAS:
            g = A[A.act == c]
            nA = int((g["pop"] & (g.sim == "rellena")).sum())
            nB = int((g["pop"] & (g.sim != "rellena")).sum())
            nC = int((~g["pop"] & (g.sim == "rellena")).sum())
            nD = int((~g["pop"] & (g.sim != "rellena")).sum())
            gA, gB, gC = g[g["pop"] & (g.sim == "rellena")], g[g["pop"] & (g.sim != "rellena")], g[~g["pop"] & (g.sim == "rellena")]
            L.append(f"    {c:5}: A {nA:4d} (EVpob {ev_pool(gA.pnl_p, gA.coste_p):+.3f}, EVsim {ev_pool(gA.pnl_s, gA.coste_s):+.3f}) | "
                     f"B {nB:4d} (EVpob {ev_pool(gB.pnl_p, gB.coste_p):+.3f}) | C {nC:3d} (EVsim {ev_pool(gC.pnl_s, gC.coste_s):+.3f}) | D {nD:4d}")
    return "\n".join(L), res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--dias", default=",".join(DIAS))
    a = ap.parse_args()
    out = Path(a.out)
    txt, res = informe(out, [d for d in a.dias.split(",") if d])
    for nom, dat in (("diag_calibracion_objeto.txt", txt + "\n"), ("diag_calibracion_objeto.json", json.dumps(res, indent=1, default=str))):
        tmp = out / (nom + f".tmp{os.getpid()}")
        tmp.write_text(dat)
        os.replace(tmp, out / nom)
    print(txt)


if __name__ == "__main__":
    main()
