"""
gate_bucket_propio.py — gate de entrada por micro-bucket de precio,
construido desde NUESTRO PROPIO histórico de PnL (results.csv), no desde
timing de ballenas. Petición explícita Javi 28-Jul, tras refutar
retrospectivamente que reusar el timing de ballenas para gatear
FAVORITO_CONFIRMADO/GBM_LATE_15M no transfiere (ver
ballenas_banda_fina_gate.py y project_gate_banda_fina_ballenas_28jul).

Datos: data/shadow/gate_bucket_propio.json, generado por
analisis_gate_bucket_propio_28jul.py (shuffle test + split-half
cronológico, n>=15 -- ver ese fichero para la metodología completa).
Solo los buckets "malo_confirmado"/"bueno_confirmado" tienen evidencia
suficiente; todo lo demás es "sin_concluir" y no se toca (fail-open).
"""
import json
from pathlib import Path

DATA_PATH = Path("data/shadow/gate_bucket_propio.json")
CONFIG_LIVE = Path("data/live/config_live.json")
STEP = 0.05

_cache = {"mtime": None, "data": {}}
_cache_cfg = {"mtime": None, "activo": False}

# 04-Ago: extensión validada con wallets EXPERTAS (sig_bhfdr=True en
# wallet_edge_score_por_activo_marco.json, no todo el ruido de ballenas) --
# dos colas simétricas donde el mercado ya está calibrado con la propia
# moneda (hit_expertas ~= precio, sin margen de edge real) Y nuestro pnl
# propio coincide en signo:
#   - py<0.20: BTC (n=14-22, aún sin confirmar solo con n propio), ETH
#     (n=11-20, [0.15,0.20) YA malo_confirmado con datos propios), SOL
#     (n=9-20, [0.20,0.25) YA malo_confirmado propio).
#   - py>=0.80: BTC (n=11,7,6, pnl=-0.060,-0.079,-0.562) y ETH (n=4,5,
#     pnl=-0.079,-0.167) -- misma firma que la cola baja, simétrica. SOL
#     SIN incluir aquí: n=1-2 en esa cola, evidencia insuficiente incluso
#     como corroboración.
# NO es lo mismo que el timing de ballenas ya refutado 28-Jul
# (ballenas_banda_fina_gate.py, ver docstring del módulo) -- esto usa
# calibración de PRECIO de wallets validadas, no minutos restantes, y NO
# se generalizó al resto del rango 0.20-0.80 donde la evidencia es más
# débil/mixta -- ver project_micro_bucket_gbmlate_ballenas_04ago.
# activo=false hasta /code-review + aprobación explícita de Javi.
_FAMILIAS_GBM_LATE = ("GBM_LATE_15M", "GBM_LATE_15M_TARDIO",
                      "GBM_LATE_15M_ESPACIO_ATR", "GBM_LATE_15M_PYCONFIRMADO")

_REGLAS_EXTENSION = (
    {"activos": ("BTC", "ETH", "SOL"), "py_min": 0.0, "py_max": 0.20},
    {"activos": ("BTC", "ETH"), "py_min": 0.80, "py_max": 1.01},
)

# 05-Ago: extensión que PROMUEVE a bueno_confirmado (no solo endurece a
# malo_confirmado como la extensión de arriba) para tuplas cuyo propio n
# en results.csv todavía es insuficiente para confirmar nada solas --
# petición explícita Javi: "las estrategias que estén en live tengan el
# filtro de micro-buckets para operar solo en la franja conocida que da
# dinero", usando SIEMPRE el mismo mecanismo único (este fichero), no
# tablas paralelas hardcodeadas en cada ejecutor (error corregido el
# mismo día, ver feedback_lookahead_bias_precio_final_no_es_edge_05ago).
#
# Validado con fuentes EXTERNAS (no resultscsv propio, insuficiente hoy):
#   - BALLENAS_TARDIAS#ETH#5min#BUY_YES: ballenas_timing_history.csv
#     (n=79859, individual por whale trade -- restante_min real 2.0-3.4min
#     sobre ventana de 5min, sin sesgo de convergencia T->0), gate
#     Wilson+shuffle+bootstrap+split-half con fee 7% real.
#   - FAVORITO_CONFIRMADO#BTC#60min#BUY_NO: cruzado con
#     franja_milimetrica_ballenas.json (ya validado, [0.55,0.60) en
#     BUY_YES = [0.40,0.45) en BUY_NO por simetría).
#   - FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min#BUY_YES:
#     coincide EXACTO con punto_confirmacion (Wilson 95% ya validado
#     21-Jul, independiente): precio~0.875.
# Ver idea_veto_microbucket_ballenas_eth5min_05ago /
# idea_veto_microbucket_favorito_confirmado_btc_05ago en memoria para el
# detalle completo, incluida la corrección de metodología del mismo día
# (look-ahead bias: NUNCA usar precio final del mercado, solo precio en
# el cruce real del umbral con tiempo restante significativo).
#
# Igual que _REGLAS_EXTENSION: NUNCA pisa un veredicto propio ya
# confirmado (malo_confirmado o bueno_confirmado) -- en cuanto
# results.csv acumule n>=15 propio en un bucket y el cron diario
# (vigia_gate_bucket_propio.py) lo confirme (en cualquier sentido), el
# dato propio manda siempre. Esto es solo el arranque -- autoaprendizaje
# real, no un parche permanente.
_ZONAS_VALIDADAS_EXTERNAMENTE = {
    "BALLENAS_TARDIAS#ETH#5min#BUY_YES": [(0.15, 0.20), (0.25, 0.30), (0.40, 0.45)],
    "FAVORITO_CONFIRMADO#BTC#60min#BUY_NO": [(0.40, 0.45)],
    "FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min#BUY_YES": [(0.85, 0.90)],
}


