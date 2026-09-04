#!/usr/bin/env python3
"""
wallet_mirror_tracker.py — Arquetipo C ("Wallet Mirror", P24), petición
Javi 23-Jul, retomado y CERRADO a nivel de investigación 29-Jul: mide si
replicar (SEGUIR) o desvanecer (FADE) el trade de wallets validadas
(BH-FDR, n≥30) en la zona de precio medio/bajo (0.1-0.6, donde nuestro
propio modelo GBM tiene edge teórico pero fill-ability ~0%) captura un
edge real, ANTES de construir ningún ejecutor de dinero real.

Fuente de detección: `fetch_polymarket_activity_ws.py` (screen
`polyactivity`, construido 28-Jul, sin conectar a nada hasta hoy) — ya
captura wallet/precio/mercado/timestamp de CADA trade real en tiempo
real vía el firehose RTDS, exactamente lo que este mecanismo necesita
(cierra el "punto 2" pendiente de idea_wallet_mirror_arquetipo_c_23jul:
medir el lag de detección — aquí la detección es casi instantánea,
mismo pipeline ya verificado con 1288 trades/25s).

Metodología (solo lectura, NO ejecuta nada, NO toca dinero):
1. Carga las wallets validadas (`sig_bhfdr=True`, n>=30) de
   `wallet_edge_score_por_activo_marco.json`, clasificadas SEGUIR
   (edge_pp>0) / FADE (edge_pp<0), cada una atada a SU (activo,marco)
   validado exacto -- no se generaliza a otros mercados de la misma
   wallet.
2. Lee `data/shadow/polymarket_activity_YYYY-MM-DD.csv` (hoy + ayer, para
   no perder trades cerca de medianoche) buscando filas cuyo `wallet`
   coincida (case-insensitive) Y cuyo (activo,marco) coincida con el de
   la validación de esa wallet.
3. Por cada match nuevo (dedup por `transaction_hash`), registra qué
   habría hecho Wallet Mirror: mismo lado que la wallet si es SEGUIR,
   lado contrario si es FADE. Precio de referencia = el precio real al
   que la wallet operó (mismo instante, no hay slippage de detección
   que estimar aparte -- eso se mide en el gate de fill-ability real,
   pendiente, no en este tracker).
4. Resuelve contra el outcome oficial (gamma-api, vía `market_slug` --
   `polymarket_activity` no loguea el market_id numérico de Gamma, solo
   `condition_id`/slugs) cuando el mercado ya haya cerrado.

Cron sugerido: cada 5-10min (no necesita ser un screen persistente --
esto es un catch-up sobre un CSV que ya se está escribiendo solo, no una
decisión en tiempo real todavía).
"""
import csv
import fcntl
import json
import math
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import requests  # noqa: E402
import live_trade as lt  # noqa: E402
from analisis_gate_riguroso import wilson_ci  # noqa: E402

DIR_SHADOW = REPO / "data" / "shadow"
# 29-Jul: polymarket_activity_*.csv vive fuera del repo (fix fetch_polymarket_activity_ws.py).
DIR_DATALOGS = Path("/root/polymarket-research-datalogs")
WALLET_SCORES = DIR_SHADOW / "wallet_edge_score_por_activo_marco.json"
OUT = DIR_SHADOW / "wallet_mirror_dry_run.csv"
OUT_LOCK = DIR_SHADOW / "wallet_mirror_dry_run.csv.lock"
VISTOS_PATH = DIR_SHADOW / "wallet_mirror_vistos.json"  # transaction_hash ya procesados
# 13-Ago (fix, encontrado escribiendo el gate de rendimiento reciente de
# abajo): OUT (wallet_mirror_dry_run.csv) lleva MUERTO desde el 04-Ago --
# wallet_mirror_tracker.py::main() dejó de ser el proceso que corre de
# verdad, sustituido por wallet_mirror_sniper.py, que escribe a su PROPIO
# CSV. Cualquier gate que necesite el histórico de mirror REAL y vivo tiene
# que leer este otro fichero, no OUT.
DRY_RUN_VIVO = DIR_SHADOW / "wallet_mirror_sniper_dry_run.csv"
# 24-Ago: fuente adicional para _historial_reciente_wallet_mirror() -- ver
# docstring de esa función. Misma fuente que wallet_edge_tracker.py::HIST.
HIST_BALLENAS = DIR_SHADOW / "ballenas_timing_history.csv"

_cache_dry_run_vivo = {"mtime": None, "filas": None}


def _leer_dry_run_vivo_filas() -> list:
    """Lee wallet_mirror_sniper_dry_run.csv UNA vez, cacheado por mtime
    (04-Sep, /code-review: _historial_reciente_wallet_mirror() y
    _historial_reciente_wallet_mirror_por_bucket() lo leían cada una por
    separado en el MISMO refresco de 30min de wallet_mirror_executor_
    dryrun.py -- doble I/O/CPU sobre un fichero de 400k+ filas y
    creciendo. Mismo patrón de caché por mtime que resolution_sniper_
    precierre_gate.py/gate_bucket_propio.py -- nunca sirve un dato más
    viejo que el propio fichero en disco, solo evita reparsearlo si no
    ha cambiado desde la última lectura."""
    try:
        mtime = DRY_RUN_VIVO.stat().st_mtime
    except OSError:
        return []
    if _cache_dry_run_vivo["mtime"] != mtime:
        with open(DRY_RUN_VIVO, encoding="utf-8") as f:
            _cache_dry_run_vivo["filas"] = list(csv.DictReader(f))
        _cache_dry_run_vivo["mtime"] = mtime
    return _cache_dry_run_vivo["filas"]


def _acierto_wallet_desde_fila_dry_run(row: dict) -> int | None:
    """None si la fila no tiene acierto resuelto. Si no, el acierto en
    semántica NATIVA de la wallet (¿acertó ELLA?), invertido para FADE --
    ver docstring de _historial_reciente_wallet_mirror() para el porqué
    (bug real 24-Ago de mezclar semánticas). /code-review 04-Sep: extraído
    a función compartida -- esta misma lógica vivía duplicada en
    _historial_reciente_wallet_mirror() y _historial_reciente_wallet_
    mirror_por_bucket(), con el riesgo real de corregir una copia y
    olvidar la otra."""
    if row.get("acierto") not in ("0", "1"):
        return None
    acierto = int(row["acierto"])
    if row.get("tipo", "") == "FADE":
        acierto = 1 - acierto
    return acierto

N_MIN_WALLET = 30
GAMMA = "https://gamma-api.polymarket.com"
UMBRAL_RESUELTO = 0.98

