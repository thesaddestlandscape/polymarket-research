#!/usr/bin/env python3
"""Franja milimétrica ballenas — cruce a resolución fina (no la banda única
[0.70,0.90) que usa el resto del sistema) de TRES fuentes por (activo,marco),
para TODOS los marcos y monedas que operamos (5min/15min/60min × BTC/ETH/
SOL/XRP/DOGE, no solo 15min):

  1. BALLENAS  — ballenas_timing_history.csv: TODAS las compras de TODAS las
     wallets en TODOS los mercados resueltos de nuestro nicho (no solo las
     "smart"), vía /trades real de Polymarket. Histórico completo de
     mercado, no filtrado por si nuestras estrategias dispararon o no ahí.
  2. SHADOW    — results.csv: qué habría pasado con cada predicción nuestra,
     para CUALQUIER estrategia BUY_YES con volumen (n agregado >=100) en ese
     (activo,marco) -- descubierto dinámicamente, no una lista fija.
  3. REAL      — trades.csv: lo que de verdad hemos operado con dinero desde
     que estamos en live, agregado por (activo,marco,BUY_YES).

Para cada bucket fino con n>=N_MIN_BUCKET_MADURO que pasa el gate riguroso
completo (Wilson+shuffle+bootstrap, misma función que usa el resto del
proyecto), se repite el gate en SPLIT-HALF cronológico (primera vs segunda
mitad de fechas) -- un bucket que solo pasa en la muestra completa pero no
en ambas mitades es candidato a sobreajuste/selección post-hoc (mirar todos
los buckets y quedarse con el mejor), NO se reporta como "robusto".

Objetivo (petición explícita Javi, 21-Jul, ampliada el mismo día a "todas
las monedas y marcos que operamos, quizá nos estemos dejando franjas sin
operar"): detectar tanto huecos de cobertura (ballenas con hit alto donde
apenas operamos) como franjas ya cubiertas por nuestras propias señales
donde el pnl/trade es mejor DENTRO de un bucket fino que en el agregado de
la tupla -- pero exigiendo que sobreviva split-half antes de proponer tocar
ningún filtro real.

Solo lectura. No decide nada, no toca prob_yes ni ningún gate real. Pensado
para correr cada inicio de sesión (protocolo CLAUDE.md punto 9) y ver cómo
crece n en cada bucket día a día antes de decidir cortar nada.
"""
import csv
import json
from collections import defaultdict
from pathlib import Path

from analisis_gate_riguroso import gate

REPO = Path(__file__).resolve().parent
BALLENAS_HIST = REPO / "data" / "shadow" / "ballenas_timing_history.csv"
RESULTS = REPO / "data" / "shadow" / "results.csv"
TRADES = REPO / "data" / "live" / "trades.csv"
OUT = REPO / "data" / "shadow" / "franja_milimetrica_ballenas.json"

STEP = 0.05
ACTIVOS = ("BTC", "ETH", "SOL", "XRP", "DOGE")
MARCOS = ("5min", "15min", "60min")           # nomenclatura results/trades
MARCO_BALLENAS_MAP = {"5min": "5m", "15min": "15m", "60min": "60m"}
N_MIN_AGREGADO_ESTRATEGIA = 100   # mínimo para que una (strategy,subtype) entre al barrido
N_MIN_BUCKET_INFORMATIVO = 15
N_MIN_BUCKET_MADURO = 40          # umbral de gate riguroso + split-half


