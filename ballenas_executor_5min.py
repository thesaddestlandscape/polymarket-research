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

# Wallet edge score por (activo,marco) -- 23-Jul, sustituye al de solo-marco
# (20-Jul). Hallazgo de la sesión de franja milimétrica: concentracion_
# ballenas() cuenta VOTOS POR TRADE, no por calidad de wallet -- cualquier
# día una wallet muy activa (buena o mediocre) puede dominar el consenso
# (top1_share hasta 35% visto en XRP) sin que el sistema lo distinga. Ahora
# SÍ se distingue: cada trade pesa según el edge_pp validado (shuffle+BH-FDR,
# wallet_edge_tracker.py) de esa wallet en ESE (activo,marco) exacto -- no
# el score mezclado de las 5 monedas que daba wallet_edge_score_por_marco.json
# (ese archivo servía de único origen hasta hoy y por eso el peso solo podía
# ser informativo, nunca decisión: mezclaba, p.ej., el comportamiento de una
# wallet en BTC#5m con su comportamiento en XRP#5m bajo el mismo número).
# Wallets desconocidas o sin significancia (sig_bhfdr=False) pesan 1.0 --
# fail-safe idéntico al conteo plano de siempre. Solo wallets VALIDADAS
# (n>=15, shuffle+BH-FDR) se alejan de 1.0, acotado [0.2, 3.0] para que
# ninguna wallet sola pueda dominar el voto ponderado.
WALLET_EDGE_POR_ACTIVO_MARCO = DIR_SHADOW / "wallet_edge_score_por_activo_marco.json"
PESO_MIN, PESO_MAX = 0.2, 3.0
_wallet_edge_cache = {"mtime": None, "data": {}}


def _cargar_wallet_edge_activo_marco():
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
    return _wallet_edge_cache["data"]


def _peso_wallet(wallet: str, activo: str) -> float:
    """1.0 (neutro) salvo wallet validada (n>=15, sig_bhfdr=True) en este
    (activo, 5m) exacto -- entonces escala con su edge_pp, acotado
    [PESO_MIN, PESO_MAX]. +25pp de edge -> peso 2.0; -25pp -> peso 0.5;
    nunca 0 (ninguna wallet se censura del todo con la n que tenemos hoy)."""
    db = _cargar_wallet_edge_activo_marco()
    d = db.get((wallet, activo, "5m"))
    if d is None or not d.get("sig_bhfdr"):
        return 1.0
    peso = 1.0 + d["edge_pp"] / 25.0
    return max(PESO_MIN, min(PESO_MAX, peso))

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"

STRATEGY = "BALLENAS_TARDIAS"
VENTANA_MIN = 5

DRY_RUN = True  # Fase 1 (18-Jul) -- ver docstring, no cambiar sin aprobación Javi + /code-review

POLL_INTERVAL_S = 1.5    # más conservador que BTC15m (1.0) -- 3 hilos concurrentes
HARD_FLOOR_S = 3.0       # uniforme, mismo suelo de seguridad que BTC15m
CONCENTRACION_MIN = 0.9  # bucket validado hoy para los 3 activos (dosis-respuesta n=195)
MIN_TRADES_BALLENA = 3

ACTIVOS = ("ETH", "SOL", "XRP", "DOGE")

