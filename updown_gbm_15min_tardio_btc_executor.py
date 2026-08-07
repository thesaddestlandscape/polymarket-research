#!/usr/bin/env python3
"""
updown_gbm_15min_tardio_btc_executor.py — Ejecutor de baja latencia para
UPDOWN_GBM_15M_TARDIO#{BTC,XRP,BNB,SOL}#15min (BUY_YES o BUY_NO, según el
signo del edge).

07-Ago: generalizado de BTC-only a XRP/BNB/SOL -- petición explícita Javi
tras encontrar que `gate_bucket_propio.json` tiene 4 micro-buckets
`bueno_confirmado` en esta familia para esas 3 monedas (nunca antes
instrumentados con baja latencia): XRP#15min#BUY_YES [0.50,0.55) n=235
pnl_shadow=+0.808€, BNB#15min#BUY_YES [0.50,0.55) n=96 pnl=+0.741€,
BNB#15min#BUY_NO [0.45,0.50) n=67 pnl=+1.417€, SOL#15min#BUY_YES
[0.50,0.55) n=94 pnl=+0.708€ -- todos con evidencia SOLO vía el polling
lento (`libro_snapshots.csv`, ~20-40s de latencia real), nunca medidos con
un ejecutor dedicado. Mismo patrón ya confirmado hoy mismo con
FAVORITO_CONFIRMADO#ETH#15min#BUY_YES: el polling lento subestima
fill-ability real (pnl -0.30€ vía snapshot lento vs +0.10€ vía señales
capturadas por el propio ejecutor de baja latencia). Nada de esto
promueve nada todavía -- solo añade la instrumentación que faltaba para
poder medirlo bien. ETH deliberadamente NO incluido (sin bucket
`bueno_confirmado` propio en esta familia hoy).

Origen (04-Ago, paso 5 del plan de acción de
project_barrido_definitivo_latencia_17_combos_03ago): candidata del
cementerio (retirada 28-Jul, "0 trades reales en 13 días") con la 2ª mayor
firma de latencia de todo el sistema (+109.0s, n=165). Mismo mecanismo que
GBM_LATE_15M/FAVORITO_CONFIRMADO#BTC#60min — la selección adversa
diagnosticada al retirarla puede ser en parte artefacto de lentitud del
ciclo lento, no de falta de edge real. Este ejecutor mide si capturar la
señal sin ese lag revive el edge -- justificación para reintentar, NO
prueba de que funcionará (ninguna promoción sin gate riguroso completo
re-verificado).

Diseño: familia de fórmula DISTINTA a GBM_LATE_15M (Black-Scholes digital
con drift/régimen, `s_updown_gbm()` en shadow_predict.py, ~250 líneas de
filtros delicados con consumidores existentes: hypothesis_tracker, el
cross-check model-free de FAVORITO_CONFIRMADO). Mismo criterio que
gbm_late_15min_executor.py: IMPORTA `s_updown_gbm()` directamente en vez
de reimplementarla -- cero riesgo de divergencia de fórmula.
`s_updown_gbm_15min_tardio()` solo envuelve `s_updown_gbm()` con un gate
de T_h<0.2 (BUY_YES_15M_TH_MAX) antes de llamarla -- se reimplementa aquí
ese único gate (comparación simple) y se llama a `s_updown_gbm()` con
`strategy_name="UPDOWN_GBM_15M_TARDIO"` tal cual hace el wrapper real.

Contexto ligero: auditado `s_updown_gbm()` línea a línea para separar qué
claves de `ctx` afectan p_up/la decisión (`precios_intraday`,
`meta_params` -- blacklist de horas, `spot_prices`) de las que son PURO
LOGUEO (`klines_raw`, `historial_mercados`, `trades_1h`, `funding_rates`,
`vwap_sesion`, `precios_ventanas_hoy` -- ninguna gatea ni cambia p_up,
todas alimentan features observacionales). Solo se cargan las 3 primeras
(las 2 primeras vía funciones ya usadas por gbm_late_15min_executor.py,
`meta_params` vía `_cargar_meta_params()`, lectura local barata de
`strategy_params.json`) -- sin fetch de funding rates ni klines_raw
(ambos solo alimentan logging, confirmado por auditoría del código real).

⚠️ DRY_RUN=True por defecto -- OBLIGATORIO. UPDOWN_GBM_15M_TARDIO#BTC#15min
NO está en pares_permitidos_live (candidata retirada) -- puede_operar_live()
la bloquea siempre por whitelist, con o sin DRY_RUN. Cambiar a False SOLO
tras revisión + aprobación explícita de Javi + /code-review, Y solo si
algún día se reconsiderara reactivarla con datos que lo justifiquen.

Corre en screen propia:
  screen -dmS updowngbmtardio bash -c "cd /root/polymarket-research && .venv/bin/python updown_gbm_15min_tardio_btc_executor.py >> logs/updown_gbm_15min_tardio_btc_executor.log 2>&1"
"""
import json
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

