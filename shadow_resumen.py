"""
shadow_resumen.py — genera data/shadow/estado_actual.md tras cada ciclo fast.

Visible en GitHub en tiempo real. Muestra:
  - Bankroll actual vs inicial (20€ operativo / 30€ depósito)
  - P&L del día y acumulado por estrategia con IC, Kelly, apuesta actual
  - Últimas 5 resoluciones
  - Señales abiertas pendientes

También envía un resumen compacto por Telegram cada TELEGRAM_INTERVALO_MIN minutos.
"""
import csv
import io
import json
import glob
import os
import time
import requests as _requests
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from pathlib import Path

from data_quality import leer_estado_calidad
from csv_lectura_tolerante import leer_csv_tolerante


_MADRID = ZoneInfo("Europe/Madrid")


def _cerrado_hoy_madrid(ts_utc, ahora_utc):
    """True si close_timestamp (ISO UTC) cae en el mismo día Madrid que ahora.
    Mismo criterio de día que live_balance.pnl_hoy_real: antes se comparaba en
    UTC y un trade cerrado 23:50Z (=01:50 Madrid) salía "0 cerrados hoy" con su
    PnL ya contado en "PnL hoy" (20-Sep)."""
    try:
        t = datetime.fromisoformat((ts_utc or "").replace("Z", "+00:00"))
        if t.tzinfo is None:
            t = t.replace(tzinfo=timezone.utc)
        return t.astimezone(_MADRID).date() == ahora_utc.astimezone(_MADRID).date()
    except Exception:
        return False

DIR_SHADOW   = Path("data/shadow")
RESULTS_PATH = DIR_SHADOW / "results.csv"
PARAMS_PATH  = DIR_SHADOW / "strategy_params.json"
OUTPUT_MD    = DIR_SHADOW / "estado_actual.md"
LAST_TG_PATH = DIR_SHADOW / "_last_telegram_update.ts"
CACHE_INCREMENTAL_PATH = DIR_SHADOW / "_cache_resumen_incremental.json"

TELEGRAM_INTERVALO_MIN = 60   # enviar resumen cada N minutos

CAPITAL_OPERATIVO = 25.44   # depósito real operativo (actualizado 2026-06-30)
DEPOSITO_TOTAL    = 30.0
RESERVA           = 4.56

# 23-Sep: días de resueltos a mantener en el índice rodante que alimenta
# "abiertas" (señales pendientes) -- solo hace falta cubrir las predicciones
# vivas en archivos_pred ([-2:] días de predictions_*.csv), 4 días da margen
# de sobra sin arrastrar historial completo.
RESUELTOS_VENTANA_DIAS = 4

# 23-Sep (/code-review, 9ª pasada): tope duro absoluto de resueltos_recientes,
# independiente de la poda por fecha -- red de seguridad si algún día
# prediction_timestamp viniera roto en masa (con _es_reciente en fail-open,
# una fila ilegible ya NO se excluye de la poda por fecha, así que sin este
# tope el crecimiento volvería a ser sin límite en ese escenario).
RESUELTOS_HARD_CAP = 20000

# 23-Sep (/code-review, hallazgo #2): tope por estrategia base del historial
# cronológico que alimenta _tendencia() -- sin esto crecía sin límite y se
# serializaba entero en JSON cada ciclo, reintroduciendo el mismo coste
# O(n_total)/ciclo que este rediseño existe para eliminar. 1000 da hasta
# 500/500 en el split-half, de sobra por encima del mínimo n>=30 que exige
# _tendencia() -- cambia la semántica de "tendencia de toda la vida" a
# "tendencia reciente" (últimas 1000 resoluciones), aviso explícito, no
# silencioso.
CRONOLOGICO_MAX_POR_BASE = 1000

# 23-Sep (/code-review, 4ª pasada): tamaño de chunk para la lectura binaria
# incremental -- evita materializar de golpe TODO el bloque pendiente en una
# reconstrucción en frío (cache borrado/corrupto, deploy nuevo, header
# cambiado), que sería tan grande como results.csv completo (cientos de MB).
CHUNK_BYTES = 8 * 1024 * 1024

# 23-Sep (/code-review, 7ª pasada): techo de escalada para _corte_seguro
# cuando un chunk no tiene ningún '\n' fuera de comillas -- cubre un campo
# citado legítimo grande sin volver a arriesgar el patrón de OOM (64MB sigue
# siendo muy por debajo del fichero completo, 587MB+). Si ni así se
# encuentra un corte seguro, se asume fila corrupta y se fuerza un corte
# crudo (ver aviso "🚨🚨 sin cierre de comillas").
CORTE_SEGURO_MAX_BYTES = 8 * CHUNK_BYTES


def _cache_incremental_vacio():
    return {
        "byte_offset": 0,
        "pnl_total": 0.0,
        "pnl_fiel_total": 0.0,
        "n_total": 0,
        "n_win": 0,
        "pnl_hoy_fecha": "",
        "pnl_hoy_sum": 0.0,
        "por_base": {},   # {strategy: {n, win, pnl, cronologico:[[ts,acierto],...]}}
        "ultimas": [],    # últimas N filas crudas (campos mínimos), más reciente al final
        "resueltos_recientes": [],  # [[prediction_timestamp, strategy, market_id], ...]
    }


def _cargar_cache_incremental() -> dict:
    """Fail-open: cualquier problema (fichero ausente/corrupto, offset mayor
    que el tamaño real de results.csv -- teóricamente imposible bajo el
    invariante APPEND-ONLY verificado con grep, pero un cache corrupto/
    manipulado a mano sí podría guardar un offset inválido) -> cache vacío,
    se reconstruye entero en el siguiente ciclo (mismo criterio que
    _idx_pred_archivo_cacheado en shadow_postmortem.py)."""
    try:
        cache = json.loads(CACHE_INCREMENTAL_PATH.read_text(encoding="utf-8"))
        tam_actual = RESULTS_PATH.stat().st_size if RESULTS_PATH.exists() else 0
        if cache.get("byte_offset", 0) > tam_actual:
            return _cache_incremental_vacio()
        return cache
    except Exception:
        return _cache_incremental_vacio()


def _guardar_cache_incremental(cache: dict) -> None:
    try:
        tmp = CACHE_INCREMENTAL_PATH.with_suffix(".tmp.json")
        tmp.write_text(json.dumps(cache), encoding="utf-8")
        os.replace(tmp, CACHE_INCREMENTAL_PATH)
    except Exception as e:
        print(f"  [aviso cache_resumen] no se pudo escribir cache: {e}")


