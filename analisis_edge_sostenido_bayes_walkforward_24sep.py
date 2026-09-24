#!/usr/bin/env python3
"""analisis_edge_sostenido_bayes_walkforward_24sep.py -- ¿un criterio bayesiano
jerárquico con decaimiento temporal decide mejor que la cadena de filtros
estrictos actual? (24-Sep, Javi: "tiene que haber una manera más óptima de que,
por tiempo, podamos considerar que un micro-bucket tiene edge sostenido").

Datos: bot_wallets_gate_bucket_fase0.csv, unidades = primer disparo fillable en
DECISIÓN por (arquetipo, activo, marco, condition_id, lado), pnl a ask de
decisión con fee 7 %. Celda = (arquetipo, activo, marco, lado, bucket 0,05).

Walk-forward diario: para cada día D (desde el 8º), se decide con datos < D qué
celdas operar y se mide el PnL REAL de las unidades de D en esas celdas.
Criterios comparados:
  TODO     -- operar todas las celdas (referencia).
  ESTRICTO -- aproximación del gate actual: n>=40, t-test p<0,05 (una cola),
              ambas mitades >0, sin los 2 mejores días >0.
  BAYES_T  -- normal-normal jerárquico: celda encogida hacia su tupla, tupla
              encogida hacia 0; pesos 0,5^(edad/H) con H=7 días; opera si
              P(edge>0) >= UMBRAL_P y n_eff >= N_EFF_MIN.
Solo lectura. Salida por consola + data/shadow/edge_sostenido_bayes_wf_24sep.json.
"""
import csv
import json
import math
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import analisis_bot_wallets_gate_bucket_25ago as g  # noqa: E402

H_DIAS = 7.0
UMBRALES_P = (0.7, 0.8, 0.9)
N_EFF_MIN = 8
OUT = REPO / "data/shadow/edge_sostenido_bayes_wf_24sep.json"


