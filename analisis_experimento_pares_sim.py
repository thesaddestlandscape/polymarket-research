#!/usr/bin/env python3
"""analisis_experimento_pares_sim.py -- resumen POR POLÍTICA del ensayo en seco con rellenos simulados del experimento
de pares 15m (dev: experimento_pares_cola_15m.py, Javi 09-Oct "hazlo así, más seguro y completo").

Fuente: datalogs/experimento_pares_dedicada_seco_<moneda>_ledger.jsonl, eventos `mercado_fin` (real false, medido) con
`politica` y `rellenos` (acc y precio por relleno; lado YES = token "Up"/"Yes" por NOMBRE). PnL por MERCADO a
resolución con desenlace OFICIAL: el ganador se lee de gamma (closed=true) POR NOMBRE de outcome (16ª #9: sin suponer
el orden), cobertura informada. Maker sin comisión; reembolso ESTIMADO aparte = 20 % de 0,07·p·(1-p) por acción.
Por política: n mercados, periodo, con relleno / par completo / una pata, PnL total y por mercado con IC90 por
bootstrap de MERCADOS, PnL sin los 2 mejores mercados; los mercados cortados (kill/señal) van aparte (16ª #8).
Solo lectura. Uso: python3 analisis_experimento_pares_sim.py [--monedas btc,sol,...] [--desde 2026-10-09T18:00]
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path

import numpy as np
import requests

DL = Path("/root/polymarket-research-datalogs")
MONEDAS = ("btc", "eth", "sol", "xrp", "doge", "bnb")
RNG = np.random.default_rng(5)


def ganadores(ids):
    """{id: 'YES'|'NO'} con el ganador por NOMBRE del outcome (Up/Yes -> YES, Down/No -> NO); solo mercados cerrados."""
    out, ids = {}, sorted(set(ids))
    for k in range(0, len(ids), 40):
        try:
            r = requests.get("https://gamma-api.polymarket.com/markets", timeout=20,
                             params=[("id", x) for x in ids[k:k + 40]] + [("closed", "true"), ("limit", "40")]).json() or []
        except Exception as e:
            print(f"gamma lote {k // 40}: {type(e).__name__}")
            continue
        for m in r:
            try:
                outs = json.loads(m["outcomes"]) if isinstance(m["outcomes"], str) else m["outcomes"]
                pr = json.loads(m["outcomePrices"]) if isinstance(m["outcomePrices"], str) else m["outcomePrices"]
                gan = [o for o, p in zip(outs, pr) if float(p) >= 0.999]
                if len(gan) == 1:
                    out[str(m["id"])] = "YES" if gan[0] in ("Up", "Yes") else "NO" if gan[0] in ("Down", "No") else None
            except (KeyError, TypeError, ValueError):
                continue
    return {k: v for k, v in out.items() if v}


def ic90(v):
    v = np.asarray(v, float)
    if len(v) < 3:
        return (float("nan"), float("nan"))
    m = v[RNG.integers(0, len(v), size=(2000, len(v)))].mean(1)
    return (float(np.quantile(m, .05)), float(np.quantile(m, .95)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--monedas", default=",".join(MONEDAS))
    ap.add_argument("--desde", default="")
    a = ap.parse_args()
    filas, faltan = [], []
    for mo in a.monedas.split(","):
        f = DL / f"experimento_pares_dedicada_seco_{mo}_ledger.jsonl"
        if not f.exists():
            faltan.append(mo)
            continue
        for ln in f.read_text().splitlines():
            try:
                e = json.loads(ln)
            except ValueError:
                continue
            if e.get("tipo") != "mercado_fin" or e.get("real") or e.get("ts", "") < a.desde or not e.get("medido"):
                continue
            r = e.get("rellenos") or {}
            acc = {s: sum(x["acc"] for x in r.get(s, [])) for s in ("YES", "NO")}
            coste = {s: sum(x["acc"] * x["precio"] for x in r.get(s, [])) for s in ("YES", "NO")}
            reb = sum(0.2 * 0.07 * x["precio"] * (1 - x["precio"]) * x["acc"] for s in ("YES", "NO") for x in r.get(s, []))
            filas.append({"moneda": mo, "id": str(e["id"]), "ts": e.get("ts", ""), "pol": e.get("politica"), "acc": acc,
                          "coste": coste, "reb": reb, "cortado": bool(e.get("kill") or e.get("senal"))})
    if faltan:
        print(f"sin ledger de ensayo: {','.join(faltan)}")
    if not filas:
        print("sin mercados medidos")
        return
    des = ganadores([x["id"] for x in filas])
    ok = [x for x in filas if x["id"] in des]
    print(f"Ensayo en seco con rellenos simulados: {len(filas)} mercados medidos ({min(x['ts'] for x in filas)[:16]} → "
          f"{max(x['ts'] for x in filas)[:16]}), con desenlace oficial {len(ok)} ({len(ok) / len(filas):.0%}); "
          f"cortados por kill/señal {sum(x['cortado'] for x in filas)} (aparte)")
    g = defaultdict(list)
    for x in ok:
        d = des[x["id"]]
        x["pnl"] = x["acc"][d] - x["coste"]["YES"] - x["coste"]["NO"]
        x["par"] = min(x["acc"]["YES"], x["acc"]["NO"])
        clave = "cortados" if x["cortado"] else x["pol"]
        g[(x["moneda"], clave)].append(x)
        g[("TODAS", clave)].append(x)
    print(f"{'moneda':6s} {'política':9s} {'merc':>4s} {'relleno':>7s} {'par':>4s} {'1 pata':>6s} {'PnL $':>8s} "
          f"{'$/merc':>7s} {'IC90 $/merc':>17s} {'sin 2 mejores':>13s} {'reemb $':>7s} {'coste par':>9s}")
    for (mo, pol), xs in sorted(g.items()):
        conr = [x for x in xs if x["acc"]["YES"] + x["acc"]["NO"] > 0]
        pares = [x for x in xs if x["par"] > 0]
        cpar = [(x["coste"]["YES"] / x["acc"]["YES"] + x["coste"]["NO"] / x["acc"]["NO"]) for x in pares]
        v = [x["pnl"] for x in xs]
        lo, hi = ic90(v)
        sin2 = sorted(v)[:-2] if len(v) > 2 else []
        print(f"{mo:6s} {pol:9s} {len(xs):4d} {len(conr):7d} {len(pares):4d} {len(conr) - len(pares):6d} {sum(v):+8.2f} "
              f"{np.mean(v):+7.3f} ({lo:+7.3f},{hi:+7.3f}) {(np.mean(sin2) if sin2 else float('nan')):+13.3f} "
              f"{sum(x['reb'] for x in xs):7.3f} {(np.mean(cpar) if cpar else float('nan')):9.3f}")
    print("\nSimulación: cola entera delante al unirse, sin cancelaciones en la cola, acuñación incluida, latencias de "
          "envío/cancelación medidas. n pequeño = orientativo, no es un gate.")


if __name__ == "__main__":
    main()
