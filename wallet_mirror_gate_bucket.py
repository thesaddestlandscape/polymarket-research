"""
wallet_mirror_gate_bucket.py — consumidor del gate por micro-bucket de
precio real de Wallet Mirror (P24), mismo patrón que gate_bucket_propio.py
pero para data/shadow/wallet_mirror_gate_bucket.json (generado por
analisis_wallet_mirror_gate_bucket_10ago.py).

Solo lectura: expone evaluar() para consultar el veredicto de una tupla
WALLET_MIRROR#tipo#activo#marco#grande sin volver a calcular nada.

24-Ago (docstring desactualizada corregida): WALLET_MIRROR SÍ está en
pares_permitidos_live desde el 10/11/12-Ago (6 tuplas BTC#5/15/60min) y
wallet_mirror_executor_dryrun.py SÍ llama a evaluar() en el camino real
de ejecución (fail-closed, exige bueno_confirmado) -- este módulo dejó
de ser "infraestructura preparada" hace semanas, es veto activo sobre
dinero real.
"""
import json
import math
from pathlib import Path

_REPO = Path(__file__).resolve().parent
DATA_PATH = _REPO / "data/shadow/wallet_mirror_gate_bucket.json"
# 24-Ago (petición explícita Javi, mismo mecanismo que gate_bucket_propio.py
# desde el 05-Ago: "asegúrate que el mecanismo autoaprendiente tenga un
# backup que lo proteja siempre"): este gate no tenía NINGÚN cortacircuitos
# de emergencia -- WALLET_MIRROR pasó a mover dinero real el 10/11/12-Ago
# sin que nadie añadiera esta pieza. Fichero propio (no comparte namespace
# con gate_bucket_propio_override.json -- el formato de clave es distinto,
# tipo#activo#marco#grande#bucket, no strategy#activo#marco#decision#bucket).
OVERRIDE_PATH = _REPO / "data/live/wallet_mirror_gate_bucket_override.json"
# 25-Ago: ventana deslizante (mismo mecanismo que gate_bucket_propio.py::
# _zonas_finas(), analisis_wallet_mirror_gate_bucket_fino_25ago.py) --
# fuente ADITIVA, solo promueve sin_concluir->bueno_confirmado, nunca pisa
# un veredicto ya confirmado por el grid fijo de arriba.
DATA_PATH_FINO = _REPO / "data/shadow/wallet_mirror_gate_bucket_fino.json"
STEP = 0.05
_CONFLUENCIA_N_MIN = 15  # 01-Sep: piso absoluto CLAUDE.md ("ninguna conclusión
# con n<15"), mismo valor que _FILLABLE_N_MIN en gate_bucket_propio.py --
# reusado aquí para la confluencia suave de abajo, ver su comentario.

_cache = {"mtime": None, "data": {}}
_cache_override = {"mtime": None, "data": {}}
_cache_fino = {"mtime": None, "data": {}}


