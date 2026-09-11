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
import time
from pathlib import Path

# 01-Sep: guardián de frescura (petición explícita Javi, "no lo podemos
# permitir, tiene que hacerlo cada vez que se vaya a hacer un trade, sino
# corremos riesgo de perder pasta") -- evaluar() YA lee el fichero en vivo
# en cada llamada (nunca cachea más allá de un ciclo, ver _cargar()), pero
# el DATO en sí solo se recalcula una vez al día (cron 06:55/06:58 UTC,
# analisis_gate_bucket_propio_28jul.py/analisis_gate_bucket_fino.py) --
# recomputar el gate riguroso completo (shuffle+bootstrap+búsqueda de
# ventana) en el instante exacto de cada señal no es viable (son minutos
# de cómputo, no compatible con la latencia de un ejecutor). La protección
# real y viable: si el fichero lleva más tiempo del esperado sin
# regenerarse (el cron se rompió, o algo lo bloqueó), tratar el dato como
# NO FIABLE (equivalente a sin datos) en vez de confiar ciegamente en un
# "bueno_confirmado" de ayer o de hace días -- fail-closed por antigüedad,
# no solo por ausencia. Margen generoso sobre la cadencia real del cron
# (2x + un colchón) para no disparar por una ejecución de cron puntualmente
# tardía.
MAX_ANTIGUEDAD_S = 30 * 3600  # 30h -- cron diario (06:55/06:58 UTC) + margen

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
# 28-Ago: veto por fill-ability real (analisis_gate_bucket_propio_fillable_
# 03ago.py, construido 03-Ago, NUNCA conectado hasta hoy -- ver
# feedback_veto_fillable_conectado_28ago). Petición explícita Javi tras
# encontrar el MISMO patrón 3 veces en una sola sesión: un bucket con
# pnl_medio espectacular en results.csv (agregado, sin filtrar fill-ability)
# resulta, al restringir al subconjunto realmente ejecutable (profundidad-al-
# origen vía features::profundidad_ratio_vs_stake o libro_snapshots.csv
# colapsado), con edge negativo o insuficiente liquidez para siquiera medir
# algo -- selección adversa disfrazada de señal. Antes esto se cazaba a mano,
# tupla por tupla, cada vez que alguien se molestaba en comprobarlo. Ver
# _veto_fillable() más abajo.
DATA_PATH_FILLABLE = _REPO / "data/shadow/gate_bucket_propio_fillable.json"
# 31-Ago: promoción condicional por consenso de bot wallets (Candidata 9,
# analisis_bot_consenso_gate_momentum_ballena.py, cron diario) -- a
# diferencia de _zonas_finas()/_zonas_validadas_externamente() (dependen
# solo de tupla_str+py), esta fuente depende TAMBIÉN de si bot_consenso_lado
# coincide con la dirección de la señal en el momento exacto -- por eso
# necesita el parámetro opcional `bot_consenso_lado` en evaluar() (ver
# pendiente #1 de project_checkpoint_sesion_31ago_dashboard_walletmirror).
# Solo cubre MOMENTUM_IBS_5M_BALLENA hoy, tupla PAUSADA (fuera de
# pares_permitidos_live desde 29-Ago) -- cero riesgo de dinero real al
# conectarlo, listo para cuando se reactive.
DATA_PATH_BOTCONSENSO = _REPO / "data/shadow/bot_consenso_gate_momentum_ballena.json"
STEP = 0.05

_cache = {"mtime": None, "data": {}}
_cache_fino = {"mtime": None, "data": {}}
_cache_fillable = {"mtime": None, "data": {}}
_cache_botconsenso = {"mtime": None, "data": {}}
_cache_cfg = {"mtime": None, "activo": False}
_cache_override = {"mtime": None, "data": {}}

