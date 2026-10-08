#!/usr/bin/env python3
"""analisis_15m_v4_twap_terminal_mes.py -- MISIÓN 15M v4, Hipótesis A terminal (08-Oct): reconstruye el ESTADO TWAP
de cada foto de libro de un mercado 15m en sus últimos 120 s, para TODO el mes (libro_ambos_lados ~45 s + ticks
Chainlink RTDS), y prueba una regla CONGELADA antes de mirar estos días.

Mecanismo: el 15m resuelve con TWAP60 de cierre ([e-62, e-3] por ws_timestamp) vs TWAP60 de apertura. En el último
minuto parte de la media ya está fijada y la que falta es una media (varianza ~R^3/3), no un punto: la probabilidad de
que el líder del TWAP sobreviva es mayor que la de un "spot vs referencia". Hipótesis: el ask del líder no lo refleja.

Sin look-ahead: en la foto t solo cuentan ticks RECIBIDOS <= t (timestamp_utc); su pertenencia a la ventana va por
ws_timestamp. Referencia = TWAP60 oficial PolyBolt de la apertura o reconstruido [e-62, e-3].
Reglas CONGELADAS 08-Oct ~07:30Z (elegidas con el observador multi-offset 25-Sep..07-Oct; OOS genuino = 16..24-Sep):
  R1: comprar el líder del TWAP proyectado si 20 <= T <= 90 s y 0,55 <= ask_líder <= 0,92. Primera foto por mercado.
  R2: R1 + |z_TWAP| >= 1.
Comisión 0,07·p·(1-p) por acción; ejecución al ask de la FOTO (cota optimista; el holdout ms mide +215 ms aparte).
Mecanismo (descriptivo): fotos donde el líder del TWAP y el del spot DISCREPAN.
Uso: nice -n 19 ionice -c3 python3 analisis_15m_v4_twap_terminal_mes.py --desde 2026-09-16 --hasta 2026-10-07
"""
import argparse
import bisect
import collections
import csv
import gzip
import math
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from analisis_b1_compradores_mes import refs_dia, twap_rtds  # noqa: E402

DL = Path("/root/polymarket-research-datalogs")
PR = Path(__file__).resolve().parent / "data" / "prices"
N_VENT = 60                                    # ticks de 1 s en [e-62, e-3]


def abrir(p):
    return gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")


def fich(base, nombre, d):
    for suf in (".csv", ".csv.gz"):
        f = base / f"{nombre}_{d}{suf}"
        if f.exists():
            return f
    return None


def ts_ms(s):
    return int(datetime.fromisoformat(s).timestamp() * 1000)


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def ticks_dia(d):
    """asset -> (recv_ms[], ws_s[], precio[]) ordenado por recepción; un tick por (asset, ws segundo)."""
    out = collections.defaultdict(lambda: ([], [], []))
    for dd in ((date.fromisoformat(d) - timedelta(days=1)).isoformat(), d):
        f = fich(PR, "chainlink", dd)
        if not f:
            continue
        vistos = set()
        for r in csv.DictReader(abrir(f)):
            if r.get("source", "chainlink") != "chainlink" or not r.get("ws_timestamp_ms"):
                continue
            try:
                ws = int(r["ws_timestamp_ms"]) // 1000
                k = (r["asset"], ws)
                if k in vistos:
                    continue
                vistos.add(k)
                o = out[r["asset"]]
                o[0].append(ts_ms(r["timestamp_utc"]))
                o[1].append(ws)
                o[2].append(float(r["price_usd"]))
            except (ValueError, KeyError):
                continue
    for a in list(out):
        idx = sorted(range(len(out[a][0])), key=out[a][0].__getitem__)
        out[a] = tuple(np.array([v[i] for i in idx]) for v in out[a])
    return out


