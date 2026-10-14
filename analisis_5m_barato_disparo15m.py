#!/usr/bin/env python3
"""analisis_5m_barato_disparo15m.py -- MISIÓN 5m barato, VÍA 3 paso 2 (DESCUBRIMIENTO, solo lectura). La subida del bid15 que
crea la señal va precedida de operaciones en el 15m (81 % en 300 ms vs 9,7 % placebo; analisis_5m_barato_precursor15m.py).
¿Disparar en esas operaciones nos adelanta a los que capturan (reaccionan al cambio del bid15: P50 97 ms tras nuestra
recepción)?

POLÍTICA: pares 5m/15m que cierran a la vez, lado s por referencias TWAP60 (|gap| >= 1 bp), ventana (C-300)s+1,5s..C-10s.
DISPARO = cada operación del 15m (token s o contrario) recibida en t (reloj de recepción), como mucho uno cada 100 ms por
par. Orden FOK de compra del 5m lado s con límite p* = p_limite(bid15_s(t) + DELTA), DELTA en {0, 0,02, 0,04} (anticipar el
salto típico del bid15: mediana +0,04); casa a t+L (L = 223, 355) si ask5_s(t+L) <= p* (nivel 1, como mucho su tamaño,
objetivo max(5, 2 €/ask)); UNA ejecución por mercado y DELTA. Desenlace oficial; comisión 0,07·p·(1-p).
Contraste: misma política con disparo cada 250 ms sin precursor (= V6) está en analisis_5m_barato_fok_vuelo.py.
Uso: nice -n 19 ionice -c3 python3 analisis_5m_barato_disparo15m.py --desde 2026-10-05 --hasta 2026-10-13
Salida: datalogs/m5barato_mision/disparo15m_D.csv.gz, disparo15m_informe.txt
"""
import argparse
import bisect
import csv
import gzip
import random
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vigia_5m_barato_forward as V  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5barato_mision")
LATS = (223, 355)
DELTAS = (0.0, 0.02, 0.04)
RNG = random.Random(9)


def cargar(dia):
    """Libro SOLO del lado s (por referencias) de cada 5m/15m del par; operaciones de ambos tokens del 15m."""
    tw = V.twap_refs([(date.fromisoformat(dia) - timedelta(days=1)).isoformat(), dia])
    def lado_s(mo, cie):
        r15, r5 = tw.get(mo, {}).get(cie - 900), tw.get(mo, {}).get(cie - 300)
        if r15 is None or r5 is None or abs((r5 / r15 - 1) * 1e4) < 1.0:
            return None
        return "YES" if r15 > r5 else "NO"
    meta, libros, ops = {}, defaultdict(V.Libro), defaultdict(lambda: V.array("q"))
    es_s = {}
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
                            cie = int(datetime.fromisoformat(c[6]).timestamp())
                            meta[c[2]] = (c[3], c[4], c[5], cie, c[7])
                            es_s[c[2]] = (cie % 900 == 0 and lado_s(c[3], cie) == c[7])
                        continue
                    if tp not in ("q,", "t,"):
                        continue
                    c = ln.rstrip("\n").split(",")
                    m = meta.get(c[2])
                    if not m or m[3] % 900:
                        continue
                    try:
                        if tp == "q,":
                            if not es_s.get(c[2]):
                                continue
                            tr = int(c[7])
                            if (m[3] - 300) * 1000 - 10000 <= tr <= m[3] * 1000:
                                g = lambda x: None if x in ("", "None") else float(x)
                                libros[c[2]].add(tr, (g(c[3]), g(c[4]), g(c[5]) or 0.0, g(c[6]) or 0.0, int(c[1])))
                        elif m[1] == "15min":
                            tr = int(c[6])
                            if (m[3] - 300) * 1000 <= tr <= m[3] * 1000:
                                ops[c[2]].append(tr)
                    except (ValueError, IndexError):
                        continue
            except (EOFError, OSError):
                pass
    for L in libros.values():
        L.ordenar()
    for k in ops:
        ops[k] = sorted(ops[k])
    return meta, libros, ops


