"""
kelly_precio_gate.py — consumidor del gate de corrección de Kelly por
precio de entrada (ver analisis_kelly_precio_gate_29jul.py para la
metodología: Wilson+shuffle+split-half+BH-FDR sobre results.csv,
agrupado por familia de arquetipo x bucket de precio 0.10).

Mismo patrón fail-open que gate_bucket_propio.py: si el fichero no existe,
la familia no tiene datos, o el bucket no está "confirmado", devuelve
factor=1.0 (no-op) -- nunca inventa una corrección sin evidencia.

Petición Javi 29-Jul: atacar primero GBM_LATE_15M#0.30-0.40 (infra-
dimensionada 1.1x-2.3x, n=1837-7234, el bucket con más evidencia de todo
el barrido). live_stake.py::_kelly_precio_factor() es el único caller.
"""
import json
import math
from pathlib import Path

DATA_PATH = Path("data/shadow/kelly_precio_gate.json")
# 25-Ago: fuente ADICIONAL para familias que no pasan por results.csv
# (mismo motivo que WALLET_MIRROR necesita joins propios en otros sitios
# del proyecto) -- generada por analisis_kelly_precio_resolution_sniper_
# naive_25ago.py, que YA filtra a solo entradas confirmado+pnl_medio>0
# (petición explícita Javi: "solo los micro-buckets y micro-buckets finos
# que tienen edge y pnl positivo confirmado"). Nunca pisa datos de
# DATA_PATH -- solo se consulta cuando la familia no aparece ahí, mismo
# patrón aditivo que zonas_validadas_externas.json en gate_bucket_propio.py.
DATA_PATH_EXTRA = Path("data/shadow/kelly_precio_resolution_sniper_naive.json")
STEP = 0.10

_cache = {"mtime": None, "data": {}}
_cache_extra = {"mtime": None, "data": {}}


def _familia(strategy: str) -> str:
    """Única fuente de verdad del agrupamiento por arquetipo (29-Jul:
    extraída aquí, antes duplicada también en
    analisis_kelly_precio_gate_29jul.py -- ese script ahora importa esta
    función en vez de tener su propia copia, para que el gate que se
    genera y el que se consume en live_stake.py nunca puedan divergir).
    Agrupa subfamilias del mismo arquetipo (ej. GBM_LATE_15M_TARDIO,
    _ESPACIO_ATR, _PYCONFIRMADO cuentan como GBM_LATE_15M) -- el patrón de
    precio es del ARQUETIPO, no de la variante exacta, y agrupar da más n
    por bucket sin mezclar arquetipos distintos (A vs B, ver
    project_dos_patrones_edge_bandera_21jul)."""
    if strategy.startswith("GBM_LATE"):
        return "GBM_LATE_15M_FAMILIA"
    if strategy.startswith("FAVORITO_CONFIRMADO"):
        return "FAVORITO_CONFIRMADO_FAMILIA"
    if strategy.startswith("BALLENAS"):
        return "BALLENAS_FAMILIA"
    if strategy.startswith("UPDOWN_GBM"):
        return "UPDOWN_GBM_FAMILIA"
    return strategy


def _cargar() -> dict:
    try:
        mtime = DATA_PATH.stat().st_mtime
    except OSError:
        return {}
    if _cache["mtime"] != mtime:
        try:
            _cache["data"] = json.loads(DATA_PATH.read_text(encoding="utf-8"))
            _cache["mtime"] = mtime
        except Exception:
            pass
    return _cache["data"]


def _cargar_extra() -> dict:
    try:
        mtime = DATA_PATH_EXTRA.stat().st_mtime
    except OSError:
        return {}
    if _cache_extra["mtime"] != mtime:
        try:
            _cache_extra["data"] = json.loads(DATA_PATH_EXTRA.read_text(encoding="utf-8"))
            _cache_extra["mtime"] = mtime
        except Exception:
            pass
    return _cache_extra["data"]