def estado_twap(rv, ws, px, fin, t, ref):
    """Estado TWAP en t (ms) con ticks RECIBIDOS <= t: (log proy/ref, z_TWAP, z_spot, σ por s, ticks fijados, spot, T)."""
    k = bisect.bisect_right(rv, t)
    if k < 30:
        return None
    S = px[k - 1]
    k0 = bisect.bisect_left(rv, t - 300_000)
    r_ = np.diff(np.log(px[k0:k]))
    r_ = r_[r_ != 0]
    dur = max(1.0, (rv[k - 1] - rv[k0]) / 1000)
    if len(r_) < 20:
        return None
    sg = math.sqrt(float((r_ ** 2).sum()) / dur)
    env = (ws[:k] >= fin - 62) & (ws[:k] <= fin - 3)
    kn = int(env.sum())
    m = max(0, N_VENT - kn)
    proj = (float(px[:k][env].sum()) + S * m) / N_VENT
    T = fin - t / 1000
    D = max(0.0, (fin - 62) - t / 1000)                # segundos hasta que empieza la ventana
    R = min(59.0, T - 3) if T > 3 else 0.0             # segundos de ventana aún por fijar
    var = (sg ** 2) * ((m / N_VENT) ** 2 * D + (R ** 3) / (3 * N_VENT ** 2))
    lp = math.log(proj / ref)
    z_tw = lp / math.sqrt(var) if var > 0 else (50.0 if lp > 0 else -50.0)
    z_sp = math.log(S / ref) / (sg * math.sqrt(max(1.0, T)))
    return lp, z_tw, z_sp, sg, kn, S, T


def procesar(d, PB, RT):
    fl = fich(DL, "libro_ambos_lados", d)
    if not fl:
        return []
    fotos = collections.defaultdict(list)
    info = {}
    g = lambda x: float(x) if x not in ("", None) else None
    for r in csv.DictReader(abrir(fl)):
        if r["marco"] != "15min":
            continue
        try:
            t = ts_ms(r["timestamp_utc"])
            fin = int(datetime.fromisoformat(r["end_date"]).timestamp())
        except (ValueError, KeyError):
            continue
        if not (10_000 <= fin * 1000 - t <= 120_000):
            continue
        fotos[r["market_id"]].append((t, g(r["ask_yes"]), g(r["ask_no"]), g(r["bid_yes"]), g(r["bid_no"])))
        info[r["market_id"]] = (r["activo"], fin)
    tk = ticks_dia(d)
    des = desenlaces(set(fotos))
    filas = []
    for mid, fs in fotos.items():
        mo, fin = info[mid]
        if mid not in des or mo not in tk:
            continue
        ref = PB.get((mo, fin - 900)) or twap_rtds(RT, mo, fin - 900)
        if ref is None:
            continue
        rv, ws, px = tk[mo]
        for (t, ay, an, by, bn) in sorted(fs):
            e = estado_twap(rv, ws, px, fin, t, ref)
            if e is None:
                continue
            lp, z_tw, z_sp, sg, kn, S, T = e
            filas.append({"dia": d, "moneda": mo, "market": mid, "fin": fin, "t": t, "T": round(T, 1),
                          "ask_y": ay, "ask_n": an, "bid_y": by, "bid_n": bn, "proj_bps": round(lp * 1e4, 3),
                          "spot_bps": round(math.log(S / ref) * 1e4, 3), "z_tw": round(z_tw, 3), "z_sp": round(z_sp, 3),
                          "fv_tw": round(phi(z_tw), 4), "fv_sp": round(phi(z_sp), 4), "sigma": round(sg * 1e4, 4),
                          "fijado": kn, "des": des[mid]})
    return filas


def fee(p):
    return 0.07 * p * (1 - p)