# Umbrales del veto de fill-ability -- deliberadamente conservadores (mismo
# n_min que el resto del proyecto, CLAUDE.md: "ninguna conclusión con n<15").
# Solo puede DEGRADAR bueno_confirmado -> malo_confirmado, nunca al revés --
# si no hay evidencia suficiente (n<15 en cualquiera de los dos chequeos),
# el veredicto original se mantiene sin tocar (fail-open EN EL VETO, no en
# el gate -- ausencia de evidencia de selección adversa no es evidencia de
# que no la haya, pero tampoco se puede inventar un umbral sin datos).
_FILLABLE_N_MIN = 15
_FILLABLE_RATE_MIN = 0.30  # por debajo del rango 53-90% típico de arquetipo B

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
    if time.time() - mtime > MAX_ANTIGUEDAD_S:
        return combinado  # 01-Sep (/code-review, hallazgo real, tercera
        # fuente sin proteger de las 3 que evaluar() consulta): dinámico
        # demasiado viejo -- se descarta, solo quedan las estáticas
        # (las estáticas no dependen de un cron, no necesitan este guardián).
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
    if time.time() - mtime > MAX_ANTIGUEDAD_S:
        return {}  # dato demasiado viejo -- tratar como sin datos, fail-closed
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
    if time.time() - mtime > MAX_ANTIGUEDAD_S:
        return {}  # 01-Sep: mismo guardián de frescura que _cargar()
    if _cache_fino["mtime"] != mtime:
        try:
            _cache_fino["data"] = json.loads(DATA_PATH_FINO.read_text(encoding="utf-8"))
            _cache_fino["mtime"] = mtime
        except Exception:
            pass
    return _cache_fino["data"]


def _cargar_fillable() -> dict:
    """{tupla_str: {bucket_str: {"n":, "pnl_medio":, ...}}} desde
    data/shadow/gate_bucket_propio_fillable.json (analisis_gate_bucket_
    propio_fillable_03ago.py, cron diario). OJO: el campo "veredicto" de
    ese fichero usa un criterio DISTINTO (solo relativo al resto de la
    tupla, sin el piso absoluto de bootstrap que sí tiene el gate
    principal desde el 08-Ago) -- _veto_fillable() de abajo NUNCA lee ese
    campo, solo "n"/"pnl_medio" en crudo para su propia comparación
    absoluta contra cero. Fail-open a {} si falta/corrupto, mismo
    criterio que el resto de fuentes de este módulo."""
    try:
        mtime = DATA_PATH_FILLABLE.stat().st_mtime
    except OSError:
        return {}
    # 01-Sep (/code-review, hallazgo real): NO se le añade el guardián de
    # frescura de las otras fuentes -- _veto_fillable() (abajo) SOLO puede
    # DEGRADAR (bueno_confirmado->malo_confirmado), nunca promocionar, y ya
    # es fail-open POR DISEÑO cuando faltan datos (`if not entrada_fill:
    # return resultado`, documentado explícitamente: "ausencia de evidencia
    # de selección adversa no es evidencia de ausencia" -- decisión previa
    # aceptada, no algo a cambiar de pasada esta noche). Añadir el guardián
    # aquí habría convertido "dato viejo" en "veto desactivado" -- el
    # sentido contrario al que se pretendía (fail-open donde se buscaba
    # fail-closed). Dejar la puerta MTIME sin tocar; solo el corte por
    # OSError (fichero ausente) sigue aplicando, igual que antes de esta
    # sesión.
    if _cache_fillable["mtime"] != mtime:
        try:
            _cache_fillable["data"] = json.loads(DATA_PATH_FILLABLE.read_text(encoding="utf-8"))
            _cache_fillable["mtime"] = mtime
        except Exception:
            pass
    return _cache_fillable["data"]


def _cargar_bot_consenso() -> dict:
    """{tupla_str: {bucket_str: {"coincide": {...}, "discrepa": {...}}}}
    desde data/shadow/bot_consenso_gate_momentum_ballena.json (31-Ago).
    Fail-open a {} si falta/corrupto, mismo criterio que el resto de
    fuentes de este módulo."""
    try:
        mtime = DATA_PATH_BOTCONSENSO.stat().st_mtime
    except OSError:
        return {}
    if time.time() - mtime > MAX_ANTIGUEDAD_S:
        return {}  # 01-Sep: mismo guardián de frescura -- fuente de promoción,
        # mismo riesgo que las otras 3 ya protegidas
    if _cache_botconsenso["mtime"] != mtime:
        try:
            _cache_botconsenso["data"] = json.loads(DATA_PATH_BOTCONSENSO.read_text(encoding="utf-8"))
            _cache_botconsenso["mtime"] = mtime
        except Exception:
            pass
    return _cache_botconsenso["data"]


