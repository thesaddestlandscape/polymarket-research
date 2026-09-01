#!/usr/bin/env python3
"""vigia_gate_bucket_wallet_mirror_fino.py — 01-Sep, vigía de la ventana
deslizante (fino) de WALLET_MIRROR cripto (analisis_wallet_mirror_gate_
bucket_fino_25ago.py), mismo patrón que vigia_gate_bucket_wallet_mirror.py
(grid) y vigia_sports_wallet_mirror_gate_bucket_fino.py (hermano de
sports, ya desplegado).

Hueco real encontrado la misma noche (petición explícita Javi: "no lo
podemos permitir, tiene que hacerlo cada vez que se vaya a hacer un
trade, sino corremos riesgo de perder pasta"): el fino de WALLET_MIRROR
cripto NUNCA tuvo un vigía programado -- a diferencia del grid (vigia_
gate_bucket_wallet_mirror.py, cada hora vía vigias_frecuentes_fase0.py)
y del hermano de sports (cron 07:07 UTC), el fino de cripto solo se
había ejecutado a mano (última vez 25-Ago, hasta que se reejecutó
manualmente esta noche). Con el guardián de frescura nuevo en
wallet_mirror_gate_bucket.py (MAX_ANTIGUEDAD_S=2h15min), sin este vigía
las 2 zonas de WALLET_MIRROR reabiertas esta noche que dependen del fino
(BTC#15min[0.09,0.14), ETH#15min[0.22,0.27), ambas origen=ventana_
deslizante_25ago) habrían quedado fail-closed por antigüedad en un par
de horas, sin nadie regenerando el dato.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/shadow/wallet_mirror_gate_bucket_fino.json"
LATCH = REPO / "data/live/vigia_gate_bucket_wallet_mirror_fino_latch.json"


def main() -> int:
    from shadow_digest import enviar_telegram

    r = subprocess.run(
        [sys.executable, str(REPO / "analisis_wallet_mirror_gate_bucket_fino_25ago.py")],
        capture_output=True, text=True, timeout=300, cwd=str(REPO),
    )
    if r.returncode != 0:
        print(f"ERROR ejecutando analisis_wallet_mirror_gate_bucket_fino_25ago.py: {r.stderr[-2000:]}")
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
                f"(n={info.get('n')} pnl/tr={info.get('pnl_medio')} p={info.get('p_valor')})"
            )
        elif v_antes != "sin_concluir" and v_nuevo == "sin_concluir":
            avisos.append(f"⚠️ {clave_str} revierte a sin_concluir (era {v_antes})")

    if avisos:
        msg = "🪞 Wallet Mirror gate bucket FINO — cambios hoy:\n" + "\n".join(avisos)
        print(msg)
        enviar_telegram(msg)
    else:
        print("Sin cambios de veredicto en el fino hoy.")

    LATCH.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
