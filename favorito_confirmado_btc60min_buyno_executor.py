#!/usr/bin/env python3
"""
favorito_confirmado_btc60min_buyno_executor.py — Ejecutor de baja latencia
para FAVORITO_CONFIRMADO#{BTC,ETH}#60min#BUY_NO.

Origen (30-Jul, barrido de tuplas whitelist estancadas): esta tupla lleva
desde 28-Jul sin trades reales (2 días) pese a estar en pares_permitidos_live
-- diagnóstico en logs/fast.log: 9/9 señales visibles mueren por "Señal
caducada" (SENAL_MAX_LATENCIA_SEG=100 de live_trade.py, mismo mecanismo ya
diagnosticado y resuelto para ALTACONVICCION#15min el mismo día). Mismo
patrón, mismo fix: s_favorito_confirmado() es MODEL-FREE (solo umbral de
precio, sin drift/sigma), barato de vigilar en un poll rápido.

04-Ago: generalizado a ETH (candidato, nunca live) -- último hueco de la
tabla de 17 combos de project_barrido_definitivo_latencia_17_combos_03ago
(FAVORITO_CONFIRMADO#ETH#60min#BUY_NO, +55.5s de gap, 12.9% de señales
perdidas, n=263). ETH no tiene entrada en GATE_VOLUMEN_VALIDADO de
shadow_predict.py (fail-open, sin gate propio todavía, mismo patrón que
BTC en favorito_altaconviccion_executor_15min.py) -- BTC SÍ mantiene su
gate validado sin cambios.

Diferencia clave frente a favorito_altaconviccion_executor_15min.py: los
mercados "hourly" (60min) NO tienen slug determinista resoluble (confirmado
en vivo -- el slug real es tipo "bitcoin-up-or-down-july-30-2026-8pm-et",
depende del mes/día/hora en texto, no de un timestamp unix como los de
5/15min). Se resuelve reusando `_universo_activo()` de
fetch_libro_ambos_lados.py (ya en producción, clasifica por TEXTO de la
pregunta, no por slug) filtrado a {activo}#60min -- margen amplio, solo
hace falta tener el market_id resuelto en algún punto de la ventana de
60min, no en el primer segundo.

Replica EXACTAMENTE la lógica de la rama BUY_NO de s_favorito_confirmado
(shadow_predict.py): FAVORITO_CONFIRMADO_UMBRAL_BAJO=0.45, sin techo (el
techo TH_MAX solo aplica al lado YES en la estrategia madre), gate de
volumen real GATE_VOLUMEN_VALIDADO (("FAVORITO_CONFIRMADO","BTC","60min",
"BUY_NO"): 35, ya validado n=215 hit=97.3% GATE OK en shadow_predict.py --
ETH sin entrada todavía, fail-open) -- a diferencia del lado YES, aquí
cuenta compras DOWN/NO, no UP/YES. gate_bucket_propio (veta si
malo_confirmado Y la tupla exacta está en pares_permitidos_live),
banda_fina_ballenas (solo observacional).

⚠️ DRY_RUN=True por defecto -- OBLIGATORIO. `FAVORITO_CONFIRMADO#BTC#60min
#BUY_NO` YA ESTÁ en pares_permitidos_live (dinero real) para el pipeline
normal; `#ETH#60min#BUY_NO` NO lo está (candidato, doble protección igual
que el resto de ejecutores de candidatas de hoy: puede_operar_live()
bloquearía ETH aunque DRY_RUN pasara a False por error). Si este proceso
arrancara con DRY_RUN=False empezaría a operar real de inmediato en BTC
en cuanto detectara la primera señal, sin revisión previa. Cambiar a
False SOLO tras revisión + aprobación explícita de Javi, mismo patrón en
dos fases que TODOS los ejecutores anteriores de este proyecto.

Corre en screen propia:
  screen -dmS favbtc60mno bash -c "cd /root/polymarket-research && .venv/bin/python favorito_confirmado_btc60min_buyno_executor.py >> logs/favorito_confirmado_btc60min_buyno.log 2>&1"
"""
import csv
import fcntl
import json
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

import live_trade as lt
from live_guard import puede_operar_live
from live_stake import bloquear_por_circuit_breaker, calcular_stake
from fetch_libro_ambos_lados import _universo_activo
from ballenas_banda_fina_gate import evaluar as _gate_banda_fina_ballenas
from gate_bucket_propio import evaluar as _gate_bucket_propio
import ballenas_firehose_cache as _fc

