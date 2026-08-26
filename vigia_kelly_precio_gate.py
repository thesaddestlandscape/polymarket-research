#!/usr/bin/env python3
"""vigia_kelly_precio_gate.py — 26-Ago, mismo patrón que el resto de
vigías de "punto ciego" de esta sesión. `analisis_kelly_precio_gate_
29jul.py` corre a diario (cron `52 6 * * *`) y `kelly_precio_gate.json`
está ACTIVAMENTE conectado a `live_stake.py::calcular_stake()` -- cada
bucket que pasa a "confirmado" cambia YA el tamaño real de las apuestas
(ratio_correccion multiplica el stake). A diferencia de gate_bucket_
propio (que solo VETA), esto MODIFICA cuánto dinero real se apuesta --
más razón todavía para que Javi se entere el mismo día, no solo si lee
el JSON a mano.

Avisa por Telegram solo veredictos NUEVOS (latch, misma clave
familia#subtype#bucket), con el ratio_correccion (>1 = apostar más de
lo que Kelly-IC decía, <1 = apostar menos) para que se vea de un vistazo
si el cambio va a subir o bajar el stake.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/shadow/kelly_precio_gate.json"
LATCH = REPO / "data/live/vigia_kelly_precio_gate_latch.json"


def main() -> int:
    from shadow_digest import enviar_telegram

    r = subprocess.run(
        [sys.executable, str(REPO / "analisis_kelly_precio_gate_29jul.py")],
        capture_output=True, text=True, timeout=180, cwd=str(REPO),
    )
    if r.returncode != 0:
        print(f"ERROR ejecutando analisis_kelly_precio_gate_29jul.py: {r.stderr[-2000:]}")
        return 1

    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    avisos = []
    estado_plano = {}
    for fam, subtypes in nuevo.get("familias", {}).items():
        for sub, buckets in subtypes.items():
            for b, info in buckets.items():
                clave = f"{fam}#{sub}#{b}"
                v_nuevo = info.get("veredicto", "sin_concluir")
                estado_plano[clave] = v_nuevo
                v_antes = previo.get(clave, "sin_concluir")
                if v_nuevo == "confirmado" and v_antes != "confirmado":
                    ratio = info.get("ratio_correccion")
                    direccion = "⬆️ SUBE" if (ratio or 0) > 1 else ("⬇️ BAJA" if (ratio or 0) < 1 else "→ neutro")
                    avisos.append(
                        f"⚖️ {clave} -> confirmado, ratio_correccion={ratio} ({direccion} el stake) "
                        f"n={info.get('n')} shuffle_p={info.get('shuffle_p')}"
                    )

    if avisos:
        msg = (
            "⚖️ Kelly-precio gate — nuevos buckets confirmados (afectan al stake real HOY):\n"
            + "\n".join(avisos)
        )
        print(msg)
        enviar_telegram(msg)
    else:
        n_conf = sum(1 for v in estado_plano.values() if v == "confirmado")
        print(f"Sin veredictos nuevos hoy ({n_conf} buckets confirmados en total).")

    LATCH.write_text(json.dumps(estado_plano, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
