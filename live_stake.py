"""
live_stake.py — Calculadora de stake y circuit breakers de riesgo.

Diseño real (verificado 2026-07-01 — el docstring anterior describía un
mecanismo de "presupuesto por ventana" que nunca se implementó así):

  calcular_stake(ic): techos en cascada por trade, no por ventana:
    1. Kelly half: IC × bankroll × 0.5
    2. Máx 10% del bankroll por trade
    3. Máximo absoluto del config (2€)
    4. Penalización de inventario direccional (Avellaneda-Stoikov, ver
       inventario_direccional_hoy/_inventory_penalty)

  verificar_circuit_breaker(): 3 frenos basados en PNL realizado, no en
  capital desplegado:
    1. Bankroll mínimo absoluto → apaga el switch
    2. Freno diario: caída ≥15% del bankroll desde el inicio del día
       (Madrid) → para el día
    3. Freno por ventana: caída ≥20% del bankroll desde el inicio de la
       ventana actual → para la ventana

  stakes_desplegados_ventana_actual() se calcula y se loguea (CLI de
  diagnóstico, motivo del freno 3) pero NO actúa como techo duro de
  exposición simultánea — el límite de trades concurrentes en una ventana
  viene solo de "máx 3 trades/ciclo" en live_trade.py + dedup por
  market_id, no de un presupuesto por ventana.
"""

import csv
import json
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

DIR_LIVE              = Path("data/live")
CONFIG_PATH           = DIR_LIVE / "config_live.json"
TRADES_CSV            = DIR_LIVE / "trades.csv"
SWITCH_PATH           = DIR_LIVE / "LIVE_MODE_ON"
LATCH_VENTANA_PATH    = DIR_LIVE / "freno_ventana_latch.json"

CAPITAL_OPERATIVO_INICIAL = 25.44  # depósito real 2026-06-29


def _cargar_config() -> dict:
    if not CONFIG_PATH.exists():
        return {}
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


def _ahora_madrid(config: dict) -> datetime:
    offset = config.get("utc_offset_verano", 2)
    return datetime.now(timezone.utc) + timedelta(hours=offset)


# ── Bankroll ──────────────────────────────────────────────────────────────────

_BALANCE_REAL_MAX_EDAD_S = 1800  # 30min: cron live_balance cada 15min + refresco por-trade
_memo_balance_real: dict = {"snap": "unset", "ts_monotonic": 0.0}
_MEMO_TTL_S = 5.0  # memoiza dentro de un mismo ciclo del fast loop (~20s, ~3s de trabajo real)


