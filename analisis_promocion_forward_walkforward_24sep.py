#!/usr/bin/env python3
"""analisis_promocion_forward_walkforward_24sep.py -- backtest walk-forward del
esquema "promoción por forward real" (24-Sep, OK de Javi):

  selector diario (bayes jerárquico temporal, P(edge>0)>=P_SEL con datos < D)
    -> la celda entra en SEGUIMIENTO desde el día en que se selecciona
    -> PROMOCIÓN a live cuando su tramo forward (solo unidades posteriores a
       la selección) cumple n>=FWD_N, días>=FWD_DIAS y media>0
    -> KILL-SWITCH en live: n_live>=20 y media<0, o suma<=-3 € (stake 1 €).

Se compara contra: operar todo, operar lo que elige el selector directamente,
y el filtro estricto actual. Universos: sports wallet mirror (34 días) y bot
wallets (15 días). Unidades = primer disparo fillable por mercado-lado.
Solo lectura.
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
import analisis_edge_sostenido_bayes_walkforward_24sep as wf  # noqa: E402

P_SEL = 0.8
FWD_N, FWD_DIAS = 20, 5
KILL_N, KILL_EUR = 20, 3.0
DIAS_CALENTAMIENTO = 7
OUT = REPO / "data/shadow/promocion_forward_walkforward_24sep.json"


def unidades_sports():
    from analisis_sports_wallet_mirror_gate_bucket_26ago import cargar_unidades_independientes, payout_win
    out = []
    for r in cargar_unidades_independientes():
        ask = float(r["mejor_ask_mirror"])
        b = round(math.floor(ask / 0.05 + 1e-9) * 0.05, 2)
        tupla = (r["categoria"], r["tipo"])
        out.append({"dia": r["timestamp_utc"][:10], "tupla": tupla, "celda": tupla + (b,),
                    "pnl": payout_win(ask) if r["acierto"] == "1" else -1.0})
    return out


def unidades_bots():
    return wf.unidades()  # ya trae dia/tupla/celda/pnl


def posterior(hist, dia):
    """Mismo modelo que wf.posterior_bayes pero con tupla explícita por unidad."""
    ref = date.fromisoformat(dia)
    wc, sc, wt, st = defaultdict(float), defaultdict(float), defaultdict(float), defaultdict(float)
    tup_de = {}
    todos = []
    for u in hist:
        w = 0.5 ** ((ref - date.fromisoformat(u["dia"])).days / wf.H_DIAS)
        wc[u["celda"]] += w; sc[u["celda"]] += w * u["pnl"]
        wt[u["tupla"]] += w; st[u["tupla"]] += w * u["pnl"]
        tup_de[u["celda"]] = u["tupla"]; todos.append(u["pnl"])
    if not todos:
        return {}
    s2 = float(np.var(todos)) or 1.0
    mt = {t: st[t] / wt[t] for t in wt}
    mc = {c: sc[c] / wc[c] for c in wc}
    tau2_t = max(np.var(list(mt.values())) - s2 / max(1.0, np.mean(list(wt.values()))), 1e-4)
    dif = [mc[c] - mt[tup_de[c]] for c in mc]
    tau2_c = max(np.var(dif) - s2 / max(1.0, np.mean(list(wc.values()))), 1e-4)
    res = {}
    for c in wc:
        t = tup_de[c]
        prec_t = 1 / tau2_t + wt[t] / s2
        m_t, v_t = (st[t] / s2) / prec_t, 1 / prec_t
        pv = tau2_c + v_t
        prec_c = 1 / pv + wc[c] / s2
        m_c = (m_t / pv + sc[c] / s2) / prec_c
        res[c] = (0.5 * (1 + math.erf(m_c / math.sqrt(2 / prec_c))), wc[c])
    return res


def simular(us, nombre):
    dias = sorted({u["dia"] for u in us})
    por_dia = defaultdict(list)
    for u in us:
        por_dia[u["dia"]].append(u)
    seguimiento = {}      # celda -> día de selección
    promovidas = {}       # celda -> día de promoción
    matadas = set()
    live = defaultdict(list)  # celda -> pnls live
    diario = {"TODO": [], "SELECTOR_DIRECTO": [], "ESTRICTO": [], "PROMO_FORWARD": []}
    eventos = []
    for i, d in enumerate(dias):
        if i < DIAS_CALENTAMIENTO:
            continue
        hist = [u for u in us if u["dia"] < d]
        post = posterior(hist, d)
        sel = {c for c, (p, ne) in post.items() if p >= P_SEL and ne >= wf.N_EFF_MIN}
        for c in sel:
            seguimiento.setdefault(c, d)
        # promoción con el tramo forward (días >= selección y < d)
        for c, d0 in seguimiento.items():
            if c in promovidas or c in matadas:
                continue
            fw = [u["pnl"] for u in hist if u["celda"] == c and u["dia"] >= d0]
            ndias = len({u["dia"] for u in hist if u["celda"] == c and u["dia"] >= d0})
            if len(fw) >= FWD_N and ndias >= FWD_DIAS and np.mean(fw) > 0:
                promovidas[c] = d
                eventos.append(f"{d} PROMOCIÓN {c} fwd n={len(fw)} días={ndias} media={np.mean(fw):+.3f}")
        est = wf.seleccion_estricta(hist) if nombre == "bots" else set()
        hoy = por_dia[d]
        diario["TODO"].append([u["pnl"] for u in hoy])
        diario["SELECTOR_DIRECTO"].append([u["pnl"] for u in hoy if u["celda"] in sel])
        diario["ESTRICTO"].append([u["pnl"] for u in hoy if u["celda"] in est])
        vivos = []
        for u in hoy:
            c = u["celda"]
            if c in promovidas and c not in matadas:
                live[c].append(u["pnl"]); vivos.append(u["pnl"])
                if (len(live[c]) >= KILL_N and np.mean(live[c]) < 0) or sum(live[c]) <= -KILL_EUR:
                    matadas.add(c)
                    eventos.append(f"{d} KILL {c} live n={len(live[c])} suma={sum(live[c]):+.2f}")
        diario["PROMO_FORWARD"].append(vivos)
    rng = np.random.default_rng(3)
    res = {"dias_evaluados": len(dias) - DIAS_CALENTAMIENTO, "promovidas": len(promovidas),
           "matadas": len(matadas), "eventos": eventos[-40:], "criterios": {}}
    print(f"\n=== {nombre}: {len(us)} unidades, {len(dias)} días, evaluados {len(dias)-DIAS_CALENTAMIENTO}, "
          f"promovidas {len(promovidas)}, matadas {len(matadas)}")
    for k, lst in diario.items():
        tot = [x for dd in lst for x in dd]
        dsum = [sum(dd) for dd in lst]
        bs = [np.mean([dsum[j] for j in rng.integers(0, len(dsum), len(dsum))]) for _ in range(3000)]
        r = {"trades": len(tot), "trades_dia": round(len(tot) / max(1, len(lst)), 1), "pnl_total": round(sum(tot), 2),
             "pnl_trade": round(float(np.mean(tot)), 4) if tot else None,
             "ci90_pnl_dia": [round(float(np.percentile(bs, 5)), 2), round(float(np.percentile(bs, 95)), 2)],
             "dias_pos": f"{sum(x > 0 for x in dsum)}/{len(dsum)}"}
        res["criterios"][k] = r
        print(f"  {k:17s} trades={r['trades']:6d} ({r['trades_dia']}/día) pnl={r['pnl_total']:+9.2f} "
              f"€/tr={r['pnl_trade']} CI90 €/día={r['ci90_pnl_dia']} días+={r['dias_pos']}")
    return res


def main():
    out = {"params": {"P_SEL": P_SEL, "FWD_N": FWD_N, "FWD_DIAS": FWD_DIAS, "KILL_N": KILL_N, "KILL_EUR": KILL_EUR,
                      "H_DIAS": wf.H_DIAS}}
    out["sports"] = simular(unidades_sports(), "sports")
    out["bots"] = simular(unidades_bots(), "bots")
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()