# 23-Jul: MARGEN_WATCH_S/MARGEN_CONFIRM_S sustituyen a los watch_lead_s/
# prob_bucket hardcodeados por activo del 18-Jul (ETH=90s/0.93, SOL=160s/
# 0.93, XRP=220s/0.83, DOGE=170s/0.77). Bug de calibración estale
# encontrado en la sesión de franja milimétrica: cargar_banda() releía la
# banda de precio fresca cada ventana, pero prob_bucket/watch_lead_s se
# quedaron congelados en su valor del día de calibración -- cuando el
# observer recalibró la banda operativa de XRP de [0.70,0.90) (hit~94%,
# 18-Jul) a [0.50,0.70) (hit=60.9%, 23-Jul), prob_bucket siguió en 0.83,
# un 22pp de sobreconfianza silenciosa (sin dinero real en juego, DRY_RUN,
# pero el log llevaba horas con un "edge" que no correspondía a nada).
# Ahora cargar_calibracion() recalcula TODO fresco cada ventana desde
# ballenas_timing_state.json (misma fuente que cargar_banda() usaba antes),
# igual que el resto del sistema: banda_lo/hi, prob_bucket (Wilson 95%
# inferior de n/n_ganadoras REAL de la banda operativa actual, no un
# bucket congelado), y el techo de confirmación (ver MARGEN_CONFIRM_S).
MARGEN_WATCH_S = 60      # cuánto antes del techo de confirmación empieza a vigilar (margen para no perderse el arranque de la ventana informativa)
MARGEN_CONFIRM_S = 15    # margen sobre rest_hi_min real antes de permitir confirmar -- ver MARGEN_CONFIRM_S y el hallazgo de desalineación de timing (abajo)

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


def concentracion_ballenas(condition_id: str, banda_lo: float, banda_hi: float,
                            activo: str) -> tuple[float | None, float | None, int, str, list]:
    """(pct_yes_crudo, pct_yes_ponderado, n, motivo, wallets_yes) -- mide
    ambos lados porque la dirección todavía no está fijada.

    23-Jul: se añade pct_yes_ponderado -- cada trade pesa según
    _peso_wallet() (1.0 si la wallet es desconocida o no validada, fuera de
    1.0 solo si tiene edge_pp significativo en ESTE activo#5m). n sigue
    siendo el conteo CRUDO de trades (gate MIN_TRADES_BALLENA no cambia --
    3 trades reales, ponderados o no, siguen siendo el suelo de datos
    mínimo). pct_yes_crudo se conserva para compararlo en el log/tracker
    con el ponderado y poder auditar cuándo divergen."""
    try:
        trades = trades_de_mercado(condition_id)
    except Exception:
        return None, None, 0, "error_api", []
    n_yes = n_no = 0
    peso_yes = peso_no = 0.0
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
        w = (t.get("proxyWallet") or "").lower()
        peso = _peso_wallet(w, activo) if w else 1.0
        if outcome_t in ("up", "yes"):
            n_yes += 1
            peso_yes += peso
            if w:
                wallets_yes.append(w)
        else:
            n_no += 1
            peso_no += peso
    n = n_yes + n_no
    if n == 0:
        return None, None, 0, "sin_trades_en_banda", []
    pct_crudo = n_yes / n
    pct_ponderado = peso_yes / (peso_yes + peso_no) if (peso_yes + peso_no) > 0 else pct_crudo
    return pct_crudo, pct_ponderado, n, "ok", wallets_yes


def _resumen_wallet_edge(wallets: list, activo: str) -> str:
    """Texto corto para el log: cuántas de las wallets confirmando tienen
    score conocido, su edge medio, y cuántas son negativas-significativas
    en este (activo,5m) -- ahora también informa si su peso ya afectó a la
    decisión (antes de 23-Jul esto era solo informativo)."""
    db = _cargar_wallet_edge_activo_marco()
    filas = [db[(w, activo, "5m")] for w in wallets if (w, activo, "5m") in db]
    edges = [f["edge_pp"] for f in filas]
    n_sig_neg = sum(1 for f in filas if f["sig_bhfdr"] and f["edge_pp"] < 0)
    n_sig_pos = sum(1 for f in filas if f["sig_bhfdr"] and f["edge_pp"] > 0)
    if not edges:
        return "wallet_edge=sin_dato"
    medio = sum(edges) / len(edges)
    return f"wallet_edge_medio={medio:+.2f}pp(n_con_score={len(edges)},n_sig_pos={n_sig_pos},n_sig_neg={n_sig_neg})"


