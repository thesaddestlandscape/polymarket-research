#!/usr/bin/env python3
"""analisis_arbitraje_anidado_precursores_eval.py -- evalúa los datasets de analisis_arbitraje_anidado_precursores.py
(B1 nueva fase, paso 1). Solo rasgos con información <= td. Todo con validación dejando FUERA cada ventana (LOWO), y en
particular entrenando SIN la ventana BTC 06-Oct 07:00 (79 % del dinero del registro ms) y probando solo en ella.
  1) estudio de eventos: rasgos en t-X de las bajadas del 15m que CREAN arbitraje vs las que no vs la rejilla;
  2) "periodo quieto": P(bajada de A en 100 ms | edad de A) y P(arbitraje en 150 ms | edad de B);
  3) predictor logístico (sklearn) de P(arbitraje nace en H ms) y de P(arbitraje >=5c en H ms) por grupos de rasgos
     (solo 15m, solo 5m, solo Binance, todo): AUC LOWO y $ garantizados por share capturados en el 1 % superior.
Uso: --dir <carpeta del constructor>
"""
import argparse
import collections
import sys

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

GRUPOS = {
    "15m": ["edad_A_ms", "ask_A", "size_A", "trades_A_1s"],
    "5m": ["edad_B_ms", "ask_B", "trades_B_1s"],
    "binance": ["bin_100", "bin_250", "bin_500", "bin_1000", "bin_3000", "bin_cambios_1s"],
    "cruzado": ["neto", "resto_s"],
}
GRUPOS["todo"] = sum(GRUPOS.values(), [])
VENTANA_GRANDE = ("BTC", 1791270000)   # 06-Oct 07:00Z


def prep(df, cols):
    X = df[cols].astype(float).copy()
    for c in cols:
        if c.startswith("edad"):
            X[c] = np.log1p(X[c].clip(lower=0))
    X = X.fillna(X.median()).fillna(0)
    return X.values


