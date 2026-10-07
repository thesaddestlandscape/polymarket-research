#!/usr/bin/env python3
"""analisis_15m_s10_cola.py -- MISIÓN DEFINITIVA 15m §10 (07-Oct): QUEUE POSITION ALPHA.
P(fill | cola, estado) y EV(fill | cola, estado) con el registro ms (m15_ms_cache: top del libro en cada cambio y TODAS
las operaciones con lado del tomador, reloj del exchange). Nunca se supone relleno porque el precio "toque".
ÓRDENES VIRTUALES (fijado antes de mirar): cada 5 s por token 15m, en [inicio+5 s, cierre−70 s], con bid en [0,05-0,95]:
una compra de SH=5 acciones que se une al MEJOR BID al FINAL de la cola (delante Q0 = tamaño del nivel). Vive 60 s.
  Relleno PESIMISTA: volumen vendedor a nuestro precio acumulado > Q0 (solo las operaciones nos adelantan), o una venta
    a precio < nuestro (atraviesa el nivel), o el nivel desaparece del libro observado y luego llega una venta <= precio.
  Relleno OPTIMISTA: además, las bajas de tamaño del nivel sin operación nos adelantan (Q = min(Q, tamaño − nada)).
Por relleno: markout del mid a +5 s y +30 s y PnL a resolución + rebate (0,2 x 0,07·p(1−p)) por acción.
EV por ORDEN COLOCADA = P(fill) x EV|fill. Cortes: cola delante (quintiles por moneda de DISC), spread (1c / >=2c),
desequilibrio N1 del token (bid vs ask en tamaño), tiempo al cierre. Periodos DISC/VALID/FINAL; IC90 por cierres.
Uso: (ulimit -v 4500000; nice -n 19 ionice -c3 python3 analisis_15m_s10_cola.py)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from m15_ms_cache import cargar  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from analisis_15m_A_quote_age import periodo  # noqa: E402

SH, VIDA, PASO = 5.0, 60_000, 5_000


def mid_en(te, bb, ba, t):
    k = np.searchsorted(te, t, side="right") - 1
    if k < 0 or not (np.isfinite(bb[k]) and np.isfinite(ba[k])):
        return np.nan
    return (bb[k] + ba[k]) / 2


def virtuales(te, bb, ba, bs, as_, T_te, T_p, T_side, T_sz, ini, fin, gana):
    out = []
    for ts in range(ini + 5000, fin - 70_000, PASO):
        k = np.searchsorted(te, ts, side="right") - 1
        if k < 0:
            continue
        P, Q0 = bb[k], bs[k]
        if not (np.isfinite(P) and np.isfinite(ba[k]) and 0.05 <= P <= 0.95 and np.isfinite(Q0)):
            continue
        spread = round(float(ba[k] - P), 2)
        imb = (bs[k] - as_[k]) / (bs[k] + as_[k]) if np.isfinite(as_[k]) and bs[k] + as_[k] > 0 else 0.0
        t_fin = ts + VIDA
        # libro y operaciones en la vida de la orden
        k1 = np.searchsorted(te, t_fin, side="right")
        j0, j1 = np.searchsorted(T_te, ts, side="right"), np.searchsorted(T_te, t_fin, side="right")
        fill = {"pes": None, "opt": None}
        for modo in ("pes", "opt"):
            Q, vol, vacio = Q0, 0.0, False
            ib = k + 1
            for j in range(j0, j1):
                tj = T_te[j]
                # actualizar estado del libro hasta tj
                while ib < k1 and te[ib] <= tj:
                    if not (np.isfinite(bb[ib]) and bb[ib] >= P - 1e-9):
                        vacio = True                        # nuestro nivel ya no está en el libro observado
                    elif abs(bb[ib] - P) < 1e-9 and modo == "opt":
                        Q = min(Q, max(0.0, bs[ib] - vol * 0))  # bajas de tamaño nos adelantan (cota optimista)
                    ib += 1
                if T_side[j] != 0:
                    continue
                p = T_p[j]
                if p < P - 1e-9 or (vacio and p <= P + 1e-9):
                    fill[modo] = tj
                    break
                if abs(p - P) < 1e-9:
                    vol += T_sz[j]
                    if vol >= Q + SH - 1e-9 or (modo == "opt" and vol >= Q):
                        fill[modo] = tj
                        break
        reb = 0.2 * 0.07 * P * (1 - P)
        fila = {"ts": ts, "P": P, "Q0": Q0, "spread": spread, "imb": imb, "t_cierre": (fin - ts) / 1000}
        for modo in ("pes", "opt"):
            tf = fill[modo]
            fila[f"lleno_{modo}"] = tf is not None
            if tf is not None:
                for h in (100, 215, 500, 1000, 2000):          # 07-Oct V3 Fase 1: curva post-relleno fina
                    fila[f"mk{h}ms_{modo}"] = mid_en(te, bb, ba, tf + h) - P
                fila[f"mid0_{modo}"] = mid_en(te, bb, ba, tf) - P   # mid en el instante del relleno (antes de movimiento)
                fila[f"mk5_{modo}"] = mid_en(te, bb, ba, tf + 5000) - P
                fila[f"mk30_{modo}"] = mid_en(te, bb, ba, tf + 30_000) - P
                fila[f"res_{modo}"] = gana - P + reb
            else:
                fila[f"mk5_{modo}"] = fila[f"mk30_{modo}"] = fila[f"res_{modo}"] = np.nan
                for h in (100, 215, 500, 1000, 2000):
                    fila[f"mk{h}ms_{modo}"] = np.nan
                fila[f"mid0_{modo}"] = np.nan
        out.append(fila)
    return out


def main():
    C = cargar()
    q, tt = C["q"], C["t"]
    toks = C["tokens"]
    des = desenlaces({k[2] for k in toks})
    bq = np.searchsorted(q["tok"], np.arange(len(toks) + 1))
    bt = np.searchsorted(tt["tok"], np.arange(len(toks) + 1))
    filas = []
    for i, (tk, act, mid_, fin, lado) in enumerate(toks):
        if mid_ not in des:
            continue
        a, b = bq[i], bq[i + 1]
        if b - a < 50:
            continue
        # 07-Oct (V3 Fase 0): --recepcion ordena libro y operaciones por NUESTRA hora de recepción (el timestamp del WS
        # puede ir hasta ~470 ms por detrás del evento real: sello de lote), en vez de por el timestamp del exchange.
        RX = "--recepcion" in sys.argv
        oq = np.argsort(q["tr"][a:b], kind="stable") if RX else np.arange(b - a)
        te = (q["tr"] if RX else q["te"])[a:b][oq]
        bb, ba = q["bb"][a:b][oq].astype(np.float64), q["ba"][a:b][oq].astype(np.float64)
        bs, as_ = q["bs"][a:b][oq].astype(np.float64), q["as_"][a:b][oq].astype(np.float64)
        ta, tb = bt[i], bt[i + 1]
        ot = np.argsort(tt["tr"][ta:tb], kind="stable") if RX else np.arange(tb - ta)
        T_te, T_p = (tt["tr"] if RX else tt["te"])[ta:tb][ot], tt["p"][ta:tb][ot].astype(np.float64)
        T_side, T_sz = tt["side"][ta:tb][ot], tt["sz"][ta:tb][ot].astype(np.float64)
        gana = 1.0 if des[mid_] == lado else 0.0
        for f in virtuales(te, bb, ba, bs, as_, T_te, T_p, T_side, T_sz, (fin - 900) * 1000, fin * 1000, gana):
            f.update(act=act, mkt=mid_, fin=fin, lado=lado)
            filas.append(f)
    R = pd.DataFrame(filas)
    R["per"] = periodo(R["ts"].values)
    R.to_parquet("/root/polymarket-research-datalogs/m15_ms_cache/s10_cola%s.parquet" % ("_recepcion" if "--recepcion" in sys.argv else ""))
    disc = R[R.per == "DISC"]
    qs = {a_: np.quantile(g.Q0, [0.2, 0.4, 0.6, 0.8]) for a_, g in disc.groupby("act")}
    R["cola_q"] = [int(np.searchsorted(qs[a_], x)) for a_, x in zip(R.act, R.Q0)]
    rng = np.random.default_rng(10)

    def tabla(g, modo):
        ll = g[f"lleno_{modo}"]
        pf = ll.mean()
        ev_f = g.loc[ll, f"res_{modo}"].mean()
        ev_o = (g[f"res_{modo}"].fillna(0)).mean()            # EV por orden colocada (sin relleno = 0)
        cie = g.assign(v=g[f"res_{modo}"].fillna(0)).groupby("fin")["v"].agg(["sum", "count"])
        S, N = cie["sum"].values, cie["count"].values
        bs = [S[x].sum() / N[x].sum() for x in (rng.integers(0, len(S), len(S)) for _ in range(500))]
        return (f"n={len(g):6} P(fill) {pf:5.3f} | mk5 {g.loc[ll, f'mk5_{modo}'].mean():+.4f} mk30 "
                f"{g.loc[ll, f'mk30_{modo}'].mean():+.4f} | EV|fill {ev_f:+.4f} | EV/orden {ev_o:+.5f} "
                f"IC90 ({np.percentile(bs, 5):+.5f},{np.percentile(bs, 95):+.5f})")
    for modo in ("pes", "opt"):
        print(f"\n===== cota {modo.upper()} ($ por acción; EV/orden = P(fill) x EV|fill) =====")
        for per in ("DISC", "VALID", "FINAL"):
            g = R[R.per == per]
            print(f"\n{per}  TODO: {tabla(g, modo)}")
            for cq, gg in g.groupby("cola_q"):
                print(f"   cola quintil {cq} (0 = cola corta): {tabla(gg, modo)}")
            for nom, m in (("spread 1c", g.spread <= 0.011), ("spread >=2c", g.spread >= 0.019),
                           ("desequilibrio a favor (imb>=0,3)", g.imb >= 0.3), ("en contra (imb<=-0,3)", g.imb <= -0.3),
                           ("últimos 3 min", g.t_cierre <= 250), ("primeros 5 min", g.t_cierre >= 600)):
                print(f"   {nom:34}: {tabla(g[m], modo)}")


if __name__ == "__main__":
    main()