def _wilson_lower(aciertos: int, n: int, z: float = 1.96) -> float:
    """Límite inferior del IC de Wilson al 95% -- mismo criterio ("no el
    punto estimado, el límite inferior") que ya usaba la nota original de
    PROB_BUCKET, ahora calculado en vivo en vez de a mano una sola vez."""
    if n <= 0:
        return 0.0
    phat = aciertos / n
    denom = 1 + z * z / n
    centro = phat + z * z / (2 * n)
    ajuste = z * ((phat * (1 - phat) / n + z * z / (4 * n * n)) ** 0.5)
    return (centro - ajuste) / denom


def cargar_calibracion(activo: str) -> dict | None:
    """Sustituye a cargar_banda() + los ACTIVOS[activo] hardcodeados del
    18-Jul -- TODO releído fresco cada ventana desde
    ballenas_timing_state.json (misma fuente que ballenas_observer.py
    recalibra cada hora vía cron), nunca congelado. Devuelve None
    (fail-closed, misma señal que antes) si el activo no es significativo
    hoy o si falta cualquier dato necesario -- un JSON parcial o corrupto
    no debe hacer que se dispare con una calibración a medias.

    23-Jul: MARGEN_CONFIRM_S es la pieza nueva que ataca la desalineación
    de timing encontrada en la sesión de franja milimétrica -- ETH
    disparaba el 70% de sus señales a 60-90s del cierre (hit=83.0%,
    n=47) mientras que firmar más cerca del cierre (15-30s) daba
    hit=100.0% (n=8, muestra pequeña pero consistente en SOL también).
    En vez de fijar un umbral a mano con esa n pequeña propia, se deriva
    de rest_hi_min -- el techo REAL del timing de confirmación de la
    banda operativa, con la n mucho mayor (cientos-miles) que ya tiene
    el observer -- + un margen corto. watch_window() ya no dispara en
    cuanto se cumple concentración; solo puede hacerlo dentro de esta
    ventana más ajustada al momento real en que las ballenas confirman."""
    try:
        estado = json.loads((DIR_SHADOW / "ballenas_timing_state.json").read_text())
    except Exception:
        return None
    e = estado.get(f"{activo}#{VENTANA_MIN}m", {})
    if not e.get("significativo"):
        return None
    lo, hi = e.get("banda_lo"), e.get("banda_hi")
    n, n_gan, rest_hi = e.get("n"), e.get("n_ganadoras"), e.get("rest_hi_min")
    if not (isinstance(lo, (int, float)) and isinstance(hi, (int, float))
            and isinstance(n, (int, float)) and n > 0
            and isinstance(n_gan, (int, float))
            and isinstance(rest_hi, (int, float))):
        return None
    prob_bucket = _wilson_lower(int(n_gan), int(n))
    confirm_ceiling_s = rest_hi * 60 + MARGEN_CONFIRM_S
    watch_lead_s = confirm_ceiling_s + MARGEN_WATCH_S
    return {"banda_lo": lo, "banda_hi": hi, "prob_bucket": prob_bucket,
            "confirm_ceiling_s": confirm_ceiling_s, "watch_lead_s": watch_lead_s,
            "n_banda": int(n)}