def _extension_activa() -> bool:
    try:
        mtime = CONFIG_LIVE.stat().st_mtime
    except OSError:
        return False
    if _cache_cfg["mtime"] != mtime:
        try:
            cfg = json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
            _cache_cfg["activo"] = bool(
                cfg.get("riesgo", {})
                .get("gate_bucket_extension_calibracion_ballenas", {})
                .get("activo", False)
            )
            _cache_cfg["mtime"] = mtime
        except Exception:
            _cache_cfg["activo"] = False
    return _cache_cfg["activo"]


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


def _regla_aplica(tupla_str: str, py: float):
    partes = tupla_str.split("#")
    if len(partes) != 4:
        return None
    familia, activo, marco, direccion = partes
    if familia not in _FAMILIAS_GBM_LATE or marco != "15min" or direccion != "BUY_YES":
        return None
    for regla in _REGLAS_EXTENSION:
        if activo in regla["activos"] and regla["py_min"] <= py < regla["py_max"]:
            return regla
    return None


def evaluar(tupla_str: str, py: float) -> dict:
    """{"veredicto": "malo_confirmado"|"bueno_confirmado"|"sin_concluir",
    "detalle": {...}|None}. No decide permitido/vetado -- eso lo hace el
    caller (fase 0: solo loguea; fase 1: veta si malo_confirmado)."""
    import math
    b = round(math.floor(py / STEP) * STEP, 4)
    tabla = _cargar().get(tupla_str, {})
    detalle = tabla.get(f"{b:.2f}")

    # La extensión solo puede ENDURECER un "sin_concluir" propio a
    # "malo_confirmado" -- nunca pisa un veredicto propio ya confirmado
    # (malo_confirmado/bueno_confirmado), ese sigue mandando siempre.
    veredicto_propio = detalle.get("veredicto", "sin_concluir") if detalle else "sin_concluir"
    if veredicto_propio == "sin_concluir" and _extension_activa():
        regla = _regla_aplica(tupla_str, py)
        if regla is not None:
            return {
                "veredicto": "malo_confirmado",
                "detalle": {
                    "origen": "extension_calibracion_expertas_04ago",
                    "motivo": f"py en [{regla['py_min']:.2f},{regla['py_max']:.2f}), "
                              "calibracion wallets expertas confirma precio ya eficiente",
                    "detalle_propio": detalle,
                },
            }

    # 05-Ago: extensión de PROMOCIÓN a bueno_confirmado (ver
    # _ZONAS_VALIDADAS_EXTERNAMENTE arriba) -- solo cuando el propio dato
    # sigue sin concluir. Sin flag de activación separado (a diferencia de
    # la extensión de arriba): son solo 3 tuplas, ya vivas hoy con dinero
    # real, aprobadas explícitamente por Javi el mismo día que se creó.
    if veredicto_propio == "sin_concluir":
        for lo, hi in _ZONAS_VALIDADAS_EXTERNAMENTE.get(tupla_str, []):
            if lo <= py < hi:
                return {
                    "veredicto": "bueno_confirmado",
                    "detalle": {
                        "origen": "validacion_externa_05ago",
                        "motivo": f"py en [{lo:.2f},{hi:.2f}), validado con fuente externa "
                                  "(ballenas_timing_history/franja_milimetrica_ballenas/"
                                  "punto_confirmacion) mientras el dato propio madura",
                        "detalle_propio": detalle,
                    },
                }

    if detalle is not None:
        return {"veredicto": veredicto_propio, "detalle": detalle}
    return {"veredicto": "sin_concluir", "detalle": None}
