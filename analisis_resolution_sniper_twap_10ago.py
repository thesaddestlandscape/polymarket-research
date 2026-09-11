#!/usr/bin/env python3
"""analisis_resolution_sniper_twap_10ago.py -- ¿sobrevive el hallazgo de
resolution_sniper_observer.py (sniping de resolución por latencia) al
cambio de régimen TWAP del 07-Ago?

Origen (Hallazgo 1 de project_revision_premisas_y_lista_riesgo_twap_09ago):
resolution_sniper_observer.py calcula `chainlink_direccion_implicita`
comparando un TICK PUNTUAL de Chainlink en cada offset_s contra un tick
puntual de referencia al abrir la ventana (`ref_open`) -- el mecanismo de
resolución VIEJO (snapshot). Desde el 07-Ago, 5min/15min resuelven por TWAP
Chainlink (30s/60s respectivamente, ver project_twap_chainlink_confirmado_09ago)
-- ese tick puntual ya no aproxima bien lo que de verdad decidió el cierre,
así que `chainlink_direccion_implicita`/`acierto_direccion_implicita` (la
columna que analisis_gate_riguroso_resolution_sniper_30jul.py usa para medir
el edge) puede estar sistemáticamente equivocada en datos post-07-Ago para
5min/15min, aunque el outcome_real (ground truth, vía API oficial) siga
siendo correcto.

Recalcula la dirección implícita SOLO para filas post-07-Ago en 5min/15min
usando el mismo proxy TWAP que analisis_regimen_twap_chainlink_09ago.py
(media ponderada por tiempo de los ticks de data/prices/chainlink_*.csv en
[end-ventana, end] vs primer tick al abrir la ventana) y repite el gate
riguroso (Wilson90 + edge + split-half, mismo criterio que
analisis_gate_riguroso_resolution_sniper_30jul.py) comparando ANTES
(snapshot, como está hoy) vs DESPUÉS (TWAP-aware) para las filas afectadas.

Solo lectura -- no toca resolution_sniper_observer.py ni ningún gate real.
"""
import csv
import glob
import gzip
import math
import random
from bisect import bisect_left, bisect_right
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
PRICES_DIR = REPO / "data" / "prices"

FECHA_CAMBIO_TWAP = datetime(2026, 8, 7, tzinfo=timezone.utc)
VENTANA_TWAP_S = {"5min": 30, "15min": 60}
DUR_S = {"5min": 300, "15min": 900}

Z_90 = 1.645
N_MIN = 15
N_SHUFFLE = 2000

_cache_ticks = {}


def _abrir_precios(fecha_str):
    plano = PRICES_DIR / f"chainlink_{fecha_str}.csv"
    gz = PRICES_DIR / f"chainlink_{fecha_str}.csv.gz"
    if plano.exists():
        return open(plano, "r", newline="", encoding="utf-8")
    if gz.exists():
        return gzip.open(gz, "rt", newline="", encoding="utf-8")
    return None


def _cargar_ticks_dia(fecha_str):
    if fecha_str in _cache_ticks:
        return _cache_ticks[fecha_str]
    f = _abrir_precios(fecha_str)
    if f is None:
        _cache_ticks[fecha_str] = {}
        return {}
    ts_por_activo = defaultdict(list)
    px_por_activo = defaultdict(list)
    with f:
        for row in csv.DictReader(f):
            try:
                dt = datetime.fromisoformat(row["timestamp_utc"])
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                ts_por_activo[row["asset"]].append(dt.timestamp())
                px_por_activo[row["asset"]].append(float(row["price_usd"]))
            except (ValueError, KeyError):
                continue
    out = {a: (ts_por_activo[a], px_por_activo[a]) for a in ts_por_activo}
    _cache_ticks[fecha_str] = out
    return out


def _twap_direccion(asset, ts_end, marco):
    """Recalcula 'Up'/'Down' con el proxy TWAP (mismo método que
    analisis_regimen_twap_chainlink_09ago.py), o None si faltan ticks."""
    fecha_str = datetime.fromtimestamp(ts_end, tz=timezone.utc).strftime("%Y-%m-%d")
    ticks = _cargar_ticks_dia(fecha_str)
    par = ticks.get(asset)
    if not par or not par[0]:
        return None
    ts_list, px_list = par
    dur_s = DUR_S[marco]
    ventana_s = VENTANA_TWAP_S[marco]
    start_epoch = ts_end - dur_s

    i0 = bisect_left(ts_list, start_epoch)
    if i0 >= len(ts_list):
        return None
    referencia = px_list[i0]

    lo = ts_end - ventana_s
    k0 = bisect_left(ts_list, lo)
    k1 = bisect_right(ts_list, ts_end)
    if k1 - k0 < 2:
        return None
    ts_v, px_v = ts_list[k0:k1], px_list[k0:k1]
    acumulado = peso_total = 0.0
    for idx in range(len(ts_v) - 1):
        dt_peso = ts_v[idx + 1] - ts_v[idx]
        acumulado += px_v[idx] * dt_peso
        peso_total += dt_peso
    if peso_total <= 0:
        return None
    proxy_twap = acumulado / peso_total
    if proxy_twap == referencia:
        return None
    return "Up" if proxy_twap > referencia else "Down"


