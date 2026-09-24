#!/usr/bin/env python3
"""analisis_sports_fade_wallets_extremas_24sep.py -- ¿rinde más el FADE de las
wallets de sports con edge MUY negativo que el FADE en general? (24-Sep,
petición Javi: "tenemos que sacarle pasta a eso").

Origen: el tracker (sports_wallet_edge_tracker.py) valida wallets con edge
muy negativo (ej. hit 0% comprando a 0,89, n=25-33). El gate existente
(analisis_sports_wallet_mirror_gate_bucket_26ago.py) agrupa FADE por
categoria x bucket de precio, pero NUNCA por lo mala que es la wallet.

Rigor (lo que la validación del tracker NO tiene):
- Fuera de muestra: solo señales del dry-run del sniper, cada una con el
  edge_pp_validado que tenía la wallet EN ESE MOMENTO (validada con datos
  anteriores a la señal).
- Precio ejecutable: mejor_ask_mirror real del lado contrario en detección,
  ratio_vs_stake >= 5 (mismo RATIO_MIN que el gate), fee sports 0,05.
- Independencia: 1 unidad por (condition_id, lado espejo), el PRIMER disparo;
  n de días y de wallets distintas, cuota de la wallet top.
- CI90 bootstrap POR BLOQUES DE DÍA (no por fila), split-half temporal.
- Incremental sobre el precio: permutación de la etiqueta de tramo DENTRO de
  cada bucket de precio 0,05 (estadístico = media de acierto-ask del tramo).
Solo lectura, no toca nada operativo.
"""
import csv
import json
import zlib
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from analisis_sports_wallet_mirror_gate_bucket_26ago import (  # noqa: E402
    DRY_RUN, RATIO_MIN, STAKE, bucket, payout_win, wilson_lo)

OUT = REPO / "data/sports/fade_wallets_extremas_24sep.json"
TRAMOS = [(-1e9, -40.0, "<=-40pp"), (-40.0, -20.0, "(-40,-20]"),
          (-20.0, -10.0, "(-20,-10]"), (-10.0, 0.0, "(-10,0)")]
N_MIN_UNIDADES = 40
ITERS = 2000


def tramo(e: float):
    for lo, hi, nombre in TRAMOS:
        if lo < e <= hi if hi < 0 else lo < e < hi:
            return nombre
    return None


