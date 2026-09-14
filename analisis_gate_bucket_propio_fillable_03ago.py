"""
analisis_gate_bucket_propio_fillable_03ago.py — v2 de
analisis_gate_bucket_propio_28jul.py: mismo gate por micro-bucket de
precio (n>=15, shuffle test, split-half cronológico, BH-FDR), pero
restringido al subconjunto REALMENTE accionable en vez de results.csv
completo.

Por qué (hallazgo 03-Ago, sesión de pausa de BALLENAS_TARDIAS#BTC#15min +
FAVORITO_15MIN_ALTACONVICCION#ETH#15min): un primer intento de cruzar
libro_snapshots.csv (ratio_vs_stake>=5x) contra results.csv mezclaba
"ejecutada" (trade real intentado) con "senal_caducada"/"fuera_ventana"
-- categorías que el proyecto YA demostró que son estructuralmente
adversas incluso con libro bueno (ver
idea_caducidad_senales_filtro_protector_28jul: las señales caducadas
que SÍ tenían profundidad pierden dinero en 11/12 tuplas si se
hubieran ejecutado -- es un filtro protector, no un bug). Incluirlas
como "fillable" sesgaba el resultado hacia negativo artificialmente.

Definición correcta de "accionable" aquí:
  - Tuplas LIVE: motivo en {ejecutada, abort_requote, fok_kill} -- intento
    real de ejecución (exitoso o abortado por fricción real de mercado,
    no por timeout). veto_profundidad queda fuera por definición (ratio<5x
    ya lo excluye el filtro fillable de más abajo).
  - Tuplas CANDIDATO (no viven en pares_permitidos_live todavía): no hay
    "ejecutada" posible (nunca se intenta con dinero real). Se usa
    candidato_evaluacion + ratio_vs_stake>=5x como la mejor proxy
    disponible de "tendría profundidad si se intentara" -- más débil que
    el caso live (nunca hubo intento real), documentado explícitamente en
    el output.

Solo lectura -- no cambia prob_yes/stake/pares_permitidos_live ni
sobreescribe gate_bucket_propio.json (el que SÍ vetea dinero real hoy).
Escribe en data/shadow/gate_bucket_propio_fillable.json para comparar
antes de decidir si sustituye a la fuente de verdad actual (requiere
/code-review, toca qué se ejecuta con dinero real).
"""
import csv
import json
import math
import os
from collections import defaultdict
from pathlib import Path

import numpy as np

# 28-Ago: reusa la MISMA fórmula de retorno normalizado que analisis_log_
# growth.py (Kelly g(f), CLAUDE.md pt.14/P28) -- NUNCA reimplementarla
# aparte, el payout asimétrico es la misma cicatriz de siempre (hit-rate
# alto + pérdidas grandes raras se come el compounding aunque pnl_medio
# agregado sea positivo). Petición explícita Javi 28-Ago: conectar payout
# asimétrico en el mismo veto que selección adversa/profundidad de libro,
# no como chequeo manual aparte cada vez.
from analisis_log_growth import _retorno as _retorno_kelly  # noqa: E402
_F_KELLY = 0.10  # mismo default que analisis_log_growth.py/live