# 13-Ago (petición explícita Javi, dinero real): "el histórico me vale para
# que entren en la muestra, pero no para que sirva como criterio para
# operar -- si una wallet se degrada y la seguimos, perdemos pasta". Hasta
# hoy la wallet que operaba con dinero real (wallet_mirror_executor_dryrun.py,
# DRY_RUN=False desde 11-Ago) solo se filtraba por histórico completo
# (sig_bhfdr, n>=N_MIN_WALLET) -- vigia_wallet_mirror_degradacion.py (13-Ago,
# cron diario) ya detectaba degradación reciente pero SOLO avisaba por
# Telegram, nunca excluía -- confirmado con datos reales de HOY mismo: 3
# wallets marcadas DEGRADADA en el latch (0xfcefc196...#BTC#15min
# hist=76.7% reciente=40.0%, 0x9866f9b7...#SOL#15min hist=54.3%
# reciente=15.0%, 0x89b8c9d6...#BTC#5min hist=81.4% reciente=40.0%) seguían
# operando con dinero real porque nada las excluía.
#
# `wallets_operativas_recientes()` de abajo convierte ese chequeo de alerta
# en filtro real, fail-closed -- pero A PROPÓSITO NO se mete dentro de
# cargar_wallets_validadas(): esa función también alimenta la detección/
# grabación continua de wallet_mirror_sniper.py (escribe cada match nuevo a
# DRY_RUN_VIVO). Filtrar ahí habría dejado a cualquier wallet excluida sin
# poder grabar NUNCA más trades bajo su clave -- estado absorbente real
# (/code-review 13-Ago: con el primer intento, 242/283 tuplas -85.5%-
# quedaban excluidas ya en el primer ciclo, incluidas wallets nuevas que
# nunca tuvieron oportunidad de acumular historial). cargar_wallets_validadas()
# se queda TAL CUAL (solo histórico) para que la detección nunca se pare;
# solo el ejecutor de dinero real llama al wrapper filtrado.
N_RECIENTE_OPERAR = 15          # 25-Ago: bajado de 18 (decisión explícita Javi,
# "mira si se degrada el payout"). Simulado con datos frescos: 77->80 operativas
# (+12 marginales, -9 perdidas, neto +3), 0/12 marginales con g_kelly_real<=0
# -- payout limpio confirmado (de paso se encontró y arregló un bug real: el
# campo "g_kelly" guardado para candidatas FADE era el de LA WALLET, no el de
# g_kelly_fade -- nuestra posición real -- lo que había dado un falso "4/12
# con payout malo" en el primer intento de esta misma verificación). Sigue sin
# resolver el hueco de cobertura fuera de BTC. Antes: 20 (hasta 24-Ago) -> 18
# (24-Ago, project_simulacion_n_reciente_operar_24ago) -> 15 (hoy). Mismo
# valor que vigia_wallet_mirror_degradacion.py::N_RECIENTE (constante
# independiente, no importada -- mantener las dos sincronizadas a mano).
MARGEN_DEGRADACION_PP_OPERAR = 15