def cargar():
    """Primer disparo FADE fillable y resuelto por (condition_id, lado espejo)."""
    primeros = {}
    with open(DRY_RUN, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("tipo") != "FADE" or r.get("acierto") not in ("0", "1"):
                continue
            try:
                ask = float(r["mejor_ask_mirror"])
                ratio = float(r["ratio_vs_stake_mirror"])
                e = float(r["edge_pp_validado"])
            except (TypeError, ValueError, KeyError):
                continue
            if ratio < RATIO_MIN or not (0.01 < ask < 0.99):
                continue
            k = (r["condition_id"], r["mirror_outcome_index"])
            ts = r["timestamp_utc"]
            if k not in primeros or ts < primeros[k]["ts"]:
                primeros[k] = {"ts": ts, "dia": ts[:10], "ask": ask, "acierto": int(r["acierto"]),
                               "edge": e, "wallet": r["wallet"], "cat": r["categoria"]}
    return list(primeros.values())


def boot_dia(unidades, seed):
    """CI90 de pnl medio remuestreando DÍAS enteros (bloques)."""
    por_dia = defaultdict(list)
    for u in unidades:
        por_dia[u["dia"]].append(u["pnl"])
    dias = list(por_dia.values())
    rng = np.random.default_rng(seed)
    medias = []
    for _ in range(ITERS):
        idx = rng.integers(0, len(dias), len(dias))
        v = [x for i in idx for x in dias[i]]
        medias.append(np.mean(v))
    return float(np.percentile(medias, 5)), float(np.percentile(medias, 95))


def resumen(nombre, us, seed):
    n = len(us)
    if n == 0:
        return {"n": 0}
    us = sorted(us, key=lambda u: u["ts"])
    hit = sum(u["acierto"] for u in us) / n
    ask = sum(u["ask"] for u in us) / n
    pnl = sum(u["pnl"] for u in us) / n
    h = n // 2
    wal = defaultdict(int)
    for u in us:
        wal[u["wallet"]] += 1
    d = {"n_unidades": n, "n_dias": len({u["dia"] for u in us}), "n_wallets": len(wal),
         "top_wallet_pct": round(max(wal.values()) / n, 3), "hit": round(hit, 4),
         "ask_medio": round(ask, 4), "wilson90lo": round(wilson_lo(hit, n), 4),
         "pnl_medio": round(pnl, 4), "exceso_hit_vs_ask_pp": round((hit - ask) * 100, 2)}
    if n >= 10:
        d["split_half"] = [round(float(np.mean([u["pnl"] for u in us[:h]])), 4),
                           round(float(np.mean([u["pnl"] for u in us[h:]])), 4)]
        lo, hi = boot_dia(us, seed)
        d["ci90_bootstrap_dia"] = [round(lo, 4), round(hi, 4)]
    return d


def perm_incremental(unidades, nombre_tramo, seed):
    """p-valor: ¿el tramo supera a los demás en acierto-ask dentro del MISMO
    bucket de precio? Permuta la etiqueta de tramo dentro de cada bucket."""
    por_b = defaultdict(list)
    for u in unidades:
        por_b[bucket(u["ask"])].append((u["acierto"] - u["ask"], u["tramo"] == nombre_tramo))
    grupos = [(np.array([x[0] for x in v]), np.array([x[1] for x in v])) for v in por_b.values()
              if any(x[1] for x in v) and not all(x[1] for x in v)]
    if not grupos:
        return None
    def stat(gs):
        num = sum(r[m].sum() for r, m in gs)
        den = sum(m.sum() for _, m in gs)
        return num / den if den else 0.0
    obs = stat(grupos)
    rng = np.random.default_rng(seed)
    mayores = 0
    for _ in range(ITERS):
        mayores += stat([(r, rng.permutation(m)) for r, m in grupos]) >= obs
    return round((mayores + 1) / (ITERS + 1), 4)


def main():
    us = cargar()
    for u in us:
        u["pnl"] = payout_win(u["ask"]) if u["acierto"] else -STAKE
        u["tramo"] = tramo(u["edge"])
    us = [u for u in us if u["tramo"]]
    out = {"n_unidades_total": len(us), "fuente": str(DRY_RUN.name),
           "global_fade": resumen("global", us, 1), "por_tramo": {}, "por_tramo_y_precio": {}}
    for i, (_, _, nombre) in enumerate(TRAMOS):
        sub = [u for u in us if u["tramo"] == nombre]
        d = resumen(nombre, sub, 10 + i)
        d["p_perm_incremental_vs_precio"] = perm_incremental(us, nombre, 100 + i)
        out["por_tramo"][nombre] = d
        # desagregado por zona de precio 0,10 (CLAUDE.md pt.17)
        zonas = defaultdict(list)
        for u in sub:
            zonas[f"[{int(u['ask'] * 10) / 10:.1f},{int(u['ask'] * 10) / 10 + 0.1:.1f})"].append(u)
        out["por_tramo_y_precio"][nombre] = {z: resumen(z, v, 1000 + zlib.crc32(z.encode()) % 1000)
                                             for z, v in sorted(zonas.items())}
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: out[k] for k in ("n_unidades_total", "global_fade", "por_tramo")},
                     indent=1, ensure_ascii=False))
    print("\nPor tramo x precio (n_unidades>=%d):" % N_MIN_UNIDADES)
    for t, zs in out["por_tramo_y_precio"].items():
        for z, d in zs.items():
            if d.get("n_unidades", 0) >= N_MIN_UNIDADES:
                print(f"  {t:10s} {z} n={d['n_unidades']:4d} dias={d['n_dias']:2d} wal={d['n_wallets']:3d} "
                      f"top={d['top_wallet_pct']:.2f} hit={d['hit']:.3f} ask={d['ask_medio']:.3f} "
                      f"pnl={d['pnl_medio']:+.3f} ci90d={d.get('ci90_bootstrap_dia')} sh={d.get('split_half')}")


if __name__ == "__main__":
    main()
