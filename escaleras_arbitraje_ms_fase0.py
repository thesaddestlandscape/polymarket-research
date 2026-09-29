#!/usr/bin/env python3
"""escaleras_arbitraje_ms_fase0.py -- FASE 0 (solo observación) de ronda3 #2 (implicaciones lógicas) con el principio
micro-latencia (29-Sep). Foto estática 29-Sep: las escaleras 'above K' de cripto NO tienen arbitraje de monotonía en reposo
(coste de cesta 1,001-1,008). Hipótesis nueva: ES TRANSITORIO -- tras un salto del spot los strikes se reprecian a
velocidades distintas y durante milisegundos puede violarse P(>K_bajo) >= P(>K_alto).

Detector de alta frecuencia (50 ms) sobre el libro por WS (libro_estado_ws.ultimo, O(1)): para cada escalera (activo, hora
de cierre) que cierra en <=15 min con strikes a <=4 % del spot, busca pares K_i<K_j con bid(YES_j) > ask(YES_i) (comprar
YES_i al ask + NO_j a 1-bid cuesta < 1 y paga >= 1). Registra cada EPISODIO (inicio ms, duración ms, pares, edge bruto,
edge neto de fee taker 0,07*p*(1-p) por pata, tamaño ejecutable min) en data/shadow/escaleras_arbitraje_ms_fase0.csv.
Pregunta: ¿aparecen episodios con edge neto > 0 y tamaño >= 5 acciones, y cuánto duran (si duran >> nuestra latencia
de envío hay ventana)? NO coloca órdenes. Hilo de observadores_fase0.
"""
import csv
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import libro_estado_ws as LE  # noqa: E402
import ya_decidido_ws_fase0 as Y  # noqa: E402

OUT = REPO / "data" / "shadow" / "escaleras_arbitraje_ms_fase0.csv"
POLL_S = 0.05
REFRESCO_S = 30
HORIZONTE_S = 15 * 60
FEE = 0.07
COLS = ["activo", "end_ts", "t_inicio_ms", "duracion_ms", "strike_bajo", "strike_alto", "edge_bruto_max", "edge_neto_max",
        "size_min_max", "n_pares_max", "ask_bajo", "bid_alto"]


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _activo(q):
    ql = q.lower()
    for k, v in Y.ACTIVOS.items():
        if k in ql:
            return v
    return ""


def _strike(q):
    import re
    m = re.search(r"above ([\d,]+(?:\.\d+)?)", q)
    return float(m.group(1).replace(",", "")) if m else None


def _mejor_par(grupo):
    """Mejor violación de monotonía del grupo: lista de (edge_bruto, edge_neto, size, ki, kj, ask_i, bid_j)."""
    res = []
    est = []
    for k, tok in grupo:
        u = LE.ultimo(tok)
        if u and u[1] is not None and u[3] is not None:
            est.append((k, u))
    est.sort()
    for i in range(len(est)):
        ki, ui = est[i]
        ask_i, sz_ai = ui[3], ui[4]
        for j in range(i + 1, len(est)):
            kj, uj = est[j]
            bid_j, sz_bj = uj[1], uj[2]
            edge = bid_j - ask_i
            if edge >= 0.005:
                fee = FEE * ask_i * (1 - ask_i) + FEE * (1 - bid_j) * bid_j
                res.append((edge, edge - fee, min(sz_ai or 0, sz_bj or 0), ki, kj, ask_i, bid_j))
    return res


def main():
    _log("arrancado -- detector de violaciones de monotonía entre strikes de escaleras cripto (50 ms, libro WS)")
    LE.iniciar(("15min",))
    grupos, ep = {}, {}          # (activo,end)->[(k,yes_token)];  (activo,end)-> episodio abierto
    prox = 0.0
    while True:
        try:
            ahora = time.time()
            if ahora >= prox:
                prox = ahora + REFRESCO_S
                nuevos = {}
                for c in Y._candidatos("escaleras"):
                    if c["end"] - ahora > HORIZONTE_S or c["end"] < ahora:
                        continue
                    k, a = _strike(c["q"]), _activo(c["q"])
                    if k is None or not a:
                        continue
                    nuevos.setdefault((a, c["end"]), []).append((k, c["toks"][0]))
                    LE.pedir([c["toks"][0]], HORIZONTE_S + 60)
                grupos = nuevos
            for g, lst in grupos.items():
                if g[1] < ahora:
                    continue
                pares = _mejor_par(lst)
                tms = int(ahora * 1000)
                if pares:
                    mejor = max(pares, key=lambda x: x[1])
                    e = ep.get(g)
                    if e is None:
                        ep[g] = e = {"t0": tms, "bruto": mejor[0], "neto": mejor[1], "size": mejor[2], "n": len(pares),
                                     "ki": mejor[3], "kj": mejor[4], "ask": mejor[5], "bid": mejor[6]}
                    else:
                        if mejor[1] > e["neto"]:
                            e.update(neto=mejor[1], ki=mejor[3], kj=mejor[4], ask=mejor[5], bid=mejor[6])
                        e["bruto"] = max(e["bruto"], mejor[0])
                        e["size"] = max(e["size"], mejor[2])
                        e["n"] = max(e["n"], len(pares))
                    e["t1"] = tms
                elif g in ep:
                    e = ep.pop(g)
                    nuevo = not OUT.exists()
                    with open(OUT, "a", newline="", encoding="utf-8") as f:
                        w = csv.DictWriter(f, fieldnames=COLS)
                        if nuevo:
                            w.writeheader()
                        w.writerow({"activo": g[0], "end_ts": g[1], "t_inicio_ms": e["t0"], "duracion_ms": e["t1"] - e["t0"],
                                    "strike_bajo": e["ki"], "strike_alto": e["kj"], "edge_bruto_max": round(e["bruto"], 4),
                                    "edge_neto_max": round(e["neto"], 4), "size_min_max": e["size"], "n_pares_max": e["n"],
                                    "ask_bajo": e["ask"], "bid_alto": e["bid"]})
        except Exception as ex:
            _log(f"WARN ciclo fallido: {type(ex).__name__}: {ex}")
        time.sleep(POLL_S)


if __name__ == "__main__":
    main()
