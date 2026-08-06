#!/usr/bin/env python3
"""analisis_gate_microbucket_nunca_live.py — Protocolo: aplicar el gate
riguroso por micro-bucket de precio (analisis_gate_microbucket_precio.py,
fuente (b) data/markets/) a TODAS las tuplas candidatas que NUNCA han
estado en pares_permitidos_live, en un único barrido.

Origen (06-Ago, petición explícita Javi tras recuperar
GBM_LATE_15M_PYCONFIRMADO#XRP de Obsidian): "esto tenemos que hacerlo con
todas las que no hayan estado nunca en live, tiene que ser protocolo" —
no repetir el análisis manual tupla a tupla, generalizarlo.

Por qué un script aparte y no repetir analisis_gate_microbucket_precio.py
con --activo-markets en un bucle: ese script relee las 50 capturas de
data/markets/ (7.9GB, 6.6M filas) desde cero en CADA invocación
(~200s+, ya dio timeout con una sola tupla) — para cientos de tuplas
haría falta un solo pase.

Diseño: UN solo pase por data/markets/*.csv, agrupando en memoria por
(activo,duracion_min) -> {market_id: [(ts, py), ...]} ordenado. Después,
por cada tupla nunca-viva, se deriva su umbral operativo real desde su
PROPIO results.csv (percentil de precio_yes_mercado que usa al disparar
-- BUY_YES: p10 como umbral 'ge'; BUY_NO: p90 como umbral 'le', reflejando
la zona de precio donde la estrategia realmente entra) y se busca el
PRIMER cruce de ese umbral en la serie cacheada (nunca el precio final,
mismo principio anti-look-ahead que el script base). Solo se procesan
tuplas con marco estándar Up/Down (5/15/60/240min) -- 'atexpiry'/'daily'/
'reach'/'sniper' no tienen ese formato de pregunta y se listan aparte
como no-cubiertas.

Solo lectura -- no toca config ni dinero. Escribe
data/shadow/gate_microbucket_nunca_live.json.
"""
import csv
import glob
import gzip
import json
import math
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

csv.field_size_limit(10_000_000)
REPO = Path(__file__).resolve().parent
FEE = 0.07
ACTIVOS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
DURACIONES = [5, 15, 60, 240]

RE_RANGE = re.compile(r' - .+?, (\d+):(\d+)(AM|PM)-(\d+):(\d+)(AM|PM) ET')
RE_HOUR = re.compile(r' - .+?, (\d+)(AM|PM) ET$')


def _duracion_min(pregunta):
    m = RE_RANGE.search(pregunta)
    if m:
        h1, m1, ap1, h2, m2, ap2 = m.groups()
        h1, m1, h2, m2 = int(h1), int(m1), int(h2), int(m2)
        t1 = (h1 % 12) * 60 + m1 + (720 if ap1 == 'PM' else 0)
        t2 = (h2 % 12) * 60 + m2 + (720 if ap2 == 'PM' else 0)
        d = t2 - t1
        return d + 1440 if d <= 0 else d
    if RE_HOUR.search(pregunta):
        return 60
    return None


def _activo_de_pregunta(q):
    for a in ACTIVOS:
        if f'{a.capitalize()} Up or Down' in q or a in q.upper():
            return a
    return None


