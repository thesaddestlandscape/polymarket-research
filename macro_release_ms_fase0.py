#!/usr/bin/env python3
"""macro_release_ms_fase0.py -- FASE 0 (solo observación) de ronda1 #7 (sniper de datos macro) con el principio
micro-latencia (29-Sep): ¿cuántos ms después de la publicación oficial podemos CONOCER el dato y cuánto tarda el libro
de Polymarket en repreciar sus bins?

Para cada evento de macro_calendario.json: desde T-3 s se sondea la fuente oficial cada ~120 ms con una sesión
keep-alive (Statistics Canada WDS: 409 'not released yet' hasta la publicación, 200 con datos justo después) y se
registra con timestamp de ns el primer 200, el dato nuevo/anterior y el bin ganador (var. % redondeada). Después,
ya_decidido_ws_fase0 aporta la línea temporal del libro de los bins alrededor de endDate: cruzando ambas se mide
(a) latencia de detección propia, (b) cuánto quedó de ventana con el bin ganador aún <0,99 y los perdedores >0,01.
-> data/shadow/macro_release_ms_fase0.csv. NO coloca órdenes. Hilo de observadores_fase0.
"""
import csv
import json
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
CAL = REPO / "macro_calendario.json"
OUT = REPO / "data" / "shadow" / "macro_release_ms_fase0.csv"
URL_WDS = "https://www150.statcan.gc.ca/t1/wds/rest/getDataFromVectorsAndLatestNPeriods"
ANTES_S, DESPUES_S, PAUSA_S = 3.0, 120.0, 0.12
COLS = ["evento", "when_utc", "t_primer_200_ms", "latencia_desde_publicacion_ms", "n_polls", "n_409", "ref_period",
        "valor_nuevo", "valor_previo", "var_pct", "bin_ganador", "http_date_header", "rtt_ultimo_ms", "estado"]


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()


def _escribir(fila):
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        if nuevo:
            w.writeheader()
        w.writerow({c: fila.get(c, "") for c in COLS})


N_HILOS = 4          # RTT a Statcan ~540 ms desde Helsinki: 4 sondeadores escalonados -> una muestra cada ~135 ms


def _parse(r, ev, when, t_ms, n, n409, rtt):
    pts = sorted(r.json()[0]["object"]["vectorDataPoint"], key=lambda p: p["refPer"])
    nuevo, prev = float(pts[-1]["value"]), float(pts[-2]["value"])
    var = (nuevo / prev - 1) * 100
    return {"evento": ev["nombre"], "when_utc": ev["when_utc"], "t_primer_200_ms": t_ms,
            "latencia_desde_publicacion_ms": t_ms - int(when * 1000), "n_polls": n, "n_409": n409,
            "ref_period": pts[-1]["refPer"], "valor_nuevo": nuevo, "valor_previo": prev,
            "var_pct": round(var, 3), "bin_ganador": round(var, ev.get("decimales", 1)),
            "http_date_header": r.headers.get("Date", ""), "rtt_ultimo_ms": rtt, "estado": "ok"}


def _sondear_statcan(ev, when):
    """N_HILOS sondeadores keep-alive escalonados; gana el primer 200 (t = instante de ENVÍO de esa petición)."""
    res, cnt = {}, {"n": 0, "n409": 0, "rtt": ""}
    lock = threading.Lock()
    body = [{"vectorId": ev["vector"], "latestN": 2}]
    fin = when + DESPUES_S

    def worker(k):
        time.sleep(k * PAUSA_S / N_HILOS * 4)
        s = requests.Session()
        s.headers.update({"Content-Type": "application/json"})
        while not res and time.time() < fin:
            t0 = time.time_ns()
            try:
                r = s.post(URL_WDS, json=body, timeout=5)
            except Exception:
                time.sleep(PAUSA_S)
                continue
            rtt = round((time.time_ns() - t0) / 1e6)
            with lock:
                cnt["n"] += 1
                cnt["rtt"] = rtt
                if r.status_code == 409:
                    cnt["n409"] += 1
                if r.status_code == 200 and not res:
                    try:
                        res["fila"] = _parse(r, ev, when, int(t0 / 1e6), cnt["n"], cnt["n409"], rtt)
                    except Exception as e:
                        res["fila"] = {"evento": ev["nombre"], "when_utc": ev["when_utc"], "t_primer_200_ms": int(t0 / 1e6),
                                       "estado": f"200_sin_parseo:{type(e).__name__}", "rtt_ultimo_ms": rtt}
            time.sleep(PAUSA_S)

    ths = [threading.Thread(target=worker, args=(k,), daemon=True) for k in range(N_HILOS)]
    for t in ths:
        t.start()
    for t in ths:
        t.join(timeout=max(1.0, fin - time.time() + 6))
    return res.get("fila") or {"evento": ev["nombre"], "when_utc": ev["when_utc"], "n_polls": cnt["n"], "n_409": cnt["n409"],
                               "estado": "sin_publicacion", "rtt_ultimo_ms": cnt["rtt"]}


def main():
    _log("arrancado -- sondeo de fuentes oficiales macro a ~120 ms desde T-3 s")
    hechos = set()
    while True:
        try:
            cal = json.loads(CAL.read_text(encoding="utf-8"))
            for ev in cal.get("eventos", []):
                when = _ts(ev["when_utc"])
                if ev["nombre"] in hechos or time.time() > when + DESPUES_S + 5:
                    continue
                if time.time() >= when - ANTES_S:
                    _log(f"sondeando {ev['nombre']}")
                    fila = _sondear_statcan(ev, when) if ev["tipo"] == "statcan_wds" else None
                    if fila:
                        _escribir(fila)
                        _log(f"{ev['nombre']}: {fila.get('estado')} latencia {fila.get('latencia_desde_publicacion_ms')} ms bin {fila.get('bin_ganador')}")
                    hechos.add(ev["nombre"])
        except Exception as e:
            _log(f"WARN ciclo fallido: {type(e).__name__}: {e}")
        time.sleep(0.5)


if __name__ == "__main__":
    main()
