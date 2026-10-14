#!/usr/bin/env python3
"""analisis_h5m_quien_gana_banda.py -- H5M parte 2 (Javi 14-Oct, opción 2): ¿QUIÉN se lleva el +0,13 €/€ de la celda
H5M-BARATO-MAKER-v1 (makers 5m que compran 0,10-0,30 a T 60-300 s) y CÓMO cotiza, para copiar el mecanismo y no el
resultado? Contexto: nuestra cola simulada (analisis_h5m_cola_simulada.py) da −0,05 en SEGUIR: las rellenas enteras
(barridos) pierden, las parciales ganan.

Datos: on-chain m5_onchain_D (mismas reglas que vigia_5m_barato_maker_forward.unidades_dia, + wallet maker, order_hash,
hora de bloque) y Binance aggTrade del registro ms (m5_registro_D, fila x, reloj de recepción).
Por wallet (5 días): unidades (mercado, lado), EV/€ (suma pnl / suma coste), días positivos.
Grupos (fijados antes de mirar): GANADORA = >= 100 unidades, EV/€ >= +0,05 y >= 4 de 5 días con PnL > 0;
PERDEDORA = >= 100 unidades y EV/€ < 0; RESTO.
Rasgos por grupo y EV dentro de cada rasgo:
  - tamaño del relleno; rellenos por order_hash; órdenes distintas por unidad (¿recotizan?);
  - vía: compra directa del lado barato vs VENTA del favorito (ask) ;
  - barrido: la tx rellena a makers del mismo lado a >= 2 precios distintos (el tomador atravesó niveles);
  - posición en la cola dentro de la tx (solo/cabeza/medio/final, como el vigía);
  - Binance en contra en [t-3 s, t] (hora de bloque, resolución ~2 s: comparación ENTRE grupos, no absoluta);
  - pares: la misma wallet también compra el otro lado del mismo mercado en la celda o fuera de ella;
  - T y precio.
Uso: nice -n 19 ionice -c3 python3 analisis_h5m_quien_gana_banda.py --desde 2026-10-09 --hasta 2026-10-13
Salida: datalogs/h5m_cola_sim/quien_gana_rellenos.csv.gz + quien_gana_informe.txt
"""
import argparse
import gzip
import sys
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_5m_v1_quien_gana import mapa_tokens  # noqa: E402
from analisis_h5m_cola_simulada import OUT  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"
VENTANA_BN_S = 3.0


def binance_dia(d):
    """moneda -> (t_rx en s ordenado, precio) del registro ms del día (y de los bordes del día vecino no hace falta:
    los mercados 5m caen dentro del día salvo los primeros minutos)."""
    f = VOL / "m5_registro" / f"m5_registro_{d}.csv.gz"
    acc = {}
    with gzip.open(f, "rt", errors="replace") as fh:
        try:
            for ln in fh:
                if ln[:2] != "x,":
                    continue
                c = ln.split(",")
                try:
                    acc.setdefault(c[2][:-4], ([], []))
                    t, p = int(c[7]) / 1000.0, float(c[3])
                except (ValueError, IndexError):
                    continue
                acc[c[2][:-4]][0].append(t)
                acc[c[2][:-4]][1].append(p)
        except (EOFError, OSError):
            pass
    out = {}
    for m, (t, p) in acc.items():
        t, p = np.asarray(t), np.asarray(p)
        o = np.argsort(t, kind="stable")
        out[m] = (t[o], p[o])
    return out


def contra_bn(bn, act, lado, ts):
    """Movimiento máximo en contra (bps) en [ts - VENTANA, ts] respecto a p(ts - VENTANA), vectorizado por moneda."""
    res = np.full(len(ts), np.nan)
    for mon in np.unique(act):
        if mon not in bn:
            continue
        t, p = bn[mon]
        idx = np.where(act == mon)[0]
        i0 = np.searchsorted(t, ts[idx] - VENTANA_BN_S)
        i1 = np.searchsorted(t, ts[idx], side="right")
        for k, j in enumerate(idx):
            a, b = i0[k], i1[k]
            if b <= a or a == 0:
                continue
            p0 = p[a - 1]
            tramo = p[a:b]
            res[j] = (p0 - tramo.min()) / p0 * 1e4 if lado[j] == "YES" else (tramo.max() - p0) / p0 * 1e4
    return res