import live_trade as lt
from live_guard import puede_operar_live
from live_stake import bloquear_por_circuit_breaker, calcular_stake
from ballenas_banda_fina_gate import evaluar as _gate_banda_fina_ballenas
from gate_bucket_propio import evaluar as _gate_bucket_propio
import ballenas_firehose_cache as _fc
from shadow_predict import (
    s_updown_gbm,
    cargar_precios_intraday,
    _cargar_spot,
    _cargar_meta_params,
    BUY_YES_15M_TH_MAX,
)

DIR = Path(__file__).resolve().parent
DIR_SHADOW = DIR / "data" / "shadow"
CONFIG_LIVE_PATH = DIR / "data" / "live" / "config_live.json"

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"

STRATEGY = "UPDOWN_GBM_15M_TARDIO"
VENTANA_MIN = 15
ACTIVOS = ("BTC", "XRP", "BNB", "SOL")  # 07-Ago: XRP/BNB/SOL añadidas -- ver docstring

DRY_RUN = True  # 04-Ago v1 -- ver docstring, NO cambiar sin revisión + aprobación explícita + /code-review.

POLL_INTERVAL_S = 2.0
HARD_FLOOR_S = 5.0
REFRESCO_CTX_S = 20.0
# Ventana de entrada: T_h<BUY_YES_15M_TH_MAX (0.2h=12min) -- se traduce a
# minutos restantes para reusar el mismo patrón de espera que el resto de
# ejecutores (evita I/O innecesario mientras faltan minutos para la
# ventana de confirmación tardía).
REST_MIN_HI = BUY_YES_15M_TH_MAX * 60.0  # 12.0 min

_session = requests.Session()
_orden_lock = threading.Lock()
_pares_live_cache = {"mtime": None, "set": set()}
_ctx_cache = {"ts": 0.0, "precios_intraday": [], "spot_prices": {}, "meta_params": {}}


def log(msg: str, activo: str = "") -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    prefijo = f"[{activo}] " if activo else ""
    print(f"[{ts}] {prefijo}{msg}", flush=True)


def _pares_live_hoy_set() -> set:
    """Mismo patrón fail-closed que el resto de ejecutores de baja latencia."""
    try:
        mtime = CONFIG_LIVE_PATH.stat().st_mtime
    except OSError:
        return _pares_live_cache["set"]
    if _pares_live_cache["mtime"] != mtime:
        try:
            data = json.loads(CONFIG_LIVE_PATH.read_text(encoding="utf-8"))
            _pares_live_cache["set"] = set(data.get("pares_permitidos_live", []))
            _pares_live_cache["mtime"] = mtime
        except Exception:
            pass
    return _pares_live_cache["set"]


def _ctx_ligero() -> dict:
    """precios_intraday + spot_prices + meta_params, recargados cada
    REFRESCO_CTX_S -- ver docstring del módulo para la auditoría de qué
    claves de ctx afectan p_up/decisión vs las que son puro logueo
    (klines_raw/historial_mercados/trades_1h/funding_rates/vwap_sesion/
    precios_ventanas_hoy quedan ausentes a propósito, sin impacto real)."""
    ahora = time.time()
    if ahora - _ctx_cache["ts"] > REFRESCO_CTX_S:
        _ctx_cache["precios_intraday"] = cargar_precios_intraday()
        _ctx_cache["spot_prices"] = _cargar_spot()
        _ctx_cache["meta_params"] = _cargar_meta_params()
        _ctx_cache["ts"] = ahora
    return {
        "precios_intraday": _ctx_cache["precios_intraday"],
        "spot_prices": _ctx_cache["spot_prices"],
        "meta_params": _ctx_cache["meta_params"],
    }


