#!/usr/bin/env python3
"""vigia_precierre_z_marco_diario.py -- Informe DIARIO (petición Javi,
29-Sep) de ronda1 #3: ¿conviene un Z_MIN_TWAP distinto por marco en
RESOLUTION_SNIPER_PRECIERRE? Hoy Z_MIN_TWAP=1,8 global
(resolution_sniper_precierre_executor.py). Pista 29-Sep: 15min T-45 s con
z en [1,0-1,8) da EV +0,08-0,11 (5 días, n=79); 5min no. Este vigía mide,
con precierre_multioffset_fase0 (ask real, ratio>=5x, fee 7 %), EV por bin
de z a T-45 s por marco, y avisa cuando 15min z[1,0-1,8) cruce el gate
(n>=40, >=10 días, IC90 por días >0). SIEMPRE envía mensaje. Solo
observación. Cron 08:40 UTC.
"""
import csv
import random
import statistics as st
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DATOS = Path("/root/polymarket-research-datalogs/precierre_multioffset_fase0.csv")
FEE = 0.07
BINS = ((1.0, 1.4), (1.4, 1.8), (1.8, 2.5), (2.5, 99.0))


def _enviar(msg: str) -> None:
    print(msg)
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram(msg, bot="cripto")
    except Exception as e:
        print(f"[vigia_precierre_z_marco_diario] error Telegram: {e}")


def _ic(vals_por_dia):
    g = list(vals_por_dia.values())
    random.seed(1)
    b = sorted(st.mean([v for k in random.choices(g, k=len(g)) for v in k]) for _ in range(1500))
    return b[75], b[1425]


def main() -> None:
    if not DATOS.exists():
        _enviar("🎯 *Precierre z por marco (ronda1 #3)*: sin datos.")
        return
    from analisis_gbm_late_imbalance import outcomes
    R = [x for x in csv.DictReader(open(DATOS, encoding="utf-8"))
         if x["z"] and not x["error"] and x["offset_s"] == "-45" and x["ask"]]
    out = outcomes({x["market_id"] for x in R})
    S = [x for x in R if x["market_id"] in out and float(x["ratio_vs_stake"] or 0) >= 5
         and 0.05 <= float(x["ask"]) <= 0.95]
    dias_tot = len({x["ts_utc"][:10] for x in R})

    def ev(x):
        a = float(x["ask"])
        w = (out[x["market_id"]] == "YES") == (x["direccion"] == "Up")
        return ((1 - a) / a if w else -1) - FEE * (1 - a), w

    partes = [f"🎯 *Precierre: z mínimo por marco (ronda1 #3)* — informe diario",
              f"Datos multi-instante: {dias_tot} días; T-45 s, ask real fillable, fee 7 %. Umbral live hoy z>=1,8."]
    gate_15 = None
    for marco in ("5m", "15m"):
        partes.append(f"*{marco}*")
        for lo, hi in BINS:
            s = [x for x in S if x["marco"] == marco and lo <= float(x["z"]) < hi]
            etq = f"z[{lo:g},{hi:g})" if hi < 99 else f"z>={lo:g}"
            if len(s) < 10:
                partes.append(f"· {etq}: n={len(s)} (<10)")
                continue
            e = [ev(x) for x in s]
            d = defaultdict(list)
            for x, (p, _) in zip(s, e):
                d[x["ts_utc"][:10]].append(p)
            lo_ic, hi_ic = _ic(d)
            partes.append(f"· {etq}: n={len(s)} hit={sum(w for _, w in e)/len(s):.0%} "
                          f"EV {st.mean(p for p, _ in e):+.3f} IC [{lo_ic:+.3f}, {hi_ic:+.3f}] días={len(d)}")
        if marco == "15m":
            s = [x for x in S if x["marco"] == "15m" and 1.0 <= float(x["z"]) < 1.8]
            if s:
                d = defaultdict(list)
                for x in s:
                    d[x["ts_utc"][:10]].append(ev(x)[0])
                lo_ic, hi_ic = _ic(d)
                gate_15 = (len(s), len(d), st.mean(v for vs in d.values() for v in vs), lo_ic)
    if gate_15:
        n, nd, m, lo_ic = gate_15
        ok = n >= 40 and nd >= 10 and lo_ic > 0
        if ok:
            partes.append(f"🚨 *GATE 15min z[1,0-1,8) CRUZADO*: n={n}, {nd} días, EV {m:+.3f}, IC90 lo {lo_ic:+.3f} > 0. "
                          f"Proponer Z_MIN por marco (15min más bajo) con /code-review + OK Javi.")
        else:
            partes.append(f"Gate 15min z[1,0-1,8): n={n} (>=40), días={nd} (>=10), IC90 lo {lo_ic:+.3f} (>0). "
                          f"Aún NO cumple — sin cambio de umbral.")
    _enviar("\n".join(partes))


if __name__ == "__main__":
    main()