def rellenos_dia(d):
    f = VOL / "m5_onchain" / f"m5_onchain_{d}.csv.gz"
    if not f.exists():
        return None
    tok = mapa_tokens([d])
    t_act = {t: v[0] for t, v in tok.items()}
    t_mkt = {t: v[1] for t, v in tok.items()}
    t_fin = {t: v[2] for t, v in tok.items()}
    t_lado = {t: v[3] for t, v in tok.items()}
    partes = []
    with gzip.open(f, "rt") as fh:
        for x in pd.read_csv(fh, chunksize=150_000, dtype={"token_id": str, "tx": str, "maker": str, "taker": str,
                                                            "order_hash": str},
                             usecols=["tipo", "ts_est", "tx", "log_index", "order_hash", "maker", "taker", "side",
                                      "token_id", "maker_amt", "taker_amt"]):
            x = x[(x.tipo == "F") & (x.taker != EXCH) & x.token_id.isin(tok.keys())]
            if not len(x):
                continue
            tk = x.token_id
            venta = x.side.values == 1
            partes.append(pd.DataFrame({
                "tx": x.tx.values, "li": x.log_index.astype(int).values, "oh": x.order_hash.values,
                "wallet": x.maker.str.lower().values, "act": tk.map(t_act).values, "mkt": tk.map(t_mkt).values,
                "ts": x.ts_est.astype(float).values, "T": tk.map(t_fin).astype(float).values - x.ts_est.astype(float).values,
                "lado": tk.map(t_lado).values, "venta": venta,
                "acc": np.where(venta, x.maker_amt.values, x.taker_amt.values).astype(float),
                "usdc": np.where(venta, x.taker_amt.values, x.maker_amt.values).astype(float)}))
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
    X["cola"] = np.where(X.n_niv < 2, "solo", np.where(X.rk == 1, "cabeza", np.where(X.rk == X.n_niv, "final", "medio")))
    X["barrido"] = X.groupby(["tx", "lado_c"]).nivel.transform("nunique") >= 2
    # pares: la wallet compra los DOS lados del mismo mercado en cualquier precio/T del día
    lados = X.groupby(["wallet", "mkt"]).lado_c.transform("nunique")
    X["pares"] = lados >= 2
    # sin look-ahead: ¿había comprado YA el otro lado (cualquier precio/T) antes de este relleno? (hora de bloque)
    primero = X.groupby(["wallet", "mkt", "lado_c"]).ts.min()
    otro = np.where(X.lado_c == "YES", "NO", "YES")
    t_otro = pd.Series(list(zip(X.wallet, X.mkt, otro))).map(primero.to_dict()).values.astype(float)
    X["pares_antes"] = t_otro < X.ts.values
    C = X[(X.pc > 0.10) & (X.pc <= 0.30) & (X["T"] > 60) & (X["T"] <= 300)].copy()
    des = desenlaces(set(C.mkt))
    C["des"] = C.mkt.map(des)
    C = C[C.des.notna()]
    C["pnl"] = np.where(C.lado_c == C.des, C.acc, 0.0) - C.coste
    C["dia"] = d
    bn = binance_dia(d)
    C["bn_contra"] = contra_bn(bn, C.act.values, C.lado_c.values, C.ts.values)
    return C.drop(columns=["usdc", "rk", "n_niv", "lado", "li"])