def unidades():
    prim = {}
    with open(g.IN, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("outcome_real") or not r.get("mejor_ask_decision"):
                continue
            try:
                ask = float(r["mejor_ask_decision"]); ratio = float(r.get("ratio_vs_stake_decision") or 0)
            except ValueError:
                continue
            if not (0 < ask < 1) or ratio < g.RATIO_MIN or g.sp.es_pre_twap(r.get("marco", "?"), r.get("timestamp_utc", "")):
                continue
            k = (r["arquetipo"], r["activo"], r["marco"], r["condition_id"], r["lado_wallet"])
            if k not in prim or r["timestamp_utc"] < prim[k][0]:
                ac = 1 if r["outcome_real"] == r["lado_wallet"] else 0
                prim[k] = (r["timestamp_utc"], ask, g.pnl_neto(ask, ac))
    out = []
    for (arq, act, mar, _cid, lado), (ts, ask, pnl) in prim.items():
        b = round(math.floor(ask / 0.05 + 1e-9) * 0.05, 2)
        out.append({"dia": ts[:10], "tupla": (arq, act, mar, lado), "celda": (arq, act, mar, lado, b), "pnl": pnl})
    return out


def _d(s):
    return date.fromisoformat(s)


def seleccion_estricta(hist):
    por = defaultdict(list)
    for u in hist:
        por[u["celda"]].append(u)
    sel = set()
    for c, us in por.items():
        if len(us) < 40:
            continue
        x = np.array([u["pnl"] for u in us])
        t = x.mean() / (x.std(ddof=1) / math.sqrt(len(x)) + 1e-12)
        if t < 1.645:
            continue
        us_s = sorted(us, key=lambda u: u["dia"]); h = len(us_s) // 2
        if np.mean([u["pnl"] for u in us_s[:h]]) <= 0 or np.mean([u["pnl"] for u in us_s[h:]]) <= 0:
            continue
        dias = defaultdict(float)
        for u in us:
            dias[u["dia"]] += u["pnl"]
        mejores = set(sorted(dias, key=lambda d: -dias[d])[:2])
        resto = [u["pnl"] for u in us if u["dia"] not in mejores]
        if resto and np.mean(resto) > 0:
            sel.add(c)
    return sel


def posterior_bayes(hist, dia_ref):
    """{celda: (P(edge>0), n_eff, post_mean)} con pesos temporales."""
    ref = _d(dia_ref)
    w_c, sx_c, sxx_c = defaultdict(float), defaultdict(float), defaultdict(float)
    w_t, sx_t = defaultdict(float), defaultdict(float)
    todos = []
    for u in hist:
        w = 0.5 ** (((ref - _d(u["dia"])).days) / H_DIAS)
        w_c[u["celda"]] += w; sx_c[u["celda"]] += w * u["pnl"]; sxx_c[u["celda"]] += w * u["pnl"] ** 2
        w_t[u["tupla"]] += w; sx_t[u["tupla"]] += w * u["pnl"]
        todos.append(u["pnl"])
    s2 = float(np.var(todos)) if todos else 1.0          # varianza por unidad (ruido)
    medias_t = {t: sx_t[t] / w_t[t] for t in w_t if w_t[t] > 0}
    medias_c = {c: sx_c[c] / w_c[c] for c in w_c if w_c[c] > 0}
    # varianzas entre tuplas y entre celdas de una tupla (momentos, suelo pequeño)
    tau2_t = max(np.var(list(medias_t.values())) - s2 / max(1.0, np.mean(list(w_t.values()))), 1e-4) if medias_t else 1e-2
    dif = [medias_c[c] - medias_t[c[:4]] for c in medias_c]
    tau2_c = max(np.var(dif) - s2 / max(1.0, np.mean(list(w_c.values()))), 1e-4) if dif else 1e-2
    res = {}
    for c in w_c:
        t = c[:4]
        # tupla encogida hacia 0
        prec_t = 1 / tau2_t + w_t[t] / s2
        m_t = (sx_t[t] / s2) / prec_t
        v_t = 1 / prec_t
        # celda encogida hacia su tupla (prior N(m_t, tau2_c + v_t))
        prior_v = tau2_c + v_t
        prec_c = 1 / prior_v + w_c[c] / s2
        m_c = (m_t / prior_v + sx_c[c] / s2) / prec_c
        p = 0.5 * (1 + math.erf(m_c / math.sqrt(2 / prec_c)))
        res[c] = (p, w_c[c], m_c)
    return res


def main():
    us = unidades()
    dias = sorted({u["dia"] for u in us})
    por_dia = defaultdict(list)
    for u in us:
        por_dia[u["dia"]].append(u)
    crit = {"TODO": [], "ESTRICTO": []} | {f"BAYES_T_p{p}": [] for p in UMBRALES_P}
    for i, d in enumerate(dias):
        if i < 7:
            continue
        hist = [u for u in us if u["dia"] < d]
        hoy = por_dia[d]
        est = seleccion_estricta(hist)
        post = posterior_bayes(hist, d)
        crit["TODO"].append([u["pnl"] for u in hoy])
        crit["ESTRICTO"].append([u["pnl"] for u in hoy if u["celda"] in est])
        for p in UMBRALES_P:
            sel = {c for c, (pp, ne, _) in post.items() if pp >= p and ne >= N_EFF_MIN}
            crit[f"BAYES_T_p{p}"].append([u["pnl"] for u in hoy if u["celda"] in sel])
    rng = np.random.default_rng(7)
    out = {"dias_evaluados": dias[7:], "n_unidades": len(us), "criterios": {}}
    print(f"unidades={len(us)} días={len(dias)} evaluados={len(dias)-7} (walk-forward)")
    for k, lst in crit.items():
        tot = [x for dd in lst for x in dd]
        diarios = [sum(dd) for dd in lst]
        bs = [np.mean([diarios[j] for j in rng.integers(0, len(diarios), len(diarios))]) for _ in range(3000)] if diarios else [0]
        r = {"trades": len(tot), "trades_dia": round(len(tot) / max(1, len(lst)), 1),
             "pnl_total": round(sum(tot), 2), "pnl_trade": round(float(np.mean(tot)), 4) if tot else None,
             "pnl_dia_medio": round(float(np.mean(diarios)), 3),
             "ci90_pnl_dia": [round(float(np.percentile(bs, 5)), 3), round(float(np.percentile(bs, 95)), 3)],
             "dias_positivos": f"{sum(x > 0 for x in diarios)}/{len(diarios)}"}
        out["criterios"][k] = r
        print(f"  {k:14s} trades={r['trades']:5d} ({r['trades_dia']}/día) pnl_total={r['pnl_total']:+8.2f} "
              f"pnl/trade={r['pnl_trade']} pnl/día={r['pnl_dia_medio']:+.3f} CI90={r['ci90_pnl_dia']} días+={r['dias_positivos']}")
    OUT.write_text(json.dumps(out, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
