#!/usr/bin/env python3
"""analisis_5m_barato_autopsia.py -- misión «5m barato» (12-Oct, prompt definitivo de Javi), pasos 2-3:
reproducción de los casos OOS de la regla congelada v4 y autopsia de selección adversa. SOLO LECTURA.

Reutiliza la maquinaria del vigía congelado (vigia_5m_barato_forward: pnl_de, fee, CONFIG; desenlaces oficiales de
analisis_maker_cancelacion_binance.desenlaces) sin modificarlo (su hash no cambia al importarlo).

Para cada señal (primer evento por (cierre, moneda), OOS desde CONFIG['congelado_utc']) da: clase a +215 ms
(A sigue barato / B cancelado o repreciado / C consumido por un tomador / D otro nivel barato / UNKNOWN), precio y
acciones ejecutables, desenlace oficial, PnL a +215 ms y PnL CONTRAFACTUAL al ask de la señal (t0, "si fuéramos
instantáneos"). Autopsia: acierto y EV contrafactual por clase -> ¿desaparecen las buenas? ¿quedan las malas?
Con --todas incluye los re-armes (variante V2 exploratoria; descriptivo, NO es validación).
Unidad de independencia: (cierre) -- varias monedas o eventos del mismo cierre comparten desenlace correlado.
Salida: stdout + informes/m5barato_autopsia_<fecha>.json
"""
import argparse
import collections
import csv
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import vigia_5m_barato_forward as V  # noqa: E402

CLASES = {"A": "A_sigue_barato", "B": "B_cancelado_o_repreciado", "C": "C_consumido_por_tomador",
          "D": "D_otro_nivel_barato", "U": "UNKNOWN"}


def _cargar(todas):
    E = []
    for f in sorted(V.SALIDA.glob("eventos_*.csv")):
        E += list(csv.DictReader(open(f)))
    cong = int(datetime.fromisoformat(V.CONFIG["congelado_utc"]).timestamp() * 1000)
    return [e for e in E if e["regla"] == "B1_5m" and int(e["t_deteccion"]) >= cong
            and (todas or e["es_primero"] == "1")]


