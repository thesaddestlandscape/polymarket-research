#!/usr/bin/env python3
"""analisis_5m_v1_quien_gana.py -- MISIÓN 5M v1 (09-Oct, Javi: "iniciar la investigación de 5m de la misma forma que
15m, ya sabes cómo hacerlo y dónde mirar"). Réplica en 5m del paso que DECIDIÓ la misión 15m v4
(analisis_15m_v4_quien_gana.py: quién gana on-chain y con qué ESTRUCTURA -> cosechadores de PARES + certeza terminal).

Misma contabilidad que el de 15m (formato on-chain verificado en analisis_15m_v3_quien_barre.py): fila con taker ==
contrato del exchange = orden TOMADORA (su campo maker es la wallet tomadora); resto = relleno de un MAKER; side 0 BUY
(maker_amt USDC, taker_amt acciones) / 1 SELL (al revés); fee en USDC solo al tomador. PnL a RESOLUCIÓN con desenlace
oficial (gamma closed=true); reembolso del maker ESTIMADO = 20 % de la comisión del tomador (aparte, nunca sumado).
Diferencias con el de 15m: (1) datos del archivo m5_onchain (volumen, 60 d) y mapa k de m15_registro (guarda las k de
TODOS los marcos); (2) el 5m tiene ~4x filas: se carga DÍA A DÍA y wallets/tx pasan a enteros nada más leer (sin
esto la RAM se acercaba al umbral de guard_ram); (3) persistencia en TODOS los pares de días consecutivos; (4) perfil
de pares por wallet (P(mercado con ambos lados), coste medio del par emparejado) también en el top por PnL.
Uso: (ulimit -v 4500000; nice -n 19 ionice -c3 python3 analisis_5m_v1_quien_gana.py --dias 2026-10-06,2026-10-07,2026-10-08)
Fuera del racimo de crons 06-09Z.
"""
import argparse
import gzip
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

DL = Path("/root/polymarket-research-datalogs")
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"
INF = Path(__file__).resolve().parent / "informes" / "m5v1_quien_gana_09oct.txt"
SALIDA = DL / "m5_cache"


def mapa_tokens(dias, marco="5min"):
    m = {}
    vistos = set()
    for d in dias:
        for k in (-1, 0, 1):
            dd = (date.fromisoformat(d) + timedelta(days=k)).isoformat()
            f = VOL / "m15_registro" / f"m15_registro_{dd}.csv.gz"
            if dd in vistos or not f.exists():
                continue
            vistos.add(dd)
            with gzip.open(f, "rt", errors="replace") as fh:
                try:
                    for ln in fh:
                        if ln.startswith("k,"):
                            c = ln.rstrip("\n").split(",")
                            if len(c) >= 8 and c[4] == marco:
                                m[c[2]] = (c[3], c[5], int(datetime.fromisoformat(c[6]).timestamp()), c[7])
                except (EOFError, OSError):
                    pass
    return m


