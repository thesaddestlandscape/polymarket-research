#!/usr/bin/env python3
"""analisis_btc5m_fv_longshot.py — BTC5M-FV-LONGSHOT (encargo Javi 15-Oct, informes/encargo_btc5m_fv_longshot_15oct.md):
¿puede FV v4 + calibración seleccionar longshots (ask <= 0,10) de BTC 5m con probabilidad real de ganar > precio + costes?
SOLO LECTURA, dry-run. Reutiliza los datasets y rasgos de FV v4 (analisis_5m_barato_fv_modelo_v4.py, sin modificarlo).

1. FV fuera de muestra en DESC (05-13): validación cruzada POR DÍAS (el modelo de cada día se entrena sin ese día; mismo
   modelo que eligió v4: boosting depth 3). En OOS (>= 14-Oct): modelo entrenado con todo DESC.
   FV = clip(mid5 + Δmid̂_3s) = probabilidad de Up "de precio"; q_raw(Up) = FV, q_raw(Down) = 1 − FV.
2. Candidatos = filas con ask del lado <= 0,10 (Up: ask5; Down: 1 − bid5). Entrada al ask REAL a +355 ms (ask5_lat /
   1 − bid5_lat; conservador frente a los ~215 ms medidos), comisión tomadora 0,07·p·(1−p) por acción, desenlace oficial.
   UNA entrada por (mercado, lado): la primera fila que cumple la regla.
3. Calibración (ajustada SOLO en DESC, sobre la primera fila candidata de cada mercado-lado): logística de la victoria
   sobre logit(q_raw) [FV] frente a logística sobre logit(ask) [solo precio] -> ¿aporta FV información sobre el precio?
4. Reglas: CONTROL = toda primera fila candidata (longshot indiscriminado); FV_M = q_cal − ask − coste ≥ M,
   M ∈ {0, 0,02, 0,05} elegido en DESC; juicio en OOS.
Uso: nice -n 19 python3 analisis_btc5m_fv_longshot.py [--oos-hasta YYYY-MM-DD]
"""
import argparse
import math
import sys
from datetime import date, timedelta
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import analisis_5m_barato_fv_modelo_v4 as F4  # noqa: E402

DESC = [f"2026-10-{d:02d}" for d in range(5, 14)]
FEE = 0.07
P_MAX = 0.10
MARGENES = (0.0, 0.02, 0.05)
OUT = F4.OUT / "fv_longshot_informe.txt"


def logit(p):
    p = np.clip(p, 1e-4, 1 - 1e-4)
    return np.log(p / (1 - p))


def modelo():
    from sklearn.ensemble import HistGradientBoostingRegressor
    return HistGradientBoostingRegressor(max_depth=3, min_samples_leaf=500, learning_rate=0.05, max_iter=300)


def preparar(df):
    df = df[df["m5_3000"].notna()].copy()
    df["dy"] = df["m5_3000"] - df["mid5"]
    return df


def candidatos(df, fv):
    """Filas candidatas por lado con su q_raw, precio de entrada (+355 ms), coste y si gana."""
    out = []
    for lado in ("Up", "Down"):
        if lado == "Up":
            ask_dec, ask_ent, q = df["ask5"].values, df["ask5_lat"].values, fv
            gana = df["y"].values == 1
        else:
            ask_dec, ask_ent, q = 1 - df["bid5"].values, 1 - df["bid5_lat"].values, 1 - fv
            gana = df["y"].values == 0
        m = (ask_dec > 0) & (ask_dec <= P_MAX) & np.isfinite(ask_ent) & (ask_ent > 0) & (ask_ent < 1)
        for i in np.nonzero(m)[0]:
            out.append((df["dia"].values[i], df["mercado"].values[i], lado, int(df["t"].values[i]), q[i], ask_dec[i],
                        ask_ent[i], bool(gana[i]), df["T"].values[i]))
    out.sort(key=lambda r: (r[1], r[2], r[3]))
    return out


def pnl_eur(p, gana):
    """PnL por 1 € al precio p con comisión tomadora 0,07·p·(1−p) por acción."""
    acciones = 1.0 / (p * (1 + FEE * (1 - p)))
    return acciones * (1.0 if gana else 0.0) - 1.0


def primera_por_unidad(rows, cond):
    vistos, sel = set(), []
    for r in rows:
        k = (r[1], r[2])
        if k in vistos or not cond(r):
            continue
        vistos.add(k)
        sel.append(r)
    return sel


