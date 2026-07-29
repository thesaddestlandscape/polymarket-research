#!/usr/bin/env python3
"""
vigia_slippage_kill_switch.py — Stage 0 (P29 ítem 6, "kill switch por
tupla"). Mecanismo DECIDIDO por Javi 29-Jul: **solo alerta**, igual que
vigia_log_growth.py/vigia_degradacion_live.py — la pausa la sigue
decidiendo él, este vigía nunca toca config_live.json.

Usa las columnas estructuradas `signal_ask`/`slip_real` de
data/live/trades.csv (añadidas hoy mismo, ver
project_logging_estructurado_slippage_29jul en memoria) — antes solo se
podían leer con regex sobre `notas`, y solo de forma AGREGADA (global,
`shadow_predict.py::_slippage_estimado_dinamico`), nunca por tupla.

Pregunta que responde: ¿alguna tupla de `pares_permitidos_live` está
pagando sistemáticamente MÁS slippage real de lo que el sistema asume al
calcular su edge (`SLIPPAGE_ESTIMADO`/su versión dinámica, hoy 0.02€ tope)?
Si sí, el edge neto real de esa tupla es menor de lo que el modelo cree —
la señal de "puede haber que revisarla" que Moon Dev formaliza como
retiro automático en sus propios bots, pero aquí queda como aviso.

Rigor: n≥15 (suelo del proyecto), CI90% de la media (normal/t, no
bootstrap -- suficiente con n≥15 y slip_real ~ distribución razonable,
mismo nivel de rigor que otros vigías de una sola muestra continua).
Alerta si el límite INFERIOR del CI90% de slip_real medio supera
SLIPPAGE_ESTIMADO -- es decir, incluso en el escenario más favorable
dentro del intervalo, el slippage real ya es peor que lo asumido.

Latch con histéresis por tupla (mismo patrón que vigia_degradacion_live):
avisa al cruzar, no vuelve a avisar hasta que el CI baje de nuevo por
debajo del umbral (con margen, evita rebote en el borde).

Cron sugerido: diario, mismo bloque 06:xx UTC que el resto de vigías de
análisis. Solo lectura -- no toca dinero, config ni decisiones.
"""
import csv
import json
import math
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

TRADES = REPO / "data/live/trades.csv"
CONFIG_LIVE = REPO / "data/live/config_live.json"
LATCH = REPO / "data/live/vigia_slippage_kill_switch_latch.json"

N_MIN = 15
Z_90 = 1.645
SLIPPAGE_ESTIMADO = 0.02   # mismo valor fallback que shadow_predict.py::SLIPPAGE_ESTIMADO
MARGEN_RECUPERACION = 0.005  # histéresis: no resetea el latch hasta bajar umbral-margen


def _log(msg: str) -> None:
    from datetime import datetime, timezone
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _tuplas_live() -> list[tuple[str, str, str]]:
    try:
        cfg = json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
    except Exception:
        return []
    out = []
    for t in cfg.get("pares_permitidos_live", []):
        partes = t.split("#")
        if len(partes) == 4:
            out.append((partes[0], f"{partes[1]}#{partes[2]}", partes[3]))
    return out


def _slips_tupla(strategy: str, subtype: str, direction: str) -> list[float]:
    slips = []
    if not TRADES.exists():
        return slips
    with open(TRADES, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if (row.get("strategy") == strategy and row.get("subtype") == subtype
                    and row.get("direction") == direction and row.get("status") == "CLOSED"):
                raw = row.get("slip_real", "")
                if raw not in ("", None):
                    try:
                        slips.append(float(raw))
                    except (TypeError, ValueError):
                        pass
    return slips


def _media_ci90(vals: list[float]) -> tuple[float, float, float]:
    n = len(vals)
    media = sum(vals) / n
    if n < 2:
        return media, media, media
    var = sum((v - media) ** 2 for v in vals) / (n - 1)
    se = math.sqrt(var / n)
    return media, media - Z_90 * se, media + Z_90 * se


def main() -> int:
    from shadow_digest import enviar_telegram

    try:
        latch = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        latch = {}

    tuplas = _tuplas_live()
    _log(f"tuplas live a revisar: {len(tuplas)}")

    cambios = False
    for strategy, subtype, direction in tuplas:
        clave = f"{strategy}#{subtype}#{direction}"
        slips = _slips_tupla(strategy, subtype, direction)
        n = len(slips)
        if n < N_MIN:
            _log(f"{clave}: n={n} < {N_MIN}, sin concluir")
            continue

        media, ci_lo, ci_hi = _media_ci90(slips)
        peor_que_asumido = ci_lo > SLIPPAGE_ESTIMADO
        estado = latch.get(clave, {})
        avisado = estado.get("avisado", False)

        _log(f"{clave}: n={n} slip_medio={media:+.4f} CI90%=[{ci_lo:+.4f},{ci_hi:+.4f}] "
             f"asumido={SLIPPAGE_ESTIMADO} {'⚠️ PEOR' if peor_que_asumido else 'ok'} "
             f"({'ya avisado' if avisado else 'sin avisar'})")

        if peor_que_asumido and not avisado:
            msg = (
                f"🔻 *Slippage real peor de lo asumido* — {clave}\n"
                f"n={n} trades reales cerrados\n"
                f"slip_real medio={media:+.4f}€ (CI90%=[{ci_lo:+.4f},{ci_hi:+.4f}])\n"
                f"asumido en el edge (SLIPPAGE_ESTIMADO)={SLIPPAGE_ESTIMADO:+.4f}€\n"
                f"El edge neto real de esta tupla es probablemente MENOR de lo que "
                f"el modelo asume — revisar manualmente, esto es solo un aviso, "
                f"no pausa nada."
            )
            _log(msg)
            enviar_telegram(msg)
            latch[clave] = {"avisado": True, "n": n, "slip_medio": round(media, 4)}
            cambios = True
        elif not peor_que_asumido and avisado and ci_hi < SLIPPAGE_ESTIMADO - MARGEN_RECUPERACION:
            _log(f"{clave}: recuperado, reseteando latch")
            latch[clave] = {"avisado": False, "n": n, "slip_medio": round(media, 4)}
            cambios = True

    if cambios:
        LATCH.write_text(json.dumps(latch, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
