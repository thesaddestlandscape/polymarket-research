#!/usr/bin/env python3
"""5m barato 4/4b — FV v4: valor justo de MILISEGUNDOS = mid5 + cambio previsto del mid (BTC 5m), 15-Oct.

Javi 14-Oct: "si no bate al mid, tendrás que conseguir que lo haga". Por qué fallaron v1-v3 (fotos de 1 s, objetivo =
desenlace, juzgadas en TODOS los segundos): a 1 s el mid del 5m ya ha absorbido Binance, el 15m y Chainlink — es
eficiente en promedio. La ventaja que sí existe es TRANSITORIA (lead-lag Binance→Polymarket 150-400 ms, bid15 que se
mueve antes que el 5m, top del 5m rancio). v4 ataca eso:
  * Puntos de decisión a ms: (a) rejilla 1 s (control) y (b) EVENTOS = Binance se mueve >= MOV_BPS en 500 ms o el mid15
    cambia >= 0,01 (como mucho 1 evento por mercado cada 2 s). Todo por hora de RECEPCIÓN (x c[7], q c[7]).
  * Rasgos sin look-ahead: retornos de Binance en 100/250/500/1000 ms convertidos a unidades de probabilidad con la
    sensibilidad φ(z)/(σ√T); cambio del mid15 en 500/1000 ms; edad del top del 5m; spread/desequilibrio; T; mid5 − Φ(z).
  * Objetivo: Δmid5 a +0,5/+1/+3 s (lo que el libro aún no ha incorporado). FV_H = clip(mid5 + Δ̂_H).
Veredicto (BTC; altcoins solo diagnóstico):
  G1 R² OOS de Δ̂ (3 s) > 0 con IC90 por días > 0 en EVENTOS;  G2 Brier vs desenlace OFICIAL: FV mejor que mid5 en
  EVENTOS con IC90 por días < 0 (ponderado por mercado);  G3 económico: tomador si FV − ask(t+355 ms) ≥ M, al ask REAL
  a +355 ms, comisión real, desenlace oficial, 1 por mercado+lado, EV/€ con IC90 por días.
Disciplina: modelo y M elegidos SOLO en DESC (entrena 05-11, valida 12-13). OOS = 14-Oct en adelante (nunca mirado por
v1-v3), juicio UNA vez; el forward diario después. Solo lectura. Caché: datalogs/m5barato_mision/fv4_dataset_D.csv.gz
Uso: nice -n 19 ionice -c3 /usr/bin/python3 analisis_5m_barato_fv_modelo_v4.py [--solo-dataset D] [--oos-desde 2026-10-14]
"""
import argparse
import gzip
import math
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vigia_5m_barato_forward as V  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5barato_mision")
FEE = 0.07
MOV_BPS = 2.0
LAT_MS = 355
HS = (500, 1000, 3000)
RB = (100, 250, 500, 1000)
COLS = (["dia", "mercado", "cierre", "t", "tipo", "T", "mid5", "bid5", "ask5", "spr5", "imb5", "edad5", "mid15", "d15_500",
         "d15_1000", "z", "pbin", "sens"] + [f"rb{x}" for x in RB] + ["ask5_lat", "bid5_lat"]
        + [f"m5_{h}" for h in HS] + ["y"])
DESC_TRAIN = [f"2026-10-{d:02d}" for d in range(5, 12)]
DESC_VAL = ["2026-10-12", "2026-10-13"]


def _phi(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)


def _Phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def leer_registro(dia):
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
                            meta[c[2]] = (c[4], c[5], int(datetime.fromisoformat(c[6]).timestamp()))
                        continue
                    if tp == "x," and pref == "m5":
                        c = ln.split(",")
                        if c[2] == "BTCUSDT":
                            try:
                                bx[0].append(int(c[7]))     # RECEPCIÓN (c[6] = E de Binance: mezcla relojes)
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
                        ini = m[2] - (300 if m[0] == "5min" else 900) - 5
                        if not (ini * 1000 <= tr <= m[2] * 1000):
                            continue
                        g = lambda x: None if x in ("", "None") else float(x)
                        libros.setdefault(c[2], V.Libro()).add(tr, (g(c[3]), g(c[4]), g(c[5]) or 0.0, g(c[6]) or 0.0,
                                                                     int(c[1])))
                    except (ValueError, IndexError):
                        continue
            except (EOFError, OSError):
                pass
    for L in libros.values():
        L.ordenar()
    bt = np.frombuffer(bx[0], dtype=np.int64)
    bp = np.frombuffer(bx[1], dtype=np.float64)
    o = np.argsort(bt, kind="stable")
    return meta, libros, bt[o], bp[o]


