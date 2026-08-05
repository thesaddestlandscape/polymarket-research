#!/usr/bin/env python3
"""
sol5min_contrario_fase0.py — FASE 0 (SOLO OBSERVACIÓN) de la estrategia
contraria de SOL#5min (ver idea_sol5min_estrategia_contraria_confirmada_
03ago): apostar el lado MINORITARIO del flujo de ballenas cuando la
concentración del lado mayoritario en banda 0.3-0.5 cruza >=0.9 acierta
82.6% (n=46, Wilson90%=[71.7%,89.9%], shuffle p=0.0000, split-half
idéntico 82.6%/82.6%). Precio de entrada real ya verificado (~0.656€
medio, n=44) contra libro_ambos_lados -- lo que falta es PROFUNDIDAD real
(tamaño, no solo precio) del lado minoritario en el momento de la señal.

Mecanismo (idéntico en espíritu a p22_cola_posicion_fase0.py — NO coloca,
cancela ni modifica ninguna orden real, no llama a ninguna función de
ejecución de live_trade.py):
  1. Reusa resolver_mercado/concentracion_ballenas/cargar_calibracion de
     ballenas_executor_5min.py (misma banda 0.3-0.5, mismo timing) para
     vigilar cada mercado SOL#5min.
  2. Cuando la concentración PONDERADA del lado mayoritario cruza
     UMBRAL_CONTRARIO (0.9) dentro de la ventana de confirmación, identifica
     el lado MINORITARIO (el candidato a apostar) y arranca un hilo de
     seguimiento del libro público de ESE lado (lt._consultar_profundidad_
     libro, solo lectura, mismo patrón que P22) cada POLL_INTERVAL_S hasta
     el cierre del mercado.
  3. Persiste en data/shadow/sol5min_contrario_fase0.csv: market_id,
     momento de detección, lado minoritario, ask/ratio_vs_stake iniciales
     y serie temporal completa -- un análisis posterior cruza esto con el
     outcome real para responder: ¿el libro aguarda de verdad una entrada
     al lado minoritario, o el precio barato esconde profundidad vacía
     (mismo patrón de selección adversa ya visto en otras familias)?

Corre en screen propia:
  screen -dmS solcontrario5m bash -c "cd /root/polymarket-research && .venv/bin/python sol5min_contrario_fase0.py >> logs/sol5min_contrario_fase0.log 2>&1"
"""
import csv
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt
import ballenas_firehose_cache as _fc
from ballenas_executor_5min import (
    cargar_calibracion, concentracion_ballenas, libro_publico, resolver_mercado,
)

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "sol5min_contrario_fase0.csv"

ACTIVO = "SOL"
VENTANA_MIN = 5
UMBRAL_CONTRARIO = 0.9
HARD_FLOOR_S = 10
POLL_INTERVAL_S = 5.0
STAKE_REFERENCIA_EUR = 1.05  # suelo real del proyecto -- mide profundidad relativa a un stake típico

COLUMNS = ["ts_deteccion_utc", "market_id", "lado_mayoria", "lado_minoria",
           "pct_mayoria_detectado", "n_ballenas", "ask_minoria_deteccion",
           "muestras_json", "outcome_pendiente"]

_lock_out = threading.Lock()
_vistos = set()


def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _cargar_vistos() -> set:
    if not OUT.exists():
        return set()
    with open(OUT, encoding="utf-8") as f:
        return {r["market_id"] for r in csv.DictReader(f)}


def _escribir_fila(fila: dict) -> None:
    with _lock_out:
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)


def _seguir_libro_minoria(market_id: str, lado_minoria: str, ts_deteccion: str,
                           lado_mayoria: str, pct_mayoria: float, n_ballenas: int,
                           ask_inicial: float, restante_s: float) -> None:
    """Hilo de seguimiento tras detectar concentración>=0.9 -- solo lectura,
    sigue el libro del lado MINORITARIO hasta el cierre del mercado."""
    try:
        yes_token, no_token, _cid = lt._get_token_ids(market_id)
        token_id = yes_token if lado_minoria == "YES" else no_token

        muestras = []
        t0 = time.monotonic()
        duracion = max(restante_s, 5)
        while time.monotonic() - t0 < duracion:
            t_offset = round(time.monotonic() - t0, 1)
            try:
                prof = lt._consultar_profundidad_libro(None, token_id, ask_inicial, STAKE_REFERENCIA_EUR)
            except Exception:
                muestras.append([t_offset, None, None])
                time.sleep(POLL_INTERVAL_S)
                continue
            if not prof.get("ok"):
                muestras.append([t_offset, None, None])
            else:
                muestras.append([t_offset, prof.get("ratio_vs_stake"), prof.get("mejor_ask")])
            time.sleep(POLL_INTERVAL_S)

        import json as _json
        _escribir_fila({
            "ts_deteccion_utc": ts_deteccion,
            "market_id": market_id,
            "lado_mayoria": lado_mayoria,
            "lado_minoria": lado_minoria,
            "pct_mayoria_detectado": round(pct_mayoria, 4),
            "n_ballenas": n_ballenas,
            "ask_minoria_deteccion": ask_inicial,
            "muestras_json": _json.dumps(muestras, separators=(",", ":")),
            "outcome_pendiente": "1",
        })
        log(f"[{market_id}] seguimiento terminado, {len(muestras)} muestras registradas")
    except Exception as e:
        log(f"[{market_id}] error en _seguir_libro_minoria: {e}")