def evaluar(u, L, titulo):
    if len(u) == 0:
        L(f"  {titulo}: sin señales")
        return
    u = u.assign(pnl=u.win - u.ask - fee(u.ask))
    u = u.assign(eur=u.pnl / u.ask)
    dm = u.groupby("dia").eur.mean()
    rng = np.random.default_rng(1)
    bs = [rng.choice(dm.values, len(dm)).mean() for _ in range(2000)]
    ds = u.groupby("dia").eur.sum().sort_values()
    sin2 = u[~u.dia.isin(ds.index[-2:])].eur.mean()
    L(f"  {titulo}: n={len(u)} días={u.dia.nunique()} (+{int((dm > 0).sum())}) acierto={u.win.mean():.3f} "
      f"ask={u.ask.mean():.3f} EV/acc={u.pnl.mean():+.4f} EV/€={u.eur.mean():+.4f} IC90d=({np.percentile(bs, 5):+.3f},"
      f"{np.percentile(bs, 95):+.3f}) sin2mej={sin2:+.4f} top_mon={u.moneda.value_counts(normalize=True).iloc[0]:.0%}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-09-16")
    ap.add_argument("--hasta", default="2026-10-07")
    ap.add_argument("--salida", default="informes/m15v4_twap_terminal_mes_08oct.txt")
    a = ap.parse_args()
    d0, d1 = date.fromisoformat(a.desde), date.fromisoformat(a.hasta)
    dias = [(d0 + timedelta(days=i)).isoformat() for i in range((d1 - d0).days + 1)]
    cache = DL / "m15_ms_cache" / "v4_twap_terminal_mes.parquet"
    if cache.exists():
        X = pd.read_parquet(cache)
    else:
        PB, RT = {}, collections.defaultdict(lambda: [0.0, 0])
        for d in [(d0 - timedelta(days=1)).isoformat()] + dias:
            refs_dia(d, PB, RT)
        filas = []
        for d in dias:
            f = procesar(d, PB, RT)
            print(f"{d}: {len(f)} fotos terminales", flush=True)
            filas += f
        X = pd.DataFrame(filas)
        X.to_parquet(cache)
    lin = []

    def L(s=""):
        print(s, flush=True)
        lin.append(s)
    L(f"Fotos terminales (10-120 s) 15m: {len(X)} de {X.market.nunique()} mercados, {X.dia.nunique()} días")
    # filas por lado
    rows = []
    for lado, s, ask in (("YES", 1, "ask_y"), ("NO", -1, "ask_n")):
        y = X.assign(lado=lado, ask=X[ask], ztw=s * X.z_tw, zsp=s * X.z_sp, win=(X.des == lado).astype(int))
        rows.append(y)
    Y = pd.concat(rows, ignore_index=True)
    Y = Y[Y.ask.notna() & (Y.ask > 0.02) & (Y.ask < 0.99)]
    Y["lider_tw"] = Y.ztw > 0
    Y["lider_sp"] = Y.zsp > 0
    Y["tramo"] = np.where(Y.dia <= "2026-09-24", "OOS 16-24Sep", "25Sep-07Oct")
    L("\nCALIBRACIÓN líder TWAP (todas las fotos): P(gana) vs ask por T × |z_TWAP|")
    lid = Y[Y.lider_tw]
    t = lid.groupby([pd.cut(lid["T"], [10, 30, 60, 90, 120]), pd.cut(lid.ztw, [0, 0.5, 1, 1.5, 2, 3, 5, 1e9])], observed=True).agg(
        n=("win", "size"), p=("win", "mean"), ask=("ask", "mean"), fv_sp=("fv_sp", "mean")).reset_index()
    for _, r in t[t.n >= 30].iterrows():
        fvs = r.fv_sp if r.fv_sp >= 0.5 else 1 - r.fv_sp
        L(f"  T {str(r['T']):>9s} z_tw {str(r.ztw):>11s}: n={int(r.n):5d} P={r.p:.3f} ask={r.ask:.3f} gap={r.p - r.ask:+.3f}")
    L("\nMECANISMO: fotos con líder TWAP != líder spot (el spot ya cruzó la referencia, la media aún no)")
    dis = Y[Y.lider_tw & ~Y.lider_sp]
    agr = Y[Y.lider_tw & Y.lider_sp]
    for nom, q in (("discrepan", dis), ("coinciden", agr)):
        for tr in ("OOS 16-24Sep", "25Sep-07Oct"):
            qq = q[q.tramo == tr]
            if len(qq):
                L(f"  {nom:9s} {tr}: n={len(qq)} P(líder TWAP gana)={qq.win.mean():.3f} ask={qq.ask.mean():.3f} gap={qq.win.mean() - qq.ask.mean():+.3f}")
    L("\nREGLAS CONGELADAS (primera foto por mercado):")
    base = Y[Y.lider_tw & (Y["T"] >= 20) & (Y["T"] <= 90) & (Y.ask >= 0.55) & (Y.ask <= 0.92)].sort_values("t")
    for nom, q in (("R1", base), ("R2", base[base.ztw >= 1])):
        u = q.groupby("market", as_index=False).first()
        for tr in ("OOS 16-24Sep", "25Sep-07Oct"):
            evaluar(u[u.tramo == tr], L, f"{nom} {tr}")
        evaluar(u, L, f"{nom} TODO")
        for mo in sorted(u.moneda.unique()):
            evaluar(u[u.moneda == mo], L, f"{nom} {mo}")
        for lo, hi in ((0.55, 0.70), (0.70, 0.80), (0.80, 0.88), (0.88, 0.92)):
            evaluar(u[(u.ask >= lo) & (u.ask < hi + 1e-9)], L, f"{nom} ask [{lo},{hi}]")
        for lo, hi in ((20, 45), (45, 70), (70, 90)):
            evaluar(u[(u["T"] >= lo) & (u["T"] <= hi)], L, f"{nom} T [{lo},{hi}]")
    Path(a.salida).write_text("\n".join(lin) + "\n")


if __name__ == "__main__":
    main()
