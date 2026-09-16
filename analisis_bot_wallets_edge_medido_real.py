#!/usr/bin/env python3
"""analisis_bot_wallets_edge_medido_real.py — 15-Sep, petición explícita
Javi ("masterizar" SNIPER/DISPERSO): remedición PERIÓDICA del edge real
(hit_rate-ask_medio) de cada bucket ya aprobado en bot_wallets_gate_
bucket.py::BUCKETS_APROBADOS_REAL.

Origen: dispersed_bot_executor_dryrun.py usaba un edge FIJO inventado
(ic_proxy=0.15, "conservador -- no hay IC real para señales de wallet")
tanto para el tamaño de la posición (Kelly) como para el presupuesto de
requote -- mismo hueco que CANDIDATA9 tenía hasta hoy mismo (ver
analisis_candidata9_edge_medido_real.py, mismo patrón exacto, reusado
aquí sin duplicar la idea).

Mecanismo: reusa cargar_filas() de analisis_bot_wallets_gate_bucket_
25ago.py (NUNCA duplicado -- misma fuente exacta que ya genera
BUCKETS_APROBADOS_REAL/el propio gate) para recalcular hit_rate-ask_medio
por (arquetipo,activo,marco,bucket).

16-Sep tarde (petición explícita Javi, tras /code-review sobre la
retirada de BUCKETS_APROBADOS_REAL de permitido_real(): "esto tiene que
ser así en todas las tuplas live... el sistema tiene que ser inteligente
para operar en cada momento en todos los micro-buckets confirmados"):
ya NO se limita a BUCKETS_APROBADOS_REAL (whitelist manual retirada de
permitido_real()) -- ahora remide TODO bucket que HOY esté
`bueno_confirmado` en bot_wallets_gate_bucket.json (única fuente de
verdad, autoaprendiente, igual que gate_bucket_propio.py), más los de
BUCKETS_APROBADOS_REAL por compatibilidad con la semilla histórica. Así
cualquier bucket nuevo que el gate diario confirme tiene su edge medido
en el MISMO ciclo cron, nunca corriendo con el fallback genérico --
bot_wallets_gate_bucket.py::permitido_real() exige esta medición viva
antes de operar real (fail-closed, ver docstring de esa función).

Escribe data/shadow/bot_wallets_edge_medido_real.json (clave
"arquetipo#activo#marco#bucket" -> edge), leído en caliente por
bot_wallets_gate_bucket.py::edge_estimado() (mtime-cache). Si un bucket
confirmado no tiene n suficiente hoy, simplemente no se escribe su clave
-- edge_estimado() cae al fallback conservador (0.15, mismo valor que el
ic_proxy fijo de antes) para /evaluar/ (dry-run), pero permitido_real()
NUNCA opera real sobre ese fallback.

Cron diario (ver crontab, franja de vigías 06:00-08:33 UTC).
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_bot_wallets_gate_bucket_25ago import cargar_filas  # noqa: E402
from bot_wallets_gate_bucket import BUCKETS_APROBADOS_REAL, GATE_PATH, _bucket  # noqa: E402

OUT = REPO / "data" / "shadow" / "bot_wallets_edge_medido_real.json"
N_MIN = 15  # mismo mínimo que el resto de gates del proyecto


def _buckets_confirmados_hoy() -> dict:
    """{(arquetipo,activo,marco): {bucket_float,...}} de TODO lo que hoy
    está bueno_confirmado en bot_wallets_gate_bucket.json -- fuente viva,
    autoaprendiente, generaliza la remedición a cualquier bucket nuevo sin
    esperar a que alguien lo añada a mano a BUCKETS_APROBADOS_REAL.
    Fail-safe: fichero ausente/corrupto -> {} (no añade nada nuevo, la
    unión con BUCKETS_APROBADOS_REAL de abajo sigue cubriendo la semilla)."""
    try:
        datos = json.loads(GATE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    out = {}
    for clave_str, tabla in datos.items():
        partes = clave_str.split("#")
        if len(partes) != 3 or not isinstance(tabla, dict):
            continue
        arquetipo, activo, marco = partes
        buckets = {float(b) for b, info in tabla.items()
                   if isinstance(info, dict) and info.get("veredicto") == "bueno_confirmado"}
        if buckets:
            out[(arquetipo, activo, marco)] = buckets
    return out


def main() -> int:
    grupos = cargar_filas()
    resultado = {}
    reporte = []
    objetivo = {k: set(v) for k, v in BUCKETS_APROBADOS_REAL.items()}
    for clave, buckets in _buckets_confirmados_hoy().items():
        objetivo.setdefault(clave, set()).update(buckets)
    for (arquetipo, activo, marco), buckets in objetivo.items():
        filas = grupos.get((arquetipo, activo, marco), [])
        for b in buckets:
            sub = [(ts, ask, pnl, w) for ts, ask, pnl, w in filas if _bucket(ask) == b]
            n = len(sub)
            if n < N_MIN:
                reporte.append(f"  {arquetipo}#{activo}#{marco}[{b:.2f}] n={n}<{N_MIN} -- se mantiene el valor previo")
                continue
            hit = sum(1 for _, _, pnl, _ in sub if pnl > 0) / n
            ask_medio = sum(a for _, a, _, _ in sub) / n
            edge = hit - ask_medio
            clave = f"{arquetipo}#{activo}#{marco}#{b:.2f}"
            resultado[clave] = round(edge, 4)
            reporte.append(f"  {arquetipo}#{activo}#{marco}[{b:.2f}] n={n} hit={hit:.3f} ask_medio={ask_medio:.3f} edge={edge:+.4f}")

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

    print(f"[analisis_bot_wallets_edge_medido_real] {len(resultado)} bucket(s) remedidos hoy, "
          f"{len(fusion)} total en el JSON:")
    for linea in reporte:
        print(linea)
    return 0


if __name__ == "__main__":
    sys.exit(main())