def _balance_real_fresco() -> dict | None:
    """Snapshot de balance real on-chain si está cacheado, fresco y con
    pnl_hoy_real válido; si no, None (fail-closed → el llamante cae al ledger).

    Memoizado ~5s en memoria de proceso (code-review 13-Jul): calcular_stake()
    y verificar_circuit_breaker() llaman a bankroll_actual()/pnl_live_hoy()
    varias veces cada uno dentro de la misma fórmula (bkr_ini_dia, margen_freno,
    etc.) — sin memoizar, cada llamada relee data/live/balance_real.json por
    separado, y si el cron/refresco por-trade lo reescribe justo entre dos de
    esas lecturas dentro del mismo ciclo, dos términos de la MISMA fórmula
    podrían leer real vs ledger de forma inconsistente. Cada invocación del
    fast loop arranca el proceso desde cero (ver run_fast.sh), así que el TTL
    corto no esconde datos rancios entre ciclos, solo estabiliza uno.

    Import perezoso (evita import circular: live_balance.py hace
    `from live_stake import CAPITAL_OPERATIVO_INICIAL` a nivel de módulo).
    Se exige pnl_hoy_real no-None además de `total`: fetch_balance_real()
    calcula pnl_hoy_real best-effort desde /activity y puede venir None en
    un snapshot por lo demás fresco (fallo puntual de esa sub-consulta) —
    usar `total` real con un pnl_hoy de ledger mezclaría dos fuentes con
    fronteras de día distintas (real=UTC, ledger=Madrid) e inconsistentes
    entre sí dentro de la misma fórmula de freno.

    Además del chequeo de edad (max_edad_s), se exige que `ts` sea del
    mismo día UTC que "ahora" (code-review 13-Jul): pnl_hoy_real se calcula
    UNA vez por fetch y queda fijo en el JSON — un snapshot de las 23:55
    UTC (pnl de AYER-UTC) sigue "fresco" por edad a las 00:05 UTC del día
    siguiente sin haber rotado, y la ventana live `prueba_23h_utc`
    (01:00-02:00 Madrid = 23:00-00:00 UTC) cruza justo ese límite. Sin este
    chequeo, bankroll_inicio_dia() quedaría corrupto ~30min tras cada
    medianoche UTC con el pnl_hoy_real del día equivocado.
    """
    ahora_mono = time.monotonic()
    if ahora_mono - _memo_balance_real["ts_monotonic"] < _MEMO_TTL_S:
        cached = _memo_balance_real["snap"]
        if cached != "unset":
            return cached

    def _memoizar(resultado):
        _memo_balance_real["snap"] = resultado
        _memo_balance_real["ts_monotonic"] = ahora_mono
        return resultado

    try:
        from live_balance import cargar_balance_real
    except Exception:
        return _memoizar(None)
    snap = cargar_balance_real(max_edad_s=_BALANCE_REAL_MAX_EDAD_S)
    if not snap or snap.get("_rancio"):
        return _memoizar(None)
    if snap.get("total") is None or snap.get("pnl_hoy_real") is None:
        return _memoizar(None)
    try:
        ts_snap = datetime.fromisoformat(snap["ts"])
        if ts_snap.date() != datetime.now(timezone.utc).date():
            return _memoizar(None)
    except Exception:
        return _memoizar(None)
    return _memoizar(snap)


def bankroll_actual() -> float:
    """Capital total: balance real on-chain (ver live_balance.py) si el
    cache está fresco, si no PNL de plan (inicial + trades cerrados).

    Decisión 13-Jul (aprobado Javi): el freno diario y el Kelly estaban
    anclados al PnL de *plan* (precio de entrada previsto), que diverge del
    real liquidado — 13-Jul: ledger -16.77€ vs real -14.32€, ~2.45€ de
    drift (mismo "tracking error" ya documentado el 07-Jul,
    project_reconciliacion_dashboard.md). El bloqueo del freno diario se
    calculaba sobre el número más pesimista, más restrictivo que la caja
    real. Fallback a ledger si el cache real falta/está rancio: por el
    signo de ese drift históricamente observado (ledger más pesimista que
    real), caer al ledger nunca infla el apetito de riesgo respecto al
    real — sigue siendo fail-closed.
    """
    real = _balance_real_fresco()
    if real is not None:
        return real["total"]
    return _bankroll_ledger()


def _bankroll_ledger() -> float:
    """Capital de plan puro: inicial + PNL de todos los trades cerrados.

    Separado de bankroll_actual() (13-Jul) para el freno de ventana: no hay
    PnL real con granularidad de ventana (solo diaria, en balance_real.json
    daily_real), así que bkr_ini_v = bkr - pnl_v en verificar_circuit_breaker
    necesita SIEMPRE la misma fuente en los dos términos — mezclar un bkr
    real (diario) con un pnl_v de ledger (intradía) daría una base de
    ventana incoherente. El freno diario sí puede usar real en ambos
    términos (bankroll_actual + pnl_live_hoy, ambos con fallback
    coordinado); el de ventana no tiene esa opción y se queda en ledger.
    """
    if not TRADES_CSV.exists():
        return CAPITAL_OPERATIVO_INICIAL
    pnl = 0.0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") == "CLOSED":
                try:
                    pnl += float(row.get("pnl_neto_eur", 0) or 0)
                except ValueError:
                    pass
    return CAPITAL_OPERATIVO_INICIAL + pnl


# ── Ventanas ──────────────────────────────────────────────────────────────────

