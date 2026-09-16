#!/usr/bin/env python3
"""analisis_candidata9_10_gate_bucket_26ago.py -- gate por micro-bucket
de precio (mismo rigor EXACTO que analisis_gate_bucket_propio_28jul.py:
shuffle vs resto de la misma tupla + bootstrap CI90% absoluto + split-half
cronológico + BH-FDR por (familia,activo), piso absoluto pnl_medio>=0
para "bueno_confirmado") aplicado a los dos hallazgos confirmados 26-Ago:

  - Candidata 9 "CANDIDATA9_BOT_CONSENSO": consenso mayoritario de las 84
    bot wallets por mercado, evento = trade EXACTO que hace cruzar a
    mayoría estricta (sin look-ahead, ver analisis_candidata9_v2_
    sinlookahead_26ago.py). Todas las (activo,marco) con datos.
  - Candidata 10 "CANDIDATA10_CROSSACTIVO": confirmación cruzada BTC
    (misma wallet, 2 activos, ventana 30min, solo confirmaciones PREVIAS
    -- ver analisis_candidata10_v2_sinlookahead_26ago.py). Solo BTC (único
    activo con n suficiente en el grupo "sin confirmar" para el contraste
    original).

pnl_neto con la fórmula exacta del proyecto: gross_win=(1-ask)/ask,
fee 7% -- import directo de kelly_precio_gate._familia() para agrupar
BH-FDR, e import directo de shuffle_test/bh_fdr_signif de
analisis_gate_bucket_propio_28jul.py (nunca duplicar la fórmula).

Solo lectura, escribe data/shadow/candidata9_10_gate_bucket.json. 15-Sep:
docstring corregido -- CANDIDATA9_BOT_CONSENSO SÍ está en pares_permitidos_
live desde principios de Sep (candidata9_gate_bucket.py::evaluar_para_recheck
lo consulta vía live_trade.py, dinero real). CANDIDATA10_CROSSACTIVO sigue
exploratoria, fuera de pares_permitidos_live/candidatos_evaluacion_live.
"""
import csv
import json
import math
import sys
from collections import defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_gate_bucket_propio_28jul import (  # noqa: E402
    shuffle_test, bh_fdr_signif, UMBRAL_ABSOLUTO_EUR, bootstrap_absoluto, rescatar_via_absoluta,
)
from analisis_bot_wallets_gate_bucket_25ago import (  # noqa: E402
    _degradar, _cargar_pnl_real_crudo, _cargar_historial_abs_previo, F_KELLY,
    _cargar_fillability_por_bucket,
)
from gate_confirmacion_historial import cargar_historial_previo, veredicto_con_tolerancia  # noqa: E402
import ballenas_cross_check as bcc  # noqa: E402 -- refuerzo informativo, ver docstring del módulo

IN_BOTS = REPO / "data/shadow/bot_wallets_gate_bucket_fase0.csv"
OUT = REPO / "data/shadow/candidata9_10_gate_bucket.json"
EXECUTOR_C9 = REPO / "data/shadow/candidata9_bot_consenso_executor.csv"

ESTRATEGIAS_CANDIDATA9_10 = ("CANDIDATA9_BOT_CONSENSO", "CANDIDATA10_CROSSACTIVO")

STEP = 0.05
N_MIN = 15
P_MAX = 0.05
FEE = 0.07
VENTANA_MIN_C10 = 30
N_MIN_BOTS_C9 = 3
# 31-Ago (/code-review sesión, pendiente #3 checkpoint 31-Ago): igual que
# analisis_bot_wallets_gate_bucket_25ago.py (mismo IN_BOTS) -- un ask
# capturado no implica profundidad real, mismo hueco ya corregido para
# Wallet Mirror el 10-Ago. Verificado con datos reales: Candidata9
# sobrevive limpio en sus 4 buckets confirmados (n_fillable>=15 en todos);
# Candidata10#BTC#60min[0.15,0.20) se queda sin evidencia suficiente
# (n_fillable=4<15, no concluyente -- no confirma ni refuta).
RATIO_MIN = 5.0


def bucket(p):
    return round(math.floor(p / STEP + 1e-9) * STEP, 4)


