#!/usr/bin/env python3
"""analisis_15m_v3_fase6_cobertura.py -- MISIÓN 15M V3 FASE 6 (07-Oct): secuencia relleno → reacción → COBERTURA.
Rellenos pesimistas de las órdenes virtuales de s10 (bid de 5 acciones al final de la cola, reloj de RECEPCIÓN; parquet
v3_maker_cross de analisis_15m_v3_maker_cross.py, con tf_pes = hora del relleno). Regla fijada antes de mirar: al recibir el relleno (tf), comprar el lado
CONTRARIO del mismo mercado al ask REAL del registro ms a tf + L (L = 0 / 100 / 250 / 500 ms; 250 ≈ nuestro camino de orden
+ taker delay). Par cubierto: PnL/acción = 1 − P − ask_contrario − fee_tomador(ask_contrario) + rebate_maker(P); garantizado.
Comparar con MANTENER (PnL a resolución + rebate, = res_pes). ¿El lado contrario reacciona tarde (asks viejos)?
Mide también el movimiento del ask contrario entre tf−1 s y tf+L. DISC/VALID (FINAL bloqueado). IC90 por cierres.
Uso: (ulimit -v 5000000; nice -n 19 ionice -c3 python3 analisis_15m_v3_fase6_cobertura.py)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from m15_ms_cache import cargar  # noqa: E402

INF = Path(__file__).resolve().parent / "informes" / "m15v3_fase6_cobertura_07oct.txt"
LS = (0, 100, 250, 500)


def main():
    C = cargar()
    q, toks = C["q"], C["tokens"]
    bq = np.searchsorted(q["tok"], np.arange(len(toks) + 1))
    libro = {}
    for i, (tk, act, mid_, fin, lado) in enumerate(toks):
        a, b = bq[i], bq[i + 1]
        if b - a < 50:
            continue
        o = np.argsort(q["tr"][a:b], kind="stable")
        libro[(str(mid_), lado)] = (q["tr"][a:b][o], q["ba"][a:b][o].astype(float))
    R = pd.read_parquet("/root/polymarket-research-datalogs/m15_ms_cache/v3_maker_cross.parquet")   # mismas órdenes virtuales de s10 --recepcion, con tf_pes
    if "tf_pes" not in R:
        sys.exit("el parquet no tiene tf_pes: re-generar con analisis_15m_s10_cola.py --recepcion")
    R = R[R.lleno_pes & (R.tf_pes > 0) & R.per.isin(["DISC", "VALID"])].copy()
    filas = []
    for r in R.itertuples(index=False):
        otro = libro.get((str(r.mkt), "NO" if r.lado == "YES" else "YES"))
        if otro is None:
            continue
        tr, ba = otro
        f = {"per": r.per, "fin": r.fin, "act": r.act, "P": r.P, "res": r.res_pes, "t_cierre": r.t_cierre}
        k0 = np.searchsorted(tr, int(r.tf_pes) - 1000, side="right") - 1
        f["ask_pre"] = ba[k0] if k0 >= 0 else np.nan
        reb = 0.2 * 0.07 * r.P * (1 - r.P)
        for L in LS:
            k = np.searchsorted(tr, int(r.tf_pes) + L, side="right") - 1
            a2 = ba[k] if k >= 0 else np.nan
            f[f"ask{L}"] = a2
            f[f"cub{L}"] = 1 - r.P - a2 - 0.07 * a2 * (1 - a2) + reb if np.isfinite(a2) else np.nan
        filas.append(f)
    D = pd.DataFrame(filas)
    rng = np.random.default_rng(4)

    def ic(g, col):
        g = g[g[col].notna()]
        c, n = g.groupby("fin")[col].sum(), g.groupby("fin").size()
        bs = [c.iloc[ix].sum() / n.iloc[ix].sum() for ix in (rng.integers(0, len(c), len(c)) for _ in range(500))]
        return np.percentile(bs, [5, 95])
    L_ = []
    P = lambda *x: L_.append(" ".join(str(y) for y in x))
    P("MISIÓN 15M V3 FASE 6 — cubrir el relleno comprando el lado contrario al ask real (recepción), por ACCIÓN rellenada")
    for per in ("DISC", "VALID"):
        g = D[D.per == per]
        lo, hi = ic(g, "res")
        P(f"\n{per}: rellenos {len(g)} | MANTENER (resolución) {g.res.mean():+.4f} IC90 ({lo:+.4f},{hi:+.4f})")
        P(f"  ask contrario 1 s ANTES del relleno: media {g.ask_pre.mean():.4f}; suma P + ask_pre media {(g.P + g.ask_pre).mean():.4f}")
        for L in LS:
            lo, hi = ic(g, f"cub{L}")
            P(f"  CUBRIR a +{L:>3} ms: {g[f'cub{L}'].mean():+.4f} IC90 ({lo:+.4f},{hi:+.4f}) | ask contrario {g[f'ask{L}'].mean():.4f} "
              f"(subió {(g[f'ask{L}'] - g.ask_pre).mean():+.4f} desde tf−1 s) | % pares con PnL>0 {(g[f'cub{L}'] > 0).mean():.1%}")
        P("  por fase (cubrir +250 / mantener): " + "  ".join(
            f"T-{hi_}..{lo_}: {x.cub250.mean():+.3f}/{x.res.mean():+.3f}" for (lo_, hi_) in ((600, 900), (300, 600), (70, 300))
            for x in [g[(g.t_cierre > lo_) & (g.t_cierre <= hi_)]]))
    INF.write_text("\n".join(L_) + "\n")
    print("\n".join(L_))


if __name__ == "__main__":
    main()
