"""
resolution_sniper_naive_gate_bucket.py — consumidor del gate por
micro-bucket de precio de RESOLUTION_SNIPER_NAIVE (P34 FASE 2), mismo
patrón exacto que wallet_mirror_gate_bucket.py/gate_bucket_propio.py:
solo lectura, expone evaluar()/evaluar_sin_override() para consultar el
veredicto de una tupla sin volver a calcular nada.

25-Ago, construcción inicial (Javi: "adelante, constrúyelo"). A esta fecha
RESOLUTION_SNIPER_NAIVE no tiene NINGÚN trade real en trades.csv (sigue en
FASE 1 dry-run) -- data/shadow/resolution_sniper_naive_gate_bucket.json
(el dato PROPIO, generado por un script análogo a
analisis_wallet_mirror_gate_bucket_10ago.py que todavía no existe -- se
construye la primera vez que haya trades reales que analizar) no existe
todavía, así que evaluar() cae siempre a la validación EXTERNA de abajo
mientras tanto -- mismo patrón que gate_bucket_propio.py::
_zonas_validadas_externamente() (promueve sin_concluir -> bueno_confirmado,
NUNCA pisa un malo_confirmado propio si en el futuro aparece uno).

Clave: "{activo}#{marco}#{direccion}" (direccion = "Up"/"Down", el mismo
vocabulario que resolution_sniper_fade_depth_fase0.py::observar_ventana ya
usa como direccion_impl -- NO "BUY_YES"/"BUY_NO", para no forzar una
conversión en el punto de llamada donde direccion_impl es lo que ya hay a
mano).
"""
import json
import math
from pathlib import Path

_REPO = Path(__file__).resolve().parent
DATA_PATH = _REPO / "data/shadow/resolution_sniper_naive_gate_bucket.json"
# Cortacircuitos de emergencia -- mismo mecanismo y mismo motivo que
# gate_bucket_propio.py/wallet_mirror_gate_bucket.py (petición explícita
# Javi 05-Ago/24-Ago: "asegúrate que el mecanismo autoaprendiente tenga un
# backup que lo proteja siempre"). SIEMPRE gana sobre cualquier otro
# veredicto, incluido bueno_confirmado -- construido desde el día 1, antes
# de que exista ningún trade real, para no repetir el hueco real que tuvo
# WALLET_MIRROR (vivió semanas en live sin ninguno).
OVERRIDE_PATH = _REPO / "data/live/resolution_sniper_naive_gate_bucket_override.json"
STEP = 0.05

# Validación EXTERNA (mismo patrón que gate_bucket_propio.py::
# _ZONAS_VALIDADAS_EXTERNAMENTE_ESTATICAS) -- sella lo que YA se confirmó
# con rigor completo el 19-Ago (analisis_gate_riguroso_resolution_sniper_
# naive_depth_19ago.py, n=472, ask∈[0.05,0.95] real tras offset 0-3s
# post-cierre, CON profundidad verificada ratio>=5x): 6/6 combos GATE OK
# en 5min -- BTC/ETH/SOL/XRP/DOGE/BNB, pnl/tr +0.51€ a +0.96€, wilson90lo
# por encima del ask medio, p_shuffle 0.0000-0.0025, split-half consistente.
# El mecanismo apuesta CON la dirección implícita sea Up o Down (la muestra
# ya mezcla ambas por construcción) -- se sella el rango completo
# [0.05,0.95) para las dos direcciones de cada uno de los 6 activos.
#
# 15min NO se sella aquí -- el gate de dirección (9/12 combos, ver
# resolution_sniper_naive_depth_fase0.py) nunca se cruzó CON profundidad
# verificada por activo (n hoy: BTC=37, ETH=29, SOL=28, XRP=28, DOGE=28,
# BNB=12, ninguno >=40), y el desglose exacto de cuáles de los 9/12 son
# 15min no está documentado por activo -- sellar aquí sería asumir, no
# confirmar (CLAUDE.md pt.17: nunca agregado). Queda sin_concluir hasta que
# una sesión futura repita el gate riguroso específico de 15min por activo.
_ACTIVOS_5MIN_CONFIRMADOS = ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")
_ZONAS_VALIDADAS_EXTERNAMENTE_ESTATICAS = {
    f"{activo}#5min#{direccion}": [(0.05, 0.95)]
    for activo in _ACTIVOS_5MIN_CONFIRMADOS
    for direccion in ("Up", "Down")
}

_cache = {"mtime": None, "data": {}}
_cache_override = {"mtime": None, "data": {}}


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


def _cargar_override() -> dict:
    """Mismo patrón exacto que gate_bucket_propio.py::_cargar_override() --
    SIEMPRE gana sobre cualquier otro veredicto, incluido bueno_confirmado.
    Un fichero corrupto/inaccesible se trata como override vacío (no
    bloquea nada por error de lectura, fail-open a la lógica normal)."""
    try:
        mtime = OVERRIDE_PATH.stat().st_mtime
    except OSError:
        return {}
    if _cache_override["mtime"] != mtime:
        try:
            _cache_override["data"] = json.loads(OVERRIDE_PATH.read_text(encoding="utf-8"))
            _cache_override["mtime"] = mtime
        except Exception:
            pass
    return _cache_override["data"]