def cargar_series_markets():
    """Un solo pase: (activo,duracion) -> {market_id: [(ts_dt, py), ...] ordenado}."""
    series = {(a, d): {} for a in ACTIVOS for d in DURACIONES}
    archivos = sorted(glob.glob(str(REPO / "data/markets/*.csv")) +
                       glob.glob(str(REPO / "data/markets/*.csv.gz")))
    total_filas = 0
    for arch in archivos:
        opener = gzip.open if arch.endswith('.gz') else open
        try:
            with opener(arch, 'rt', encoding='utf-8', errors='replace') as f:
                reader = csv.reader(f)
                header = next(reader)
                idx = {name: j for j, name in enumerate(header)}
                i_ts, i_mid = idx['timestamp_utc'], idx['market_id']
                i_q, i_ed, i_py = idx['question'], idx['end_date'], idx['price_yes']
                for row in reader:
                    total_filas += 1
                    try:
                        q = row[i_q]
                        activo = _activo_de_pregunta(q)
                        if activo is None:
                            continue
                        dur = _duracion_min(q)
                        if dur not in DURACIONES:
                            continue
                        py_raw = row[i_py]
                        if not py_raw:
                            continue
                        py = float(py_raw)
                        ed = row[i_ed]
                        ed_dt = datetime.fromisoformat(ed.replace('Z', '+00:00')) if 'T' in ed else None
                        if ed_dt is None:
                            continue
                        if ed_dt.tzinfo is None:
                            ed_dt = ed_dt.replace(tzinfo=timezone.utc)
                        ts_dt = datetime.fromisoformat(row[i_ts].replace('Z', '+00:00'))
                        if ts_dt > ed_dt:
                            continue
                        series[(activo, dur)].setdefault(row[i_mid], []).append((ts_dt, py))
                    except Exception:
                        continue
        except Exception as e:
            print(f"  aviso: no se pudo leer {arch}: {e}", file=sys.stderr)
    for key in series:
        for mid in series[key]:
            series[key][mid].sort(key=lambda t: t[0])
    print(f"cargar_series_markets: {total_filas} filas totales procesadas, "
          f"{sum(len(v) for v in series.values())} series (activo,duracion,market) construidas")
    return series


def _outcomes_todas_estrategias():
    outcomes = {}
    with open(REPO / "data/shadow/results.csv") as f:
        for row in csv.DictReader(f):
            mid = row.get('market_id')
            o = row.get('outcome_real')
            if mid and o in ('YES', 'NO'):
                outcomes[mid] = o
    return outcomes


def _poblacion_propia(strategy, subtype, decision):
    rows = []
    with open(REPO / "data/shadow/results.csv") as f:
        for row in csv.DictReader(f):
            if (row.get('strategy') != strategy or row.get('subtype') != subtype
                    or row.get('decision') != decision):
                continue
            try:
                rows.append(float(row['precio_yes_mercado']))
            except Exception:
                continue
    return rows


def _primer_cruce(series_market, umbral, direccion):
    for ts, py in series_market:
        if direccion == 'ge' and py >= umbral:
            return py, ts
        if direccion == 'le' and py <= umbral:
            return py, ts
    return None


def _pnl_desde_cruce(mercados_cruce, outcomes, decision):
    rows = []
    for mid, (py, ts) in mercados_cruce.items():
        o = outcomes.get(mid)
        if o is None:
            continue
        if decision == 'BUY_NO':
            price_paid, gano = 1 - py, (o == 'NO')
        else:
            price_paid, gano = py, (o == 'YES')
        if not (0 < price_paid < 1):
            continue
        gross = (1 - price_paid) / price_paid if gano else -1.0
        net = gross - FEE * (1 - price_paid)
        rows.append((py, net))
    return rows


