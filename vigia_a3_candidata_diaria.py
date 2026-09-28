#!/usr/bin/env python3
"""vigia_a3_candidata_diaria.py -- (28-Sep, petición explícita Javi: "anota
seguir vigilando A3 con los hallazgos diariamente"). Reusa TODO el motor de
vigia_saltos_ask_real.py -- incluida cargar_resueltos() (extraída de su
main() el mismo día, /code-review: esta vigía reimplementaba ese mismo
bucle resolver/filtrar antes, riesgo real de divergencia silenciosa) --
solo añade el corte "segundo salto + BTC + Up" encontrado hoy (la única
pista de A3 que no está claramente refutada tras agotar 12 ángulos, ver
memoria idea_a3_exploracion_exhaustiva_cerrada_28sep).

Estado a 28-Sep (referencia, NO se repite el cálculo aquí cada vez que se
lee este docstring -- el JSON/Telegram de cada corrida es la fuente de
verdad): n=1.025, 602 mercados, EV=+0,025€/tr, IC90=[-0,007,+0,054]
(casi no cruza cero) pero split-half FALLA (mitad1 negativa) -- no es
candidata todavía, es la pista a vigilar.

"Segundo salto": salto de precio-justo en el MISMO mercado (slug), MISMA
dirección implícita, <=30s después de un salto anterior en ese mercado --
proxy de "el mercado confirma la tendencia" en vez de un salto aislado.

MODO LECTURA. Salida: data/shadow/vigia_a3_candidata_diaria.json +
Telegram diario (SIEMPRE, no solo hallazgos nuevos -- mismo criterio que
vigia_dispersed_bot_progreso_diario.py: es seguimiento de una pista, no
una alerta puntual)."""
import collections
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
csv.field_size_limit(10_000_000)

import vigia_saltos_ask_real as v  # noqa: E402

OUT = REPO / "data/shadow/vigia_a3_candidata_diaria.json"
VENTANA_SEGUNDO_SALTO_S = 30


def _cargar_filas():
    """Devuelve TODOS los saltos resueltos (fillables o no) -- /code-review 28-Sep,
    hallazgo real: filtrar por fillability ANTES de construir la cadena de "segundo
    salto" descartaba saltos1 no-fillables, dejando huérfano al salto2 que SÍ era
    fillable (nunca tenía un i-1 contra el que compararse) -- infracontaba la señal
    que este script existe para medir. La fillability se marca por fila (campo
    "fillable") y se aplica SOLO al filtrar `candidata` en main(), después de que
    la cadena ya esté construida sobre el universo completo de saltos del mercado."""
    xs_base, _pendientes, _sin_libro, _fuente_res, _n_totales = v.cargar_resueltos()
    xs = []
    for x in xs_base:
        ask, gana = x["ask"], x["gana"]
        # /code-review 28-Sep, hallazgo GRAVE: la versión anterior usaba x["ini"] (apertura
        # de la ventana del mercado, CONSTANTE para todas las señales de ese mercado) como
        # "ts_epoch" -- la comprobación "<=30s del salto anterior" nunca medía tiempo real,
        # veía siempre una diferencia de 0s entre cualquier par de señales del mismo mercado
        # (verificado con datos reales: un mercado con 7 señales en 206s reales, todas
        # marcadas como "segundo salto" igual). Fix: parsear el timestamp REAL de la señal
        # (`t`, formato ISO con milisegundos) a epoch.
        try:
            ts_real = datetime.fromisoformat(x["t"]).timestamp()
        except (ValueError, TypeError):
            continue  # timestamp ilegible -- fail-closed, esta señal no puede compararse
        fillable = v.es_fillable(x["ratio"], ask)
        xs.append({"gana": gana, "px_ev": ask, "ev": v.pnl(ask, gana), "activo": x["activo"],
                   "marco": x["marco"], "dia": x["dia"], "direccion": x["direccion"],
                   "ts_epoch": ts_real, "slug": x["slug"], "t": x["t"], "fillable": fillable})
    return xs


def _marcar_segundo_salto(xs: list) -> set:
    """IDs (id() de fila) de señales que son un SEGUNDO salto confirmando
    tendencia -- mismo mercado (slug), misma dirección, <=VENTANA_SEGUNDO_
    SALTO_S del salto anterior en ESE mercado.

    /code-review 28-Sep, hallazgo real: la primera versión agrupaba por
    `activo` (no por `slug`) antes de ordenar y comparar con el vecino
    inmediato -- con varios marcos del mismo activo corriendo a la vez
    (5min/15min/60min), un salto de OTRO mercado del mismo activo podía
    colarse entre dos saltos reales del MISMO mercado en el orden temporal
    global, haciendo que `grupo_ord[i-1]` ya no fuera el salto anterior
    real de ese mercado -- infracontando segundos saltos genuinos. Agrupar
    directamente por `slug` lo evita por construcción (cada grupo es un
    único mercado, sin mezcla)."""
    por_slug = collections.defaultdict(list)
    for x in xs:
        por_slug[x["slug"]].append(x)
    segundo_ids = set()
    for grupo in por_slug.values():
        grupo_ord = sorted(grupo, key=lambda x: x["ts_epoch"])
        for i in range(1, len(grupo_ord)):
            prev, cur = grupo_ord[i - 1], grupo_ord[i]
            if (cur["ts_epoch"] - prev["ts_epoch"] <= VENTANA_SEGUNDO_SALTO_S
                    and cur["direccion"] == prev["direccion"]):
                segundo_ids.add(id(cur))
    return segundo_ids


def main() -> int:
    xs = _cargar_filas()
    segundo_ids = _marcar_segundo_salto(xs)  # cadena construida sobre TODOS los saltos, fillables o no

    candidata = [x for x in xs if id(x) in segundo_ids and x["activo"] == "BTC" and x["direccion"] == "Up"
                 and x["fillable"]]
    r_candidata = v.resumen(candidata, "ev")

    salida = {"actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "candidata": "segundo_salto_BTC_Up", "resumen": r_candidata}
    OUT.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")

    msg = ["🔬 A3 -- seguimiento diario de la única pista no refutada (segundo salto + BTC + Up)"]
    if r_candidata:
        mitades = r_candidata.get("mitades")
        mitades_ok = mitades is not None and mitades[0] > 0 and mitades[1] > 0
        ic = r_candidata.get("ic90_dias")
        ic_ok = ic is not None and ic[0] > 0
        gate_n_dias_ev = r_candidata["n"] >= 40 and r_candidata["dias"] >= 5 and r_candidata["ev"] >= 0.10
        veredicto = "CANDIDATA robusta" if (gate_n_dias_ev and mitades_ok and ic_ok) else "sigue sin confirmar"
        msg.append(f"n={r_candidata['n']} días={r_candidata['dias']} acierto={r_candidata['acierto']:.0%} "
                   f"EV/€={r_candidata['ev']:+.4f} IC90_dias={ic} mitades={mitades} -> {veredicto}")
    else:
        msg.append("sin señales todavía")
    msg.append("Recordatorio: A3 en su forma general (comprar el salto a cualquier precio) sigue "
               "refutado -- esta es la ÚNICA sub-variante que no lo está, y tampoco está confirmada.")
    texto = "\n".join(msg)
    print(texto)
    try:
        from shadow_digest import enviar_telegram
        ok = enviar_telegram(texto, bot="cripto")
        print(f"telegram: {'ok' if ok else 'fallo'}")
    except Exception as e:
        print(f"aviso: no se pudo enviar Telegram: {type(e).__name__}: {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
