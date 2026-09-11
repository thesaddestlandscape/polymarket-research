#!/usr/bin/env python3
"""¿El maker (ya refutado en agregado, maker_sim.csv z≈-2) funciona en el
subconjunto más estrecho: señales de ALTA conviction Y fase TEMPRANA de la
ventana (antes de que llegue el flujo informado, según el estudio de
ballenas)? Petición Javi 12-Jul, tarea #4 de la lista de soluciones.

Reusa maker_sim.csv (ya simulado, miles de filas, mismo método de fill por
tape que el piloto real) cruzado con results.csv (edge_neto ya calculado,
restante_min dentro de features) — CERO llamadas nuevas a la API, decisión
ladder: ya existe el dato, solo hace falta cruzarlo distinto.

Conviction = |edge_neto| (cuánto más alto, más convencido el modelo).
Fase temprana = restante_min alto dentro de la ventana de entrada (GBM_LATE
entra en los últimos 3-20min; "temprano" aquí = más minutos restantes
dentro de ese rango, no el inicio absoluto del mercado de 15min).

Solo lectura, no toca dinero ni config.
"""
import csv
import json
import statistics as st

MAKER_SIM = "data/shadow/maker_sim.csv"
RESULTS = "data/shadow/results.csv"


def cargar_results_idx():
    idx = {}
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                feats = json.loads(r.get("features") or "{}")
            except Exception:
                feats = {}
            idx[(r["strategy"], r["subtype"], r["market_id"], r["decision"])] = {
                "edge_neto": r.get("edge_neto"),
                "restante_min": feats.get("restante_min"),
            }
    return idx


def _ev(rows):
    n = len(rows)
    if n == 0:
        return None
    pnls = [float(r["pnl1_maker"]) for r in rows]
    ev = sum(pnls) / n
    sd = st.stdev(pnls) if n > 1 else 0.0
    se = sd / (n ** 0.5) if n > 1 else 0.0
    z = ev / se if se > 0 else 0.0
    fill = sum(1 for r in rows if r.get("filled") == "1") / n
    return n, ev, z, fill


def main():
    idx = cargar_results_idx()
    rows = list(csv.DictReader(open(MAKER_SIM, encoding="utf-8")))

    enriquecidas = []
    for r in rows:
        info = idx.get((r["strategy"], r["subtype"], r["market_id"], r["decision"]))
        if not info or info["edge_neto"] is None or info["restante_min"] is None:
            continue
        try:
            edge = abs(float(info["edge_neto"]))
            restante = float(info["restante_min"])
        except (ValueError, TypeError):
            continue
        enriquecidas.append((r, edge, restante))

    print(f"maker_sim.csv: {len(rows)} filas | con edge_neto+restante_min cruzados: {len(enriquecidas)}\n")

    if len(enriquecidas) < 20:
        print("Muestra insuficiente para segmentar.")
        return

    edges = sorted(e for _, e, _ in enriquecidas)
    restantes = sorted(rt for _, _, rt in enriquecidas)
    p66_edge = edges[int(len(edges) * 0.66)]
    p66_rest = restantes[int(len(restantes) * 0.66)]

    print(f"Umbral alta conviction (|edge_neto| top tercio): >={p66_edge:.4f}")
    print(f"Umbral ventana temprana (restante_min top tercio): >={p66_rest:.2f} min\n")

    segmentos = {
        "TODO (baseline, ya conocido)": [r for r, _, _ in enriquecidas],
        "Alta conviction (cualquier momento)": [r for r, e, _ in enriquecidas if e >= p66_edge],
        "Ventana temprana (cualquier conviction)": [r for r, _, rt in enriquecidas if rt >= p66_rest],
        "Alta conviction Y ventana temprana": [r for r, e, rt in enriquecidas if e >= p66_edge and rt >= p66_rest],
        "Alta conviction Y ventana TARDÍA": [r for r, e, rt in enriquecidas if e >= p66_edge and rt < p66_rest],
    }

    print(f"{'segmento':42s} {'n':>5} {'EV_maker/señal':>15} {'z':>7} {'fill%':>7}")
    print("-" * 85)
    for nombre, subset in segmentos.items():
        res = _ev(subset)
        if res is None:
            print(f"{nombre:42s}   n=0")
            continue
        n, ev, z, fill = res
        print(f"{nombre:42s} {n:5d} {ev:+15.4f} {z:+7.2f} {fill:6.1%}")


if __name__ == "__main__":
    main()
