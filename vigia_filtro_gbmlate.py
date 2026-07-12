#!/usr/bin/env python3
"""Vigía filtro_causal en GBM_LATE_15M: avisa por Telegram si alguna vez
aparece un filtro_causal (skip automático de señal live) en las claves
recién añadidas a FEATURE_RULES (12-Jul, ver shadow_postmortem.py).

Origen: /code-review sobre el commit que añadió GBM_LATE_15M a
FEATURE_RULES encontró que, por primera vez, un results.csv corrupto/
duplicado (ya pasó una vez, ver memoria project_tracking_error_
arqueologia_11jul) podría generar un filtro_causal con n>=15 IC<-0.12 que
saltaría señales live reales (SOL/ETH BUY_YES) sin que nadie lo note hasta
mirar estado_actual.md a mano. Dry-run 12-Jul: 0 filtros hoy, solo
patrones_ganadores (boosts, inertes mientras el stake siga pineado).

Read-only, no toca dinero ni config — solo lee strategy_params.json y
avisa. No bloquea nada (fail-loud, no fail-closed): si dispara, Javi decide
si el filtro es legítimo o síntoma de datos corruptos.
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

PARAMS = REPO / "data/shadow/strategy_params.json"
LATCH = REPO / "data/live/vigia_filtro_gbmlate_latch.json"
CLAVES = [
    "GBM_LATE_15M",
    "GBM_LATE_15M#BTC#15min",
    "GBM_LATE_15M#ETH#15min",
    "GBM_LATE_15M#SOL#15min",
    "GBM_LATE_15M#XRP#15min",
]


def _firma(f: dict) -> str:
    return f"{f.get('feature')}|{f.get('condicion')}|{f.get('umbral')}|{f.get('direccion')}"


def main() -> int:
    from shadow_digest import enviar_telegram

    if not PARAMS.exists():
        return 0
    try:
        sp = json.loads(PARAMS.read_text())
    except Exception as e:
        print(f"[vigia_filtro_gbmlate] strategy_params.json ilegible: {e}")
        return 0
    est = sp.get("estrategias", sp)

    try:
        vistos = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        vistos = {}

    nuevos = []
    for clave in CLAVES:
        filtros = (est.get(clave, {}) or {}).get("filtros_causales", []) or []
        ya = set(vistos.get(clave, []))
        for f in filtros:
            firma = _firma(f)
            if firma not in ya:
                nuevos.append((clave, f))
                ya.add(firma)
        vistos[clave] = sorted(ya)

    print(f"[vigia_filtro_gbmlate] claves={len(CLAVES)} filtros_nuevos={len(nuevos)}")

    if nuevos:
        detalle = "\n".join(
            f"  {clave}: {f.get('feature')} {f.get('condicion')} {f.get('umbral')} "
            f"dir={f.get('direccion')} ic_malo={f.get('ic_malo')} n_malo={f.get('n_malo')}"
            for clave, f in nuevos
        )
        msg = (
            f"⚠️ VIGÍA: nuevo filtro_causal en GBM_LATE_15M (estrategia live)\n"
            f"{detalle}\n"
            f"Esto puede saltar señales live reales (SOL/ETH BUY_YES) desde el "
            f"próximo ciclo de predict. Revisar si el bucket tiene sentido o es "
            f"síntoma de datos corruptos en results.csv (ic_bucket/n arriba) "
            f"antes de asumir que es un hallazgo real. No se ha bloqueado nada."
        )
        ok = enviar_telegram(msg)
        print(f"[vigia_filtro_gbmlate] aviso enviado (telegram={ok})")

    LATCH.write_text(json.dumps(vistos, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_filtro_gbmlate] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