# 14-Sep (hallazgo real de sesión, ver project_discrepancia_gate_fillable_
# pnlfiel_14sep): este script y `shadow_pnl_fiel.py` medían "fill-ability"
# con DOS metodologías incompatibles sobre la misma tupla --
# FAVORITO_CONFIRMADO#BTC#5min#BUY_NO daba pnl_medio=-0.15€ aquí (todos los
# buckets grandes negativos) y +0.044€/trade en pnl_fiel (CI90 sin cruzar
# cero) para la MISMA población nominal ("candidato_evaluacion, ratio>=5x").
# Causa encontrada, dos diferencias reales:
#   1. Este script no filtraba por VENTANA HORARIA -- contaba señales de
#      cualquier hora del día, incluidas las que la operativa real de
#      config_live.json nunca opera. pnl_fiel sí filtra (ventana_en()).
#   2. Este script usaba `precio_yes_mercado` (precio de DETECCIÓN, el que
#      logueó shadow_predict.py) + slippage flat 2% -- pnl_fiel usa el
#      `mejor_ask` real del libro en el momento de evaluación (precio de
#      EJECUCIÓN) + fee 7% real (validado contra fees on-chain, solo se
#      paga en el lado ganador, no un flat en todas las filas).
# Dado que `_veto_fillable()` en gate_bucket_propio.py SOLO puede DEGRADAR
# un "bueno_confirmado" a "malo_confirmado" (nunca promocionar, ver su
# docstring) -- una metodología con estas dos discrepancias puede estar
# VETANDO buckets genuinamente rentables por error de medición, no por
# selección adversa real (exactamente el riesgo que motivó esta sesión:
# "lo mismo estamos perdiendo dinero de estrategias que están calladas").
# Fix: usa las MISMAS fuentes que pnl_fiel (import, no reimplementación) --
# ventana_en()+cargar_config() para el filtro horario, mejor_ask del libro
# (ya cargado vía colapsar_libro()) en vez de precio_yes_mercado, y
# FEE_RATE_TAKER_CRYPTO (7%, ganador-only) en vez de SLIPPAGE_NORMALIZADO
# (2% flat). g_kelly (_retorno_kelly, arriba) queda FUERA de este fix: es
# intrínsecamente relativo (fracción del stake, no €) y ya usa
# precio_yes_mercado de forma consistente con el resto del proyecto
# (analisis_log_growth.py, vigilado en vivo) -- cambiar su base de precio
# es un cambio de alcance mayor, no parte de esta corrección puntual.
from shadow_pnl_fiel import cargar_config, ventana_en, parse_ts, FEE_RATE_TAKER_CRYPTO  # noqa: E402

REPO = Path(__file__).resolve().parent
RESULTS = str(REPO / "data/shadow/results.csv")
LIBRO = str(REPO / "data/live/libro_snapshots.csv")
CONFIG_LIVE = str(REPO / "data/live/config_live.json")
OUT = str(REPO / "data/shadow/gate_bucket_propio_fillable.json")

STEP = 0.05
N_MIN = 15
P_MAX = 0.05
ITERS = 1000
RATIO_MIN = 5.0

# 18-Ago (/code-review): NO se comparten con libro_snapshots_prioridad.py
# a propósito -- ambas listas tienen orden relativo PROPIO, distinto del
# canónico (ej. fok_kill va DESPUÉS de abort_requote aquí, antes en el
# canónico), y PRIORIDAD_COLAPSO incluye "candidato_evaluacion", que ni
# existe en el canónico. No son subconjuntos filtrables -- forzar el
# import cambiaría el desempate real de este script.
PRIORIDAD_LIVE = ["ejecutada", "abort_requote", "abort_gate_bucket_postrequote", "fok_kill"]
PRIORIDAD_COLAPSO = ["ejecutada", "veto_profundidad", "abort_requote",
                      "abort_gate_bucket_postrequote", "fok_kill",
                      "veto_sin_datos", "senal_caducada", "no_viable_stake",
                      "candidato_evaluacion", "fuera_ventana"]


def bucket(p):
    # 06-Ago fix: +1e-9 evita mal-clasificar precios EXACTOS en un múltiplo
    # de STEP al bucket inferior (coma flotante) -- ver idea_bug_bucketing_
    # float_precision_micro_buckets_06ago.
    return round(math.floor(p / STEP + 1e-9) * STEP, 4)


def cargar_tuplas_live():
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
                continue
            vistos[t] = (strategy, f"{activo}#{marco}", decision, t, es_live)
    return list(vistos.values())


