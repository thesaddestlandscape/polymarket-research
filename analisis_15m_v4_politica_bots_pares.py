#!/usr/bin/env python3
"""analisis_15m_v4_politica_bots_pares.py -- MISIÓN 15M v4 (08-Oct): INGENIERÍA INVERSA de la política de los
cosechadores de pares a partir de sus rellenos MAKER on-chain (caché v4_quien_gana.parquet de
analisis_15m_v4_quien_gana.py). Solo días de EXTRACCIÓN (05-06 Oct): lo que salga se escribe como política ANTES de
ver PnL y se juzga con días NO usados (07-08 Oct). Mi política v1/v2 (analisis_15m_v4_cosechador_pares.py) quedó en
~11-19 rellenos/mercado y ~80 % emparejado frente a 37-60 y 96-99 % de estos bots: aquí se mide QUÉ hacen distinto.

Por bot y mercado (orden = hora del bloque; dentro del bloque, orden de fichero):
  - inventario I = acciones YES - NO acumuladas: máximo |I|, |I| medio ponderado por relleno, |I| final / acciones;
  - EMPAREJADO FIFO de acciones: cada acción de un lado se casa con la siguiente del otro -> retraso (s) y coste
    del par (p_yes + p_no) por acción emparejada; margen = 1 - coste;
  - reacción al desequilibrio: P(el siguiente relleno es del lado que EMPAREJA) según |I| antes del relleno;
    tamaño del relleno según lado (empareja / agranda);
  - precio de la pata que empareja vs 1 - coste medio de la pata suelta (¿anclaje?);
  - perfil por fase del ciclo (T): rellenos, desequilibrio.
Uso: nice -n 19 python3 analisis_15m_v4_politica_bots_pares.py [--dias 2026-10-05,2026-10-06] [--activo BTC]
"""
import argparse
from collections import deque
from pathlib import Path

import numpy as np
import pandas as pd

DL = Path("/root/polymarket-research-datalogs")
BOTS = {"0x2903c7dc01c98c8e332d11e9b0f08740bdd55906": "2903", "0xf548517cbefe7636bef51ee31a1817f021e7c20e": "f548",
        "0x86b9a88a75194d15bb36c092ea85202da5596d67": "86b9", "0x81c935efa4b16376d93c9d0a7970644643de94cd": "81c9",
        "0xcfddfb6e1b321fcfdcb6f9aa09b11990142ce5da": "cfdd"}


