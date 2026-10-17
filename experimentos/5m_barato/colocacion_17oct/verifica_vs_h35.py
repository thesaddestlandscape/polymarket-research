#!/usr/bin/env python3
"""Regresión contra la caché de H35 (NO se modifica): las unidades de LÍNEA BASE de coloc (primera decisión, motores DEEP_k1, DEEP_k2, JOIN)
deben coincidir con las de `m5_maker_banda_deep_peg/unidades_D.csv.gz` (mismas claves dia,motor,mkt,lado,tramo) en lleno/coste/norders.
Uso: python3 verifica_vs_h35.py --dia 2026-10-10 [--base-dir DIR]   (compara base_D.csv.gz de coloc con la caché de H35)"""
import argparse
import sys
from pathlib import Path

import pandas as pd

H35 = Path("/root/polymarket-research-datalogs/m5_maker_banda_deep_peg")
OUT = Path("/root/polymarket-research-datalogs/m5_maker_colocacion")
MOT = ["DEEP_k1|C0|CONS|5", "DEEP_k2|C0|CONS|5", "JOIN|C0|CONS|5"]


def comparar(B, U, solo_mkts=None, tol=1e-4):
    """B, U: DataFrames con columnas motor, mkt, lado, tramo, lleno, coste, norders. -> dict de resultados."""
    r = {}
    for mot in MOT:
        b = B[B.motor == mot].set_index(["mkt", "lado", "tramo"])
        u = U[U.motor == mot].set_index(["mkt", "lado", "tramo"])
        if solo_mkts is not None:
            b = b[b.index.get_level_values(0).isin(solo_mkts)]
            u = u[u.index.get_level_values(0).isin(solo_mkts)]
        idx = b.index.intersection(u.index)
        dl = (b.loc[idx, "lleno"] - u.loc[idx, "lleno"]).abs()
        dc = (b.loc[idx, "coste"] - u.loc[idx, "coste"]).abs()
        dn = (b.loc[idx, "norders"] - u.loc[idx, "norders"]).abs()
        r[mot] = {"unidades_coloc": len(b), "unidades_h35": len(u), "comunes": len(idx), "solo_coloc": len(b.index.difference(u.index)),
                  "solo_h35": len(u.index.difference(b.index)), "dif_lleno>tol": int((dl > tol).sum()), "dif_coste>tol": int((dc > tol).sum()),
                  "dif_norders": int((dn > 0).sum())}
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dia", required=True)
    ap.add_argument("--base-dir", default=str(OUT))
    a = ap.parse_args()
    B = pd.read_csv(Path(a.base_dir) / f"base_{a.dia}.csv.gz", dtype={"mkt": str})
    U = pd.read_csv(H35 / f"unidades_{a.dia}.csv.gz", dtype={"mkt": str})
    r = comparar(B, U)
    ok = True
    for mot, v in r.items():
        print(mot, v)
        ok &= v["comunes"] > 0 and v["dif_lleno>tol"] == 0 and v["dif_coste>tol"] == 0 and v["dif_norders"] == 0 and v["solo_coloc"] == 0
    print("REGRESION_OK" if ok else "REGRESION_DIFIERE")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
