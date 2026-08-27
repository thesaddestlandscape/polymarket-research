#!/usr/bin/env python3
"""
vigia_sports_micro_bucket_kill_switch_wallet_mirror.py — cortacircuitos
de dinero real sobre el gate de micro-bucket de Sports Wallet Mirror
(sports_wallet_mirror_gate_bucket.py). Mismo mecanismo EXACTO que
vigia_micro_bucket_kill_switch_wallet_mirror.py (24-Ago, cripto), sin la
dimensión `jugada_grande` que sports no tiene.

27-Ago noche (petición explícita Javi: "construye lo que falte de sports
para tenerlo ya hecho cuando toque operar en directo"): sports todavía no
tiene ni un solo trade real (pares_permitidos_live=[]), así que hoy este
vigía no encuentra nada que vetar -- pero construido AHORA para que el
día que Javi promocione la primera tupla (CS#SEGUIR[0.24,0.29) el
candidato más maduro hoy) el backstop ya exista desde el primer trade
real, no semanas después como pasó con WALLET_MIRROR en cripto (10/11/
12-Ago con dinero real, kill switch añadido recién el 24-Ago).

Mecanismo: agrupa trades reales CERRADOS de sports (data/sports/trades.csv)
por (categoria,tipo,bucket). Si un bucket que el gate dice
"bueno_confirmado" lleva n>=3 trades reales con PnL neto agregado
NEGATIVO, escribe override en
data/sports/wallet_mirror_gate_bucket_override.json (gana sobre cualquier
otro veredicto) + aviso Telegram (bot="sports", latch por clave+bucket).

Cron/scheduler: mismo patrón que el hermano de cripto -- añadir a un
consolidador de vigías de sports si/cuando exista uno con cadencia
~1800s, o cron propio diario mientras tanto.
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
N_MIN_ALERTA = 3


def main() -> int:
    from shadow_digest import enviar_telegram

    try:
        vistos = json.loads(LATCH.read_text()) if LATCH.exists() else {}
    except Exception:
        vistos = {}

    try:
        override = json.loads(OVERRIDE_PATH.read_text()) if OVERRIDE_PATH.exists() else {}
    except Exception:
        override = {}

    por_clave_bucket: dict[str, list[float]] = {}
    if TRADES.exists():
        with open(TRADES, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("status") != "CLOSED":
                    continue
                categoria = row.get("categoria", "")
                tipo = row.get("tipo", "")
                if not categoria or not tipo:
                    continue
                try:
                    ask = float(row["entry_price"])
                    pnl = float(row["pnl_neto_eur"])
                except Exception:
                    continue
                clave_str = sgb.clave(categoria, tipo)
                b = sgb.bucket(ask)
                clave_bucket = f"{clave_str}#{b:.2f}"
                por_clave_bucket.setdefault(clave_bucket, []).append(pnl)

    alertas = []
    nuevos_override = {}
    for clave_bucket, pnls in por_clave_bucket.items():
        n = len(pnls)
        if n < N_MIN_ALERTA:
            continue
        pnl_total = sum(pnls)
        if pnl_total >= 0:
            continue

        clave_str, b_str = clave_bucket.rsplit("#", 1)
        categoria, tipo = clave_str.split("#")
        b = float(b_str)
        veredicto = sgb.evaluar_sin_override(categoria, tipo, b + sgb.STEP / 2)["veredicto"]
        if veredicto != "bueno_confirmado":
            continue  # ya vetado o sin_concluir -- el gate ya protege, no hace falta el kill switch

        ya_override = clave_bucket in override
        if clave_bucket in vistos and ya_override:
            continue

        alertas.append((clave_bucket, n, pnl_total))
        if not ya_override:
            nuevos_override[clave_bucket] = {
                "motivo": f"kill_switch automático: {n} trades reales en este bucket, "
                          f"PnL neto agregado {pnl_total:+.2f}€, pese a veredicto bueno_confirmado",
                "desde": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            }
        vistos[clave_bucket] = {"n": n, "pnl_total": round(pnl_total, 2)}

    print(f"[vigia_sports_micro_bucket_kill_switch_wallet_mirror] {len(por_clave_bucket)} celdas con n>=1, "
          f"{len(alertas)} bucket(s) confirmado(s)-pero-sangrando")

    if nuevos_override:
        override.update(nuevos_override)
        OVERRIDE_PATH.write_text(json.dumps(override, ensure_ascii=False, indent=1))
        print(f"[vigia_sports_micro_bucket_kill_switch_wallet_mirror] 🚨 override AUTOMÁTICO escrito para: "
              f"{list(nuevos_override.keys())}")

    if alertas:
        detalle = "\n".join(
            f"  {clave}: n={n} PnL real={pnl:+.2f}€" for clave, n, pnl in alertas
        )
        msg = (
            "🚨🔒 KILL SWITCH micro-bucket SPORTS WALLET MIRROR: el gate confirma 'bueno_confirmado' pero "
            "el dinero real está perdiendo ahí:\n"
            f"{detalle}\nOverride escrito, bloqueado hasta revisión."
        )
        enviar_telegram(msg, bot="sports")

    LATCH.write_text(json.dumps(vistos, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
