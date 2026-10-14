#!/usr/bin/env python3
"""analisis_5m_barato_fv_modelo_v2.py -- FV v2 BTC 5m (subestrategia 4/4b). v1 (analisis_5m_barato_fv_modelo.py) NO batió al mid
(Δ Brier +0,0025, IC90 (−0,0003, +0,0052)). v2 añade información que el mid podría no tener todavía, sobre las MISMAS fotos
(cachés fv_dataset_D de v1):
  - Chainlink (regla real: TWAP60 de cierre [C-62, C-3] por hora del oráculo vs referencia): proyección del TWAP con los
    ticks RECIBIDOS <= t (trampa: filtrar por recepción), distancia a ref5 en bps, z_cl con la varianza del tiempo que falta
    (hasta la ventana + promedio del TWAP);
  - operaciones del 15m (ambos tokens) en el último segundo y en 300 ms (precursor medido 81 % vs 9,7 %);
  - flujo firmado del 5m (compras − ventas tomadoras del token YES) en 2 s.
Modelo: gradient boosting (HistGradientBoosting) sobre rasgos + logit(mid5). Selección SOLO con DESC: entrena 05-08 y valida
09 entre {logística v2, boosting con 2 profundidades}; la elegida se reentrena con 05-09 y se juzga UNA vez en OOS 10-13.
Uso: nice -n 19 /usr/bin/python3 analisis_5m_barato_fv_modelo_v2.py
Salida: datalogs/m5barato_mision/fv2_extra_D.csv.gz (caché de rasgos extra), fv2_modelo_informe.txt
"""
import bisect
import csv
import gzip
import math
from collections import defaultdict
from datetime import datetime
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_5m_barato_fv_modelo import logit, metricas  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5barato_mision")
PRICES = Path(__file__).resolve().parent / "data" / "prices"
DIAS = ["2026-10-05", "2026-10-06", "2026-10-07", "2026-10-08", "2026-10-09", "2026-10-10", "2026-10-11", "2026-10-12",
        "2026-10-13"]


def chainlink(dia):
    """BTC, source=chainlink: arrays (recepción ms, oráculo ms, precio) ordenados por recepción."""
    filas = []
    for d in (dia,):
        for suf in (".csv", ".csv.gz"):
            f = PRICES / f"chainlink_{d}{suf}"
            if f.exists():
                op = gzip.open if suf.endswith("gz") else open
                with op(f, "rt") as fh:
                    for r in csv.DictReader(fh):
                        if r.get("asset") == "BTC" and r.get("source", "chainlink") == "chainlink":
                            try:
                                rx = int(datetime.fromisoformat(r["timestamp_utc"]).timestamp() * 1000)
                                filas.append((rx, int(r["ws_timestamp_ms"]), float(r["price_usd"])))
                            except (ValueError, KeyError):
                                pass
    filas.sort()
    return [x[0] for x in filas], [x[1] for x in filas], [x[2] for x in filas]


def ops_dia(dia):
    """operaciones (recepción ms, token, BUY=1) de BTC 5m YES y 15m (ambos) que cierran con un 15m."""
    meta, ops = {}, defaultdict(list)
    for pref in ("m15", "m5"):
        f = VOL / f"{pref}_registro" / f"{pref}_registro_{dia}.csv.gz"
        with gzip.open(f, "rt", errors="replace") as fh:
            try:
                for ln in fh:
                    tp = ln[:2]
                    if tp == "k,":
                        c = ln.rstrip("\n").split(",")
                        if len(c) >= 8 and c[3] == "BTC" and c[4] in ("5min", "15min"):
                            cie = int(datetime.fromisoformat(c[6]).timestamp())
                            if cie % 900 == 0:
                                meta[c[2]] = (c[4], cie, c[7])
                    elif tp == "t,":
                        c = ln.split(",")
                        m = meta.get(c[2])
                        if m:
                            try:
                                ops[(m[0], m[1], m[2])].append((int(c[6]), 1 if c[4] == "BUY" else -1, float(c[5])))
                            except (ValueError, IndexError):
                                pass
            except (EOFError, OSError):
                pass
    for k in ops:
        ops[k].sort()
    return ops