def _gate(py_arr, pnl_arr, lo, hi, rng, n_min_gate=40, iters=400):
    mask = (py_arr >= lo) & (py_arr < hi)
    n = int(mask.sum())
    if n < 15:
        return None
    pnls = pnl_arr[mask]
    wins = int(np.sum(pnls > 0))
    hit_rate = wins / n
    pnl_medio = float(pnls.mean())
    z = 1.645
    p_ = wins / n
    denom = 1 + z * z / n
    center = p_ + z * z / (2 * n)
    margin = z * math.sqrt(p_ * (1 - p_) / n + z * z / (4 * n * n))
    wlo = (center - margin) / denom
    boot_idx = rng.integers(0, n, size=(iters, n))
    boot_means = pnls[boot_idx].mean(axis=1)
    boot_lo, boot_hi = np.percentile(boot_means, [5, 95])
    rest = pnl_arr[~mask]
    if len(rest) == 0:
        pval = 1.0
    else:
        obs_diff = pnls.mean() - rest.mean()
        combo = np.concatenate([pnls, rest])
        diffs = np.empty(iters)
        for i in range(iters):
            perm = rng.permutation(combo)
            diffs[i] = perm[:n].mean() - perm[n:].mean()
        pval = float((diffs >= obs_diff).mean() if obs_diff >= 0 else (diffs <= obs_diff).mean())
    half = n // 2
    first = float(pnls[:half].mean()) if half else None
    second = float(pnls[half:].mean()) if (n - half) else None
    consistente = (first is not None and ((first >= 0 and second >= 0) or (first < 0 and second < 0)))
    gate_ok = (n >= n_min_gate and (boot_lo > 0 or boot_hi < 0) and pval < 0.05 and consistente)
    veredicto = ("GATE_OK_BUENO" if (gate_ok and pnl_medio > 0) else
                 "GATE_OK_MALO" if (gate_ok and pnl_medio < 0) else "sin_concluir")
    return {"n": n, "hit": round(hit_rate, 4), "wilson_lo": round(wlo, 4),
            "pnl_medio": round(pnl_medio, 4), "boot90": [round(float(boot_lo), 4), round(float(boot_hi), 4)],
            "p_shuffle": round(pval, 4), "split": [first, second], "veredicto": veredicto}


