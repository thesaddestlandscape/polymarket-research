#!/usr/bin/env python3
"""buscador_edge_perdido.py -- (22-Sep, diseño e implementación V1, directiva
Javi 21-Sep: "diseñar una estrategia que se dedique a buscar edge perdido en
cada estrategia... tiene que buscar edge y minar pasta de cualquier sitio que
lo haya perdido"). Ver memoria project_estrategia_buscador_edge_perdido_21sep
y CLAUDE.md pt.24.

MODO LECTURA -- no conecta a evaluar() de ningún ejecutor ni toca dinero.
Mismo patrón que edge_quirurgico_rolling.py (aditiva, requiere OK de Javi +
/code-review antes de engancharse a nada real).

## Problema que ataca
Una tupla en pares_permitidos_live puede perder edge en agregado (racha
negativa reciente, mismo criterio de vigia_degradacion_live.py) sin que el
edge haya desaparecido del todo -- puede haberse MOVIDO a otra franja de
alguna dimensión (hora del día, día de la semana...), el mismo fenómeno que
ya se confirmó para PRECIO el 21-Sep (edge_quirurgico_rolling.py: SNIPER#
BTC#15min[0.10,0.15) vive mejor en [0.13,0.16); WM ETH#15min#1 pierde
[0.45,0.50) pero gana [0.48,0.51)).

## Detector (paso 1)
Una tupla está "degradada" si:
  (a) está en pares_permitidos_live HOY (config_live.json), Y
  (b) vigia_degradacion_live_latch.json la marca negativo=true (ventana
      reciente de N=30 trades ejecutados en pnl/trade negativo).
Cruce explícito con (a) porque el latch es un diccionario que persiste para
siempre -- una tupla pausada/retirada semanas atrás puede seguir marcada
negativo=true sin que nadie la haya limpiado (verificado 22-Sep: el latch
tenía entradas de FAVORITO_CONFIRMADO/GBM_LATE_15M/BALLENAS_TARDIAS#BTC de
la era anterior, ya fuera de pares_permitidos_live desde Jul/Ago -- sin este
cruce el buscador perseguiría fantasmas).

## Búsqueda (paso 2) -- dimensiones cubiertas en V1
  - hora_utc (0-23): ¿hay una franja horaria donde el edge sigue vivo?
  - dia_semana (0=lunes..6=domingo): ¿hay días donde el edge sigue vivo?
Cada bucket candidato pasa el MISMO rigor que edge_quirurgico_rolling.py:
  - forward-validado: split train/test por cutoff = hoy - FORWARD_DIAS,
    el bucket se ELIGE con datos de train, se MIDE con datos de test
    (nunca al revés -- data leakage es el error #1 de este tipo de barrido).
  - test: n>=N_FORWARD_MIN y pnl medio >= PISO_EUR.
  - train: robustez_dias() (gate_dias_independientes.py) -- el bucket
    tiene que sobrevivir quitar los 2 mejores días, no ser una racha de
    2-3 días buena escondida dentro de un agregado malo.
  - p-valor de permutación (shuffle_chunked, bit-idéntico a la versión sin
    chunking) del bucket vs el resto de esa dimensión en TRAIN, con
    corrección BH-FDR sobre todos los buckets de esa dimensión (24 horas /
    7 días) -- sin esto, testear 24 horas a la vez da ~1 falso positivo
    "significativo" por pura casualidad aunque no exista ningún patrón.

## Dimensión "confluencia_ballenas" (28-Sep, Parte A del pedido de Javi
"buscar ineficiencias del mercado/ballenas/wallets... para explotarlas a
nuestro favor"): SOLO para tuplas "clasicas" (no P-GALLINA -- esas ya
correlacionan con wallets por otra vía, ver `wallet_subset` pendiente).
Para cada señal (ts, market_id) de la tupla degradada:
  1. market_id -> condition_id vía market_id_resolver.resolver_lote()
     (índice persistido, SIN fallback a API -- este script corre cada 6h
     en modo lectura, no debe generar tráfico de red por lote).
  2. condition_id -> trades de ballenas en ESE mercado, filtrados a
     ts_trade <= ts de la señal (fail-closed contra look-ahead -- mismo
     error real que refutó el reactivo GBM_LATE del 22-Sep, ver
     idea_gbm_late_reactivo_lookahead_refutado_23sep: nunca mirar
     ballenas que operaron DESPUÉS de nuestra propia señal).
  3. bucket = "confluye" si el volumen (size_usd) de ballenas en ESE
     mercado hasta ese instante tiene mayoría en el MISMO lado que la
     decisión de la tupla (BUY_YES/BUY_NO), "diverge" si la mayoría es
     el lado contrario, "sin_ballenas" si no hay trades de ballenas
     todavía en ese instante o el market_id no resuelve a condition_id.
`ballenas_timing_history.csv` (282MB/1,7M filas) se indexa SOLO para los
condition_id que hacen falta (mismo patrón que evitó el OOM real de
analisis_fade_regimen_arquetipoA.py, 28-Sep) -- nunca se carga entero.

## Dimensiones NO cubiertas todavía (fase 2, roadmap explícito, NO fingir
que están hechas):
  - subconjunto de wallets (aplica a WALLET_MIRROR/bot_wallets -- requiere
    cruzar con wallet_mirror_tracker/bot_wallets, estructura de datos
    distinta a results.csv)
  - latencia de entrada (requiere libro_snapshots.csv o el CSV de fase0
    específico de cada ejecutor, no unificado)
  - cruce cross-activo (requiere correlacionar la misma franja temporal
    entre activos distintos)
  - tamaño del trade (requiere stake_eur de trades.csv, no results.csv)
Cada una se añade como su propia función `_dimension_*()` siguiendo el
mismo contrato (bucket_id, filas_train, filas_test) -> ver `DIMENSIONES`
más abajo -- diseño pensado para extenderse sin reescribir el core.

## Salida
data/shadow/buscador_edge_perdido.json (tupla degradada -> por dimensión,
lista de buckets candidatos con evidencia) + Telegram (latch, solo
hallazgos NUEVOS) vía vigia_buscador_edge_perdido.py.
"""
import csv
import wm_ejecutor_csv  # 25-Sep: lector unificado principal+reconstruido (solo análisis)
import json
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from analisis_gate_bucket_propio_28jul import (  # noqa: E402
    cargar_tuplas_live, cargar_filas, bh_fdr_signif,
    FECHA_CAMBIO_TWAP, MARCOS_TWAP_AFECTADOS, FECHA_CAMBIO_TWAP_5MIN_60S,
    ESTRATEGIAS_FIX_PRECIO_CANDIDATA9_10, FECHA_FIX_PRECIO_CANDIDATA9_10,
    _marco_de_subtype,
)
from gate_dias_independientes import robustez_dias  # noqa: E402
from shuffle_chunked import diffs_permutacion  # noqa: E402
import shadow_postmortem as sp  # noqa: E402 -- reusa es_pre_twap
from market_id_resolver import resolver_lote, _cargar_indice  # noqa: E402

