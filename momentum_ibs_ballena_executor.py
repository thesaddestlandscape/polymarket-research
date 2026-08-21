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

100% observacional -- NUNCA envía una orden real. No importa
live_stake.py/live_guard.py ni ninguna función de envío de live_trade.py
-- solo `_consultar_profundidad_libro` (solo lectura, libro público). No
hay DRY_RUN que activar/desactivar: este script no tiene camino de
ejecución real que exista para desactivar. MOMENTUM_IBS_*_BALLENA no
está en pares_permitidos_live (n=338/166 hoy, IC todavía débil/negativo,
lejos de cualquier gate) -- shadow_predict.py sigue generando estas
mismas estrategias por el ciclo lento en paralelo (mismo patrón de doble
camino ya aceptado en producción, dedup por (strategy,market_id,decision)
en shadow_resolve.py).

Corre en screen propia:
  screen -dmS momentumballena bash -c "cd /root/polymarket-research && .venv/bin/python momentum_ibs_ballena_executor.py >> logs/momentum_ibs_ballena_executor.log 2>&1"
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
import ballenas_firehose_cache as _fc
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

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"

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
    log(f"momentum_ibs_ballena_executor arrancado (100% observacional, sin envío de orden real)")
    _fc.iniciar()
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