DIR = Path(__file__).resolve().parent
DIR_SHADOW = DIR / "data" / "shadow"
STRATEGY_PARAMS_PATH = DIR_SHADOW / "strategy_params.json"
CONFIG_LIVE_PATH = DIR / "data" / "live" / "config_live.json"
PREDICTIONS_LOCK_PATH = DIR_SHADOW / ".predictions_lock"

CLOB = "https://clob.polymarket.com"

STRATEGY = "FAVORITO_CONFIRMADO"
DIRECTION = "BUY_NO"
ACTIVOS = ("BTC", "ETH")
MARCO = "60min"
VENTANA_MIN = 60

DRY_RUN = False  # 04-Ago: activado -- aprobación explícita Javi tras revisión adversarial
# manual (constantes UMBRAL_BAJO/NUDGE verificadas idénticas a shadow_predict.py,
# guardias idénticas al resto del proyecto -- idempotencia lt._ya_operados_hoy()
# comprobada dos veces, whitelist, circuit breaker, veto CLV, calcular_stake()
# real, sin lógica custom). Solo BTC#60min#BUY_NO está en pares_permitidos_live
# -- ETH#60min#BUY_NO sigue bloqueada por puede_operar_live() aunque DRY_RUN ya
# no la proteja, doble protección real, no solo en teoría (verificado 04-Ago).

POLL_INTERVAL_S = 1.5
HARD_FLOOR_S = 3.0
REFRESCO_UNIVERSO_S = 30.0  # cadencia para volver a leer data/markets/HOY.csv
# cuando aún no hay mercado resuelto -- barato, el CSV lo mantiene
# capture_markets.py (run_slow.sh), no red nueva.

# Mismos valores exactos que shadow_predict.py (FAVORITO_CONFIRMADO_UMBRAL_BAJO
# / _NUDGE) -- duplicados aquí (mismo criterio que el resto de ejecutores de
# baja latencia: no importar shadow_predict.py completo). Si cambian allí,
# replicar aquí a mano -- vigilar en cada sesión que toque esta estrategia.
UMBRAL_BAJO = 0.45
NUDGE = 0.06

# Mismo gate real que _gate_volumen_ballenas en shadow_predict.py
# (GATE_VOLUMEN_VALIDADO) -- validado 27-Jul para BTC: n=215 alto=147
# hit=97.3% +0.916€ GATE OK. ETH sin entrada todavía -- None = fail-open
# (sin gate propio), mismo patrón que BTC en favorito_altaconviccion_
# executor_15min.py antes de tener su propio umbral validado.
GATE_VOLUMEN_VALIDADO = {
    "BTC": 35,
}

_session = requests.Session()
_orden_lock = threading.Lock()
_pares_live_cache = {"mtime": None, "set": set()}
_tokens_cache: dict[str, tuple[str, str]] = {}  # market_id -> (yes_token, no_token)


def log(msg: str, activo: str = "") -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    prefijo = f"[{activo}] " if activo else ""
    print(f"[{ts}] {prefijo}{msg}", flush=True)


def _pares_live_hoy_set() -> set:
    """Mismo patrón fail-closed que shadow_predict.py::_pares_live_hoy_set."""
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


def resolver_mercado(activo: str) -> dict | None:
    """{activo}#60min activo con edt más próximo (el universo debería
    tener como mucho uno vivo a la vez para este combo, pero por si acaso
    se toma el de cierre más cercano)."""
    try:
        universo = _universo_activo()
    except Exception as e:
        log(f"_universo_activo error: {e}", activo)
        return None
    candidatos = [(mid, cid, edt) for mid, (act, marco, cid, edt) in universo.items()
                  if act == activo and marco == MARCO]
    if not candidatos:
        return None
    mid, cid, edt = min(candidatos, key=lambda x: x[2])
    if mid in _tokens_cache:
        yes_token, no_token = _tokens_cache[mid]
    else:
        try:
            yes_token, no_token, _cid = lt._get_token_ids(mid)
        except Exception as e:
            log(f"_get_token_ids error para {mid}: {e}", activo)
            return None
        _tokens_cache[mid] = (yes_token, no_token)
    return {"market_id": mid, "condition_id": cid, "yes_token": yes_token,
            "no_token": no_token, "end_date": edt.isoformat()}


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


