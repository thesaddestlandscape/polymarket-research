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
  4. BH-FDR POR (FAMILIA, MONEDA) (04-Ago, corregido dos veces el mismo
     día -- primero de global a por familia, luego Javi señaló que hay
     que desagregar TAMBIÉN por moneda, mismo principio que CLAUDE.md
     pt.17/feedback_desagregar_por_activo_siempre exige en todo el
     proyecto: antes se aplicaba GLOBAL sobre las ~264 tuplas×bucket del
     sistema a la vez, diluyendo el presupuesto de significancia de
     familias/monedas con menos tests candidatos. Hallazgo real: SOL#15min
     tenía 3 buckets con shuffle p<0.05 Y split-half consistente en ambas
     mitades -- exactamente el mismo rigor que sí confirmaba otros
     buckets -- pero se quedaban en "sin_concluir" solo por competir con
     miles de tests de otras familias/monedas en el mismo corte BH-FDR.
     Usa `_familia()` de kelly_precio_gate.py -- misma fuente de verdad de
     agrupamiento por arquetipo que el resto del sistema, GBM_LATE_15M{,
     _TARDIO,_ESPACIO_ATR,_PYCONFIRMADO} cuentan como una familia -- pero
     BTC/ETH/SOL/XRP/DOGE/BNB dentro de esa familia corrigen cada uno por
     su cuenta, no mezclados).

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
from collections import defaultdict
from pathlib import Path

import numpy as np

from kelly_precio_gate import _familia

REPO = Path(__file__).resolve().parent
RESULTS = str(REPO / "data/shadow/results.csv")
CONFIG_LIVE = str(REPO / "data/live/config_live.json")
OUT = str(REPO / "data/shadow/gate_bucket_propio.json")

STEP = 0.05
N_MIN = 15
P_MAX = 0.05
ITERS = 1000


def bucket(p):
    # 06-Ago fix: +1e-9 evita mal-clasificar precios EXACTOS en un múltiplo
    # de STEP al bucket inferior (coma flotante) -- ver idea_bug_bucketing_
    # float_precision_micro_buckets_06ago. Regenera gate_bucket_propio.json,
    # que consume gate_bucket_propio.py::evaluar() (mismo fix aplicado ahí).
    return round(math.floor(p / STEP + 1e-9) * STEP, 4)


def cargar_tuplas_live():
    """28-Jul: extendido a candidatos_evaluacion_live (petición explícita
    Javi, "aplícalo también a candidatos_evaluacion_live") -- el análisis
    en sí no distingue live/candidato (ambos ya están en results.csv,
    shadow_predict.py loguea todo igual), la diferencia real vive en el
    RUNTIME: gate_bucket_propio.py solo VETA ejecución si la tupla está
    en pares_permitidos_live (dinero real); en candidatos solo se loguea
    el veredicto como feature, nunca bloquea (no tiene sentido frenar la
    propia acumulación de fill-ability de un candidato por su PnL en
    shadow, que es justo lo que se está todavía evaluando). Devuelve
    (strategy, subtype, decision, tupla_str, es_live) -- es_live=True
    solo para las de pares_permitidos_live (dedupe: si una tupla está
    en ambas listas, cuenta como live).

    06-Ago (petición explícita Javi, "hay que recogerlo todo y hacerlo
    bien" -- mismo espíritu que el fix del cementerio del mismo día):
    ADEMÁS de las dos listas de config_live.json, escanea results.csv
    directamente y añade CUALQUIER (strategy,subtype,decision) que no
    esté ya cubierto -- es_live=False (candidato "descubierto", nunca
    puede vetar dinero real por construcción, ver runtime en
    gate_bucket_propio.py::evaluar()). Antes de este cambio, una
    estrategia nueva que empezara a generar en shadow se quedaba SIN
    micro-buckets hasta que alguien se acordara de añadirla a mano a
    candidatos_evaluacion_live -- confirmado real el mismo día: 24
    combos activos en results.csv (LIQUIDACIONES aparte, ya añadidas
    antes) llevaban tiempo sin cobertura, y el formato de 3 segmentos de
    WEEKLY_PRICE (activo sin marco, ej. "WEEKLY_PRICE#SOL#BUY_YES") ni
    siquiera lo soportaba el parseo de arriba (exigía exactamente 4
    segmentos). Con esto, la cobertura ya no depende de que nadie
    recuerde mantener una lista -- se auto-mantiene sola cada vez que
    este script corre (cron diario 06:55 UTC)."""
    with open(CONFIG_LIVE, encoding="utf-8") as f:
        c = json.load(f)
    vistos = {}
    for lista, es_live in ((c.get("pares_permitidos_live", []), True),
                            (c.get("candidatos_evaluacion_live", []), False)):
        for t in lista:
            partes = t.split("#")
            if len(partes) != 4:
                continue
            strategy, activo, marco, decision = partes
            if t in vistos and vistos[t][4]:
                continue  # ya está marcada live, no degradar a candidato
            vistos[t] = (strategy, f"{activo}#{marco}", decision, t, es_live)

    claves_cubiertas = {(s, sub, d) for s, sub, d, _, _ in vistos.values()}
    descubiertos = 0
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            s = row.get("strategy", "")
            sub = row.get("subtype", "")
            d = row.get("decision", "")
            if not s or not sub or not d:
                continue
            if (s, sub, d) in claves_cubiertas:
                continue
            t = f"{s}#{sub}#{d}"
            if t in vistos:
                continue
            claves_cubiertas.add((s, sub, d))
            vistos[t] = (s, sub, d, t, False)
            descubiertos += 1
    if descubiertos:
        print(f"[cargar_tuplas_live] {descubiertos} tuplas descubiertas directamente "
              f"en results.csv (no estaban en config_live.json)")
    return list(vistos.values())


