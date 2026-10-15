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

pnl_neto (07-Oct: comisión REAL del tomador 0,07·p·(1−p) en cada compra; antes 7 % de la ganancia
solo en aciertos) por € arriesgado, una observación por (mercado, lado, bucket) -- ver cargar_filas(),
sobre el ASK REAL de wallet_mirror_executor_dryrun.csv en el momento de
decisión (no precio_wallet, aproximación optimista ya refutada hoy) +
outcome real resuelto en el propio wallet_mirror_executor_dryrun.csv
(columnas outcome_real/acierto, añadidas 13-Sep -- ver wallet_mirror_
executor_dryrun.py --resolver).

⚠️ 13-Sep (bug real encontrado en barrido de salud, ver idea_join_wallet_
mirror_executor_sniper_roto_13sep): ANTES este script cruzaba EXECUTOR
(fillability, roster = wallets_operativas_recientes(), rendimiento
reciente, rota) contra wallet_mirror_sniper_dry_run.csv (outcomes, roster
= cargar_wallets_validadas(), histórico completo) por (wallet,market_
slug,trade_timestamp) -- son DOS POBLACIONES DE WALLETS DISTINTAS por
diseño (13-Ago), y el cruce por clave exacta entre ambas solo emparejaba
~0.3% de las filas (52/16.971 combos wallet+market en común), dando n/p
inestables entre corridas consecutivas sin que cambiara nada real (ej.
SEGUIR#BTC#5min[0.10,0.15) pasó de n=2170,p=0.04 a n=2672,p=0.752 en
<1h). Fix: outcome resuelto DIRECTAMENTE en el CSV de EXECUTOR (misma
mecánica --resolver que ya usaba sniper.py) -- ya no hace falta cruzar
con ningún otro fichero, el gate mide exactamente la población que
decide con dinero real.

