#!/usr/bin/env python3
"""
resolution_sniper_precierre_gate.py — gate VIVO de micro-bucket para
RESOLUTION_SNIPER_PRECIERRE, mismo patrón exacto que gate_bucket_propio.py/
wallet_mirror_gate_bucket.py: `evaluar()` relee el JSON del disco (con
caché por mtime, nunca hardcodea una zona) y exige CONVERGENCIA grid+fino
antes de dar luz verde.

Origen (02-Sep, corrección explícita de Javi tras revisar el diseño del
script de prueba de ejecutabilidad): "los micro-buckets propios y el
micro-bucket fino se actualizan constantemente y el sistema los
reconfirma antes de lanzar un trade" -- el primer borrador del test
hardcodeaba BTC#[0.47,0.52) como constantes fijas, exactamente el
antipatrón que el resto del proyecto ya prohibió (F5 en
project_lecciones_aprendidas_estrategias: "NUNCA crear tabla de zonas
hardcodeada, generalizar el mecanismo ya existente"). Un bucket bueno
hoy puede revertir mañana si n crece con signo contrario, o un bucket
nuevo (BNB/DOGE/SOL/XRP, hoy con n<40) puede confirmar en cualquier
momento -- una constante fija en el código no se entera de ninguno de
los dos casos.

Fuente: data/shadow/resolution_sniper_precierre_gate_riguroso.json,
regenerado por analisis_gate_riguroso_resolution_sniper_precierre_02sep.py
(cron diario, ver vigias_frecuentes_fase0.py). MAX_ANTIGUEDAD_S: mismo
criterio de guardián de frescura que gate_bucket_propio.py/wallet_mirror_
gate_bucket.py (01-Sep) -- dato viejo se trata como sin datos, fail-closed.
"""
import json
import math
import time
from pathlib import Path

_REPO = Path(__file__).resolve().parent
DATA_PATH = _REPO / "data" / "shadow" / "resolution_sniper_precierre_gate_riguroso.json"
STEP = 0.05
MAX_ANTIGUEDAD_S = 30 * 3600  # cron diario + margen, mismo criterio que el resto del proyecto

_cache = {"mtime": None, "data": None}


def bucket(ask: float) -> str:
    return f"{round(math.floor(ask / STEP + 1e-9) * STEP, 2):.2f}"


def _cargar() -> dict | None:
    try:
        mtime = DATA_PATH.stat().st_mtime
    except OSError:
        return None
    if time.time() - mtime > MAX_ANTIGUEDAD_S:
        return None  # dato demasiado viejo -- fail-closed, tratar como sin datos
    if _cache["mtime"] != mtime:
        try:
            _cache["data"] = json.loads(DATA_PATH.read_text(encoding="utf-8"))
            _cache["mtime"] = mtime
        except Exception:
            return None
    return _cache["data"]


def evaluar(activo: str, ask: float, offset_s: int) -> dict:
    """{"confirmado": bool, "motivo": str, "grid": {...}|None, "fino": {...}|None}.

    Solo True si AMBOS (grid Y fino) dicen bueno_confirmado para este
    activo/precio EN ESE OFFSET -- misma regla de convergencia del 01-Sep
    aplicada al resto del proyecto. Fail-closed en cualquier ausencia de dato.

    `offset_s` es OBLIGATORIO desde el 03-Sep (petición explícita Javi tras
    el fallo de la prueba controlada): el edge de esta familia está medido
    por offset y NO se hereda entre offsets -- mover el instante de entrada
    cambia la distribución (a -8s el mercado es más incierto y el ask es
    otro), así que una zona confirmada a -1s no autoriza absolutamente nada
    a -5s. Si el JSON no trae evidencia de ESE offset exacto, se rechaza."""
    d = _cargar()
    if d is None:
        return {"confirmado": False, "motivo": "sin_datos_o_gate_viejo", "grid": None, "fino": None}

    # Formato v2 (por_offset). Un JSON en formato viejo (sin eje de offset)
    # se trata como SIN DATOS: sus veredictos mezclaban offsets y no se
    # puede saber a cuál corresponden -- fail-closed, nunca reinterpretar.
    bloque = (d.get("por_offset") or {}).get(str(int(offset_s)))
    if not bloque:
        return {"confirmado": False, "motivo": f"sin_datos_para_offset_{int(offset_s)}s",
                "grid": None, "fino": None}

    clave_grid = f"{activo}#{bucket(ask)}"
    grid = bloque.get("grid", {}).get(clave_grid)
    fino_activo = bloque.get("fino", {}).get(activo)
    fino = None
    if fino_activo and fino_activo.get("veredicto") == "bueno_confirmado":
        lo, hi = fino_activo.get("lo"), fino_activo.get("hi")
        if lo is not None and hi is not None and lo <= ask < hi:
            fino = fino_activo

    grid_ok = bool(grid and grid.get("veredicto") == "bueno_confirmado")
    fino_ok = bool(fino)

    if grid_ok and fino_ok:
        return {"confirmado": True, "motivo": "convergencia_grid_fino", "grid": grid, "fino": fino}
    if grid_ok and not fino_ok:
        return {"confirmado": False, "motivo": "grid_ok_fino_no_converge", "grid": grid, "fino": fino_activo}
    if fino_ok and not grid_ok:
        return {"confirmado": False, "motivo": "fino_ok_grid_no_converge", "grid": grid, "fino": fino}
    return {"confirmado": False, "motivo": "ninguno_confirma", "grid": grid, "fino": fino_activo}
