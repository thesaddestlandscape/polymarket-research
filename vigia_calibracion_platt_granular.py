#!/usr/bin/env python3
"""vigia_calibracion_platt_granular.py — Vigía diario de la calibración
Platt granular (analisis_calibracion_platt_granular.py /
data/shadow/calibracion_platt_granular.json).

Petición explícita Javi (06-Ago): avisar en cuanto una combinación
(estrategia,activo)/(estrategia,activo,marco) cruce n>=200 y se evalúe
por primera vez -- confirme o rechace la corrección -- sin tener que
revisarlo a mano cada día. Mismo patrón exacto que
vigia_gate_bucket_propio.py (28-Jul).

Origen del mecanismo que vigila: BALLENAS_TARDIAS#ETH#5min (tupla LIVE)
estaba mal_calibrado_confirmado (vigia_gate_calibracion.py) sin corrección
porque el fit solo se hacía a nivel agregado (6 monedas mezcladas). El
06-Ago se generalizó a granularidad extrema para TODAS las estrategias,
fuera del hot path del fast loop (ver analisis_calibracion_platt_
granular.py para el porqué). n=184/200 al desplegar esto -- crecimiento
reciente ~30-100/día, ETA corta.

Hace 3 cosas, mismo patrón que vigia_gate_bucket_propio.py:
1. Re-corre analisis_calibracion_platt_granular.py (results.csv crece
   cada ciclo -- una clave puede cruzar n>=200 de un día para otro).
2. Diffea contra el estado de AYER (latch) -- avisa por Telegram SOLO
   claves NUEVAS evaluadas por primera vez (antes n<200, ahora n>=200),
   diciendo si consiguió corrección o no. Marca explícitamente si la
   clave es relevante para una tupla en pares_permitidos_live (dinero
   real) -- esas se destacan aparte.
3. Reporta cobertura: cuántas claves totales, cuántas evaluadas, cuántas
   confirmadas.

Puramente informativo -- NO toca prob_yes/stake/pares_permitidos_live.
_buscar_calibracion() en shadow_predict.py ya lee el JSON directamente
(caché por mtime) -- una corrección nueva se aplica sola en cuanto este
script actualiza el fichero, el aviso es para que Javi lo sepa, no una
puerta de aprobación (esa ya se cruzó con el /code-review del mecanismo
en sí, no se repite por cada clave nueva individual).
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATA_PATH = REPO / "data/shadow/calibracion_platt_granular.json"
CONFIG_LIVE = REPO / "data/live/config_live.json"
LATCH = REPO / "data/live/vigia_calibracion_platt_granular_latch.json"


def _es_relevante_live(clave: str, pares_live: set) -> bool:
    """clave tipo 'ESTRATEGIA#ACTIVO' o 'ESTRATEGIA#ACTIVO#MARCO' --
    relevante si alguna tupla de pares_permitidos_live empieza por la
    misma estrategia+activo (con o sin marco, con cualquier dirección)."""
    partes = clave.split("#")
    prefijo = "#".join(partes[:2]) if len(partes) >= 2 else clave
    return any(p.startswith(prefijo) for p in pares_live)


def main() -> int:
    from shadow_digest import enviar_telegram

    r = subprocess.run([sys.executable, str(REPO / "analisis_calibracion_platt_granular.py")],
                        capture_output=True, text=True, timeout=300, cwd=str(REPO))
    if r.returncode != 0:
        print(f"[vigia_calibracion_granular] análisis falló: {r.stderr[-500:]}")
        return 1
    print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else "(sin salida)")

    try:
        datos = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[vigia_calibracion_granular] no se pudo leer {DATA_PATH}: {e}")
        return 1

    try:
        pares_live = set(json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
                          .get("pares_permitidos_live", []))
    except Exception:
        pares_live = set()

    latch = {}
    if LATCH.exists():
        try:
            latch = json.loads(LATCH.read_text())
        except Exception:
            latch = {}
    es_primera_ejecucion = not latch

    nuevas = []
    for clave, info in sorted(datos.items()):
        if clave in latch:
            continue  # ya evaluada antes, no repetir aviso
        nuevas.append((clave, info))
        latch[clave] = {"n": info.get("n"), "confirmado": bool(info.get("calibracion_prob"))}

    print(f"[vigia_calibracion_granular] {len(datos)} claves con n>=200 evaluadas, "
          f"{len(nuevas)} nuevas desde ayer, primera_ejecucion={es_primera_ejecucion}")

    if not es_primera_ejecucion and nuevas:
        lineas = []
        for clave, info in nuevas[:25]:
            confirmado = bool(info.get("calibracion_prob"))
            live_tag = " 🔴 RELEVANTE PARA TUPLA LIVE" if _es_relevante_live(clave, pares_live) else ""
            if confirmado:
                c = info["calibracion_prob"]
                lineas.append(f"  🟢 {clave} (n={info['n']}): CORRECCIÓN CONFIRMADA "
                               f"a={c['a']} b={c['b']} mejora_oos={c['mejora_media_oos']}{live_tag}")
            else:
                lineas.append(f"  ⚪ {clave} (n={info['n']}): evaluada, NO pasa rigor "
                               f"(sin corrección, sigue con prob_yes_modelo crudo){live_tag}")
        extra = f"\n  ... y {len(nuevas)-25} más" if len(nuevas) > 25 else ""
        msg = (
            f"📐 VIGÍA calibración Platt granular: {len(nuevas)} clave(s) NUEVA(s) "
            f"cruzaron n>=200 hoy\n" + "\n".join(lineas) + extra +
            f"\n\nDetalle completo en data/shadow/calibracion_platt_granular.json"
        )
        ok = enviar_telegram(msg)
        print(f"[vigia_calibracion_granular] aviso enviado (telegram={ok}, {len(nuevas)} nuevas)")

    LATCH.write_text(json.dumps(latch, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
