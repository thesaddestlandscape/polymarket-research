#!/usr/bin/env python3
"""POST-HOC (declarado en INFORME, no en PREREG): segundo instrumento para las reglas de cartera de B.
Pseudo-B sobre la POBLACIÓN de makers (b_seleccion_adversa/datos/units/units_D.pkl: primeras 5 acc por maker/mercado/lado, ETH/SOL/XRP 5m,
pc 0,10-0,30, T 60-300, desenlace oficial). Cada réplica: por cierre (fin) se toma el cierre con prob QC y dentro cada moneda con prob QM; de cada
(cierre, moneda) elegida, UN relleno al azar (B solo tiene una cara por mercado). Densidad ~ B real (~0,8 posiciones por cierre tomado, 78 % en cierres
compartidos). Se aplican las MISMAS funciones de regla de analisis_tandas.py por día (pausas/rachas no cruzan la noche) y se mide ΔPnL por día.
También: EV por bloque de 4 h UTC por día (¿08-12 UTC peor de forma estable?).
Uso: nice -n 19 ionice -c3 python3 pob_reglas.py [--rep 200]"""
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import analisis_tandas as A  # noqa: E402

UNITS = AQUI.parent.parent / "b_seleccion_adversa" / "datos" / "units"
REP = int(sys.argv[sys.argv.index("--rep") + 1]) if "--rep" in sys.argv else 200
QC, QM = 0.45, 0.6
REGLAS = {k: v for k, v in A.REGLAS.items() if k in ("R1a_RACHA5", "R1b_RACHA8", "R2b_CONC3", "R3_UNA_POR_CIERRE", "R4a_STOPDIA5",
                                                       "R6b_WF_HORA4")}


def cargar():
    dfs = []
    for f in sorted(UNITS.glob("units_*.pkl")):
        d = pd.read_pickle(f)[["dia", "mkt", "lado_c", "act", "c", "p", "sh", "T", "pc", "fin", "gana", "ts", "hora"]]
        dfs.append(d)
    d = pd.concat(dfs, ignore_index=True)
    return d[d["dia"] < "2026-10-21"]          # 21-Oct parcial en esta fuente


MODO = sys.argv[sys.argv.index("--modo") + 1] if "--modo" in sys.argv else "azar"   # azar | primero (el relleno más temprano del mercado)


def pseudo_b(d, rng):
    fins = d["fin"].unique()
    tom_c = set(fins[rng.random(len(fins)) < QC])
    sub = d[d["fin"].isin(tom_c)]
    g = sub.groupby(["fin", "act"]).indices
    filas = []
    for (fin, act), idx in g.items():
        if rng.random() >= QM:
            continue
        if MODO == "primero":
            r = sub.iloc[idx[int(np.argmin(sub["ts"].values[idx]))]]
        else:
            r = sub.iloc[idx[rng.integers(len(idx))]]
        filas.append(dict(tf=float(r.ts), fin=float(fin), tk=float(fin) + 60, tanda=0, coin=act, outcome=r.lado_c, acc=float(r.sh),
                          coste=float(r.c), pnl=float(r.p), win=bool(r.gana), precio=float(r.pc), mercado=f"{act}-{fin}",
                          hora=int(r.hora), dia=r.dia))
    filas.sort(key=lambda p: (p["tf"], p["mercado"]))
    return filas


