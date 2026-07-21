#!/usr/bin/env python3
"""
ballenas_executor_5min.py — Ejecutor de baja latencia multi-activo para
BALLENAS_TARDIAS#{ETH,SOL,XRP,DOGE}#5min#BUY_YES.

Origen (18-Jul): tras corregir el gate _solo_late que bloqueaba
GBM_LATE_5M desde su nacimiento (commit 820422edff), se corrió el mismo
análisis riguroso que aprobó BALLENAS_TARDIAS#BTC#15min —
analisis_ballenas_5min_fillability_retro_18jul.py (profundidad real,
0% mercados <5x stake) + analisis_ballenas_dosis_respuesta_16jul.py
(dosis-respuesta n=195, bucket concentracion>=0.9: ETH n=57 hit=100%
Wilson=[93.7,100]%, SOL n=52 hit=100% Wilson=[93.1,100]%, XRP n=49
hit=93.9% Wilson=[83.5,97.9]%). Los 3 superan el precedente que aprobó
BTC#15min (98.5% n=48). BTC#5m queda FUERA (n=14, ventana casi
degenerada ~0s) — mismo motivo que excluye BTC#15m de
veto_ballenas.combos_validados, Javi lo trata aparte.

DOGE añadido 20-Jul tras arreglar la exclusión de NOMBRE_A_TICKER
(smart_money_tracker.py, commit 6450288420) — significativo en el primer
ciclo de ballenas_observer.py, pero con n=9 en la dosis-respuesta propia
(ver ACTIVOS abajo) — MUCHO más flojo que los otros 3. Se añade solo para
que DRY_RUN acumule su propia confirmación en tiempo real, no porque ya
esté validado al mismo nivel.

Diseño: UN proceso, 3 hilos (uno por activo) en vez de 3 procesos —
coordinar el ritmo de sondeo contra data-api.polymarket.com/trades (sin
backoff/rate-limit propio, ver smart_money_tracker.trades_de_mercado) es
mucho más fácil dentro de un proceso. POLL_INTERVAL_S=1.5 (no 1.0 como
BTC15m) por el mismo motivo: 3 hilos concurrentes + los picos que
coinciden con el ciclo de BTC15m. Un threading.Lock() serializa el tramo
de ejecución real (disparar) porque ORDEN_EN_CURSO_PATH (live_trade.py)
es un marcador global sin clave por activo — sin este lock, dos hilos
confirmando casi a la vez podrían pisarse ese fichero.

Screen propia `ballenas_5m` (NO reutiliza `ballenas_fast`, que ya opera
BTC15m con dinero real — un bug en este código nuevo no debe poder
tumbar ese proceso).

DRY_RUN=True fijo en esta fase: loguea qué habría hecho, nunca llama a
_ejecutar_orden_polymarket. Las 3 tuplas NO están en pares_permitidos_live
todavía -- puede_operar_live() reportará honestamente "no está en
whitelist", visibilidad completa sin tocar el gate de dinero real. Pasar
a DRY_RUN=False requiere: código en pares_permitidos_live, /code-review y
aprobación explícita de Javi (mismo patrón en dos fases que BTC15m).

Corre en screen propia:
  screen -dmS ballenas_5m bash -c "cd /root/polymarket-research && .venv/bin/python ballenas_executor_5min.py >> logs/ballenas_5m.log 2>&1"
"""
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import requests

import live_trade as lt
from live_guard import puede_operar_live
from live_stake import calcular_stake, verificar_circuit_breaker
from smart_money_tracker import trades_de_mercado

DIR = Path(__file__).resolve().parent
DIR_SHADOW = DIR / "data" / "shadow"

# Wallet edge score por marco (20-Jul, wallet_edge_tracker.py) -- PURAMENTE
# INFORMATIVO en texto de log, no toca pct_yes/CONCENTRACION_MIN/decisión.
# Mismo hallazgo que motivó el cableado gemelo en shadow_predict.py
# (s_ballenas_confirmadas_15m): "smart" (leaderboard) no es lo mismo que
# "informativo para Up/Down 5min" -- este campo deja constancia en el log
# DRY_RUN de qué wallets concretas confirmaron cada señal, para poder
# auditar después si las que más pasta generan de verdad (edge_pp alto,
# marco=5m) son las que están detrás de las confirmaciones reales.
WALLET_EDGE_POR_MARCO = DIR_SHADOW / "wallet_edge_score_por_marco.json"
_wallet_edge_cache = {"mtime": None, "data": {}}


