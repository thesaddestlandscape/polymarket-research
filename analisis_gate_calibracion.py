#!/usr/bin/env python3
"""
Gate de calibración pre-promoción (31-Jul, Opción B tras el hallazgo del
vigía log_loss del mismo día: UPDOWN_GBM_IBS_ALTO es LIVE-CANDIDATA con
IC=+0.219 pero log-loss gap=-0.1735 frente al mercado — sobreconfiada. Ver
memoria idea_gate_calibracion_log_loss_31jul).

Complementa, NO sustituye, a vigia_log_loss_vs_mercado.py: ese vigía avisa
en cuanto una estrategia cruza n>=15 y sale peor que el mercado en
log-loss puntual (sin significancia). Este script aplica el mismo rigor
que el resto del proyecto (n>=40, bootstrap CI, split-half) para dar un
veredicto que SÍ se pueda usar como gate antes de promocionar una
candidata a `pares_permitidos_live` -- exactamente el mismo patrón que
gate_bucket_propio.py (rigor primero, vigía de aviso después).

Deliberadamente NO toca prob_yes ni ninguna decisión de shadow_predict.py
-- ver Opción A (pendiente, requiere aprobación explícita + /code-review,
misma cautela que P19/P20 en CLAUDE.md) para la corrección de raíz. Este
gate es solo un CHECK adicional a mirar manualmente antes de promocionar,
igual que IC/n/Wilson/fill-ability ya lo son.

Solo lectura sobre results.csv. Guarda data/shadow/gate_calibracion.json.
"""
import csv
import json
import math
import random
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data" / "shadow" / "results.csv"
PARAMS = REPO / "data" / "shadow" / "strategy_params.json"
OUT = REPO / "data" / "shadow" / "gate_calibracion.json"

N_MIN = 40           # mismo mínimo de promoción que el resto del proyecto
N_BOOT = 1500
CI = 0.90            # mismo nivel que el resto de gates rigurosos del proyecto


def _log_loss(p: float, outcome_yes: bool) -> float:
    p = min(max(p, 1e-9), 1 - 1e-9)
    o = 1.0 if outcome_yes else 0.0
    return -(o * math.log(p) + (1 - o) * math.log(1 - p))


def _cargar_diffs() -> dict:
    """clave (strategy) -> lista de diff = ll_modelo - ll_mercado por fila
    resuelta (positivo = modelo peor que el mercado en esa fila)."""
    diffs = {}
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("outcome_real") not in ("YES", "NO"):
                continue
            try:
                p_modelo = float(r.get("prob_yes_modelo", "") or "nan")
                p_mercado = float(r.get("precio_yes_mercado", "") or "nan")
            except ValueError:
                continue
            if not (0.0 < p_modelo < 1.0) or not (0.0 < p_mercado < 1.0):
                continue
            outcome_yes = r["outcome_real"] == "YES"
            d = _log_loss(p_modelo, outcome_yes) - _log_loss(p_mercado, outcome_yes)
            diffs.setdefault(r["strategy"], []).append(d)
    return diffs


def _bootstrap_ci(vals: list, n_boot: int = N_BOOT, ci: float = CI, seed: int = 42):
    rng = random.Random(seed)
    n = len(vals)
    boots = sorted(
        sum(vals[rng.randrange(n)] for _ in range(n)) / n
        for _ in range(n_boot)
    )
    lo_idx = int((1 - ci) / 2 * len(boots))
    hi_idx = int((1 + ci) / 2 * len(boots)) - 1
    return boots[lo_idx], boots[hi_idx]


def _veredicto(vals: list) -> dict:
    n = len(vals)
    media = sum(vals) / n
    if n < N_MIN:
        return {"n": n, "gap_medio": round(media, 4), "veredicto": "sin_concluir",
                "motivo": f"n<{N_MIN}"}

    ci_lo, ci_hi = _bootstrap_ci(vals)

    mitad = n // 2
    m1 = sum(vals[:mitad]) / mitad if mitad else 0.0
    m2 = sum(vals[mitad:]) / (n - mitad) if (n - mitad) else 0.0
    split_half_consistente = (m1 > 0) == (m2 > 0) == (media > 0)

    if ci_lo > 0 and split_half_consistente and media > 0:
        veredicto = "mal_calibrado_confirmado"
        motivo = f"CI{int(CI*100)}%=[{ci_lo:.4f},{ci_hi:.4f}] no cruza 0, split-half consistente"
    elif ci_hi < 0 and split_half_consistente and media < 0:
        veredicto = "bien_calibrado_confirmado"
        motivo = f"CI{int(CI*100)}%=[{ci_lo:.4f},{ci_hi:.4f}] no cruza 0, split-half consistente"
    else:
        veredicto = "sin_concluir"
        motivo = (f"CI{int(CI*100)}%=[{ci_lo:.4f},{ci_hi:.4f}]" +
                  ("" if split_half_consistente else " split-half inconsistente"))

    return {
        "n": n, "gap_medio": round(media, 4),
        "ci_lo": round(ci_lo, 4), "ci_hi": round(ci_hi, 4),
        "mitad1": round(m1, 4), "mitad2": round(m2, 4),
        "veredicto": veredicto, "motivo": motivo,
    }


def _tiene_calibracion_activa(strategy: str) -> bool:
    """results.csv guarda prob_yes_modelo CRUDO a propósito (shadow_postmortem
    reentrena Platt sobre la señal original, no sobre su propia corrección --
    ver comentario en shadow_predict.py línea ~5338). Si la estrategia YA
    tiene calibracion_prob en strategy_params.json, el hallazgo de este gate
    sobre el CRUDO puede estar ya resuelto en la práctica -- no es una alarma
    nueva, es la evidencia de por qué la corrección existe."""
    try:
        params = json.loads(PARAMS.read_text())
    except Exception:
        return False
    entry = params.get("estrategias", {}).get(strategy, {})
    return "calibracion_prob" in entry


def main() -> int:
    diffs = _cargar_diffs()
    resultado = {}
    for s, vals in sorted(diffs.items()):
        v = _veredicto(vals)
        v["calibracion_activa"] = _tiene_calibracion_activa(s)
        resultado[s] = v
    OUT.write_text(json.dumps({"estrategias": resultado}, indent=2, ensure_ascii=False),
                    encoding="utf-8")

    sin_corregir = [s for s, v in resultado.items()
                    if v["veredicto"] == "mal_calibrado_confirmado" and not v["calibracion_activa"]]
    ya_corregido = [s for s, v in resultado.items()
                    if v["veredicto"] == "mal_calibrado_confirmado" and v["calibracion_activa"]]
    bien = [s for s, v in resultado.items() if v["veredicto"] == "bien_calibrado_confirmado"]
    print(f"[gate_calibracion] {len(resultado)} estrategias evaluadas "
          f"(n>={N_MIN} para veredicto firme)")
    print(f"[gate_calibracion] mal_calibrado y SIN corregir ({len(sin_corregir)}): {sin_corregir}")
    print(f"[gate_calibracion] mal_calibrado en crudo pero YA con Platt activo ({len(ya_corregido)}): {ya_corregido}")
    print(f"[gate_calibracion] bien_calibrado_confirmado ({len(bien)}): {bien}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[gate_calibracion] ERROR {type(e).__name__}: {e}")
        sys.exit(1)