def watch_window(activo: str, ts_end: int) -> bool:
    """Vigila un mercado {activo}#5min concreto desde watch_lead_s hasta
    el cierre. True si ejecutó (o habría ejecutado en DRY_RUN).

    23-Jul: calibración (banda, prob_bucket, watch_lead_s, confirm_ceiling_s)
    releída fresca vía cargar_calibracion() -- ya no hay cfg estático por
    activo. Además, no confirma en cuanto se cumple concentración: solo
    puede hacerlo dentro de confirm_ceiling_s (ver cargar_calibracion),
    y usa la concentración PONDERADA por calidad de wallet, no la cruda."""
    calib = cargar_calibracion(activo)
    if calib is None:
        log(f"[{ts_end}] {activo}#5m no significativo o calibración incompleta en ballenas_timing_state.json -- se salta", activo)
        return False
    banda_lo, banda_hi = calib["banda_lo"], calib["banda_hi"]
    watch_lead_s, confirm_ceiling_s = calib["watch_lead_s"], calib["confirm_ceiling_s"]
    prob_bucket = calib["prob_bucket"]
    ts_start = ts_end - VENTANA_MIN * 60

    mercado = None
    contadores = {"ok": 0, "sin_trades_en_banda": 0, "error_api": 0}
    contador_prematuro = 0  # cumple condición pero aún fuera de confirm_ceiling_s -- solo para el log final
    while True:
        restante = ts_end - time.time()
        if restante > watch_lead_s:
            time.sleep(min(restante - watch_lead_s, 5))
            continue
        if restante < HARD_FLOOR_S:
            log(f"[{ts_end}] suelo de seguridad ({HARD_FLOOR_S}s) alcanzado sin confirmación -- se abandona "
                f"(resumen vigilancia: {sum(contadores.values())} polls, "
                f"ok={contadores['ok']} sin_trades_en_banda={contadores['sin_trades_en_banda']} "
                f"error_api={contadores['error_api']} prematuros={contador_prematuro})", activo)
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
            f_conc = ex.submit(concentracion_ballenas, mercado["condition_id"], banda_lo, banda_hi, activo)
            f_libro = ex.submit(libro_publico, mercado["yes_token"])
            pct_crudo, pct_ponderado, n, motivo_conc, wallets_yes = f_conc.result()
            libro = f_libro.result()

        contadores[motivo_conc] = contadores.get(motivo_conc, 0) + 1
        if pct_ponderado is not None:
            log(f"[{ts_end}] restante={restante:.1f}s concentracion_yes_cruda={pct_crudo:.2f} "
                f"ponderada={pct_ponderado:.2f} n={n} ask={libro.get('best_ask') if libro else None}", activo)
        elif motivo_conc == "error_api":
            log(f"[{ts_end}] restante={restante:.1f}s ⚠️ error_api consultando ballenas -- sin dato este ciclo", activo)

        cumple_concentracion = (pct_ponderado is not None and n >= MIN_TRADES_BALLENA
                                 and pct_ponderado >= CONCENTRACION_MIN
                                 and libro and libro.get("best_ask") is not None
                                 and banda_lo <= libro["best_ask"] < banda_hi)
        if cumple_concentracion and restante > confirm_ceiling_s:
            # 23-Jul: cumple la condición pero todavía está fuera de la
            # ventana real de confirmación (rest_hi_min de la banda operativa)
            # -- se sigue vigilando en vez de disparar ya, es el fix directo
            # al hallazgo de desalineación de timing (ver docstring arriba).
            contador_prematuro += 1
            time.sleep(POLL_INTERVAL_S)
            continue

        if cumple_concentracion:
            py = libro["best_ask"]
            edge = prob_bucket - py
            log(f"[{ts_end}] CONFIRMADO concentracion_ponderada={pct_ponderado:.2f} (cruda={pct_crudo:.2f}) "
                f"n={n} py={py:.3f} prob_bucket={prob_bucket:.3f} edge={edge:+.3f} restante={restante:.1f}s "
                f"confirm_ceiling_s={confirm_ceiling_s:.1f} {_resumen_wallet_edge(wallets_yes, activo)}", activo)
            _registrar_tracker(activo, mercado, py, edge, pct_ponderado, n, restante)
            return disparar(activo, mercado, py, edge, restante, prob_bucket)

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


