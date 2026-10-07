#!/usr/bin/env python3
"""analisis_15m_v3_fase3_apertura.py -- MISIÓN 15M V3 FASE 3 (07-Oct): ciclo del 15m, FASE PREVIA a la ventana.
Hipótesis (fijada antes de mirar): antes del inicio de la ventana la referencia (TWAP Chainlink de apertura) aún no existe,
así que el precio justo de Up es ~0,50. Si el libro cotiza un lado con ask <= 0,50 − d, comprarlo tiene EV ≈ +d − fee.
Regla: rejilla de 10 s en [inicio − 600 s, inicio − 5 s] (reloj de RECEPCIÓN); por token (YES y NO) primer instante con
ask <= 0,50 − d; compra al ask REAL del registro ms a +250 ms (si sigue <= 0,50 − d/2); PnL/acción = gana − ask − 0,07·ask(1−ask).
Un evento por (mercado, lado, d). Desenlace oficial (gamma). IC90 por cierres; por moneda y por día; EV sin los 2 mejores cierres.
Además: distribución del mid YES en la fase previa (¿está centrado en 0,50?).
Uso: (ulimit -v 5000000; nice -n 19 ionice -c3 python3 analisis_15m_v3_fase3_apertura.py)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from m15_ms_cache import cargar  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

INF = Path(__file__).resolve().parent / "informes" / "m15v3_fase3_apertura_07oct.txt"
DS = (0.02, 0.03, 0.05, 0.08)


def main():
    C = cargar()
    q, toks = C["q"], C["tokens"]
    des = desenlaces({str(t[2]) for t in toks})
    bq = np.searchsorted(q["tok"], np.arange(len(toks) + 1))
    filas, mids = [], []
    for i, (tk, act, mid_, fin, lado) in enumerate(toks):
        mid_ = str(mid_)
        if mid_ not in des:
            continue
        a, b = bq[i], bq[i + 1]
        if b - a < 50:
            continue
        o = np.argsort(q["tr"][a:b], kind="stable")
        tr = q["tr"][a:b][o]
        bb, ba = q["bb"][a:b][o].astype(float), q["ba"][a:b][o].astype(float)
        ini = (int(fin) - 900) * 1000
        g = np.arange(ini - 600_000, ini - 5_000, 10_000)
        k = np.searchsorted(tr, g, side="right") - 1
        ok = k >= 0
        ask = np.where(ok, ba[np.clip(k, 0, None)], np.nan)
        bid = np.where(ok, bb[np.clip(k, 0, None)], np.nan)
        if lado == "YES":
            mids.extend(((ask + bid) / 2)[np.isfinite(ask) & np.isfinite(bid)].tolist())
        gana = 1.0 if des[mid_] == lado else 0.0
        for d in DS:
            idx = np.where(np.isfinite(ask) & (ask <= 0.50 - d + 1e-9))[0]
            if not len(idx):
                continue
            t = g[idx[0]]
            k2 = np.searchsorted(tr, t + 250, side="right") - 1
            a2 = ba[k2] if k2 >= 0 else np.nan
            if not (np.isfinite(a2) and 0.02 <= a2 <= 0.50 - d / 2 + 1e-9):
                continue
            filas.append(dict(act=act, mkt=mid_, fin=int(fin), lado=lado, d=d, ask=a2, gana=gana,
                              t_antes=(ini - t) / 1000, dia="2026-10-05" if ini < 1791244800000 else "2026-10-06",
                              pnl=gana - a2 - 0.07 * a2 * (1 - a2)))
    R = pd.DataFrame(filas)
    m = np.array(mids)
    L = []
    P = lambda *x: L.append(" ".join(str(y) for y in x))
    P("MISIÓN 15M V3 FASE 3 — fase previa a la ventana (10 min antes del inicio), 05-06 Oct, registro ms por recepción")
    P(f"mid YES en la fase previa (n={len(m)} fotos): P5/P25/P50/P75/P95 {np.percentile(m, [5, 25, 50, 75, 95]).round(3)}; "
      f"fracción con |mid−0,5| >= 0,03: {np.mean(np.abs(m - 0.5) >= 0.03):.1%}")
    rng = np.random.default_rng(9)
    for d in DS:
        g = R[R.d == d]
        if len(g) < 10:
            P(f"d={d:.2f}: n={len(g)} (insuficiente)")
            continue
        c = g.groupby("fin").pnl.sum()
        n = g.groupby("fin").size()
        bs = [c.iloc[ix].sum() / n.iloc[ix].sum() for ix in (rng.integers(0, len(c), len(c)) for _ in range(2000))]
        sin2 = g[~g.fin.isin(c.nlargest(2).index)].pnl.mean()
        P(f"\nd={d:.2f}: n={len(g)} eventos, {g.fin.nunique()} cierres, {g.mkt.nunique()} mercados | acierto {g.gana.mean():.1%} "
          f"ask medio {g.ask.mean():.3f} | EV/acción {g.pnl.mean():+.4f} IC90 cierres ({np.percentile(bs, 5):+.4f},"
          f"{np.percentile(bs, 95):+.4f}) | sin 2 mejores cierres {sin2:+.4f} | t antes del inicio mediana {g.t_antes.median():.0f} s")
        P("   por día: " + "  ".join(f"{k}: n={len(x)} EV {x.pnl.mean():+.4f}" for k, x in g.groupby("dia")))
        P("   por moneda: " + "  ".join(f"{k}: n={len(x)} EV {x.pnl.mean():+.3f}" for k, x in g.groupby("act")))
        P("   por lado: " + "  ".join(f"{k}: n={len(x)} acierto {x.gana.mean():.0%} EV {x.pnl.mean():+.3f}" for k, x in g.groupby("lado")))
    INF.write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
