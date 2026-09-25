#!/usr/bin/env python3
"""
resolution_sniper_precierre_executor.py — ejecutor de baja latencia
RESOLUTION_SNIPER_PRECIERRE. Arquitectura obligatoria de
project_diseno_ejecutor_precierre_camino_critico_03sep (Javi, 03-Sep,
textual: "cuando toque ya sabes como lo tiene que hacer, grabatelo a
fuego"): todo lo caro se resuelve en la fase de PRECÁLCULO (T-12s del
instante objetivo), y en el INSTANTE objetivo (offset=-2s respecto al
cierre nominal) solo se hace 1 lectura de libro + firma + POST — nunca
pasa por live_trade._ejecutar_orden_polymarket. Ese camino genérico
gasta ~2s enteros en vetos de ballenas/re-quote/re-chequeo multi-lectura
(pensados para señales con ~20s de vida útil), y fue la causa real y
medida de que la prueba controlada del 03-Sep fallara con "trading is
disabled" exactamente en el segundo del cierre — NO fue el muro de
Polymarket, fue latencia propia (ver la memoria de diseño para el
desglose completo por tramo: GET/book 61ms, firma 3-6ms con caché
caliente, POST/order 180-277ms incl. taker delay).

Presupuesto medido 03-Sep (VPS Helsinki): camino crítico completo
~247ms mediana / ~380ms peor caso (con taker delay 50ms), ~347/480ms
desde el 04-Sep 14:00 UTC (taker delay sube a 150ms). Offset -2s da
2000ms de presupuesto → margen 4,2x sobre el peor caso medido.

DRY_RUN=True por defecto (04-Sep, construcción inicial): recorre TODO
el camino crítico incluida la FIRMA real (mide t_firma real, coste cero
— firmar no gasta nada ni se envía a ningún sitio) pero nunca llama a
post_order, así que no puede mover un solo euro. Pasar a DRY_RUN=False
requiere /code-review + aprobación EXPLÍCITA de Javi.

09-Sep (checklist de 6 categorías, fix real): esta tupla SÍ pasa ahora
por live_guard.puede_operar_live(STRATEGY, "{activo}#sniper") como
segunda guardia independiente del flag DRY_RUN, aplicada solo cuando
DRY_RUN=False (mismo criterio de doble protección que WALLET_MIRROR
cripto/weather y sports_wallet_mirror_sniper.py) -- antes se llamaba SIN
strategy/subtype en main(), lo que saltaba la comprobación de whitelist
por completo (strategy="" es falsy). Esta tupla no está en
pares_permitidos_live todavía (no promovida) -- con el fix, aunque
alguien pusiera DRY_RUN=False por error, ese guardián bloquearía el
envío igual que si DRY_RUN siguiera en True.

Sirve TAMBIÉN como medición continua de latencia in-situ (sustituye,
para el día a día, la repetición manual de medir_latencia_camino_
critico.py — esa herramienta sigue siendo la referencia para medir el
taker delay puro tras un cambio de infraestructura de Polymarket, pero
esto mide el camino real completo incluido el gate en cada ventana real):
cada intento evaluado (dispare orden o no) se registra en
data/shadow/resolution_sniper_precierre_executor_dryrun.csv con
t_lectura_ms/t_firma_ms y el veredicto del gate.

Gate: resolution_sniper_precierre_gate.evaluar(activo, ask, offset_s) —
relee el JSON del disco cada vez (caché por mtime), exige convergencia
grid+fino, fail-closed si no hay evidencia de ESE offset exacto. A
04-Sep solo BTC#5min tiene evidencia confirmada (n=74) — el resto de
activos se evalúan igual (nunca se hardcodea una tabla de zonas, ver F5
en project_lecciones_aprendidas_estrategias) y confirmarán solos en
cuanto n crezca lo suficiente.

23-Sep (validación con ask REAL de libro, memoria
idea_precierre_rafaga_multimoneda_validado_23sep, aprobado por Javi "ok,
adelante" -- sigue DRY_RUN=True): el criterio de decisión pasa a ser el
DETECTOR DE RÁFAGA, no el gate por activo (que solo tiene evidencia de 5min,
no distingue marco y confirma 5/212 claves -- se sigue evaluando y
registrando como `gate_legacy_*`, solo informativo):
  - fase A: se leen EN PARALELO los libros de las 6 monedas en el instante
    objetivo (dirección implícita Chainlink vs ref_open, ask del lado);
  - n_rafaga = monedas con dirección y ask en [ASK_RAFAGA_MIN, ASK_MAX);
  - dispara solo si n_rafaga >= MIN_MONEDAS_RAFAGA, ask en la banda de su
    marco y profundidad >= MIN_RATIO_PROFUNDIDAD.
Evidencia (offset -2s, 1€, fee 0,07·(1-p), outcome Chainlink): 5min n=1341
+0,63/tr 15/23 días+ (peor día -15,6€); 15min n=426 +0,89/tr 13/14 días+;
sin la guarda (1 moneda) los días tranquilos pierden. En 5min ask<0,20
pierde (n=54) -> banda propia por marco. Corre 5min y 15min en hilos
paralelos (misma cola Chainlink). 60min: n=25, no incluido todavía.
Pendiente de decisión de Javi antes de DRY_RUN=False: techo de correlación
en ráfaga (MAX_DISPAROS_POR_VENTANA) y sizing (peor día 5min -15,6€ a 1€).
"""
import csv
import threading
import time
from concurrent.futures import ThreadPoolExecutor, wait
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt
import live_guard
import live_stake
import resolution_sniper_precierre_gate as gate
import resolution_sniper_naive_executor_dryrun as _naive_viejo   # COMBOS_CONFIRMADOS / _veto_clv
import resolution_sniper_naive_gate_bucket as rsngb
from resolution_sniper_observer import ASSETS, mercado_slot, token_ids, _TAIL, resolver_universo

REPO = Path(__file__).resolve().parent
# 23-Sep: marcos en paralelo. (dur_s, marco_tag, subtype_suffix, ask_min_disparo)
MARCOS = {
    "5min": (300, "5m", "5min", 0.20),    # 5min: ask<0,20 pierde (n=54, -0,14/tr)
    "15min": (900, "15m", "15min", 0.05),
    # 23-Sep (petición Javi: "mete 60 minutos en dry-run con todas las monedas"): SOLO DRY_RUN
    # (MARCOS_SOLO_DRY_RUN, además no hay tuplas 60min en la whitelist). Retro (resolution_sniper_obs,
    # ask real -2s, ráfaga>=2): n=25, 9 cierres, 6/6 días, +0,86 €/tr -- n insuficiente para live.
    # Polymarket SOLO ofrece hourly Up/Down de BTC/ETH/SOL hoy (verificado 23-Sep: XRP/DOGE/BNB sin
    # mercado 2026; los slugs "{x}-up-or-down-..." que responden son de 2025, cerrados). Sin slug
    # determinista -> descubrimiento por universo (resolver_universo), marco_tag None.
    "60min": (3600, None, "60min", 0.05),
}
# Marcos que NUNCA envían aunque DRY_RUN=False: corte antes del POST en _firmar_enviar_registrar,
# sin reserva de hueco en _despachar (ni liberación), pools propios; además sin tuplas en whitelist.
MARCOS_SOLO_DRY_RUN = {"60min"}
# monedas con mercado en cada marco (por defecto ASSETS). 60min: solo BTC/ETH/SOL existen hoy -- buscar
# las demás en el universo era lento (preparar() 69s medido) y siempre vacío.
MONEDAS_POR_MARCO = {"60min": ["BTC", "ETH", "SOL"]}
# precálculo por marco: el descubrimiento de universo (60min) tarda ~11s la 1ª vez (luego caché)
PRECALCULO_ANTES_POR_MARCO_S = {"60min": 60}
ASK_RAFAGA_MIN = 0.05       # banda con la que se CUENTAN monedas para la ráfaga (la validada)
ASK_MAX = 0.80              # >=0,80 ya descontado (validado 23-Sep y guarda RSN 22-Sep)
MIN_MONEDAS_RAFAGA = 2
# 23-Sep (decisión Javi: "probamos con 2 y lo vamos subiendo poco a poco cuando tengamos más
# pnl"): hasta 2 órdenes por cierre, enviadas EN PARALELO (las 2 de más profundidad). Retro
# (ask real, 1€): techo 1 -> 15min +77,6€/5min +155,5€; techo 6 -> +378,7€/+856,9€ (peor
# cierre -2,1€/-6,2€). Cada orden adicional respeta además, en la MISMA reserva atómica, el
# techo de correlación (abiertas+enviadas en este cierre, misma dirección) y el margen del
# freno diario (stakes de este cierre descontados) -- ver _reservar_disparo.
MAX_DISPAROS_POR_VENTANA = 2
# /code-review 23-Sep: tope COMPARTIDO entre marcos por instante de cierre (a :00/:15/:30/:45
# cierran 5min y 15min a la vez, mismo movimiento Chainlink -> órdenes correlacionadas).
_disparos_por_cierre: dict = {}
_disparos_lock = threading.Lock()
# 23-Sep: mercados con orden enviada por ESTE proceso (precierre o naive) -- las guardas de
# ya_operados se precalculan en T-12s y no verían un disparo de T-2s; esto sí.
_mercados_enviados: set = set()
# Marca compartida ENTRE PROCESOS (lo lee resolution_sniper_naive_executor_dryrun.py antes de
# enviar): una línea market_id por orden intentada. Append atómico de una línea, sin lock.
RUTA_MARCAS_ENVIO = REPO / "data" / "live" / "precierre_mercados_enviados.txt"


def _marcar_enviado_disco(market_id: str) -> None:
    with open(RUTA_MARCAS_ENVIO, "a", encoding="utf-8") as f:
        f.write(f"{market_id}\n")
        f.flush()
# /code-review 23-Sep: un solo pool para ambos marcos (<=6 lecturas concurrentes: el pool de
# conexiones de la sesión HTTP compartida es 10; 12 simultáneas abrían TLS nuevo en el
# instante crítico) y tope de espera de las lecturas de fase A.
_POOL_LIBROS = ThreadPoolExecutor(max_workers=6, thread_name_prefix="libro_precierre")
# 23-Sep (techo >1): pool propio para los envíos -- cada envío bloquea en _verificar_fill_real
# (hasta ~4,5s); en serie, la 2ª orden saldría con el mercado ya cerrado.
_POOL_ENVIOS = ThreadPoolExecutor(max_workers=6, thread_name_prefix="envio_precierre")
# pools SEPARADOS para los marcos solo dry-run (60min): nunca compiten con los reales de 5/15min
_POOL_LIBROS_DRY = ThreadPoolExecutor(max_workers=3, thread_name_prefix="libro_precierre_dry")
_POOL_ENVIOS_DRY = ThreadPoolExecutor(max_workers=3, thread_name_prefix="envio_precierre_dry")


