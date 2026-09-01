#!/usr/bin/env python3
"""
analisis_sports_crossmercado_eventos.py — 01-Sep, propuesta #6 del backlog
cross-repo (idea_ronda2_propuestas_profundas_27ago / actualizacion_01sep):
correlación entre mercados del MISMO evento deportivo.

Dos preguntas, sobre `data/sports/activity_ws_*.csv` (firehose real de
trades, columna `event_slug` agrupa mercados relacionados, confirmado
01-Sep: 3.421 eventos con >=2 market_slug en 15 días):

1. LEAD-LAG: dentro de un evento con exactamente 2 mercados, ¿el cambio
   de precio de un mercado predice el cambio de precio del otro con
   unos minutos de adelanto? (ej. mercado "partido completo" se mueve
   antes que un mercado de mapa/juego individual del mismo evento, o al
   revés). Series remuestreadas en bins de 5min (mismo timeframe que
   los mercados 5min de cripto), devuelto por diferencia (return), pool
   de TODOS los pares evento-bin con z-score por evento (para no dejar
   que un evento con más varianza domine), correlación de Pearson por
   lag con test de permutación (shuffle del emparejamiento evento-a-evento,
   1000 iteraciones) — nunca un solo evento decide nada.

2. ARBITRAJE DE SUMA: para eventos con EXACTAMENTE 2 mercados cuyo
   market_slug sugiere lados complementarios del mismo partido (heurística:
   2 mercados, cada uno de un solo outcome_index observado, sin sufijo
   -game/-map — la estructura real de "quién gana X" cripto-equivalente),
   ¿la suma de precios de ambos lados se desvía de 1 con margen suficiente
   tras fee=0.05 (confirmado 26-Ago contra gamma-api) para ser explotable?

FEE=0.05 sports (no 0.07 de cripto). Solo lectura de data/sports/ -- no
toca dinero real, no conecta a ningún ejecutor. Salida:
data/shadow/sports_crossmercado_eventos.json
"""
import csv
import glob
import json
import math
import random
import statistics
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
FEE = 0.05
BIN_S = 300  # 5min
N_SHUFFLE = 1000
LAGS = range(-3, 4)  # -15min..+15min en bins de 5min
OUT = REPO / "data" / "shadow" / "sports_crossmercado_eventos.json"


def parse_ts(s):
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()
    except Exception:
        return None


