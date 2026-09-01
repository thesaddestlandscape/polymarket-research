#!/usr/bin/env python3
"""analisis_wallet_mirror_gate_bucket_10ago.py — gate permanente por
micro-bucket de precio real para Wallet Mirror (P24), mismo mecanismo y
mismo rigor que gate_bucket_propio.py (28-Jul) pero aplicado a una fuente
de datos distinta (Wallet Mirror no pasa por results.csv/shadow_predict.py,
así que el gate original nunca lo cubre).

Origen (10-Ago, petición explícita Javi: "conecta la solución a selección
adversa/payout asimétrico que ya tenemos, agota TODAS las opciones antes
de cerrar"): el análisis agregado por (activo,jugada_grande) refutaba
Wallet Mirror SEGUIR con ask real -- desagregado por micro-bucket de
precio (script de una sola sesión, analisis_wallet_mirror_microbucket_
precio_10ago.py) apareció SEGUIR#ETH#no_grande#ask[0.50,0.55) con edge
real (wilson90lo=58.6%>breakeven=53.6%). Este script convierte ese
hallazgo puntual en mecanismo RECURRENTE (cron diario, como el resto del
proyecto) para que el veredicto se actualice solo conforme crece n, en
vez de depender de que alguien re-corra el script a mano.

Añade una desagregación más que el análisis original: MARCO temporal
(5min/15min) -- lección reforzada el mismo día (CLAUDE.md pt.17): el
bucket ETH[0.50,0.55) agregaba 5min+15min, y 15min resultó mucho más
robusto (wilson90lo=58.1%, margen +4.5pp) que 5min (wilson90lo=54.1%,
margen +0.4pp, al límite). Clave del gate: (tipo, activo, marco,
jugada_grande, bucket).

Rigor idéntico a gate_bucket_propio.py: n>=15, shuffle test (pnl_dentro
vs pnl_fuera del mismo (activo,marco,jugada_grande)), split-half
cronológico, BH-FDR por (activo,marco,jugada_grande) -- mismo nivel de
agrupación que la corrección por (familia,activo) del gate original.

pnl_neto calculado con la fórmula exacta (gross_win=(1-ask)/ask, fee 7%)
sobre el ASK REAL de wallet_mirror_executor_dryrun.csv en el momento de
decisión (no precio_wallet, aproximación optimista ya refutada hoy) +
outcome real de wallet_mirror_sniper_dry_run.csv.

Solo lectura de sus fuentes, solo ESCRIBE data/shadow/wallet_mirror_gate_
bucket.json -- no toca ningún gate real, WALLET_MIRROR no puede estar en
pares_permitidos_live (tupla sintética, ver wallet_mirror_executor_dryrun.py).
"""
import csv
import json
import math
import sys
import zlib
from collections import defaultdict
from pathlib import Path

import numpy as np

from gate_confirmacion_historial import cargar_historial_previo, veredicto_con_tolerancia

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import shadow_postmortem as sp  # noqa: E402 -- reusa TWAP_MARCOS_AFECTADOS/TWAP_FECHA_CAMBIO

EXECUTOR = REPO / "data/shadow/wallet_mirror_executor_dryrun.csv"
SNIPER = REPO / "data/shadow/wallet_mirror_sniper_dry_run.csv"
TRADES_REAL = REPO / "data/live/trades.csv"
OUT = REPO / "data/shadow/wallet_mirror_gate_bucket.json"

STEP = 0.05
N_MIN = 40  # 01-Sep: subido de 15 a 40 (n>=40 = estandar de confirmacion del
# proyecto, CLAUDE.md) tras confirmar que buckets confirmados con n=30-65
# se revertian a sin_concluir/malo_confirmado horas despues de disparar
# dinero real (vigia_wallet_mirror_postfix.py n=15 hit=26.7% pnl=-6.33EUR,
# ver nota _pares_walletmirror_pausa_nota_2026-09-01 en config_live.json)
P_MAX = 0.05
ITERS = 2000
FEE = 0.07
F_KELLY = 0.10  # 29-Ago: mismo default que analisis_log_growth.py/gate_bucket_propio.py (P28/CLAUDE.md pt.14)


