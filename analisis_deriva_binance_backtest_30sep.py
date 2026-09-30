#!/usr/bin/env python3
"""analisis_deriva_binance_backtest_30sep.py -- ¿se puede disparar con el MISMO evento que las
tomadoras que ganan? Ellas compran el lado a favor de un movimiento de Binance de ~1-3 bps en los
2-5 s previos (19 % de sus compras siguen a un movimiento >2 bps en 3 s; control 6 %).

Backtest sin mirar al futuro, 1 entrada por mercado (primer disparo):
  disparo  : en el instante s, |retorno de Binance en los últimos 3 s| >= theta bps (mid bookTicker).
  lado     : Up si subió, Down si bajó, en el mercado up/down en curso de esa moneda (5 y 15 min),
             con >= 30 s por delante y >= 20 s desde la apertura.
  precio   : no hay libro histórico sub-segundo, así que se usa el precio al que de verdad se
             negoció ese lado justo después: trades EJECUTADOS (ws_timestamp, hora del exchange) en
             los 2 segundos enteros siguientes al del disparo. MEDIANA y MÁXIMO (pesimista).
  resultado: a resolución, fee tomador 7 %.
Entrenamiento = primer día, validación = resto. Solo lectura.
Uso: python3 analisis_deriva_binance_backtest_30sep.py 2026-09-25 2026-09-28 2026-09-29
"""
import bisect, csv, gzip, random, statistics as st, sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
REPO = Path(__file__).resolve().parent; DATALOGS = Path("/root/polymarket-research-datalogs")
THETAS = (1.0, 1.5, 2.0, 3.0, 5.0); MARCOS = {"5m": 300, "15m": 900}
def ab(p): return gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")
def ruta(d, pre, dia):
    for c in (d / f"{pre}_{dia}.csv", d / f"{pre}_{dia}.csv.gz"):
        if c.exists(): return c
def ts(s): return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()
def main():
    dias = sys.argv[1:] or ["2026-09-25", "2026-09-28", "2026-09-29"]
    R = defaultdict(lambda: defaultdict(list))     # (theta, marco, version) -> dia -> [(pnl, acierto, precio, activo, resto)]
    for dia in dias:
        pb, pa, po = ruta(DATALOGS, "binance_bookticker", dia), ruta(DATALOGS, "polymarket_activity", dia), ruta(REPO / "data/shadow", "resolution_sniper_obs", dia)
        if not (pb and pa and po): print(dia, "faltan ficheros"); continue
        out = {}
        with ab(po) as f:
            for r in csv.DictReader(f):
                if r.get("outcome_real") in ("Up", "Down"): out[r["slug"]] = r["outcome_real"]
        B = defaultdict(lambda: ([], []))
        with ab(pb) as f:
            for r in csv.DictReader(f):
                try: B[r["activo"]][0].append(int(r["ts_recepcion_ms"]) / 1000); B[r["activo"]][1].append(float(r["mid"]))
                except (ValueError, TypeError): pass
        P = defaultdict(list)
        with ab(pa) as f:
            for r in csv.DictReader(f):
                if r["market_slug"] not in out or r["outcome"] not in ("Up", "Down"): continue
                try: p, t = float(r["price"]), float(r["ws_timestamp"])     # segundo de EJECUCIÓN en el exchange
                except (ValueError, TypeError): continue
                if 0 < p < 1: P[r["market_slug"]].append((t, p if r["outcome"] == "Up" else 1 - p))
        T = {}
        for s in P: P[s].sort(); T[s] = [x[0] for x in P[s]]
        n_ev = 0
        for activo, (bt, bm) in B.items():
            if len(bt) < 1000: continue
            hechos = {th: set() for th in THETAS}
            j0 = 0
            for i in range(len(bt)):
                t = bt[i]
                while bt[j0] < t - 3.0: j0 += 1
                if j0 == 0 or t - bt[j0 - 1] > 6: continue            # hueco en la captura
                mov = (bm[i] / bm[j0 - 1] - 1) * 1e4
                am = abs(mov)
                if am < THETAS[0]: continue
                lado = "Up" if mov > 0 else "Down"
                for tag, dur in MARCOS.items():
                    ini = int(t) - int(t) % dur; slug = f"{activo.lower()}-updown-{tag}-{ini}"
                    if slug not in out or t - ini < 20 or ini + dur - t < 30: continue
                    # trades EJECUTADOS en los 2 segundos enteros siguientes al del disparo (nunca el mismo
                    # segundo: no se sabe si fue antes o después) -> entre >0 y <3 s después, hora del exchange
                    a, b = bisect.bisect_left(T[slug], int(t) + 1), bisect.bisect_right(T[slug], int(t) + 2)
                    if b <= a: continue
                    px = [(u if lado == "Up" else 1 - u) for _, u in P[slug][a:b]]
                    for th in THETAS:
                        if am < th or slug in hechos[th]: continue
                        hechos[th].add(slug)
                        ac = 1 if out[slug] == lado else 0
                        for ver, p in (("mediana", st.median(px)), ("maximo", max(px))):
                            if 0.05 <= p < 0.95:
                                R[(th, tag, ver)][dia].append((ac / p - 1 - 0.07 * (1 - p), ac, p, activo, ini + dur - t)); n_ev += 1
        print(dia, "entradas simuladas:", n_ev, flush=True)
    dias_ok = sorted({d for v in R.values() for d in v})
    if not dias_ok: return 1
    def res(vd, filtro=lambda x: True):
        vd = {d: [x for x in v if filtro(x)] for d, v in vd.items()}; x = [y for v in vd.values() for y in v]
        if len(x) < 40: return "(n<40)"
        por_dia = " ".join(f"{d[-2:]}:{sum(y[0] for y in v) / len(v):+.3f}" if v else f"{d[-2:]}:-" for d, v in sorted(vd.items()))
        return f"n={len(x):5d} hit {sum(y[1] for y in x) / len(x):.1%} precio {sum(y[2] for y in x) / len(x):.3f} EV/€ {sum(y[0] for y in x) / len(x):+.4f} | por día {por_dia}"
    for tag in MARCOS:
        print(f"\n== mercados de {tag} ==")
        for th in THETAS:
            for ver in ("mediana", "maximo"):
                print(f"theta>={th:3.1f} bps precio={ver:7s} {res(R[(th, tag, ver)])}")
        th = 2.0
        print(f"  desglose theta>=2 (precio máximo, pesimista):")
        for nombre, f in (("precio 0,05-0,40", lambda x: x[2] < 0.40), ("precio 0,40-0,60", lambda x: 0.40 <= x[2] < 0.60), ("precio 0,60-0,80", lambda x: 0.60 <= x[2] < 0.80), ("precio 0,80-0,95", lambda x: x[2] >= 0.80),
                          ("quedan >120 s", lambda x: x[4] > 120), ("quedan 30-120 s", lambda x: x[4] <= 120)) + tuple((a, (lambda x, a=a: x[3] == a)) for a in ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")):
            print(f"    {nombre:18s} {res(R[(th, tag, 'maximo')], f)}")
    return 0
if __name__ == "__main__": sys.exit(main())
