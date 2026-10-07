#!/usr/bin/env python3
"""analisis_wm_eth15m_021_024_verificacion_07oct.py -- verificación INDEPENDIENTE (Javi 07-Oct: "sí, haz la verificación")
de la zona quirúrgica WALLET_MIRROR#ETH#15min#g0 [0,21-0,24) (forward n=45, +0,62, IC90 [+0,13,+1,12], top1 40 %).
Criterios fijados antes de mirar:
  1. Fuente: wallet_mirror_executor_dryrun.csv + reconstruido 08-22 Sep (solo filas anteriores a su corte), ETH 15min,
     es_jugada_grande=0, sigue_fillable_en_decision=1, resuelta (acierto 0/1), excluye pre-TWAP (07-Ago).
  2. Precio = ask_decision (NUESTRO ask al decidir con nuestra latencia). Comisión REAL del tomador 0,07·p·(1−p) por
     acción en cada compra: PnL/€ = acierto / (p·(1 + 0,07·(1−p))) − 1.
  3. UNA fila por (mercado, lado): la primera señal (no inflar n con fills de varias wallets/repeticiones).
  4. TRAIN < 2026-09-30 <= FORWARD. IC90 bootstrap por DÍAS, sin los 2 mejores días, días positivos.
  5. Sin la wallet top del forward; concentración por wallet.
  6. Vecinos [0,18-0,21) y [0,24-0,27); y por tipo de wallet.
Solo lectura. Uso: python3 analisis_wm_eth15m_021_024_verificacion_07oct.py
"""
import collections
import csv
import sys
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import shadow_postmortem as sp  # noqa: E402  (es_pre_twap: misma exclusión que el cargador del gate)

FUENTES = [REPO / "data/shadow/wallet_mirror_executor_dryrun.csv",
           REPO / "data/shadow/wallet_mirror_executor_dryrun_reconstruido_08_22sep.csv"]
CORTE_RECON = "2026-09-22T23:59:59"
CUTOFF = "2026-09-30"


def pnl(p, ac):
    return ac / (p * (1 + 0.07 * (1 - p))) - 1


def cargar():
    filas, vistos = [], set()
    for k, f in enumerate(FUENTES):
        if not f.exists():
            continue
        for r in csv.DictReader(open(f, encoding="utf-8")):
            if k == 1 and r["timestamp_utc"][:19] > CORTE_RECON:
                continue
            if r.get("activo") != "ETH" or r.get("marco") != "15min" or r.get("es_jugada_grande") == "1":
                continue
            if r.get("sigue_fillable_en_decision") != "1" or r.get("acierto") not in ("0", "1"):
                continue
            if sp.es_pre_twap("15min", r["timestamp_utc"]):
                continue
            try:
                p = float(r["ask_decision"])
            except (TypeError, ValueError):
                continue
            if not 0 < p < 1:
                continue
            clave = (r["timestamp_utc"], r["wallet"], r["market_slug"], r["mirror_lado"])
            if clave in vistos:
                continue
            vistos.add(clave)
            filas.append((r["timestamp_utc"], r["market_slug"], r["mirror_lado"], r["wallet"], r.get("tipo", "?"), p,
                          int(r["acierto"])))
    filas.sort()
    return filas


def resumen(nom, xs, rng):
    if len(xs) < 3:
        print(f"   {nom:40} n={len(xs)}")
        return
    v = np.array([pnl(p, a) for (_, _, _, _, _, p, a) in xs])
    dias = collections.defaultdict(list)
    for x, val in zip(xs, v):
        dias[x[0][:10]].append(val)
    D = sorted(dias)
    S = np.array([sum(dias[d]) for d in D])
    N = np.array([len(dias[d]) for d in D])
    bs = [S[k].sum() / N[k].sum() for k in (rng.integers(0, len(D), len(D)) for _ in range(4000))]
    o = np.argsort(-S)
    sin2 = (S.sum() - S[o[:2]].sum()) / max(1, N.sum() - N[o[:2]].sum())
    hit = np.mean([a for *_, a in xs])
    pm = np.mean([p for *_, p, _ in xs])
    wal = collections.Counter(x[3] for x in xs)
    top, ntop = wal.most_common(1)[0]
    print(f"   {nom:40} n={len(xs):4} días={len(D):2} ({(S > 0).sum()}+) | acierto {hit:.3f} vs precio medio {pm:.3f} | "
          f"PnL/€ {v.mean():+.3f} IC90 días ({np.percentile(bs, 5):+.3f},{np.percentile(bs, 95):+.3f}) sin 2 mejores "
          f"{sin2:+.3f} | wallet top {ntop / len(xs):.0%} ({top[:10]})")
    return top


def main():
    rng = np.random.default_rng(7)
    F = cargar()
    print(f"filas ETH 15m g0 ejecutables resueltas: {len(F)} ({F[0][0][:10]} -> {F[-1][0][:10]})")
    uno, vistos = [], set()
    for x in F:                                       # 1 por (mercado, lado): primera señal
        k = (x[1], x[2])
        if k not in vistos:
            vistos.add(k)
            uno.append(x)
    for lo, hi in ((0.18, 0.21), (0.21, 0.24), (0.24, 0.27)):
        print(f"\n=== banda [{lo:.2f}-{hi:.2f}) ===")
        for nom, base in (("TODAS las filas (como el quirúrgico)", F), ("1 por mercado-lado", uno)):
            z = [x for x in base if lo - 1e-9 <= x[5] < hi - 1e-9]
            tr = [x for x in z if x[0][:10] < CUTOFF]
            fw = [x for x in z if x[0][:10] >= CUTOFF]
            print(f" {nom}:")
            resumen("TRAIN", tr, rng)
            top = resumen("FORWARD (>= 30-Sep)", fw, rng)
            if top and lo == 0.21:
                resumen("FORWARD sin la wallet top", [x for x in fw if x[3] != top], rng)
                resumen("TRAIN sin esa misma wallet", [x for x in tr if x[3] != top], rng)
                for t in sorted({x[4] for x in fw}):
                    resumen(f"FORWARD tipo {t}", [x for x in fw if x[4] == t], rng)


if __name__ == "__main__":
    main()