def lowo(df, cols, y, k=8):
    """Validación agrupada por ventana (k bloques; ninguna ventana en train y test a la vez)."""
    ventanas = np.array(sorted(df["ventana"].unique()))
    rng = np.random.default_rng(11)
    bloque = dict(zip(ventanas, rng.permutation(len(ventanas)) % k))
    b = df["ventana"].map(bloque).values
    pred = np.full(len(df), np.nan)
    for v in range(k):
        te = b == v
        tr = ~te
        if df.loc[tr, y].sum() < 5 or te.sum() == 0:
            continue
        m = LogisticRegression(max_iter=500, class_weight="balanced")
        Xtr = prep(df[tr], cols)
        mu, sd = Xtr.mean(0), Xtr.std(0) + 1e-9
        m.fit((Xtr - mu) / sd, df.loc[tr, y].values)
        pred[te] = m.predict_proba((prep(df[te], cols) - mu) / sd)[:, 1]
    return pred


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--H", type=int, default=150)
    a = ap.parse_args()
    ev = pd.read_csv(f"{a.dir}/eventos_baja_15m.csv")
    gr = pd.read_csv(f"{a.dir}/rejilla_100ms.csv")
    for d in (ev, gr):
        d["ventana"] = d["moneda"] + "_" + d["cierre"].astype(str)
    H = a.H
    print(f"eventos (bajadas del ask 15m x leads): {len(ev)} filas, {ev['t_evento'].nunique()} bajadas, "
          f"{ev.loc[ev.crea_arb == 1, 't_evento'].nunique()} crean arbitraje | rejilla: {len(gr)} puntos, "
          f"{gr['ventana'].nunique()} ventanas")

    # 1) estudio de eventos
    print("\n== 1. Estudio de eventos: media de rasgos en t-X (crea arbitraje vs bajada que no lo crea vs rejilla) ==")
    for X in (0, 25, 50, 100, 250, 500):
        e = ev[ev.lead_ms == X]
        s = e[e.crea_arb == 1]
        o = e[e.crea_arb == 0]
        def m(df, c):
            v = df[c].astype(float)
            return f"{v.median():+.2f}"
        print(f"  t-{X:3} ms | crea n={len(s):4}: bin250 {m(s, 'bin_250')} bin1000 {m(s, 'bin_1000')} edadA {m(s, 'edad_A_ms')} "
              f"edadB {m(s, 'edad_B_ms')} neto {m(s, 'neto')} | no crea n={len(o):5}: bin250 {m(o, 'bin_250')} "
              f"bin1000 {m(o, 'bin_1000')} edadA {m(o, 'edad_A_ms')} edadB {m(o, 'edad_B_ms')} neto {m(o, 'neto')}")
    print(f"  rejilla: bin250 {gr.bin_250.median():+.2f} bin1000 {gr.bin_1000.median():+.2f} edadA {gr.edad_A_ms.median():.0f} "
          f"edadB {gr.edad_B_ms.median():.0f} neto {gr.neto.median():+.3f}")

    # 2) periodo quieto
    print("\n== 2. ¿Más tiempo quieta => más probable el cambio? (rejilla) ==")
    for col, lab in (("edad_A_ms", "baja_100"), ("edad_B_ms", f"arb_{H}"), ("edad_A_ms", f"arb_{H}")):
        b = pd.cut(gr[col], [-1, 1000, 5000, 10000, 15000, 20000, 25000, 30000, 60000, 1e9],
                   labels=["<1s", "1-5", "5-10", "10-15", "15-20", "20-25", "25-30", "30-60", ">60"])
        t = gr.groupby(b, observed=True)[lab].agg(["mean", "size"])
        print(f"  {lab} según {col}: " + " | ".join(f"{i} {r['mean'] * 100:.2f}% (n={int(r['size'])})" for i, r in t.iterrows()))

    # 3) predictores
    print(f"\n== 3. Predictor de P(arbitraje nace en {H} ms) y P(>=5c en {H} ms), validación agrupada por ventana, 8 bloques (sin futuro) ==")
    for y in (f"arb_{H}", f"arb5c_{H}"):
        pos = int(gr[y].sum())
        print(f"  objetivo {y}: positivos {pos} de {len(gr)} ({pos / len(gr):.3%}), ventanas con positivos "
              f"{gr.loc[gr[y] == 1, 'ventana'].nunique()}")
        if pos < 10:
            print("    (muy pocos positivos: no se puede validar)")
            continue
        for g, cols in GRUPOS.items():
            p = lowo(gr, cols, y)
            ok = ~np.isnan(p)
            auc = roc_auc_score(gr.loc[ok, y], p[ok]) if gr.loc[ok, y].nunique() == 2 else float("nan")
            # $ capturados en el 1 % de mayor puntuación
            d = gr.loc[ok].assign(p=p[ok])
            top = d[d.p >= d.p.quantile(0.99)]
            dinero = d[f"arbneto_{H}"].fillna(0).clip(lower=0)
            cap = top[f"arbneto_{H}"].fillna(0).clip(lower=0).sum() / max(dinero.sum(), 1e-9)
            # sin la ventana grande: entrenar sin ella ya lo hace LOWO; AUC fuera de ella
            fuera = d[d.ventana != f"{VENTANA_GRANDE[0]}_{VENTANA_GRANDE[1]}"]
            auc_f = roc_auc_score(fuera[y], fuera.p) if fuera[y].nunique() == 2 else float("nan")
            dentro = d[d.ventana == f"{VENTANA_GRANDE[0]}_{VENTANA_GRANDE[1]}"]
            auc_d = roc_auc_score(dentro[y], dentro.p) if dentro[y].nunique() == 2 else float("nan")
            print(f"    {g:8} AUC LOWO {auc:.3f} | sin la ventana BTC grande {auc_f:.3f} | SOLO en ella (entrenado sin "
                  f"ella) {auc_d:.3f} | top 1 % captura {cap:5.1%} del neto/share")


if __name__ == "__main__":
    main()
