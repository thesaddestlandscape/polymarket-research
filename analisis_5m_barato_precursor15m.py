#!/usr/bin/env python3
"""analisis_5m_barato_precursor15m.py -- MISIÓN 5m barato, VÍA 3 (OK Javi 14-Oct): ¿qué pasa JUSTO ANTES de que suba el bid
del 15m del lado s y cree la señal (bid15 - ask5 - fee >= 0,05)? Si hay un precursor público que llega >= ~100 ms antes,
podemos dispararnos con él y ganar la carrera sin servidor nuevo (los que capturan reaccionan al cambio del 15m: P50 97 ms
tras nuestra recepción). SOLO LECTURA (registro ms m5/m15 + Binance del registro).

Eventos: SUBIDAS del mejor bid del 15m del lado s (s por referencias TWAP60 oficiales, |gap| >= 1 bp) en los últimos 300 s
de los 15m que cierran con un 5m. CREA = antes del cambio margen < 0,05 y después >= 0,05 (con el ask5 vigente).
PLACEBO = subidas que NO crean señal (margen después < 0,05), mismas monedas y franja.
Precursores en [t-W, t) (reloj de RECEPCIÓN, W = 300 y 1000 ms; t = recepción de la q del 15m):
  op15_s / op15_o: operaciones en el 15m (token s / token contrario) y su lado tomador; ask15_s cambia; mid5_s sube;
  Binance orientado al lado (retorno y nº de aggTrades); primer instante del precursor -> antelación.
Uso: nice -n 19 ionice -c3 python3 analisis_5m_barato_precursor15m.py --desde 2026-10-05 --hasta 2026-10-13
Salida: datalogs/m5barato_mision/precursor15m_eventos_D.csv.gz, precursor15m_informe.txt
"""
import argparse
import bisect
import csv
import gzip
import statistics as st
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_5m_barato_82ms import Cols  # noqa: E402
import vigia_5m_barato_forward as V4  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5barato_mision")