def main():
    rng = np.random.default_rng(A.SEED)
    d = cargar()
    dias = sorted(d["dia"].unique())
    out = {"modo": MODO, "dias": dias, "n_units": int(len(d)), "rep": REP, "QC": QC, "QM": QM}
    # EV por bloque de 4 h y día (toda la población, ponderado por €)
    d["hb"] = (d["hora"] // 4) * 4
    t = d.groupby(["dia", "hb"]).agg(pnl=("p", "sum"), c=("c", "sum"), n=("p", "size")).reset_index()
    t["ev"] = t.pnl / t.c
    piv = t.pivot(index="dia", columns="hb", values="ev").round(3)
    out["ev_bloque4h_por_dia"] = json.loads(piv.to_json(orient="index"))
    tot = d.groupby("hb").agg(pnl=("p", "sum"), c=("c", "sum"), n=("p", "size"))
    out["ev_bloque4h_total"] = {int(k): dict(ev=round(v.pnl / v.c, 4), n=int(v.n)) for k, v in tot.iterrows()}
    # días en que 08-12 es el peor bloque / está por debajo del resto
    peor = []
    for dia in dias:
        x = t[t.dia == dia]
        a = x[x.hb == 8]
        r = x[x.hb != 8]
        if len(a):
            peor.append(float(a.ev.iloc[0] - r.pnl.sum() / r.c.sum()))
    out["dif_08_12_vs_resto_por_dia"] = [round(v, 3) for v in peor]
    # reglas sobre pseudo-B
    acc = {k: defaultdict(list) for k in REGLAS}
    base = defaultdict(list)
    for _ in range(REP):
        Pall = pseudo_b(d, rng)
        por_dia = defaultdict(list)
        for p in Pall:
            por_dia[p["dia"]].append(p)
        for dia, P in por_dia.items():
            c0 = sum(p["coste"] for p in P)
            base[dia].append((sum(p["pnl"] for p in P), c0, len(P)))
            for nom, f in REGLAS.items():
                w = f(P)
                dl = sum(p["pnl"] * (x - 1) for p, x in zip(P, w))
                cq = sum(p["coste"] * (1 - x) for p, x in zip(P, w))
                pk = sum(p["pnl"] * x for p, x in zip(P, w))
                ck = sum(p["coste"] * x for p, x in zip(P, w))
                acc[nom][dia].append((dl, cq, pk, ck))
    res = {}
    for nom in REGLAS:
        filas = []
        for dia in dias:
            v = acc[nom].get(dia)
            if not v:
                continue
            dl = np.array([x[0] for x in v])
            cq = np.array([x[1] for x in v])
            pk = sum(x[2] for x in v)
            ck = sum(x[3] for x in v)
            ev_q = float(-dl.sum() / cq.sum()) if cq.sum() else float("nan")
            ev_k = float(pk / ck) if ck else float("nan")
            filas.append(dict(dia=dia, ev_retenido=round(ev_k, 4), info=round(ev_k - ev_q, 4), delta_medio=round(float(dl.mean()), 2), ev_quitado=round(float(-dl.sum() / cq.sum()), 4) if cq.sum() else None,
                              frac_rep_delta_pos=round(float((dl > 0).mean()), 2), coste_quitado_medio=round(float(cq.mean()), 1)))
        dm = np.array([f["delta_medio"] for f in filas])
        boot = [float(np.random.default_rng(i).choice(dm, len(dm)).mean()) for i in range(5000)]
        inf = np.array([f["info"] for f in filas])
        bi = [float(np.random.default_rng(i).choice(inf, len(inf)).mean()) for i in range(5000)]
        res[nom] = dict(info_media=round(float(inf.mean()), 4), info_ic90_dias=[round(float(np.percentile(bi, 5)), 4), round(float(np.percentile(bi, 95)), 4)],
                        info_dias_pos=int((inf > 0).sum()), por_dia=filas, delta_medio_dia=round(float(dm.mean()), 2), ic90_dias=[round(float(np.percentile(boot, 5)), 2),
                        round(float(np.percentile(boot, 95)), 2)], dias_pos=int((dm > 0).sum()), n_dias=len(dm),
                        delta_sin_2_mejores_dias=round(float(np.sort(dm)[:-2].mean()), 2))
    out["reglas"] = res
    out["base_por_dia"] = {dia: dict(pnl_medio=round(float(np.mean([x[0] for x in v])), 2), coste_medio=round(float(np.mean([x[1] for x in v])), 1),
                                     n_medio=round(float(np.mean([x[2] for x in v])), 1),
                                     ev=round(float(sum(x[0] for x in v) / sum(x[1] for x in v)), 4)) for dia, v in sorted(base.items())}
    (AQUI / f"pob_resultados_{MODO}.json").write_text(json.dumps(out, indent=1, ensure_ascii=False, default=str))
    print(json.dumps(out, indent=1, ensure_ascii=False, default=str)[:12000])


if __name__ == "__main__":
    main()
