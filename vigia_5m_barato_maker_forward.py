#!/usr/bin/env python3
"""vigia_5m_barato_maker_forward.py -- forward DIARIO de la hipótesis CONGELADA H5M-BARATO-MAKER-v1 (09-Oct, Javi "ok":
informes/m5v1_hipotesis_congelada_banda_barata_09oct.json, sha256 fijado abajo; si el fichero cambia, no corre).

Regla (no se reajusta): rellenos MAKER on-chain de mercados Up/Down 5m que COMPRAN un lado (venta maker de un token =
compra del contrario a 1-p) a precio pagado pc en (0,10, 0,30] con T en (60, 300]. Unidad = (mercado, lado comprado);
EV/€ = suma pnl / suma coste de la unidad; EV de la celda = media de unidades. PnL a resolución con desenlace OFICIAL,
sin reembolso. Solo días >= 2026-10-09 (los de la congelación no cuentan).

Posición en la cola (lo que importa para NOSOTROS, que no iríamos delante): dentro de una transacción, los makers de un
mismo (lado comprado, precio) se rellenan en orden de prioridad y log_index conserva ese orden. Para niveles con >= 2
makers en la tx: CABEZA = primer maker, FINAL = último (el más al fondo de la cola alcanzado). Aproximación: no ve el
libro ni las cancelaciones. EV de unidades formadas solo por rellenos "final" -> criterio "al final de la cola > 0".

Por día: cache gz de unidades en datalogs/vigia_5m_barato_maker/unidades_D.csv.gz (no se recalcula). Informe
acumulado + gates de la congelación -> informe.json/txt y Telegram (--telegram).
Uso: nice -n 19 python3 vigia_5m_barato_maker_forward.py [--telegram]   (cron 05:20, tras el archivo on-chain de 04:10)
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
from analisis_5m_v1_quien_gana import mapa_tokens  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

REPO = Path(__file__).resolve().parent
CONGELADA = REPO / "informes" / "m5v1_hipotesis_congelada_banda_barata_09oct.json"
SHA = "b6cf2fed95e1c8ecad7c5981860b7790542df6b692f27c7bc196efa5c548dbde"
OUT = Path("/root/polymarket-research-datalogs/vigia_5m_barato_maker")
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"
PRIMER_DIA = date(2026, 10, 9)
RNG = np.random.default_rng(11)


def unidades_dia(d):
    """Unidades (mercado, lado comprado) de la celda congelada para el día d, con banderas de posición en la cola."""
    f = VOL / "m5_onchain" / f"m5_onchain_{d}.csv.gz"
    if not f.exists():
        return None, None
    tok = mapa_tokens([d])
    t_act = {t: v[0] for t, v in tok.items()}
    t_mkt = {t: v[1] for t, v in tok.items()}
    t_fin = {t: v[2] for t, v in tok.items()}
    t_lado = {t: v[3] for t, v in tok.items()}
    partes = []
    with gzip.open(f, "rt") as fh:
        for x in pd.read_csv(fh, chunksize=150_000, dtype={"token_id": str, "tx": str, "maker": str, "taker": str},
                             usecols=["tipo", "ts_est", "tx", "log_index", "maker", "taker", "side", "token_id",
                                      "maker_amt", "taker_amt"]):
            x = x[(x.tipo == "F") & (x.taker != EXCH) & x.token_id.isin(tok.keys())]     # solo rellenos MAKER
            if not len(x):
                continue
            tk = x.token_id
            venta = x.side.values == 1
            acc = np.where(venta, x.maker_amt.values, x.taker_amt.values).astype(float)
            usdc = np.where(venta, x.taker_amt.values, x.maker_amt.values).astype(float)
            lado = tk.map(t_lado).values
            partes.append(pd.DataFrame({
                "tx": x.tx.values, "li": x.log_index.astype(int).values, "act": tk.map(t_act).values,
                "mkt": tk.map(t_mkt).values, "T": tk.map(t_fin).astype(float).values - x.ts_est.astype(float).values,
                "lado": lado, "venta": venta, "acc": acc, "usdc": usdc}))
    X = pd.concat(partes, ignore_index=True)
    X = X[X.acc > 0]
    X["lado_c"] = np.where(X.venta, np.where(X.lado == "YES", "NO", "YES"), X.lado)
    X["pc"] = np.where(X.venta, 1 - X.usdc / X.acc, X.usdc / X.acc)
    X["coste"] = np.where(X.venta, X.acc - X.usdc, X.usdc)
    X = X[X.coste > 0]
    # posición en la cola: por (tx, lado comprado, precio) con >= 2 makers, orden por log_index
    X["nivel"] = X.pc.round(3)
    g = X.groupby(["tx", "lado_c", "nivel"]).li
    X["n_niv"] = g.transform("size")
    X["rk"] = g.rank(method="first")
    X["cola"] = np.where(X.n_niv < 2, "solo", np.where(X.rk == 1, "cabeza", np.where(X.rk == X.n_niv, "final", "medio")))
    C = X[(X.pc > 0.10) & (X.pc <= 0.30) & (X["T"] > 60) & (X["T"] <= 300)].copy()
    des = desenlaces(set(X.mkt))
    cob = pd.Series(list(set(X.mkt))).map(des).notna().mean() if len(X) else 0.0
    C["des"] = C.mkt.map(des)
    C = C[C.des.notna()]
    C["pnl"] = np.where(C.lado_c == C.des, C.acc, 0.0) - C.coste
    # compra equivalente de lado_c: acciones = acc (una venta de un token a p = compra de acc acciones del contrario a 1-p)
    filas = []
    for (mkt, lado_c), u in C.groupby(["mkt", "lado_c"]):
        fin = u[u.cola == "final"]
        filas.append({"dia": d, "mkt": mkt, "lado": lado_c, "act": u.act.iloc[0], "pnl": u.pnl.sum(), "coste": u.coste.sum(),
                      "pnl_final": fin.pnl.sum(), "coste_final": fin.coste.sum(), "n": len(u)})
    return pd.DataFrame(filas), float(cob)


def media_ic_dias(ev_dia):
    """Media de días e IC90 por bootstrap de DÍAS."""
    v = np.asarray(ev_dia, float)
    if len(v) < 2:
        return float(v.mean()) if len(v) else float("nan"), (float("nan"), float("nan"))
    m = v[RNG.integers(0, len(v), size=(2000, len(v)))].mean(1)
    return float(v.mean()), (float(np.quantile(m, .05)), float(np.quantile(m, .95)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--telegram", action="store_true")
    a = ap.parse_args()
    if hashlib.sha256(CONGELADA.read_bytes()).hexdigest() != SHA:
        msg = "🚨 Vigía 5m barato MAKER: la hipótesis congelada CAMBIÓ (hash distinto): no corro"
        print(msg)
        if a.telegram:
            from shadow_digest import enviar_telegram
            enviar_telegram(msg)
        sys.exit(2)
    OUT.mkdir(exist_ok=True)
    hoy = datetime.now(timezone.utc).date()
    d = PRIMER_DIA
    cobs = {}
    while d < hoy:
        ds = d.isoformat()
        cache = OUT / f"unidades_{ds}.csv.gz"
        meta = OUT / f"cobertura_{ds}.json"
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
    lin = ["🧊 Vigía forward H5M-BARATO-MAKER-v1 (congelada 09-Oct 17:05Z): makers 5m compran 0,10-0,30 a T 60-300 s; "
           "unidad mercado-lado, desenlace oficial, sin reembolso. Solo días >= 09-Oct."]
    res = {"hipotesis": "H5M-BARATO-MAKER-v1", "dias": {}, "cobertura": cobs}
    if not fs:
        lin.append("Sin días forward todavía.")
    else:
        U = pd.concat([pd.read_csv(f) for f in fs], ignore_index=True)
        U["ev"] = U.pnl / U.coste
        F = U[U.coste_final > 0].copy()
        F["ev"] = F.pnl_final / F.coste_final
        por_dia = U.groupby("dia").agg(n=("ev", "size"), ev=("ev", "mean"), pnl=("pnl", "sum"), coste=("coste", "sum"))
        fin_dia = F.groupby("dia").ev.mean()
        sinbtc_dia = U[U.act != "BTC"].groupby("dia").ev.mean()
        for ds, r in por_dia.iterrows():
            res["dias"][ds] = {"n": int(r.n), "ev": round(r.ev, 4), "ev_final_cola": round(float(fin_dia.get(ds, np.nan)), 4),
                               "ev_sin_btc": round(float(sinbtc_dia.get(ds, np.nan)), 4), "cobertura": cobs.get(ds)}
            lin.append(f"  {ds}: unidades {int(r.n)} | EV/€ {r.ev:+.4f} | final de la cola {fin_dia.get(ds, np.nan):+.4f} "
                       f"| sin BTC {sinbtc_dia.get(ds, np.nan):+.4f} | cobertura {cobs.get(ds, 0):.1%}")
        m, (lo, hi) = media_ic_dias(por_dia.ev.values)
        mf, (lof, hif) = media_ic_dias(fin_dia.values)
        ms, (los, his) = media_ic_dias(sinbtc_dia.values)
        pos = por_dia.pnl.clip(lower=0)
        top_dia = float(pos.max() / pos.sum()) if pos.sum() > 0 else float("nan")
        g = {"G1_dias>=5": len(por_dia) >= 5, "G2_EV>=0,05": m >= 0.05, "G3_IC90_dias>0": lo > 0,
             "G4_sin_BTC>0": ms > 0, "G5_ningun_dia>40%": top_dia <= 0.40, "G6_final_cola>0": mf > 0 and lof > 0}
        res.update({"ev_medio_dias": m, "ic90_dias": [lo, hi], "ev_final_cola": mf, "ic90_final_cola": [lof, hif],
                    "ev_sin_btc": ms, "top_dia_pnl": top_dia, "gates": g,
                    "veredicto": "CONFIRMADA" if all(g.values()) else "EN_CURSO"})
        lin.append(f"ACUMULADO {len(por_dia)} días, {len(U)} unidades: EV/€ {m:+.4f} IC90 días ({lo:+.4f},{hi:+.4f}) | final de la cola "
                   f"{mf:+.4f} ({lof:+.4f},{hif:+.4f}) n={len(F)} | sin BTC {ms:+.4f} | día top {top_dia:.0%} del PnL")
        lin.append("gates: " + " ".join(f"{k}{'✅' if v else '❌'}" for k, v in g.items()))
        lin.append(f"VEREDICTO: {res['veredicto']} (in-sample 06-08: +0,138; nada pasa a dinero sin gates + /code-review + OK Javi)")
    txt = "\n".join(lin)
    (OUT / "informe.txt").write_text(txt + "\n")
    (OUT / "informe.json").write_text(json.dumps(res, indent=1, default=str))
    print(txt)
    if a.telegram:
        from shadow_digest import enviar_telegram
        enviar_telegram(txt)


if __name__ == "__main__":
    main()
