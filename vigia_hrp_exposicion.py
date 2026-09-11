#!/usr/bin/env python3
"""vigia_hrp_exposicion.py — 26-Ago, mismo patrón que
vigia_wallet_especialistas_huecos.py de esta sesión: `analisis_hrp_
exposicion_diaria.py` corre cada 2h (cron `10 */2 * * *`) desde el
27-Jul y calcula `excede_techo_hrp_x1_5` por tupla madura, pero solo lo
escribe en el JSON -- nunca avisa. Encontrado hoy marcando en vivo
`BALLENAS_CONFIRMADAS_15M#ETH#15min#BUY_YES` al 100% de la exposición
reciente, excediendo su techo HRP -- la misma tupla que disparó el
circuit breaker esta madrugada. Punto ciego real, mismo defecto de
proceso que motivó `feedback_proactividad_puntos_ciegos`.

Avisa por Telegram cuando una tupla madura excede el techo HRP x1.5,
con un latch por FECHA (no solo por tupla) para no repetir el mismo
aviso cada 2 horas mientras la condición persiste -- máximo un aviso
por tupla por día, pero si sigue excedida al día siguiente SÍ vuelve a
avisar (a diferencia del resto de vigías de esta sesión, aquí la
persistencia del riesgo es justo lo que interesa que no se pierda de
vista, no solo el cambio de estado).

Puramente informativo -- NO aplica ningún límite real en live_stake.py.
Decisión de convertir esto en techo real sigue siendo 100% de Javi, con
/code-review antes (ver idea_propuesta_hrp_portfolio_23jul).
"""
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/shadow/hrp_exposicion_diaria.json"
LATCH = REPO / "data/live/vigia_hrp_exposicion_latch.json"


def main() -> int:
    from shadow_digest import enviar_telegram

    r = subprocess.run(
        [sys.executable, str(REPO / "analisis_hrp_exposicion_diaria.py")],
        capture_output=True, text=True, timeout=120, cwd=str(REPO),
    )
    if r.returncode != 0:
        print(f"ERROR ejecutando analisis_hrp_exposicion_diaria.py: {r.stderr[-2000:]}")
        return 1

    if not DATA_PATH.exists():
        print("hrp_exposicion_diaria.json no se generó -- nada que hacer.")
        return 0
    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    hoy = datetime.now(timezone.utc).date().isoformat()

    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    excedidas = [t for t in nuevo.get("tuplas_maduras", []) if t.get("excede_techo_hrp_x1_5")]
    avisos = []
    for t in excedidas:
        clave = t["tupla"]
        ultima_alerta = previo.get(clave)
        if ultima_alerta == hoy:
            continue
        avisos.append(
            f"⚖️ {clave} excede techo HRP x1,5 -- peso_hrp={t['peso_hrp']:.3f} "
            f"exposición={t['exposicion_reciente_eur']:.2f}€ "
            f"(share={t['share_exposicion_reciente']:.0%} de la exposición reciente total)"
        )
        previo[clave] = hoy

    # limpiar del latch las que ya no excedan (para que si vuelven a exceder mañana avisen igual)
    claves_excedidas_hoy = {t["tupla"] for t in excedidas}
    previo = {k: v for k, v in previo.items() if k in claves_excedidas_hoy}

    if avisos:
        msg = "⚖️ HRP exposición — tuplas excediendo techo x1,5:\n" + "\n".join(avisos)
        print(msg)
        enviar_telegram(msg)
    else:
        print(f"Sin avisos nuevos hoy ({len(excedidas)} tuplas excedidas ya avisadas hoy).")

    LATCH.write_text(json.dumps(previo, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
