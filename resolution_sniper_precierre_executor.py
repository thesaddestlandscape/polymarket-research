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
from resolution_sniper_observer import ASSETS, mercado_slot, token_ids, _TAIL

REPO = Path(__file__).resolve().parent
# 23-Sep: marcos en paralelo. (dur_s, marco_tag, subtype_suffix, ask_min_disparo)
MARCOS = {
    "5min": (300, "5m", "5min", 0.20),    # 5min: ask<0,20 pierde (n=54, -0,14/tr)
    "15min": (900, "15m", "15min", 0.05),
}
ASK_RAFAGA_MIN = 0.05       # banda con la que se CUENTAN monedas para la ráfaga (la validada)
ASK_MAX = 0.80              # >=0,80 ya descontado (validado 23-Sep y guarda RSN 22-Sep)
MIN_MONEDAS_RAFAGA = 2
MAX_DISPAROS_POR_VENTANA = 1  # conservador hasta decisión de Javi sobre techo de correlación
# /code-review 23-Sep: tope COMPARTIDO entre marcos por instante de cierre (a :00/:15/:30/:45
# cierran 5min y 15min a la vez, mismo movimiento Chainlink -> órdenes correlacionadas).
_disparos_por_cierre: dict = {}
_disparos_lock = threading.Lock()
# /code-review 23-Sep: un solo pool para ambos marcos (<=6 lecturas concurrentes: el pool de
# conexiones de la sesión HTTP compartida es 10; 12 simultáneas abrían TLS nuevo en el
# instante crítico) y tope de espera de las lecturas de fase A.
_POOL_LIBROS = ThreadPoolExecutor(max_workers=6, thread_name_prefix="libro_precierre")
MAX_ESPERA_LECTURAS_S = 0.9   # lecturas que no llegan en 0,9s (desde T-2s) se descartan
MIN_MARGEN_PRECIERRE_S = 0.3  # si tras preparar() queda menos que esto hasta T-2s, ventana perdida
MARGEN_MIN_POST_S = 0.5       # nunca enviar la orden a menos de 0,5s del cierre nominal
# 23-Sep (checklist pre-live): prob. de acierto CONSERVADORA para el Kelly de calcular_stake --
# cota baja del hit validado con ráfaga (15min 93,7% n=426, 5min 87,0% n=1285), no la media.
P_ACIERTO_CONSERVADORA = {"5min": 0.84, "15min": 0.90}
OFFSET_S = -2                # medido y elegido 03-Sep -- ver docstring arriba
STAKE_EUR = 1.05             # suelo CLOB, mismo criterio que la prueba controlada del 02-Sep
MIN_RATIO_PROFUNDIDAD = 5.0  # mismo umbral que el resto del proyecto
PRECALCULO_ANTES_S = 12      # arrancar precálculo con margen sobre el instante objetivo
DRY_RUN = True                # 04-Sep: construcción inicial -- ver docstring arriba.
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
        for activo in ASSETS:
            _slug, mkt = mercado_slot(activo, self.marco_tag, ts_start)
            if not mkt:
                continue
            token_yes, token_no = token_ids(mkt)
            if not token_yes or not token_no:
                continue
            ref_open = _TAIL.precio_en(activo, ts_start) or _TAIL.precio_en(activo, ts_start + 2)
            self.mercados[activo] = {
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
        g["ok"], g["motivo"] = True, ""
    except Exception as e:
        g["motivo"] = f"error_precalculo:{type(e).__name__}:{e}"
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


def _leer(pre: _Precalculo, activo: str) -> dict | None:
    """Fase A (paralela entre monedas): dirección implícita Chainlink + UNA
    lectura de libro del lado implícito. None si no hay mercado/precio."""
    m = pre.mercados.get(activo)
    if not m or m["ref_open"] is None or m["ref_open"] <= 0:
        return None

    precio_actual = _TAIL.precio_ultimo(activo)
    if precio_actual is None:
        return None
    if precio_actual > m["ref_open"]:
        dir_impl = "Up"
    elif precio_actual < m["ref_open"]:
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
            "market_id": m["market_id"]}


def _cuenta_para_rafaga(lectura: dict | None) -> bool:
    if not lectura or not lectura["depth"].get("ok"):
        return False
    ask = lectura["depth"].get("mejor_ask")
    return ask is not None and ASK_RAFAGA_MIN <= ask < ASK_MAX


