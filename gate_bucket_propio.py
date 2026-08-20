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

# 15-Ago (/code-review, hallazgo real): estas rutas eran relativas al cwd
# del proceso que importa este módulo -- funcionaba mientras solo lo
# importaban procesos ya arrancados con cwd=repo (run_fast.sh/run_slow.sh
# hacen cd primero). vigia_degradacion_live.py corre por cron SIN cd previo
# (cwd=$HOME=/root), así que cargar_pares_live_fail_closed() fallaba
# SIEMPRE ahí (mismo patrón de bug ya documentado en el proyecto para
# run_fast.sh, ver project_fix_cpu_ram_consolidacion_11ago). Ancladas al
# fichero del módulo para que funcionen sin importar el cwd del caller.
_REPO = Path(__file__).resolve().parent
DATA_PATH = _REPO / "data/shadow/gate_bucket_propio.json"
CONFIG_LIVE = _REPO / "data/live/config_live.json"
OVERRIDE_PATH = _REPO / "data/live/gate_bucket_propio_override.json"
# 20-Ago: ventana deslizante (analisis_gate_bucket_fino.py), extensión de
# PROMOCIÓN a bueno_confirmado -- ver _zonas_finas()/evaluar() abajo.
DATA_PATH_FINO = _REPO / "data/shadow/gate_bucket_fino.json"
STEP = 0.05

_cache = {"mtime": None, "data": {}}
_cache_fino = {"mtime": None, "data": {}}
_cache_cfg = {"mtime": None, "activo": False}
_cache_override = {"mtime": None, "data": {}}

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
#   - FAVORITO_CONFIRMADO#BTC#60min#BUY_NO: la validación por simetría
#     con franja_milimetrica_ballenas.json citada aquí originalmente
#     (05-Ago) quedó OBSOLETA -- ver nota 10-Ago más abajo, contradice
#     este mismo bullet: con datos post-TWAP el bucket [0.40,0.45) YA NO
#     pasa el rigor. Este bullet se deja como registro histórico de lo
#     que se creía entonces, no como validación vigente.
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
#
# 09-Ago noche: Polymarket cambió la resolución de los mercados 5min/15min
# de snapshot a TWAP Chainlink (30s/60s) el 07-Ago (confirmado vía API +
# verificación empírica propia, ver memoria project_twap_chainlink_
# confirmado_09ago). Las 2 entradas de abajo se sembraron el 05-Ago desde
# fuentes 100% pre-cambio -- pausadas el 09-Ago (fail-closed) hasta
# reconfirmar con datos TWAP-safe.
#
# 10-Ago: reconfirmadas -- `analisis_zonas_validadas_externas_post_twap_
# 10ago.py` recalcula estas 2 tuplas SOLO con datos post-07-Ago de
# ballenas_timing_history.csv (n=2500-14700/zona, Wilson90lo vs breakeven
# real con fee 7%, concentración de mercado <=30%, split-half consistente
# en ambas mitades del periodo) -- ver memoria project_zonas_externas_
# reconfirmadas_post_twap_10ago. Se carga DINÁMICO (no hardcodeado) desde
# data/shadow/zonas_validadas_externas.json, regenerado a diario (cron
# vigia_zonas_validadas_externas.py) para que crezca solo con el n nuevo.
# 10-Ago: FAVORITO_CONFIRMADO#BTC#60min#BUY_NO tenía aquí una entrada
# ESTÁTICA [(0.40,0.45)] desde el 05-Ago -- anterior al cambio TWAP
# (07-Ago) y NUNCA revalidada, hallazgo real al añadir esta tupla al
# análisis dinámico: con solo datos post-TWAP ese bucket ya NO pasa el
# rigor (margen +0.0pp). La tupla lleva desde entonces operando en ese
# rango usando validación pre-TWAP obsoleta -- corregido moviendo la
# tupla al mecanismo DINÁMICO (analisis_zonas_validadas_externas_post_
# twap_10ago.py, zonas reales hoy: [0.10,0.15)/[0.35,0.40)/[0.90,0.95)),
# que sustituye (no sólo complementa) cualquier entrada estática con la
# misma clave -- ver _zonas_validadas_externamente() abajo.
_ZONAS_VALIDADAS_EXTERNAMENTE_ESTATICAS = {}
_ZONAS_DINAMICAS_PATH = Path("data/shadow/zonas_validadas_externas.json")
_cache_zonas_dinamicas = {"mtime": None, "data": {}}