def _zonas_finas() -> dict:
    """{clave_str: {"lo":, "hi":, "veredicto":, ...}} desde
    wallet_mirror_gate_bucket_fino.json. Fail-open a {} si el fichero
    falta o está corrupto -- nunca bloquea el arranque por un fichero de
    refuerzo, mismo criterio que el resto de fuentes de este módulo."""
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
    """Mismo patrón exacto que gate_bucket_propio.py::_cargar_override() --
    SIEMPRE gana sobre cualquier otro veredicto, incluido bueno_confirmado.
    Un fichero corrupto/inaccesible se trata como override vacío (no
    bloquea nada por error de lectura)."""
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
    gate_bucket_propio.py::bucket() (24-Ago, /code-review): cualquier
    vigía externo que necesite reconstruir la MISMA clave exacta debe
    importar esto, no reimplementar la fórmula a mano."""
    return round(math.floor(ask / STEP + 1e-9) * STEP, 4)


def clave(tipo: str, activo: str, marco: str, jugada_grande: bool) -> str:
    """Única fuente de verdad del formato de clave (sin el sufijo de
    bucket) -- mismo motivo que bucket()."""
    return f"{tipo}#{activo}#{marco}#{'1' if jugada_grande else '0'}"


def evaluar(tipo: str, activo: str, marco: str, ask: float, jugada_grande: bool) -> dict:
    """{"veredicto": "malo_confirmado"|"bueno_confirmado"|"sin_concluir",
    "detalle": {...}|None}.

    Cortacircuitos de emergencia -- SIEMPRE se comprueba primero, gana
    sobre cualquier otro veredicto (incluido bueno_confirmado propio)."""
    clave_str = clave(tipo, activo, marco, jugada_grande)
    b_str = f"{bucket(ask):.2f}"
    override = _cargar_override()
    ov = override.get(f"{clave_str}#{b_str}") or override.get(clave_str)
    if ov is not None:
        return {
            "veredicto": "malo_confirmado",
            "detalle": {"origen": "override_emergencia", "motivo": ov.get("motivo", "sin motivo registrado"),
                        "desde": ov.get("desde")},
        }
    return evaluar_sin_override(tipo, activo, marco, ask, jugada_grande)


def evaluar_sin_override(tipo: str, activo: str, marco: str, ask: float, jugada_grande: bool) -> dict:
    """MISMA lógica que evaluar() pero SIN consultar el override de
    emergencia -- exclusivamente para el vigía de reapertura (24-Ago,
    /code-review, mismo hallazgo real que en gate_bucket_propio.py: con
    el override todavía escrito, evaluar() SIEMPRE devuelve
    malo_confirmado, sea cual sea el estado real de la tabla -- la
    condición de reapertura nunca se cumpliría)."""
    clave_str = clave(tipo, activo, marco, jugada_grande)
    b_str = f"{bucket(ask):.2f}"
    tabla = _cargar().get(clave_str, {})
    detalle = tabla.get(b_str)
    veredicto_propio = detalle.get("veredicto", "sin_concluir") if detalle else "sin_concluir"

    # 25-Ago: ventana deslizante como fuente ADITIVA de promoción -- solo
    # cuando el grid fijo sigue sin_concluir, nunca pisa un veredicto ya
    # confirmado (mismo orden que gate_bucket_propio.py::
    # evaluar_sin_override()).
    if veredicto_propio == "sin_concluir":
        fina = _zonas_finas().get(clave_str)
        if fina and fina.get("veredicto") == "bueno_confirmado":
            lo, hi = fina.get("lo"), fina.get("hi")
            if lo is not None and hi is not None and lo <= ask < hi:
                # 01-Sep: confluencia suave, mismo patrón y misma razón que
                # gate_bucket_propio.py::_evaluar_sin_override_ni_veto()
                # (ver ese commit para el caso fundacional completo) -- el
                # fino puede seguir promocionando en solitario cuando el
                # grid está sin_concluir, pero NO si el propio grid, en
                # ESTE bucket exacto (el que contiene `ask`, dentro de la
                # ventana que el fino confirma), ya apunta en contra
                # (pnl_medio negativo con n suficiente). Verificado con
                # SEGUIR#BTC#15min#0 (fino confirma [0.11,0.16)): la parte
                # de la ventana que cae en el bucket 0.15 del grid
                # (malo_confirmado) ya queda protegida SIN este fix -- ese
                # bucket nunca llega a "sin_concluir" en primer lugar, así
                # que la rama de promoción del fino ni se evalúa ahí. Este
                # fix cubre el caso distinto: un bucket de grid sin_concluir
                # (no malo_confirmado) pero con pnl_medio ya negativo --
                # evidencia de que discrepa, aunque no haya llegado a
                # confirmarse como malo todavía. Exige n>=_CONFLUENCIA_N_MIN
                # para que el pnl del grid cuente como evidencia real
                # (mismo bug que /code-review cazó en gate_bucket_propio.py:
                # sin este guardián, un bucket de grid con n=1-3 podría
                # vetar una confirmación robusta).
                n_grid = (detalle or {}).get("n") or 0
                pnl_grid = (detalle or {}).get("pnl_medio")
                if pnl_grid is not None and n_grid >= _CONFLUENCIA_N_MIN and pnl_grid < 0:
                    return {
                        "veredicto": "sin_concluir",
                        "detalle": {
                            "origen": "confluencia_suave_01sep",
                            "motivo": f"fino confirma [{lo:.2f},{hi:.2f}) pero el grid en "
                                      f"{b_str} (n={n_grid}) ya apunta en contra "
                                      f"(pnl_medio={pnl_grid:.3f}) -- no se promociona sin "
                                      "corroboración",
                            "detalle_propio": detalle,
                            "detalle_fino": fina,
                        },
                    }
                return {
                    "veredicto": "bueno_confirmado",
                    "detalle": {
                        "origen": "ventana_deslizante_25ago",
                        "motivo": f"ask en [{lo:.2f},{hi:.2f}), ventana fina "
                                  f"(n={fina.get('n')}, p={fina.get('p_valor')}) "
                                  "mientras el grid fijo sigue sin_concluir "
                                  "(confluencia suave: grid no contradice)",
                        "detalle_propio": detalle,
                    },
                }

    if detalle is not None:
        return {"veredicto": veredicto_propio, "detalle": detalle}
    return {"veredicto": "sin_concluir", "detalle": None}


def evaluar_para_recheck(subtype: str, direction: str, py: float, contexto: dict) -> dict:
    """Firma uniforme que live_trade.py::_ejecutar_orden_polymarket usa en
    el re-chequeo post-requote (25-Ago, ver idea_wallet_mirror_recheck_
    postrequote_fuente_equivocada_25ago) -- ANTES ese recheck consultaba
    siempre gate_bucket_propio.py (zonas de ballenas, sin jugada_grande),
    nunca este módulo. `py` llega en perspectiva YES (misma convención que
    gate_bucket_propio.json); WALLET_MIRROR opera SIEMPRE tipo SEGUIR
    (mirror_lado = lado_wallet, ver wallet_mirror_executor_dryrun.py), y
    `jugada_grande` debe venir en contexto (el executor lo calcula ya para
    su propio chequeo upstream -- si falta, fail-closed a False, nunca
    asumir "grande")."""
    partes = subtype.split("#")
    if len(partes) != 2:
        return {"veredicto": "sin_concluir", "detalle": {"origen": "subtype_invalido"}}
    activo, marco = partes
    ask = py if direction == "BUY_YES" else round(1.0 - py, 6)
    jugada_grande = bool(contexto.get("jugada_grande", False))
    return evaluar("SEGUIR", activo, marco, ask, jugada_grande)