def _liberar_disparo(ts_end: int, direction: str, stake_eur: float) -> None:
    """Deshace una reserva de _reservar_disparo cuyo envío no llegó a hacer POST."""
    with _disparos_lock:
        e = _disparos_por_cierre.get(ts_end)
        if not e or e["n"] <= 0:
            return
        e["n"] -= 1
        e["dir"][direction] = max(0, e["dir"].get(direction, 0) - 1)
        e["stake"] = max(0.0, e["stake"] - stake_eur)


def _foto_vivo() -> dict:
    """/code-review 23-Sep (latencia): UNA lectura en vivo por ventana de config (whitelist,
    interruptor naive, ventana) + switch, compartida por todas las monedas del instante."""
    try:
        cfg = lt._cargar_config()
        en_v, _m = live_guard.en_ventana_horaria(cfg)
        return {"pares": set(cfg.get("pares_permitidos_live", [])), "switch": live_guard.switch_activo(),
                "en_ventana": en_v, "rapido": naive_camino_rapido_activo(cfg)}
    except Exception as e:
        return {"error": f"{type(e).__name__}"}


def _despachar(resultados: list, ts_end: int) -> None:
    """Recibe los resultados de decisión (ordenados por prioridad). Los que traen `_envio`
    (pasaron todas las guardas) reservan hueco EN ORDEN (_reservar_disparo: techo, correlación,
    freno diario) y los reservados se lanzan EN PARALELO sin esperarlos. /code-review 23-Sep:
    si la reserva rechaza un candidato, el hueco pasa al siguiente; si un envío falla antes del
    POST, su hueco se libera. Escribe el CSV con COPIAS (las filas de envío, al terminar)."""
    candidatos = [r for r in resultados if r.get("_envio")]
    lanzar = []
    for r in candidatos:
        if DRY_RUN or r.get("marco") in MARCOS_SOLO_DRY_RUN:
            lanzar.append(r)   # dry-run: sin reserva (nunca llega a POST, ver _firmar_enviar_registrar)
            continue
        if len(lanzar) >= MAX_DISPAROS_POR_VENTANA:
            r["gate_confirmado"], r["gate_motivo"] = False, "tope_disparos_ventana"
            continue
        ok, motivo = _reservar_disparo(ts_end, r["_dir"], float(r.get("stake_eur") or 0), r["_guardas"])
        if ok:
            r["_reservado"] = True   # SOLO lo reservado se puede liberar (/code-review 23-Sep, 60min)
            lanzar.append(r)
        else:
            r["gate_confirmado"], r["gate_motivo"] = False, motivo
    def _fila(r: dict, extra: str = "") -> dict:
        c = dict(r)   # copia atómica (C) -- nunca iterar el dict que un hilo aún puede escribir
        for k in ("_envio", "_dir", "_guardas", "_reservado"):
            c.pop(k, None)
        if extra:
            c["gate_motivo"] = f"{c.get('gate_motivo', '')}|{extra}"
        _append_csv({"timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
                     "ts_end": ts_end, **c,
                     "dry_run": DRY_RUN or c.get("marco") in MARCOS_SOLO_DRY_RUN})

    def _al_terminar(r: dict, f) -> None:
        # /code-review 23-Sep: el envío falló ANTES del POST (firma, reloj, CB, marca en disco) ->
        # liberar su hueco para que el naive de T+0 (u otro) pueda usarlo.
        # /code-review 23-Sep: liberar SOLO si este resultado reservó hueco (un dry-run de 60min,
        # que comparte ts_end con 5/15min cada hora, nunca reserva y jamás debe liberar huecos reales).
        if r.get("_reservado") and not r.get("disparado"):
            _liberar_disparo(ts_end, r["_dir"], float(r.get("stake_eur") or 0))
        err = f.exception()
        _fila(r, f"envio_excepcion:{type(err).__name__}" if err else "")

    # /code-review 23-Sep: NO se espera a los envíos (cada uno bloquea en _verificar_fill_real
    # hasta ~4,5s y retrasaba al naive del mismo cierre): la fila de cada envío se escribe al
    # terminar (callback); las no lanzadas se escriben ya.
    ids_lanzados = {id(r) for r in lanzar}
    for r in resultados:
        if id(r) not in ids_lanzados:
            _fila(r)
    for r in lanzar:
        pool = _POOL_ENVIOS_DRY if r.get("marco") in MARCOS_SOLO_DRY_RUN else _POOL_ENVIOS
        pool.submit(r["_envio"]).add_done_callback(lambda f, r=r: _al_terminar(r, f))
MAX_ESPERA_LECTURAS_S = 0.9   # lecturas que no llegan en 0,9s (desde T-2s) se descartan
MIN_MARGEN_PRECIERRE_S = 0.3  # si tras preparar() queda menos que esto hasta T-2s, ventana perdida
MARGEN_MIN_POST_S = 0.5       # nunca enviar la orden a menos de 0,5s del cierre nominal
# 23-Sep (checklist pre-live): prob. de acierto CONSERVADORA para el Kelly de calcular_stake --
# cota baja del hit validado con ráfaga (15min 93,7% n=426, 5min 87,0% n=1285), no la media.
P_ACIERTO_CONSERVADORA = {"5min": 0.84, "15min": 0.90, "60min": 0.90}   # 60min: 25/25 retro, cota prudente

# ---- 23-Sep: camino rápido RESOLUTION_SNIPER_NAIVE (petición explícita Javi: "tiene que enviar
# entre 0 y 3 segs después del cierre, arregla la latencia... a milisegundos"). El ejecutor viejo
# (resolution_sniper_naive_executor_dryrun.py vía observadores) decidía a T+4,1s de mediana y
# enviaba por _ejecutar_orden_polymarket (~1,5-2s más): llegaba con el libro ya cerrado ("trading
# is disabled", 59/59 el 01-Sep, enviadas a T+14s). Aquí: precálculo en T-12s, libros de las 6
# monedas en paralelo a T+0, quórum de ráfaga de golpe (sin esperar a otros hilos), firma caliente
# y POST FOK directo -> envío ~T+0,3-0,5s. Mismos gates que el viejo: combos confirmados,
# whitelist exacta BUY_Up/BUY_Down, ventana horaria, >=2 monedas fillable, ask<0,80, micro-bucket
# bueno_confirmado (rsngb), veto CLV, correlación, stake/freno, idempotencia.
# Interruptor ÚNICO compartido por ambos procesos (/code-review 23-Sep): clave de config_live.json
# "resolution_sniper_naive_camino_rapido" (True -> este proceso envía a T+0 y el ejecutor viejo
# delega). Leída en cada precálculo aquí y en cada decisión allí: nunca dos flags a sincronizar.
CLAVE_CONFIG_CAMINO_RAPIDO = "resolution_sniper_naive_camino_rapido"


def naive_camino_rapido_activo(cfg: dict | None = None) -> bool:
    try:
        cfg = cfg if cfg is not None else lt._cargar_config()
        return cfg.get(CLAVE_CONFIG_CAMINO_RAPIDO) is True
    except Exception:
        return False   # sin config legible: el camino rápido NO opera
STRATEGY_NAIVE = "RESOLUTION_SNIPER_NAIVE"
NAIVE_OFFSET_S = 0.0
# 24-Sep: el corte REAL del exchange está en ~+1,5 s tras el cierre (sondeo post-only aceptado a
# +0,19 s; accepting_orders=True hasta +1,5 s mediana en 15.702 ventanas; las 59/59 órdenes naive
# rechazadas eran a >=+2 s). Límite de envío +1,2 s.
NAIVE_MAX_ENVIO_S = 1.2
# 24-Sep: NAIVE con regla TWAP (ver MODO_TWAP): solo 5min (lo validado con curva_cierre 9-24 Sep:
# ask del ganador en [0,05,0,80) a T-1..+0,5 s, n~130, EV positivo; [0,80,0,97) EV -0,04).
NAIVE_TWAP_MARCOS = {"5min"}
NAIVE_TWAP_KILL_LATCH_NAME = "naive_twap_kill.json"
NAIVE_TWAP_DESDE_NAME = "naive_twap_desde.txt"
NAIVE_ASK_MIN, NAIVE_ASK_MAX_DET, NAIVE_ASK_MAX_OPERAR = 0.05, 0.95, 0.80
NAIVE_RATIO_MIN = 5.0
NAIVE_MIN_MONEDAS = 2
NAIVE_IC_PROXY = 0.15            # mismo ic_proxy que el ejecutor viejo para calcular_stake
# CLV: _veto_clv resetea la caché y tarda ~8,4s por llamada (medido 23-Sep) -- inasumible en el
# precálculo de T-12s. Se refresca en un hilo aparte; fail-closed si falta o está viejo.
CLV_REFRESCO_S = 600
CLV_MAX_EDAD_S = 1800
# /code-review 23-Sep: el refresco (~6-8s de CPU con el GIL) solo arranca lejos de cualquier
# cierre de 5min (ts%300 en esta franja), nunca solapando T-12s..T+3s.
CLV_FRANJA_SEGURA = (15, 240)
_clv_estado = {"ts": 0.0, "ok": False, "filas": {}}
_clv_lock = threading.Lock()


def _refrescar_clv_una_vez() -> None:
    """Carga UNA vez el CLV (misma fuente/filtros que lt._clv_tupla) y guarda solo las filas de
    las tuplas NAIVE, para evaluar por micro-bucket en caliente sin tocar disco a T+0."""
    lt._CLV_CACHE = None
    lt._clv_tupla(STRATEGY_NAIVE, "BTC#5min", "BUY_YES")   # fuerza la carga
    cache = lt._CLV_CACHE or {}
    filas = {}
    for (activo, marco) in _naive_viejo.COMBOS_CONFIRMADOS:
        for d in ("BUY_YES", "BUY_NO"):
            k = f"{STRATEGY_NAIVE}#{activo}#{marco}#{d}"
            filas[k] = list(cache.get(k, []))
    with _clv_lock:
        # fail-closed (/code-review): _clv_tupla traga errores de lectura y deja la caché vacía;
        # una caché vacía NO es "sin veto", es "no sé" -> ok=False veta todo.
        _clv_estado["ok"] = len(cache) > 0
        _clv_estado["filas"] = filas
        _clv_estado["ts"] = time.time()


def _hilo_clv() -> None:
    while True:
        try:
            if naive_camino_rapido_activo():
                while not (CLV_FRANJA_SEGURA[0] <= time.time() % 300 <= CLV_FRANJA_SEGURA[1]):
                    time.sleep(1)
                _refrescar_clv_una_vez()
            else:
                time.sleep(30)   # /code-review: interruptor apagado -> reintentar pronto, no 10 min
                continue
        except Exception as e:
            _log(f"refresco CLV falló ({type(e).__name__}: {e}) -- se mantiene el anterior (o veto por edad)")
        time.sleep(CLV_REFRESCO_S)


def _clv_veta(activo: str, marco: str, direction: str, py_yes: float) -> bool:
    """True = vetar. Mismo criterio que lt._clv_tupla(py=...) (11-Ago: por micro-bucket del precio
    YES, convención de results.csv). Fail-closed: sin carga válida o con más de CLV_MAX_EDAD_S."""
    with _clv_lock:
        if not _clv_estado["ok"] or time.time() - _clv_estado["ts"] > CLV_MAX_EDAD_S:
            return True
        filas = _clv_estado["filas"].get(f"{STRATEGY_NAIVE}#{activo}#{marco}#{direction}", [])
    b = lt._clv_bucket(py_yes)
    vals = [clv for precio, clv in filas if precio is not None and lt._clv_bucket(precio) == b]
    return bool(len(vals) >= lt.CLV_VETO_MIN_N and sum(vals) / len(vals) < 0)