def bucket(ask: float) -> float:
    """Único punto de verdad del bucketing (STEP=0.05, mismo fix +1e-9 que
    gate_bucket_propio.py::bucket() -- un ask exacto en un múltiplo de STEP
    puede caer en el bucket inferior por precisión de coma flotante sin
    el margen)."""
    return round(math.floor(ask / STEP + 1e-9) * STEP, 4)


def clave(activo: str, marco: str, direccion: str) -> str:
    """Única fuente de verdad del formato de clave (sin el sufijo de
    bucket) -- reutilizar, no reimplementar a mano."""
    return f"{activo}#{marco}#{direccion}"


def evaluar(activo: str, marco: str, direccion: str, ask: float) -> dict:
    """{"veredicto": "malo_confirmado"|"bueno_confirmado"|"sin_concluir",
    "detalle": {...}|None}. No decide permitido/vetado -- eso lo hace el
    caller (fail-closed: exige bueno_confirmado antes de operar dinero
    real).

    Cortacircuitos de emergencia -- SIEMPRE se comprueba primero, gana
    sobre cualquier otro veredicto (incluido bueno_confirmado propio)."""
    clave_str = clave(activo, marco, direccion)
    b_str = f"{bucket(ask):.2f}"
    override = _cargar_override()
    ov = override.get(f"{clave_str}#{b_str}") or override.get(clave_str)
    if ov is not None:
        return {
            "veredicto": "malo_confirmado",
            "detalle": {"origen": "override_emergencia", "motivo": ov.get("motivo", "sin motivo registrado"),
                        "desde": ov.get("desde")},
        }
    return evaluar_sin_override(activo, marco, direccion, ask)


def evaluar_sin_override(activo: str, marco: str, direccion: str, ask: float) -> dict:
    """MISMA lógica que evaluar() pero SIN consultar el override de
    emergencia -- exclusivamente para un futuro vigía de reapertura (mismo
    motivo que gate_bucket_propio.py/wallet_mirror_gate_bucket.py: con el
    override todavía escrito, evaluar() SIEMPRE devuelve malo_confirmado,
    haciendo que la condición de reapertura nunca se cumpla)."""
    clave_str = clave(activo, marco, direccion)
    b_str = f"{bucket(ask):.2f}"
    tabla = _cargar().get(clave_str, {})
    detalle = tabla.get(b_str)
    veredicto_propio = detalle.get("veredicto", "sin_concluir") if detalle else "sin_concluir"

    # Validación externa -- solo PROMUEVE sin_concluir -> bueno_confirmado,
    # nunca pisa un veredicto propio ya confirmado (mismo orden que
    # gate_bucket_propio.py::evaluar_sin_override()).
    if veredicto_propio == "sin_concluir":
        for lo, hi in _ZONAS_VALIDADAS_EXTERNAMENTE_ESTATICAS.get(clave_str, []):
            if lo <= ask < hi:
                return {
                    "veredicto": "bueno_confirmado",
                    "detalle": {
                        "origen": "validacion_externa_19ago",
                        "motivo": f"ask en [{lo:.2f},{hi:.2f}), gate riguroso completo con profundidad "
                                  "verificada (n=472, analisis_gate_riguroso_resolution_sniper_naive_depth_19ago.py) "
                                  "mientras el dato propio (trades reales) madura",
                        "detalle_propio": detalle,
                    },
                }

    if detalle is not None:
        return {"veredicto": veredicto_propio, "detalle": detalle}
    return {"veredicto": "sin_concluir", "detalle": None}


def evaluar_para_recheck(subtype: str, direction: str, py: float, contexto: dict) -> dict:
    """Firma uniforme que live_trade.py::_ejecutar_orden_polymarket usa en
    el re-chequeo post-requote -- mismo mecanismo añadido 25-Ago para
    WALLET_MIRROR (ver wallet_mirror_gate_bucket.py::evaluar_para_recheck),
    aplicado aquí desde el diseño inicial en vez de tener que arreglarlo
    después. `py` llega en perspectiva YES; `contexto` no se usa (esta
    familia no tiene un equivalente a jugada_grande), solo está en la
    firma para mantenerla uniforme con el resto del registro."""
    partes = subtype.split("#")
    if len(partes) != 2:
        return {"veredicto": "sin_concluir", "detalle": {"origen": "subtype_invalido"}}
    activo, marco = partes
    direccion_impl = "Up" if direction == "BUY_YES" else "Down"
    ask = py if direction == "BUY_YES" else round(1.0 - py, 6)
    return evaluar(activo, marco, direccion_impl, ask)
