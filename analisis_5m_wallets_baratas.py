#!/usr/bin/env python3
"""analisis_5m_wallets_baratas.py — (Javi 15-Oct) universo de wallets que COMPRAN MUY BARATO en mercados 5m: ¿hay
wallets con ventaja real y persistente cuando operan a precio bajo, y qué hacen? FASE 1 = lo VISIBLE (on-chain).
SOLO LECTURA. Fuente: m5_onchain (OrderFilled; contabilidad idéntica a analisis_5m_barato_quien_gana.py: la fila es
del dueño de la orden `maker`; taker == exchange -> esa orden era TOMADORA y paga `fee`). Desenlace OFICIAL.
Universo: COMPRAS (side 0) a precio <= 0,20 en mercados 5m (BTC = principal; resto de monedas solo diagnóstico),
bandas [0,00-0,10] y (0,10-0,20]. Unidad de PnL = (wallet, mercado, token) con todos sus rellenos baratos.
Persistencia SIN selección por resultado: se eligen wallets con días SEL (05-09 Oct) y se miden en días TEST (10-14):
  GANADORA_SEL = >= 15 unidades, PnL > 0 y >= 3 días positivos en SEL; se compara su EV en TEST con el de TODAS las wallets
  del universo en TEST (placebo) y con las PERDEDORA_SEL (mismo criterio con PnL < 0).
Salida: datalogs/m5barato_mision/baratas_unidades_D.csv.gz (caché), baratas_wallets.csv, baratas_informe.txt
Uso: nice -n 19 ionice -c3 python3 analisis_5m_wallets_baratas.py
"""
import gzip
import sys
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_5m_barato_quien_gana import mapas, EXCH  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5barato_mision")
SEL = [f"2026-10-{d:02d}" for d in range(5, 10)]
TEST = [f"2026-10-{d:02d}" for d in range(10, 15)]
P_MAX = 0.20


def unidades_dia(d):
    """(wallet, mercado, token) -> compras baratas agregadas del día, con desenlace oficial. Caché por día."""
    c = OUT / f"baratas_unidades_{d}.csv.gz"
    if c.exists():
        return pd.read_csv(c, dtype={"wallet": str, "mercado": str, "token": str})
    tok = mapas(d)["5min"]                                # token -> (activo, mercado, cierre, lado)
    f = VOL / "m5_onchain" / f"m5_onchain_{d}.csv.gz"
    partes = []
    with gzip.open(f, "rt") as fh:
        for x in pd.read_csv(fh, chunksize=300_000, dtype={"token_id": str, "maker": str, "taker": str},
                             usecols=["tipo", "ts_est", "maker", "taker", "side", "token_id", "maker_amt", "taker_amt",
                                      "fee"]):
            x = x[(x.tipo == "F") & (x.side == 0) & x.token_id.isin(tok.keys())]
            if not len(x):
                continue
            usdc, acc = x.maker_amt.astype(float), x.taker_amt.astype(float)
            precio = usdc / acc.where(acc > 0)
            x = x.assign(usdc=usdc, acc=acc, precio=precio)
            x = x[(x.precio > 0) & (x.precio <= P_MAX)]
            if not len(x):
                continue
            info = x.token_id.map(tok)
            x = x.assign(activo=[i[0] for i in info], mercado=[str(i[1]) for i in info], cierre=[i[2] for i in info],
                         lado=[i[3] for i in info], tomador=(x.taker.str.lower() == EXCH).astype(int),
                         T=[i[2] for i in info] - x.ts_est.astype(float))
            partes.append(x[["maker", "token_id", "activo", "mercado", "cierre", "lado", "tomador", "T", "precio",
                             "usdc", "acc", "fee"]])
    if not partes:
        return None
    x = pd.concat(partes, ignore_index=True).rename(columns={"maker": "wallet", "token_id": "token"})
    x["wallet"] = x.wallet.str.lower()
    des = desenlaces(set(x.mercado))
    x["gana"] = [1 if des.get(m) == l else (0 if des.get(m) in ("YES", "NO") else -1)
                 for m, l in zip(x.mercado, x.lado)]
    x = x[x.gana >= 0]
    x["banda"] = np.where(x.precio <= 0.10, "0-0.10", "0.10-0.20")
    g = x.groupby(["wallet", "mercado", "token", "activo", "lado", "banda"], as_index=False).agg(
        usdc=("usdc", "sum"), acc=("acc", "sum"), fee=("fee", "sum"), gana=("gana", "first"),
        rellenos=("precio", "size"), tomador=("tomador", "mean"), T_med=("T", "median"), precio_med=("precio", "median"),
        cierre=("cierre", "first"))
    g["pnl"] = g.acc * g.gana - g.usdc - g.fee
    g["dia"] = d
    OUT.mkdir(parents=True, exist_ok=True)
    g.to_csv(c, index=False, compression="gzip")
    return g


def ev(df):
    return float(df.pnl.sum() / df.usdc.sum()) if len(df) and df.usdc.sum() > 0 else float("nan")