def simular_dia(dia):
    r = cargar(dia)
    if r is None:
        return None
    meta, libros, ops = r
    tw = V.twap_refs([(date.fromisoformat(dia) - timedelta(days=1)).isoformat(), dia])
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
        o = "NO" if s == "YES" else "YES"
        L5, L15 = libros.get(toks[("5min", s)]), libros.get(toks[("15min", s)])
        if not L5 or not L15 or not L5.t or not L15.t:
            continue
        disparos = sorted(ops.get(toks[("15min", s)], []) + ops.get(toks[("15min", o)], []))
        t_ini, t_fin = (cie - 300) * 1000 + 1500, (cie - 10) * 1000
        hecho = {}
        ult = -10 ** 9
        for t in disparos:
            if not (t_ini <= t < t_fin) or t - ult < 100:
                continue
            ult = t
            _, q15 = L15.en(t)
            if not q15 or q15[0] is None or (q15[1] is not None and q15[0] > q15[1]):
                continue
            for dl in DELTAS:
                plim = V.p_limite(min(0.99, q15[0] + dl))
                if plim is None:
                    continue
                for L in LATS:
                    if (dl, L) in hecho:
                        continue
                    _, qa = L5.en(t + L)
                    if not qa or qa[1] is None or qa[1] > plim + 1e-9 or (qa[0] is not None and qa[0] > qa[1]):
                        continue
                    ask = qa[1]
                    acc = min(max(5.0, 2.0 / ask), qa[3])
                    if acc <= 0:
                        continue
                    hecho[(dl, L)] = {"dia": dia, "moneda": mo, "cierre": cie, "mercado": meta[toks[("5min", s)]][2],
                                      "lado": "Up" if s == "YES" else "Down", "delta": dl, "L": L, "t": t,
                                      "bid15": q15[0], "p_lim": plim, "ask": ask, "acc": round(acc, 3)}
        filas += list(hecho.values())
    des = desenlaces({f["mercado"] for f in filas})
    for f in filas:
        r = des.get(f["mercado"])
        if r:
            g = (r == "YES") == (f["lado"] == "Up")
            p = f["ask"]
            f.update({"gana": g, "pnl": round(f["acc"] * ((1.0 if g else 0.0) - p - V.fee(p)), 4),
                      "coste": round(f["acc"] * (p + V.fee(p)), 4)})
    return filas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-10-05")
    ap.add_argument("--hasta", default="2026-10-13")
    a = ap.parse_args()
    filas = []
    d, d1 = date.fromisoformat(a.desde), date.fromisoformat(a.hasta)
    while d <= d1:
        dia = d.isoformat()
        d += timedelta(days=1)
        c = OUT / f"disparo15m_{dia}.csv.gz"
        if c.exists():
            with gzip.open(c, "rt") as fh:
                for r in csv.DictReader(fh):
                    if r.get("pnl"):
                        filas.append({**r, "pnl": float(r["pnl"]), "coste": float(r["coste"]), "delta": float(r["delta"]),
                                      "L": int(r["L"]), "gana": r["gana"] == "True"})
            continue
        fs = simular_dia(dia)
        if fs is None:
            continue
        if fs:
            with gzip.open(c, "wt") as fh:
                w = csv.DictWriter(fh, fieldnames=list(dict.fromkeys(k for f in fs for k in f)))
                w.writeheader()
                w.writerows(fs)
        print(f"{dia}: {len(fs)} ejecuciones simuladas", flush=True)
        filas += [f for f in fs if f.get("pnl") is not None]
    L = [f"DISPARO EN OPERACIONES DEL 15m -> FOK 5m lado s (DESCUBRIMIENTO {a.desde}..{a.hasta})"]
    for uni in ("TODAS", "BTC"):
        for dl in DELTAS:
            for lat in LATS:
                R = [f for f in filas if f["delta"] == dl and f["L"] == lat and (uni == "TODAS" or f["moneda"] == "BTC")]
                if not R:
                    continue
                pdd = defaultdict(lambda: [0.0, 0.0])
                for f in R:
                    pdd[f["dia"]][0] += f["pnl"]
                    pdd[f["dia"]][1] += f["coste"]
                ks = list(pdd)
                ic = None
                if len(ks) >= 3:
                    m = sorted(sum(pdd[k][0] for k in sm) / sum(pdd[k][1] for k in sm) for sm in ([RNG.choice(ks) for _ in ks] for _ in range(2000)))
                    ic = (round(m[100], 3), round(m[1900], 3))
                pn = sorted((f["pnl"] for f in R), reverse=True)
                L.append(f"  {uni:5s} delta {dl:.2f} L{lat}: n {len(R):4d} días {len(ks)} acierto {sum(f['gana'] for f in R) / len(R):.0%} "
                         f"PnL {sum(pn):+8.2f} € EV/€ {sum(pn) / sum(f['coste'] for f in R):+.3f} IC90 días {ic} sin top3 {sum(pn[3:]):+.2f}")
    txt = "\n".join(L)
    print(txt)
    (OUT / "disparo15m_informe.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
