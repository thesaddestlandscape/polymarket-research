#!/usr/bin/env python3
"""vigia_sports_promocion_n40.py — 27-Ago, petición explícita Javi tras
el checklist de promoción de CS#SEGUIR[0.24,0.29): todo el checklist
pasa limpio (fill-ability real, concentración sana, payout muy por
encima de breakeven, Kelly g>0) salvo el n mínimo del proyecto (n≥40) --
hoy en n=21. En vez de esperar a acordarnos de revisarlo, este vigía
lo vigila cada día y avisa por Telegram en el momento exacto en que
cruce el umbral.

Distinto de vigia_sports_wallet_mirror_gate_bucket_fino.py: ese avisa
cuando el VEREDICTO cambia (sin_concluir -> confirmado); CS#SEGUIR ya
está en bueno_confirmado desde el 26-Ago, así que ese vigía no vuelve a
avisar aunque n siga creciendo. Este vigía vigila específicamente el
cruce del umbral de PROMOCIÓN (n>=40), que es un umbral distinto y más
alto que el de "confirmado" del gate (n>=15).

Lee el JSON que YA regenera vigia_sports_wallet_mirror_gate_bucket_fino.py
a diario (cron 07:07 UTC) -- no re-ejecuta el análisis, solo lo lee y
compara contra el umbral. Cron sugerido: justo después, 07:09 UTC.

Puramente informativo. No promociona nada por sí solo, no toca
config_live.json ni ningún fichero de producción -- avisa para que
Javi decida.

02-Sep (bug real encontrado en barrido de sesión): el script NUNCA
comprobaba `pares_permitidos_live` -- CS#SEGUIR y CS#FADE se
promocionaron el 01-Sep (ver `_pares_cs_seguir_fade_promocion_nota_
2026-09-01` en config_live_sports.json) pero siguieron en VIGILADAS,
así que en cuanto el gate FINO (distinto del grid usado para la
promoción) cruzó su propio n=40 el vigía volvió a avisar "LISTA PARA
REVISAR PROMOCIÓN" sobre algo YA promocionado. Fix: comprobar contra
`config_live_sports.json::pares_permitidos_live` antes de avisar --
si ya está en whitelist, el mensaje cambia a informativo (confirmación
adicional, no una promoción pendiente).
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/sports/wallet_mirror_gate_bucket_fino.json"
CONFIG_PATH = REPO / "data/sports/config_live_sports.json"
LATCH = REPO / "data/live/vigia_sports_promocion_n40_latch.json"

N_PROMOCION = 40

# Tuplas en seguimiento activo hacia promoción -- añadir aquí cuando el
# checklist de promoción se revise y quede pendiente solo por n.
VIGILADAS = [
    "CS#SEGUIR",
    "CS#FADE",
]


def _ya_promocionada(tupla_str: str, config: dict) -> bool:
    """True si YA existe alguna entrada categoria#tipo#lo:hi en
    pares_permitidos_live para esta categoria#tipo (cualquier bucket) --
    no comparamos el bucket exacto porque el fino usa ventana deslizante,
    no el mismo grid que decidió la promoción original."""
    prefijo = f"{tupla_str}#"
    return any(p.startswith(prefijo) for p in config.get("pares_permitidos_live", []))


def main() -> int:
    from shadow_digest import enviar_telegram

    if not DATA_PATH.exists():
        print("sin datos todavía (wallet_mirror_gate_bucket_fino.json no existe)")
        return 1

    nuevo = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    try:
        config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except Exception:
        config = {}
    try:
        previo = json.loads(LATCH.read_text(encoding="utf-8")) if LATCH.exists() else {}
    except Exception:
        previo = {}

    avisos = []
    estado_plano = {}
    for tupla_str in VIGILADAS:
        info = nuevo.get(tupla_str)
        if not info:
            continue
        n = info.get("n", 0)
        veredicto = info.get("veredicto")
        estado_plano[tupla_str] = n
        n_antes = previo.get(tupla_str, 0)
        cruzo_ahora = n >= N_PROMOCION and n_antes < N_PROMOCION
        if cruzo_ahora and veredicto == "bueno_confirmado":
            ya_promocionada = _ya_promocionada(tupla_str, config)
            if ya_promocionada:
                avisos.append(
                    f"ℹ️ {tupla_str} [{info['lo']:.2f},{info['hi']:.2f}) cruzó n={n}>={N_PROMOCION} "
                    f"(pnl/tr={info['pnl_medio']:+.3f} p={info['p_valor']}) -- YA está en "
                    f"pares_permitidos_live, esto solo refuerza la confirmación (no requiere decisión)"
                )
            else:
                avisos.append(
                    f"🚀 {tupla_str} [{info['lo']:.2f},{info['hi']:.2f}) cruzó n={n}>={N_PROMOCION} "
                    f"(pnl/tr={info['pnl_medio']:+.3f} p={info['p_valor']}) -- LISTA PARA REVISAR PROMOCIÓN"
                )
        print(f"{tupla_str}: n={n}/{N_PROMOCION} veredicto={veredicto} "
              f"ya_promocionada={_ya_promocionada(tupla_str, config)}")

    if avisos:
        msg = "🎯 Sports — candidata cruzó el umbral de promoción (n≥40):\n" + "\n".join(avisos)
        print(msg)
        enviar_telegram(msg)
    else:
        print("Ninguna vigilada ha cruzado n=40 todavía.")

    LATCH.write_text(json.dumps(estado_plano, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
