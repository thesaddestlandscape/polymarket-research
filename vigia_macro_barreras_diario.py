#!/usr/bin/env python3
"""vigia_macro_barreras_diario.py -- informe DIARIO Telegram (29-Sep) de las dos FASE 0 de micro-latencia:
 (a) macro_release_ms_fase0 (ronda1 #7): latencia hasta conocer el dato oficial tras la hora de publicación;
 (b) barreras_touch_ms_fase0 (ronda2 #5): tras el trade de Binance que cruza el strike, ¿cuánto queda ejecutable
     en el libro del YES (ask<0,97) a +50..+10000 ms? SIEMPRE envía. Cron 09:15 UTC."""
import csv
import statistics as st
import sys
from collections import defaultdict
from pathlib import Path
REPO = Path(__file__).resolve().parent


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def main():
    L = ["⚡ *Micro-latencia: datos macro y barreras (FASE 0)* — informe diario"]
    m = REPO / "data/shadow/macro_release_ms_fase0.csv"
    if m.exists():
        R = list(csv.DictReader(open(m, encoding="utf-8")))
        ok = [r for r in R if r["estado"] == "ok"]
        L.append(f"Macro: {len(R)} eventos sondeados, {len(ok)} con dato capturado.")
        for r in R[-4:]:
            if r["estado"] == "ok":
                L.append(f"· {r['evento']}: dato en {r['latencia_desde_publicacion_ms']} ms tras la hora oficial "
                         f"({r['n_polls']} polls, RTT {r['rtt_ultimo_ms']} ms), var {r['var_pct']}% → bin {r['bin_ganador']}")
            else:
                L.append(f"· {r['evento']}: {r['estado']} ({r['n_polls']} polls)")
    else:
        L.append("Macro: aún sin eventos.")
    b = REPO / "data/shadow/barreras_touch_ms_fase0.csv"
    if b.exists():
        R = list(csv.DictReader(open(b, encoding="utf-8")))
        ev = defaultdict(dict)
        for r in R:
            ev[(r["market_id"], r["t_trade_ms"])][int(r["offset_ms"])] = r
        L.append(f"Barreras: {len(ev)} cruces de strike detectados (latencia de feed mediana "
                 f"{st.median(_f(r['latencia_feed_ms']) for r in R if _f(r['latencia_feed_ms']) is not None):.0f} ms).")
        for off in (-1000, 100, 500, 1000, 3000, 10000):
            asks = [_f(d[off]["best_ask"]) for d in ev.values() if off in d and _f(d[off]["best_ask"]) is not None]
            if asks:
                L.append(f"· a {off:+d} ms del trade: ask YES mediano {st.median(asks):.3f}, "
                         f"{sum(a < 0.97 for a in asks)}/{len(asks)} aún <0,97 (ejecutables)")
        L.append("Gate: n>=30 cruces con ask<0,97 a +250 ms antes de pensar en un ejecutor con envío de baja latencia.")
    else:
        L.append("Barreras: aún sin cruces (strikes a <=2 % del spot; suelen tardar horas).")
    a = REPO / "data/shadow/escaleras_arbitraje_ms_fase0.csv"
    if a.exists():
        R = list(csv.DictReader(open(a, encoding="utf-8")))
        neto = [_f(r["edge_neto_max"]) for r in R if _f(r["edge_neto_max"]) is not None]
        dur = [_f(r["duracion_ms"]) for r in R if _f(r["duracion_ms"]) is not None]
        L.append(f"Arbitraje de monotonía entre strikes (50 ms): {len(R)} episodios; duración mediana "
                 f"{st.median(dur):.0f} ms; edge bruto máx {max(_f(r['edge_bruto_max']) for r in R):.3f}; "
                 f"{sum(n > 0 for n in neto)} con edge NETO de fee >0; tamaño ejecutable máx {max(_f(r['size_min_max']) or 0 for r in R):.0f} acciones.")
    else:
        L.append("Arbitraje de monotonía entre strikes: sin episodios (edge bruto >=0,5c) todavía.")
    import glob, gzip
    fc = sorted(glob.glob("/root/polymarket-research-datalogs/colas_escaleras_ws_*.csv.gz"))
    if fc:
        C = []
        for f_ in fc[-3:]:
            C += list(csv.DictReader(gzip.open(f_, "rt", encoding="utf-8")))
        por = defaultdict(list)
        for r in C:
            if r["token"] == "YES" and _f(r["best_bid"]) is not None:
                por[int(r["offset_s"])].append(r)
        for off in (-900, -300, -60):
            v = por.get(off, [])
            if v:
                bids = [_f(r["best_bid"]) for r in v]
                L.append(f"Colas horarias (strikes 1-6 % del spot) a {off // 60:+d} min: n={len(v)}, bid YES mediano {st.median(bids):.3f}, "
                         f"{sum(b >= 0.02 for b in bids)}/{len(v)} con bid>=2c (comprar NO a <=0,98 posible)")
    msg = "\n".join(L)
    print(msg)
    try:
        sys.path.insert(0, str(REPO))
        from shadow_digest import enviar_telegram
        enviar_telegram(msg, bot="cripto")
    except Exception as e:
        print(f"[vigia_macro_barreras_diario] error Telegram: {e}")


if __name__ == "__main__":
    main()
