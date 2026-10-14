#!/usr/bin/env python3
"""analisis_5m_barato_fv_modelo.py -- SUBESTRATEGIA 4/4b de 5m barato (Javi 14-Oct): modelo PROPIO de valor justo P(Up gana)
para los 5m de BTC que cierran con un 15m. LISTÓN (trampa conocida: Φ(z) con σ 300 s era PEOR que el mid): el modelo solo se
usa si BATE AL MID DEL 5m fuera de muestra (Brier y log-loss) y está calibrado. SOLO LECTURA.

Dataset: una foto por segundo en T (s al cierre) de 298 a 10, con información recibida <= t (reloj de recepción):
  mid5/spread5/desequilibrio del top del 5m (token YES), mid15/spread15 del 15m (token YES), distancia de Binance (aggTrade)
  a la referencia de apertura del 5m (TWAP60 oficial PolyBolt, como v4) en bps, volatilidad realizada de Binance (120 s,
  bps/√s), z = dist / (σ·√T), gap de referencias ref5 vs ref15, T. Objetivo: desenlace OFICIAL del 5m (Up = YES).
Validación: entrena con días DESC y evalúa en días OOS (por defecto 05-09 / 10-13), métricas por foto y por mercado
(media por mercado para no inflar con fotos correlacionadas), calibración por deciles.
Uso: nice -n 19 /usr/bin/python3 analisis_5m_barato_fv_modelo.py [--desc 2026-10-05,2026-10-09] [--oos 2026-10-10,2026-10-13]
Salida: datalogs/m5barato_mision/fv_dataset_D.csv.gz (caché), fv_modelo_informe.txt, fv_modelo.json (coeficientes)
"""
import argparse
import bisect
import csv
import gzip
import json
import math
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vigia_5m_barato_forward as V  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5barato_mision")
COLS = ["dia", "mercado", "cierre", "T", "mid5", "spr5", "imb5", "mid15", "spr15", "dist_bps", "sigma", "z", "gap_ref", "y"]


def dataset_dia(dia):
    meta, libros, bx = {}, {}, (V.array("q"), V.array("d"))
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
                        if len(c) >= 8 and c[3] == "BTC" and c[4] in ("5min", "15min") and c[7] == "YES":
                            cie = int(datetime.fromisoformat(c[6]).timestamp())
                            if cie % 900 == 0:
                                meta[c[2]] = (c[4], c[5], cie)
                        continue
                    if tp == "x," and pref == "m5":
                        c = ln.split(",")
                        if c[2] == "BTCUSDT":
                            try:
                                bx[0].append(int(c[7]))
                                bx[1].append(float(c[3]))
                            except (ValueError, IndexError):
                                pass
                        continue
                    if tp != "q,":
                        continue
                    c = ln.rstrip("\n").split(",")
                    m = meta.get(c[2])
                    if not m:
                        continue
                    try:
                        tr = int(c[7])
                        if not ((m[2] - 305) * 1000 <= tr <= m[2] * 1000):
                            continue
                        g = lambda x: None if x in ("", "None") else float(x)
                        libros.setdefault(c[2], V.Libro()).add(tr, (g(c[3]), g(c[4]), g(c[5]) or 0.0, g(c[6]) or 0.0, int(c[1])))
                    except (ValueError, IndexError):
                        continue
            except (EOFError, OSError):
                pass
    for L in libros.values():
        L.ordenar()
    bt = np.frombuffer(bx[0], dtype=np.int64)
    bp = np.frombuffer(bx[1], dtype=np.float64)
    o = np.argsort(bt, kind="stable")
    bt, bp = bt[o], bp[o]
    tw = V.twap_refs([(date.fromisoformat(dia) - timedelta(days=1)).isoformat(), dia])
    por_cierre = {}
    for tk, (marco, mkt, cie) in meta.items():
        por_cierre.setdefault(cie, {})[marco] = (tk, mkt)
    d0 = int(datetime.fromisoformat(dia + "T00:00:00+00:00").timestamp())
    filas = []
    des = desenlaces({v["5min"][1] for v in por_cierre.values() if "5min" in v})
    for cie, toks in por_cierre.items():
        if not (d0 < cie <= d0 + 86400) or "5min" not in toks or "15min" not in toks:
            continue
        r15, r5 = tw.get("BTC", {}).get(cie - 900), tw.get("BTC", {}).get(cie - 300)
        res = des.get(toks["5min"][1])
        L5, L15 = libros.get(toks["5min"][0]), libros.get(toks["15min"][0])
        if r15 is None or r5 is None or res is None or not L5 or not L15:
            continue
        y = 1 if res == "YES" else 0
        for T in range(298, 9, -1):
            t = (cie - T) * 1000
            _, q5 = L5.en(t)
            _, q15 = L15.en(t)
            if not q5 or not q15 or None in (q5[0], q5[1], q15[0], q15[1]) or q5[0] > q5[1] or q15[0] > q15[1]:
                continue
            i = int(np.searchsorted(bt, t, side="right")) - 1
            j = int(np.searchsorted(bt, t - 120_000, side="right"))
            if i < 0 or i - j < 20:
                continue
            seg = bp[j:i + 1]
            # σ en bps por √s con retornos de ~1 s (submuestreo por índice temporal)
            ts = bt[j:i + 1]
            idx = np.searchsorted(ts, np.arange(ts[0], ts[-1], 1000))
            pts = seg[np.clip(idx, 0, len(seg) - 1)]
            rets = np.diff(np.log(pts)) * 1e4
            sigma = float(np.std(rets)) if len(rets) > 10 else float("nan")
            dist = (bp[i] / r5 - 1) * 1e4
            z = dist / (sigma * math.sqrt(T)) if sigma and sigma == sigma and sigma > 0 else float("nan")
            bsz, asz = q5[2], q5[3]
            filas.append([dia, toks["5min"][1], cie, T, (q5[0] + q5[1]) / 2, q5[1] - q5[0],
                          (bsz - asz) / (bsz + asz) if bsz + asz > 0 else 0.0, (q15[0] + q15[1]) / 2, q15[1] - q15[0],
                          round(dist, 4), round(sigma, 5), round(z, 4), round((r5 / r15 - 1) * 1e4, 4), y])
    return filas