def _bot_consenso_coincide(tupla_str: str, bot_consenso_lado):
    """True/False si `bot_consenso_lado` (feature cruda de _bots_consenso()
    en shadow_predict.py, valores "Up"/"Down") coincide con la dirección
    codificada en `tupla_str` (STRATEGY#ACTIVO#MARCO#DIRECCION). None si no
    se puede determinar (tupla_str mal formada, lado vacío, o dirección
    fuera del vocabulario BUY_YES/BUY_NO -- ej. WALLET_MIRROR usa
    BUY_Up/BUY_Down, este mecanismo no aplica ahí).

    MISMA fórmula que analisis_bot_consenso_gate_momentum_ballena.py
    (única fuente de verdad, no reimplementar aparte -- ver ese script si
    esto diverge)."""
    if not bot_consenso_lado:
        return None
    partes = tupla_str.split("#")
    if len(partes) != 4:
        return None
    decision = partes[3]
    if decision == "BUY_YES":
        return bot_consenso_lado == "Up"
    if decision == "BUY_NO":
        return bot_consenso_lado == "Down"
    return None


def _veto_fillable(tupla_str: str, py: float, resultado: dict) -> dict:
    """Último paso de evaluar(): si el resultado es "bueno_confirmado"
    (venga del propio gate_bucket_propio.json, de zonas_finas o de
    zonas_validadas_externamente -- no importa el origen), lo contrasta
    contra el subconjunto REALMENTE fillable de ese mismo micro-bucket de
    precio. Solo puede DEGRADAR a malo_confirmado, nunca promocionar --
    si no hay evidencia (n<15 en ambos chequeos), el resultado original
    se devuelve intacto.

    TRES señales independientes, cualquiera basta (28-Ago, hallazgo real:
    3 tuplas confirmadas por gate_bucket_fino en la misma sesión con pnl
    de shadow espectacular resultaron, al mirar el subconjunto fillable,
    en 6-32% de fill real y/o pnl invertido -- ver feedback_veto_
    fillable_conectado_28ago; ampliado el mismo día tras corrección
    explícita de Javi -- "ya sabes que tenemos la solución al payout
    asimétrico" -- el primer intento solo cubría selección adversa/
    profundidad, faltaba la tercera pata):
      1. El subconjunto fillable tiene n>=15 propio Y su pnl_medio es
         negativo -- contradicción directa y medible, no solo "poca
         liquidez": el edge que parecía confirmado no sobrevive donde
         de verdad se podría haber ejecutado.
      2. La TASA de fill (fillable / total del propio gate_bucket_
         propio.json en ese bucket) cae por debajo de _FILLABLE_RATE_MIN
         -- incluso sin pnl suficiente para concluir signo, un bucket
         donde menos del 30% de las señales tenían libro real es
         estructuralmente el mismo patrón que arquetipo A (edge y hueco
         de libro coinciden en el tiempo), no una señal operable.
      3. Payout asimétrico (Kelly g(f=10%), CLAUDE.md pt.14/P28, misma
         fórmula que analisis_log_growth.py -- NUNCA reimplementada
         aparte): con n_fill>=15, g_kelly_f10<=0 en el subconjunto
         fillable -- hit-rate alto con pérdidas grandes y raras puede
         dar pnl_medio positivo y aun así crecimiento compuesto
         negativo. Mismo bug que casi promociona MOMENTUM_IBS_5M_
         BALLENA#ETH#5min#BUY_YES con el agregado equivocado esta
         misma sesión (el agregado sin filtrar por bucket daba
         g=-0.01535; restringido al bucket operativo real daba
         g=+0.01332) -- ahora el gate lo calcula solo, no hace falta
         repetir el cálculo a mano cada vez que se evalúa una promoción.

    LIMITACIÓN CONOCIDA (documentada, no bloqueante): gate_bucket_propio_
    fillable.json usa el mismo grid fijo (STEP=0.05) que este módulo,
    pero una confirmación de zonas_finas (ventana deslizante, ancho
    libre, NO anclada al grid) puede caer a caballo entre dos buckets
    fijos -- el veto solo ve el bucket fijo que contiene el `py` exacto
    de la señal, no toda la ventana fina. Cobertura parcial es mejor que
    ninguna, pero no es una garantía perfecta para ventanas finas que
    crucen un límite de 0.05."""
    if resultado.get("veredicto") != "bueno_confirmado":
        return resultado
    b_str = f"{bucket(py):.2f}"
    entrada_fill = _cargar_fillable().get(tupla_str, {}).get(b_str)
    if not entrada_fill:
        return resultado
    n_fill = entrada_fill.get("n", 0)
    pnl_fill = entrada_fill.get("pnl_medio")
    g_kelly = entrada_fill.get("g_kelly_f10")
    n_total = (_cargar().get(tupla_str, {}).get(b_str) or {}).get("n", 0)

    motivo = None
    if n_fill >= _FILLABLE_N_MIN and pnl_fill is not None and pnl_fill < 0:
        motivo = (f"subconjunto fillable (n={n_fill}) da pnl_medio={pnl_fill:+.4f} "
                  f"negativo pese a bueno_confirmado -- selección adversa")
    elif n_fill >= _FILLABLE_N_MIN and g_kelly is not None and g_kelly <= 0:
        motivo = (f"subconjunto fillable (n={n_fill}) da g_kelly(f=10%)={g_kelly:+.5f} "
                  f"-- payout inverso (hit-rate alto con pérdidas grandes raras)")
    elif n_total >= _FILLABLE_N_MIN and n_fill < n_total * _FILLABLE_RATE_MIN:
        ratio_pct = (n_fill / n_total * 100) if n_total else 0.0
        motivo = (f"fill-ability real {n_fill}/{n_total} ({ratio_pct:.1f}%) por debajo "
                  f"del {_FILLABLE_RATE_MIN*100:.0f}% mínimo -- selección adversa")
    if motivo is None:
        return resultado
    return {
        "veredicto": "malo_confirmado",
        "detalle": {"origen": "veto_fillable_28ago", "motivo": motivo,
                    "detalle_original": resultado.get("detalle")},
    }


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
    return tupla_str in _zonas_validadas_externamente_claves()


