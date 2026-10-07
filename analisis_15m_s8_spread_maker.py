#!/usr/bin/env python3
"""analisis_15m_s8_spread_maker.py -- MISIÓN DEFINITIVA 15m §8 (spread mining) + §18 (arbitraje de ejecución), 07-Oct.
Pregunta: cuando el spread de un 15m es ancho, ¿una puja post-only DENTRO del spread captura NET EXECUTABLE EDGE?
Si se llenan las dos patas (YES a bb_y+0,01 y NO a bb_n+0,01) el par cuesta 1 − spread + 0,02 -> beneficio
GARANTIZADO spread − 0,02 sin predecir el ganador; si solo se llena una, riesgo direccional + selección adversa.

POLÍTICA (fijada antes de mirar): SPREAD_k, k = 2, 3, 4 céntimos. Por token: mientras (ask − mejor bid de los DEMÁS) >= k,
mantener una puja post-only de SH=5 acciones en (mejor bid de los demás + 0,01) -> primera en su nivel (cola 0). Si el
libro cambia, la recolocación/cancelación es efectiva a RECEPCIÓN + L (L = 40 ms: firma 6 + ida ~34, medido 07-Oct con
órdenes reales); mientras tanto la puja vieja sigue expuesta (atropello). Relleno: operación vendedora (taker SELL) a
precio <= nuestro precio con hora del exchange mientras la puja está activa (vamos primeros); acumula hasta SH.
Tope 50 acciones por token y mercado. Ventana [inicio+5 s, cierre−10 s], precio en [0,05-0,95].
PnL a resolución oficial + rebate maker estimado (0,2 x 0,07·p(1−p) por acción, rebateRate verificado 07-Oct).
Periodos A1-A3: DISC (diseño) / VALID / FINAL; IC90 bootstrap de CIERRES; por moneda; pares completos vs patas sueltas.
Uso: (ulimit -v 4500000; nice -n 19 ionice -c3 python3 analisis_15m_s8_spread_maker.py)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from m15_ms_cache import cargar  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from analisis_15m_A_quote_age import periodo  # noqa: E402

SH, MAX_SH, L = 5.0, 50.0, 40
KS = (2, 3, 4)


def simular(te, tr, bb, ba, T_te, T_p, T_side, T_sz, t0, t1, k):
    """Puja propia dentro del spread de UN token. -> (acciones, coste, n_rellenos)."""
    # acciones de la puja: (t_efectivo, precio o None) decididas al RECIBIR cada cambio del libro
    acc_t, acc_p = [], []
    for i in range(len(te)):
        if te[i] > t1:
            break
        b, a = bb[i], ba[i]
        p = None
        if np.isfinite(b) and np.isfinite(a) and a - b >= k / 100 - 1e-9:
            p = round(float(b) + 0.01, 2)
            if not (0.05 <= p <= 0.95) or p >= a - 1e-9:
                p = None
        if not acc_p or p != acc_p[-1]:
            acc_t.append(tr[i] + L)
            acc_p.append(p)
    acc_t = np.array(acc_t, dtype=np.int64)
    sh = coste = 0.0
    nrel = 0
    j0 = np.searchsorted(T_te, t0)
    for j in range(j0, len(T_te)):
        t = T_te[j]
        if t > t1 or sh >= MAX_SH:
            break
        if T_side[j] != 0:                 # solo tomadores VENDEDORES llenan una puja
            continue
        a = np.searchsorted(acc_t, t, side="right") - 1
        if a < 0 or acc_p[a] is None:
            continue
        mi = acc_p[a]
        if T_p[j] <= mi + 1e-9:
            q = min(float(T_sz[j]), SH, MAX_SH - sh)
            if q > 0:
                sh += q
                coste += q * mi
                nrel += 1
    return sh, coste, nrel


def main():
    C = cargar()
    q, tt = C["q"], C["t"]
    toks = C["tokens"]
    des = desenlaces({k[2] for k in toks})
    bq = np.searchsorted(q["tok"], np.arange(len(toks) + 1))
    bt = np.searchsorted(tt["tok"], np.arange(len(toks) + 1))
    filas = []
    for i, (tk, act, mid_, fin, lado) in enumerate(toks):
        if mid_ not in des:
            continue
        a, b = bq[i], bq[i + 1]
        if b - a < 50:
            continue
        te, tr = q["te"][a:b], q["tr"][a:b]
        bb, ba = q["bb"][a:b].astype(np.float64), q["ba"][a:b].astype(np.float64)
        ta, tb = bt[i], bt[i + 1]
        T_te, T_p = tt["te"][ta:tb], tt["p"][ta:tb].astype(np.float64)
        T_side, T_sz = tt["side"][ta:tb], tt["sz"][ta:tb].astype(np.float64)
        t0, t1 = (fin - 900) * 1000 + 5000, fin * 1000 - 10_000
        gana = 1.0 if des[mid_] == lado else 0.0
        for k in KS:
            sh, coste, nrel = simular(te, tr, bb, ba, T_te, T_p, T_side, T_sz, t0, t1, k)
            pm = coste / sh if sh else 0.0
            reb = 0.2 * 0.07 * pm * (1 - pm) * sh
            filas.append((k, act, mid_, fin, lado, sh, coste, nrel, sh * gana - coste, sh * gana - coste + reb))
    R = pd.DataFrame(filas, columns=["k", "act", "mkt", "fin", "lado", "acc", "coste", "nrel", "pnl", "pnl_reb"])
    R["per"] = periodo((R["fin"].values - 450) * 1000)
    R.to_parquet("/root/polymarket-research-datalogs/m15_ms_cache/s8_spread_maker.parquet")
    rng = np.random.default_rng(8)
    # por mercado: YES+NO; pares completos = acciones emparejadas min(acc_yes, acc_no)
    P = R.pivot_table(index=["k", "per", "act", "mkt", "fin"], columns="lado",
                      values=["acc", "coste", "pnl", "pnl_reb"], aggfunc="sum").fillna(0)
    P.columns = [f"{a}_{b}" for a, b in P.columns]
    lados = sorted({c.split("_", 1)[1] for c in P.columns if c.startswith("acc_")})
    P["acc"] = sum(P[f"acc_{l}"] for l in lados)
    P["par"] = np.minimum(*(P[f"acc_{l}"] for l in lados)) if len(lados) == 2 else 0
    P["pnl"] = sum(P[f"pnl_{l}"] for l in lados)
    P["pnl_reb"] = sum(P[f"pnl_reb_{l}"] for l in lados)
    P = P.reset_index()
    print("§8 SPREAD_k: puja post-only en mejor bid + 1c mientras el spread de los demás >= k; L = 40 ms; SH = 5")
    print(f"{'k':>2} {'per':5} | {'merc':>4} {'%c/relleno':>10} {'acc':>6} {'pares':>6} | {'$/merc':>7} {'+rebate':>8} "
          f"{'IC90 cierres':>18} {'sin mejor':>9}")
    for (k, per), g in P.groupby(["k", "per"]):
        if per == "EMB":
            continue
        cie = g.groupby("fin")["pnl_reb"].agg(["sum", "count"])
        S, N = cie["sum"].values, cie["count"].values
        bs = [S[x].sum() / N[x].sum() for x in (rng.integers(0, len(S), len(S)) for _ in range(1000))]
        o = np.argsort(-S)
        sin = (S.sum() - S[o[0]]) / (N.sum() - N[o[0]])
        print(f"{k:2} {per:5} | {len(g):4} {100 * (g.acc > 0).mean():9.0f}% {g.acc.sum():6.0f} {g.par.sum():6.0f} | "
              f"{g.pnl.mean():+7.3f} {g.pnl_reb.mean():+8.3f} ({np.percentile(bs, 5):+.3f},{np.percentile(bs, 95):+.3f}) "
              f"{sin:+9.3f}")
    print("\nPor moneda (VALID+FINAL, $/mercado con rebate):")
    G = P[P.per.isin(["VALID", "FINAL"])].groupby(["k", "act"])["pnl_reb"].mean().unstack()
    print(G.round(3).to_string())
    print("\nDescomposición (todas las k, VALID+FINAL): PnL de la parte EMPAREJADA (garantizada) vs patas sueltas")
    for k, g in P[P.per.isin(["VALID", "FINAL"])].groupby("k"):
        # coste medio por acción de cada lado -> parte emparejada = par x (1 − precio medio YES − precio medio NO)
        py = (g[f"coste_{lados[0]}"] / g[f"acc_{lados[0]}"].replace(0, np.nan)).fillna(0)
        pn = (g[f"coste_{lados[1]}"] / g[f"acc_{lados[1]}"].replace(0, np.nan)).fillna(0)
        garant = (g["par"] * (1 - py - pn)).where(g["par"] > 0, 0)
        print(f"   k={k}: emparejado {garant.sum():+8.2f} $ ({g.par.sum():.0f} pares) | resto (patas sueltas) "
              f"{(g.pnl - garant).sum():+8.2f} $ | total {g.pnl.sum():+8.2f} $ en {len(g)} mercados")


if __name__ == "__main__":
    main()