def watch_window(ts_end: int) -> None:
    calib = cargar_calibracion(ACTIVO)
    if calib is None:
        log(f"[{ts_end}] SOL#5m no significativo ahora mismo -- se salta ventana")
        return
    banda_lo, banda_hi = calib["banda_lo"], calib["banda_hi"]
    watch_lead_s, confirm_ceiling_s = calib["watch_lead_s"], calib["confirm_ceiling_s"]
    ts_start = ts_end - VENTANA_MIN * 60

    mercado = None
    detectado = False
    while True:
        restante = ts_end - time.time()
        if restante > watch_lead_s:
            time.sleep(min(restante - watch_lead_s, 5))
            continue
        if restante < HARD_FLOOR_S or detectado:
            return

        if mercado is None:
            mercado = resolver_mercado(ACTIVO, ts_start)
            if mercado is None:
                return
            if mercado["market_id"] in _vistos:
                return

        with ThreadPoolExecutor(max_workers=2) as ex:
            f_conc = ex.submit(concentracion_ballenas, mercado["condition_id"], banda_lo, banda_hi, ACTIVO)
            f_libro = ex.submit(libro_publico, mercado["yes_token"])
            pct_crudo, pct_ponderado, n, motivo_conc, wallets_yes, n_yes_total, n_trades_crudo = f_conc.result()
            libro = f_libro.result()

        if pct_ponderado is not None and restante <= confirm_ceiling_s and n >= 3:
            pct_mayoria = max(pct_ponderado, 1 - pct_ponderado)
            if pct_mayoria >= UMBRAL_CONTRARIO:
                lado_mayoria = "YES" if pct_ponderado >= 0.5 else "NO"
                lado_minoria = "NO" if lado_mayoria == "YES" else "YES"
                ask_inicial = libro.get("best_ask") if libro else None
                if ask_inicial is None:
                    time.sleep(POLL_INTERVAL_S)
                    continue
                ts_deteccion = datetime.now(timezone.utc).isoformat(timespec="seconds")
                log(f"[{mercado['market_id']}] DETECTADO concentracion={pct_mayoria:.2f} "
                    f"lado_mayoria={lado_mayoria} -> vigilando lado_minoria={lado_minoria} "
                    f"restante={restante:.1f}s")
                _vistos.add(mercado["market_id"])
                threading.Thread(
                    target=_seguir_libro_minoria,
                    args=(mercado["market_id"], lado_minoria, ts_deteccion, lado_mayoria,
                          pct_mayoria, n, ask_inicial, restante),
                    daemon=True,
                ).start()
                detectado = True
                return

        time.sleep(POLL_INTERVAL_S)


def main():
    global _vistos
    _vistos = _cargar_vistos()
    log(f"sol5min_contrario_fase0 arrancado (solo observación, {len(_vistos)} mercados ya vistos)")
    # 04-Ago: concentracion_ballenas() (importada de ballenas_executor_5min)
    # ahora lee ballenas_firehose_cache en vez de la API rota -- ese cache
    # es estado de proceso, así que este proceso (screen propia,
    # solcontrario5m) necesita arrancar su PROPIO hilo de captura, no
    # comparte el de ballenas_executor_5min.py (proceso distinto). Sin
    # esto, concentracion_ballenas() aquí devolvería firehose_no_sano
    # siempre -- mismo bug de fondo, cable sin conectar.
    _fc.iniciar()
    time.sleep(3)
    while True:
        try:
            now = time.time()
            ts_end = (int(now) // (VENTANA_MIN * 60) + 1) * (VENTANA_MIN * 60)
            watch_window(ts_end)
            time.sleep(max(1, ts_end + 2 - time.time()))
        except Exception as e:
            log(f"error en bucle principal: {e} -- reintenta en 5s")
            time.sleep(5)


if __name__ == "__main__":
    main()
