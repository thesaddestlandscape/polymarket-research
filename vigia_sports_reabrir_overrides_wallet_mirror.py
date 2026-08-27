#!/usr/bin/env python3
"""
vigia_sports_reabrir_overrides_wallet_mirror.py — auto-revisión y
REAPERTURA del override que escribe
vigia_sports_micro_bucket_kill_switch_wallet_mirror.py. Mismo mecanismo
EXACTO que vigia_reabrir_overrides_wallet_mirror.py (24-Ago, cripto),
sin la dimensión `jugada_grande`.

Solo toca entradas de wallet_mirror_gate_bucket_override.json (sports)
cuyo motivo empiece por "kill_switch automático" -- nunca un override
manual.

27-Ago noche (petición explícita Javi: "construye lo que falte de sports
para tenerlo ya hecho"): construido junto al kill switch, mismo motivo --
que el backstop completo (bloquear Y reabrir) exista desde el primer
trade real de sports, no se añada semanas después.
"""
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import sports_wallet_mirror_gate_bucket as sgb

TRADES = REPO / "data/sports/trades.csv"
OVERRIDE_PATH = sgb.OVERRIDE_PATH
LATCH = REPO / "data/sports/vigia_micro_bucket_kill_switch_wallet_mirror_latch.json"
HISTORIAL = REPO / "data/sports/wallet_mirror_gate_bucket_override_historial.json"
N_MIN_REAPERTURA = 5
PREFIJO_AUTOMATICO = "kill_switch automático"


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
        print("[vigia_sports_reabrir_overrides_wallet_mirror] 0 overrides automáticos activos -- nada que revisar")
        return 0

    trades_todos = []
    if TRADES.exists():
        with open(TRADES, encoding="utf-8") as f:
            trades_todos = [r for r in csv.DictReader(f) if r.get("status") == "CLOSED"]

    reabiertas = []
    for clave_bucket, entrada in candidatas.items():
        clave_str, b_str = clave_bucket.rsplit("#", 1)
        try:
            categoria, tipo = clave_str.split("#")
            b = float(b_str)
        except Exception:
            continue
        try:
            desde_dt = datetime.fromisoformat(entrada["desde"])
        except Exception:
            continue

        pnls_recientes = []
        for row in trades_todos:
            if row.get("categoria") != categoria or row.get("tipo") != tipo:
                continue
            try:
                ts_close = datetime.fromisoformat(row.get("close_timestamp", ""))
                ask = float(row["entry_price"])
                pnl = float(row["pnl_neto_eur"])
            except Exception:
                continue
            if ts_close <= desde_dt or sgb.bucket(ask) != b:
                continue
            pnls_recientes.append(pnl)

        n = len(pnls_recientes)
        if n < N_MIN_REAPERTURA:
            continue
        pnl_total = sum(pnls_recientes)
        if pnl_total < 0:
            continue

        veredicto_hoy = sgb.evaluar_sin_override(categoria, tipo, b + sgb.STEP / 2)["veredicto"]
        if veredicto_hoy == "malo_confirmado":
            continue

        reabiertas.append({
            "clave": clave_bucket, "n_reciente": n, "pnl_reciente": round(pnl_total, 2),
            "veredicto_hoy": veredicto_hoy, "bloqueado_desde": entrada["desde"],
        })

    if not reabiertas:
        print(f"[vigia_sports_reabrir_overrides_wallet_mirror] {len(candidatas)} override(s) automático(s) "
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
    print(f"[vigia_sports_reabrir_overrides_wallet_mirror] ✅ {len(reabiertas)} bucket(s) reabierto(s):\n{detalle}")
    enviar_telegram(
        f"🔓 REAPERTURA automática micro-bucket SPORTS WALLET MIRROR ({len(reabiertas)}):\n{detalle}",
        bot="sports",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
