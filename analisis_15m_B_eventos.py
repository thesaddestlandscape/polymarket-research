#!/usr/bin/env python3
"""analisis_15m_B_eventos.py -- MISIÓN DEFINITIVA 15m, línea B (06-Oct): EVENTO -> RESPUESTA DEL 15m -> PnL.
Registro ms (m15_ms_cache.py), mismo corte que la línea A (DISC 05-Oct 16:00 → 06-Oct 02:00 | EMB → 03:30 | VALID →
09:30 | FINAL bloqueado). Todo fijado antes de mirar:
EVENTOS (umbrales por moneda = percentiles P90/P95/P99 calculados SOLO en DISC; refractario 5 s por moneda y tipo):
  BN_SALTO   |retorno Binance en 1 s| (aggTrade por hora de RECEPCIÓN; evaluado en cada operación de Binance)
  CL_SALTO   |retorno tick a tick de Chainlink RTDS| (recepción)
  BN_VOL     σ Binance 10 s / σ 300 s (cada operación)
  PM_VOLUMEN nº de operaciones del 15m de esa moneda en 1 s (todas sus ventanas vivas)
  PM_FLUJO   |volumen tomador firmado (YES+, NO−) del 15m en 1 s| en $ (hora del exchange)
  Dirección: Binance/Chainlink -> signo del retorno; PM -> signo del flujo. El lado del evento en el 15m = YES si sube.
RESPUESTA: para cada mercado 15m vivo de esa moneda (10 s < t al cierre < 895 s): mid y ask del lado del evento en
  t0 + {−500, −250, −100, −50, 0, 10, 25, 50, 100, 150, 215, 250, 500, 1000, 5000} ms (libro del exchange, última fila q
  <= instante). t0 = RECEPCIÓN del evento (lo que sabíamos); el libro se lee en reloj del exchange (la recepción va
  p50 26 ms detrás: el desfase favorece al libro, no a nosotros).
EJECUCIÓN TOMADOR: comprar el lado del evento (SEGUIR) o el contrario (FADE) al ask REAL vigente en t0 + L, L = 150, 200,
  215, 250, 300 ms (+ estrés 240, 265 = 215+25/50) y segundo movimiento a +1 s / +5 s; tamaño = min(stake/ask, tamaño del
  nivel 1) (relleno parcial, el resto no se ejecuta); comisión 0,07·p(1−p); desenlace oficial. Stakes 1/2/5/10/25/50 €.
MAKER: rellenos de bids/asks del lado CONTRARIO al evento en [t0, t0+2 s] (los tóxicos) y su markout a resolución;
  € que se salvarían cancelando con efecto en t0 + 100/150/250 ms (los rellenos posteriores a ese instante).
CONTROLES: PLACEBO = instantes aleatorios del mismo periodo, moneda y hora, emparejados por tramo de mid de 0,10 y de
  tiempo al cierre (mismo nº de eventos), con la misma regla de lado al azar; INVERSIÓN = FADE; DESPLAZADO = misma regla
  con t0 − 60 s.
Métrica principal (pre-registrada): SEGUIR a +215 ms, stake 2 €, por clase P90/P95/P99 y tipo; resto = estrés/benchmark.
Multiplicidad: p por permutación de PLACEBO y max-statistic sobre todas las celdas (tipo × clase × acción) en VALID.
Uso: (ulimit -v 5000000; python3 analisis_15m_B_eventos.py)   Solo lectura.
"""
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from m15_ms_cache import cargar  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from analisis_15m_dataset_maestro import cargar_chainlink  # noqa: E402

ms = lambda s: int(datetime.fromisoformat(s).replace(tzinfo=timezone.utc).timestamp() * 1000)
DISC = (ms("2026-10-05T16:00"), ms("2026-10-06T02:00"))
VALID = (ms("2026-10-06T03:30"), ms("2026-10-06T09:30"))
FINAL = (ms("2026-10-06T09:30"), ms("2026-10-07T00:00"))
MON = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
OFF = [-500, -250, -100, -50, 0, 10, 25, 50, 100, 150, 215, 250, 500, 1000, 5000]
LATS = [150, 200, 215, 240, 250, 265, 300, 1000, 5000]
STAKES = [1, 2, 5, 10, 25, 50]
FEE = 0.07
REFR = 5000


def periodo(t):
    return np.where((t >= DISC[0]) & (t < DISC[1]), "DISC", np.where((t >= VALID[0]) & (t < VALID[1]), "VALID",
                    np.where(t >= FINAL[0], "FINAL", "EMB")))