def _ventanas_hoy(config: dict) -> list:
    ahora = _ahora_madrid(config)
    dia   = ahora.weekday()  # 0=lunes…6=domingo
    if dia < 5:
        return config.get("ventanas_lunes_viernes", [])
    modo_fds = config.get("fines_de_semana", "off")
    if modo_fds == "ventanas":
        return config.get("ventanas_fin_de_semana", [])
    return []


def _ventana_actual(config: dict) -> dict | None:
    """Devuelve la ventana en la que estamos ahora, o None."""
    ahora = _ahora_madrid(config).time()
    for v in _ventanas_hoy(config):
        try:
            h_ini = datetime.strptime(v["inicio"], "%H:%M").time()
            h_fin = datetime.strptime(v["fin"],    "%H:%M").time()
            if h_ini <= ahora <= h_fin:
                return v
        except Exception:
            continue
    return None


def ventanas_restantes_hoy(config: dict) -> int:
    """Número de ventanas que quedan hoy (incluida la actual si estamos en una)."""
    ahora = _ahora_madrid(config).time()
    restantes = 0
    for v in _ventanas_hoy(config):
        try:
            h_fin = datetime.strptime(v["fin"], "%H:%M").time()
            if h_fin >= ahora:
                restantes += 1
        except Exception:
            continue
    return max(restantes, 1)  # nunca 0 para evitar división por cero


# ── Stakes por ventana ────────────────────────────────────────────────────────

def _ts_inicio_ventana_utc(v: dict, config: dict) -> datetime:
    """Timestamp UTC del inicio de la ventana de hoy."""
    offset  = config.get("utc_offset_verano", 2)
    ahora_m = _ahora_madrid(config)
    h_ini   = datetime.strptime(v["inicio"], "%H:%M").time()
    inicio_madrid = ahora_m.replace(hour=h_ini.hour, minute=h_ini.minute,
                                    second=0, microsecond=0)
    return inicio_madrid - timedelta(hours=offset)


def _ts_inicio_dia_utc(config: dict) -> datetime:
    """Timestamp UTC de las 00:00 de hoy en Madrid (para filtrar 'trades de hoy')."""
    offset  = config.get("utc_offset_verano", 2)
    ahora_m = _ahora_madrid(config)
    inicio_madrid = ahora_m.replace(hour=0, minute=0, second=0, microsecond=0)
    return inicio_madrid - timedelta(hours=offset)


def _parse_ts(ts_str: str) -> datetime | None:
    if not ts_str:
        return None
    try:
        ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
        return ts
    except Exception:
        return None


def stakes_desplegados_ventana_actual() -> float:
    """
    Suma de stakes colocados en la ventana horaria actual (trades OPEN o STUB).
    Este es el 'capital en juego' de la ventana — el freno se basa en esto.
    """
    if not TRADES_CSV.exists():
        return 0.0
    config = _cargar_config()
    v      = _ventana_actual(config)
    if v is None:
        return 0.0

    ts_ini = _ts_inicio_ventana_utc(v, config)
    total  = 0.0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") not in ("OPEN", "STUB"):
                continue
            ts = _parse_ts(row.get("timestamp_utc") or "")
            if ts is not None and ts >= ts_ini:
                try:
                    total += float(row.get("stake_eur", 0) or 0)
                except ValueError:
                    pass
    return total


