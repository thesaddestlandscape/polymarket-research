#!/usr/bin/env python3
"""analisis_15m_v3_precursores.py -- MISIÓN 15M V3 §24-26 (07-Oct): ¿qué se ve ANTES de un barrido, si no es Binance?
Entrada: datalogs/m15_ms_cache/v3_quien_barre.parquet (analisis_15m_v3_quien_barre.py: cada orden tomadora on-chain de 15m
emparejada con su fila t del registro ms, con hora de RECEPCIÓN tr_ms). Todo con NUESTRO reloj de recepción, nada posterior
a tr_ms − 0 ms entra en un precursor. Precursores en la dirección del tomador:
  own  = cambio del mid YES del PROPIO mercado en [tr−2000, tr−100] (recepción)
  cross= media del cambio del mid YES de los 15m de las OTRAS monedas con el MISMO cierre, en [tr−2000, tr−100]
  bin  = retorno Binance de su moneda en [tr−500, tr]
Barrido (descriptivo, usa el futuro): salto del mid >= 4 c (bloque−3 s → +5 s).
Uso: (ulimit -v 5000000; nice -n 19 ionice -c3 python3 analisis_15m_v3_precursores.py)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from m15_ms_cache import cargar  # noqa: E402

DL = Path("/root/polymarket-research-datalogs")
INF = Path(__file__).resolve().parent / "informes" / "m15v3_precursores_07oct.txt"


def main():
    C = cargar()
    q, toks = C["q"], C["tokens"]
    bq = np.searchsorted(q["tok"], np.arange(len(toks) + 1))
    serie = {}
    yes_de = {}
    for i, (tk, act, mid_, fin, lado) in enumerate(toks):
        if lado != "YES":
            continue
        a, b = bq[i], bq[i + 1]
        o = np.argsort(q["tr"][a:b], kind="stable")
        bb, ba = q["bb"][a:b][o].astype(float), q["ba"][a:b][o].astype(float)
        serie[str(mid_)] = (q["tr"][a:b][o], (bb + ba) / 2)
        yes_de.setdefault(int(fin), []).append((act, str(mid_)))

    def mid(m, t):
        s = serie.get(m)
        if s is None:
            return np.nan
        k = np.searchsorted(s[0], t, side="right") - 1
        return s[1][k] if k >= 0 else np.nan

    R = pd.read_parquet(DL / "m15_ms_cache" / "v3_quien_barre.parquet")
    R = R[np.isfinite(R.tr_ms) & (R.t_cierre > 0) & (R.t_cierre <= 900)].copy()
    R["barrido"] = R.salto >= 0.04
    own, cross = [], []
    for r in R.itertuples(index=False):
        t = int(r.tr_ms)
        own.append(r.d * (mid(r.mkt, t - 100) - mid(r.mkt, t - 2000)))
        v = [mid(m, t - 100) - mid(m, t - 2000) for a_, m in yes_de.get(int(r.fin), []) if a_ != r.act]
        v = [x for x in v if np.isfinite(x)]
        cross.append(r.d * np.mean(v) if v else np.nan)
    R["own"], R["cross"] = own, cross
    R["res_usdc"] = R.res * R.acc
    L = []
    P = lambda *a: L.append(" ".join(str(x) for x in a))
    P(f"MISIÓN 15M V3 §24-26 precursores (05-06 Oct, órdenes tomadoras 15m emparejadas: {len(R)}, barridos {R.barrido.sum()})")
    B, N = R[R.barrido], R[~R.barrido]
    for nom, cond in (("Binance 500ms >=1bps", R.b500 >= 1), ("own >=1c", R.own >= 0.01), ("own >=2c", R.own >= 0.02),
                      ("cross >=1c", R.cross >= 0.01), ("cross >=2c", R.cross >= 0.02),
                      ("ALGUNO (bin>=1bps | own>=1c | cross>=1c)", (R.b500 >= 1) | (R.own >= 0.01) | (R.cross >= 0.01))):
        P(f"  {nom:42} en barridos {cond[R.barrido].mean():6.1%}  en no-barridos {cond[~R.barrido].mean():6.1%}  "
          f"EV res|precursor {R[cond].res.mean():+.4f} (n={cond.sum()})  PnL/$ {R[cond].res_usdc.sum() / R[cond].usdc.sum():+.3f}")
    P("\nEV a resolución y % barrido por cubo de 'cross' (otras monedas, mismo cierre, 2 s previos):")
    for lo, hi in ((-1, -0.02), (-0.02, -0.005), (-0.005, 0.005), (0.005, 0.02), (0.02, 1)):
        g = R[(R.cross > lo) & (R.cross <= hi)]
        P(f"  ({lo:+.3f},{hi:+.3f}] n={len(g):>6} %barr {g.barrido.mean():5.1%} EV res {g.res.mean():+.4f} mk30 {g.mk30.mean():+.4f} "
          f"PnL/$ {g.res_usdc.sum() / max(g.usdc.sum(), 1):+.3f}")
    P("\nEV por cubo de 'own' (propio mercado, 2 s previos):")
    for lo, hi in ((-1, -0.02), (-0.02, -0.005), (-0.005, 0.005), (0.005, 0.02), (0.02, 1)):
        g = R[(R.own > lo) & (R.own <= hi)]
        P(f"  ({lo:+.3f},{hi:+.3f}] n={len(g):>6} %barr {g.barrido.mean():5.1%} EV res {g.res.mean():+.4f} mk30 {g.mk30.mean():+.4f} "
          f"PnL/$ {g.res_usdc.sum() / max(g.usdc.sum(), 1):+.3f}")
    sin = R[R.barrido & ~((R.b500 >= 1) | (R.own >= 0.01) | (R.cross >= 0.01))]
    P(f"\nBARRIDOS SIN NINGÚN PRECURSOR visible: {len(sin)} ({len(sin) / len(B):.1%} de los barridos); EV res {sin.res.mean():+.4f}, "
      f"t_cierre mediana {sin.t_cierre.median():.0f} s, tamaño mediano {sin.usdc.median():.1f} $; "
      f"top10 wallets {sin.groupby('wallet').usdc.sum().nlargest(10).sum() / sin.usdc.sum():.1%} del volumen")
    INF.write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