# 24-Sep (Javi: "soluciona esto para que puedan operar"): a T-2s el lado ganador ya no tiene
# asks (0,14-0,21 % de lecturas) y los asks residuales eran trampas -- el mercado se resuelve por
# TWAP60 al cierre vs TWAP60 en la apertura (verificado: 99,3 % 5min / 99,6 % 15min en 10 días,
# analisis_precierre_twap_multidia_24sep.py), NO por spot vs spot de apertura como asumía este
# ejecutor. Modo nuevo: disparo a T-45s, dirección = TWAP PROYECTADO al cierre (media de ticks ya
# conocidos en [fin-60, ahora] + spot actual para el resto) vs TWAP de apertura, sin exigir
# ráfaga, ask real en [ASK_TWAP_MIN, ASK_TWAP_MAX). Validación 10 días, asks frescos <=10 s,
# 5min T-45s: acierto 95,7 %, EV +0,21 EUR/EUR (n=718, 9/10 días+); banda 0,25-0,65 ~+0,38.
OFFSET_S = -45
MODO_TWAP = True
# Banda validada (asks frescos <=10 s): 5min T-45 tramo 0,25-0,65 ~+0,38 EUR/EUR (n~205);
# 15min T-45 n=84 +0,32 (7/10 días+), con asks de <=25 s n=770 +0,46 (10/10). >=0,70: EV~0.
ASK_TWAP_MIN, ASK_TWAP_MAX = 0.25, 0.65
TWAP_N_MIN_TICKS = 20                    # ticks mínimos en [inicio-60, inicio] para fiarse del TWAP de apertura
TWAP_N_MIN_CIERRE = 10                   # ticks mínimos ya transcurridos en [fin-60, ahora] (/code-review)
TWAP_DESDE_PATH = REPO / "data" / "live" / "precierre_twap_desde.txt"   # arranque real del modo (kill-switch)
# 24-Sep (OK Javi "dale a exigir z>=1"): filtro de margen. Las 2 pérdidas del 24-Sep 12:15 eran
# photo finish (SOL +0,45 pb, DOGE +0,06 pb a T-44 s). z = |ln(proy/ref)| / (vol_1s * sqrt(var del
# promedio restante)). Validado 10 días, 5min T-45, asks frescos [0,25,0,65): z<0,5 acierto 55 %
# EV +0,06; z>=1 n=55 acierto 81-100 % EV +0,99 EUR/EUR. Naive (T+0, sin validar): mismo z con
# suelo de varianza de 15 s (error de medida vs TWAP oficial en empates).
Z_MIN_TWAP = 1.0
Z_VOL_VENTANA_S = 300
Z_VAR_SUELO_NAIVE_S = 15.0
TWAP_ERROR_VIGENTE_S = 1800              # filas ERROR cuentan como abiertas solo 30 min (luego las reconcilia
                                         # reconciliar_fill_fantasma.py o eran fantasmas sin dinero)
TWAP_KILL_N, TWAP_KILL_EUR = 20, 5.0     # n>=20 reales con media<0, o suma <= -5 EUR -> se cierra (latch)
TWAP_KILL_LATCH = REPO / "data" / "live" / "precierre_twap_kill.json"
STAKE_EUR = 1.05             # suelo CLOB, mismo criterio que la prueba controlada del 02-Sep
MIN_RATIO_PROFUNDIDAD = 5.0  # mismo umbral que el resto del proyecto
PRECALCULO_ANTES_S = 12      # arrancar precálculo con margen sobre el instante objetivo
# 23-Sep: DRY_RUN=False con aprobación EXPLÍCITA de Javi ("3 - ok", "vamos, venga") tras
# checklist pre-live + /code-review medium. Tuplas: 5min+15min x 6 monedas x 2 direcciones.
DRY_RUN = False
# 23-Sep (decisión explícita Javi: "para este caso en concreto puedes quitar los filtros
# horarios"): SOLO el PRECIERRE ignora las ventanas horarias (21% del PnL retro 15min y 36% del
# 5min caían fuera). Se mantienen switch, whitelist exacta, CB/freno diario, correlación.
# El camino rápido NAIVE (abajo) SÍ respeta ventanas, igual que su ejecutor original.
IGNORAR_VENTANAS_HORARIAS = True
STRATEGY = "RESOLUTION_SNIPER_PRECIERRE"

# 23-Sep: fichero nuevo (esquema con marco/ráfaga); el viejo queda como histórico.
OUT_LOG = REPO / "data" / "shadow" / "resolution_sniper_precierre_executor_v2.csv"
_CAMPOS = [
    "timestamp_utc", "ts_end", "marco", "dry_run", "activo", "direccion_implicita", "ask_implicita",
    "n_rafaga", "rafaga_ok", "en_banda", "gate_legacy_confirmado", "gate_legacy_motivo",
    "market_id",
    "gate_confirmado", "gate_motivo", "ratio_vs_stake", "vwap_fill_estimado",
    "whitelist_ok",  # 09-Sep, ver checklist de 6 categorías
    "t_lectura_ms", "t_firma_ms", "t_total_ms", "disparado", "order_ok", "order_error",
    "stake_eur", "t_guardas_ms",   # 23-Sep, al FINAL (ver _rotar_si_cabecera_distinta)
    "estrategia", "t_envio_rel_cierre_s", "z_twap",
]


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


_csv_lock = threading.Lock()


def _append_csv(row: dict) -> None:
    with _csv_lock:
        _append_csv_sin_lock(row)


_cabecera_verificada = False


def _rotar_si_cabecera_distinta() -> None:
    """/code-review 23-Sep: si el CSV existente tiene otra cabecera, las filas nuevas quedarían
    desalineadas en silencio -- se renombra a *_prev_<ts>.csv y se empieza uno nuevo."""
    if not OUT_LOG.exists() or OUT_LOG.stat().st_size == 0:
        return
    with open(OUT_LOG, encoding="utf-8") as f:
        cab = f.readline().strip().split(",")
    if cab != _CAMPOS:
        destino = OUT_LOG.with_name(f"{OUT_LOG.stem}_prev_{int(time.time())}.csv")
        OUT_LOG.rename(destino)
        _log(f"CSV con cabecera distinta rotado a {destino.name}")


def _append_csv_sin_lock(row: dict) -> None:
    global _cabecera_verificada
    if not _cabecera_verificada:
        _rotar_si_cabecera_distinta()
        _cabecera_verificada = True
    nuevo = not OUT_LOG.exists()
    with open(OUT_LOG, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=_CAMPOS)
        if nuevo:
            w.writeheader()
        w.writerow({k: row.get(k, "") for k in _CAMPOS})


