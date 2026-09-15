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
por (arquetipo,activo,marco,bucket) sobre TODOS los buckets ya aprobados
hoy -- nunca añade buckets nuevos a la whitelist, solo remide el edge de
los que Javi ya aprobó explícitamente.

Escribe data/shadow/bot_wallets_edge_medido_real.json (clave
"arquetipo#activo#marco#bucket" -> edge), leído en caliente por
bot_wallets_gate_bucket.py::edge_estimado() (mtime-cache). Si un bucket
aprobado no tiene n suficiente hoy, simplemente no se escribe su clave
-- edge_estimado() cae al fallback conservador (0.15, mismo valor que el
ic_proxy fijo de antes), nunca sin protección.

Cron diario (ver crontab, franja de vigías 06:00-08:33 UTC).
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_bot_wallets_gate_bucket_25ago import cargar_filas  # noqa: E402
from bot_wallets_gate_bucket import BUCKETS_APROBADOS_REAL, _bucket  # noqa: E402

OUT = REPO / "data" / "shadow" / "bot_wallets_edge_medido_real.json"
N_MIN = 15  # mismo mínimo que el resto de gates del proyecto


def main() -> int:
    grupos = cargar_filas()
    resultado = {}
    reporte = []
    for (arquetipo, activo, marco), buckets in BUCKETS_APROBADOS_REAL.items():
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
