"""Cruce (19-Jul, petición Javi): ¿el win-rate de las ballenas es mayor
cuando el mercado en el que operan ABRE en una marca "fuerte" del
quarter-hour effect (minuto 0/30, burst mecánico confirmado más intenso en
[[idea_quarter_hour_effect_confirmado_19jul]]) que cuando abre en una marca
"débil" (15/45, u otro minuto cualquiera para marco=5m)?

Solo tiene sentido para marco=15m (abre exactamente en 0/15/30/45, hay
contraste real) y marco=5m (abre en cualquiera de los 12 slots de 5min por
hora, hay contraste real). marco=60m/240m/weekly siempre abren en minuto 0
-- sin variación interna que comparar, se excluyen.

Metodología: reconstruir open_time = ts_trade + restante_min*60s -
duracion_marco*60s (ts_trade + restante_min ya da el cierre del mercado).
Bucketizar por minuto-de-apertura y comparar acierto (win-rate de la
apuesta de esa ballena) por activo -- desagregado, nunca agregado
(feedback_desagregar_por_activo_siempre).

Puramente de lectura -- no escribe nada en data/, no toca ninguna estrategia.
Uso: python3 analisis_ballenas_quarter_hour_19jul.py
"""
import csv
from collections import defaultdict
from datetime import datetime, timedelta, timezone

HISTORY = "data/shadow/ballenas_timing_history.csv"
DURACION_MARCO = {"5m": 5, "15m": 15}  # 60m/240m/weekly excluidos (sin variación interna)
MARCAS_FUERTES_15M = {0, 30}
MARCAS_DEBILES_15M = {15, 45}
MARCAS_FUERTES_5M = {0, 15, 30, 45}


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def procesar():
    # (marco, activo) -> {"fuerte": [n,win], "debil": [n,win]}
    datos = defaultdict(lambda: {"fuerte": [0, 0], "debil": [0, 0]})

    with open(HISTORY, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            marco = row["marco"]
            if marco not in DURACION_MARCO:
                continue
            try:
                ts_trade = parse_ts(row["ts_trade"])
                restante_min = float(row["restante_min"])
                acierto = int(row["acierto"])
            except (ValueError, KeyError):
                continue
            cierre = ts_trade + timedelta(minutes=restante_min)
            apertura = cierre - timedelta(minutes=DURACION_MARCO[marco])
            minuto = apertura.minute

            if marco == "15m":
                if minuto in MARCAS_FUERTES_15M:
                    cat = "fuerte"
                elif minuto in MARCAS_DEBILES_15M:
                    cat = "debil"
                else:
                    continue  # no debería pasar para 15m, pero por si acaso
            else:  # 5m
                cat = "fuerte" if minuto in MARCAS_FUERTES_5M else "debil"

            d = datos[(marco, row["activo"])][cat]
            d[0] += 1
            d[1] += acierto

    return datos


def main():
    datos = procesar()
    print(f"{'marco':<6} {'activo':<6} {'fuerte n/win%':<16} {'debil n/win%':<16} {'gap_pp':>8}")
    print("-" * 60)
    resumen = []
    for marco in ("15m", "5m"):
        for (m, activo), cats in sorted(datos.items()):
            if m != marco:
                continue
            nf, wf = cats["fuerte"]
            nd, wd = cats["debil"]
            if nf < 15 or nd < 15:
                print(f"{marco:<6} {activo:<6} n insuficiente (fuerte={nf}, debil={nd})")
                continue
            hitf = wf / nf * 100
            hitd = wd / nd * 100
            gap = hitf - hitd
            print(f"{marco:<6} {activo:<6} n={nf:>6} {hitf:5.1f}%      n={nd:>6} {hitd:5.1f}%      {gap:+.1f}pp")
            resumen.append((marco, activo, nf, hitf, nd, hitd, gap))

    print("\n=== Resumen ordenado por |gap| ===")
    for marco, activo, nf, hitf, nd, hitd, gap in sorted(resumen, key=lambda r: -abs(r[6])):
        print(f"{marco:<6} {activo:<6} fuerte={hitf:5.1f}% (n={nf})  debil={hitd:5.1f}% (n={nd})  gap={gap:+.1f}pp")


if __name__ == "__main__":
    main()
