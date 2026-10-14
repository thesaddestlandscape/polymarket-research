#!/usr/bin/env python3
"""analisis_5m_barato_fok_vuelo.py -- MISIÓN 5m barato (14-Oct), mecanismo "orden EN VUELO" (DESCUBRIMIENTO, solo lectura).

Hallazgo previo (analisis_5m_barato_competencia.py): el ask barato del 5m lo compran tomadores pequeños y dispersos
(46 wallets / 62 casos, al precio exacto del nivel, ~1/3 del tamaño) ~80 ms (hora del exchange) después de que aparezca:
órdenes que YA estaban en vuelo (taker delay 150 ms) cuando un maker publicó el ask equivocado; después el maker lo
recoloca. Un tomador que reacciona al precio barato llega tarde; uno que YA está en vuelo con un límite correcto, no.

POLÍTICA SIMULADA (fijada antes de mirar): para cada par 5m/15m que cierra a la vez (lado s por referencias TWAP60
oficiales como v4, |gap| >= 1 bp), en cada instante de decisión t cada PASO_MS desde (C-300) s + 1,5 s hasta C - 10 s:
  límite p* = vigia_5m_barato_forward.p_limite(bid15_s(t)) (mayor precio de rejilla con bid15 - p - fee(p) >= 0,05);
  sin bid15, libro 15m cruzado o p* None -> no se envía.  Orden FOK de compra del 5m lado s a p*, que casa a t + L
  (L = llegada al casado: 223 ms optimizada, 355 P50 actual, 475 P90). Se llena si ask5_s(t+L) <= p*, al ask5 del
  nivel 1 y como mucho su tamaño (sin niveles 2-3: conservador), acciones objetivo max(5, 2 €/ask). UNA ejecución por
  mercado (la primera). Una FOK que no casa no cuesta nada (salvo límites de peticiones de la API: no modelado).
  Se marca si en t el ask ya estaba <= p* ("visible", = señal v4) o no ("anticipada": el ask bajó durante el vuelo).
Rasgos en t (sin futuro): edad del bid15 (ms desde su último cambio de precio), Binance orientado 1 s.
Resultado con desenlace OFICIAL. Unidad = mercado; IC90 por días y por cierre.
Uso: nice -n 19 ionice -c3 python3 analisis_5m_barato_fok_vuelo.py --desde 2026-10-05 --hasta 2026-10-13 [--paso 250]
Salida: datalogs/m5barato_mision/fok_vuelo_D.csv.gz (caché), fok_vuelo_informe.txt
"""
import argparse
import bisect
import csv
import gzip
import random
import statistics as st
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vigia_5m_barato_forward as V  # noqa: E402  (solo lectura: Libro, twap_refs, p_limite, fee)
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5barato_mision")
LATS = (223, 355, 475)
RNG = random.Random(5)