CONFIG_LIVE = REPO / "data/live/config_live.json"
LATCH_DEGRADACION = REPO / "data/live/vigia_degradacion_live_latch.json"
OUT = REPO / "data/shadow/buscador_edge_perdido.json"
RESULTS_PATH = REPO / "data/shadow/results.csv"
BALLENAS_HIST = REPO / "data/shadow/ballenas_timing_history.csv"

# FASE 1B (22-Sep): loader directo para la familia P-GALLINA. No reusa
# analisis_bot_wallets_gate_bucket_25ago.py::cargar_filas() ni analisis_
# wallet_mirror_gate_bucket_10ago.py::cargar_filas() porque esas funciones
# COLAPSAN ambas direcciones (Up/Down) en una sola clave (arquetipo,activo,
# marco) -- pares_permitidos_live SÍ separa por dirección (...#BUY_Up vs
# #BUY_Down), así que hace falta filtrar por lado aquí, no reagrupar después.
BW_FASE0 = REPO / "data/shadow/bot_wallets_gate_bucket_fase0.csv"
WM_EXECUTOR = REPO / "data/shadow/wallet_mirror_executor_dryrun.csv"
FEE_PGALLINA = 0.07
RATIO_MIN_PGALLINA = 5.0


def _pnl_neto_pgallina(ask: float, acierto: bool) -> float:
    gross_win = (1 - ask) / ask
    return gross_win * (1 - FEE_PGALLINA) if acierto else -1.0


