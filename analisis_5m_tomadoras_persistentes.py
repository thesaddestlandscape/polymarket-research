#!/usr/bin/env python3
"""analisis_5m_tomadoras_persistentes.py -- MISIÓN (Javi 14-Oct): descifrar a las TOMADORAS persistentes que ganan en los
5m que cierran con un 15m (456 ganadoras / 326 tomadoras / +153,6 k$ en 8 días). SOLO LECTURA sobre las cachés on-chain de
analisis_5m_barato_quien_gana.py (quien_gana_fills_D.csv.gz). Paso 1 (qué compran) + paso 3 (¿persiste fuera de muestra?).

DISEÑO ANTI-TRAMPA (universo fijo / selección por resultado):
  SELECCIÓN con días DESC (por defecto 06-09 Oct): tomadora = >= 50 % de su volumen 5m como tomadora, >= 3 días activos,
  volumen 5m tomador >= 200 $; GANADORA = PnL tomador > 0 en >= 75 % de sus días activos y total > 0; PERDEDORA = PnL
  tomador < 0 en >= 75 % de sus días; RESTO = las demás tomadoras.
  VALIDACIÓN con días OOS (10-13 Oct) que no intervienen en la selección: EV/€ de las compras tomadoras de cada grupo
  (unidad = wallet-mercado-lado: suma pnl / suma coste), IC90 por días, % de wallets que siguen positivas.
QUÉ COMPRAN (en DESC y OOS, por grupo; compras TOMADORAS del 5m): lado comprado = favorito (precio >= 0,5) o barato,
  tramo de precio, segundos al cierre (T), tamaño (acciones), moneda, compras por mercado, % de mercados en los que compran
  los dos lados, y EV/€ de cada celda para ganadoras vs resto (¿dónde está la diferencia?).
Uso: nice -n 19 python3 analisis_5m_tomadoras_persistentes.py [--desc 2026-10-06,2026-10-09] [--oos 2026-10-10,2026-10-13]
Salida: datalogs/m5barato_mision/tomadoras_grupos.csv, tomadoras_informe.txt
"""
import argparse
import glob
import random
from pathlib import Path

import numpy as np
import pandas as pd

D = Path("/root/polymarket-research-datalogs/m5barato_mision")
RNG = random.Random(7)
VOL_TOTAL = {}


def cargar(d0, d1):
    """Solo filas TOMADORAS del 5m (memoria); el volumen total por wallet (maker+tomador) se agrega aparte."""
    partes, vol = [], []
    for f in sorted(glob.glob(str(D / "quien_gana_fills_2026-10-*.csv.gz"))):
        dia = Path(f).name[17:27]
        if not (d0 <= dia <= d1):
            continue
        for x in pd.read_csv(f, chunksize=400_000, usecols=["marco", "wallet", "rol", "act", "mkt", "cierre", "lado", "compra",
                                                             "acc", "usdc", "fee", "T", "pnl"]):
            x = x[x.marco == "5m"]
            vol.append(x.groupby("wallet").usdc.sum())
            x = x[x.rol == "T"].drop(columns=["marco", "rol"])
            partes.append(x.assign(dia=dia, coste=np.where(x.compra, x.usdc, x.acc - x.usdc) + x.fee, rol="T"))
    X = pd.concat(partes, ignore_index=True)
    VOL_TOTAL[d0] = pd.concat(vol).groupby(level=0).sum()
    return X


def grupos(X):
    t = X
    v_all = VOL_TOTAL[X.dia.min()]
    v_t = t.groupby("wallet").usdc.sum()
    pd_ = t.groupby(["wallet", "dia"]).pnl.sum()
    act = pd_.groupby("wallet").size()
    pos = pd_.gt(0).groupby("wallet").mean()
    neg = pd_.lt(0).groupby("wallet").mean()
    tot = pd_.groupby("wallet").sum()
    W = pd.DataFrame({"vol": v_all, "vol_t": v_t, "dias": act, "f_pos": pos, "f_neg": neg, "pnl_t": tot}).dropna()
    W = W[(W.vol_t >= 0.5 * W.vol) & (W.dias >= 3) & (W.vol_t >= 200)]
    W["grupo"] = np.where((W.f_pos >= 0.75) & (W.pnl_t > 0), "GANADORA", np.where(W.f_neg >= 0.75, "PERDEDORA", "RESTO"))
    return W


def ev_unidades(T):
    """EV/€ con unidad wallet-mercado-lado."""
    u = T.groupby(["wallet", "mkt", "lado"]).agg(pnl=("pnl", "sum"), coste=("coste", "sum"))
    return u.pnl.sum() / u.coste.sum() if u.coste.sum() > 0 else float("nan"), len(u)