def resolver_mercado(activo: str, ts_start: int) -> dict | None:
    """Mismo patrón que gbm_late_15min_executor.py -- una sola llamada
    gamma-api por ventana de 15min, capturando también liquidity/spread
    (s_updown_gbm() los exige: liquidity>=2000, spread<=0.05)."""
    slug = f"{activo.lower()}-updown-{VENTANA_MIN}m-{ts_start}"
    try:
        r = _session.get(f"{GAMMA}/events", params={"slug": slug}, timeout=5)
        if r.status_code != 200:
            return None
        ev = r.json()
        if not ev or not ev[0].get("markets"):
            return None
        mkt = ev[0]["markets"][0]
        tokens = json.loads(mkt.get("clobTokenIds") or "[]")
        if len(tokens) < 2:
            return None
        return {
            "market_id": mkt.get("id", ""),
            "condition_id": mkt.get("conditionId", ""),
            "question": mkt.get("question", ""),
            "spread": mkt.get("spread"),
            "liquidity": mkt.get("liquidity"),
            "yes_token": tokens[0],
            "no_token": tokens[1],
            "end_date": mkt.get("endDate", ""),
        }
    except Exception as e:
        log(f"resolver_mercado error: {e}", activo)
        return None


def libro_publico(token_id: str) -> dict | None:
    try:
        r = _session.get(f"{CLOB}/book", params={"token_id": token_id}, timeout=5)
        if r.status_code != 200:
            return None
        b = r.json()
        asks = [(float(a["price"]), float(a["size"])) for a in (b.get("asks") or [])]
        best_ask = min((p for p, _ in asks), default=None)
        return {"best_ask": best_ask}
    except Exception:
        return None


def _registrar_prediccion(mercado: dict, activo: str, resultado: dict, direccion: str,
                           restante_s: float) -> None:
    """Mismo formato que shadow_predict.py/el resto de ejecutores."""
    import csv
    import fcntl
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    archivo = DIR_SHADOW / f"predictions_{ts[:10]}.csv"
    subtype = f"{activo}#{VENTANA_MIN}min"
    py = mercado["_precio_yes_usado"]
    prob_yes = resultado["prob_yes"]
    edge = prob_yes - py
    features = dict(resultado["features"])
    features["ejecutor_baja_latencia"] = True
    features_json = json.dumps(features, separators=(",", ":"))
    lock_path = DIR_SHADOW / ".predictions_lock"
    try:
        with open(lock_path, "w") as lock_f:
            fcntl.flock(lock_f, fcntl.LOCK_EX)
            try:
                nuevo = not archivo.exists()
                with open(archivo, "a", newline="", encoding="utf-8") as f:
                    w = csv.writer(f)
                    if nuevo:
                        w.writerow([
                            "timestamp_utc", "strategy", "market_id", "question", "end_date",
                            "horas_a_vencimiento", "precio_yes_mercado", "prob_yes_modelo",
                            "edge_bruto", "edge_neto", "edge_direccional", "decision", "razon",
                            "subtype", "apuesta", "features",
                        ])
                    w.writerow([
                        ts, STRATEGY, mercado["market_id"], "", mercado.get("end_date", ""),
                        f"{restante_s / 3600:.4f}", f"{py:.4f}", f"{prob_yes:.4f}",
                        f"{edge:.4f}", f"{edge:.4f}", f"{edge:.4f}", direccion,
                        resultado.get("razon", "") + " (ejecutor baja latencia)", subtype,
                        "1.05", features_json,
                    ])
            finally:
                fcntl.flock(lock_f, fcntl.LOCK_UN)
    except Exception as e:
        log(f"aviso: no se pudo registrar predicción para postmortem: {e}", activo)