def bucket(p):
    return round(math.floor(p / STEP + 1e-9) * STEP, 4)


def pnl_neto(ask, acierto):
    gross_win = (1 - ask) / ask
    return gross_win * (1 - FEE) if acierto else -1.0


def cargar_outcomes():
    out = {}
    with open(SNIPER, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("acierto") not in ("0", "1"):
                continue
            out[(r["wallet"], r["market_slug"], r["trade_timestamp"])] = int(r["acierto"])
    return out


def cargar_filas():
    """11-Ago (petición explícita Javi, auditoría de huecos TWAP):
    excluye filas pre-07-Ago de marcos afectados (5min/15min/240min,
    reusa shadow_postmortem.TWAP_MARCOS_AFECTADOS/TWAP_FECHA_CAMBIO) --
    hallazgo real: este script no tenía NINGÚN filtro de régimen, mismo
    hueco ya cerrado hoy en shadow_postmortem.py/gate_bucket_propio.py/
    kelly_precio_gate.py/live_trade.py::_clv_tupla. Los 3 candidatos de
    Wallet Mirror viven en marcos afectados (5min/15min) y toda su
    ventana de datos (03->10-Ago) cruza el cambio TWAP (07-Ago) -- su
    veredicto podía estar contaminado igual que los demás mecanismos."""
    outcomes = cargar_outcomes()
    # clave de grupo: (tipo, activo, marco, jugada_grande) -> [(ts, ask, pnl), ...]
    grupos = defaultdict(list)
    with open(EXECUTOR, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("sigue_fillable_en_decision") != "1":
                continue
            clave_out = (r["wallet"], r["market_slug"], r["trade_timestamp"])
            ac = outcomes.get(clave_out)
            if ac is None:
                continue
            try:
                ask = float(r["ask_decision"])
            except (TypeError, ValueError):
                continue
            if not (0.0 < ask < 1.0):
                continue
            marco = r.get("marco", "?")
            if sp.es_pre_twap(marco, r.get("timestamp_utc", "")):
                continue
            pnl = pnl_neto(ask, ac)
            tipo = r.get("tipo", "?")
            activo = r.get("activo", "?")
            grande = "1" if r.get("es_jugada_grande") == "1" else "0"
            grupos[(tipo, activo, marco, grande)].append((r["timestamp_utc"], ask, pnl))
    return grupos


def shuffle_test(a, b, seed_key, iters=ITERS):
    """20-Ago (fix real, hallazgo del vigía spameando "nuevo veredicto"
    sin parar para el mismo bucket con los mismos datos, n y pnl idénticos
    pero shuffle_p distinto cada ciclo): antes usaba un único _rng module-
    level compartido entre TODAS las llamadas del bucle de main() -- con
    semilla fija (42) pero ESTADO COMPARTIDO, el resultado para un bucket
    concreto dependía de cuántas llamadas a shuffle_test() lo precedían en
    ESE ciclo, que cambia según cuántos otros grupos/buckets cruzan N_MIN
    ese día. Efecto práctico: no determinista por bucket pese a tener
    semilla. Fix: un generador nuevo por llamada, seedeado por un hash
    estable de `seed_key` (clave_str+bucket) -- mismo bucket, mismo par de
    poblaciones -> mismo p_valor siempre, sin importar el orden de
    iteración ni cuántos otros grupos se evalúen ese ciclo."""
    rng = np.random.default_rng(zlib.crc32(seed_key.encode("utf-8")))
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    na, nb = len(a), len(b)
    diff_real = a.mean() - b.mean()
    todos = np.concatenate([a, b])
    n = na + nb
    idx = rng.random((iters, n)).argsort(axis=1)
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


def _cargar_pnl_real_por_bucket() -> dict:
    """{clave_str: {bucket_str: [pnl_neto_eur, ...]}} de trades.csv REALES
    (WALLET_MIRROR, CLOSED) -- verdad de suelo, no proxy.

    31-Ago (petición explícita Javi, "solucionalo" -- ya son 18 trades
    reales -7,04€ 33,3% win-rate pese al veto de payout asimétrico del
    29-Ago): el veredicto de este gate se calcula ENTERO sobre el log del
    ejecutor (EXECUTOR arriba, decisiones fillable, nunca lo que el dinero
    real terminó haciendo en esa tupla/bucket exacta) -- nunca se había
    contrastado contra trades.csv. Mismo espíritu que el veto de payout
    asimétrico (degrada, nunca promueve): si YA hay evidencia real
    (n_real>=2, mismo umbral mínimo de "no ruido de una sola vez" que el
    resto del proyecto) y esa evidencia es negativa, no seguir confiando
    ciegamente en el proxy del ejecutor para ESE bucket concreto.

    Fail-safe: fichero ausente/corrupto -> {} (comportamiento idéntico al
    de antes de este cambio, ningún bucket se degrada)."""
    out = defaultdict(lambda: defaultdict(list))
    try:
        with open(TRADES_REAL, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r.get("strategy") != "WALLET_MIRROR" or r.get("status") != "CLOSED":
                    continue
                notas = r.get("notas") or ""
                if "tipo=SEGUIR" in notas:
                    tipo = "SEGUIR"
                elif "tipo=FADE" in notas:
                    tipo = "FADE"
                else:
                    continue
                grande = "1" if "grande=1" in notas else "0"
                subtype = r.get("subtype") or ""
                if "#" not in subtype:
                    continue
                activo, marco = subtype.split("#", 1)
                try:
                    ask = float(r.get("entry_price") or "")
                    pnl = float(r.get("pnl_neto_eur") or "")
                except (TypeError, ValueError):
                    continue
                if not (0.0 < ask < 1.0):
                    continue
                clave_str = f"{tipo}#{activo}#{marco}#{grande}"
                out[clave_str][f"{bucket(ask):.2f}"].append(pnl)
    except Exception:
        return {}
    return {k: dict(v) for k, v in out.items()}


def main():
    grupos = cargar_filas()
    print(f"Grupos (tipo,activo,marco,grande): {len(grupos)}")
    historial_previo = cargar_historial_previo(OUT, anidado_por_bucket=True)
    pnl_real_por_bucket = _cargar_pnl_real_por_bucket()

    resultado = {}  # "tipo#activo#marco#grande" -> {bucket_str: entrada}
    pendientes = []
    for clave, filas in grupos.items():
        tipo, activo, marco, grande = clave
        clave_str = f"{tipo}#{activo}#{marco}#{grande}"
        if len(filas) < N_MIN:
            # /code-review 01-Sep (mismo patrón que gate_bucket_propio_
            # 28jul.py): no perder el historial_crudo de los buckets de
            # esta clave si hoy cae por debajo de N_MIN a nivel clave -- un
            # día flojo no es un día MALO a nivel bucket.
            historial_clave = historial_previo.get(clave_str, {})
            resultado[clave_str] = {
                b: {"veredicto": "sin_concluir", "historial_crudo": hist}
                for b, hist in historial_clave.items() if hist
            }
            continue
        por_bucket = defaultdict(list)
        for ts, ask, pnl in filas:
            por_bucket[bucket(ask)].append((ts, pnl))

        tabla = {}
        for b in sorted(por_bucket):
            dentro = por_bucket[b]
            fuera = [(ts, pnl) for bb, fs in por_bucket.items() if bb != b for ts, pnl in fs]
            n_d = len(dentro)
            pnl_d = [pnl for _, pnl in dentro]
            media_d = sum(pnl_d) / n_d
            # 29-Ago (hallazgo real, sesión de racha de pérdidas reales en
            # WALLET_MIRROR -7,01€/16 trades): este módulo nunca tuvo el
            # veto de payout asimétrico (Kelly g(f)) que sí protege a
            # GBM_LATE/FAVORITO/BALLENAS/MOMENTUM_IBS vía gate_bucket_
            # propio.py::_veto_fillable() señal #2 (CLAUDE.md pt.14/P28) --
            # WALLET_MIRROR tiene su propio gate separado porque nunca
            # escribe en results.csv, y ese gate propio se quedó sin la
            # actualización del 28-Ago. `pnl_d` aquí ya es el retorno neto
            # por trade (fee 7% aplicado en pnl_neto() arriba, mismo
            # concepto que analisis_log_growth.py::_retorno()) -- misma
            # fórmula g(f)=mean(ln(1+f*x)), f=0.10 (F_KELLY, mismo default
            # que el resto del proyecto), NO reimplementa _retorno() porque
            # la forma del dato de entrada es distinta (ask/acierto ya
            # reducidos a pnl, no una fila de results.csv), pero es la
            # MISMA matemática.
            g_kelly = sum(math.log(1 + F_KELLY * x) for x in pnl_d) / n_d if n_d > 0 else None
            # /code-review 01-Sep: sembrar historial_crudo aquí -- si este
            # bucket no sobrevive más abajo (BH-FDR/piso), esta entrada por
            # defecto es la que queda escrita, y sin la semilla perdía el
            # historial acumulado sin que hubiera pasado un día MALO.
            historial_semilla = historial_previo.get(clave_str, {}).get(f"{b:.2f}", [])
            entrada = {"n": n_d, "pnl_medio": round(media_d, 4), "g_kelly_f10": round(g_kelly, 5),
                       "shuffle_p": None, "split_half": None, "veredicto": "sin_concluir",
                       "historial_crudo": historial_semilla}
            tabla[f"{b:.2f}"] = entrada
            if n_d >= N_MIN and fuera:
                pnl_f = [pnl for _, pnl in fuera]
                diff, p_valor = shuffle_test(pnl_d, pnl_f, seed_key=f"{clave_str}#{b:.2f}")
                entrada["shuffle_p"] = round(p_valor, 4)
                dentro_sorted = sorted(dentro, key=lambda x: x[0])
                mid = n_d // 2
                m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
                if len(m1) >= 5 and len(m2) >= 5:
                    media_fuera = sum(pnl_f) / len(pnl_f)
                    d1 = sum(pnl for _, pnl in m1) / len(m1) - media_fuera
                    d2 = sum(pnl for _, pnl in m2) / len(m2) - media_fuera
                    entrada["split_half"] = [round(d1, 4), round(d2, 4)]
                    consistente = (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)
                    if consistente:
                        pendientes.append({"clave_str": clave_str, "bucket": f"{b:.2f}",
                                            "entrada": entrada, "p": p_valor, "diff": diff})
        resultado[clave_str] = tabla

    # BH-FDR por (activo,marco,grande) -- mismo nivel de agrupación que
    # gate_bucket_propio.py usa por (familia,activo), aquí no hay familia
    # (todo es Wallet Mirror) así que agrupamos por activo+marco+grande.
    por_grupo = defaultdict(list)
    for idx, p in enumerate(pendientes):
        _, activo, marco, grande = p["clave_str"].split("#")
        por_grupo[(activo, marco, grande)].append(idx)

    sobreviven = set()
    for grupo, indices in por_grupo.items():
        p_valores = [pendientes[i]["p"] for i in indices]
        sobreviven |= {indices[j] for j in bh_fdr_signif(p_valores, q=P_MAX)}

    veredictos_nuevos = []
    veredictos_pendientes_confirmacion = []
    for idx, p in enumerate(pendientes):
        if idx not in sobreviven:
            continue
        if p["diff"] < 0:
            veredicto_crudo = "malo_confirmado"
        elif p["entrada"]["pnl_medio"] >= 0:
            veredicto_crudo = "bueno_confirmado"
        else:
            continue  # piso absoluto, mismo criterio que gate_bucket_propio 08-Ago
        # 29-Ago: veto de payout asimétrico -- degrada bueno_confirmado si
        # el crecimiento compuesto (Kelly g(f=10%)) es <=0 pese a pnl_medio
        # lineal positivo (hit-rate alto con pérdidas grandes raras que se
        # comen el compounding). Mismo criterio que gate_bucket_propio.py::
        # _veto_fillable() señal #2 -- solo puede DEGRADAR, nunca promover.
        nota_payout = ""
        g_kelly = p["entrada"].get("g_kelly_f10")
        if veredicto_crudo == "bueno_confirmado" and g_kelly is not None and g_kelly <= 0:
            veredicto_crudo = "malo_confirmado"
            nota_payout = f" [degradado: payout asimétrico g_kelly(f=10%)={g_kelly:+.5f}<=0]"

        # 31-Ago: veto de verdad-de-suelo -- degrada bueno_confirmado si YA
        # hay trades REALES (no proxy) en este bucket exacto y su pnl medio
        # es negativo. n_real>=2 (mismo umbral mínimo de "no ruido de una
        # sola vez" que el resto del proyecto usa para split-half). Solo
        # puede degradar, nunca promover -- ver _cargar_pnl_real_por_bucket().
        nota_real = ""
        pnls_reales = pnl_real_por_bucket.get(p["clave_str"], {}).get(p["bucket"])
        if veredicto_crudo == "bueno_confirmado" and pnls_reales and len(pnls_reales) >= 2:
            media_real = sum(pnls_reales) / len(pnls_reales)
            if media_real < 0:
                veredicto_crudo = "malo_confirmado"
                nota_real = (f" [degradado: {len(pnls_reales)} trades REALES "
                             f"pnl_medio={media_real:+.3f}€<0]")

        p["entrada"]["veredicto_crudo_hoy"] = veredicto_crudo
        b = p["bucket"]

        # 31-Ago (mismo guard que gate_bucket_propio.py, petición explícita
        # Javi): asimétrico, "malo_confirmado" sigue inmediato (1 día basta
        # para vetar). Este gate ya opera con dinero real hoy (WALLET_MIRROR
        # #BTC, DRY_RUN=False desde 11-Ago) -- máxima cautela.
        # 01-Sep (petición explícita Javi, "un día de mala racha no puede
        # entorpecer esto"): antes exigía el día INMEDIATAMENTE anterior
        # también bueno_confirmado (reset a 1 día flojo). Ahora exige 2 de
        # los últimos 3 días (incluido hoy) vía gate_confirmacion_historial.py.
        historial_bucket = historial_previo.get(p["clave_str"], {}).get(b)
        veredicto, p["entrada"]["historial_crudo"] = veredicto_con_tolerancia(
            veredicto_crudo, historial_bucket)
        if veredicto == "sin_concluir" and veredicto_crudo == "bueno_confirmado":
            veredictos_pendientes_confirmacion.append(
                f"⏳ {p['clave_str']} [{b},{float(b)+STEP:.2f}) n={p['entrada']['n']} "
                f"pnl_medio={p['entrada']['pnl_medio']:+.3f} bueno_confirmado HOY, "
                f"esperando confirmación de mañana"
            )

        p["entrada"]["veredicto"] = veredicto
        if veredicto == "sin_concluir":
            continue
        marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
        veredictos_nuevos.append(
            f"{marca} {p['clave_str']} [{b},{float(b)+STEP:.2f}) "
            f"n={p['entrada']['n']} pnl_medio={p['entrada']['pnl_medio']:+.3f} "
            f"g_kelly={g_kelly:+.5f} p={p['p']:.4f} {veredicto}{nota_payout}{nota_real}"
        )

    print(f"\n{len(veredictos_nuevos)} bucket(s) con veredicto tras BH-FDR:")
    for linea in veredictos_nuevos:
        print(f"  {linea}")
    if veredictos_pendientes_confirmacion:
        print(f"\n{len(veredictos_pendientes_confirmacion)} bucket(s) pendientes de 2ª confirmación mañana:")
        for linea in veredictos_pendientes_confirmacion:
            print(f"  {linea}")

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    print(f"\nGuardado en {OUT}")


if __name__ == "__main__":
    main()