WALLET_EDGE_POR_ACTIVO_MARCO = DIR_SHADOW / "wallet_edge_score_por_activo_marco.json"
_wallet_edge_cache = {"mtime": None, "data": {}}


def _cargar_wallet_edge_activo_marco() -> dict:
    """Mismo patrón que ballenas_executor_btc15m.py -- fichero estático,
    sin llamada de red, cacheado por mtime."""
    try:
        mtime = WALLET_EDGE_POR_ACTIVO_MARCO.stat().st_mtime
    except OSError:
        return {}
    if _wallet_edge_cache["mtime"] != mtime:
        try:
            todo = json.loads(WALLET_EDGE_POR_ACTIVO_MARCO.read_text(encoding="utf-8"))
            _wallet_edge_cache["data"] = {(v["wallet"], v["activo"], v["marco"]): v for v in todo.values()}
        except Exception:
            _wallet_edge_cache["data"] = {}
        _wallet_edge_cache["mtime"] = mtime
    return _wallet_edge_cache["data"] or {}


def _n_no_total(condition_id: str, activo: str) -> tuple[int | None, dict | None]:
    """Compras DOWN/NO en TODO el mercado -- mismo cálculo que
    _gate_volumen_ballenas(direccion='BUY_NO') en shadow_predict.py.

    03-Ago (petición Javi, conectar infraestructura de ballenas):
    reutiliza la MISMA lista de trades ya descargada para el gate de
    volumen -- añade un resumen de wallet_edge_score PURAMENTE
    observacional (no veta, no toca n_no_total ni la decisión), sin
    ninguna llamada de red adicional. Devuelve (n_no_total, resumen_edge).

    04-Ago: fuente cambiada de smart_money_tracker.trades_de_mercado()
    (data-api.polymarket.com/trades -- tope duro de 250 + lag de
    indexación de minutos/horas, mismo bug diagnosticado y arreglado esa
    noche en el resto de ejecutores de ballenas/favorito) a
    ballenas_firehose_cache.trades_de_mercado_firehose() (websocket propio
    a RTDS, en memoria, sin tope ni lag). Si el cache no está sano
    devuelve (None, None) -- fail-open, mismo comportamiento que antes
    tenía un error de red. Ver feedback_verificar_api_trades_correcta_no_
    rota_04ago (memoria, esta pieza estaba en el inventario pendiente)."""
    if not _fc.esta_sano():
        return None, None
    trades = _fc.trades_de_mercado_firehose(condition_id)
    n_no_total = sum(1 for t in trades if (t.get("side") or "").strip().upper() == "BUY"
                      and (t.get("outcome") or "").strip().lower() in ("down", "no"))

    db = _cargar_wallet_edge_activo_marco()
    wallets_no = {(t.get("proxyWallet") or t.get("wallet") or "").lower() for t in trades
                  if (t.get("side") or "").strip().upper() == "BUY"
                  and (t.get("outcome") or "").strip().lower() in ("down", "no")}
    filas = [db[(w, activo, "60m")] for w in wallets_no if (w, activo, "60m") in db]
    edges = [f["edge_pp"] for f in filas]
    resumen_edge = {
        "wallet_edge_medio": round(sum(edges) / len(edges), 3) if edges else None,
        "wallet_n_con_score": len(edges),
        "wallet_n_sig_pos": sum(1 for f in filas if f["sig_bhfdr"] and f["edge_pp"] > 0),
        "wallet_n_sig_neg": sum(1 for f in filas if f["sig_bhfdr"] and f["edge_pp"] < 0),
    }
    return n_no_total, resumen_edge


def _activa_permite_disparo(activo: str) -> tuple[bool, str]:
    """Mismo mecanismo de autoconciencia que el resto de ejecutores de baja
    latencia -- respeta el veredicto de shadow_postmortem sobre el ic_bayes
    real de esta tupla en cuanto tenga n suficiente."""
    subtype = f"{activo}#{MARCO}"
    lookup_keys = [f"{STRATEGY}#{subtype}", f"{STRATEGY}#{activo}", f"{STRATEGY}#{MARCO}"]
    try:
        params = json.loads(STRATEGY_PARAMS_PATH.read_text(encoding="utf-8")).get("estrategias", {})
    except Exception:
        return True, "sin strategy_params.json legible -- fail-open"
    for k in lookup_keys:
        e = params.get(k)
        if e is None:
            continue
        campo = "activa_BUY_NO" if "activa_BUY_NO" in e else "activa"
        if not e.get(campo, True):
            return False, f"postmortem desactivó {k} ({campo}=False)"
    return True, "activa"