def cargar(dia):
    meta = {}
    q = defaultdict(lambda: Cols("qqddd"))       # (rx, ex, bid, ask, asz)
    t = defaultdict(lambda: Cols("qqdqd"))       # (ex, rx, precio, BUY=1, tamaño)
    bn = defaultdict(lambda: Cols("qd"))
    for pref in ("m15", "m5"):
        f = VOL / f"{pref}_registro" / f"{pref}_registro_{dia}.csv.gz"
        if not f.exists():
            return None
        with gzip.open(f, "rt", errors="replace") as fh:
            try:
                for ln in fh:
                    tp = ln[:2]
                    if tp == "k,":
                        c = ln.rstrip("\n").split(",")
                        if len(c) >= 8 and c[4] in ("5min", "15min"):
                            meta[c[2]] = (c[3], c[4], c[5], int(datetime.fromisoformat(c[6]).timestamp()), c[7])
                        continue
                    if tp == "x,":
                        if pref == "m5":
                            c = ln.split(",")
                            try:
                                tr = int(c[7])
                                if (tr // 1000) % 900 < 588 and (tr // 1000) % 900 != 0:
                                    continue
                                bn[c[2][:-4]].append((tr, float(c[3])))
                            except (ValueError, IndexError):
                                pass
                        continue
                    if tp not in ("q,", "t,"):
                        continue
                    c = ln.rstrip("\n").split(",")
                    m = meta.get(c[2])
                    if not m or m[3] % 900:
                        continue
                    try:
                        if tp == "q,":
                            tr = int(c[7])
                            if (m[3] - 305) * 1000 <= tr <= m[3] * 1000:
                                q[c[2]].append((tr, int(c[1]), None if c[3] in ("", "None") else float(c[3]),
                                                None if c[4] in ("", "None") else float(c[4]), float(c[6] or 0)))
                        else:
                            tr = int(c[6])
                            if (m[3] - 305) * 1000 <= tr <= m[3] * 1000:
                                t[c[2]].append((int(c[1]), tr, float(c[3]), 1 if c[4] == "BUY" else 0, float(c[5])))
                    except (ValueError, IndexError):
                        continue
            except (EOFError, OSError):
                pass
    for dct in (q, bn):
        for k in dct:
            dct[k].ordenar()
    for k in t:                                   # operaciones: ordenar por RECEPCIÓN (columna 1)
        import numpy as np
        o = np.argsort(np.frombuffer(t[k].c[1], dtype=np.int64), kind="stable")
        t[k].c = [type(col)(col.typecode, [col[int(i)] for i in o]) for col in t[k].c]
    return meta, q, t, bn


def dia_eventos(dia):
    r = cargar(dia)
    if r is None:
        return None
    meta, q, t, bn = r
    tw = V4.twap_refs([(date.fromisoformat(dia) - timedelta(days=1)).isoformat(), dia])
    tok = {(m[0], m[3], m[1], m[4]): k for k, m in meta.items()}
    filas = []
    for (mo, cie, marco, lado), k15 in tok.items():
        if marco != "15min" or cie % 900:
            continue
        r15, r5 = tw.get(mo, {}).get(cie - 900), tw.get(mo, {}).get(cie - 300)
        if r15 is None or r5 is None or abs((r5 / r15 - 1) * 1e4) < 1.0 or lado != ("YES" if r15 > r5 else "NO"):
            continue
        k5 = tok.get((mo, cie, "5min", lado))
        k15o = tok.get((mo, cie, "15min", "NO" if lado == "YES" else "YES"))
        Q15, Q5 = q.get(k15), q.get(k5)
        if not Q15 or not Q5 or not len(Q15):
            continue
        q5t = Q5.c[0]
        T15s, T15o = t.get(k15), t.get(k15o)
        B = bn.get(mo)
        prev_bid = None
        for i in range(len(Q15)):
            rx, ex, bid, ask, _ = Q15[i]
            if bid is None or (ask is not None and bid > ask):
                prev_bid = None
                continue
            if prev_bid is not None and bid > prev_bid + 1e-9 and rx >= (cie - 300) * 1000:
                j = bisect.bisect_right(q5t, rx) - 1
                if j < 0:
                    prev_bid = bid
                    continue
                a5 = Q5[j][3]
                if a5 is None:
                    prev_bid = bid
                    continue
                antes, despues = V4.margen(prev_bid, a5), V4.margen(bid, a5)
                crea = antes < 0.05 <= despues
                if not crea and despues >= 0.05:
                    prev_bid = bid
                    continue                          # ya había señal: ni CREA ni placebo limpio
                f = {"dia": dia, "moneda": mo, "cierre": cie, "t_rx": rx, "crea": crea, "salto_bid15": round(bid - prev_bid, 3),
                     "margen_despues": despues, "resto_s": round(cie - rx / 1000, 1)}
                for W in (300, 1000):
                    for nom, T in (("op15_s", T15s), ("op15_o", T15o)):
                        if T is None or not len(T):
                            f[f"{nom}_{W}"] = 0
                            f[f"{nom}_compra_{W}"] = 0
                            continue
                        lo, hi = bisect.bisect_left(T.c[1], rx - W), bisect.bisect_left(T.c[1], rx)
                        f[f"{nom}_{W}"] = hi - lo
                        f[f"{nom}_compra_{W}"] = sum(T.c[3][x] for x in range(lo, hi))
                    if B is not None and len(B):
                        i1, i0 = bisect.bisect_right(B.c[0], rx) - 1, bisect.bisect_right(B.c[0], rx - W) - 1
                        f[f"bin_{W}"] = (round((B.c[1][i1] / B.c[1][i0] - 1) * 1e4 * (1 if lado == "YES" else -1), 3)
                                         if i1 >= 0 and i0 >= 0 else None)
                        f[f"bin_n_{W}"] = i1 - i0
                    jw = bisect.bisect_right(q5t, rx - W) - 1
                    m5a = None if jw < 0 or Q5[jw][2] is None or Q5[jw][3] is None else (Q5[jw][2] + Q5[jw][3]) / 2
                    m5b = None if Q5[j][2] is None else (Q5[j][2] + a5) / 2
                    f[f"dmid5_{W}"] = None if m5a is None or m5b is None else round(m5b - m5a, 4)
                # antelación del primer precursor (op 15m s o contraria, Binance >= 0,5 bp a favor) en los 1000 ms previos
                lead = []
                for T in (T15s, T15o):
                    if T is not None and len(T):
                        lo, hi = bisect.bisect_left(T.c[1], rx - 1000), bisect.bisect_left(T.c[1], rx)
                        if hi > lo:
                            lead.append(rx - T.c[1][lo])
                f["antelacion_op15_ms"] = max(lead) if lead else None
                filas.append(f)
            prev_bid = bid
    return filas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-10-05")
    ap.add_argument("--hasta", default="2026-10-13")
    a = ap.parse_args()
    d, d1 = date.fromisoformat(a.desde), date.fromisoformat(a.hasta)
    agg = defaultdict(lambda: defaultdict(list))
    while d <= d1:
        dia = d.isoformat()
        d += timedelta(days=1)
        c = OUT / f"precursor15m_eventos_{dia}.csv.gz"
        if c.exists():
            with gzip.open(c, "rt") as fh:
                F = list(csv.DictReader(fh))
        else:
            F = dia_eventos(dia)
            if F is None:
                continue
            if F:
                with gzip.open(c, "wt") as fh:
                    w = csv.DictWriter(fh, fieldnames=list(F[0]))
                    w.writeheader()
                    w.writerows(F)
            print(f"{dia}: {len(F)} subidas del bid15 (crean señal {sum(1 for f in F if f['crea'] in (True, 'True'))})", flush=True)
        for f in F:
            g = "CREA" if f["crea"] in (True, "True") else "PLACEBO"
            for k, v in f.items():
                if k in ("dia", "moneda", "cierre", "t_rx", "crea"):
                    continue
                try:
                    agg[g][k].append(float(v))
                except (TypeError, ValueError):
                    pass
    L = ["VÍA 3 — precursores de la SUBIDA del bid del 15m (lado s): CREA señal vs PLACEBO"]
    for k in sorted(agg["CREA"]):
        if k.startswith("margen"):
            continue
        cr, pl = agg["CREA"][k], agg["PLACEBO"][k]
        if not cr or not pl:
            continue
        pc = lambda v: sum(1 for x in v if x > 0) / len(v)
        L.append(f"  {k:24s} CREA n={len(cr):5d} med {st.median(cr):+8.3f} %>0 {pc(cr):6.1%} | PLACEBO n={len(pl):7d} med "
                 f"{st.median(pl):+8.3f} %>0 {pc(pl):6.1%}")
    txt = "\n".join(L)
    print(txt)
    (OUT / "precursor15m_informe.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
