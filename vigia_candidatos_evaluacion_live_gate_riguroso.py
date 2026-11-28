#!/usr/bin/env python3
"""
vigia_candidatos_evaluacion_live_gate_riguroso.py -- 31-Ago, petición
explícita Javi: "del punto 7 tienes que hacer un control diario y
avisarme cuando acumule N y pase los gates. De hecho deberás hacerlo con
todas las estrategias que tenemos en candidatas evaluacion live".

NO reimplementa el gate -- reusa analisis_gate_riguroso.py entero
(cargar_candidatos/cargar_filas/gate/benjamini_hochberg), que ya aplica
a las 409 tuplas de config_live.json::candidatos_evaluacion_live el
mismo rigor que el resto del proyecto: n>=40, IC>=0.08, Wilson90% no
cruza 0.5, shuffle p<0.05, PnL bootstrap CI90% no cruza cero, y
corrección BH-FDR por comparaciones múltiples sobre las K candidatas
evaluadas simultáneamente ese día.

Este vigía es la capa que faltaba: persiste el veredicto de cada tupla
día a día (data/shadow/candidatos_evaluacion_live_gate_riguroso.json) y
avisa por Telegram SOLO la primera vez que una tupla cruza a "GATE OK"
(latch, mismo patrón que vigia_gate_bucket_propio.py/vigia_log_growth.py
-- nunca reenvía el mismo aviso). También reporta si una tupla que
estaba en GATE OK deja de estarlo (para no perder de vista una reversión
real, aunque no es lo que Javi pidió explícitamente, es el mismo
principio de "nunca fallar silenciosamente" del resto del proyecto).

Puramente informativo -- NO promociona nada a pares_permitidos_live por
sí solo (esa decisión sigue siendo manual, con checklist de 6 categorías
y aprobación explícita de Javi, CLAUDE.md). Solo dice "esta tupla ya
tiene el rigor estadístico mínimo para que valga la pena revisarla".

Cron sugerido: después de que results.csv/postmortem del día hayan
corrido un rato (el fast loop resuelve cada ~20s, así que cualquier hora
sirve) -- se deja en la misma franja que el resto de vigías de gate,
07:20 UTC (después del resumen diario único, 07:15).
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_gate_riguroso import (  # noqa: E402
    cargar_candidatos, gate, benjamini_hochberg, RES,
)
from shadow_digest import enviar_telegram  # noqa: E402

OUT = REPO / "data" / "shadow" / "candidatos_evaluacion_live_gate_riguroso.json"
LATCH = REPO / "data" / "live" / "vigia_candidatos_evaluacion_live_latch.json"


def cargar_filas(claves):
    """27-Nov: misma semantica que analisis_gate_riguroso.cargar_filas (filas con `acierto`
    resuelto de las claves buscadas) pero conservando SOLO las columnas que usa gate()
    (acierto, pnl_neto). El original guardaba el DictReader completo (features JSON, question):
    ~3 GB sobre 1,5 GB de results.csv, y bajo el MemoryHigh del cgroup de cron_pesado se atascaba 1 h.
    No se edita analisis_gate_riguroso.py: lo importa wallet_mirror_tracker (cadena de observadores)."""
    import csv
    csv.field_size_limit(1 << 27)
    wanted = {(s, sub, d) for _, s, sub, d in claves}
    filas = {}
    with open(RES, newline="") as f:
        rd = csv.reader(f)
        cab = next(rd)
        i_s, i_sub, i_d = cab.index("strategy"), cab.index("subtype"), cab.index("decision")
        i_a, i_p = cab.index("acierto"), cab.index("pnl_neto")
        mx = max(i_s, i_sub, i_d, i_a, i_p)
        for r in rd:
            if len(r) <= mx or r[i_a] == "":
                continue
            k = (r[i_s], r[i_sub], r[i_d])
            if k in wanted:
                filas.setdefault(k, []).append({"acierto": r[i_a], "pnl_neto": r[i_p]})
    return filas


def _cargar_latch() -> dict:
    try:
        return json.loads(LATCH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _guardar_latch(latch: dict) -> None:
    LATCH.write_text(json.dumps(latch, ensure_ascii=False, indent=1), encoding="utf-8")


def main() -> int:
    claves = cargar_candidatos()
    filas_por_clave = cargar_filas(claves)

    resultados = []
    for tupla, strat, sub, dec in claves:
        rows = filas_por_clave.get((strat, sub, dec), [])
        g = gate(rows)
        resultados.append((tupla, g))

    con_datos = [(i, r[1]["p_shuf"]) for i, r in enumerate(resultados) if r[1] is not None]
    keep_bh = benjamini_hochberg([p for _, p in con_datos]) if con_datos else []
    bh_ok = {con_datos[j][0] for j, k in enumerate(keep_bh) if k}

    salida = {}
    for i, (tupla, g) in enumerate(resultados):
        if g is None:
            salida[tupla] = {"n": 0, "veredicto": "sin datos"}
            continue
        razones = [] if g["veredicto"] == "GATE OK" else [g["veredicto"].split(": ", 1)[1]]
        if i not in bh_ok:
            razones.append("no sobrevive FDR-BH multi-test")
        veredicto = "GATE OK" if not razones else "NO CONCLUYENTE: " + ", ".join(razones)
        entrada = dict(g)
        entrada["veredicto_final"] = veredicto
        salida[tupla] = entrada

    latch = _cargar_latch()
    nuevos_gate_ok = []
    reversiones = []
    for tupla, entrada in salida.items():
        estaba_ok = latch.get(tupla, {}).get("gate_ok", False)
        esta_ok = entrada.get("veredicto_final") == "GATE OK"
        if esta_ok and not estaba_ok:
            nuevos_gate_ok.append((tupla, entrada))
        elif estaba_ok and not esta_ok:
            reversiones.append((tupla, entrada))
        latch[tupla] = {"gate_ok": esta_ok, "n": entrada.get("n", 0)}

    OUT.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    _guardar_latch(latch)

    print(f"[vigia_candidatos_evaluacion_live] {len(salida)} tuplas evaluadas, "
          f"{sum(1 for e in salida.values() if e.get('veredicto_final') == 'GATE OK')} en GATE OK, "
          f"{len(nuevos_gate_ok)} nuevas hoy, {len(reversiones)} revirtieron")

    if not nuevos_gate_ok and not reversiones:
        return 0

    lineas = [f"🎯 *Candidatos evaluación live — cambios de gate riguroso hoy*"]
    if nuevos_gate_ok:
        lineas.append(f"\n🟢 *{len(nuevos_gate_ok)} nueva(s) en GATE OK* (n≥40, IC≥0.08, Wilson+shuffle+PnL bootstrap+BH-FDR):")
        for tupla, e in nuevos_gate_ok:
            pnl_str = f" pnl/tr={e['pnl_media']:+.3f}€" if "pnl_media" in e else ""
            lineas.append(f"  {tupla} n={e['n']} hit={e['hit']*100:.1f}% ic={e['ic']:+.3f}{pnl_str}")
    if reversiones:
        lineas.append(f"\n🔴 *{len(reversiones)} revirtieron* (estaban GATE OK, ya no):")
        for tupla, e in reversiones:
            lineas.append(f"  {tupla} n={e['n']} -> {e.get('veredicto_final')}")
    lineas.append(f"\nRecuerda: GATE OK = rigor estadístico mínimo, NO promoción automática. "
                   f"Sigue el checklist de 6 categorías antes de tocar pares_permitidos_live.")
    texto = "\n".join(lineas)
    if len(texto) > 4000:
        texto = texto[:3950] + "\n\n… (truncado, ver " + str(OUT) + ")"
    ok = enviar_telegram(texto, bot="cripto")
    print(f"Telegram enviado={ok}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
