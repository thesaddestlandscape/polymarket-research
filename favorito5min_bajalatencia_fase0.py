#!/usr/bin/env python3
"""
favorito5min_bajalatencia_fase0.py — FASE 0 (SOLO OBSERVACIÓN) de latencia
real en FAVORITO_CONFIRMADO#{DOGE,XRP}#5min#BUY_NO.

Origen (07-Ago, petición explícita Javi "no podemos descartar nada" tras
[[idea_favorito5min_xrp_latencia_confirmada_precio_confundido_07ago]]):
un shuffle test (nunca antes hecho) confirmó que la latencia SÍ importa en
ambas monedas (split por mediana de lag: DOGE p=0.033, XRP p=0.001,
rápido>lento en pnl) pero se midió sobre el polling de ~20-40s de
`candidato_evaluacion` (shadow_predict.py, ciclo normal, reintenta la
señal viva cada ~20s). Al escanear umbrales de velocidad con ESOS datos:
DOGE nunca cruza a pnl positivo, ni en su cuartil más rápido observado
(lag<=10s, n=17, pnl=-0.456€) -- parece cerrado. XRP sí cruza (lag<=15s,
n=49, pnl=+0.122€, p=0.0013, split-half consistente) pero 19/49 casos
caen en el mismo micro-bucket de precio [0.40,0.45) que YA rondaba
significancia por sí solo sin sobrevivir BH-FDR -- probable confusión
latencia/precio, no evidencia independiente, y el umbral 15s se eligió
tras escanear 4 candidatos (sesgo de grados de libertad).

Este observador vigila el libro con polling MUCHO más rápido
(POLL_INTERVAL_S, ~1s vs los ~20-40s del ciclo normal) para:
  1. Ver si DOGE con latencia genuinamente baja (no solo "el cuartil más
     rápido que el polling lento pudo medir") cambia el cuadro -- los
     datos actuales NO cubren ese régimen, solo lo extrapolan.
  2. Acumular n NUEVO para XRP en el bucket [0.40,0.45) con lag real
     bajo, sin el sesgo de haber elegido el umbral mirando estos mismos
     datos -- confirmación limpia o refutación, no re-análisis del mismo
     dataset.

Mecanismo (NO coloca, cancela ni modifica ninguna orden real, no llama a
ninguna función de ejecución de live_trade.py):
  1. Reusa resolver_mercado/libro_publico de ballenas_executor_5min.py
     (slug determinista f"{activo.lower()}-updown-5m-{ts_start}").
  2. Vigila cada mercado {DOGE,XRP}#5min desde que abre hasta que cierra,
     polling cada POLL_INTERVAL_S. En el PRIMER instante que el ask YES
     cruza UMBRAL_BAJO (mismo valor que s_favorito_confirmado en
     shadow_predict.py), registra el lag real desde la apertura de la
     ventana y consulta profundidad del libro NO (lt._consultar_
     profundidad_libro, solo lectura) para fill-ability.
  3. Escribe una fila de auditoría propia (favorito5min_bajalatencia_
     fase0.csv) Y una predicción a predictions_YYYY-MM-DD.csv con
     STRATEGY sintética "FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA" --
     mismo principio que las tuplas sintéticas WALLET_MIRROR#* (nunca
     puede estar en pares_permitidos_live, aislada del stream real de
     FAVORITO_CONFIRMADO para no contaminar su aprendizaje causal ni
     gate_bucket_propio, ya activos con dinero real en otras tuplas de
     esa familia). shadow_resolve.py la resuelve con la infraestructura
     existente sin cambios -- así este observador hereda pnl_neto/
     acierto reales gratis, sin duplicar lógica de resolución.

⚠️ Corre DESDE EL ARRANQUE fusionado en observadores_fase0.py (política
05-Ago, CPU limitada a 2 cores, ver docstring de ese fichero) -- NO tiene
screen propia, corre como hilo. Nunca lanzar
`screen -dmS ... favorito5min_bajalatencia_fase0.py` suelto: duplicaría
el proceso (mismo incidente que motivó matar la screen duplicada de
favbtc60mno esta sesión).
"""
import csv
import fcntl
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt
import ballenas_firehose_cache as _fc
from ballenas_executor_5min import libro_publico, resolver_mercado

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "favorito5min_bajalatencia_fase0.csv"
PREDICTIONS_LOCK_PATH = DIR_SHADOW / ".predictions_lock"

STRATEGY = "FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA"  # sintética, nunca en pares_permitidos_live
DIRECTION = "BUY_NO"
ACTIVOS = ("DOGE", "XRP")
VENTANA_MIN = 5

# Mismos valores exactos que s_favorito_confirmado (shadow_predict.py).
UMBRAL_BAJO = 0.45
NUDGE = 0.06

POLL_INTERVAL_S = 1.0  # vs ~20-40s del ciclo normal -- esto es lo que se está probando
HARD_FLOOR_S = 3.0
STAKE_REFERENCIA_EUR = 1.05  # suelo real del proyecto, solo para medir profundidad relativa