def _cargar_wallet_edge_5m():
    try:
        mtime = WALLET_EDGE_POR_MARCO.stat().st_mtime
    except OSError:
        return {}
    if _wallet_edge_cache["mtime"] != mtime:
        try:
            todo = json.loads(WALLET_EDGE_POR_MARCO.read_text(encoding="utf-8"))
            _wallet_edge_cache["data"] = {v["wallet"]: v for v in todo.values() if v.get("marco") == "5m"}
        except Exception:
            _wallet_edge_cache["data"] = {}
        _wallet_edge_cache["mtime"] = mtime
    return _wallet_edge_cache["data"]

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"

STRATEGY = "BALLENAS_TARDIAS"
VENTANA_MIN = 5

DRY_RUN = True  # Fase 1 (18-Jul) -- ver docstring, no cambiar sin aprobación Javi + /code-review

POLL_INTERVAL_S = 1.5    # más conservador que BTC15m (1.0) -- 3 hilos concurrentes
HARD_FLOOR_S = 3.0       # uniforme, mismo suelo de seguridad que BTC15m
CONCENTRACION_MIN = 0.9  # bucket validado hoy para los 3 activos (dosis-respuesta n=195)
MIN_TRADES_BALLENA = 3

# Por activo: WATCH_LEAD_S = rest_hi_min calibrado (ballenas_timing_state.json,
# sesión 18-Jul) + ~30s margen. PROB_BUCKET = Wilson 95% inferior del bucket
# concentracion>=0.9 (no el punto estimado 100% -- mal calibrado, mismo
# espíritu que la nota de ic_conviccion en ballenas_executor_btc15m.py).
ACTIVOS = {
    "ETH": {"watch_lead_s": 90,  "prob_bucket": 0.93},
    "SOL": {"watch_lead_s": 160, "prob_bucket": 0.93},
    "XRP": {"watch_lead_s": 220, "prob_bucket": 0.83},
    # DOGE (20-Jul): NOMBRE_A_TICKER llevaba excluyendo DOGE de todo el
    # pipeline de ballenas desde su origen (fix en smart_money_tracker.py,
    # commit 6450288420) -- tras el fix, DOGE#5m salió "significativo" en
    # el primer ciclo de ballenas_observer.py (banda [0.7,0.9), z=3.67,
    # n=133, 58 wallets, top1_share=0.17 -- bien repartido). PERO la
    # dosis-respuesta propia (analisis_ballenas_dosis_respuesta_16jul.py
    # DOGE#5m) da n=9 en el bucket concentracion>=0.9 -- muy por debajo
    # de ETH/SOL/XRP cuando se calibraron (n=48-57) y del propio umbral
    # n>=15 del proyecto para concluir nada. prob_bucket aquí es el
    # Wilson90 inferior de 9/9 (0.769), NO un número con la misma
    # confianza que los otros 3 -- solo para que DRY_RUN loguee algo
    # razonable mientras acumula. Recalibrar en cuanto n cruce ~40.
    "DOGE": {"watch_lead_s": 170, "prob_bucket": 0.77},
}

_session = requests.Session()
_orden_lock = threading.Lock()  # serializa el tramo de ejecución real entre los 3 hilos


def log(msg: str, activo: str = ""):
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    prefijo = f"[{activo}] " if activo else ""
    print(f"[{ts}] {prefijo}{msg}", flush=True)


def resolver_mercado(activo: str, ts_start: int) -> dict | None:
    """Una sola llamada gamma-api por ventana de 5min -- mismo patrón
    determinista que ballenas_executor_btc15m.resolver_mercado."""
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
            "yes_token": tokens[0],
            "no_token": tokens[1],
            "end_date": mkt.get("endDate", ""),
        }
    except Exception as e:
        log(f"resolver_mercado error: {e}", activo)
        return None


def libro_publico(token_id: str) -> dict | None:
    """Lectura pública del libro (sin auth), mismo endpoint que
    ballenas_executor_btc15m.libro_publico."""
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