def _top(L, t):
    """(mid, bid, ask, bid_sz, ask_sz, t_cambio) válido (no cruzado) a hora de recepción t, o None."""
    tc, q = L.en(t)
    if not q or q[0] is None or q[1] is None or q[0] >= q[1]:
        return None
    return (q[0] + q[1]) / 2, q[0], q[1], q[2], q[3], tc


def dataset_dia(dia):
    c = OUT / f"fv4_dataset_{dia}.csv.gz"
    if c.exists():
        return c
    r = leer_registro(dia)
    if r is None:
        return None
    meta, libros, bt, bp = r
    tw = V.twap_refs([(date.fromisoformat(dia) - timedelta(days=1)).isoformat(), dia])
    por_cierre = defaultdict(dict)
    for tk, (marco, mkt, cie) in meta.items():
        if marco == "5min" or cie % 900 == 0:
            por_cierre[cie][marco] = (tk, mkt)
    d0 = int(datetime.fromisoformat(dia + "T00:00:00+00:00").timestamp())
    des = desenlaces({v["5min"][1] for v in por_cierre.values() if "5min" in v})
    # el 15m que contiene a cada 5m: cierre del 15m = siguiente múltiplo de 900 >= cierre del 5m
    filas = []

    def bin_px(t):
        i = int(np.searchsorted(bt, t, side="right")) - 1
        return bp[i] if i >= 0 else None

    for cie, toks in sorted(por_cierre.items()):
        if not (d0 < cie <= d0 + 86400) or "5min" not in toks:
            continue
        c15 = cie + (-cie) % 900
        tk15 = por_cierre.get(c15, {}).get("15min")
        r5 = tw.get("BTC", {}).get(cie - 300)
        res = des.get(toks["5min"][1])
        L5 = libros.get(toks["5min"][0])
        L15 = libros.get(tk15[0]) if tk15 else None
        if r5 is None or res is None or not L5 or not L15:
            continue
        y = 1 if res == "YES" else 0
        t_ini, t_fin = (cie - 298) * 1000, (cie - 10) * 1000
        pts = [(t, "grid") for t in range(t_ini, t_fin + 1, 1000)]
        # eventos: Binance >= MOV_BPS en 500 ms, o mid15 cambia >= 0,01; 1 cada 2 s
        i0, i1 = int(np.searchsorted(bt, t_ini)), int(np.searchsorted(bt, t_fin))
        ult = -10**15
        j = i0
        for i in range(i0, i1):
            t = int(bt[i])
            while bt[j] < t - 500:
                j += 1
            if t - ult >= 2000 and abs(bp[i] / bp[j] - 1) * 1e4 >= MOV_BPS:
                pts.append((t, "evento"))
                ult = t
        k0 = int(np.searchsorted(np.frombuffer(L15.t, dtype=np.int64), t_ini))
        prev = None
        ult15 = -10**15
        for k in range(k0, len(L15.t)):
            t = L15.t[k]
            if t > t_fin:
                break
            q = L15.fila(k)
            if q[0] is None or q[1] is None or q[0] >= q[1]:
                continue
            m = (q[0] + q[1]) / 2
            if prev is not None and abs(m - prev) >= 0.01 and t - ult15 >= 2000:
                pts.append((t, "evento15"))
                ult15 = t
            prev = m
        for t, tipo in pts:
            a5, a15 = _top(L5, t), _top(L15, t)
            p_now = bin_px(t)
            if not a5 or not a15 or p_now is None:
                continue
            j = int(np.searchsorted(bt, t - 120_000, side="right"))
            i = int(np.searchsorted(bt, t, side="right")) - 1
            if i - j < 20:
                continue
            ts = bt[j:i + 1]
            idx = np.searchsorted(ts, np.arange(ts[0], ts[-1], 1000))
            serie = bp[j:i + 1][np.clip(idx, 0, i - j)]
            rets = np.diff(np.log(serie)) * 1e4
            sig = float(np.std(rets)) if len(rets) > 10 else 0.0
            T = (cie * 1000 - t) / 1000.0
            if sig <= 0:
                continue
            dist = (p_now / r5 - 1) * 1e4
            z = dist / (sig * math.sqrt(T))
            sens = _phi(z) / (sig * math.sqrt(T))          # dP/d(bps)
            rbs = []
            for x in RB:
                pa = bin_px(t - x)
                rbs.append((p_now / pa - 1) * 1e4 * sens if pa else 0.0)
            m15a, m15b = _top(L15, t - 500), _top(L15, t - 1000)
            futs = []
            for h in HS:
                f5 = _top(L5, t + h)
                futs.append(f5[0] if f5 else "")
            lat = _top(L5, t + LAT_MS)
            filas.append([dia, toks["5min"][1], cie, t, tipo, round(T, 3), a5[0], a5[1], a5[2], round(a5[2] - a5[1], 4),
                          round((a5[3] - a5[4]) / (a5[3] + a5[4]), 4) if a5[3] + a5[4] > 0 else 0.0, t - a5[5], a15[0],
                          round(a15[0] - m15a[0], 4) if m15a else 0.0, round(a15[0] - m15b[0], 4) if m15b else 0.0,
                          round(z, 4), round(_Phi(z), 5), round(sens, 6)] + [round(v, 6) for v in rbs]
                         + [lat[2] if lat else "", lat[1] if lat else ""] + futs + [y])
    OUT.mkdir(parents=True, exist_ok=True)
    tmp = c.with_suffix(".tmp")
    with gzip.open(tmp, "wt") as fh:
        fh.write(",".join(COLS) + "\n")
        for f in filas:
            fh.write(",".join(str(v) for v in f) + "\n")
    tmp.rename(c)
    return c


