#!/usr/bin/env python3
"""analisis_pares15_filtro_entrada.py -- misión «pares 15m» (12-Oct), filtro de ENTRADA. SOLO LECTURA.
¿Se puede predecir, con información disponible ANTES de pujar (apertura del 15m, T=898 s), qué mercados acaban con pata
suelta? Para cada mercado del ensayo en seco (ledgers _seco_{sol,btc}) calcula en t_ent = apertura + 2 s (recepción):
  libro (m15_registro, q): bid/ask de YES y NO, spread de cada lado, margen potencial del par en el mejor bid
  (1 - bidYES - bidNO), desequilibrio de tamaños en el bid, |mid YES - 0,5|;
  Binance (filas x del mismo archivo, aggTrade): retorno 60 s y 300 s previos (|·|) y nº de operaciones en 60 s.
Resultado por mercado: par / suelta / nada y PnL original (pnl_original de analisis_pares15_patas_sueltas). Muestra por
terciles de cada variable: % suelta y PnL/mercado. Con --desde/--hasta se elige el periodo (DESCUBRIMIENTO 09-10 Oct por
defecto; la validación es el ensayo 'crear' desde 12-Oct 14:59Z).
"""
import argparse
import bisect
import collections
import gzip
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from analisis_experimento_pares_sim import ganadores  # noqa: E402
from analisis_pares15_patas_sueltas import REG, cargar_libros, cargar_mercados, libro_en, pnl_original  # noqa: E402

SIMB = {"BTC": "BTCUSDT", "SOL": "SOLUSDT"}


def cargar_binance(dias):
    out = collections.defaultdict(lambda: ([], []))
    for d in dias:
        f = REG / f"m15_registro_{d}.csv.gz"
        if not f.exists():
            continue
        with gzip.open(f, "rt", errors="replace") as fh:
            try:
                for ln in fh:
                    if ln.startswith("x,"):
                        c = ln.rstrip("\n").split(",")
                        if c[2] in SIMB.values():
                            try:
                                out[c[2]][0].append(int(c[7]) if len(c) > 7 and c[7] else int(c[1]))
                                out[c[2]][1].append(float(c[3]))
                            except (ValueError, IndexError):
                                continue
            except (EOFError, OSError):
                pass
    for k, (t, p) in out.items():
        o = sorted(range(len(t)), key=t.__getitem__)
        out[k] = ([t[i] for i in o], [p[i] for i in o])
    return out


def precio_bn(B, sym, t):
    ts, ps = B.get(sym, ([], []))
    i = bisect.bisect_right(ts, t) - 1
    return ps[i] if i >= 0 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-10-09")
    ap.add_argument("--hasta", default="2026-10-12")
    a = ap.parse_args()
    M = cargar_mercados(a.desde, a.hasta)
    des = ganadores([m["id"] for m in M])
    M = [m for m in M if m["id"] in des]
    L = cargar_libros(M)
    dias = sorted({datetime.fromtimestamp(m["cierre"], timezone.utc).date().isoformat() for m in M})
    B = cargar_binance(dias)
    F = []
    for m in M:
        o = pnl_original(m, des[m["id"]])
        t = (m["cierre"] - 900) * 1000 + 2000
        y, n = libro_en(L, m["id"], "YES", t), libro_en(L, m["id"], "NO", t)
        if not (y and n and None not in (y[0], y[1], n[0], n[1])):
            continue
        sym = SIMB[m["moneda"]]
        p0, p60, p300 = precio_bn(B, sym, t), precio_bn(B, sym, t - 60000), precio_bn(B, sym, t - 300000)
        ts, _ = B.get(sym, ([], []))
        nops = bisect.bisect_right(ts, t) - bisect.bisect_right(ts, t - 60000)
        res = "par" if o["par"] >= 5 - 1e-9 else ("suelta" if o["lado_res"] else "nada")
        F.append({"res": res, "pnl": o["pnl_par"] + o["pnl_res"], "moneda": m["moneda"], "pol": m["pol"],
                  "margen_bid": 1 - y[0] - n[0], "spread_yes": y[1] - y[0], "spread_no": n[1] - n[0],
                  "desequilibrio_bid": (y[2] - n[2]) / (y[2] + n[2]) if (y[2] + n[2]) > 0 else 0.0,
                  "dist_mid": abs((y[0] + y[1]) / 2 - 0.5),
                  "bn_ret60_abs_bps": abs(p0 / p60 - 1) * 1e4 if p0 and p60 else None,
                  "bn_ret300_abs_bps": abs(p0 / p300 - 1) * 1e4 if p0 and p300 else None, "bn_ops60": nops})
    print(f"mercados con libro en la apertura: {len(F)} de {len(M)} ({a.desde} → {a.hasta}); par {sum(f['res'] == 'par' for f in F)}, "
          f"suelta {sum(f['res'] == 'suelta' for f in F)}, nada {sum(f['res'] == 'nada' for f in F)}; PnL total {sum(f['pnl'] for f in F):+.2f} $\n")
    print(f"{'variable (en la apertura)':22} {'tercil':>6} {'rango':>17} {'n':>3} {'% suelta':>8} {'% par':>6} {'PnL/merc':>8}")
    for var in ("margen_bid", "spread_yes", "spread_no", "desequilibrio_bid", "dist_mid", "bn_ret60_abs_bps", "bn_ret300_abs_bps", "bn_ops60"):
        v = sorted((f for f in F if f[var] is not None), key=lambda f: f[var])
        if len(v) < 9:
            continue
        k = len(v) // 3
        for i, g in enumerate((v[:k], v[k:2 * k], v[2 * k:])):
            print(f"{var:22} {i + 1:>6} [{g[0][var]:+7.3f},{g[-1][var]:+7.3f}] {len(g):3d} {sum(x['res'] == 'suelta' for x in g) / len(g):8.0%} "
                  f"{sum(x['res'] == 'par' for x in g) / len(g):6.0%} {sum(x['pnl'] for x in g) / len(g):+8.3f}")
        print()


if __name__ == "__main__":
    main()