def _registrar_prediccion(activo: str, mercado: dict, py: float, prob_yes: float,
                           restante_s: float, n_no_total: int | None,
                           resumen_edge: dict | None = None) -> None:
    """Mismo formato que shadow_predict.py -- shadow_resolve.py/
    shadow_postmortem.py lo resuelven y aprenden de él sin duplicar esa
    lógica aquí, igual que el resto de ejecutores de baja latencia."""
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    archivo = DIR_SHADOW / f"predictions_{ts[:10]}.csv"
    subtype = f"{activo}#{MARCO}"
    edge = prob_yes - py  # perspectiva YES, por convención (CLAUDE.md)
    gate_bf = _gate_banda_fina_ballenas(activo, MARCO, py, restante_s / 60.0)
    features = json.dumps({
        "py_entrada": round(py, 4), "n_total_lado": n_no_total,
        "restante_min": round(restante_s / 60.0, 2),
        "hora_utc": datetime.now(timezone.utc).hour,
        "banda_fina_vetaria_fase1": gate_bf["vetaria_fase1"], "banda_fina_motivo": gate_bf["motivo"],
        "ejecutor_baja_latencia": True,
        **(resumen_edge or {}),
    }, separators=(",", ":"))
    try:
        with open(PREDICTIONS_LOCK_PATH, "w") as lock_f:
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
                        f"{edge:.4f}", f"{edge:.4f}", f"{edge:.4f}", DIRECTION,
                        "favorito_confirmado momentum-consenso (ejecutor baja latencia)", subtype,
                        "1.05", features,
                    ])
            finally:
                fcntl.flock(lock_f, fcntl.LOCK_UN)
    except Exception as e:
        log(f"aviso: no se pudo registrar predicción para postmortem: {e}")


def watch_window(activo: str, mercado: dict) -> bool:
    """Vigila un mercado {activo}#60min concreto hasta su cierre. True si
    ejecutó (o habría ejecutado en DRY_RUN)."""
    try:
        end_dt = datetime.fromisoformat(mercado["end_date"])
    except Exception:
        log(f"end_date ilegible: {mercado.get('end_date')} -- se abandona", activo)
        return False
    ts_end = end_dt.timestamp()
    umbral_vol = GATE_VOLUMEN_VALIDADO.get(activo)
    n_polls = 0
    while True:
        restante = ts_end - time.time()
        if restante < HARD_FLOOR_S:
            log(f"[{mercado['market_id']}] suelo de seguridad alcanzado sin confirmación ({n_polls} polls)", activo)
            return False
        if mercado["market_id"] in lt._ya_operados_hoy():
            log(f"[{mercado['market_id']}] ya operado -- se abandona", activo)
            return False

        libro = libro_publico(mercado["yes_token"])
        n_polls += 1
        py = libro.get("best_ask") if libro else None

        if py is not None and py <= UMBRAL_BAJO:
            n_no_total, resumen_edge = _n_no_total(mercado["condition_id"], activo) \
                if umbral_vol is not None else (None, None)
            if umbral_vol is not None and (n_no_total is None or n_no_total < umbral_vol):
                log(f"[{mercado['market_id']}] py={py:.3f} cruza umbral pero n_no_total="
                    f"{n_no_total} < {umbral_vol} -- vetado por volumen bajo", activo)
                time.sleep(POLL_INTERVAL_S)
                continue

            tupla_str = f"{STRATEGY}#{activo}#{MARCO}#{DIRECTION}"
            gate_bp = _gate_bucket_propio(tupla_str, py)
            if gate_bp["veredicto"] == "malo_confirmado" and tupla_str in _pares_live_hoy_set():
                log(f"[{mercado['market_id']}] py={py:.3f} vetado por gate_bucket_propio (malo_confirmado)", activo)
                return False

            prob_yes = max(0.03, py - NUDGE)
            log(f"[{mercado['market_id']}] CONFIRMADO py={py:.3f} prob_yes={prob_yes:.3f} "
                f"restante={restante:.1f}s n_no_total={n_no_total} "
                f"wallet_edge_medio={resumen_edge.get('wallet_edge_medio') if resumen_edge else None} "
                f"({n_polls} polls)", activo)
            _registrar_prediccion(activo, mercado, py, prob_yes, restante, n_no_total, resumen_edge)
            return disparar(activo, mercado, py, prob_yes, restante)

        time.sleep(POLL_INTERVAL_S)