def pnl_live_hoy() -> float:
    """
    PNL neto real de hoy (día UTC, ver live_balance.py) si el balance real
    está fresco — para mantener consistencia con bankroll_actual() dentro de
    la misma fórmula de freno (mezclar bkr real con pnl de ledger, o
    viceversa, sería incoherente). Si no, PNL de plan de trades cerrados hoy
    (día Madrid): compara datetimes reales contra las 00:00 Madrid de hoy en
    UTC, no substrings de fecha — comparar fecha UTC de close_timestamp
    contra "hoy" en Madrid excluía para siempre los trades que cierran entre
    22:00-23:59 UTC (00:00-01:59 Madrid del día siguiente, dentro de la
    ventana de prueba 01:00-02:00 Madrid), corrompiendo el freno diario.

    Nota (13-Jul): en modo real el "día" es UTC, no Madrid — pequeña
    diferencia de frontera en horas tempranas de Madrid (00:00-02:00), igual
    que la ya documentada arriba pero en sentido inverso. Aceptado: preferir
    coherencia bkr↔pnl dentro del cálculo del freno sobre coincidencia exacta
    de frontera de día, que además solo importa en una franja horaria corta.
    """
    real = _balance_real_fresco()
    if real is not None:
        return real["pnl_hoy_real"]
    if not TRADES_CSV.exists():
        return 0.0
    config    = _cargar_config()
    ts_ini    = _ts_inicio_dia_utc(config)
    pnl       = 0.0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "CLOSED":
                continue
            ts = _parse_ts(row.get("close_timestamp") or row.get("timestamp_utc") or "")
            if ts is not None and ts >= ts_ini:
                try:
                    pnl += float(row.get("pnl_neto_eur", 0) or 0)
                except ValueError:
                    pass
    return pnl


def stakes_abiertos_total() -> float:
    """
    Suma de stakes de TODAS las posiciones abiertas (OPEN o STUB), sin filtro
    de fecha: cualquier stake abierto puede perderse hoy, así que cuenta como
    riesgo vivo del día. bankroll_actual() solo resta PnL de trades CLOSED,
    por lo que este dinero no está reflejado ahí. Código de seguridad live.
    """
    if not TRADES_CSV.exists():
        return 0.0
    total = 0.0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") not in ("OPEN", "STUB"):
                continue
            try:
                total += float(row.get("stake_eur", 0) or 0)
            except ValueError:
                pass
    return total


def racha_perdidas_consecutivas() -> int:
    """
    Nº de pérdidas CLOSED consecutivas al final de la secuencia de hoy (día
    Madrid), ordenadas por close_timestamp. Una racha así es la firma de un
    modo de fallo sistemático (modelo desfasado, régimen hostil), no de
    varianza — 2026-07-03: 4 pérdidas en 5 minutos (-6.54€) y los frenos en €
    no la cortaron a tiempo. Si circuit_breaker.racha_vigente_desde existe,
    solo cuentan cierres posteriores (para no re-castigar una racha anterior
    a una reapertura manual del usuario). Código de seguridad live.
    """
    if not TRADES_CSV.exists():
        return 0
    config = _cargar_config()
    ts_ini = _ts_inicio_dia_utc(config)
    desde  = _parse_ts(config.get("riesgo", {}).get("circuit_breaker", {})
                       .get("racha_vigente_desde") or "")
    if desde is not None and desde > ts_ini:
        ts_ini = desde
    cierres = []
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "CLOSED":
                continue
            ts = _parse_ts(row.get("close_timestamp") or "")
            if ts is None or ts < ts_ini:
                continue
            try:
                cierres.append((ts, float(row.get("pnl_neto_eur", 0) or 0)))
            except ValueError:
                pass
    racha = 0
    for _, pnl in sorted(cierres, reverse=True):
        if pnl < 0:
            racha += 1
        else:
            break
    return racha


# ── Circuit breaker ───────────────────────────────────────────────────────────

def freno_diario_pct_hoy(config: dict | None = None) -> float:
    """
    Porcentaje del freno diario aplicable HOY. Permite un override puntual con
    fecha (riesgo.circuit_breaker.freno_diario_pct_override = {fecha, pct})
    que solo aplica si fecha == hoy (Madrid) — al día siguiente vuelve solo al
    valor normal, sin depender de que nadie se acuerde de revertir el config.
    Añadido 2026-07-03: decisión del usuario de seguir operando tras el freno
    de -28.6%, con suelo duro en bankroll_minimo_eur.
    """
    if config is None:
        config = _cargar_config()
    cb  = config.get("riesgo", {}).get("circuit_breaker", {})
    pct = cb.get("freno_diario_pct", 0.15)
    ov  = cb.get("freno_diario_pct_override") or {}
    try:
        if ov.get("fecha") == _ahora_madrid(config).date().isoformat():
            return float(ov["pct"])
    except (KeyError, TypeError, ValueError):
        pass
    return pct


