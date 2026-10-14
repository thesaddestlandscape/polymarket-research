#!/usr/bin/env python3
"""analisis_5m_barato_retraso_deliberado.py -- SUBESTRATEGIA 9 de 5m barato (Javi 14-Oct): "entrada con retraso deliberado".
Pista: en v4 el EV/€ SUBE con la latencia (lab 05-13: L215 +1,28 -> L355 +1,63 -> L475 +1,88) => lo que solo pilla el rápido
sería la trampa. Control propio, mismos eventos (laboratorio lab_lat: maquinaria v4 a L150/215/300/355/475/600), SOLO LECTURA:
  A) por latencia L: ejecutables, EV/€ (unidad = cierre-moneda, primera señal), IC90 por días, sin 05-Oct, sin top3;
  B) EMPAREJADO 215 vs L: eventos ejecutables a 215 y NO a L ("solo el rápido") vs ejecutables a L ("siguen al esperar"):
     EV de cada grupo AL MISMO PRECIO (el de su propia ejecución) -> si "solo el rápido" pierde, esperar filtra.
Universos: BTC (decisión) y TODAS (contraste). Primera señal por (cierre, moneda) y todas las señales (re-armes).
Uso: python3 analisis_5m_barato_retraso_deliberado.py
"""
import csv
import random
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vigia_5m_barato_forward as V  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

LAB = Path("/root/polymarket-research-datalogs/m5barato_mision/lab_lat")
LATS = (150, 215, 300, 355, 475, 600)
RNG = random.Random(9)


def dia(e):
    return datetime.fromtimestamp(int(e["cierre"]), timezone.utc).date().isoformat()


def ic(pares_dia, n=3000):
    ks = [k for k in pares_dia if pares_dia[k][1] > 0]
    if len(ks) < 3:
        return None
    m = sorted(sum(pares_dia[k][0] for k in s) / sum(pares_dia[k][1] for k in s) for s in ([RNG.choice(ks) for _ in ks] for _ in range(n)))
    return (round(m[int(.05 * n)], 3), round(m[int(.95 * n)], 3))


def main():
    E = []
    for f in sorted(LAB.glob("eventos_*.csv")):
        E += [e for e in csv.DictReader(open(f)) if e["regla"] == "B1_5m"]
    des = desenlaces({e["market_compra"] for e in E})
    L = []
    for uni in ("BTC", "TODAS"):
        for sel, nom_sel in ((lambda e: e["es_primero"] == "1", "primera señal"), (lambda e: True, "todas las señales")):
            ev = [e for e in E if sel(e) and (uni == "TODAS" or e["moneda"] == "BTC")]
            L.append(f"\n== {uni} / {nom_sel}: {len(ev)} señales")
            for lat in LATS:
                pp = [(e, V.pnl_de(e, des, f"L{lat}")) for e in ev]
                pp = [(e, p) for e, p in pp if p and p[1] > 0]
                if not pp:
                    continue
                pdd = defaultdict(lambda: [0.0, 0.0])
                for e, p in pp:
                    pdd[dia(e)][0] += p[0]
                    pdd[dia(e)][1] += p[1]
                sin5 = [(e, p) for e, p in pp if dia(e) != "2026-10-05"]
                pn = sorted((p[0] for _, p in pp), reverse=True)
                L.append(f"  L{lat:3d}: ejec {len(pp):3d} | PnL {sum(pn):+8.2f} € | EV/€ {sum(pn) / sum(p[1] for _, p in pp):+.3f} | "
                         f"IC90 días {ic(pdd)} | sin 05-Oct EV {sum(p[0] for _, p in sin5) / max(1e-9, sum(p[1] for _, p in sin5)):+.3f} "
                         f"(n={len(sin5)}) | sin top3 {sum(pn[3:]):+.2f} €")
            for lat in (355, 475):
                solo, siguen = [], []
                for e in ev:
                    a = V.pnl_de(e, des, "L215")
                    b = V.pnl_de(e, des, f"L{lat}")
                    if a and a[1] > 0 and not (b and b[1] > 0):
                        solo.append(a)
                    if b and b[1] > 0:
                        siguen.append(b)
                f = lambda X: (f"n={len(X)} EV/€ {sum(x[0] for x in X) / sum(x[1] for x in X):+.3f} PnL {sum(x[0] for x in X):+.2f} €"
                               if X else "n=0")
                L.append(f"  emparejado 215 vs {lat}: SOLO EL RÁPIDO (ejec a 215, no a {lat}) {f(solo)} | SIGUEN AL ESPERAR (ejec a {lat}) {f(siguen)}")
    txt = "\n".join(L)
    print(txt)
    (LAB.parent / "retraso_deliberado_informe.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