class _Precalculo:
    """Todo lo caro de esta ventana, resuelto ANTES del instante objetivo:
    mercado/tokens por activo (Gamma API, cacheada por mercado_slot) y
    cliente CLOB calentado (paga aquí los 193-278ms de la PRIMERA firma,
    nunca en el disparo)."""

    def __init__(self, marco: str):
        self.marco = marco
        self.dur_s, self.marco_tag, self.subtype_suffix, self.ask_min = MARCOS[marco]
        self.ts_end = None
        self.guardas = {"ok": False, "motivo": "sin_precalculo"}
        self.vivo = None   # foto en vivo por ventana (_foto_vivo), se toma al empezar a decidir
        self.stake_ref = STAKE_EUR
        self.mercados = {}
        self.client = None

    def _precalcular_guardas(self) -> None:
        self.guardas = _guardas_precalculadas(self)
        stakes = [float(i.get("stake_eur") or 0) for i in self.guardas.get("stake", {}).values()
                  if i.get("viable")]
        self.stake_ref = max(stakes) if stakes else STAKE_EUR

    def preparar(self, ts_end: int) -> None:
        self.ts_end = ts_end
        ts_start = ts_end - self.dur_s
        self._precalcular_guardas()
        self.mercados = {}
        for activo in MONEDAS_POR_MARCO.get(self.marco, ASSETS):
            if self.marco_tag is None:
                # 60min: descubrimiento por universo (sin slug determinista), mismo mecanismo que
                # el observer; normaliza al formato de mercado_slot.
                u = resolver_universo(self.dur_s // 60, activo, ts_start, ts_end)
                if not u:
                    continue
                mkt = {"id": u["market_id"], "question": "", "conditionId": u["condition_id"],
                       "endDate": datetime.fromtimestamp(ts_end, timezone.utc).isoformat()}
                token_yes, token_no = u["token_yes"], u["token_no"]
            else:
                _slug, mkt = mercado_slot(activo, self.marco_tag, ts_start)
                if not mkt:
                    continue
                token_yes, token_no = token_ids(mkt)
            if not token_yes or not token_no:
                continue
            ref_open = _TAIL.precio_en(activo, ts_start) or _TAIL.precio_en(activo, ts_start + 2)
            ref_twap, n_twap = _media_tail(activo, ts_start - 60, ts_start)
            self.mercados[activo] = {
                "ref_twap": ref_twap if n_twap >= TWAP_N_MIN_TICKS else None,
                "market_id": mkt.get("id", ""), "question": mkt.get("question", ""),
                "end_date": mkt.get("endDate", ""),
                "token_yes": token_yes, "token_no": token_no, "ref_open": ref_open,
                "condition_id": mkt.get("conditionId", ""),  # 15-Sep: necesario para _verificar_fill_real
            }
        if self.client is None:
            try:
                self.client = lt._get_clob_client()
            except Exception as e:
                _log(f"aviso: no se pudo crear cliente CLOB ({e})")
                self.client = None
        if self.client is not None and self.mercados:
            try:
                from py_clob_client_v2 import MarketOrderArgsV2
                primer_token = next(iter(self.mercados.values()))["token_yes"]
                # firma de descarte a precio absurdo (nunca se envía) --
                # paga aquí el coste de la PRIMERA firma (fetch tick_size/
                # neg_risk), fuera del camino crítico.
                self.client.create_market_order(
                    MarketOrderArgsV2(token_id=primer_token, amount=STAKE_EUR, side="BUY", price=0.01))
            except Exception as e:
                _log(f"aviso: no se pudo calentar la firma ({e})")


def _guardas_precalculadas(pre) -> dict:
    """/code-review 23-Sep: todo lo que lee ficheros (trades.csv, config, bankroll) se resuelve
    en el PRECÁLCULO (T-12s), nunca en la ventana crítica de T-2s. Fail-closed: cualquier error
    deja las guardas bloqueando. Riesgo aceptado: ~10s de antigüedad; el CB se re-chequea igual
    antes del POST y hay un límite de reloj duro (MARGEN_MIN_POST_S)."""
    g = {"ok": False, "motivo": "sin_precalculo", "ya_operados": set(), "abiertas": {},
         "max_correl": 2, "stake": {}}
    try:
        g["ya_operados"] = lt._ya_operados_hoy()
        g["max_correl"] = lt._cargar_config().get("riesgo", {}).get("max_posiciones_abiertas_misma_direccion", 2)
        for d in ("BUY_YES", "BUY_NO"):
            g["abiertas"][d] = lt._posiciones_abiertas_misma_direccion(d)
            # Kelly con ask de referencia 0,50 (mediana validada); el stake queda capado por
            # max_pct_bankroll/max_stake en cualquier caso -- lo que importa aquí es freno/bankroll.
            p_ok = P_ACIERTO_CONSERVADORA[pre.marco]
            ic = max(0.0, (p_ok - 0.5) / 0.5)
            info = live_stake.calcular_stake(ic, STRATEGY, f"BTC#{pre.subtype_suffix}", direction=d,
                                             precio_entrada=0.5)
            g["stake"][d] = info
        # margen del freno diario / suelo de bankroll -- MISMA fórmula que calcular_stake (freno
        # prospectivo): lo que aún se puede perder hoy contando los stakes ya abiertos. Se descuenta
        # en memoria por cada orden reservada en el cierre (_reservar_disparo).
        cfg_m = lt._cargar_config()
        bkr_ini = live_stake.bankroll_inicio_dia()
        abiertos_eur = live_stake.stakes_abiertos_total()
        if bkr_ini <= 0:
            raise ValueError("bankroll_inicio_dia<=0")
        g["margen_dia"] = min(
            bkr_ini * live_stake.freno_diario_pct_hoy(cfg_m) + live_stake.pnl_live_hoy() - abiertos_eur,
            live_stake.bankroll_actual() - live_stake.bankroll_minimo_eur_hoy(cfg_m) - abiertos_eur)
        g["ok"], g["motivo"] = True, ""
    except Exception as e:
        g["ok"] = False   # fail-closed: ninguna guarda a medias
        g["motivo"] = f"error_precalculo:{type(e).__name__}:{e}"
    # --- naive: SEPARADO (/code-review 23-Sep) -- un fallo aquí bloquea SOLO al naive, nunca al
    # precierre; y solo se calcula si el camino rápido está activo (no alarga preparar() si no).
    g["naive_ok"], g["naive_motivo"] = False, "camino_rapido_inactivo"
    try:
        cfg = lt._cargar_config()
        if naive_camino_rapido_activo(cfg):
            g["naive_stake"] = {}
            for activo in ASSETS:
                if (activo, pre.marco) not in _naive_viejo.COMBOS_CONFIRMADOS:
                    continue
                for d in ("BUY_YES", "BUY_NO"):
                    g["naive_stake"][(activo, d)] = live_stake.calcular_stake(
                        NAIVE_IC_PROXY, STRATEGY_NAIVE, f"{activo}#{pre.subtype_suffix}", direction=d)
            g["naive_ok"], g["naive_motivo"] = True, ""
    except Exception as e:
        g["naive_ok"], g["naive_motivo"] = False, f"error_precalculo_naive:{type(e).__name__}:{e}"
    return g


def _profundidad_correcta(token_id: str, stake_eur: float) -> dict:
    """Mismo cálculo que live_trade._consultar_profundidad_libro (téco =
    mejor_ask*1.05, banda real sobre el precio de entrada), pero SIN pasar
    un precio_entrada adivinado: aquí se lee el libro UNA sola vez y se
    ancla el techo al mejor_ask REAL descubierto en esa misma lectura, no a
    un precio_entrada de partida. NO se toca _consultar_profundidad_libro
    (código de seguridad live, CLAUDE.md: no tocar para reutilizar parseo
    con código nuevo) — se replica su lógica aquí en su lugar.

    /code-review 04-Sep, hallazgo real: pasar precio_entrada=1.0 (para
    'cubrir todo el rango de precio' antes de conocer el ask) hacía
    techo=1.05 -- por encima del precio máximo posible (1.0) de un mercado
    binario, así que TODOS los niveles del libro entraban en la suma de
    profundidad, incluidos los que están lejísimos del precio real de
    fill. ratio_vs_stake medía la profundidad de TODO el libro, no la
    profundidad cerca del mejor ask (lo único que importa para una orden
    marketable) -- el gate de profundidad podía pasar con MIN_RATIO_
    PROFUNDIDAD=5.0 aunque el libro estuviera vacío justo donde se
    ejecutaría la orden."""
    book = lt._fetch_book_publico(token_id)
    if book is None:
        return {"ok": False, "error": "sin respuesta del libro (público)"}
    asks = book.get("asks") or []
    mejor_ask = None
    for lvl in asks:
        try:
            p = float(lvl.get("price"))
        except (TypeError, ValueError, AttributeError):
            continue
        if mejor_ask is None or p < mejor_ask:
            mejor_ask = p
    if mejor_ask is None:
        return {"ok": True, "mejor_ask": None, "profundidad_eur": 0.0, "n_niveles": len(asks),
                "ratio_vs_stake": 0.0, "vwap_fill_estimado": None, "fill_completo_en_niveles": False}
    techo = mejor_ask * 1.05
    profundidad_eur = 0.0
    for lvl in asks:
        try:
            p = float(lvl.get("price"))
            s = float(lvl.get("size"))
        except (TypeError, ValueError, AttributeError):
            continue
        if p <= techo:
            profundidad_eur += p * s
    ratio = (profundidad_eur / stake_eur) if stake_eur > 0 else None
    vwap_fill_estimado, fill_completo_en_niveles = lt.vwap_fill_desde_niveles(asks, stake_eur, mejor_ask)
    return {
        "ok": True, "mejor_ask": mejor_ask, "profundidad_eur": round(profundidad_eur, 2),
        "n_niveles": len(asks), "ratio_vs_stake": round(ratio, 1) if ratio is not None else None,
        "vwap_fill_estimado": vwap_fill_estimado, "fill_completo_en_niveles": fill_completo_en_niveles,
    }


CHAINLINK_MAX_EDAD_S = 2.0      # /code-review 23-Sep: nunca decidir con un precio más viejo
# naive: espera como mucho esto un tick con ts >= cierre - NAIVE_TICK_ANTES_CIERRE_S. Medido
# 23-Sep 16:55: el tick POSTERIOR al cierre llega a ~T+1,1s por la cola (fichero, poll 0,3s) y
# en BNB ni llegó en 1,2s -> retrasaba el envío ~1s. El edge a offset 0 está validado con el
# último tick disponible en T+0 (resolution_sniper_obs), así que basta un tick FRESCO del último
# 1,5s (protege igual contra websocket colgado: nunca un precio de más de 1,5s antes del cierre).
NAIVE_ESPERA_TICK_POST_S = 0.3
NAIVE_TICK_ANTES_CIERRE_S = 1.5


def _ultimo_tick(activo: str):
    """(ts_epoch, precio) del último tick Chainlink de la cola compartida, o None. Se lee la
    estructura interna de _TAIL (bajo su lock) para tener la marca de tiempo -- precio_ultimo()
    no la devuelve y es un módulo compartido que no se toca aquí."""
    with _TAIL._lock:
        dq = _TAIL._buf.get(activo)
        return dq[-1] if dq else None


def _media_tail(activo: str, t0: float, t1: float):
    """(media, n) de los ticks Chainlink con hora del ORÁCULO en [t0, t1] (/code-review: la
    validación usa ws_timestamp_ms, no la hora de recepción)."""
    with _TAIL._lock:
        dq = list(_TAIL._buf_oracle.get(activo, ()))
    vals = [p for t, p in dq if t0 <= t <= t1]
    return (sum(vals) / len(vals), len(vals)) if vals else (None, 0)


def _ultimo_oracle(activo: str):
    with _TAIL._lock:
        dq = _TAIL._buf_oracle.get(activo)
        return dq[-1] if dq else None


def _twap_proyectado(activo: str, ts_end: float):
    """TWAP60 al cierre proyectado, en tiempo del ORÁCULO: media de ticks de [ts_end-60, t_ult] +
    último spot para los segundos que faltan desde t_ult (idéntico a la validación multi-día).
    None si el último tick es viejo o faltan ticks en el tramo ya transcurrido (fail-closed)."""
    ult = _ultimo_oracle(activo)
    if ult is None or time.time() - ult[0] > CHAINLINK_MAX_EDAD_S + 2.0:
        return None
    t_ult, spot = ult
    t_hasta = min(t_ult, ts_end)   # /code-review: nunca ticks posteriores al cierre (naive a T+0)
    m, n = _media_tail(activo, ts_end - 60, t_hasta)
    resto = max(0.0, min(60.0, ts_end - t_hasta))
    if resto >= 60.0:
        return spot
    if m is None or n < TWAP_N_MIN_CIERRE:
        return None
    return (m * n + spot * resto) / (n + resto)


def _z_margen(activo: str, ts_end: float, proy: float, ref: float, suelo_var_s: float = 0.0):
    """z-score del margen del TWAP proyectado frente a la referencia (misma fórmula que la
    validación). None si no hay ticks suficientes para la volatilidad (fail-closed en el caller)."""
    import math
    ult = _ultimo_oracle(activo)
    if ult is None or proy <= 0 or ref <= 0:
        return None
    t_hasta = min(ult[0], ts_end)
    precios = []
    with _TAIL._lock:   # /code-review: recorrer desde el final, sin copiar el buffer entero (~15k ticks)
        for t, p in reversed(_TAIL._buf_oracle.get(activo, ())):
            if t < t_hasta - Z_VOL_VENTANA_S:
                break
            if t <= t_hasta and p > 0:
                precios.append(p)
    precios.reverse()
    if len(precios) < 60:
        return None
    rets = [math.log(b / a) for a, b in zip(precios, precios[1:])]
    media = sum(rets) / len(rets)
    vol = math.sqrt(sum((r - media) ** 2 for r in rets) / len(rets))
    resto = max(0.0, min(60.0, ts_end - t_hasta))
    var_s = max((resto / 60.0) ** 2 * resto / 3.0, suelo_var_s)
    if vol <= 0 or var_s <= 0:
        return None
    return abs(math.log(proy / ref)) / (vol * math.sqrt(var_s))


def _twap_desde(path=None) -> str:
    """Instante real de arranque del modo TWAP (persistente). Se crea la primera vez."""
    path = path or TWAP_DESDE_PATH
    try:
        if path.exists():
            return path.read_text(encoding="utf-8").strip()
        v = datetime.now(timezone.utc).isoformat(timespec="seconds")
        path.write_text(v, encoding="utf-8")
        return v
    except Exception:
        return "1970-01-01T00:00:00"   # fail-closed: cuenta TODOS los trades de la estrategia


def _kill_twap(strategy: str = None, latch=None, desde_path=None, etiqueta: str = "PRECIERRE") -> tuple[bool, str]:
    """(matado, motivo) del modo TWAP de `strategy` (por defecto el precierre). Latch persistente;
    fail-closed si el latch es ilegible o trades.csv no se puede leer."""
    import json
    strategy = strategy or STRATEGY
    TWAP_KILL_LATCH_ = latch or TWAP_KILL_LATCH
    desde = _twap_desde(desde_path or TWAP_DESDE_PATH)
    if TWAP_KILL_LATCH_.exists():
        try:
            d = json.loads(TWAP_KILL_LATCH_.read_text(encoding="utf-8"))
            if not isinstance(d, dict) or d.get("matado"):
                return True, (d or {}).get("motivo", "latch") if isinstance(d, dict) else "latch_corrupto"
        except Exception:
            return True, "latch_ilegible"
    pnls, abiertos = [], 0.0
    ahora = time.time()
    try:
        with open(lt.TRADES_CSV, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r.get("strategy") != strategy or (r.get("timestamp_utc") or "") < desde:
                    continue
                st = r.get("status")
                if st == "CLOSED":
                    try:
                        pnls.append(float(r["pnl_neto_eur"]))
                    except (KeyError, TypeError, ValueError):
                        pnls.append(-(float(r.get("stake_eur") or 0) or STAKE_EUR))
                elif st == "OPEN":
                    abiertos += float(r.get("stake_eur") or 0) or STAKE_EUR
                elif st == "ERROR":
                    try:
                        dt = datetime.fromisoformat(r["timestamp_utc"])
                        if dt.tzinfo is None:
                            dt = dt.replace(tzinfo=timezone.utc)   # /code-review: sin zona = UTC
                        edad = ahora - dt.timestamp()
                    except (KeyError, ValueError):
                        edad = 0.0   # ilegible: se cuenta (fail-closed)
                    if edad <= TWAP_ERROR_VIGENTE_S:
                        abiertos += float(r.get("stake_eur") or 0) or STAKE_EUR
    except Exception:
        return True, "trades_ilegible"
    motivo = ""
    if len(pnls) >= TWAP_KILL_N and sum(pnls) / len(pnls) < 0:
        motivo = f"media {sum(pnls)/len(pnls):+.3f} en n={len(pnls)} reales"
    elif sum(pnls) - abiertos <= -TWAP_KILL_EUR:
        motivo = f"peor caso {sum(pnls) - abiertos:+.2f} EUR (cerrados n={len(pnls)}, abiertos {abiertos:.2f})"
    if motivo:
        try:
            tmp = TWAP_KILL_LATCH_.with_name(TWAP_KILL_LATCH_.name + ".tmp")
            tmp.write_text(json.dumps({"matado": True, "motivo": motivo,
                                       "ts": datetime.now(timezone.utc).isoformat(timespec="seconds")}), encoding="utf-8")
            import os
            os.replace(tmp, TWAP_KILL_LATCH_)
            from shadow_digest import enviar_telegram
            enviar_telegram(f"🛑 {etiqueta} modo TWAP CERRADO por kill-switch: {motivo}")
        except Exception:
            pass
        return True, motivo
    return False, ""


def _leer(pre: _Precalculo, activo: str, ts_min: float | None = None) -> dict | None:
    """Fase A (paralela entre monedas): dirección implícita Chainlink + UNA
    lectura de libro del lado implícito. None si no hay mercado/precio.
    /code-review 23-Sep: precio con frescura verificada (<= CHAINLINK_MAX_EDAD_S) y, si se pasa
    ts_min (naive), SOLO un tick con ts >= ts_min (precio del cierre, no el previo)."""
    m = pre.mercados.get(activo)
    if not m or m["ref_open"] is None or m["ref_open"] <= 0:
        return None

    tick = _ultimo_tick(activo)
    if ts_min is not None and not MODO_TWAP:   # modo TWAP: la dirección sale del TWAP, no del tick post-cierre
        limite = time.time() + NAIVE_ESPERA_TICK_POST_S
        while (tick is None or tick[0] < ts_min) and time.time() < limite:
            time.sleep(0.02)
            tick = _ultimo_tick(activo)
        if tick is None or tick[0] < ts_min:
            return None
    if tick is None or time.time() - tick[0] > CHAINLINK_MAX_EDAD_S:
        return None
    precio_actual = tick[1]
    if MODO_TWAP:
        # modo TWAP (precierre y naive): regla real de resolución (TWAP fin vs TWAP apertura)
        if m.get("ref_twap") is None:
            return None
        proy = _twap_proyectado(activo, pre.ts_end)
        if proy is None:
            return None
        ref = m["ref_twap"]
        precio_actual = proy
        z_twap = _z_margen(activo, pre.ts_end, proy, ref,
                           Z_VAR_SUELO_NAIVE_S if ts_min is not None else 0.0)
    else:
        ref = m["ref_open"]
        z_twap = None
    if precio_actual > ref:
        dir_impl = "Up"
    elif precio_actual < ref:
        dir_impl = "Down"
    else:
        return None
    token_id = m["token_yes"] if dir_impl == "Up" else m["token_no"]

    # ÚNICA lectura de libro del instante crítico (~61ms mediana, /book
    # público, sin cliente autenticado) -- ver _profundidad_correcta() para
    # por qué no se usa live_trade._consultar_profundidad_libro aquí
    # directamente (habría que pasarle un precio_entrada adivinado).
    t0 = time.perf_counter()
    depth = _profundidad_correcta(token_id, pre.stake_ref)
    t_lectura_ms = (time.perf_counter() - t0) * 1000
    return {"activo": activo, "direccion_implicita": dir_impl, "token_id": token_id,
            "t_lectura_ms": round(t_lectura_ms, 1), "depth": depth,
            "market_id": m["market_id"], "z_twap": z_twap}


def _z_nota(lectura: dict | None) -> str:
    """25-Sep (Javi: 'nos va a servir para filtrar super bien'): deja el z de margen con el que se
    decidió la orden en `notas` de trades.csv (` z=1.83`, ` z=na` si no hay), para poder segmentar
    después el PnL real por z. Solo texto: no interviene en ninguna decisión ni puede lanzar."""
    try:
        z = (lectura or {}).get("z_twap")
        if z is None or z != z:   # None o NaN
            return " z=na"
        return f" z={float(z):.2f}"
    except (TypeError, ValueError):
        return " z=na"


def _cuenta_para_rafaga(lectura: dict | None) -> bool:
    if not lectura or not lectura["depth"].get("ok"):
        return False
    ask = lectura["depth"].get("mejor_ask")
    return ask is not None and ASK_RAFAGA_MIN <= ask < ASK_MAX


def _reservar_disparo(ts_end: int, direction: str, stake_eur: float, g: dict) -> tuple[bool, str]:
    """Reserva ATÓMICA por instante de cierre (compartida entre hilos, marcos y estrategias
    precierre/naive). Comprueba a la vez: (1) techo de disparos MAX_DISPAROS_POR_VENTANA;
    (2) techo de correlación: abiertas en esa dirección (foto T-12s) + ya reservadas en este
    cierre en esa dirección < max_posiciones_abiertas_misma_direccion; (3) freno diario: suma de
    stakes reservados en este cierre + este <= margen_dia (mismo cálculo que calcular_stake, foto
    T-12s). Fail-closed si falta cualquier dato."""
    with _disparos_lock:
        for k in [k for k in _disparos_por_cierre if k < ts_end - 3600]:
            del _disparos_por_cierre[k]
        e = _disparos_por_cierre.setdefault(ts_end, {"n": 0, "dir": {}, "stake": 0.0})
        if e["n"] >= MAX_DISPAROS_POR_VENTANA:
            return False, "tope_disparos_ventana"
        abiertas = g.get("abiertas", {}).get(direction)
        max_correl = g.get("max_correl")
        margen = g.get("margen_dia")
        if abiertas is None or max_correl is None or margen is None:
            return False, "reserva_sin_datos"
        if abiertas + e["dir"].get(direction, 0) >= max_correl:
            return False, f"techo_correlacion_{direction}_en_cierre"
        if e["stake"] + stake_eur > margen + 0.005:   # calcular_stake redondea a 2 decimales
            return False, f"freno_diario_margen={margen:.2f}_usado={e['stake']:.2f}"
        e["n"] += 1
        e["dir"][direction] = e["dir"].get(direction, 0) + 1
        e["stake"] += stake_eur
        return True, ""


def _firmar_enviar_registrar(pre: "_Precalculo", m: dict, activo: str, direction: str, token_id: str,
                             ask: float, stake_eur: float, strategy: str, notas_base: str,
                             resultado: dict, limite_envio_ts: float, t_lectura_ms: float) -> dict:
    """23-Sep: tramo firma -> [DRY_RUN corta aquí] -> límite de reloj -> CB -> POST FOK ->
    verificación de fill real -> registro, COMPARTIDO por PRECIERRE (T-2s) y el camino rápido
    NAIVE (T+0s). Extraído sin cambios de lógica de _instante_critico (antes inline)."""
    from py_clob_client_v2 import MarketOrderArgsV2, OrderType
    # 23-Sep fix: `ask` ya es el mejor ask del TOKEN comprado (YES o NO) y la
    # convención de trades.csv es entry_price = precio del token comprado; el
    # antiguo `1.0 - ask` para Down registraba entrada/slip erróneos si faltaba
    # trade_real (latente, DRY_RUN).
    precio_orden = ask
    t1 = time.perf_counter()
    try:
        args = MarketOrderArgsV2(token_id=token_id, amount=stake_eur, side="BUY", price=ask)
        signed = pre.client.create_market_order(args)
        t_firma_ms = (time.perf_counter() - t1) * 1000
    except Exception as e:
        resultado["gate_confirmado"] = False
        resultado["gate_motivo"] = f"error_firma:{e}"
        return resultado
    resultado["t_firma_ms"] = round(t_firma_ms, 1)

    if DRY_RUN or pre.marco in MARCOS_SOLO_DRY_RUN:
        resultado["disparado"] = False
        resultado["dry_run"] = True   # la fila CSV refleja el dry-run por marco (60min)
        _log(f"[DRY-RUN] {strategy} {pre.marco} {activo} {direction} ask={ask} {notas_base} "
             f"t_lectura={t_lectura_ms:.0f}ms t_firma={t_firma_ms:.0f}ms -- NO se envía (dry-run)")
        return resultado

    # ---- Solo alcanzable con DRY_RUN=False, tras /code-review + aprobación explícita de Javi ----
    # /code-review 23-Sep: límite de reloj DURO -- si ya no queda margen hasta el cierre, no se
    # envía (el libro cierra en endDate exacto: "trading is disabled", ver RSN naive).
    if time.time() > limite_envio_ts:
        resultado["gate_confirmado"] = False
        resultado["gate_motivo"] = "sin_margen_reloj_antes_post"
        return resultado
    # /code-review 23-Sep: re-chequeo del circuit breaker JUSTO antes de enviar (el del bucle
    # puede tener hasta ~15 min en el hilo de 15min) -- mismo fix que dispersed 07-Sep.
    try:
        cb_disparado, cb_motivo = live_stake.verificar_circuit_breaker()
    except Exception as e:
        cb_disparado, cb_motivo = True, f"error_verificando:{e}"   # fail-closed
    if cb_disparado:
        resultado["gate_confirmado"] = False
        resultado["gate_motivo"] = f"circuit_breaker:{cb_motivo}"
        return resultado
    # (La reserva del hueco -- techo/correlación/freno -- la hace _despachar ANTES de lanzar este
    # envío, en orden de prioridad; con DRY_RUN=False nunca se llega aquí sin reserva.)
    # /code-review 23-Sep: el CB y la reserva leen ficheros (20-130ms con carga) -- último
    # chequeo de reloj JUSTO antes del POST.
    if time.time() > limite_envio_ts:
        resultado["gate_confirmado"] = False
        resultado["gate_motivo"] = "sin_margen_reloj_antes_post"
        return resultado
    # /code-review 23-Sep: marca EN DISCO antes del POST para que el ejecutor naive viejo (otro
    # proceso) no envíe una segunda orden al mismo mercado mientras trades.csv aún no la refleja.
    try:
        _marcar_enviado_disco(m["market_id"])
    except Exception as e:
        resultado["gate_confirmado"] = False
        resultado["gate_motivo"] = f"error_marca_disco:{type(e).__name__}"   # fail-closed
        return resultado
    t2 = time.perf_counter()
    try:
        resp = pre.client.post_order(signed, OrderType.FOK)
        ok, error = True, None
    except Exception as e:
        resp, ok, error = None, False, str(e)
    t_post_ms = (time.perf_counter() - t2) * 1000
    resultado["t_envio_rel_cierre_s"] = round(time.time() - pre.ts_end, 3)
    # /code-review 23-Sep: marcar SIEMPRE tras intentar el POST -- una excepción (timeout) puede
    # ocultar una orden que sí llegó al exchange; sin saberlo, nunca reenviar al mismo mercado.
    with _disparos_lock:
        _mercados_enviados.add(m["market_id"])
    resultado["disparado"] = True
    resultado["order_error"] = error
    resultado["t_total_ms"] = round(t_lectura_ms + (resultado.get("t_guardas_ms") or 0) + t_firma_ms + t_post_ms, 1)

    # 15-Sep (hallazgo real, barrido de salud pedido por Javi: "no quiero
    # un trade fantasma en ningún repo"): `ok=True` en cuanto post_order()
    # no lanza excepción NUNCA es suficiente -- puede devolver una
    # respuesta con orderID sin haber casado con contraparte (mismo hueco
    # que causó el trade fantasma real de sports el 31-Ago, ya corregido
    # en live_trade.py/sports_live_trade.py/weather_live_trade.py el mismo
    # día que este). Este ejecutor lo tenía sin corregir -- dormido porque
    # DRY_RUN=True, pero listo para repetir el mismo incidente en cuanto
    # alguien lo activara. Verificación real contra get_trades() antes de
    # registrar nada, fail-closed, reusando la misma función que ya usan
    # los otros tres ejecutores (un solo punto de verdad).
    trade_real = None
    sin_fill_confirmado = False
    if ok:
        order_id = resp.get("orderID") or resp.get("id") or str(resp)
        ts_envio = time.time()
        trade_real = lt._verificar_fill_real(pre.client, m.get("condition_id", ""), order_id, ts_envio)
        if trade_real is None:
            # /code-review 15-Sep, hallazgo real: ok=False aquí NO debe
            # dejar la orden sin ningún rastro -- mismo criterio que
            # _ejecutar_orden_polymarket (live_trade.py, 01-Sep): la API SÍ
            # aceptó la orden, un falso negativo de get_trades() (indexado
            # lento) es indistinguible aquí de un fantasma real, así que se
            # registra una fila ERROR (nunca OPEN) para dejar rastro
            # reconciliable en vez de un aviso de Telegram sin ningún
            # registro en trades.csv.
            ok = False
            sin_fill_confirmado = True
            error = "orden aceptada por la API pero sin evidencia de fill real en get_trades()"
            _log(f"  ⛔ {activo} {direction} orden aceptada (order_id={order_id}) pero SIN evidencia "
                 f"de fill real -- fail-closed, se registra como ERROR (no OPEN)")
            lt.enviar_telegram(
                f"⚠️ {strategy}\nOrden aceptada pero sin fill confirmado (posible fantasma)\n"
                f"activo={activo} direction={direction} order_id={order_id}\n"
                f"Registrada como ERROR (no OPEN) -- revisar manualmente contra get_trades()/Polygonscan."
            )
    resultado["order_ok"] = ok
    _log(f"ORDEN REAL {strategy} {pre.marco} {activo} {direction} ask={ask} t_envio_rel={resultado['t_envio_rel_cierre_s']}s -> ok={ok} resp={str(resp)[:120]} "
         f"t_lectura={t_lectura_ms:.0f}ms t_firma={t_firma_ms:.0f}ms t_post={t_post_ms:.0f}ms "
         f"error={error}")

    # Se registra siempre que la API haya llegado a aceptar la orden
    # (resp is not None) -- OPEN si el fill se verificó, ERROR si no. Un
    # FOK kill (resp sigue None, la excepción ya viene en `error`) nunca
    # llegó a existir en el exchange y no se registra, igual que el resto
    # del proyecto.
    if resp is not None:
        filled_price = float(trade_real.get("price", precio_orden)) if trade_real else precio_orden
        fee_rate_bps = (trade_real.get("fee_rate_bps") if trade_real else None) or 0
        notas = (f"{strategy} {pre.marco} {notas_base} t_envio_rel={resultado['t_envio_rel_cierre_s']}s "
                 f"t_total={resultado['t_total_ms']}ms")
        if sin_fill_confirmado:
            notas += " | sin_fill_confirmado=1 (revisar manualmente)"
        trade = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "market_id": m["market_id"], "question": m["question"], "end_date": m["end_date"],
            "strategy": strategy, "subtype": f"{activo}#{pre.subtype_suffix}", "direction": direction,
            "stake_eur": stake_eur, "entry_price": filled_price,
            "signal_ask": round(ask, 4), "slip_real": round(filled_price - precio_orden, 4),
            "ic_modelo": "", "edge_neto": "", "conviction_score": "", "kelly_recomendado": stake_eur,
            "status": "OPEN" if ok else "ERROR",
            "close_timestamp": "", "exit_price": "", "outcome_real": "",
            "fee_eur": round(float(fee_rate_bps) / 10000 * stake_eur, 4) if fee_rate_bps else 0.0,
            "pnl_bruto_eur": "", "pnl_neto_eur": "",
            "notas": notas,
        }
        lt._registrar_trade(trade)
    # 23-Sep (petición Javi): aviso de CADA orden real, ejecutada o rechazada -- fuera del camino
    # crítico (el POST ya salió). Un fallo de Telegram nunca afecta a la orden ni al registro.
    try:
        if ok:
            lt.enviar_telegram(
                f"🎯 *Orden live ejecutada ({strategy})*\n"
                f"{strategy}#{activo}#{pre.subtype_suffix}#{direction}\n"
                f"Precio fill: {filled_price:.4f} (ask {ask:.4f})  |  Stake: {stake_eur:.2f}$\n"
                f"Envío T{resultado['t_envio_rel_cierre_s']:+.3f}s respecto al cierre  |  {notas_base}")
        elif not sin_fill_confirmado:
            lt.enviar_telegram(
                f"❌ *Orden live NO ejecutada ({strategy})*\n"
                f"{strategy}#{activo}#{pre.subtype_suffix}#{direction} ask={ask:.4f}\n"
                f"Envío T{resultado['t_envio_rel_cierre_s']:+.3f}s respecto al cierre\n"
                f"{str(error)[:200]}")
    except Exception as e:
        _log(f"  aviso Telegram falló ({type(e).__name__}: {e}) -- la orden no se ve afectada")
    return resultado


def _instante_critico(pre: _Precalculo, lectura: dict, n_rafaga: int, ts_end: int) -> dict:
    """Fase B: decisión + firma (+ POST solo si DRY_RUN=False) para UNA moneda
    ya leída en fase A. Criterio 23-Sep: ráfaga + banda de ask + profundidad."""
    activo = lectura["activo"]
    m = pre.mercados[activo]
    dir_impl = lectura["direccion_implicita"]
    direction = "BUY_YES" if dir_impl == "Up" else "BUY_NO"
    token_id = lectura["token_id"]
    depth = lectura["depth"]
    t_lectura_ms = lectura["t_lectura_ms"]
    base = {"activo": activo, "direccion_implicita": dir_impl, "t_lectura_ms": t_lectura_ms,
            "marco": pre.marco, "n_rafaga": n_rafaga, "market_id": lectura["market_id"],
            "estrategia": STRATEGY, "z_twap": lectura.get("z_twap")}
    if not depth.get("ok"):
        return {**base, "gate_confirmado": False, "gate_motivo": "sin_libro"}

    ask = depth.get("mejor_ask")
    if ask is None:
        return {**base, "gate_confirmado": False, "gate_motivo": "sin_ask"}

    # gate por activo (legacy, solo 5min, no distingue marco): solo informativo desde 23-Sep
    veredicto = gate.evaluar(activo, ask, OFFSET_S)
    ratio = depth.get("ratio_vs_stake")
    if MODO_TWAP:
        rafaga_ok = True   # modo TWAP: cada moneda por su cuenta (lo validado es por mercado)
        en_banda = ASK_TWAP_MIN <= ask < ASK_TWAP_MAX
    else:
        rafaga_ok = n_rafaga >= MIN_MONEDAS_RAFAGA
        en_banda = pre.ask_min <= ask < ASK_MAX
    resultado = {
        **base, "ask_implicita": ask, "rafaga_ok": rafaga_ok, "en_banda": en_banda,
        "gate_legacy_confirmado": veredicto["confirmado"], "gate_legacy_motivo": veredicto["motivo"],
        "gate_confirmado": False, "gate_motivo": "",
        "ratio_vs_stake": ratio, "vwap_fill_estimado": depth.get("vwap_fill_estimado"),
    }
    if not rafaga_ok:
        resultado["gate_motivo"] = f"sin_rafaga_n={n_rafaga}"
        return resultado
    if not en_banda:
        resultado["gate_motivo"] = f"fuera_banda_ask={ask}"
        return resultado
    if MODO_TWAP:
        z = lectura.get("z_twap")
        if z is None or z < Z_MIN_TWAP:
            resultado["gate_motivo"] = f"z_bajo={None if z is None else round(z, 2)}"
            return resultado
    if ratio is None or ratio < MIN_RATIO_PROFUNDIDAD:
        resultado["gate_motivo"] = f"profundidad_insuficiente_ratio={ratio}"
        return resultado
    # ---- 23-Sep, checklist pre-live: mismas guardas estructurales que el resto de
    # ejecutores live (dispersed/wallet_mirror). Se evalúan también en DRY_RUN para
    # medir cuántas veces habrían bloqueado (el motivo queda en el CSV).
    t_g0 = time.perf_counter()
    g = pre.guardas
    if not g.get("ok"):
        resultado["gate_motivo"] = f"guardas:{g.get('motivo')}"
        return resultado
    if m["market_id"] in g["ya_operados"] or m["market_id"] in _mercados_enviados:
        resultado["gate_motivo"] = "ya_operado"
        return resultado
    if g["abiertas"].get(direction, 99) >= g["max_correl"]:
        resultado["gate_motivo"] = f"techo_correlacion_{direction}"
        return resultado
    stake_info = g["stake"].get(direction) or {}
    if not stake_info.get("viable") or float(stake_info.get("stake_eur") or 0) < 1.0:
        resultado["gate_motivo"] = f"stake_no_viable:{stake_info.get('motivo')}"
        return resultado
    stake_eur = float(stake_info["stake_eur"])
    resultado["stake_eur"] = stake_eur
    if depth.get("profundidad_eur") is not None and depth["profundidad_eur"] < MIN_RATIO_PROFUNDIDAD * stake_eur:
        resultado["gate_motivo"] = f"profundidad_insuficiente_para_stake={stake_eur}"
        return resultado
    resultado["t_guardas_ms"] = round((time.perf_counter() - t_g0) * 1000, 2)
    # DRY_RUN: sin tope -- se registran TODAS las monedas de la ráfaga (lo validado es la
    # ráfaga entera, /code-review 23-Sep). Live: tope compartido entre marcos.
    if MODO_TWAP:
        matado, motivo_kill = _kill_twap()
        if matado:
            resultado["gate_motivo"] = f"kill_twap:{motivo_kill}"
            return resultado
    resultado["gate_confirmado"] = True
    resultado["gate_motivo"] = "twap_proy" if MODO_TWAP else f"rafaga_n={n_rafaga}"
    # 09-Sep (checklist de 6 categorías, hallazgo real): main() llamaba a
    # live_guard.puede_operar_live() SIN strategy/subtype -- con strategy=""
    # (falsy), la comprobación `if strategy and not estrategia_permitida(...)`
    # de live_guard.py nunca se evalúa, así que pares_permitidos_live queda
    # sin comprobar del todo. El docstring del módulo (líneas 30-31) decía
    # explícitamente que esto era intencional ("el flag de módulo gobierna
    # con independencia de pares_permitidos_live") -- pero rompe la doble
    # protección que exige el resto del proyecto para código de dinero real
    # (WALLET_MIRROR cripto/weather, sports: SIEMPRE dos guardias
    # independientes, para que un DRY_RUN=False accidental no baste solo).
    # Solo se APLICA como bloqueo con DRY_RUN=False -- con DRY_RUN=True esta
    # tupla nunca está en pares_permitidos_live (a propósito, no promovida
    # todavía), y bloquear aquí también en DRY_RUN mataría el propósito
    # explícito del modo (medir el camino crítico completo, incluida la
    # firma real, sin gastar dinero -- ver docstring del módulo). Se sigue
    # auditando SIEMPRE en el CSV (whitelist_ok), solo con DRY_RUN=True.
    # /code-review 09-Sep, hallazgo real: "sniper" no es el subtype real --
    # el registro de trades (más abajo) usa f"{activo}#{SUBTYPE_SUFFIX}"
    # ("BTC#5min"), igual que el resto del proyecto (ballenas_executor_*,
    # wallet_mirror_executor_dryrun.py, config_live.json). Con "sniper" el
    # prefijo nunca habría coincidido con una futura entrada real en
    # pares_permitidos_live -- fail-closed (no es un riesgo de dinero),
    # pero habría bloqueado la promoción para siempre en silencio.
    subtype_whitelist = f"{activo}#{pre.subtype_suffix}"
    # /code-review 23-Sep (latencia): switch + whitelist EXACTA con dirección (+ ventana si no se
    # ignora) desde UNA foto en vivo por ventana (pre.vivo, tomada al empezar a decidir), no 3
    # lecturas de disco por moneda. Fail-closed si la foto falló.
    v = pre.vivo or {"error": "sin_foto"}
    tupla_exacta = f"{STRATEGY}#{subtype_whitelist}#{direction}"
    if v.get("error"):
        ok_whitelist, motivo_whitelist = False, f"foto_vivo:{v['error']}"
    elif not v["switch"]:
        ok_whitelist, motivo_whitelist = False, "switch_OFF"
    elif tupla_exacta not in v["pares"]:
        ok_whitelist, motivo_whitelist = False, f"{tupla_exacta} no está en lista de permitidos"
    elif not IGNORAR_VENTANAS_HORARIAS and not v["en_ventana"]:
        ok_whitelist, motivo_whitelist = False, "fuera_ventana_horaria"
    else:
        ok_whitelist, motivo_whitelist = True, "ok"
    resultado["whitelist_ok"] = ok_whitelist
    # 60min (MARCOS_SOLO_DRY_RUN): no se bloquea aquí para que el dry-run llegue a firmar y medir;
    # nunca envía (corte en _firmar_enviar_registrar) ni reserva/libera huecos (_despachar).
    if not DRY_RUN and not ok_whitelist and pre.marco not in MARCOS_SOLO_DRY_RUN:
        resultado["gate_confirmado"] = False
        resultado["gate_motivo"] = f"no_permitido:{motivo_whitelist}"
        return resultado
    if pre.client is None:
        resultado["gate_confirmado"] = False
        resultado["gate_motivo"] = "sin_cliente_clob"
        return resultado

    # 23-Sep (techo >1): no se envía aquí -- se devuelve el envío preparado para que
    # _despachar reserve hueco en orden de prioridad y lance a la vez los reservados.
    resultado["_dir"], resultado["_guardas"] = direction, pre.guardas
    resultado["_envio"] = lambda: _firmar_enviar_registrar(
        pre, m, activo, direction, token_id, ask, stake_eur, STRATEGY,
        (f"modo=twap_proy offset={OFFSET_S}s{_z_nota(lectura)}" if MODO_TWAP else f"offset={OFFSET_S}s rafaga_n={n_rafaga}{_z_nota(lectura)}"), resultado,
        pre.ts_end - MARGEN_MIN_POST_S, t_lectura_ms)
    return resultado


def _naive_fillable(l: dict | None) -> bool:
    """Mismo criterio de 'detección fillable' que el ejecutor viejo/análisis (ask en
    [0,05,0,95] y ratio>=5x) -- es lo que cuenta para el quórum de >=2 monedas."""
    if not l or not l["depth"].get("ok"):
        return False
    ask, ratio = l["depth"].get("mejor_ask"), l["depth"].get("ratio_vs_stake")
    return (ask is not None and NAIVE_ASK_MIN <= ask <= NAIVE_ASK_MAX_DET
            and ratio is not None and ratio >= NAIVE_RATIO_MIN)


def _instante_naive(pre: _Precalculo, lectura: dict, n_det: int, ts_end: int) -> dict:
    """Decisión NAIVE para una moneda ya leída a T+0 (sin I/O de disco: todo precalculado)."""
    activo = lectura["activo"]
    m = pre.mercados[activo]
    dir_impl = lectura["direccion_implicita"]
    direction = "BUY_YES" if dir_impl == "Up" else "BUY_NO"
    depth = lectura["depth"]
    ask = depth.get("mejor_ask")
    ratio = depth.get("ratio_vs_stake")
    sub = f"{activo}#{pre.subtype_suffix}"
    r = {"activo": activo, "direccion_implicita": dir_impl, "t_lectura_ms": lectura["t_lectura_ms"],
         "marco": pre.marco, "n_rafaga": n_det, "market_id": lectura["market_id"],
         "estrategia": STRATEGY_NAIVE, "ask_implicita": ask, "ratio_vs_stake": ratio,
         "z_twap": lectura.get("z_twap"),
         "vwap_fill_estimado": depth.get("vwap_fill_estimado"),
         "gate_confirmado": False, "gate_motivo": ""}

    def _no(motivo: str) -> dict:
        r["gate_motivo"] = motivo
        return r

    t_g0 = time.perf_counter()
    g = pre.guardas
    if not g.get("ok"):
        return _no(f"guardas:{g.get('motivo')}")
    if not g.get("naive_ok"):
        return _no(f"guardas_naive:{g.get('naive_motivo')}")
    if not MODO_TWAP and (activo, pre.marco) not in _naive_viejo.COMBOS_CONFIRMADOS:
        return _no("combo_no_confirmado")
    if not _naive_fillable(lectura):
        return _no(f"no_fillable_ask={ask}_ratio={ratio}")
    # 24-Sep: en modo TWAP no se exige quórum (validación por mercado) y no aplican combos, gate
    # rsngb ni CLV: salen de historia con la dirección SPOT (regla equivocada, 89 %).
    r["rafaga_ok"] = MODO_TWAP or n_det >= NAIVE_MIN_MONEDAS
    if not r["rafaga_ok"]:
        return _no(f"deteccion_aislada_n={n_det}")
    r["en_banda"] = ask < NAIVE_ASK_MAX_OPERAR
    if not r["en_banda"]:
        return _no(f"ask>={NAIVE_ASK_MAX_OPERAR}")
    if MODO_TWAP:
        z = lectura.get("z_twap")
        if z is None or z < Z_MIN_TWAP:
            return _no(f"z_bajo={None if z is None else round(z, 2)}")
    if MODO_TWAP:
        # /code-review: calculado UNA vez por ventana antes de T+0 (procesar_ventana_naive), sin I/O aquí
        matado, motivo_kill = getattr(pre, "naive_kill", (True, "sin_calcular"))
        if matado:
            return _no(f"kill_twap:{motivo_kill}")
    else:
        gb = rsngb.evaluar(activo, pre.marco, dir_impl, ask)
        r["gate_legacy_motivo"] = f"rsngb={gb.get('veredicto')}"
        if gb.get("veredicto") != "bueno_confirmado":
            return _no(f"micro_bucket={gb.get('veredicto')}")
        py_yes = ask if dir_impl == "Up" else round(1.0 - ask, 6)   # convención results.csv (precio YES)
        if _clv_veta(activo, pre.marco, direction, py_yes):
            return _no("veto_clv")
    if m["market_id"] in g["ya_operados"] or m["market_id"] in _mercados_enviados:
        return _no("ya_operado")
    if g["abiertas"].get(direction, 99) >= g["max_correl"]:
        return _no(f"techo_correlacion_{direction}")
    stake_info = g["naive_stake"].get((activo, direction)) or {}
    if not stake_info.get("viable") or float(stake_info.get("stake_eur") or 0) < 1.0:
        return _no(f"stake_no_viable:{stake_info.get('motivo')}")
    stake_eur = float(stake_info["stake_eur"])
    r["stake_eur"] = stake_eur
    if depth.get("profundidad_eur") is None or depth["profundidad_eur"] < NAIVE_RATIO_MIN * stake_eur:
        return _no(f"profundidad_insuficiente_para_stake={stake_eur}")
    # /code-review 23-Sep: switch, whitelist exacta y ventana EN VIVO (no la foto de T-12s) --
    # un /off o una retirada de la whitelist tiene efecto hasta el último instante.
    v = pre.vivo or {"error": "sin_foto"}   # UNA foto en vivo por ventana (ver _foto_vivo)
    if v.get("error"):
        return _no(f"error_guardas_vivo:{v['error']}")
    tupla = f"{STRATEGY_NAIVE}#{sub}#BUY_{dir_impl}"
    r["whitelist_ok"] = tupla in v["pares"]
    switch_ok, en_ventana, rapido_ok = v["switch"], v["en_ventana"], v["rapido"]
    if not rapido_ok:
        return _no("camino_rapido_desactivado")
    if not DRY_RUN and not switch_ok:
        return _no("switch_OFF")
    if not DRY_RUN and not r["whitelist_ok"]:
        return _no(f"no_permitido:{tupla}")
    if not en_ventana:
        return _no("fuera_ventana_horaria")
    r["t_guardas_ms"] = round((time.perf_counter() - t_g0) * 1000, 2)
    if pre.client is None:
        return _no("sin_cliente_clob")
    r["gate_confirmado"] = True
    r["gate_motivo"] = "naive_twap" if MODO_TWAP else f"naive_monedas={n_det}"
    r["_dir"], r["_guardas"] = direction, pre.guardas
    r["_envio"] = lambda: _firmar_enviar_registrar(
        pre, m, activo, direction, lectura["token_id"], ask, stake_eur,
        STRATEGY_NAIVE, (f"modo=twap offset=+{NAIVE_OFFSET_S}s{_z_nota(lectura)}" if MODO_TWAP
                         else f"offset=+{NAIVE_OFFSET_S}s monedas={n_det}{_z_nota(lectura)}"), r,
        ts_end + NAIVE_MAX_ENVIO_S, lectura["t_lectura_ms"])
    return r


def procesar_ventana_naive(pre: _Precalculo, ts_end: int) -> None:
    """T+0: 6 libros en paralelo, quórum de ráfaga de golpe, decisión y envío por moneda."""
    if MODO_TWAP and pre.marco not in NAIVE_TWAP_MARCOS:
        # /code-review: dejar rastro (tuplas en whitelist pero marco no validado para la regla TWAP)
        _append_csv({"timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
                     "ts_end": ts_end, "dry_run": DRY_RUN, "marco": pre.marco, "activo": "*",
                     "estrategia": STRATEGY_NAIVE, "gate_confirmado": False,
                     "gate_motivo": "naive_twap_marco_no_validado"})
        return
    if MODO_TWAP:
        # /code-review: kill-switch del naive una vez por ventana y ANTES de dormir hasta T+0
        # (lee trades.csv; fuera del camino crítico)
        pre.naive_kill = _kill_twap(STRATEGY_NAIVE, REPO / "data" / "live" / NAIVE_TWAP_KILL_LATCH_NAME,
                                    REPO / "data" / "live" / NAIVE_TWAP_DESDE_NAME, "NAIVE")
    objetivo = ts_end + NAIVE_OFFSET_S
    espera = objetivo - time.time()
    if espera < -1.0:
        _log(f"[{pre.marco}] naive {ts_end}: llegamos {-espera:.2f}s tarde -- no se evalúa")
        return
    if espera > 0:
        time.sleep(espera)
    futuros = {_POOL_LIBROS.submit(_leer, pre, a, ts_end - NAIVE_TICK_ANTES_CIERRE_S): a for a in ASSETS
               if MODO_TWAP or (a, pre.marco) in _naive_viejo.COMBOS_CONFIRMADOS}
    hechos, pendientes = wait(futuros, timeout=NAIVE_ESPERA_TICK_POST_S + MAX_ESPERA_LECTURAS_S)
    lecturas = []
    for f in hechos:
        try:
            l = f.result()
        except Exception as e:
            _log(f"[{pre.marco}] naive lectura {futuros[f]} falló: {type(e).__name__}: {e}")
            continue
        if l is not None:
            lecturas.append(l)
    if time.time() > ts_end + NAIVE_MAX_ENVIO_S - 0.3:
        _log(f"[{pre.marco}] naive {ts_end}: lecturas tardías -- no se decide")
        return
    n_det = sum(1 for l in lecturas if _naive_fillable(l))
    lecturas.sort(key=lambda l: -(l["depth"].get("ratio_vs_stake") or 0))
    pre.vivo = _foto_vivo()
    resultados = [_instante_naive(pre, lectura, n_det, ts_end) for lectura in lecturas]
    _despachar(resultados, ts_end)   # escribe las filas (las de envío, al terminar cada envío)
    for f in pendientes:
        _append_csv({"timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
                      "ts_end": ts_end, "dry_run": DRY_RUN, "marco": pre.marco, "activo": futuros[f],
                      "estrategia": STRATEGY_NAIVE, "n_rafaga": n_det, "gate_confirmado": False,
                      "gate_motivo": "lectura_tarde"})


def procesar_ventana(pre: _Precalculo, ts_end: int) -> None:
    objetivo = ts_end + OFFSET_S
    espera = objetivo - time.time()
    if espera < -0.2:
        _log(f"[{pre.marco}] ventana {ts_end} perdida: llegamos {-espera:.2f}s tarde a T{OFFSET_S}s")
        return
    if espera > 0:
        time.sleep(espera)
    # Fase A en paralelo, con tope de espera: una lectura colgada no arrastra a las demás
    # más allá del cierre (/code-review 23-Sep).
    # /code-review 23-Sep: 60min con su propio pool y solo sus monedas -- no compite a :00 con las
    # lecturas reales de 5/15min (MAX_ESPERA_LECTURAS_S las descartaría).
    pool_libros = _POOL_LIBROS_DRY if pre.marco in MARCOS_SOLO_DRY_RUN else _POOL_LIBROS
    futuros = {pool_libros.submit(_leer, pre, a): a for a in MONEDAS_POR_MARCO.get(pre.marco, ASSETS)}
    hechos, pendientes = wait(futuros, timeout=MAX_ESPERA_LECTURAS_S)
    lecturas = []
    for f in hechos:
        try:
            l = f.result()
        except Exception as e:
            _log(f"[{pre.marco}] lectura {futuros[f]} falló: {type(e).__name__}: {e}")
            continue
        if l is not None:
            lecturas.append(l)
    tarde = [futuros[f] for f in pendientes]
    if time.time() > ts_end - 0.3:
        _log(f"[{pre.marco}] ventana {ts_end}: lecturas terminaron a <0,3s del cierre -- no se decide")
        return
    n_rafaga = sum(1 for l in lecturas if _cuenta_para_rafaga(l))
    # live: el tope se lo lleva la moneda con más profundidad (no el orden de ASSETS)
    lecturas.sort(key=lambda l: -(l["depth"].get("ratio_vs_stake") or 0))
    pre.vivo = _foto_vivo()
    resultados = [_instante_critico(pre, lectura, n_rafaga, ts_end) for lectura in lecturas]
    _despachar(resultados, ts_end)   # escribe las filas (las de envío, al terminar cada envío)
    for a in tarde:
        _append_csv({"timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
                      "ts_end": ts_end, "dry_run": DRY_RUN or pre.marco in MARCOS_SOLO_DRY_RUN,
                      "marco": pre.marco, "activo": a,
                      "n_rafaga": n_rafaga, "gate_confirmado": False, "gate_motivo": "lectura_tarde"})


def _bucle_marco(marco: str) -> None:
    pre = _Precalculo(marco)
    dur_s = pre.dur_s
    while True:
        try:
            if not DRY_RUN and marco not in MARCOS_SOLO_DRY_RUN:   # 60min dry-run: medir siempre
                # switch global (sin ventana: el precierre ignora ventanas; el naive las comprueba
                # por su cuenta en _instante_naive)
                ok_switch = live_guard.switch_activo()
                if not ok_switch:
                    time.sleep(5)
                    continue
                disparado_cb, motivo_cb = live_stake.verificar_circuit_breaker()
                if disparado_cb:
                    _log(f"[{marco}] circuit breaker disparado: {motivo_cb} -- en espera")
                    time.sleep(5)
                    continue
            now = time.time()
            ts_end = (int(now) // dur_s + 1) * dur_s
            objetivo_precalculo = ts_end + OFFSET_S - PRECALCULO_ANTES_POR_MARCO_S.get(marco, PRECALCULO_ANTES_S)
            # /code-review 04-Sep, hallazgo real: bucle hasta estar realmente
            # cerca de T-12s (un solo sleep(min(margen,30)) precalculaba minutos antes).
            while True:
                margen = objetivo_precalculo - time.time()
                if margen <= 0:
                    break
                time.sleep(min(margen, 30))
            if ts_end + OFFSET_S - time.time() < 1.0:
                # llegamos tarde a esta ventana (arranque/pausa): dormir hasta que pase el cierre
                # (/code-review 23-Sep: sin sleep era un busy-spin de hasta ~3s)
                time.sleep(max(0.5, ts_end + 1 - time.time()))
                continue
            pre.preparar(ts_end)
            if ts_end + OFFSET_S - time.time() < MIN_MARGEN_PRECIERRE_S:
                _log(f"[{marco}] preparar() tardó demasiado para {ts_end} -- ventana perdida")
                time.sleep(max(0.5, ts_end + 1 - time.time()))
                continue
            procesar_ventana(pre, ts_end)
            # /code-review 24-Sep: con el precierre a T-45s las guardas tendrían ~57 s al llegar el
            # naive (T+0,1s) -- se recalculan a T-PRECALCULO_ANTES_S, misma antigüedad que antes.
            espera_g = ts_end - PRECALCULO_ANTES_S - time.time()
            if espera_g > 0:
                time.sleep(espera_g)
            pre._precalcular_guardas()
            if pre.guardas.get("naive_ok"):   # = clave de config activa en el precálculo de esta ventana
                procesar_ventana_naive(pre, ts_end)
            resto =ts_end + max(OFFSET_S, 0) + 3 - time.time()
            if resto > 0:
                time.sleep(min(resto, 30))
        except Exception as e:
            # /code-review 04-Sep: un ciclo malo no tumba el proceso, se reintenta
            _log(f"[{marco}] error en ciclo principal ({type(e).__name__}: {e}) -- se reintenta")
            time.sleep(5)


def main() -> None:
    _TAIL.arrancar()
    time.sleep(2)
    _log(f"resolution_sniper_precierre_executor arrancado -- DRY_RUN={DRY_RUN} "
         f"offset={OFFSET_S}s stake={STAKE_EUR}€ activos={ASSETS} marcos={list(MARCOS)} "
         + (f"modo=TWAP_proy ask[{ASK_TWAP_MIN},{ASK_TWAP_MAX})" if MODO_TWAP
            else f"criterio=rafaga>={MIN_MONEDAS_RAFAGA} ask<{ASK_MAX}"))
    hilos = {}
    hilo_clv = None
    while True:
        if hilo_clv is None or not hilo_clv.is_alive():
            hilo_clv = threading.Thread(target=_hilo_clv, daemon=True, name="precierre_clv")
            hilo_clv.start()
        for marco in MARCOS:
            h = hilos.get(marco)
            if h is None or not h.is_alive():
                if h is not None:
                    _log(f"[{marco}] hilo murió -- se relanza")
                h = threading.Thread(target=_bucle_marco, args=(marco,), daemon=True, name=f"precierre_{marco}")
                h.start()
                hilos[marco] = h
        time.sleep(30)


if __name__ == "__main__":
    main()