def freno_ventana_pct_hoy(config: dict | None = None) -> float:
    """
    Como freno_diario_pct_hoy pero para el freno de ventana: override puntual
    con fecha (riesgo.circuit_breaker.freno_ventana_pct_override = {fecha, pct})
    que solo aplica hoy (Madrid) y autoexpira. Añadido 2026-07-03 tarde:
    decisión del usuario de reabrir la ventana tras el latch de las 17:07 y
    dejar como único corte el suelo de 8€ (freno diario 0.65 + bankroll_minimo).
    """
    if config is None:
        config = _cargar_config()
    cb  = config.get("riesgo", {}).get("circuit_breaker", {})
    pct = cb.get("freno_ventana_pct", 0.20)
    ov  = cb.get("freno_ventana_pct_override") or {}
    try:
        if ov.get("fecha") == _ahora_madrid(config).date().isoformat():
            return float(ov["pct"])
    except (KeyError, TypeError, ValueError):
        pass
    return pct


def bankroll_inicio_dia() -> float:
    """Bankroll al inicio del día de hoy (antes de cualquier trade de hoy)."""
    bkr_ahora = bankroll_actual()
    pnl_hoy   = pnl_live_hoy()
    return bkr_ahora - pnl_hoy


def pnl_live_ventana_actual() -> float:
    """PNL neto de trades cerrados en la ventana horaria actual."""
    if not TRADES_CSV.exists():
        return 0.0
    config = _cargar_config()
    v = _ventana_actual(config)
    if v is None:
        return 0.0
    ts_ini = _ts_inicio_ventana_utc(v, config)
    pnl = 0.0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "CLOSED":
                continue
            ts = _parse_ts(row.get("close_timestamp") or row.get("timestamp_utc") or "")
            if ts is not None and ts >= ts_ini:
                try:
                    pnl += float(row.get("pnl_neto_eur", 0) or 0)
                except ValueError:
                    pass
    return pnl