def _cargar_filas_pgallina(tupla_str: str) -> list[tuple]:
    """Devuelve [(ts, py, pnl), ...] para una tupla de la familia P-GALLINA,
    en la MISMA forma que cargar_filas() de results.csv (así _sweep_dimension
    no necesita saber de qué familia viene la tupla). Usa el precio de
    DECISIÓN (ask_decision/mejor_ask_decision), no el de detección -- es el
    que de verdad se paga (mismo criterio ya aplicado a candidata9, ver
    feedback_gate_debe_usar_precio_decision_no_deteccion_10sep). El gate
    canónico (`analisis_bot_wallets_gate_bucket_25ago.py`) TODAVÍA usa
    detección para bot_wallets -- es un hueco conocido y sin cerrar ahí, NO
    reproducirlo aquí a propósito. Consecuencia esperada y aceptada: la
    población de este buscador puede no coincidir 1:1 con la del gate
    canónico para la misma tupla."""
    if tupla_str.startswith("WALLET_MIRROR#"):
        if not WM_EXECUTOR.exists():
            return []
        filas = []
        if True:  # lectura unificada principal+reconstruido (25-Sep), ver wm_ejecutor_csv.py
            for r in wm_ejecutor_csv.iter_filas(WM_EXECUTOR):
                if r.get("tupla_sintetica") != tupla_str:
                    continue
                if not r.get("outcome_real"):
                    continue
                if r.get("sigue_fillable_en_decision") != "1":
                    continue
                ask_raw = r.get("ask_decision", "")
                if not ask_raw:
                    continue
                try:
                    ask = float(ask_raw)
                except (TypeError, ValueError):
                    continue
                if not (0.0 < ask < 1.0):
                    continue
                marco = r.get("marco", "?")
                ts = r.get("resolved_ts") or r.get("trade_timestamp", "")
                if sp.es_pre_twap(marco, ts):
                    continue
                if r.get("acierto") not in ("0", "1"):
                    continue
                pnl = _pnl_neto_pgallina(ask, r["acierto"] == "1")
                filas.append((ts, ask, pnl))
        return filas

    partes = tupla_str.split("#")
    if len(partes) != 4 or not partes[3].startswith("BUY_"):
        return []
    arquetipo, activo, marco, decision = partes
    lado = decision[len("BUY_"):]
    if not BW_FASE0.exists():
        return []
    filas = []
    with open(BW_FASE0, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r.get("arquetipo") != arquetipo or r.get("activo") != activo
                    or r.get("marco") != marco or r.get("lado_wallet") != lado):
                continue
            if not r.get("outcome_real"):
                continue
            if r.get("sigue_fillable_decision") != "1":
                continue
            ask_raw = r.get("mejor_ask_decision", "")
            if not ask_raw:
                continue
            try:
                ask = float(ask_raw)
            except (TypeError, ValueError):
                continue
            if not (0.0 < ask < 1.0):
                continue
            ratio_raw = r.get("ratio_vs_stake_decision", "")
            try:
                ratio = float(ratio_raw) if ratio_raw else None
            except (TypeError, ValueError):
                ratio = None
            if ratio is None or ratio < RATIO_MIN_PGALLINA:
                continue
            ts = r.get("resolved_ts") or r.get("trade_timestamp", "")
            if sp.es_pre_twap(marco, ts):
                continue
            if r.get("acierto") not in ("0", "1"):
                continue
            pnl = _pnl_neto_pgallina(ask, r["acierto"] == "1")
            filas.append((ts, ask, pnl))
    return filas