def main():
    # 06-Ago (hallazgo /code-review): `estrategias_alguna_vez_live.json` es
    # a propósito granularidad FAMILIA (ver bootstrap_alguna_vez_live.py,
    # mismo criterio que ACUMULAR_SHADOW_AUNQUE_DESACTIVADA) -- filtrar por
    # ahí aquí excluía de golpe cualquier tupla de una familia con OTRA
    # tupla ya viva, aunque esa tupla exacta nunca lo hubiera estado (~37%
    # de candidatos_evaluacion_live, confirmado). Este script necesita la
    # tupla exacta, no la familia -- usa tuplas_alguna_vez_live.json.
    tuplas_path = REPO / "data/live/tuplas_alguna_vez_live.json"
    if not tuplas_path.exists():
        sys.exit("data/live/tuplas_alguna_vez_live.json no existe -- correr "
                 "bootstrap_alguna_vez_live.py primero (genera ambos ficheros).")
    tuplas_alguna_vez_live = set(json.loads(tuplas_path.read_text()))
    config = json.loads((REPO / "data/live/config_live.json").read_text())
    candidatos = set(config.get("candidatos_evaluacion_live", []))

    nunca_live = []
    no_cubiertas = []
    for t in sorted(candidatos):
        parts = t.split('#')
        if len(parts) != 4:
            continue
        strat, activo, marco, decision = parts
        if t in tuplas_alguna_vez_live:
            continue
        m = re.match(r'(\d+)min$', marco)
        if not m or activo not in ACTIVOS:
            no_cubiertas.append(t)
            continue
        dur = int(m.group(1))
        if dur not in DURACIONES:
            no_cubiertas.append(t)
            continue
        nunca_live.append((strat, activo, f"{activo}#{marco}", dur, decision))

    print(f"{len(candidatos)} candidatos totales, {len(nunca_live)} nunca-live con marco estándar cubrible, "
          f"{len(no_cubiertas)} no cubiertas (marco no estándar: {no_cubiertas[:10]}{'...' if len(no_cubiertas) > 10 else ''})")

    print("Cargando data/markets/ (un solo pase, puede tardar varios minutos)...")
    series = cargar_series_markets()
    outcomes = _outcomes_todas_estrategias()
    print(f"{len(outcomes)} outcomes conocidos (todas las estrategias combinadas)")

    rng = np.random.default_rng(42)
    edges = [round(i * 0.05, 2) for i in range(20)] + [1.0]
    resultados = {}

    for strat, activo, subtype, dur, decision in nunca_live:
        clave = f"{strat}#{subtype}#{decision}"
        propia = _poblacion_propia(strat, subtype, decision)
        if len(propia) < 5:
            resultados[clave] = {"estado": "n_propio_insuficiente", "n_propio": len(propia)}
            continue
        propia_arr = np.array(propia)
        # 06-Ago (hallazgo /code-review): la dirección del cruce NO puede
        # derivarse de BUY_YES/BUY_NO -- ese label dice qué lado se compra,
        # no en qué ZONA DE PRECIO entra la estrategia (arquetipo A, ej.
        # GBM_LATE, dispara con py BAJO incluso siendo BUY_YES; arquetipo B,
        # ej. FAVORITO_CONFIRMADO, con py ALTO). Se deriva empíricamente de
        # dónde vive la propia señal (mediana de precio_yes_mercado en
        # results.csv): mediana>=0.5 -> zona alta, cruce al SUBIR (ge) desde
        # su percentil bajo; mediana<0.5 -> zona baja, cruce al BAJAR (le)
        # desde su percentil alto. Mismo principio que --umbral-direccion
        # explícito en analisis_gate_microbucket_precio.py (el script base),
        # que exige este argumento a mano exactamente por este motivo.
        if float(np.median(propia_arr)) >= 0.5:
            umbral, direccion = float(np.percentile(propia_arr, 10)), 'ge'
        else:
            umbral, direccion = float(np.percentile(propia_arr, 90)), 'le'

        serie_key = (activo, dur)
        mercados = series.get(serie_key, {})
        cruces = {}
        for mid, obs in mercados.items():
            r = _primer_cruce(obs, umbral, direccion)
            if r is not None:
                cruces[mid] = r
        rows = _pnl_desde_cruce(cruces, outcomes, decision)
        if len(rows) < 15:
            resultados[clave] = {"estado": "n_markets_insuficiente", "n_propio": len(propia),
                                  "umbral_derivado": round(umbral, 3), "n_markets": len(rows)}
            continue

        py_arr = np.array([r[0] for r in rows])
        pnl_arr = np.array([r[1] for r in rows])
        buckets = {}
        buenos, malos = [], []
        for lo, hi in zip(edges, edges[1:]):
            g = _gate(py_arr, pnl_arr, lo, hi, rng)
            if g is None:
                continue
            buckets[f"[{lo:.2f},{hi:.2f})"] = g
            if g["veredicto"] == "GATE_OK_BUENO":
                buenos.append([lo, hi])
            elif g["veredicto"] == "GATE_OK_MALO":
                malos.append([lo, hi])
        resultados[clave] = {
            "estado": "evaluado", "n_propio": len(propia), "umbral_derivado": round(umbral, 3),
            "direccion_umbral": direccion, "n_markets_total": len(rows),
            "zonas_buenas": buenos, "zonas_malas": malos, "buckets": buckets,
        }
        tag = f"BUENAS={buenos}" if buenos else (f"MALAS={malos}" if malos else "sin_concluir")
        print(f"  {clave}: n_propio={len(propia)} umbral~{umbral:.2f}({direccion}) n_markets={len(rows)} -> {tag}")

    salida = {
        "generado": datetime.now(timezone.utc).isoformat(),
        "no_cubiertas_marco_no_estandar": no_cubiertas,
        "resultados": resultados,
    }
    out_path = REPO / "data/shadow/gate_microbucket_nunca_live.json"
    out_path.write_text(json.dumps(salida, indent=2, ensure_ascii=False))
    print(f"\nEscrito {out_path}")
    n_buenas = sum(1 for r in resultados.values() if r.get("zonas_buenas"))
    n_malas = sum(1 for r in resultados.values() if r.get("zonas_malas") and not r.get("zonas_buenas"))
    print(f"Resumen: {len(resultados)} tuplas evaluadas, {n_buenas} con alguna zona BUENA confirmada, "
          f"{n_malas} solo zonas MALAS, resto sin_concluir/n insuficiente")


if __name__ == "__main__":
    main()
