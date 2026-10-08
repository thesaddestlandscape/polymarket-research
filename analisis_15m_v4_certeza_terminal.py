#!/usr/bin/env python3
"""analisis_15m_v4_certeza_terminal.py -- MISIÓN 15M v4, vías TOMADOR e HÍBRIDO (08-Oct): la "certeza terminal".
Wallets persistentes (PnL > 0 los 3 días 05-07 Oct, analisis_15m_v4_tres_vias.py) que compran el lado líder a
0,87-0,99 en los últimos minutos: 0x9c8f91bc (tomador, p~0,96, T~184 s, 206/206 mercados > 0), 0x44832d0d (híbrido,
p~0,87, T~44 s), grupo 0,99 (0x48ac40fc, 0xee65685d, 0x2277c18f, 0xaad03b40, 0x6fc44ec4, 0xc5b9ca6c).
Pregunta: ¿qué ESTADO del contrato distingue sus compras de las del resto al MISMO precio y fase?
Cada compra (on-chain, rol tomador o maker, side BUY) con p >= P_MIN y T <= T_MAX se cruza con el estado TWAP en
t = bloque - 2,06 s (desfase bloque-exchange medido en V3) con ticks Chainlink RECIBIDOS <= t
(analisis_15m_v4_twap_terminal_mes.estado_twap: z_TWAP con la ventana [e-62, e-3], z_spot, σ 300 s).
Salida: P(gana) por z_TWAP del lado comprado × banda de precio × T para TODOS los compradores (superficie a precio
REAL negociado) y, aparte, distribución de z de las persistentes vs el resto. Solo EXTRACCIÓN (05-06); 07 se reporta
aparte como primer contraste.
Uso: nice -n 19 python3 analisis_15m_v4_certeza_terminal.py
"""
import collections
import sys
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_b1_compradores_mes import refs_dia, twap_rtds  # noqa: E402
from analisis_15m_v4_twap_terminal_mes import estado_twap, ticks_dia, fee  # noqa: E402

DL = Path("/root/polymarket-research-datalogs")
P_MIN, T_MAX, DESFASE_S = 0.80, 300, 2.06
PERSIST = {"0x9c8f91bc", "0x44832d0d", "0x48ac40fc", "0xee65685d", "0x2277c18f", "0xaad03b40", "0x6fc44ec4", "0xc5b9ca6c"}
INF = Path(__file__).resolve().parent / "informes" / "m15v4_certeza_terminal_08oct.txt"


def main():
    X = pd.read_parquet(DL / "m15_ms_cache" / "v4_quien_gana.parquet",
                        columns=["wallet", "rol", "side", "dia", "act", "mkt", "fin", "lado", "ts_est", "acc", "usdc", "p", "T", "pnl", "des"])
    X = X[(X.side == 0) & (X.p >= P_MIN) & (X.p < 0.995) & (X["T"] <= T_MAX) & (X["T"] > 3)].copy()
    dias = sorted(X.dia.unique())
    PB, RT = {}, collections.defaultdict(lambda: [0.0, 0])
    for d in [(date.fromisoformat(dias[0]) - timedelta(days=1)).isoformat()] + dias:
        refs_dia(d, PB, RT)
    filas = []
    for d in dias:
        tk = ticks_dia(d)
        for r in X[X.dia == d].itertuples(index=False):
            if r.act not in tk:
                continue
            fin = int(r.fin)
            ref = PB.get((r.act, fin - 900)) or twap_rtds(RT, r.act, fin - 900)
            if ref is None:
                continue
            rv, ws, px = tk[r.act]
            e = estado_twap(rv, ws, px, fin, int((r.ts_est - DESFASE_S) * 1000), ref)
            if e is None:
                continue
            s = 1 if r.lado == "YES" else -1
            filas.append({"dia": d, "w": r.wallet[:10], "rol": r.rol, "act": r.act, "mkt": r.mkt, "p": r.p, "T": r.T,
                          "acc": r.acc, "win": int(r.lado == r.des), "z_tw": s * e[1], "z_sp": s * e[2],
                          "lead_bps": s * e[0] * 1e4})
        del tk
    F = pd.DataFrame(filas)
    F["pers"] = F.w.isin(PERSIST)
    F["pnl_acc"] = F.win - F.p - np.where(F.rol == "tomador", fee(F.p), 0.0)
    F.to_parquet(DL / "m15_ms_cache" / "v4_certeza_terminal.parquet")
    lin = []

    def L(s=""):
        print(s, flush=True)
        lin.append(s)
    L(f"Certeza terminal — compras p∈[{P_MIN},0,995) T∈(3,{T_MAX}] s con estado TWAP: {len(F)} rellenos, {F.mkt.nunique()} mercados, días {dias}")
    for tramo, G in (("EXTRACCIÓN 05-06", F[F.dia <= "2026-10-06"]), ("CONTRASTE 07", F[F.dia == "2026-10-07"])):
        L(f"\n===== {tramo}: {len(G)} rellenos =====")
        for nom, q in (("persistentes", G[G.pers]), ("resto", G[~G.pers])):
            if len(q) == 0:
                continue
            L(f"  {nom}: n={len(q)} merc={q.mkt.nunique()} acierto={np.average(q.win, weights=q.acc):.4f} p_med={np.average(q.p, weights=q.acc):.3f} "
              f"PnL/acc={np.average(q.pnl_acc, weights=q.acc):+.4f} | z_TWAP P10/P50/P90 {q.z_tw.quantile(.1):.2f}/{q.z_tw.median():.2f}/{q.z_tw.quantile(.9):.2f} "
              f"| z_spot P50 {q.z_sp.median():.2f} | lead P50 {q.lead_bps.median():.1f} bps | T P50 {q['T'].median():.0f}")
        L("  SUPERFICIE a precio negociado (todos): z_TWAP del lado comprado × banda de precio -> acierto vs precio (ponderado por acciones), PnL/acc")
        G = G.assign(zb=pd.cut(G.z_tw, [-1e9, 0, 1, 2, 3, 4, 6, 1e9]), pb=pd.cut(G.p, [0.80, 0.90, 0.95, 0.97, 0.99, 0.995]))
        for (zb, pb), q in G.groupby(["zb", "pb"], observed=True):
            if q.mkt.nunique() < 15:
                continue
            L(f"    z {str(zb):>12s} p {str(pb):>13s}: n={len(q):5d} merc={q.mkt.nunique():4d} acierto={np.average(q.win, weights=q.acc):.4f} "
              f"precio={np.average(q.p, weights=q.acc):.4f} PnL/acc={np.average(q.pnl_acc, weights=q.acc):+.4f}")
    INF.write_text("\n".join(lin) + "\n")


if __name__ == "__main__":
    main()