def emparejar(fs):
    """fs: lista de (ts, lado, acc, p). FIFO por acciones. Devuelve lista de (retraso_s, coste_par, acc) y
    trayectoria de I antes de cada relleno."""
    cola = {"YES": deque(), "NO": deque()}
    pares, Iantes = [], []
    I = 0.0
    for ts, lado, acc, p in fs:
        Iantes.append(I)
        otro = "NO" if lado == "YES" else "YES"
        rest = acc
        while rest > 1e-9 and cola[otro]:
            t0, a0, p0 = cola[otro][0]
            q = min(rest, a0)
            pares.append((ts - t0, p + p0, q))
            rest -= q
            if q >= a0 - 1e-9:
                cola[otro].popleft()
            else:
                cola[otro][0] = (t0, a0 - q, p0)
        if rest > 1e-9:
            cola[lado].append((ts, rest, p))
        I += acc if lado == "YES" else -acc
    return pares, Iantes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", default="2026-10-05,2026-10-06")
    ap.add_argument("--activo", default="BTC")
    ap.add_argument("--salida", default="informes/m15v4_politica_bots_pares_08oct.txt")
    a = ap.parse_args()
    X = pd.read_parquet(DL / "m15_ms_cache" / "v4_quien_gana.parquet",
                        columns=["wallet", "rol", "side", "dia", "act", "mkt", "lado", "ts_est", "acc", "p", "T", "pnl", "fin"])
    X = X[(X.rol == "maker") & (X.side == 0) & X.dia.isin(a.dias.split(",")) & X.wallet.isin(BOTS)]
    if a.activo:
        X = X[X.act == a.activo]
    lin = []

    def L(s=""):
        print(s, flush=True)
        lin.append(s)
    L(f"Política de cosechadores de pares — días {a.dias}, activo {a.activo or 'todos'} (solo EXTRACCIÓN)")
    for w, nom in BOTS.items():
        B = X[X.wallet == w].sort_values(["mkt", "ts_est"], kind="stable")
        if B.empty:
            L(f"\n== {nom}: sin rellenos")
            continue
        P, filas_I, merc = [], [], []
        for mkt, g in B.groupby("mkt", sort=False):
            fs = list(zip(g.ts_est, g.lado, g.acc, g.p))
            pares, Iantes = emparejar(fs)
            P += pares
            tot = g.acc.sum()
            Ifin = abs(g.acc[g.lado == "YES"].sum() - g.acc[g.lado == "NO"].sum())
            absI = np.abs(Iantes)
            merc.append({"mkt": mkt, "n": len(g), "acc": tot, "maxI": absI.max(), "Imed": np.average(absI, weights=g.acc),
                         "Ifin_frac": Ifin / tot, "t_primero": g["T"].max(), "t_ultimo": g["T"].min(), "pnl": g.pnl.sum(),
                         "dur": g.ts_est.max() - g.ts_est.min()})
            for (ts, lado, acc, p), I0, T in zip(fs, Iantes, g["T"]):
                emp = (lado == "NO" and I0 > 0) or (lado == "YES" and I0 < 0)
                filas_I.append({"absI": abs(I0), "empareja": emp, "plano": abs(I0) < 1e-9, "acc": acc, "T": T, "p": p})
        M = pd.DataFrame(merc)
        F = pd.DataFrame(filas_I)
        Pq = pd.DataFrame(P, columns=["lag", "coste", "acc"])
        w_ = Pq.acc
        L(f"\n== {nom}: {len(M)} mercados, rellenos/merc P50 {M.n.median():.0f}, acciones/merc P50 {M.acc.median():.0f}, "
          f"tamaño/relleno P50 {F.acc.median():.1f} P90 {F.acc.quantile(.9):.0f}")
        L(f"   inventario: max|I| P50 {M.maxI.median():.0f} P90 {M.maxI.quantile(.9):.0f} acc; |I| medio P50 {M.Imed.median():.0f}; "
          f"|I| final/acciones P50 {M.Ifin_frac.median():.3f} P90 {M.Ifin_frac.quantile(.9):.3f}")
        L(f"   actividad: 1er relleno T P50 {M.t_primero.median():.0f} s, último T P50 {M.t_ultimo.median():.0f} s, "
          f"duración P50 {M.dur.median():.0f} s")
        if len(Pq):
            q = lambda s, x: float(np.quantile(s, x))
            orden = np.argsort(Pq.lag.values)
            cum = np.cumsum(w_.values[orden]) / w_.sum()
            lag_p = lambda x: Pq.lag.values[orden][np.searchsorted(cum, x)]
            L(f"   emparejado FIFO: retraso entre patas (ponderado por acciones) P25 {lag_p(.25):.0f} s, P50 {lag_p(.5):.0f} s, "
              f"P75 {lag_p(.75):.0f} s, P90 {lag_p(.9):.0f} s; %acciones emparejadas en <=2 s (mismo bloque) "
              f"{w_[Pq.lag <= 2].sum() / w_.sum():.1%}, <=10 s {w_[Pq.lag <= 10].sum() / w_.sum():.1%}")
            L(f"   coste del par por acción: media {np.average(Pq.coste, weights=w_):.4f}, P10 {q(Pq.coste, .1):.3f}, P50 {q(Pq.coste, .5):.3f}, "
              f"P90 {q(Pq.coste, .9):.3f}; % pares > 1,00 {w_[Pq.coste > 1.0].sum() / w_.sum():.1%}")
            for lo, hi in ((0, 2), (2, 10), (10, 60), (60, 1e9)):
                s = Pq[(Pq.lag > lo - 1e-9) & (Pq.lag <= hi)] if lo == 0 else Pq[(Pq.lag > lo) & (Pq.lag <= hi)]
                if len(s):
                    L(f"     retraso ({lo},{hi if hi < 1e9 else '∞'}] s: {s.acc.sum() / w_.sum():.1%} de acciones, coste medio {np.average(s.coste, weights=s.acc):.4f}")
        F["bin"] = pd.cut(F.absI, [-1, 0.5, 10, 30, 100, 300, 1e9])
        t = F.groupby("bin", observed=True).agg(n=("empareja", "size"), p_emp=("empareja", "mean"), acc=("acc", "median"))
        L("   reacción al desequilibrio |I| antes del relleno -> P(relleno del lado que empareja), tamaño mediano:")
        for b, r in t.iterrows():
            L(f"     |I| {str(b):>14s}: n={int(r.n):5d} P(empareja)={r.p_emp:.2f} tamaño={r.acc:.1f}")
        tF = F.groupby(pd.cut(F["T"], [0, 60, 120, 300, 600, 900, 2000]), observed=True).agg(n=("acc", "size"), absI=("absI", "median"))
        L("   por fase (T s): " + "; ".join(f"{str(b)} n={int(r.n)} |I|med={r.absI:.0f}" for b, r in tF.iterrows()))
    Path(a.salida).write_text("\n".join(lin) + "\n")


if __name__ == "__main__":
    main()
