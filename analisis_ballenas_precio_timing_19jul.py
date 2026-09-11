"""Continuación directa de analisis_ballenas_quarter_hour_19jul.py (19-Jul):
la fuerza del burst de apertura NO explica el win-rate de las ballenas
(resultado nulo). Este script muestra qué SÍ lo explica, con números
frescos sobre el mismo dataset (marco 5m/15m, ballenas_timing_history.csv):
precio de entrada (¿favorito confirmado, precio>=0.7?) y timing dentro de
la ventana (¿tardío?) -- el mecanismo ya conocido en el proyecto
(FAVORITO_CONFIRMADO, ballenas_observer.py) pero mostrado explícito aquí,
desagregado por activo, sobre el mismo corte de datos que ya se usó para
el cruce del quarter-hour effect.

Puramente de lectura -- no escribe nada en data/, no toca ninguna estrategia.
Uso: python3 analisis_ballenas_precio_timing_19jul.py
"""
import csv
from collections import defaultdict

HISTORY = "data/shadow/ballenas_timing_history.csv"
MARCOS = {"5m", "15m"}

BUCKETS_PRECIO = [
    (0.0, 0.5, "underdog <0.5"),
    (0.5, 0.7, "mild [0.5,0.7)"),
    (0.7, 0.9, "favorito [0.7,0.9)"),
    (0.9, 1.01, "casi-cierto >=0.9"),
]


def bucket_precio(p):
    for lo, hi, nombre in BUCKETS_PRECIO:
        if lo <= p < hi:
            return nombre
    return None


def bucket_timing(marco, restante_min):
    # umbrales aproximados a las bandas ya calibradas en ballenas_timing_state.json
    tope = 15 if marco == "15m" else 5
    frac = restante_min / tope
    if frac < 0.2:
        return "tardio (<20% ventana)"
    elif frac < 0.5:
        return "medio (20-50%)"
    else:
        return "temprano (>50%)"


def main():
    # (marco, activo) -> {(bucket_precio, bucket_timing): [n, win]}
    datos = defaultdict(lambda: defaultdict(lambda: [0, 0]))

    with open(HISTORY, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            marco = row["marco"]
            if marco not in MARCOS:
                continue
            try:
                precio = float(row["precio"])
                restante_min = float(row["restante_min"])
                acierto = int(row["acierto"])
            except (ValueError, KeyError):
                continue
            bp = bucket_precio(precio)
            bt = bucket_timing(marco, restante_min)
            if bp is None:
                continue
            d = datos[(marco, row["activo"])][(bp, bt)]
            d[0] += 1
            d[1] += acierto

    for marco in ("15m", "5m"):
        for (m, activo), celdas in sorted(datos.items()):
            if m != marco:
                continue
            print(f"\n=== {marco} {activo} ===")
            print(f"  {'precio':<20} {'timing':<22} {'n':>7} {'win%':>7}")
            total_n = sum(v[0] for v in celdas.values())
            for bp_nombre in [b[2] for b in BUCKETS_PRECIO]:
                for bt_nombre in ["temprano (>50%)", "medio (20-50%)", "tardio (<20% ventana)"]:
                    n, win = celdas.get((bp_nombre, bt_nombre), [0, 0])
                    if n < 15:
                        continue
                    hit = win / n * 100
                    print(f"  {bp_nombre:<20} {bt_nombre:<22} {n:>7} {hit:>6.1f}%")
            print(f"  (total filas en este activo/marco: {total_n})")


if __name__ == "__main__":
    main()