def _ic90_por_grupo(grupos, n=4000):
    g = [v for v in grupos.values() if v]
    if len(g) < 3:
        return None
    rng, med = random.Random(7), []
    for _ in range(n):
        s = [x for _ in g for x in rng.choice(g)]
        med.append(sum(s) / len(s))
    med.sort()
    return [round(med[int(0.05 * n)], 3), round(med[int(0.95 * n)], 3)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--todas", action="store_true", help="incluir re-armes (variante V2 exploratoria)")
    a = ap.parse_args()
    from analisis_maker_cancelacion_binance import desenlaces
    ev = _cargar(a.todas)
    des = desenlaces({e["market_compra"] for e in ev})
    filas = []
    for e in ev:
        if e["market_compra"] not in des:
            continue
        gana = (des[e["market_compra"]] == "YES") == (e["lado"] == "Up")
        p0 = float(e["ask_compra_t0"])
        acc0 = float(e["acciones_objetivo"])
        r215 = V.pnl_de(e, des, "L215")
        clase = (e["L215_clase"] or "U")[0]
        filas.append({
            "event_id": e["event_id"], "moneda": e["moneda"], "cierre": e["cierre"], "lado": e["lado"],
            "t": datetime.fromtimestamp(int(e["t_deteccion"]) / 1000, timezone.utc).isoformat(timespec="milliseconds"),
            "resto_s": round(float(e["resto_s"]), 1), "ask_t0": p0, "bid15_t0": float(e["bid_otro_t0"]),
            "margen_neto": float(e["margen_neto"]), "p_limite": float(e["p_limite"]), "clase": CLASES.get(clase, clase),
            "acc_215": float(e["L215_acciones"] or 0), "precio_215": e["L215_precio"], "gana": gana,
            "pnl_215": None if r215 is None else round(r215[0], 3), "riesgo_215": None if r215 is None else round(r215[1], 3),
            # contrafactual: comprar las acciones objetivo al ask de la señal (latencia 0), mismo fee
            "pnl_t0": round(acc0 * ((1.0 if gana else 0.0) - p0 - V.fee(p0)), 3), "riesgo_t0": round(acc0 * (p0 + V.fee(p0)), 3),
            "edad_ask_ms": e["c_edad_ask_ms"], "c_ask_sz": e["c_ask_sz"], "o_bid_sz": e["o_bid_sz"],
            "c_trades_1s": e["c_trades_1s"], "c_cancel_1s": e["c_cancel_1s"], "bin_ret_1s_bps": e["bin_ret_1s_bps"],
        })
    filas.sort(key=lambda f: f["t"])
    etiqueta = "TODAS las señales (con re-armes, V2 exploratoria)" if a.todas else "PRIMERA señal por (cierre, moneda) = regla congelada v4"
    print(f"== {etiqueta}: {len(filas)} señales OOS con desenlace oficial (de {len(ev)}) ==\n")
    print(f"{'hora UTC':19} {'mon':4} {'lado':4} {'ask0':>5} {'bid15':>5} {'marg':>5} {'clase':26} {'acc':>5} {'p215':>5} {'gana':>4} {'PnL215':>7} {'PnL_t0':>7}")
    for f in filas:
        print(f"{f['t'][:19]} {f['moneda']:4} {f['lado']:4} {f['ask_t0']:5.2f} {f['bid15_t0']:5.2f} {f['margen_neto']:5.2f} "
              f"{f['clase']:26} {f['acc_215']:5.1f} {str(f['precio_215'])[:5]:>5} {'sí' if f['gana'] else 'no':>4} "
              f"{(f['pnl_215'] if f['pnl_215'] is not None else float('nan')):+7.2f} {f['pnl_t0']:+7.2f}")

    print("\n== AUTOPSIA por clase a +215 ms (acierto y EV €/€ si hubiéramos comprado al ask de la señal, t0) ==")
    res = {"etiqueta": etiqueta, "n": len(filas), "por_clase": {}, "filas": filas}
    por_clase = collections.defaultdict(list)
    for f in filas:
        por_clase[f["clase"]].append(f)
    print(f"{'clase':26} {'n':>3} {'acierto':>7} {'ask0 medio':>10} {'EV€/€ t0':>9} {'ejecutadas':>10} {'EV€/€ 215':>9}")
    for c, v in sorted(por_clase.items()):
        ev_t0 = sum(x["pnl_t0"] for x in v) / sum(x["riesgo_t0"] for x in v)
        ej = [x for x in v if x["acc_215"] > 0 and x["pnl_215"] is not None]
        ev215 = (sum(x["pnl_215"] for x in ej) / sum(x["riesgo_215"] for x in ej)) if ej else None
        res["por_clase"][c] = {"n": len(v), "acierto": round(sum(x["gana"] for x in v) / len(v), 3),
                               "ask0_medio": round(sum(x["ask_t0"] for x in v) / len(v), 3), "ev_t0": round(ev_t0, 3),
                               "ejecutadas": len(ej), "ev_215": None if ev215 is None else round(ev215, 3)}
        print(f"{c:26} {len(v):3d} {res['por_clase'][c]['acierto']:7.0%} {res['por_clase'][c]['ask0_medio']:10.2f} "
              f"{ev_t0:+9.3f} {len(ej):10d} {('%+.3f' % ev215) if ev215 is not None else '-':>9}")

    def bloque(nombre, sub, pnl_k, rie_k):
        sub = [x for x in sub if x[pnl_k] is not None and x[rie_k]]
        if not sub:
            return None
        pnl, rie = sum(x[pnl_k] for x in sub), sum(x[rie_k] for x in sub)
        porc = collections.defaultdict(list)
        for x in sub:
            porc[x["cierre"]].append(x[pnl_k] / x[rie_k])
        top = max(sub, key=lambda x: x[pnl_k])
        sin_top = [x for x in sub if x is not top]
        d = {"n": len(sub), "cierres": len(porc), "acierto": round(sum(x["gana"] for x in sub) / len(sub), 3),
             "pnl_eur": round(pnl, 2), "ev_eur_por_eur": round(pnl / rie, 3), "ic90_por_cierre": _ic90_por_grupo(porc),
             "pnl_sin_mejor_op": round(sum(x[pnl_k] for x in sin_top), 2),
             "mejor_op": {k: top[k] for k in ("t", "moneda", "lado", "ask_t0", "precio_215", "acc_215", "pnl_215", "pnl_t0")}}
        print(f"{nombre:46} n={d['n']:3d} cierres={d['cierres']:3d} acierto={d['acierto']:.0%} PnL={d['pnl_eur']:+7.2f}€ "
              f"EV={d['ev_eur_por_eur']:+.3f}€/€ IC90(cierre)={d['ic90_por_cierre']} sin mejor op={d['pnl_sin_mejor_op']:+.2f}€")
        return d

    print("\n== Políticas sobre la MISMA muestra (contrafactual t0 = cota superior por velocidad, NO alcanzable hoy) ==")
    res["politicas"] = {
        "real_215_ejecutadas": bloque("real a +215 ms (lo que se llena)", [x for x in filas if x["acc_215"] > 0], "pnl_215", "riesgo_215"),
        "t0_todas": bloque("todas al ask de la señal (latencia 0)", filas, "pnl_t0", "riesgo_t0"),
        "t0_las_que_desaparecen": bloque("al ask t0, solo las que desaparecen (B+C)",
                                         [x for x in filas if x["clase"][0] in "BC"], "pnl_t0", "riesgo_t0"),
        "t0_las_que_quedan": bloque("al ask t0, solo las que quedan (A+D)",
                                    [x for x in filas if x["clase"][0] in "AD"], "pnl_t0", "riesgo_t0"),
    }
    out = REPO / "informes" / f"m5barato_autopsia_{'todas' if a.todas else 'primera'}_{datetime.now(timezone.utc):%d%b}.json".lower()
    out.write_text(json.dumps(res, indent=1, ensure_ascii=False, default=str), encoding="utf-8")
    print(f"\nJSON: {out}")


if __name__ == "__main__":
    main()
