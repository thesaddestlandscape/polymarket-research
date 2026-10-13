#!/usr/bin/env python3
"""vigia_15m_barato_reposicion_forward.py -- forward DIARIO de la hipótesis CONGELADA H15-BARATO-REPOSICION-V1 (13-Oct
17:45Z, informes/m15v5_hipotesis_congelada_barato_reposicion_13oct.json, sha256 fijado abajo; si el fichero cambia, no corre).

Regla (no se reajusta): rellenos MAKER on-chain de BTC 15m que COMPRAN un lado (venta maker de un token = compra del
contrario a 1-p) a precio pagado pc en [0,10, 0,40) con T restante en (60, 600] s. EV/€ PONDERADO POR VOLUMEN
(suma pnl / suma coste) = lo que cobraría una puja que se repone tras cada relleno; bootstrap por (mercado, lado).
Desenlace OFICIAL, sin reembolso. Solo días >= 2026-10-13 (08-12 se usó para formularla).
Cola (como vigia_5m_barato_maker_forward.py): por (tx, lado comprado, precio) con >= 2 makers, FINAL = último por log_index.
Caché por día en datalogs/vigia_15m_barato_reposicion/unidades_D.csv.gz. Informe acumulado + gates -> informe.json/txt.
Uso: nice -n 19 python3 vigia_15m_barato_reposicion_forward.py [--telegram]   (cron 05:35, tras el archivo on-chain 03:55)
"""
import argparse
import gzip
import hashlib
import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from analisis_15m_v5_pares_cola_onchain import tokens  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

REPO = Path(__file__).resolve().parent
CONGELADA = REPO / "informes" / "m15v5_hipotesis_congelada_barato_reposicion_13oct.json"
SHA = "d007dcbf98cefaa9403850fe5b91cd9f5d14a6ad4d64b23e40f37ea29f77b4c3"
OUT = Path("/root/polymarket-research-datalogs/vigia_15m_barato_reposicion")
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"
PRIMER_DIA = date(2026, 10, 13)
RNG = np.random.default_rng(13)


