#!/usr/bin/env python3
"""analisis_ventana_w_binance_polymarket.py -- mide la VENTANA DE MERCADO W = t2 - t0 entre un movimiento de Binance y su
incorporación en Polymarket (up/down 5m y 15m), con hora del EXCHANGE en ambos lados (programa
informes/latency_alpha_window_programa_05oct.md, medición M1). Fuente: registro maker_ms_*.csv.gz (x = aggTrade Binance
con T del exchange; q = top de Polymarket sin muestrear con hora del exchange; k = mapa de tokens).

Definiciones (fijadas antes de mirar):
- t0: T del aggTrade de Binance que completa un movimiento >= UMBRAL bps (por moneda) respecto al precio de hace <= 1 s.
  Eventos de una moneda separados >= 3 s (se toma el primero).
- Mercado: el token YES del mercado VIVO de esa moneda (t0 dentro de su ventana, >= 20 s antes del cierre) en 5m y 15m.
- mid(t) = (bid+ask)/2 del top de Polymarket (q). Ajuste final A = mid(t0 + 5 s) - mid(t0); solo eventos con
  |A| >= 0,01 en la dirección del movimiento (si Polymarket no se mueve, no hay W que medir: se cuenta aparte).
- t1: primer cambio del mid >= 0,01 en la dirección del movimiento tras t0.
- t2(f): primer instante en que mid - mid(t0) alcanza f*A, f = 0,25/0,50/0,75/0,90.
- Pre-alpha: cuánto del ajuste ya había ocurrido entre t0 - 1 s y t0 (Polymarket moviéndose ANTES que Binance).
Reloj: el de cada exchange (Binance T, Polymarket timestamp). Cota de error de nuestro reloj ~21 ms (chrony); los relojes de
los exchanges no se pueden auditar desde aquí: buckets < 10-25 ms no son sostenibles.
Uso: python3 analisis_ventana_w_binance_polymarket.py --desde YYYY-MM-DD [--hasta YYYY-MM-DD] [--umbral 2]
"""
import argparse
import bisect
import collections
import datetime as dt
import gzip
import sys
from pathlib import Path

DATALOGS = Path("/root/polymarket-research-datalogs")
ESCALA = {"BTC": 1.0, "ETH": 1.2, "SOL": 1.6, "XRP": 1.6, "DOGE": 2.0, "BNB": 1.2}
SIM2ACT = {"BTCUSDT": "BTC", "ETHUSDT": "ETH", "SOLUSDT": "SOL", "XRPUSDT": "XRP", "DOGEUSDT": "DOGE", "BNBUSDT": "BNB"}


def leer(dias):
    meta, top, binance = {}, collections.defaultdict(list), collections.defaultdict(list)
    for dia in dias:
        for f in sorted(DATALOGS.glob(f"maker_ms_{dia}_*.csv.gz")):
            try:
                with gzip.open(f, "rt", encoding="utf-8") as fh:
                    for linea in fh:
                        r = linea.rstrip("\n").split(",")
                        try:
                            if r[0] == "q" and r[3] not in ("", "None") and r[4] not in ("", "None"):
                                top[r[2]].append((int(r[1]), (float(r[3]) + float(r[4])) / 2))
                            elif r[0] == "x":
                                binance[SIM2ACT.get(r[2])].append((int(r[1]), float(r[3])))
                            elif r[0] == "k":
                                meta[r[2]] = (r[3], r[4], r[5], r[6], r[7])
                        except (ValueError, IndexError):
                            continue
            except (EOFError, OSError, gzip.BadGzipFile) as e:
                print(f"  aviso: {f.name} truncado ({type(e).__name__}); se usa lo leído", file=sys.stderr)
    for d in (top, binance):
        for k in d:
            d[k].sort()
    return meta, top, binance


def eventos(serie, umbral):
    out, ult = [], -10 ** 15
    ts = [x[0] for x in serie]
    j = 0
    for i, (t, p) in enumerate(serie):
        while ts[j] < t - 1000:
            j += 1
        ref = min(serie[j:i + 1], key=lambda x: x[0])[1] if i > j else None
        if ref is None:
            continue
        lo = min(x[1] for x in serie[j:i + 1])
        hi = max(x[1] for x in serie[j:i + 1])
        sube = (p / lo - 1) * 1e4 >= umbral
        baja = (1 - p / hi) * 1e4 >= umbral
        if (sube or baja) and t - ult >= 3000:
            out.append((t, 1 if sube else -1))
            ult = t
    return out


def mid_en(serie_t, serie_m, t):
    i = bisect.bisect_right(serie_t, t) - 1
    return serie_m[i] if i >= 0 else None