def cargar(dia):
    d = date.fromisoformat(dia)
    meta = {}
    libros = defaultdict(V.Libro)
    binance = defaultdict(lambda: (V.array("q"), V.array("d")))
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
                    elif tp == "q,":
                        c = ln.rstrip("\n").split(",")
                        m = meta.get(c[2])
                        if not m or m[3] % 900:
                            continue
                        try:
                            tr = int(c[7])
                            if not ((m[3] - 300) * 1000 - 10000 <= tr <= m[3] * 1000):
                                continue
                            g = lambda x: None if x in ("", "None") else float(x)
                            libros[c[2]].add(tr, (g(c[3]), g(c[4]), g(c[5]) or 0.0, g(c[6]) or 0.0, int(c[1])))
                        except (ValueError, IndexError):
                            continue
                    elif tp == "x," and pref == "m5":
                        c = ln.split(",")
                        try:
                            tr = int(c[7])
                            if (tr // 1000) % 900 < 590 and (tr // 1000) % 900 != 0:
                                continue                  # solo los últimos ~310 s antes de cada cierre de 15 min
                            b = binance[c[2][:-4]]
                            b[0].append(tr)
                            b[1].append(float(c[3]))
                        except (ValueError, IndexError):
                            continue
            except (EOFError, OSError):
                pass
    for L in libros.values():
        L.ordenar()
    bn = {}
    import numpy as np
    for k, (t, p) in binance.items():
        ta, pa = np.frombuffer(t, dtype=np.int64), np.frombuffer(p, dtype=np.float64)
        o = np.argsort(ta, kind="stable")
        bn[k] = (ta[o].tolist(), pa[o])
    tw = V.twap_refs([(d - timedelta(days=1)).isoformat(), dia])
    return meta, libros, bn, tw


def edad_bid(L, t):
    i = bisect.bisect_right(L.t, t) - 1
    if i < 0:
        return None
    b = L.fila(i)[0]
    j = i
    while j > 0 and L.fila(j - 1)[0] == b:
        j -= 1
    return t - L.t[j]


def simular_dia(dia, paso):
    r = cargar(dia)
    if r is None:
        return None
    meta, libros, bn, tw = r
    d0 = int(datetime.fromisoformat(dia + "T00:00:00+00:00").timestamp())
    idx = defaultdict(dict)
    for tk, (mo, marco, mkt, cie, lado) in meta.items():
        if d0 < cie <= d0 + 86400 and cie % 900 == 0:
            idx[(mo, cie)][(marco, lado)] = tk
    filas = []
    for (mo, cie), toks in idx.items():
        if not all(k in toks for k in (("5min", "YES"), ("5min", "NO"), ("15min", "YES"), ("15min", "NO"))):
            continue
        r15, r5 = tw.get(mo, {}).get(cie - 900), tw.get(mo, {}).get(cie - 300)
        if r15 is None or r5 is None or abs((r5 / r15 - 1) * 1e4) < 1.0:
            continue
        s = "YES" if r15 > r5 else "NO"
        L5, L15 = libros.get(toks[("5min", s)]), libros.get(toks[("15min", s)])
        if not L5 or not L15 or not L5.t or not L15.t:
            continue
        mkt5 = meta[toks[("5min", s)]][2]
        b = bn.get(mo)
        hecho = {L: None for L in LATS}
        n_env = 0
        for t in range((cie - 300) * 1000 + 1500, (cie - 10) * 1000, paso):
            _, q15 = L15.en(t)
            if not q15 or q15[0] is None or (q15[1] is not None and q15[0] > q15[1]):
                continue
            plim = V.p_limite(q15[0])
            if plim is None:
                continue
            n_env += 1
            _, q5 = L5.en(t)
            visible = bool(q5 and q5[1] is not None and q5[1] <= plim + 1e-9)
            for L in LATS:
                if hecho[L] is not None:
                    continue
                _, qa = L5.en(t + L)
                if not qa or qa[1] is None or qa[1] > plim + 1e-9 or (qa[0] is not None and qa[0] > qa[1]):
                    continue
                ask, sz = qa[1], qa[3]
                acc = min(max(5.0, 2.0 / ask), sz)
                if acc <= 0:
                    continue
                bin1 = None
                if b is not None:
                    i = bisect.bisect_right(b[0], t) - 1
                    j = bisect.bisect_right(b[0], t - 1000) - 1
                    if i >= 0 and j >= 0:
                        bin1 = round((b[1][i] / b[1][j] - 1) * 1e4 * (1 if s == "YES" else -1), 3)
                hecho[L] = {"dia": dia, "moneda": mo, "cierre": cie, "mercado": mkt5, "lado": "Up" if s == "YES" else "Down",
                            "L": L, "t_decision": t, "resto_s": round(cie - t / 1000, 2), "bid15": q15[0], "p_lim": plim,
                            "ask_t": q5[1] if q5 else None, "visible": visible, "ask_llegada": ask, "acc": round(acc, 3),
                            "edad_bid15_ms": edad_bid(L15, t), "bin1s_lado_bps": bin1, "n_fok_previas": n_env}
            if all(v is not None for v in hecho.values()):
                break
        filas += [v for v in hecho.values() if v is not None]
    des = desenlaces({f["mercado"] for f in filas})
    for f in filas:
        r = des.get(f["mercado"])
        f["desenlace"] = r or ""
        if r:
            gana = (r == "YES") == (f["lado"] == "Up")
            p = f["ask_llegada"]
            f["gana"] = gana
            f["pnl"] = round(f["acc"] * ((1.0 if gana else 0.0) - p - V.fee(p)), 4)
            f["coste"] = round(f["acc"] * (p + V.fee(p)), 4)
    return filas


def ev(rows):
    c = sum(r["coste"] for r in rows)
    return sum(r["pnl"] for r in rows) / c if c > 0 else float("nan")


def ic_dias(rows, n=3000):
    pd = defaultdict(lambda: [0.0, 0.0])
    for r in rows:
        pd[r["dia"]][0] += r["pnl"]
        pd[r["dia"]][1] += r["coste"]
    ks = list(pd)
    if len(ks) < 3:
        return None
    m = sorted(sum(pd[k][0] for k in s) / sum(pd[k][1] for k in s) for s in ([RNG.choice(ks) for _ in ks] for _ in range(n)))
    return (round(m[int(.05 * n)], 3), round(m[int(.95 * n)], 3))


def linea(nom, rows):
    if not rows:
        return f"  {nom:34s} n=0"
    pn = sorted((r["pnl"] for r in rows), reverse=True)
    return (f"  {nom:34s} n={len(rows):4d} días {len({r['dia'] for r in rows})} acierto {sum(r['gana'] for r in rows) / len(rows):.0%} "
            f"PnL {sum(pn):+8.2f} € EV/€ {ev(rows):+.3f} IC90 días {ic_dias(rows)} sin top3 {sum(pn[3:]):+7.2f} € "
            f"ask med {st.median(r['ask_llegada'] for r in rows):.2f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-10-05")
    ap.add_argument("--hasta", default="2026-10-13")
    ap.add_argument("--paso", type=int, default=250)
    a = ap.parse_args()
    filas = []
    d, d1 = date.fromisoformat(a.desde), date.fromisoformat(a.hasta)
    while d <= d1:
        c = OUT / f"fok_vuelo_{d}_p{a.paso}.csv.gz"
        if c.exists():
            with gzip.open(c, "rt") as fh:
                for r in csv.DictReader(fh):
                    for k in ("pnl", "coste", "ask_llegada", "acc", "bid15", "p_lim"):
                        r[k] = float(r[k]) if r.get(k) not in (None, "") else None
                    r["L"] = int(r["L"])
                    r["gana"] = r.get("gana") == "True"
                    r["visible"] = r["visible"] == "True"
                    filas.append(r)
        else:
            fs = simular_dia(d.isoformat(), a.paso)
            if fs is not None:
                if fs:
                    with gzip.open(c, "wt") as fh:
                        w = csv.DictWriter(fh, fieldnames=list(dict.fromkeys(k for f in fs for k in f)))
                        w.writeheader()
                        w.writerows(fs)
                print(f"{d}: {len(fs)} ejecuciones simuladas (todas las L)", flush=True)
                filas += fs
        d += timedelta(days=1)
    filas = [f for f in filas if f.get("pnl") is not None]
    out = [f"FOK EN VUELO 5m (DESCUBRIMIENTO {a.desde}..{a.hasta}, paso {a.paso} ms, nivel 1, stake 2 €, 1 por mercado)"]
    for L in LATS:
        R = [f for f in filas if f["L"] == L]
        out.append(f"\nL={L} ms:")
        out.append(linea("TODAS", R))
        out.append(linea("  visible en t (señal v4)", [f for f in R if f["visible"]]))
        out.append(linea("  anticipada (ask bajó en vuelo)", [f for f in R if not f["visible"]]))
        out.append(linea("  BTC", [f for f in R if f["moneda"] == "BTC"]))
        out.append(linea("  sin BTC", [f for f in R if f["moneda"] != "BTC"]))
        def fl(x):
            try:
                return float(x)
            except (TypeError, ValueError):
                return None
        out.append(linea("  bid15 fresco (<=250 ms)", [f for f in R if fl(f["edad_bid15_ms"]) is not None and fl(f["edad_bid15_ms"]) <= 250]))
        out.append(linea("  bid15 viejo (>250 ms)", [f for f in R if fl(f["edad_bid15_ms"]) is not None and fl(f["edad_bid15_ms"]) > 250]))
        out.append(linea("  Binance 1 s >= -1 bp a favor/plano", [f for f in R if fl(f["bin1s_lado_bps"]) is not None and fl(f["bin1s_lado_bps"]) >= -1]))
        out.append(linea("  Binance 1 s < -1 bp en contra", [f for f in R if fl(f["bin1s_lado_bps"]) is not None and fl(f["bin1s_lado_bps"]) < -1]))
        pdia = defaultdict(float)
        for f in R:
            pdia[f["dia"]] += f["pnl"]
        out.append("   por día: " + " ".join(f"{k[5:]} {v:+.1f}" for k, v in sorted(pdia.items())))
    txt = "\n".join(out)
    print(txt)
    (OUT / f"fok_vuelo_informe_p{a.paso}.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