def unidades_dia(d):
    """Unidades (mercado, lado comprado) BTC 15m de la celda congelada del día d (sumas: pnl, coste, acc, final de cola)."""
    f = VOL / "m15_onchain" / f"m15_onchain_{d}.csv.gz"
    if not f.exists():
        return None, None
    tok = {t: v for t, v in tokens(d).items() if v[0] == "BTC"}
    if not tok:
        return None, None
    partes = []
    with gzip.open(f, "rt") as fh:
        for x in pd.read_csv(fh, chunksize=150_000, dtype={"token_id": str, "tx": str, "maker": str, "taker": str},
                             usecols=["tipo", "ts_est", "tx", "log_index", "maker", "taker", "side", "token_id",
                                      "maker_amt", "taker_amt"]):
            x = x[(x.tipo == "F") & (x.taker != EXCH) & x.token_id.isin(tok.keys())]     # solo rellenos MAKER BTC 15m
            if not len(x):
                continue
            tk = x.token_id
            venta = x.side.values == 1
            acc = np.where(venta, x.maker_amt.values, x.taker_amt.values).astype(float)
            usdc = np.where(venta, x.taker_amt.values, x.maker_amt.values).astype(float)
            partes.append(pd.DataFrame({
                "tx": x.tx.values, "li": x.log_index.astype(int).values, "mkt": tk.map(lambda t: tok[t][1]).values,
                "T": tk.map(lambda t: tok[t][2]).astype(float).values - x.ts_est.astype(float).values,
                "lado": tk.map(lambda t: tok[t][3]).values, "venta": venta, "acc": acc, "usdc": usdc}))
    if not partes:
        return pd.DataFrame(), 1.0
    X = pd.concat(partes, ignore_index=True)
    X = X[X.acc > 0]
    X["lado_c"] = np.where(X.venta, np.where(X.lado == "YES", "NO", "YES"), X.lado)
    X["pc"] = np.where(X.venta, 1 - X.usdc / X.acc, X.usdc / X.acc)
    X["coste"] = np.where(X.venta, X.acc - X.usdc, X.usdc)
    X = X[X.coste > 0]
    X["nivel"] = X.pc.round(3)
    g = X.groupby(["tx", "lado_c", "nivel"]).li
    X["n_niv"] = g.transform("size")
    X["rk"] = g.rank(method="first")
    X["final"] = (X.n_niv >= 2) & (X.rk == X.n_niv)
    C = X[(X.pc >= 0.10) & (X.pc < 0.40) & (X["T"] > 60) & (X["T"] <= 600)].copy()
    des = desenlaces(set(X.mkt))
    cob = pd.Series(list(set(X.mkt))).map(des).notna().mean() if len(X) else 0.0
    C["des"] = C.mkt.map(des)
    C = C[C.des.notna()]
    C["gana"] = (C.lado_c == C.des)
    C["pnl"] = np.where(C.gana, C.acc, 0.0) - C.coste
    filas = []
    for (mkt, lado_c), u in C.groupby(["mkt", "lado_c"]):
        fin = u[u.final]
        filas.append({"dia": d, "mkt": mkt, "lado": lado_c, "gana": bool(u.gana.iloc[0]), "pnl": u.pnl.sum(),
                      "coste": u.coste.sum(), "acc": u.acc.sum(), "pnl_final": fin.pnl.sum(), "coste_final": fin.coste.sum(),
                      "n": len(u)})
    return pd.DataFrame(filas), float(cob)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--telegram", action="store_true")
    a = ap.parse_args()

    def enviar(t):
        if a.telegram:
            from shadow_digest import enviar_telegram
            enviar_telegram(t)

    if hashlib.sha256(CONGELADA.read_bytes()).hexdigest() != SHA:
        msg = "🚨 Vigía 15m barato REPOSICIÓN: la hipótesis congelada CAMBIÓ (hash distinto): no corro"
        print(msg)
        enviar(msg)
        sys.exit(2)
    OUT.mkdir(exist_ok=True)
    hoy = datetime.now(timezone.utc).date()
    d, cobs = PRIMER_DIA, {}
    while d < hoy:
        ds = d.isoformat()
        cache, meta = OUT / f"unidades_{ds}.csv.gz", OUT / f"cobertura_{ds}.json"
        if not cache.exists():
            U, cob = unidades_dia(ds)
            if U is not None:
                if cob < 0.99:
                    print(f"{ds}: cobertura de desenlaces {cob:.1%} < 99 %: no se cachea (se reintenta mañana)")
                    cobs[ds] = cob
                else:
                    U.to_csv(cache, index=False, compression="gzip")
                    meta.write_text(json.dumps({"cobertura": cob}))
        if meta.exists():
            cobs[ds] = json.loads(meta.read_text())["cobertura"]
        d += timedelta(days=1)
    fs = sorted(OUT.glob("unidades_*.csv.gz"))
    lin = ["🧊 Vigía forward H15-BARATO-REPOSICION-V1 (congelada 13-Oct 17:45Z): makers BTC 15m compran 0,10-0,40 a T 60-600 s; "
           "EV ponderado por volumen (puja que se repone), desenlace oficial, sin reembolso. Solo días >= 13-Oct."]
    res = {"hipotesis": "H15-BARATO-REPOSICION-V1", "dias": {}, "cobertura": cobs}
    fs = [f for f in fs if f.stat().st_size > 30]
    if not fs:
        lin.append("Sin días forward todavía.")
    else:
        U = pd.concat([pd.read_csv(f) for f in fs], ignore_index=True)
        dd = U.groupby("dia").agg(n=("pnl", "size"), pnl=("pnl", "sum"), coste=("coste", "sum"))
        dd["ev"] = dd.pnl / dd.coste
        ev = U.pnl.sum() / U.coste.sum()
        i = RNG.integers(0, len(U), size=(2000, len(U)))
        bs = U.pnl.values[i].sum(1) / U.coste.values[i].sum(1)
        lo, hi = float(np.quantile(bs, .05)), float(np.quantile(bs, .95))
        sin = dd.drop(dd.pnl.idxmax()) if len(dd) > 1 else dd
        ev_sin = float(sin.pnl.sum() / sin.coste.sum()) if len(dd) > 1 else float("nan")
        ventaja = float(U.gana.mean() - U.coste.sum() / U.acc.sum())
        ev_fin = float(U.pnl_final.sum() / U.coste_final.sum()) if U.coste_final.sum() > 0 else float("nan")
        for ds, r in dd.iterrows():
            res["dias"][ds] = {"unidades": int(r.n), "ev": round(float(r.ev), 4), "cobertura": cobs.get(ds)}
            lin.append(f"  {ds}: unidades {int(r.n)} | EV ponderado {r.ev:+.4f} | cobertura {cobs.get(ds, 0):.1%}")
        g = {"G1_dias>=5": len(dd) >= 5, "G2_EV>=0,10": ev >= 0.10, "G3_IC90>0": lo > 0,
             "G4_dias+>=80%": (dd.ev > 0).mean() >= 0.8, "G5_sin_mejor_dia>0": ev_sin > 0,
             "G6_ventaja_unidad>0": ventaja > 0, "G7_final_cola>0": ev_fin > 0}
        res.update({"ev": ev, "ic90": [lo, hi], "ev_sin_mejor_dia": ev_sin, "ventaja_unidad": ventaja, "ev_final_cola": ev_fin,
                    "gates": g, "veredicto": "CONFIRMADA" if all(g.values()) else "EN_CURSO"})
        lin.append(f"ACUMULADO {len(dd)} días, {len(U)} unidades: EV {ev:+.4f} IC90 ({lo:+.4f},{hi:+.4f}) | sin mejor día {ev_sin:+.4f} "
                   f"| P(gana)−precio {ventaja:+.4f} | final de cola {ev_fin:+.4f}")
        lin.append("gates: " + " ".join(f"{k}{'✅' if v else '❌'}" for k, v in g.items()))
        lin.append(f"VEREDICTO: {res['veredicto']} (exploración 08-12, ya vista: +0,263 IC90 (+0,024,+0,483); nada a dinero sin "
                   "simulación con cola + /code-review + OK Javi)")
    txt = "\n".join(lin)
    (OUT / "informe.txt").write_text(txt + "\n")
    (OUT / "informe.json").write_text(json.dumps(res, indent=1, default=str))
    print(txt)
    enviar(txt)


if __name__ == "__main__":
    main()
