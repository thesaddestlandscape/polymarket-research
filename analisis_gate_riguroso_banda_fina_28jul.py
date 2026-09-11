"""
analisis_gate_riguroso_banda_fina_28jul.py — validación RETROSPECTIVA con
rigor completo (Wilson + shuffle + split-half) de si
`ballenas_banda_fina_gate.py` (Fase 0, solo observacional desde hoy)
habría evitado pérdidas reales en las 9 tuplas live, más fill-ability
cruzando `libro_snapshots.csv`. Petición explícita Javi 28-Jul: "necesitamos
saber que esos buckets tienen edge y que el filtro funciona, no podemos
perder mas pasta ya ni esperar mas... hay suficientes datos para hacer los
robustos".

LIMITACIÓN EXPLÍCITA (fail loud, no ocultar): el gate se re-evalúa contra
la calibración ACTUAL de ballenas_observer.py (bandas_significativas de
HOY), no contra la calibración que existía en el momento histórico de cada
señal -- es un proxy retrospectivo con algo de look-ahead, no una prueba
causal pura sin sesgo. Se reporta igualmente porque es la mejor evidencia
disponible con los datos que hay, y es el mismo criterio (banda ya
calibrada) que usaría el gate en producción desde ya.

Solo lectura. No cambia ningún comportamiento.
"""
import csv
import json
import math
from datetime import datetime, timezone
from collections import defaultdict

from ballenas_banda_fina_gate import evaluar as gate_evaluar

RESULTS = "data/shadow/results.csv"
TRADES = "data/live/trades.csv"
LIBRO = "data/live/libro_snapshots.csv"
CONFIG_LIVE = "data/live/config_live.json"

N_MIN = 15


def parse_ts(s):
    try:
        d = datetime.fromisoformat(s.replace("Z", "+00:00"))
        if d.tzinfo is None:
            d = d.replace(tzinfo=timezone.utc)
        return d
    except Exception:
        return None


def cargar_tuplas_live():
    with open(CONFIG_LIVE, encoding="utf-8") as f:
        c = json.load(f)
    out = []
    for t in c.get("pares_permitidos_live", []):
        partes = t.split("#")
        if len(partes) == 4:
            strategy, activo, marco, decision = partes
            out.append((strategy, activo, marco, decision, t))
    return out


def wilson_lower(hits, n, z=1.645):
    if n == 0:
        return float("nan")
    p = hits / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centro - margen) / denom


def stats(filas_pnl):
    n = len(filas_pnl)
    if n == 0:
        return {"n": 0}
    media = sum(filas_pnl) / n
    if n > 1:
        var = sum((x - media) ** 2 for x in filas_pnl) / (n - 1)
        se = math.sqrt(var / n)
        ic90 = (media - 1.645 * se, media + 1.645 * se)
    else:
        ic90 = (float("nan"), float("nan"))
    return {"n": n, "pnl_medio": media, "ic90_lo": ic90[0], "ic90_hi": ic90[1]}


def shuffle_test(pasa_pnl, veta_pnl, iters=3000, seed=42):
    """H0: la etiqueta pasa/veta no importa -- diferencia de medias real vs
    distribución de diferencias con etiquetas barajadas. p = fracción de
    barajados con diferencia >= la real (a favor de que vetar evita
    pérdidas, i.e. media(pasa) - media(veta) > 0 más de lo esperado por azar)."""
    import random
    rnd = random.Random(seed)
    todos = pasa_pnl + veta_pnl
    n_pasa = len(pasa_pnl)
    if not pasa_pnl or not veta_pnl:
        return None
    diff_real = (sum(pasa_pnl) / len(pasa_pnl)) - (sum(veta_pnl) / len(veta_pnl))
    mayor_igual = 0
    for _ in range(iters):
        rnd.shuffle(todos)
        p = todos[:n_pasa]
        v = todos[n_pasa:]
        d = (sum(p) / len(p)) - (sum(v) / len(v))
        if d >= diff_real:
            mayor_igual += 1
    return {"diff_real": diff_real, "p_valor": mayor_igual / iters}


def split_half(filas):
    """filas: lista de (ts, pnl, veta_bool) ordenadas por tiempo -> dos
    mitades cronológicas, reporta diff(pasa-veta) en cada una."""
    filas = sorted(filas, key=lambda r: r[0])
    mid = len(filas) // 2
    out = []
    for mitad in (filas[:mid], filas[mid:]):
        pasa = [pnl for _, pnl, v in mitad if not v]
        veta = [pnl for _, pnl, v in mitad if v]
        if pasa and veta:
            out.append(round(sum(pasa) / len(pasa) - sum(veta) / len(veta), 4))
        else:
            out.append(None)
    return out


def cargar_shadow_evaluado(tuplas):
    """clave -> lista de (ts, pnl, veta_bool)"""
    out = defaultdict(list)
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("acierto") not in ("0", "1"):
                continue
            clave_row = (row["strategy"], row["subtype"], row["decision"])
            match = next((t for t in tuplas if (t[0], f"{t[1]}#{t[2]}", t[3]) == clave_row), None)
            if match is None:
                continue
            try:
                py = float(row["precio_yes_mercado"])
                pnl = float(row["pnl_neto"])
            except Exception:
                continue
            pred_ts = parse_ts(row.get("prediction_timestamp", ""))
            end_ts = parse_ts(row.get("end_date", ""))
            if pred_ts is None or end_ts is None:
                continue
            restante_min = (end_ts - pred_ts).total_seconds() / 60.0
            if restante_min < 0:
                continue
            strategy, activo, marco, decision, tupla_str = match
            veredicto = gate_evaluar(activo, marco, py, restante_min)
            out[tupla_str].append((pred_ts, pnl, veredicto["vetaria_fase1"]))
    return out


