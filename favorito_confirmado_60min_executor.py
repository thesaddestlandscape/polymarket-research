#!/usr/bin/env python3
"""
favorito_confirmado_60min_executor.py — Ejecutor de baja latencia para
FAVORITO_CONFIRMADO#{BTC,SOL}#60min#BUY_YES.

Origen (04-Ago, petición explícita Javi, "construye los ejecutores para
las 4 pausadas"): estas 2 tuplas se PAUSARON 28-Jul -- el ÚNICO drenaje
concluyente del live hasta esa fecha (`_pares_favorito60min_buyyes_pausa_
nota_2026-07-28`): combinado n=31 PnL/trade=-0.276€ IC90%=[-0.539,-0.012]
no cruza cero, -8.57€ total, persistente en ambas mitades. Causa
documentada entonces: los 31 trades reales entraron TODOS con 29-66min
restantes, donde "favorito confirmado" no confirma nada de verdad (hit
41-50% vs breakeven 58-60%). El barrido de latencia definitivo del 03-Ago
(`project_barrido_definitivo_latencia_17_combos_03ago`) encontró que AMBAS
tuplas muestran también la firma de latencia (BTC +50.5s/23.4% perdido,
SOL +48.0s/41.4% perdido) -- hipótesis a probar: parte del problema podría
ser que las señales que SÍ se llenan son precisamente las tardías/mal
temporizadas (selección adversa por latencia amplificando el problema de
timing ya documentado), no que el mecanismo sea inservible en cualquier
timing. Este ejecutor construye la infraestructura para medir con datos
de baja latencia REALES si vigilar desde el principio de la ventana (en
vez de solo cuando el pipeline lento por fin llega) cambia la distribución
de timing de entrada -- NO es una reactivación, es DRY_RUN puro.

Mismo patrón EXACTO que favorito_confirmado_btc60min_buyno_executor.py
(no reinventar), pero para BUY_YES en vez de BUY_NO y generalizado a 2
activos (BTC, SOL). Diferencia clave frente a los ejecutores de 15min: los
mercados "hourly" (60min) NO tienen slug determinista resoluble -- se
resuelve reusando `_universo_activo()` de fetch_libro_ambos_lados.py (ya
en producción, clasifica por TEXTO de la pregunta, no por slug).

Replica la rama BUY_YES exacta de s_favorito_confirmado (shadow_predict.py):
FAVORITO_CONFIRMADO_UMBRAL=0.55, sin techo, gate de volumen real
GATE_VOLUMEN_VALIDADO (BTC/SOL#60min#BUY_YES: 35, ambos ya validados: BTC
n=185 hit=92.5%, SOL n=195 hit=88.3%), gate_bucket_propio (veta si
malo_confirmado Y la tupla exacta está en pares_permitidos_live -- hoy NO
lo está, solo loguea), banda_fina_ballenas (solo observacional).

⚠️ DRY_RUN=True por defecto -- OBLIGATORIO, y AQUÍ TIENE UNA SEGUNDA CAPA
DE PROTECCIÓN: ninguna de las 2 tuplas está en pares_permitidos_live hoy
(a diferencia de favbtc60mno, que protege una tupla YA live) --
`puede_operar_live()` las bloquearía SIEMPRE por whitelist, con o sin
DRY_RUN. Cambiar DRY_RUN a False no bastaría para mover dinero real: haría
falta ADEMÁS re-promocionar la tupla, decisión separada y explícita de
Javi con gate riguroso re-verificado -- especialmente aquí, donde el
motivo de pausa original (timing, no solo latencia) sigue sin refutar.

Corre en screen propia:
  screen -dmS fav60mexec bash -c "cd /root/polymarket-research && .venv/bin/python favorito_confirmado_60min_executor.py >> logs/favorito_confirmado_60min_executor.log 2>&1"
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
DIRECTION = "BUY_YES"
MARCO = "60min"
ACTIVOS = ("BTC", "SOL")

DRY_RUN = True  # 04-Ago v1 -- ver docstring, NO cambiar sin revisión + aprobación explícita.
# Además: ninguna de las 2 tuplas está en pares_permitidos_live hoy, así
# que puede_operar_live() bloquearía igual aunque DRY_RUN pasara a False
# por error -- doble protección, no confiar solo en esta variable.

POLL_INTERVAL_S = 1.5
HARD_FLOOR_S = 3.0
REFRESCO_UNIVERSO_S = 30.0  # cadencia para volver a leer data/markets/HOY.csv
# cuando aún no hay mercado resuelto -- barato, el CSV lo mantiene
# capture_markets.py (run_slow.sh), no red nueva.

# Mismos valores exactos que shadow_predict.py (FAVORITO_CONFIRMADO_UMBRAL /
# _NUDGE) -- duplicados aquí, mismo criterio que el resto de ejecutores de
# baja latencia. Si cambian allí, replicar aquí a mano.
UMBRAL = 0.55
NUDGE = 0.06

# Mismo gate real que GATE_VOLUMEN_VALIDADO en shadow_predict.py -- ambos
# ya validados: BTC n=185 alto=133 hit=92.5% +0.950€ GATE OK, SOL n=195
# alto=145 hit=88.3% +0.667€ GATE OK.
GATE_VOLUMEN_VALIDADO = {
    ("BTC", "60min", "BUY_YES"): 35,
    ("SOL", "60min", "BUY_YES"): 35,
}

_session = requests.Session()
_orden_lock = threading.Lock()
_pares_live_cache = {"mtime": None, "set": set()}
_tokens_cache: dict[str, tuple[str, str]] = {}  # market_id -> (yes_token, no_token)


def log(msg: str, activo: str = ""):
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
    """{activo}#60min activo con edt más próximo -- mismo patrón que
    favorito_confirmado_btc60min_buyno_executor.py::resolver_mercado_btc60min,
    generalizado a cualquier activo."""
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


def _n_yes_total(condition_id: str, activo: str) -> tuple[int | None, dict | None]:
    """Compras YES en TODO el mercado, vía ballenas_firehose_cache (NO la
    API rota) -- más un resumen de wallet_edge_score PURAMENTE
    observacional. Devuelve (n_yes_total, resumen_edge)."""
    if not _fc.esta_sano():
        return None, None
    trades = _fc.trades_de_mercado_firehose(condition_id)
    n_yes_total = sum(1 for t in trades if (t.get("side") or "").strip().upper() == "BUY"
                       and (t.get("outcome") or "").strip().lower() in ("up", "yes"))

    db = _cargar_wallet_edge_activo_marco()
    wallets_yes = {(t.get("proxyWallet") or "").lower() for t in trades
                   if (t.get("side") or "").strip().upper() == "BUY"
                   and (t.get("outcome") or "").strip().lower() in ("up", "yes")}
    filas = [db[(w, activo, "60m")] for w in wallets_yes if (w, activo, "60m") in db]
    edges = [f["edge_pp"] for f in filas]
    resumen_edge = {
        "wallet_edge_medio": round(sum(edges) / len(edges), 3) if edges else None,
        "wallet_n_con_score": len(edges),
        "wallet_n_sig_pos": sum(1 for f in filas if f["sig_bhfdr"] and f["edge_pp"] > 0),
        "wallet_n_sig_neg": sum(1 for f in filas if f["sig_bhfdr"] and f["edge_pp"] < 0),
    }
    return n_yes_total, resumen_edge


def _activa_permite_disparo(activo: str) -> tuple[bool, str]:
    """Mismo mecanismo de autoconciencia que el resto de ejecutores de baja
    latencia."""
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
        campo = "activa_BUY_YES" if "activa_BUY_YES" in e else "activa"
        if not e.get(campo, True):
            return False, f"postmortem desactivó {k} ({campo}=False)"
    return True, "activa"


def _registrar_prediccion(activo: str, mercado: dict, py: float, prob_yes: float,
                           restante_s: float, n_yes_total: int | None,
                           resumen_edge: dict | None = None) -> None:
    """Mismo formato que shadow_predict.py -- shadow_resolve.py/
    shadow_postmortem.py lo resuelven y aprenden de él sin duplicar esa
    lógica aquí."""
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    archivo = DIR_SHADOW / f"predictions_{ts[:10]}.csv"
    subtype = f"{activo}#{MARCO}"
    edge = prob_yes - py
    gate_bf = _gate_banda_fina_ballenas(activo, MARCO, py, restante_s / 60.0)
    features = json.dumps({
        "py_entrada": round(py, 4), "n_total_lado": n_yes_total,
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
        log(f"aviso: no se pudo registrar predicción para postmortem: {e}", activo)


def watch_window(activo: str, mercado: dict) -> bool:
    """Vigila un mercado {activo}#60min concreto hasta su cierre. True si
    ejecutó (o habría ejecutado en DRY_RUN)."""
    try:
        end_dt = datetime.fromisoformat(mercado["end_date"])
    except Exception:
        log(f"end_date ilegible: {mercado.get('end_date')} -- se abandona", activo)
        return False
    ts_end = end_dt.timestamp()
    umbral_vol = GATE_VOLUMEN_VALIDADO.get((activo, MARCO, "BUY_YES"))
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

        if py is not None and py >= UMBRAL:
            n_yes_total, resumen_edge = _n_yes_total(mercado["condition_id"], activo) \
                if umbral_vol is not None else (None, None)
            if umbral_vol is not None and (n_yes_total is None or n_yes_total < umbral_vol):
                log(f"[{mercado['market_id']}] py={py:.3f} cruza umbral pero n_yes_total="
                    f"{n_yes_total} < {umbral_vol} -- vetado por volumen bajo", activo)
                time.sleep(POLL_INTERVAL_S)
                continue

            tupla_str = f"{STRATEGY}#{activo}#{MARCO}#{DIRECTION}"
            gate_bp = _gate_bucket_propio(tupla_str, py)
            if gate_bp["veredicto"] == "malo_confirmado" and tupla_str in _pares_live_hoy_set():
                log(f"[{mercado['market_id']}] py={py:.3f} vetado por gate_bucket_propio (malo_confirmado)", activo)
                return False

            prob_yes = min(0.97, py + NUDGE)
            log(f"[{mercado['market_id']}] CONFIRMADO py={py:.3f} prob_yes={prob_yes:.3f} "
                f"restante={restante:.1f}s n_yes_total={n_yes_total} "
                f"wallet_edge_medio={resumen_edge.get('wallet_edge_medio') if resumen_edge else None} "
                f"({n_polls} polls)", activo)
            _registrar_prediccion(activo, mercado, py, prob_yes, restante, n_yes_total, resumen_edge)
            return disparar(activo, mercado, py, prob_yes, restante)

        time.sleep(POLL_INTERVAL_S)


def disparar(activo: str, mercado: dict, py: float, prob_yes: float, restante_s: float) -> bool:
    """Mismos guardias que el resto de ejecutores de baja latencia, en el
    mismo orden -- puede_operar_live() bloqueará SIEMPRE aquí (tupla no
    está en pares_permitidos_live) -- ver nota de doble protección en el
    docstring del módulo."""
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

        lt._CLV_CACHE = None
        clv_medio, n_clv = lt._clv_tupla(STRATEGY, subtype, DIRECTION)
        if n_clv >= lt.CLV_VETO_MIN_N and clv_medio < 0:
            log(f"  ⛔ Veto CLV: clv_medio={clv_medio:+.4f} (n={n_clv}) < 0 -- "
                f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        ic_conviccion = max(0.0, (prob_yes - py) / (1 - py)) if py < 1 else 0.0
        stake_info = calcular_stake(ic_conviccion, STRATEGY, subtype, direction=DIRECTION)
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
            edge_dir=prob_yes - py, contexto={"strategy": STRATEGY, "subtype": subtype})

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
            "notas": (f"favorito_confirmado_60min_baja_latencia restante={restante_s:.1f}s"
                      if resultado.get("ok") else resultado.get("error", "")),
        }
        lt._registrar_trade(trade)
        log(f"  {'EJECUTADO' if resultado['ok'] else 'ERROR'}: {resultado}", activo)
        if resultado["ok"]:
            lt.enviar_telegram(
                f"🎯 *Orden live ejecutada (FAVORITO_CONFIRMADO 60min baja latencia)*\n"
                f"Estrategia: {STRATEGY}#{subtype}#{DIRECTION}\n"
                f"Precio fill: {resultado['entry_price']:.4f} (slip {resultado.get('slip_real', 0):+.4f})\n"
                f"Stake: {stake_info['stake_eur']:.2f}$  |  restante={restante_s:.1f}s\n"
                f"Bankroll operativo: {lt.bankroll_actual():.2f}$ (real al cierre de ciclo)"
            )
        else:
            lt.enviar_telegram(
                f"❌ *Orden live ERROR (FAVORITO_CONFIRMADO 60min baja latencia)*\n"
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
    log(f"favorito_confirmado_60min_executor arrancado (DRY_RUN={DRY_RUN}, activos={list(ACTIVOS)})")
    _fc.iniciar()
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
