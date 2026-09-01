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
import time
from pathlib import Path

_REPO = Path(__file__).resolve().parent
DATA_PATH = _REPO / "data/sports/wallet_mirror_gate_bucket.json"
DATA_PATH_FINO = _REPO / "data/sports/wallet_mirror_gate_bucket_fino.json"
OVERRIDE_PATH = _REPO / "data/sports/wallet_mirror_gate_bucket_override.json"
STEP = 0.05

# 01-Sep: guardián de frescura + confluencia suave, mismo patrón aplicado
# esta misma noche a gate_bucket_propio.py y wallet_mirror_gate_bucket.py
# (cripto) -- petición explícita Javi ("no lo podemos permitir, tiene que
# hacerlo cada vez que se vaya a hacer un trade, sino corremos riesgo de
# perder pasta"). Sports tiene dinero real desde 31-Ago (WALLET_MIRROR#LoL,
# ver data/sports/trades.csv), mismo riesgo exacto que motivó el fix en
# cripto -- el grid/fino de sports (cron diario 07:05/07:07 UTC) no tenían
# ninguna de las dos protecciones hasta ahora. N_MIN_MIN local para el
# chequeo de confluencia (piso absoluto CLAUDE.md, mismo valor que
# _FILLABLE_N_MIN/_CONFLUENCIA_N_MIN de los módulos gemelos).
MAX_ANTIGUEDAD_S = 30 * 3600  # cron diario + margen, mismo criterio que gate_bucket_propio.py
_CONFLUENCIA_N_MIN = 15

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
    if time.time() - mtime > MAX_ANTIGUEDAD_S:
        return {}  # 01-Sep: dato demasiado viejo -- tratar como sin datos, fail-closed
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
    if time.time() - mtime > MAX_ANTIGUEDAD_S:
        return {}  # 01-Sep: mismo guardián de frescura
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


def techo_confirmado(categoria: str, tipo: str, ask: float, resultado_evaluar: dict) -> float | None:
    """Propuesta #3 Arquetipo A aplicada a sports (01-Sep, aprobación
    explícita Javi): techo de precio seguro para ensanchar el límite del
    FOK real -- mismo hallazgo que en cripto (`_techo_precio_fok` en
    live_trade.py), verificado aquí con `wallet_mirror_sniper_dry_run.csv`
    (mediana ratio_vs_stake_mirror=499,8x, incluso más liquidez agregada
    de sobra que en cripto), pero sports NO tiene un edge_dir/requote en
    unidades de precio como cripto -- en vez de derivar el margen del
    edge, se usa el límite superior de la ZONA EXACTA que `evaluar()` ya
    validó como `bueno_confirmado`, sea grid fijo o ventana fina. Nunca
    ensancha más allá de la zona ya confirmada rentable, sin necesitar
    traducir `edge_pp` (comportamental, wallet) a precio.

    `resultado_evaluar` es el dict YA devuelto por `evaluar()` para este
    mismo (categoria, tipo, ask) -- se reusa en vez de recalcular, y así
    el techo siempre corresponde EXACTAMENTE a la zona que produjo el
    veredicto que el caller ya comprobó. None si el veredicto no es
    bueno_confirmado (fail-closed: sin zona confirmada, no hay techo que
    ofrecer -- el caller no debería llegar aquí en ese caso de todas
    formas, dado que el gate ya bloquea antes)."""
    if resultado_evaluar.get("veredicto") != "bueno_confirmado":
        return None
    detalle = resultado_evaluar.get("detalle") or {}
    if detalle.get("origen") == "ventana_fina":
        # code-review 01-Sep (hallazgo real): sin este chequeo, un
        # `resultado_evaluar` desincronizado con el `ask` real (p.ej. de un
        # caller futuro que reusara un dict de una iteración anterior) daría
        # un techo de una zona equivocada sin ninguna señal de alarma --
        # exigir que `ask` caiga de verdad dentro de [lo,hi) antes de
        # confiar en `hi`, fail-closed si no.
        lo, hi = detalle.get("lo"), detalle.get("hi")
        if lo is None or hi is None or not (lo <= ask < hi):
            return None
        return float(hi)
    # grid_fijo (u override, aunque ese caso nunca es bueno_confirmado):
    # el bucket fijo de ancho STEP que contiene `ask`, mismo bucketing
    # que usa evaluar() para indexar la tabla.
    return round(bucket(ask) + STEP, 6)


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
    # /code-review 01-Sep (hallazgo real, tercera ronda): el generador de
    # sports (analisis_sports_wallet_mirror_gate_bucket_26ago.py) escribe
    # "n_insuficiente" para buckets con n<N_MIN, NO "sin_concluir" como el
    # gemelo de cripto -- la promoción del fino (línea de abajo) y la
    # confluencia suave comparan contra "sin_concluir" a secas, así que
    # "n_insuficiente" nunca entraba ahí: la promoción del fino llevaba
    # TODA su vida inerte en sports para cualquier bucket bajo n=40 (antes
    # n=15), no solo desde el fix de esta noche. Normalizado aquí en vez
    # de en el generador para no tocar el vocabulario que otros
    # consumidores (vigía, dashboard) puedan mostrar distinto.
    if veredicto_propio == "n_insuficiente":
        veredicto_propio = "sin_concluir"

    # Ventana deslizante como fuente ADITIVA de promoción -- solo cuando el
    # grid fijo sigue sin_concluir, nunca pisa un veredicto ya decidido por
    # el grid fijo.
    if veredicto_propio == "sin_concluir":
        fino = _zonas_finas().get(clave_str)
        lo_fino, hi_fino = (fino or {}).get("lo"), (fino or {}).get("hi")
        # /code-review 01-Sep (hallazgo real): defaults silenciosos a 0
        # (fino.get("lo",0)) en vez de exigir explícitamente que ambos
        # existan -- mismo fix ya aplicado al gemelo de cripto
        # (wallet_mirror_gate_bucket.py). Un JSON parcial (falta "lo",
        # sobra "hi" y bueno_confirmado) ensancharía la promoción a
        # [0, hi) en vez de fallar cerrado.
        if fino and lo_fino is not None and hi_fino is not None and lo_fino <= ask < hi_fino \
                and fino.get("veredicto") == "bueno_confirmado":
            # 01-Sep: confluencia suave, mismo patrón que gate_bucket_propio.py/
            # wallet_mirror_gate_bucket.py -- el fino puede promocionar en
            # solitario mientras el grid está sin_concluir, pero no si el
            # propio grid, en este bucket exacto, ya apunta en contra
            # (pnl_medio negativo con n>=_CONFLUENCIA_N_MIN).
            n_grid = (detalle or {}).get("n") or 0
            pnl_grid = (detalle or {}).get("pnl_medio")
            if pnl_grid is not None and n_grid >= _CONFLUENCIA_N_MIN and pnl_grid < 0:
                return {
                    "veredicto": "sin_concluir",
                    "detalle": {"origen": "confluencia_suave_01sep",
                                "motivo": f"fino confirma pero el grid en {b_str} (n={n_grid}) "
                                          f"ya apunta en contra (pnl_medio={pnl_grid:.3f})",
                                "detalle_propio": detalle, "detalle_fino": fino},
                }
            return {"veredicto": "bueno_confirmado", "detalle": {**fino, "origen": "ventana_fina"}}

    return {"veredicto": veredicto_propio, "detalle": {**detalle, "origen": "grid_fijo"} if detalle else None}