def extra_dia(dia):
    c = OUT / f"fv2_extra_{dia}.csv.gz"
    if c.exists():
        with gzip.open(c, "rt") as fh:
            return {(int(float(r["cierre"])), int(float(r["T"]))): r for r in csv.DictReader(fh)}
    base = OUT / f"fv_dataset_{dia}.csv.gz"
    if not base.exists():
        return {}
    import vigia_5m_barato_forward as V
    from datetime import date, timedelta
    tw = V.twap_refs([(date.fromisoformat(dia) - timedelta(days=1)).isoformat(), dia])
    crx, cws, cpx = chainlink(dia)
    ops = ops_dia(dia)
    out = {}
    with gzip.open(base, "rt") as fh:
        filas = list(csv.DictReader(fh))
    for r in filas:
        cie, T = int(float(r["cierre"])), int(float(r["T"]))
        t = (cie - T) * 1000
        ref5 = tw.get("BTC", {}).get(cie - 300)
        e = {"cierre": cie, "T": T}
        i = bisect.bisect_right(crx, t) - 1                     # último tick RECIBIDO <= t
        if i >= 0 and ref5 and t - crx[i] < 15000:
            spot = cpx[i]
            v0, v1 = (cie - 62) * 1000, (cie - 3) * 1000
            ws_rec = [(cws[k], cpx[k]) for k in range(max(0, i - 400), i + 1) if v0 <= cws[k] <= v1]
            if ws_rec:
                n = len(ws_rec)
                m = sum(p for _, p in ws_rec) / n
                resto = max(0.0, (v1 - max(w for w, _ in ws_rec)) / 1000)
                proy = (m * n + spot * resto) / (n + resto)
            else:
                proy = spot
            pre = [cpx[k] for k in range(max(0, i - 120), i + 1)]
            rets = np.diff(np.log(pre)) if len(pre) > 20 else np.array([])
            vol = float(np.std(rets)) if len(rets) else float("nan")
            resto_t = min(60.0, max(0.0, T - 3))
            var = max(0.0, T - 62) + (resto_t / 60.0) ** 2 * resto_t / 3.0
            e["dist_cl_bps"] = round((proy / ref5 - 1) * 1e4, 4)
            e["z_cl"] = round(math.log(proy / ref5) / (vol * math.sqrt(var)), 4) if vol and vol == vol and vol > 0 and var > 0 else ""
        for nom, k in (("op15y", ("15min", cie, "YES")), ("op15n", ("15min", cie, "NO"))):
            L = ops.get(k, [])
            ts = [x[0] for x in L]
            e[f"{nom}_1s"] = bisect.bisect_left(ts, t) - bisect.bisect_left(ts, t - 1000)
            e[f"{nom}_300"] = bisect.bisect_left(ts, t) - bisect.bisect_left(ts, t - 300)
        L = ops.get(("5min", cie, "YES"), [])
        ts = [x[0] for x in L]
        lo, hi = bisect.bisect_left(ts, t - 2000), bisect.bisect_left(ts, t)
        e["flujo5_2s"] = round(sum(L[x][1] * L[x][2] for x in range(lo, hi)), 2)
        out[(cie, T)] = e
    campos = ["cierre", "T", "dist_cl_bps", "z_cl", "op15y_1s", "op15y_300", "op15n_1s", "op15n_300", "flujo5_2s"]
    with gzip.open(c, "wt") as fh:
        w = csv.DictWriter(fh, fieldnames=campos, extrasaction="ignore")
        w.writeheader()
        for e in out.values():
            w.writerow(e)
    print(f"{dia}: rasgos extra {len(out)}", flush=True)
    return {k: {kk: str(vv) for kk, vv in v.items()} for k, v in out.items()}


def matriz(dias):
    X, y, mk, mid = [], [], [], []
    for dia in dias:
        base = OUT / f"fv_dataset_{dia}.csv.gz"
        if not base.exists():
            continue
        ex = extra_dia(dia)
        with gzip.open(base, "rt") as fh:
            for r in csv.DictReader(fh):
                k = (int(float(r["cierre"])), int(float(r["T"])))
                e = ex.get(k, {})
                f = lambda x: float(x) if x not in (None, "", "nan") else float("nan")
                T = f(r["T"])
                zc = f(e.get("z_cl"))
                X.append([logit(np.array([f(r["mid5"])]))[0], logit(np.array([f(r["mid15"])]))[0], f(r["z"]), T,
                          f(r["spr5"]), f(r["imb5"]), f(r["spr15"]), f(e.get("dist_cl_bps")), zc,
                          0.0 if zc != zc else math.erf(zc / math.sqrt(2)) * 0.5 + 0.5,
                          f(e.get("op15y_1s")), f(e.get("op15n_1s")), f(e.get("op15y_300")), f(e.get("op15n_300")),
                          f(e.get("flujo5_2s"))])
                y.append(int(float(r["y"])))
                mk.append(r["mercado"])
                mid.append(f(r["mid5"]))
    return np.array(X), np.array(y), mk, np.array(mid)