def ic90_dias(df):
    pd_ = df.groupby("dia").apply(lambda z: z.pnl.sum() / z.usdc.sum() if z.usdc.sum() > 0 else np.nan).dropna().values
    if len(pd_) < 3:
        return None
    b = np.random.default_rng(7).choice(pd_, size=(5000, len(pd_))).mean(axis=1)
    return round(float(np.percentile(b, 5)), 3), round(float(np.percentile(b, 95)), 3)


def main():
    todos = [u for u in (unidades_dia(d) for d in SEL + TEST) if u is not None]
    u = pd.concat(todos, ignore_index=True)
    lines = [f"WALLETS QUE COMPRAN BARATO (<= {P_MAX}) en 5m — SEL {SEL[0]}..{SEL[-1]}, TEST {TEST[0]}..{TEST[-1]}",
             "Unidad = (wallet, mercado, token) en una banda; PnL a desenlace OFICIAL con comisión; EV por € invertido."]
    for activo_txt, sub in (("BTC", u[u.activo == "BTC"]), ("resto (diagnóstico)", u[u.activo != "BTC"])):
        lines.append(f"\n== {activo_txt}")
        for banda in ("0-0.10", "0.10-0.20"):
            s = sub[sub.banda == banda]
            lines.append(f"  banda {banda}: unidades {len(s)} wallets {s.wallet.nunique()} mercados {s.mercado.nunique()} "
                         f"invertido {s.usdc.sum():,.0f} $ | EV/€ {ev(s):+.3f} | acierto {s.gana.mean():.3f} vs precio "
                         f"medio pond. {s.usdc.sum() / s.acc.sum():.3f} | maker {1 - s.tomador.mean():.0%}")
            for rol, rr in (("maker", s[s.tomador < 0.5]), ("tomador", s[s.tomador >= 0.5])):
                lines.append(f"     {rol:8s} n {len(rr):6d} EV/€ {ev(rr):+.3f} acierto {rr.gana.mean() if len(rr) else 0:.3f}")
    # persistencia (BTC, ambas bandas juntas por wallet)
    b = u[u.activo == "BTC"]
    sel, test = b[b.dia.isin(SEL)], b[b.dia.isin(TEST)]
    w = sel.groupby("wallet").agg(n=("pnl", "size"), pnl=("pnl", "sum"), usdc=("usdc", "sum"),
                                  dias_pos=("dia", lambda z: 0))
    dp = sel.groupby(["wallet", "dia"]).pnl.sum().gt(0).groupby("wallet").sum()
    w["dias_pos"] = dp
    gan = w[(w.n >= 15) & (w.pnl > 0) & (w.dias_pos >= 3)].index
    per = w[(w.n >= 15) & (w.pnl < 0) & (w.dias_pos <= 2)].index
    lines.append(f"\n== PERSISTENCIA BTC (selección con SEL, medida en TEST; placebo = todo el universo en TEST)")
    for nom, ws in (("GANADORA_SEL", gan), ("PERDEDORA_SEL", per)):
        t = test[test.wallet.isin(ws)]
        lines.append(f"  {nom:14s} wallets {len(ws):4d} (activas en TEST {t.wallet.nunique()}) | SEL EV/€ "
                     f"{ev(sel[sel.wallet.isin(ws)]):+.3f} -> TEST EV/€ {ev(t):+.3f} IC90 días {ic90_dias(t)} "
                     f"| unidades TEST {len(t)} invertido {t.usdc.sum():,.0f} $")
    lines.append(f"  PLACEBO todo TEST: EV/€ {ev(test):+.3f} IC90 días {ic90_dias(test)} | unidades {len(test)}")
    # ranking de wallets persistentes (positivas en SEL y TEST) para la FASE 2 (lo invisible)
    wt = test.groupby("wallet").agg(n_t=("pnl", "size"), pnl_t=("pnl", "sum"), usdc_t=("usdc", "sum"))
    r = w.join(wt, how="inner")
    r = r[(r.index.isin(gan)) & (r.pnl_t > 0)].copy()
    r["ev_sel"], r["ev_test"] = r.pnl / r.usdc, r.pnl_t / r.usdc_t
    r = r.sort_values("pnl_t", ascending=False)
    lines.append(f"\n  persistentes (ganadora en SEL y PnL>0 en TEST): {len(r)} de {len(gan)}")
    for wa, x in r.head(15).iterrows():
        sx = b[b.wallet == wa]
        lines.append(f"   {wa[:12]} SEL n {int(x.n):4d} EV {x.ev_sel:+.2f} | TEST n {int(x.n_t):4d} EV {x.ev_test:+.2f} "
                     f"PnL {x.pnl_t:+8.0f} $ | maker {1 - sx.tomador.mean():.0%} precio med {sx.precio_med.median():.3f} "
                     f"T med {sx.T_med.median():.0f} s | banda<=0,10 {(sx.banda == '0-0.10').mean():.0%}")
    r.to_csv(OUT / "baratas_wallets.csv")
    txt = "\n".join(lines)
    print(txt)
    (OUT / "baratas_informe.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
