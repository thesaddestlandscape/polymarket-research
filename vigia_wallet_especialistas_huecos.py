#!/usr/bin/env python3
"""vigia_wallet_especialistas_huecos.py — 26-Ago, petición explícita e
imperativa de Javi: "no podemos permitirnos perder señales de wallets
especialistas, informadas, ballenas... tenemos que tener toda la
información existente."

Bug de proceso real cazado esta sesión: `wallet_especialistas_observer.py`
lleva desde el 23-Jul corriendo a diario (cron `45 6 * * *`) y YA
CALCULA los huecos de cobertura (wallet especialista con edge validado,
n propio<15 en ese activo/marco) -- pero solo los IMPRIME en el log,
nunca avisa. El hueco de BNB#15min (wallet con n=240, edge+12,65pp,
cobertura propia=0) llevaba desde el 23-Ago sin que nadie lo viera hasta
el barrido manual de hoy. Mismo patrón exacto que motivó
`feedback_proactividad_puntos_ciegos` -- "vigía, no promesa": nunca más
depender de que alguien relea el log a mano.

Lee `data/shadow/wallet_especialistas_state.json` (ya escrito por
wallet_especialistas_observer.py, que corre justo antes en cron) y
avisa por Telegram SOLO huecos NUEVOS (latch, misma clave
wallet#activo#marco que el propio observer) con edge_pp>=UMBRAL_EDGE y
n>=UMBRAL_N -- evita alertar de huecos triviales (n bajo o edge
marginal), reserva la alerta para candidatos con volumen real.

Puramente informativo. NO crea ninguna estrategia ni conecta a
ejecutores -- eso requiere diseño explícito (ver memoria de la sesión,
26-Ago) y aprobación de Javi caso por caso.
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

STATE = REPO / "data/shadow/wallet_especialistas_state.json"
LATCH = REPO / "data/live/vigia_wallet_especialistas_huecos_latch.json"

UMBRAL_N = 40
UMBRAL_EDGE_PP = 5.0
UMBRAL_COBERTURA_PROPIA_N = 15


def main() -> int:
    from shadow_digest import enviar_telegram

    if not STATE.exists():
        print("wallet_especialistas_state.json no existe todavía -- nada que hacer.")
        return 0
    estado = json.loads(STATE.read_text(encoding="utf-8"))
    wallets = estado.get("wallets", {})

    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    huecos = {
        clave: v for clave, v in wallets.items()
        if v.get("cobertura_propia_n", 0) < UMBRAL_COBERTURA_PROPIA_N
        and v.get("n", 0) >= UMBRAL_N
        and abs(v.get("edge_pp", 0)) >= UMBRAL_EDGE_PP
    }
    print(f"Huecos de cobertura totales (n>={UMBRAL_N}, |edge_pp|>={UMBRAL_EDGE_PP}, "
          f"cobertura_propia_n<{UMBRAL_COBERTURA_PROPIA_N}): {len(huecos)}")

    nuevos = {k: v for k, v in huecos.items() if k not in previo}
    avisos = []
    for clave, v in sorted(nuevos.items(), key=lambda kv: -kv[1]["n"]):
        avisos.append(
            f"🕳️ HUECO {v['wallet'][:12]}... {v['activo']}#{v['marco']} "
            f"n_wallet={v['n']} hit={v['hit']:.3f} edge_pp={v['edge_pp']:+.2f} "
            f"precio_medio={v['precio_medio']:.3f} -- nuestro n=0-{UMBRAL_COBERTURA_PROPIA_N - 1}"
        )

    if avisos:
        msg = (
            "🐋 Wallets especialistas — huecos de cobertura NUEVOS "
            "(edge validado, sin señal propia ahí):\n" + "\n".join(avisos)
        )
        print(msg)
        enviar_telegram(msg)
    else:
        print("Sin huecos nuevos hoy.")

    LATCH.write_text(json.dumps(huecos, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
