#!/usr/bin/env python3
"""Vigía XRP fill-ability general: avisa por Telegram (una vez, latch) si el
hit-rate FILLABLE (proxy vía libro_snapshots.csv, ratio_vs_stake>=5x) de
XRP en ventana móvil reciente deja de ser peor que un coinflip -- señal de
que la microestructura de XRP (libro fino/tóxico) podría haber mejorado y
merece re-investigarse.

Origen (23-Jul): tras el retiro de XRP de pares_permitidos_live (10-Jul,
selección adversa taker confirmada: ejecutadas n=41 hit=41% -8.28€) y el
descarte del rescate maker estático (analisis_maker_xrp_tardio.py, EV
negativo en 6 precios), sesión de hoy volvió a confirmar el mismo patrón
con datos frescos y cobertura completa (candidatos_evaluacion_live tiene
las 46 tuplas XRP desde el 21-Jul): TODAS las combinaciones
estrategia#dirección con n>=10 en el subconjunto fillable caen entre
18-47% de acierto (peor que azar), pese a que en shadow sin filtrar esas
mismas estrategias muestran 60-70%+ -- selección adversa sistémica, no de
una estrategia concreta.

XRP no está bloqueada para siempre -- el diagnóstico es de liquidez/
microestructura, que puede cambiar con el tiempo (más volumen, más market
makers). Este vigía deja de mirar el histórico completo (contaminado por
el mismo período tóxico ya diagnosticado 3 veces) y solo mira la ventana
móvil de los últimos VENTANA_DIAS días, agregando TODAS las estrategias/
direcciones de XRP (el problema es de libro, no de señal) -- si el hit-rate
fillable reciente ya no es indistinguible de un coinflip (Wilson lower
bound > 0.50) con n>=N_MIN, avisa para que alguien revise si vale la pena
reabrir la investigación. NO decide nada, NO reactiva XRP solo -- decisión
de Javi siempre.

Read-only sobre libro_snapshots.csv (no toca dinero ni config).
"""
import csv
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_gate_riguroso import wilson_ci

LIBRO = REPO / "data/live/libro_snapshots.csv"
LATCH = REPO / "data/live/vigia_xrp_fillability_latch.json"

VENTANA_DIAS = 14
N_MIN = 40
RATIO_MIN = 5.0


def _cargar_latch():
    try:
        return json.loads(LATCH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _filas_fillable_recientes():
    corte = (datetime.now(timezone.utc) - timedelta(days=VENTANA_DIAS)).isoformat()
    filas = []
    if not LIBRO.exists():
        return filas
    with open(LIBRO, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("motivo") != "candidato_evaluacion":
                continue
            if not r.get("subtype", "").startswith("XRP"):
                continue
            if (r.get("timestamp_utc") or "") < corte:
                continue
            try:
                ratio = float(r.get("ratio_vs_stake") or 0)
            except (TypeError, ValueError):
                continue
            if ratio < RATIO_MIN:
                continue
            filas.append(r)
    return filas


def _outcomes_index():
    idx = {}
    results = REPO / "data/shadow/results.csv"
    if not results.exists():
        return idx
    with open(results, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("subtype", "").startswith("XRP"):
                continue
            if r.get("acierto") not in ("0", "1"):
                continue
            idx[(r["market_id"], r["strategy"], r["decision"])] = r
    return idx


def main() -> int:
    latch = _cargar_latch()
    if latch.get("avisado"):
        print(f"[vigia_xrp_fillability] ya avisado el {latch.get('avisado_en')} -- nada que hacer")
        return 0

    snapshots = _filas_fillable_recientes()
    outcomes = _outcomes_index()

    matched = []
    for r in snapshots:
        k = (r["market_id"], r["strategy"], r["direction"])
        o = outcomes.get(k)
        if o is not None:
            matched.append(o)

    n = len(matched)
    print(f"[vigia_xrp_fillability] ventana {VENTANA_DIAS}d: n={n}/{N_MIN} snapshots fillable con outcome")
    if n < N_MIN:
        return 0

    aciertos = sum(1 for o in matched if o["acierto"] == "1")
    hit = aciertos / n
    lo, hi = wilson_ci(aciertos, n)
    print(f"[vigia_xrp_fillability] hit={hit*100:.1f}% Wilson90%=[{lo*100:.1f}%,{hi*100:.1f}%]")

    if lo <= 0.50:
        return 0  # sigue sin distinguirse de un coinflip -- nada que avisar

    msg = (
        f"🐢 VIGÍA XRP fill-ability: la ventana móvil de los últimos {VENTANA_DIAS} días "
        f"ya NO es indistinguible de un coinflip (antes sí, 3 diagnósticos: 10-Jul dinero real, "
        f"21-Jul y 23-Jul proxy de libro).\n"
        f"n={n}  hit={hit*100:.1f}%  Wilson90%=[{lo*100:.1f}%,{hi*100:.1f}%] (lower bound > 50%)\n"
        f"Posible señal de que la microestructura de XRP mejoró -- NO decide nada solo, "
        f"revisar con analisis_fills.py + analisis_gate_riguroso.py por estrategia antes de "
        f"considerar reabrir. Decisión de reactivar sigue siendo 100% tuya."
    )
    try:
        from shadow_digest import enviar_telegram
        ok = enviar_telegram(msg)
        print(f"[vigia_xrp_fillability] aviso enviado (telegram={ok})")
    except Exception as e:
        print(f"[vigia_xrp_fillability] error enviando telegram: {e}")
        ok = False

    latch["avisado"] = True
    latch["avisado_en"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    latch["n"] = n
    latch["hit"] = round(hit, 4)
    latch["wilson_lo"] = round(lo, 4)
    LATCH.write_text(json.dumps(latch, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_xrp_fillability] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