def verificar_circuit_breaker() -> tuple[bool, str]:
    """
    Tres niveles de freno (de mayor a menor prioridad):

      1. Bankroll mínimo absoluto (5€): apaga el switch, avisa al usuario.
      2. Freno diario (-15%): si el bankroll cayó 15% desde inicio del día → para hoy.
      3. Freno por ventana (-20%): si en esta ventana se ha perdido 20% del bankroll
         del inicio de la ventana → para esta ventana.

    Devuelve (disparado, motivo).
    """
    config  = _cargar_config()
    cb      = config.get("riesgo", {}).get("circuit_breaker", {})
    bkr     = bankroll_actual()
    bkr_min = cb.get("bankroll_minimo_eur", 5.0)

    # Freno 1 — bankroll mínimo absoluto (máxima prioridad, apaga el switch).
    # Usa min(real, ledger) explícitamente, no solo lo que bankroll_actual()
    # eligió (code-review 13-Jul): el fallback a ledger cuando el real
    # falta/está rancio asume que el ledger es más pesimista que el real
    # (cierto hoy, ~2.45€ de drift documentado), pero es una observación
    # histórica, no una garantía. Si algún día el real es PEOR que el
    # ledger (ej. fee/slippage no modelado) justo cuando el cache real cae
    # rancio, bankroll_actual() a secas reportaría el número más optimista
    # en el único freno con veto sobre todos los demás. min() es barato
    # (_bankroll_ledger() siempre disponible desde trades.csv) y cierra ese
    # hueco sin depender del signo del drift.
    bkr_suelo = min(bkr, _bankroll_ledger())
    if bkr_suelo <= bkr_min:
        if SWITCH_PATH.exists():
            SWITCH_PATH.unlink()
        return True, f"🛑 bankroll {bkr_suelo:.2f}€ ≤ mínimo {bkr_min:.2f}€ — switch desactivado"

    # Freno 2 — caída diaria (pct puede venir de un override con fecha)
    freno_dia_pct = freno_diario_pct_hoy(config)
    bkr_ini_dia   = bankroll_inicio_dia()
    if bkr_ini_dia > 0:
        caida_dia = (bkr_ini_dia - bkr) / bkr_ini_dia
        if caida_dia >= freno_dia_pct:
            return True, (f"🛑 caída diaria {caida_dia*100:.1f}% "
                          f"({bkr_ini_dia:.2f}€ → {bkr:.2f}€) ≥ freno {freno_dia_pct*100:.0f}%")

    # Freno 4 — racha de pérdidas consecutivas (para el día, como el freno 2)
    max_racha = cb.get("max_perdidas_consecutivas", 4)
    if max_racha:
        racha = racha_perdidas_consecutivas()
        if racha >= max_racha:
            return True, (f"🛑 {racha} pérdidas live consecutivas ≥ {max_racha} "
                          f"— racha sistemática, para el día")

    # Freno 3 — caída en ventana actual
    # Con latch: una vez disparado, la ventana queda cerrada el resto del día
    # aunque el PnL recupere (2026-07-03: disparó a las 14:35, un WIN lo
    # rearmó a los 50s y siguió operando en la misma ventana).
    freno_v_pct = freno_ventana_pct_hoy(config)
    v = _ventana_actual(config)
    if v:
        nombre_v = v.get("nombre") or f"{v.get('inicio','')}-{v.get('fin','')}"
        latch = _leer_latch_ventana()
        if (latch.get("fecha") == _ahora_madrid(config).date().isoformat()
                and latch.get("ventana") == nombre_v):
            return True, (f"🛑 ventana '{nombre_v}' cerrada por freno a las "
                          f"{latch.get('ts','?')} — no reabre hasta la siguiente ventana")
        pnl_v       = pnl_live_ventana_actual()
        desp        = stakes_desplegados_ventana_actual()
        # _bankroll_ledger() (no bkr, que puede ser real): pnl_v es de ledger
        # y no hay real con granularidad de ventana — ver docstring de
        # _bankroll_ledger(). Mezclar bkr real con pnl_v de ledger daría una
        # base de ventana incoherente.
        bkr_ini_v   = _bankroll_ledger() - pnl_v  # bankroll al inicio de esta ventana
        if bkr_ini_v > 0 and pnl_v < 0:
            caida_v = abs(pnl_v) / bkr_ini_v
            if caida_v >= freno_v_pct:
                _escribir_latch_ventana(nombre_v, config)
                return True, (f"🛑 caída en ventana '{nombre_v}' "
                               f"{caida_v*100:.1f}% ({pnl_v:.2f}€) ≥ freno {freno_v_pct*100:.0f}%")

    return False, f"✅ OK  (bkr={bkr:.2f}€  pnl_día={pnl_live_hoy():+.2f}€)"