def logit(p):
    p = np.clip(p, 1e-4, 1 - 1e-4)
    return np.log(p / (1 - p))


def X_de(A):
    """Rasgos del modelo (todo disponible en t)."""
    T = A[:, 3]
    z = np.nan_to_num(A[:, 11], nan=0.0)
    return np.column_stack([logit(A[:, 4]), logit(A[:, 7]), z, np.clip(z, -6, 6) * (1 / np.sqrt(T)),
                            A[:, 5], A[:, 6], A[:, 8], np.sign(A[:, 12]), logit(A[:, 4]) * np.log(T)])


def metricas(p, y, mk):
    p = np.clip(p, 1e-4, 1 - 1e-4)
    brier = (p - y) ** 2
    ll = -(y * np.log(p) + (1 - y) * np.log(1 - p))
    # por mercado (media dentro del mercado, luego media de mercados)
    u = {}
    for b, l_, m in zip(brier, ll, mk):
        s = u.setdefault(m, [0.0, 0.0, 0])
        s[0] += b
        s[1] += l_
        s[2] += 1
    bm = np.mean([v[0] / v[2] for v in u.values()])
    lm = np.mean([v[1] / v[2] for v in u.values()])
    return brier.mean(), ll.mean(), bm, lm, len(u)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desc", default="2026-10-05,2026-10-09")
    ap.add_argument("--oos", default="2026-10-10,2026-10-13")
    a = ap.parse_args()
    d0, d1 = a.desc.split(",")
    o0, o1 = a.oos.split(",")
    datos = {}
    d = date.fromisoformat(min(d0, o0))
    while d <= date.fromisoformat(max(d1, o1)):
        ds = d.isoformat()
        c = OUT / f"fv_dataset_{ds}.csv.gz"
        if not c.exists():
            fs = dataset_dia(ds)
            if fs:
                with gzip.open(c, "wt") as fh:
                    w = csv.writer(fh)
                    w.writerow(COLS)
                    w.writerows(fs)
                print(f"{ds}: {len(fs)} fotos", flush=True)
        if c.exists():
            with gzip.open(c, "rt") as fh:
                r = csv.reader(fh)
                next(r)
                datos[ds] = [row for row in r]
        d += timedelta(days=1)

    def matriz(d_ini, d_fin):
        rows = [x for k, v in datos.items() if d_ini <= k <= d_fin for x in v]
        A = np.array([[float(x[i]) for i in range(2, 14)] for x in rows])
        A = np.column_stack([np.zeros(len(A)), np.zeros(len(A)), A])      # mantener índices de COLS
        mk = [x[1] for x in rows]
        return A, mk
    from sklearn.linear_model import LogisticRegression
    Ad, mkd = matriz(d0, d1)
    Ao, mko = matriz(o0, o1)
    Xd, yd = X_de(Ad), Ad[:, 13]
    Xo, yo = X_de(Ao), Ao[:, 13]
    mu, sd = Xd.mean(0), Xd.std(0) + 1e-9
    clf = LogisticRegression(C=1.0, max_iter=2000).fit((Xd - mu) / sd, yd)
    po = clf.predict_proba((Xo - mu) / sd)[:, 1]
    L = [f"MODELO FV BTC 5m (pares 5m/15m) — DESC {d0}..{d1} ({len(set(mkd))} mercados, {len(Ad)} fotos) / OOS {o0}..{o1} "
         f"({len(set(mko))} mercados, {len(Ao)} fotos)"]
    for nom, p in (("mid del 5m (baseline)", Ao[:, 4]), ("mid del 15m", Ao[:, 7]), ("MODELO", po)):
        b, l_, bm, lm, nm = metricas(p, yo, mko)
        L.append(f"  {nom:24s} Brier {b:.5f} | logloss {l_:.5f} | por mercado: Brier {bm:.5f} logloss {lm:.5f} (n={nm})")
    # por tramo de tiempo
    for lo, hi in ((10, 60), (60, 150), (150, 300)):
        m = (Ao[:, 3] >= lo) & (Ao[:, 3] < hi)
        if m.sum():
            b0 = metricas(Ao[m, 4], yo[m], [x for x, k in zip(mko, m) if k])[0]
            b1 = metricas(po[m], yo[m], [x for x, k in zip(mko, m) if k])[0]
            L.append(f"  T[{lo},{hi}) Brier mid5 {b0:.5f} vs modelo {b1:.5f} ({'MEJOR' if b1 < b0 else 'peor'})")
    # calibración por deciles del modelo
    q = np.quantile(po, np.linspace(0, 1, 11))
    L.append("  calibración (decil: predicho medio -> observado):")
    for k in range(10):
        m = (po >= q[k]) & (po <= q[k + 1])
        if m.sum():
            L.append(f"    {k}: {po[m].mean():.3f} -> {yo[m].mean():.3f} (n={m.sum()})")
    # bootstrap por MERCADO de la mejora de Brier (modelo - mid5)
    u = {}
    for pm, p5, yy, mm in zip(po, Ao[:, 4], yo, mko):
        s = u.setdefault(mm, [0.0, 0.0, 0])
        s[0] += (pm - yy) ** 2
        s[1] += (p5 - yy) ** 2
        s[2] += 1
    dif = np.array([(v[0] - v[1]) / v[2] for v in u.values()])
    rng = np.random.default_rng(4)
    bs = [rng.choice(dif, len(dif)).mean() for _ in range(3000)]
    L.append(f"  Δ Brier (modelo − mid5) por mercado: {dif.mean():+.5f} IC90 ({np.quantile(bs, .05):+.5f}, {np.quantile(bs, .95):+.5f}) "
             f"-> {'MODELO BATE AL MID' if np.quantile(bs, .95) < 0 else 'NO bate al mid con IC90'}")
    L.append("  coeficientes (estandarizados): " + ", ".join(f"{n} {c:+.3f}" for n, c in zip(
        ["logit_mid5", "logit_mid15", "z", "z/√T", "spr5", "imb5", "spr15", "signo_gap", "logit_mid5·lnT"], clf.coef_[0])))
    txt = "\n".join(L)
    print(txt)
    (OUT / "fv_modelo_informe.txt").write_text(txt + "\n")
    (OUT / "fv_modelo.json").write_text(json.dumps({"mu": mu.tolist(), "sd": sd.tolist(), "coef": clf.coef_[0].tolist(),
                                                    "intercept": float(clf.intercept_[0]), "desc": a.desc, "oos": a.oos}))


if __name__ == "__main__":
    main()