def main():
    from sklearn.ensemble import HistGradientBoostingClassifier
    from sklearn.linear_model import LogisticRegression
    desc_tr, desc_va, desc, oos = DIAS[:4], DIAS[4:5], DIAS[:5], DIAS[5:]
    Xtr, ytr, _, _ = matriz(desc_tr)
    Xva, yva, mkva, midva = matriz(desc_va)
    cands = {
        "logistica_v2": lambda: LogisticRegression(C=1.0, max_iter=3000),
        "boosting_d3": lambda: HistGradientBoostingClassifier(max_depth=3, learning_rate=0.05, max_iter=300,
                                                              l2_regularization=1.0, random_state=1),
        "boosting_d5": lambda: HistGradientBoostingClassifier(max_depth=5, learning_rate=0.05, max_iter=300,
                                                              l2_regularization=1.0, random_state=1),
    }
    prep = lambda X, mu=None, sd=None: np.nan_to_num((X - mu) / sd, nan=0.0)
    mu, sd = np.nanmean(Xtr, 0), np.nanstd(Xtr, 0) + 1e-9
    L = ["FV v2 BTC 5m — selección en DESC (entrena 05-08, valida 09); juicio único en OOS 10-13"]
    b_mid = metricas(midva, yva, mkva)[2]
    L.append(f"  validación 09-Oct: mid5 Brier/mercado {b_mid:.5f}")
    mejor, mejor_b = None, 9
    for nom, mk_ in cands.items():
        clf = mk_().fit(prep(Xtr, mu, sd), ytr)
        b = metricas(clf.predict_proba(prep(Xva, mu, sd))[:, 1], yva, mkva)[2]
        L.append(f"  validación 09-Oct: {nom:14s} Brier/mercado {b:.5f} ({'mejor que mid' if b < b_mid else 'peor que mid'})")
        if b < mejor_b:
            mejor, mejor_b = nom, b
    L.append(f"  ELEGIDO (solo con DESC): {mejor}")
    Xd, yd, _, _ = matriz(desc)
    Xo, yo, mko, mido = matriz(oos)
    mu, sd = np.nanmean(Xd, 0), np.nanstd(Xd, 0) + 1e-9
    clf = cands[mejor]().fit(prep(Xd, mu, sd), yd)
    po = clf.predict_proba(prep(Xo, mu, sd))[:, 1]
    for nom, p in (("mid del 5m", mido), (f"MODELO {mejor}", po)):
        b, l_, bm, lm, nm = metricas(p, yo, mko)
        L.append(f"  OOS {nom:22s} Brier {b:.5f} logloss {l_:.5f} | por mercado Brier {bm:.5f} logloss {lm:.5f} (n={nm})")
    u = {}
    for pm, p5, yy, mm in zip(po, mido, yo, mko):
        s = u.setdefault(mm, [0.0, 0.0, 0])
        s[0] += (pm - yy) ** 2
        s[1] += (p5 - yy) ** 2
        s[2] += 1
    dif = np.array([(v[0] - v[1]) / v[2] for v in u.values()])
    rng = np.random.default_rng(4)
    bs = [rng.choice(dif, len(dif)).mean() for _ in range(3000)]
    L.append(f"  OOS Δ Brier (modelo − mid5) por mercado: {dif.mean():+.5f} IC90 ({np.quantile(bs, .05):+.5f}, {np.quantile(bs, .95):+.5f}) "
             f"-> {'MODELO BATE AL MID' if np.quantile(bs, .95) < 0 else 'NO bate al mid con IC90'}")
    T = Xo[:, 3]
    for lo, hi in ((10, 60), (60, 150), (150, 300)):
        m = (T >= lo) & (T < hi)
        b0 = metricas(mido[m], yo[m], [x for x, k in zip(mko, m) if k])[0]
        b1 = metricas(po[m], yo[m], [x for x, k in zip(mko, m) if k])[0]
        L.append(f"  OOS T[{lo},{hi}) Brier mid5 {b0:.5f} vs modelo {b1:.5f} ({'MEJOR' if b1 < b0 else 'peor'})")
    txt = "\n".join(L)
    print(txt)
    (OUT / "fv2_modelo_informe.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
