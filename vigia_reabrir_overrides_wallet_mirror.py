#!/usr/bin/env python3
"""
vigia_reabrir_overrides_wallet_mirror.py — auto-revisión y REAPERTURA del
override que escribe vigia_micro_bucket_kill_switch_wallet_mirror.py.
Mismo mecanismo EXACTO que vigia_reabrir_overrides_micro_bucket.py
(24-Ago) aplicado al gate paralelo de WALLET_MIRROR (wallet_mirror_gate_
bucket.py) -- ver ese fichero para el razonamiento completo (petición
Javi: "si una se bloquea, en el próximo ciclo la revisas y si está OK la
desbloqueas, no podemos dejar estrategias muertas así").

Solo toca entradas de wallet_mirror_gate_bucket_override.json cuyo motivo
empiece por "kill_switch automático" -- nunca un override manual.

Cron/scheduler: consolidado en vigias_frecuentes_fase0.py, DESPUÉS de
vigia_micro_bucket_kill_switch_wallet_mirror.py en la lista.
"""
import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import wallet_mirror_gate_bucket as wmgb

TRADES = REPO / "data/live/trades.csv"
OVERRIDE_PATH = wmgb.OVERRIDE_PATH
LATCH = REPO / "data/live/vigia_micro_bucket_kill_switch_wallet_mirror_latch.json"
HISTORIAL = REPO / "data/live/wallet_mirror_gate_bucket_override_historial.json"
STEP = 0.05
N_MIN_REAPERTURA = 5
PREFIJO_AUTOMATICO = "kill_switch automático"

_RE_NOTAS = re.compile(r"tipo=(SEGUIR|FADE)\s+grande=([01])")


def _parsear_notas(notas: str):
    m = _RE_NOTAS.search(notas or "")
    if not m:
        return None, None
    return m.group(1), m.group(2) == "1"


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
        print("[vigia_reabrir_overrides_wallet_mirror] 0 overrides automáticos activos -- nada que revisar")
        return 0

    trades_todos = []
    if TRADES.exists():
        with open(TRADES, encoding="utf-8") as f:
            trades_todos = [r for r in csv.DictReader(f)
                             if r.get("status") == "CLOSED" and r.get("strategy") == "WALLET_MIRROR"]

    reabiertas = []
    for clave_bucket, entrada in candidatas.items():
        clave_str, b_str = clave_bucket.rsplit("#", 1)
        try:
            tipo_c, activo, marco, grande_c = clave_str.split("#")
            b = float(b_str)
        except Exception:
            continue
        try:
            desde_dt = datetime.fromisoformat(entrada["desde"])
        except Exception:
            continue

        pnls_recientes = []
        for row in trades_todos:
            if row.get("subtype") != f"{activo}#{marco}":
                continue
            tipo, grande = _parsear_notas(row.get("notas", ""))
            if tipo != tipo_c or grande is None or ("1" if grande else "0") != grande_c:
                continue
            try:
                ts_close = datetime.fromisoformat(row.get("close_timestamp", ""))
                ask = float(row["signal_ask"])
                pnl = float(row["pnl_neto_eur"])
            except Exception:
                continue
            if ts_close <= desde_dt or wmgb.bucket(ask) != b:
                continue
            pnls_recientes.append(pnl)

        n = len(pnls_recientes)
        if n < N_MIN_REAPERTURA:
            continue
        pnl_total = sum(pnls_recientes)
        if pnl_total < 0:
            continue

        veredicto_hoy = wmgb.evaluar_sin_override(tipo_c, activo, marco, b + STEP / 2, grande_c == "1")["veredicto"]
        if veredicto_hoy == "malo_confirmado":
            continue

        reabiertas.append({
            "clave": clave_bucket, "n_reciente": n, "pnl_reciente": round(pnl_total, 2),
            "veredicto_hoy": veredicto_hoy, "bloqueado_desde": entrada["desde"],
        })

    if not reabiertas:
        print(f"[vigia_reabrir_overrides_wallet_mirror] {len(candidatas)} override(s) automático(s) "
              f"activos, 0 cumplen criterio de reapertura")
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
    print(f"[vigia_reabrir_overrides_wallet_mirror] ✅ {len(reabiertas)} bucket(s) reabierto(s):\n{detalle}")
    enviar_telegram(
        f"🔓 REAPERTURA automática micro-bucket WALLET_MIRROR ({len(reabiertas)}):\n{detalle}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
