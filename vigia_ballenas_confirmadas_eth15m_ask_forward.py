#!/usr/bin/env python3
"""vigia_ballenas_confirmadas_eth15m_ask_forward.py -- forward CONGELADO (02-Oct, Javi "si" al protocolo)
de BALLENAS_CONFIRMADAS_15M#ETH#15min#BUY_YES comprando solo con ask real < 0,60.

Origen (memoria project_ballenas_confirmadas_eth15m_ask060_02oct): un análisis del 02-Oct daba +0,156 €/€
(tupla) y +0,275 (ask<0,60), pero tenía un BUG: no filtraba `direction` en libro_snapshots (854 mercados con
el ask del token NO). Con este script (BUY_YES filtrado) la regla da +0,027 post-TWAP (IC90 cruza 0): el
camino del ejecutor real −0,047 y el de shadow_predict +0,33 hasta 07-Sep y −0,015 después. REFUTADA como
candidata live; se deja el script SIN cron por si se quiere re-medir.

Regla congelada: primera fila de libro_snapshots por market_id con strategy=BALLENAS_CONFIRMADAS_15M,
subtype=ETH#15min, direction=BUY_YES, ratio_vs_stake>=5, 0<mejor_ask<0,60; PnL por € con ask_real.pnl_1eur;
desenlace oficial = outcome_real de results.csv (analisis_gbm_late_imbalance.outcomes). Confirmada = n>=40,
>=10 días, EV>=+0,10 €/€ e IC90 bootstrap por días >0. Nada pasa a real sin checklist de 6 categorías +
techo de ask en el ejecutor (/code-review) + OK de Javi. Cron diario; --telegram envía el resumen.
"""
import csv
import json
import random
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import ask_real  # noqa: E402
from analisis_gbm_late_imbalance import outcomes  # noqa: E402

SNAP = REPO / "data" / "live" / "libro_snapshots.csv"
OUT = REPO / "data" / "shadow" / "vigia_ballenas_confirmadas_eth15m_ask_forward.json"
CORTE = "2026-10-02T10:00:00"
TUPLA = ("BALLENAS_CONFIRMADAS_15M", "ETH#15min", "BUY_YES")
ASK_MAX, RATIO_MIN = 0.60, 5.0
N_MIN, DIAS_MIN, EV_MIN = 40, 10, 0.10


def _primeras_filas() -> dict:
    """{market_id: (timestamp_utc, ask)} con la primera fila por mercado que cumple la regla."""
    vistos, out = set(), {}
    with open(SNAP, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if (r.get("strategy"), r.get("subtype"), r.get("direction")) != TUPLA:
                continue
            m = r.get("market_id")
            if m in vistos:
                continue
            vistos.add(m)                       # la PRIMERA lectura del mercado decide, cumpla o no
            try:
                a, ratio = float(r["mejor_ask"]), float(r["ratio_vs_stake"] or 0)
            except (TypeError, ValueError, KeyError):
                continue
            if ratio >= RATIO_MIN and 0 < a < ASK_MAX:
                out[m] = (r["timestamp_utc"], a)
    return out


def _resumen(filas) -> dict:
    por_dia = defaultdict(list)
    for ts, a, ac in filas:
        por_dia[ts[:10]].append(ask_real.pnl_1eur(a, ac))
    vals = [v for vs in por_dia.values() for v in vs]
    if not vals:
        return {"n": 0, "dias": 0}
    ic = None
    dias = list(por_dia.values())
    if len(dias) >= 3:
        rnd = random.Random(11)
        bs = sorted(sum(sum(x) for x in m) / sum(len(x) for x in m)
                    for m in ([rnd.choice(dias) for _ in dias] for _ in range(2000)))
        ic = [round(bs[100], 4), round(bs[1900], 4)]
    ev = sum(vals) / len(vals)
    return {"n": len(vals), "dias": len(por_dia), "dias_positivos": sum(sum(v) > 0 for v in dias),
            "acierto": round(sum(1 for _, _, ac in filas if ac) / len(filas), 3),
            "ask_medio": round(sum(a for _, a, _ in filas) / len(filas), 3), "ev": round(ev, 4), "ic90_dias": ic,
            "confirmada": bool(len(vals) >= N_MIN and len(por_dia) >= DIAS_MIN and ev >= EV_MIN and ic and ic[0] > 0)}


def main() -> int:
    prim = _primeras_filas()
    out = outcomes(set(prim))
    antes, fwd, pendientes = [], [], 0
    for m, (ts, a) in prim.items():
        g = out.get(m)
        if g is None:
            pendientes += ts >= CORTE
            continue
        (fwd if ts >= CORTE else antes).append((ts, a, g == "YES"))
    res = {"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "corte": CORTE,
           "regla": f"{'#'.join(TUPLA)} ask<{ASK_MAX} ratio>={RATIO_MIN}",
           "antes_del_corte": _resumen(antes), "forward": _resumen(fwd), "forward_sin_desenlace": pendientes}
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    f, a = res["forward"], res["antes_del_corte"]
    lineas = [f"🐋 *BALLENAS_CONFIRMADAS ETH 15m, ask<0,60* — forward congelado desde {CORTE}Z",
              f"Antes del corte: n={a.get('n')} días={a.get('dias')} EV {a.get('ev')} IC90 {a.get('ic90_dias')}",
              f"Forward: n={f.get('n')} días={f.get('dias')} (+{f.get('dias_positivos', 0)}) acierto {f.get('acierto')} "
              f"ask medio {f.get('ask_medio')} EV {f.get('ev')} IC90 {f.get('ic90_dias')} | sin desenlace aún {pendientes}",
              ("✅ CONFIRMADA en forward: toca checklist 6 categorías + techo de ask en el ejecutor (/code-review) + OK Javi."
               if f.get("confirmada") else f"Gate: n>={N_MIN}, >={DIAS_MIN} días, EV>=+{EV_MIN}, IC90 por días >0. Aún no.")]
    print("\n".join(lineas))
    if "--telegram" in sys.argv:
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram("\n".join(lineas), bot="cripto")
        except Exception as e:
            print(f"(no se pudo avisar por Telegram: {e})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
