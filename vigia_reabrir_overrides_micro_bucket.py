#!/usr/bin/env python3
"""
vigia_reabrir_overrides_micro_bucket.py — auto-revisión y REAPERTURA del
override que escribe vigia_micro_bucket_kill_switch.py.

Origen (24-Ago, corrección explícita de Javi tras revisar el kill switch:
"no podemos revisarlo nosotros, es tu trabajo... si una se bloquea, en el
próximo ciclo la revisas y si está OK la desbloqueas. No podemos dejar
estrategias muertas así"): el kill switch (05-Ago) bloquea un bucket para
SIEMPRE hasta que alguien borre la entrada a mano -- sin este vigía, un
bloqueo por mala suerte con n=3 (umbral deliberadamente bajo, "proteger
primero") podía dejar una zona de precio realmente buena cerrada
indefinidamente sin que nadie la revisara, sangrando la misma estrategia
que se intentaba proteger.

Mecanismo (mismo espíritu fail-closed que el resto del proyecto -- más
difícil reabrir que cerrar):
  Para cada entrada de gate_bucket_propio_override.json cuyo "motivo"
  empiece por "kill_switch automático" (NUNCA toca un override manual de
  Javi -- esos no llevan ese prefijo, se dejan intactos siempre):
    1. Cuenta trades reales CERRADOS en trades.csv para esa tupla+bucket
       ocurridos DESPUÉS de "desde" (el momento del bloqueo).
    2. Exige n>=N_MIN_REAPERTURA (5, más alto que el n=3 que bloquea --
       asimetría deliberada: cerrar es barato, reabrir exige más
       evidencia) Y pnl_total agregado >= 0.
    3. Exige TAMBIÉN que el gate estadístico riguroso (gate_bucket_propio.
       json, regenerado a diario) YA NO clasifique ese bucket como
       "malo_confirmado" con los datos de hoy -- dos señales
       independientes (dinero real reciente Y estadística fresca), no
       basta con una sola coincidencia favorable.
  Si ambas condiciones se cumplen: borra la entrada del override (bucket
  vuelve a operar bajo el veredicto normal del gate), avisa por Telegram,
  y registra la decisión en data/live/gate_bucket_propio_override_
  historial.json (auditoría permanente, nunca se sobreescribe).
  Si NO se cumplen: no hace nada, sin spam de Telegram -- solo log.

Cron sugerido (mismo scheduler que vigia_micro_bucket_kill_switch.py,
consolidado en vigias_frecuentes_fase0.py):
  cada 30 min, después del propio kill switch.
"""
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import gate_bucket_propio as gbp

TRADES = REPO / "data/live/trades.csv"
OVERRIDE_PATH = gbp.OVERRIDE_PATH
LATCH = REPO / "data/live/vigia_micro_bucket_kill_switch_latch.json"
HISTORIAL = REPO / "data/live/gate_bucket_propio_override_historial.json"
STEP = 0.05
N_MIN_REAPERTURA = 5
PREFIJO_AUTOMATICO = "kill_switch automático"


def _bucket(py: float) -> float:
    import math
    return round(math.floor(py / STEP + 1e-9) * STEP, 4)


def _py_real(direction: str, entry_price: float) -> float:
    return 1 - entry_price if direction == "BUY_NO" else entry_price


def _parsear_clave(clave: str):
    """'STRATEGY#ACTIVO#MARCO#DECISION#0.05' -> (tupla_str, bucket_float).
    El bucket siempre es el último segmento (formato fijo b:.2f, sin '#')."""
    tupla_str, bucket_str = clave.rsplit("#", 1)
    try:
        return tupla_str, float(bucket_str)
    except ValueError:
        return None, None


