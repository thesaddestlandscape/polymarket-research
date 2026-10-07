#!/usr/bin/env python3
"""analisis_15m_s24_patas.py -- MISIÓN DEFINITIVA 15m §24 (07-Oct): ¿qué pata del movimiento tiene PnL neto capturable?
Evento (pata 1, fijado antes de mirar): el mid YES del 15m se mueve >= 3 c en 1 s (|y_vel_1s| >= 0,03). 1 por mercado-minuto.
  PATA 2 (continuación): comprar el lado del movimiento al ask REAL a +215 ms.  PATA 3 (reversión): comprar el contrario.
  Salidas: bid real a +215 ms + 5 s / + 30 s (ida y vuelta, fee en ambas patas) y resolución oficial (fee de entrada).
  Cortes: Binance 1 s en el MISMO sentido (|bn_ret_1s| >= 1 bps) vs no.
Datos: m15_maestro_06oct.csv (DISC/VALID/FINAL de A1-A3) y m15_maestro_07oct.csv (06-Oct 12:30 → 07-Oct 08:30 = OOS2;
se solapa con FINAL 06-Oct 12:30-24:00: se reporta como bloque aparte). PnL por € con comision_cripto.pnl_por_euro.
Uso: (ulimit -v 3500000; nice -n 10 python3 analisis_15m_s24_patas.py)
"""
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comision_cripto import pnl_por_euro, FEE_CRIPTO  # noqa: E402

COLS = ["market", "cierre", "t", "desenlace", "t_desde_inicio_s", "y_vel_1s", "bn_ret_1s_bps", "Y_askY_215", "Y_askN_215",
        "Y_bidY_5000", "Y_bidN_5000", "Y_bidY_30000", "Y_bidN_30000"]


def ms(s):
    return int(datetime.fromisoformat(s).replace(tzinfo=timezone.utc).timestamp() * 1000)


def per_de(t, fuente):
    if fuente == "07oct":
        return np.full(len(t), "OOS2")
    return np.select([t < ms("2026-10-06T02:00"), (t >= ms("2026-10-06T03:30")) & (t < ms("2026-10-06T09:30")),
                      t >= ms("2026-10-06T09:30")], ["DISC", "VALID", "FINAL"], "EMB")


def rt(a, b):
    ok = (a > 0) & (a < 1) & (b > 0)
    return np.where(ok, (b - a - FEE_CRIPTO * a * (1 - a) - FEE_CRIPTO * b * (1 - b)) / (a * (1 + FEE_CRIPTO * (1 - a))), np.nan)


def main():
    filas = []
    for fuente, f in (("06oct", "m15_maestro_06oct.csv"), ("07oct", "m15_maestro_07oct.csv")):
        d = pd.read_csv(f"/root/polymarket-research-datalogs/{f}", usecols=lambda c: c in COLS)
        d = d[d.y_vel_1s.abs() >= 0.03].copy()
        d["min"] = (d.t_desde_inicio_s // 60).astype(int)
        d = d.sort_values("t").drop_duplicates(["market", "min"])
        d["per"] = per_de(d.t.values, fuente)
        filas.append(d)
    E = pd.concat(filas)
    up = E.y_vel_1s.values > 0
    gana_yes = (E.desenlace.values == "YES").astype(int)
    aY, aN = E.Y_askY_215.values, E.Y_askN_215.values
    for nom, compra_yes in (("PATA2_continua", up), ("PATA3_revierte", ~up)):
        a = np.where(compra_yes, aY, aN)
        g = np.where(compra_yes, gana_yes, 1 - gana_yes)
        E[f"{nom}_res"] = [pnl_por_euro(x, y) if 0 < x < 1 else np.nan for x, y in zip(a, g)]
        E[f"{nom}_rt5"] = rt(a, np.where(compra_yes, E.Y_bidY_5000.values, E.Y_bidN_5000.values))
        E[f"{nom}_rt30"] = rt(a, np.where(compra_yes, E.Y_bidY_30000.values, E.Y_bidN_30000.values))
    E["bn_mismo"] = np.sign(E.bn_ret_1s_bps.fillna(0)) * np.sign(E.y_vel_1s) > 0
    E.loc[E.bn_ret_1s_bps.abs() < 1, "bn_mismo"] = False
    rng = np.random.default_rng(24)
    print(f"eventos (|Δmid 1 s| >= 3 c, 1 por mercado-minuto): {len(E)} | por periodo: {E.per.value_counts().to_dict()}")
    for per in ("DISC", "VALID", "FINAL", "OOS2"):
        g0 = E[E.per == per]
        for corte, g in (("todos", g0), ("Binance mismo sentido", g0[g0.bn_mismo]), ("sin Binance", g0[~g0.bn_mismo])):
            lin = []
            for nom in ("PATA2_continua", "PATA3_revierte"):
                for k in ("rt5", "rt30", "res"):
                    v = g[f"{nom}_{k}"]
                    ok = v.notna()
                    c = g[ok].groupby("cierre")[f"{nom}_{k}"].agg(["sum", "count"])
                    if len(c) >= 5:
                        S, N = c["sum"].values, c["count"].values
                        bs = [S[x].sum() / N[x].sum() for x in (rng.integers(0, len(S), len(S)) for _ in range(500))]
                        lin.append(f"{nom[:5]}{nom[-8:]} {k}: {v[ok].mean():+.3f} ({np.percentile(bs, 5):+.3f},{np.percentile(bs, 95):+.3f})")
            print(f"{per:5} {corte:22} n={len(g):4} | " + " | ".join(lin))


if __name__ == "__main__":
    main()