def cargar():
    filas = []
    for fn in sorted(glob.glob(str(REPO / "data/shadow/resolution_sniper_obs_*.csv"))):
        with open(fn, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if not r.get("outcome_real") or not r.get("chainlink_direccion_implicita"):
                    continue
                try:
                    offset = int(float(r["offset_s"]))
                    ts_end = int(float(r["ts_end"]))
                except (ValueError, KeyError):
                    continue
                if offset > 2:
                    continue  # mismo corte "accionable" que el gate original
                marco = r["marco"]
                if marco not in VENTANA_TWAP_S:
                    continue
                ask_up = r.get("ask_yes")
                ask_down = r.get("ask_no")
                ts_end_dt = datetime.fromtimestamp(ts_end, tz=timezone.utc)
                post_twap = ts_end_dt >= FECHA_CAMBIO_TWAP
                filas.append({
                    "activo": r["activo"], "marco": marco, "offset": offset,
                    "ts_end": ts_end, "outcome_real": r["outcome_real"],
                    "dir_vieja": r["chainlink_direccion_implicita"],
                    "ask_yes": ask_up, "ask_no": ask_down,
                    "post_twap": post_twap,
                })
    return filas


def _direccion_y_ask(fila, usar_twap):
    if usar_twap and fila["post_twap"]:
        d = _twap_direccion(fila["activo"], fila["ts_end"], fila["marco"])
        if d is None:
            return None, None
    else:
        d = fila["dir_vieja"]
    ask = fila["ask_yes"] if d == "Up" else fila["ask_no"]
    try:
        ask = float(ask)
    except (TypeError, ValueError):
        return None, None
    return d, ask


def wilson_lower(hits, n, z=Z_90):
    if n == 0:
        return 0.0
    p = hits / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centro - margen) / denom


def _gate(filas, usar_twap, etiqueta):
    grupos = defaultdict(list)
    for fila in filas:
        d, ask = _direccion_y_ask(fila, usar_twap)
        if d is None or ask is None:
            continue
        acierto = d == fila["outcome_real"]
        grupos[(fila["activo"], fila["marco"], fila["offset"])].append((acierto, ask, fila["ts_end"]))

    print(f"\n=== {etiqueta} ===")
    print(f"{'activo':<6}{'marco':<7}{'offset':>7}{'n':>6}{'hit%':>8}{'wilson90lo':>12}{'ask_medio':>11}{'edge':>8}")
    resultados = []
    for (activo, marco, offset), grupo in sorted(grupos.items()):
        n = len(grupo)
        if n < N_MIN:
            continue
        hits = sum(1 for a, _, _ in grupo if a)
        hit_rate = hits / n
        wlo = wilson_lower(hits, n)
        ask_medio = sum(a for _, a, _ in grupo) / n
        edge = hit_rate - ask_medio
        grupo_ordenado = sorted(grupo, key=lambda g: g[2])
        mitad = n // 2
        h1, h2 = grupo_ordenado[:mitad], grupo_ordenado[mitad:]
        hit1 = sum(1 for a, _, _ in h1 if a) / len(h1) if h1 else 0
        hit2 = sum(1 for a, _, _ in h2 if a) / len(h2) if h2 else 0
        print(f"{activo:<6}{marco:<7}{offset:>7}{n:>6}{hit_rate*100:>7.1f}%{wlo:>12.3f}{ask_medio:>11.3f}{edge:>+8.3f}"
              f"  split={hit1*100:.0f}%/{hit2*100:.0f}%")
        resultados.append({"activo": activo, "marco": marco, "offset": offset, "n": n,
                            "hit_rate": hit_rate, "wilson90_lo": wlo, "edge": edge,
                            "split1": hit1, "split2": hit2})

    gate_ok = [r for r in resultados if r["wilson90_lo"] > 0.5 and r["edge"] > 0
               and abs(r["split1"] - r["split2"]) < 0.30]
    print(f"GATE OK: {len(gate_ok)} de {len(resultados)} combos evaluados (n>={N_MIN})")
    for r in gate_ok:
        print(f"  {r['activo']}#{r['marco']}#offset={r['offset']}: n={r['n']} "
              f"hit={r['hit_rate']*100:.1f}% wilson90lo={r['wilson90_lo']:.3f} edge={r['edge']:+.3f}")
    return resultados, gate_ok


def main():
    filas = cargar()
    pre = [f for f in filas if not f["post_twap"]]
    post = [f for f in filas if f["post_twap"]]
    print(f"Filas accionables (offset<=2, outcome_real presente): {len(filas)} total "
          f"({len(pre)} pre-TWAP, {len(post)} post-TWAP-07Ago)")

    if pre:
        _gate(pre, usar_twap=False, etiqueta="PRE-07-Ago (snapshot, régimen viejo -- sin cambio)")

    if post:
        _, gate_snapshot = _gate(post, usar_twap=False,
                                  etiqueta="POST-07-Ago con SNAPSHOT (método actual del logger, probablemente sesgado)")
        _, gate_twap = _gate(post, usar_twap=True,
                              etiqueta="POST-07-Ago con TWAP recalculado (método correcto para el régimen nuevo)")
        print(f"\n=== Resumen comparación POST-07-Ago ===")
        print(f"GATE OK con snapshot (método viejo, como está hoy el logger): {len(gate_snapshot)}")
        print(f"GATE OK con TWAP recalculado (método correcto):              {len(gate_twap)}")
    else:
        print("\nSin filas post-07-Ago con outcome_real todavía -- repetir cuando acumule más n.")


if __name__ == "__main__":
    main()
