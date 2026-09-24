#!/usr/bin/env python3
"""analisis_leadlag_chainlink_libro_24sep.py -- A3 "ganarles al entrar" (24-Sep, Javi), FASE 0 medición.

Pregunta: cuando el precio JUSTO de un mercado Up/Down (derivado de Chainlink con la regla real
TWAP) salta, ¿cuántos segundos tarda el mercado de Polymarket en incorporarlo, y qué EV tendríamos
entrando L segundos después al precio que marca el mercado en ese instante?

Datos (un día, 5/15min, 6 monedas):
  - Chainlink: data/prices/chainlink_{dia}.csv(.gz) -- hora de RECEPCIÓN (timestamp_utc) para saber
    cuándo lo sabríamos nosotros; los valores se ordenan por esa hora.
  - Trades: datalogs/polymarket_activity_{dia}.csv -- precio de Up por segundo (Down -> 1-precio),
    mediana de los trades del segundo; hora de recepción del websocket (misma tubería RTDS).
Precio justo en t: ref = media Chainlink [apertura-60, apertura]; proy = spot (>60 s) o TWAP
proyectado (último minuto); p = Phi(ln(proy/ref) / (sigma_1s * sqrt(T_eff))), T_eff como
shadow_predict._t_efectivo_twap_h (suelo 15 s); sigma de los últimos 300 s, recalculada cada 60 s.
Resultado del mercado: regla TWAP con Chainlink (99,0-99,8 % de acierto verificado 24-Sep).
Evento: |p_justo(t) - p_justo(t-2)| >= SALTO y |p_justo(t) - p_mkt(t)| >= SALTO (el mercado aún no
lo tiene); un evento por mercado cada 20 s como máximo. Entrada simulada a p_mkt(t+L) (último trade
conocido en t+L, NO el ask: cota optimista, sin profundidad) en la dirección del salto.
Uso: python3 analisis_leadlag_chainlink_libro_24sep.py [YYYY-MM-DD]
"""
import bisect
import csv
import gzip
import json
import math
import statistics
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
DATALOGS = Path("/root/polymarket-research-datalogs")
DUR = {"5min": 300, "15min": 900}
ACTIVOS = {"BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"}
SALTO = 0.08
LAGS = (0, 0.5, 1, 2, 5, 10, 30)
FEE = 0.07
csv.field_size_limit(10_000_000)


def ts(s):
    d = datetime.fromisoformat(s.replace("Z", "+00:00"))
    return (d if d.tzinfo else d.replace(tzinfo=timezone.utc)).timestamp()


def abrir(p):
    return gzip.open(p, "rt") if str(p).endswith(".gz") else open(p)


def phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def chainlink(dia):
    s = defaultdict(lambda: ([], []))
    for p in (REPO / f"data/prices/chainlink_{dia}.csv", REPO / f"data/prices/chainlink_{dia}.csv.gz"):
        if not p.exists():
            continue
        with abrir(p) as f:
            for r in csv.DictReader(f):
                try:
                    s[r["asset"]][0].append(ts(r["timestamp_utc"]))
                    s[r["asset"]][1].append(float(r["price_usd"]))
                except (ValueError, KeyError):
                    continue
    out = {}
    for a, (xs, ys) in s.items():
        o = sorted(zip(xs, ys))
        out[a] = ([x for x, _ in o], [y for _, y in o])
    return out


def trades(dia):
    """{market_slug: {'activo','marco','t':[seg], 'p':[precio Up mediano del segundo]}}"""
    por = defaultdict(lambda: defaultdict(list))
    meta = {}
    p = DATALOGS / f"polymarket_activity_{dia}.csv"
    if not p.exists():
        p = DATALOGS / f"polymarket_activity_{dia}.csv.gz"
    with abrir(p) as f:
        for r in csv.DictReader(f):
            if r.get("marco") not in DUR or r.get("activo") not in ACTIVOS:
                continue
            try:
                t = ts(r["timestamp_utc"])
                pr = float(r["price"])
            except (ValueError, KeyError):
                continue
            if not 0.0 < pr < 1.0:
                continue
            up = pr if r.get("outcome") == "Up" else 1 - pr if r.get("outcome") == "Down" else None
            if up is None:
                continue
            m = r["market_slug"]
            meta[m] = (r["activo"], r["marco"])
            por[m][int(t)].append(up)
    out = {}
    for m, seg in por.items():
        xs = sorted(seg)
        out[m] = {"activo": meta[m][0], "marco": meta[m][1], "t": xs,
                  "p": [statistics.median(seg[x]) for x in xs]}
    return out


def media(xs, ys, t0, t1):
    i, j = bisect.bisect_left(xs, t0), bisect.bisect_right(xs, t1)
    return (sum(ys[i:j]) / (j - i), j - i) if j > i else (None, 0)


def sigma_1s(xs, ys, t):
    j, i = bisect.bisect_left(xs, t - 300), bisect.bisect_right(xs, t) - 1
    r = [math.log(ys[k + 1] / ys[k]) / math.sqrt(max(xs[k + 1] - xs[k], 1e-3)) for k in range(j, i)
         if ys[k] > 0 and ys[k + 1] > 0 and xs[k + 1] > xs[k]]
    return statistics.pstdev(r) if len(r) >= 30 else None


