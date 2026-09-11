#!/usr/bin/env python3
"""
resolution_sniper_precierre_curva_cierre_fase0.py — 09-Sep, petición
explícita Javi: "hay que saber cuándo cierra [el libro] y cuáles son los
segundos óptimos para entrar, como si son milisegundos". Ampliado el
mismo día a los 6 activos ("dejalo acumular para todas las monedas unos
días, quizá hay algo") -- empezó solo con BTC (única con evidencia
histórica de edge real), pero el cambio de régimen podría no ser
universal, y no cuesta mucho más medirlo en los 6 a la vez.

Origen: resolution_sniper_precierre_executor.py (DRY_RUN=True desde
04-Sep) lleva 5+ días SIN disparar ni una vez para BTC -- investigado y
confirmado un cambio de régimen real (resolution_sniper_precierre_depth_
fase0.csv: BTC con ask válido en offset -1/-2s cayó de 22-84/día
(01-03-Sep) a 0-2/día desde el 04-Sep). Ese observador solo muestrea en
8 offsets FIJOS (-30,-20,-12,-8,-5,-3,-2,-1s) -- resolución de segundo
entero, no sirve para encontrar un óptimo en milisegundos ni para saber
si el libro se vacía en un instante preciso o se va degradando.

Mecanismo: para cada ventana de 5min (BTC/ETH/SOL/XRP/DOGE/BNB comparten
el mismo `ts_end`, un solo bucle de polling sirve para las 6), resuelve
mercado/tokens de cada activo a T-12s (mismo _Precalculo/_profundidad_
correcta que el ejecutor, reusados sin duplicar, SIN cliente CLOB --
esto es puro observador, no firma nada), y desde T-10s hasta T+1s
consulta el libro público cada POLL_INTERVALO_MS (250ms por defecto) del
lado implicado por el precio Chainlink en ese instante, PARA LOS 6
ACTIVOS EN PARALELO (ThreadPoolExecutor, igual que fetch_mercados_
paralelo en shadow_resolve.py) -- 6 requests concurrentes por tick caben
de sobra en el presupuesto de 250ms (cada una ~50-80ms). Registra
mejor_ask/profundidad/ratio por activo en cada poll con el segundo exacto
(con decimales) respecto al cierre -- permite reconstruir la curva
completa de liquidez por activo, no solo un punto.

⚠️ Solo observación -- NO coloca ninguna orden, no firma nada, no toca
dinero real. Salida: data/shadow/resolution_sniper_precierre_curva_cierre_fase0.csv

Corre en screen propia:
  screen -dmS curvacierre bash -c "cd /root/polymarket-research && .venv/bin/python resolution_sniper_precierre_curva_cierre_fase0.py >> logs/resolution_sniper_precierre_curva_cierre_fase0.log 2>&1"
"""
import csv
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt
from resolution_sniper_observer import ASSETS, mercado_slot, token_ids, _TAIL
from resolution_sniper_precierre_executor import _profundidad_correcta

REPO = Path(__file__).resolve().parent
OUT = REPO / "data" / "shadow" / "resolution_sniper_precierre_curva_cierre_fase0.csv"

MARCO_TAG = "5m"
DUR_S = 300
STAKE_REF_EUR = 1.05
DESDE_S = -10.0         # empieza a pollear 10s antes del cierre nominal
HASTA_S = 1.0           # y sigue hasta 1s DESPUÉS (por si acaso, aunque ya sabemos que ahí "trading is disabled")
POLL_INTERVALO_MS = 250
PRECALCULO_ANTES_S = 12
_POOL = ThreadPoolExecutor(max_workers=len(ASSETS))

_CAMPOS = [
    "ts_end", "ts_poll_utc", "restante_s", "activo", "direccion_implicita",
    "mejor_ask", "profundidad_eur", "ratio_vs_stake", "n_niveles", "t_lectura_ms",
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
    ts_start = ts_end - DUR_S
    mercados = {}
    for activo in ASSETS:
        _slug, mkt = mercado_slot(activo, MARCO_TAG, ts_start)
        if not mkt:
            continue
        token_yes, token_no = token_ids(mkt)
        if not token_yes or not token_no:
            continue
        ref_open = _TAIL.precio_en(activo, ts_start) or _TAIL.precio_en(activo, ts_start + 2)
        if ref_open is None or ref_open <= 0:
            continue
        mercados[activo] = {"token_yes": token_yes, "token_no": token_no, "ref_open": ref_open}
    return mercados


def _poll_un_activo(activo: str, mkt: dict, ts_poll: float) -> dict | None:
    precio_actual = _TAIL.precio_ultimo(activo)
    if precio_actual is None:
        return None
    if precio_actual > mkt["ref_open"]:
        dir_impl, token_id = "Up", mkt["token_yes"]
    elif precio_actual < mkt["ref_open"]:
        dir_impl, token_id = "Down", mkt["token_no"]
    else:
        return None

    t0 = time.perf_counter()
    depth = _profundidad_correcta(token_id, STAKE_REF_EUR)
    t_lectura_ms = (time.perf_counter() - t0) * 1000
    return {
        "activo": activo, "direccion_implicita": dir_impl,
        "mejor_ask": depth.get("mejor_ask", "") if depth.get("ok") else "",
        "profundidad_eur": depth.get("profundidad_eur", "") if depth.get("ok") else "",
        "ratio_vs_stake": depth.get("ratio_vs_stake", "") if depth.get("ok") else "",
        "n_niveles": depth.get("n_niveles", "") if depth.get("ok") else "",
        "t_lectura_ms": round(t_lectura_ms, 1),
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

        futuros = {activo: _POOL.submit(_poll_un_activo, activo, mkt, t_poll)
                   for activo, mkt in mercados.items()}
        filas = []
        for activo, fut in futuros.items():
            try:
                r = fut.result(timeout=2.0)
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
    _log(f"resolution_sniper_precierre_curva_cierre_fase0 arrancado -- "
         f"activos={ASSETS} poll={POLL_INTERVALO_MS}ms ventana=[{DESDE_S},{HASTA_S}]s")
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
