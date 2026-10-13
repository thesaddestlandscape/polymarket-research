#!/usr/bin/env python3
"""analisis_15m_v5_pares_cola_onchain.py -- MISIÓN 15M v5 (Javi 13-Oct) PASOS 2, 3 y 5: economía de los COSECHADORES DE
PARES on-chain y su POSICIÓN EN LA COLA, medida directamente (sin simulador).

Fuente: datalogs/m15_onchain (rellenos on-chain del exchange 0xe111…; formato de analisis_15m_v4_quien_gana.py: filas F;
fila con taker == exchange = orden TOMADORA; resto = relleno de un MAKER; side 0 BUY / 1 SELL; fee solo al tomador).
Mapa token→(activo, mercado, cierre, lado): filas k de m15_registro (marco 15min). Desenlace oficial gamma (closed=true).

1) RECONCILIACIÓN por día: suma PnL maker + tomador = −comisiones (si no cuadra → el resto no vale).
   Reembolso ESTIMADO = 0,2 × comisión del tomador de la tx, repartido entre sus makers por acciones (se reporta APARTE).
2) Universo de cosechadores: makers con ≥80 % de sus compras emparejadas (min(YES,NO)·2/compras, por mercado) y vol ≥2.000
   USDC, elegidos SOLO con DESCUBRIMIENTO 05-07; su resultado en 08-12 es forward (selección no retrospectiva).
3) Descomposición por (wallet, mercado): margen de los pares completos = emparejadas·(1 − p̄YES − p̄NO); resultado de lo
   residual = PnL − margen; reembolso aparte. Coste por par p̄YES + p̄NO.
4) COLA, observada: en cada tx, los rellenos maker del mismo token y precio aparecen en orden de PRIORIDAD (precio-tiempo,
   log_index). Rango del maker dentro de su nivel (1 = primero). Baseline: E[rango 1] = media de 1/k. Además: ¿se rellena en el
   PRIMER nivel de precio que barre la tx (= estaba en el mejor bid)?
Uso: (ulimit -v 5000000; nice -n 19 ionice -c3 python3 analisis_15m_v5_pares_cola_onchain.py)
"""
import gzip
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

VOL = Path("/mnt/HC_Volume_106538179")
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"
DIAS = [f"2026-10-{d:02d}" for d in range(5, 13)]
DESC = DIAS[:3]
INF = Path(__file__).resolve().parent / "informes" / "m15v5_pares_cola_onchain_13oct.txt"
FOCO = ["0xcfddfb6e", "0x2903c7dc"]


def tokens(d):
    m = {}
    base = datetime.fromisoformat(d)
    for dd in (base - timedelta(days=1), base, base + timedelta(days=1)):
        f = VOL / "m15_registro" / f"m15_registro_{dd:%Y-%m-%d}.csv.gz"
        if not f.exists():
            continue
        cache = Path("/root/polymarket-research-datalogs/m15v5_k_cache") / (f.name + ".k")
        if cache.exists():
            out = cache.read_text()
        else:
            out = subprocess.run(f"zcat {f} 2>/dev/null | grep -a '^k,'", shell=True, capture_output=True).stdout.decode()
            cache.parent.mkdir(exist_ok=True)
            cache.write_text(out)
        for ln in out.splitlines():
            c = ln.split(",")
            if len(c) >= 8 and c[4] == "15min":
                m[c[2]] = (c[3], c[5], int(datetime.fromisoformat(c[6]).timestamp()), c[7])
    return m


