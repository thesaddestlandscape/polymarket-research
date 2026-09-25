#!/usr/bin/env python3
"""analisis_binance_jump_leadlag.py -- lee /root/polymarket-research-datalogs/binance_jump_leadlag_fase0.csv (observador
binance_jump_leadlag_fase0.py) y mide, por moneda x marco y offset de entrada (0,3/0,6/1,0 s tras el
salto de Binance), con el ASK REAL leído y profundidad >=5x stake:
  - reprecio ya descontado: ask(offset) - ask(0)   [en céntimos]
  - markout: bid(+4 s) - ask(offset)               [lo que se cobraría saliendo al bid a los 4 s]
  - EV por EUR reteniendo a resolución (gamma-api, fee 7 % sobre ganancia), IC90 bootstrap por DÍAS
Uso: python3 analisis_binance_jump_leadlag.py [--desde YYYY-MM-DD]. Solo lectura + cache de outcomes.
Decisión (n>=40 eventos independientes por celda, >=3 días, IC90 por días > 0) siempre en el análisis,
nunca en el observador."""
import csv, json, random, sys, time
from collections import defaultdict
from pathlib import Path
REPO = Path(__file__).resolve().parent
CSV = Path("/root/polymarket-research-datalogs/binance_jump_leadlag_fase0.csv")
CACHE = REPO / "data/shadow/binance_jump_leadlag_outcomes.json"
FEE = 0.07
ENTRADAS = [0.3, 0.6, 1.0]
DESDE = sys.argv[sys.argv.index("--desde") + 1] if "--desde" in sys.argv else "0000"


def _resolver(mids):
    import requests
    try:
        cache = json.loads(CACHE.read_text())
    except Exception:
        cache = {}
    pend = [m for m in mids if m not in cache]
    for i in range(0, len(pend), 20):
        try:
            r = requests.get("https://gamma-api.polymarket.com/markets",
                             params=[("id", m) for m in pend[i:i + 20]] + [("closed", "true")], timeout=20)
            for m in r.json():
                outs = json.loads(m["outcomes"]) if isinstance(m["outcomes"], str) else m["outcomes"]
                pr = [float(x) for x in (json.loads(m["outcomePrices"]) if isinstance(m["outcomePrices"], str) else m["outcomePrices"])]
                if max(pr) >= 0.99:
                    cache[str(m["id"])] = outs[pr.index(max(pr))]
        except Exception:
            pass
        time.sleep(0.2)
    CACHE.write_text(json.dumps(cache))
    return cache


def calcular(desde="0000"):
    """Devuelve (n_eventos, n_con_resultado, celdas) con celdas[(activo,marco,offset)] = dict."""
    ev = defaultdict(dict)
    for r in csv.DictReader(open(CSV, encoding="utf-8")):
        if r["ts_evento"] < desde or r["error"]:
            continue
        try:
            ev[(r["ts_evento"], r["activo"], r["marco"], r["market_id"], r["direccion"])][float(r["offset_s"])] = (
                float(r["ask"]), float(r["bid"]), float(r["ratio_vs_stake"]))
        except (TypeError, ValueError):
            continue
    ganador = _resolver(sorted({k[3] for k in ev}))
    filas = defaultdict(list)
    for (t, act, marco, mid, dr), o in ev.items():
        if 0.0 not in o or 4.0 not in o:
            continue
        for e in ENTRADAS:
            if e not in o:
                continue
            ask, bid, ratio = o[e]
            if not (0.05 <= ask < 0.95) or ratio < 5:
                continue
            mk = o[4.0][1] - ask
            g = ganador.get(mid)
            ev_hold = None if g is None else (((1 - ask) / ask * (1 - FEE)) if g == dr else -1.0)
            filas[(act, marco, e)].append((t[:10], ask - o[0.0][0], mk, ev_hold))
            filas[("TODAS", marco, e)].append((t[:10], ask - o[0.0][0], mk, ev_hold))
    celdas = {}
    for k, v in filas.items():
        n = len(v)
        c = {"n": n, "descontado_c": round(sum(x[1] for x in v) / n * 100, 1),
             "markout_c": round(sum(x[2] for x in v) / n * 100, 1), "n_res": 0, "ev": None, "ic90_lo": None, "dias": 0}
        res = [x for x in v if x[3] is not None]
        if res:
            by = defaultdict(list)
            for x in res:
                by[x[0]].append(x[3])
            dl = list(by.values()); random.seed(1); bs = []
            for _ in range(400):
                sm = [y for a in random.choices(dl, k=len(dl)) for y in a]; bs.append(sum(sm) / len(sm))
            bs.sort()
            c.update({"n_res": len(res), "ev": round(sum(x[3] for x in res) / len(res), 3),
                      "ic90_lo": round(bs[20], 3), "dias": len(dl)})
        celdas[k] = c
    return len(ev), sum(k[3] in ganador for k in ev), celdas


def main():
    n_ev, n_res, celdas = calcular(DESDE)
    print(f"eventos (evento x mercado) {n_ev}; con resultado {n_res}")
    print("celda (moneda,marco,offset s) | n | ya descontado Δask(c) | markout bid(+4s)-ask (c) | n_res EV/€ hold | IC90 días lo")
    for k in sorted(celdas):
        c = celdas[k]
        print(f"{k} | {c['n']} | {c['descontado_c']:+.1f} | {c['markout_c']:+.1f} | "
              f"{c['n_res']} {c['ev'] if c['ev'] is not None else '-'} | {c['ic90_lo'] if c['ic90_lo'] is not None else '-'} días={c['dias']}")


if __name__ == "__main__":
    main()