def cargar_filas(tuplas):
    claves = {(s, sub, d): t for s, sub, d, t, _ in tuplas}
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


_rng = np.random.default_rng(42)


def shuffle_test(a, b, iters=ITERS):
    """Vectorizado con numpy -- la versión con random.shuffle en Python
    puro (O(n) por iteración con listas de miles de filas, cientos de
    tuplas/buckets) tardaba minutos en el barrido completo de
    candidatos_evaluacion_live (248 tuplas). Mismo test estadístico
    (permutación), resultado idéntico en distribución, solo más rápido:
    genera todas las permutaciones de golpe como matriz (iters, n) y
    calcula las medias de grupo con sumas acumuladas (argpartition)."""
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    na, nb = len(a), len(b)
    diff_real = a.mean() - b.mean()
    todos = np.concatenate([a, b])
    n = na + nb
    # (iters, n) de índices barajados -- argsort de valores aleatorios es
    # la forma estándar de vectorizar "shuffle" por filas en numpy.
    idx = _rng.random((iters, n)).argsort(axis=1)
    permutado = todos[idx]
    media_a = permutado[:, :na].mean(axis=1)
    media_b = permutado[:, na:].mean(axis=1)
    diffs = media_a - media_b
    p_valor = float(np.mean(np.abs(diffs) >= abs(diff_real)))
    return float(diff_real), p_valor


def bh_fdr_signif(p_valores, q=0.05):
    """Benjamini-Hochberg -- devuelve el set de ÍNDICES (en el orden
    original de p_valores) que sobreviven la corrección a nivel q.
    Con cientos/miles de tests simultáneos (candidatos_evaluacion_live:
    ~230 tuplas x ~10 buckets = miles de tests), p<0.05 SIN corregir
    produce ~5% de falsos positivos por puro azar -- con ~2000 tests,
    ~100 buckets "confirmados" que no serían nada. BH-FDR controla la
    tasa de falsos descubrimientos sobre el conjunto completo, mismo
    criterio que el resto del proyecto exige para hipótesis con muchos
    tests (feedback_shuffle_antes_de_bloquear, feedback_no_declarar_
    muerta_sin_agotar_opciones)."""
    n = len(p_valores)
    if n == 0:
        return set()
    orden = sorted(range(n), key=lambda i: p_valores[i])
    corte = -1
    for rank, i in enumerate(orden, start=1):
        if p_valores[i] <= (rank / n) * q:
            corte = rank
    if corte == -1:
        return set()
    return set(orden[:corte])