def _reservar_disparo(ts_end: int) -> bool:
    """Tope compartido entre hilos/marcos por instante de cierre (ver _disparos_por_cierre)."""
    with _disparos_lock:
        for k in [k for k in _disparos_por_cierre if k < ts_end - 3600]:
            del _disparos_por_cierre[k]
        if _disparos_por_cierre.get(ts_end, 0) >= MAX_DISPAROS_POR_VENTANA:
            return False
        _disparos_por_cierre[ts_end] = _disparos_por_cierre.get(ts_end, 0) + 1
        return True


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
            "marco": pre.marco, "n_rafaga": n_rafaga, "market_id": lectura["market_id"]}
    if not depth.get("ok"):
        return {**base, "gate_confirmado": False, "gate_motivo": "sin_libro"}

    ask = depth.get("mejor_ask")
    if ask is None:
        return {**base, "gate_confirmado": False, "gate_motivo": "sin_ask"}

    # gate por activo (legacy, solo 5min, no distingue marco): solo informativo desde 23-Sep
    veredicto = gate.evaluar(activo, ask, OFFSET_S)
    ratio = depth.get("ratio_vs_stake")
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
    if m["market_id"] in g["ya_operados"]:
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
    if not DRY_RUN and not _reservar_disparo(ts_end):
        resultado["gate_motivo"] = "tope_disparos_ventana"
        return resultado
    resultado["gate_confirmado"] = True
    resultado["gate_motivo"] = f"rafaga_n={n_rafaga}"
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
    ok_whitelist, motivo_whitelist = live_guard.puede_operar_live(STRATEGY, subtype_whitelist)
    # 23-Sep: puede_operar_live sin dirección deja pasar CUALQUIER dirección si una está en la
    # whitelist -- exigir además la tupla EXACTA con dirección (fail-closed).
    if ok_whitelist and not live_guard.estrategia_permitida(STRATEGY, subtype_whitelist, direction=direction):
        ok_whitelist, motivo_whitelist = False, f"{STRATEGY}#{subtype_whitelist}#{direction} no está en lista de permitidos"
    resultado["whitelist_ok"] = ok_whitelist
    if not DRY_RUN and not ok_whitelist:
        resultado["gate_confirmado"] = False
        resultado["gate_motivo"] = f"no_permitido:{motivo_whitelist}"
        return resultado
    if pre.client is None:
        resultado["gate_confirmado"] = False
        resultado["gate_motivo"] = "sin_cliente_clob"
        return resultado

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

    if DRY_RUN:
        resultado["disparado"] = False
        _log(f"[DRY-RUN] {pre.marco} {activo} {direction} ask={ask} rafaga_n={n_rafaga} "
             f"ratio={ratio} t_lectura={t_lectura_ms:.0f}ms t_firma={t_firma_ms:.0f}ms "
             f"-- NO se envía (DRY_RUN=True)")
        return resultado

    # ---- Solo alcanzable con DRY_RUN=False, tras /code-review + aprobación explícita de Javi ----
    # /code-review 23-Sep: límite de reloj DURO -- si ya no queda margen hasta el cierre, no se
    # envía (el libro cierra en endDate exacto: "trading is disabled", ver RSN naive).
    if time.time() > pre.ts_end - MARGEN_MIN_POST_S:
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
    t2 = time.perf_counter()
    try:
        resp = pre.client.post_order(signed, OrderType.FOK)
        ok, error = True, None
    except Exception as e:
        resp, ok, error = None, False, str(e)
    t_post_ms = (time.perf_counter() - t2) * 1000
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
                f"⚠️ RESOLUTION_SNIPER_PRECIERRE\nOrden aceptada pero sin fill confirmado (posible fantasma)\n"
                f"activo={activo} direction={direction} order_id={order_id}\n"
                f"Registrada como ERROR (no OPEN) -- revisar manualmente contra get_trades()/Polygonscan."
            )
    resultado["order_ok"] = ok
    _log(f"ORDEN REAL {activo} {direction} ask={ask} -> ok={ok} resp={str(resp)[:120]} "
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
        notas = (f"RESOLUTION_SNIPER_PRECIERRE {pre.marco} offset={OFFSET_S}s rafaga_n={n_rafaga} "
                 f"t_total={resultado['t_total_ms']}ms")
        if sin_fill_confirmado:
            notas += " | sin_fill_confirmado=1 (revisar manualmente)"
        trade = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "market_id": m["market_id"], "question": m["question"], "end_date": m["end_date"],
            "strategy": STRATEGY, "subtype": f"{activo}#{pre.subtype_suffix}", "direction": direction,
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
    return resultado


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
    futuros = {_POOL_LIBROS.submit(_leer, pre, a): a for a in ASSETS}
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
    for lectura in lecturas:
        r = _instante_critico(pre, lectura, n_rafaga, ts_end)
        _append_csv({"timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
                      "ts_end": ts_end, "dry_run": DRY_RUN, **r})
    for a in tarde:
        _append_csv({"timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
                      "ts_end": ts_end, "dry_run": DRY_RUN, "marco": pre.marco, "activo": a,
                      "n_rafaga": n_rafaga, "gate_confirmado": False, "gate_motivo": "lectura_tarde"})


def _bucle_marco(marco: str) -> None:
    pre = _Precalculo(marco)
    dur_s = pre.dur_s
    while True:
        try:
            if not DRY_RUN:
                ok_switch, motivo = live_guard.puede_operar_live()
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
            objetivo_precalculo = ts_end + OFFSET_S - PRECALCULO_ANTES_S
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
            resto = ts_end + max(OFFSET_S, 0) + 3 - time.time()
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
         f"criterio=rafaga>={MIN_MONEDAS_RAFAGA} ask<{ASK_MAX}")
    hilos = {}
    while True:
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