def pnl_neto(ask, acierto):
    gross_win = (1 - ask) / ask
    return gross_win * (1 - FEE) if acierto else -1.0


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def to_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def eventos_candidata9():
    """tupla_str -> [(ts, ask, pnl), ...] para TODAS las (activo,marco)."""
    por_mercado = defaultdict(list)
    with open(IN_BOTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("outcome_real"):
                continue
            por_mercado[r["condition_id"]].append(r)

    eventos = defaultdict(list)
    for cond, filas in por_mercado.items():
        if len(filas) < N_MIN_BOTS_C9:
            continue
        votos_final = defaultdict(int)
        for r in filas:
            votos_final[r["lado_wallet"]] += 1
        if len(votos_final) == 1:
            continue
        lado_mayoria = max(votos_final, key=votos_final.get)
        n_mayoria = votos_final[lado_mayoria]
        n_total = sum(votos_final.values())
        if n_mayoria == n_total - n_mayoria:
            continue
        activo = filas[0]["activo"]
        marco = filas[0]["marco"]
        outcome = filas[0]["outcome_real"]

        filas_ordenadas = sorted(filas, key=lambda r: parse_ts(r["trade_timestamp"]))
        cuenta = defaultdict(int)
        trigger = None
        for r in filas_ordenadas:
            cuenta[r["lado_wallet"]] += 1
            resto = sum(v for k, v in cuenta.items() if k != lado_mayoria)
            if cuenta[lado_mayoria] > resto and r["lado_wallet"] == lado_mayoria:
                trigger = r
                break
        if trigger is None:
            continue

        ask = to_float(trigger["mejor_ask_deteccion"])
        if ask is None or not (0.0 < ask < 1.0):
            continue
        ratio = to_float(trigger.get("ratio_vs_stake_deteccion", ""))
        if ratio is None or ratio < RATIO_MIN:
            continue
        acierto = 1 if lado_mayoria == outcome else 0
        pnl = pnl_neto(ask, acierto)
        ts = parse_ts(trigger["trade_timestamp"])
        tupla_str = f"CANDIDATA9_BOT_CONSENSO#{activo}#{marco}"
        eventos[tupla_str].append((ts, ask, pnl))
    return eventos


def eventos_candidata10():
    """tupla_str -> [(ts, ask, pnl), ...] para CUALQUIER activo, grupo con_confirm.

    11-Sep: generalizado de "solo BTC" a todos los activos -- la
    restricción original (26-Ago) era por falta de n en el grupo
    "sin_confirmar" para ETH/SOL en ese momento (`analisis_candidata10_
    v2_sinlookahead_26ago.py`), no una limitación estructural del
    mecanismo. Han pasado >2 semanas más de acumulación en
    bot_wallets_gate_bucket_fase0.csv desde entonces -- comprobar si
    ahora hay n suficiente en más activos antes de descartarlos.

    16-Sep, fix de rendimiento (causa raíz real del timeout de
    vigia_candidata9_10_gate_bucket, diagnosticado con conteo real de
    iteraciones -- NO era ballenas_cross_check.consultar(), que ya
    cachea por mtime): el bucle original comparaba cada trade de una
    wallet contra TODOS sus trades previos (`trs_ts[:idx]`), O(k^2) por
    wallet. Con wallets de hasta 24.321 trades, la suma de k^2 sobre las
    wallets con >=2 activos medía 4.600 millones de iteraciones -- eso
    explica el timeout incluso a 2700s. Reemplazado por una ventana
    deslizante (deque) matemáticamente equivalente: como `trs_ts` ya
    está ordenado por tiempo y la condición original exige
    `(ts_i-ts_j).total_seconds()<=VENTANA_MIN_C10*60`, cualquier trade
    que caiga fuera de esa ventana respecto a ts_i también caerá fuera
    respecto a cualquier ts posterior (los timestamps solo crecen) -- se
    puede purgar permanentemente del extremo antiguo sin cambiar el
    resultado. O(k) amortizado por wallet."""
    filas = []
    with open(IN_BOTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("outcome_real") or not r.get("acierto"):
                continue
            filas.append(r)

    por_wallet = defaultdict(list)
    for r in filas:
        por_wallet[r["wallet"]].append(r)

    eventos = defaultdict(list)
    ventana_s = VENTANA_MIN_C10 * 60
    for w, trs in por_wallet.items():
        if len({t["activo"] for t in trs}) < 2:
            continue
        trs_ts = sorted([(parse_ts(t["trade_timestamp"]), t) for t in trs], key=lambda x: x[0])
        ventana = deque()  # (ts, activo, lado_wallet) de trades recientes (<=ventana_s)
        for ts_i, ti in trs_ts:
            while ventana and (ts_i - ventana[0][0]).total_seconds() > ventana_s:
                ventana.popleft()
            confirm = any(
                activo != ti["activo"] and lado == ti["lado_wallet"]
                for _, activo, lado in ventana
            )
            ventana.append((ts_i, ti["activo"], ti["lado_wallet"]))
            if not confirm:
                continue
            ask = to_float(ti["mejor_ask_deteccion"])
            if ask is None or not (0.0 < ask < 1.0):
                continue
            ratio = to_float(ti.get("ratio_vs_stake_deteccion", ""))
            if ratio is None or ratio < RATIO_MIN:
                continue
            acierto = int(ti["acierto"])
            pnl = pnl_neto(ask, acierto)
            marco = ti["marco"]
            tupla_str = f"CANDIDATA10_CROSSACTIVO#{ti['activo']}#{marco}"
            eventos[tupla_str].append((ts_i, ask, pnl))
    return eventos


def _familia(tupla_str):
    return tupla_str.split("#")[0]


def _pnl_real_por_bucket_desde_crudo(pnl_real_crudo: dict) -> dict:
    """Bucketiza (grid 0.05) el crudo de arriba -- formato exacto que
    _degradar() espera ({clave_str: {bucket_str: [pnl,...]}})."""
    out = defaultdict(lambda: defaultdict(list))
    for clave_str, pares in pnl_real_crudo.items():
        for ask, pnl in pares:
            out[clave_str][f"{bucket(ask):.2f}"].append(pnl)
    return {k: dict(v) for k, v in out.items()}


def main():
    eventos = defaultdict(list)
    for tupla_str, evs in eventos_candidata9().items():
        eventos[tupla_str].extend(evs)
    for tupla_str, evs in eventos_candidata10().items():
        eventos[tupla_str].extend(evs)

    print(f"Tuplas (candidata9+10): {len(eventos)}")
    pnl_real_por_bucket = _pnl_real_por_bucket_desde_crudo(
        _cargar_pnl_real_crudo(ESTRATEGIAS_CANDIDATA9_10))
    # 16-Sep tarde: fill-ability real SOLO existe para CANDIDATA9_BOT_CONSENSO
    # (candidata9_bot_consenso_executor.py) -- CANDIDATA10_CROSSACTIVO no
    # tiene ejecutor propio (exploratoria, fuera de pares_permitidos_live),
    # así que nunca se le pasa este dict a _degradar() (ver bucle de abajo,
    # fillability_por_bucket=None para ella -- fail-neutral, no fail-closed
    # por un hueco de infraestructura que no le corresponde).
    #
    # /code-review 16-Sep (hallazgo real): eventos_candidata9() bucketiza
    # con el ask de DETECCIÓN (mejor_ask_deteccion, de bot_wallets_gate_
    # bucket_fase0.csv) -- usar aquí "ask_decision" (post-Kelly/circuit-
    # breaker, ya movido por degradacion_ask_pct) mezclaba fill-ability de
    # una población de precio distinta bajo la misma etiqueta de bucket.
    # "ask_deteccion" es el campo equivalente en el propio ejecutor (mismo
    # instante conceptual que mejor_ask_deteccion), alinea los dos lados.
    fillability_c9 = _cargar_fillability_por_bucket(
        EXECUTOR_C9, col_bucket="ask_deteccion", col_fill="sigue_fillable_en_decision",
        arquetipo_fijo="CANDIDATA9_BOT_CONSENSO")

    # 15-Sep, petición explícita Javi ("que la confirmación de CANDIDATA9 sea
    # igual de exigente que la de SNIPER/DISPERSO"): esta familia SÍ está en
    # pares_permitidos_live (a diferencia de lo que dice el docstring del
    # módulo, desactualizado desde que se promocionó) pero, a diferencia de
    # bot_wallets_gate_bucket (SNIPER/DISPERSO/WEEKLY_*), nunca se conectó al
    # guard de estabilidad multi-día (gate_confirmacion_historial.py, 01-Sep)
    # -- podía confirmar "bueno_confirmado" con el BH-FDR de un solo día,
    # mientras el resto de la familia P-GALLINA exige 2 de los últimos 3 días
    # antes de promover (malo_confirmado sigue siendo inmediato, asimetría
    # deliberada). Mismo patrón EXACTO que analisis_bot_wallets_gate_bucket_
    # 25ago.py -- namespaces independientes para vía relativa y vía absoluta
    # (ver _cargar_historial_abs_previo: mezclar los dos permitía "reconfirmar"
    # bueno con solo 2 días de rescate absoluto sobre un malo_confirmado
    # relativo).
    historial_previo = cargar_historial_previo(OUT, anidado_por_bucket=True)
    historial_abs_previo = _cargar_historial_abs_previo(OUT)

    pendientes = []
    candidatos_abs = []  # vía absoluta (12-Sep), ver UMBRAL_ABSOLUTO_EUR
    resultado = {}
    for tupla_str, filas in eventos.items():
        if len(filas) < N_MIN:
            # Mismo patrón que analisis_bot_wallets_gate_bucket_25ago.py: un
            # día flojo a nivel tupla no debe perder el historial_crudo ya
            # acumulado a nivel bucket. /code-review 15-Sep: el hermano
            # también preserva SOLO historial_crudo (vía relativa) aquí,
            # descartando en silencio historial_crudo_abs (vía absoluta) --
            # exactamente el hueco de "un día flojo no puede entorpecer esto"
            # que gate_confirmacion_historial.py existe para evitar, aquí a
            # nivel tupla. Se corrige en este módulo preservando ambos
            # namespaces por separado (nunca mezclados, mismo motivo que
            # _cargar_historial_abs_previo).
            historial_tupla = historial_previo.get(tupla_str, {})
            historial_tupla_abs = historial_abs_previo.get(tupla_str, {})
            buckets_previos = set(historial_tupla) | set(historial_tupla_abs)
            resultado[tupla_str] = {}
            for b in buckets_previos:
                hist = historial_tupla.get(b)
                hist_abs = historial_tupla_abs.get(b)
                if not hist and not hist_abs:
                    continue
                entrada = {"veredicto": "sin_concluir"}
                if hist:
                    entrada["historial_crudo"] = hist
                if hist_abs:
                    entrada["historial_crudo_abs"] = hist_abs
                resultado[tupla_str][b] = entrada
            continue

        _, activo, marco = tupla_str.split("#")
        por_bucket = defaultdict(list)
        for ts, ask, pnl in filas:
            por_bucket[bucket(ask)].append((ts, pnl))

        tabla = {}
        for b in sorted(por_bucket):
            dentro = por_bucket[b]
            fuera = [(ts, pnl) for bb, fs in por_bucket.items() if bb != b for ts, pnl in fs]
            n_d = len(dentro)
            pnl_d = [pnl for _, pnl in dentro]
            pnl_f = [pnl for _, pnl in fuera]
            media_d = sum(pnl_d) / n_d
            g_kelly = sum(math.log(1 + F_KELLY * x) for x in pnl_d) / n_d if n_d > 0 else None
            historial_semilla = historial_previo.get(tupla_str, {}).get(f"{b:.2f}", [])
            # 15-Sep (petición explícita Javi, "masterizar" pt.4, refuerzo
            # nunca veto): `ask` ya en perspectiva de decisión (el lado que
            # de verdad dispara la mayoría), consultado como "BUY_YES"
            # (misma convención que el resto de gates portados hoy).
            ballenas = bcc.consultar(activo, marco, b, "BUY_YES")

            entrada = {"n": n_d, "pnl_medio": round(media_d, 4),
                       "g_kelly_f10": round(g_kelly, 5) if g_kelly is not None else None,
                       "diff_vs_resto": round(media_d - (sum(pnl_f) / len(pnl_f)), 4) if pnl_f else None,
                       "tercio3_n": 0, "tercio3_pnl_medio": None,
                       "ballenas_hit_rate_yes": ballenas["hit_rate_yes"], "ballenas_n": ballenas["n"],
                       "ballenas_coincide": ballenas["coincide"],
                       "shuffle_p": None, "split_half_diff": None,
                       "ci90_bootstrap_absoluto": None, "veredicto": "sin_concluir",
                       "historial_crudo": historial_semilla}
            tabla[f"{b:.2f}"] = entrada

            if n_d >= N_MIN:
                # 12-Sep (decisión explícita Javi, ver UMBRAL_ABSOLUTO_EUR en
                # analisis_gate_bucket_propio_28jul.py): vía absoluta,
                # independiente de pnl_f. Reemplaza el bootstrap ad-hoc que
                # tenía este módulo (semilla no determinista, hash() varía
                # entre procesos) por el compartido -- mismo criterio "nunca
                # duplicar la fórmula" del docstring de este fichero.
                ci_lo90, ci_hi90, p_valor_abs = bootstrap_absoluto(
                    pnl_d, seed_key=f"abs#{tupla_str}#{b:.2f}")
                entrada["ci90_bootstrap_absoluto"] = [round(ci_lo90, 4), round(ci_hi90, 4)]
                entrada["p_valor_abs"] = round(p_valor_abs, 4)
                dentro_sorted = sorted(dentro, key=lambda x: x[0])
                # 16-Sep (ver docstring de _degradar() -- criterio de
                # tendencia reciente, caso real que lo motivó: CANDIDATA9_
                # BOT_CONSENSO#BNB#5min[0.25) pasaba el bootstrap CI90%
                # limpio pero decaía a negativo en el último tercio.
                # /code-review: reusa dentro_sorted en vez de ordenar dos
                # veces -- la primera versión ordenaba para TODOS los
                # buckets, incluso por debajo de N_MIN, inflando runtime).
                _k_tend = n_d // 3
                # /code-review 16-Sep (hallazgo real, mismo fix en los 3
                # ficheros): dentro_sorted[2*_k_tend:] dejaba caer el resto de
                # la división en el tercio3, ensanchando la ventana "reciente"
                # más allá de 1/3 para n no múltiplo de 3. Toma exactamente
                # los últimos _k_tend elementos -- definición estable.
                _tercio3 = dentro_sorted[n_d - _k_tend:] if _k_tend > 0 else []
                tercio3_n = len(_tercio3)
                if tercio3_n >= 15:
                    entrada["tercio3_n"] = tercio3_n
                    entrada["tercio3_pnl_medio"] = round(sum(pnl for _, pnl in _tercio3) / tercio3_n, 4)
                mid = n_d // 2
                m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
                split_half_abs = None
                if len(m1) >= 5 and len(m2) >= 5:
                    m1_abs = sum(pnl for _, pnl in m1) / len(m1)
                    m2_abs = sum(pnl for _, pnl in m2) / len(m2)
                    split_half_abs = [round(m1_abs, 4), round(m2_abs, 4)]
                    entrada["split_half_absoluto"] = split_half_abs
                candidatos_abs.append({"clave_str": tupla_str, "bucket": f"{b:.2f}",
                                        "entrada": entrada, "p_valor_abs": p_valor_abs,
                                        "split_half_abs": split_half_abs})
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
                                            "p": p_valor, "diff": diff})
        resultado[tupla_str] = tabla

    por_familia_activo = defaultdict(list)
    for idx, p in enumerate(pendientes):
        partes = p["tupla_str"].split("#")
        activo = partes[1] if len(partes) > 1 else "?"
        clave = (_familia(p["tupla_str"]), activo)
        por_familia_activo[clave].append(idx)

    sobreviven = set()
    for (familia, activo), indices in por_familia_activo.items():
        p_valores_grupo = [pendientes[i]["p"] for i in indices]
        sobreviven_grupo = bh_fdr_signif(p_valores_grupo, q=P_MAX)
        sobreviven |= {indices[j] for j in sobreviven_grupo}
        print(f"  familia={familia} activo={activo}: {len(indices)} tests candidatos, "
              f"{len(sobreviven_grupo)} sobreviven BH-FDR q={P_MAX}")

    print(f"\nTests candidatos: {len(pendientes)} | sobreviven BH-FDR: {len(sobreviven)}")

    veredictos_nuevos = []
    for idx, p in enumerate(pendientes):
        if idx not in sobreviven:
            continue
        ci = p["entrada"]["ci90_bootstrap_absoluto"]
        if p["diff"] < 0:
            veredicto = "malo_confirmado"
        elif p["entrada"]["pnl_medio"] >= 0 and ci is not None and ci[0] > 0:
            veredicto = "bueno_confirmado"
        else:
            continue
        fillability_arg = fillability_c9 if p["tupla_str"].startswith("CANDIDATA9_BOT_CONSENSO#") else None
        veredicto_crudo, nota_payout, nota_real, nota_concentracion, nota_tendencia, nota_fill, g_kelly = _degradar(
            veredicto, p["entrada"], p["tupla_str"], p["bucket"], pnl_real_por_bucket, fillability_arg)
        p["entrada"]["veredicto_crudo_hoy"] = veredicto_crudo
        historial_bucket = historial_previo.get(p["tupla_str"], {}).get(p["bucket"])
        veredicto, p["entrada"]["historial_crudo"] = veredicto_con_tolerancia(
            veredicto_crudo, historial_bucket)
        resultado[p["tupla_str"]][p["bucket"]]["veredicto"] = veredicto
        if veredicto == "sin_concluir":
            continue
        marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
        b = p["bucket"]
        veredictos_nuevos.append(
            f"{marca} {p['tupla_str']} [{b},{float(b)+STEP:.2f}) n={p['entrada']['n']} "
            f"pnl_medio={p['entrada']['pnl_medio']:+.3f} g_kelly={g_kelly:+.5f} "
            f"p={p['p']:.4f} {veredicto}{nota_payout}{nota_real}{nota_concentracion}{nota_tendencia}{nota_fill}"
        )

    # 12-Sep, vía absoluta (decisión explícita Javi, ver UMBRAL_ABSOLUTO_EUR
    # en analisis_gate_bucket_propio_28jul.py): rescata buckets rentables de
    # sobra que la vía relativa dejó en malo_confirmado/sin_concluir solo
    # por ser peores que un vecino de la misma tupla.
    rescatados = rescatar_via_absoluta(
        candidatos_abs, agrupador_fn=lambda tupla_str: (_familia(tupla_str), tupla_str.split("#")[1]))
    for c in rescatados:
        b = c["bucket"]
        fillability_arg = fillability_c9 if c["clave_str"].startswith("CANDIDATA9_BOT_CONSENSO#") else None
        veredicto_crudo_abs, nota_payout, nota_real, nota_concentracion, nota_tendencia, nota_fill, g_kelly = _degradar(
            "bueno_confirmado", c["entrada"], c["clave_str"], b, pnl_real_por_bucket, fillability_arg)
        historial_bucket = historial_abs_previo.get(c["clave_str"], {}).get(b)
        veredicto, c["entrada"]["historial_crudo_abs"] = veredicto_con_tolerancia(
            veredicto_crudo_abs, historial_bucket)
        c["entrada"]["veredicto_crudo_hoy_abs"] = veredicto_crudo_abs
        if veredicto == "sin_concluir":
            # NUNCA pisa el veredicto ya decidido por la vía relativa --
            # mismo criterio que analisis_bot_wallets_gate_bucket_25ago.py.
            # /code-review 15-Sep: "via" NO se marca aquí -- c["entrada"] es
            # el MISMO objeto que resultado[clave_str][b] (ver "tabla[...] =
            # entrada" más arriba), así que fijar "via" antes de este
            # continue lo dejaba corrupto (marcado "absoluta") incluso
            # cuando el veredicto vigente lo puso la vía relativa. El
            # hermano (analisis_bot_wallets_gate_bucket_25ago.py) tiene el
            # mismo orden -- pendiente de aplicar allí también.
            continue
        resultado[c["clave_str"]][b]["veredicto"] = veredicto
        resultado[c["clave_str"]][b]["via"] = "absoluta"
        marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
        veredictos_nuevos.append(
            f"{marca} [vía absoluta] {c['clave_str']} [{b},{float(b)+STEP:.2f}) n={c['entrada']['n']} "
            f"pnl_medio={c['entrada']['pnl_medio']:+.3f} g_kelly={g_kelly:+.5f} "
            f"p_abs={c['p_valor_abs']:.4f} {veredicto}{nota_payout}{nota_real}{nota_concentracion}{nota_tendencia}{nota_fill}"
        )

    print(f"\n{len(veredictos_nuevos)} bucket(s) con veredicto tras BH-FDR:")
    for linea in veredictos_nuevos:
        print(f"  {linea}")

    OUT.write_text(json.dumps(resultado, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nEscrito {OUT}")


if __name__ == "__main__":
    main()
