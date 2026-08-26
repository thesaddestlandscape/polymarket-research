#!/usr/bin/env python3
"""vigia_sports_wallet_mirror_gate_bucket_fino.py — 26-Ago, vigía diario
de la ventana deslizante de sports (analisis_sports_wallet_mirror_gate_
bucket_fino.py), mismo patrón latch que el resto de vigías de gate.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/sports/wallet_mirror_gate_bucket_fino.json"
LATCH = REPO / "data/live/vigia_sports_wallet_mirror_gate_bucket_fino_latch.json"


def main() -> int:
    from shadow_digest import enviar_telegram

    r = subprocess.run(
        [sys.executable, str(REPO / "analisis_sports_wallet_mirror_gate_bucket_fino.py")],
        capture_output=True, text=True, timeout=300, cwd=str(REPO),
    )
    if r.returncode != 0:
        print(f"ERROR: {r.stderr[-2000:]}")
        return 1
    print(r.stdout[-2000:])

    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8")) if DATA_PATH.exists() else {}
    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    avisos = []
    for tupla_str, info in nuevo.items():
        v_nuevo = info.get("veredicto")
        v_antes = previo.get(tupla_str, {}).get("veredicto")
        if v_nuevo in ("bueno_confirmado", "malo_confirmado") and v_nuevo != v_antes:
            avisos.append(
                f"{'🟢' if v_nuevo == 'bueno_confirmado' else '🔴'} {tupla_str} "
                f"[{info['lo']:.2f},{info['hi']:.2f}) -> {v_nuevo} "
                f"(n={info['n']} pnl/tr={info['pnl_medio']:+.3f} p={info['p_valor']})"
            )

    if avisos:
        msg = "🏆 Sports Wallet Mirror gate FINO (ventana deslizante) — nuevos veredictos:\n" + "\n".join(avisos)
        print(msg)
        enviar_telegram(msg)
    else:
        print("Sin veredictos nuevos hoy.")

    LATCH.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
