#!/usr/bin/env python3
"""analisis_candidata9_edge_medido_real.py — 15-Sep, petición explícita
Javi ("10 propuestas para explotar MÁS el edge ya capturado", #1):
remedición PERIÓDICA del edge real (hit_rate-ask_medio) de cada bucket
ya aprobado en candidata9_gate_bucket.py::BUCKETS_APROBADOS_REAL.

Origen: EDGE_MEDIDO_REAL (candidata9_gate_bucket.py) era una foto fija
-- solo se remedía a mano cuando alguien añadía un bucket nuevo
(ETH#15min seguía con el dato de una sola sesión del 08-Sep, 7+ días sin
refrescar mientras el resto de buckets se remedían cada vez que se
tocaba el fichero). El edge cambia con el tiempo igual que cualquier
otro gate del proyecto -- el requote (live_trade.py::_decidir_requote,
vía _GATES_EXTERNOS_POR_ESTRATEGIA) usa este valor como presupuesto de
cuánto puede deteriorarse el libro antes de abortar una orden real; un
valor desactualizado puede abortar de más (edge real subió) o de menos
(edge real bajó, protección insuficiente).

Mecanismo: reusa eventos_candidata9() de analisis_candidata9_10_gate_
bucket_26ago.py (NUNCA duplicado -- misma fuente exacta que ya genera
BUCKETS_APROBADOS_REAL/el propio gate) para recalcular hit_rate-ask_medio
por (activo,marco,bucket).

16-Sep tarde (petición explícita Javi, tras /code-review sobre la
retirada de BUCKETS_APROBADOS_REAL de permitido_real(): "esto tiene que
ser así en todas las tuplas live... el sistema tiene que ser inteligente
para operar en cada momento en todos los micro-buckets confirmados"):
ya NO se limita a BUCKETS_APROBADOS_REAL -- ahora remide TODO bucket que
HOY esté `bueno_confirmado` en candidata9_10_gate_bucket.json (única
fuente de verdad, autoaprendiente), más los de BUCKETS_APROBADOS_REAL
por compatibilidad con la semilla histórica. Así cualquier bucket nuevo
que el gate diario confirme tiene su edge medido en el MISMO ciclo cron
-- candidata9_gate_bucket.py::permitido_real() exige esta medición viva
antes de operar real (fail-closed, ver docstring de esa función).

Escribe data/shadow/candidata9_edge_medido_real.json (clave
"activo#marco#bucket" -> edge), leído en caliente por
candidata9_gate_bucket.py::edge_estimado() (mtime-cache, mismo patrón
que el resto de gates del proyecto). Si un bucket confirmado no tiene
n suficiente hoy (mercado nuevo, poco histórico), simplemente no se
escribe su clave -- edge_estimado() cae al dict estático EDGE_MEDIDO_REAL
(semilla) o al fallback conservador para /evaluar/ (dry-run), pero
permitido_real() NUNCA opera real sobre ese fallback.

Cron diario (ver crontab, franja de vigías 06:00-08:33 UTC).
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_candidata9_10_gate_bucket_26ago import eventos_candidata9  # noqa: E402
from candidata9_gate_bucket import BUCKETS_APROBADOS_REAL, GATE_PATH, GATE_STEP, _bucket  # noqa: E402

OUT = REPO / "data" / "shadow" / "candidata9_edge_medido_real.json"
N_MIN = 15  # mismo mínimo que el resto de gates del proyecto -- por debajo, no concluye nada


def _buckets_confirmados_hoy() -> dict:
    """{(activo,marco): {bucket_float,...}} de TODO lo que hoy está
    bueno_confirmado en candidata9_10_gate_bucket.json para la familia
    CANDIDATA9_BOT_CONSENSO -- CANDIDATA10_CROSSACTIVO se ignora (no tiene
    executor, no opera real, ver docstring del generador del gate).
    Fail-safe: fichero ausente/corrupto -> {}."""
    try:
        datos = json.loads(GATE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    out = {}
    for clave_str, tabla in datos.items():
        if not clave_str.startswith("CANDIDATA9_BOT_CONSENSO#") or not isinstance(tabla, dict):
            continue
        _, activo, marco = clave_str.split("#")
        buckets = {float(b) for b, info in tabla.items()
                   if isinstance(info, dict) and info.get("veredicto") == "bueno_confirmado"}
        if buckets:
            out[(activo, marco)] = buckets
    return out


def main() -> int:
    eventos = eventos_candidata9()
    resultado = {}
    reporte = []
    objetivo = {k: set(v) for k, v in BUCKETS_APROBADOS_REAL.items()}
    for clave, buckets in _buckets_confirmados_hoy().items():
        objetivo.setdefault(clave, set()).update(buckets)
    for (activo, marco), buckets in objetivo.items():
        tupla_str = f"CANDIDATA9_BOT_CONSENSO#{activo}#{marco}"
        filas = eventos.get(tupla_str, [])
        for b in buckets:
            sub = [(ts, ask, pnl) for ts, ask, pnl in filas if _bucket(ask) == b]
            n = len(sub)
            if n < N_MIN:
                reporte.append(f"  {activo}#{marco}[{b:.2f}] n={n}<{N_MIN} -- se mantiene el valor previo (semilla/JSON viejo)")
                continue
            hit = sum(1 for _, _, pnl in sub if pnl > 0) / n
            ask_medio = sum(a for _, a, _ in sub) / n
            edge = hit - ask_medio
            clave = f"{activo}#{marco}#{b:.2f}"
            resultado[clave] = round(edge, 4)
            reporte.append(f"  {activo}#{marco}[{b:.2f}] n={n} hit={hit:.3f} ask_medio={ask_medio:.3f} edge={edge:+.4f}")

    # Preservar entradas de ejecuciones previas que hoy no tienen n
    # suficiente (mismo criterio "nunca perder progreso ya medido" del
    # resto del proyecto) -- solo se sobrescribe una clave si HOY hay
    # datos frescos suficientes.
    previo = {}
    if OUT.exists():
        try:
            previo = json.loads(OUT.read_text(encoding="utf-8"))
        except Exception:
            previo = {}
    fusion = {**previo, **resultado}

    tmp = OUT.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(fusion, indent=1, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    tmp.replace(OUT)

    print(f"[analisis_candidata9_edge_medido_real] {len(resultado)} bucket(s) remedidos hoy, "
          f"{len(fusion)} total en el JSON:")
    for linea in reporte:
        print(linea)
    return 0


if __name__ == "__main__":
    sys.exit(main())