FORWARD_DIAS = 7          # mismo horizonte que edge_quirurgico_rolling.py
N_FORWARD_MIN = 15
PISO_EUR = 0.10
ITERS = 1000
# 28-Sep: tope de resoluciones vía API por corrida para confluencia_ballenas --
# resolver_lote(usar_api_fallback=False) solo usa el índice cacheado
# (market_id_condition_id_map.json), y verificado con datos reales la
# cobertura cacheada es muy desigual por tupla (0,6% a 100% según qué tan
# vieja/popular sea) -- sin este fallback acotado la dimensión se queda casi
# siempre en "sin_ballenas" por falta de mapeo, no por falta de ballenas de
# verdad. Prioriza los market_id de las señales MÁS RECIENTES (lo que más
# importa para "dónde se fue el edge"), nunca ilimitado -- este script corre
# cada 6h en modo lectura, un tope duro evita tráfico de red descontrolado.
MAX_RESOLVER_API = 300
_rng = np.random.default_rng(202)


def _tuplas_degradadas() -> list[str]:
    """(a) ^ (b) del docstring -- devuelve tupla_str de pares_permitidos_live
    marcados negativo=true en el latch de vigia_degradacion_live.py."""
    try:
        cfg = json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
        vivos = set(cfg.get("pares_permitidos_live", []))
    except Exception:
        return []
    try:
        latch = json.loads(LATCH_DEGRADACION.read_text(encoding="utf-8"))
    except Exception:
        latch = {}
    negativas = {k for k, v in latch.items() if v.get("negativo")}
    return sorted(vivos & negativas)


def _shuffle_p(dentro: list[float], fuera: list[float]) -> float:
    if len(dentro) < 2 or len(fuera) < 2:
        return 1.0
    a = np.asarray(dentro, dtype=np.float64)
    b = np.asarray(fuera, dtype=np.float64)
    diff_real = a.mean() - b.mean()
    todos = np.concatenate([a, b])
    diffs = diffs_permutacion(_rng, todos, len(a), ITERS)
    return float(np.mean(np.abs(diffs) >= abs(diff_real)))


def _sweep_dimension(filas: list[tuple], cutoff: str, clave_bucket) -> list[dict]:
    """filas: [(ts, py, pnl), ...] TWAP-safe de cargar_filas(). clave_bucket:
    funcion ts -> id de bucket (ej. hora UTC, dia de semana). Devuelve la
    lista de candidatos que sobreviven train (robustez_dias + shuffle+BH-FDR)
    y test (forward, n>=N_FORWARD_MIN, pnl>=PISO_EUR) -- forward-validado,
    nunca al reves."""
    train = [(ts, py, pnl) for ts, py, pnl in filas if str(ts)[:19] < cutoff]
    test = [(ts, py, pnl) for ts, py, pnl in filas if str(ts)[:19] >= cutoff]
    if len(train) < 30:
        return []

    por_bucket_train = defaultdict(list)   # bucket -> [(ts, pnl), ...]
    for ts, _py, pnl in train:
        por_bucket_train[clave_bucket(ts)].append((ts, pnl))
    por_bucket_test = defaultdict(list)    # bucket -> [pnl, ...]
    for ts, _py, pnl in test:
        por_bucket_test[clave_bucket(ts)].append(pnl)

    todo_pnl_train = [pnl for _ts, pnl in [x for v in por_bucket_train.values() for x in v]]

    claves = sorted(por_bucket_train)
    if len(claves) < 2:
        return []
    p_valores = []
    stats = []
    for bk in claves:
        dentro = [pnl for _ts, pnl in por_bucket_train[bk]]
        fuera = [pnl for k2, v in por_bucket_train.items() if k2 != bk for _ts, pnl in v]
        n_tr = len(dentro)
        pnl_tr = sum(dentro) / n_tr if n_tr else None
        rob = robustez_dias([(ts, pnl) for ts, pnl in por_bucket_train[bk]])
        p = _shuffle_p(dentro, fuera) if n_tr >= 8 and fuera else 1.0
        p_valores.append(p)
        stats.append({
            "bucket": bk, "n_train": n_tr, "pnl_train": pnl_tr,
            "robusto_dias": rob["robusto"], "n_dias_train": rob["n_dias"],
            "pnl_sin_2_mejores_dias": rob["pnl_sin_mejores"], "p_shuffle": p,
        })

    sig_idx = bh_fdr_signif(p_valores, q=0.05)
    candidatos = []
    for i, s in enumerate(stats):
        if i not in sig_idx:
            continue
        if not (s["pnl_train"] is not None and s["pnl_train"] >= PISO_EUR and s["robusto_dias"]):
            continue
        bk = s["bucket"]
        test_pnls = por_bucket_test.get(bk, [])
        n_te = len(test_pnls)
        pnl_te = sum(test_pnls) / n_te if n_te else None
        forward_ok = bool(n_te >= N_FORWARD_MIN and pnl_te is not None and pnl_te >= PISO_EUR)
        candidatos.append({**s, "n_test": n_te, "pnl_test": pnl_te, "forward_ok": forward_ok})
    return candidatos


