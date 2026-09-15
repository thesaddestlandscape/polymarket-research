#!/usr/bin/env python3
"""
resolution_sniper_freeze_estado_fase0.py — 15-Sep, petición explícita
Javi: determinar el límite EXACTO (en microsegundos, no en segundos
enteros) en que Polymarket deja de aceptar órdenes reales cerca del
cierre de un mercado — "diseccionar con bisturí todo antes que
arriesgar un euro, no estamos en esas".

Origen: dos pruebas reales ya ejecutadas (03-Sep, ver memoria
`idea_resolution_sniper_precierre_tambien_falla_en_ventana_edge_15sep`)
dispararon órdenes reales a offset=-2s con el libro completamente sano
(profundidad≈244€, 37 niveles) y Polymarket las rechazó con
`PolyApiException 503: "trading is disabled"`. La profundidad del libro
público (`lt._fetch_book_publico`, lo que ya mide
`resolution_sniper_precierre_curva_cierre_fase0.py`) NO refleja ese
bloqueo — el libro seguía lleno cuando la orden ya era rechazada. Hace
falta una señal distinta.

Hallazgo de esta sesión (15-Sep): el endpoint público del CLOB
`GET https://clob.polymarket.com/markets/{condition_id}` expone un campo
`accepting_orders` (sin auth, sin firmar nada, ~90ms/llamada) que SÍ
podría reflejar el bloqueo de aceptación de órdenes en tiempo real —
verificado que existe y responde 200 OK sobre un condition_id real.

Mecanismo (mismo patrón EXACTO que resolution_sniper_precierre_curva_
cierre_fase0.py — reusa ASSETS/mercado_slot/token_ids/_TAIL de ese
módulo y de resolution_sniper_observer.py, NUNCA duplicado): para cada
ventana de 5min, resuelve los 6 mercados a T-12s, y desde T-15s hasta
T+2s consulta SOLO `accepting_orders` cada POLL_INTERVALO_MS (150ms por
defecto — más fino que los 250ms del hermano porque aquí el objetivo es
el instante exacto del corte) para los 6 activos en paralelo.

15-Sep, ajuste tras la primera prueba en vivo: la versión inicial
consultaba TAMBIÉN la profundidad de libro en cada tick (12 llamadas
concurrentes/150ms) -- el CLOB empezó a fallar bajo esa carga (latencia
subiendo a 900ms, varias peticiones fallando en <15ms de forma
sospechosa, probablemente descartadas por backpressure/rate-limit).
Como la profundidad de libro YA la mide el observador hermano
(resolution_sniper_precierre_curva_cierre_fase0.py) corriendo en
paralelo, este script mide SOLO accepting_orders (la señal nueva) y se
cruza con el CSV del hermano por `ts_end`+`ts_poll_utc` en el análisis
posterior -- mitad de peticiones, mismo resultado, sin duplicar
medición ni sobrecargar el endpoint.

⚠️ 100% observación — NO coloca, cancela ni modifica ninguna orden real,
no firma nada, no toca dinero real ni credenciales. Cada consulta es una
llamada REST pública anónima. Salida:
data/shadow/resolution_sniper_freeze_estado_fase0.csv

Corre en screen propia:
  screen -dmS freezeestado bash -c "cd /root/polymarket-research && .venv/bin/python resolution_sniper_freeze_estado_fase0.py >> logs/resolution_sniper_freeze_estado_fase0.log 2>&1"
"""
import csv
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import requests

from resolution_sniper_observer import ASSETS, mercado_slot, token_ids, _TAIL

REPO = Path(__file__).resolve().parent
OUT = REPO / "data" / "shadow" / "resolution_sniper_freeze_estado_fase0.csv"

MARCO_TAG = "5m"
DUR_S = 300
STAKE_REF_EUR = 1.05
DESDE_S = -15.0          # empieza 15s antes del cierre nominal
HASTA_S = 2.0            # sigue hasta 2s después
POLL_INTERVALO_MS = 150  # más fino que el hermano (250ms) -- el objetivo es el instante del corte
PRECALCULO_ANTES_S = 17  # margen extra sobre DESDE_S para resolver mercados con tiempo de sobra
CLOB_MARKET_URL = "https://clob.polymarket.com/markets/{condition_id}"
_TIMEOUT_S = 5
_POOL = ThreadPoolExecutor(max_workers=len(ASSETS))
_SESSION = requests.Session()

_CAMPOS = [
    "ts_end", "ts_poll_utc", "restante_s", "activo", "direccion_implicita",
    "accepting_orders", "closed_flag", "t_lectura_estado_ms",
]


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _append_csv_filas(filas: list) -> None:
    if not filas:
        return
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=_CAMPOS)
        if nuevo:
            w.writeheader()
        for fila in filas:
            w.writerow({k: fila.get(k, "") for k in _CAMPOS})