def bucket(p):
    return round((p // STEP) * STEP, 3)


def cargar_ballenas():
    """(activo,marco_ballenas) -> bucket -> [aciertos, n]."""
    out = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    with open(BALLENAS_HIST, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            activo, marco = row.get("activo"), row.get("marco")
            if activo not in ACTIVOS or marco not in MARCO_BALLENAS_MAP.values():
                continue
            if row.get("compro_yes") not in ("0", "1"):
                continue
            try:
                p = float(row["precio"])
                acierto = int(row["acierto"])
            except (TypeError, ValueError):
                continue
            d = out[(activo, marco)][bucket(p)]
            d[0] += acierto
            d[1] += 1
    return out


def cargar_shadow_filas():
    """(strategy,subtype,decision) -> lista de filas (dict results.csv),
    solo BUY_YES, solo subtypes que acaben en alguno de MARCOS."""
    out = defaultdict(list)
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["decision"] != "BUY_YES":
                continue
            sub = row["subtype"] or ""
            if "#" not in sub:
                continue
            activo, marco = sub.split("#", 1)
            if activo not in ACTIVOS or marco not in MARCOS:
                continue
            if row.get("acierto") not in ("0", "1"):
                continue
            try:
                float(row["precio_yes_mercado"])
            except (TypeError, ValueError):
                continue
            out[(row["strategy"], sub, "BUY_YES")].append(row)
    return out


def cargar_real():
    """(activo,marco) -> bucket -> [n, aciertos, pnl_total] -- dinero real."""
    out = defaultdict(lambda: defaultdict(lambda: [0, 0, 0.0]))
    if not TRADES.exists():
        return out
    with open(TRADES, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "CLOSED" or row.get("direction") != "BUY_YES":
                continue
            sub = row.get("subtype") or ""
            if "#" not in sub:
                continue
            activo, marco = sub.split("#", 1)
            if activo not in ACTIVOS or marco not in MARCOS:
                continue
            try:
                p = float(row["entry_price"])
                pnl = float(row["pnl_neto_eur"])
            except (TypeError, ValueError):
                continue
            acierto = 1 if pnl > 0 else 0
            d = out[(activo, marco)][bucket(p)]
            d[0] += 1
            d[1] += acierto
            d[2] += pnl
    return out


def split_half(rows):
    filas = sorted(rows, key=lambda r: r.get("prediction_timestamp", ""))
    mid = len(filas) // 2
    return filas[:mid], filas[mid:]


def main():
    ballenas = cargar_ballenas()
    shadow_filas = cargar_shadow_filas()
    real = cargar_real()

    # (strategy,subtype,decision) -> bucket fino -> filas
    shadow_buckets = defaultdict(lambda: defaultdict(list))
    for clave, filas in shadow_filas.items():
        for r in filas:
            b = bucket(float(r["precio_yes_mercado"]))
            shadow_buckets[clave][b].append(r)

    resultado = {}
    robustos, fragiles, huecos_totales = [], [], []

    print(f"{'='*110}")
    print(f"FRANJA MILIMÉTRICA — ballenas / shadow / real, step={STEP}, marcos={MARCOS}")
    print(f"{'='*110}")

    for marco in MARCOS:
        marco_b = MARCO_BALLENAS_MAP[marco]
        for activo in ACTIVOS:
            estrategias = [k for k in shadow_buckets if k[1] == f"{activo}#{marco}"
                           and sum(len(v) for v in shadow_buckets[k].values()) >= N_MIN_AGREGADO_ESTRATEGIA]
            ballenas_ab = ballenas.get((activo, marco_b), {})
            real_ab = real.get((activo, marco), {})
            if not estrategias and not ballenas_ab:
                continue

            print(f"\n########## {activo}#{marco} ##########")

            # huecos de cobertura: bucket con ballenas fuerte donde NINGUNA
            # estrategia nuestra tiene n>=N_MIN_BUCKET_INFORMATIVO
            todos_los_buckets = set(ballenas_ab.keys())
            for k in estrategias:
                todos_los_buckets |= set(shadow_buckets[k].keys())
            for b in sorted(todos_los_buckets):
                ab, nb = ballenas_ab.get(b, [0, 0])
                if nb < 50:
                    continue
                hit_b = ab / nb * 100
                if hit_b < 70:
                    continue
                n_shadow_total = sum(len(shadow_buckets[k].get(b, [])) for k in estrategias)
                if n_shadow_total < N_MIN_BUCKET_INFORMATIVO:
                    huecos_totales.append((activo, marco, b, hit_b, nb, n_shadow_total))

            if not estrategias:
                print("  (sin estrategia shadow con volumen suficiente aquí)")
                continue

            for k in sorted(estrategias):
                strat, sub, dec = k
                bd = shadow_buckets[k]
                n_total = sum(len(v) for v in bd.values())
                buenos = []
                for b, filas in sorted(bd.items()):
                    n = len(filas)
                    if n < N_MIN_BUCKET_MADURO:
                        continue
                    v = gate(filas)
                    if v is None or v["veredicto"] != "GATE OK":
                        continue
                    h1, h2 = split_half(filas)
                    v1 = gate(h1) if len(h1) >= 15 else None
                    v2 = gate(h2) if len(h2) >= 15 else None
                    pnl1 = v1["pnl_media"] if v1 else None
                    pnl2 = v2["pnl_media"] if v2 else None
                    robusto = (pnl1 is not None and pnl2 is not None
                               and pnl1 > 0 and pnl2 > 0)
                    ab, nb = ballenas_ab.get(b, [0, 0])
                    fila = {
                        "bucket": f"[{b:.2f},{b+STEP:.2f})", "n": n,
                        "hit": round(v["hit"] * 100, 1), "pnl_media": round(v["pnl_media"], 3),
                        "pnl_ci90": [round(v["pnl_lo"], 3), round(v["pnl_hi"], 3)],
                        "split_half_pnl": [round(pnl1, 3) if pnl1 is not None else None,
                                           round(pnl2, 3) if pnl2 is not None else None],
                        "robusto_split_half": robusto,
                        "ballenas_hit": round(ab / nb * 100, 1) if nb else None, "ballenas_n": nb,
                    }
                    buenos.append(fila)
                    (robustos if robusto else fragiles).append((strat, sub, dec, fila))
                if buenos:
                    print(f"  {strat}#{sub}#{dec} (n_total={n_total}):")
                    for fila in buenos:
                        marca = "✅ ROBUSTO" if fila["robusto_split_half"] else "⚠️  frágil (no sobrevive split-half)"
                        sh = fila["split_half_pnl"]
                        print(f"    {fila['bucket']} n={fila['n']:4d} hit={fila['hit']:5.1f}% "
                              f"pnl/trade={fila['pnl_media']:+.3f} CI90%={fila['pnl_ci90']} "
                              f"split_half=[{sh[0]},{sh[1]}]  ballenas_hit={fila['ballenas_hit']} (n={fila['ballenas_n']})  {marca}")
                    resultado[f"{strat}#{sub}#{dec}"] = buenos

    print(f"\n\n{'='*110}")
    print(f"RESUMEN — {len(robustos)} bucket(s) ROBUSTO(S) (gate OK + split-half positivo ambas mitades):")
    print(f"{'='*110}")
    for strat, sub, dec, fila in robustos:
        print(f"  {strat}#{sub}#{dec} {fila['bucket']} n={fila['n']} pnl/trade={fila['pnl_media']:+.3f}")

    print(f"\n{len(fragiles)} bucket(s) pasan gate en muestra completa pero NO split-half (no accionar):")
    for strat, sub, dec, fila in fragiles:
        print(f"  {strat}#{sub}#{dec} {fila['bucket']} n={fila['n']} pnl/trade={fila['pnl_media']:+.3f} split_half={fila['split_half_pnl']}")

    if huecos_totales:
        print(f"\n🚨 HUECOS DE COBERTURA (ballenas n>=50 hit>=70%, shadow_n<{N_MIN_BUCKET_INFORMATIVO} sumando todas las estrategias):")
        for activo, marco, b, hit_b, nb, n_sh in huecos_totales:
            print(f"  {activo}#{marco} [{b:.2f},{b+STEP:.2f}) ballenas hit={hit_b:.1f}% (n={nb}) — shadow_n_total={n_sh}")

    OUT.write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nGuardado en {OUT}")


if __name__ == "__main__":
    main()
