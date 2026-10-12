#!/usr/bin/env python3
"""analisis_5m_barato_latencia.py -- misión «5m barato» (12-Oct): ¿cuánto vale ser más rápido? SOLO LECTURA.
Sobre los eventos OOS del vigía congelado v4 (desde CONFIG['congelado_utc']), con su propia ejecución simulada a cada
latencia (columnas L150..L300 = libro real del 5m a t0+L, niveles 1-3) y desenlace oficial:
  - por latencia: % ejecutable, acierto de lo ejecutado, EV €/€, PnL, PnL/día (stake 2 € del vigía);
  - L=0 (contrafactual, NO alcanzable): comprar las acciones objetivo al ask de la señal;
  - profundidad en t0: tamaño del mejor ask (c_ask_sz) x precio = € disponibles al precio barato (solo nivel 1:
    cota INFERIOR de la capacidad) -> PnL/día si en cada señal se comprase TODO el nivel 1 a L=0 (techo teórico);
  - señales/día (primera señal por (cierre, moneda) y todas).
L=100 no está medida en el vigía (mínimo 150): queda acotada entre L0 y L150, no se inventa.
Uso: python3 analisis_5m_barato_latencia.py [--todas]
"""
import argparse
import collections
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import vigia_5m_barato_forward as V  # noqa: E402
from analisis_5m_barato_autopsia import _cargar, _ic90_por_grupo  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--todas", action="store_true")
    a = ap.parse_args()
    from analisis_maker_cancelacion_binance import desenlaces
    ev = _cargar(a.todas)
    des = desenlaces({e["market_compra"] for e in ev})
    ev = [e for e in ev if e["market_compra"] in des]
    dias = sorted({datetime.fromtimestamp(int(e["t_deteccion"]) / 1000, timezone.utc).date() for e in ev})
    nd = max(1, (dias[-1] - dias[0]).days + 1) if dias else 1
    print(f"{'todas las señales' if a.todas else 'primera señal por (cierre, moneda)'}: {len(ev)} señales en {nd} días "
          f"({len(ev) / nd:.1f}/día), desenlace oficial 100 %\n")
    res = {"senales": len(ev), "dias": nd, "por_latencia": {}}
    print(f"{'latencia':>8} {'ejecutables':>11} {'acierto':>7} {'EV €/€':>7} {'PnL €':>8} {'PnL/día':>8} {'IC90 cierre':>17} {'sin mejor op':>12}")
    for L in [0] + V.CONFIG["latencias_diagnostico_ms"]:
        filas = []
        for e in ev:
            gana = (des[e["market_compra"]] == "YES") == (e["lado"] == "Up")
            if L == 0:
                p, acc = float(e["ask_compra_t0"]), float(e["acciones_objetivo"])
                pnl, rie = acc * ((1.0 if gana else 0.0) - p - V.fee(p)), acc * (p + V.fee(p))
            else:
                r = V.pnl_de(e, des, f"L{L}")
                if r is None or r[1] <= 0:
                    continue
                pnl, rie = r
            filas.append((e["cierre"], gana, pnl, rie))
        if not filas:
            continue
        porc = collections.defaultdict(list)
        for c, g, pnl, rie in filas:
            porc[c].append(pnl / rie)
        pnl, rie = sum(f[2] for f in filas), sum(f[3] for f in filas)
        top = max(filas, key=lambda f: f[2])
        d = {"ejecutables": len(filas), "pct": round(len(filas) / len(ev), 3), "acierto": round(sum(f[1] for f in filas) / len(filas), 3),
             "ev": round(pnl / rie, 3), "pnl": round(pnl, 2), "pnl_dia": round(pnl / nd, 2), "ic90_cierre": _ic90_por_grupo(porc),
             "pnl_sin_mejor_op": round(pnl - top[2], 2)}
        res["por_latencia"][f"L{L}"] = d
        print(f"{('L' + str(L) + (' (contraf.)' if L == 0 else '')):>8} {d['ejecutables']:5d} ({d['pct']:4.0%}) {d['acierto']:7.0%} {d['ev']:+7.3f} "
              f"{d['pnl']:+8.2f} {d['pnl_dia']:+8.2f} {str(d['ic90_cierre']):>17} {d['pnl_sin_mejor_op']:+12.2f}")

    # profundidad al precio barato en t0 (nivel 1)
    prof = []
    for e in ev:
        try:
            sz, p = float(e["c_ask_sz"]), float(e["ask_compra_t0"])
        except (TypeError, ValueError):
            continue
        gana = (des[e["market_compra"]] == "YES") == (e["lado"] == "Up")
        prof.append((sz * p, sz, p, gana))
    if prof:
        eur = sorted(x[0] for x in prof)
        q = lambda f: eur[min(len(eur) - 1, int(f * len(eur)))]  # noqa: E731
        techo = sum(sz * ((1.0 if g else 0.0) - p - V.fee(p)) for _, sz, p, g in prof)
        coste = sum(sz * (p + V.fee(p)) for _, sz, p, g in prof)
        res["profundidad_t0_nivel1_eur"] = {"P25": round(q(.25), 2), "P50": round(q(.5), 2), "P75": round(q(.75), 2),
                                            "P90": round(q(.9), 2), "max": round(eur[-1], 2), "suma": round(sum(eur), 2)}
        res["techo_L0_todo_nivel1"] = {"pnl": round(techo, 2), "pnl_dia": round(techo / nd, 2), "capital_por_dia": round(coste / nd, 2),
                                       "ev": round(techo / coste, 3) if coste else None}
        print(f"\nprofundidad al precio barato en t0 (solo nivel 1, €): P25 {q(.25):.1f} | P50 {q(.5):.1f} | P75 {q(.75):.1f} | "
              f"P90 {q(.9):.1f} | máx {eur[-1]:.1f} | suma {sum(eur):.0f} € en {nd} días")
        print(f"TECHO teórico (L=0, comprando TODO el nivel 1 de cada señal): PnL {techo:+.2f} € = {techo / nd:+.2f} €/día, "
              f"capital {coste / nd:.0f} €/día, EV {techo / coste:+.3f} €/€  -> x365 = {techo / nd * 365:+,.0f} €/año (cota, NO previsión)")
    out = REPO / "informes" / f"m5barato_latencia_{'todas' if a.todas else 'primera'}_{datetime.now(timezone.utc):%d%b}.json".lower()
    out.write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"\nJSON: {out}")


if __name__ == "__main__":
    main()