def _zonas_validadas_externamente_claves() -> set:
    """01-Sep (/code-review, hallazgo real): tiene_alguna_fuente_evaluable()
    llamaba a _zonas_validadas_externamente() -- desde el guardián de
    frescura de esta noche, esa función devuelve SOLO las estáticas cuando
    el dinámico está viejo, así que una tupla cuya ÚNICA cobertura sea la
    zona dinámica (ahora stale) desaparecía del todo del set de claves, y
    tiene_alguna_fuente_evaluable() pasaba a devolver False -- en
    live_trade.py eso NO degrada a 'siempre abortar' (el efecto que el
    docstring de arriba documenta como aceptable), salta el bloque de
    re-chequeo post-requote ENTERO, dejando pasar el fill sin ningún veto.
    Esta función responde una pregunta distinta y más barata: ¿existe
    ALGUNA fuente (estática o dinámica, viva o stale) que en principio
    pudiera cubrir esta tupla? -- pura existencia de clave, ignora
    antigüedad a propósito (evaluar() ya se encarga de que una zona stale
    nunca promocione nada; aquí solo interesa que el re-chequeo no se
    salte por completo)."""
    claves = set(_ZONAS_VALIDADAS_EXTERNAMENTE_ESTATICAS.keys())
    # /code-review 01-Sep (hallazgo real): la primera versión releía y
    # reparseaba el JSON en CADA llamada (esta función se invoca en el
    # camino de cada trade real, vía tiene_alguna_fuente_evaluable() desde
    # live_trade.py) en vez de reusar el mismo caché por mtime que el resto
    # del módulo -- comparte _cache_zonas_dinamicas con
    # _zonas_validadas_externamente(), refrescándolo igual (sin el
    # guardián de frescura, a propósito: aquí solo interesa la existencia
    # de la clave, no si el dato es fiable ahora mismo).
    try:
        mtime = _ZONAS_DINAMICAS_PATH.stat().st_mtime
    except OSError:
        return claves
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
    claves |= set(_cache_zonas_dinamicas["data"].keys())
    return claves


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