def main():
    tuplas = cargar_tuplas_live()
    filas_por_tupla = cargar_filas(tuplas)
    n_live = sum(1 for *_, es_live in tuplas if es_live)
    print(f"Tuplas a evaluar: {len(tuplas)} ({n_live} live, {len(tuplas) - n_live} candidatos)")

    # PASADA 1: calcular todos los buckets candidatos (n>=N_MIN, split-half
    # consistente) y acumular p-valores SIN decidir veredicto todavía --
    # BH-FDR necesita la familia completa de tests antes de cortar.
    pendientes = []
    resultado = {}
    for i, (strategy, subtype, decision, tupla_str, es_live) in enumerate(tuplas):
        if i % 25 == 0:
            print(f"  ... {i}/{len(tuplas)} tuplas procesadas (pasada 1/2)", flush=True)
        filas = filas_por_tupla.get(tupla_str, [])
        if len(filas) < N_MIN:
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

            entrada = {"n": n_d, "pnl_medio": round(media_d, 4),
                       "diff_vs_resto": round(media_d - (sum(pnl_f) / len(pnl_f)), 4) if pnl_f else None,
                       "shuffle_p": None, "split_half_diff": None, "veredicto": "sin_concluir"}
            tabla[f"{b:.2f}"] = entrada

            if n_d >= N_MIN and pnl_f:
                diff, p_valor = shuffle_test(pnl_d, pnl_f)
                entrada["shuffle_p"] = round(p_valor, 4)
                dentro_sorted = sorted(dentro, key=lambda x: x[0])
                mid = n_d // 2
                m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
                if len(m1) >= 5 and len(m2) >= 5:
                    d1 = sum(pnl for _, pnl in m1) / len(m1) - sum(pnl_f) / len(pnl_f)
                    d2 = sum(pnl for _, pnl in m2) / len(m2) - sum(pnl_f) / len(pnl_f)
                    entrada["split_half_diff"] = [round(d1, 4), round(d2, 4)]
                    consistente = (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)
                    if consistente:
                        pendientes.append({"tupla_str": tupla_str, "bucket": f"{b:.2f}", "entrada": entrada,
                                            "p": p_valor, "diff": diff, "es_live": es_live})
        resultado[tupla_str] = tabla

    # PASADA 2: BH-FDR POR (FAMILIA, MONEDA) -- cada (arquetipo, activo)
    # corrige solo contra sus propios tests candidatos, no contra los de
    # las ~264 tuplas×bucket del sistema entero NI contra las otras 5
    # monedas de la misma familia (CLAUDE.md pt.17, desagregar siempre por
    # activo). Estrategias sin agrupar en kelly_precio_gate._familia()
    # (devuelve el nombre tal cual) quedan igual, solo se añade la moneda
    # a la clave.
    por_familia_moneda = defaultdict(list)
    for idx, p in enumerate(pendientes):
        partes = p["tupla_str"].split("#")
        strategy = partes[0]
        activo = partes[1] if len(partes) > 1 else "?"
        clave = (_familia(strategy), activo)
        por_familia_moneda[clave].append(idx)

    sobreviven = set()
    for (familia, activo), indices in por_familia_moneda.items():
        p_valores_grupo = [pendientes[i]["p"] for i in indices]
        sobreviven_grupo = bh_fdr_signif(p_valores_grupo, q=P_MAX)
        sobreviven |= {indices[j] for j in sobreviven_grupo}
        print(f"  familia={familia} activo={activo}: {len(indices)} tests candidatos, "
              f"{len(sobreviven_grupo)} sobreviven BH-FDR q={P_MAX}")

    print(f"\nTests candidatos: {len(pendientes)} | sobreviven BH-FDR (por familia+moneda): {len(sobreviven)}")

    veredictos_nuevos = []
    for idx, p in enumerate(pendientes):
        if idx not in sobreviven:
            continue
        veredicto = "malo_confirmado" if p["diff"] < 0 else "bueno_confirmado"
        p["entrada"]["veredicto"] = veredicto
        marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
        etiqueta = "LIVE" if p["es_live"] else "candidato"
        b = p["bucket"]
        veredictos_nuevos.append(
            f"{marca} [{etiqueta}] {p['tupla_str']} [{b},{float(b)+STEP:.2f}) n={p['entrada']['n']} "
            f"pnl_medio={p['entrada']['pnl_medio']:+.3f} p={p['p']:.4f} {veredicto}"
        )

    print(f"\n{len(veredictos_nuevos)} bucket(s) con veredicto final tras BH-FDR:")
    for linea in veredictos_nuevos:
        print(f"  {linea}")

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    print(f"\nGuardado en {OUT}")


if __name__ == "__main__":
    main()