def watch_window(activo: str, mercado: dict) -> bool:
    """Vigila un mercado {activo}#15min concreto -- entra en juego en
    cuanto restante_min cae dentro de [0, REST_MIN_HI] (T_h<0.2h, mismo
    gate que s_updown_gbm_15min_tardio) y sale sola cuando la ventana
    cierra. True si ejecutó (o habría ejecutado en DRY_RUN)."""
    try:
        end_dt = datetime.fromisoformat(mercado["end_date"].replace("Z", "+00:00"))
        if end_dt.tzinfo is None:
            end_dt = end_dt.replace(tzinfo=timezone.utc)
    except Exception:
        log(f"end_date ilegible: {mercado.get('end_date')} -- se abandona", activo)
        return False
    ts_end = end_dt.timestamp()
    n_polls = 0
    contadores = {"ok_sin_edge": 0, "sin_dato": 0, "vetado_gate_bucket": 0}

    while True:
        restante_s = ts_end - time.time()
        restante_min = restante_s / 60.0
        if restante_s < HARD_FLOOR_S:
            log(f"[{mercado['market_id']}] ventana cerrada (restante={restante_min:.1f}min) -- "
                f"se abandona ({n_polls} polls, {contadores})", activo)
            return False
        if mercado["market_id"] in lt._ya_operados_hoy():
            log(f"[{mercado['market_id']}] ya operado -- se abandona", activo)
            return False
        if restante_min > REST_MIN_HI:
            time.sleep(min((restante_min - REST_MIN_HI) * 60, 5))
            continue

        libro = libro_publico(mercado["yes_token"])
        n_polls += 1
        py = libro.get("best_ask") if libro else None
        if py is None:
            contadores["sin_dato"] += 1
            time.sleep(POLL_INTERVAL_S)
            continue

        market_full = dict(mercado)
        market_full["_precio_yes"] = py
        market_full["_precio_yes_usado"] = py
        market_full["_horas"] = restante_s / 3600.0
        ctx = _ctx_ligero()
        resultado = s_updown_gbm(market_full, ctx, strategy_name=STRATEGY)
        if resultado is None:
            contadores["ok_sin_edge"] += 1
            time.sleep(POLL_INTERVAL_S)
            continue

        prob_yes_dir = resultado["prob_yes"]
        direccion = "BUY_YES" if prob_yes_dir >= py else "BUY_NO"

        tupla_str = f"{STRATEGY}#{activo}#{VENTANA_MIN}min#{direccion}"
        gate_bp = _gate_bucket_propio(tupla_str, py)
        resultado["features"]["gate_bucket_propio_veredicto"] = gate_bp["veredicto"]
        if gate_bp["veredicto"] == "malo_confirmado" and tupla_str in _pares_live_hoy_set():
            contadores["vetado_gate_bucket"] += 1
            log(f"[{mercado['market_id']}] py={py:.3f} vetado por gate_bucket_propio "
                f"(malo_confirmado)", activo)
            return False

        log(f"[{mercado['market_id']}] CONFIRMADO {direccion} py={py:.3f} "
            f"prob_yes={prob_yes_dir:.3f} restante={restante_s:.1f}s ({n_polls} polls)", activo)
        _registrar_prediccion(market_full, activo, resultado, direccion, restante_s)
        return disparar(activo, mercado, py, prob_yes_dir, direccion, restante_s)