def bucket(py: float) -> float:
    """Único punto de verdad del bucketing (STEP=0.05) -- reutilizado por
    evaluar()/evaluar_sin_override() y por cualquier vigía externo que
    necesite reconstruir la MISMA clave exacta (24-Ago, /code-review:
    antes cada vigía de kill-switch/reapertura reimplicaba esta fórmula a
    mano, riesgo real de que un cambio aquí divergiera en silencio de las
    copias). 06-Ago (fix real): sin el +1e-9, un precio EXACTO en un
    múltiplo de STEP (ej. 0.70) puede dar 13.999999999999998 en la
    división por coma flotante -- math.floor lo trunca al bucket INFERIOR
    (0.65 en vez de 0.70). Verificado real: el bucket "0.65" de
    FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min#BUY_YES (n=189, el
    de más datos) no tenía NINGÚN precio real 0.65-0.699 -- eran todos
    0.70 exactos mal etiquetados. 5.08% de las filas de results.csv
    afectadas (3998/78659)."""
    import math
    return round(math.floor(py / STEP + 1e-9) * STEP, 4)


def evaluar(tupla_str: str, py: float, bot_consenso_lado=None) -> dict:
    """{"veredicto": "malo_confirmado"|"bueno_confirmado"|"sin_concluir",
    "detalle": {...}|None}. No decide permitido/vetado -- eso lo hace el
    caller (fase 0: solo loguea; fase 1: veta si malo_confirmado).

    `bot_consenso_lado` (31-Ago, opcional, default None -- NINGÚN caller
    existente cambia de comportamiento si no lo pasa): feature cruda
    "Up"/"Down" de _bots_consenso() en shadow_predict.py, en el momento
    exacto de la señal. Si se pasa, habilita la promoción adicional de
    bot_consenso_gate_momentum_ballena.json (ver _evaluar_sin_override_ni_
    veto() abajo) -- hoy solo cubre MOMENTUM_IBS_5M_BALLENA.

    Cortacircuitos de emergencia -- SIEMPRE se comprueba primero, gana
    sobre cualquier otro veredicto (incluido bueno_confirmado propio)."""
    b_str = f"{bucket(py):.2f}"
    override = _cargar_override()
    ov = override.get(f"{tupla_str}#{b_str}") or override.get(tupla_str)
    if ov is not None:
        return {
            "veredicto": "malo_confirmado",
            "detalle": {"origen": "override_emergencia", "motivo": ov.get("motivo", "sin motivo registrado"),
                        "desde": ov.get("desde")},
        }
    return evaluar_sin_override(tupla_str, py, bot_consenso_lado=bot_consenso_lado)


def evaluar_sin_override(tupla_str: str, py: float, bot_consenso_lado=None) -> dict:
    """MISMA lógica que evaluar() pero SIN consultar el override de
    emergencia -- exclusivamente para los vigías de reapertura (24-Ago,
    /code-review, hallazgo real): un vigía que quiere comprobar "¿el gate
    de verdad, sin el bloqueo que él mismo puso, ya no confirma malo?" NO
    puede llamar a evaluar() a secas -- mientras el override siga escrito,
    evaluar() lo ve primero y SIEMPRE devuelve malo_confirmado, sea cual
    sea el estado real de la tabla, haciendo que la condición de
    reapertura nunca se cumpla (bug real cazado antes de desplegar, ver
    feedback de Javi "no podemos dejar estrategias muertas así"). Esta
    función es el núcleo que evaluar() envuelve con el override.

    28-Ago (/code-review, hallazgo real): el veto de fill-ability (ver
    _veto_fillable() abajo) SIEMPRE se aplica aquí también, no solo desde
    evaluar() -- sin esto, un vigía de reapertura que llame a esta función
    directamente (ej. vigia_reabrir_overrides_micro_bucket.py) vería
    "bueno_confirmado" cuando el gate real (vía evaluar()) ya lo habría
    degradado a malo_confirmado por selección adversa/payout inverso,
    reabriendo overrides con un diagnóstico falso -- mismo patrón exacto
    que el bug de "sin override" que motivó separar esta función el
    24-Ago, ahora aplicado al veto nuevo."""
    return _veto_fillable(tupla_str, py, _evaluar_sin_override_ni_veto(tupla_str, py, bot_consenso_lado))