def _corte_seguro(chunk: bytes) -> int:
    """Índice del último '\\n' en `chunk` que NO cae dentro de un campo CSV
    entrecomillado (ver /code-review 23-Sep, 5ª pasada, en el docstring de
    _actualizar_cache_incremental). -1 si no hay ningún corte seguro."""
    pos = chunk.rfind(b"\n")
    while pos != -1:
        if chunk[:pos + 1].count(b'"') % 2 == 0:
            return pos
        pos = chunk.rfind(b"\n", 0, pos)
    return -1


def _actualizar_cache_incremental(hoy: str, ahora: datetime) -> dict:
    """23-Sep (rediseño, causa raíz de 14 OOM-kills/24h -- ver
    project_rediseno_shadow_resumen_prioritario_23sep): antes, main() hacía
    `resultados = list(csv.DictReader(...))` de TODO results.csv (666k filas,
    560MB+) en CADA ciclo (~20-60s vía run_fast_mantenimiento.sh), materializando
    ~1,5GB de dicts Python que competían por RAM con live_trade.py/shadow_
    resumen.py mismos, disparando el OOM-killer del kernel. results.csv es
    estrictamente APPEND-ONLY (mismo invariante que shadow_resolve.py:414
    documenta y explota tras verificar con grep que ningún script lo abre en
    modo escritura no-append -- no existe ningún proceso de dedup/reescritura
    real sobre este fichero, verificado antes de escribir esto) -- este cache
    guarda un offset de bytes + agregados
    ya reducidos (sumas/contadores, nunca la fila cruda completa salvo
    `ultimas`/`resueltos_recientes`, ambos acotados) y en cada ciclo solo
    parsea las líneas NUEVAS desde el offset, actualizando los agregados in
    situ. Coste por ciclo pasa de O(n_total) a O(filas_nuevas) -- normalmente
    0-5 filas entre ciclos de 20-60s.

    /code-review 23-Sep, 2 hallazgos corregidos:
    (1) leer en modo texto y calcular `len(linea.encode('utf-8'))` para el
    offset desincroniza si el fichero tiene CRLF (confirmado real en
    results.csv) -- universal-newline strippea el '\\r' antes de medir,
    subcontando 1 byte/línea, y el offset guardado deja de apuntar a un
    límite de línea real. Mismo bug que shadow_resolve.py ya evita abriendo
    en 'rb' y calculando el offset sobre bytes crudos -- se replica ese
    patrón aquí en vez de reinventar uno nuevo (decisión ladder CLAUDE.md).
    (2) `cronologico` sin tope crecía para siempre y se serializaba/
    deserializaba en JSON cada ciclo -- volvía a ser O(n_total) por ciclo
    (ahora vía JSON, no vía CSV), el mismo patrón que este cambio existe
    para eliminar. Acotado a CRONOLOGICO_MAX_POR_BASE por estrategia
    (recorte por delante, se queda con las más recientes) -- sigue siendo
    ampliamente suficiente para el split-half de _tendencia() (exige n>=30,
    aquí quedan hasta 1000/500-500), pero cambia su semántica de "primera
    mitad de TODO el historial vs segunda mitad" a "primera mitad de las
    últimas 1000 vs segunda mitad" -- tendencia reciente, no de toda la
    vida. Aviso explícito para Javi, no un cambio silencioso.

    /code-review 23-Sep (2ª pasada), 3 hallazgos más corregidos:
    (1) `fieldnames` cacheado nunca se revalidaba contra la cabecera ACTUAL
    del fichero -- si results.csv ganara/reordenara una columna con
    offset>0, csv.DictReader seguiría zipeando con el orden viejo sin
    lanzar ningún error (silenciosamente mal, el caso exacto que CLAUDE.md
    pide parar y surfacear). shadow_resolve.py, el patrón que este código
    dice replicar, SÍ relee la cabecera cada vez y invalida su caché si no
    coincide -- aquí faltaba ese paso, añadido ahora (header_actual se lee
    siempre, barato, una sola línea).
    (2) import de `_pnl_realista` movido fuera del bucle -- estaba dentro,
    ejecutándose una vez por fila (irrelevante en ciclos normales de 0-5
    filas nuevas, pero carísimo en la reconstrucción inicial de 666k filas)."""
    cache = _cargar_cache_incremental()
    cache_modificado = False
    if cache.get("pnl_hoy_fecha") != hoy:
        cache["pnl_hoy_fecha"] = hoy
        cache["pnl_hoy_sum"] = 0.0
        # /code-review 23-Sep (7ª pasada): sin este reseteo diario,
        # filas_corruptas/pnl_fiel_errores eran contadores DE TODA LA VIDA --
        # una sola fila mala de hace meses seguiría mostrando "⚠️ 1 fila(s)
        # corrupta(s)" en el markdown/Telegram para siempre, sin poder saber
        # si el problema es de hoy o arqueología. El aviso por print() en el
        # momento del fallo (va a logs/fast.log) sigue siendo permanente y
        # correcto -- este contador es solo el indicador "¿hoy hay algo roto?".
        cache["filas_corruptas"] = 0
        cache["pnl_fiel_errores"] = 0
        cache_modificado = True

    if not RESULTS_PATH.exists():
        return cache

    size_actual = RESULTS_PATH.stat().st_size
    offset_inicial = cache.get("byte_offset", 0)
    offset = offset_inicial
    fieldnames = cache.get("fieldnames")

    # /code-review 23-Sep (2ª pasada): releer SIEMPRE la cabecera actual (una
    # línea, barato) y compararla contra la cacheada -- mismo patrón exacto
    # que shadow_resolve.py::cargar_ya_resueltas (header_previo==header_actual)
    # para el mismo invariante. Sin esto, si results.csv ganara/reordenara una
    # columna con offset>0, csv.DictReader seguiría zipeando contra el orden
    # viejo sin lanzar ningún error -- mal silenciosamente, nunca detectado.
    with open(RESULTS_PATH, "rb") as f:
        header_bytes = f.readline()
    if not header_bytes:
        return cache
    fieldnames_actual = next(csv.reader([header_bytes.decode("utf-8", errors="replace")]))

    cache_invalido = (
        (offset > 0 and not fieldnames)
        or (offset > 0 and fieldnames != fieldnames_actual)
    )
    if cache_invalido:
        # Cache no fiable (formato viejo/corrupto, o el header cambió de
        # verdad) -- reconstruir desde cero en vez de arriesgar un doble
        # conteo o columnas desplazadas. Mismo criterio que
        # _cargar_cache_incremental cuando byte_offset > tamaño del fichero.
        # /code-review 23-Sep (3ª pasada): _cache_incremental_vacio() resetea
        # pnl_hoy_fecha a "" -- sin re-ponerlo a `hoy` aquí, main() reportaría
        # pnl_hoy=0.0 este ciclo Y el siguiente (el check de arriba, "" != hoy,
        # volvería a disparar y pisar pnl_hoy_sum ANTES de que este mismo
        # ciclo termine de reconstruirlo), perdiendo silenciosamente el PnL
        # de hoy en el dashboard/Telegram hasta el cambio de día.
        cache = _cache_incremental_vacio()
        cache["pnl_hoy_fecha"] = hoy
        offset = 0
        cache_modificado = True

    por_base = cache.setdefault("por_base", {})
    ultimas = cache.setdefault("ultimas", [])
    resueltos = cache.setdefault("resueltos_recientes", [])

    if offset == 0:
        fieldnames = fieldnames_actual
        offset = len(header_bytes)
        cache["fieldnames"] = fieldnames

    def _es_reciente(ts_pred: str, cutoff: float) -> bool:
        """/code-review 23-Sep (9ª pasada, revierte la 6ª): fail-OPEN (True)
        de nuevo -- la 6ª pasada lo puso en fail-closed para evitar fuga de
        memoria con timestamps ilegibles, pero eso introdujo una regresión
        real: una fila YA resuelta con prediction_timestamp roto se excluía
        de resueltos_recientes PARA SIEMPRE (el offset ya avanzó sobre ella,
        no se puede reprocesar) y `abiertas` la mostraba como "señal abierta"
        indefinidamente aunque ya estuviera cerrada -- el código viejo (match
        por tupla exacta, sin fecha) nunca tenía este problema. La fuga de
        memoria real se corta ahora con RESUELTOS_HARD_CAP (tope duro por
        cantidad, no por fecha) como red de seguridad -- las dos cosas a la
        vez: no se pierde información por incertidumbre, y no puede crecer
        sin límite aunque las fechas vengan todas rotas."""
        try:
            t = datetime.fromisoformat((ts_pred or "").replace("Z", "+00:00"))
            if t.tzinfo is None:
                t = t.replace(tzinfo=timezone.utc)
            return t.timestamp() >= cutoff
        except Exception:
            return True

    def _podar_resueltos(lista: list) -> list:
        """Filtro por fecha + tope duro (RESUELTOS_HARD_CAP) -- devuelve una
        lista NUEVA, nunca muta `lista` in situ. /code-review 23-Sep (9ª
        pasada): el checkpoint periódico reasignaba `cache["resueltos_
        recientes"]` a esta lista podada pero NUNCA reasignaba la variable
        local `resueltos` que el bucle sigue usando para `.append()` --
        durante una reconstrucción en frío, `resueltos` crecía sin límite
        real (666k+ filas) pese a que el checkpoint "parecía" podarlo. Ahora
        el resultado de esta función se reasigna a AMBOS."""
        podada = [x for x in lista if _es_reciente(x[0], cutoff)]
        if len(podada) > RESUELTOS_HARD_CAP:
            podada = podada[-RESUELTOS_HARD_CAP:]
        return podada

    # /code-review 23-Sep (8ª pasada): un único `cutoff`, calculado una vez
    # aquí (antes había un `cutoff_final` redundante al final del todo,
    # recalculado a partir de los mismos `ahora`/RESUELTOS_VENTANA_DIAS que
    # nunca cambian dentro de esta llamada -- siempre daba el mismo valor).
    cutoff = ahora.timestamp() - RESUELTOS_VENTANA_DIAS * 86400

    if offset < size_actual:
        from dashboard_server import _pnl_realista  # /code-review: fuera del bucle, no por fila
        # /code-review 23-Sep (4ª pasada), 3 hallazgos de "reconstrucción en
        # frío" corregidos (deploy nuevo, cache borrado/corrupto, o header
        # cambiado -- offset=0 sobre 666k+ filas):
        # (1) `f.read(size_actual - offset)` de una sola vez volvía a
        # materializar el fichero pendiente ENTERO (cientos de MB) -- el
        # mismo patrón de OOM que este rediseño existe para eliminar, solo
        # que en la reconstrucción en frío en vez de en cada ciclo normal.
        # Ahora se lee en CHUNK_BYTES trozos, nunca más de eso en memoria.
        # /code-review 23-Sep (6ª pasada): checkpoint periódico durante una
        # reconstrucción en frío (666k+ filas puede tardar bastante) -- sin
        # esto, un kill a mitad de camino (watchdog, OOM en otro proceso,
        # deploy) perdía TODO el progreso y volvía a empezar desde 0, mismo
        # patrón "pasada larga sin puntos de control" que el incidente de
        # shadow_postmortem.py que motivó este rediseño.
        CHECKPOINT_INTERVAL_S = 5
        t_ultimo_checkpoint = time.time()
        with open(RESULTS_PATH, "rb") as f:
            f.seek(offset)
            pos = offset
            while pos < size_actual:
                chunk = f.read(min(CHUNK_BYTES, size_actual - pos))
                if not chunk:
                    break
                # /code-review 23-Sep (5ª pasada): cortar en el último '\n'
                # crudo no es CSV-aware -- si algún campo (ej. `question`)
                # tuviera algún día un salto de línea embebido dentro de
                # comillas, el corte partiría ese campo en dos filas mal
                # formadas sin lanzar ninguna excepción (comprobado hoy:
                # results.csv no tiene ninguna fila así, pero nada impide que
                # aparezca en el futuro). _corte_seguro cuenta comillas dobles
                # hasta cada candidato a '\n' -- un conteo impar significa que
                # ese salto cae DENTRO de un campo citado, y retrocede al
                # anterior.
                #
                # /code-review 23-Sep (7ª pasada): esta misma heurística
                # puede quedarse en LIVELOCK PERMANENTE si una fila queda
                # truncada con un número impar de comillas -- ej. shadow_
                # resolve.py matado a mitad de un writerow() (el propio
                # incidente de OOM-kills que motivó este rediseño). Sin
                # escape, _corte_seguro devolvería -1 para siempre y el
                # offset nunca volvería a avanzar, en silencio. Escalada
                # acotada: si no hay corte seguro, ampliar la ventana leída
                # hasta CORTE_SEGURO_MAX_BYTES: si un campo citado legítimo
                # cierra ahí, se recupera solo; si no cierra nunca (fila
                # realmente corrupta), se rinde y fuerza un corte crudo
                # (ignora comillas) gritando el problema -- Fail Loud en vez
                # de congelarse silenciosamente.
                ultimo_nl = _corte_seguro(chunk)
                bloque_forzado = False
                while ultimo_nl == -1 and pos + len(chunk) < size_actual \
                        and len(chunk) < CORTE_SEGURO_MAX_BYTES:
                    extra = f.read(min(CHUNK_BYTES, size_actual - pos - len(chunk),
                                        CORTE_SEGURO_MAX_BYTES - len(chunk)))
                    if not extra:
                        break
                    chunk += extra
                    ultimo_nl = _corte_seguro(chunk)
                if ultimo_nl == -1:
                    ultimo_nl_crudo = chunk.rfind(b"\n")
                    if ultimo_nl_crudo == -1:
                        # de verdad ni una línea completa (chunk pequeño al
                        # final del fichero) -- se deja para el próximo ciclo.
                        break
                    cache["cortes_forzados"] = cache.get("cortes_forzados", 0) + 1
                    print(f"  🚨🚨 [cache_resumen] sin cierre de comillas tras {len(chunk)} "
                          f"bytes en offset={pos} -- posible fila corrupta en results.csv "
                          f"(revisar a mano). Usando corte crudo para no bloquear el resto "
                          f"del historial para siempre.")
                    ultimo_nl = ultimo_nl_crudo
                    # /code-review 23-Sep (9ª pasada): un corte crudo puede
                    # desalinear columnas de las filas de ESTE bloque sin que
                    # csv.DictReader ni el try/except de acierto/pnl_neto lo
                    # detecten (si el valor desplazado por casualidad castea
                    # a int/float, se suma a pnl_total/n_total EN SILENCIO --
                    # envenenamiento de datos, no solo pérdida de fila). Se
                    # marcan TODAS las filas de este bloque como sospechosas
                    # en filas_corruptas -- se siguen contando (mejor esfuerzo,
                    # no se descarta el bloque entero), pero queda visible.
                    bloque_forzado = True
                texto_util = chunk[:ultimo_nl + 1]
                texto = texto_util.decode("utf-8", errors="replace")
                for r in csv.DictReader(io.StringIO(texto), fieldnames=fieldnames):
                    if bloque_forzado:
                        cache["filas_corruptas"] = cache.get("filas_corruptas", 0) + 1
                    strat = r.get("strategy", "?")
                    sub   = r.get("subtype", "")
                    # Una fila con acierto/pnl_neto ilegible se descarta para
                    # siempre (el offset ya avanzó sobre sus bytes, no se
                    # puede reprocesar) -- el código viejo, en cambio, hacía
                    # crashear TODO el script con esa misma fila (Fail Loud).
                    # Aquí no se puede reproducir ese crash sin tirar abajo
                    # el resumen/Telegram en cada ciclo hasta que alguien
                    # arregle la fila a mano, así que en su lugar se cuenta y
                    # se grita por print (va a logs/fast.log, visible) --
                    # "silencioso" es lo prohibido, no "no crashea".
                    try:
                        acierto = int(r.get("acierto", 0) or 0)
                        pnl = float(r.get("pnl_neto", 0) or 0)
                    except Exception as e:
                        cache["filas_corruptas"] = cache.get("filas_corruptas", 0) + 1
                        print(f"  🚨 [cache_resumen] fila descartada (acierto/pnl_neto ilegible): "
                              f"{type(e).__name__}: {e} -- strategy={strat} market_id={r.get('market_id','')}")
                        continue
                    ts_res = r.get("resolution_timestamp", "") or ""

                    cache["pnl_total"] = cache.get("pnl_total", 0.0) + pnl
                    cache["n_total"] = cache.get("n_total", 0) + 1
                    cache["n_win"] = cache.get("n_win", 0) + acierto
                    if ts_res[:10] == hoy:
                        cache["pnl_hoy_sum"] = cache.get("pnl_hoy_sum", 0.0) + pnl

                    try:
                        v_fiel = _pnl_realista(r)
                        if v_fiel is not None:
                            cache["pnl_fiel_total"] = cache.get("pnl_fiel_total", 0.0) + v_fiel
                    except Exception as e:
                        # Antes un fallo aquí tumbaba TODO el cálculo de
                        # pnl_fiel (try/except envolvía el sum() completo) y
                        # el markdown mostraba "⚠️ error" -- visible. Ahora es
                        # por fila, así que hay que gritarlo explícito en vez
                        # de tragárselo -- se cuenta en el cache (visible en
                        # el propio JSON) y se imprime, no en silencio.
                        cache["pnl_fiel_errores"] = cache.get("pnl_fiel_errores", 0) + 1
                        print(f"  🚨 [cache_resumen] _pnl_realista() falló en una fila: "
                              f"{type(e).__name__}: {e} -- strategy={strat} market_id={r.get('market_id','')}")

                    base = por_base.setdefault(strat, {"n": 0, "win": 0, "pnl": 0.0, "cronologico": []})
                    base["n"] += 1
                    base["win"] += acierto
                    base["pnl"] += pnl
                    base["cronologico"].append([ts_res, acierto])
                    # (2) recorte por lotes, no fila a fila: `del lista[:-N]`
                    # es O(len) -- recortar en cada fila una vez superado el
                    # tope convierte una reconstrucción en frío (100k+ filas
                    # en una sola estrategia) en decenas de millones de
                    # desplazamientos de lista. Se deja crecer hasta 2x el
                    # tope y ENTONCES se recorta de golpe -- mismo resultado
                    # final, coste amortizado.
                    if len(base["cronologico"]) > CRONOLOGICO_MAX_POR_BASE * 2:
                        del base["cronologico"][:-CRONOLOGICO_MAX_POR_BASE]

                    ultimas.append({
                        "resolution_timestamp": ts_res, "strategy": strat, "subtype": sub,
                        "question": r.get("question", ""), "acierto": r.get("acierto", "0"),
                        "pnl_neto": r.get("pnl_neto", "0"),
                    })
                    del ultimas[:-5]

                    # (3) filtrar por recencia AQUÍ, antes de acumular -- no
                    # después de haber acumulado las 666k+ filas de una
                    # reconstrucción en frío y podar al final (memoria
                    # transitoria O(n_total) que el resto de este rediseño
                    # evita expresamente).
                    ts_pred = r.get("prediction_timestamp", "")
                    if _es_reciente(ts_pred, cutoff):
                        resueltos.append([ts_pred, strat, r.get("market_id", "")])

                pos += len(texto_util)
                f.seek(pos)
                if time.time() - t_ultimo_checkpoint >= CHECKPOINT_INTERVAL_S:
                    resueltos = _podar_resueltos(resueltos)
                    cache["byte_offset"] = pos
                    cache["resueltos_recientes"] = resueltos
                    _guardar_cache_incremental(cache)
                    t_ultimo_checkpoint = time.time()
            offset = pos

    cache["byte_offset"] = offset
    cache["resueltos_recientes"] = _podar_resueltos(resueltos)

    # /code-review 23-Sep (8ª pasada): guardar solo si algo cambió de verdad
    # -- antes se reescribía el cache ENTERO (ya ~6MB reales: 54 estrategias
    # x hasta 1000 cronologico + resueltos_recientes) en CADA ciclo de
    # 20-60s aunque no hubiera ni una fila nueva (el caso normal), ~26GB/día
    # de I/O de escritura evitable. `cache_modificado` cubre rollover de día/
    # invalidación; `offset != offset_inicial` cubre filas nuevas procesadas.
    if cache_modificado or offset != offset_inicial:
        _guardar_cache_incremental(cache)
    return cache