def concentracion_ballenas(condition_id: str, banda_lo: float, banda_hi: float) -> tuple[float | None, int, str, list]:
    """(pct_yes, n, motivo, wallets_yes) -- idéntico a
    ballenas_executor_btc15m.concentracion_ballenas, mide ambos lados porque
    la dirección todavía no está fijada. wallets_yes (nuevo 20-Jul) son las
    wallets del lado YES, guardadas SOLO para logging informativo del
    wallet-edge-score -- no participan en pct_yes ni en ninguna decisión."""
    try:
        trades = trades_de_mercado(condition_id)
    except Exception:
        return None, 0, "error_api", []
    n_yes = n_no = 0
    wallets_yes = []
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
        if outcome_t in ("up", "yes"):
            n_yes += 1
            w = (t.get("proxyWallet") or "").lower()
            if w:
                wallets_yes.append(w)
        else:
            n_no += 1
    n = n_yes + n_no
    if n == 0:
        return None, 0, "sin_trades_en_banda", []
    return n_yes / n, n, "ok", wallets_yes


def _resumen_wallet_edge(wallets: list) -> str:
    """Texto corto para el log: cuántas de las wallets confirmando tienen
    score conocido, su edge medio, y cuántas son negativas-significativas
    (mismo criterio 20-Jul que shadow_predict.s_ballenas_confirmadas_15m).
    Puramente informativo."""
    db = _cargar_wallet_edge_5m()
    edges = [db[w]["edge_pp"] for w in wallets if w in db]
    n_sig_neg = sum(1 for w in wallets if w in db and db[w]["sig_bhfdr"] and db[w]["edge_pp"] < 0)
    if not edges:
        return "wallet_edge=sin_dato"
    medio = sum(edges) / len(edges)
    return f"wallet_edge_medio={medio:+.2f}pp(n_con_score={len(edges)},n_sig_neg={n_sig_neg})"


def cargar_banda(activo: str) -> tuple[float, float] | None:
    """Banda de precio calibrada por ballenas_observer.py -- leída fresca
    cada ventana, nunca hardcodeada (puede moverse si el observer
    recalibra). Igual que ballenas_executor_btc15m.cargar_banda_btc15m,
    generalizada por activo."""
    try:
        estado = json.loads((DIR_SHADOW / "ballenas_timing_state.json").read_text())
    except Exception:
        return None
    e = estado.get(f"{activo}#{VENTANA_MIN}m", {})
    if not e.get("significativo"):
        return None
    lo, hi = e.get("banda_lo"), e.get("banda_hi")
    if not (isinstance(lo, (int, float)) and isinstance(hi, (int, float))):
        return None
    return lo, hi


def watch_window(activo: str, ts_end: int) -> bool:
    """Vigila un mercado {activo}#5min concreto desde watch_lead_s hasta
    el cierre. True si ejecutó (o habría ejecutado en DRY_RUN)."""
    cfg = ACTIVOS[activo]
    watch_lead_s = cfg["watch_lead_s"]
    ts_start = ts_end - VENTANA_MIN * 60
    banda = cargar_banda(activo)
    if banda is None:
        log(f"[{ts_end}] {activo}#5m no significativo en ballenas_timing_state.json -- se salta", activo)
        return False
    banda_lo, banda_hi = banda

    mercado = None
    contadores = {"ok": 0, "sin_trades_en_banda": 0, "error_api": 0}
    while True:
        restante = ts_end - time.time()
        if restante > watch_lead_s:
            time.sleep(min(restante - watch_lead_s, 5))
            continue
        if restante < HARD_FLOOR_S:
            log(f"[{ts_end}] suelo de seguridad ({HARD_FLOOR_S}s) alcanzado sin confirmación -- se abandona "
                f"(resumen vigilancia: {sum(contadores.values())} polls, "
                f"ok={contadores['ok']} sin_trades_en_banda={contadores['sin_trades_en_banda']} "
                f"error_api={contadores['error_api']})", activo)
            return False

        if mercado is None:
            mercado = resolver_mercado(activo, ts_start)
            if mercado is None:
                log(f"[{ts_end}] no se pudo resolver el mercado -- se abandona", activo)
                return False
            if mercado["market_id"] in lt._ya_operados_hoy():
                log(f"[{ts_end}] {mercado['market_id']} ya operado -- se salta", activo)
                return False

        with ThreadPoolExecutor(max_workers=2) as ex:
            f_conc = ex.submit(concentracion_ballenas, mercado["condition_id"], banda_lo, banda_hi)
            f_libro = ex.submit(libro_publico, mercado["yes_token"])
            pct_yes, n, motivo_conc, wallets_yes = f_conc.result()
            libro = f_libro.result()

        contadores[motivo_conc] = contadores.get(motivo_conc, 0) + 1
        if pct_yes is not None:
            log(f"[{ts_end}] restante={restante:.1f}s concentracion_yes={pct_yes:.2f} n={n} "
                f"ask={libro.get('best_ask') if libro else None}", activo)
        elif motivo_conc == "error_api":
            log(f"[{ts_end}] restante={restante:.1f}s ⚠️ error_api consultando ballenas -- sin dato este ciclo", activo)

        if (pct_yes is not None and n >= MIN_TRADES_BALLENA
                and pct_yes >= CONCENTRACION_MIN
                and libro and libro.get("best_ask") is not None
                and banda_lo <= libro["best_ask"] < banda_hi):
            py = libro["best_ask"]
            edge = cfg["prob_bucket"] - py
            log(f"[{ts_end}] CONFIRMADO concentracion={pct_yes:.2f} n={n} py={py:.3f} "
                f"edge={edge:+.3f} restante={restante:.1f}s {_resumen_wallet_edge(wallets_yes)}", activo)
            _registrar_tracker(activo, mercado, py, edge, pct_yes, n, restante)
            return disparar(activo, mercado, py, edge, restante)

        time.sleep(POLL_INTERVAL_S)