def _evaluar_sin_override_ni_veto(tupla_str: str, py: float, bot_consenso_lado=None) -> dict:
    b = bucket(py)
    b_str = f"{b:.2f}"
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
                # 01-Sep: confluencia suave (petición explícita Javi, tras
                # el hallazgo de la misma noche de que n<40 en una sola
                # fuente ya disparó dinero real dos veces) -- el fino puede
                # seguir promocionando en solitario cuando el grid está
                # sin_concluir por falta de n (ese es su propósito
                # original, 20-Ago: rescatar un edge más estrecho que el
                # grid de 0.05 diluye), pero NO si el propio grid, con los
                # datos que sí tiene en ESTE bucket exacto (el que contiene
                # `py`, dentro de la ventana que el fino está confirmando),
                # ya apunta en contra (pnl_medio negativo). No exige que el
                # grid TAMBIÉN confirme (eso mataría el caso fundacional
                # BALLENAS_TARDIAS#ETH#5min, 17/17 buckets fijos
                # sin_concluir con edge real dentro) -- solo exige que no
                # contradiga. Sin dato de grid en este bucket (detalle is
                # None) se trata como neutral, no como bloqueo.
                #
                # /code-review 01-Sep (2 hallazgos reales, corregidos antes
                # de commitear):
                # 1. La primera versión leía pnl_medio SIN exigir n mínimo
                #    -- analisis_gate_bucket_propio_28jul.py::main() escribe
                #    pnl_medio para CUALQUIER bucket no vacío (n_d>=1), los
                #    campos de rigor (shuffle/CI/veredicto) solo se añaden
                #    si n_d>=N_MIN. Un bucket de grid con n=1-3 (ruido puro)
                #    podía vetar una confirmación robusta del fino (caso
                #    real de hoy: WEEKLY_PRICE#ETH#BUY_NO bucket 0.50, n=3
                #    pnl_medio=-1.02, mientras el fino confirma esa zona con
                #    n=55 p<0.05). Reusa _FILLABLE_N_MIN (15, piso absoluto
                #    CLAUDE.md) como mínimo para que el pnl del grid cuente
                #    como evidencia real.
                # 2. La segunda versión comprobaba el bucket del grid en
                #    `b_str` (el bucket de CUALQUIER `py`, calculado al
                #    principio de la función) ANTES de saber si `py` caía
                #    dentro de [lo,hi) -- para un `py` fuera de la ventana
                #    fina pero con esa misma tupla teniendo una ventana fina
                #    confirmada EN OTRO PRECIO, el chequeo se ejecutaba
                #    igual y podía devolver sin_concluir sin motivo,
                #    cortando en seco las extensiones de abajo (validación
                #    externa, bot_consenso) que son mecanismos independientes
                #    para ESE `py` distinto. Movido dentro de este
                #    `if lo <= py < hi:` -- ahora solo se compara el grid
                #    contra la MISMA ventana que el fino está confirmando.
                n_grid = (detalle or {}).get("n") or 0
                pnl_grid = (detalle or {}).get("pnl_medio")
                if pnl_grid is not None and n_grid >= _FILLABLE_N_MIN and pnl_grid < 0:
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
                        "origen": "ventana_deslizante_20ago",
                        "motivo": f"py en [{lo:.2f},{hi:.2f}), ventana fina "
                                  f"(n={fina.get('n')}, p={fina.get('p_valor')}) "
                                  "mientras el grid fijo sigue sin_concluir "
                                  "(confluencia suave: grid no contradice)",
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
                # 01-Sep: confluencia suave, mismo patrón que la rama del
                # fino de arriba (ver ese comentario para el caso
                # fundacional completo) -- una fuente externa puede seguir
                # promocionando en solitario mientras el dato propio
                # madura, pero no si el propio grid, en el bucket exacto
                # que la fuente externa está validando, ya apunta en
                # contra (pnl_medio negativo con n>=_FILLABLE_N_MIN).
                n_grid = (detalle or {}).get("n") or 0
                pnl_grid = (detalle or {}).get("pnl_medio")
                if pnl_grid is not None and n_grid >= _FILLABLE_N_MIN and pnl_grid < 0:
                    return {
                        "veredicto": "sin_concluir",
                        "detalle": {
                            "origen": "confluencia_suave_01sep",
                            "motivo": f"validación externa confirma [{lo:.2f},{hi:.2f}) pero "
                                      f"el grid en {b_str} (n={n_grid}) ya apunta en contra "
                                      f"(pnl_medio={pnl_grid:.3f}) -- no se promociona sin "
                                      "corroboración",
                            "detalle_propio": detalle,
                        },
                    }
                return {
                    "veredicto": "bueno_confirmado",
                    "detalle": {
                        "origen": "validacion_externa_05ago",
                        "motivo": f"py en [{lo:.2f},{hi:.2f}), validado con fuente externa "
                                  "(ballenas_timing_history/franja_milimetrica_ballenas/"
                                  "punto_confirmacion) mientras el dato propio madura "
                                  "(confluencia suave: grid no contradice)",
                        "detalle_propio": detalle,
                    },
                }

    # 31-Ago: extensión de PROMOCIÓN a bueno_confirmado vía consenso
    # CONDICIONAL de bot wallets (Candidata 9, bot_consenso_gate_momentum_
    # ballena.json) -- distinta de las 2 extensiones de arriba porque no
    # depende solo de (tupla_str, py): el edge de bot_consenso solo existe
    # cuando el consenso de bots COINCIDE con la dirección de nuestra
    # señal (bucket "discrepa" es un régimen distinto, con su propio
    # veredicto independiente). Sin flag de activación separado, mismo
    # criterio que validacion_externa_05ago -- solo promueve, nunca
    # degrada, y pasa igualmente por _veto_fillable() en evaluar_sin_
    # override(). Requiere bot_consenso_lado (opcional, ver evaluar()) --
    # si el caller no lo pasa, esta rama simplemente no aplica, cero
    # cambio de comportamiento. Hoy solo cubre MOMENTUM_IBS_5M_BALLENA
    # (tupla pausada, fuera de pares_permitidos_live) -- diseñado y
    # conectado por adelantado para cuando se reactive, ver pendiente #1
    # de project_checkpoint_sesion_31ago_dashboard_walletmirror.
    #
    # LIMITACIÓN CONOCIDA (/code-review 31-Ago, no bloqueante -- mismo
    # espíritu que la limitación ya documentada en _veto_fillable() para
    # zonas_finas): _veto_fillable() (más abajo en evaluar_sin_override())
    # contrasta esta promoción contra gate_bucket_propio_fillable.json, que
    # mide fill-ability sobre la población AGREGADA del bucket (coincide +
    # discrepa mezclados), no sobre el subconjunto exacto que produjo este
    # veredicto. Hoy degrada correctamente ambas celdas bueno_confirmado
    # existentes (payout inverso real, g_kelly_f10<0, verificado a mano) --
    # pero eso es coincidencia empírica, no garantía estructural: en teoría
    # podría dejar pasar una promoción con población agregada sana pero
    # subconjunto coincide/discrepa realmente adverso, o vetar una buena por
    # ruido del otro subconjunto. No construir el fillable desagregado por
    # coincide/discrepa hasta que MOMENTUM_IBS_5M_BALLENA esté cerca de
    # reactivarse -- prematuro mientras la tupla siga pausada.
    if veredicto_propio == "sin_concluir" and bot_consenso_lado:
        coincide = _bot_consenso_coincide(tupla_str, bot_consenso_lado)
        if coincide is not None:
            entrada = _cargar_bot_consenso().get(tupla_str, {}).get(b_str, {}).get(
                "coincide" if coincide else "discrepa")
            if entrada and entrada.get("veredicto") == "bueno_confirmado":
                # 01-Sep: confluencia suave, mismo patrón que las 2 ramas
                # de arriba -- bot_consenso puede seguir promocionando en
                # solitario, pero no si el propio grid, en este bucket
                # exacto, ya apunta en contra.
                n_grid = (detalle or {}).get("n") or 0
                pnl_grid = (detalle or {}).get("pnl_medio")
                if pnl_grid is not None and n_grid >= _FILLABLE_N_MIN and pnl_grid < 0:
                    return {
                        "veredicto": "sin_concluir",
                        "detalle": {
                            "origen": "confluencia_suave_01sep",
                            "motivo": f"bot_consenso confirma pero el grid en {b_str} "
                                      f"(n={n_grid}) ya apunta en contra "
                                      f"(pnl_medio={pnl_grid:.3f}) -- no se promociona sin "
                                      "corroboración",
                            "detalle_propio": detalle,
                        },
                    }
                return {
                    "veredicto": "bueno_confirmado",
                    "detalle": {
                        "origen": "bot_consenso_gate_momentum_ballena_31ago",
                        "motivo": f"bot_consenso_lado={bot_consenso_lado} "
                                  f"({'coincide' if coincide else 'discrepa'} con la dirección), "
                                  f"n={entrada.get('n')} pnl/tr={entrada.get('pnl_medio')} "
                                  f"p={entrada.get('p_binomial')} "
                                  "(confluencia suave: grid no contradice)",
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
