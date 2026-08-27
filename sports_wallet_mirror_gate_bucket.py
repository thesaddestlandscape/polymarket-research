"""
sports_wallet_mirror_gate_bucket.py — consumidor del gate por micro-bucket
de precio real de Sports Wallet Mirror, mismo patrón EXACTO que
wallet_mirror_gate_bucket.py (P24, cripto) pero sin la dimensión
`jugada_grande` (sports no la tiene todavía) y sobre
data/sports/wallet_mirror_gate_bucket.json / _fino.json (generados por
analisis_sports_wallet_mirror_gate_bucket_26ago.py /
analisis_sports_wallet_mirror_gate_bucket_fino.py).

27-Ago noche (petición explícita Javi: "construye lo que falte de sports
para tenerlo ya hecho cuando toque operar en directo"): hasta ahora
`sports_wallet_mirror_sniper.py` solo comprobaba la whitelist estática
(`pares_permitidos_live`, categoria#tipo#lo:hi editada a mano por Javi) --
sin este módulo, un bucket que Javi aprobó una vez y que luego empieza a
sangrar dinero real seguiría operando hasta que alguien lo notara y
editara el JSON a mano. Este módulo añade el SEGUNDO guardián (mismo
patrón que WALLET_MIRROR cripto: whitelist estática + gate vivo,
independientes) -- `evaluar()` se consulta en el camino real de decisión,
y el kill switch (`vigia_sports_micro_bucket_kill_switch_wallet_mirror.py`)
puede vetar un bucket automáticamente sin tocar `pares_permitidos_live`.

Solo lectura: expone evaluar() para consultar el veredicto de una tupla
CATEGORIA#TIPO sin volver a calcular nada.
"""
import json
import math
from pathlib import Path

_REPO = Path(__file__).resolve().parent
DATA_PATH = _REPO / "data/sports/wallet_mirror_gate_bucket.json"
DATA_PATH_FINO = _REPO / "data/sports/wallet_mirror_gate_bucket_fino.json"
OVERRIDE_PATH = _REPO / "data/sports/wallet_mirror_gate_bucket_override.json"
STEP = 0.05

_cache = {"mtime": None, "data": {}}
_cache_override = {"mtime": None, "data": {}}
_cache_fino = {"mtime": None, "data": {}}


def _zonas_finas() -> dict:
    """{clave_str: {"lo":, "hi":, "veredicto":, ...}} desde
    wallet_mirror_gate_bucket_fino.json. Fail-open a {} si el fichero
    falta o está corrupto -- nunca bloquea el arranque por un fichero de
    refuerzo."""
    try:
        mtime = DATA_PATH_FINO.stat().st_mtime
    except OSError:
        return {}
    if _cache_fino["mtime"] != mtime:
        try:
            _cache_fino["data"] = json.loads(DATA_PATH_FINO.read_text(encoding="utf-8"))
            _cache_fino["mtime"] = mtime
        except Exception:
            pass
    return _cache_fino["data"]


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
    """Mismo patrón que wallet_mirror_gate_bucket.py::_cargar_override() --
    SIEMPRE gana sobre cualquier otro veredicto, incluido bueno_confirmado.
    Fichero corrupto/inaccesible se trata como override vacío."""
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
    """Único punto de verdad del bucketing (STEP=0.05) -- mismo motivo que
    gate_bucket_propio.py::bucket()/wallet_mirror_gate_bucket.py::bucket():
    cualquier vigía externo que necesite reconstruir la MISMA clave exacta
    debe importar esto, no reimplementar la fórmula a mano."""
    return round(math.floor(ask / STEP + 1e-9) * STEP, 4)


def clave(categoria: str, tipo: str) -> str:
    """Única fuente de verdad del formato de clave (sin el sufijo de
    bucket)."""
    return f"{categoria}#{tipo}"


def evaluar(categoria: str, tipo: str, ask: float) -> dict:
    """{"veredicto": "malo_confirmado"|"bueno_confirmado"|"sin_concluir",
    "detalle": {...}|None}.

    Cortacircuitos de emergencia -- SIEMPRE se comprueba primero, gana
    sobre cualquier otro veredicto (incluido bueno_confirmado propio)."""
    clave_str = clave(categoria, tipo)
    b_str = f"{bucket(ask):.2f}"
    override = _cargar_override()
    ov = override.get(f"{clave_str}#{b_str}") or override.get(clave_str)
    if ov is not None:
        return {
            "veredicto": "malo_confirmado",
            "detalle": {"origen": "override_emergencia", "motivo": ov.get("motivo", "sin motivo registrado"),
                        "desde": ov.get("desde")},
        }
    return evaluar_sin_override(categoria, tipo, ask)


def evaluar_sin_override(categoria: str, tipo: str, ask: float) -> dict:
    """MISMA lógica que evaluar() pero SIN consultar el override de
    emergencia -- exclusivamente para el vigía de reapertura (mismo motivo
    que wallet_mirror_gate_bucket.py: con el override todavía escrito,
    evaluar() SIEMPRE devuelve malo_confirmado, la condición de reapertura
    nunca se cumpliría)."""
    clave_str = clave(categoria, tipo)
    b_str = f"{bucket(ask):.2f}"
    tabla = _cargar().get(clave_str, {})
    detalle = tabla.get(b_str)
    veredicto_propio = detalle.get("veredicto", "sin_concluir") if detalle else "sin_concluir"

    # Ventana deslizante como fuente ADITIVA de promoción -- solo cuando el
    # grid fijo sigue sin_concluir, nunca pisa un veredicto ya decidido por
    # el grid fijo.
    if veredicto_propio == "sin_concluir":
        fino = _zonas_finas().get(clave_str)
        if fino and fino.get("lo", 0) <= ask < fino.get("hi", 0) and fino.get("veredicto") == "bueno_confirmado":
            return {"veredicto": "bueno_confirmado", "detalle": {**fino, "origen": "ventana_fina"}}

    return {"veredicto": veredicto_propio, "detalle": {**detalle, "origen": "grid_fijo"} if detalle else None}