COLUMNS = ["ts_deteccion_utc", "market_id", "activo", "lag_apertura_s", "restante_s",
           "py_ask_yes", "profundidad_ratio_no", "profundidad_ask_no"]

_lock_out = threading.Lock()
_vistos: set[str] = set()


def log(msg: str, activo: str = "") -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    prefijo = f"[{activo}] " if activo else ""
    print(f"[{ts}] {prefijo}{msg}", flush=True)


def _cargar_vistos() -> set:
    if not OUT.exists():
        return set()
    with open(OUT, encoding="utf-8") as f:
        return {r["market_id"] for r in csv.DictReader(f)}


def _escribir_auditoria(fila: dict) -> None:
    with _lock_out:
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)


def _registrar_prediccion(activo: str, mercado: dict, py: float, prob_yes: float,
                           restante_s: float, lag_apertura_s: float,
                           profundidad: dict | None) -> None:
    """Mismo formato que el resto de ejecutores de baja latencia --
    shadow_resolve.py/shadow_postmortem.py la resuelven y aprenden de
    ella sin duplicar esa lógica aquí. STRATEGY sintética: no toca el
    stream de FAVORITO_CONFIRMADO real."""
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    archivo = DIR_SHADOW / f"predictions_{ts[:10]}.csv"
    subtype = f"{activo}#{VENTANA_MIN}min"
    edge = prob_yes - py  # perspectiva YES, por convención (CLAUDE.md)
    features = json.dumps({
        "py_entrada": round(py, 4),
        "restante_min": round(restante_s / 60.0, 2),
        "hora_utc": datetime.now(timezone.utc).hour,
        "lag_apertura_s": round(lag_apertura_s, 2),
        "profundidad_ratio_no": profundidad.get("ratio_vs_stake") if profundidad else None,
        "fase0_solo_observacion": True,
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
                        "favorito_confirmado bajalatencia fase0 (solo observación)", subtype,
                        "1.05", features,
                    ])
            finally:
                fcntl.flock(lock_f, fcntl.LOCK_UN)
    except Exception as e:
        log(f"aviso: no se pudo registrar predicción para postmortem: {e}", activo)


def watch_window(activo: str, ts_end: int) -> None:
    ts_start = ts_end - VENTANA_MIN * 60
    mercado = None
    n_polls = 0
    while True:
        now = time.time()
        restante = ts_end - now
        if restante < HARD_FLOOR_S:
            return

        if mercado is None:
            mercado = resolver_mercado(activo, ts_start)
            if mercado is None:
                time.sleep(POLL_INTERVAL_S)
                continue
            if mercado["market_id"] in _vistos:
                return

        libro = libro_publico(mercado["yes_token"])
        n_polls += 1
        py = libro.get("best_ask") if libro else None

        if py is not None and py <= UMBRAL_BAJO:
            ts_deteccion = datetime.now(timezone.utc).isoformat(timespec="seconds")
            lag_apertura_s = now - ts_start
            prob_yes = max(0.03, py - NUDGE)

            try:
                prof = lt._consultar_profundidad_libro(None, mercado["no_token"], 1.0 - py,
                                                        STAKE_REFERENCIA_EUR)
            except Exception:
                prof = None

            log(f"[{mercado['market_id']}] CONFIRMADO py={py:.3f} lag_apertura={lag_apertura_s:.1f}s "
                f"restante={restante:.1f}s ratio_no={prof.get('ratio_vs_stake') if prof and prof.get('ok') else None} "
                f"({n_polls} polls)", activo)

            _vistos.add(mercado["market_id"])
            _escribir_auditoria({
                "ts_deteccion_utc": ts_deteccion,
                "market_id": mercado["market_id"],
                "activo": activo,
                "lag_apertura_s": round(lag_apertura_s, 2),
                "restante_s": round(restante, 1),
                "py_ask_yes": round(py, 4),
                "profundidad_ratio_no": prof.get("ratio_vs_stake") if prof and prof.get("ok") else "",
                "profundidad_ask_no": prof.get("mejor_ask") if prof and prof.get("ok") else "",
            })
            _registrar_prediccion(activo, mercado, py, prob_yes, restante, lag_apertura_s, prof)
            return

        time.sleep(POLL_INTERVAL_S)


def hilo_activo(activo: str) -> None:
    log("hilo arrancado", activo)
    while True:
        try:
            now = time.time()
            ts_end = (int(now) // (VENTANA_MIN * 60) + 1) * (VENTANA_MIN * 60)
            watch_window(activo, ts_end)
            time.sleep(max(1, ts_end + 2 - time.time()))
        except Exception as e:
            log(f"error en hilo: {e} -- reintenta en 5s", activo)
            time.sleep(5)


def main():
    global _vistos
    _vistos = _cargar_vistos()
    log(f"favorito5min_bajalatencia_fase0 arrancado (solo observación, activos={list(ACTIVOS)}, "
        f"{len(_vistos)} mercados ya vistos)")
    _fc.iniciar()
    time.sleep(3)

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
