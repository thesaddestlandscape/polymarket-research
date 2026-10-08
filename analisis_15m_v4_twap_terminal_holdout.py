#!/usr/bin/env python3
"""analisis_15m_v4_twap_terminal_holdout.py -- regla R2 congelada (analisis_15m_v4_twap_terminal_mes.py) medida con
EJECUCIÓN REAL y PROFUNDIDAD (08-Oct):
  (a) dataset ms 06-07 Oct (m15_maestro_07oct.csv, fila por segundo): señal con el ask de t, compra al ask REAL a
      +215 ms (Y_ask*_215) si sigue <= 0,92; profundidad del nivel 1 a +215 ms (Y_ask*sz_215).
  (b) observador precierre_multioffset 15m (25-Sep..): su propio z_TWAP (v2 desde 02-Oct), ask del lado proyectado
      leído por WS con 60-100 ms y profundidad en €; offsets -90..-20, |z| >= 1, ask en [0,55, 0,92], 1ª por mercado.
R2: líder del TWAP proyectado, 20 <= T <= 90 s, |z_TWAP| >= 1, 0,55 <= ask <= 0,92. Comisión 0,07·p·(1-p).
Uso: nice -n 19 python3 analisis_15m_v4_twap_terminal_holdout.py
"""
import collections
import sys
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_b1_compradores_mes import refs_dia, twap_rtds  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from analisis_15m_v4_twap_terminal_mes import estado_twap, ticks_dia, fee  # noqa: E402

DL = Path("/root/polymarket-research-datalogs")


def resumen(u, px, titulo):
    if len(u) == 0:
        print(f"  {titulo}: sin señales")
        return
    pnl = u.win - u[px] - fee(u[px])
    eur = pnl / u[px]
    dm = eur.groupby(u.dia).mean()
    print(f"  {titulo}: n={len(u)} días={u.dia.nunique()} (+{int((dm > 0).sum())}) acierto={u.win.mean():.3f} "
          f"precio={u[px].mean():.3f} EV/acc={pnl.mean():+.4f} EV/€={eur.mean():+.4f} "
          f"top_mon={u.moneda.value_counts(normalize=True).iloc[0]:.0%}")


def parte_a():
    cols = ["dia", "moneda", "market", "cierre", "t", "desenlace", "t_hasta_cierre_s", "y_ask", "n_ask", "y_asz",
            "n_asz", "Y_askY_215", "Y_askN_215", "Y_askYsz_215", "Y_askNsz_215"]
    M = pd.read_csv(DL / "m15_maestro_07oct.csv", usecols=cols)
    M = M[(M.t_hasta_cierre_s >= 20) & (M.t_hasta_cierre_s <= 90)].sort_values("t")
    dias = sorted(M.dia.unique())
    PB, RT = {}, collections.defaultdict(lambda: [0.0, 0])
    for d in [(date.fromisoformat(dias[0]) - timedelta(days=1)).isoformat()] + dias:
        refs_dia(d, PB, RT)
    sen = []
    for d in dias:
        tk = ticks_dia(d)
        for mid, g in M[M.dia == d].groupby("market"):
            mo, fin = g.moneda.iloc[0], int(g.cierre.iloc[0])
            ref = PB.get((mo, fin - 900)) or twap_rtds(RT, mo, fin - 900)
            if ref is None or mo not in tk:
                continue
            rv, ws, px = tk[mo]
            for r in g.itertuples():
                e = estado_twap(rv, ws, px, fin, r.t, ref)
                if e is None:
                    continue
                z = e[1]
                lado = "YES" if z > 0 else "NO"
                ask = r.y_ask if lado == "YES" else r.n_ask
                if abs(z) >= 1 and ask == ask and 0.55 <= ask <= 0.92:
                    a215 = r.Y_askY_215 if lado == "YES" else r.Y_askN_215
                    sz = r.Y_askYsz_215 if lado == "YES" else r.Y_askNsz_215
                    sz0 = r.y_asz if lado == "YES" else r.n_asz
                    sen.append({"dia": d, "moneda": mo, "market": mid, "T": e[6], "z": abs(z), "ask": ask,
                                "ask215": a215, "sz215": sz, "sz0": sz0, "win": int(r.desenlace == lado)})
                    break
    S = pd.DataFrame(sen)
    print(f"(a) HOLDOUT ms 06-07 Oct: {len(S)} señales R2 de {M.market.nunique()} mercados")
    resumen(S, "ask", "al ask de la decisión (t)")
    F = S[S.ask215.notna() & (S.ask215 <= 0.92)]
    print(f"  rellenables a +215 ms (ask215 <= 0,92): {len(F)}/{len(S)}; ask215 - ask: media {(F.ask215 - F.ask).mean():+.4f}, "
          f"P50 {(F.ask215 - F.ask).median():+.4f}")
    resumen(F, "ask215", "al ask REAL a +215 ms")
    print(f"  profundidad nivel 1 a +215 ms (acciones): P25 {F.sz215.quantile(.25):.0f} P50 {F.sz215.median():.0f} "
          f"P75 {F.sz215.quantile(.75):.0f}; en € P50 {(F.sz215 * F.ask215).median():.1f}")
    return S


def parte_b():
    d = pd.read_csv(DL / "precierre_multioffset_fase0.csv", low_memory=False)
    d = d[(d.marco == "15m") & d.market_id.notna() & d.error.isna() & d.offset_s.between(-90, -20)].copy()
    d["market"] = d.market_id.astype(int).astype(str)
    des = desenlaces(set(d.market))
    d["des"] = d.market.map(des)
    d = d[d.des.notna()]
    d["zz"] = d.z_v2.where(d.z_v2.notna(), d.z).abs()
    d["dirx"] = d.direccion_v2.where(d.direccion_v2.notna(), d.direccion)
    d = d[(d.zz >= 1) & d.ask.between(0.55, 0.92)].sort_values("ts_utc")
    u = d.groupby("market", as_index=False).first()
    u["win"] = (((u.dirx == "Up") & (u.des == "YES")) | ((u.dirx == "Down") & (u.des == "NO"))).astype(int)
    u["dia"] = u.ts_utc.str[:10]
    u["moneda"] = u.activo
    print(f"\n(b) OBSERVADOR multi-offset 15m (libro WS 60-100 ms), {u.dia.nunique()} días")
    resumen(u, "ask", "R2 todo")
    for tr, q in (("25Sep-01Oct", u[u.dia <= "2026-10-01"]), ("02-07Oct", u[u.dia >= "2026-10-02"])):
        resumen(q, "ask", f"R2 {tr}")
    print(f"  profundidad € del lado comprado: P25 {u.profundidad_eur.quantile(.25):.1f} P50 {u.profundidad_eur.median():.1f} "
          f"P75 {u.profundidad_eur.quantile(.75):.1f}")
    return u


if __name__ == "__main__":
    parte_a()
    parte_b()