def cargar_filas(dias=15):
    archivos = sorted(glob.glob(str(REPO / "data" / "sports" / "activity_ws_*.csv")))[-dias:]
    por_evento = defaultdict(lambda: defaultdict(list))  # event_slug -> market_slug -> [(ts, price)]
    n_rows = 0
    for fn in archivos:
        with open(fn, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                ts = parse_ts(r.get("timestamp_utc", ""))
                try:
                    price = float(r.get("price", ""))
                except (TypeError, ValueError):
                    continue
                if ts is None or not (0.0 < price < 1.0):
                    continue
                por_evento[r.get("event_slug", "")][r.get("market_slug", "")].append((ts, price))
                n_rows += 1
    print(f"[cross_eventos] {n_rows} filas, {len(por_evento)} eventos ({len(archivos)} dias)")
    return por_evento


def resample(puntos, bin_s):
    """Lista (ts,price) -> dict bin_idx -> ultimo precio del bin."""
    puntos.sort()
    out = {}
    for ts, p in puntos:
        out[int(ts // bin_s)] = p  # se queda con el ultimo trade del bin
    return out


def serie_returns(bins_dict):
    """dict bin_idx->precio (con huecos) -> dict bin_idx->return, solo bins consecutivos reales."""
    idxs = sorted(bins_dict)
    rets = {}
    for a, b in zip(idxs, idxs[1:]):
        if b - a == 1:
            rets[b] = bins_dict[b] - bins_dict[a]
    return rets


def analizar_leadlag(por_evento):
    """Pool de pares (evento, lag) -> lista de (r_a, r_b_lag) con z-score por evento."""
    pool_por_lag = {lag: [] for lag in LAGS}
    n_eventos_usados = 0
    for event_slug, mercados in por_evento.items():
        if len(mercados) != 2:
            continue
        (slug_a, puntos_a), (slug_b, puntos_b) = list(mercados.items())
        if len(puntos_a) < 20 or len(puntos_b) < 20:
            continue
        bins_a = resample(puntos_a, BIN_S)
        bins_b = resample(puntos_b, BIN_S)
        ra = serie_returns(bins_a)
        rb = serie_returns(bins_b)
        if len(ra) < 8 or len(rb) < 8:
            continue
        # z-score por evento para no dejar que un evento con mas varianza domine el pool
        va = list(ra.values())
        vb = list(rb.values())
        sa = statistics.pstdev(va) or 1e-9
        sb = statistics.pstdev(vb) or 1e-9
        ma = statistics.fmean(va)
        mb = statistics.fmean(vb)
        usado_este_evento = False
        for lag in LAGS:
            for idx, r_a in ra.items():
                idx_b = idx + lag
                if idx_b in rb:
                    za = (r_a - ma) / sa
                    zb = (rb[idx_b] - mb) / sb
                    pool_por_lag[lag].append((za, zb, event_slug))
                    usado_este_evento = True
        if usado_este_evento:
            n_eventos_usados += 1

    resultado = {}
    for lag in LAGS:
        muestras = pool_por_lag[lag]
        n = len(muestras)
        if n < 40:
            resultado[lag] = {"n": n, "veredicto": "n_insuficiente"}
            continue
        xs = [m[0] for m in muestras]
        ys = [m[1] for m in muestras]
        r_obs = _pearson(xs, ys)
        eventos_lista = [m[2] for m in muestras]
        distintos = sorted(set(eventos_lista))
        idx_evento = {e: i for i, e in enumerate(distintos)}
        # permutacion en BLOQUE por evento (evita inflar falsos positivos
        # por autocorrelacion dentro del mismo evento, mismo criterio que
        # el resto del proyecto -- CLAUDE.md feedback_shuffle_antes_de_bloquear)
        ys_por_evento = defaultdict(list)
        for x, y, e in muestras:
            ys_por_evento[e].append(y)
        conteo_mayor_igual = 0
        rng = random.Random(42)
        for _ in range(N_SHUFFLE):
            orden = distintos[:]
            rng.shuffle(orden)
            mapa = dict(zip(distintos, orden))
            ys_perm = []
            for x, y, e in muestras:
                pool_e = ys_por_evento[mapa[e]]
                ys_perm.append(pool_e[rng.randrange(len(pool_e))])
            r_perm = _pearson(xs, ys_perm)
            if abs(r_perm) >= abs(r_obs):
                conteo_mayor_igual += 1
        p_shuffle = (conteo_mayor_igual + 1) / (N_SHUFFLE + 1)
        resultado[lag] = {
            "n": n, "n_eventos": len(distintos), "r": round(r_obs, 4),
            "p_shuffle": round(p_shuffle, 4),
            "veredicto": "confirmado" if (p_shuffle < 0.05 and n >= 40) else "sin_concluir",
        }
    return resultado, n_eventos_usados


def _pearson(xs, ys):
    n = len(xs)
    if n < 2:
        return 0.0
    mx = statistics.fmean(xs)
    my = statistics.fmean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    dy = math.sqrt(sum((y - my) ** 2 for y in ys))
    if dx == 0 or dy == 0:
        return 0.0
    return num / (dx * dy)


def analizar_arb_suma(por_evento):
    """Eventos de 2 mercados sin sufijo -game/-map (heurística de lados
    complementarios del mismo partido) -- deviación de suma de precios vs 1."""
    desviaciones = []
    n_snapshots_explotables = 0
    for event_slug, mercados in por_evento.items():
        if len(mercados) != 2:
            continue
        slugs = list(mercados.keys())
        if any(suf in s for s in slugs for suf in ("-game", "-map")):
            continue
        (slug_a, puntos_a), (slug_b, puntos_b) = list(mercados.items())
        bins_a = resample(puntos_a, BIN_S)
        bins_b = resample(puntos_b, BIN_S)
        comunes = sorted(set(bins_a) & set(bins_b))
        for idx in comunes:
            p_a, p_b = bins_a[idx], bins_b[idx]
            suma = p_a + p_b
            desviaciones.append(suma - 1.0)
            # explotable si el margen tras fee es positivo. /code-review
            # 01-Sep: la fórmula original (coste=suma*(1+FEE)) cobraba fee
            # proporcional al PRECIO pagado -- el fee real de Polymarket
            # (verificado en sports_resolve.py/analisis_sports_wallet_mirror_
            # gate_bucket_26ago.py contra fee_eur real) es proporcional a
            # (1-precio), cobrado solo sobre la pata que GANA al resolver
            # (el $1 de payout), no sobre lo que se paga por comprar. Al
            # comprar ambas patas no se sabe cuál ganará -- se usa el caso
            # peor (fee más alto = precio más bajo de las dos) para no
            # sobreestimar explotabilidad.
            coste = suma + FEE * (1 - min(p_a, p_b))
            if coste < 1.0:
                n_snapshots_explotables += 1
    n = len(desviaciones)
    if n < 40:
        return {"n": n, "veredicto": "n_insuficiente"}
    media = statistics.fmean(desviaciones)
    sd = statistics.pstdev(desviaciones) or 1e-9
    # t-test de una muestra contra 0, aproximado por bootstrap simple
    rng = random.Random(7)
    boot = []
    for _ in range(1000):
        muestra = [desviaciones[rng.randrange(n)] for _ in range(n)]
        boot.append(statistics.fmean(muestra))
    boot.sort()
    ci90 = (boot[int(0.05 * len(boot))], boot[int(0.95 * len(boot))])
    return {
        "n": n,
        "pct_snapshots_explotables_tras_fee": round(n_snapshots_explotables / n * 100, 2),
        "media_desviacion_suma_vs_1": round(media, 4),
        "ci90_bootstrap": [round(ci90[0], 4), round(ci90[1], 4)],
        "veredicto": "confirmado" if (ci90[0] > 0 or ci90[1] < 0) else "sin_concluir",
    }


def main():
    por_evento = cargar_filas()
    leadlag, n_eventos_leadlag = analizar_leadlag(por_evento)
    arb = analizar_arb_suma(por_evento)
    salida = {
        "generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "n_eventos_totales": len(por_evento),
        "n_eventos_usados_leadlag": n_eventos_leadlag,
        "leadlag_por_lag_bins5min": {str(k): v for k, v in leadlag.items()},
        "arb_suma_complementaria": arb,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(salida, f, indent=2, ensure_ascii=False)
    print(json.dumps(salida, indent=2, ensure_ascii=False))
    print(f"[cross_eventos] -> {OUT}")


if __name__ == "__main__":
    main()
