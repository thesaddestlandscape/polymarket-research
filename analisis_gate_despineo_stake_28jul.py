#!/usr/bin/env python3
"""
analisis_gate_despineo_stake_28jul.py — gate de reapertura del despineo de
max_stake_eur (28-Jul, ver _max_stake_nota en data/live/config_live.json).

La vez anterior que se despineó el stake (07-Jul, 1.05€→1.75€) salió con
correlación NEGATIVA entre stake_eur y acierto en forward (n=50, corr≈-0.32)
y se re-pineó el mismo día -- con un gate de reapertura ("n≥15 trades
des-pineados limpios") que nunca se llegó a cumplir porque nadie volvió a
mirarlo. Este script es la vigilancia explícita para que no se repita ese
olvido: correlación point-biserial entre stake_eur y acierto (pnl_neto_eur>0)
sobre los trades reales CERRADOS desde la fecha de reapertura, con test de
permutación (no basta con el signo del coeficiente, mismo criterio de rigor
que el resto del proyecto).

Solo lectura -- no toca config_live.json ni decide nada solo. El veredicto
"correlación negativa significativa" es una alerta para que Javi decida
re-pinear, no una acción automática.
"""
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
TRADES_CSV = REPO / "data/live/trades.csv"
OUT_JSON = REPO / "data/shadow/gate_despineo_stake.json"

FECHA_DESPINEO = "2026-07-28T18:55:00+00:00"  # commit del cambio, ver git log
N_MIN = 15
ITERS = 20000
_rng = np.random.default_rng(42)


def cargar_trades_post_despineo():
    if not TRADES_CSV.exists():
        return []
    filas = []
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "CLOSED":
                continue
            cierre = row.get("close_timestamp") or row.get("timestamp_utc") or ""
            if cierre < FECHA_DESPINEO:
                continue
            try:
                stake = float(row["stake_eur"])
                pnl = float(row["pnl_neto_eur"])
            except (KeyError, ValueError):
                continue
            filas.append({"stake": stake, "acierto": 1.0 if pnl > 0 else 0.0,
                          "pnl": pnl, "cierre": cierre,
                          "tupla": f"{row.get('strategy','?')}#{row.get('subtype','?')}#{row.get('direction','?')}"})
    return filas


def correlacion_shuffle(stakes, aciertos, iters=ITERS):
    stakes = np.asarray(stakes, dtype=np.float64)
    aciertos = np.asarray(aciertos, dtype=np.float64)
    if stakes.std() == 0 or aciertos.std() == 0:
        return 0.0, 1.0  # sin varianza (todos el mismo stake o todos ganan/pierden) -- no concluyente
    corr_real = float(np.corrcoef(stakes, aciertos)[0, 1])
    n = len(stakes)
    idx = _rng.random((iters, n)).argsort(axis=1)
    aciertos_perm = aciertos[idx]
    # corr vectorizada: cov(stake, acierto_perm) / (std_stake * std_acierto_perm)
    stakes_c = stakes - stakes.mean()
    aciertos_perm_c = aciertos_perm - aciertos_perm.mean(axis=1, keepdims=True)
    cov = (stakes_c[None, :] * aciertos_perm_c).sum(axis=1)
    std_prod = stakes_c.std() * aciertos_perm_c.std(axis=1) * n
    with np.errstate(divide="ignore", invalid="ignore"):
        corr_perm = np.where(std_prod > 0, cov / std_prod, 0.0)
    p = float((np.abs(corr_perm) >= abs(corr_real)).mean())
    return corr_real, p


def main():
    filas = cargar_trades_post_despineo()
    n = len(filas)
    resultado = {
        "generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "fecha_despineo": FECHA_DESPINEO,
        "n": n,
        "n_min": N_MIN,
    }
    if n < N_MIN:
        resultado["veredicto"] = f"sin_concluir (n={n}/{N_MIN})"
        print(f"[gate_despineo_stake] n={n}/{N_MIN} -- sin concluir todavía")
    else:
        stakes = [f["stake"] for f in filas]
        aciertos = [f["acierto"] for f in filas]
        corr, p = correlacion_shuffle(stakes, aciertos)
        stake_medio = sum(stakes) / n
        stake_variado = len(set(round(s, 2) for s in stakes)) > 1
        if not stake_variado:
            veredicto = f"sin_concluir (todos los trades con el mismo stake={stake_medio:.2f}€ -- Kelly/HRP/boosts aún no han disparado ninguna variación real)"
        elif corr < 0 and p < 0.05:
            veredicto = f"🚨 ALERTA -- correlación NEGATIVA significativa (corr={corr:+.3f}, p={p:.4f}): mismo patrón que el 07-Jul, considerar re-pinear"
        elif corr < 0:
            veredicto = f"correlación negativa pero NO significativa (corr={corr:+.3f}, p={p:.4f}) -- vigilar, no concluyente"
        else:
            veredicto = f"OK -- correlación no negativa (corr={corr:+.3f}, p={p:.4f}), gate pasado"
        resultado.update({"corr": corr, "p_shuffle": p, "stake_medio": round(stake_medio, 3),
                          "veredicto": veredicto})
        print(f"[gate_despineo_stake] n={n} corr={corr:+.3f} p={p:.4f} -- {veredicto}")

    OUT_JSON.write_text(json.dumps(resultado, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Guardado en {OUT_JSON}")


if __name__ == "__main__":
    main()