def cargar_params():
    if not PARAMS_PATH.exists():
        return {}
    with open(PARAMS_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("estrategias", {})


def main():
    ahora = datetime.now(timezone.utc)
    hoy   = ahora.strftime("%Y-%m-%d")

    # 23-Sep: cache incremental en vez de `resultados = cargar_csv(RESULTS_PATH)`
    # (todo el histórico, 666k+ filas, ~1,5GB de dicts en CADA ciclo de 20-60s --
    # causa raíz de 14 OOM-kills/24h, ver _actualizar_cache_incremental()).
    # `por_strat` y `_stats_directas()` (más abajo en el fichero) se
    # calculaban pero nunca se consumían -- dead code eliminado junto con
    # este cambio, no arrastrado al cache.
    cache      = _actualizar_cache_incremental(hoy, ahora)
    params     = cargar_params()

    # ── Bankroll ──────────────────────────────────────────────────────────────
    pnl_total = cache["pnl_total"]
    bankroll  = CAPITAL_OPERATIVO + pnl_total
    roi_op    = pnl_total / CAPITAL_OPERATIVO * 100
    roi_dep   = pnl_total / DEPOSITO_TOTAL    * 100

    # P&L del día de hoy (ya acotado a `hoy` dentro del cache)
    pnl_hoy = cache["pnl_hoy_sum"] if cache.get("pnl_hoy_fecha") == hoy else 0.0

    # Agrupado a nivel estrategia base (ya acumulado incrementalmente)
    por_base = cache["por_base"]

    # ── Últimas 5 resoluciones ────────────────────────────────────────────────
    ultimas = cache["ultimas"]

    # ── Señales abiertas (predicciones no resueltas) ──────────────────────────
    # Ventana rodante (RESUELTOS_VENTANA_DIAS) en vez de todo el histórico --
    # archivos_pred solo mira los últimos 2 días de predictions_*.csv, así
    # que una resolución de hace semanas nunca puede casar con nada de ahí.
    resueltos_ids = set(tuple(x) for x in cache["resueltos_recientes"])
    # 18-Ago: lectura tolerante por FICHERO -- mismo fix que shadow_resolve.py::
    # cargar_predicciones_pendientes()/shadow_postmortem.py::
    # cargar_predicciones_index(), mismo motivo (shadow_predict.py, proceso
    # independiente desde el desacoplo de run_fast_mantenimiento.sh, puede
    # estar a mitad de un predictions_HOY.csv.write() justo cuando este
    # proceso lo lee). csv_lectura_tolerante reintenta una vez tras 0.5s
    # antes de saltar el fichero y reportarlo como fallo persistente (no
    # silenciado para siempre como "probable concurrencia").
    archivos_pred = sorted(glob.glob(str(DIR_SHADOW / "predictions_*.csv")))[-2:]
    abiertas = 0

    def _contar_abiertas(arch: Path) -> int:
        n = 0
        with open(arch, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("decision","") not in ("BUY_YES","BUY_NO"):
                    continue
                clave = (row.get("timestamp_utc",""), row.get("strategy",""), row.get("market_id",""))
                if clave not in resueltos_ids:
                    n += 1
        return n

    for arch in archivos_pred:
        n_arch = leer_csv_tolerante(Path(arch), _contar_abiertas, log_fn=print)
        if n_arch:
            abiertas += n_arch

    # ── Construir Markdown ────────────────────────────────────────────────────
    ts = ahora.strftime("%Y-%m-%d %H:%M UTC")
    n_total = cache["n_total"]
    n_win   = cache["n_win"]
    wr_g    = n_win / n_total * 100 if n_total else 0

    signo_pnl    = "+" if pnl_total >= 0 else ""
    signo_hoy    = "+" if pnl_hoy   >= 0 else ""
    emoji_roi    = "🟢" if pnl_total >= 0 else "🔴"
    emoji_hoy    = "🟢" if pnl_hoy   >= 0 else "🔴"

    # ── Live real on-chain (mismo origen que dashboard/digest/Telegram) ──────
    try:
        from live_balance import cargar_balance_real
        snap = cargar_balance_real(max_edad_s=3600)
    except Exception:
        snap = None
    if snap and not snap.get("_rancio"):
        em_live = "🟢" if snap["pnl_real"] >= 0 else "🔴"
        hoy_r = snap.get("pnl_hoy_real")
        d7_r  = snap.get("pnl_7d_real")
        live_rows = [
            f"| Total depositado | {snap['deposito_inicial']:.2f} $ |",
            f"| Balance on-chain | **{snap['total']:.2f} $** |",
            f"| P&L real total | {em_live} **{snap['pnl_real']:+.2f} $** |",
        ]
        if hoy_r is not None:
            live_rows.append(f"| P&L real hoy | {hoy_r:+.2f} $ |")
        if d7_r is not None:
            live_rows.append(f"| P&L real 7 días | {d7_r:+.2f} $ |")
    else:
        live_rows = ["| ⚠️ | Sin snapshot on-chain fresco (live_balance.py, cron 15min) |"]

    # Fees reales pagados (fix 08-Jul) -- coste de Polymarket antes invisible,
    # cobrado solo al comprar. Mismo trades.csv que dashboard/Telegram.
    try:
        trades_csv_md = Path("data/live/trades.csv")
        if trades_csv_md.exists() and trades_csv_md.stat().st_size > 100:
            cerrados_md = [r for r in csv.DictReader(open(trades_csv_md, encoding="utf-8"))
                          if r.get("status") == "CLOSED"]
            fees_md = sum(float(r.get("fee_eur") or 0) for r in cerrados_md)
            live_rows.append(f"| Fees pagados (real) | {fees_md:.2f} $ |")
    except Exception:
        pass

    # PnL fiel: stake fijo 1$ + slippage, sin compounding — misma función que el
    # dashboard. Cota superior: no modela fill-ability (~8%, selección adversa).
    # 23-Sep: acumulado incrementalmente dentro de _actualizar_cache_incremental
    # (misma _pnl_realista, sumada fila a fila conforme llegan, no en un solo
    # pase sobre todo el histórico).
    try:
        pnl_fiel = cache["pnl_fiel_total"]
        n_err_fiel = cache.get("pnl_fiel_errores", 0)
        n_err_filas = cache.get("filas_corruptas", 0)
        aviso = (f" ⚠️ {n_err_fiel} fila(s) con error" if n_err_fiel else "")
        aviso += (f" ⚠️ {n_err_filas} fila(s) corrupta(s)" if n_err_filas else "")
        fiel_row = f"| P&L fiel (stake fijo 1$) | {pnl_fiel:+.2f} $ {aviso}|"
    except Exception:
        fiel_row = "| P&L fiel (stake fijo 1$) | ⚠️ error |"

    lines = [
        f"# Estado del bot — {ts}",
        "",
        "## Live — dinero real (on-chain)",
        f"| | |",
        f"|---|---|",
    ] + live_rows + [
        "",
        "## Shadow — MODELO SIMULADO (no cobrable)",
        f"| | |",
        f"|---|---|",
        fiel_row,
        f"| P&L sim compuesto | {emoji_roi} {signo_pnl}{pnl_total:.2f} $ (ficción Kelly: {signo_pnl}{roi_op:.0f}% s/ operativo) |",
        f"| P&L sim hoy ({hoy}) | {emoji_hoy} {signo_hoy}{pnl_hoy:.2f} $ |",
        f"| Operaciones resueltas | {n_total} ({n_win} WIN / {n_total-n_win} LOSS) — {wr_g:.1f}% |",
        f"| Señales abiertas | {abiertas} |",
        "",
        "## Estrategias (visión global)",
        "",
        "| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |",
        "|---|---|---|---|---|---|---|---|",
    ]

    # Estrategias base ordenadas por PNL
    for s, d in sorted(por_base.items(), key=lambda x: x[1]["pnl"], reverse=True):
        n   = d["n"]
        wr  = d["win"] / n * 100 if n else 0
        pnl = d["pnl"]
        ic  = (d["win"] + 1) / (n + 2) - 0.5
        confianza = min(1.0, n / 20)
        ic_ef = ic * confianza
        tendencia = _tendencia(d["cronologico"])
        # /code-review 23-Sep (9ª pasada): CRONOLOGICO_MAX_POR_BASE cambia la
        # semántica de _tendencia() de "toda la vida" a "recientes" para
        # cualquier estrategia con n>tope -- antes ese aviso solo vivía en un
        # comentario de código que Javi nunca lee; ahora se ve en la propia
        # tabla, que es lo que de verdad se consulta cada sesión.
        if n > CRONOLOGICO_MAX_POR_BASE:
            tendencia += " (últ. 1000)"

        sp = params.get(s, {})
        activa = sp.get("activa", True)
        apuesta = sp.get("apuesta_kelly", 0.90)

        est_str = "✅ activa" if activa else "🚫 desactivada"
        if activa and n < 8:
            est_str = "⏳ acumulando"
        elif activa and ic_ef < 0:
            est_str = "⚠️ IC negativo"

        signo = "+" if pnl >= 0 else ""
        lines.append(
            f"| {s} | {n} | {wr:.1f}% | {ic_ef:+.3f} | {tendencia} | {signo}{pnl:.2f}$ | {apuesta:.2f}$ | {est_str} |"
        )

    lines += [
        "",
        "## Últimas 5 resoluciones",
        "",
        "| Timestamp | Estrategia | Mercado | Resultado | PNL |",
        "|---|---|---|---|---|",
    ]

    for r in reversed(ultimas):
        ts_r   = (r.get("resolution_timestamp","") or "")[:16]
        strat  = r.get("strategy","")
        sub    = r.get("subtype","")
        label  = f"{strat}#{sub}" if sub else strat
        q      = (r.get("question","") or "")[:50]
        acierto = r.get("acierto","0")
        emoji  = "✅ WIN" if acierto == "1" else "❌ LOSS"
        pnl_r  = float(r.get("pnl_neto", 0))
        signo_r = "+" if pnl_r >= 0 else ""
        lines.append(f"| {ts_r} | {label} | {q}… | {emoji} | {signo_r}{pnl_r:.2f}$ |")

    # ─── Sección calidad de datos ──────────────────────────────────────────
    dq = leer_estado_calidad()
    dq_ts   = dq.get("timestamp_utc", "")[:16]
    dq_glob = dq.get("estado_global", "DESCONOCIDO")
    dq_icon = {"OK": "✅", "DEGRADED": "⚠️", "CRITICAL": "🚨"}.get(dq_glob, "❓")
    rechazos = dq.get("rechazos_1h", {})

    dq_rows = []
    for sym, info in dq.get("assets", {}).items():
        ic_sym = {"OK": "✅", "DEGRADED": "⚠️", "CRITICAL": "🚨"}.get(info.get("estado"), "❓")
        age_s  = info.get("age_seconds")
        age_str = f"{age_s/60:.1f}min" if age_s is not None else "N/A"
        px     = info.get("ultimo_precio")
        px_str = f"${px:,.2f}" if px else "N/A"
        alertas = " ".join(info.get("alertas", []))
        dq_rows.append(f"| {ic_sym} {sym} | {px_str} | {age_str} | {alertas} |")

    lines += [
        "",
        "## Calidad de datos",
        "",
        f"{dq_icon} **{dq_glob}** — última verificación {dq_ts} UTC"
        + (f" | rechazos 1h: {rechazos.get('total',0)}"
           f" (rango={rechazos.get('rango',0)}, spike={rechazos.get('spike',0)})"
           if rechazos.get("total", 0) > 0 else ""),
    ]
    if dq_rows:
        lines += [
            "",
            "| Asset | Precio | Age | Alertas |",
            "|---|---|---|---|",
        ] + dq_rows

    # Cross-source si está disponible
    cross = dq.get("cross_source", {})
    if cross.get("fuentes_activas"):
        fuentes = ", ".join(cross["fuentes_activas"])
        consenso = cross.get("consenso", {})
        fe = cross.get("fuente_elegida", {}) if "fuente_elegida" in cross else {}
        cross_rows = []
        for sym, px in consenso.items():
            src = fe.get(sym, "consenso")
            div_str = ""
            for a in cross.get("alertas", []):
                if a["sym"] == sym:
                    div_str = f"⚠️ div {a['max_div_pct']:.2f}%"
            blk = "🚨 BLOQUEADO" if sym in cross.get("bloqueados", []) else ""
            cross_rows.append(f"| {sym} | ${px:,.2f} | {src} | {div_str}{blk} |")
        if cross_rows:
            lines += [
                "",
                f"**Cross-source** ({fuentes}):",
                "",
                "| Asset | Consenso | Fuente | Estado |",
                "|---|---|---|---|",
            ] + cross_rows

    alertas_dq = dq.get("alertas", [])
    if alertas_dq:
        lines.append("")
        lines.append("**Alertas activas:**")
        for a in alertas_dq[:5]:
            lines.append(f"- ⚠ {a}")

    lines += [
        "",
        "---",
        f"*Actualizado automáticamente cada ~60s por el fast loop*",
    ]

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"  [resumen] Bankroll={bankroll:.2f}€ PNL={signo_pnl}{pnl_total:.2f}€ "
          f"({signo_pnl}{roi_op:.1f}% op) | Hoy={signo_hoy}{pnl_hoy:.2f}€ | "
          f"n={n_total} wr={wr_g:.1f}% | abiertas={abiertas}")

    # Telegram periódico (solo LIVE, ver _telegram_periodico)
    _telegram_periodico(ahora)


def _ic_bayes(win, n):
    return ((win + 1) / (n + 2) - 0.5) * min(1.0, n / 20)


def _tendencia(cronologico):
    """Propuesta #5 (artículo breakout, 09-Jul, ver ic_rolling.py): split-half
    cronológico para ver si el edge MADURA o se AGOTA sin correr el script a
    mano. n<30 (o <15 por mitad) no concluye nada — mismo umbral que el resto
    del proyecto."""
    n = len(cronologico)
    if n < 30:
        return "—"
    ordenado = sorted(cronologico, key=lambda x: x[0])
    mid = n // 2
    primera, segunda = ordenado[:mid], ordenado[mid:]

    def ic(rows):
        wins = sum(a for _, a in rows)
        return (wins + 1) / (len(rows) + 2) - 0.5

    gap = ic(segunda) - ic(primera)
    if abs(gap) < 0.03:
        return "➡️ estable"
    return f"📈 madura ({gap:+.2f})" if gap > 0 else f"📉 agota ({gap:+.2f})"


def _esc(s):
    """Escapa _ y * para Markdown v1 de Telegram."""
    return s.replace('_', '\\_').replace('*', '\\*')


def _telegram_periodico(ahora):
    tok = os.environ.get("TELEGRAM_TOKEN", "")
    cid = os.environ.get("TELEGRAM_CHAT_ID", "")
    if not tok or not cid:
        return

    # Comprobar si toca enviar
    ahora_ts = ahora.timestamp()
    if LAST_TG_PATH.exists():
        try:
            ultimo = float(LAST_TG_PATH.read_text().strip())
            if ahora_ts - ultimo < TELEGRAM_INTERVALO_MIN * 60:
                return
        except Exception:
            pass

    # ── Estado live (switch + ventana) ───────────────────────────────────────
    try:
        from live_guard import estado_live
        est       = estado_live()
        switch_on = est["switch"]
        en_ventana = est["en_ventana"]
        # estado_live no expone 'proxima_ventana'; la próxima va dentro de motivo,
        # p.ej. "fuera_de_ventana (proxima: hoy 08:30)"
        if en_ventana:
            live_estado = f"✅ ON — en ventana"
        elif switch_on:
            live_estado = f"🟡 ON — {_esc(est.get('motivo', ''))}"
        else:
            live_estado = f"❌ OFF — {_esc(est.get('motivo', ''))}"
    except Exception as e:
        print(f"[shadow_resumen] excepción en estado_live(): {type(e).__name__}: {e}")
        live_estado = "? (error)"

    # ── Stats live: balance real on-chain (mismo origen que dashboard/digest) ─
    try:
        from live_balance import cargar_balance_real
        snap = cargar_balance_real(max_edad_s=3600)
    except Exception as e:
        print(f"[shadow_resumen] excepción cargando balance real: {type(e).__name__}: {e}")
        snap = None

    # WR y nº de trades reales desde trades.csv (métricas de actividad, no de saldo)
    trades_csv = Path("data/live/trades.csv")
    hoy = ahora.strftime("%Y-%m-%d")
    n_live_hoy = n_live_total = w_live_total = 0
    fees_total_live = 0.0
    try:
        if trades_csv.exists() and trades_csv.stat().st_size > 100:
            cerrados = [r for r in csv.DictReader(open(trades_csv, encoding="utf-8"))
                        if r.get("status") == "CLOSED"]
            n_live_total = len(cerrados)
            n_live_hoy   = sum(1 for r in cerrados
                               if _cerrado_hoy_madrid(r.get("close_timestamp", ""), ahora))
            w_live_total = sum(1 for r in cerrados
                               if float(r.get("pnl_neto_eur") or 0) > 0)
            # fees reales pagados (fix 08-Jul) -- coste de verdad, antes invisible
            fees_total_live = sum(float(r.get("fee_eur") or 0) for r in cerrados)
    except Exception as e:
        print(f"[shadow_resumen] excepción leyendo trades.csv: {type(e).__name__}: {e}")

    def _post(msg):
        _requests.post(
            f"https://api.telegram.org/bot{tok}/sendMessage",
            json={"chat_id": cid, "text": msg, "parse_mode": "Markdown"},
            timeout=10,
        )

    # ════════════════════════════════════════════════════════════════════════
    # MENSAJE 1 — LIVE (dinero real, verdad de suelo on-chain)
    # ════════════════════════════════════════════════════════════════════════
    if snap and not snap.get("_rancio"):
        pnl_t_real = snap["pnl_real"]
        deposito = snap["deposito_inicial"]
        bkr_em = "📈" if pnl_t_real >= 0 else "📉"
        pct_total = (pnl_t_real / deposito * 100) if deposito else None
        pct_hoy = (snap["pnl_hoy_real"] / deposito * 100
                   if deposito and snap.get("pnl_hoy_real") is not None else None)
        hoy_str = (f"{snap['pnl_hoy_real']:+.2f}$ ({pct_hoy:+.1f}%)"
                   if snap.get("pnl_hoy_real") is not None and pct_hoy is not None else "—")
        d7_str  = (f"{snap['pnl_7d_real']:+.2f}$"
                   if snap.get("pnl_7d_real") is not None else "—")
        if n_live_total:
            wr_live = w_live_total / n_live_total * 100
            live_perf = (
                f"Trades: {n_live_total}  |  WR {wr_live:.0f}%  |  hoy {n_live_hoy} cerrados\n"
                f"PnL hoy: {hoy_str}  ·  7 días: {d7_str}\n"
                f"Fees pagados (real): {fees_total_live:.2f}$"
            )
        else:
            live_perf = "Sin trades cerrados aún — esperando primera ventana"
        pct_str = f" ({pct_total:+.1f}% sobre depósito)" if pct_total is not None else ""
        msg_live = (
            f"💰 *BOT LIVE — dinero real* — {ahora.strftime('%H:%M UTC')}\n"
            f"\n"
            f"{bkr_em} Balance: *{snap['total']:.2f}$*  "
            f"(depósito {deposito:.2f}$ → {pnl_t_real:+.2f}${pct_str})\n"
            f"{live_perf}\n"
            f"\n"
            f"Estado: {live_estado}"
        )
    else:
        # Fail loud: sin snapshot on-chain fresco no se inventan saldos.
        msg_live = (
            f"💰 *BOT LIVE* — {ahora.strftime('%H:%M UTC')}\n"
            f"\n"
            f"⚠️ Sin balance on-chain fresco (live\\_balance.py corre por cron cada "
            f"15min) — no muestro saldo hasta recuperarlo.\n"
            f"\n"
            f"Estado: {live_estado}"
        )

    # Solo se envía el mensaje LIVE por Telegram (petición Javi 09-Jul: las
    # simulaciones (shadow) ya se consultan en el dashboard — Telegram queda
    # reservado a lo que está pasando de verdad, dinero real). El resumen
    # shadow completo (GBM en observación, whitelist, PnL fiel) sigue
    # generándose en data/shadow/estado_actual.md y en el dashboard, solo
    # dejó de duplicarse por Telegram.
    try:
        _post(msg_live)
        LAST_TG_PATH.write_text(str(ahora_ts))
        print(f"  [telegram] Mensaje live CRIPTO enviado ({ahora.strftime('%H:%M UTC')})")
    except Exception as e:
        print(f"  [telegram] Error: {e}")

    # ════════════════════════════════════════════════════════════════════════
    # MENSAJE 2 — SPORTS (dinero real, mismo /update -- petición explícita
    # Javi 27-Ago: quiere las dos infos juntas en el mismo comando, con
    # indicador claro de cuál es cuál, sin necesidad de un bot de Telegram
    # separado).
    # ════════════════════════════════════════════════════════════════════════
    try:
        import sports_live_guard
        import sports_live_stake
        est_sp = sports_live_guard.estado_live()
        bkr_sp = sports_live_stake.bankroll_actual()
        pares_sp = est_sp["pares_permitidos"]
        switch_sp_txt = "✅ ON" if est_sp["switch"] else "❌ OFF"
        pares_sp_txt = f"{len(pares_sp)} activo(s)" if pares_sp else "0 (fail-closed, nada opera)"

        trades_sp_csv = Path("data/sports/trades.csv")
        n_sp_total = n_sp_hoy = w_sp_total = 0
        if trades_sp_csv.exists() and trades_sp_csv.stat().st_size > 100:
            cerrados_sp = [r for r in csv.DictReader(open(trades_sp_csv, encoding="utf-8"))
                           if r.get("status") == "CLOSED"]
            n_sp_total = len(cerrados_sp)
            n_sp_hoy = sum(1 for r in cerrados_sp
                           if _cerrado_hoy_madrid(r.get("close_timestamp", ""), ahora))
            w_sp_total = sum(1 for r in cerrados_sp if float(r.get("pnl_neto_eur") or 0) > 0)

        if n_sp_total:
            wr_sp = w_sp_total / n_sp_total * 100
            sp_perf = f"Trades: {n_sp_total}  |  WR {wr_sp:.0f}%  |  hoy {n_sp_hoy} cerrados"
        else:
            sp_perf = "Sin trades cerrados aún"

        msg_sports = (
            f"⚽ *BOT SPORTS — dinero real* — {ahora.strftime('%H:%M UTC')}\n"
            f"\n"
            f"Bankroll: *{bkr_sp:.2f}€*\n"
            f"{sp_perf}\n"
            f"\n"
            f"Switch: {switch_sp_txt}  |  pares_permitidos_live: {pares_sp_txt}"
        )
        _post(msg_sports)
        print(f"  [telegram] Mensaje live SPORTS enviado ({ahora.strftime('%H:%M UTC')})")
    except Exception as e:
        print(f"  [telegram] Error generando/enviando mensaje SPORTS: {type(e).__name__}: {e}")

    # ════════════════════════════════════════════════════════════════════════
    # MENSAJE 3 — WEATHER (dinero real, mismo /update -- petición explícita
    # Javi 15-Sep: "cada vez que le dé a update en telegram que me mande un
    # reporte de cómo vamos en trading de Cripto, Sports (como hasta ahora)
    # y Weather", mismo día del primer depósito real de weather (6€).
    #
    # Lectura cross-repo de FICHEROS de estado (config_live.json/trades.csv),
    # no de código -- weather es un repo independiente (/root/polymarket-
    # weather, CLAUDE.md: "no mezclar datos, código ni params"), pero leer
    # sus ficheros para un resumen de solo-lectura no importa ningún módulo
    # de weather ni escribe nada ahí -- mismo criterio ya aplicado en
    # live_balance.py::_weather_capital_en_free_usdc() el mismo día.
    # ════════════════════════════════════════════════════════════════════════
    try:
        WEATHER_REPO = Path("/root/polymarket-weather")
        weather_cfg = json.loads((WEATHER_REPO / "data/live/config_live.json").read_text(encoding="utf-8"))
        switch_we = (WEATHER_REPO / "data/live/LIVE_MODE_ON").exists()
        pares_we = weather_cfg.get("pares_permitidos_live", [])
        depositos_we = sum(float(d.get("eur", 0) or 0) for d in weather_cfg.get("depositos", []))

        trades_we_csv = WEATHER_REPO / "data/live/trades.csv"
        n_we_total = n_we_hoy = w_we_total = 0
        pnl_we_total = 0.0
        if trades_we_csv.exists() and trades_we_csv.stat().st_size > 100:
            cerrados_we = [r for r in csv.DictReader(open(trades_we_csv, encoding="utf-8"))
                           if r.get("status") == "CLOSED"]
            n_we_total = len(cerrados_we)
            n_we_hoy = sum(1 for r in cerrados_we
                           if _cerrado_hoy_madrid(r.get("close_timestamp", ""), ahora))
            w_we_total = sum(1 for r in cerrados_we if float(r.get("pnl_neto_eur") or 0) > 0)
            pnl_we_total = sum(float(r.get("pnl_neto_eur") or 0) for r in cerrados_we)
        bkr_we = depositos_we + pnl_we_total  # mismo criterio que weather_live_stake.bankroll_actual()

        switch_we_txt = "✅ ON" if switch_we else "❌ OFF"
        pares_we_txt = f"{len(pares_we)} activo(s)" if pares_we else "0 (fail-closed, nada opera)"
        if n_we_total:
            wr_we = w_we_total / n_we_total * 100
            we_perf = (f"Trades: {n_we_total}  |  WR {wr_we:.0f}%  |  hoy {n_we_hoy} cerrados  |  "
                       f"PnL: {pnl_we_total:+.2f}€")
        else:
            we_perf = "Sin trades cerrados aún"

        msg_weather = (
            f"🌦️ *BOT WEATHER — dinero real* — {ahora.strftime('%H:%M UTC')}\n"
            f"\n"
            f"Bankroll: *{bkr_we:.2f}€*  (depósito {depositos_we:.2f}€)\n"
            f"{we_perf}\n"
            f"\n"
            f"Switch: {switch_we_txt}  |  pares_permitidos_live: {pares_we_txt}"
        )
        _post(msg_weather)
        print(f"  [telegram] Mensaje live WEATHER enviado ({ahora.strftime('%H:%M UTC')})")
    except Exception as e:
        print(f"  [telegram] Error generando/enviando mensaje WEATHER: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