TRACKER_PATH = DIR_SHADOW / "ballenas_5min_dry_run.csv"
_tracker_lock = threading.Lock()


def _registrar_tracker(activo: str, mercado: dict, py: float, edge: float,
                        concentracion: float, n_ballenas: int, restante_s: float) -> None:
    """21-Jul (petición Javi, gap detectado: 3 días de CONFIRMADO sin ningún
    tracker de resultados). Persiste ANTES de disparar() a propósito -- una
    confirmación es "la señal de ballenas dijo esto" independientemente de
    si puede_operar_live() la deja pasar (switch OFF hoy bloquea el 100% de
    los disparos, ver disparar()); el tracker debe medir la señal, no el
    gate de dinero real que la envuelve. resuelve_ballenas_5min.py lee este
    CSV y rellena outcome_real/acierto vía gamma-api (mismo mecanismo que
    shadow_resolve.py) cuando el mercado ya haya cerrado."""
    nuevo = not TRACKER_PATH.exists()
    fila = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "activo": activo,
        "market_id": mercado.get("market_id", ""),
        "condition_id": mercado.get("condition_id", ""),
        "end_date": mercado.get("end_date", ""),
        "py": round(py, 4),
        "edge": round(edge, 4),
        "concentracion": round(concentracion, 4),
        "n_ballenas": n_ballenas,
        "restante_s": round(restante_s, 1),
        "outcome_real": "",
        "acierto": "",
        "resolved_ts": "",
    }
    with _tracker_lock:
        import csv as _csv
        with open(TRACKER_PATH, "a", newline="", encoding="utf-8") as f:
            w = _csv.DictWriter(f, fieldnames=list(fila.keys()))
            if nuevo:
                w.writeheader()
            w.writerow(fila)