RASGOS = ["T", "spr5", "imb5", "edad5", "d15_500", "d15_1000", "pbin_m_mid", "m15_m_mid", "sens"] + [f"rb{x}" for x in RB]


def cargar(dias):
    import pandas as pd
    dfs = []
    for d in dias:
        c = dataset_dia(d)
        if c is not None:
            dfs.append(pd.read_csv(c))
    if not dfs:
        return None
    df = pd.concat(dfs, ignore_index=True)
    df["pbin_m_mid"] = df["pbin"] - df["mid5"]
    df["m15_m_mid"] = df["mid15"] - df["mid5"]
    df["edad5"] = np.log1p(df["edad5"].clip(lower=0))
    return df


def ic90_dias(vals_por_dia):
    v = np.array([x for x in vals_por_dia if x == x])
    if len(v) < 3:
        return None
    rng = np.random.default_rng(7)
    b = rng.choice(v, size=(5000, len(v))).mean(axis=1)
    return float(np.percentile(b, 5)), float(np.percentile(b, 95))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo-dataset")
    ap.add_argument("--oos-desde", default="2026-10-14")
    ap.add_argument("--oos-hasta", default=None)
    a = ap.parse_args()
    if a.solo_dataset:
        print(dataset_dia(a.solo_dataset))
        return
    from sklearn.ensemble import HistGradientBoostingRegressor
    from sklearn.linear_model import Ridge
    hasta = a.oos_hasta or (date.today() - timedelta(days=1)).isoformat()
    oos = []
    d = date.fromisoformat(a.oos_desde)
    while d <= date.fromisoformat(hasta):
        oos.append(d.isoformat())
        d += timedelta(days=1)
    tr, va, te = cargar(DESC_TRAIN), cargar(DESC_VAL), cargar(oos)
    lines = [f"FV v4 BTC 5m — DESC entrena {DESC_TRAIN[0]}..{DESC_TRAIN[-1]}, valida {DESC_VAL}, OOS {oos}"]
    H = 3000
    tgt = f"m5_{H}"

    def prep(df):
        df = df[df[tgt].notna()].copy()
        df["dy"] = df[tgt] - df["mid5"]
        return df

    tr, va, te = prep(tr), prep(va), prep(te) if te is not None else None
    X = lambda df: df[RASGOS].fillna(0.0).values
    cands = {"ridge": Ridge(alpha=10.0), "hgb_d3": HistGradientBoostingRegressor(max_depth=3, min_samples_leaf=500,
                                                                                  learning_rate=0.05, max_iter=300)}
    res_val = {}
    for nom, mdl in cands.items():
        mdl.fit(X(tr), tr["dy"].values)
        ev = va["tipo"] != "grid"
        p = mdl.predict(X(va[ev]))
        r2 = 1 - np.mean((va[ev]["dy"] - p) ** 2) / np.mean(va[ev]["dy"] ** 2)
        res_val[nom] = r2
        lines.append(f"  DESC val {nom}: R² Δmid 3 s en eventos = {r2:+.4f} (n={ev.sum()})")
    mejor = max(res_val, key=res_val.get)
    mdl = cands[mejor]
    # M elegido en validación (económico, tomador al ask a +355 ms)
    def econ(df, p, M):
        fv = np.clip(df["mid5"].values + p, 0.01, 0.99)
        out = defaultdict(list)
        vistos = set()
        for i, r in enumerate(df.itertuples()):
            if r.tipo == "grid":
                continue
            for lado, f, ask in (("Up", fv[i], r.ask5_lat), ("Down", 1 - fv[i], (1 - r.bid5_lat) if r.bid5_lat == r.bid5_lat else np.nan)):
                if not (ask == ask) or ask <= 0 or ask >= 1 or f - ask < M:
                    continue
                k = (r.mercado, lado)
                if k in vistos:
                    continue
                vistos.add(k)
                gana = (r.y == 1) == (lado == "Up")
                out[r.dia].append((1.0 if gana else 0.0) / (ask * (1 + FEE * (1 - ask))) - 1.0)
        return out
    pv = mdl.predict(X(va))
    elecM, mejorEV = None, -9
    for M in (0.02, 0.03, 0.05, 0.08):
        o = econ(va, pv, M)
        allv = [x for v in o.values() for x in v]
        ev = np.mean(allv) if allv else float("nan")
        lines.append(f"  DESC val M={M}: n={len(allv)} EV/€ {ev:+.3f}")
        if allv and len(allv) >= 10 and ev > mejorEV:
            elecM, mejorEV = M, ev
    lines.append(f"ELEGIDO EN DESC: modelo={mejor} M={elecM}")
    if te is None or te.empty:
        lines.append("OOS: sin datos todavía")
    else:
        mdl.fit(X(pd_concat(tr, va)), pd_concat(tr, va)["dy"].values)
        p = mdl.predict(X(te))
        te = te.assign(fv=np.clip(te["mid5"] + p, 0.01, 0.99))
        ev = te["tipo"] != "grid"
        r2d, brd = [], []
        for dia, g in te[ev].groupby("dia"):
            pg = p[te.index.get_indexer(g.index)]
            r2d.append(1 - np.mean((g["dy"] - pg) ** 2) / np.mean(g["dy"] ** 2))
            w = 1.0 / g.groupby("mercado")["mercado"].transform("count")
            brd.append(float(np.sum(w * ((g["fv"] - g["y"]) ** 2 - (g["mid5"] - g["y"]) ** 2)) / w.sum()))
        lines.append(f"OOS G1 R² Δmid 3 s eventos por día {[round(x, 4) for x in r2d]} IC90 {ic90_dias(r2d)}")
        lines.append(f"OOS G2 ΔBrier (FV − mid) eventos por día {[round(x, 5) for x in brd]} IC90 {ic90_dias(brd)}")
        if elecM is not None:
            o = econ(te, p, elecM)
            allv = [x for v in o.values() for x in v]
            lines.append(f"OOS G3 tomador M={elecM}: n={len(allv)} EV/€ {np.mean(allv) if allv else float('nan'):+.3f} "
                         f"por día {[(k[5:], len(v), round(float(np.mean(v)), 3)) for k, v in sorted(o.items())]} "
                         f"IC90 días {ic90_dias([np.mean(v) for v in o.values()])}")
    txt = "\n".join(lines)
    print(txt)
    (OUT / "fv4_informe.txt").write_text(txt + "\n")


def pd_concat(*dfs):
    import pandas as pd
    return pd.concat(dfs, ignore_index=True)


if __name__ == "__main__":
    main()
