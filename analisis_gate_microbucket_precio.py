#!/usr/bin/env python3
"""
analisis_gate_microbucket_precio.py — Gate riguroso por micro-bucket de
precio (0.05), reutilizable para cualquier tupla live o candidata a
promoción.

Origen (05-Ago, petición explícita Javi tras 3 pérdidas reales -6.91€ en
BALLENAS_TARDIAS#ETH#5min en zona de precio nunca confirmada, y tras
repetir el mismo proceso a mano para las 2 tuplas FAVORITO_CONFIRMADO
restantes): "cada vez que saquemos una tupla a la whitelist, quiero que
lo hagas igual, así sabemos exactamente en qué micro-buckets tiene que
operar cada tupla para minar pasta" — CLAUDE.md, sección "Barra de
calidad por entregable" lo referencia como paso obligatorio de
promoción/auditoría.

Qué hace:
  1. Reúne la población de trades históricos por micro-bucket de precio
     0.05, con la MEJOR fuente de datos disponible, en este orden:
       (a) results.csv de la tupla exacta (siempre disponible, pero suele
           tener poco n por bucket para estrategias jóvenes).
       (b) Si se pasa --activo-markets, extrae precio-justo-antes-del-
           cierre de TODOS los mercados históricos de ese activo/duración
           desde data/markets/*.csv(.gz) (capturas ~1min desde 16-Jun) y
           cruza el outcome con results.csv de TODAS las estrategias
           combinadas (un mismo market_id lo predicen varias a la vez,
           así que casi siempre hay outcome sin llamar a ninguna API).
           Da órdenes de magnitud más n (705-3253 mercados reales en los
           casos ya hechos, vs 338-422 en el histórico propio).
       (c) Fuente externa específica (ballenas_timing_history.csv u
           otra) -- no automatizado aquí, usar el patrón manual de
           idea_veto_microbucket_ballenas_eth5min_05ago si aplica.
  2. Calcula, por bucket de 0.05: n, hit-rate, Wilson lower bound,
     pnl_neto/trade (fee 7% real, gross_win=(1-p)/p -- NUNCA (1-p), error
     real cometido una vez que invierte el signo del análisis en precios
     bajos), CI90% bootstrap, p-shuffle (permutación bucket-vs-resto),
     consistencia split-half.
  3. Veredicto GATE_OK_BUENO / GATE_OK_MALO / sin_concluir: exige
     n>=40 Y CI90% no cruza cero Y p_shuffle<0.05 Y split-half consistente
     -- las 4 a la vez, igual que el resto de gates del proyecto.

Uso:
  python3 analisis_gate_microbucket_precio.py --strategy FAVORITO_CONFIRMADO \\
      --subtype BTC#60min --decision BUY_NO
  python3 analisis_gate_microbucket_precio.py --strategy BALLENAS_TARDIAS \\
      --subtype ETH#5min --decision BUY_YES \\
      --activo-markets BTC --duracion-min 60   # si hace falta la fuente (b)

Solo lectura, no toca dinero ni config -- imprime la tabla, no decide
nada solo. Cablear el veto resultante en el ejecutor correspondiente
sigue siendo un paso manual deliberado (mismo criterio que gate_bucket_
propio.py: el cálculo no es la aprobación).
"""
import argparse
import csv
import glob
import gzip
import math
import re
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

csv.field_size_limit(10_000_000)
REPO = Path(__file__).resolve().parent
FEE = 0.07

RE_RANGE = re.compile(r' - .+?, (\d+):(\d+)(AM|PM)-(\d+):(\d+)(AM|PM) ET')
RE_HOUR = re.compile(r' - .+?, (\d+)(AM|PM) ET$')


def _duracion_min(pregunta: str) -> int | None:
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


def _outcomes_todas_estrategias() -> dict:
    outcomes = {}
    with open(REPO / "data/shadow/results.csv") as f:
        for row in csv.DictReader(f):
            mid = row.get('market_id')
            o = row.get('outcome_real')
            if mid and o in ('YES', 'NO'):
                outcomes[mid] = o
    return outcomes


def _extraer_desde_markets(activo: str, duracion_min: int) -> dict:
    """market_id -> (py_cerca_del_cierre, timestamp_iso). Precio de la
    última captura ANTES del cierre de cada mercado 'activo Up or Down'
    de la duración pedida, en TODO el histórico de data/markets/."""
    mercados = {}
    archivos = sorted(glob.glob(str(REPO / "data/markets/*.csv")) +
                       glob.glob(str(REPO / "data/markets/*.csv.gz")))
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
                    try:
                        q = row[i_q]
                        if f'{activo.capitalize()} Up or Down' not in q and activo.upper() not in q.upper():
                            continue
                        if _duracion_min(q) != duracion_min:
                            continue
                        mid, ed, ts, py_raw = row[i_mid], row[i_ed], row[i_ts], row[i_py]
                        if not py_raw:
                            continue
                        py = float(py_raw)
                        ed_dt = datetime.fromisoformat(ed.replace('Z', '+00:00')) if 'T' in ed else None
                        if ed_dt is None:
                            continue
                        if ed_dt.tzinfo is None:
                            ed_dt = ed_dt.replace(tzinfo=timezone.utc)
                        ts_dt = datetime.fromisoformat(ts.replace('Z', '+00:00'))
                        if ts_dt > ed_dt:
                            continue
                        prev = mercados.get(mid)
                        if prev is None or ts_dt > prev[1]:
                            mercados[mid] = (py, ts_dt)
                    except Exception:
                        continue
        except Exception as e:
            print(f"  aviso: no se pudo leer {arch}: {e}")
    return mercados


