#!/usr/bin/env python3
"""
momentum_ibs_ballena_executor.py — Ejecutor de baja latencia para
MOMENTUM_IBS_5M_BALLENA / MOMENTUM_IBS_15M_BALLENA
(BTC/ETH/SOL/XRP/DOGE/BNB, ambos marcos).

Origen (17-Ago, continuación de sesión, petición explícita Javi: empezar
por el ejecutor de baja latencia "1+2" -- 1) capturar la señal más cerca
del instante real en vez de esperar al ciclo genérico de shadow_predict.py
(~20-100s), 2) mover el chequeo de profundidad de libro AL ORIGEN de la
señal en vez de medirla solo después. Continúa el hallazgo central de la
misma tarde (idea_momentum_gateado_por_ballenas_hallazgo_central_17ago):
el momentum genuino (drift+ibs) SOLO tiene edge real cuando una ballena
está operando el mismo mercado en ese momento -- las variantes
s_momentum_ibs_5m_ballena/s_momentum_ibs_15m_ballena YA existen en
shadow_predict.py y generan vía el loop genérico, pero para cuando ese
loop las detecta, el libro ya pudo moverse -- mismo problema de latencia
que ya resolvieron BALLENAS_TARDIAS/GBM_LATE_15M con su propio ejecutor
dedicado.

Explícitamente DESCARTADO para GBM_LATE (misma sesión, pregunta directa
de Javi): el arquetipo A de GBM_LATE tiene selección adversa ESTRUCTURAL
(el libro se vacía por una causa distinta a "llegamos tarde a una
reacción de mercado" -- verificado con gbmlate_fade_depth_fase0.py,
12-Ago: incluso cuando el libro SÍ tiene profundidad, el hit-rate CAE,
12.9% peor que el azar). El mecanismo de momentum-ballena es distinto: el
edge viene de que una wallet informada ya se movió, así que llegar antes
SÍ puede capturar liquidez mientras el edge sigue vigente -- la premisa
de este ejecutor no se hereda a GBM_LATE, no se construye lo mismo ahí.

Diseño (mismo criterio que gbm_late_15min_executor.py, mismo motivo):
IMPORTA s_momentum_ibs_5m_ballena/s_momentum_ibs_15m_ballena DIRECTAMENTE
de shadow_predict.py -- misma fórmula (drift+ibs+gate de ballena real)
que usa el ciclo lento, cero riesgo de divergencia. Solo se replica a
mano la capa exterior: resolución de mercado, polling de libro,
dirección por prob_yes vs py, y el chequeo de profundidad al origen.

Punto 2 (profundidad de libro AL ORIGEN, no solo medida después): en
cuanto la señal dispara, se consulta el libro público del lado exacto
que se compraría (`lt._consultar_profundidad_libro`, la MISMA función
canónica que usa el pipeline principal para veto_profundidad -- solo
lectura, nunca ordena) y el resultado (ratio_vs_stake, mejor_ask) se
persiste como feature de la propia predicción. Puro logging -- NO vetea
la escritura de la predicción (el causal learning decide si "profundidad
suficiente" es una condición real, mismo principio que _libro_calidad()
en shadow_predict.py) -- pero es la pieza que le faltaba a esta familia
para que, si algún día se plantea promoción, la fill-ability real ya
esté medida desde el primer día en vez de descubrirse tarde (el error
que ya sufrió toda la familia GBM_LATE/arquetipo A).

25-Ago: DRY_RUN=False a nivel de módulo, pero SOLO opera dinero real
MOMENTUM_IBS_5M_BALLENA#SOL#5min#BUY_YES -- mismo patrón exacto que
ballenas_executor_15min.py (20-Ago, ETH#15min#BUY_YES) y
gbm_late_15min_executor.py: `puede_operar_live()`/`pares_permitidos_live`
son la whitelist real, así que el resto de combos (BTC/ETH/XRP/DOGE/BNB
en ambos marcos, y MOMENTUM_IBS_15M_BALLENA entero) siguen bloqueados por
whitelist aunque DRY_RUN sea False a nivel de módulo -- para ellos no
cambia nada, siguen siendo puro logging. Motivo de la promoción: bucket
[0.30,0.35) confirmado con rigor propio (n=61, pnl/tr=+0.390€, shuffle
p=0.007, split-half consistente) Y fill-ability real ya verificada por
este mismo ejecutor desde el 17-Ago (61/62=98% de las señales con libro
real, sin selección adversa) -- petición explícita Javi 25-Ago tras
verificar ambas piezas, ver idea_momentum_ibs_ballena_sol_fillability_
confirmada_25ago. Checklist de 6 categorías completo salvo
kelly_precio_gate (familia no incluida en familias_permitidas todavía,
pendiente explícito, no bloqueante) y banda gruesa de ballenas (sin
entrada SOL#5min, tampoco bloqueante -- gate_bucket_propio es la
protección primaria activa).

Añade gate_bucket_propio (fail-closed, exige bueno_confirmado antes de
operar tuplas ya en pares_permitidos_live -- mismo mecanismo que el
resto del sistema) + veto CLV + circuit breaker + techo de correlación +
Kelly exacto -- mismos guardias, mismo orden, que ballenas_executor_
15min.py/gbm_late_15min_executor.py.

Se fusiona en observadores_fase0.py -- MOVIDO a
executores_live_consolidado.py (screen ejeclive) desde el 25-Ago, mismo
motivo que ballenas_executor_15min.py el 20-Ago: un módulo con
DRY_RUN=False no puede vivir en un proceso observacional auto-reiniciado
libremente.
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
from gate_bucket_propio import evaluar as _gate_bucket_propio
from shadow_predict import (
    s_momentum_ibs_5m_ballena,
    s_momentum_ibs_15m_ballena,
    cargar_precios_intraday,
    MOMENTUM_IBS_5M_PARES,
    MOMENTUM_IBS_15M_PARES,
)
from gbm_confluencia import evaluar as _gbm_confluencia  # 21-Ago, mismo patrón que
# shadow_predict.py/ballenas_executor_5min.py/favorito_confirmado_btc60min_buyno_executor.py
# -- puro logging (FASE 1), nunca vetea. Verificado retroactivo el mismo día: en el
# subconjunto REALMENTE fillable (ratio>=5x) de MOMENTUM_IBS_5M_BALLENA#ETH#5min#BUY_NO,
# "NO" (GBM discrepa) da pnl/tr=-0.152€ confirmado negativo (bootstrap CI90% no cruza
# cero) vs "SI" (coincide) que deja de perder (+0.013€/tr, CI cruza cero pero ya no
# negativo) -- ver idea del 21-Ago. Cobertura baja (~8% del fillable tiene señal GBM en
# el mismo mercado), por eso esto es logging para acumular n propio, no un veto todavía.

DIR = Path(__file__).resolve().parent
DIR_SHADOW = DIR / "data" / "shadow"
CONFIG_LIVE_PATH = DIR / "data" / "live" / "config_live.json"

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"

DRY_RUN = False  # 25-Ago: ver docstring -- solo opera MOMENTUM_IBS_5M_BALLENA
# #SOL#5min#BUY_YES de verdad, el resto sigue bloqueado por whitelist
# (puede_operar_live/pares_permitidos_live). NO cambiar sin revisión +
# aprobación explícita + verificación del checklist de 6 categorías.

_pares_live_cache = {"mtime": None, "set": set()}
_orden_lock = threading.Lock()  # serializa el tramo de ejecución real entre los hilos


def _pares_live_hoy_set() -> set:
    """Mismo patrón fail-closed que el resto de ejecutores de baja latencia
    (ballenas_executor_15min.py, gbm_late_15min_executor.py)."""
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

# (activo, ventana_min) -- las 6 monedas en ambos marcos, mismo universo
# que las funciones que se importan arriba (MOMENTUM_IBS_5M_PARES/15M_PARES
# ya son las 6 en los dos casos hoy, pero se deriva de ahí para no
# duplicar la lista a mano si algún día difieren).
VENTANAS = ((5, MOMENTUM_IBS_5M_PARES, s_momentum_ibs_5m_ballena, "MOMENTUM_IBS_5M_BALLENA"),
            (15, MOMENTUM_IBS_15M_PARES, s_momentum_ibs_15m_ballena, "MOMENTUM_IBS_15M_BALLENA"))

POLL_INTERVAL_S = 2.0
HARD_FLOOR_S = 5.0        # margen de seguridad antes del cierre del mercado
REFRESCO_CTX_S = 20.0     # misma cadencia que gbm_late_15min_executor.py
STAKE_REF_EUR = 1.05      # mismo suelo que el resto del sistema, para la consulta de profundidad

_session = requests.Session()
_ctx_cache = {"ts": 0.0, "precios_intraday": []}


def log(msg: str, tag: str = "") -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    prefijo = f"[{tag}] " if tag else ""
    print(f"[{ts}] {prefijo}{msg}", flush=True)


def _ctx_ligero() -> dict:
    """Solo precios_intraday -- lo único que _drift_e_ibs_ventana() (dentro
    de s_momentum_ibs_*_ballena) necesita. Mismo criterio que
    gbm_late_15min_executor.py::_ctx_ligero()."""
    ahora = time.time()
    if ahora - _ctx_cache["ts"] > REFRESCO_CTX_S:
        _ctx_cache["precios_intraday"] = cargar_precios_intraday()
        _ctx_cache["ts"] = ahora
    return {"precios_intraday": _ctx_cache["precios_intraday"]}


def resolver_mercado(activo: str, ventana_min: int, ts_start: int) -> dict | None:
    """Mismo patrón que gbm_late_15min_executor.py/ballenas_executor_5min.py
    -- una sola llamada gamma-api por ventana."""
    slug = f"{activo.lower()}-updown-{ventana_min}m-{ts_start}"
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


def _profundidad_al_origen(direccion: str, py: float, mercado: dict) -> dict:
    """Punto 2 del diseño: consulta la profundidad real del lado exacto que
    se compraría, EN EL INSTANTE en que la señal disparó -- no después.
    Reusa la función canónica del pipeline principal (solo lectura, mismo
    criterio de riesgo que wallet_mirror_tracker.py::_fillability_mirror,
    que hace exactamente esto). Nunca vetea aquí -- solo mide y persiste,
    el causal learning decide si importa (mismo principio que
    _libro_calidad())."""
    if direccion == "BUY_YES":
        token_id, precio_entrada = mercado["yes_token"], py
    else:
        token_id, precio_entrada = mercado["no_token"], round(1.0 - py, 6)
    try:
        resultado = lt._consultar_profundidad_libro(None, token_id, precio_entrada, STAKE_REF_EUR)
    except Exception as e:
        return {"ok": False, "error": str(e)}
    return resultado


def _registrar_prediccion(mercado: dict, activo: str, ventana_min: int, strategy: str,
                           resultado: dict, direccion: str, restante_s: float,
                           profundidad: dict, gbm_conf: dict) -> None:
    """Mismo formato/lock que gbm_late_15min_executor.py::_registrar_prediccion
    -- shadow_resolve.py/shadow_postmortem.py lo resuelven sin duplicar
    lógica aquí."""
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    archivo = DIR_SHADOW / f"predictions_{ts[:10]}.csv"
    subtype = f"{activo}#{ventana_min}min"
    py = resultado["features"]["py_entrada"]
    prob_yes = resultado["prob_yes"]
    edge = prob_yes - py
    features = dict(resultado["features"])
    features["ejecutor_baja_latencia"] = True
    features["profundidad_ok"] = bool(profundidad.get("ok"))
    features["profundidad_ratio_vs_stake"] = profundidad.get("ratio_vs_stake", "")
    features["profundidad_mejor_ask"] = profundidad.get("mejor_ask", "")
    features["gbm_direccion_coincide"] = gbm_conf["gbm_direccion_coincide"]
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
                        ts, strategy, mercado["market_id"], "", mercado.get("end_date", ""),
                        f"{restante_s / 3600:.4f}", f"{py:.4f}", f"{prob_yes:.4f}",
                        f"{edge:.4f}", f"{edge:.4f}", f"{edge:.4f}", direccion,
                        resultado.get("razon", "") + " (ejecutor baja latencia)", subtype,
                        "1.05", features_json,
                    ])
            finally:
                fcntl.flock(lock_f, fcntl.LOCK_UN)
    except Exception as e:
        log(f"aviso: no se pudo registrar predicción para postmortem: {e}", activo)


def disparar(activo: str, ventana_min: int, mercado: dict, strategy: str, py: float,
             prob_yes: float, direccion: str, restante_s: float) -> bool:
    """Decide y (si no es DRY_RUN, y la tupla exacta está en
    pares_permitidos_live) ejecuta. Mismos guardias, mismo orden, que
    ballenas_executor_15min.py/gbm_late_15min_executor.py -- este
    ejecutor tampoco pasa por live_trade.py::main(), ninguno de sus
    guardias se aplica gratis."""
    subtype = f"{activo}#{ventana_min}min"
    tupla_str = f"{strategy}#{subtype}#{direccion}"

    # Whitelist por TUPLA EXACTA (con dirección) primero y fail-closed --
    # puede_operar_live(strategy, subtype) SIN direction NO discrimina
    # dirección (docstring propio de live_guard.py: "permitida si alguna
    # dirección de ese strategy#subtype lo está"). Sin este check exacto
    # aquí, una señal BUY_NO nunca verificada podría colarse a ejecución
    # real solo porque BUY_YES del mismo par sí está en pares_permitidos_
    # live -- encontrado en revisión manual antes de desplegar, 25-Ago.
    if tupla_str not in _pares_live_hoy_set():
        log(f"  {tupla_str} no está en pares_permitidos_live -- "
            f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
        return False

    gate_bp = _gate_bucket_propio(tupla_str, py)
    if gate_bp["veredicto"] != "bueno_confirmado":
        log(f"  ⛔ vetado por gate_bucket_propio (veredicto={gate_bp['veredicto']}) -- "
            f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
        return False

    ok_operar, motivo_operar = puede_operar_live(strategy, subtype)
    if not ok_operar:
        log(f"  {motivo_operar} -- {'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
        return False

    with _orden_lock:
        config = lt._cargar_config()
        max_misma_dir = config.get("riesgo", {}).get("max_posiciones_abiertas_misma_direccion", 2)
        abiertas_dir = lt._posiciones_abiertas_misma_direccion(direccion)
        if abiertas_dir >= max_misma_dir:
            log(f"  techo de correlación: {abiertas_dir} posiciones {direccion} abiertas >= {max_misma_dir} -- "
                f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        if mercado["market_id"] in lt._ya_operados_hoy():
            log(f"  {mercado['market_id']} ya operado por otro proceso/hilo -- "
                f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        if bloquear_por_circuit_breaker(
                lambda motivo: log(f"  circuit breaker activo ({motivo}) -- "
                                    f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)):
            return False

        lt._CLV_CACHE = None
        clv_medio, n_clv = lt._clv_tupla(strategy, subtype, direccion, py=py)
        if n_clv >= lt.CLV_VETO_MIN_N and clv_medio < 0:
            log(f"  ⛔ Veto CLV: clv_medio={clv_medio:+.4f} (n={n_clv}) < 0 -- "
                f"{'[DRY-RUN] no ejecutaría' if DRY_RUN else 'no se ejecuta'}", activo)
            return False

        # Kelly exacto real para binarias (mismo criterio que ballenas_executor_
        # 15min.py/gbm_late_15min_executor.py): BUY_YES: f*=(p-py)/(1-py);
        # BUY_NO: f*=(py-p)/py. precio_entrada en perspectiva de la DECISIÓN.
        if direccion == "BUY_YES":
            edge_dir = prob_yes - py
            ic_conviccion = max(0.0, edge_dir / (1 - py)) if py < 1 else 0.0
            precio_decision = py
        else:
            edge_dir = py - prob_yes
            ic_conviccion = max(0.0, edge_dir / py) if py > 0 else 0.0
            precio_decision = round(1.0 - py, 6)

        stake_info = calcular_stake(ic_conviccion, strategy, subtype, direction=direccion,
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
            edge_dir=edge_dir, contexto={"strategy": strategy, "subtype": subtype})

        if resultado.get("no_fill"):
            log(f"  no_fill: {resultado.get('error')}", activo)
            return False

        trade = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "market_id": mercado["market_id"], "question": "", "end_date": mercado.get("end_date", ""),
            "strategy": strategy, "subtype": subtype, "direction": direccion,
            "stake_eur": stake_info["stake_eur"] if resultado["ok"] else 0.0,
            "entry_price": resultado["entry_price"],
            "signal_ask": round(py, 4), "slip_real": resultado.get("slip_real", ""),
            "ic_modelo": round(prob_yes, 4), "edge_neto": round(prob_yes - py, 4),
            "conviction_score": round(prob_yes, 4), "kelly_recomendado": stake_info["stake_eur"],
            "status": "OPEN" if resultado["ok"] else "ERROR",
            "close_timestamp": "", "exit_price": "", "outcome_real": "",
            "fee_eur": resultado.get("fee_eur", 0), "pnl_bruto_eur": "", "pnl_neto_eur": "",
            "notas": (f"{strategy.lower()}_baja_latencia restante={restante_s:.1f}s"
                      if resultado.get("ok") else resultado.get("error", "")),
        }
        lt._registrar_trade(trade)
        log(f"  {'EJECUTADO' if resultado['ok'] else 'ERROR'}: {resultado}", activo)
        if resultado["ok"]:
            lt.enviar_telegram(
                f"🎯 *Orden live ejecutada ({strategy} baja latencia)*\n"
                f"Estrategia: {strategy}#{subtype}#{direccion}\n"
                f"Precio fill: {resultado['entry_price']:.4f} (slip {resultado.get('slip_real', 0):+.4f})\n"
                f"Stake: {stake_info['stake_eur']:.2f}€"
            )
        return resultado["ok"]


def watch_window(activo: str, ventana_min: int, fn_senal, strategy: str, mercado: dict) -> bool:
    try:
        end_dt = datetime.fromisoformat(mercado["end_date"].replace("Z", "+00:00"))
        if end_dt.tzinfo is None:
            end_dt = end_dt.replace(tzinfo=timezone.utc)
    except Exception:
        log(f"end_date ilegible: {mercado.get('end_date')} -- se abandona", f"{activo}#{ventana_min}m")
        return False
    ts_end = end_dt.timestamp()
    n_polls = 0
    tag = f"{activo}#{ventana_min}m"

    while True:
        restante_s = ts_end - time.time()
        if restante_s < HARD_FLOOR_S:
            log(f"[{mercado['market_id']}] ventana cerrada ({n_polls} polls) -- se abandona", tag)
            return False

        libro = libro_publico(mercado["yes_token"])
        n_polls += 1
        py = libro.get("best_ask") if libro else None
        if py is None:
            time.sleep(POLL_INTERVAL_S)
            continue

        market_full = dict(mercado)
        market_full["question"] = mercado.get("question", "")
        market_full["_precio_yes"] = py
        ctx = _ctx_ligero()

        resultado = fn_senal(market_full, ctx)
        if resultado is None:
            time.sleep(POLL_INTERVAL_S)
            continue

        py_edge = resultado["features"]["py_entrada"]
        prob_yes = resultado["prob_yes"]
        direccion = "BUY_YES" if prob_yes >= py_edge else "BUY_NO"

        profundidad = _profundidad_al_origen(direccion, py_edge, mercado)
        gbm_conf = _gbm_confluencia(mercado.get("market_id") or mercado.get("condition_id"), direccion)
        log(f"[{mercado['market_id']}] {strategy} CONFIRMADO {direccion} py={py_edge:.3f} "
            f"prob_yes={prob_yes:.3f} restante={restante_s:.1f}s "
            f"profundidad_ok={profundidad.get('ok')} ratio={profundidad.get('ratio_vs_stake')} "
            f"gbm_coincide={gbm_conf['gbm_direccion_coincide']} ({n_polls} polls)", tag)
        _registrar_prediccion(mercado, activo, ventana_min, strategy, resultado, direccion,
                              restante_s, profundidad, gbm_conf)
        disparar(activo, ventana_min, mercado, strategy, py_edge, prob_yes, direccion, restante_s)
        return True  # una señal por ventana es suficiente, mismo criterio que GBM


def hilo_activo(activo: str, ventana_min: int, fn_senal, strategy: str) -> None:
    tag = f"{activo}#{ventana_min}m"
    log("hilo arrancado", tag)
    mercado_vigilado = None
    while True:
        try:
            now = time.time()
            ts_end = (int(now) // (ventana_min * 60) + 1) * (ventana_min * 60)
            ts_start = ts_end - ventana_min * 60
            if ts_start == mercado_vigilado:
                time.sleep(5)
                continue
            mercado = resolver_mercado(activo, ventana_min, ts_start)
            if mercado is None:
                time.sleep(10)
                continue
            mercado_vigilado = ts_start
            watch_window(activo, ventana_min, fn_senal, strategy, mercado)
        except Exception as e:
            log(f"error en hilo: {e} -- reintenta en 5s", tag)
            time.sleep(5)


def main():
    log(f"momentum_ibs_ballena_executor arrancado (DRY_RUN={DRY_RUN}, "
        f"whitelist real via pares_permitidos_live)")
    # 22-Ago: se retiró _fc.iniciar() (conexión websocket RTDS + caché en
    # memoria propia de ballenas_firehose_cache) -- código muerto desde el
    # 17-Ago: nada en este fichero llama a trades_de_mercado_firehose(),
    # solo _ballena_activa_reciente() (en shadow_predict.py), que usa
    # leer_snapshot_reciente() (lee data/live/ballenas_recientes.json en
    # disco, escrito por el proceso `polyactivity`, no requiere iniciar()).
    # Diagnóstico OOM 22-Ago: al fusionarse este script dentro de
    # observadores_fase0.py (20-Ago), esa conexión+caché sin consumidor
    # empezó a sumar peso real en un proceso ya con 17 hilos más. Ver
    # memoria idea_fix_oom_momentum_iniciar_muerto_22ago.
    time.sleep(3)

    hilos = []
    for ventana_min, pares, fn_senal, strategy in VENTANAS:
        for activo in sorted(pares):
            h = threading.Thread(target=hilo_activo, args=(activo, ventana_min, fn_senal, strategy),
                                  daemon=True, name=f"{activo}#{ventana_min}m")
            hilos.append(h)
            h.start()

    while True:
        time.sleep(30)
        for i, h in enumerate(hilos):
            if not h.is_alive():
                tag = h.name
                activo, resto = tag.split("#", 1)
                ventana_min = int(resto.rstrip("m"))
                strategy = next(s for v, p, f, s in VENTANAS if v == ventana_min)
                fn_senal = next(f for v, p, f, s in VENTANAS if v == ventana_min)
                log("hilo murió inesperadamente -- reiniciando", tag)
                nuevo = threading.Thread(target=hilo_activo, args=(activo, ventana_min, fn_senal, strategy),
                                          daemon=True, name=tag)
                nuevo.start()
                hilos[i] = nuevo


if __name__ == "__main__":
    main()