def _evaluar_extra(familia: str, precio_decision: float, subtype: str) -> dict | None:
    """Consulta DATA_PATH_EXTRA -- primero el bucket fijo (misma
    granularidad STEP=0.10 que el gate principal), y si no hay entrada
    ahí, las ventanas finas (paso 0.01, ancho 0.05, cada una ya viene
    filtrada a confirmado+pnl_medio>0 por el generador). Ambas fuentes
    solo contienen entradas ya confirmadas y positivas -- no hace falta
    re-chequear veredicto aquí, a diferencia de _cargar()."""
    datos = _cargar_extra()

    tabla = datos.get("familias", {}).get(familia, {}).get(subtype)
    if tabla:
        b = round(math.floor(precio_decision / STEP + 1e-9) * STEP, 4)
        entrada = tabla.get(f"{b:.2f}")
        if entrada is not None:
            return {
                "veredicto": "confirmado",
                "ratio_correccion": entrada.get("ratio_correccion"),
                "bucket": f"{b:.2f}", "familia": familia, "subtype": subtype,
                "n": entrada.get("n"), "fuente": "extra_grid",
            }

    ventanas = datos.get("ventanas_finas", {}).get(familia, {}).get(subtype)
    if ventanas:
        for v in ventanas:
            if v["lo"] <= precio_decision < v["hi"] and v.get("ratio_correccion") is not None:
                return {
                    "veredicto": "confirmado",
                    "ratio_correccion": v["ratio_correccion"],
                    "bucket": f"[{v['lo']:.2f},{v['hi']:.2f})", "familia": familia,
                    "subtype": subtype, "n": v.get("n"), "fuente": "extra_fino",
                }
    return None


def evaluar(strategy: str, precio_decision: float, subtype: str | None = None) -> dict | None:
    """precio_decision = precio en la perspectiva de la DECISIÓN (ya
    flipado a 1-precio_yes si es BUY_NO -- el caller es responsable de
    resolver esto, igual que gate_bucket_propio.evaluar()).

    29-Jul (petición Javi, "desagregar por moneda y marco es la clave"):
    el gate ahora está indexado por (familia, activo#marco, bucket), no
    solo (familia, bucket) -- un bucket confirmado en ETH#15min ya NO se
    aplica a SOL#15min o XRP#15min de la misma familia sin evidencia
    propia. `subtype` es obligatorio en la práctica (sin él, fail-open
    igual que sin evidencia) -- se deja opcional solo por compatibilidad
    de firma, todo caller real de este proyecto pasa subtype.

    Devuelve None si no hay evidencia (fail-open, factor=1.0 para el
    caller), o {"veredicto", "ratio_correccion", "bucket", "familia", "n"}
    si el bucket está en el gate (confirmado o no)."""
    familia = _familia(strategy)
    if not subtype:
        return None
    familias = _cargar().get("familias", {})
    por_subtype = familias.get(familia)
    tabla = por_subtype.get(subtype) if por_subtype else None
    if not tabla:
        return _evaluar_extra(familia, precio_decision, subtype)
    # 06-Ago fix: +1e-9 evita que un precio EXACTO en un múltiplo de STEP
    # (ej. 0.70) caiga en el bucket inferior por precisión de coma flotante
    # -- ver idea_bug_bucketing_float_precision_micro_buckets_06ago (mismo
    # bug en gate_bucket_propio.py, 5.08% de las filas afectadas).
    b = round(math.floor(precio_decision / STEP + 1e-9) * STEP, 4)
    entrada = tabla.get(f"{b:.2f}")
    if entrada is None:
        return _evaluar_extra(familia, precio_decision, subtype)
    return {
        "veredicto": entrada.get("veredicto", "sin_concluir"),
        "ratio_correccion": entrada.get("ratio_correccion"),
        "bucket": f"{b:.2f}",
        "familia": familia,
        "subtype": subtype,
        "n": entrada.get("n"),
    }