def _zonas_validadas_externamente() -> dict:
    """Combina las zonas estáticas (familias no afectadas por TWAP) con las
    dinámicas (regeneradas a diario desde ballenas_timing_history.csv
    post-TWAP). Fail-open a solo estáticas si el JSON dinámico falta o está
    corrupto -- nunca bloquea el arranque por un fichero de refuerzo.

    10-Ago (/code-review, hallazgo real): el merge anterior solo
    sobreescribía la entrada estática cuando la dinámica para esa misma
    clave era una lista NO vacía (`if zonas:`) -- si en el futuro se
    reintrodujera una entrada estática para una tupla cuya dinámica
    recalculara a "sin zonas" ([]), la estática sobreviviría intacta sin
    que nadie lo notara, exactamente el fallo que este mecanismo existe
    para evitar. Ahora sobreescribe siempre que la clave EXISTE en el
    dinámico, sea la lista vacía o no -- "sin zonas confirmadas hoy" debe
    poder anular una zona estática vieja, no solo una lista con contenido."""
    combinado = dict(_ZONAS_VALIDADAS_EXTERNAMENTE_ESTATICAS)
    try:
        mtime = _ZONAS_DINAMICAS_PATH.stat().st_mtime
    except OSError:
        return combinado
    if _cache_zonas_dinamicas["mtime"] != mtime:
        try:
            bruto = json.loads(_ZONAS_DINAMICAS_PATH.read_text(encoding="utf-8"))
            _cache_zonas_dinamicas["data"] = {
                tupla: [tuple(z) for z in info.get("zonas_bueno_confirmado", [])]
                for tupla, info in bruto.items()
            }
            _cache_zonas_dinamicas["mtime"] = mtime
        except Exception:
            pass
    for tupla, zonas in _cache_zonas_dinamicas["data"].items():
        combinado[tupla] = zonas
    return combinado


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


def _cargar_override() -> dict:
    """Cortacircuitos de emergencia (05-Ago, petición explícita Javi:
    "asegúrate que el mecanismo autoaprendiente tenga un backup que lo
    proteja siempre y no nos haga perder pasta"). data/live/gate_bucket_
    propio_override.json -- {"TUPLA#bucket": {"motivo":..., "desde":...}}
    o {"TUPLA": {...}} para vetar toda la tupla. Escribible a mano
    (Javi/sesión) o automáticamente por vigia_micro_bucket_kill_switch.py
    cuando el dinero real en un bucket "bueno_confirmado" empieza a
    sangrar de verdad. SIEMPRE gana sobre cualquier otro veredicto,
    incluido bueno_confirmado -- es la última palabra, fail-closed. Un
    fichero corrupto/inaccesible se trata como override VACÍO (no bloquea
    nada por error de lectura, pero tampoco dice "bueno" -- evaluar()
    sigue cayendo al resto de la lógica normal)."""
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


def _zonas_finas() -> dict:
    """{tupla_str: {"lo":, "hi":, "veredicto":, ...}} desde
    data/shadow/gate_bucket_fino.json (analisis_gate_bucket_fino.py,
    20-Ago) -- ventana deslizante (paso 0.01, ancho libre, NO anclada al
    grid fijo de 0.05) sobre el mismo results.csv, con su propio rigor
    (permutación max-statistic + split-half + BH-FDR por familia/moneda,
    ver docstring de ese script). Fail-open a {} si el fichero falta o
    está corrupto -- nunca bloquea el arranque por un fichero de refuerzo,
    mismo criterio que el resto de fuentes de este módulo."""
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


def tiene_datos_propios(tupla_str: str) -> bool:
    """False si `tupla_str` no tiene NINGÚN bucket con datos reales en
    gate_bucket_propio.json -- clave ausente, o mapeada a un dict vacío
    ({}, el placeholder de estrategias como WALLET_MIRROR que nunca
    escriben en results.csv, ver analisis_gate_bucket_propio_28jul.py).
    OJO: {} también es lo que escribe analisis_gate_bucket_propio_28jul.py
    para CUALQUIER tupla con n<15 propio, no solo las estructuralmente
    huérfanas -- una tupla recién promocionada que SÍ tiene cobertura vía
    _zonas_validadas_externamente() da igualmente {} aquí. NO usar esta
    función sola para decidir si el gate aplica (ver tiene_alguna_fuente_
    evaluable), solo para inspección/diagnóstico."""
    return bool(_cargar().get(tupla_str))