def disparar(activo: str, mercado: dict, py: float, prob_yes: float, restante_s: float) -> bool:
    """Mismos guardias que favorito_altaconviccion_executor_15min.py::
    disparar, en el mismo orden -- este executor tampoco pasa por
    live_trade.py::main(), así que ninguno de sus guardias se aplica gratis."""
    subtype = f"{activo}#{MARCO}"

    ok_activa, motivo_activa = _activa_permite_disparo(activo)
    if not ok_activa:
        log(f"  {motivo_activa} -- {'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
        return False

    ok_operar, motivo_operar = puede_operar_live(STRATEGY, subtype)
    if not ok_operar:
        log(f"  {motivo_operar} -- {'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
        return False

    config = lt._cargar_config()
    max_misma_dir = config.get("riesgo", {}).get("max_posiciones_abiertas_misma_direccion", 2)
    abiertas_dir = lt._posiciones_abiertas_misma_direccion(DIRECTION)
    if abiertas_dir >= max_misma_dir:
        log(f"  techo de correlación: {abiertas_dir} posiciones {DIRECTION} abiertas >= {max_misma_dir} -- "
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

        # 30-Jul: veto CLV (mismo mecanismo que live_trade.py::main(), nunca
        # replicado en NINGÚN ejecutor de baja latencia -- hallazgo del
        # barrido de "cableado" de esta sesión, afecta a los 5 ejecutores
        # existentes por igual). _clv_tupla cachea a nivel de módulo
        # (pensado para un proceso fresco por ciclo, como live_trade.py
        # invocado desde run_fast.sh); este ejecutor es persistente, así
        # que se fuerza una relectura fresca de results.csv cada vez --
        # barato, solo ocurre en el momento raro de confirmar una señal,
        # nunca en cada poll de 1.5s.
        lt._CLV_CACHE = None
        clv_medio, n_clv = lt._clv_tupla(STRATEGY, subtype, DIRECTION)
        if n_clv >= lt.CLV_VETO_MIN_N and clv_medio < 0:
            log(f"  ⛔ Veto CLV: clv_medio={clv_medio:+.4f} (n={n_clv}) < 0 -- "
                f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        # edge en perspectiva de NUESTRA dirección (BUY_NO): py-prob_yes,
        # positivo cuando el modelo confía más en NO que el precio de
        # mercado -- ver CLAUDE.md ("edge_neto SIEMPRE en perspectiva YES:
        # en filas BUY_NO el edge a favor es -edge_neto").
        edge_dir = py - prob_yes
        ic_conviccion = max(0.0, edge_dir / py) if py > 0 else 0.0
        precio_entrada_no = round(1.0 - py, 6)  # ver docstring calcular_stake: "el caller
        # resuelve 1-precio_yes si es BUY_NO"
        stake_info = calcular_stake(ic_conviccion, STRATEGY, subtype, direction=DIRECTION,
                                    precio_entrada=precio_entrada_no)
        if not stake_info.get("viable"):
            log(f"  stake no viable: {stake_info.get('motivo')} -- "
                f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        if DRY_RUN:
            log(f"  [DRY-RUN] habría ejecutado {DIRECTION} {mercado['market_id']} py={py:.3f} "
                f"stake={stake_info['stake_eur']:.2f}€ restante={restante_s:.1f}s", activo)
            return True

        resultado = lt._ejecutar_orden_polymarket(
            mercado["market_id"], DIRECTION, stake_info["stake_eur"], py,
            edge_dir=edge_dir, contexto={"strategy": STRATEGY, "subtype": subtype})

        if resultado.get("no_fill"):
            log(f"  no_fill: {resultado.get('error')}", activo)
            return False

        trade = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "market_id": mercado["market_id"], "question": "", "end_date": mercado.get("end_date", ""),
            "strategy": STRATEGY, "subtype": subtype, "direction": DIRECTION,
            "stake_eur": stake_info["stake_eur"] if resultado["ok"] else 0.0,
            "entry_price": resultado["entry_price"],
            "signal_ask": round(py, 4), "slip_real": resultado.get("slip_real", ""),
            "ic_modelo": round(prob_yes, 4), "edge_neto": round(prob_yes - py, 4),
            "conviction_score": round(prob_yes, 4), "kelly_recomendado": stake_info["stake_eur"],
            "status": "OPEN" if resultado["ok"] else "ERROR",
            "close_timestamp": "", "exit_price": "", "outcome_real": "",
            "fee_eur": resultado.get("fee_eur", 0), "pnl_bruto_eur": "", "pnl_neto_eur": "",
            "notas": (f"favorito_confirmado_60min_buyno_baja_latencia restante={restante_s:.1f}s"
                      if resultado.get("ok") else resultado.get("error", "")),
        }
        lt._registrar_trade(trade)
        log(f"  {'EJECUTADO' if resultado['ok'] else 'ERROR'}: {resultado}", activo)
        if resultado["ok"]:
            lt.enviar_telegram(
                f"🎯 *Orden live ejecutada (FAVORITO_CONFIRMADO {activo}#60min#BUY_NO baja latencia)*\n"
                f"Estrategia: {STRATEGY}#{subtype}#{DIRECTION}\n"
                f"Precio fill: {resultado['entry_price']:.4f} (slip {resultado.get('slip_real', 0):+.4f})\n"
                f"Stake: {stake_info['stake_eur']:.2f}$  |  restante={restante_s:.1f}s\n"
                f"Bankroll operativo: {lt.bankroll_actual():.2f}$ (real al cierre de ciclo)"
            )
        else:
            lt.enviar_telegram(
                f"❌ *Orden live ERROR (FAVORITO_CONFIRMADO {activo}#60min#BUY_NO baja latencia)*\n"
                f"{STRATEGY}#{subtype} {DIRECTION}\n{resultado.get('error', '')[:200]}"
            )
        return True


def hilo_activo(activo: str):
    log("hilo arrancado", activo)
    mercado_vigilado = None
    while True:
        try:
            mercado = resolver_mercado(activo)
            if mercado is None:
                time.sleep(REFRESCO_UNIVERSO_S)
                continue
            if mercado["market_id"] == mercado_vigilado:
                # ya se vigiló hasta el final (watch_window es bloqueante) --
                # no debería volver aquí salvo carrera con el refresco de
                # universo justo al cierre; esperar a que ruede al siguiente.
                time.sleep(5)
                continue
            mercado_vigilado = mercado["market_id"]
            watch_window(activo, mercado)
        except Exception as e:
            log(f"error en hilo: {e} -- reintenta en 5s", activo)
            time.sleep(5)


def main():
    log(f"favorito_confirmado_btc60min_buyno_executor arrancado (DRY_RUN={DRY_RUN}, activos={list(ACTIVOS)})")
    _fc.iniciar()
    # Deja el cache calentar un momento antes de empezar a vigilar --
    # esta_sano() exige un mensaje reciente, y con miles de trades/min en
    # el firehose esto tarda segundos, no minutos.
    time.sleep(3)
    if not DRY_RUN:
        _ = lt._get_clob_client()
        log("ClobClient precalentado")

    hilos = [threading.Thread(target=hilo_activo, args=(activo,), daemon=True, name=activo)
             for activo in ACTIVOS]
    for h in hilos:
        h.start()

    ciclos_firehose_no_sano = 0
    while True:
        time.sleep(30)
        for i, h in enumerate(hilos):
            if not h.is_alive():
                activo = h.name
                log("hilo murió inesperadamente -- reiniciando", activo)
                nuevo = threading.Thread(target=hilo_activo, args=(activo,), daemon=True, name=activo)
                nuevo.start()
                hilos[i] = nuevo

        if _fc.esta_sano():
            ciclos_firehose_no_sano = 0
        else:
            ciclos_firehose_no_sano += 1
            if ciclos_firehose_no_sano >= 4:
                log(f"⚠️ cache de firehose lleva ~{ciclos_firehose_no_sano * 30}s no sano -- "
                    f"revisar conexión RTDS/logs, el ejecutor no puede confirmar señales así")


if __name__ == "__main__":
    main()
