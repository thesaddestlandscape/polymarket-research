#!/usr/bin/env python3
"""vigia_bot_wallets_gate_bucket.py — Vigía diario del gate por micro-
bucket de PnL real de bot wallets (bot_wallets_gate_bucket_fase0.py /
analisis_bot_wallets_gate_bucket_25ago.py / data/shadow/bot_wallets_gate_
bucket.json).

Petición explícita Javi 25-Ago: "tenemos que trackear esto día a día".
Mismo patrón EXACTO que vigia_gate_bucket_propio.py (28-Jul) aplicado a
este gate nuevo:
1. Re-corre analisis_bot_wallets_gate_bucket_25ago.py (regenera el JSON
   con el n de hoy).
2. Diffea contra el estado de AYER (latch) — avisa por Telegram SOLO
   veredictos NUEVOS (bucket que cruza a bueno_confirmado/malo_confirmado,
   o que cambia de sentido).
3. Añade una fila por bucket a `data/shadow/bot_wallets_gate_bucket_
   historico.csv` cada día — el JSON en sí se sobreescribe cada corrida
   (solo estado actual), este CSV es la serie temporal para ver cómo
   evoluciona n/pnl_medio/veredicto día a día sin tener que re-derivarlo
   de git log.

Cron diario 06:59 UTC (justo después del gate en sí, 06:57).
"""
import csv
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/shadow/bot_wallets_gate_bucket.json"
LATCH = REPO / "data/shadow/vigia_bot_wallets_gate_bucket_latch.json"
HISTORICO = REPO / "data/shadow/bot_wallets_gate_bucket_historico.csv"
COLUMNS = ["fecha", "clave", "bucket", "n", "pnl_medio", "shuffle_p", "veredicto"]


def _append_historico(nuevo: dict) -> None:
    hoy = date.today().isoformat()
    nuevo_archivo = not HISTORICO.exists()
    filas = []
    for clave_str, tabla in nuevo.items():
        for b, info in tabla.items():
            filas.append([hoy, clave_str, b, info.get("n"), info.get("pnl_medio"),
                          info.get("shuffle_p"), info.get("veredicto")])
    if not filas:
        return
    with open(HISTORICO, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo_archivo:
            w.writerow(COLUMNS)
        w.writerows(filas)


def main() -> int:
    from shadow_digest import enviar_telegram

    r = subprocess.run([sys.executable, str(REPO / "analisis_bot_wallets_gate_bucket_25ago.py")],
                        capture_output=True, text=True, timeout=300, cwd=str(REPO))
    if r.returncode != 0:
        print(f"ERROR ejecutando analisis_bot_wallets_gate_bucket_25ago.py: {r.stderr[-2000:]}")
        return 1

    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    avisos = []
    cobertura = []
    for clave_str, tabla in nuevo.items():
        veredictos_antes = previo.get(clave_str, {})
        n_sin_concluir = 0
        n_total_buckets = len(tabla)
        for b, info in tabla.items():
            v_nuevo = info.get("veredicto", "sin_concluir")
            v_antes = veredictos_antes.get(b, {}).get("veredicto", "sin_concluir")
            if v_nuevo != "sin_concluir":
                if v_antes != v_nuevo:
                    avisos.append(
                        f"{'🔴' if v_nuevo == 'malo_confirmado' else '🟢'} {clave_str} "
                        f"[{b},{float(b)+0.05:.2f}) -> {v_nuevo} "
                        f"(n={info['n']} pnl/tr={info['pnl_medio']:+.3f} p={info.get('shuffle_p')})"
                    )
            else:
                n_sin_concluir += 1
        if n_total_buckets:
            cobertura.append(f"{clave_str}: {n_total_buckets - n_sin_concluir}/{n_total_buckets} buckets con veredicto")

    print("\n".join(cobertura))
    _append_historico(nuevo)

    if avisos:
        msg = "🤖 Bot wallets gate bucket — nuevos veredictos hoy:\n" + "\n".join(avisos)
        print(msg)
        enviar_telegram(msg)
    else:
        print("Sin veredictos nuevos hoy.")

    LATCH.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