def tiene_alguna_fuente_evaluable(tupla_str: str) -> bool:
    """True si `evaluar(tupla_str, py)` puede dar un veredicto informado
    para ALGÚN precio -- porque hay datos propios (tiene_datos_propios) O
    porque hay una zona validada externamente para esta tupla (dato propio
    todavía madurando, cubierto por _zonas_validadas_externamente()).

    18-Ago (/code-review medium, hallazgo real): live_trade.py usaba
    tiene_datos_propios() solo -- una tupla recién promocionada con n<15
    propio pero YA con zona externa confirmada (el camino normal descrito
    en CLAUDE.md pt. 'Veto de micro-bucket de precio') tiene {} en
    gate_bucket_propio.json exactamente igual que WALLET_MIRROR (que
    nunca escribe en results.csv y tiene su propio gate separado,
    wallet_mirror_gate_bucket.py, aplicado río arriba) -- ambos casos
    eran indistinguibles y el re-chequeo post-requote se saltaba entero
    para los dos, dejando pasar cualquier precio de fill sin veto en la
    tupla recién promocionada. Esta función solo excluye del re-chequeo
    la situación verdaderamente estructural: sin dato propio Y sin ninguna
    zona externa que pueda evaluarse -- ahí evaluar() no tiene NADA con lo
    que emitir un veredicto salvo 'sin_concluir' fijo (que abortaría SIEMPRE
    ese fill, el mismo efecto práctico que excluirla, pero explícito)."""
    if tiene_datos_propios(tupla_str):
        return True
    return tupla_str in _zonas_validadas_externamente()


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
    # 06-Ago (fix real, hallazgo al responder una pregunta de Javi sobre
    # cobertura de buckets): sin el +1e-9, un precio EXACTO en un múltiplo
    # de STEP (ej. 0.70) puede dar 13.999999999999998 en la división por
    # coma flotante -- math.floor lo trunca al bucket INFERIOR (0.65 en vez
    # de 0.70). Verificado real: el bucket "0.65" de FAVORITO_CONFIRMADO_
    # 15MIN_ALTACONVICCION#BTC#15min#BUY_YES (n=189, el de más datos) no
    # tenía NINGÚN precio real 0.65-0.699 -- eran todos 0.70 exactos mal
    # etiquetados. 5.08% de las filas de results.csv afectadas (3998/78659).
    # Mismo bug duplicado en 6 ficheros más, ver idea_bug_bucketing_float_
    # precision_micro_buckets_06ago en memoria.
    b = round(math.floor(py / STEP + 1e-9) * STEP, 4)
    b_str = f"{b:.2f}"

    # Cortacircuitos de emergencia -- SIEMPRE se comprueba primero, gana
    # sobre cualquier otro veredicto (incluido bueno_confirmado propio).
    override = _cargar_override()
    ov = override.get(f"{tupla_str}#{b_str}") or override.get(tupla_str)
    if ov is not None:
        return {
            "veredicto": "malo_confirmado",
            "detalle": {"origen": "override_emergencia", "motivo": ov.get("motivo", "sin motivo registrado"),
                        "desde": ov.get("desde")},
        }

    tabla = _cargar().get(tupla_str, {})
    detalle = tabla.get(b_str)

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

    # 20-Ago: extensión de PROMOCIÓN a bueno_confirmado vía ventana
    # deslizante (analisis_gate_bucket_fino.py, ver _zonas_finas() arriba)
    # -- mismo patrón aditivo que _zonas_validadas_externamente() de abajo,
    # pero con NUESTROS PROPIOS datos a resolución fina (paso 0.01, ancho
    # libre) en vez de una fuente externa. Va ANTES que la extensión
    # externa a propósito: mismo results.csv que el grid fijo, solo con
    # una ventana mejor situada -- más directamente relevante que una
    # fuente externa (ballenas) cuando ambas están disponibles. Solo
    # promueve, nunca degrada -- si el propio dato YA confirmó algo
    # (bueno/malo), esta rama ni se evalúa (veredicto_propio ya no es
    # "sin_concluir"). Origen: BALLENAS_TARDIAS#ETH#5min#BUY_YES (LIVE)
    # llevaba 17/17 buckets fijos "sin_concluir" pese a tener un edge real
    # más estrecho que el grid de 0.05 diluía -- ver idea_gate_bucket_fino_
    # ventana_deslizante_20ago.
    if veredicto_propio == "sin_concluir":
        fina = _zonas_finas().get(tupla_str)
        if fina and fina.get("veredicto") == "bueno_confirmado":
            lo, hi = fina.get("lo"), fina.get("hi")
            if lo is not None and hi is not None and lo <= py < hi:
                return {
                    "veredicto": "bueno_confirmado",
                    "detalle": {
                        "origen": "ventana_deslizante_20ago",
                        "motivo": f"py en [{lo:.2f},{hi:.2f}), ventana fina "
                                  f"(n={fina.get('n')}, p={fina.get('p_valor')}) "
                                  "mientras el grid fijo sigue sin_concluir",
                        "detalle_propio": detalle,
                    },
                }

    # 05-Ago: extensión de PROMOCIÓN a bueno_confirmado (ver
    # _ZONAS_VALIDADAS_EXTERNAMENTE arriba) -- solo cuando el propio dato
    # sigue sin concluir. Sin flag de activación separado (a diferencia de
    # la extensión de arriba): son solo 3 tuplas, ya vivas hoy con dinero
    # real, aprobadas explícitamente por Javi el mismo día que se creó.
    if veredicto_propio == "sin_concluir":
        for lo, hi in _zonas_validadas_externamente().get(tupla_str, []):
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


