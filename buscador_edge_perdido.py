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

## Dimensiones NO cubiertas todavía (fase 2, roadmap explícito, NO fingir
que están hechas):
  - subconjunto de wallets (aplica a WALLET_MIRROR/bot_wallets -- requiere
    cruzar con wallet_mirror_tracker/bot_wallets, estructura de datos
    distinta a results.csv)
  - latencia de entrada (requiere libro_snapshots.csv o el CSV de fase0
    específico de cada ejecutor, no unificado)
  - confluencia con ballenas/smart money (requiere ballenas_timing_history.
    csv, cruce por market_id)
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
)
from gate_dias_independientes import robustez_dias  # noqa: E402
from shuffle_chunked import diffs_permutacion  # noqa: E402

CONFIG_LIVE = REPO / "data/live/config_live.json"
LATCH_DEGRADACION = REPO / "data/live/vigia_degradacion_live_latch.json"
OUT = REPO / "data/shadow/buscador_edge_perdido.json"

FORWARD_DIAS = 7          # mismo horizonte que edge_quirurgico_rolling.py
N_FORWARD_MIN = 15
PISO_EUR = 0.10
ITERS = 1000
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

DIMENSIONES_PENDIENTES = [
    "wallet_subset", "latencia_entrada", "confluencia_ballenas",
    "cruce_cross_activo", "tamano_trade",
]

# 22-Sep, hallazgo real durante el diseño: `pares_permitidos_live` mezcla dos
# familias de tuplas con esquemas de datos TOTALMENTE distintos. Las
# estrategias "clasicas" (GBM_LATE, FAVORITO_CONFIRMADO, BALLENAS_TARDIAS,
# RESOLUTION_SNIPER, CANDIDATA9/10, MOMENTUM_IBS...) logean en results.csv
# via shadow_predict.py -- esas SI las cubre cargar_filas() de arriba. Pero
# HOY la mayoria de pares_permitidos_live (23/23 al diseñar esto) son la
# familia P-GALLINA (SNIPER/DISPERSO/WALLET_MIRROR/WEEKLY_TEMPRANO/
# WEEKLY_TARDIO#activo#marco#BUY_Up|BUY_Down) -- esas viven en
# bot_wallets_gate_bucket_fase0.csv / wallet_mirror_executor_dryrun.csv
# (leidas por analisis_bot_wallets_gate_bucket_25ago.py::cargar_filas() /
# analisis_wallet_mirror_gate_bucket_10ago.py::cargar_filas(), con claves de
# grupo y forma de tupla (ts,val,pnl,...) distintas -- el mismo motor de
# edge_quirurgico_rolling.py ya resuelve ese mapeo). Migrar ese mapeo aqui es
# FASE 1B, sin implementar todavia (no fingir cobertura que no existe --
# CLAUDE.md "claves de features fantasma"). V1 se limita a la familia de
# results.csv y lo dice explicitamente en la salida por cada tupla que no
# pueda resolver.
_PREFIJOS_SIN_LOADER = ("SNIPER#", "DISPERSO#", "WALLET_MIRROR#",
                        "WEEKLY_TEMPRANO#", "WEEKLY_TARDIO#")


def main() -> int:
    ahora = datetime.now(timezone.utc)
    cutoff = (ahora - timedelta(days=FORWARD_DIAS)).strftime("%Y-%m-%dT00:00:00")

    degradadas = _tuplas_degradadas()
    print(f"[buscador_edge_perdido] tuplas degradadas (live + negativo=true): {len(degradadas)}")

    sin_loader = [t for t in degradadas if t.startswith(_PREFIJOS_SIN_LOADER)]
    con_loader = [t for t in degradadas if t not in sin_loader]
    if sin_loader:
        print(f"[buscador_edge_perdido] ⚠️ {len(sin_loader)} degradadas son familia "
              f"P-GALLINA (SNIPER/DISPERSO/WALLET_MIRROR/WEEKLY_*) -- loader FASE 1B "
              f"pendiente, no evaluadas todavia: {sin_loader}")

    if not degradadas:
        salida = {"generado_utc": ahora.isoformat(timespec="seconds"), "cutoff": cutoff,
                   "n_tuplas_degradadas": 0, "tuplas": {},
                   "dimensiones_pendientes": DIMENSIONES_PENDIENTES}
        OUT.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
        return 0

    tuplas_live_todas = cargar_tuplas_live()
    filas_por_tupla = cargar_filas(tuplas_live_todas)

    resultado = {t: {"n_filas": 0, "dimensiones": {}, "sin_loader": True,
                      "motivo": "familia P-GALLINA, loader FASE 1B pendiente"}
                 for t in sin_loader}
    for tupla_str in con_loader:
        filas = filas_por_tupla.get(tupla_str, [])
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
