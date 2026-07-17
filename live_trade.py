"""
live_trade.py — Motor de ejecución live. Se añade al fast loop tras shadow_predict.

Flujo por ciclo:
  1. live_guard: ¿puede operar ahora? (switch + ventana)
  2. Leer predicciones del ciclo actual (predictions_HOY.csv)
  3. Filtrar señales que pasan el umbral IC mínimo y son de estrategias permitidas
  4. Evitar duplicados: no operar en el mismo mercado dos veces
  5. Calcular stake con live_stake.py
  6. Ejecutar orden real en Polymarket via CLOB API (py-clob-client)
  7. Registrar en data/live/trades.csv
  8. Log completo en logs/live.log
"""

import csv
import fcntl
import json
import math
import os
import requests
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

from live_guard import puede_operar_live, estado_live, switch_activo
from live_stake import (calcular_stake, bankroll_actual, verificar_circuit_breaker, cooldown_factor_streak,
                        pnl_live_hoy, stakes_desplegados_ventana_actual,
                        stakes_abiertos_total, freno_diario_pct_hoy, bankroll_inicio_dia)
from shadow_digest import enviar_telegram
from live_balance import actualizar_balance_real, cargar_balance_real
from smart_money_tracker import trades_de_mercado

DIR_LIVE    = Path("data/live")
DIR_SHADOW  = Path("data/shadow")

CLV_VETO_MIN_N = 20   # resoluciones con clv en ventana para poder vetar
CLV_VETO_DIAS  = 7    # ventana móvil del CLV medio por tupla
# Fee real taker Polymarket (validado 10-Jul contra fees on-chain al céntimo,
# ver project_fee_real_no_contabilizado): fee = FEE_RATE_TAKER_CRYPTO * p * (1-p).
# Solo se paga en taker (nuestras órdenes son FOK); shadow_predict.py neta
# slippage en edge_neto pero NUNCA este fee — se veta aquí, alcance live only.
FEE_RATE_TAKER_CRYPTO = 0.07
_CLV_CACHE: dict | None = None  # tupla → [clv,...]; una lectura por ciclo

# H-CUSTOM-SMARTMONEY-FAVORITO-SOL (confirmada 12-Jul, re-verificada 14-Jul
# 3 veces con n creciente, última: alineado n=95 hit=73.7% pnl=+10.03€ vs
# contrario n=98 hit=59.2% pnl=-23.03€, z≈2.13): mismo umbral que el análisis
# manual que confirmó la hipótesis — no cambiar sin repetir esa validación.
SMARTMONEY_SOL_CONSENSO_MIN   = 0.1  # |smart_money_consensus| mínimo para considerar "con convicción"
SMARTMONEY_SOL_N_WALLETS_MIN  = 3    # wallets "smart" mínimas detrás del consenso
# Techo sobre el boost COMBINADO de ic_para_stake (coincidencia × smartmoney,
# y cualquier boost futuro que se añada al mismo patrón) — ninguno de los
# boosts individuales se validó contra la combinación de ambos a la vez.
BOOST_IC_COMBINADO_MAX = 1.3

# veto_ballenas (16-Jul, decisión Javi tras idea_vigia_ballenas_tiempo_real_no_viable_16jul
# corregida + analisis_ballenas_dosis_respuesta_16jul.py): a diferencia del boost
# smartmoney de arriba (consenso de wallets, agregado, solo afecta STAKE y hoy
# es no-op porque min=max=1.05€), esto es un VETO de ejecución — solo puede
# reducir riesgo (saltar una señal), nunca aumentarlo. Mide la concentración
# del flujo de ballenas EN ESE MERCADO CONCRETO dentro de la banda de precio
# ya calibrada por ballenas_observer.py para (activo,marco): dosis-respuesta
# verificada 16-Jul sobre 366 mercados SOL/ETH/XRP#15min ya resueltos
# (banda de precio constante) — concentración 50-60% acierta 52.6% (n=19,
# coinflip real) vs concentración 90-100% acierta 98.5% (n=273). El chequeo
# SOLO se activa cuando el precio de nuestra señal cae dentro de la banda ya
# validada para ese (activo,marco) — fuera de esa banda (ej. GBM_LATE entrando
# cerca de 0.50, sin confirmar todavía) no hay evidencia y el veto no aplica
# (no bloquea, tampoco genera falsa confianza). Alcance real vive en
# combos_validados en config_live.json (16-Jul: SOL#15m, ETH#15m, SOL#60m,
# BTC#60m, ETH#60m — ver `_veto_ballenas_nota` para el backtest propio de
# cada uno; BTC#15m sigue excluido por ventana de ballenas degenerada
# [0.07,0.52]min). No hardcodear la lista aquí — es la ÚNICA fuente de
# verdad, ya vive en config para poder ampliarse sin tocar código.
#
# Fail-open ante datos insuficientes (n<min_trades) o error de API — decisión
# EXPLÍCITA de Javi 16-Jul tras discutir la tensión con la regla CLAUDE.md
# "cada guardia nueva es fail-closed": fallar cerrado aquí podría vaciar el
# volumen de SOL#15min (una de las mejores tuplas live) sin evidencia de que
# bloquear ahí sea correcto — es la primera vez que se consulta esto EN el
# momento de ejecución, cobertura real desconocida todavía. Mitigación:
# cada evaluación (con o sin datos) se registra en
# data/live/veto_ballenas_eventos.jsonl; vigia_ballenas_cobertura.py (cron)
# alerta por Telegram si el % de sin_datos se dispara — fail-open vigilado,
# no fail-open silencioso.
#
# code-review 16-Jul (antes de desplegar): el diseño original ponía este
# chequeo DESPUÉS del re-quote — bug real, corregido. Las 1-2 llamadas de
# red que necesita (hasta ~20s en el peor caso) habrían invalidado la
# garantía de precio fresco que el re-quote existe para dar (mismo patrón
# de fallo que el bug de precio stale de 2026-07-03). Por eso se evalúa
# ANTES de consultar el libro — no depende de `depth`, así que no pierde
# nada por ir antes; el re-quote sigue siendo el último chequeo antes de
# firmar, como estaba diseñado originalmente.
VETO_BALLENAS_UMBRAL_PCT_DEFAULT = 0.6
VETO_BALLENAS_MIN_TRADES_DEFAULT = 3
VETO_BALLENAS_EVENTOS_PATH = DIR_LIVE / "veto_ballenas_eventos.jsonl"
_MARCO_BALLENAS_MAP = {"5min": "5m", "15min": "15m", "60min": "60m", "240min": "240m"}


def _cargar_ballenas_timing_state() -> dict:
    """Estado de ballenas_observer.py (banda de precio + ventana de tiempo
    calibradas por (activo,marco)), leído fresco cada vez -- sin caché: el
    proceso se reinvoca desde cero en cada uno de los 4 reintentos por
    ciclo (run_fast.sh), así que un caché en memoria no sobrevive entre
    invocaciones y solo añade estado que mantener sin beneficio real
    (fichero ~30KB, parseo sub-milisegundo). Mismo fichero que consume
    shadow_predict.py para PYCONFIRMADO (con su propio caché por mtime,
    justificado ahí porque shadow_predict.py sí procesa muchos mercados
    dentro de la misma invocación)."""
    path = DIR_SHADOW / "ballenas_timing_state.json"
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _marco_ballenas(subtype: str) -> str | None:
    """'SOL#15min' -> '15m' (nomenclatura de ballenas_observer.py). Split
    exacto por '#' en vez de substring — evita que "5min" cuele dentro de
    "15min" si el mapeo se recorre en el orden equivocado."""
    partes = (subtype or "").split("#")
    if len(partes) < 2:
        return None
    return _MARCO_BALLENAS_MAP.get(partes[1])


def _ballenas_conviccion_mercado(condition_id: str, banda_lo: float, banda_hi: float,
                                  lado_deseado: str) -> tuple[float | None, int]:
    """% del flujo BUY de ballenas en ESTE mercado, dentro de la banda de
    precio dada, que apostó por `lado_deseado` ('YES'/'NO' -- misma
    dirección que nuestra señal). Devuelve (None, 0) si no hay trades
    suficientes en banda -- fail-open, ver nota junto a las constantes."""
    try:
        trades = trades_de_mercado(condition_id)
    except Exception:
        return None, 0
    n_total = 0
    n_nuestro = 0
    for t in trades:
        if (t.get("side") or "").strip().upper() != "BUY":
            continue
        precio_t = t.get("price")
        outcome_t = (t.get("outcome") or "").strip().lower()
        if precio_t is None or outcome_t not in ("up", "down", "yes", "no"):
            continue
        try:
            precio_t = float(precio_t)
        except (ValueError, TypeError):
            continue
        if not (banda_lo <= precio_t < banda_hi):
            continue
        n_total += 1
        compro_yes = outcome_t in ("up", "yes")
        lado_t = "YES" if compro_yes else "NO"
        if lado_t == lado_deseado:
            n_nuestro += 1
    if n_total == 0:
        return None, 0
    return n_nuestro / n_total, n_total


def _evaluar_veto_ballenas(condition_id: str | None, activo: str, marco: str | None,
                           precio_plan: float, direction: str, config: dict) -> dict:
    """Evalúa el veto_ballenas para una señal ya identificada (condition_id
    reusado de _get_token_ids, cero llamadas de red extra hasta que hace
    falta de verdad). Guard clauses planas (early-return), ver nota de
    altitud en code-review 16-Jul.

    Devuelve dict con 'aplica' (False = combo/banda no validados, no-op
    total) y si aplica, 'motivo' + 'veta' (bool) + 'pct'/'n' cuando hay
    datos. 'banda_no_significativa' cubre el caso en que
    ballenas_observer.py dejó de confirmar el combo (deriva de calibración)
    aunque siga en combos_validados -- evita usar una banda_lo/banda_hi
    obsoleta sin darse cuenta."""
    veto_cfg = config.get("riesgo", {}).get("veto_ballenas", {})
    if not veto_cfg.get("activo") or not marco:
        return {"aplica": False}
    combo = f"{activo}#{marco}"
    if combo not in set(veto_cfg.get("combos_validados", [])):
        return {"aplica": False}
    banda = _cargar_ballenas_timing_state().get(combo, {})
    if not banda.get("significativo"):
        return {"aplica": False, "combo": combo, "motivo_no_aplica": "banda_no_significativa"}
    banda_lo, banda_hi = banda.get("banda_lo"), banda.get("banda_hi")
    if not (isinstance(banda_lo, (int, float)) and isinstance(banda_hi, (int, float))):
        return {"aplica": False, "combo": combo, "motivo_no_aplica": "banda_invalida"}
    if not (banda_lo <= precio_plan < banda_hi):
        return {"aplica": False, "combo": combo, "motivo_no_aplica": "fuera_de_banda"}
    if not condition_id:
        return {"aplica": True, "veta": False, "motivo": "sin_condition_id",
                "combo": combo, "pct": None, "n": 0}

    lado_deseado = "YES" if direction == "BUY_YES" else "NO"
    pct, n = _ballenas_conviccion_mercado(condition_id, banda_lo, banda_hi, lado_deseado)
    min_trades = veto_cfg.get("min_trades", VETO_BALLENAS_MIN_TRADES_DEFAULT)
    umbral = veto_cfg.get("umbral_pct", VETO_BALLENAS_UMBRAL_PCT_DEFAULT)
    if pct is None or n < min_trades:
        return {"aplica": True, "veta": False, "motivo": "sin_datos",
                "combo": combo, "pct": pct, "n": n}
    if pct < umbral:
        return {"aplica": True, "veta": True, "motivo": "concentracion_debil",
                "combo": combo, "pct": pct, "n": n, "umbral": umbral}
    return {"aplica": True, "veta": False, "motivo": "concentracion_ok",
            "combo": combo, "pct": pct, "n": n, "umbral": umbral}


def _registrar_evento_ballenas(market_id: str, veto_vb: dict) -> None:
    """Log JSONL de cada evaluación del veto_ballenas (aplique o no haya
    datos) -- consumido por vigia_ballenas_cobertura.py para alertar si el
    % de 'sin_datos' se dispara. Nunca lanza (logging best-effort, igual
    que _registrar_snapshot_libro)."""
    try:
        evento = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                  "market_id": market_id, **veto_vb}
        with open(VETO_BALLENAS_EVENTOS_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(evento, ensure_ascii=False) + "\n")
    except Exception:
        pass


