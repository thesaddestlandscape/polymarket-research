#!/usr/bin/env python3
"""vigia_bot_wallets_gate_bucket_fino.py — 14-Sep, vigía de la ventana
deslizante (fino) de la familia P-GALLINA (SNIPER/DISPERSO/WEEKLY_*),
mismo patrón que vigia_gate_bucket_wallet_mirror_fino.py.

Petición explícita Javi (14-Sep, tras encontrar que 5 buckets SNIPER ya
`bueno_confirmado` en el grid seguían bloqueados por una whitelist manual
sin actualizar): "tenemos que hacer aquí como en wallet mirror, que
cuando se confirme un micro-bucket propio y fino bueno, nos avise por
telegram para tenerlo claro. Porque sino, estamos dejando dinero de
sniper encima de la mesa." Este vigía (fino) + vigia_bot_wallets_gate_
bucket.py (grid, ya existente desde 08-Sep) cubren ambos mecanismos,
igual que wallet_mirror.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/shadow/bot_wallets_gate_bucket_fino.json"
LATCH = REPO / "data/live/vigia_bot_wallets_gate_bucket_fino_latch.json"


def main() -> int:
    from shadow_digest import enviar_telegram

    r = subprocess.run(
        [sys.executable, str(REPO / "analisis_bot_wallets_gate_bucket_fino.py")],
        capture_output=True, text=True, timeout=300, cwd=str(REPO),
    )
    if r.returncode != 0:
        print(f"ERROR ejecutando analisis_bot_wallets_gate_bucket_fino.py: {r.stderr[-2000:]}")
        return 1
    print(r.stdout[-2000:])

    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8")) if DATA_PATH.exists() else {}
    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    avisos = []
    for clave_str, info in nuevo.items():
        v_nuevo = info.get("veredicto", "sin_concluir")
        v_antes = previo.get(clave_str, {}).get("veredicto", "sin_concluir")
        if v_nuevo != "sin_concluir" and v_antes != v_nuevo:
            avisos.append(
                f"{'🔴' if v_nuevo == 'malo_confirmado' else '🟢'} {clave_str} "
                f"[{info.get('lo')},{info.get('hi')}) -> {v_nuevo} "
                f"(n={info.get('n')} pnl/tr={info.get('pnl_medio')} "
                f"g_kelly={info.get('g_kelly_f10')} p={info.get('p_valor')})"
            )
        elif v_antes != "sin_concluir" and v_nuevo == "sin_concluir":
            avisos.append(f"⚠️ {clave_str} revierte a sin_concluir (era {v_antes})")

    if avisos:
        msg = "🎯 Bot wallets (SNIPER/DISPERSO/WEEKLY) gate bucket FINO — cambios hoy:\n" + "\n".join(avisos)
        print(msg)
        enviar_telegram(msg)
    else:
        print("Sin cambios de veredicto en el fino hoy.")

    LATCH.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
