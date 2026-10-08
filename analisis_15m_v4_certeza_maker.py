#!/usr/bin/env python3
"""analisis_15m_v4_certeza_maker.py -- MISIÓN 15M v4, vía 2 (08-Oct, orden de Javi 3 -> 2 -> 1): CERTEZA TERMINAL
COMO MAKER. Lo que hace el grupo "0,99" persistente (0x48ac40fc, 0xee65685d, 0x2277c18f, 0xaad03b40, 0x6fc44ec4: maker a
~0,99 en T 13-57 s, 82-100 % de mercados > 0). Como tomador quedó refutada (mes 18-Sep..04-Oct EV +0,04c, IC cruza 0).

Regla CONGELADA 08-Oct antes de correr:
  - De T=60 s a T=5 s, cada 1 s (reloj de recepción): estado TWAP del líder con ticks Chainlink RECIBIDOS <= t
    (estado_twap, ventana [e-62, e-3]). Si z_TWAP(líder) >= 3, mantener UNA puja de TAM acciones a precio B en el token
    del líder (solo maker puro: si el ask visto ya es <= B, no se puja). Si z < 3 o T < 5 s, se cancela.
  - Variantes declaradas: B = 0,98 y 0,99.
  - Relleno = modelo de cola de analisis_15m_v4_cosechador_pares.simular_v3: cola delante = tamaño visible si B es el
    mejor bid al entrar; si B MEJORA el mejor bid, cola 0 (somos el nuevo mejor bid); si B < mejor bid, solo
    atravesando. Consumen la cola: tomador VENDE el líder a <= B, o tomador COMPRA el contrario a >= 1 - B (acuñación).
    Alta/cancelación efectivas +100 ms. Una orden viva conserva su cola mientras siga deseada.
  - PnL por acción = gana - B (maker: sin comisión); reembolso del maker ESTIMADO aparte (20 % de 0,07·B·(1-B)).
Fidelidad: rellenos maker del grupo 0,99 en el mismo tramo (p >= 0,975, T <= 60) -> acierto y volumen por mercado.
Uso: (ulimit -v 4500000; nice -n 19 python3 analisis_15m_v4_certeza_maker.py --cache DIR [--activos BTC])
"""
import argparse
import collections
import os
import sys
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_b1_compradores_mes import refs_dia, twap_rtds  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from analisis_15m_v4_twap_terminal_mes import estado_twap, ticks_dia  # noqa: E402

TAM, Z_MIN, T_INI, T_FIN, PASO_MS, LAT_MS = 10.0, 3.0, 60, 5, 1000, 100
PRECIOS = (0.98, 0.99)