def disparar(activo: str, mercado: dict, py: float, prob_yes: float, direccion: str,
             restante_s: float) -> bool:
    """Mismos guardias, mismo orden, que gbm_late_15min_executor.py."""
    subtype = f"{activo}#{VENTANA_MIN}min"

    ok_operar, motivo_operar = puede_operar_live(STRATEGY, subtype)
    if not ok_operar:
        log(f"  {motivo_operar} -- {'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
        return False

    config = lt._cargar_config()
    max_misma_dir = config.get("riesgo", {}).get("max_posiciones_abiertas_misma_direccion", 2)
    abiertas_dir = lt._posiciones_abiertas_misma_direccion(direccion)
    if abiertas_dir >= max_misma_dir:
        log(f"  techo de correlación: {abiertas_dir} posiciones {direccion} abiertas >= {max_misma_dir} -- "
            f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
        return False

    with _orden_lock:
        if mercado["market_id"] in lt._ya_operados_hoy():
            log(f"  {mercado['market_id']} ya operado por otro proceso -- "
                f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        if bloquear_por_circuit_breaker(
                lambda motivo: log(f"  circuit breaker activo ({motivo}) -- "
                                    f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)):
            return False

        lt._CLV_CACHE = None
        clv_medio, n_clv = lt._clv_tupla(STRATEGY, subtype, direccion)
        if n_clv >= lt.CLV_VETO_MIN_N and clv_medio < 0:
            log(f"  ⛔ Veto CLV: clv_medio={clv_medio:+.4f} (n={n_clv}) < 0 -- "
                f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        if direccion == "BUY_YES":
            edge_dir = prob_yes - py
            ic_conviccion = max(0.0, edge_dir / (1 - py)) if py < 1 else 0.0
            precio_decision = py
        else:
            edge_dir = py - prob_yes
            ic_conviccion = max(0.0, edge_dir / py) if py > 0 else 0.0
            precio_decision = round(1.0 - py, 6)

        stake_info = calcular_stake(ic_conviccion, STRATEGY, subtype, direction=direccion,
                                    precio_entrada=precio_decision)
        if not stake_info.get("viable"):
            log(f"  stake no viable: {stake_info.get('motivo')} -- "
                f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        if DRY_RUN:
            log(f"  [DRY-RUN] habría ejecutado {direccion} {mercado['market_id']} py={py:.3f} "
                f"prob_yes={prob_yes:.3f} stake={stake_info['stake_eur']:.2f}€ restante={restante_s:.1f}s",
                activo)
            return True

        resultado = lt._ejecutar_orden_polymarket(
            mercado["market_id"], direccion, stake_info["stake_eur"], py,
            edge_dir=edge_dir, contexto={"strategy": STRATEGY, "subtype": subtype})

        if resultado.get("no_fill"):
            log(f"  no_fill: {resultado.get('error')}", activo)
            return False

        trade = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "market_id": mercado["market_id"], "question": "", "end_date": mercado.get("end_date", ""),
            "strategy": STRATEGY, "subtype": subtype, "direction": direccion,
            "stake_eur": stake_info["stake_eur"] if resultado["ok"] else 0.0,
            "entry_price": resultado["entry_price"],
            "signal_ask": round(py, 4), "slip_real": resultado.get("slip_real", ""),
            "ic_modelo": round(prob_yes, 4), "edge_neto": round(prob_yes - py, 4),
            "conviction_score": round(prob_yes, 4), "kelly_recomendado": stake_info["stake_eur"],
            "status": "OPEN" if resultado["ok"] else "ERROR",
            "close_timestamp": "", "exit_price": "", "outcome_real": "",
            "fee_eur": resultado.get("fee_eur", 0), "pnl_bruto_eur": "", "pnl_neto_eur": "",
            "notas": (f"updown_gbm_15m_tardio_baja_latencia restante={restante_s:.1f}s"
                      if resultado.get("ok") else resultado.get("error", "")),
        }
        lt._registrar_trade(trade)
        log(f"  {'EJECUTADO' if resultado['ok'] else 'ERROR'}: {resultado}", activo)
        if resultado["ok"]:
            lt.enviar_telegram(
                f"🎯 *Orden live ejecutada (UPDOWN_GBM_15M_TARDIO baja latencia)*\n"
                f"Estrategia: {STRATEGY}#{subtype}#{direccion}\n"
                f"Precio fill: {resultado['entry_price']:.4f} (slip {resultado.get('slip_real', 0):+.4f})\n"
                f"Stake: {stake_info['stake_eur']:.2f}$  |  restante={restante_s:.1f}s\n"
                f"Bankroll operativo: {lt.bankroll_actual():.2f}$ (real al cierre de ciclo)"
            )
        else:
            lt.enviar_telegram(
                f"❌ *Orden live ERROR (UPDOWN_GBM_15M_TARDIO baja latencia)*\n"
                f"{STRATEGY}#{subtype} {direccion}\n{resultado.get('error', '')[:200]}"
            )
        return True


def hilo_activo(activo: str) -> None:
    log("hilo arrancado", activo)
    mercado_vigilado = None
    while True:
        try:
            now = time.time()
            ts_end = (int(now) // (VENTANA_MIN * 60) + 1) * (VENTANA_MIN * 60)
            ts_start = ts_end - VENTANA_MIN * 60
            if ts_start == mercado_vigilado:
                time.sleep(5)
                continue
            mercado = resolver_mercado(activo, ts_start)
            if mercado is None:
                time.sleep(10)
                continue
            mercado_vigilado = ts_start
            watch_window(activo, mercado)
        except Exception as e:
            log(f"error en hilo: {e} -- reintenta en 5s", activo)
            time.sleep(5)


def main():
    log(f"updown_gbm_15min_tardio_btc_executor arrancado (DRY_RUN={DRY_RUN}, activos={list(ACTIVOS)})")
    _fc.iniciar()
    time.sleep(3)
    if not DRY_RUN:
        _ = lt._get_clob_client()
        log("ClobClient precalentado")

    hilos = [threading.Thread(target=hilo_activo, args=(activo,), daemon=True, name=activo)
             for activo in ACTIVOS]
    for h in hilos:
        h.start()

    while True:
        time.sleep(30)
        for i, h in enumerate(hilos):
            if not h.is_alive():
                activo = h.name
                log("hilo murió inesperadamente -- reiniciando", activo)
                nuevo = threading.Thread(target=hilo_activo, args=(activo,), daemon=True, name=activo)
                nuevo.start()
                hilos[i] = nuevo


if __name__ == "__main__":
    main()
