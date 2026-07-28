"""
analisis_gate_bucket_propio_28jul.py — gate de entrada por micro-bucket de
precio (paso 0.05) construido desde NUESTRO PROPIO histórico de PnL
(results.csv), no desde el timing de ballenas (que la validación
retrospectiva del mismo día refutó -- ver ballenas_banda_fina_gate.py y
project_gate_banda_fina_ballenas_28jul en memoria: mezclar el timing de
ballenas con la causalidad de FAVORITO_CONFIRMADO/GBM_LATE no transfiere,
en 3/5 tuplas con n suficiente vetaba el grupo BUENO).

Rigor por bucket (petición explícita Javi, "hay suficientes datos para
hacer los robustos"):
  1. n >= N_MIN (15, mínimo CLAUDE.md)
  2. shuffle test: pnl del bucket vs pnl del RESTO de la misma tupla,
     H0 = la etiqueta bucket/resto no importa. p < P_MAX para considerar
     la diferencia real (no ruido de muestreo).
  3. split-half CRONOLÓGICO: el signo de (pnl_bucket - pnl_resto) tiene
     que repetirse en las dos mitades temporales -- un resultado que solo
     aparece en una mitad es la firma de un artefacto puntual, no un
     patrón estable (mismo criterio que analisis_gate_riguroso.py usa en
     el resto del proyecto).

Un bucket se marca "malo_confirmado" (candidato a stake=0 en el filtro) o
"bueno_confirmado" solo si pasa las 3 barras. Todo lo demás queda
"sin_concluir" -- fail-open, no se toca.

Solo lectura -- no cambia prob_yes/stake/pares_permitidos_live. Genera
`data/shadow/gate_bucket_propio.json`, consumido por
`gate_bucket_propio.py` (Fase 0 observacional, igual patrón que
ballenas_banda_fina_gate).
"""
import csv
import json
import math
import random
from collections import defaultdict

RESULTS = "data/shadow/results.csv"
CONFIG_LIVE = "data/live/config_live.json"
OUT = "data/shadow/gate_bucket_propio.json"

STEP = 0.05
N_MIN = 15
P_MAX = 0.05
ITERS = 4000


def bucket(p):
    return round(math.floor(p / STEP) * STEP, 4)


def cargar_tuplas_live():
    with open(CONFIG_LIVE, encoding="utf-8") as f:
        c = json.load(f)
    out = []
    for t in c.get("pares_permitidos_live", []):
        partes = t.split("#")
        if len(partes) == 4:
            strategy, activo, marco, decision = partes
            out.append((strategy, f"{activo}#{marco}", decision, t))
    return out


def cargar_filas(tuplas):
    claves = {(s, sub, d): t for s, sub, d, t in tuplas}
    out = defaultdict(list)  # tupla_str -> [(ts, py, pnl), ...]
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("acierto") not in ("0", "1"):
                continue
            clave = (row["strategy"], row["subtype"], row["decision"])
            t = claves.get(clave)
            if t is None:
                continue
            try:
                py = float(row["precio_yes_mercado"])
                pnl = float(row["pnl_neto"])
            except Exception:
                continue
            out[t].append((row.get("prediction_timestamp", ""), py, pnl))
    return out


def shuffle_test(a, b, iters=ITERS, seed=42):
    rnd = random.Random(seed)
    diff_real = (sum(a) / len(a)) - (sum(b) / len(b))
    todos = a + b
    na = len(a)
    mayor_igual_abs = 0
    for _ in range(iters):
        rnd.shuffle(todos)
        da = sum(todos[:na]) / na - sum(todos[na:]) / len(todos[na:])
        if abs(da) >= abs(diff_real):
            mayor_igual_abs += 1
    return diff_real, mayor_igual_abs / iters


def main():
    tuplas = cargar_tuplas_live()
    filas_por_tupla = cargar_filas(tuplas)
    resultado = {}

    for strategy, subtype, decision, tupla_str in tuplas:
        filas = filas_por_tupla.get(tupla_str, [])
        print(f"\n{'='*112}\n{tupla_str}  (n_total={len(filas)})\n{'='*112}")
        if len(filas) < N_MIN:
            print("  n_total insuficiente, sin conclusión posible.")
            resultado[tupla_str] = {}
            continue

        por_bucket = defaultdict(list)
        for ts, py, pnl in filas:
            por_bucket[bucket(py)].append((ts, pnl))

        tabla = {}
        for b in sorted(por_bucket):
            dentro = por_bucket[b]
            fuera = [(ts, pnl) for bb, fs in por_bucket.items() if bb != b for ts, pnl in fs]
            n_d = len(dentro)
            pnl_d = [pnl for _, pnl in dentro]
            pnl_f = [pnl for _, pnl in fuera]
            media_d = sum(pnl_d) / n_d

            veredicto = "sin_concluir"
            p_valor = None
            split = None
            if n_d >= N_MIN and pnl_f:
                diff, p_valor = shuffle_test(pnl_d, pnl_f)
                dentro_sorted = sorted(dentro, key=lambda x: x[0])
                mid = n_d // 2
                m1 = dentro_sorted[:mid]
                m2 = dentro_sorted[mid:]
                if len(m1) >= 5 and len(m2) >= 5:
                    d1 = sum(pnl for _, pnl in m1) / len(m1) - sum(pnl_f) / len(pnl_f)
                    d2 = sum(pnl for _, pnl in m2) / len(m2) - sum(pnl_f) / len(pnl_f)
                    split = [round(d1, 4), round(d2, 4)]
                    consistente = (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)
                    if p_valor < P_MAX and consistente:
                        veredicto = "malo_confirmado" if diff < 0 else "bueno_confirmado"

            tabla[f"{b:.2f}"] = {
                "n": n_d, "pnl_medio": round(media_d, 4),
                "diff_vs_resto": round(media_d - (sum(pnl_f) / len(pnl_f)), 4) if pnl_f else None,
                "shuffle_p": round(p_valor, 4) if p_valor is not None else None,
                "split_half_diff": split, "veredicto": veredicto,
            }
            marca = {"malo_confirmado": "🔴", "bueno_confirmado": "🟢", "sin_concluir": "➖"}[veredicto]
            print(f"  [{b:.2f},{b+STEP:.2f}) n={n_d:4d} pnl_medio={media_d:+.3f} "
                  f"p={p_valor if p_valor is None else round(p_valor,4)} split={split} {marca} {veredicto}")

        resultado[tupla_str] = tabla

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    print(f"\nGuardado en {OUT}")


if __name__ == "__main__":
    main()