def ev(df):
    return df.pnl.sum() / df.coste.sum() if len(df) and df.coste.sum() > 0 else float("nan")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-10-09")
    ap.add_argument("--hasta", default="2026-10-13")
    a = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    partes = []
    d, d1 = date.fromisoformat(a.desde), date.fromisoformat(a.hasta)
    while d <= d1:
        cache = OUT / f"quien_gana_rellenos_v2_{d}.csv.gz"
        if cache.exists():
            partes.append(pd.read_csv(cache, dtype={"wallet": str, "mkt": str, "oh": str, "tx": str}))
        else:
            C = rellenos_dia(d.isoformat())
            if C is not None:
                C.to_csv(cache, index=False, compression="gzip")
                partes.append(C)
                print(f"{d}: {len(C)} rellenos maker en la celda", flush=True)
        d += timedelta(days=1)
    C = pd.concat(partes, ignore_index=True)
    C["mkt"] = C.mkt.astype(str)
    n_dias = C.dia.nunique()
    # por wallet
    U = C.groupby(["wallet", "mkt", "lado_c"]).agg(pnl=("pnl", "sum"), coste=("coste", "sum"), dia=("dia", "first"))
    W = U.groupby("wallet").agg(unid=("pnl", "size"), pnl=("pnl", "sum"), coste=("coste", "sum"))
    W["ev"] = W.pnl / W.coste
    dpos = U.groupby(["wallet", "dia"]).pnl.sum().gt(0).groupby("wallet").sum()
    W["dias_pos"] = dpos.reindex(W.index).fillna(0).astype(int)
    W["grupo"] = "RESTO"
    W.loc[(W.unid >= 100) & (W.ev >= 0.05) & (W.dias_pos >= max(1, n_dias - 1)), "grupo"] = "GANADORA"
    W.loc[(W.unid >= 100) & (W.ev < 0), "grupo"] = "PERDEDORA"
    C["grupo"] = C.wallet.map(W.grupo)
    lin = [f"H5M quién gana en la banda ({a.desde}..{a.hasta}, {n_dias} días): {len(C)} rellenos maker, {C.wallet.nunique()} "
           f"wallets, EV/€ global {ev(C):+.4f}"]
    for gname in ("GANADORA", "PERDEDORA", "RESTO"):
        Wg = W[W.grupo == gname]
        Cg = C[C.grupo == gname]
        lin.append(f"\n{gname}: wallets {len(Wg)} | rellenos {len(Cg)} | coste {Cg.coste.sum():,.0f} $ "
                   f"({Cg.coste.sum() / C.coste.sum():.0%} del volumen) | PnL {Cg.pnl.sum():+,.0f} $ | EV/€ {ev(Cg):+.4f}")
    lin.append("\nTOP 15 wallets por PnL (unid, EV/€, días+, PnL $):")
    for w, r in W.sort_values("pnl", ascending=False).head(15).iterrows():
        lin.append(f"  {w[:10]} {r.grupo:9s} unid {int(r.unid):5d} EV {r.ev:+.3f} días+ {int(r.dias_pos)}/{n_dias} PnL {r.pnl:+8.0f}")
    # rasgos por grupo
    lin.append("\nRASGOS (mediana o %; entre corchetes EV/€ de los rellenos con ese rasgo):")
    C["n_oh"] = C.groupby("oh").acc.transform("size")
    oh_unid = C.groupby(["wallet", "mkt", "lado_c"]).oh.nunique()
    for gname in ("GANADORA", "PERDEDORA", "RESTO"):
        Cg = C[C.grupo == gname]
        if not len(Cg):
            continue
        ou = oh_unid[oh_unid.index.get_level_values(0).isin(W[W.grupo == gname].index)]
        bnv = Cg.bn_contra.dropna()
        lin.append(f"\n  {gname}:")
        lin.append(f"    relleno med {Cg.acc.median():.1f} acc | rellenos/orden med {Cg.n_oh.median():.0f} | órdenes distintas por "
                   f"unidad med {ou.median():.0f} (p90 {ou.quantile(.9):.0f}) | T med {Cg['T'].median():.0f} s | precio med "
                   f"{Cg.pc.median():.3f}")
        for nom, m in (("vía VENTA del favorito", Cg.venta), ("vía compra directa", ~Cg.venta),
                       ("en BARRIDO (>=2 niveles en la tx)", Cg.barrido), ("sin barrido", ~Cg.barrido),
                       ("cola final", Cg.cola == "final"), ("cola cabeza", Cg.cola == "cabeza"), ("solo en su nivel", Cg.cola == "solo"),
                       ("wallet hace PARES en el mercado", Cg.pares), ("solo un lado", ~Cg.pares),
                       ("  pares: otro lado YA comprado antes", Cg.pares & Cg.pares_antes),
                       ("  pares: otro lado solo DESPUÉS", Cg.pares & ~Cg.pares_antes)):
            sub = Cg[m.values]
            lin.append(f"    {nom:36s} {len(sub) / len(Cg):6.1%} de rellenos [{ev(sub):+.3f}]")
        for u in (1, 2, 3, 5):
            con = Cg[Cg.bn_contra >= u]
            lin.append(f"    Binance en contra >= {u} bps en 3 s previos {len(con) / max(1, len(bnv)):6.1%} [{ev(con):+.3f}] "
                       f"vs resto [{ev(Cg[Cg.bn_contra < u]):+.3f}]")
    txt = "\n".join(lin)
    print(txt)
    (OUT / "quien_gana_informe.txt").write_text(txt + "\n")
    W.to_csv(OUT / "quien_gana_wallets.csv")


if __name__ == "__main__":
    main()