def _cargar_poblacion_resultscsv(strategy: str, subtype: str, decision: str) -> list:
    rows = []
    with open(REPO / "data/shadow/results.csv") as f:
        for row in csv.DictReader(f):
            if (row.get('strategy') != strategy or row.get('subtype') != subtype
                    or row.get('decision') != decision):
                continue
            try:
                py = float(row['precio_yes_mercado'])
                pnl = float(row['pnl_neto'])
                ts = row.get('resolution_timestamp', '')
            except Exception:
                continue
            rows.append((py, pnl, ts))
    return rows


def _pnl_desde_markets(mercados: dict, outcomes: dict, decision: str) -> list:
    rows = []
    for mid, (py, ts) in mercados.items():
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
        rows.append((py, net, ts.isoformat()))
    return rows


def _gate(py_arr, pnl_arr, lo, hi, rng, n_min_gate=40, iters=600):
    mask = (py_arr >= lo) & (py_arr < hi)
    n = int(mask.sum())
    if n < 15:
        return None
    pnls = pnl_arr[mask]
    wins = int(np.sum(pnls > 0))
    hit_rate = wins / n
    pnl_medio = pnls.mean()
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
    return {"n": n, "hit": hit_rate, "wilson_lo": wlo, "pnl_medio": float(pnl_medio),
            "boot90": [float(boot_lo), float(boot_hi)], "p_shuffle": pval,
            "split": [first, second], "veredicto": veredicto}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strategy", required=True)
    ap.add_argument("--subtype", required=True, help="ej. BTC#60min")
    ap.add_argument("--decision", required=True, choices=["BUY_YES", "BUY_NO"])
    ap.add_argument("--activo-markets", default=None,
                     help="Si se pasa (ej. BTC), amplía la población extrayendo TODO el "
                          "histórico de data/markets/ para ese activo en vez de usar solo "
                          "el results.csv propio de la tupla")
    ap.add_argument("--duracion-min", type=int, default=None,
                     help="Duración en minutos del marco (60, 15, 5...) -- obligatorio con --activo-markets")
    args = ap.parse_args()

    if args.activo_markets:
        if not args.duracion_min:
            raise SystemExit("--duracion-min es obligatorio junto a --activo-markets")
        print(f"Extrayendo histórico de data/markets/ para {args.activo_markets} "
              f"({args.duracion_min}min)... (puede tardar varios minutos)")
        mercados = _extraer_desde_markets(args.activo_markets, args.duracion_min)
        print(f"  {len(mercados)} mercados encontrados")
        outcomes = _outcomes_todas_estrategias()
        rows = _pnl_desde_markets(mercados, outcomes, args.decision)
        fuente = f"data/markets/ + outcomes de TODAS las estrategias ({len(outcomes)} market_ids conocidos)"
    else:
        rows = _cargar_poblacion_resultscsv(args.strategy, args.subtype, args.decision)
        fuente = "results.csv propio de la tupla"

    rows.sort(key=lambda r: r[2])
    py_arr = np.array([r[0] for r in rows])
    pnl_arr = np.array([r[1] for r in rows])
    print(f"\n=== {args.strategy}#{args.subtype}#{args.decision} "
          f"-- fuente: {fuente} -- n_total={len(rows)} ===\n")

    rng = np.random.default_rng(42)
    edges = [round(i * 0.05, 2) for i in range(20)] + [1.0]
    buenos = []
    for lo, hi in zip(edges, edges[1:]):
        r = _gate(py_arr, pnl_arr, lo, hi, rng)
        if r is None:
            continue
        print(f"[{lo:.2f},{hi:.2f}) n={r['n']:5d} hit={r['hit']*100:5.2f}% "
              f"wilson_lo={r['wilson_lo']*100:5.2f}% pnl_neto/trade={r['pnl_medio']:+.4f} "
              f"boot90=[{r['boot90'][0]:+.4f},{r['boot90'][1]:+.4f}] p_shuffle={r['p_shuffle']:.4f} "
              f"split=[{r['split'][0]:+.4f},{r['split'][1]:+.4f}] {r['veredicto']}")
        if r['veredicto'] == 'GATE_OK_BUENO':
            buenos.append((lo, hi))

    print(f"\nZonas confirmadas GATE_OK_BUENO: {buenos or 'NINGUNA -- no cablear ningún veto '
          'todavía, o vetar la tupla entera hasta que confirme algo (mismo criterio que ETH sin '
          'zona buena en el veto de sigma_ewma_delta_pct, 05-Ago)'}")


if __name__ == "__main__":
    main()