def _leer_latch_ventana() -> dict:
    if not LATCH_VENTANA_PATH.exists():
        return {}
    try:
        return json.loads(LATCH_VENTANA_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        # Fail loud (13-Jul, purificación): un latch corrupto se lee igual
        # que "nunca disparó" (dict vacío) — reproduce EXACTAMENTE el bug
        # del 03-Jul que este latch existe para prevenir (freno de ventana
        # se rearmaba solo al recuperar PnL, disparó 14:35, un WIN lo
        # rearmó a los 50s y siguió operando en la misma ventana). No se
        # cambia el fail-open aquí (sería una decisión de riesgo nueva, no
        # una limpieza) — solo se deja rastro de que pasó.
        print(f"  ⚠️ latch de ventana ilegible ({type(e).__name__}: {e}) — "
              f"se trata como si el freno de ventana NUNCA hubiera disparado hoy")
        return {}


def _escribir_latch_ventana(nombre_ventana: str, config: dict) -> None:
    try:
        LATCH_VENTANA_PATH.write_text(json.dumps({
            "fecha": _ahora_madrid(config).date().isoformat(),
            "ventana": nombre_ventana,
            "ts": _ahora_madrid(config).strftime("%H:%M"),
        }), encoding="utf-8")
    except Exception as e:
        # el freno ya devuelve True este ciclo (no bloquea); ver nota en
        # _leer_latch_ventana sobre por qué SÍ importa que esto se vea.
        print(f"  ⚠️ fallo al escribir latch de ventana ({type(e).__name__}: {e}) "
              f"— si no se persiste, el freno de esta ventana podría no "
              f"recordarse en ciclos futuros")


# ── Inventario direccional (Shaw & Dalen 2025 — AS en logit space) ───────────

def inventario_direccional_hoy() -> dict:
    """
    Cuenta las posiciones abiertas de hoy por dirección (BUY_YES / BUY_NO).
    Devuelve {'BUY_YES': n, 'BUY_NO': n, 'q_net': n}.
    q_net > 0 → sesgo largo (más YES); q_net < 0 → sesgo corto (más NO).
    """
    if not TRADES_CSV.exists():
        return {"BUY_YES": 0, "BUY_NO": 0, "q_net": 0}
    config = _cargar_config()
    ts_ini = _ts_inicio_dia_utc(config)
    n_yes  = 0
    n_no   = 0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") not in ("OPEN", "STUB"):
                continue
            ts = _parse_ts(row.get("timestamp_utc") or "")
            if ts is None or ts < ts_ini:
                continue
            if row.get("direction") == "BUY_YES":
                n_yes += 1
            elif row.get("direction") == "BUY_NO":
                n_no += 1
    return {"BUY_YES": n_yes, "BUY_NO": n_no, "q_net": n_yes - n_no}


def _inventory_penalty(direction: str, inv: dict) -> float:
    """
    Factor de penalización de stake según inventario acumulado (principio AS).
    Si apostamos en la misma dirección que el inventario neto, reducimos el stake.
    Primera apuesta en esa dirección: sin penalización.
    Cada apuesta adicional en la misma dirección: -20%, mínimo 50%.
    """
    q_net = inv.get("q_net", 0)
    if direction == "BUY_YES" and q_net > 0:
        exceso = q_net          # posiciones YES de más
    elif direction == "BUY_NO" and q_net < 0:
        exceso = abs(q_net)     # posiciones NO de más
    else:
        return 1.0              # dirección contraria o neutral — sin penalización
    return max(0.50, 1.0 - exceso * 0.20)


# ── Calcular stake ────────────────────────────────────────────────────────────

def calcular_stake(ic: float, strategy: str = "", subtype: str = "",
                   direction: str = "") -> dict:
    """
    Stake para una señal con IC dado.
    Opera con el bankroll completo en cada ventana (compounding natural).

    Techos en cascada:
      1. Kelly half: IC × bankroll × 0.5
      2. Máx 10% del bankroll por trade (nunca más de 2€ con bankroll=20€)
      3. Máximo absoluto del config (2€)
    """
    config     = _cargar_config()
    riesgo     = config.get("riesgo", {})
    bkr        = bankroll_actual()
    half_kelly = riesgo.get("half_kelly", True)
    max_pct    = riesgo.get("max_pct_bankroll_por_trade", 0.10)
    min_stake  = riesgo.get("min_stake_eur", 0.25)
    max_stake  = riesgo.get("max_stake_eur", 2.00)

    techo_kelly  = bkr * abs(ic) * (0.5 if half_kelly else 1.0)
    techo_pct    = bkr * max_pct
    techo_config = max_stake

    stake = min(techo_kelly, techo_pct, techo_config)
    stake = max(stake, min_stake) if bkr >= min_stake else 0.0

    # Penalización por inventario (Avellaneda-Stoikov en logit space):
    # si ya tenemos posiciones abiertas en la misma dirección, reducir stake.
    inv_factor = 1.0
    inv_str    = ""
    if direction:
        inv = inventario_direccional_hoy()
        inv_factor = _inventory_penalty(direction, inv)
        if inv_factor < 1.0:
            stake = max(min_stake, stake * inv_factor)
            inv_str = (f" | inv_penalty×{inv_factor:.2f} "
                       f"(q_net={inv['q_net']:+d} YES={inv['BUY_YES']} NO={inv['BUY_NO']})")

    # Freno diario prospectivo: el freno 2 del circuit breaker
    # (verificar_circuit_breaker) solo mira PnL realizado, así que con stakes
    # de ~8% del bankroll un solo trade puede cruzar el límite diario de largo
    # (2026-07-02: -12.9% realizado antes del último trade y el día cerró en
    # -20%). Techo extra: si este stake Y todos los abiertos se perdieran
    # enteros, la caída del día no puede superar freno_diario_pct. Los stakes
    # abiertos sin resolver se restan del margen — no contarlos fue lo que el
    # 2026-07-03 dejó desplegar 6.54€ (28.6% del bankroll) con freno del 15%:
    # a las 06:38 había 3.19€ abiertos, pnl realizado 0.00€, y entraron
    # 3.35€ más. Suelo adicional: en el peor caso el bankroll no puede quedar
    # por debajo de bankroll_minimo_eur. Si el margen restante no da ni para
    # min_stake, la señal deja de ser viable (equivale a disparar el freno un
    # trade antes). Código de seguridad live — no minimizar.
    freno_str = ""
    freno_dia_pct = freno_diario_pct_hoy(config)
    bkr_min       = riesgo.get("circuit_breaker", {}).get("bankroll_minimo_eur", 5.0)
    bkr_ini_dia   = bankroll_inicio_dia()
    abiertos      = stakes_abiertos_total()
    if bkr_ini_dia > 0:
        margen_freno = bkr_ini_dia * freno_dia_pct + pnl_live_hoy() - abiertos
        margen_suelo = bkr - bkr_min - abiertos
        margen_dia   = min(margen_freno, margen_suelo)
        if stake > margen_dia:
            stake = max(0.0, margen_dia)
            if stake < min_stake:
                stake = 0.0
            freno_str = (f" | techo_freno_diario={margen_dia:.2f}€ "
                         f"(freno={freno_dia_pct*100:.0f}% de {bkr_ini_dia:.2f}€, "
                         f"pnl_hoy={pnl_live_hoy():+.2f}€, abiertos={abiertos:.2f}€, "
                         f"suelo_bkr={bkr_min:.2f}€)")

    motivo = (
        f"bankroll={bkr:.2f}€ | "
        f"Kelly={techo_kelly:.2f}€  max10%={techo_pct:.2f}€  máx={techo_config:.2f}€"
        f"{inv_str}{freno_str} → stake={stake:.2f}€"
    )

    return {
        "stake_eur":  round(stake, 2),
        "bankroll":   round(bkr, 2),
        "motivo":     motivo,
        "viable":     stake >= min_stake,
    }


# ── CLI de diagnóstico ────────────────────────────────────────────────────────

if __name__ == "__main__":
    config = _cargar_config()
    bkr    = bankroll_actual()
    n_rest = ventanas_restantes_hoy(config)
    desp   = stakes_desplegados_ventana_actual()
    pnl_h  = pnl_live_hoy()
    v      = _ventana_actual(config)
    cb, motivo_cb = verificar_circuit_breaker()

    print(f"Bankroll actual:       {bkr:.2f}€")
    print(f"PNL hoy:               {pnl_h:+.2f}€")
    print(f"Ventana actual:        {v['nombre'] if v else 'fuera de ventana'}")
    print(f"Ventanas restantes:    {n_rest}")
    print(f"Budget esta ventana:   {bkr/n_rest:.2f}€")
    print(f"Ya desplegado:         {desp:.2f}€")
    print(f"Restante ventana:      {max(0, bkr/n_rest - desp):.2f}€")
    print(f"Circuit breaker:       {'🛑 DISPARADO — ' + motivo_cb if cb else '✅ OK'}")
    print()
    print("Simulación de stakes:")
    for ic in [0.08, 0.10, 0.15, 0.22]:
        r = calcular_stake(ic)
        print(f"  IC={ic:+.2f} → {r['stake_eur']:.2f}€  |  {r['motivo']}")
