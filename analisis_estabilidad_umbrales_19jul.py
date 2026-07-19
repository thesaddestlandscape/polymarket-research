"""Verificación (19-Jul, petición Javi tras un tuit sobre optimización de
parámetros): shadow_postmortem.py::aprender_patrones_causales() prueba SOLO
5 percentiles candidatos (0.25/0.33/0.50/0.66/0.75) y se queda con el que
maximiza el IC observado -- sin comprobar si los umbrales VECINOS muestran
un efecto similar (estabilidad) o si es un pico aislado (sobreajuste).
Estos patrones alimentan kelly_boost, que SÍ afecta stake real en tuplas
live (FAVORITO_CONFIRMADO#SOL#15min, GBM_LATE_15M#{ETH,SOL}#15min, todas
en pares_permitidos_live).

Este script re-barre un grid FINO (cada 5%, 0.05 a 0.95) alrededor de
umbrales ya descubiertos y en producción, replicando la misma lógica de
_evaluar_bucket, para ver si el IC es una meseta estable o un pico aislado.

Puramente de lectura -- no escribe nada en data/, no toca ninguna estrategia.
Uso: python3 analisis_estabilidad_umbrales_19jul.py
"""
import csv
import json

RESULTS = "data/shadow/results.csv"

# (strategy, subtype, direction, feature, condicion, umbral_descubierto, n_original)
CASOS = [
    ("GBM_LATE_15M", "ETH#15min", "BUY_YES", "dist_vwap_pct", "gt", 0.8259, 19),
    ("GBM_LATE_15M", "ETH#15min", "BUY_YES", "sigma_ewma_delta_pct", "gt", 7.253, 75),
    ("GBM_LATE_15M", "SOL#15min", "BUY_YES", "sigma_ewma_delta_pct", "gt", 5.326, 91),
    ("FAVORITO_CONFIRMADO", "SOL#15min", "BUY_YES", "py_entrada", "gt", 0.675, 203),
    ("FAVORITO_CONFIRMADO", "SOL#15min", "BUY_YES", "hora_utc", "gt", 18.0, 104),
]

PERCENTILES_FINOS = [round(0.05 * i, 2) for i in range(1, 20)]  # 0.05..0.95
N_MIN_PARA_MOSTRAR = 10


def cargar_datos(strategy, subtype, direction, feature):
    vals = []
    with open(RESULTS, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["strategy"] != strategy or row["subtype"] != subtype or row["decision"] != direction:
                continue
            try:
                feats = json.loads(row["features"])
            except (json.JSONDecodeError, TypeError):
                continue
            v = feats.get(feature)
            if v is None:
                continue
            try:
                v = float(v)
            except (ValueError, TypeError):
                continue
            vals.append((int(row["acierto"]), v))
    return vals


def evaluar(vals, umbral, condicion):
    if condicion == "gt":
        bueno = [(r, v) for r, v in vals if v > umbral]
    else:  # lt
        bueno = [(r, v) for r, v in vals if v < umbral]
    n = len(bueno)
    if n == 0:
        return n, None
    wins = sum(r for r, _ in bueno)
    ic = (wins + 1) / (n + 2) - 0.5
    return n, ic


def main():
    for strategy, subtype, direction, feature, condicion, umbral_orig, n_orig in CASOS:
        vals = cargar_datos(strategy, subtype, direction, feature)
        print(f"\n=== {strategy}#{subtype} {direction} | {feature} {condicion} "
              f"{umbral_orig} (original: ic reportado, n={n_orig}) ===")
        print(f"  Datos totales disponibles: n={len(vals)}")
        raw_vals = sorted(v for _, v in vals)
        if not raw_vals:
            print("  Sin datos.")
            continue

        curva = []
        for p in PERCENTILES_FINOS:
            idx = int(len(raw_vals) * p)
            umbral = raw_vals[idx] if idx < len(raw_vals) else raw_vals[-1]
            n, ic = evaluar(vals, umbral, condicion)
            curva.append((p, umbral, n, ic))

        print(f"  {'percentil':>9} {'umbral':>10} {'n':>6} {'ic':>8}")
        for p, umbral, n, ic in curva:
            marca = " <-- umbral original~" if abs(umbral - umbral_orig) < max(abs(umbral_orig) * 0.05, 0.01) else ""
            if n < N_MIN_PARA_MOSTRAR:
                print(f"  {p:>9.2f} {umbral:>10.4f} {n:>6} {'(n<10)':>8}{marca}")
            else:
                print(f"  {p:>9.2f} {umbral:>10.4f} {n:>6} {ic:>+8.4f}{marca}")


if __name__ == "__main__":
    main()