def _clv_tupla(strategy: str, subtype: str, decision: str) -> tuple[float, int]:
    """
    CLV medio y n de la tupla STRATEGY#SUBTYPE#DECISION en los últimos
    CLV_VETO_DIAS días de results.csv. (0.0, 0) si no hay datos o error —
    el veto solo actúa con n suficiente, nunca por ausencia de datos.
    """
    global _CLV_CACHE
    if _CLV_CACHE is None:
        _CLV_CACHE = {}
        try:
            corte = (datetime.now(timezone.utc) - timedelta(days=CLV_VETO_DIAS)).isoformat()
            with open(DIR_SHADOW / "results.csv", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    if (row.get("resolution_timestamp") or "") < corte:
                        continue
                    try:
                        clv = float(row.get("clv"))
                    except (TypeError, ValueError):
                        continue
                    k = f"{row.get('strategy')}#{row.get('subtype')}#{row.get('decision')}"
                    _CLV_CACHE.setdefault(k, []).append(clv)
        except Exception:
            pass
    vals = _CLV_CACHE.get(f"{strategy}#{subtype}#{decision}", [])
    if not vals:
        return 0.0, 0
    return sum(vals) / len(vals), len(vals)
TRADES_CSV  = DIR_LIVE  / "trades.csv"
PARAMS_PATH = DIR_SHADOW / "strategy_params.json"
LOG_PATH    = Path("logs/live.log")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
ORDEN_EN_CURSO_PATH = DIR_LIVE / "orden_en_curso.json"
# TRADES_LOCK_PATH (16-Jul, ballenas_executor_btc15m.py): _registrar_trade()
# no tenía ningún lock -- inofensivo mientras live_trade.py corría en un
# solo proceso a la vez (4 reintentos SECUENCIALES por ciclo desde
# run_fast.sh). Con un segundo proceso persistente escribiendo al mismo
# trades.csv, dos escrituras concurrentes podían entrelazarse a nivel de
# fichero. flock() es barato (un solo fichero, nunca contended en la
# práctica -- las ventanas de señal de ambos ejecutores no se solapan en
# el tiempo) y cierra ese caso sin rediseñar el resto del pipeline.
TRADES_LOCK_PATH = DIR_LIVE / ".trades_lock"


def _marcar_orden_en_curso(market_id: str, direction: str):
    """Marca que hay una orden real en vuelo hacia el CLOB. watchdog_fast.sh
    la comprueba antes de matar la screen 'fast' para no interrumpir un
    envío ya hecho al exchange justo antes de registrarlo en trades.csv."""
    try:
        ORDEN_EN_CURSO_PATH.write_text(json.dumps({
            "market_id": market_id, "direction": direction,
            "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }), encoding="utf-8")
    except Exception as e:
        # Fail loud (13-Jul, auditoría de purificación): si esto falla en
        # silencio, watchdog_fast.sh pierde la única señal que le impide
        # matar 'fast' a mitad de una orden ya enviada al exchange — el
        # propio mecanismo de seguridad que este marker existe para dar,
        # sin dejar rastro de por qué. La orden sigue enviándose igual
        # (esto no bloquea el flujo), solo se pierde la protección.
        log(f"  ⚠️ fallo al escribir orden_en_curso.json ({market_id}): {e} "
            f"— watchdog podría matar 'fast' a mitad de esta orden")


def _limpiar_orden_en_curso():
    try:
        ORDEN_EN_CURSO_PATH.unlink(missing_ok=True)
    except Exception as e:
        log(f"  ⚠️ fallo al borrar orden_en_curso.json: {e} — quedará un "
            f"marker obsoleto (watchdog lo detecta y avisa, no bloquea)")

TRADES_COLS = [
    "timestamp_utc", "market_id", "question", "end_date",
    "strategy", "subtype", "direction", "stake_eur",
    "entry_price", "ic_modelo", "edge_neto",
    "conviction_score", "kelly_recomendado",
    "status", "close_timestamp", "exit_price",
    "outcome_real", "fee_eur", "pnl_bruto_eur", "pnl_neto_eur", "notas",
]


def log(msg: str):
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def _cargar_params() -> dict:
    if not PARAMS_PATH.exists():
        return {}
    with open(PARAMS_PATH, encoding="utf-8") as f:
        return json.load(f).get("estrategias", {})


def _cargar_config() -> dict:
    p = DIR_LIVE / "config_live.json"
    if not p.exists():
        return {}
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def _ya_operados_hoy() -> set:
    """Set de todos los market_id que ya tienen trade OPEN o CLOSED (cada
    market_id es una ventana concreta e irrepetible, nunca reaparece en un
    día distinto, así que no hace falta ni conviene acotar por fecha).
    Antes se filtraba comparando una fecha Madrid (UTC+offset) contra
    timestamp_utc crudo (UTC) — durante 23:00-24:00 UTC (=01:00-02:00 Madrid,
    justo la ventana de prueba activa) la fecha Madrid ya era "mañana" y
    ningún trade de esa ventana entraba en `vistos`, permitiendo re-operar
    el mismo mercado varias veces con dinero real."""
    if not TRADES_CSV.exists():
        return set()
    vistos = set()
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            vistos.add(row.get("market_id", ""))
    return vistos


def _posiciones_abiertas_misma_direccion(direction: str) -> int:
    """Nº de trades con status OPEN ahora mismo en la misma dirección.

    Límite de correlación (2026-07-03): BTC/ETH/SOL/XRP se mueven casi al
    unísono intradía, así que N posiciones misma-dirección abiertas a la vez
    son en la práctica UNA apuesta con stake ×N, no N apuestas — el cluster
    shadow de 2026-07-02 01h UTC perdió -24.4€ en 17 BUY_NO simultáneos
    multi-par cuando todo subió a la vez. La penalización de inventario de
    live_stake reduce el stake pero no acota el nº de posiciones; este techo
    duro sí. Código de seguridad live — no minimizar."""
    if not TRADES_CSV.exists():
        return 0
    n = 0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            # OPEN y STUB cuentan como posición viva — mismo criterio que
            # live_stake.py (stakes_desplegados_ventana_actual e
            # inventario_direccional_hoy); solo OPEN dejaba colarse trades
            # STUB por el techo.
            if (row.get("status") in ("OPEN", "STUB")
                    and row.get("direction") == direction):
                n += 1
    return n


def _cargar_predicciones_hoy() -> list:
    """Carga las predicciones de hoy con decision BUY_YES o BUY_NO."""
    hoy  = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = DIR_SHADOW / f"predictions_{hoy}.csv"
    if not path.exists():
        return []
    rows = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("decision") in ("BUY_YES", "BUY_NO"):
                rows.append(row)
    return rows


def _feature_match(feat_val, cond, umbral):
    """Idéntico a shadow_predict.py::_feature_match — mismo criterio para
    evaluar condiciones de patrones_ganadores/filtros_causales. Estricto en
    los 4 casos (ver comentario en shadow_predict.py: coincide con el límite
    "malo" de _evaluar_bucket, antes abs_lt/lt colaban el umbral de más)."""
    try:
        v, u = float(feat_val), float(umbral)
        if cond == "abs_gt": return abs(v) > u
        if cond == "abs_lt": return abs(v) < u
        if cond == "gt":     return v > u
        if cond == "lt":     return v < u
    except (TypeError, ValueError):
        pass
    return False


def _ic_n_para_subtype(strategy: str, subtype: str, params: dict,
                       decision: str = "", min_n: int = 40, min_ic: float = 0.08,
                       features: dict | None = None) -> tuple[float, int]:
    """IC Bayesiano efectivo del subtype + n de la muestra que lo respalda.
    Usa ic_BUY_NO/ic_BUY_YES (direccional) solo si su propio n_BUY_NO/n_BUY_YES
    ya cumple min_n; si no, cae al ic_bayes/n agregados. Así el n devuelto
    siempre corresponde a la muestra real detrás del IC usado (antes se
    comparaba min_n contra el n agregado aunque se usara un IC direccional
    de muestra mucho menor).

    2026-07-01 a 13-Jul: esta función tenía un fallback que, si el resultado
    normal no alcanzaba min_n+min_ic, comprobaba si un patrón causal ya
    confirmado (patrones_ganadores) rehabilitaba la señal, y si la
    rehabilitación se colaba, la trataba como si fuera dinero real
    autorizado — un patrón recién descubierto por postmortem, sin revisión
    humana, podía así autorizar un trade real (ej. GBM_LATE_15M#ETH#15min
    #BUY_YES, tupla ya en pares_permitidos_live).

    13-Jul: RETIRADO. Los dos únicos llamadores de esta función en todo el
    repo (main(), la ejecución real, y _snapshots_por_lista/
    _snapshots_fuera_ventana, el snapshot de fill-ability) ya filtran la
    tupla contra pares_permitidos_live ANTES de llegar aquí — es decir,
    CUALQUIER llamada a esta función hoy es sobre un par que YA es dinero
    real, sin excepción. Por eso un fail-safe "solo si es par live" sería
    una tautología (siempre cierto) y no protegería nada de verdad — la
    única forma honesta de cerrar el gap es que la rehabilitación por
    patrones_ganadores nunca se aplique aquí, punto (mismo criterio de
    promoción manual explícita que _es_par_live_protegido en
    shadow_predict.py exige para los filtros/patrones que sí tocan pares
    live). Se deja el escaneo y el log de qué patrón HABRÍA rehabilitado
    (más abajo) para que la evidencia siga siendo visible y así decidir a
    mano si algún día merece un mecanismo de promoción explícito — pero
    nunca se aplica solo."""
    claves = []
    if "#" in subtype:
        a, d = subtype.split("#", 1)
        claves = [f"{strategy}#{subtype}", f"{strategy}#{a}", f"{strategy}#{d}", strategy]
    elif subtype:
        claves = [f"{strategy}#{subtype}", strategy]
    else:
        claves = [strategy]

    ic_normal, n_normal, clave_usada = None, None, None
    for k in claves:
        if k in params:
            p = params[k]
            if decision == "BUY_NO" and p.get("ic_BUY_NO") is not None:
                n_dir = p.get("n_BUY_NO", 0)
                if n_dir >= min_n:
                    ic_normal, n_normal, clave_usada = float(p["ic_BUY_NO"]), n_dir, k
                    break
            elif decision == "BUY_YES" and p.get("ic_BUY_YES") is not None:
                n_dir = p.get("n_BUY_YES", 0)
                if n_dir >= min_n:
                    ic_normal, n_normal, clave_usada = float(p["ic_BUY_YES"]), n_dir, k
                    break
            ic_normal, n_normal, clave_usada = float(p.get("ic_bayes", 0)), p.get("n", 0), k
            break

    if clave_usada is None:
        return 0.0, 0
    if n_normal >= min_n and ic_normal >= min_ic:
        return ic_normal, n_normal

    # No alcanza min_n+min_ic por la vía normal — probar patrón causal confirmado.
    # Veto previo: si el subtype EXACTO ya tiene evidencia direccional propia
    # NEGATIVA (o agregada negativa si no hay direccional), ningún patrón de una
    # clave más genérica puede rehabilitarlo para live — un patrón de
    # UPDOWN_GBM#15min (aprendido sobre todo en ETH/XRP) validó en vivo un
    # SOL#15min BUY_NO cuyo ic_BUY_NO propio era -0.025 (trade real perdido
    # 2026-07-02 19:26 UTC, -2.00€). El patrón sigue valiendo para subtypes
    # sin historial propio o con historial propio ≥0 pero insuficiente.
    # Código de seguridad live — no minimizar.
    if features:
        p_exacto = params.get(claves[0], {})
        ic_propio = p_exacto.get(f"ic_{decision}") if decision else None
        if ic_propio is None:
            ic_propio = p_exacto.get("ic_bayes")
        if ic_propio is not None and float(ic_propio) < 0:
            return ic_normal, n_normal

        mejor_patron = None
        for k in claves:
            for patron in params.get(k, {}).get("patrones_ganadores", []):
                if patron.get("direccion") not in (None, decision):
                    continue
                n_patron = patron.get("n_patron", 0)
                if n_patron < min_n:
                    continue
                ic_patron = float(patron.get("ic_patron", 0))
                if ic_patron < min_ic:
                    continue
                fv = features.get(patron.get("feature"))
                if fv is None:
                    continue
                if not _feature_match(fv, patron.get("condicion", ""), patron.get("umbral", 999)):
                    continue
                if mejor_patron is None or ic_patron > mejor_patron[0]:
                    mejor_patron = (ic_patron, n_patron)
        if mejor_patron:
            log(f"  ⚠️ patron_ganador {strategy}#{subtype}#{decision} "
                f"(ic_patron={mejor_patron[0]:+.3f} n_patron={mejor_patron[1]}) "
                f"rehabilitaría la señal pero NO se aplica (fail-safe 13-Jul: "
                f"requiere promoción manual explícita, ver docstring)")

    return ic_normal, n_normal


_clob_redondeo_parcheado = False


def _parchear_redondeo_clob():
    """Sustituye los helpers de redondeo de py_clob_client_v2 por versiones
    exactas basadas en Decimal. Los originales operan en float puro
    (floor(x * 10**n) / 10**n), y para ciertas combinaciones stake/precio el
    residuo binario deja maker/taker amounts con más decimales de los que el
    CLOB admite → rechazo "invalid amounts" (2 señales reales perdidas:
    2026-06-30 y 2026-07-02 19:22 UTC). Esta es la causa raíz; el reintento
    con stake±0.01€ de _ejecutar_orden_polymarket se mantiene como red de
    seguridad. Se parchean tanto helpers como builder (importa por nombre).

    Causa raíz principal encontrada 2026-07-03: los mercados cripto up/down
    usan tick 0.001 (precios de 3 decimales, ej. 0.485), y para ese tick la
    librería redondea el taker amount a 5 decimales (RoundConfig(amount=5)),
    pero el CLOB solo admite 4 en market orders ("taker amount a max of 4
    decimals") → la orden falla exactamente cuando el 5º decimal del cociente
    maker/precio no es cero, de ahí la intermitencia. Se sustituye también
    get_market_order_amounts por una versión que respeta los límites reales
    del CLOB para market orders: maker (USDC) ≤2 decimales, taker (shares) ≤4.
    Código de seguridad live — no minimizar."""
    global _clob_redondeo_parcheado
    if _clob_redondeo_parcheado:
        return
    from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_UP
    from py_clob_client_v2.order_builder import builder as _b, helpers as _h
    from py_clob_client_v2.order_utils import Side as _Side

    def _q(sig_digits: int) -> Decimal:
        return Decimal(1).scaleb(-sig_digits)

    def round_down(x: float, sig_digits: int) -> float:
        return float(Decimal(str(x)).quantize(_q(sig_digits), rounding=ROUND_FLOOR))

    def round_up(x: float, sig_digits: int) -> float:
        return float(Decimal(str(x)).quantize(_q(sig_digits), rounding=ROUND_CEILING))

    def round_normal(x: float, sig_digits: int) -> float:
        return float(Decimal(str(x)).quantize(_q(sig_digits), rounding=ROUND_HALF_UP))

    def to_token_decimals(x: float) -> int:
        return int((Decimal(str(x)) * 10**6).quantize(Decimal(1), rounding=ROUND_HALF_UP))

    for mod in (_h, _b):
        mod.round_down = round_down
        mod.round_up = round_up
        mod.round_normal = round_normal
        mod.to_token_decimals = to_token_decimals

    MAX_DEC_TAKER_MARKET = 4  # límite del CLOB para market orders, no depende del tick

    def get_market_order_amounts(self, side, amount, price, round_config):
        if isinstance(side, _Side):
            side = _b.BUY if side == _Side.BUY else _b.SELL
        raw_price = round_down(price, round_config.price)
        max_dec = min(round_config.amount, MAX_DEC_TAKER_MARKET)
        if side == _b.BUY:
            # maker = USDC gastado (≤2 dec), taker = shares recibidas (≤4 dec).
            # Shares hacia abajo: nunca pedir más de lo que el dinero compra.
            raw_maker = round_down(amount, round_config.size)
            raw_taker = round_down(raw_maker / raw_price, max_dec)
            return _Side.BUY, to_token_decimals(raw_maker), to_token_decimals(raw_taker)
        elif side == _b.SELL:
            raw_maker = round_down(amount, round_config.size)
            raw_taker = round_down(raw_maker * raw_price, max_dec)
            return _Side.SELL, to_token_decimals(raw_maker), to_token_decimals(raw_taker)
        raise ValueError(f"order_args.side must be '{_b.BUY}' or '{_b.SELL}'")

    _b.OrderBuilder.get_market_order_amounts = get_market_order_amounts
    _clob_redondeo_parcheado = True


def _get_clob_client():
    """Crea cliente CLOB V2 autenticado desde .env."""
    from dotenv import load_dotenv
    from py_clob_client_v2 import ClobClient, ApiCreds
    from py_clob_client_v2.constants import POLYGON
    _parchear_redondeo_clob()
    load_dotenv(DIR_LIVE / ".env")
    key = os.getenv("POLY_PRIVATE_KEY")
    creds = ApiCreds(
        api_key=os.getenv("POLY_API_KEY"),
        api_secret=os.getenv("POLY_API_SECRET"),
        api_passphrase=os.getenv("POLY_API_PASSPHRASE"),
    )
    deposit_wallet = os.getenv("POLY_DEPOSIT_WALLET")
    return ClobClient(
        "https://clob.polymarket.com",
        key=key,
        chain_id=POLYGON,
        creds=creds,
        signature_type=3,       # POLY_1271 — deposit wallet flow
        funder=deposit_wallet,
    )


def _get_token_ids(market_id: str) -> tuple[str, str, str | None]:
    """Devuelve (yes_token_id, no_token_id, condition_id) desde Gamma API.

    Valida el orden real contra `outcomes` en vez de asumir ciegamente
    clobTokenIds[0]=YES/UP — si algún mercado trajera el orden invertido,
    asumirlo a ciegas compraría el token contrario con dinero real sin
    ningún aviso. Si `outcomes` no trae las etiquetas esperadas, falla
    fuerte (se captura arriba en _ejecutar_orden_polymarket) en vez de
    arriesgar una dirección adivinada.

    condition_id (16-Jul, veto_ballenas): la misma respuesta ya trae
    `conditionId` — devolverlo aquí evita una 2ª llamada idéntica a Gamma
    API solo para ese campo (código de seguridad live 03-Jul: "el import
    de py_clob_client se paga solo cuando toca" tiene el mismo espíritu,
    no pagar dos veces la misma llamada de red)."""
    resp = requests.get(
        f"https://gamma-api.polymarket.com/markets/{market_id}",
        timeout=10
    )
    resp.raise_for_status()
    data = resp.json()
    condition_id = data.get("conditionId") or None
    raw = data.get("clobTokenIds", [])
    tokens = json.loads(raw) if isinstance(raw, str) else raw
    if len(tokens) < 2:
        raise ValueError(f"clobTokenIds incompleto para market {market_id}: {tokens}")

    raw_outcomes = data.get("outcomes", [])
    outcomes = json.loads(raw_outcomes) if isinstance(raw_outcomes, str) else raw_outcomes
    if len(outcomes) < 2:
        raise ValueError(f"outcomes incompleto para market {market_id}: {outcomes}")

    AFIRMATIVOS = {"yes", "up"}
    NEGATIVOS   = {"no", "down"}
    o0 = str(outcomes[0]).strip().lower()
    o1 = str(outcomes[1]).strip().lower()
    if o0 in AFIRMATIVOS and o1 in NEGATIVOS:
        return tokens[0], tokens[1], condition_id
    if o0 in NEGATIVOS and o1 in AFIRMATIVOS:
        return tokens[1], tokens[0], condition_id
    raise ValueError(
        f"outcomes inesperados para market {market_id}: {outcomes} — "
        f"no se puede mapear YES/NO con seguridad"
    )


CLOB_BOOK_URL = "https://clob.polymarket.com/book"


def _fetch_book_publico(token_id: str) -> dict | None:
    """Libro de un token vía REST público (sin auth, sin construir ClobClient).
    2026-07-10: perfilado mostró que importar py_clob_client_v2 cuesta ~270ms
    (el objeto en sí es ~2ms — el coste es el import de web3/eth_account), y
    /book es público (verificado: 200 OK sin credenciales). El cliente
    autenticado solo hace falta para FIRMAR una orden real, nunca para leer
    el libro. Antes se pagaba ese import en CADA consulta de profundidad —
    incluidas las de solo-instrumentación (candidatos_evaluacion_live,
    fuera_ventana, senal_caducada) que son ~95% de las llamadas y NUNCA
    ordenan (veto_profundidad 2515 vs ejecutada 129, histórico). None en
    error — mismo contrato que antes (el caller ya lo trata como fail-closed)."""
    try:
        r = requests.get(CLOB_BOOK_URL, params={"token_id": token_id}, timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception:
        return None


def _consultar_profundidad_libro(client, token_id: str, precio_entrada: float,
                                 stake_eur: float) -> dict:
    """
    Observación pura (no cambia ninguna decisión): consulta el order book
    real de Polymarket para el token que vamos a comprar y mide cuánta
    profundidad hay en el lado ask cerca del precio de entrada. Se loguea
    junto a cada orden para poder cruzar después si los kills de FOK
    ("sin liquidez a ese precio") correlacionan con libros finos.

    client=None usa el endpoint público /book (ver _fetch_book_publico) — es
    el camino por defecto para toda consulta de solo lectura. Pasar un
    ClobClient real solo aporta algo distinto si algún día hace falta el
    libro autenticado (no es el caso hoy: /book es idéntico autenticado o no).
    """
    try:
        book = _fetch_book_publico(token_id) if client is None else client.get_order_book(token_id)
        if book is None:
            return {"ok": False, "error": "sin respuesta del libro (público)"}
        asks = (book.get("asks") if isinstance(book, dict) else getattr(book, "asks", None)) or []
        techo = precio_entrada * 1.05  # banda razonable sobre el precio objetivo
        profundidad_eur = 0.0
        mejor_ask = None
        for lvl in asks:
            p = float(lvl.get("price") if isinstance(lvl, dict) else lvl.price)
            s = float(lvl.get("size") if isinstance(lvl, dict) else lvl.size)
            if mejor_ask is None or p < mejor_ask:
                mejor_ask = p
            if p <= techo:
                profundidad_eur += p * s
        ratio = (profundidad_eur / stake_eur) if stake_eur > 0 else None
        return {
            "ok": True,
            "mejor_ask": mejor_ask,
            "profundidad_eur": round(profundidad_eur, 2),
            "n_niveles": len(asks),
            "ratio_vs_stake": round(ratio, 1) if ratio is not None else None,
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}


# Estimador empírico de slippage por profundidad (10-Jul, propuesta #4 quant-
# desk "Kyle's lambda"). NO es Kyle's lambda clásico (que predice MENOS
# impacto con MÁS profundidad) — aquí el signo medido es el CONTRARIO: más
# ratio_vs_stake en el momento de ejecutar correlaciona con PEOR slip_real
# (n=130 ejecutadas, robusto por par: SOL corr=-0.57 ETH=-0.55 XRP=-0.77).
# Hipótesis de mecanismo: un libro muy profundo en el micro-instante de nuestra
# ejecución probablemente señala una orden grande de un market-maker
# profesional activo justo ahí (los mismos actores del estudio de ballenas
# 10-Jul), no "liquidez fácil". OJO: comprobado que EXCLUIR esas señales
# EMPEORA el PnL real (n=130: sin techo +0.109€/trade, con techo ratio<=200
# -0.127€/trade) — los libros profundos llevan más edge genuino, no menos;
# el re-quote actúa de filtro (solo sobrevive al deterioro una señal con edge
# de partida fuerte). Por eso esto es SOLO una estimación logueada para
# comparar con slip_real, NUNCA un veto ni cambia edge_neto/decisión.
# Ajuste: slip_estimado = a + b*sqrt(ratio_vs_stake), OLS sobre n=130
# ejecutadas reales, R²=0.395 (mejor que lineal en ratio R²=0.32 o en
# ln(ratio) R²=0.38).
_SLIP_KYLE_A = -0.00105
_SLIP_KYLE_B = 0.00286


def _estimar_slip_kyle(ratio_vs_stake: float | None) -> float | None:
    """|slip| esperado dado el ratio_vs_stake al momento de ejecutar. Solo
    logging — comparar contra slip_real post-hoc para validar el modelo antes
    de plantear si algún día sustituye a SLIPPAGE_ESTIMADO (decisión futura,
    no hoy). None si no hay ratio (mismo comportamiento fail-soft que el resto
    de este módulo: falta de dato no bloquea nada, solo no se loguea)."""
    if ratio_vs_stake is None or ratio_vs_stake < 0:
        return None
    return round(max(0.0, _SLIP_KYLE_A + _SLIP_KYLE_B * math.sqrt(ratio_vs_stake)), 5)


SNAPSHOT_LIBRO_CSV = DIR_LIVE / "libro_snapshots.csv"

# ── Tendencia de profundidad (12-Jul, idea VPIN/order-book-imbalance) ──────
# Javi compartió técnicas de detección de toxic flow de market making
# (canarios, pull-quotes-and-fade, VPIN). Los canarios no aplican (CLOB
# exige mínimo $1, no hay hueco para sondas), pull-quotes-and-fade explica
# el mecanismo ya conocido de selección adversa (no es algo que hagamos
# nosotros). VPIN/order-book-imbalance SÍ tiene un ángulo nuevo: H-OBI se
# archivó como "irrecuperable" (idea_hobi_refutada_sin_dato) porque el
# dataset histórico Jon-Becker no tiene order book — pero eso solo bloquea
# el BACKTEST; hacia adelante, el reintento del ciclo rápido (~cada 4-5s)
# ya vuelve a consultar el mismo mercado varias veces, así que podemos medir
# la TENDENCIA de profundidad (¿se llena o se vacía entre lecturas?) gratis,
# sin infraestructura nueva. Puramente observacional: se logea junto al
# snapshot existente, nunca decide nada. Validar con el mismo pipeline
# causal×fillable ya construido antes de plantear cualquier veto.
PROFUNDIDAD_TENDENCIA_JSON = DIR_LIVE / "profundidad_tendencia_state.json"
PROFUNDIDAD_TENDENCIA_TTL_SEG = 1800  # 30min — más que suficiente para 15min de vida de mercado más margen


def _tendencia_profundidad(market_id: str, strategy: str, direction: str,
                            profundidad_eur) -> float | None:
    """Delta de profundidad_eur vs la última lectura de esta MISMA tupla
    (market_id+strategy+direction). None si es la primera lectura o si la
    anterior es demasiado vieja (mercado distinto reutilizando el id no
    debería pasar, pero TTL protege igual). Nunca lanza — solo lectura."""
    try:
        estado = json.loads(PROFUNDIDAD_TENDENCIA_JSON.read_text()) \
            if PROFUNDIDAD_TENDENCIA_JSON.exists() else {}
    except Exception:
        estado = {}
    clave = f"{market_id}#{strategy}#{direction}"
    ahora = datetime.now(timezone.utc)
    delta = None
    if profundidad_eur is not None and profundidad_eur != "":
        try:
            pf_actual = float(profundidad_eur)
            prev = estado.get(clave)
            if prev:
                prev_ts = datetime.fromisoformat(prev["ts"])
                if (ahora - prev_ts).total_seconds() <= PROFUNDIDAD_TENDENCIA_TTL_SEG:
                    delta = round(pf_actual - float(prev["profundidad_eur"]), 4)
            estado[clave] = {"profundidad_eur": pf_actual, "ts": ahora.isoformat(timespec="seconds")}
        except Exception:
            pass
    # poda: fuera del TTL, para no crecer sin límite durante el día
    estado = {k: v for k, v in estado.items()
              if (ahora - datetime.fromisoformat(v["ts"])).total_seconds() <= PROFUNDIDAD_TENDENCIA_TTL_SEG}
    try:
        PROFUNDIDAD_TENDENCIA_JSON.write_text(json.dumps(estado))
    except Exception:
        pass
    return delta


def _registrar_snapshot_libro(motivo: str, market_id: str, direction: str,
                              precio_plan, stake_eur, depth: dict | None,
                              contexto: dict | None = None) -> None:
    """
    Dataset para el análisis maker (2026-07-03): estado del libro de CADA
    señal que llega a fase de ejecución, se ejecute o se aborte. Hallazgo que
    lo motiva: los fills taker aciertan 19% y las señales vetadas por
    profundidad 83% (mismo día, mismas tuplas) — la fill-ability es un
    anti-predictor y no quedaba registrada para las no ejecutadas. Cruzar
    con results.csv por market_id. Nunca lanza.
    """
    try:
        ctx = contexto or {}
        d = depth or {}
        delta_prof = _tendencia_profundidad(market_id, ctx.get("strategy", ""),
                                             direction, d.get("profundidad_eur"))
        nuevo = not SNAPSHOT_LIBRO_CSV.exists()
        with open(SNAPSHOT_LIBRO_CSV, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if nuevo:
                w.writerow(["timestamp_utc", "market_id", "strategy", "subtype",
                            "direction", "motivo", "precio_plan", "stake_eur",
                            "mejor_ask", "profundidad_eur", "n_niveles",
                            "ratio_vs_stake", "delta_profundidad_eur"])
            w.writerow([datetime.now(timezone.utc).isoformat(timespec="seconds"),
                        market_id, ctx.get("strategy", ""), ctx.get("subtype", ""),
                        direction, motivo, precio_plan, stake_eur,
                        d.get("mejor_ask", ""), d.get("profundidad_eur", ""),
                        d.get("n_niveles", ""), d.get("ratio_vs_stake", ""),
                        delta_prof if delta_prof is not None else ""])
    except Exception:
        pass


def _snapshot_senal_bloqueada(market_id: str, direction: str, precio_yes,
                              stake_ref: float, contexto: dict,
                              motivo: str = "no_viable_stake") -> None:
    """Snapshot del libro para señales que NO llegan a ejecución porque el
    stake no es viable (suelo bankroll_minimo / freno diario). Sin esto el
    dataset del análisis maker (libro_snapshots.csv) deja de acumular justo
    cuando el live está congelado (2026-07-03: suelo 8€ mordiendo toda señal)
    — que es cuando hace falta para decidir la reapertura. Una fila por
    market#direction: el proceso es nuevo cada ciclo (~20s) y sin dedupe
    serían ~45 filas y consultas CLOB por señal de 15min. stake_ref es
    nominal (min_stake_eur) para que ratio_vs_stake sea comparable con los
    snapshots de ejecución. Solo lee el libro — nunca ordena, nunca lanza."""
    try:
        if SNAPSHOT_LIBRO_CSV.exists():
            with open(SNAPSHOT_LIBRO_CSV, newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    fila_motivo = row.get("motivo")
                    mismo_grupo = (
                        fila_motivo == motivo
                        or (fila_motivo in ("no_viable_stake", "fuera_ventana")
                            and motivo in ("no_viable_stake", "fuera_ventana"))
                    )
                    if (str(row.get("market_id")) == str(market_id)
                            and row.get("direction") == direction
                            and mismo_grupo):
                        return
        yes_token, no_token, _ = _get_token_ids(market_id)
        if direction == "BUY_YES":
            token_id, precio = yes_token, float(precio_yes)
        else:
            token_id, precio = no_token, round(1.0 - float(precio_yes), 6)
        # client=None -> libro público (2026-07-10): esta función NUNCA ordena,
        # solo instrumenta (no_viable_stake/fuera_ventana/senal_caducada/
        # candidato_evaluacion) — construir el ClobClient autenticado aquí
        # pagaba ~270ms de import por nada en cada una de estas llamadas.
        depth = _consultar_profundidad_libro(None, token_id, precio, stake_ref)
        _registrar_snapshot_libro(motivo, market_id, direction,
                                  precio, stake_ref, depth, contexto)
    except Exception:
        pass


def _snapshots_por_lista(tuplas: set, motivo: str, aplicar_gate_ic: bool) -> None:
    """Núcleo compartido de _snapshots_fuera_ventana y
    _snapshots_candidatos_evaluacion: recorre las predicciones de hoy, filtra
    por tupla strategy#subtype#decision, descarta mercados ya cerrados y
    snapshotea el libro (solo lectura, nunca ordena). aplicar_gate_ic=True
    exige además la barra IC/n de riesgo (uso: tuplas YA whitelisted, fuera de
    ventana); aplicar_gate_ic=False no filtra por IC (uso: candidatos aún sin
    barra que cumplir, el objetivo es medir profundidad ANTES de decidir)."""
    if not tuplas:
        return
    config = _cargar_config()
    riesgo = config.get("riesgo", {})
    stake_ref = riesgo.get("min_stake_eur", 1.05)
    if aplicar_gate_ic:
        params      = _cargar_params()
        min_ic      = riesgo.get("min_ic_para_live", 0.08)
        min_n       = riesgo.get("min_n_para_live", 40)
        min_ic_asim = riesgo.get("min_ic_asimetrico", {})
    ahora = datetime.now(timezone.utc)
    for pred in _cargar_predicciones_hoy():
        strategy = pred.get("strategy", "")
        subtype  = pred.get("subtype", "")
        mid      = pred.get("market_id", "")
        dec      = pred.get("decision", "")
        if f"{strategy}#{subtype}#{dec}" not in tuplas:
            continue
        end_str = pred.get("end_date", "")
        try:
            if not end_str:
                continue
            end_dt = datetime.fromisoformat(end_str.replace("Z", "+00:00"))
            if end_dt.tzinfo is None:
                end_dt = end_dt.replace(tzinfo=timezone.utc)
            if end_dt <= ahora:
                continue
        except Exception:
            continue
        if aplicar_gate_ic:
            min_ic_efectivo = min_ic_asim.get(f"{strategy}#{dec}", min_ic)
            try:
                feats = json.loads(pred.get("features", "{}") or "{}")
            except Exception:
                feats = {}
            ic_h, n_h = _ic_n_para_subtype(strategy, subtype, params,
                                           decision=dec, min_n=min_n,
                                           min_ic=min_ic_efectivo,
                                           features=feats)
            if ic_h < min_ic_efectivo or n_h < min_n:
                continue
        _snapshot_senal_bloqueada(mid, dec,
                                  pred.get("precio_yes_mercado", 0.5),
                                  stake_ref,
                                  {"strategy": strategy, "subtype": subtype},
                                  motivo=motivo)


def _snapshots_fuera_ventana() -> None:
    """Acumula libro_snapshots también con el live cerrado (switch OFF, fuera
    de ventana, fin de semana). Motivo: el dataset de fill-ability — criterio
    de reapertura, n>=30 en analisis_fills.py — solo crecía dentro de ventanas
    L-V, y el live se congeló un viernes por la tarde (03-Jul): 1 fila en 2
    días. Aplica los mismos filtros de elegibilidad que el flujo live (tupla
    whitelisted + mercado abierto + barra IC/n) para que las filas sean
    comparables con las de ejecución. Solo lee el libro — nunca ordena, nunca
    lanza."""
    try:
        config   = _cargar_config()
        pares_ok = set(config.get("pares_permitidos_live", []))
        _snapshots_por_lista(pares_ok, motivo="fuera_ventana", aplicar_gate_ic=True)
    except Exception:
        pass


def _snapshots_candidatos_evaluacion() -> None:
    """Acumula libro_snapshots para tuplas que NO están en pares_permitidos_live
    todavía pero se están evaluando como candidatas a promoción (ver
    candidatos_evaluacion_live en config_live.json). Motivo: cada promoción
    anterior (SOL/XRP BUY_NO) se decidió por fill-ability, no por IC — pero
    el dataset de profundidad solo se llena para tuplas YA whitelisted
    (_snapshots_fuera_ventana), así que una tupla nueva siempre arranca desde
    cero justo cuando más falta hace el dato. Esta función mide profundidad
    real ANTES de que la tupla cruce el gate de IC/n (aplicar_gate_ic=False:
    un candidato por definición no lo cumple todavía), para no perder tiempo
    cuando llegue el momento de decidir. Se llama en cada ciclo, dentro y
    fuera de ventana — no participa en la ejecución real, no toca
    pares_permitidos_live, no ordena. Solo lee el libro."""
    try:
        config     = _cargar_config()
        candidatos = set(config.get("candidatos_evaluacion_live", []))
        _snapshots_por_lista(candidatos, motivo="candidato_evaluacion",
                             aplicar_gate_ic=False)
    except Exception:
        pass


REQUOTE_EDGE_MIN  = 0.02   # mismo listón que EDGE_MINIMO de shadow_predict
REQUOTE_PRECIO_MAX = 0.95  # nunca pagar más de esto por el token, pase lo que pase
MIN_ORDEN_CLOB_USD = 1.00  # el CLOB rechaza marketable BUY < $1 ("min size: 1")
# Descubierto 11-Jul: las órdenes limit/GTD (no marketable) tienen un mínimo
# DISTINTO al de arriba — 5 shares, no $1 notional. Con maker_pilot.stake_eur
# a 1.05€ y precios ~0.48-0.52 (zona típica GBM_LATE) el size salía ~2.0-2.2,
# rechazado 5/5 veces reales ("Size (2.02) lower than the minimum: 5"). Fix:
# stake del piloto subido a 2.75€ (aprobado Javi) + esta guardia fail-closed
# como red de seguridad si el precio sube lo bastante para volver a caer
# bajo el mínimo con el nuevo stake.
MIN_SHARES_CLOB_LIMIT = 5.0
REQUOTE_DIVERGENCIA_MAX = 0.10  # |ask - plan| máx; más allá el modelo está desfasado


# ============================================================================
# PILOTO MAKER-SOBRE-VETADAS (2026-07-10, aprobado Javi — propuesta #1)
#
# Motivación (analisis_fills, histórico completo, ambos lados n>=30): las
# señales vetadas por profundidad aciertan 97% (+123.59€ a precio plan, n=86)
# vs 47% las ejecutadas taker (n=131) — selección adversa. maker_sim refutó
# maker GENERAL (EV−, fill 53.6%), pero nunca se probó maker CONDICIONAL al
# subconjunto vetado (tensión documentada en project_diagnostico_perdidas_10jul).
# Este piloto la resuelve con dinero real acotado: limit GTD post-solo-precio
# (nunca cruza el ask) únicamente en señales que pasaron TODOS los gates
# (whitelist, IC, CLV, evaluador, stake, techo dirección, latencia<100s) y
# murieron exclusivamente en veto_profundidad.
#
# Seguridad (código de dinero real — no minimizar):
#  - GTD: la orden expira SOLA en el exchange a T-cancelar_antes_fin_seg
#    (mismo margen CANCEL_MIN=4min que maker_sim). Si este proceso muere, no
#    queda orden eterna colgada.
#  - Estado persistente en maker_orders.json; intent se escribe ANTES de
#    postear (crash entre post y save → la huérfana se adopta o descarta en
#    la reconciliación vía get_open_orders).
#  - Fill solo se registra en trades.csv cuando la API lo confirma
#    (get_order: size_matched>0); stake real = size_matched × precio.
#  - Señal con orden maker viva se salta también la ruta taker (el libro
#    fluctúa: sin este check, un ciclo posterior podría pasar el veto y
#    ejecutar taker → doble posición en el mismo mercado).
#  - Killswitch: config maker_pilot.activo=false apaga la colocación (la
#    reconciliación de órdenes ya vivas sigue corriendo siempre).
#  - Caps: max_ordenes_abiertas simultáneas, stake fijo del piloto.
#  - Las órdenes maker abiertas NO computan en el freno diario prospectivo
#    (bloquean USDC en el CLOB sin ser posición) — exposición acotada por
#    max_ordenes_abiertas × stake ≈ 2.10€, documentado y aceptado en el
#    diseño del piloto.
# ============================================================================
MAKER_ORDERS_JSON = DIR_LIVE / "maker_orders.json"
MAKER_GTD_BUFFER_MIN_SEG = 90   # no colocar si la expiración quedaría a <90s
# ⚠️ GTD y el "1 minute security threshold" del CLOB (README py-clob-client):
# el exchange exige expiration > ahora + ~60s. El buffer de 90s lo cubre. Si
# la semántica real fuera "expira en expiration−60s", la orden moriría a
# T-300s en vez de T-240s — dirección SEGURA (muere antes, nunca después del
# margen anti-sniper diseñado). No "compensar" sumando 60s a expiration: eso
# invertiría el error hacia el lado peligroso (viva en la fase sniper).


def _maker_pilot_cfg() -> dict:
    cfg = _cargar_config().get("maker_pilot", {})
    return {
        "activo": bool(cfg.get("activo", False)),   # fail-closed: ausente = off
        "max_ordenes_abiertas": int(cfg.get("max_ordenes_abiertas", 2)),
        "stake_eur": float(cfg.get("stake_eur", 1.05)),
        "cancelar_antes_fin_seg": int(cfg.get("cancelar_antes_fin_seg", 240)),
    }


def _maker_estado_cargar() -> list:
    try:
        if MAKER_ORDERS_JSON.exists():
            data = json.loads(MAKER_ORDERS_JSON.read_text())
            if isinstance(data, list):
                return data
    except Exception as e:
        # Fail-closed: estado ilegible → tratar como "hay órdenes" es
        # imposible sin datos; se loguea fuerte y se devuelve lista vacía,
        # pero la colocación queda bloqueada vía _maker_estado_ok.
        log(f"  ⚠️ maker_orders.json ilegible: {e}")
        return None
    return []


def _maker_estado_guardar(ordenes: list) -> None:
    # Prune (code-review 10-Jul): los estados terminales se quedaban para
    # siempre y el fichero (leído+reescrito entero en el hot loop) crecía
    # sin límite. Se conservan 7 días de terminales para análisis del piloto.
    corte = (datetime.now(timezone.utc) - timedelta(days=7)).isoformat()
    vivos = [o for o in ordenes
             if o.get("estado") in ("enviando", "abierta")
             or str(o.get("ts_colocacion", "")) >= corte]
    tmp = MAKER_ORDERS_JSON.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(vivos, indent=1, ensure_ascii=False))
    tmp.replace(MAKER_ORDERS_JSON)


def _maker_mids_activos(ordenes: list | None) -> set:
    if not ordenes:
        return set()
    return {o.get("market_id", "") for o in ordenes
            if o.get("estado") in ("enviando", "abierta")}


def _maker_registrar_fill(o: dict, size_matched: float, precio_fill: float) -> bool:
    """Fila en trades.csv con la economía REAL del fill (API-confirmada).
    shadow_resolve la cierra a resolución como cualquier trade live.
    IDEMPOTENTE por market_id (code-review 10-Jul): si el mercado ya tiene
    fila en trades.csv (crash entre este append y la persistencia del estado
    'fill' en maker_orders.json → el ciclo siguiente re-ve MATCHED y volvería
    a entrar aquí), NO se duplica. Devuelve True solo si registró de verdad
    (el caller decide el Telegram con eso — nunca notificar un dedup)."""
    mid = o.get("market_id", "")
    if mid in _ya_operados_hoy():
        log(f"  ℹ️ maker fill ya registrado (dedup idempotente): {mid}")
        return False
    stake_real = round(size_matched * precio_fill, 4)
    trade = {
        "timestamp_utc":    datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "market_id":        mid,
        "question":         o.get("question", ""),
        "end_date":         o.get("end_date", ""),
        "strategy":         o.get("strategy", ""),
        "subtype":          o.get("subtype", ""),
        "direction":        o.get("direction", ""),
        "stake_eur":        stake_real,
        "entry_price":      precio_fill,
        "ic_modelo":        o.get("ic_modelo", ""),
        "edge_neto":        o.get("edge_neto", ""),
        "conviction_score": o.get("conviction_score", ""),
        "kelly_recomendado": o.get("stake_eur", ""),
        "status":           "OPEN",
        "fee_eur":          0.0,   # maker no paga fee de trading en el CLOB
        "notas":            (f"maker_pilot=1 precio_limit={o.get('precio_limit')} "
                             f"ask_colocacion={o.get('mejor_ask_colocacion')} "
                             f"size_matched={size_matched}"),
    }
    _registrar_trade(trade)
    return True


def _reconciliar_ordenes_maker() -> None:
    """Cada ciclo: consulta el estado real de cada orden maker no terminal.
    Nunca lanza. Solo construye el ClobClient si hay algo que reconciliar."""
    try:
        ordenes = _maker_estado_cargar()
        if not ordenes:   # None (ilegible) o lista vacía → nada que hacer aquí
            return
        pendientes = [o for o in ordenes if o.get("estado") in ("enviando", "abierta")]
        if not pendientes:
            return
        client = _get_clob_client()
        ahora = datetime.now(timezone.utc)
        cambiado = False
        for o in pendientes:
            try:
                # Huérfana: intent escrito pero sin order_id (crash antes de
                # guardar, o post OK con id bajo clave inesperada — ambos
                # dejan estado='enviando', recuperable). Se busca en las
                # órdenes abiertas reales del token. Precio comparado como
                # FLOAT con tolerancia (code-review 10-Jul: str(0.5) != '0.50'
                # del API mataba órdenes vivas). Margen de 120s antes de dar
                # por muerta: el post puede tardar en reflejarse.
                if o.get("estado") == "enviando" and not o.get("order_id"):
                    try:
                        from py_clob_client_v2 import OpenOrderParams
                        abiertas = client.get_open_orders(
                            OpenOrderParams(asset_id=o.get("token_id", ""))) or []
                        candidata = None
                        for a in abiertas:
                            try:
                                if (a.get("side", "").upper() == "BUY" and
                                        abs(float(a.get("price")) -
                                            float(o.get("precio_limit"))) < 0.005):
                                    candidata = a
                                    break
                            except (TypeError, ValueError):
                                continue
                        if candidata:
                            o["order_id"] = candidata.get("id", "")
                            o["estado"] = "abierta"
                            cambiado = True
                        else:
                            ts_col = datetime.fromisoformat(
                                str(o.get("ts_colocacion", "1970-01-01T00:00:00+00:00")))
                            if ts_col.tzinfo is None:
                                ts_col = ts_col.replace(tzinfo=timezone.utc)
                            if (ahora - ts_col).total_seconds() > 120:
                                o["estado"] = "muerta_sin_post"
                                cambiado = True
                    except Exception as e:
                        log(f"  ⚠️ maker: no se pudo adoptar huérfana {o.get('market_id')}: {e}")
                    continue

                info = client.get_order(o["order_id"]) or {}
                status = str(info.get("status", "")).upper()
                size_matched = float(info.get("size_matched", 0) or 0)
                precio_fill = float(info.get("price", o.get("precio_limit", 0)) or 0)

                # Timeout zombie (code-review 10-Jul): status no reconocido
                # (purgada → '', 'UNMATCHED'...) dejaba la orden 'abierta'
                # eterna, bloqueando el mercado y un slot del piloto. Pasado
                # el fin de mercado + 10min, se fuerza terminal registrando
                # el fill parcial si lo hubo.
                zombie = False
                try:
                    end_dt = datetime.fromisoformat(
                        str(o.get("end_date", "")).replace("Z", "+00:00"))
                    if end_dt.tzinfo is None:
                        end_dt = end_dt.replace(tzinfo=timezone.utc)
                    zombie = (ahora - end_dt).total_seconds() > 600
                except Exception:
                    pass

                es_fill = (status in ("MATCHED", "FILLED")
                           or (status in ("CANCELED", "CANCELLED", "EXPIRED")
                               and size_matched > 0)
                           or (zombie and size_matched > 0))
                if es_fill:
                    # Orden crítico anti-duplicado/anti-fantasma:
                    # (1) trades.csv (fuente de verdad de posiciones),
                    # (2) persistir estado YA (no al final del loop),
                    # (3) Telegram al final y solo si registró de verdad.
                    # Crash entre (1) y (2): el próximo ciclo re-entra y el
                    # dedup de _maker_registrar_fill lo hace idempotente.
                    registrado = _maker_registrar_fill(o, size_matched, precio_fill)
                    o["estado"] = "fill"
                    o["size_matched"] = size_matched
                    _maker_estado_guardar(ordenes)
                    cambiado = False
                    if registrado:
                        enviar_telegram(
                            f"🧷 *Fill MAKER (piloto vetadas)*\n"
                            f"{o.get('strategy')}#{o.get('subtype')} {o.get('direction')}\n"
                            f"Precio: {precio_fill:.4f} (limit {o.get('precio_limit')})\n"
                            f"Stake real: {size_matched * precio_fill:.2f}$ "
                            f"({size_matched} shares)"
                        )
                elif status in ("CANCELED", "CANCELLED", "EXPIRED") or zombie:
                    o["estado"] = "expirada_sin_fill" if not zombie else "zombie_cerrada"
                    cambiado = True
                    log(f"  ⏹ maker {o['estado']}: {o.get('market_id')} "
                        f"limit={o.get('precio_limit')} status_api={status or 'N/A'}")
                else:
                    # Sigue viva: si el mercado ya cerró y la orden no expiró
                    # (reloj del exchange vs el nuestro), cancelar activamente.
                    try:
                        end_dt = datetime.fromisoformat(
                            str(o.get("end_date", "")).replace("Z", "+00:00"))
                        if end_dt.tzinfo is None:
                            end_dt = end_dt.replace(tzinfo=timezone.utc)
                        if ahora > end_dt:
                            from py_clob_client_v2 import OrderPayload
                            client.cancel_order(OrderPayload(orderID=o["order_id"]))
                            log(f"  ⏹ maker cancelada post-cierre: {o.get('market_id')}")
                            # el estado real (fill parcial incluido) se lee en
                            # el próximo ciclo vía get_order — no se asume nada
                    except Exception:
                        pass
            except Exception as e:
                # Un fallo en UNA orden no bloquea el resto; la orden queda
                # tal cual y se reintenta el ciclo siguiente. GTD garantiza
                # que aunque esto falle para siempre, la orden muere sola.
                log(f"  ⚠️ maker: error reconciliando {o.get('market_id')}: {e}")
        if cambiado:
            _maker_estado_guardar(ordenes)
    except Exception as e:
        log(f"  ⚠️ maker: reconciliación abortada: {e}")


def _colocar_orden_maker(pred: dict, dec: str, contexto: dict) -> bool:
    """Coloca limit GTD a precio que NO cruza el ask, solo para señales
    recién vetadas por profundidad. Devuelve True si quedó colocada.
    Fail-closed en todo: cualquier duda → no colocar."""
    try:
        cfg = _maker_pilot_cfg()
        if not cfg["activo"]:
            return False
        ordenes = _maker_estado_cargar()
        if ordenes is None:   # estado ilegible → no colocar nada nuevo
            return False
        mid = pred.get("market_id", "")
        if mid in _maker_mids_activos(ordenes):
            return False   # ya hay orden viva para este mercado
        n_abiertas = sum(1 for o in ordenes
                         if o.get("estado") in ("enviando", "abierta"))
        if n_abiertas >= cfg["max_ordenes_abiertas"]:
            return False

        # Expiración GTD: T_fin - margen anti-sniper (maker_sim CANCEL_MIN).
        end_str = pred.get("end_date", "")
        end_dt = datetime.fromisoformat(end_str.replace("Z", "+00:00"))
        if end_dt.tzinfo is None:
            end_dt = end_dt.replace(tzinfo=timezone.utc)
        expiracion = end_dt.timestamp() - cfg["cancelar_antes_fin_seg"]
        ahora_ts = datetime.now(timezone.utc).timestamp()
        if expiracion - ahora_ts < MAKER_GTD_BUFFER_MIN_SEG:
            return False   # demasiado tarde para que la limit tenga sentido

        # Libro fresco para fijar el precio límite sin cruzar.
        yes_token, no_token, _ = _get_token_ids(mid)
        precio_yes = float(pred.get("precio_yes_mercado", 0.5))
        if dec == "BUY_YES":
            token_id, precio_plan = yes_token, precio_yes
        else:
            token_id, precio_plan = no_token, round(1.0 - precio_yes, 6)
        # Stake del piloto es SU PROPIA exposición acotada (max_ordenes_abiertas
        # x stake_eur, ya aprobada), no un techo adicional sobre stake_aprobado:
        # con el stake global pineado (max=min=1.05€), min(cfg_stake, stake_aprobado)
        # devolvía siempre 1.05€ pase lo que pase en config — bug descubierto
        # 11-Jul al intentar subir cfg_stake para cubrir el mínimo de 5 shares
        # del CLOB en órdenes limit y comprobar que no tenía ningún efecto. La
        # señal ya pasó IC/n/CLV/whitelist antes de llegar aquí (mismo bar que
        # cualquier señal taker), así que no hay conviction diferencial que
        # preservar limitando por stake_aprobado.
        stake = cfg["stake_eur"]

        # Freno diario prospectivo (code-review 11-Jul, mismo cálculo que
        # calcular_stake en live_stake.py): al dejar de capar por
        # stake_aprobado, el stake del piloto ya no heredaba este control —
        # mismo tipo de gap que el bug del 03-Jul (stakes abiertos sin
        # descontar dejó desplegar 6.54€ con el freno del 15%). Si el peor
        # caso (este stake + todo lo ya abierto perdido entero) rompe el
        # freno diario o el suelo de bankroll, no se coloca. Fail-closed.
        config_completo = _cargar_config()
        bkr_ini_dia = bankroll_inicio_dia()
        if bkr_ini_dia > 0:
            bkr_min = config_completo.get("riesgo", {}).get("circuit_breaker", {}).get("bankroll_minimo_eur", 5.0)
            # stakes_abiertos_total() solo ve trades.csv (posiciones YA
            # ejecutadas); las órdenes maker 'enviando'/'abierta' de este
            # mismo piloto aún no están ahí pero SÍ pueden llegar a llenarse
            # — hay que sumarlas o dos órdenes maker seguidas pasarían cada
            # una su propio check sin ver el riesgo pendiente de la otra
            # (mismo patrón que el bug de stakes abiertos del 03-Jul).
            pendientes_maker = sum(o.get("stake_eur", 0) or 0 for o in ordenes
                                    if o.get("estado") in ("enviando", "abierta"))
            abiertos = stakes_abiertos_total() + pendientes_maker
            margen_freno = bkr_ini_dia * freno_diario_pct_hoy(config_completo) + pnl_live_hoy() - abiertos
            margen_suelo = bankroll_actual() - bkr_min - abiertos
            margen_dia = min(margen_freno, margen_suelo)
            if stake > margen_dia:
                return False   # sin margen suficiente hoy para el stake del piloto

        depth = _consultar_profundidad_libro(None, token_id, precio_plan, stake)
        mejor_ask = depth.get("mejor_ask") if depth.get("ok") else None
        if mejor_ask is None:
            return False   # sin ask no hay referencia para no cruzar
        precio_limit = round(min(precio_plan, float(mejor_ask) - 0.01), 2)
        if precio_limit < 0.01 or precio_limit > REQUOTE_PRECIO_MAX:
            return False
        size = round(stake / precio_limit, 2)
        # Fail-closed (code-review 10-Jul, actualizado 11-Jul): si el notional
        # o el nº de shares quedan bajo el mínimo del CLOB, NO se infla el
        # tamaño (el bump podía exceder el stake aprobado por riesgo) —
        # simplemente no se coloca. Con stake_eur=2.75€ (11-Jul) esto no
        # ocurre en el rango de precios observado (~0.48-0.52); la guardia
        # protege si el precio se aleja de esa zona o el stake baja de nuevo.
        if size * precio_limit < MIN_ORDEN_CLOB_USD:
            return False
        if size < MIN_SHARES_CLOB_LIMIT:
            return False

        # Intent ANTES de postear (recuperable si morimos a mitad).
        entrada = {
            "estado": "enviando", "order_id": "",
            "market_id": mid, "token_id": token_id,
            "question": pred.get("question", ""),
            "end_date": end_str,
            "strategy": contexto.get("strategy", ""),
            "subtype": contexto.get("subtype", ""),
            "direction": dec,
            "stake_eur": round(size * precio_limit, 4),
            "precio_limit": precio_limit, "size": size,
            "mejor_ask_colocacion": mejor_ask,
            "ic_modelo": pred.get("prob_yes_modelo", ""),
            "edge_neto": pred.get("edge_neto", ""),
            "conviction_score": contexto.get("ic_hist", ""),
            "expiracion_utc": int(expiracion),
            "ts_colocacion": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
        ordenes.append(entrada)
        _maker_estado_guardar(ordenes)

        from py_clob_client_v2 import OrderArgsV2, OrderType
        client = _get_clob_client()
        order_args = OrderArgsV2(token_id=token_id, price=precio_limit,
                                 size=size, side="BUY",
                                 expiration=int(expiracion))
        signed = client.create_order(order_args)
        resp = client.post_order(signed, OrderType.GTD)
        entrada["order_id"] = resp.get("orderID") or resp.get("id") or ""
        # Sin order_id parseable NO es terminal (code-review 10-Jul): el post
        # pudo triunfar con el id bajo otra clave — se deja 'enviando' y la
        # rama de adopción de huérfanas lo resuelve (adopta si está viva en
        # el exchange, muerta_sin_post si tras 120s no aparece).
        entrada["estado"] = "abierta" if entrada["order_id"] else "enviando"
        _maker_estado_guardar(ordenes)
        _registrar_snapshot_libro("maker_colocada", mid, dec,
                                  precio_plan, stake, depth, contexto)
        log(f"  🧷 MAKER colocada (piloto vetadas): {mid} {dec} "
            f"limit={precio_limit} size={size} exp=T-{cfg['cancelar_antes_fin_seg']}s")
        return bool(entrada["order_id"])
    except Exception as e:
        log(f"  ⚠️ maker: colocación falló ({pred.get('market_id')}): {e}")
        return False

# Latencia máxima señal→ejecución (2026-07-10, hallazgo racha de pérdidas):
# predictions.csv loguea prob_yes_modelo/edge UNA vez (dedup ya_predichos) y
# live_trade reintenta la MISMA señal cada ciclo (~20-40s) hasta ejecutar o
# expirar la ventana — el re-quote solo refresca el PRECIO, nunca el modelo
# subyacente. Mecanismo confirmado en libro_snapshots: 11/12 señales con
# latencia≥100s tuvieron múltiples veto_profundidad antes de ejecutar (el
# libro, servido por bots de market-making activos en TODOS estos mercados,
# fluctúa de profundidad y solo deja pasar la señal por azar). Backtest sobre
# n=121 trades live (histórico completo, confound-checked por par y hora):
# latencia<100s → PnL total +32.26€; latencia≥100s → PnL total -16.45€. El
# efecto se sostiene DENTRO de cada par por separado (SOL delta -1.03€/trade,
# ETH -0.91€/trade), no es artefacto de un solo par. Código de seguridad
# live — no minimizar.
# ⚠️ Umbral plano aplicado a TODA predicción que llegue a este loop, pero el
# backtest que lo respalda es de GBM_LATE_15M (única estrategia en whitelist
# hoy, ventana de entrada 3-12min). Si se promociona a live una estrategia con
# ventana muy distinta (60min, daily...), revalidar 100s para esa estrategia
# antes de asumir que el mismo umbral aplica — no extender sin re-medir.
SENAL_MAX_LATENCIA_SEG = 100


def _decidir_requote(edge_dir: float, precio_plan: float,
                     mejor_ask: float | None) -> tuple[float, float, bool, str]:
    """Re-cotización en el momento de ejecutar (fix 2026-07-03).

    Antes la orden FOK salía al precio de la PREDICCIÓN (minutos de
    antigüedad): si el mercado había mejorado, el FOK moría ("couldn't be
    fully filled", 3 kills seguidos 2026-07-02 19:25) y perdíamos la entrada
    buena; si había empeorado, nos llenaban igual — selección adversa pura:
    solo ejecutábamos cuando el libro venía en contra.

    Con el mejor ask actual del libro:
      - deterioro = mejor_ask - precio_plan (>0 → pagamos más que al señalar)
      - el edge restante se recorta por el deterioro; la mejora NO infla el
        edge estimado (conservador)
      - si el edge restante < REQUOTE_EDGE_MIN → no operar (la señal caducó)
      - si sigue vivo → ejecutar al precio REAL del libro (el FOK casa)

    Devuelve (precio_final, edge_restante, operar, motivo).
    Sin libro (mejor_ask None) se mantiene el comportamiento anterior:
    precio de la predicción, edge tal cual. Código de seguridad live — no
    minimizar."""
    if mejor_ask is None:
        return precio_plan, edge_dir, True, "sin libro — precio de predicción"
    if mejor_ask > REQUOTE_PRECIO_MAX:
        return mejor_ask, 0.0, False, (
            f"mejor_ask={mejor_ask:.4f} > tope {REQUOTE_PRECIO_MAX}")
    deterioro = round(mejor_ask - precio_plan, 4)
    # Divergencia extrema plan↔libro = el mercado sabe algo que el snapshot
    # del modelo no vio (spot movido tras la señal). Un ask MUY por debajo
    # del plan no es regalo: 2026-07-03 08:49 XRP#15min BUY_YES señal a
    # 0.475 (modelo 0.62), libro a 0.12, fill 0.04 → resolvió NO, -1.63€.
    # El mercado a 11min del cierre tenía razón. El lado deterioro>0 ya lo
    # corta el chequeo de edge; este guard corta el lado "mejora" que antes
    # se celebraba. Código de seguridad live — no minimizar.
    if abs(deterioro) > REQUOTE_DIVERGENCIA_MAX:
        return mejor_ask, 0.0, False, (
            f"divergencia plan↔libro {deterioro:+.4f} > {REQUOTE_DIVERGENCIA_MAX} "
            f"(plan {precio_plan:.4f}, ask {mejor_ask:.4f}) — modelo desfasado, no operar")
    edge_ahora = round(edge_dir - max(0.0, deterioro), 4)
    if edge_ahora < REQUOTE_EDGE_MIN:
        return mejor_ask, edge_ahora, False, (
            f"edge evaporado: {edge_dir:+.4f} → {edge_ahora:+.4f} "
            f"(ask {precio_plan:.4f}→{mejor_ask:.4f}) < {REQUOTE_EDGE_MIN}")
    if deterioro > 0:
        motivo = f"deterioro {deterioro:+.4f} pero edge vivo ({edge_ahora:+.4f})"
    elif deterioro < 0:
        motivo = f"precio mejoró {deterioro:+.4f} — antes el FOK moría aquí"
    else:
        motivo = "precio sin cambios"
    return mejor_ask, edge_ahora, True, motivo


def _ejecutar_orden_polymarket(market_id: str, direction: str,
                               stake_eur: float, entry_price: float,
                               edge_dir: float | None = None,
                               contexto: dict | None = None) -> dict:
    """Ejecuta orden real en Polymarket via CLOB API.

    edge_dir: edge neto A FAVOR de nuestra dirección (edge_neto de la
    predicción con el signo ya resuelto: +edge para BUY_YES, -edge para
    BUY_NO). Si se pasa, se re-cotiza contra el libro actual antes de
    ejecutar (ver _decidir_requote)."""
    depth: dict = {}
    precio_plan = entry_price
    try:
        from py_clob_client_v2 import MarketOrderArgsV2, OrderType
        yes_token, no_token, condition_id = _get_token_ids(market_id)
        if direction == "BUY_YES":
            token_id = yes_token
            precio   = entry_price
        else:  # BUY_NO
            token_id = no_token
            precio   = round(1.0 - entry_price, 6)
        precio_plan = precio   # precio del token en el momento de la señal

        # veto_ballenas (16-Jul, ver constantes/docstring arriba): evaluado
        # AQUÍ, antes del libro/re-quote, a propósito -- no depende de
        # `depth`, y así el re-quote sigue siendo el último chequeo antes de
        # firmar (moverlo después del re-quote fue el bug real que cazó el
        # code-review de este mismo día: sus llamadas de red podían dejar
        # stale el precio que el re-quote acababa de confirmar fresco).
        ctx = contexto or {}
        activo_vb = (ctx.get("subtype") or "").split("#")[0]
        marco_vb = _marco_ballenas(ctx.get("subtype") or "")
        veto_vb = _evaluar_veto_ballenas(condition_id, activo_vb, marco_vb, precio_plan,
                                         direction, _cargar_config())
        if veto_vb.get("aplica"):
            _registrar_evento_ballenas(market_id, veto_vb)
            motivo_vb = veto_vb.get("motivo")
            if motivo_vb in ("sin_datos", "sin_condition_id"):
                log(f"  🐋 Ballenas {veto_vb.get('combo')}: SIN DATOS ({motivo_vb}, n={veto_vb.get('n', 0)}) "
                    f"— fail-open vigilado (vigia_ballenas_cobertura.py), se sigue evaluando normal")
            elif veto_vb.get("veta"):
                log(f"  🐋 Ballenas {veto_vb['combo']}: {veto_vb['pct']*100:.1f}% a favor (n={veto_vb['n']}) "
                    f"< umbral {veto_vb['umbral']*100:.0f}% — VETO")
                _registrar_snapshot_libro("veto_ballenas_debil", market_id, direction,
                                          precio_plan, stake_eur, depth, contexto)
                return {
                    "ok": False, "no_fill": True, "ballenas_debil": True,
                    "order_id": None, "entry_price": entry_price,
                    "fee_eur": 0.0,
                    "error": f"ballenas {veto_vb['pct']*100:.1f}% (n={veto_vb['n']}) "
                             f"< umbral {veto_vb['umbral']*100:.0f}%",
                }
            else:
                log(f"  🐋 Ballenas {veto_vb['combo']}: {veto_vb['pct']*100:.1f}% a favor (n={veto_vb['n']}) "
                    f">= umbral {veto_vb['umbral']*100:.0f}% — OK")

        # Libro público (2026-07-10): el ClobClient autenticado NO hace falta
        # para leer profundidad (/book es público) — construirlo aquí pagaba
        # ~270ms de import EN TODO INTENTO, incluidos los que terminan en
        # veto_profundidad/veto_sin_datos/abort_requote (la inmensa mayoría:
        # histórico 2515+345 vetos vs 129 ejecutadas). Se construye más abajo,
        # SOLO si de verdad vamos a firmar y enviar la orden.
        depth = _consultar_profundidad_libro(None, token_id, precio, stake_eur)
        if depth.get("ok"):
            log(f"  📊 Libro {market_id}/{direction}: mejor_ask={depth['mejor_ask']} "
                f"profundidad≈{depth['profundidad_eur']:.2f}€ "
                f"({depth['n_niveles']} niveles, ratio={depth['ratio_vs_stake']}x stake)")
        else:
            log(f"  📊 Libro {market_id}/{direction}: error consultando profundidad — {depth.get('error')}")

        # Veto por profundidad: 2026-07-03 XRP/SOL#15min ejecutaron contra
        # libros con profundidad 0.00€ (ratio=0.0x, ask oscilando 0.52↔0.75
        # en segundos) y el slippage real (+0.04/+0.085) se comió el edge:
        # -3.19€. El re-quote solo mira el mejor ask de UN snapshot — en un
        # libro vacío ese snapshot es ruido. Fail-closed: si la consulta del
        # libro falla tampoco se ejecuta (sin libro no hay re-quote fiable).
        # Código de seguridad live — no minimizar.
        min_ratio = _cargar_config().get("riesgo", {}).get("min_profundidad_ratio_libro", 5.0)
        if not depth.get("ok"):
            log(f"  ⛔ Sin datos de libro — no se ejecuta (fail-closed)")
            _registrar_snapshot_libro("veto_sin_datos", market_id, direction,
                                      precio_plan, stake_eur, depth, contexto)
            return {
                "ok": False, "no_fill": True, "libro_sin_datos": True,
                "order_id": None, "entry_price": entry_price,
                "fee_eur": 0.0, "error": f"profundidad no consultable: {depth.get('error')}",
            }
        ratio = depth.get("ratio_vs_stake")
        if ratio is None or ratio < min_ratio:
            log(f"  ⛔ Libro sin profundidad: ratio={ratio}x < {min_ratio}x stake — no se ejecuta")
            _registrar_snapshot_libro("veto_profundidad", market_id, direction,
                                      precio_plan, stake_eur, depth, contexto)
            return {
                "ok": False, "no_fill": True, "libro_vacio": True,
                "order_id": None, "entry_price": entry_price,
                "fee_eur": 0.0, "error": f"profundidad insuficiente: ratio={ratio}x < {min_ratio}x",
            }

        # Re-cotización con el libro actual (solo si el caller pasó edge_dir)
        if edge_dir is not None:
            mejor_ask = depth.get("mejor_ask") if depth.get("ok") else None
            mejor_ask = float(mejor_ask) if mejor_ask is not None else None
            precio, edge_vivo, operar, motivo_rq = _decidir_requote(
                edge_dir, precio_plan, mejor_ask)
            log(f"  🔁 Re-quote: {motivo_rq}")
            if not operar:
                _registrar_snapshot_libro("abort_requote", market_id, direction,
                                          precio_plan, stake_eur, depth, contexto)
                return {
                    "ok": False, "no_fill": True, "edge_evaporado": True,
                    "order_id": None, "entry_price": entry_price,
                    "fee_eur": 0.0, "error": f"requote: {motivo_rq}",
                }

        # Estimación Kyle (10-Jul, solo logging — ver _estimar_slip_kyle):
        # ratio del snapshot de profundidad YA calculado arriba, antes del
        # requote. No cambia ninguna decisión, se compara con slip_real real
        # una vez conocido más abajo.
        slip_estimado_kyle = _estimar_slip_kyle(depth.get("ratio_vs_stake") if depth.get("ok") else None)

        client = _get_clob_client()  # recién aquí: vetos/requote ya pasaron, orden real inminente
        _marcar_orden_en_curso(market_id, direction)
        try:
            # py_clob_client_v2 calcula makerAmount/takerAmount dividiendo
            # amount/price en float puro y redondeando después — para ciertas
            # combinaciones concretas el resultado conserva más decimales de
            # los que el tick del mercado permite y el CLOB rechaza la orden
            # con "invalid amounts" (confirmado en real 2026-07-01, stake=0€
            # perdido = ningún dinero en riesgo, solo la señal). Es un bug de
            # precisión de coma flotante en la librería (order_builder/
            # builder.py::get_market_order_amounts, no en nuestro código), no
            # reproducible de forma determinista sin acceso al validador del
            # CLOB. Mitigación: un reintento con el stake desplazado 1
            # céntimo cambia el resultado de la división y en la práctica
            # evita la misma colisión — ningún intento previo llega a
            # ejecutarse de verdad (el rechazo es previo al match), así que
            # reintentar no puede duplicar la operación.
            _max_stake = _cargar_config().get("riesgo", {}).get("max_stake_eur", 2.00)
            intentos_stake = [stake_eur, round(stake_eur - 0.01, 2)]
            _mas = round(stake_eur + 0.01, 2)
            if _mas <= _max_stake:
                intentos_stake.append(_mas)
            # El CLOB exige ≥$1 en órdenes marketable BUY ("min size: 1") —
            # 2026-07-03: 2 señales rechazadas con stake 0.94/0.98€. El suelo
            # min_stake_eur=1.05 del config debería impedir llegar aquí con
            # menos; este filtro es la red fail-closed si alguna ruta lo salta.
            intentos_stake = [a for a in intentos_stake if a >= MIN_ORDEN_CLOB_USD]
            if not intentos_stake:
                log(f"  ⛔ Stake {stake_eur:.2f}€ < mínimo CLOB ${MIN_ORDEN_CLOB_USD:.2f} — no se ejecuta")
                return {
                    "ok": False, "no_fill": True, "stake_bajo_minimo": True,
                    "order_id": None, "entry_price": entry_price,
                    "fee_eur": 0.0,
                    "error": f"stake {stake_eur:.2f} < mínimo CLOB {MIN_ORDEN_CLOB_USD}",
                }
            resp = None
            for intento, amt in enumerate(intentos_stake):
                if amt <= 0:
                    continue
                order_args = MarketOrderArgsV2(
                    token_id=token_id,
                    amount=amt,
                    side="BUY",
                    price=precio,
                )
                try:
                    signed_order = client.create_market_order(order_args)
                    resp = client.post_order(signed_order, OrderType.FOK)
                    stake_eur = amt
                    if intento > 0:
                        log(f"  ⚠️  Orden aceptada en reintento {intento} con stake={amt:.2f}€ "
                            f"(precisión decimal, ver comentario en código)")
                    break
                except Exception as e_intento:
                    if "invalid amounts" not in str(e_intento) or intento == len(intentos_stake) - 1:
                        raise
                    log(f"  ⚠️  'invalid amounts' con stake={amt:.2f}€, reintentando con otro monto...")
            if resp is None:
                raise RuntimeError("no se pudo construir una orden con amounts válidos")
        finally:
            _limpiar_orden_en_curso()

        order_id = resp.get("orderID") or resp.get("id") or str(resp)
        filled_price = float(resp.get("price", precio))
        fee = float(resp.get("feeRateBps", 0)) / 10000 * stake_eur

        # Slippage real señal→fill (en el token comprado). Se acumula en
        # `notas` para calibrar SLIPPAGE_ESTIMADO (hoy constante 0.02) con
        # datos reales cuando haya n≥30 fills.
        slip_real = round(filled_price - precio_plan, 4)

        log(f"  ✅ Orden ejecutada: {direction} market={market_id} "
            f"stake={stake_eur:.2f}€ precio={filled_price:.4f} "
            f"slip={slip_real:+.4f} order_id={order_id}")
        _registrar_snapshot_libro("ejecutada", market_id, direction,
                                  precio_plan, stake_eur, depth, contexto)
        return {
            "ok":          True,
            "order_id":    order_id,
            "entry_price": filled_price,
            "fee_eur":     fee,
            "slip_real":   slip_real,
            "slip_estimado_kyle": slip_estimado_kyle,
            "error":       "",
        }
    except Exception as e:
        err_str = str(e)
        if "couldn't be fully filled" in err_str or "FOK" in err_str:
            log(f"  ⚠️  FOK kill (sin liquidez a ese precio) — no fill: {e}")
            _registrar_snapshot_libro("fok_kill", market_id, direction,
                                      precio_plan, stake_eur, depth, contexto)
            return {
                "ok":       False,
                "no_fill":  True,
                "order_id": None,
                "entry_price": entry_price,
                "fee_eur":  0.0,
                "error":    err_str,
            }
        # post_only_mode (16-Jul, primera vez visto en real: FAVORITO_CONFIRMADO
        # #SOL#60min, 04:08 UTC): el CLOB entra en un estado temporal donde solo
        # acepta post-only/cancels, y la propia respuesta incluye
        # "retry_after_seconds" — es transitorio del exchange, no un problema
        # con nuestra orden. Antes caía al branch genérico de abajo con
        # no_fill=False, así que el caller (main()) escribía un trade ERROR y
        # el market_id quedaba bloqueado en ya_operados_hoy para siempre — la
        # señal se perdía pese a que la propia API pedía reintentar. Tratado
        # igual que FOK kill: no_fill=True, no se registra nada, la señal
        # sigue viva y el próximo ciclo (~5s, ya menor que el retry_after_seconds
        # típico de 6s) la re-evalúa: si sigue siendo buena (sigue viva,
        # latencia<100s, pasa los mismos gates) se reintenta sola; si el
        # estado persiste hasta que la señal caduque, muere por señal_caducada
        # como cualquier otra — nunca se fuerza un reintento bloqueante aquí.
        if "post_only_mode" in err_str or "post-only mode" in err_str:
            log(f"  ⚠️  CLOB en post-only mode (temporal, reintentable) — no fill: {e}")
            _registrar_snapshot_libro("post_only_mode", market_id, direction,
                                      precio_plan, stake_eur, depth, contexto)
            return {
                "ok":       False,
                "no_fill":  True,
                "order_id": None,
                "entry_price": entry_price,
                "fee_eur":  0.0,
                "error":    err_str,
            }
        log(f"  ❌ Error ejecutando orden: {e}")
        return {
            "ok":          False,
            "no_fill":     False,
            "order_id":    None,
            "entry_price": entry_price,
            "fee_eur":     0.0,
            "error":       err_str,
        }


# ── Smart Exit — stop-loss (16-Jul, petición Javi) ─────────────────────────
# Venta anticipada de una posición live OPEN antes de resolución, cuando la
# pérdida no realizada (con haircut de spread+fee real) cruza un umbral —
# espejo del take-profit original de idea_smart_exit.md. Calibración: n=28
# pérdidas reales (smart_exit_prices.csv desde 10-Jul), umbral -0.30€ mejora
# esas 28 en +12.68€ SI se pudiera vender cualquier tamaño; la restricción
# real del CLOB (min_order_size del libro, shares=stake/entry_price casi
# siempre <5 con stake pineado en 1.05€) recorta la mejora a +1.71€ (6/28
# elegibles). Gateado por riesgo.smart_exit_stop_loss.activo en
# config_live.json — shadow_resolve._check_salidas_tempranas no llama a
# nada de esto mientras activo=false (default). Fail-closed en cada paso:
# libro no consultable, shares por debajo del mínimo del CLOB, o cualquier
# error de firma/red → no vende, la posición sigue OPEN y el camino normal
# de resolución sigue intacto. Nunca puede empeorar el resultado. Código de
# seguridad live — no minimizar.

def _consultar_libro_venta(token_id: str, min_order_size_fallback: float) -> dict:
    """Lado bid del libro (donde vendemos), vía el mismo endpoint público que
    _fetch_book_publico. min_order_size viene del propio libro (campo real
    del CLOB, verificado 16-Jul en ~10 mercados cripto) si lo expone; si no,
    se usa el fallback de config. Nunca lanza — ok=False en cualquier duda."""
    try:
        book = _fetch_book_publico(token_id)
        if book is None:
            return {"ok": False, "error": "sin respuesta del libro (público)"}
        bids = (book.get("bids") if isinstance(book, dict) else getattr(book, "bids", None)) or []
        if not bids:
            return {"ok": False, "error": "libro sin bids"}
        try:
            min_order_size = float(book.get("min_order_size"))
        except (TypeError, ValueError):
            min_order_size = min_order_size_fallback
        mejor_bid = max(float(b.get("price") if isinstance(b, dict) else b.price) for b in bids)
        return {"ok": True, "mejor_bid": mejor_bid, "min_order_size": min_order_size}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def _ejecutar_venta_temprana(market_id: str, direction: str, entry_price: float,
                             stake_eur: float) -> dict:
    """Vende anticipadamente en el CLOB la posición (market_id, direction)
    comprada a entry_price/stake_eur. Devuelve siempre {"ok": ...} — nunca
    lanza; el caller (shadow_resolve._check_salidas_tempranas) deja la
    posición OPEN sin cambios si ok=False."""
    try:
        if entry_price <= 0 or stake_eur <= 0:
            return {"ok": False, "error": "entry_price/stake_eur inválidos"}
        from py_clob_client_v2 import MarketOrderArgsV2, OrderType
        yes_token, no_token, _ = _get_token_ids(market_id)
        token_id = yes_token if direction == "BUY_YES" else no_token
        shares = stake_eur / entry_price

        cfg = _cargar_config().get("riesgo", {}).get("smart_exit_stop_loss", {})
        min_fallback = float(cfg.get("min_profundidad_ratio_bid", 5.0))

        libro = _consultar_libro_venta(token_id, min_fallback)
        if not libro.get("ok"):
            log(f"  ⛔ Smart-exit stop-loss: libro no consultable ({libro.get('error')}) — no se vende, sigue OPEN")
            return {"ok": False, "no_fill": True, "error": libro.get("error")}

        min_order_size = libro["min_order_size"]
        if shares < min_order_size:
            log(f"  ⛔ Smart-exit stop-loss: shares={shares:.3f} < min_order_size={min_order_size} — no se vende, sigue OPEN")
            return {"ok": False, "no_fill": True, "shares_insuficientes": True,
                    "error": f"shares {shares:.3f} < min_order_size {min_order_size}"}

        client = _get_clob_client()
        _marcar_orden_en_curso(market_id, direction)
        try:
            order_args = MarketOrderArgsV2(
                token_id=token_id,
                amount=round(shares, 4),
                side="SELL",
                price=0,  # auto-calculado por el cliente contra el libro real al firmar
            )
            signed_order = client.create_market_order(order_args)
            resp = client.post_order(signed_order, OrderType.FOK)
        finally:
            _limpiar_orden_en_curso()

        order_id = resp.get("orderID") or resp.get("id") or str(resp)
        filled_price = float(resp.get("price", libro.get("mejor_bid", 0)))
        valor_venta_eur = filled_price * shares
        fee = float(resp.get("feeRateBps", 0)) / 10000 * valor_venta_eur
        pnl_neto = valor_venta_eur - stake_eur - fee

        log(f"  🔴 Smart-exit stop-loss EJECUTADO: {market_id}/{direction} "
            f"shares={shares:.3f} precio_venta={filled_price:.4f} "
            f"pnl_neto={pnl_neto:+.2f}€ order_id={order_id}")
        return {
            "ok": True, "order_id": order_id, "exit_price": filled_price,
            "valor_venta_eur": round(valor_venta_eur, 4),
            "fee_eur": round(fee, 4), "pnl_neto_eur": round(pnl_neto, 4),
        }
    except Exception as e:
        err = str(e)
        if "couldn't be fully filled" in err or "FOK" in err:
            log(f"  ⚠️  Smart-exit stop-loss FOK kill (sin liquidez) — sigue OPEN: {e}")
        else:
            log(f"  ❌ Error en venta anticipada (smart-exit stop-loss) — sigue OPEN: {e}")
        return {"ok": False, "no_fill": True, "error": err}


def _evaluar_pre_trade(pred: dict, decision: str) -> tuple[bool, str]:
    """
    Evaluador independiente pre-trade (generator/evaluator split — Loop Engineering).
    Actúa como skeptic: asume que la señal está mal hasta que se demuestre lo contrario.
    Rechaza si ≥2 señales independientes contradicen la predicción.
    Las señales individuales son ruidosas; se necesita consenso para rechazar.
    """
    flags = []

    try:
        feats = json.loads(pred.get("features", "{}") or "{}")
    except Exception:
        feats = {}

    # 1. Predicción vieja (>5 min) — el mercado pudo moverse desde que se generó
    try:
        pred_ts = datetime.fromisoformat(
            pred.get("timestamp_utc", "").replace("Z", "+00:00"))
        if pred_ts.tzinfo is None:
            pred_ts = pred_ts.replace(tzinfo=timezone.utc)
        age_min = (datetime.now(timezone.utc) - pred_ts).total_seconds() / 60
        if age_min > 5:
            flags.append(f"pred_vieja={age_min:.0f}min>5")
    except Exception:
        pass

    # 2. Edge en el momento de ejecutar demasiado pequeño (más estricto que el modelo)
    try:
        edge = float(pred.get("edge_neto", 0))
    except (ValueError, TypeError):
        edge = 0.0
    if abs(edge) < 0.025:
        flags.append(f"edge={edge:.4f}<0.025")

    # 3. Funding rate de perps contradice la dirección
    fr = feats.get("funding_rate_8h")  # % por 8h
    if fr is not None:
        if decision == "BUY_YES" and fr > 0.05:
            flags.append(f"funding={fr:+.3f}%/8h longs_sobrecargados vs BUY_YES")
        elif decision == "BUY_NO" and fr < -0.02:
            flags.append(f"funding={fr:+.3f}%/8h shorts_sobrecargados vs BUY_NO")

    # 4. Drift interno de Polymarket (poly_drift_5obs) contradice fuertemente
    poly_d = feats.get("poly_drift_5obs")
    if poly_d is not None and abs(poly_d) > 1.5:
        if decision == "BUY_YES" and poly_d < -1.5:
            flags.append(f"poly_drift={poly_d:+.2f}% vende_YES vs BUY_YES")
        elif decision == "BUY_NO" and poly_d > 1.5:
            flags.append(f"poly_drift={poly_d:+.2f}% compra_YES vs BUY_NO")

    if len(flags) >= 2:
        return False, f"{len(flags)} señales contrarias: " + " | ".join(flags)
    flag_str = f"({flags[0]})" if flags else "sin flags"
    return True, f"PASS {flag_str}"


def _registrar_trade(row: dict):
    # flock (16-Jul): ver nota junto a TRADES_LOCK_PATH -- protege el
    # append en sí de un entrelazado entre dos procesos escribiendo a la
    # vez (no es una garantía TOCTOU completa sobre ya_operados, pero
    # cierra el riesgo real que existe hoy: dos escrituras simultáneas al
    # mismo fichero).
    with open(TRADES_LOCK_PATH, "w") as lock_f:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        try:
            nuevo = not TRADES_CSV.exists()
            with open(TRADES_CSV, "a", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=TRADES_COLS)
                if nuevo:
                    w.writeheader()
                w.writerow({col: row.get(col, "") for col in TRADES_COLS})
        finally:
            fcntl.flock(lock_f, fcntl.LOCK_UN)


OVERRIDES_NOTIF_PATH = DIR_LIVE / "overrides_notificados.json"


def _avisar_override_superado(key: str, n_real: int, min_n_global: int):
    """Telegram una sola vez cuando el n direccional real de una key con
    min_n_overrides alcanza el umbral global — a partir de ahí el override
    ya no hace falta y se puede quitar de config_live.json."""
    try:
        notificados = json.loads(OVERRIDES_NOTIF_PATH.read_text()) if OVERRIDES_NOTIF_PATH.exists() else {}
    except Exception:
        notificados = {}
    if notificados.get(key):
        return
    enviar_telegram(
        f"✅ *Override de min_n ya no hace falta*\n"
        f"{key}\n"
        f"n real = {n_real} ≥ min_n_para_live ({min_n_global})\n"
        f"Puedes quitar la entrada de `min_n_overrides` en config_live.json."
    )
    log(f"  ℹ️  Override {key} superó min_n global ({n_real}≥{min_n_global}) — avisado por Telegram")
    notificados[key] = {"n_real": n_real, "ts": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    OVERRIDES_NOTIF_PATH.write_text(json.dumps(notificados, indent=2))


def _latencia_seg(pred: dict) -> float | None:
    """Segundos desde timestamp_utc de la predicción hasta ahora. None si
    vacío o sin parsear (fail-closed: el llamante debe tratar None como
    caducado, igual que el chequeo de señal caducada en main())."""
    ts_str = pred.get("timestamp_utc", "")
    try:
        if not ts_str:
            return None
        ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - ts).total_seconds()
    except Exception:
        return None


def _tupla_activa(strategy: str, subtype: str, params: dict, direccion: str = "") -> bool:
    """True si NINGÚN nivel de la jerarquía strategy/subtype/activo/dirección
    está desactivado en strategy_params.json. Fail-closed: cualquier nivel
    desactivado bloquea, igual que shadow_predict.py para generar.

    Direction-aware (auditoría 15-Jul): el 'activa' de cada nivel se calcula
    en shadow_postmortem.py sobre el IC MIXTO (BUY_YES+BUY_NO); una tupla
    live es siempre de una sola dirección, así que un BUY_NO hundido (aunque
    ni siquiera sea live) podía apagar en silencio un BUY_YES live sano, o
    al revés enmascarar uno malo. Si se pasa `direccion` y el nivel tiene el
    campo direction-aware `activa_{direccion}`, se usa ese; si no existe
    (datos viejos u otra dirección sin volumen), cae al 'activa' mixto —
    mismo comportamiento fail-closed de antes."""
    if "#" in subtype:
        _a, _d = subtype.split("#", 1)
        keys = [f"{strategy}#{subtype}", f"{strategy}#{_a}", f"{strategy}#{_d}", strategy]
    elif subtype:
        keys = [f"{strategy}#{subtype}", strategy]
    else:
        keys = [strategy]
    campo_dir = f"activa_{direccion}" if direccion else None
    for k in keys:
        entry = params.get(k)
        if not entry:
            continue
        if campo_dir and campo_dir in entry:
            if not entry[campo_dir]:
                return False
        elif not entry.get("activa", True):
            return False
    return True


def main():
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    log(f"=== live_trade ciclo {ts} ===")

    # 1. Guardián: ¿podemos operar ahora?
    puede, motivo = puede_operar_live()
    est = estado_live()
    log(f"  Switch: {'ON' if est['switch'] else 'OFF'} | "
        f"Ventana: {'SÍ' if est['en_ventana'] else 'NO'} ({motivo}) | "
        f"Hora Madrid: {est['hora_madrid']} ({est['dia']})")

    _snapshots_candidatos_evaluacion()
    # Reconciliación maker ANTES del gate de ventana: un fill puede llegar en
    # cualquier momento y debe registrarse pronto (shadow_resolve lo cierra,
    # los frenos lo cuentan). Es bookkeeping de órdenes ya colocadas, no
    # riesgo nuevo.
    _reconciliar_ordenes_maker()

    if not puede:
        log(f"  → Fuera de operación. Motivo: {motivo}")
        _snapshots_fuera_ventana()
        return

    # 2. Circuit breaker — verificar límites de pérdida antes de operar
    disparado, motivo_cb = verificar_circuit_breaker()
    desp  = stakes_desplegados_ventana_actual()
    pnl_d = pnl_live_hoy()
    log(f"  Circuit breaker: desplegado_ventana={desp:.2f}€  pnl_día={pnl_d:+.2f}€  → {'🛑 DISPARADO' if disparado else '✅ OK'}")

    if disparado:
        log(f"  🛑 CIRCUIT BREAKER: {motivo_cb}")
        # Aviso Telegram UNA vez por día Madrid Y POR TIPO de freno (petición
        # Javi 13-Jul: el ciclo rápido reintenta live_trade 4x/~20s, así que
        # sin latch esto reenviaba el mismo aviso cada pocos segundos —
        # mismo patrón de spam ya resuelto en vigia_ic_live_latch.json
        # (12-Jul). Clave por TIPO, no por motivo_cb completo: motivo_cb
        # lleva números que cambian cada ciclo (bkr, %, racha), así que
        # dedupar por el string entero no dedupa nada; clave por fecha SOLA
        # tampoco vale, silenciaría un freno DISTINTO y más grave que se
        # disparase el mismo día tras uno más leve (ej. racha=4 por la
        # mañana, bankroll_minimo por la tarde) — cada tipo avisa una vez,
        # independientemente de si otro tipo ya avisó hoy. Se resetea solo
        # con el día nuevo, sin acción manual.
        if "bankroll" in motivo_cb and "mínimo" in motivo_cb:
            _tipo_cb = "bankroll_minimo"
        elif "caída diaria" in motivo_cb:
            _tipo_cb = "freno_diario"
        elif "pérdidas live consecutivas" in motivo_cb:
            _tipo_cb = "racha"
        elif "ventana" in motivo_cb:
            _tipo_cb = "freno_ventana"
        else:
            _tipo_cb = "otro"
        _cb_latch_path = DIR_LIVE / "circuit_breaker_aviso_latch.json"
        try:
            _cb_latch = json.loads(_cb_latch_path.read_text()) if _cb_latch_path.exists() else {}
        except Exception:
            _cb_latch = {}
        _fecha_hoy = est.get("fecha", "")
        _clave_cb = f"{_fecha_hoy}#{_tipo_cb}"
        if _cb_latch.get("clave") != _clave_cb:
            _snap_cb = cargar_balance_real(max_edad_s=3600)
            _real_cb = (f"Balance real: {_snap_cb['total']:.2f}$ (PnL real {_snap_cb['pnl_real']:+.2f})\n"
                        if _snap_cb and not _snap_cb.get("_rancio") else "")
            ok = enviar_telegram(
                f"🛑 *CIRCUIT BREAKER DISPARADO*\n"
                f"{motivo_cb}\n"
                f"Bankroll operativo: {bankroll_actual():.2f}$\n"
                f"PNL hoy (operativo): {pnl_live_hoy():+.2f}$\n"
                f"{_real_cb}"
                f"Bot parado. Usa `/live_switch.sh on` para reactivar.\n"
                f"(Este aviso solo llega una vez por tipo de freno al día — "
                f"el freno sigue activo aunque no recibas más mensajes de este tipo.)"
            )
            try:
                _cb_latch_path.write_text(json.dumps({"clave": _clave_cb, "motivo": motivo_cb, "telegram_ok": ok}))
            except Exception:
                pass  # best-effort, igual que _escribir_latch_ventana — el freno ya paró el ciclo
        return

    # 3. Cargar predicciones y parámetros
    predicciones = _cargar_predicciones_hoy()
    params       = _cargar_params()
    config       = _cargar_config()
    riesgo       = config.get("riesgo", {})
    min_ic       = riesgo.get("min_ic_para_live", 0.08)
    min_n        = riesgo.get("min_n_para_live", 40)
    min_n_overrides   = riesgo.get("min_n_overrides", {})
    min_ic_asimetrico = riesgo.get("min_ic_asimetrico", {})
    factor_ic_concurrente = riesgo.get("factor_ic_2a_senal_concurrente", 0.25)
    # Whitelist por tupla exacta STRATEGY#SUBTYPE#DIRECTION. Antes eran dos
    # listas independientes (estrategias × subtypes) y el producto cartesiano
    # dejaba pasar combinaciones nunca aprobadas: UPDOWN_GBM#SOL#15min
    # (02-Jul, -2.00€ real) y UPDOWN_GBM#BTC#15min (03-Jul, -2.00€ real).
    # Fail-closed: lista vacía o ausente → no se opera nada. Código de
    # seguridad live — no minimizar.
    pares_ok = set(config.get("pares_permitidos_live", []))
    if not pares_ok:
        log("  ⚠️ pares_permitidos_live vacío o ausente en config — no se opera (fail-closed)")

    # Ensemble entre tuplas whitelisted (propuesta #8 backlog quant-desk,
    # aprobado Javi 11-Jul, ver analisis_ensemble_estrategias.py): dos tuplas
    # whitelisted distintas prediciendo sobre el MISMO market_id no son
    # independientes. Shadow (7 tuplas exactas de pares_permitidos_live,
    # results.csv): coinciden en dirección → hit 67.8% n=239 (vs 62.7% n=833
    # solas); discrepan en dirección → hit 50.0% n=30, y ese n=30 es
    # ÍNTEGRAMENTE un solo par estructural (FAVORITO_CONFIRMADO#BTC#BUY_NO vs
    # GBM_LATE_15M_ESPACIO_ATR#BTC#BUY_YES, ambas whitelisted en direcciones
    # opuestas sobre el mismo activo/ventana). Mapa mid → decision →
    # {tuplas}, construido UNA vez por ciclo a partir de las predicciones de
    # HOY (no solo las que llegan a ejecutarse) para que la señal que se
    # procesa primero en el bucle no decida el conflicto por orden arbitrario.
    # Mismos dos filtros fail-closed que ya se exigen a la señal que se
    # ejecuta (code-review adversarial 11-Jul, antes de esto el mapa se
    # construía sin ellos): (1) latencia < SENAL_MAX_LATENCIA_SEG — sin esto
    # una fila de hace horas del mismo mercado (aún abierto) podía vetar/
    # boostear con datos caducos; (2) activa=True — sin esto una tupla
    # desactivada que sigue emitiendo por ACUMULAR_SHADOW_AUNQUE_DESACTIVADA
    # podía vetar a una tupla hermana que sí es plenamente ejecutable.
    _wl_por_mercado: dict[str, dict[str, set]] = defaultdict(lambda: defaultdict(set))
    for _p in predicciones:
        _p_strat, _p_sub, _p_dec = _p.get("strategy", ""), _p.get("subtype", ""), _p.get("decision", "")
        _key = f"{_p_strat}#{_p_sub}#{_p_dec}"
        if _key not in pares_ok:
            continue
        _lat = _latencia_seg(_p)
        if _lat is None or _lat >= SENAL_MAX_LATENCIA_SEG:
            continue
        if not _tupla_activa(_p_strat, _p_sub, params, _p_dec):
            continue
        _wl_por_mercado[_p.get("market_id", "")][_p_dec].add(_key)
    boost_ic_coincidencia   = riesgo.get("boost_ic_coincidencia_tuplas", 1.0)
    boost_ic_smartmoney_sol = riesgo.get("boost_ic_smartmoney_favorito_sol", 1.0)

    ya_operados  = _ya_operados_hoy()
    # Mercados con orden maker viva (piloto): también se saltan la ruta
    # taker — el libro fluctúa y un ciclo posterior podría pasar el veto de
    # profundidad y ejecutar taker con la maker aún abierta → doble posición.
    # FAIL-CLOSED (code-review 10-Jul): estado ilegible (None) = no sabemos
    # QUÉ mercados tienen órdenes vivas → no se abre NINGÚN trade nuevo este
    # ciclo. Las GTD ya colocadas expiran solas en el exchange; los fills
    # previos ya están en trades.csv. Antes esto degradaba a set() vacío y
    # el guard anti-doble-posición quedaba fail-OPEN con el fichero corrupto.
    _estado_maker = _maker_estado_cargar()
    if _estado_maker is None:
        log("  ⛔ maker_orders.json ILEGIBLE — fail-closed: sin trades nuevos "
            "este ciclo (arreglar/borrar el fichero para reanudar)")
        return
    mids_maker   = _maker_mids_activos(_estado_maker)
    bkr          = bankroll_actual()

    log(f"  Predicciones hoy: {len(predicciones)} | Bankroll: {bkr:.2f}€ | Mercados ya operados (histórico): {len(ya_operados)}")

    ejecutados = 0
    for pred in predicciones:
        strategy = pred.get("strategy", "")
        subtype  = pred.get("subtype", "")
        mid      = pred.get("market_id", "")
        dec      = pred.get("decision", "")

        # Filtros de elegibilidad — tupla exacta aprobada para live
        if f"{strategy}#{subtype}#{dec}" not in pares_ok:
            continue
        # Veto activa=False (code-review 11-Jul): antes de hoy ninguna tupla
        # whitelisted pertenecía a ACUMULAR_SHADOW_AUNQUE_DESACTIVADA
        # (shadow_predict.py) — estrategias que siguen generando predicciones
        # aunque strategy_params.json las marque desactivadas, precisamente
        # para seguir midiendo. Este código nunca miraba 'activa', solo
        # IC/n — con GBM_LATE_15M_ESPACIO_ATR entrando hoy en whitelist (SÍ
        # está en ese set), una desactivación manual futura (no solo por IC
        # bajo, que ya bloquearía por el gate de abajo) seguiría operando
        # dinero real en silencio. Fail-closed: cualquier nivel de la
        # jerarquía marcado activa=False bloquea, igual que hace
        # shadow_predict.py para generar.
        if not _tupla_activa(strategy, subtype, params, dec):
            log(f"  ⛔ {strategy}#{subtype} {dec}: estrategia desactivada (activa=False) "
                f"pese a estar en whitelist — no se ejecuta")
            continue
        if mid in ya_operados:
            continue
        if mid in mids_maker:
            continue  # orden maker viva en este mercado (ver nota arriba)

        # Mercado ya cerrado → no operar (evita "invalid order version" de la API).
        # Fail-closed: end_date vacío o sin parsear NO debe dejar pasar el
        # trade sin validar — código de seguridad live, no se minimiza (ver
        # CLAUDE.md). No observado en producción (0/117 predicciones de hoy
        # con end_date vacío) pero es el comportamiento correcto si pasa.
        end_str = pred.get("end_date", "")
        try:
            if not end_str:
                continue
            end_dt = datetime.fromisoformat(end_str.replace("Z", "+00:00"))
            if end_dt.tzinfo is None:
                end_dt = end_dt.replace(tzinfo=timezone.utc)
            if end_dt <= datetime.now(timezone.utc):
                continue
        except Exception:
            continue

        # Señal caducada (2026-07-10, ver SENAL_MAX_LATENCIA_SEG arriba):
        # prob_yes_modelo/edge se calculan UNA vez en shadow_predict; si han
        # pasado >=100s sin ejecutar (reintentos bloqueados por veto_profundidad
        # mientras el libro fluctúa), el edge ya no es fiable — no operar.
        # Fail-closed: timestamp_utc vacío o sin parsear = tratar como caducada.
        latencia_seg = _latencia_seg(pred)
        if latencia_seg is None or latencia_seg >= SENAL_MAX_LATENCIA_SEG:
            log(f"  ⛔ Señal caducada: {strategy}#{subtype} {dec} mid={mid} "
                f"latencia={latencia_seg if latencia_seg is not None else '?'}s "
                f"(máx {SENAL_MAX_LATENCIA_SEG}s) — no se ejecuta")
            try:
                precio_yes_caduca = float(pred.get("precio_yes_mercado", 0.5))
            except (TypeError, ValueError):
                precio_yes_caduca = 0.5
            _snapshot_senal_bloqueada(mid, dec, precio_yes_caduca,
                                      riesgo.get("min_stake_eur", 1.05),
                                      {"strategy": strategy, "subtype": subtype},
                                      motivo="senal_caducada")
            continue

        # IC mínimo confirmado en histórico (n_hist siempre corresponde a la
        # muestra real detrás de ic_hist, direccional o agregada), umbral global.
        # Barra asimétrica: strategy#decision con evidencia estructural de que
        # esa dirección rinde peor (ver H-CUSTOM-GBM-BUYYES-GLOBAL-MALO,
        # confirmada 2026-07-01, n=507 IC=-0.076) exige un min_ic más alto que
        # el global, en vez del mismo umbral para las dos direcciones.
        min_ic_efectivo = min_ic_asimetrico.get(f"{strategy}#{dec}", min_ic)
        try:
            feats_pred = json.loads(pred.get("features", "{}") or "{}")
        except Exception:
            feats_pred = {}
        ic_hist, n_hist = _ic_n_para_subtype(strategy, subtype, params, decision=dec,
                                              min_n=min_n, min_ic=min_ic_efectivo, features=feats_pred)
        pasa = not (ic_hist < min_ic_efectivo or n_hist < min_n)

        # Override puntual por strategy#subtype#decision (config_live.json):
        # solo mira el n/ic direccional de ESA clave exacta, nunca una clave
        # más amplia de la jerarquía de fallback — antes el min_n rebajado se
        # colaba dentro de _ic_n_para_subtype y podía validar la señal contra
        # el ic_bayes/n agregado de toda la estrategia (una muestra mucho más
        # amplia y potencialmente más débil que la que motivó el override).
        override_key = f"{strategy}#{subtype}#{dec}"
        if not pasa and override_key in min_n_overrides:
            min_n_override = min_n_overrides[override_key]
            exact_key = f"{strategy}#{subtype}" if subtype else strategy
            p_exact = params.get(exact_key, {})
            campo_ic = f"ic_{dec}"
            campo_n  = f"n_{dec}"
            ic_exacto = p_exact.get(campo_ic)
            n_exacto  = p_exact.get(campo_n, 0)
            if ic_exacto is not None and n_exacto >= min_n_override and float(ic_exacto) >= min_ic_efectivo:
                ic_hist, n_hist = float(ic_exacto), n_exacto
                pasa = True
                if n_hist >= min_n:
                    _avisar_override_superado(override_key, n_hist, min_n)
        if not pasa:
            continue

        # Veto CLV (2026-07-03): tupla con CLV medio < 0 sostenido pierde
        # contra la línea de cierre sistemáticamente — el IC/PnL tarda más
        # en reflejarlo (binario, n~40) que el CLV (continuo, n~20). Guardia
        # adicional sobre el IC, no sustituto; sin datos CLV no veta.
        clv_medio, n_clv = _clv_tupla(strategy, subtype, dec)
        if n_clv >= CLV_VETO_MIN_N and clv_medio < 0:
            log(f"  ⛔ Veto CLV: {strategy}#{subtype}#{dec} clv_medio={clv_medio:+.4f}"
                f" (n={n_clv}, ventana {CLV_VETO_DIAS}d) < 0 — no se ejecuta")
            continue

        # IC del modelo para esta señal concreta
        try:
            prob_y = float(pred.get("prob_yes_modelo", 0.5))
            precio = float(pred.get("precio_yes_mercado", 0.5))
            edge   = float(pred.get("edge_neto", 0))
        except ValueError:
            continue

        # Veto fee real taker (propuesta #5, 11-Jul, aprobado Javi — alcance
        # SOLO live, no toca shadow_predict.py/EDGE_MINIMO global para no
        # invalidar el IC histórico de las ~170 estrategias shadow). edge_neto
        # neta slippage pero nunca el fee de Polymarket; en p~0.5 el fee real
        # (~1.7¢) se comía casi todo el EDGE_MINIMO=0.02, dejando ~break-even.
        # edge_dir = edge_neto con el signo resuelto hacia nuestra dirección
        # (shadow_predict: en>=min → BUY_YES, -en>=min → BUY_NO); se calcula
        # aquí una sola vez y se reutiliza más abajo para _decidir_requote.
        edge_dir = edge if dec == "BUY_YES" else -edge
        fee_est = FEE_RATE_TAKER_CRYPTO * precio * (1 - precio)
        edge_tras_fee = edge_dir - fee_est
        if edge_tras_fee <= 0:
            log(f"  ⛔ Veto fee: {strategy}#{subtype} {dec} edge_neto={edge_dir:+.4f} "
                f"fee_est={fee_est:.4f} → tras fee={edge_tras_fee:+.4f} <= 0, no se ejecuta")
            continue

        # Veto discrepancia entre tuplas whitelisted (propuesta #8, ver nota
        # junto a _wl_por_mercado más arriba): otra tupla whitelisted DE OTRA
        # ESTRATEGIA/SUBTYPE predice HOY la dirección OPUESTA sobre este mismo
        # market_id → esta señal ya no es la de 62.7-67.8% que su propio IC
        # dice, es la mitad de un conflicto que en shadow acierta 50.0%
        # (n=30). Fail-closed: no ejecuta NINGUNA de las dos (la conflictiva
        # se procesará después en este mismo bucle y verá el mismo mapa,
        # también se saltará — ningún orden de iteración deja pasar una).
        # n=30 está en el límite del umbral n≥15 del proyecto, no n≥40: veto
        # conservador mientras se acumula más dato, no una desactivación
        # permanente. Excluye conflictos de la MISMA strategy#subtype
        # (code-review 11-Jul): shadow_predict recalcula `dec` cada ciclo
        # desde el precio actual sin histéresis, así que una tupla puede
        # cambiar de dirección entre ciclos dentro de la vida del mismo
        # mercado — sin este filtro esa fila vieja (aunque ya filtrada por
        # latencia arriba, podría seguir dentro de los 100s) se auto-vetaría.
        own_prefix = f"{strategy}#{subtype}#"
        decs_en_mercado = _wl_por_mercado.get(mid, {})
        conflictos = sorted(k for d, ks in decs_en_mercado.items() if d != dec
                             for k in ks if not k.startswith(own_prefix))
        if conflictos:
            log(f"  ⛔ Veto discrepancia: {strategy}#{subtype} {dec} mid={mid} — "
                f"otra tupla whitelist predice dirección opuesta en el mismo "
                f"mercado ({conflictos}) — no se ejecuta ninguna")
            _snapshot_senal_bloqueada(mid, dec, precio,
                                      riesgo.get("min_stake_eur", 1.05),
                                      {"strategy": strategy, "subtype": subtype},
                                      motivo="veto_discrepancia_tuplas")
            continue

        # Boost por coincidencia: otra tupla whitelisted distinta predice HOY
        # la MISMA dirección sobre este mismo market_id → en shadow ese
        # subconjunto acierta 67.8% (n=239) vs 62.7% (n=833) en solitario.
        # Solo afecta el TAMAÑO (ic_para_stake, entra en calcular_stake), no
        # la elegibilidad — ic_hist crudo ya pasó su propio gate arriba sin
        # ayuda de este boost. Reutiliza todos los techos existentes de
        # calcular_stake (Kelly, 10% bankroll, max_stake_eur, freno diario),
        # no introduce un techo nuevo. boost=1.0 por defecto (sin efecto si
        # no está en config). Impacto hoy GARANTIZADO 0€, no solo probable:
        # max_stake_eur está pineado exactamente igual que min_stake_eur
        # (ambos 1.05€, re-pineado 07-Jul) → calcular_stake devuelve 1.05€
        # siempre, sea cual sea el IC de entrada. El boost queda correctamente
        # cableado y se activa solo el día que max_stake_eur se despinee
        # (mismo patrón ya documentado para P15 en CLAUDE.md).
        coincide = bool(decs_en_mercado.get(dec, set()) - {override_key})
        ic_para_stake = ic_hist
        if coincide and boost_ic_coincidencia != 1.0:
            ic_para_stake = ic_hist * boost_ic_coincidencia
            log(f"  ✚ Coincidencia: {strategy}#{subtype} {dec} mid={mid} — otra tupla "
                f"whitelist coincide en dirección, ic_para_stake {ic_hist:+.3f}→"
                f"{ic_para_stake:+.3f} (boost×{boost_ic_coincidencia:.2f})")

        # Boost condicionado a smart money para FAVORITO_CONFIRMADO#SOL (ver
        # H-CUSTOM-SMARTMONEY-FAVORITO-SOL arriba). Mismo patrón que el boost
        # de coincidencia: solo afecta ic_para_stake (tamaño, entra en
        # calcular_stake), nunca la elegibilidad — ic_hist crudo ya pasó su
        # propio gate arriba sin ayuda de este boost. Implementado 14-Jul
        # pero DEJADO INACTIVO (boost=1.0 en config) a petición explícita de
        # Javi: activar más adelante junto al despineo de max_stake_eur —
        # hasta entonces impacto en euros GARANTIZADO 0 (boost=1.0 es no-op
        # explícito, ni siquiera depende del pineo actual de min/max_stake_eur
        # como el de coincidencia). La hipótesis sigue acumulando n en shadow
        # vía hypothesis_tracker.py sin depender de este cableado.
        smartmoney_boost_aplicado = False
        if strategy == "FAVORITO_CONFIRMADO" and subtype.startswith("SOL") and boost_ic_smartmoney_sol != 1.0:
            sm_consenso  = feats_pred.get("smart_money_consensus")
            sm_n_wallets = feats_pred.get("smart_money_n_wallets") or 0
            if (sm_consenso is not None and sm_n_wallets >= SMARTMONEY_SOL_N_WALLETS_MIN
                    and abs(sm_consenso) > SMARTMONEY_SOL_CONSENSO_MIN):
                alineado_sm = (dec == "BUY_YES" and sm_consenso > SMARTMONEY_SOL_CONSENSO_MIN) or \
                              (dec == "BUY_NO" and sm_consenso < -SMARTMONEY_SOL_CONSENSO_MIN)
                if alineado_sm:
                    ic_prev = ic_para_stake
                    ic_para_stake = ic_para_stake * boost_ic_smartmoney_sol
                    smartmoney_boost_aplicado = True
                    log(f"  ✚ Smart money alineado: {strategy}#{subtype} {dec} mid={mid} — "
                        f"consenso={sm_consenso:+.3f} (n_wallets={sm_n_wallets}), "
                        f"ic_para_stake {ic_prev:+.3f}→{ic_para_stake:+.3f} "
                        f"(boost×{boost_ic_smartmoney_sol:.2f})")

        # Techo al boost COMBINADO (code-review 14-Jul, sesión siguiente):
        # coincidencia y smartmoney son independientes y se aplican en
        # cascada sobre la misma ic_para_stake — si algún día ambas están
        # activas a la vez sobre la misma señal (posible: una tupla
        # FAVORITO_CONFIRMADO#SOL que además coincide en dirección con otra
        # tupla whitelist), se compondrían multiplicativamente sin que
        # ninguna de las dos validaciones (n=239/833 la de coincidencia,
        # n=95/98 z≈2.13 la de smartmoney) midiera esa combinación. Mismo
        # patrón de "techo sobre un boost compuesto" que KELLY_COMPUESTO_MAX
        # en shadow_predict.py (ahí para rachas, aquí para boosts
        # independientes). Con las dos activas a 1.15/1.2 el producto sería
        # ×1.38 — el techo se fija en el orden del boost más agresivo
        # previsto (KELLY_COMPUESTO_MAX=2.00 es para otro mecanismo, no
        # reutilizable aquí sin mezclar fenómenos distintos).
        ic_para_stake = min(ic_para_stake, ic_hist * BOOST_IC_COMBINADO_MAX)

        # Stake (con penalización de inventario direccional)
        # Techo de correlación direccional: los pares cripto se mueven casi
        # al unísono — más de N posiciones abiertas en la misma dirección es
        # una sola apuesta con stake multiplicado (ver
        # _posiciones_abiertas_misma_direccion).
        max_misma_dir = riesgo.get("max_posiciones_abiertas_misma_direccion", 2)
        abiertas_dir = _posiciones_abiertas_misma_direccion(dec)
        if abiertas_dir >= max_misma_dir:
            log(f"  SKIP {strategy}#{subtype} {dec}: ya hay {abiertas_dir} "
                f"posiciones abiertas {dec} (techo correlación = {max_misma_dir})")
            continue

        # Filtro de calidad en 2ª señal concurrente (propuesta #7, 10-Jul,
        # aprobado Javi 11-Jul): con 1+ posición ya abierta en la misma
        # dirección, el riesgo de correlación (los pares cripto se mueven casi
        # al unísono) exige más convicción, no solo hueco bajo el techo. Exige
        # IC un factor más alto que el mínimo vigente para esa tupla (mismo
        # min_ic_efectivo ya usado más arriba, respeta la barra asimétrica).
        if abiertas_dir >= 1:
            # Fail-closed: si min_ic_efectivo no es positivo (dato/config
            # corrupta), el factor multiplicativo invertiría la barra en vez
            # de subirla — se cae al mínimo global positivo en ese caso.
            base_ic_concurrente = min_ic_efectivo if min_ic_efectivo > 0 else min_ic
            ic_min_concurrente = base_ic_concurrente * (1 + factor_ic_concurrente)
            if ic_hist < ic_min_concurrente:
                log(f"  SKIP {strategy}#{subtype} {dec}: ya hay {abiertas_dir} "
                    f"posición(es) {dec} abierta(s) — exige IC≥{ic_min_concurrente:.3f} "
                    f"({(1+factor_ic_concurrente):.0%} del mínimo, tiene {ic_hist:+.3f})")
                continue

        # Cooldown streak (H-STREAK-COOLDOWN, ver live_stake.py::cooldown_factor_streak):
        # 2 derrotas reales seguidas en esta misma strategy#subtype reducen
        # ic_para_stake temporalmente. Mismo patrón que los boosts de arriba
        # (afecta solo tamaño, nunca elegibilidad — ic_hist crudo ya pasó su
        # gate). factor=1.0 por defecto (riesgo.circuit_breaker.streak_cooldown_factor_ic
        # ausente/1.0) = no-op explícito, igual que boost_ic_smartmoney_favorito_sol.
        # config= reutiliza el ya cargado arriba en vez de releer config_live.json
        # del disco en cada señal candidata del ciclo.
        cooldown_factor, cooldown_motivo = cooldown_factor_streak(strategy, subtype, config)
        cooldown_activo = cooldown_factor != 1.0
        if cooldown_activo:
            ic_para_stake = ic_para_stake * cooldown_factor
            log(f"  ⏸ {cooldown_motivo} — ic_para_stake→{ic_para_stake:+.3f}")

        stake_info = calcular_stake(ic_para_stake, strategy, subtype, direction=dec)
        if not stake_info["viable"]:
            log(f"  SKIP {strategy}#{subtype}: stake no viable — {stake_info['motivo']}")
            _snapshot_senal_bloqueada(mid, dec, precio,
                                      riesgo.get("min_stake_eur", 1.05),
                                      {"strategy": strategy, "subtype": subtype})
            continue

        stake    = stake_info["stake_eur"]
        entry_p  = precio

        log(f"  SEÑAL → {strategy}#{subtype} {dec} "
            f"precio={entry_p:.4f} IC_hist={ic_hist:+.3f} n={n_hist} "
            f"stake={stake:.2f}€")
        log(f"         {stake_info['motivo']}")

        # Evaluador pre-trade independiente (generator/evaluator split)
        eval_ok, eval_motivo = _evaluar_pre_trade(pred, dec)
        log(f"  Evaluador: {eval_motivo}")
        if not eval_ok:
            # Solo log, no Telegram: la señal rechazada no se registra, así
            # que se re-evalúa (y se re-rechazaría) cada ciclo ~20s mientras
            # la predicción siga viva — un Telegram aquí es un mensaje por
            # ciclo. Misma clase de spam que la notificación pre-ejecución
            # eliminada 2026-07-03.
            log(f"  ⛔ EVALUADOR RECHAZA — no se ejecuta")
            continue

        # 3+4. Ejecutar y notificar DESPUÉS con el resultado real.
        # Antes el Telegram "señal detectada" salía antes de ejecutar: una
        # señal con no_fill (FOK kill, o edge evaporado en re-quote) no se
        # registra y se reintenta cada ciclo (~20s) mientras la predicción
        # siga viva → un mensaje por ciclo (ocurrió 2026-07-02 19:25, 3
        # mensajes en 90s; el re-quote lo habría amplificado). Los reintentos
        # silenciosos quedan en live.log; Telegram solo recibe fills y
        # errores reales, una vez, porque ambos se registran en trades.csv y
        # el mercado entra en ya_operados.
        resultado = _ejecutar_orden_polymarket(mid, dec, stake, entry_p,
                                               edge_dir=edge_dir,
                                               contexto={"strategy": strategy,
                                                         "subtype": subtype})

        # FOK kill o edge evaporado en re-quote = no registrar ni contar;
        # la señal puede reintentarse en ciclos siguientes si sigue viva.
        if resultado.get("no_fill"):
            # Piloto maker-sobre-vetadas: SOLO si el motivo fue exactamente
            # veto_profundidad (libro_vacio) — la señal ya pasó todos los
            # gates y el subconjunto vetado acierta 97% (analisis_fills).
            if resultado.get("libro_vacio"):
                if _colocar_orden_maker(pred, dec,
                                        {"strategy": strategy,
                                         "subtype": subtype,
                                         "ic_hist": round(ic_hist, 4)}):
                    mids_maker.add(mid)
            continue

        # 5. Registrar
        ts_now = datetime.now(timezone.utc).isoformat(timespec="seconds")
        trade = {
            "timestamp_utc":   ts_now,
            "market_id":       mid,
            "question":        pred.get("question", ""),
            "end_date":        pred.get("end_date", ""),
            "strategy":        strategy,
            "subtype":         subtype,
            "direction":       dec,
            "stake_eur":       stake if resultado["ok"] else 0.0,
            "entry_price":     resultado["entry_price"],
            "ic_modelo":       round(prob_y, 4),
            "edge_neto":       round(edge, 4),
            "conviction_score": round(ic_hist, 4),
            "kelly_recomendado": stake,
            "status":          "OPEN" if resultado["ok"] else "ERROR",
            "close_timestamp": "",
            "exit_price":      "",
            "outcome_real":    "",
            "fee_eur":         resultado.get("fee_eur", 0),
            "pnl_bruto_eur":   "",
            "pnl_neto_eur":    "",
            "notas":           ((f"slip_real={resultado['slip_real']:+.4f}"
                                + (f" slip_est_kyle={resultado['slip_estimado_kyle']:.4f}"
                                   if resultado.get("slip_estimado_kyle") is not None else "")
                                if resultado.get("ok") and "slip_real" in resultado
                                else resultado.get("error", ""))
                                + (f" coincide_tupla=1 ic_boost={ic_para_stake:+.3f}" if coincide else "")
                                + (f" smartmoney_boost=1 ic_boost={ic_para_stake:+.3f}" if smartmoney_boost_aplicado else "")
                                + (f" streak_cooldown=1 ic_cooldown={ic_para_stake:+.3f}" if cooldown_activo else "")),
        }
        _registrar_trade(trade)
        ya_operados.add(mid)
        ejecutados += 1

        if resultado["ok"]:
            enviar_telegram(
                f"🎯 *Orden live ejecutada*\n"
                f"Estrategia: {strategy}#{subtype}\n"
                f"Dirección: {dec}\n"
                f"Precio fill: {resultado['entry_price']:.4f} "
                f"(slip {resultado.get('slip_real', 0):+.4f})\n"
                f"Stake: {stake:.2f}$  |  IC: {ic_hist:+.3f}\n"
                f"Bankroll operativo: {bankroll_actual():.2f}$ (real al cierre de ciclo)"
            )
        else:
            enviar_telegram(
                f"❌ *Orden live ERROR*\n"
                f"{strategy}#{subtype} {dec}\n"
                f"{resultado.get('error', '')[:200]}"
            )

        # No más de 3 operaciones por ciclo (espacio entre señales)
        if ejecutados >= 3:
            log(f"  Límite de 3 operaciones por ciclo alcanzado.")
            break

    log(f"  Operaciones ejecutadas este ciclo: {ejecutados}")

    # Resumen de ventana si hubo actividad
    if ejecutados > 0:
        bkr_final = bankroll_actual()
        pnl_d     = pnl_live_hoy()
        # Refresca el balance REAL on-chain tras abrir posiciones → el dashboard
        # y este mensaje reflejan el wallet al instante (no esperan al cron 15min).
        snap = actualizar_balance_real()
        if snap:
            linea_real = (f"Balance real: {snap['total']:.2f}$ "
                          f"(PnL real {snap['pnl_real']:+.2f} · operativo {bkr_final:.2f}$)")
        else:
            linea_real = f"Bankroll operativo: {bkr_final:.2f}$ (balance real n/d)"
        enviar_telegram(
            f"📊 *Ciclo live completado*\n"
            f"Operaciones este ciclo: {ejecutados}\n"
            f"PNL hoy (operativo): {pnl_d:+.2f}$\n"
            f"{linea_real}"
        )

    log(f"=== Fin live_trade ===")


if __name__ == "__main__":
    main()