def p_justo(xs, ys, t, ini, fin, sig):
    ref, nr = media(xs, ys, ini - 60, ini)
    i = bisect.bisect_right(xs, t) - 1
    if ref is None or nr < 10 or i < 0 or t - xs[i] > 5 or not sig:
        return None
    spot, resto = ys[i], max(0.0, fin - t)
    if resto > 60:
        proy = spot
    else:
        m, n = media(xs, ys, fin - 60, t)
        if m is None or n < 5:
            return None
        tr = t - (fin - 60)
        proy = (m * tr + spot * resto) / 60.0
    teff = max(resto - 40 if resto > 60 else resto ** 3 / (3 * 3600), 15.0)
    return phi(math.log(proy / ref) / (sig * math.sqrt(teff)))


def p_mkt(mk, t):
    i = bisect.bisect_right(mk["t"], t) - 1
    return mk["p"][i] if i >= 0 and t - mk["t"][i] <= 20 else None


def main():
    dia = sys.argv[1] if len(sys.argv) > 1 else "2026-09-23"
    cl = chainlink(dia)
    tr = trades(dia)
    print(f"{dia}: chainlink {sorted(cl)}, mercados con trades {len(tr)}", flush=True)
    eventos = []
    for slug, mk in tr.items():
        a, marco = mk["activo"], mk["marco"]
        if a not in cl:
            continue
        try:
            ini = int(slug.rsplit("-", 1)[1])
        except ValueError:
            continue
        fin = ini + DUR[marco]
        xs, ys = cl[a]
        # resultado por regla TWAP
        r0, n0 = media(xs, ys, ini - 60, ini)
        r1, n1 = media(xs, ys, fin - 60, fin)
        if not r0 or not r1 or n0 < 10 or n1 < 10 or r0 == r1:
            continue
        up_gana = r1 > r0
        sig, sig_t, ult_ev, prev = None, -1e9, -1e9, None
        for t in range(ini + 5, fin - 3):
            if t - sig_t >= 60:
                sig, sig_t = sigma_1s(xs, ys, t), t
            pj = p_justo(xs, ys, t, ini, fin, sig)
            if pj is None:
                prev = None
                continue
            if prev is not None and t - ult_ev >= 20:
                pm = p_mkt(mk, t)
                if pm is not None and abs(pj - prev) >= SALTO and abs(pj - pm) >= SALTO \
                        and (pj - prev) * (pj - pm) > 0:
                    sube = pj > pm
                    ev = {"activo": a, "marco": marco, "t": t, "resto": fin - t, "pj": pj, "pm0": pm,
                          "sube": sube, "gana": up_gana == sube}
                    for L in LAGS:
                        pl = p_mkt(mk, t + L)
                        if pl is None:
                            continue
                        entry = pl if sube else 1 - pl
                        if 0.01 < entry < 0.99:
                            ev[f"pnl_L{L}"] = (1 - entry) / entry * (1 - FEE) if ev["gana"] else -1.0
                            ev[f"entry_L{L}"] = entry
                    # segundos hasta cerrar la mitad del hueco
                    obj = pm + (pj - pm) / 2
                    ev["lag_mitad"] = next((s for s in range(1, 61)
                                            if (p_mkt(mk, t + s) is not None
                                                and ((p_mkt(mk, t + s) >= obj) if sube else (p_mkt(mk, t + s) <= obj)))),
                                           None)
                    eventos.append(ev)
                    ult_ev = t
            prev = pj
    print(f"eventos: {len(eventos)}")
    res = {}
    grupos = defaultdict(list)
    for e in eventos:
        grupos["TODOS"].append(e)
        grupos[e["marco"]].append(e)
        grupos[f"{e['activo']}#{e['marco']}"].append(e)
    for g, es in sorted(grupos.items()):
        lagm = sorted(e["lag_mitad"] for e in es if e["lag_mitad"] is not None)
        d = {"n": len(es), "acierto": round(sum(e["gana"] for e in es) / len(es), 3),
             "lag_mitad_mediana_s": lagm[len(lagm) // 2] if lagm else None,
             "sin_cerrar_mitad_60s": sum(1 for e in es if e["lag_mitad"] is None)}
        for L in LAGS:
            v = [e[f"pnl_L{L}"] for e in es if f"pnl_L{L}" in e]
            en = [e[f"entry_L{L}"] for e in es if f"entry_L{L}" in e]
            if v:
                d[f"L{L}"] = {"n": len(v), "pnl_tr": round(sum(v) / len(v), 3), "entry_medio": round(sum(en) / len(en), 3)}
        res[g] = d
        if d["n"] >= 20:
            print(g.ljust(12), f"n={d['n']} acierto={d['acierto']:.0%} lag½={d['lag_mitad_mediana_s']}s",
                  " ".join(f"L{L}:{d[f'L{L}']['pnl_tr']:+.3f}@{d[f'L{L}']['entry_medio']:.2f}" for L in LAGS if f"L{L}" in d))
    out = REPO / f"data/shadow/leadlag_chainlink_libro_{dia}.json"
    out.write_text(json.dumps({"dia": dia, "salto": SALTO, "grupos": res}, indent=1), encoding="utf-8")
    print(f"-> {out}")


if __name__ == "__main__":
    main()