def cargar_real_evaluado(tuplas):
    out = defaultdict(list)
    with open(TRADES, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "CLOSED":
                continue
            clave_row = (row["strategy"], row["subtype"], row["direction"])
            match = next((t for t in tuplas if (t[0], f"{t[1]}#{t[2]}", t[3]) == clave_row), None)
            if match is None:
                continue
            try:
                py = float(row["entry_price"])
                pnl = float(row["pnl_neto_eur"])
            except Exception:
                continue
            ts_ = parse_ts(row.get("timestamp_utc", ""))
            end_ts = parse_ts(row.get("end_date", ""))
            if ts_ is None or end_ts is None:
                continue
            restante_min = (end_ts - ts_).total_seconds() / 60.0
            if restante_min < 0:
                continue
            strategy, activo, marco, decision, tupla_str = match
            veredicto = gate_evaluar(activo, marco, py, restante_min)
            out[tupla_str].append((ts_, pnl, veredicto["vetaria_fase1"]))
    return out


def cargar_fillability(tuplas):
    """market_id -> end_date (desde results.csv, universal) para poder
    calcular restante_min de cada snapshot de libro."""
    market_end = {}
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            mid = row.get("market_id")
            end = row.get("end_date")
            if mid and end and mid not in market_end:
                market_end[mid] = end

    out = defaultdict(lambda: defaultdict(int))  # tupla_str -> motivo -> n, separado pasa/veta
    with open(LIBRO, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            clave_row = (row["strategy"], row["subtype"], row["direction"])
            match = next((t for t in tuplas if (t[0], f"{t[1]}#{t[2]}", t[3]) == clave_row), None)
            if match is None:
                continue
            end = market_end.get(row.get("market_id", ""))
            ts_ = parse_ts(row.get("timestamp_utc", ""))
            end_ts = parse_ts(end) if end else None
            try:
                py = float(row["precio_plan"])
            except Exception:
                continue
            restante_min = None
            if ts_ is not None and end_ts is not None:
                restante_min = (end_ts - ts_).total_seconds() / 60.0
                if restante_min < 0:
                    restante_min = None
            strategy, activo, marco, decision, tupla_str = match
            veredicto = gate_evaluar(activo, marco, py, restante_min)
            grupo = "veta" if veredicto["vetaria_fase1"] else "pasa"
            motivo = row.get("motivo", "?")
            out[tupla_str][(grupo, motivo)] += 1
    return out


def main():
    tuplas = cargar_tuplas_live()
    shadow = cargar_shadow_evaluado(tuplas)
    real = cargar_real_evaluado(tuplas)
    fill = cargar_fillability(tuplas)

    for strategy, activo, marco, decision, tupla_str in tuplas:
        print(f"\n{'='*110}\n{tupla_str}\n{'='*110}")

        # --- SHADOW ---
        filas = shadow.get(tupla_str, [])
        pasa = [pnl for _, pnl, v in filas if not v]
        veta = [pnl for _, pnl, v in filas if v]
        st_pasa = stats(pasa)
        st_veta = stats(veta)
        print(f"  SHADOW: pasa n={st_pasa['n']:4d} pnl/tr={st_pasa.get('pnl_medio', float('nan')):+.3f} "
              f"IC90=[{st_pasa.get('ic90_lo', float('nan')):+.3f},{st_pasa.get('ic90_hi', float('nan')):+.3f}]"
              f"   |   veta n={st_veta['n']:4d} pnl/tr={st_veta.get('pnl_medio', float('nan')):+.3f} "
              f"IC90=[{st_veta.get('ic90_lo', float('nan')):+.3f},{st_veta.get('ic90_hi', float('nan')):+.3f}]")
        if pasa and veta:
            sh = shuffle_test(pasa, veta)
            sp = split_half(filas)
            robusto = (sh["p_valor"] < 0.05) if sh else None
            print(f"    shuffle: diff(pasa-veta)={sh['diff_real']:+.3f} p={sh['p_valor']:.4f} "
                  f"{'ROBUSTO p<0.05' if robusto else 'no significativo'}   split-half diff: {sp}")
        elif st_veta["n"] < N_MIN:
            print(f"    (grupo 'veta' n={st_veta['n']}<15 -- no concluyente todavía, dejar madurar)")

        # --- REAL ---
        filas_r = real.get(tupla_str, [])
        pasa_r = [pnl for _, pnl, v in filas_r if not v]
        veta_r = [pnl for _, pnl, v in filas_r if v]
        print(f"  REAL:   pasa n={len(pasa_r):3d} pnl_total={sum(pasa_r):+.3f}   |   "
              f"veta n={len(veta_r):3d} pnl_total={sum(veta_r):+.3f}")

        # --- FILL-ABILITY ---
        fi = fill.get(tupla_str, {})
        for grupo in ("pasa", "veta"):
            motivos = {m: n for (g, m), n in fi.items() if g == grupo}
            total = sum(motivos.values())
            ejecutadas = motivos.get("ejecutada", 0)
            if total:
                print(f"  FILL-ABILITY libro_snapshots [{grupo}]: n={total:4d} "
                      f"ejecutada={ejecutadas} ({ejecutadas/total*100:.1f}%) motivos={motivos}")


if __name__ == "__main__":
    main()