def cargar_pares_live_fail_closed() -> tuple[set, bool]:
    """Lee pares_permitidos_live de config_live.json para los helpers de
    abajo. Devuelve (pares, ok) -- ok=False si config_live.json no se pudo
    leer/parsear: el caller NUNCA debe interpretar un set() vacío en ese
    caso como "no hay tuplas live" (fail-open), sino decidir explícitamente
    qué hacer sin datos (15-Ago, /code-review: filtro nuevo de zona
    confirmada era fail-open en exactamente este punto)."""
    try:
        pares = set(json.loads(CONFIG_LIVE.read_text()).get("pares_permitidos_live", []))
        return pares, True
    except Exception:
        return set(), False


def parsear_features(raw) -> dict:
    """json.loads() seguro para la columna `features` (results.csv/
    predictions.csv): degrada a {} tanto si el JSON no parsea como si
    parsea a algo que NO es un dict (null, número, string -- una fila de
    CSV corrupta por una carrera de escritura concurrente, ya vista una vez
    en este proyecto el 14-Ago, puede producir cualquiera de los dos).
    15-Ago (/code-review): antes cada caller solo envolvía el json.loads()
    en try/except y llamaba .get() directo sobre el resultado -- un JSON
    válido pero no-dict (ej. "null") pasaba el try/except y reventaba con
    AttributeError en el primer .get()."""
    try:
        feats = json.loads(raw or "{}")
    except Exception:
        return {}
    return feats if isinstance(feats, dict) else {}


def veredicto_bloquea_ejecucion(feats: dict) -> bool:
    """True si el veredicto de gate_bucket_propio en `feats` (ya parseado
    con parsear_features) debe bloquear la ejecución real de una tupla ya
    en pares_permitidos_live -- fail-closed: exige 'bueno_confirmado'
    explícito, cualquier otra cosa (malo_confirmado/sin_concluir) o
    ausencia total del feature en una tupla que SÍ lo consulta bloquea.
    Si la predicción nunca trae esta clave (estrategias que no consultan
    este gate) el caller debe decidir aparte -- esta función solo mira lo
    que ya está presente, no decide si debía estarlo."""
    veredicto = feats.get("gate_bucket_propio_veredicto")
    return veredicto is not None and veredicto != "bueno_confirmado"


def filtrar_filas_zona_confirmada(filas: list, pares_live: set) -> list:
    """Filtra filas de results.csv (dicts con strategy/subtype/decision/
    features) excluyendo, SOLO para tuplas ya en pares_permitidos_live, las
    que caigan en una zona de precio no confirmada (gate_bucket_propio_
    veredicto presente y != 'bueno_confirmado'). Filas de tuplas que no
    están live, o sin ese feature (estrategias que nunca consultan este
    gate), pasan sin filtrar.

    15-Ago: extraído como helper único tras el fix del estado absorbente
    de shadow_predict.py (las tuplas live ya no suprimen su predicción
    entera en zonas no confirmadas, así que cualquier consumidor de
    results.csv que calcule una métrica AGREGADA para una tupla live tiene
    que aplicar este mismo filtro o mezcla evidencia de zonas que nunca
    fueron -- ni serán -- candidatas reales de ejecución. /code-review
    encontró la misma falta de filtro, tras aplicarlo ya en
    shadow_postmortem.py, en analisis_log_growth.py (gate de crecimiento
    logarítmico, CLAUDE.md pt.12/14) y vigia_degradacion_live.py (monitor
    shadow-vs-real) -- los 3 ahora comparten esta única función en vez de
    reimplementar el mismo criterio por separado."""
    if not pares_live:
        return filas
    out = []
    for r in filas:
        tupla = f"{r.get('strategy', '')}#{r.get('subtype', '')}#{r.get('decision', '')}"
        if tupla in pares_live and veredicto_bloquea_ejecucion(parsear_features(r.get("features"))):
            continue
        out.append(r)
    return out