def colapsar_libro():
    """market_id -> mejor fila por (tupla), prioridad = PRIORIDAD_COLAPSO.
    Mismo criterio que analisis_fills.py -- NUNCA contar filas sueltas."""
    by_key = {}
    with open(LIBRO, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            tupla = (r["strategy"], r["subtype"], r["direction"])
            mid = r["market_id"]
            k = (tupla, mid)
            motivo = r.get("motivo", "")
            if k not in by_key:
                by_key[k] = r
            else:
                prev = by_key[k].get("motivo", "")
                if motivo in PRIORIDAD_COLAPSO and prev in PRIORIDAD_COLAPSO and \
                        PRIORIDAD_COLAPSO.index(motivo) < PRIORIDAD_COLAPSO.index(prev):
                    by_key[k] = r
    return by_key


def es_accionable(motivo, ratio, es_live):
    try:
        ratio_f = float(ratio) if ratio not in (None, "") else None
    except Exception:
        ratio_f = None
    if ratio_f is None or ratio_f < RATIO_MIN:
        return False
    if es_live:
        return motivo in PRIORIDAD_LIVE
    return motivo == "candidato_evaluacion"


def cargar_filas_accionables(tuplas, config):
    claves = {(s, sub, d): (t, es_live) for s, sub, d, t, es_live in tuplas}
    by_key = colapsar_libro()

    # market_id accionable -> fila de libro (para el mejor_ask real), por
    # tupla -- 14-Sep: ANTES solo se guardaba el set de mids, el precio se
    # releía de results.csv (precio de detección); ahora se necesita la
    # fila del libro para el precio de EJECUCIÓN.
    accionables_por_tupla: dict[str, dict[str, dict]] = defaultdict(dict)
    for (tupla_libro, mid), r in by_key.items():
        strat, sub, direc = tupla_libro
        info = claves.get((strat, sub, direc))
        if info is None:
            continue
        t, es_live = info
        if es_accionable(r.get("motivo"), r.get("ratio_vs_stake"), es_live):
            accionables_por_tupla[t][mid] = r

    out = defaultdict(list)
    n_fuera_ventana = 0
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("acierto") not in ("0", "1"):
                continue
            clave = (row["strategy"], row["subtype"], row["decision"])
            info = claves.get(clave)
            if info is None:
                continue
            t, es_live = info
            mid = row.get("market_id")
            libro_row = accionables_por_tupla.get(t, {}).get(mid)
            if libro_row is None:
                continue
            # 14-Sep: mismo filtro de ventana horaria que shadow_pnl_fiel.py
            # -- una señal fuera de la operativa real (config_live.json::
            # ventanas_*) no es "fillable" en el sentido que le importa a
            # Javi (¿operaríamos esto de verdad?), aunque tuviera libro con
            # profundidad. Sin este filtro, "accionable" mezclaba horas que
            # el propio proyecto nunca opera con las que sí -- la causa
            # principal de la discrepancia con pnl_fiel (ver comentario en
            # los imports de arriba).
            #
            # /code-review (mismo día, hallazgo real): filtrar por ventana
            # AQUÍ y nada más rompía la Señal 2 de gate_bucket_propio.py::
            # _veto_fillable() (ratio n_fill/n_total) -- n_total viene del
            # script HERMANO (analisis_gate_bucket_propio_28jul.py), que
            # NUNCA filtra por ventana. Reducir n_fill sin tocar n_total
            # hunde artificialmente el ratio y puede degradar buckets sanos
            # (verificado: FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min#
            # BUY_NO [0.45,0.50) pasaba de 43% a 25% de fill-ability, cruzando
            # el piso _FILLABLE_RATE_MIN=30% por el filtro, no por selección
            # adversa real). Fix: NUNCA se descarta la fila aquí -- se marca
            # `en_ventana` y se cuenta SIEMPRE para `n` (paridad con n_total,
            # Señal 2 sigue viendo la población de siempre); solo las filas
            # CON en_ventana=True entran en pnl_d/shuffle/split-half/g_kelly
            # (Señal 1/3, la corrección real de hoy) -- ver más abajo en main().
            ts_dt = parse_ts(row.get("prediction_timestamp", ""))
            en_ventana = ts_dt is not None and ventana_en(ts_dt, config) is not None
            if not en_ventana:
                n_fuera_ventana += 1
            try:
                py = float(row["precio_yes_mercado"])  # solo para bucketizar/g_kelly, no para pnl
                precio_fill = float(libro_row["mejor_ask"])
            except (KeyError, TypeError, ValueError):
                continue
            if not (0.01 < precio_fill < 0.99):
                continue
            acierto = row["acierto"] == "1"
            fee = FEE_RATE_TAKER_CRYPTO * precio_fill * (1 - precio_fill)
            # 14-Sep: pnl a precio de EJECUCIÓN (mejor_ask del libro, lo que
            # de verdad se habría pagado) + fee 7% real ganador-only -- antes
            # era precio de DETECCIÓN (precio_yes_mercado) + slippage flat
            # 2% en toda fila. `precio_fill` ya está en la perspectiva
            # correcta del lado operado (indexado por `direction` en
            # colapsar_libro()), sin necesidad del 1-p de _pnl_normalizado.
            pnl = (1.0 / precio_fill - 1.0) - fee if acierto else -1.0
            out[t].append((row.get("prediction_timestamp", ""), py, pnl, row["decision"], row["acierto"], en_ventana))
    if n_fuera_ventana:
        print(f"[cargar_filas_accionables] {n_fuera_ventana} señales accionables fuera de ventana "
              f"horaria real -- se cuentan para el ratio de fill-ability (Señal 2) pero NO entran "
              f"en pnl_medio/shuffle/g_kelly (Señal 1/3)")
    return out, {t: len(accionables_por_tupla.get(t, {})) for _, _, _, t, _ in tuplas}


_rng = np.random.default_rng(42)


def shuffle_test(a, b, iters=ITERS):
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    na, nb = len(a), len(b)
    diff_real = a.mean() - b.mean()
    todos = np.concatenate([a, b])
    n = na + nb
    idx = _rng.random((iters, n)).argsort(axis=1)
    permutado = todos[idx]
    media_a = permutado[:, :na].mean(axis=1)
    media_b = permutado[:, na:].mean(axis=1)
    diffs = media_a - media_b
    p_valor = float(np.mean(np.abs(diffs) >= abs(diff_real)))
    return float(diff_real), p_valor


def bh_fdr_signif(p_valores, q=0.05):
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
    config = cargar_config(REPO)
    tuplas = cargar_tuplas_live()
    filas_por_tupla, n_accionables = cargar_filas_accionables(tuplas, config)
    n_live = sum(1 for *_, es_live in tuplas if es_live)
    print(f"Tuplas a evaluar: {len(tuplas)} ({n_live} live, {len(tuplas) - n_live} candidatos)")
    print(f"Tuplas con >=1 mercado accionable: {sum(1 for v in n_accionables.values() if v > 0)}")

    pendientes = []
    resultado = {}
    for i, (strategy, subtype, decision, tupla_str, es_live) in enumerate(tuplas):
        filas = filas_por_tupla.get(tupla_str, [])
        if len(filas) < N_MIN:
            resultado[tupla_str] = {"_n_accionable_total": len(filas)}
            continue

        por_bucket = defaultdict(list)
        for ts, py, pnl, dec, acierto, en_ventana in filas:
            por_bucket[bucket(py)].append((ts, pnl, py, dec, acierto, en_ventana))

        tabla = {"_n_accionable_total": len(filas), "_es_live": es_live}
        for b in sorted(por_bucket):
            dentro_todo = por_bucket[b]
            # 14-Sep (/code-review, fix Señal 2): `n` (y todo lo que depende
            # de pnl -- shuffle/split-half/g_kelly) SOLO usa la ventana
            # horaria real; `n_accionable_dia_completo` cuenta TODAS las
            # señales accionables del bucket sin filtrar por ventana, misma
            # población que `n_total` del script hermano (gate_bucket_propio.
            # py lee ambos para la Señal 2 -- ver _veto_fillable()). Sin
            # este segundo conteo, reducir `n` por ventana sin más hundía el
            # ratio n_fill/n_total artificialmente.
            dentro = [f for f in dentro_todo if f[5]]
            n_accionable_dia_completo = len(dentro_todo)
            # "fuera" (el RESTO de la tupla, para shuffle-vs-resto) usa la
            # MISMA población ventana-filtrada que "dentro" -- comparar un
            # bucket filtrado contra un resto sin filtrar mezclaría de nuevo
            # las dos poblaciones que este fix separa.
            fuera = [(ts, pnl) for bb, fs in por_bucket.items() if bb != b
                     for ts, pnl, *_r, ev in fs if ev]
            n_d = len(dentro)
            entrada = {"n": n_d, "n_accionable_dia_completo": n_accionable_dia_completo,
                       "pnl_medio": None, "diff_vs_resto": None, "g_kelly_f10": None,
                       "shuffle_p": None, "split_half_diff": None, "veredicto": "sin_concluir"}
            tabla[f"{b:.2f}"] = entrada
            if n_d == 0 or not fuera:
                continue

            pnl_d = [pnl for _, pnl, *_ in dentro]
            pnl_f = [pnl for _, pnl in fuera]
            media_d = sum(pnl_d) / n_d
            entrada["pnl_medio"] = round(media_d, 4)
            entrada["diff_vs_resto"] = round(media_d - (sum(pnl_f) / len(pnl_f)), 4) if pnl_f else None

            # Payout asimétrico (Kelly g(f=10%)) sobre el MISMO subconjunto
            # fillable -- un bucket puede tener pnl_medio positivo y aun así
            # crecimiento compuesto negativo (hit-rate alto, pérdidas grandes
            # raras). Solo se calcula con n_d>=N_MIN (mismo piso que el resto
            # del gate); con menos, g_kelly queda None (sin evidencia, no se
            # inventa un valor).
            if n_d >= N_MIN:
                retornos = [_retorno_kelly({"precio_yes_mercado": py, "decision": dec, "acierto": acierto})
                            for _, _, py, dec, acierto, _ev in dentro]
                entrada["g_kelly_f10"] = round(sum(math.log(1 + _F_KELLY * r) for r in retornos) / n_d, 5)

            if n_d >= N_MIN and pnl_f:
                diff, p_valor = shuffle_test(pnl_d, pnl_f)
                entrada["shuffle_p"] = round(p_valor, 4)
                dentro_sorted = sorted(dentro, key=lambda x: x[0])
                mid = n_d // 2
                m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
                if len(m1) >= 5 and len(m2) >= 5:
                    d1 = sum(pnl for _, pnl, *_ in m1) / len(m1) - sum(pnl_f) / len(pnl_f)
                    d2 = sum(pnl for _, pnl, *_ in m2) / len(m2) - sum(pnl_f) / len(pnl_f)
                    entrada["split_half_diff"] = [round(d1, 4), round(d2, 4)]
                    consistente = (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)
                    if consistente:
                        pendientes.append({"tupla_str": tupla_str, "bucket": f"{b:.2f}", "entrada": entrada,
                                            "p": p_valor, "diff": diff, "es_live": es_live})
        resultado[tupla_str] = tabla

    p_valores = [p["p"] for p in pendientes]
    sobreviven = bh_fdr_signif(p_valores, q=P_MAX)
    print(f"\nTests candidatos: {len(pendientes)} | sobreviven BH-FDR q={P_MAX}: {len(sobreviven)}")

    veredictos_nuevos = []
    for idx, p in enumerate(pendientes):
        if idx not in sobreviven:
            continue
        veredicto = "malo_confirmado" if p["diff"] < 0 else "bueno_confirmado"
        p["entrada"]["veredicto"] = veredicto
        marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
        etiqueta = "LIVE" if p["es_live"] else "candidato(proxy)"
        b = p["bucket"]
        veredictos_nuevos.append(
            f"{marca} [{etiqueta}] {p['tupla_str']} [{b},{float(b)+STEP:.2f}) n={p['entrada']['n']} "
            f"pnl_medio={p['entrada']['pnl_medio']:+.3f} p={p['p']:.4f} {veredicto}"
        )

    print(f"\n{len(veredictos_nuevos)} bucket(s) con veredicto final tras BH-FDR:")
    for linea in veredictos_nuevos:
        print(f"  {linea}")

    # 31-Ago (/code-review, hallazgo real): escritura atómica -- desde que
    # vigia_gate_bucket_propio.py (06:55 UTC) también invoca este script
    # además del cron dedicado vigia_gate_bucket_propio_fillable.py (06:59
    # UTC, flock DISTINTO, sin exclusión mutua entre los dos), dos
    # ejecuciones concurrentes de este fichero podían escribir OUT a la vez
    # y dejarlo truncado/corrupto -- gate_bucket_propio.py::_cargar_fillable()
    # solo hace `except Exception: pass` y mantiene el cache previo, dejando
    # el veto de fill-ability silenciosamente desactivado ({}) ese ciclo sin
    # ningún error visible más allá de un print. tmp+os.replace() es atómico
    # dentro del mismo filesystem (mismo patrón ya usado en shadow_postmortem.
    # py/market_id_resolver.py/backfill_fee_historico.py) -- un lector nunca
    # ve un fichero a medio escribir, gane quien gane la carrera.
    tmp = OUT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    os.replace(tmp, OUT)
    print(f"\nGuardado en {OUT}")


if __name__ == "__main__":
    main()