def _historial_reciente_wallet_mirror(wallets_objetivo: set | None = None) -> dict:
    """(wallet, activo, marco_activity, tipo) -> [(trade_timestamp, acierto), ...] ordenado.

    24-Ago (hallazgo real, petición Javi: "wallets ETH bloqueadas solo por
    insuficiente reciente -- vamos a solucionar esto"): antes SOLO leía
    DRY_RUN_VIVO (wallet_mirror_sniper_dry_run.csv, arranca 30-Jul, solo
    trades que nuestro PROPIO sniper detectó en tiempo real) -- fuera de
    BTC (mucho menos volumen de mercado, ver project_kill_switch_
    reapertura_wallet_mirror_24ago), muchas wallets con histórico completo
    excelente nunca acumulaban 20 matches recientes propios, aunque llevaran
    semanas operando de verdad en el mercado.

    Ahora se enriquece con `ballenas_timing_history.csv` -- LA MISMA fuente
    que `wallet_edge_tracker.py` ya usa para calcular `info["hit"]` (el
    histórico contra el que se compara "reciente" para detectar
    degradación), con muchísima más profundidad (arranca 12-Jun) y SIN el
    sesgo de "solo lo que nuestro sniper llegó a detectar en tiempo real".
    Metodológicamente más consistente que antes: comparar "reciente" y
    "histórico" desde la MISMA fuente, no una filtrada (sniper) contra otra
    sin filtrar (ballenas). El "acierto" es el resultado de LA PROPIA
    wallet, independiente de tipo SEGUIR/FADE (igual que `info["hit"]"`) --
    por eso la misma lista sirve para ambos tipos de la misma (wallet,
    activo,marco). Excluye pre-TWAP igual que wallet_edge_tracker.py (mismo
    régimen de resolución que ya usa el histórico de referencia).

    DRY_RUN_VIVO se mantiene como fuente ADICIONAL (no sustituida): capta
    trades más recientes que `ballenas_observer.py` (cron horario) puede
    tardar hasta 1h en reflejar. Dedup por (wallet, condition_id) --
    ambas fuentes pueden solapar en fechas comunes."""
    from shadow_postmortem import es_pre_twap  # noqa: E402 -- import perezoso, evita ciclo con wallet_edge_tracker

    hist = defaultdict(dict)  # clave -> {(wallet,condition_id): (ts, acierto)} para dedup

    if HIST_BALLENAS.exists():
        with open(HIST_BALLENAS, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                w = (row.get("wallet") or "").lower()
                if wallets_objetivo is not None and w not in wallets_objetivo:
                    continue
                if row.get("acierto") not in ("0", "1"):
                    continue
                marco_corto = row.get("marco", "")
                marco_activity = MARCO_A_ACTIVITY.get(marco_corto)
                if marco_activity is None:
                    continue
                ts = row.get("ts_trade", "")
                if es_pre_twap(marco_activity, ts):
                    continue
                cid = row.get("condition_id", "")
                for tipo in ("SEGUIR", "FADE"):
                    clave = (w, row.get("activo", ""), marco_activity, tipo)
                    hist[clave][(w, cid)] = (ts, int(row["acierto"]))

    # 24-Ago (/code-review, bug real cazado antes de desplegar): el
    # "acierto" de este CSV es el resultado de NUESTRA POSICIÓN
    # (resolver_pendientes(): acierto=1 si outcome==mirror_lado), NO el de
    # la wallet -- para SEGUIR coinciden (mirror_lado=lado_wallet), pero
    # para FADE mirror_lado es el lado CONTRARIO, así que acierto=1 aquí
    # significa que LA WALLET PERDIÓ. ballenas_timing_history.csv (arriba)
    # usa la semántica nativa "acertó la wallet" -- la misma que
    # info["hit"] (la referencia con la que se compara en
    # wallets_operativas_recientes()). _acierto_wallet_desde_fila_dry_run()
    # invierte para FADE, dejando las dos fuentes en la MISMA semántica
    # antes de mezclarlas bajo la misma clave.
    for row in _leer_dry_run_vivo_filas():
        acierto = _acierto_wallet_desde_fila_dry_run(row)
        if acierto is None:
            continue
        w = row.get("wallet", "").lower()
        if wallets_objetivo is not None and w not in wallets_objetivo:
            continue
        tipo = row.get("tipo", "")
        clave = (w, row.get("activo", ""), row.get("marco", ""), tipo)
        cid = row.get("condition_id", "")
        hist[clave][(w, cid)] = (row.get("trade_timestamp", ""), acierto)

    out = {}
    for clave, por_cid in hist.items():
        out[clave] = sorted(por_cid.values(), key=lambda x: x[0])
    return out


def wallets_operativas_recientes() -> dict:
    """Wrapper de cargar_wallets_validadas() SOLO para lo que toca dinero real
    (wallet_mirror_executor_dryrun.py) -- exige rendimiento RECIENTE (últimos
    N_RECIENTE_OPERAR trades resueltos, fuente ballenas_timing_history.csv +
    DRY_RUN_VIVO, ver _historial_reciente_wallet_mirror) no degradado frente
    al histórico Y con borde estadístico propio sobre el 50%. Fail-closed:
    candidata sin suficiente historial reciente propio se EXCLUYE, no hay
    fallback silencioso al histórico agregado. NO usar para detección/logging
    (eso sigue siendo cargar_wallets_validadas() sin filtrar, ver nota arriba)."""
    candidatas = cargar_wallets_validadas()
    if not candidatas:
        return candidatas
    wallets_objetivo = {w for w, _, _ in candidatas}
    hist = _historial_reciente_wallet_mirror(wallets_objetivo)
    out = {}
    for clave, info in candidatas.items():
        w, activo, marco = clave
        aciertos = hist.get((w, activo, marco, info["tipo"]), [])
        if len(aciertos) < N_RECIENTE_OPERAR:
            continue  # sin evidencia reciente suficiente -> no se opera
        if info.get("hit") is None:
            continue  # sin hit histórico (dato inesperado) -> fail-closed, no se opera
        recientes = [a for _, a in aciertos[-N_RECIENTE_OPERAR:]]
        k, n = sum(recientes), len(recientes)  # k = nº recientes donde ACERTÓ LA WALLET (semántica nativa, ver _historial_reciente_wallet_mirror)
        ci_lo, ci_hi = wilson_ci(k, n)
        hit_hist = info["hit"] * 100
        if ci_hi * 100 < (hit_hist - MARGEN_DEGRADACION_PP_OPERAR):
            continue  # degradada frente a SU histórico -- mismo criterio que vigia_wallet_mirror_degradacion.py
        # 13-Ago (fix del mismo día, gap real encontrado probando el filtro
        # de arriba en vivo): comparar solo contra el histórico no basta --
        # si la wallet lleva un tiempo mal, sus propios trades recientes YA
        # están dentro de ese histórico y lo arrastran hacia abajo con ella,
        # así que "reciente no mucho peor que el histórico" deja de disparar
        # aunque el reciente siga siendo malo en términos absolutos (caso
        # real: 0xfcefc196...#BTC#15min, hist bajó de 76.7%->59.3% en unas
        # horas arrastrado por sus propias 8/20 recientes, dejando de
        # marcarse degradada pese a que 40% reciente sigue sin edge). Exigir
        # ADEMÁS que el propio reciente muestre borde estadístico real sobre
        # 50% (Wilson90 INFERIOR, no el superior de arriba) -- "hit rate
        # alto validado reciente" tiene que sostenerse por sí mismo, no solo
        # relativo a una línea base que puede estar degradándose con él.
        # 24-Ago (/code-review, bug crítico cazado antes de desplegar):
        # k/ci_lo/ci_hi de arriba están en semántica "acertó LA WALLET"
        # (necesaria para la comparación de degradación de arriba, que
        # compara contra hit_hist -- también wallet-win). Pero el edge que
        # de verdad importa aquí es el de NUESTRA POSICIÓN: para SEGUIR
        # coincide con "acertó la wallet" (mismo lado), para FADE es lo
        # contrario (apostamos contra ella -- queremos su hit CONFIRMADO
        # BAJO, no alto). Sin este split, el check exigía ci_lo>50% de
        # "acertó la wallet" también para FADE -- justo lo opuesto de la
        # tesis FADE (se selecciona porque hit_hist<50%), excluyendo casi
        # todas las candidatas FADE reales (verificado: 5/97 sobrevivían
        # vs 68/230 SEGUIR).
        k_posicion = k if info["tipo"] == "SEGUIR" else (n - k)
        ci_lo_posicion, _ = wilson_ci(k_posicion, n)
        if ci_lo_posicion <= 0.50:
            continue  # sin edge reciente confirmado por sí mismo -> no se opera
        out[clave] = info
    return out


# 04-Sep (petición explícita Javi, tras el hallazgo real de
# idea_walletmirror_15min_causa_concentracion_wallet_04sep -- la racha
# 1W/6L de WALLET_MIRROR#BTC/ETH#15min no fue varianza pura: una wallet
# concentraba el 26,2% del volumen de ETH#15min[0.22,0.27) y su hit-rate
# EN ESA ZONA de precio concreta venía cayendo 41,9%->26,9% en días,
# mientras `wallets_operativas_recientes()` de arriba -- que solo mira
# (wallet,activo,marco,tipo), sin desagregar por precio -- seguía
# admitiéndola porque su agregado en BTC/ETH#15min entero no había caído
# lo suficiente para disparar la comparación de arriba. CLAUDE.md pt.17:
# "desagregar SIEMPRE por micro-bucket de precio, en TODO análisis" --
# esto faltaba aquí. Mismo mecanismo que wallets_operativas_recientes(),
# un eje más de segmentación (bucket de precio, STEP=0.05, MISMA función
# que wallet_mirror_gate_bucket.bucket() -- no reinventar el bucketing).
from wallet_mirror_gate_bucket import bucket as _bucket_precio  # noqa: E402

N_RECIENTE_BUCKET_OPERAR = 8    # calibrado 04-Sep sobre datos reales: con
# N=8, 8.624/17.826 combinaciones (wallet,activo,marco,tipo,bucket) tienen
# evidencia suficiente para evaluarse (resto queda fail-closed, "sin
# evidencia" -- normal y esperado, un bucket de 0,05 de ancho recibe mucho
# menos volumen que el marco entero). Con N=15 (mismo valor que el check
# agregado) solo 6.076/17.826 -- demasiado restrictivo para un primer
# despliegue; revisar con más n según crezca el histórico.
MARGEN_DEGRADACION_PP_BUCKET = 15  # mismo criterio que MARGEN_DEGRADACION_PP_OPERAR
MIN_ANTIGUOS_DEGRADACION_BUCKET = 5  # mínimo de trades ANTERIORES a la ventana reciente
# para que el histórico DEL PROPIO BUCKET sea informativo -- ver uso en
# wallets_operativas_recientes_por_bucket().


def _historial_reciente_wallet_mirror_por_bucket(wallets_objetivo: set | None = None) -> dict:
    """(wallet, activo, marco_activity, tipo, bucket_precio) -> [(ts, acierto), ...].

    MISMA semántica de "acierto" (resultado de LA WALLET, no de nuestra
    posición -- FADE invertido igual que en _historial_reciente_wallet_
    mirror()) que la función agregada de arriba, con un eje extra: el
    bucket de precio (STEP=0,05) al que perteneció CADA trade individual.

    /code-review 04-Sep, hallazgo real: la primera versión mezclaba
    HIST_BALLENAS (bucket por `precio`, el precio al que operó LA WALLET
    en el mercado -- feed de actividad de mercado, sin ningún concepto de
    "nuestro ask") y DRY_RUN_VIVO (bucket por `mejor_ask_deteccion`,
    NUESTRO precio de entrada real) bajo la MISMA clave de bucket -- dos
    puntos de medida distintos, mezclados. Fix: esta función usa SOLO
    DRY_RUN_VIVO (`wallet_mirror_sniper_dry_run.csv`, 400k+ filas
    resueltas desde 30-Jul -- de sobra para esta capa) para que el bucket
    represente SIEMPRE el mismo precio (nuestro ask real), consistente
    con lo que se comprueba en el ejecutor (`ask_ref`). La función
    agregada de arriba (wallets_operativas_recientes(), sin eje de
    precio) SÍ sigue combinando ambas fuentes -- ahí no hay mezcla de
    semánticas de precio porque no hay bucket que corromper.

    Función separada (no se reutiliza la de arriba) a propósito: añadir
    un elemento al tuple interno (ts, acierto) de la función agregada,
    ya usada en producción por wallets_operativas_recientes(), es más
    riesgo del necesario para un cambio que solo hace falta aquí -- más
    vale una function nueva y clara que tocar código ya en dinero real."""
    hist = defaultdict(dict)  # clave -> {(wallet,condition_id): (ts, acierto)} para dedup

    for row in _leer_dry_run_vivo_filas():
        acierto = _acierto_wallet_desde_fila_dry_run(row)
        if acierto is None:
            continue
        w = row.get("wallet", "").lower()
        if wallets_objetivo is not None and w not in wallets_objetivo:
            continue
        tipo = row.get("tipo", "")
        # mejor_ask_deteccion (nuestro precio de entrada real) es el ÚNICO
        # ancla válida para el bucket -- mismo campo que usa
        # wallet_mirror_gate_bucket.py. /code-review 04-Sep (2ª ronda):
        # la primera versión caía a precio_wallet cuando mejor_ask_
        # deteccion venía vacío ("" en ~1,4% de las filas, cuando
        # fill_deteccion.get("ok") es False en el sniper) -- eso
        # reintroducía la MISMA mezcla de dos precios distintos bajo la
        # misma clave que se acababa de corregir. Sin fallback: una fila
        # sin ask real conocido se descarta para el bucket (sigue contando
        # para el check AGREGADO, que no depende de precio).
        precio_raw = row.get("mejor_ask_deteccion")
        try:
            precio = float(precio_raw)
        except (TypeError, ValueError):
            continue
        b = _bucket_precio(precio)
        clave = (w, row.get("activo", ""), row.get("marco", ""), tipo, b)
        cid = row.get("condition_id", "")
        hist[clave][(w, cid)] = (row.get("trade_timestamp", ""), acierto)

    out = {}
    for clave, por_cid in hist.items():
        out[clave] = sorted(por_cid.values(), key=lambda x: x[0])
    return out


def wallets_operativas_recientes_por_bucket(wallets_admitidas: dict | None = None) -> dict:
    """(wallet, activo, marco, tipo, bucket_precio) -> info si la wallet
    tiene evidencia reciente SUFICIENTE Y CON EDGE dentro de ESE
    micro-bucket de precio concreto -- no solo en agregado. Fail-closed:
    ausente de este dict = no operar en ese bucket con esa wallet, aunque
    esté admitida en agregado.

    wallets_admitidas: dict de wallets_operativas_recientes() (opcional,
    recomendado) -- si se pasa, solo se evalúa el bucket para wallets que
    YA pasaron el filtro agregado (evita trabajo redundante; el check de
    bucket es una capa ADICIONAL sobre el agregado, no un sustituto -- una
    wallet degradada en agregado sigue vetada aunque un bucket concreto
    pareciera bien por casualidad de n bajo)."""
    candidatas = cargar_wallets_validadas()
    if not candidatas:
        return {}
    if wallets_admitidas is not None:
        candidatas = {k: v for k, v in candidatas.items() if k in wallets_admitidas}
    wallets_objetivo = {w for w, _, _ in candidatas}
    hist = _historial_reciente_wallet_mirror_por_bucket(wallets_objetivo)
    out = {}
    for (w, activo, marco, tipo, b), aciertos in hist.items():
        clave_agregada = (w, activo, marco)
        info = candidatas.get(clave_agregada)
        if info is None or info["tipo"] != tipo:
            continue
        if len(aciertos) < N_RECIENTE_BUCKET_OPERAR:
            continue  # sin evidencia reciente suficiente en ESTE bucket -> no operar aquí
        recientes_tup = aciertos[-N_RECIENTE_BUCKET_OPERAR:]
        recientes = [a for _, a in recientes_tup]
        k, n = sum(recientes), len(recientes)
        # /code-review 04-Sep, hallazgo real: faltaba el check de
        # degradación-vs-histórico que SÍ tiene la función agregada
        # (wallets_operativas_recientes) -- sin esto, una wallet que se
        # degrada dentro de un bucket concreto pero sigue por encima del
        # 50% plano pasaba el gate igual, exactamente el caso que motivó
        # este mecanismo (0xeebde... en ETH#15min[0.22,0.27), 41,9%->26,9%
        # en días, ambas cifras por encima de breakeven de la zona). El
        # histórico de ESTE bucket concreto no está precalculado en
        # ningún sitio (a diferencia de info["hit"] agregado) -- se
        # calcula aquí mismo con la parte de `aciertos` anterior a la
        # ventana reciente. MIN_ANTIGUOS_DEGRADACION: si no hay suficiente
        # historia previa al margen reciente, no se puede comparar --
        # se deja pasar solo por el criterio de borde >50% de arriba
        # (fail-closed seguiría siendo excesivo con un bucket que apenas
        # tiene más que los N_RECIENTE_BUCKET_OPERAR mínimos).
        antiguos_tup = aciertos[:-N_RECIENTE_BUCKET_OPERAR]
        if len(antiguos_tup) >= MIN_ANTIGUOS_DEGRADACION_BUCKET:
            k_hist = sum(a for _, a in antiguos_tup)
            hit_hist_bucket = k_hist / len(antiguos_tup) * 100
            _, ci_hi = wilson_ci(k, n)
            if ci_hi * 100 < (hit_hist_bucket - MARGEN_DEGRADACION_PP_BUCKET):
                continue  # degradada frente a SU histórico EN ESTE BUCKET -> no operar aquí
        k_posicion = k if tipo == "SEGUIR" else (n - k)
        ci_lo_posicion, _ = wilson_ci(k_posicion, n)
        if ci_lo_posicion <= 0.50:
            continue  # sin edge reciente confirmado EN ESTE BUCKET -> no operar aquí
        out[(w, activo, marco, tipo, b)] = {"n": n, "hit_reciente": round(k / n, 4)}
    return out


def wallet_aprueba_bucket(wallet: str, activo: str, marco: str, tipo: str, ask: float,
                          cache: dict) -> bool:
    """Lookup de conveniencia para el ejecutor: ¿esta wallet, en este
    micro-bucket de precio, tiene evidencia reciente con edge? `cache` es
    el dict ya calculado por wallets_operativas_recientes_por_bucket()
    (refrescado cada REFRESCO_WALLETS_S, mismo cadencia que el agregado --
    el llamante lo recalcula, esta función no vuelve a leer disco)."""
    b = _bucket_precio(ask)
    return (wallet.lower(), activo, marco, tipo, b) in cache


# 29-Jul (bug real encontrado en el primer smoke test, 0 matches pese a
# haber decenas en los datos crudos): wallet_edge_score_por_activo_marco.json
# usa "5m"/"15m"/"60m"/"240m"/"weekly", polymarket_activity_*.csv usa
# "5min"/"15min"/"60min"/"240min"/"weekly" -- sin normalizar, el join nunca
# cruzaba nada. "weekly" AÑADIDO 29-Jul (petición Javi: cubrir todas las
# monedas/marcos) -- fetch_polymarket_activity_ws.py ahora clasifica
# hourly/weekly por TEXTO del título (fallback cuando el slug no resuelve,
# mismo mecanismo ya usado en fetch_libro_ambos_lados.py), así que el feed
# de activity ya produce marco="weekly" para mercados WEEKLY_PRICE.
MARCO_A_ACTIVITY = {"5m": "5min", "15m": "15min", "60m": "60min", "240m": "240min", "weekly": "weekly"}


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def cargar_wallets_validadas() -> dict:
    """(wallet_lower, activo, marco) -> {"tipo": "SEGUIR"|"FADE", "edge_pp": float, "n": int}.
    Solo histórico completo (sig_bhfdr, n>=N_MIN_WALLET) -- para dinero real usar
    wallets_operativas_recientes(), que además exige rendimiento reciente."""
    try:
        datos = json.loads(WALLET_SCORES.read_text(encoding="utf-8"))
    except Exception:
        return {}
    out = {}
    for v in datos.values():
        if not v.get("sig_bhfdr") or v.get("n", 0) < N_MIN_WALLET:
            continue
        w = (v.get("wallet") or "").lower()
        if not w:
            continue
        marco_activity = MARCO_A_ACTIVITY.get(v["marco"])
        if marco_activity is None:
            continue  # "weekly" -- sin equivalente en el feed de activity
        # 29-Jul: gate riguroso sobre wallet_mirror_dry_run.csv encontró
        # BTC#5min#FADE (n=271) invertido -- hit=33.2% (Wilson90_lo=28.7%),
        # consistente en ~20 wallets distintas, no un caso aislado. Causa
        # diagnosticada: edge_pp=(hit-precio_medio)*100 es EV/calibración,
        # no dirección -- una wallet puede tener edge_pp<0 (mal EV) con
        # hit>50% si sistemáticamente sobrepaga por el favorito (mismo
        # patrón payout-asimétrico que FAVORITO_CONFIRMADO). Fadear a esa
        # wallet significa apostar por el lado underdog de SU apuesta, que
        # tiene hit-rate BAJO por definición (ella gana la mayoría) --
        # invertir dirección de una wallet con hit>50% garantiza que el
        # mirror pierda la mayoría de las veces, aunque el EV en teoría
        # compense. Confirmado: 29-Jul, 52 wallets FADE validadas
        # globalmente, 15 (29%) tenían hit>50% -- exactamente el patrón.
        # FADE ahora exige TAMBIÉN hit<50% (wallet que se equivoca de
        # lado más de la mitad de las veces, no solo mal EV) -- las
        # excluidas (edge_pp<0 pero hit>=50%) se descartan por ahora, sin
        # estrategia validada para ese caso todavía.
        #
        # 24-Ago (mismo mecanismo de fondo, hallazgo real): edge_pp es EV
        # LINEAL -- puede ser positivo con crecimiento Kelly (g_kelly)
        # NEGATIVO si la wallet entra en zona "favorito ya confirmado"
        # (hit alto, payout pequeño, pérdida rara pero casi total). 20/245
        # wallets que pasaban el filtro solo con edge_pp tenían g_kelly<0
        # (10 de ellas en BTC, el único activo con tuplas WALLET_MIRROR
        # live) -- ver wallet_edge_tracker.py::_g_kelly. .get() con default
        # 0 (fail-closed): un JSON viejo sin el campo nuevo excluye la
        # wallet en vez de admitirla sin comprobar.
        if v["edge_pp"] > 0 and v.get("g_kelly", 0) > 0:
            tipo = "SEGUIR"
            g_kelly_real = v.get("g_kelly")
        elif v["hit"] < 0.5:
            # 24-Ago tarde (pendiente idea_wallet_edge_criterio_payout_vs_
            # hitrate_21ago, feedback_payout_fade_usa_posicion_propia_24ago):
            # el fix de arriba (edge_pp>0 Y g_kelly>0) solo cubre SEGUIR --
            # g_kelly ahí es el crecimiento de LA WALLET, correcto porque
            # copiamos su misma apuesta. Para FADE hasta ahora solo se
            # exigía hit<0.5 (nativo), sin comprobar el Kelly de NUESTRA
            # posición real (la contraria: hit invertido, precio
            # complementario) -- mismo hueco de payout-asimétrico que ya
            # se corrigió para SEGUIR, sin resolver aquí. Ejemplo concreto:
            # wallet con hit=0.30, precio_medio=0.75 (apuesta cara, pierde
            # la mayoría) -- nuestra posición FADE entra a 1-0.75=0.25 con
            # hit implícito 1-0.30=0.70, que puede seguir siendo payout
            # inverso si 0.25 todavía no es lo bastante barato.
            precio_medio = v.get("precio_medio")
            if precio_medio is None:
                continue  # fail-closed, sin dato no se opera
            hit_fade = 1 - v["hit"]
            precio_fade = 1 - precio_medio
            p_clamped = min(0.99, max(0.01, precio_fade))
            r_win = (1 - p_clamped) / p_clamped - 0.02  # misma SLIPPAGE que wallet_edge_tracker._g_kelly
            r_lose = -1 - 0.02
            g_kelly_fade = hit_fade * math.log(1 + 0.10 * r_win) + (1 - hit_fade) * math.log(1 + 0.10 * r_lose)
            if g_kelly_fade <= 0:
                continue  # payout inverso en NUESTRA posición fade -- fail-closed
            tipo = "FADE"
            # 25-Ago (bug real encontrado en el barrido de N_RECIENTE_OPERAR,
            # petición Javi): más abajo se guardaba v.get("g_kelly") también
            # para FADE -- el g_kelly de LA WALLET (su apuesta nativa), NO el
            # de g_kelly_fade (nuestra posición real, ya validado positivo
            # arriba). Cualquier consumidor que leyera este campo para
            # verificar payout de una candidata FADE (ej. una simulación de
            # N_RECIENTE_OPERAR) veía un número negativo engañoso pese a que
            # el filtro real ya garantiza payout limpio -- mismo tipo de
            # confusión que feedback_payout_fade_usa_posicion_propia_24ago
            # ya corrigió en el filtro, colada de nuevo en el campo mostrado.
            g_kelly_real = g_kelly_fade
        else:
            continue  # edge_pp<=0 (o payout Kelly negativo) y hit>=50% -- payout asimétrico, no dirección; sin mirror validado
        out[(w, v["activo"], marco_activity)] = {
            "tipo": tipo, "edge_pp": v["edge_pp"], "n": v["n"],
            "size_mediana": v.get("size_mediana"), "hit": v.get("hit"),
            "g_kelly": g_kelly_real,
        }
    # NO filtrar por rendimiento reciente aquí -- esta función también
    # alimenta la detección/grabación continua (wallet_mirror_sniper.py),
    # que tiene que seguir viendo TODAS las wallets históricamente válidas
    # para no dejar de acumular evidencia sobre ellas (ver nota grande
    # arriba de N_RECIENTE_OPERAR). El filtro de dinero real vive en
    # wallets_operativas_recientes().
    return out


def _archivos_activity(dias: int = 2) -> list[Path]:
    hoy = datetime.now(timezone.utc)
    out = []
    for d in range(dias):
        fecha = (hoy - timedelta(days=d)).strftime("%Y-%m-%d")
        p = DIR_DATALOGS / f"polymarket_activity_{fecha}.csv"
        if p.exists():
            out.append(p)
    return out


def _vistos_cargar() -> set:
    try:
        return set(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return set()


def _vistos_guardar(vistos: set) -> None:
    # Cap razonable -- solo necesitamos dedup reciente, no un histórico infinito.
    lista = list(vistos)[-50000:]
    VISTOS_PATH.write_text(json.dumps(lista), encoding="utf-8")


def detectar_matches(wallets: dict, vistos: set) -> tuple[list[dict], set]:
    """Una señal por (wallet, market_slug) -- no por transaction_hash. Una
    wallet activa puede rellenar la misma posición en decenas de fills
    (visto en el primer smoke test: 3135 "matches" en un solo día, la
    inmensa mayoría re-fills del mismo mercado) -- eso no son señales
    independientes, es ruido que infla n artificialmente. Se queda con el
    PRIMER fill BUY de cada (wallet, mercado): esa es "la wallet abrió
    posición aquí", el resto es solo tamaño acumulado de la misma apuesta."""
    nuevos = []
    vistos_nuevo = set(vistos)
    for path in _archivos_activity():
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if (row.get("side") or "").strip().upper() != "BUY":
                    continue  # solo aperturas de posición, no ventas/cierres
                w = (row.get("wallet") or "").lower()
                clave = (w, row.get("activo", ""), row.get("marco", ""))
                info = wallets.get(clave)
                if info is None:
                    continue
                dedup_key = f"{w}|{row.get('market_slug','')}"
                if dedup_key in vistos_nuevo:
                    continue
                vistos_nuevo.add(dedup_key)
                lado_wallet = row.get("outcome", "")  # "Up"/"Down"
                mirror_lado = lado_wallet if info["tipo"] == "SEGUIR" else _opuesto(lado_wallet)
                th = row.get("transaction_hash", "")
                fill = _fillability_mirror(row.get("market_slug", ""), mirror_lado, row.get("price", ""))
                # 29-Jul (idea_grandes_jugadas_wallets_validadas_29jul, petición
                # Javi): tamaño de ESTA apuesta relativo a la mediana propia de
                # la wallet en esta (activo,marco) -- confirmado con gate
                # riguroso (shuffle p=0.0000, split-half estable) sobre las 70
                # wallets ya validadas: >=2x mediana propia hit=79.2% (n=1200)
                # vs <=0.5x hit=48.7% (n=1537). Tamaño RELATIVO, no USD absoluto
                # (eso solo refleja capital disponible). size_mediana viene de
                # wallet_edge_score_por_activo_marco.json (wallet_edge_tracker.py).
                ratio_size = None
                size_mediana = info.get("size_mediana")
                try:
                    usd_trade = float(row.get("usd_value") or 0)
                except (TypeError, ValueError):
                    usd_trade = 0.0
                if size_mediana and usd_trade > 0:
                    ratio_size = round(usd_trade / size_mediana, 2)
                nuevos.append({
                    "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                    "trade_timestamp": row.get("timestamp_utc", ""),
                    "wallet": w,
                    "tipo": info["tipo"],
                    "edge_pp_validado": info["edge_pp"],
                    "n_validado": info["n"],
                    "activo": row.get("activo", ""),
                    "marco": row.get("marco", ""),
                    "condition_id": row.get("condition_id", ""),
                    "market_slug": row.get("market_slug", ""),
                    "lado_wallet": lado_wallet,
                    "precio_wallet": row.get("price", ""),
                    "mirror_lado": mirror_lado,
                    "transaction_hash": th,
                    "outcome_real": "",
                    "acierto": "",
                    "resolved_ts": "",
                    "ratio_vs_stake_deteccion": fill.get("ratio_vs_stake", "") if fill.get("ok") else "",
                    "mejor_ask_deteccion": fill.get("mejor_ask", "") if fill.get("ok") else "",
                    "usd_trade": usd_trade if usd_trade > 0 else "",
                    "size_mediana_wallet": size_mediana if size_mediana else "",
                    "ratio_vs_mediana_propia": ratio_size if ratio_size is not None else "",
                    "es_jugada_grande": int(ratio_size >= 2.0) if ratio_size is not None else "",
                })
    return nuevos, vistos_nuevo


def _opuesto(lado: str) -> str:
    """29-Jul: antes mezclaba las dos parejas de etiquetas (Up/Down de
    mercados Up/Down, Yes/No de WEEKLY_PRICE y otros) -- _opuesto("Yes")
    devolvía "Down" en vez de "No", así que nunca habría coincidido con el
    outcome_real real de un mercado weekly. Ahora respeta la pareja de
    entrada."""
    l = (lado or "").strip().lower()
    if l == "up":
        return "Down"
    if l == "down":
        return "Up"
    if l == "yes":
        return "No"
    if l == "no":
        return "Yes"
    return ""


STAKE_REF_EUR = 1.05  # mismo suelo que min_stake_eur en config_live.json
RATIO_OBJETIVO = 5.0  # mismo umbral que veto_profundidad/analisis_fills.py/P22


def _mercado_para_slug(market_slug: str) -> dict | None:
    """06-Ago, P24 FASE 2 (diseño): único punto que llama a /events por slug,
    reusado tanto por `_token_para_lado` (ya existía) como por
    `_market_id_y_direccion` (nuevo, para _ejecutar_orden_polymarket, que
    exige el `id` numérico de Gamma -- wallet_mirror solo traía slug/
    condition_id hasta hoy). Devuelve {"id","outcomes","tokens"} o None."""
    try:
        r = requests.get(f"{GAMMA}/events", params={"slug": market_slug}, timeout=8)
        if r.status_code != 200:
            return None
        ev = r.json()
        if not ev or not ev[0].get("markets"):
            return None
        mkt = ev[0]["markets"][0]
        outcomes = mkt.get("outcomes")
        outcomes = json.loads(outcomes) if isinstance(outcomes, str) else outcomes
        tokens = mkt.get("clobTokenIds")
        tokens = json.loads(tokens) if isinstance(tokens, str) else tokens
        if not outcomes or not tokens or len(outcomes) != len(tokens):
            return None
        return {"id": mkt.get("id"), "outcomes": outcomes, "tokens": tokens,
                "end_date": mkt.get("endDate") or ""}
    except Exception:
        return None


def _token_para_lado(market_slug: str, lado: str) -> str | None:
    """29-Jul: fill-ability -- ninguna señal de wallet_mirror medía si
    el libro real habría dejado ejecutar el mirror. wallet_mirror_dry_run.csv
    solo trae market_slug/condition_id (no market_id numérico de Gamma), así
    que en vez de _get_token_ids(market_id) (live_trade.py) se resuelve por
    slug vía /events -- mismo endpoint que ya usa outcome_por_slug() en este
    fichero. Valida el orden real contra `outcomes` en vez de asumir
    clobTokenIds[0]=primer outcome (mismo criterio que _get_token_ids)."""
    info = _mercado_para_slug(market_slug)
    if info is None:
        return None
    lado_l = (lado or "").strip().lower()
    for o, t in zip(info["outcomes"], info["tokens"]):
        if (o or "").strip().lower() == lado_l:
            return t
    return None


def _market_id_y_direccion(market_slug: str, mirror_lado: str) -> tuple[str, str, str] | None:
    """06-Ago, P24 FASE 2 (diseño): resuelve (market_id numérico de Gamma,
    direction BUY_YES/BUY_NO, end_date) para poder llamar a
    live_trade._ejecutar_orden_polymarket -- ese endpoint exige market_id,
    no slug/token_id directo. Mismo criterio de mapeo AFIRMATIVOS/NEGATIVOS
    que `live_trade._get_token_ids` (up/yes=YES, down/no=NO) -- si el orden
    de `outcomes` no encaja con ninguno de los dos patrones esperados,
    devuelve None (fail-closed: nunca adivinar dirección con dinero real).

    11-Ago (/code-review): añadido end_date al retorno -- sin él, un trade
    real registrado por wallet_mirror_executor_dryrun.py escribía
    end_date="" en trades.csv, lo que hace que analisis_diario_salud_
    sistema.py::medir_integridad_datos() (CLAUDE.md pt.18, el monitor que
    detecta trades OPEN atascados con end_date ya pasado) nunca pueda
    parsear la fecha y salte esa fila en silencio para siempre."""
    info = _mercado_para_slug(market_slug)
    if info is None or info.get("id") is None:
        return None
    outcomes = info["outcomes"]
    if len(outcomes) != 2:
        return None
    AFIRMATIVOS = {"yes", "up"}
    NEGATIVOS = {"no", "down"}
    o0 = str(outcomes[0]).strip().lower()
    o1 = str(outcomes[1]).strip().lower()
    if not ((o0 in AFIRMATIVOS and o1 in NEGATIVOS) or (o0 in NEGATIVOS and o1 in AFIRMATIVOS)):
        return None  # outcomes inesperados, no arriesgar dirección
    lado_l = (mirror_lado or "").strip().lower()
    if lado_l not in AFIRMATIVOS and lado_l not in NEGATIVOS:
        return None
    direction = "BUY_YES" if lado_l in AFIRMATIVOS else "BUY_NO"
    return str(info["id"]), direction, info.get("end_date", "")


def _fillability_mirror(market_slug: str, mirror_lado: str, precio_wallet: str,
                        token_id_precargado: str | None = None) -> dict:
    """Consulta el libro PÚBLICO (solo lectura, nunca ordena) para el token
    del lado que Wallet Mirror habría comprado, en el instante de detección
    (no en el instante original del trade de la wallet -- mismo desfase que
    ya acepta P22/candidato_evaluacion, aceptable dado el cron de 10min).
    precio de referencia: si mirror_lado==lado_wallet (SEGUIR), el mismo
    precio que pagó la wallet; si es el lado contrario (FADE), 1-precio.

    token_id_precargado (12-Ago, perfilado de latencia real con py-spy +
    medición directa a petición de Javi): `wallet_mirror_executor_dryrun.py`
    llama a esta función DOS veces por trade (detección y decisión) sobre
    el MISMO market_slug -- sin este parámetro, ambas resuelven
    `_token_para_lado`→`_mercado_para_slug` (gamma-api /events) por
    separado, medido en 90-300ms por llamada, hasta 2/3 de los
    lag_deteccion_a_decision_ms=463ms medianos que motivaron el perfilado.
    El token_id de un mercado no cambia durante su vida -- pasar el de la
    1ª llamada a la 2ª elimina una consulta de red completamente
    redundante sin cambiar qué se mide (la 2ª consulta al LIBRO, que sí
    puede haber cambiado, se sigue haciendo igual). None (default)
    preserva el comportamiento exacto de antes para el resto de
    llamadores (wallet_mirror_sniper.py, wallet_mirror_tracker.py, cada
    uno llama una sola vez por evento)."""
    try:
        precio_w = float(precio_wallet)
    except (TypeError, ValueError):
        return {"ok": False}
    token_id = token_id_precargado if token_id_precargado is not None \
        else _token_para_lado(market_slug, mirror_lado)
    if token_id is None:
        return {"ok": False}
    precio_entrada = precio_w  # aproximación -- ver docstring
    resultado = lt._consultar_profundidad_libro(None, token_id, precio_entrada, STAKE_REF_EUR)
    resultado["token_id"] = token_id
    return resultado


COLUMNS = ["timestamp_utc", "trade_timestamp", "wallet", "tipo", "edge_pp_validado",
           "n_validado", "activo", "marco", "condition_id", "market_slug",
           "lado_wallet", "precio_wallet", "mirror_lado", "transaction_hash",
           "outcome_real", "acierto", "resolved_ts",
           "ratio_vs_stake_deteccion", "mejor_ask_deteccion",
           "usd_trade", "size_mediana_wallet", "ratio_vs_mediana_propia", "es_jugada_grande"]


def guardar(filas: list) -> None:
    if not filas:
        return
    lock_f = open(OUT_LOCK, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        try:
            nuevo = not OUT.exists()
            with open(OUT, "a", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=COLUMNS)
                if nuevo:
                    w.writeheader()
                for fila in filas:
                    w.writerow(fila)
        finally:
            fcntl.flock(lock_f, fcntl.LOCK_UN)
    finally:
        lock_f.close()


def outcome_por_slug(market_slug: str) -> str | None:
    """29-Jul: devolvía "Up"/"Down" a pelo, asumiendo que outcomes[0]="Up" y
    outcomes[1]="Down" -- correcto para mercados Up/Down, pero WEEKLY_PRICE
    (añadido esta sesión, mercados de rango de precio) usa otras etiquetas
    (p.ej. "Yes"/"No") y esto lo habría resuelto siempre mal (comparación
    contra mirror_lado="Yes"/"No" nunca habría coincidido con "Up"/"Down").
    Ahora lee las etiquetas reales de `outcomes` en vez de asumirlas -- mismo
    criterio de validar-no-asumir que _get_token_ids en live_trade.py."""
    try:
        r = requests.get(f"{GAMMA}/events", params={"slug": market_slug}, timeout=8)
        if r.status_code != 200:
            return None
        ev = r.json()
        if not ev or not ev[0].get("markets"):
            return None
        mkt = ev[0]["markets"][0]
        pr = mkt.get("outcomePrices")
        pr = json.loads(pr) if isinstance(pr, str) else pr
        outcomes = mkt.get("outcomes")
        outcomes = json.loads(outcomes) if isinstance(outcomes, str) else outcomes
        if not pr or not outcomes or len(pr) != len(outcomes):
            return None
        for o, p in zip(outcomes, pr):
            if float(p) >= UMBRAL_RESUELTO:
                return o
    except Exception:
        pass
    return None


MAX_SLUGS_POR_CICLO = 150  # cap por ciclo -- muchas filas comparten market_slug
                            # (varias wallets en el mismo mercado), resolver por
                            # slug único evita pedir lo mismo N veces y acota el
                            # tiempo de ejecución (llamadas de red secuenciales).


def resolver_pendientes() -> int:
    """Mismo diseño que resuelve_ballenas_5min.py (/code-review 27-Jul): leer
    sin lock, resolver TODAS las llamadas de red sin lock, adquirir el lock
    solo para el tramo final de escritura (releer fresco por si el tracker
    añadió filas mientras tanto)."""
    if not OUT.exists():
        return 0
    with open(OUT, newline="", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))

    slugs_pendientes = sorted({r["market_slug"] for r in filas
                                if not r.get("outcome_real") and r.get("market_slug")})
    outcomes_por_slug = {}
    for slug in slugs_pendientes[:MAX_SLUGS_POR_CICLO]:
        outcome = outcome_por_slug(slug)
        if outcome is not None:
            outcomes_por_slug[slug] = outcome

    if not outcomes_por_slug:
        return 0

    lock_f = open(OUT_LOCK, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        try:
            with open(OUT, newline="", encoding="utf-8") as f:
                filas = list(csv.DictReader(f))
            resueltas = 0
            for r in filas:
                if r.get("outcome_real"):
                    continue
                outcome = outcomes_por_slug.get(r.get("market_slug"))
                if outcome is None:
                    continue
                r["outcome_real"] = outcome
                r["acierto"] = "1" if outcome == r.get("mirror_lado") else "0"
                r["resolved_ts"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
                resueltas += 1
            if resueltas:
                with open(OUT, "w", newline="", encoding="utf-8") as f:
                    w = csv.DictWriter(f, fieldnames=COLUMNS)
                    w.writeheader()
                    w.writerows(filas)
            return resueltas
        finally:
            fcntl.flock(lock_f, fcntl.LOCK_UN)
    finally:
        lock_f.close()


def main() -> int:
    wallets = cargar_wallets_validadas()
    _log(f"wallets validadas cargadas: {len(wallets)} (SEGUIR="
         f"{sum(1 for v in wallets.values() if v['tipo']=='SEGUIR')}, "
         f"FADE={sum(1 for v in wallets.values() if v['tipo']=='FADE')})")

    vistos = _vistos_cargar()
    nuevos, vistos = detectar_matches(wallets, vistos)
    _log(f"matches nuevos detectados: {len(nuevos)}")
    guardar(nuevos)
    _vistos_guardar(vistos)

    resueltas = resolver_pendientes()
    _log(f"resueltas este ciclo: {resueltas}")

    if OUT.exists():
        with open(OUT, newline="", encoding="utf-8") as f:
            filas = [r for r in csv.DictReader(f) if r.get("outcome_real")]
        if filas:
            n = len(filas)
            aciertos = sum(1 for r in filas if r["acierto"] == "1")
            n_seguir = sum(1 for r in filas if r["tipo"] == "SEGUIR")
            n_fade = n - n_seguir
            _log(f"acumulado resuelto: n={n} hit={aciertos/n*100:.1f}% "
                 f"(SEGUIR n={n_seguir}, FADE n={n_fade})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