Solo lectura de sus fuentes, solo ESCRIBE data/shadow/wallet_mirror_gate_
bucket.json -- no toca ningún gate real, WALLET_MIRROR no puede estar en
pares_permitidos_live (tupla sintética, ver wallet_mirror_executor_dryrun.py).
"""
import csv
import json
import os
import math
import sys
import zlib
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

from shuffle_chunked import diffs_permutacion
from gate_dias_independientes import robustez_dias, ENFORCE as DIAS_ENFORCE, K_MEJORES_DIAS, PISO_EUR as PISO_DIAS_EUR

from gate_confirmacion_historial import (  # 13-Oct: días de calendario y corridas no decisivas
    BUENO, cargar_estado_previo, estado_vacio, veredicto_decidido, mantener_dos_vias, claves_sin_filas_hoy,
    aplicar_malos_de_hoy,
    campos_historial, semilla, entradas_sin_filas_hoy, ahora_utc,
)

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import shadow_postmortem as sp  # noqa: E402 -- reusa TWAP_MARCOS_AFECTADOS/TWAP_FECHA_CAMBIO
import ballenas_cross_check as bcc  # noqa: E402 -- refuerzo informativo, ver docstring del módulo
from analisis_gate_bucket_propio_28jul import (  # noqa: E402
    UMBRAL_ABSOLUTO_EUR, bootstrap_absoluto, rescatar_via_absoluta,
)

EXECUTOR = REPO / "data/shadow/wallet_mirror_executor_dryrun.csv"
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


# 15-Oct (OK Javi, /code-review medium): la "verdad de suelo" degradaba un bueno con n_real>=2 y media<0 y era un ESTADO
# ABSORBENTE: el veto impide operar el bucket y nunca llegan trades reales que lo levanten (BTC 15m grande [0,35-0,40):
# 229 unidades +0,28 €/€, 35/45 días +, malo_confirmado el 15-Oct 02:34Z por 1 de 5 reales). Ahora degrada solo si el
# PnL medio POR € de los reales es INCOMPATIBLE con la distribución del ejecutor en ese bucket (remuestreo: P(media de
# n_real unidades del ejecutor <= media real) < P_SUELO_REAL; tiene en cuenta el tamaño del pago, no solo el acierto) o
# si ya hay N_REAL_DIRECTO reales con media < 0. Sin ventana de días (una ventana reabría a la vez todo lo que los reales
# viejos habían vetado).
P_SUELO_REAL = 0.05
N_REAL_DIRECTO = 15
SIMS_SUELO_REAL = 20000


def _p_media_real(pnl_ejecutor: list, media_real: float, n_real: int, seed_key: str) -> float:
    """P(media de n_real retornos por € remuestreados del ejecutor <= media_real)."""
    rng = np.random.default_rng(zlib.crc32(seed_key.encode()))
    sims = rng.choice(np.asarray(pnl_ejecutor, dtype=float), size=(SIMS_SUELO_REAL, n_real)).mean(axis=1)
    return float((sims <= media_real + 1e-12).mean())


# 07-Oct: versión del método de la unidad/comisión. Si cambia, el historial de tolerancia (2 de 3 días) calculado con el
# método anterior NO cuenta (fichero aparte para no alterar el JSON que leen los consumidores).
METODO = "v2_mercado_lado_bucket_fee_real_07oct"
METODO_PATH = REPO / "data/shadow/wallet_mirror_gate_bucket_metodo.json"


def pnl_neto(ask, acierto):
    """PnL por € arriesgado con la comisión REAL del tomador cripto (07-Oct): 0,07·p·(1−p) por acción en CADA compra
    (gane o pierda) -> acciones por € = 1 / (p·(1 + FEE·(1−p))). Antes: 7 % de la ganancia y solo en aciertos."""
    return (1.0 if acierto else 0.0) / (ask * (1 + FEE * (1 - ask))) - 1.0


def cargar_filas():
    """11-Ago (petición explícita Javi, auditoría de huecos TWAP):
    excluye filas pre-07-Ago de marcos afectados (5min/15min/240min,
    reusa shadow_postmortem.TWAP_MARCOS_AFECTADOS/TWAP_FECHA_CAMBIO) --
    hallazgo real: este script no tenía NINGÚN filtro de régimen, mismo
    hueco ya cerrado hoy en shadow_postmortem.py/gate_bucket_propio.py/
    kelly_precio_gate.py/live_trade.py::_clv_tupla. Los 3 candidatos de
    Wallet Mirror viven en marcos afectados (5min/15min) y toda su
    ventana de datos (03->10-Ago) cruza el cambio TWAP (07-Ago) -- su
    veredicto podía estar contaminado igual que los demás mecanismos.

    13-Sep: el outcome se lee DIRECTAMENTE de EXECUTOR (columna `acierto`,
    resuelta por `wallet_mirror_executor_dryrun.py --resolver`) -- ya NO
    se cruza con wallet_mirror_sniper_dry_run.csv (ver docstring del
    módulo, población de wallets distinta, el join fallaba ~99.7%)."""
    # clave de grupo: (tipo, activo, marco, jugada_grande) -> [(ts, ask, pnl, wallet), ...]
    # 07-Oct (Javi "arregla ese cargador", 2 pasadas de /code-review): UNA observación por (mercado, lado, bucket de
    # STEP del ask) = la PRIMERA copia en ese bucket, con SU ask y SU pnl (sin promediar: promediar mezclaba buckets y por
    # convexidad inflaba las ganadoras). Wallet = la que más copias tiene en la unidad (la dominante no se esconde si
    # copia segunda). Antes cada fila contaba como observación independiente aunque compartiera mercado y desenlace:
    # WM ETH 15m g0 [0,21-0,24) forward n=45 eran 14 mercado-lado; SEGUIR BTC 15m g0 [0,25) n=1.315 eran 139.
    # Fail-closed: filas sin market_slug/mirror_lado se descartan; unidades con desenlace contradictorio se descartan.
    # Up y Down del mismo mercado siguen siendo 2 observaciones (el ejecutor live compra ambos si los copia).
    unidades = defaultdict(list)
    n_sin_clave = 0
    with open(EXECUTOR, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("sigue_fillable_en_decision") != "1":
                continue
            if r.get("acierto") not in ("0", "1"):
                continue  # sin resolver todavía (resolver_pendientes corre horario)
            ac = int(r["acierto"])
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
            mercado, lado = r.get("market_slug") or "", r.get("mirror_lado") or ""
            if not mercado or not lado:
                n_sin_clave += 1
                continue
            unidades[((tipo, activo, marco, grande), mercado, lado, bucket(ask))].append(
                (r["timestamp_utc"], ask, pnl, r.get("wallet", ""), ac))
    grupos = defaultdict(list)
    n_contradictorias = 0
    for (clave, _m, _l, _b), xs in unidades.items():
        if len({x[4] for x in xs}) > 1:
            n_contradictorias += 1
            continue
        xs.sort()
        wallet = Counter(x[3] for x in xs).most_common(1)[0][0]
        grupos[clave].append((xs[0][0], xs[0][1], xs[0][2], wallet))
    for v in grupos.values():
        v.sort()                      # orden cronológico (split-half / forward de los consumidores)
    if n_sin_clave or n_contradictorias:
        print(f"⚠️ cargar_filas: {n_sin_clave} filas sin market_slug/mirror_lado y {n_contradictorias} unidades con "
              f"desenlace contradictorio descartadas (fail-closed)")
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
    # 21-Sep: por bloques (shuffle_chunked.py) -- 3 matrices iters x n a la vez
    # causaban OOM; resultado bit-identico (verificado).
    diffs = diffs_permutacion(rng, todos, na, iters)
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
    de antes de este cambio, ningún bucket se degrada).

    15-Oct (/code-review x2): guarda el retorno POR € recalculado con pnl_neto(signal_ask, ganó) -- la MISMA función
    y comisión que el ejecutor (pnl_neto_eur/stake_eur daba −1,043 en cada pérdida, por debajo del mínimo −1,0 del
    ejecutor, y el remuestreo salía p=0 siempre); el bucket sale del ask de la SEÑAL (entry_price solo si falta); y UNA
    observación por (market_id, direction, bucket), como la unidad del ejecutor."""
    vistos_unidad = set()
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
                    ask = float(r.get("signal_ask") or r.get("entry_price") or "")
                    gano = float(r.get("pnl_neto_eur") or "") > 0
                except (TypeError, ValueError):
                    continue
                if not (0.0 < ask < 1.0):
                    continue
                clave_str = f"{tipo}#{activo}#{marco}#{grande}"
                unidad = (clave_str, r.get("market_id"), r.get("direction"), bucket(ask))
                if unidad in vistos_unidad:
                    continue
                vistos_unidad.add(unidad)
                out[clave_str][f"{bucket(ask):.2f}"].append(pnl_neto(ask, gano))
    except Exception:
        return {}
    return {k: dict(v) for k, v in out.items()}