def pct(v, q):
    v = sorted(v)
    return v[min(len(v) - 1, int(q * len(v)))] if v else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", required=True)
    ap.add_argument("--hasta")
    ap.add_argument("--umbral", type=float, default=2.0, help="bps para BTC; se escala por moneda")
    a = ap.parse_args()
    d0 = dt.date.fromisoformat(a.desde)
    d1 = dt.date.fromisoformat(a.hasta) if a.hasta else d0
    dias = [(d0 + dt.timedelta(days=i)).isoformat() for i in range((d1 - d0).days + 1)]
    meta, top, binance = leer(dias)
    yes_por_act = collections.defaultdict(list)          # (act, marco) -> [(t_ini, t_fin, token)]
    for tk, (act, marco, mid, fin, lado) in meta.items():
        if lado != "YES" or marco not in ("5min", "15min"):
            continue
        try:
            t_fin = int(dt.datetime.fromisoformat(fin).timestamp() * 1000)
        except ValueError:
            continue
        dur = 300000 if marco == "5min" else 900000
        yes_por_act[(act, marco)].append((t_fin - dur, t_fin, tk))
    res = collections.defaultdict(list)
    sin_mov = collections.Counter()
    pre = collections.defaultdict(list)
    for act, serie in binance.items():
        if not act:
            continue
        for t0, sgn in eventos(serie, a.umbral * ESCALA[act]):
            for marco in ("5min", "15min"):
                vivos = [tk for ti, tf, tk in yes_por_act[(act, marco)] if ti <= t0 <= tf - 20000 and tk in top]
                if not vivos:
                    continue
                s = top[vivos[0]]
                st, sm = [x[0] for x in s], [x[1] for x in s]
                m0, m5, mpre = mid_en(st, sm, t0), mid_en(st, sm, t0 + 5000), mid_en(st, sm, t0 - 1000)
                if m0 is None or m5 is None:
                    continue
                A = m5 - m0
                if A * sgn < 0.01 - 1e-9:
                    sin_mov[(act, marco)] += 1
                    continue
                if mpre is not None:
                    pre[(act, marco)].append((m0 - mpre) / A)
                i0 = bisect.bisect_right(st, t0)
                t1, t2 = None, {}
                for t, m in zip(st[i0:], sm[i0:]):
                    if t > t0 + 5000:
                        break
                    d = (m - m0) * sgn
                    if t1 is None and d >= 0.01 - 1e-9:
                        t1 = t - t0
                    for f in (0.25, 0.5, 0.75, 0.9):
                        if f not in t2 and d >= f * abs(A) - 1e-9:
                            t2[f] = t - t0
                res[(act, marco)].append((t1, t2, abs(A)))
    todos = [x for v in res.values() for x in v]
    print(f"días {dias}  umbral {a.umbral} bps (BTC, escalado por moneda)")
    print(f"eventos con ajuste de Polymarket >= 1c: {len(todos)}; sin ajuste: {sum(sin_mov.values())}")
    def fila(nombre, xs):
        if not xs:
            return
        t1 = [x[0] for x in xs if x[0] is not None]
        partes = [f"{nombre:14} n={len(xs):4} ajuste_med={sum(x[2] for x in xs) / len(xs) * 100:.1f}c",
                  "t1 p10/50/90=" + "/".join(str(pct(t1, q)) for q in (0.1, 0.5, 0.9))]
        for f in (0.5, 0.9):
            v = [x[1][f] for x in xs if f in x[1]]
            partes.append(f"t2({int(f * 100)}%) p10/25/50/75/90/95/99=" +
                          "/".join(str(pct(v, q)) for q in (0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99)))
        print("  " + "  ".join(partes))
    fila("TODOS", todos)
    for k in sorted(res):
        fila(f"{k[0]} {k[1]}", res[k])
    print("\nBuckets de t2(50 %) (ms desde t0), todos:")
    v = [x[1][0.5] for x in todos if 0.5 in x[1]]
    cortes = [0, 10, 25, 50, 75, 100, 125, 150, 200, 250, 500, 1000, 5001]
    for lo, hi in zip(cortes, cortes[1:]):
        n = sum(1 for x in v if lo <= x < hi)
        print(f"  [{lo:>4},{hi:>4}) {n:4} {n / max(1, len(v)):.0%}")
    pv = [x for v in pre.values() for x in v]
    if pv:
        print(f"\nPre-alpha: fracción del ajuste ya hecha entre t0-1 s y t0: mediana {pct(pv, 0.5):+.2f}, "
              f"p75 {pct(pv, 0.75):+.2f}, p90 {pct(pv, 0.9):+.2f} (n={len(pv)})")


if __name__ == "__main__":
    main()