def disparar(activo: str, mercado: dict, py: float, edge: float, restante_s: float,
              prob_bucket: float) -> bool:
    """Decide y (si no es DRY_RUN) ejecuta. Reutiliza circuit breaker +
    stake de live_stake.py y _ejecutar_orden_polymarket de live_trade.py --
    mismo presupuesto de riesgo que el resto del sistema. Serializado con
    _orden_lock: ORDEN_EN_CURSO_PATH (live_trade.py) es un marcador global
    sin clave por activo -- con 3 hilos, dos confirmaciones casi simultáneas
    podrían pisarse ese fichero sin este lock.

    23-Jul: prob_bucket llega como parámetro (calculado fresco en
    cargar_calibracion() para esta ventana concreta) en vez de leerse de
    ACTIVOS[activo] hardcodeado -- ver el hallazgo de calibración estale
    en el docstring de cargar_calibracion()."""
    subtype = f"{activo}#{VENTANA_MIN}min"
    config = lt._cargar_config()  # una sola lectura, reusada abajo para stake_ref y max_misma_dir

    # Fill-ability real (roadmap Fase 2, punto 1, 21-Jul; BUG FIX 22-Jul,
    # ver memoria idea_bug_disparar_5min_whitelist_mata_snapshot_22jul):
    # esto tiene que capturarse SIEMPRE que llegue una confirmación DRY_RUN,
    # ANTES del check puede_operar_live() de abajo -- ese check exige que la
    # tupla esté en pares_permitidos_live, y una candidata por DEFINICIÓN
    # nunca lo está (si lo estuviera ya no sería candidata). Antes este
    # snapshot vivía DESPUÉS de puede_operar_live() y de calcular_stake(),
    # así que moría siempre en el primer check: 79 confirmaciones en 4 días
    # (18→22-Jul), CERO snapshots en libro_snapshots.csv, el vigía
    # vigia_ballenas_5min_fillability.py atascado en n=0 permanentemente.
    #
    # Segundo fix 22-Jul (code-review): vive FUERA de with _orden_lock --
    # ese lock serializa el tramo de EJECUCIÓN real entre los 3-4 hilos
    # (ver su comentario de definición), y la consulta de red de este
    # snapshot no forma parte de eso; ponerla bajo el lock bloqueaba a
    # otros hilos/activos mientras esta consulta tardaba (antes de este fix
    # el tramo bajo lock era casi instantáneo, porque puede_operar_live()
    # cortaba de inmediato para estas tuplas nunca-whitelisted). Usa
    # lt._snapshot_senal_bloqueada (dedup real por market_id+direction+
    # motivo, mismo mecanismo que el resto del sistema) en vez de llamar a
    # _consultar_profundidad_libro/_registrar_snapshot_libro a mano --
    # evita duplicar filas si el proceso se reinicia a mitad de una ventana
    # de confirmación (pipeline_watchdog.py reinicia ballenas_5m cada 5min
    # si detecta stale). Solo lectura, nunca bloquea ni cambia ninguna
    # decisión de abajo -- ver except.
    if DRY_RUN:
        try:
            stake_ref = config.get("riesgo", {}).get("min_stake_eur", 1.05)
            lt._snapshot_senal_bloqueada(mercado["market_id"], "BUY_YES", py, stake_ref,
                                         {"strategy": STRATEGY, "subtype": subtype},
                                         motivo="candidato_evaluacion")
        except Exception as e:
            log(f"fill-ability snapshot error (no bloquea): {e}", activo)

    with _orden_lock:
        ok_operar, motivo_operar = puede_operar_live(STRATEGY, subtype)
        if not ok_operar:
            log(f"{motivo_operar} -- {'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

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

        ic_conviccion = (prob_bucket - 0.5) * 2
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
            "ic_modelo": round(prob_bucket, 4),
            "edge_neto": round(edge, 4),
            "conviction_score": round(prob_bucket, 4),
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
    proceso entero -- se captura y se reintenta tras un margen corto.

    23-Jul: watch_lead_s ya no es estático -- se relee vía
    cargar_calibracion() en cada vuelta del bucle (se puede recalibrar
    entre ventanas, cada hora, vía el cron de ballenas_observer.py).
    Si el activo no es significativo en este momento, duerme hasta la
    siguiente ventana en vez de reintentar en bucle apretado."""
    log("hilo arrancado (calibración dinámica, ver cargar_calibracion)", activo)
    while True:
        try:
            now = time.time()
            ts_end = (int(now) // (VENTANA_MIN * 60) + 1) * (VENTANA_MIN * 60)
            calib = cargar_calibracion(activo)
            if calib is None:
                log("no significativo ahora mismo -- duerme hasta la siguiente ventana", activo)
                time.sleep(max(5, ts_end + 2 - time.time()))
                continue
            dormir = ts_end - calib["watch_lead_s"] - time.time()
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