def simular(qL, tL, tC, fin_ms, tk, ref, gana_lider_fn, B):
    """qL: vistas del libro de cada lado {'Y': {...}, 'N': {...}} (tr, bb_tr, ba_tr, te, bb_te, bs_te).
    tL: operaciones por lado {'Y': (te,p,side,sz), 'N': ...}. Devuelve (acciones, lado, n_rellenos)."""
    rv, ws, px = tk
    orden = None                                   # dict(lado, rest, cola, ultimo_te)
    lleno = {"Y": 0.0, "N": 0.0}
    nrell = 0

    def avanzar(o, hasta):
        nonlocal nrell
        mismo, contra = (tL["Y"], tL["N"]) if o["lado"] == "Y" else (tL["N"], tL["Y"])
        ev = []
        te, pp, sd, sz = mismo
        for k in range(np.searchsorted(te, o["ultimo_te"], side="right"), np.searchsorted(te, hasta, side="right")):
            if sd[k] == 0:
                ev.append((te[k], float(pp[k]), float(sz[k])))
        te, pp, sd, sz = contra
        for k in range(np.searchsorted(te, o["ultimo_te"], side="right"), np.searchsorted(te, hasta, side="right")):
            if sd[k] == 1:
                ev.append((te[k], round(1 - float(pp[k]), 4), float(sz[k])))
        ev.sort()
        for _, p, q in ev:
            if o["rest"] <= 0:
                break
            if p < B - 1e-9:
                f = o["rest"]
            elif abs(p - B) < 1e-9 and o["cola"] is not None:
                o["cola"] -= q
                f = min(o["rest"], -o["cola"]) if o["cola"] < 0 else 0.0
                if o["cola"] < 0:
                    o["cola"] = 0.0
            else:
                f = 0.0
            if f > 0:
                o["rest"] -= f
                lleno[o["lado"]] += f
                nrell += 1
        o["ultimo_te"] = hasta

    for ts in range(fin_ms - T_INI * 1000, fin_ms - T_FIN * 1000, PASO_MS):
        efec = ts + LAT_MS
        if orden is not None:
            avanzar(orden, efec)
        e = estado_twap(rv, ws, px, fin_ms // 1000, ts, ref)
        lado = None
        if e is not None and abs(e[1]) >= Z_MIN:
            lado = "Y" if e[1] > 0 else "N"
        deseo = None
        if lado is not None:
            L = qL[lado]
            j = np.searchsorted(L["tr"], ts, side="right") - 1
            if j >= 0 and L["ba_tr"][j] == L["ba_tr"][j] and L["ba_tr"][j] > B + 1e-9:   # maker puro
                deseo = lado
        if orden is not None and (deseo != orden["lado"] or orden["rest"] <= 0):
            orden = None                               # cancelación efectiva en efec (ya liquidado hasta efec)
        if deseo is not None and orden is None and lleno[deseo] < TAM:
            L = qL[deseo]
            j = np.searchsorted(L["te"], efec, side="right") - 1
            bb = float(L["bb_te"][j]) if j >= 0 else np.nan
            if bb != bb or B > bb + 1e-9:
                cola = 0.0                             # mejoramos el bid: primeros
            elif abs(B - bb) < 1e-9:
                cola = float(L["bs_te"][j])
            else:
                cola = None                            # por debajo del mejor bid: solo atravesando
            orden = {"lado": deseo, "rest": TAM - lleno[deseo], "cola": cola, "ultimo_te": efec}
    if orden is not None:
        avanzar(orden, fin_ms - T_FIN * 1000 + LAT_MS)
    return lleno, nrell


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", default="/root/polymarket-research-datalogs/m15_ms_cache")
    ap.add_argument("--activos", default="")
    ap.add_argument("--salida", default="informes/m15v4_certeza_maker_08oct.txt")
    a = ap.parse_args()
    os.environ["M15_CACHE_DIR"] = a.cache
    from m15_ms_cache import cargar
    C = cargar()
    q, T = C["q"], C["t"]
    toks = C["tokens"]
    bq = np.searchsorted(q["tok"], np.arange(len(toks) + 1))
    o = np.lexsort((T["te"], T["tok"]))
    T = {k: v[o] for k, v in T.items()}
    bt = np.searchsorted(T["tok"], np.arange(len(toks) + 1))
    merc = {}
    for i, (tk_, act, mid, fin, lado) in enumerate(toks):
        merc.setdefault(str(mid), {"act": act, "fin": int(fin)})[lado] = i
    des = desenlaces(set(merc))
    dias = sorted({pd.Timestamp(m["fin"], unit="s").strftime("%Y-%m-%d") for m in merc.values()})
    PB, RT = {}, collections.defaultdict(lambda: [0.0, 0])
    for d in [(date.fromisoformat(dias[0]) - timedelta(days=1)).isoformat()] + dias:
        refs_dia(d, PB, RT)

    def vistas(c0, c1):
        otr = np.argsort(q["tr"][c0:c1], kind="stable")
        ote = np.argsort(q["te"][c0:c1], kind="stable")
        return {"tr": q["tr"][c0:c1][otr], "bb_tr": q["bb"][c0:c1][otr].astype(float), "ba_tr": q["ba"][c0:c1][otr].astype(float),
                "te": q["te"][c0:c1][ote], "bb_te": q["bb"][c0:c1][ote].astype(float), "bs_te": q["bs"][c0:c1][ote].astype(float)}
    filas = []
    for d in dias:
        tkd = ticks_dia(d)
        for mid, m in merc.items():
            dia_m = pd.Timestamp(m["fin"], unit="s").strftime("%Y-%m-%d")
            if dia_m != d or "YES" not in m or "NO" not in m or mid not in des or m["act"] not in tkd:
                continue
            if a.activos and m["act"] not in a.activos.split(","):
                continue
            iy, inn = m["YES"], m["NO"]
            if bq[iy + 1] - bq[iy] < 50 or bq[inn + 1] - bq[inn] < 50:
                continue
            fin_ms = m["fin"] * 1000
            ref = PB.get((m["act"], m["fin"] - 900)) or twap_rtds(RT, m["act"], m["fin"] - 900)
            if ref is None:
                continue
            rv, ws, px = tkd[m["act"]]
            k0, k1 = np.searchsorted(rv, fin_ms - 420_000), np.searchsorted(rv, fin_ms)
            tk = (rv[k0:k1], ws[k0:k1], px[k0:k1])
            if len(tk[0]) < 60:
                continue
            qL = {"Y": vistas(bq[iy], bq[iy + 1]), "N": vistas(bq[inn], bq[inn + 1])}
            tL = {"Y": tuple(T[k][bt[iy]:bt[iy + 1]] for k in ("te", "p", "side", "sz")),
                  "N": tuple(T[k][bt[inn]:bt[inn + 1]] for k in ("te", "p", "side", "sz"))}
            for B in PRECIOS:
                lleno, nr = simular(qL, tL, None, fin_ms, tk, ref, None, B)
                for lado, acc in lleno.items():
                    if acc > 0:
                        win = 1.0 if (des[mid] == ("YES" if lado == "Y" else "NO")) else 0.0
                        filas.append({"dia": d, "act": m["act"], "mkt": mid, "B": B, "acc": acc, "win": win,
                                      "pnl": acc * (win - B), "reb": 0.2 * 0.07 * B * (1 - B) * acc, "nrell": nr})
                filas.append({"dia": d, "act": m["act"], "mkt": mid, "B": B, "acc": 0.0, "win": np.nan, "pnl": 0.0, "reb": 0.0,
                              "nrell": 0, "_merc": 1})
        del tkd
    R = pd.DataFrame(filas)
    lin = []

    def L(s=""):
        print(s, flush=True)
        lin.append(s)
    nm = R[R.get("_merc") == 1].groupby("B").mkt.nunique()
    L(f"Certeza terminal MAKER — cache {a.cache}, días {dias}, activos {a.activos or 'todos'}; z_TWAP>={Z_MIN}, T {T_INI}->{T_FIN} s, TAM {TAM}")
    for B, g in R[R.acc > 0].groupby("B"):
        dm = g.groupby("dia").pnl.sum()
        L(f"\n== B={B}: mercados evaluados {nm.get(B, 0)}, con relleno {g.mkt.nunique()} ({g.mkt.nunique() / max(1, nm.get(B, 1)):.0%}); "
          f"acciones {g.acc.sum():.0f}; acierto {np.average(g.win, weights=g.acc):.4f}; fallos {int((g.win == 0).sum())}; "
          f"PnL/acc {g.pnl.sum() / g.acc.sum():+.4f}; PnL total {g.pnl.sum():+.2f} $ (+ reembolso est. {g.reb.sum():.2f}); "
          f"por día " + ", ".join(f"{k} {v:+.2f}" for k, v in dm.items()))
        for act, h in g.groupby("act"):
            L(f"   {act}: merc {h.mkt.nunique()} acierto {np.average(h.win, weights=h.acc):.4f} PnL/acc {h.pnl.sum() / h.acc.sum():+.4f}")
    Path(a.salida).write_text("\n".join(lin) + "\n")
    R.to_parquet(Path(a.cache) / "v4_certeza_maker.parquet")


if __name__ == "__main__":
    main()
