#!/usr/bin/env python3
"""vigia_pares15_entrada_mid.py -- HIPÓTESIS PAIR15_ENTRY_MID_V1, CONGELADA el 2026-10-12T17:15:00Z (misión «pares 15m»,
filtro de entrada; prompt de Javi 12-Oct). SOLO LECTURA: evalúa la regla sobre los ledgers del ensayo en seco
(experimento_pares_cola_15m.py) con el libro del archivo m15_registro y el desenlace oficial.

REGLA (congelada; cambiarla = V2 + nuevo periodo): en la apertura del 15m (t = cierre - 900 s + 2 s, hora de recepción),
mid YES = (mejor bid + mejor ask)/2 del token YES. Se PARTICIPA en el mercado solo si |mid YES - 0,5| <= 0,02 y el libro
de ambos tokens existe (si falta -> no se participa, fail-closed). La política de pujas no cambia (anclar/crear/mixta).
Descubrimiento (09-10 Oct, 80 mercados, NO cuenta): 26 mercados pasan, 4 patas sueltas (vs 27/80), PnL +6,76 $
(+0,26 $/merc), sin el mejor +3,86; positivo en SOL y BTC. Mecanismo: mercado que abre ya inclinado = información
direccional presente -> se llena el lado perdedor; abierto equilibrado -> rellenos simétricos y pares completos.
VALIDACIÓN: solo mercados con mercado_fin posterior a VALIDA_DESDE (ensayo 'crear' lanzado 12-Oct 14:59Z, NO mirado al
fijar la regla). Necesita el archivo m15_registro del día (cron 03:45 del día siguiente).
Uso: python3 vigia_pares15_entrada_mid.py [--desde ISO] [--hasta ISO]
"""
import argparse
import collections
import hashlib
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from analisis_experimento_pares_sim import ganadores  # noqa: E402
from analisis_pares15_patas_sueltas import cargar_libros, cargar_mercados, libro_en, pnl_original  # noqa: E402

CONFIG = {"nombre": "PAIR15_ENTRY_MID_V1", "congelado_utc": "2026-10-12T17:15:00+00:00", "t_entrada_s": 2,
          "max_dist_mid": 0.02, "valida_desde": "2026-10-12T14:59:00"}
HASH = hashlib.sha256(json.dumps(CONFIG, sort_keys=True).encode()).hexdigest()[:16]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default=CONFIG["valida_desde"])
    ap.add_argument("--hasta", default="2099")
    a = ap.parse_args()
    M = cargar_mercados(a.desde, a.hasta)
    des = ganadores([m["id"] for m in M]) if M else {}
    M = [m for m in M if m["id"] in des]
    L = cargar_libros(M)
    filas = []
    for m in M:
        o = pnl_original(m, des[m["id"]])
        t = (m["cierre"] - 900 + CONFIG["t_entrada_s"]) * 1000
        y, n = libro_en(L, m["id"], "YES", t), libro_en(L, m["id"], "NO", t)
        ok_libro = y and n and None not in (y[0], y[1], n[0], n[1])
        entra = bool(ok_libro) and abs((y[0] + y[1]) / 2 - 0.5) <= CONFIG["max_dist_mid"] + 1e-12
        filas.append({"entra": entra, "sin_libro": not ok_libro, "pnl": o["pnl_par"] + o["pnl_res"], "moneda": m["moneda"],
                      "pol": m["pol"], "res": "par" if o["par"] >= 5 - 1e-9 else ("suelta" if o["lado_res"] else "nada")})
    print(f"{CONFIG['nombre']} (hash {HASH}) | periodo {a.desde} → {a.hasta} | mercados {len(filas)} (sin libro {sum(f['sin_libro'] for f in filas)})")
    for nom, g in (("CON filtro (participa)", [f for f in filas if f["entra"]]), ("excluidos por el filtro", [f for f in filas if not f["entra"]]),
                   ("SIN filtro (todos)", filas)):
        if not g:
            print(f"  {nom}: 0")
            continue
        pn = sorted(f["pnl"] for f in g)
        print(f"  {nom:24} n={len(g):3d} sueltas={sum(f['res'] == 'suelta' for f in g):3d} pares={sum(f['res'] == 'par' for f in g):3d} "
              f"PnL={sum(pn):+7.2f} $ ({sum(pn) / len(g):+.3f}/merc) sin el mejor={sum(pn[:-1]):+7.2f}")
        for k in sorted({(f["moneda"], f["pol"]) for f in g}):
            gg = [f for f in g if (f["moneda"], f["pol"]) == k]
            print(f"       {k[0]} {k[1]:7} n={len(gg):3d} sueltas={sum(f['res'] == 'suelta' for f in gg):2d} PnL={sum(f['pnl'] for f in gg):+7.2f}")
    print("Estado: FORWARD_PENDING hasta n>=40 mercados filtrados en validación; nada a dinero sin gates + /code-review + OK Javi.")


if __name__ == "__main__":
    main()