def main() -> int:
    from shadow_digest import enviar_telegram

    try:
        override = json.loads(OVERRIDE_PATH.read_text()) if OVERRIDE_PATH.exists() else {}
    except Exception:
        override = {}

    try:
        vistos = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        vistos = {}

    try:
        historial = json.loads(HISTORIAL.read_text()) if HISTORIAL.exists() else []
    except Exception:
        historial = []

    candidatas = {k: v for k, v in override.items()
                  if str(v.get("motivo", "")).startswith(PREFIJO_AUTOMATICO)}
    if not candidatas:
        print("[vigia_reabrir_overrides_micro_bucket] 0 overrides automáticos activos -- nada que revisar")
        return 0

    trades_todos = []
    if TRADES.exists():
        with open(TRADES, encoding="utf-8") as f:
            trades_todos = list(csv.DictReader(f))

    reabiertas = []
    for clave, entrada in candidatas.items():
        tupla_str, bucket = _parsear_clave(clave)
        if tupla_str is None:
            continue
        partes = tupla_str.split("#")
        if len(partes) != 4:
            continue
        strategy, activo, marco, direction = partes
        subtype = f"{activo}#{marco}"
        try:
            desde_dt = datetime.fromisoformat(entrada["desde"])
        except Exception:
            continue

        pnls_recientes = []
        for row in trades_todos:
            if row.get("status") != "CLOSED":
                continue
            if (row.get("strategy"), row.get("subtype"), row.get("direction")) != (strategy, subtype, direction):
                continue
            try:
                ts_close = datetime.fromisoformat(row.get("close_timestamp", ""))
                entry = float(row["entry_price"])
                pnl = float(row["pnl_neto_eur"])
            except Exception:
                continue
            if ts_close <= desde_dt:
                continue
            if _bucket(_py_real(direction, entry)) != bucket:
                continue
            pnls_recientes.append(pnl)

        n = len(pnls_recientes)
        if n < N_MIN_REAPERTURA:
            continue
        pnl_total = sum(pnls_recientes)
        if pnl_total < 0:
            continue

        veredicto_hoy = gbp.evaluar(tupla_str, bucket + STEP / 2)["veredicto"]
        if veredicto_hoy == "malo_confirmado":
            continue  # dinero real reciente OK, pero la estadística fresca sigue diciendo que no -- se queda bloqueado

        reabiertas.append({
            "clave": clave, "n_reciente": n, "pnl_reciente": round(pnl_total, 2),
            "veredicto_hoy": veredicto_hoy, "bloqueado_desde": entrada["desde"],
        })

    if not reabiertas:
        print(f"[vigia_reabrir_overrides_micro_bucket] {len(candidatas)} override(s) automático(s) "
              f"activos, 0 cumplen criterio de reapertura (n>={N_MIN_REAPERTURA}, pnl>=0, "
              f"veredicto fresco != malo_confirmado)")
        return 0

    ahora = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for r in reabiertas:
        motivo_original = candidatas[r["clave"]].get("motivo", "")
        del override[r["clave"]]
        vistos.pop(r["clave"], None)
        historial.append({
            "clave": r["clave"], "accion": "reabierto_automatico", "ts": ahora,
            "motivo_bloqueo_original": motivo_original, "bloqueado_desde": r["bloqueado_desde"],
            "n_trades_reales_desde_bloqueo": r["n_reciente"], "pnl_trades_reales": r["pnl_reciente"],
            "veredicto_gate_al_reabrir": r["veredicto_hoy"],
        })

    OVERRIDE_PATH.write_text(json.dumps(override, ensure_ascii=False, indent=1))
    LATCH.write_text(json.dumps(vistos, ensure_ascii=False, indent=1))
    HISTORIAL.write_text(json.dumps(historial, ensure_ascii=False, indent=1))

    detalle = "\n".join(
        f"  {r['clave']}: {r['n_reciente']} trades reales desde el bloqueo, "
        f"PnL={r['pnl_reciente']:+.2f}€, gate hoy={r['veredicto_hoy']}"
        for r in reabiertas
    )
    print(f"[vigia_reabrir_overrides_micro_bucket] ✅ {len(reabiertas)} bucket(s) reabierto(s):\n{detalle}")
    msg = (
        f"🔓 REAPERTURA automática de micro-bucket ({len(reabiertas)}):\n{detalle}\n"
        f"Dinero real reciente + gate estadístico fresco ya no confirman el problema -- "
        f"vuelve a operar bajo el veredicto normal."
    )
    enviar_telegram(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
