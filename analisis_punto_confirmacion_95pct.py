#!/usr/bin/env python3
"""analisis_punto_confirmacion_95pct.py — CLAUDE.md protocolo pt.10.

Busca, por (activo,marco), el punto (bucket de precio, bucket de tiempo
restante al cierre) donde el límite inferior de un IC de Wilson al 95%
ya supera 95% de acierto con edge real (precio del favorito < 0.90),
sobre TODO el histórico acumulado de punto_confirmacion_YYYY-MM-DD.csv
(punto_confirmacion_logger.py, screen `puntoconf`, desde 23-Jul).

Grid: precio en buckets de 0.05 (solo <0.90, edge real), restante_s en
buckets de 60s. N_MIN=30 por celda (mismo mínimo del proyecto). Reporta
la celda con MENOR restante_s_max (más pronto detectable) que ya cruza
el gate, por (activo,marco) -- ese es el "punto de confirmación" real.
"""
import csv
import glob
import math
from collections import defaultdict

Z_95 = 1.96
N_MIN = 30
PASO_PRECIO = 0.05
PASO_TIEMPO = 60


def wilson_lower(hits, n, z=Z_95):
    if n == 0:
        return 0.0
    p = hits / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centro - margen) / denom


def bucket(x, paso):
    return math.floor(x / paso) * paso


def main():
    celdas = defaultdict(lambda: [0, 0])  # (activo,marco,precio_b,tiempo_b) -> [hits, n]
    n_filas = 0
    for f in sorted(glob.glob("data/shadow/punto_confirmacion_*.csv")):
        with open(f, encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                try:
                    # precio del FAVORITO (no precio_yes crudo -- si lado_favorito=NO,
                    # precio_yes bajo es justo lo contrario de "favorito barato").
                    precio = float(r.get("best_ask_favorito") or "nan")
                    restante = float(r.get("restante_s_real") or r.get("restante_s_objetivo") or "nan")
                    gano = int(r.get("favorito_gano") or -1)
                except (TypeError, ValueError):
                    continue
                if gano not in (0, 1) or not (0.0 < precio < 0.90) or restante < 0:
                    continue
                activo, marco = r.get("activo"), r.get("marco")
                if not activo or not marco:
                    continue
                pb = bucket(precio, PASO_PRECIO)
                tb = bucket(restante, PASO_TIEMPO)
                k = (activo, marco, pb, tb)
                celdas[k][0] += gano
                celdas[k][1] += 1
                n_filas += 1
    print(f"{n_filas} filas válidas (precio<0.90, favorito_gano conocido) sobre "
          f"{len(glob.glob('data/shadow/punto_confirmacion_*.csv'))} días acumulados\n")

    por_activo_marco = defaultdict(list)
    for (activo, marco, pb, tb), (hits, n) in celdas.items():
        if n < N_MIN:
            continue
        wlo = wilson_lower(hits, n)
        por_activo_marco[(activo, marco)].append((tb, pb, hits, n, wlo))

    if not por_activo_marco:
        print("Ninguna celda con n>=30 todavía en ningún (activo,marco).")
        return

    for (activo, marco), celdas_ok in sorted(por_activo_marco.items()):
        confirmadas = [c for c in celdas_ok if c[4] >= 0.95]
        print(f"=== {activo}#{marco} ({len(celdas_ok)} celdas con n>={N_MIN}) ===")
        if confirmadas:
            # la más pronta (menor restante_s) que ya confirma -- el punto real
            mas_pronta = min(confirmadas, key=lambda c: c[0])
            tb, pb, hits, n, wlo = mas_pronta
            print(f"  🟢 PUNTO DE CONFIRMACIÓN: restante>={tb:.0f}s, precio en "
                  f"[{pb:.2f},{pb+PASO_PRECIO:.2f}) -> hit={hits/n*100:.1f}% "
                  f"wilson95lo={wlo*100:.1f}% (n={n})")
            for tb2, pb2, h2, n2, w2 in sorted(confirmadas):
                if (tb2, pb2) != (tb, pb):
                    print(f"     también confirma: restante>={tb2:.0f}s precio[{pb2:.2f},{pb2+PASO_PRECIO:.2f}) "
                          f"hit={h2/n2*100:.1f}% wilson95lo={w2*100:.1f}% n={n2}")
        else:
            mejor = max(celdas_ok, key=lambda c: c[4])
            tb, pb, hits, n, wlo = mejor
            print(f"  ⏳ aún ninguna celda confirma 95%. Mejor hoy: restante>={tb:.0f}s "
                  f"precio[{pb:.2f},{pb+PASO_PRECIO:.2f}) hit={hits/n*100:.1f}% "
                  f"wilson95lo={wlo*100:.1f}% (n={n})")
        print()


if __name__ == "__main__":
    main()
