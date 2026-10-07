#!/usr/bin/env python3
"""analisis_15m_A3_politica_maker.py -- MISIÓN DEFINITIVA 15m, línea A3 (06-Oct): ¿alguna política KEEP / CANCEL / WIDEN
gana más que mantener una cotización pasiva sin información? Registro ms (m15_ms_cache.py), corte de la línea A
(DISC / EMB / VALID / FINAL); umbrales SOLO de DISC; aquí se mira FINAL por primera vez (decisión final).

Simulación (reloj del exchange para libro y operaciones; señales por hora de RECEPCIÓN + latencia):
  - Un bid de SH acciones por token (YES y NO) en el MEJOR bid, al FINAL de la cola (delante = tamaño del nivel al entrar).
    Si el mejor bid sube, nos movemos (al final otra vez). Si baja sin operación a nuestro precio, seguimos ahí solos.
  - Relleno: operación a precio < nuestro bid (lo atraviesa) o volumen acumulado a nuestro precio > cola delante + SH.
    Cancelaciones de los de delante NO nos adelantan (conservador). Tope 50 acciones por token y mercado.
  - Solo entre inicio+5 s y cierre−10 s, bid en [0,05-0,95]. PnL a resolución, maker sin comisión.
Políticas:
  KEEP          pasiva.
  CANCEL_BN_P90 / _P99  cancela cuando Binance (aggTrade, recepción) se mueve en 1 s en CONTRA del token por encima del
                P90/P99 de DISC; efecto en recepción + L; vuelve a cotizar 2 s después del último disparo.
  CANCEL_CL_P90 cancela con un tick de Chainlink en contra por encima del P90 de DISC.
  WIDEN         un tick (0,01) por debajo del mejor bid; sin conocer su cola: solo relleno si una operación lo atraviesa.
  L = 150 y 250 ms (+25 y +50 ms de estrés sobre 250); SH = 5 y 25 (REDUCE/tamaño).
Estadística: PnL por mercado (YES+NO), IC90 bootstrap de CIERRES, por periodo; diferencia contra KEEP emparejada por
mercado; sin el mejor cierre; por moneda.
Uso: (ulimit -v 5000000; python3 analisis_15m_A3_politica_maker.py)   Solo lectura.
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from m15_ms_cache import cargar  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from analisis_15m_dataset_maestro import cargar_chainlink  # noqa: E402
from analisis_15m_A_quote_age import DISC, periodo, MON  # noqa: E402

MAX_SH = 50.0
ENFR = 2000


def senales(C, cl):
    """Por moneda: (t_recepcion, retorno firmado) de Binance 1 s y de Chainlink tick a tick, y umbrales P90/P99 de DISC."""
    x = C["x"]
    out = {}
    for si, act in enumerate(MON):
        m = x["s"] == si
        T, P = x["tr"][m], x["p"][m]
        o = np.argsort(T, kind="stable")
        T, P = T[o], P[o]
        k = np.searchsorted(T, T - 1000, side="right") - 1
        r = np.where(k >= 0, (P / P[np.clip(k, 0, None)] - 1) * 1e4, 0.0)
        d = (T >= DISC[0]) & (T < DISC[1])
        q90 = np.quantile(np.abs(r[d]), 0.90) if d.any() else np.nan      # 07-Oct: caché sin DISC (--nuevo) -> NaN,
        q99 = np.quantile(np.abs(r[d]), 0.99) if d.any() else np.nan      # que main() sustituye por los umbrales fijos
        bn = (T, r, q90, q99)
        clx = None
        if act in cl:
            ct = np.frombuffer(cl[act].t, dtype=np.int64)
            cp = np.frombuffer(cl[act].p, dtype=np.float64)
            rr = np.r_[0, (cp[1:] / cp[:-1] - 1) * 1e4]
            dd = (ct >= DISC[0]) & (ct < DISC[1])
            clx = (ct, rr, np.quantile(np.abs(rr[dd]), 0.90) if dd.any() else np.nan)
        out[act] = (bn, clx)
    return out


def bloqueos(sig_t, sig_r, thr, sentido, t0, t1, L):
    """Intervalos [t+L, t+L+ENFR) en que la cotización está retirada (señales en contra, umbral thr)."""
    m = (sig_t >= t0 - ENFR) & (sig_t <= t1) & (np.abs(sig_r) >= thr) & (np.sign(sig_r) == -sentido)
    ts = sig_t[m] + L
    if not len(ts):
        return np.empty(0, np.int64), np.empty(0, np.int64)
    ini, fin = [ts[0]], [ts[0] + ENFR]
    for t in ts[1:]:
        if t <= fin[-1]:
            fin[-1] = t + ENFR
        else:
            ini.append(t)
            fin.append(t + ENFR)
    return np.array(ini), np.array(fin)


def simular(te, bb, bs, cb, T_te, T_p, T_sz, t0, t1, SH, bloq, widen):
    """-> (acciones, coste) del bid simulado de un token."""
    bi, bf = bloq
    ev_q = np.flatnonzero(cb & (te >= t0 - 60_000) & (te <= t1))
    ev_t = np.flatnonzero((T_te >= t0) & (T_te <= t1))
    # fusión ordenada: (t, tipo 0=libro 1=operación 2=bloqueo empieza 3=bloqueo acaba, índice)
    ev = [(te[i], 0, i) for i in ev_q] + [(T_te[j], 1, j) for j in ev_t]
    ev += [(b, 2, 0) for b in bi if t0 <= b <= t1] + [(f, 3, 0) for f in bf if t0 <= f <= t1]
    ev.sort()
    sh = coste = 0.0
    cot = None                     # [precio, delante, vol_a_precio]
    bloqueado = bool(len(bi)) and np.any((bi <= t0) & (bf > t0))
    best, best_sz = np.nan, 0.0
    k0 = np.searchsorted(te, t0, side="right") - 1
    if k0 >= 0:
        best, best_sz = bb[k0], bs[k0]

    def poner():
        if sh >= MAX_SH or not np.isfinite(best) or not (0.05 <= best <= 0.95):
            return None
        if widen:
            return [round(best - 0.01, 2), np.inf, 0.0] if best - 0.01 >= 0.05 else None
        return [best, best_sz, 0.0]

    if not bloqueado:
        cot = poner()
    for t, tipo, i in ev:
        if t < t0:
            if tipo == 0:
                best, best_sz = bb[i], bs[i]
            continue
        if tipo == 2:
            bloqueado, cot = True, None
            continue
        if tipo == 3:
            bloqueado = bool(np.any((bi <= t) & (bf > t)))
            if not bloqueado and cot is None:
                cot = poner()
            continue
        if tipo == 0:
            best, best_sz = bb[i], bs[i]
            if not bloqueado and (cot is None or (np.isfinite(best) and best > cot[0] + 1e-9 + (0.01 if widen else 0))):
                cot = poner()
            continue
        if cot is None:
            continue
        p, sz = T_p[i], T_sz[i]
        lleno = p < cot[0] - 1e-9
        if not lleno and abs(p - cot[0]) < 1e-9:
            cot[2] += sz
            lleno = cot[2] >= cot[1] + SH
        if lleno:
            q = min(SH, MAX_SH - sh)
            sh += q
            coste += q * cot[0]
            cot = None
            if not bloqueado:
                cot = poner()
    return sh, coste


# 07-Oct (misión 15M v2, rastreo de A3 BTC con días NUEVOS): --nuevo usa la caché M15_CACHE_DIR (días posteriores al
# diseño), umbrales CONGELADOS publicados en informes/m15_A3_politica_maker_combo_06oct.txt (no se recalculan), la política
# congelada CANCEL_CL+BN_P90 L=250 SH=5 frente a KEEP, y solo mercados que cierran tras el 06-Oct 16:15 UTC.
NUEVO = "--nuevo" in sys.argv
UMB_FIJOS = {"BTC": (1.29, 3.26, 0.28), "ETH": (5.09, 45.58, 0.36), "SOL": (2.48, 10.77, 0.45),
             "XRP": (2.00, 5.99, 0.57), "DOGE": (4.17, 21.22, 0.65), "BNB": (1.28, 5.22, 0.36)}
CORTE_NUEVO = 1791339300                 # 2026-10-06T16:15:00Z


def main():
    C = cargar()
    q, tt = C["q"], C["t"]
    toks = C["tokens"]
    des = desenlaces({k[2] for k in toks})
    cl = cargar_chainlink(["2026-10-06", "2026-10-07"] if NUEVO else ["2026-10-05", "2026-10-06"])
    S = senales(C, cl)
    if NUEVO:                             # umbrales congelados del diseño, nunca recalculados con los días nuevos
        for act, (b90, b99, c90) in UMB_FIJOS.items():
            if act in S:
                bn, clx = S[act]
                S[act] = ((bn[0], bn[1], b90, b99), (clx[0], clx[1], c90) if clx else None)
    for act in MON:
        bn, clx = S[act]
        print(f"umbrales DISC {act}: Binance 1 s P90 {bn[2]:.2f} bps P99 {bn[3]:.2f} | Chainlink tick P90 "
              f"{clx[2] if clx else float('nan'):.2f} bps")
    bq = np.searchsorted(q["tok"], np.arange(len(toks) + 1))
    bt = np.searchsorted(tt["tok"], np.arange(len(toks) + 1))
    configs = [("KEEP", None, 0, 5, False), ("KEEP", None, 0, 25, False), ("WIDEN", None, 0, 5, False)]
    for L in (150, 250, 275, 300):
        configs += [("CANCEL_BN_P90", "bn90", L, 5, False), ("CANCEL_BN_P99", "bn99", L, 5, False),
                    ("CANCEL_CL_P90", "cl90", L, 5, False)]
    configs += [("CANCEL_BN_P90", "bn90", 250, 25, False)]
    if NUEVO:
        configs = [("KEEP", None, 0, 5, False), ("CANCEL_CL+BN_P90", "combo", 250, 5, False)]
    elif "--curva" in sys.argv:       # 07-Oct misión definitiva §5/§29: curva latencia->dinero del maker que cancela. La
        # cancelación medida con órdenes reales cuesta ~60 ms ida y vuelta (~30 ms de ida) + firma ~6 ms: L realista ~40 ms,
        # no 150-300 (A3 original usaba latencias de tomador). Misma regla CL+BN P90 de DISC, L de 0 a 300 ms.
        configs = [("KEEP", None, 0, 5, False)] + [("CANCEL_CL+BN_P90", "combo", L, 5, False)
                                                   for L in ((-130, -100, -60, -30, 0) if "--neg" in sys.argv
                                                             else (0, 25, 50, 75, 100, 150, 200, 250, 300))]
        # --neg: L negativa = recibir la señal ANTES (cota superior del valor de un feed más rápido que Binance-Tokio,
        # p. ej. Kraken/Bitstamp ~100 ms antes en Helsinki, SI se movieran a la vez que Binance; ver leadlag_venues_llegada)
    elif "--combo" in sys.argv:       # 2ª pasada (06-Oct): UNA combinación declarada antes: las dos señales protectoras
        configs = [("KEEP", None, 0, 5, False)] + [("CANCEL_CL+BN_P90", "combo", L, 5, False) for L in (150, 250, 275, 300)]
    filas = []
    for i, (tk, act, mid_, fin, lado) in enumerate(toks):
        if mid_ not in des or act not in S:
            continue
        if NUEVO and fin < CORTE_NUEVO:
            continue
        a, b = bq[i], bq[i + 1]
        if b - a < 50:
            continue
        te = q["te"][a:b]
        bb = q["bb"][a:b].astype(np.float64)
        bs = q["bs"][a:b].astype(np.float64)
        bbf = np.nan_to_num(bb, nan=-1)
        cb = np.r_[True, bbf[1:] != bbf[:-1]]
        ta, tb = bt[i], bt[i + 1]
        T_te, T_p, T_sz = tt["te"][ta:tb], tt["p"][ta:tb].astype(np.float64), tt["sz"][ta:tb].astype(np.float64)
        t0, t1 = (fin - 900) * 1000 + 5000, fin * 1000 - 10_000
        gana = 1.0 if des[mid_] == lado else 0.0
        sentido = 1 if lado in ("YES", "Up") else -1
        bn, clx = S[act]
        for nom, sig, L, SH, _ in configs:
            if sig is None:
                bl = (np.empty(0, np.int64), np.empty(0, np.int64))
            elif sig == "combo":
                if clx is None:
                    continue
                b1 = bloqueos(bn[0], bn[1], bn[2], sentido, t0, t1, L)
                b2 = bloqueos(clx[0], clx[1], clx[2], sentido, t0, t1, L)
                iv = sorted(zip(np.r_[b1[0], b2[0]], np.r_[b1[1], b2[1]]))
                ini, fin_ = [], []
                for x0, x1 in iv:
                    if ini and x0 <= fin_[-1]:
                        fin_[-1] = max(fin_[-1], x1)
                    else:
                        ini.append(x0)
                        fin_.append(x1)
                bl = (np.array(ini, dtype=np.int64), np.array(fin_, dtype=np.int64))
            elif sig.startswith("bn"):
                bl = bloqueos(bn[0], bn[1], bn[2] if sig == "bn90" else bn[3], sentido, t0, t1, L)
            else:
                if clx is None:
                    continue
                bl = bloqueos(clx[0], clx[1], clx[2], sentido, t0, t1, L)
            sh, coste = simular(te, bb, bs, cb, T_te, T_p, T_sz, t0, t1, SH, bl, nom == "WIDEN")
            # rebate del maker (07-Oct, verificado en clob-markets: rebateRate 0.2 de la comisión 0,07·p·(1−p) del tomador
            # que nos rellena); estimación con el precio medio de nuestros rellenos
            pm = coste / sh if sh > 0 else 0.0
            reb = 0.2 * 0.07 * pm * (1 - pm) * sh
            filas.append((nom, L, SH, act, mid_, fin, lado, sh, coste, sh * gana - coste, sh * gana - coste + reb))
    R = pd.DataFrame(filas, columns=["pol", "L", "SH", "act", "mkt", "fin", "lado", "acc", "coste", "pnl", "pnl_reb"])
    R["per"] = "NUEVO" if NUEVO else periodo((R["fin"].values - 450) * 1000)
    suf = "_nuevo" if NUEVO else ("_curva_neg" if "--neg" in sys.argv else "_curva") if "--curva" in sys.argv else "_combo" if "--combo" in sys.argv else ""
    R.to_parquet("/root/polymarket-research-datalogs/m15_ms_cache/A3_politicas%s.parquet" % suf)
    if "--curva" in sys.argv or NUEVO:
        curva(R)
        return
    informe(R)


def curva(R):
    """$/mercado (YES+NO) por L y periodo, sin y con rebate; IC90 bootstrap de CIERRES; por moneda en VALID+FINAL."""
    rng = np.random.default_rng(3)
    M = R.groupby(["pol", "L", "per", "mkt", "fin", "act"], as_index=False)[["acc", "pnl", "pnl_reb"]].sum()
    print("\nCURVA LATENCIA -> DINERO del maker que cancela (CL+BN P90), $/mercado; L = ms desde la RECEPCIÓN del dato")
    print(f"{'pol':16} {'L':>4} {'per':5} | {'merc':>4} {'acc':>6} | {'$/merc':>7} {'con rebate':>10} {'IC90 cierres (rebate)':>24}")
    for (pol, L, per), g in M.groupby(["pol", "L", "per"]):
        if per == "EMB":
            continue
        cie = g.groupby("fin")["pnl_reb"].agg(["sum", "count"])
        S, N = cie["sum"].values, cie["count"].values
        bs = [S[k].sum() / N[k].sum() for k in (rng.integers(0, len(S), len(S)) for _ in range(1000))]
        print(f"{pol:16} {L:4} {per:5} | {len(g):4} {g.acc.sum():6.0f} | {g.pnl.mean():+7.3f} {g.pnl_reb.mean():+10.3f} "
              f"({np.percentile(bs, 5):+.3f},{np.percentile(bs, 95):+.3f})")
    print("\nPor moneda, VALID+FINAL, $/mercado con rebate:")
    G = M[M.per.isin(["VALID", "FINAL", "NUEVO"])].groupby(["pol", "L", "per", "act"])["pnl_reb"].mean().unstack()
    print(G.round(3).to_string())


def informe(R):
    rng = np.random.default_rng(2)
    M = R.groupby(["pol", "L", "SH", "per", "mkt", "fin", "act"], as_index=False)[["acc", "coste", "pnl"]].sum()
    base = M[(M.pol == "KEEP") & (M.SH == 5)][["per", "mkt", "pnl"]].rename(columns={"pnl": "pnl_keep"})
    print(f"\n{'política':14} {'L':>4} {'SH':>3} {'per':5} | {'merc':>4} {'acc':>6} {'$/merc':>7} {'PnL/€':>7} "
          f"{'IC90 cierres $/merc':>20} {'sin mejor cierre':>8} | {'vs KEEP $/merc':>14} {'IC90':>18} | por moneda $/merc")
    for (pol, L, SH, per), g in M.groupby(["pol", "L", "SH", "per"]):
        if per == "EMB":
            continue
        gc = g.groupby("fin")["pnl"].agg(["sum", "count"])
        bs = [gc.iloc[rng.integers(0, len(gc), len(gc))].pipe(lambda x: x["sum"].sum() / x["count"].sum()) for _ in range(800)]
        mejor = gc["sum"].idxmax()
        sin = (gc["sum"].sum() - gc.loc[mejor, "sum"]) / (gc["count"].sum() - gc.loc[mejor, "count"])
        dd = g.merge(base[base.per == per], on=["per", "mkt"])
        dd["d"] = dd["pnl"] - dd["pnl_keep"]
        dc = dd.groupby("fin")["d"].agg(["sum", "count"])
        bd = [dc.iloc[rng.integers(0, len(dc), len(dc))].pipe(lambda x: x["sum"].sum() / x["count"].sum()) for _ in range(800)]
        mon = g.groupby("act")["pnl"].mean()
        print(f"{pol:14} {L:4} {SH:3} {per:5} | {len(g):4} {g.acc.sum():6.0f} {g.pnl.mean():+7.3f} "
              f"{g.pnl.sum() / max(1e-9, g.coste.sum()):+7.3f} ({np.percentile(bs, 5):+7.3f},{np.percentile(bs, 95):+7.3f}) "
              f"{sin:+8.3f} | {dd.d.mean():+14.3f} ({np.percentile(bd, 5):+7.3f},{np.percentile(bd, 95):+7.3f}) | "
              + " ".join(f"{k}:{v:+.2f}" for k, v in mon.items()))


if __name__ == "__main__":
    main()
