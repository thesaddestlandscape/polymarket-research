#!/usr/bin/env python3
"""vigia_bot_consenso_gate_momentum_ballena.py — vigía diario de
analisis_bot_consenso_gate_momentum_ballena.py (26-Ago, propuesta #2).
`bot_consenso_lado` solo se loguea desde el 25-Ago -- muy joven, hoy (26-
Ago) ninguna celda fina (0.05 x coincide/discrepa) llega a n>=15 todavía
pese a que el agregado por bucket ancho (0.10, sin desagregar por
moneda) sí mostraba señal fuerte. Este vigía deja que n crezca solo y
avisa por Telegram en cuanto la primera celda cruce rigor -- mismo
patrón latch que vigia_gate_bucket_propio.py.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/shadow/bot_consenso_gate_momentum_ballena.json"
LATCH = REPO / "data/live/vigia_bot_consenso_gate_momentum_ballena_latch.json"


def main() -> int:
    from shadow_digest import enviar_telegram

    r = subprocess.run(
        [sys.executable, str(REPO / "analisis_bot_consenso_gate_momentum_ballena.py")],
        capture_output=True, text=True, timeout=120, cwd=str(REPO),
    )
    if r.returncode != 0:
        print(f"ERROR: {r.stderr[-2000:]}")
        return 1
    print(r.stdout)

    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    avisos = []
    for tupla_str, buckets in nuevo.items():
        for b, sides in buckets.items():
            for lado, info in sides.items():
                v_nuevo = info.get("veredicto", "sin_concluir")
                v_antes = previo.get(tupla_str, {}).get(b, {}).get(lado, {}).get("veredicto", "sin_concluir")
                if v_nuevo in ("bueno_confirmado", "malo_confirmado") and v_nuevo != v_antes:
                    avisos.append(
                        f"{'🟢' if v_nuevo == 'bueno_confirmado' else '🔴'} "
                        f"{tupla_str} [{b},{float(b)+0.05:.2f}) {lado} -> {v_nuevo} "
                        f"(n={info.get('n')} pnl/tr={info.get('pnl_medio')} p={info.get('p_binomial')})"
                    )

    if avisos:
        msg = "🤝 Bot consenso × MOMENTUM_IBS_5M_BALLENA — nuevos veredictos:\n" + "\n".join(avisos)
        print(msg)
        enviar_telegram(msg)
    else:
        print("Sin veredictos nuevos hoy.")

    LATCH.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