def cargar(dias, tok, solo_makers=False):
    """Un DataFrame compacto: wallet y tx como enteros (nombres de wallet en `nombres`)."""
    wid, nombres, partes, tom = {}, [], [], []
    t_act = {t: v[0] for t, v in tok.items()}
    t_mkt = {t: v[1] for t, v in tok.items()}
    t_fin = {t: v[2] for t, v in tok.items()}
    t_lado = {t: v[3] for t, v in tok.items()}
    txid = {}

    def ids(vals, dic, lista=None):
        out = np.empty(len(vals), dtype=np.int64)
        for j, v in enumerate(vals):
            k = dic.get(v)
            if k is None:
                k = dic[v] = len(dic)
                if lista is not None:
                    lista.append(v)
            out[j] = k
        return out
    for i, d in enumerate(dias):
        txid.clear()                                            # tx únicas por día (ids desplazados por día)
        base = i * 10**9
        n_dia = 0
        with gzip.open(VOL / "m5_onchain" / f"m5_onchain_{d}.csv.gz", "rt") as fh:
            # por bloques: el pico transitorio de cadenas (tx, wallets, token) no crece con el tamaño del día
            for x in pd.read_csv(fh, chunksize=150_000, dtype={"token_id": str, "maker": str, "taker": str, "tx": str},
                                 usecols=["tipo", "ts_est", "tx", "maker", "taker", "side", "token_id", "maker_amt", "taker_amt", "fee"]):
                x = x[(x.tipo == "F") & x.token_id.isin(tok.keys())]
                if solo_makers and len(x):      # 09-Oct tarde (RAM): tomadores fuera ANTES de construir nada
                    t_ = x[x.taker == EXCH]
                    tom.append(pd.DataFrame({"tx": ids(t_.tx.values, txid) + base, "fee": t_.fee.astype(float).values}))
                    x = x[x.taker != EXCH]
                    del t_
                if not len(x):
                    continue
                # 09-Oct tarde: map a valores COMPARTIDOS (una cadena por token, no una por fila: `.str[i]` creaba
                # ~4,6 M x 4 cadenas nuevas y el guardián de RAM paró el análisis dos veces)
                tk = x.token_id
                y = pd.DataFrame({"dia": d, "ts_est": x.ts_est.astype(float).values, "side": x.side.astype("int8").values,
                                  "maker_amt": x.maker_amt.astype(float).values, "taker_amt": x.taker_amt.astype(float).values,
                                  "fee": x.fee.astype(float).values, "tomador": (x.taker == EXCH).values,
                                  "tx": ids(x.tx.values, txid) + base, "wallet": ids(x.maker.values, wid, nombres).astype(np.int32),
                                  "act": tk.map(t_act).values, "mkt": tk.map(t_mkt).values,
                                  "fin": tk.map(t_fin).astype(float).values, "lado": tk.map(t_lado).values})
                n_dia += len(y)
                partes.append(y)
                del x, tk
        print(f"{d}: {n_dia:,} rellenos 5m", file=sys.stderr, flush=True)
    return pd.concat(partes, ignore_index=True), nombres, (pd.concat(tom, ignore_index=True) if tom else None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", default="2026-10-06,2026-10-07,2026-10-08")
    ap.add_argument("--solo-makers", action="store_true",
                    help="solo secciones 3-4 (filas maker; de los tomadores solo la comisión por tx): menos RAM")
    a = ap.parse_args()
    global INF
    if a.solo_makers:
        INF = INF.with_name(INF.stem.replace("quien_gana", "quien_gana_makers") + INF.suffix)
    dias = a.dias.split(",")
    tok = mapa_tokens(dias)
    print(f"tokens 5m: {len(tok)}", file=sys.stderr)
    X, nombres, tom = cargar(dias, tok, a.solo_makers)
    des = desenlaces(set(X.mkt))
    X["des"] = X.mkt.map(des)
    cob = X.drop_duplicates("mkt").des.notna().mean()
    n_merc = X.mkt.nunique()
    X = X[X.des.notna()].copy()
    buy = X.side == 0
    X["acc"] = np.where(buy, X.taker_amt, X.maker_amt)
    X["usdc"] = np.where(buy, X.maker_amt, X.taker_amt)
    X = X[X.acc > 0].copy()
    buy = X.side == 0
    X["p"] = X.usdc / X.acc
    win = (X.lado == X.des).astype(float)
    X["rol"] = np.where(X.tomador, "tomador", "maker")
    X["pnl"] = np.where(buy, X.acc * win - X.usdc, X.usdc - X.acc * win) - np.where(X.tomador, X.fee, 0.0)
    X["T"] = X.fin - X.ts_est
    X["firm"] = np.where(buy, 1, -1) * np.where(X.lado == "YES", 1, -1)   # +1 = largo YES
    fee_tx = (tom.groupby("tx").fee.sum() if tom is not None else X[X.tomador].groupby("tx").fee.sum())
    del tom
    mk = ~X.tomador
    acc_tx = X[mk].groupby("tx").acc.sum()
    X["rebate_est"] = 0.0
    X.loc[mk, "rebate_est"] = 0.2 * X.loc[mk, "tx"].map(fee_tx).fillna(0).values * X.loc[mk, "acc"].values / X.loc[mk, "tx"].map(acc_tx).values
    # 09-Oct tarde (RAM): columnas que ya no se usan
    X.drop(columns=["maker_amt", "taker_amt", "tx", "ts_est", "fin", "des", "tomador"], inplace=True)
    del fee_tx, acc_tx, mk, buy, win
    import gc
    gc.collect()
    lin = []

    def L(s=""):
        print(s, flush=True)
        lin.append(s)

    def nom(w):
        return nombres[int(w)][:10]

    W = None
    if a.solo_makers:
        L(f"Rellenos 5m on-chain {dias[0]}..{dias[-1]} (SOLO MAKERS, secciones 3-4): {len(X)} filas, {X.mkt.nunique()} mercados "
          f"resueltos de {n_merc} (cobertura desenlace {cob:.1%}). Secciones 1-2: logs/mision5m_quien_gana.log (16:19Z)")
    else:
        L(f"Rellenos 5m on-chain {dias[0]}..{dias[-1]}: {len(X)} filas, {X.mkt.nunique()} mercados resueltos de {n_merc} "
          f"(cobertura desenlace {cob:.1%})")
        L("\n1) PnL AGREGADO A RESOLUCIÓN por rol y día (USDC)")
        g = X.groupby(["dia", "rol"]).agg(filas=("pnl", "size"), vol=("usdc", "sum"), pnl=("pnl", "sum"), fee=("fee", "sum"),
                                          rebate=("rebate_est", "sum"), wallets=("wallet", "nunique"))
        g["pnl_por_vol"] = g.pnl / g.vol
        L(g.round(3).to_string())
        L("\n1b) por activo (3 días): volumen, PnL maker / tomador")
        ga = X.groupby(["act", "rol"]).agg(vol=("usdc", "sum"), pnl=("pnl", "sum")).unstack()
        L(ga.round(0).to_string())
        W = X.groupby(["rol", "wallet", "dia"]).agg(n=("pnl", "size"), merc=("mkt", "nunique"), vol=("usdc", "sum"),
                                                     pnl=("pnl", "sum"), rebate=("rebate_est", "sum")).reset_index()
        for rol in ("maker", "tomador"):
            w = W[W.rol == rol].groupby("wallet").agg(dias=("dia", "nunique"), n=("n", "sum"), merc=("merc", "sum"),
                                                       vol=("vol", "sum"), pnl=("pnl", "sum"), rebate=("rebate", "sum"))
            w["pnl_vol"] = w.pnl / w.vol
            tot_pos = w.pnl[w.pnl > 0].sum()
            L(f"\n2) {rol.upper()}: {len(w)} wallets; PnL total {w.pnl.sum():+.0f}; ganancias brutas de las ganadoras {tot_pos:+.0f}; "
              f"top10 ganadoras = {w.pnl.nlargest(10).sum() / tot_pos:.0%} de ellas; top10 por volumen = {w.vol.nlargest(10).sum() / w.vol.sum():.0%} del volumen")
            for titulo, orden in (("top 15 por PnL", "pnl"), ("top 10 por VOLUMEN", "vol")):
                L(f"   {titulo}:")
                for wa, r in w.sort_values(orden, ascending=False).head(15 if orden == "pnl" else 10).iterrows():
                    L(f"   {nom(wa)} días={r.dias} n={int(r.n):7d} vol={r.vol:10.0f} PnL={r.pnl:+9.0f} PnL/vol={r.pnl_vol:+.3f} rebate_est={r.rebate:6.0f}")
            for d1, d2 in zip(dias, dias[1:]):
                p = W[(W.rol == rol) & W.dia.isin([d1, d2])].pivot_table(index="wallet", columns="dia", values=["pnl", "vol"]).dropna()
                p = p[(p[("vol", d1)] >= 2000) & (p[("vol", d2)] >= 2000)]
                if len(p) >= 10:
                    x1, x2 = p[("pnl", d1)] / p[("vol", d1)], p[("pnl", d2)] / p[("vol", d2)]
                    L(f"   PERSISTENCIA {d1[5:]}→{d2[5:]} ({len(p)} wallets ≥2.000 USDC ambos días): Spearman PnL/vol {x1.corr(x2, method='spearman'):+.3f}; "
                      f"positivas ambos {int(((x1 > 0) & (x2 > 0)).sum())}, negativas ambos {int(((x1 < 0) & (x2 < 0)).sum())}, cambian {int(((x1 > 0) != (x2 > 0)).sum())}")
    L("\n3) PERFIL MAKERS (vol ≥2.000 USDC TODOS los días): ganadoras todos los días vs resto")
    # 09-Oct tarde: desde aquí solo hacen falta las filas MAKER y estas columnas; X entero se libera (el guardián de RAM
    # paró el análisis en esta sección con X + copias en memoria)
    M = X.loc[X.rol == "maker", ["dia", "wallet", "mkt", "lado", "side", "firm", "acc", "usdc", "pnl", "rebate_est", "p",
                                 "T", "act"]]
    del X
    W = None
    gc.collect()
    wd = M.groupby(["wallet", "dia"]).agg(vol=("usdc", "sum"), pnl=("pnl", "sum")).unstack().dropna()
    ok = wd[(wd["vol"] >= 2000).all(axis=1)]
    ganw = set(ok[(ok["pnl"] > 0).all(axis=1)].index)
    perw = set(ok.index) - ganw

    def perfil(ws, etiqueta):
        q = M[M.wallet.isin(ws)]
        if len(q) == 0:
            L(f"  {etiqueta}: 0 wallets")
            return
        pm = q.groupby(["wallet", "mkt", "lado"]).size().unstack(fill_value=0)
        ambos = ((pm.get("YES", 0) > 0) & (pm.get("NO", 0) > 0)).mean()
        q2 = q.assign(pos=q.firm * q.acc)
        neto = q2.groupby(["wallet", "mkt"]).pos.sum().abs().sum() / q2.acc.sum()
        L(f"  {etiqueta}: wallets={len(ws)} rellenos={len(q)} vol={q.usdc.sum():.0f} PnL={q.pnl.sum():+.0f} PnL/vol={q.pnl.sum() / q.usdc.sum():+.4f} "
          f"rebate_est={q.rebate_est.sum():.0f} | precio medio {q.p.mean():.3f}, P(p<0,2 o >0,8) {((q.p < 0.2) | (q.p > 0.8)).mean():.0%}, "
          f"rellenos T<60s {(q['T'] < 60).mean():.0%}, T<120s {(q['T'] < 120).mean():.0%}, mercados con ambos lados {ambos:.0%}, "
          f"|posición neta| / acciones {neto:.2f}, tamaño mediano {q.acc.median():.0f} acc")
    perfil(ganw, "GANADORAS todos los días")
    perfil(perw, "RESTO (≥2.000 todos los días)")
    L("\n3b) ESTRUCTURA de los 15 makers con más PnL (pares vs direccional): % mercados con ambos lados, |neto|/acciones, "
      "coste medio del par (precio medio YES + precio medio NO comprados, mercados con ambos lados)")
    top = M.groupby("wallet").pnl.sum().nlargest(15).index
    for wa in top:
        q = M[(M.wallet == wa) & (M.side == 0)]
        if len(q) == 0:
            continue
        pm = q.groupby(["mkt", "lado"]).apply(lambda s: pd.Series({"acc": s.acc.sum(), "usdc": s.usdc.sum()}), include_groups=False).unstack()
        both = pm.dropna()
        coste = ((both[("usdc", "YES")] / both[("acc", "YES")]) + (both[("usdc", "NO")] / both[("acc", "NO")])).median() if len(both) else float("nan")
        q2 = M[M.wallet == wa].assign(pos=lambda d: d.firm * d.acc)
        neto = q2.groupby("mkt").pos.sum().abs().sum() / q2.acc.sum()
        L(f"   {nom(wa)} PnL={M[M.wallet == wa].pnl.sum():+8.0f} mercados={q.mkt.nunique():5d} ambos_lados={len(both) / max(1, len(pm)):.0%} "
          f"|neto|/acc={neto:.2f} coste_par_mediano={coste:.3f} T<60s={(q['T'] < 60).mean():.0%} act={q.act.value_counts().index[0]}")
    L("\n4) PnL MAKER por fase del ciclo y banda de precio (todos los makers)")
    MM = M
    t = MM.groupby([pd.cut(MM["T"], [-60, 0, 15, 30, 60, 120, 200, 300, 2000]), pd.cut(MM.p, [0, 0.1, 0.3, 0.5, 0.7, 0.9, 1])], observed=True).agg(
        vol=("usdc", "sum"), pnl=("pnl", "sum"))
    t["pnl_vol"] = t.pnl / t.vol
    L(t.round(4).to_string())
    INF.write_text("\n".join(lin) + "\n")
    SALIDA.mkdir(exist_ok=True)
    M.assign(wallet_hex=M.wallet.map(lambda w: nombres[int(w)])).to_parquet(SALIDA / "v1_quien_gana_makers.parquet")
    print(f"informe: {INF}", file=sys.stderr)


if __name__ == "__main__":
    main()