def resumen(sel):
    if not sel:
        return "n=0"
    pn = [pnl_eur(r[6], r[7]) for r in sel]
    pd_ = {}
    for r, x in zip(sel, pn):
        pd_.setdefault(r[0], []).append(x)
    medias = np.array([np.mean(v) for v in pd_.values()])
    ic = None
    if len(medias) >= 3:
        b = np.random.default_rng(7).choice(medias, size=(5000, len(medias))).mean(axis=1)
        ic = (round(float(np.percentile(b, 5)), 3), round(float(np.percentile(b, 95)), 3))
    sin_mejor = None
    if len(pd_) >= 2:
        mejor = max(pd_, key=lambda d: sum(pd_[d]))
        resto = [x for d, v in pd_.items() if d != mejor for x in v]
        sin_mejor = round(float(np.mean(resto)), 3) if resto else None
    return (f"n={len(sel)} acierto {np.mean([r[7] for r in sel]):.3f} precio med {np.mean([r[6] for r in sel]):.3f} "
            f"EV/€ {np.mean(pn):+.3f} PnL {np.sum(pn):+.1f} € | días {len(pd_)} IC90 días {ic} sin mejor día {sin_mejor}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--oos-hasta", default=(date.today() - timedelta(days=1)).isoformat())
    a = ap.parse_args()
    oos, d = [], date(2026, 10, 14)
    while d <= date.fromisoformat(a.oos_hasta):
        oos.append(d.isoformat())
        d += timedelta(days=1)
    desc = preparar(F4.cargar(DESC))
    X = lambda df: df[F4.RASGOS].fillna(0.0).values
    # 1. FV fuera de muestra en DESC por días
    fv_desc = np.zeros(len(desc))
    for dia in DESC:
        m = desc["dia"].values == dia
        if not m.any():
            continue
        mdl = modelo().fit(X(desc[~m]), desc["dy"].values[~m])
        fv_desc[m] = np.clip(desc["mid5"].values[m] + mdl.predict(X(desc[m])), 0.005, 0.995)
    rows_d = candidatos(desc, fv_desc)
    # 3. calibración en DESC sobre la primera fila candidata de cada unidad
    from sklearn.linear_model import LogisticRegression
    base = primera_por_unidad(rows_d, lambda r: True)
    yb = np.array([r[7] for r in base])
    cal_fv = LogisticRegression(C=1.0).fit(logit(np.array([[r[4]] for r in base])), yb)
    cal_px = LogisticRegression(C=1.0).fit(logit(np.array([[r[5]] for r in base])), yb)

    def qcal(rows, cal, col):
        return cal.predict_proba(logit(np.array([[r[col]] for r in rows])))[:, 1] if rows else np.array([])

    lines = [f"BTC5M-FV-LONGSHOT — DESC {DESC[0]}..{DESC[-1]} (FV por validación cruzada por días), OOS {oos}",
             f"Candidato = ask del lado <= {P_MAX}; entrada al ask real +355 ms; comisión 0,07·p·(1−p); 1 por mercado-lado.",
             f"DESC: unidades candidatas {len(base)} | acierto real {yb.mean():.3f} vs precio medio "
             f"{np.mean([r[5] for r in base]):.3f}"]
    # calibración: Brier y log loss de cada calibrador en DESC (in-sample del calibrador; el juicio es OOS)
    for nom, cal, col in (("FV", cal_fv, 4), ("solo precio", cal_px, 5)):
        q = qcal(base, cal, col)
        lines.append(f"  calibrador {nom:11s}: Brier {np.mean((q - yb) ** 2):.5f} logloss "
                     f"{-np.mean(yb * np.log(q) + (1 - yb) * np.log(1 - q)):.5f}")
    # 4. elegir M en DESC
    lines.append("\n== DESC (elección de M; FV fuera de muestra por días)")
    lines.append(f"  CONTROL longshot indiscriminado: {resumen(base)}")
    mejor_m, mejor_ev = None, -9
    for M in MARGENES:
        qd = dict(zip([(r[1], r[2], r[3]) for r in rows_d], qcal(rows_d, cal_fv, 4)))
        coste = lambda r: FEE * r[6] * (1 - r[6])
        sel = primera_por_unidad(rows_d, lambda r: qd[(r[1], r[2], r[3])] - r[6] - coste(r) >= M)
        lines.append(f"  FV M={M:<4}: {resumen(sel)}")
        if len(sel) >= 30:
            evm = np.mean([pnl_eur(r[6], r[7]) for r in sel])
            if evm > mejor_ev:
                mejor_m, mejor_ev = M, evm
    lines.append(f"  ELEGIDO EN DESC: M={mejor_m}")
    # OOS
    te = preparar(F4.cargar(oos)) if oos else None
    if te is None or te.empty:
        lines.append("OOS: sin datos")
    else:
        mdl = modelo().fit(X(desc), desc["dy"].values)
        fv_te = np.clip(te["mid5"].values + mdl.predict(X(te)), 0.005, 0.995)
        rows_t = candidatos(te, fv_te)
        lines.append(f"\n== OOS {oos[0]}..{oos[-1]} (juicio)")
        lines.append(f"  CONTROL longshot indiscriminado: {resumen(primera_por_unidad(rows_t, lambda r: True))}")
        if mejor_m is not None:
            qt = dict(zip([(r[1], r[2], r[3]) for r in rows_t], qcal(rows_t, cal_fv, 4)))
            sel = primera_por_unidad(rows_t, lambda r: qt[(r[1], r[2], r[3])] - r[6] - FEE * r[6] * (1 - r[6]) >= mejor_m)
            lines.append(f"  FV M={mejor_m} (elegido en DESC): {resumen(sel)}")
            # calibración OOS por tramos de q
            bt = primera_por_unidad(rows_t, lambda r: True)
            q = qcal(bt, cal_fv, 4)
            y = np.array([r[7] for r in bt])
            for lo, hi in ((0, 0.03), (0.03, 0.06), (0.06, 0.10), (0.10, 0.20), (0.20, 1.01)):
                k = (q >= lo) & (q < hi)
                if k.sum():
                    lines.append(f"    q_cal [{lo:.2f},{hi:.2f}): n {int(k.sum()):4d} q medio {q[k].mean():.3f} "
                                 f"acierto real {y[k].mean():.3f}")
    txt = "\n".join(lines)
    print(txt)
    OUT.write_text(txt + "\n")


if __name__ == "__main__":
    main()
