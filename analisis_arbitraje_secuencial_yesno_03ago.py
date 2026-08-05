#!/usr/bin/env python3
"""
analisis_arbitraje_secuencial_yesno_03ago.py — prueba la hipótesis nueva
(petición Javi 03-Ago, tras revisar idea_arbitraje_yes_no_wallets_
expertas_30jul): las wallets expertas que arbitran YES+NO NO compran los
dos lados simultáneamente (mediana 49s de diferencia, hallazgo 5 de esa
memoria) -- box_builder_fase0.py sí exige simultaneidad (ask_yes+ask_no
del MISMO snapshot), lo que explica por qué solo 1/56 eventos detectados
tenía profundidad en ambos lados a la vez (arbitraje "de papel").

Pregunta: ¿el mínimo de ask_yes y el mínimo de ask_no DENTRO de una
ventana de ~90s (aunque no coincidan en el mismo instante) suman menos
que el umbral rentable (~0.95-0.96 con fee) más a menudo que exigir
ambos mínimos en el MISMO tick? Si sí, confirma que el mecanismo real es
"comprar cada pata en su momento barato", no "comprar las dos a la vez".

Fuente: /root/polymarket-research-datalogs/libro_ambos_lados_YYYY-MM-DD.csv
(solo precios, sin profundidad -- esto mide si el fenómeno de PRECIO
existe, no si es ejecutable; la profundidad hay que seguir midiéndola con
box_builder_fase0.py aparte). Solo lectura.
"""
import csv
import glob
from collections import defaultdict

UMBRAL_RENTABLE = 0.96
VENTANA_S = 90
# Filtros anti-artefacto (03-Ago, corrección tras 1er resultado espurio
# 87.5%): cerca de la resolución el lado perdedor cae hacia 0 de forma
# NORMAL (el mercado ya se decidió), no es arbitraje de spread -- sin
# estos filtros, cualquier mercado direccional "parece" arbitrable
# combinando el mínimo histórico de cada lado por separado.
RESTANTE_MIN_S = 120       # excluir ticks a <2min del cierre (colapso de certeza)
PRECIO_FLOOR = 0.03        # ambos lados deben seguir "vivos" (no cerca de 0)

FILES = sorted(glob.glob("/root/polymarket-research-datalogs/libro_ambos_lados_*.csv"))[-3:]


def cargar():
    por_mercado = defaultdict(list)
    for path in FILES:
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                try:
                    ts = row["timestamp_utc"]
                    ay = float(row["ask_yes"]) if row["ask_yes"] else None
                    an = float(row["ask_no"]) if row["ask_no"] else None
                    restante = float(row["restante_s"]) if row["restante_s"] else None
                except (ValueError, KeyError):
                    continue
                if ay is None or an is None or restante is None:
                    continue
                # filtro anti-artefacto: excluir ticks ya cerca de la
                # resolución o con un lado prácticamente muerto
                if restante < RESTANTE_MIN_S:
                    continue
                if ay < PRECIO_FLOOR or an < PRECIO_FLOOR:
                    continue
                por_mercado[(row["market_id"], row["activo"], row["marco"])].append((ts, ay, an))
    return por_mercado


def _parse_ts(ts: str) -> float:
    from datetime import datetime
    return datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp()


def main():
    datos = cargar()
    n_mercados = 0
    n_simultaneo_rentable = 0
    n_secuencial_rentable = 0
    ejemplos = []

    for (mid, activo, marco), filas in datos.items():
        if len(filas) < 3:
            continue
        n_mercados += 1
        filas_ts = [(_parse_ts(ts), ay, an) for ts, ay, an in filas]
        filas_ts.sort()

        # simultáneo: mínimo de (ay+an) en el mismo tick, en toda la vida del mercado
        min_sum_simultaneo = min(ay + an for _, ay, an in filas_ts)
        if min_sum_simultaneo < UMBRAL_RENTABLE:
            n_simultaneo_rentable += 1

        # secuencial: para cada tick de referencia, min ay en ventana + min an en
        # la MISMA ventana (no necesariamente el mismo tick)
        mejor_secuencial = 999.0
        for i, (t0, _, _) in enumerate(filas_ts):
            ventana = [(t, ay, an) for t, ay, an in filas_ts if t0 <= t <= t0 + VENTANA_S]
            if len(ventana) < 2:
                continue
            min_ay = min(ay for _, ay, _ in ventana)
            min_an = min(an for _, _, an in ventana)
            suma = min_ay + min_an
            if suma < mejor_secuencial:
                mejor_secuencial = suma
        if mejor_secuencial < UMBRAL_RENTABLE:
            n_secuencial_rentable += 1
            if len(ejemplos) < 8 and mejor_secuencial < min_sum_simultaneo - 0.01:
                ejemplos.append((activo, marco, mid, round(min_sum_simultaneo, 4), round(mejor_secuencial, 4)))

    print(f"Mercados analizados (>=3 ticks): {n_mercados}")
    print(f"Rentables exigiendo simultaneidad (mismo tick, umbral<{UMBRAL_RENTABLE}): "
          f"{n_simultaneo_rentable} ({n_simultaneo_rentable/n_mercados*100:.1f}%)")
    print(f"Rentables permitiendo secuencial (ventana {VENTANA_S}s, umbral<{UMBRAL_RENTABLE}): "
          f"{n_secuencial_rentable} ({n_secuencial_rentable/n_mercados*100:.1f}%)")
    print(f"\nDiferencia: secuencial encuentra {n_secuencial_rentable - n_simultaneo_rentable} "
          f"mercados rentables MÁS que simultáneo "
          f"({(n_secuencial_rentable - n_simultaneo_rentable)/n_mercados*100:.1f}pp)")

    if ejemplos:
        print("\nEjemplos donde secuencial mejora claramente sobre simultáneo:")
        print(f"{'activo':>6} {'marco':>6} {'market_id':>10} {'sum_simult':>11} {'sum_secuencial':>15}")
        for a, m, mid, s1, s2 in ejemplos:
            print(f"{a:>6} {m:>6} {mid:>10} {s1:>11} {s2:>15}")


if __name__ == "__main__":
    main()