def _clave_hora(ts: str) -> int:
    try:
        return datetime.fromisoformat(ts).hour
    except Exception:
        return -1


def _clave_dia_semana(ts: str) -> int:
    try:
        return datetime.fromisoformat(ts).weekday()
    except Exception:
        return -1


DIMENSIONES = {
    "hora_utc": _clave_hora,
    "dia_semana": _clave_dia_semana,
}

# ---- confluencia_ballenas (28-Sep) -- SOLO tuplas "clasicas", ver docstring ----


def _cargar_market_ids(tuplas: list[str], tuplas_live_todas: list[tuple]) -> dict:
    """tupla_str -> {prediction_timestamp: market_id}. Segundo scan de
    results.csv, deliberado -- no se puede reusar el de cargar_filas()
    (analisis_gate_bucket_propio_28jul.py) sin cambiar su forma de
    retorno, que también usa el gate canónico. MISMO filtro TWAP/precio-
    invertido que cargar_filas() para que los `ts` casen 1:1 con los que
    ya trae `filas` de esa función -- una sola vez, aunque haya varias
    tuplas degradadas, filtrando por estrategia desde la primera línea
    (no materializa nada de las ~750k filas que no hacen falta)."""
    tuplas_set = set(tuplas)
    if not tuplas_set:
        return {}
    claves = {(s, sub, d): t for s, sub, d, t, _ in tuplas_live_todas if t in tuplas_set}
    marco_por_tupla = {t: _marco_de_subtype(sub) for s, sub, d, t, _ in tuplas_live_todas if t in tuplas_set}
    estrategias = {s for s, _sub, _d, t, _ in tuplas_live_todas if t in tuplas_set}
    out = defaultdict(dict)
    if not RESULTS_PATH.exists():
        return out
    with open(RESULTS_PATH, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("strategy") not in estrategias or row.get("acierto") not in ("0", "1"):
                continue
            clave = (row["strategy"], row["subtype"], row["decision"])
            t = claves.get(clave)
            if t is None:
                continue
            marco_t = marco_por_tupla.get(t)
            if marco_t in MARCOS_TWAP_AFECTADOS:
                try:
                    ts_dt = datetime.fromisoformat(row.get("prediction_timestamp", ""))
                except Exception:
                    continue  # fail-closed, mismo criterio que cargar_filas()
                corte = FECHA_CAMBIO_TWAP_5MIN_60S if marco_t == "5min" else FECHA_CAMBIO_TWAP
                if ts_dt < corte:
                    continue
            if row["strategy"] in ESTRATEGIAS_FIX_PRECIO_CANDIDATA9_10 and row["decision"] == "BUY_NO":
                try:
                    ts_dt = datetime.fromisoformat(row.get("prediction_timestamp", ""))
                except Exception:
                    continue
                if ts_dt < FECHA_FIX_PRECIO_CANDIDATA9_10:
                    continue
            mid = row.get("market_id")
            if not mid:
                continue
            ts = row.get("prediction_timestamp", "")
            # /code-review 28-Sep, hallazgo real verificado contra results.csv
            # (7.907 colisiones de (strategy,subtype,decision,ts) con >1
            # market_id distinto, ~1% de las filas, ej. UPDOWN_GBM): shadow_
            # predict.py calcula `ts` UNA vez por ciclo para todas las filas
            # que genera ese ciclo -- dos señales de la MISMA tupla pueden
            # compartir ts si el ciclo produjo dos predicciones (mercados
            # distintos) en la misma pasada. Indexar solo por ts sin esto
            # asignaría el market_id del último visto a TODAS las filas con
            # ese ts, envenenando en silencio la dimensión con el mercado
            # equivocado. Fail-closed: si dos market_id distintos comparten
            # ts para esta tupla, se marca ambiguo (None) -- clave_bucket ya
            # trata None como "sin dato" -> bucket "sin_ballenas", nunca
            # adivina cuál de los dos mercados era.
            actual = out[t].get(ts, "_SIN_VER_")
            if actual == "_SIN_VER_":
                out[t][ts] = mid
            elif actual is not None and actual != mid:
                out[t][ts] = None
    return out


def _index_ballenas(condition_ids: set) -> dict:
    """condition_id -> [(ts_trade, compro_yes, size_usd), ...] ordenado por
    ts_trade. Filtra ballenas_timing_history.csv (282MB/1,7M filas) a los
    condition_id pedidos DESDE la primera línea -- nunca materializa el
    fichero completo (mismo patrón que evitó el OOM real de
    analisis_fade_regimen_arquetipoA.py, 28-Sep, misma sesión)."""
    idx = defaultdict(list)
    if not condition_ids or not BALLENAS_HIST.exists():
        return idx
    with open(BALLENAS_HIST, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            cid = row.get("condition_id")
            if cid not in condition_ids:
                continue
            ts = row.get("ts_trade")
            if not ts:
                continue
            try:
                size = float(row.get("size_usd") or 0)
            except (TypeError, ValueError):
                continue
            compro_yes = row.get("compro_yes") in ("True", "true", "1")
            idx[cid].append((ts, compro_yes, size))
    for cid in idx:
        idx[cid].sort(key=lambda x: x[0])
    return idx


def _bucket_confluencia_factory(decision_yes: bool, market_ids_por_ts: dict,
                                 mid_to_cid: dict, ballenas_idx: dict):
    """Devuelve clave_bucket(ts) -> 'confluye'|'diverge'|'sin_ballenas',
    cerrando sobre el contexto de UNA tupla concreta (misma forma que
    _clave_hora/_clave_dia_semana, ts->bucket_id, para encajar sin cambios
    en _sweep_dimension). Solo cuenta ballenas con ts_trade <= ts de la
    señal -- fail-closed contra look-ahead (ver idea_gbm_late_reactivo_
    lookahead_refutado_23sep, mismo error real ya cazado en este proyecto)."""
    def clave_bucket(ts: str):
        mid = market_ids_por_ts.get(ts)
        cid = mid_to_cid.get(mid) if mid else None
        if not cid or cid not in ballenas_idx:
            return "sin_ballenas"
        vol_yes = vol_no = 0.0
        for ts_trade, compro_yes, size in ballenas_idx[cid]:
            if ts_trade > ts:
                break  # lista ordenada por ts_trade -- corta en cuanto se pasa de la señal
            if compro_yes:
                vol_yes += size
            else:
                vol_no += size
        if vol_yes + vol_no <= 0:
            return "sin_ballenas"
        mayoria_yes = vol_yes > vol_no
        return "confluye" if mayoria_yes == decision_yes else "diverge"
    return clave_bucket

DIMENSIONES_PENDIENTES = [
    "wallet_subset", "latencia_entrada", "cruce_cross_activo", "tamano_trade",
]  # confluencia_ballenas implementada 28-Sep, ver _bucket_confluencia_factory

# FASE 1B (22-Sep, ver _cargar_filas_pgallina arriba): `pares_permitidos_live`
# mezcla dos familias de tuplas con esquemas de datos totalmente distintos.
# Las "clasicas" (GBM_LATE, FAVORITO_CONFIRMADO, BALLENAS_TARDIAS,
# RESOLUTION_SNIPER, CANDIDATA9/10, MOMENTUM_IBS...) logean en results.csv
# via shadow_predict.py. La familia P-GALLINA (SNIPER/DISPERSO/WALLET_MIRROR/
# WEEKLY_TEMPRANO/WEEKLY_TARDIO#activo#marco#BUY_Up|BUY_Down) -- hoy la
# mayoria de pares_permitidos_live -- vive en bot_wallets_gate_bucket_fase0.
# csv / wallet_mirror_executor_dryrun.csv, ya cubierta por
# _cargar_filas_pgallina().
_PREFIJOS_PGALLINA = ("SNIPER#", "DISPERSO#", "WALLET_MIRROR#",
                      "WEEKLY_TEMPRANO#", "WEEKLY_TARDIO#")


def main() -> int:
    ahora = datetime.now(timezone.utc)
    cutoff = (ahora - timedelta(days=FORWARD_DIAS)).strftime("%Y-%m-%dT00:00:00")

    degradadas = _tuplas_degradadas()
    print(f"[buscador_edge_perdido] tuplas degradadas (live + negativo=true): {len(degradadas)}")

    if not degradadas:
        salida = {"generado_utc": ahora.isoformat(timespec="seconds"), "cutoff": cutoff,
                   "n_tuplas_degradadas": 0, "tuplas": {},
                   "dimensiones_pendientes": DIMENSIONES_PENDIENTES}
        OUT.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
        return 0

    pgallina = [t for t in degradadas if t.startswith(_PREFIJOS_PGALLINA)]
    clasicas = [t for t in degradadas if t not in pgallina]

    tuplas_live_todas = cargar_tuplas_live()
    filas_clasicas = cargar_filas(tuplas_live_todas)

    # confluencia_ballenas: solo tuplas clasicas con filas de verdad. Preparación
    # ÚNICA para todas (no repetir el scan de results.csv/ballenas por tupla).
    # /code-review 28-Sep: esto es un SEGUNDO scan completo de results.csv,
    # además del que ya hace cargar_filas() arriba -- decisión consciente, no
    # descuido: (a) es coste de I/O en streaming (csv.DictReader fila a fila,
    # filtrado por estrategia desde la primera línea), nunca materializa el
    # fichero -- no es la misma clase de bug que los OOM reales de hoy
    # (esos SÍ guardaban estructuras completas en memoria); (b) solo se paga
    # cuando hay tuplas clasicas degradadas de verdad (hoy: 0, coste real =
    # 0) -- no en cada ciclo del fast loop; (c) medido: ~7s para una tupla de
    # 464 señales, de sobra dentro del timeout de 1800s del vigía. Fusionar
    # este scan con el de cargar_filas() (módulo compartido con el gate
    # canónico) para ahorrar esos segundos cambiaría una función usada por
    # dinero real sin necesidad -- el riesgo de esa fusión es mayor que el
    # coste que evita.
    clasicas_con_filas = [t for t in clasicas if filas_clasicas.get(t)]
    market_ids_por_tupla, mid_to_cid, ballenas_idx = {}, {}, {}
    if clasicas_con_filas:
        market_ids_por_tupla = _cargar_market_ids(clasicas_con_filas, tuplas_live_todas)
        # /code-review 28-Sep, riesgo real: _cargar_market_ids() reimplementa
        # a mano el mismo filtro (TWAP/precio-invertido) que cargar_filas() --
        # si algún día diverge un filtro ahí y no aquí, el conjunto de `ts`
        # de ambos dejaría de casar 1:1 y confluencia_ballenas degradaría en
        # SILENCIO a puro "sin_ballenas" (nunca un error, solo cada vez menos
        # señales resueltas). Guarda activa: comparar tamaños y avisar fuerte
        # si divergen más de lo esperable (fail loud, no fail silent).
        for t in clasicas_con_filas:
            n_filas, n_mids = len(filas_clasicas.get(t, [])), len(market_ids_por_tupla.get(t, {}))
            if n_mids < n_filas * 0.9:
                print(f"  ⚠️ confluencia_ballenas: {t} tiene {n_filas} filas (cargar_filas) pero "
                      f"solo {n_mids} market_id resueltos (_cargar_market_ids) -- posible "
                      f"divergencia de filtro entre ambas funciones, revisar antes de fiarse "
                      f"de esta dimensión para esta tupla")
        # ts_por_mid: para poder priorizar por recencia qué resolver vía API
        # (ver más abajo) -- un mismo market_id puede repetirse entre tuplas,
        # nos quedamos con el ts más reciente visto para ese mid. `mid is
        # None` = ts ambiguo (colisión detectada en _cargar_market_ids) --
        # se descarta aquí, nunca se intenta resolver "None" como market_id.
        ts_por_mid: dict[str, str] = {}
        for m_ts in market_ids_por_tupla.values():
            for ts, mid in m_ts.items():
                if mid is None:
                    continue
                if mid not in ts_por_mid or ts > ts_por_mid[mid]:
                    ts_por_mid[mid] = ts
        mids = set(ts_por_mid)
        if mids:
            mid_to_cid = resolver_lote(list(mids), usar_api_fallback=False)
            # /code-review 28-Sep, hallazgo real: una resolución de API fallida
            # (mercado sin conditionId, timeout, 404...) se persiste en el índice
            # como None PARA SIEMPRE (ver market_id_resolver.py::resolver_lote) --
            # `mid_to_cid.get(mid)` no distingue "nunca intentado" de "intentado
            # y fallido", así que sin este chequeo contra el índice crudo los
            # market_id permanentemente irresolubles (mercados muy viejos/
            # expirados fuera de gamma-api) volverían a ocupar el cupo de
            # MAX_RESOLVER_API cada 6h para siempre, desplazando a los market_id
            # genuinamente nuevos que sí podrían resolverse. Solo reintenta los
            # AUSENTES del índice (nunca intentados).
            indice_crudo = _cargar_indice()
            faltan = sorted((mid for mid in mids if mid not in indice_crudo),
                             key=lambda mid: ts_por_mid[mid], reverse=True)[:MAX_RESOLVER_API]
            if faltan:
                n_permanentes = sum(1 for mid in mids if mid in indice_crudo and not indice_crudo[mid])
                print(f"[buscador_edge_perdido] confluencia_ballenas: {len(faltan)} market_id "
                      f"nunca intentados resueltos vía API (más recientes primero, tope "
                      f"{MAX_RESOLVER_API}; {n_permanentes} ya marcados irresolubles, se saltan)")
                mid_to_cid.update(resolver_lote(faltan, usar_api_fallback=True))
        cids = {cid for cid in mid_to_cid.values() if cid}
        if cids:
            ballenas_idx = _index_ballenas(cids)
        print(f"[buscador_edge_perdido] confluencia_ballenas: {len(mids)} market_id, "
              f"{len(cids)}/{len(mids)} resueltos a condition_id, "
              f"{len(ballenas_idx)} con trades de ballenas indexados")

    resultado = {}
    for tupla_str in degradadas:
        filas = (_cargar_filas_pgallina(tupla_str) if tupla_str in pgallina
                 else filas_clasicas.get(tupla_str, []))
        if not filas:
            resultado[tupla_str] = {"n_filas": 0, "dimensiones": {}}
            continue
        dims_out = {}
        for nombre, fn in DIMENSIONES.items():
            cands = _sweep_dimension(filas, cutoff, fn)
            dims_out[nombre] = cands
            if cands:
                ok = [c for c in cands if c["forward_ok"]]
                print(f"  {tupla_str} | {nombre}: {len(cands)} candidato(s) train, "
                      f"{len(ok)} forward_ok")
        if tupla_str in clasicas_con_filas:
            decision_yes = tupla_str.endswith("BUY_YES")
            fn_ballenas = _bucket_confluencia_factory(
                decision_yes, market_ids_por_tupla.get(tupla_str, {}), mid_to_cid, ballenas_idx)
            cands = _sweep_dimension(filas, cutoff, fn_ballenas)
            dims_out["confluencia_ballenas"] = cands
            if cands:
                ok = [c for c in cands if c["forward_ok"]]
                print(f"  {tupla_str} | confluencia_ballenas: {len(cands)} candidato(s) train, "
                      f"{len(ok)} forward_ok")
        resultado[tupla_str] = {"n_filas": len(filas), "dimensiones": dims_out}

    salida = {
        "generado_utc": ahora.isoformat(timespec="seconds"),
        "forward_dias": FORWARD_DIAS, "cutoff": cutoff, "n_forward_min": N_FORWARD_MIN,
        "piso_eur": PISO_EUR,
        "n_tuplas_degradadas": len(degradadas),
        "tuplas": resultado,
        "dimensiones_pendientes": DIMENSIONES_PENDIENTES,
    }
    OUT.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[buscador_edge_perdido] guardado en {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