def main():
    grupos = cargar_filas()
    print(f"Grupos (tipo,activo,marco,grande): {len(grupos)}")
    # 13-Oct: historial con MARCA por entrada y días de calendario (gate_confirmacion_historial, reglas 1-7),
    # vías relativa y absoluta en una sola lectura.
    AHORA = ahora_utc()
    _estado = cargar_estado_previo(OUT)
    try:
        metodo_previo = json.loads(METODO_PATH.read_text(encoding="utf-8")).get("metodo")
    except Exception:
        metodo_previo = None
    if metodo_previo != METODO:
        # 07-Oct (/code-review): el historial de días bueno/malo se calculó con otra unidad/comisión -> no cuenta para la
        # regla de 2 de 3 días; el método nuevo tiene que confirmarse por sí mismo.
        print(f"método {metodo_previo} -> {METODO}: historial de tolerancia previo IGNORADO")
        _estado = estado_vacio()
    pnl_real_por_bucket = _cargar_pnl_real_por_bucket()
    pnl_ejecutor_por_bucket = {}

    resultado = {}  # "tipo#activo#marco#grande" -> {bucket_str: entrada}
    pendientes = []
    candidatos_abs = []  # vía absoluta (12-Sep), ver UMBRAL_ABSOLUTO_EUR
    for clave, filas in grupos.items():
        tipo, activo, marco, grande = clave
        clave_str = f"{tipo}#{activo}#{marco}#{grande}"
        if len(filas) < N_MIN:
            # /code-review 01-Sep (mismo patrón que gate_bucket_propio_
            # 28jul.py): no perder el historial_crudo de los buckets de
            # esta clave si hoy cae por debajo de N_MIN a nivel clave -- un
            # día flojo no es un día MALO a nivel bucket.
            resultado[clave_str] = {}
            entradas_sin_filas_hoy(resultado[clave_str], clave_str, _estado, AHORA)
            continue
        por_bucket = defaultdict(list)
        for ts, ask, pnl, wallet in filas:
            por_bucket[bucket(ask)].append((ts, pnl, wallet))

        tabla = {}
        for b in sorted(por_bucket):
            dentro = por_bucket[b]
            fuera = [(ts, pnl) for bb, fs in por_bucket.items() if bb != b for ts, pnl, _w in fs]
            n_d = len(dentro)
            pnl_d = [pnl for _, pnl, _w in dentro]
            media_d = sum(pnl_d) / n_d
            # 15-Sep (petición explícita Javi, "masterizar" la familia --
            # mismo veto que SNIPER/DISPERSO/CANDIDATA9 ya tienen desde
            # hoy): WALLET_MIRROR solo tenía un REPORTE de concentración
            # (analisis_wallet_mirror_concentracion.py, "no vetea ni pausa
            # nada") -- aquí degrada el veredicto en línea, mismo umbral.
            _conteo_wallets = Counter(w for _, _, w in dentro if w)
            concentracion_top1 = (max(_conteo_wallets.values()) / n_d) if (_conteo_wallets and n_d) else None
            # 29-Ago (hallazgo real, sesión de racha de pérdidas reales en
            # WALLET_MIRROR -7,01€/16 trades): este módulo nunca tuvo el
            # veto de payout asimétrico (Kelly g(f)) que sí protege a
            # GBM_LATE/FAVORITO/BALLENAS/MOMENTUM_IBS vía gate_bucket_
            # propio.py::_veto_fillable() señal #2 (CLAUDE.md pt.14/P28) --
            # WALLET_MIRROR tiene su propio gate separado porque nunca
            # escribe en results.csv, y ese gate propio se quedó sin la
            # actualización del 28-Ago. `pnl_d` aquí ya es el retorno neto
            # por € (comisión real del tomador en pnl_neto() arriba, mismo
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
            # 15-Sep (petición explícita Javi, "masterizar" pt.4, refuerzo
            # nunca veto): `ask` ya en perspectiva de decisión (el lado
            # SEGUIR), consultado como "BUY_YES" (misma convención que el
            # resto de gates portados hoy).
            ballenas = bcc.consultar(activo, marco, b, "BUY_YES")
            pnl_ejecutor_por_bucket[(clave_str, f"{b:.2f}")] = pnl_d  # 15-Oct: para el test de la verdad de suelo
            entrada = {"n": n_d, "pnl_medio": round(media_d, 4), "g_kelly_f10": round(g_kelly, 5),
                       "concentracion_top1_wallet": round(concentracion_top1, 4) if concentracion_top1 is not None else None,
                       "tercio3_n": 0, "tercio3_pnl_medio": None,
                       "ballenas_hit_rate_yes": ballenas["hit_rate_yes"], "ballenas_n": ballenas["n"],
                       "ballenas_coincide": ballenas["coincide"],
                       "shuffle_p": None, "split_half": None, "veredicto": "sin_concluir",
                       **semilla(_estado, clave_str, f"{b:.2f}", AHORA)}
            tabla[f"{b:.2f}"] = entrada
            if n_d >= N_MIN:
                # 12-Sep (decisión explícita Javi, ver UMBRAL_ABSOLUTO_EUR
                # en analisis_gate_bucket_propio_28jul.py): vía absoluta,
                # independiente de si hay "fuera" -- un bucket rentable de
                # sobra no debe depender de tener vecinos con los que
                # compararse. dentro_sorted se reusa más abajo también para
                # el split-half relativo si hay `fuera`.
                dentro_sorted = sorted(dentro, key=lambda x: x[0])
                # 21-Sep (aprobado por Javi): robustez por DIAS INDEPENDIENTES, ver
                # gate_dias_independientes.py -- solo alimenta _degradar().
                _rob = robustez_dias([(_ts, _p) for _ts, _p, _w in dentro_sorted])
                entrada["n_dias"] = _rob["n_dias"]
                entrada["pnl_sin_mejores_dias"] = _rob["pnl_sin_mejores"]
                entrada["robusto_dias"] = _rob["robusto"]
                # 16-Sep (ver docstring de _degradar() más abajo -- criterio
                # de tendencia reciente. /code-review: reusa dentro_sorted
                # en vez de ordenar dos veces -- la primera versión ordenaba
                # SIEMPRE, incluso para buckets por debajo de N_MIN que
                # nunca pueden confirmar; con buckets de hasta 8.423 filas
                # en esta familia eso llevó el runtime de este script de
                # varios minutos a 28min, cerca del timeout de 2400s).
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
                    entrada["tercio3_pnl_medio"] = round(sum(pnl for _, pnl, _w in _tercio3) / tercio3_n, 4)
                _, _, p_valor_abs = bootstrap_absoluto(pnl_d, seed_key=f"abs#{clave_str}#{b:.2f}")
                entrada["p_valor_abs"] = round(p_valor_abs, 4)
                mid = n_d // 2
                m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
                split_half_abs = None
                if len(m1) >= 5 and len(m2) >= 5:
                    m1_abs = sum(pnl for _, pnl, _w in m1) / len(m1)
                    m2_abs = sum(pnl for _, pnl, _w in m2) / len(m2)
                    split_half_abs = [round(m1_abs, 4), round(m2_abs, 4)]
                    entrada["split_half_absoluto"] = split_half_abs
                candidatos_abs.append({"clave_str": clave_str, "bucket": f"{b:.2f}",
                                        "entrada": entrada, "p_valor_abs": p_valor_abs,
                                        "split_half_abs": split_half_abs})
            if n_d >= N_MIN and fuera:
                pnl_f = [pnl for _, pnl in fuera]
                diff, p_valor = shuffle_test(pnl_d, pnl_f, seed_key=f"{clave_str}#{b:.2f}")
                entrada["shuffle_p"] = round(p_valor, 4)
                mid = n_d // 2
                m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
                if len(m1) >= 5 and len(m2) >= 5:
                    media_fuera = sum(pnl_f) / len(pnl_f)
                    d1 = sum(pnl for _, pnl, _w in m1) / len(m1) - media_fuera
                    d2 = sum(pnl for _, pnl, _w in m2) / len(m2) - media_fuera
                    entrada["split_half"] = [round(d1, 4), round(d2, 4)]
                    consistente = (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)
                    if consistente:
                        pendientes.append({"clave_str": clave_str, "bucket": f"{b:.2f}",
                                            "entrada": entrada, "p": p_valor, "diff": diff})
        entradas_sin_filas_hoy(tabla, clave_str, _estado, AHORA)  # 13-Oct: no perder buckets sin filas hoy
        resultado[clave_str] = tabla

    claves_sin_filas_hoy(resultado, _estado, AHORA)  # 13-Oct: claves enteras sin filas hoy

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

    def _degradar(veredicto_crudo, entrada, clave_str, b):
        """29-Ago/31-Ago: vetos de payout asimétrico (Kelly g(f=10%)<=0) y
        verdad-de-suelo (trades REALES ya negativos en este bucket exacto,
        n_real>=2) -- factorizado 12-Sep para reusarlo también en la vía
        absoluta de abajo, mismo criterio EXACTO, solo puede DEGRADAR,
        nunca promover.

        15-Sep: añadido veto de concentración de wallet (mismo umbral 30%
        que SNIPER/DISPERSO/CANDIDATA9 desde hoy) -- antes esta familia
        solo tenía un REPORTE (analisis_wallet_mirror_concentracion.py,
        "no vetea ni pausa nada"), la única de las 4 sin veto automático.

        16-Sep: añadido veto de TENDENCIA RECIENTE, mismo criterio EXACTO
        portado de analisis_bot_wallets_gate_bucket_25ago.py::_degradar()
        (ver su docstring para el caso real que lo motivó, CANDIDATA9_
        BOT_CONSENSO#BNB#5min[0.25) -- pasaba el bootstrap CI90% con la
        muestra completa pero decaía a negativo en el último tercio
        cronológico) -- esta familia opera con dinero real desde el
        11-Ago, mismo motivo de máxima cautela que el veto de arriba."""
        nota_payout = ""
        g_kelly = entrada.get("g_kelly_f10")
        if veredicto_crudo == "bueno_confirmado" and g_kelly is not None and g_kelly <= 0:
            veredicto_crudo = "malo_confirmado"
            nota_payout = f" [degradado: payout asimétrico g_kelly(f=10%)={g_kelly:+.5f}<=0]"
        nota_real = ""
        pnls_reales = pnl_real_por_bucket.get(clave_str, {}).get(b)
        if veredicto_crudo == "bueno_confirmado" and pnls_reales and len(pnls_reales) >= 2:
            n_r = len(pnls_reales)
            media_real = sum(pnls_reales) / n_r
            if media_real < 0:
                pnl_ej = pnl_ejecutor_por_bucket.get((clave_str, b))
                # sin distribución del ejecutor -> p=0, se degrada como antes (fail-closed)
                p_real = _p_media_real(pnl_ej, media_real, n_r, f"real#{clave_str}#{b}") if pnl_ej else 0.0
                if p_real < P_SUELO_REAL or n_r >= N_REAL_DIRECTO:
                    veredicto_crudo = "malo_confirmado"
                    nota_real = (f" [degradado: {n_r} trades REALES pnl_medio={media_real:+.3f}/€<0, "
                                 f"P(ejecutor <= real)={p_real:.3f}]")
                else:
                    nota_real = (f" [verdad de suelo NO degrada: {n_r} reales pnl_medio={media_real:+.3f}/€ "
                                 f"compatibles con el ejecutor, P={p_real:.3f}]")
        nota_concentracion = ""
        concentracion = entrada.get("concentracion_top1_wallet")
        if veredicto_crudo == "bueno_confirmado" and concentracion is not None and concentracion > 0.30:
            veredicto_crudo = "malo_confirmado"
            nota_concentracion = f" [degradado: concentración top1_wallet={concentracion:.1%}>30%]"
        nota_tendencia = ""
        tercio3_n = entrada.get("tercio3_n") or 0
        tercio3_pnl = entrada.get("tercio3_pnl_medio")
        # 16-Sep tarde (mismo fix que analisis_bot_wallets_gate_bucket_25ago.py):
        # n>=5 permitía degradar con una racha de solo 5 trades, por debajo
        # del estándar n>=15 del resto del proyecto.
        if (veredicto_crudo == "bueno_confirmado" and tercio3_n >= 15
                and tercio3_pnl is not None and tercio3_pnl < UMBRAL_ABSOLUTO_EUR):
            veredicto_crudo = "malo_confirmado"
            nota_tendencia = (f" [degradado: tendencia reciente último_tercio "
                               f"n={tercio3_n} pnl_medio={tercio3_pnl:+.3f}€<{UMBRAL_ABSOLUTO_EUR}]")
        if (DIAS_ENFORCE and veredicto_crudo == "bueno_confirmado"
                and entrada.get("robusto_dias") is not True):
            veredicto_crudo = "sin_concluir"
            nota_tendencia += (f" [sin_concluir: no robusto por dias -- sin los {K_MEJORES_DIAS} mejores dias "
                               f"pnl_medio={entrada.get('pnl_sin_mejores_dias')} (<{PISO_DIAS_EUR}) "
                               f"n_dias={entrada.get('n_dias')}]")
        return veredicto_crudo, nota_payout, nota_real, nota_concentracion, nota_tendencia, g_kelly

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
        b = p["bucket"]
        veredicto_crudo, nota_payout, nota_real, nota_concentracion, nota_tendencia, g_kelly = _degradar(
            veredicto_crudo, p["entrada"], p["clave_str"], b)
        p["entrada"]["veredicto_crudo_hoy"] = veredicto_crudo

        # 31-Ago (mismo guard que gate_bucket_propio.py, petición explícita
        # Javi): asimétrico, "malo_confirmado" sigue inmediato (1 día basta
        # para vetar). Este gate ya opera con dinero real hoy (WALLET_MIRROR
        # #BTC, DRY_RUN=False desde 11-Ago) -- máxima cautela.
        # 01-Sep (petición explícita Javi, "un día de mala racha no puede
        # entorpecer esto"): antes exigía el día INMEDIATAMENTE anterior
        # también bueno_confirmado (reset a 1 día flojo). Ahora exige 2 de
        # los últimos 3 días (incluido hoy) vía gate_confirmacion_historial.py.
        # 10-Sep: versión "diaria" del wrapper -- este generador corre
        # horario; desde 13-Oct veredicto_dia() con marca por entrada (gate_confirmacion_historial).
        veredicto, _h, _m = veredicto_decidido(veredicto_crudo, p["entrada"]["historial_crudo"],
                                          p["entrada"]["historial_fechas"], AHORA)
        p["entrada"].update(campos_historial(_h, _m))
        if veredicto == "sin_concluir" and veredicto_crudo == "bueno_confirmado":
            veredictos_pendientes_confirmacion.append(
                f"⏳ {p['clave_str']} [{b},{float(b)+STEP:.2f}) n={p['entrada']['n']} "
                f"pnl_medio={p['entrada']['pnl_medio']:+.3f} bueno_confirmado HOY, "
                f"esperando confirmación de mañana"
            )

        p["entrada"]["veredicto"] = veredicto
        if veredicto == "sin_concluir" or (veredicto == "malo_confirmado" and veredicto_crudo != "malo_confirmado"):
            continue  # pendiente, o malo arrastrado de una corrida anterior de hoy (no es veredicto nuevo)
        marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
        veredictos_nuevos.append(
            f"{marca} {p['clave_str']} [{b},{float(b)+STEP:.2f}) "
            f"n={p['entrada']['n']} pnl_medio={p['entrada']['pnl_medio']:+.3f} "
            f"g_kelly={g_kelly:+.5f} p={p['p']:.4f} {veredicto}{nota_payout}{nota_real}{nota_concentracion}{nota_tendencia}"
        )

    # 12-Sep, vía absoluta (decisión explícita Javi, ver UMBRAL_ABSOLUTO_EUR
    # en analisis_gate_bucket_propio_28jul.py): rescata buckets rentables de
    # sobra (pnl_medio>=UMBRAL_ABSOLUTO_EUR, robusto tras BH-FDR) que la vía
    # relativa de arriba dejó en "malo_confirmado" solo por ser peores que
    # un vecino de la misma tupla -- pasa por las MISMAS degradaciones
    # (payout asimétrico, verdad-de-suelo) y la MISMA tolerancia diaria que
    # la vía relativa, nunca las relaja.
    rescatados = rescatar_via_absoluta(
        candidatos_abs, agrupador_fn=lambda clave_str: tuple(clave_str.split("#")[1:]))
    for c in rescatados:
        b = c["bucket"]
        veredicto_crudo, nota_payout, nota_real, nota_concentracion, nota_tendencia, g_kelly = _degradar(
            "bueno_confirmado", c["entrada"], c["clave_str"], b)
        c["entrada"]["veredicto_crudo_hoy_abs"] = veredicto_crudo
        # Namespace INDEPENDIENTE de historial (historial_abs_previo/
        # *_abs, cargar_estado_previo) -- /code-review 12-Sep:
        # reusar historial_crudo/fecha_historial de la vía relativa
        # contaminaba su ventana de tolerancia (un malo_confirmado
        # relativo podía "reconfirmarse" bueno con solo 2 días de rescate
        # absoluto, sin que la vía relativa hubiera cambiado de opinión).
        veredicto, _h, _m = veredicto_decidido(veredicto_crudo, c["entrada"]["historial_crudo_abs"],
                                          c["entrada"]["historial_fechas_abs"], AHORA)
        c["entrada"].update(campos_historial(_h, _m, "_abs"))
        if veredicto == "sin_concluir":
            # NUNCA pisa el veredicto ya decidido por la vía relativa (que
            # puede ser malo_confirmado, sin_concluir o -- imposible aquí,
            # ver rescatar_via_absoluta -- bueno_confirmado) mientras la
            # vía absoluta no acumule sus propios 2-de-3-días.
            if veredicto_crudo == "bueno_confirmado":
                veredictos_pendientes_confirmacion.append(
                    f"⏳ [vía absoluta] {c['clave_str']} [{b},{float(b)+STEP:.2f}) "
                    f"n={c['entrada']['n']} pnl_medio={c['entrada']['pnl_medio']:+.3f} "
                    f"bueno_confirmado HOY, esperando confirmación de mañana")
            continue
        c["entrada"]["veredicto"] = veredicto
        c["entrada"]["via"] = "absoluta"
        if veredicto == "malo_confirmado" and veredicto_crudo != "malo_confirmado":
            continue  # malo arrastrado de una corrida anterior de hoy (no es veredicto nuevo)
        marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
        veredictos_nuevos.append(
            f"{marca} [vía absoluta] {c['clave_str']} [{b},{float(b)+STEP:.2f}) "
            f"n={c['entrada']['n']} pnl_medio={c['entrada']['pnl_medio']:+.3f} "
            f"g_kelly={g_kelly:+.5f} p_abs={c['p_valor_abs']:.4f} {veredicto}{nota_payout}{nota_real}{nota_concentracion}{nota_tendencia}"
        )

    # 13-Oct: buckets que esta corrida NO decidió (no sobreviven al BH-FDR, split-half inconsistente...): tolerancia de
    # 2 de 3 días de CALENDARIO con las guardas y el suelo de HOY, solo si la corrida anterior los publicó bueno
    # (gate_confirmacion_historial.mantener_dos_vias). Antes hacían `continue` y un bueno parpadeaba a sin_concluir.
    mantenidos = mantener_dos_vias(resultado, AHORA, N_MIN, _estado, pendientes, "clave_str",
                                   lambda c, b, e: _degradar(BUENO, e, c, b)[0], P_MAX, UMBRAL_ABSOLUTO_EUR, "split_half")
    if mantenidos:
        print(f"\n{len(mantenidos)} bucket(s) sin confirmación nueva en esta corrida (tolerancia / guardas):")
        for linea in mantenidos:
            print(f"  {linea}")

    print(f"\n{len(veredictos_nuevos)} bucket(s) con veredicto tras BH-FDR:")
    for linea in veredictos_nuevos:
        print(f"  {linea}")
    if veredictos_pendientes_confirmacion:
        print(f"\n{len(veredictos_pendientes_confirmacion)} bucket(s) pendientes de 2ª confirmación mañana:")
        for linea in veredictos_pendientes_confirmacion:
            print(f"  {linea}")

    # 13-Oct: regla 4 en UN solo punto, después de todas las vías (gate_confirmacion_historial.aplicar_malos_de_hoy).
    forzados = aplicar_malos_de_hoy(resultado, AHORA)
    if forzados:
        print(f"\n{len(forzados)} bucket(s) con un malo decidido HOY se siguen publicando malo_confirmado "
              f"(tenían en esta corrida: {', '.join(f'{c} [{b}) {v}' for c, b, v in forzados[:20])})")

    # 21-Sep: escritura atomica -- el ejecutor real (y los kill switches) leen
    # este JSON en paralelo; json.dump directo sobre OUT deja una ventana con
    # el fichero truncado.
    _tmp = OUT.with_name(f"{OUT.name}.{os.getpid()}.tmp")
    with open(_tmp, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    os.replace(_tmp, OUT)
    try:
        METODO_PATH.write_text(json.dumps({"metodo": METODO}), encoding="utf-8")
    except Exception as e:
        print(f"⚠️ no se pudo escribir {METODO_PATH}: {e}")
    print(f"\nGuardado en {OUT}")


if __name__ == "__main__":
    main()