def disparar(activo: str, mercado: dict, py: float, edge: float, restante_s: float) -> bool:
    """Decide y (si no es DRY_RUN) ejecuta. Reutiliza circuit breaker +
    stake de live_stake.py y _ejecutar_orden_polymarket de live_trade.py --
    mismo presupuesto de riesgo que el resto del sistema. Serializado con
    _orden_lock: ORDEN_EN_CURSO_PATH (live_trade.py) es un marcador global
    sin clave por activo -- con 3 hilos, dos confirmaciones casi simultáneas
    podrían pisarse ese fichero sin este lock."""
    subtype = f"{activo}#{VENTANA_MIN}min"
    cfg = ACTIVOS[activo]

    with _orden_lock:
        ok_operar, motivo_operar = puede_operar_live(STRATEGY, subtype)
        if not ok_operar:
            log(f"{motivo_operar} -- {'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        config = lt._cargar_config()
        max_misma_dir = config.get("riesgo", {}).get("max_posiciones_abiertas_misma_direccion", 2)
        abiertas_dir = lt._posiciones_abiertas_misma_direccion("BUY_YES")
        if abiertas_dir >= max_misma_dir:
            log(f"techo de correlación: {abiertas_dir} posiciones BUY_YES abiertas >= {max_misma_dir} -- "
                f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        if mercado["market_id"] in lt._ya_operados_hoy():
            log(f"{mercado['market_id']} ya operado por otro proceso/hilo -- "
                f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        ok_breaker, motivo_breaker = verificar_circuit_breaker()
        if not ok_breaker:
            log(f"circuit breaker activo ({motivo_breaker}) -- {'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        ic_conviccion = (cfg["prob_bucket"] - 0.5) * 2
        stake_info = calcular_stake(ic_conviccion, STRATEGY, subtype, direction="BUY_YES")
        if not stake_info.get("viable"):
            log(f"stake no viable: {stake_info.get('motivo')} -- {'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        if DRY_RUN:
            log(f"[DRY-RUN] habría ejecutado BUY_YES {mercado['market_id']} py={py:.3f} "
                f"edge={edge:+.3f} stake={stake_info['stake_eur']:.2f}€ restante={restante_s:.1f}s", activo)
            return True

        resultado = lt._ejecutar_orden_polymarket(
            mercado["market_id"], "BUY_YES", stake_info["stake_eur"], py,
            edge_dir=edge, contexto={"strategy": STRATEGY, "subtype": subtype})

        if resultado.get("no_fill"):
            log(f"no_fill: {resultado.get('error')}", activo)
            return False

        trade = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "market_id": mercado["market_id"],
            "question": "",
            "end_date": mercado.get("end_date", ""),
            "strategy": STRATEGY, "subtype": subtype, "direction": "BUY_YES",
            "stake_eur": stake_info["stake_eur"] if resultado["ok"] else 0.0,
            "entry_price": resultado["entry_price"],
            "ic_modelo": round(cfg["prob_bucket"], 4),
            "edge_neto": round(edge, 4),
            "conviction_score": round(cfg["prob_bucket"], 4),
            "kelly_recomendado": stake_info["stake_eur"],
            "status": "OPEN" if resultado["ok"] else "ERROR",
            "close_timestamp": "", "exit_price": "", "outcome_real": "",
            "fee_eur": resultado.get("fee_eur", 0),
            "pnl_bruto_eur": "", "pnl_neto_eur": "",
            "notas": (f"ballenas_tardias_5min restante={restante_s:.1f}s"
                      if resultado.get("ok") else resultado.get("error", "")),
        }
        lt._registrar_trade(trade)
        log(f"{'EJECUTADO' if resultado['ok'] else 'ERROR'}: {resultado}", activo)
        return True


def hilo_activo(activo: str):
    """Bucle de vida de un activo: calcula el próximo cierre de 5min y
    vigila, en bucle infinito. Un traceback aquí no debe tumbar el
    proceso entero -- se captura y se reintenta tras un margen corto."""
    log(f"hilo arrancado (watch_lead_s={ACTIVOS[activo]['watch_lead_s']}s "
        f"prob_bucket={ACTIVOS[activo]['prob_bucket']})", activo)
    while True:
        try:
            now = time.time()
            ts_end = (int(now) // (VENTANA_MIN * 60) + 1) * (VENTANA_MIN * 60)
            dormir = ts_end - ACTIVOS[activo]["watch_lead_s"] - time.time()
            if dormir > 0:
                time.sleep(dormir)
            watch_window(activo, ts_end)
            time.sleep(max(0, ts_end + 2 - time.time()))
        except Exception as e:
            log(f"error en hilo_activo: {e} -- reintenta en 5s", activo)
            time.sleep(5)


def main():
    log(f"ballenas_executor_5min arrancado (DRY_RUN={DRY_RUN}, activos={list(ACTIVOS)})")
    if not DRY_RUN:
        # Precalienta el import pesado UNA vez desde el hilo principal, antes
        # de lanzar los 3 hilos -- evita que dos hilos llamen
        # _get_clob_client() a la vez en el arranque y re-apliquen el
        # monkeypatch de _parchear_redondeo_clob() concurrentemente (benigno
        # pero evitable).
        _ = lt._get_clob_client()
        log("ClobClient precalentado")

    hilos = [threading.Thread(target=hilo_activo, args=(activo,), daemon=True, name=activo)
             for activo in ACTIVOS]
    for h in hilos:
        h.start()

    # Hilo principal: supervivencia -- si un hilo muere (no debería, hilo_activo
    # captura sus propias excepciones), lo reinicia sin tumbar el proceso.
    while True:
        time.sleep(30)
        for i, h in enumerate(hilos):
            if not h.is_alive():
                activo = h.name
                log(f"hilo murió inesperadamente -- reiniciando", activo)
                nuevo = threading.Thread(target=hilo_activo, args=(activo,), daemon=True, name=activo)
                nuevo.start()
                hilos[i] = nuevo


if __name__ == "__main__":
    main()