def ic_dias(T, n=2000):
    pdd = T.groupby("dia").agg(p=("pnl", "sum"), c=("coste", "sum"))
    ks = list(pdd.index)
    if len(ks) < 3:
        return None
    m = sorted(pdd.loc[[RNG.choice(ks) for _ in ks]].p.sum() / pdd.loc[[RNG.choice(ks) for _ in ks]].c.sum() for _ in range(n))
    return (round(m[int(.05 * n)], 3), round(m[int(.95 * n)], 3))


def perfil(T, nom):
    C = T[T.compra]
    p = C.usdc / C.acc
    fav = p >= 0.5
    L = [f"  {nom}: compras {len(C)} en {C.mkt.nunique()} mercados | favorito (p>=0,5) {fav.mean():.0%} | precio P10/50/90 "
         f"{np.percentile(p, [10, 50, 90]).round(2).tolist()} | T P10/50/90 {np.percentile(C['T'], [10, 50, 90]).round(0).tolist()} s | "
         f"acc P50 {C.acc.median():.1f} | BTC {(C.act == 'BTC').mean():.0%} | ventas {(~T.compra).mean():.0%} | "
         f"merc. con ambos lados {(C.groupby(['wallet', 'mkt']).lado.nunique() > 1).mean():.0%}"]
    return L


def celdas(Tg, Tr, nom):
    """EV/€ por celda (precio x T) para ganadoras vs resto: dónde está la diferencia."""
    L = [f"  EV/€ por celda {nom} (GANADORAS | RESTO, n compras):"]
    for (plo, phi) in ((0, .2), (.2, .4), (.4, .6), (.6, .8), (.8, 1.01)):
        fila = []
        for (tlo, thi) in ((0, 30), (30, 90), (90, 180), (180, 300), (300, 1e9)):
            def ev(T):
                c = T[T.compra]
                pr = c.usdc / c.acc
                s = c[(pr >= plo) & (pr < phi) & (c["T"] >= tlo) & (c["T"] < thi)]
                return (s.pnl.sum() / s.coste.sum() if s.coste.sum() > 0 else float("nan"), len(s))
            g, r = ev(Tg), ev(Tr)
            fila.append(f"T{int(tlo)}-{int(thi) if thi < 1e9 else '∞'}: {g[0]:+.2f}|{r[0]:+.2f} ({g[1]}|{r[1]})")
        L.append(f"    p[{plo:.1f},{min(phi, 1):.1f}) " + "  ".join(fila))
    return L


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desc", default="2026-10-06,2026-10-09")
    ap.add_argument("--oos", default="2026-10-10,2026-10-13")
    a = ap.parse_args()
    d0, d1 = a.desc.split(",")
    o0, o1 = a.oos.split(",")
    XD = cargar(d0, d1)
    W = grupos(XD)
    W.to_csv(D / "tomadoras_grupos.csv")
    XO = cargar(o0, o1)
    L = [f"TOMADORAS PERSISTENTES 5m pares — selección DESC {d0}..{d1}, validación OOS {o0}..{o1}",
         f"tomadoras en DESC: {len(W)} | GANADORAS {int((W.grupo == 'GANADORA').sum())} | PERDEDORAS {int((W.grupo == 'PERDEDORA').sum())} | RESTO {int((W.grupo == 'RESTO').sum())}"]
    for per, X in (("DESC (in-sample)", XD), ("OOS", XO)):
        T = X[X.rol == "T"]
        L.append(f"\n== {per}")
        for g in ("GANADORA", "PERDEDORA", "RESTO"):
            ws = set(W.index[W.grupo == g])
            Tg = T[T.wallet.isin(ws)]
            if not len(Tg):
                continue
            e, n = ev_unidades(Tg)
            pw = Tg.groupby("wallet").pnl.sum()
            L.append(f"  {g:9s} wallets activas {Tg.wallet.nunique():4d} | unidades {n:6d} | PnL {Tg.pnl.sum():+10,.0f} $ | EV/€ {e:+.4f} "
                     f"IC90 días {ic_dias(Tg)} | wallets con PnL>0 {(pw > 0).mean():.0%} | sin top5 wallets {Tg.pnl.sum() - pw.nlargest(5).sum():+,.0f} $")
        TG = T[T.wallet.isin(set(W.index[W.grupo == "GANADORA"]))]
        TR = T[T.wallet.isin(set(W.index[W.grupo != "GANADORA"]))]
        L += perfil(TG, "GANADORAS") + perfil(TR, "RESTO+PERD.")
        L += celdas(TG, TR, per)
        # por moneda
        L.append("  EV/€ por moneda GANADORAS|RESTO: " + "  ".join(
            f"{m} {TG[TG.act == m].pnl.sum() / max(1e-9, TG[TG.act == m].coste.sum()):+.3f}|{TR[TR.act == m].pnl.sum() / max(1e-9, TR[TR.act == m].coste.sum()):+.3f}"
            for m in sorted(T.act.unique())))
    txt = "\n".join(L)
    print(txt)
    (D / "tomadoras_informe.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