def cargar(d):
    tok = tokens(d)
    with gzip.open(VOL / "m15_onchain" / f"m15_onchain_{d}.csv.gz", "rt") as fh:
        x = pd.read_csv(fh, dtype={"token_id": str, "maker": str, "taker": str, "tx": str},
                        usecols=["tipo", "ts_est", "tx", "log_index", "maker", "taker", "side", "token_id", "maker_amt",
                                 "taker_amt", "fee"])
    x = x[(x.tipo == "F") & x.token_id.isin(tok.keys())].copy()
    info = x.token_id.map(tok)
    x["act"], x["mkt"], x["fin"], x["lado"] = info.str[0], info.str[1], info.str[2], info.str[3]
    x["dia"] = d
    x["es_tom"] = x.taker == EXCH
    x["maker"] = x.maker.str[:10]
    x = x.drop(columns=["tipo", "taker"])
    for c in ("tx", "token_id", "act", "mkt", "lado", "dia", "maker"):
        x[c] = x[c].astype("category")
    return x


def main():
    X = pd.concat([cargar(d) for d in DIAS], ignore_index=True)
    for c in ("tx", "token_id", "act", "mkt", "lado", "dia", "maker"):
        X[c] = X[c].astype(str).astype("category")
    des = desenlaces(set(X.mkt.astype(str)))
    X["des"] = X.mkt.map(des)
    cob = X.drop_duplicates("mkt").des.notna().groupby(X.drop_duplicates("mkt").dia).mean()
    X = X[X.des.notna()].copy()
    buy = X.side == 0
    X["acc"] = np.where(buy, X.taker_amt, X.maker_amt).astype(float)
    X["usdc"] = np.where(buy, X.maker_amt, X.taker_amt).astype(float)
    X = X[X.acc > 0].copy()
    X["p"] = (X.usdc / X.acc).round(4)
    X["buy"] = (X.side == 0)
    win = (X.lado == X.des).astype(float)
    X["rol"] = np.where(X.es_tom, "tomador", "maker")
    X["wallet"] = X.maker
    X["fee"] = X.fee.astype(float).fillna(0)
    X["pnl"] = np.where(X.buy, X.acc * win - X.usdc, X.usdc - X.acc * win) - np.where(X.rol == "tomador", X.fee, 0.0)
    mk = X.rol == "maker"
    fee_tx = X[~mk].groupby("tx").fee.sum()
    acc_tx = X[mk].groupby("tx").acc.sum()
    X["rebate"] = 0.0
    X.loc[mk, "rebate"] = 0.2 * X.loc[mk, "tx"].map(fee_tx).fillna(0).values * X.loc[mk, "acc"].values / X.loc[mk, "tx"].map(acc_tx).values
    lin = []

    def L(s=""):
        print(s, flush=True)
        lin.append(s)

    L(f"Rellenos 15m on-chain {DIAS[0]}..{DIAS[-1]}: {len(X)} filas, {X.mkt.nunique()} mercados; cobertura desenlace por día: "
      + ", ".join(f"{k[5:]} {v:.1%}" for k, v in cob.items()))
    L("\n1) RECONCILIACIÓN por día (USDC): PnL maker + PnL tomador debe = −comisión tomadora")
    g = X.groupby(["dia", "rol"]).agg(vol=("usdc", "sum"), pnl=("pnl", "sum"), fee=("fee", "sum"), rebate=("rebate", "sum")).unstack()
    r = pd.DataFrame({"vol_tom": g[("vol", "tomador")], "pnl_maker": g[("pnl", "maker")], "pnl_tom": g[("pnl", "tomador")],
                      "fee_tom": g[("fee", "tomador")], "rebate_est": g[("rebate", "maker")]})
    r["cuadre"] = r.pnl_maker + r.pnl_tom + r.fee_tom
    r["bruto_tom"] = r.pnl_tom + r.fee_tom
    L(r.round(0).to_string())
    L("   lectura: bruto_tom = lo que los tomadores ganan a los makers ANTES de comisión (= −pnl_maker).")

    # ---- por (wallet, mercado) de los makers
    M = X[mk]
    M = M.assign(by=np.where(M.buy & (M.lado == "YES"), M.acc, 0.0), cy=np.where(M.buy & (M.lado == "YES"), M.usdc, 0.0),
                 bn=np.where(M.buy & (M.lado == "NO"), M.acc, 0.0), cn=np.where(M.buy & (M.lado == "NO"), M.usdc, 0.0),
                 sv=np.where(~M.buy, M.usdc, 0.0))
    WM = M.groupby(["wallet", "mkt", "dia", "act"]).agg(by=("by", "sum"), cy=("cy", "sum"), bn=("bn", "sum"), cn=("cn", "sum"),
                                                        sv=("sv", "sum"), vol=("usdc", "sum"), pnl=("pnl", "sum"),
                                                        rebate=("rebate", "sum"), n=("pnl", "size")).reset_index()
    WM["emp"] = np.minimum(WM.by, WM.bn)
    WM["pares_frac"] = np.where(WM.by + WM.bn > 0, 2 * WM.emp / (WM.by + WM.bn), 0)
    WM["coste_par"] = np.where(WM.emp > 0, WM.cy / WM.by.replace(0, np.nan) + WM.cn / WM.bn.replace(0, np.nan), np.nan)
    WM["margen_pares"] = WM.emp * (1 - WM.coste_par.fillna(1))
    WM["resto"] = WM.pnl - WM.margen_pares
    d = WM[WM.dia.isin(DESC)].groupby("wallet").agg(vol=("vol", "sum"), by=("by", "sum"), bn=("bn", "sum"), emp=("emp", "sum"), sv=("sv", "sum"))
    d["frac"] = 2 * d.emp / (d.by + d.bn)
    cos = sorted(d[(d.vol >= 2000) & (d.frac >= 0.8) & (d.sv < 0.05 * d.vol)].index)
    L(f"\n2) COSECHADORES elegidos con 05-07 (≥80 % emparejado, vol ≥2.000, ventas <5 %): {len(cos)} wallets")

    def bloque(sub, nombre):
        s = sub
        if len(s) == 0:
            return
        dias = s.groupby("dia").agg(pnl=("pnl", "sum"), reb=("rebate", "sum"))
        cp = (s.coste_par * s.emp).sum() / s.emp.sum() if s.emp.sum() else np.nan
        L(f"   {nombre:28s} merc {s.mkt.nunique():5d} vol {s.vol.sum():9.0f} PnL {s.pnl.sum():+8.0f} (pares {s.margen_pares.sum():+8.0f}, "
          f"residual {s.resto.sum():+8.0f}) reemb.est {s.rebate.sum():+6.0f} | coste/par {cp:.4f} | emparejado {2 * s.emp.sum() / (s.by.sum() + s.bn.sum()):.0%}"
          f" | PnL/día {dias.pnl.mean():+7.0f} (+reemb {(dias.pnl + dias.reb).mean():+7.0f}) días+ {(dias.pnl > 0).sum()}/{len(dias)} "
          f"(+reemb {((dias.pnl + dias.reb) > 0).sum()})")

    for per, ds in (("DESC 05-07", DESC), ("FORWARD 08-12", DIAS[3:])):
        L(f"\n  [{per}]")
        sub = WM[WM.dia.isin(ds)]
        bloque(sub[sub.wallet.isin(cos)], "grupo cosechadores")
        for w in FOCO:
            bloque(sub[sub.wallet == w], w)
            for a in ("BTC", "SOL", "ETH", "XRP"):
                bloque(sub[(sub.wallet == w) & (sub.act == a)], f"   {w} {a}")
    L("\n  cosechadores por wallet (FORWARD 08-12): PnL, reembolso, coste/par")
    f = WM[WM.dia.isin(DIAS[3:]) & WM.wallet.isin(cos)].groupby("wallet").agg(vol=("vol", "sum"), pnl=("pnl", "sum"), reb=("rebate", "sum"),
                                                                             emp=("emp", "sum"), cpe=("coste_par", lambda s: 0))
    for w in cos:
        s = WM[WM.dia.isin(DIAS[3:]) & (WM.wallet == w)]
        if len(s) == 0:
            L(f"   {w} sin actividad 08-12")
            continue
        cp = (s.coste_par * s.emp).sum() / s.emp.sum() if s.emp.sum() else np.nan
        L(f"   {w} vol {s.vol.sum():9.0f} PnL {s.pnl.sum():+7.0f} reemb {s.rebate.sum():+6.0f} pares {s.margen_pares.sum():+7.0f} residual {s.resto.sum():+7.0f} coste/par {cp:.4f}")

    # ---- cola observada
    L("\n4) COLA OBSERVADA (orden de relleno dentro de cada nivel de precio de una tx; rango 1 = primero en prioridad)")
    Mk = X[mk & X.buy].sort_values(["tx", "log_index"])
    Mk["k"] = Mk.groupby(["tx", "token_id", "p"]).wallet.transform("size")
    Mk["rango"] = Mk.groupby(["tx", "token_id", "p"]).cumcount() + 1
    pmax = Mk.groupby(["tx", "token_id"]).p.transform("max")
    Mk["nivel1"] = Mk.p == pmax
    Mk["ultimo"] = Mk.rango == Mk.k
    multi = Mk[Mk.k >= 2]

    def cola(s, nombre):
        if len(s) < 30:
            L(f"   {nombre:24s} n={len(s)} (insuficiente)")
            return
        L(f"   {nombre:24s} n={len(s):7d} P(rango1)={(s.rango == 1).mean():.3f} vs azar E[1/k]={(1 / s.k).mean():.3f} | "
          f"rango medio/k {(s.rango / s.k).mean():.3f} | último del nivel {s.ultimo.mean():.3f} | k medio {s.k.mean():.1f}")

    for per, ds in (("DESC 05-07", DESC), ("FORWARD 08-12", DIAS[3:])):
        L(f"  [{per}] niveles con ≥2 makers")
        s = multi[multi.dia.isin(ds)]
        cola(s, "todos los makers")
        cola(s[s.wallet.isin(cos)], "cosechadores")
        cola(s[~s.wallet.isin(cos)], "resto makers")
        for w in FOCO:
            cola(s[s.wallet == w], w)
    L("\n  ¿relleno en el PRIMER nivel de la tx (= en el mejor bid en ese instante)? y PnL por acción según rango (todos los días)")
    for nombre, s in (("cosechadores", Mk[Mk.wallet.isin(cos)]), ("resto", Mk[~Mk.wallet.isin(cos)]), ("0xcfddfb6e", Mk[Mk.wallet == "0xcfddfb6e"])):
        L(f"   {nombre:14s} nivel1 {s.nivel1.mean():.3f} | PnL/acc: nivel1 {s[s.nivel1].pnl.sum() / s[s.nivel1].acc.sum():+.4f} "
          f"más profundo {s[~s.nivel1].pnl.sum() / max(s[~s.nivel1].acc.sum(), 1e-9):+.4f}")
        ss = s[s.k >= 2]
        if len(ss) > 30:
            L(f"   {'':14s} en niveles compartidos: PnL/acc rango1 {ss[ss.rango == 1].pnl.sum() / ss[ss.rango == 1].acc.sum():+.4f} "
              f"| detrás {ss[ss.rango > 1].pnl.sum() / ss[ss.rango > 1].acc.sum():+.4f} | último {ss[ss.ultimo].pnl.sum() / ss[ss.ultimo].acc.sum():+.4f}")
    L("\n  PnL por acción de los makers según rango y k (todos los makers, compras, todos los días): selección adversa por posición")
    t = multi.assign(pos=np.where(multi.rango == 1, "1º", np.where(multi.ultimo, "último", "medio"))).groupby(
        [np.minimum(multi.k, 5), "pos"]).agg(n=("pnl", "size"), acc=("acc", "sum"), pnl=("pnl", "sum"))
    t["pnl_acc"] = t.pnl / t.acc
    L(t.round(4).to_string())
    INF.write_text("\n".join(lin) + "\n")
    L(f"\n→ {INF}")


if __name__ == "__main__":
    main()