def _preparar_mercados(ts_end: int) -> dict:
    """Igual que el hermano (curva_cierre_fase0), + guarda condition_id
    (necesario aquí para consultar /markets/{condition_id}, el hermano
    no lo necesitaba porque solo consultaba el libro por token_id)."""
    ts_start = ts_end - DUR_S
    mercados = {}
    for activo in ASSETS:
        _slug, mkt = mercado_slot(activo, MARCO_TAG, ts_start)
        if not mkt:
            continue
        token_yes, token_no = token_ids(mkt)
        if not token_yes or not token_no:
            continue
        condition_id = mkt.get("conditionId")
        if not condition_id:
            continue
        ref_open = _TAIL.precio_en(activo, ts_start) or _TAIL.precio_en(activo, ts_start + 2)
        if ref_open is None or ref_open <= 0:
            continue
        mercados[activo] = {
            "token_yes": token_yes, "token_no": token_no,
            "condition_id": condition_id, "ref_open": ref_open,
        }
    return mercados


def _consultar_estado_mercado(condition_id: str) -> dict:
    """GET público /markets/{condition_id} -- sin auth, sin firmar nada.
    ok=False en error (guarda también el motivo para diagnosticar fallos
    reales vs backpressure -- 15-Sep, hallazgo real: bajo carga alta el
    CLOB puede fallar rápido, ver docstring del módulo), mismo contrato
    fail-closed que _fetch_book_publico."""
    try:
        r = _SESSION.get(CLOB_MARKET_URL.format(condition_id=condition_id), timeout=_TIMEOUT_S)
        r.raise_for_status()
        d = r.json()
        return {"ok": True, "accepting_orders": d.get("accepting_orders"), "closed": d.get("closed")}
    except Exception as e:
        return {"ok": False, "accepting_orders": None, "closed": None, "error": repr(e)}


def _poll_un_activo(activo: str, mkt: dict) -> dict | None:
    precio_actual = _TAIL.precio_ultimo(activo)
    if precio_actual is None:
        return None
    if precio_actual > mkt["ref_open"]:
        dir_impl = "Up"
    elif precio_actual < mkt["ref_open"]:
        dir_impl = "Down"
    else:
        return None

    t0 = time.perf_counter()
    estado = _consultar_estado_mercado(mkt["condition_id"])
    t_estado_ms = (time.perf_counter() - t0) * 1000

    return {
        "activo": activo, "direccion_implicita": dir_impl,
        "accepting_orders": estado["accepting_orders"] if estado["ok"] else "",
        "closed_flag": estado["closed"] if estado["ok"] else "",
        "t_lectura_estado_ms": round(t_estado_ms, 1),
    }


def _pollear_ventana(ts_end: int) -> None:
    objetivo_precalculo = ts_end - PRECALCULO_ANTES_S
    espera = objetivo_precalculo - time.time()
    if espera > 0:
        time.sleep(espera)
    mercados = _preparar_mercados(ts_end)
    if not mercados:
        return

    while time.time() < ts_end + DESDE_S:
        time.sleep(0.05)

    fin_poll = ts_end + HASTA_S
    while time.time() < fin_poll:
        t_poll = time.time()
        ts_poll_utc = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
        restante_s = round(ts_end - t_poll, 3)

        futuros = {activo: _POOL.submit(_poll_un_activo, activo, mkt)
                   for activo, mkt in mercados.items()}
        filas = []
        for activo, fut in futuros.items():
            try:
                r = fut.result(timeout=_TIMEOUT_S + 1)
            except Exception:
                r = None
            if r is None:
                continue
            filas.append({"ts_end": ts_end, "ts_poll_utc": ts_poll_utc, "restante_s": restante_s, **r})
        _append_csv_filas(filas)

        restante_intervalo = (POLL_INTERVALO_MS / 1000.0) - (time.time() - t_poll)
        if restante_intervalo > 0:
            time.sleep(restante_intervalo)


def main() -> None:
    _TAIL.arrancar()
    time.sleep(2)
    _log(f"resolution_sniper_freeze_estado_fase0 arrancado -- "
         f"activos={ASSETS} poll={POLL_INTERVALO_MS}ms ventana=[{DESDE_S},{HASTA_S}]s "
         f"campo=accepting_orders (100% observación, sin dinero real)")
    while True:
        try:
            now = time.time()
            ts_end = (int(now) // DUR_S + 1) * DUR_S
            objetivo = ts_end - PRECALCULO_ANTES_S
            margen = objetivo - time.time()
            if margen > 0:
                time.sleep(margen)
            _pollear_ventana(ts_end)
            resto = ts_end + HASTA_S + 1 - time.time()
            if resto > 0:
                time.sleep(min(resto, 30))
        except Exception as e:
            _log(f"error en ciclo principal ({type(e).__name__}: {e}) -- se reintenta en el siguiente ciclo")
            time.sleep(5)


if __name__ == "__main__":
    main()