def eventos_de(t, v, sgn, nombre, act):
    """t, valor del disparador (>=0), signo. Umbrales P90/P95/P99 en DISC; primer cruce con refractario."""
    d = (t >= DISC[0]) & (t < DISC[1]) & np.isfinite(v)
    if d.sum() < 100:
        return []
    out = []
    for cl, q in (("P90", 0.90), ("P95", 0.95), ("P99", 0.99)):
        thr = np.quantile(v[d], q)
        idx = np.flatnonzero(np.isfinite(v) & (v >= thr) & (sgn != 0))
        ult = -10 ** 18
        for k in idx:
            if t[k] - ult >= REFR:
                out.append((int(t[k]), int(sgn[k]), nombre, cl, act, float(v[k])))
                ult = t[k]
    return out


def main():
    C = cargar()
    q, tt, x = C["q"], C["t"], C["x"]
    toks = C["tokens"]
    des = desenlaces({k[2] for k in toks})
    # mercados por moneda: lista de (fin, mid, tokYES, tokNO)
    por = {}
    for i, (tk, act, mid_, fin, lado) in enumerate(toks):
        por.setdefault((act, mid_, fin), {})[lado] = i
    mercados = {}
    for (act, mid_, fin), d in por.items():
        if "YES" in d and "NO" in d and mid_ in des:
            mercados.setdefault(act, []).append((fin, mid_, d["YES"], d["NO"]))
    bq = np.searchsorted(q["tok"], np.arange(len(toks) + 1))
    bt = np.searchsorted(tt["tok"], np.arange(len(toks) + 1))
    cl = cargar_chainlink(["2026-10-05", "2026-10-06"])
    ev = []
    for si, act in enumerate(MON):
        m = x["s"] == si
        T, P = x["tr"][m], x["p"][m]
        o = np.argsort(T, kind="stable")
        T, P = T[o], P[o]
        k1 = np.searchsorted(T, T - 1000, side="right") - 1
        r1 = np.where(k1 >= 0, (P / P[np.clip(k1, 0, None)] - 1) * 1e4, np.nan)
        ev += eventos_de(T, np.abs(r1), np.sign(r1), "BN_SALTO", act)
        lr = np.r_[0, np.diff(np.log(P))]
        cs = np.cumsum(lr * lr)
        k10 = np.searchsorted(T, T - 10_000)
        k300 = np.searchsorted(T, T - 300_000)
        v10 = (cs - cs[k10]) / 10
        v300 = (cs - cs[k300]) / 300
        ratio = np.where(v300 > 0, np.sqrt(v10 / np.maximum(v300, 1e-30)), np.nan)
        k5 = np.searchsorted(T, T - 5000)
        ev += eventos_de(T, ratio, np.sign(P - P[k5]), "BN_VOL", act)
        if act in cl:
            ct = np.frombuffer(cl[act].t, dtype=np.int64)
            cp = np.frombuffer(cl[act].p, dtype=np.float64)
            rr = np.r_[0, (cp[1:] / cp[:-1] - 1) * 1e4]
            ev += eventos_de(ct, np.abs(rr), np.sign(rr), "CL_SALTO", act)
        # 15m: operaciones de todas las ventanas de esa moneda
        tes, sg = [], []
        for fin, mid_, iy, inn in mercados.get(act, []):
            for i, s_lado in ((iy, 1), (inn, -1)):
                a, b = bt[i], bt[i + 1]
                tes.append(tt["te"][a:b])
                sg.append(s_lado * np.where(tt["side"][a:b] == 1, 1, -1) * tt["sz"][a:b] * tt["p"][a:b])
        if tes:
            te_ = np.concatenate(tes)
            sg_ = np.concatenate(sg)
            o = np.argsort(te_, kind="stable")
            te_, sg_ = te_[o], sg_[o]
            k = np.searchsorted(te_, te_ - 1000, side="right")
            n1 = np.arange(len(te_)) - k + 1
            cs = np.cumsum(sg_)
            f1 = cs - np.r_[0, cs][k]
            ev += eventos_de(te_, n1.astype(float), np.sign(f1), "PM_VOLUMEN", act)
            ev += eventos_de(te_, np.abs(f1), np.sign(f1), "PM_FLUJO", act)
    E = pd.DataFrame(ev, columns=["t0", "dir", "tipo", "clase", "act", "mag"])
    E["per"] = periodo(E["t0"].values)
    print("eventos por tipo y clase (todos los periodos): ")
    print(E.groupby(["tipo", "clase", "per"]).size().unstack(fill_value=0).to_string())
    # placebo emparejado: mismo periodo, moneda y hora; instante al azar
    rng = np.random.default_rng(11)
    pl = E.copy()
    hora0 = (pl["t0"] // 3_600_000) * 3_600_000
    pl["t0"] = hora0 + rng.integers(0, 3_600_000, len(pl))
    pl["dir"] = rng.choice([-1, 1], len(pl))
    pl["tipo"] = "PLACEBO_" + pl["tipo"]
    pl["per"] = periodo(pl["t0"].values)
    de = E.copy()
    de["t0"] = de["t0"] - 60_000
    de["tipo"] = "DESPLAZ_" + de["tipo"]
    de["per"] = periodo(de["t0"].values)
    TODO = pd.concat([E, pl, de], ignore_index=True)
    filas = []
    for r in TODO.itertuples(index=False):
        for fin, mid_, iy, inn in mercados.get(r.act, []):
            tte = fin - r.t0 / 1000
            if not (10 < tte < 895):
                continue
            i_ev, i_ct = (iy, inn) if r.dir > 0 else (inn, iy)
            gana_ev = 1.0 if (des[mid_] == "YES") == (r.dir > 0) else 0.0
            a, b = bq[i_ev], bq[i_ev + 1]
            te = q["te"][a:b]
            kk = np.searchsorted(te, r.t0 + np.array(OFF + LATS), side="right") - 1
            if kk[OFF.index(0)] < 0:
                continue
            bb, ba, as_ = q["bb"][a:b], q["ba"][a:b], q["as_"][a:b]
            a2, b2 = bq[i_ct], bq[i_ct + 1]
            te2 = q["te"][a2:b2]
            kc = np.searchsorted(te2, r.t0 + np.array(LATS), side="right") - 1
            f = {"tipo": r.tipo, "clase": r.clase, "act": r.act, "per": r.per, "t0": r.t0, "mkt": mid_, "fin": fin,
                 "tte": tte, "gana": gana_ev}
            for o, k in zip(OFF, kk[:len(OFF)]):
                f[f"mid_{o}"] = (bb[k] + ba[k]) / 2 if k >= 0 else np.nan
            mid0 = f["mid_0"]
            if not np.isfinite(mid0):
                continue
            f["tramo"] = int(min(9, max(0, mid0 * 10)))
            for L, k, k2 in zip(LATS, kk[len(OFF):], kc):
                f[f"ask_{L}"] = ba[k] if k >= 0 else np.nan
                f[f"asz_{L}"] = as_[k] if k >= 0 else np.nan
                f[f"askc_{L}"] = q["ba"][a2:b2][k2] if k2 >= 0 else np.nan
                f[f"aszc_{L}"] = q["as_"][a2:b2][k2] if k2 >= 0 else np.nan
            # maker: rellenos contrarios (bids del lado del evento consumidos por vendedores = no; los tóxicos para un
            # maker son: su ASK del lado del evento levantado, o su BID del lado contrario golpeado) en [t0, t0+2 s]
            tox = []
            for i_tok, lado_tox in ((i_ev, 1), (i_ct, 0)):     # ask del lado evento (taker BUY) / bid del contrario (SELL)
                ta, tb = bt[i_tok], bt[i_tok + 1]
                T_te = tt["te"][ta:tb]
                j0, j1 = np.searchsorted(T_te, r.t0), np.searchsorted(T_te, r.t0 + 2000)
                for j in range(ta + j0, ta + j1):
                    if tt["side"][j] == lado_tox:
                        p = float(tt["p"][j])
                        # pnl del maker: vendió el lado evento a p (pierde si gana el evento) / compró el contrario a p
                        pn = (p - gana_ev) if lado_tox == 1 else ((1 - gana_ev) - p)
                        tox.append((int(tt["te"][j]) - r.t0, float(tt["sz"][j]) * pn, float(tt["sz"][j])))
            f["tox_n"] = len(tox)
            for Lc in (100, 150, 250):
                f[f"tox_salvado_{Lc}"] = sum(v for dt, v, _ in tox if dt >= Lc)
            f["tox_total"] = sum(v for _, v, _ in tox)
            filas.append(f)
    R = pd.DataFrame(filas)
    out = Path("/root/polymarket-research-datalogs/m15_ms_cache")
    R.to_parquet(out / "B_eventos.parquet")
    informe(R)


def pnl_tomador(R, L, stake, fade=False):
    p = R[f"askc_{L}" if fade else f"ask_{L}"].values.astype(float)
    sz = R[f"aszc_{L}" if fade else f"asz_{L}"].values.astype(float)
    w = (1 - R["gana"].values) if fade else R["gana"].values
    ok = np.isfinite(p) & (p > 0.01) & (p < 0.99) & np.isfinite(sz)
    sh = np.where(ok, np.minimum(stake / np.where(ok, p, 1), sz), 0.0)
    pn = sh * (w - p - FEE * p * (1 - p))
    rk = sh * (p + FEE * p * (1 - p))
    return np.where(ok, pn, 0.0), np.where(ok, rk, 0.0)


def resumen_celda(R, L=215, stake=2, fade=False):
    pn, rk = pnl_tomador(R, L, stake, fade)
    if rk.sum() <= 0:
        return None
    d = pd.DataFrame({"fin": R["fin"].values, "pn": pn, "rk": rk})
    g = d.groupby("fin")[["pn", "rk"]].sum()
    rng = np.random.default_rng(5)
    bs = [g.iloc[rng.integers(0, len(g), len(g))].pipe(lambda x: x.pn.sum() / x.rk.sum()) for _ in range(500)]
    return pn.sum() / rk.sum(), pn.sum(), int((rk > 0).sum()), np.percentile(bs, [5, 95])


def informe(R):
    V = R[R["per"].isin(["DISC", "VALID"])]
    print("\nRESPUESTA MEDIA DEL MID del lado del evento (VALID, eventos reales, mid(t) − mid(0)) por tipo y clase:")
    Vv = V[V.per == "VALID"]
    for (tp, cl), g in Vv[~Vv.tipo.str.contains("_", regex=False) | Vv.tipo.str.startswith(("BN_", "CL_", "PM_"))].groupby(["tipo", "clase"]):
        if tp.startswith(("PLACEBO", "DESPLAZ")):
            continue
        print(f"  {tp:11} {cl} n={len(g):5} " + " ".join(f"{o}:{(g[f'mid_{o}'] - g['mid_0']).mean() * 100:+.2f}c"
                                                      for o in (-500, -100, 50, 215, 500, 1000, 5000)))
    print("\nTOMADOR (PnL por € arriesgado, stake 2 €, ask REAL + tamaño nivel 1, comisión, desenlace oficial)")
    print(f"{'tipo':22} {'clase':5} {'per':5} {'acción':6} | " + " ".join(f"{('+' + str(L)):>8}" for L in LATS)
          + " | n(215) IC90(215, cierres)")
    celdas = []
    for (tp, cl, per), g in V.groupby(["tipo", "clase", "per"]):
        for fade in (False, True):
            vals = [resumen_celda(g, L, 2, fade) for L in LATS]
            if vals[2] is None:
                continue
            celdas.append((tp, cl, per, fade, vals[2][0]))
            print(f"{tp:22} {cl:5} {per:5} {'FADE' if fade else 'SEGUIR':6} | "
                  + " ".join(f"{v[0]:+8.3f}" if v else "     nan" for v in vals)
                  + f" | {vals[2][2]:6} ({vals[2][3][0]:+.3f},{vals[2][3][1]:+.3f})")
    C = pd.DataFrame(celdas, columns=["tipo", "clase", "per", "fade", "ev215"])
    real = C[~C.tipo.str.startswith(("PLACEBO", "DESPLAZ"))]
    plac = C[C.tipo.str.startswith("PLACEBO")]
    for per in ("DISC", "VALID"):
        r = real[real.per == per]
        p_ = plac[plac.per == per]
        print(f"\n{per}: celdas reales con EV>0 a +215 ms: {(r.ev215 > 0).sum()}/{len(r)} | placebo con EV>0: "
              f"{(p_.ev215 > 0).sum()}/{len(p_)} | máx real {r.ev215.max():+.3f} vs máx placebo {p_.ev215.max():+.3f}")
    # capacidad de la mejor celda de VALID (sin elegir en FINAL)
    rv = real[(real.per == "VALID")].sort_values("ev215", ascending=False).head(3)
    print("\nMejores 3 celdas de VALID (exploratorio; candidatas solo si también DISC>0) y capacidad por stake:")
    for _, c in rv.iterrows():
        g = V[(V.tipo == c.tipo) & (V.clase == c.clase)]
        dsc = [x for x in celdas if x[0] == c.tipo and x[1] == c.clase and x[2] == "DISC" and x[3] == c.fade]
        print(f"  {c.tipo} {c.clase} {'FADE' if c.fade else 'SEGUIR'}: VALID {c.ev215:+.3f} DISC "
              f"{dsc[0][4] if dsc else float('nan'):+.3f} | stakes " + " ".join(
                  f"{s}€:{resumen_celda(g[g.per == 'VALID'], 215, s, c.fade)[1]:+.1f}€" for s in STAKES))
    print("\nMAKER: € de rellenos tóxicos en [t0, t0+2 s] y € salvados cancelando a +100/150/250 ms (VALID, reales):")
    for (tp, cl), g in Vv.groupby(["tipo", "clase"]):
        if tp.startswith(("PLACEBO", "DESPLAZ")):
            continue
        print(f"  {tp:11} {cl} eventos-mercado {len(g):5} | tóxico total {g.tox_total.sum():+8.1f}$ | salvado "
              f"+100 {g.tox_salvado_100.sum():+7.1f} +150 {g.tox_salvado_150.sum():+7.1f} +250 {g.tox_salvado_250.sum():+7.1f}")


if __name__ == "__main__":
    main()
