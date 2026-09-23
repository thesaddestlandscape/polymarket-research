#!/usr/bin/env python3
"""
bot_consenso_amplio_fase0.py -- FASE 0, 19-Sep, petición explícita Javi:
"vamos a tener que diseñar una estrategia que sea wallet consensum tal y
como tenemos en weather pero para cripto".

CANDIDATA9_BOT_CONSENSO (candidata9_bot_consenso_reactivo_fase0.py) ya
mide consenso mayoritario en cripto, pero el ejecutor real cuenta votos
de las 84 "bot wallets" preclasificadas GLOBALMENTE (bot_wallets_
universo_25ago.json), SIN exigir que cada wallet tenga edge validado
específicamente en el (activo,marco) del mercado que se vota -- una
wallet con edge solo en BTC#weekly cuenta igual que una con edge en
BTC#5min si ambas están en el panel de 84. Este observador corrige eso
desde el diseño (petición explícita Javi, 19-Sep, tras revisar la primera
versión de este fichero -- que contaba CUALQUIER wallet sin exigir edge
propio en absoluto, todavía peor): exige edge confirmado (sig_bhfdr +
g_kelly>0 + edge_pp>0, MISMO umbral que bot_consenso_lib.py) EN EL
(activo,marco) EXACTO del voto, vía wallet_edge_score_por_activo_marco.json
(11587 entradas wallet#activo#marco, ya construido por el proyecto).

⚠️ Mismo hallazgo reportado aparte para CANDIDATA9_BOT_CONSENSO (dinero
real): bot_consenso_lib.py::_cargar_bot_wallets_por_activo() SÍ filtra
por activo pero colapsa todos los marcos de ese activo en un solo set --
mismo bug, impacto medido hoy: 8 de 235 combos wallet-activo con edge
validado en más de un marco. NO se toca aquí (afecta código de dinero
real, requiere aprobación explícita + diseño cuidadoso, CLAUDE.md) -- solo
se corrige en este observador nuevo, que es puramente observacional.

Fuente de datos: polymarket_activity_YYYY-MM-DD.csv (/root/polymarket-
research-datalogs/, fetch_polymarket_activity_ws.py, firehose RTDS real-
time) vía wallet_mirror_tracker.leer_activity_incremental() -- MISMA
fuente, MISMO checkpoint incremental, MISMA función que ya usan
candidata9_bot_consenso_reactivo_fase0.py/bot_wallets_gate_bucket_fase0.py/
dispersed_bot_executor_dryrun.py, reusada sin duplicar (evita repetir el
incidente de CPU del 07-Sep, 4 consumidores releyendo el fichero completo
cada ciclo).

Mecanismo (idéntico a candidata9_bot_consenso_reactivo_fase0.py salvo el
filtro de wallets):
  1. Trackea votos BUY por condition_id de TODOS los activos/marcos, solo
     de wallets con edge validado en ESE (activo,marco) exacto.
  2. En cuanto un voto hace cruzar a mayoría ESTRICTA con >=N_MIN_VOTOS
     votos totales, consulta profundidad real AHORA (detección) y otra
     vez ~3s después (decisión simulada) -- mismo patrón P24 ya probado.
  3. Registra la auditoría completa en bot_consenso_amplio_fase0.csv.

NO existe gate propio todavía (es la pieza 2 del diseño, pendiente) --
por eso, a diferencia de candidata9_bot_consenso_reactivo_fase0.py, este
observador NUNCA registra en predictions_YYYY-MM-DD.csv (no hay zona
confirmada contra la que consultar; registrar sin gate contaminaría el
aprendizaje causal con datos sin filtrar, mismo criterio documentado en
el hermano). Puramente observacional -- construir gate_bucket propio
(mismo rigor Wilson+shuffle+bootstrap+concentración+BH-FDR+tolerancia
2-de-3-días que el resto del proyecto) es el siguiente paso, una vez haya
n suficiente aquí.

NO coloca, cancela ni modifica ninguna orden real.

Se fusiona en observadores_fase0.py (screen "observadores") -- NUNCA
lanzar una screen suelta para este script (mismo criterio de presupuesto
de CPU ya aplicado a los hermanos, py-spy encontró 85 hilos vivos ahí).

Resolución periódica (cron, llamadas de red, NO en el loop en vivo):
  .venv/bin/python bot_consenso_amplio_fase0.py --resolver
"""
import csv
from escritura_atomica import escribir_csv_atomico  # 23-Sep, ver ese módulo
import fcntl
import json
import sys
import threading
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from wallet_mirror_tracker import (  # noqa: E402
    _fillability_mirror, outcome_por_slug, leer_activity_incremental,
)

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "bot_consenso_amplio_fase0.csv"
OUT_LOCK = DIR_SHADOW / "bot_consenso_amplio_fase0.csv.lock"

# 19-Sep (petición explícita Javi, tras la primera versión sin filtro:
# "tienen que ser wallets con edge validado, hit rate, pnl muy positivo
# en el activo y marco temporal que entre el trade"): la primera versión
# contaba CUALQUIER wallet, sin exigir edge propio -- puro ruido de
# consenso, ni siquiera el filtro (más laxo) que ya usa CANDIDATA9.
# wallet_edge_score_por_activo_marco.json (11587 entradas,
# wallet#activo#marco) es la fuente de verdad ya existente en el
# proyecto (usada por bot_consenso_lib.py::_cargar_bot_wallets_por_activo,
# mismo umbral sig_bhfdr+g_kelly>0+edge_pp>0) -- MISMO umbral aquí, pero
# exigiendo (activo,marco) EXACTOS, no solo activo (hallazgo real de esta
# sesión: _cargar_bot_wallets_por_activo() colapsa todos los marcos de un
# activo en un solo set, dejando que una wallet validada solo en
# BTC#weekly cuente también para BTC#5min -- 8 de 235 combos wallet-
# activo afectados hoy; ver feedback de la sesión, bug reportado aparte
# para CANDIDATA9_BOT_CONSENSO, que SÍ toca dinero real y no se toca aquí
# sin aprobación explícita).
WEDGE_PATH = DIR_SHADOW / "wallet_edge_score_por_activo_marco.json"
# El firehose (polymarket_activity_*.csv) usa "5min"/"15min"/"60min"/
# "240min"; wallet_edge_score_por_activo_marco.json usa "5m"/"15m"/"60m"/
# "240m"/"weekly" -- mapeo explícito, nunca asumir que coinciden.
_MARCO_A_WEDGE = {"5min": "5m", "15min": "15m", "60min": "60m", "240min": "240m", "weekly": "weekly"}

_wallets_validadas_cache: dict = {"mtime": None, "por_activo_marco": {}}


def _cargar_wallets_validadas_por_activo_marco(activo: str, marco: str) -> frozenset:
    """frozenset de wallets con edge confirmado (sig_bhfdr + g_kelly>0 +
    edge_pp>0) específicamente para (activo, marco) -- fail-closed:
    fichero ausente/corrupto o combinación sin ninguna wallet validada
    todavía -> frozenset() vacío (ningún voto cuenta, nunca se asume)."""
    global _wallets_validadas_cache
    marco_wedge = _MARCO_A_WEDGE.get(marco)
    if marco_wedge is None:
        return frozenset()
    try:
        mtime = WEDGE_PATH.stat().st_mtime
    except OSError:
        return frozenset()
    if _wallets_validadas_cache["mtime"] != mtime:
        try:
            wedge = json.loads(WEDGE_PATH.read_text(encoding="utf-8"))
        except Exception:
            return _wallets_validadas_cache["por_activo_marco"].get((activo, marco_wedge), frozenset())
        por_am: dict = {}
        for v in wedge.values():
            if not (v.get("sig_bhfdr") and v.get("g_kelly", 0) > 0 and v.get("edge_pp", 0) > 0):
                continue
            a, m, w = v.get("activo"), v.get("marco"), (v.get("wallet") or "").lower()
            if not a or not m or not w:
                continue
            por_am.setdefault((a, m), set()).add(w)
        por_am = {k: frozenset(ws) for k, ws in por_am.items()}
        _wallets_validadas_cache = {"mtime": mtime, "por_activo_marco": por_am}
    return _wallets_validadas_cache["por_activo_marco"].get((activo, marco_wedge), frozenset())
VISTOS_PATH = DIR_SHADOW / "bot_consenso_amplio_fase0_vistos.json"
ACTIVITY_CHECKPOINT_PATH = DIR_SHADOW / "bot_consenso_amplio_fase0_activity_checkpoint.json"
MAX_SLUGS_POR_CICLO = 150  # mismo cap que wallet_mirror_tracker.py::resolver_pendientes

N_MIN_VOTOS = 3  # mismo mínimo que candidata9_bot_consenso_reactivo_fase0.py
STEP_BUCKET = 0.05  # mismo STEP que gate_bucket_propio.py/bot_wallets_gate_bucket.py
SEGUNDA_CONSULTA_ESPERA_S = 3.0
POLL_S = 5
RATIO_MIN = 5.0

COLUMNS = [
    "timestamp_utc", "trade_timestamp_trigger", "condition_id", "market_slug",
    "activo", "marco", "lado_mayoria", "n_votos_mayoria", "n_votos_total",
    "bucket_precio", "precio_trigger",
    "ratio_deteccion", "ask_deteccion", "ratio_decision", "ask_decision",
    "degradacion_ask_pct", "sigue_fillable_en_decision",
    "outcome_real", "acierto", "resolved_ts",
]


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _bucket(p: float) -> float:
    import math
    return round(math.floor(p / STEP_BUCKET + 1e-9) * STEP_BUCKET, 4)


def _vistos_cargar() -> set:
    try:
        return set(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return set()


def _vistos_guardar(vistos: set) -> None:
    VISTOS_PATH.write_text(json.dumps(list(vistos)[-100000:]), encoding="utf-8")


def _escribir_auditoria(fila: dict) -> None:
    nuevo = not OUT.exists()
    lock_f = open(OUT_LOCK, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)
    finally:
        fcntl.flock(lock_f, fcntl.LOCK_UN)
        lock_f.close()


def _completar_decision_en_hilo(condition_id: str, market_slug: str, lado_mayoria: str,
                                 trigger: dict, ask_det, ratio_det, token_id) -> None:
    time.sleep(SEGUNDA_CONSULTA_ESPERA_S)
    fill_dec = _fillability_mirror(market_slug, lado_mayoria, trigger["precio"], token_id)
    ask_dec = fill_dec.get("mejor_ask")
    ratio_dec = fill_dec.get("ratio_vs_stake") if fill_dec.get("ok") else None

    degradacion = None
    if ask_det is not None and ask_dec is not None and ask_det > 0:
        degradacion = round((ask_dec - ask_det) / ask_det * 100, 2)

    sigue_fillable = bool(ratio_dec is not None and ratio_dec >= RATIO_MIN)

    try:
        precio_bucket = float(trigger["precio"])
    except (TypeError, ValueError):
        precio_bucket = None

    _log(f"[{trigger['activo']}#{trigger['marco']}] {condition_id[:12]}.. "
         f"TRIGGER lado={lado_mayoria} n_votos={trigger['n_mayoria']}/{trigger['n_total']} "
         f"ask_det={ask_det} ratio_det={ratio_det} -> ask_dec={ask_dec} ratio_dec={ratio_dec} "
         f"degradacion={degradacion}% sigue_fillable={sigue_fillable}")

    _escribir_auditoria({
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "trade_timestamp_trigger": trigger["ts"], "condition_id": condition_id,
        "market_slug": market_slug, "activo": trigger["activo"], "marco": trigger["marco"],
        "lado_mayoria": lado_mayoria, "n_votos_mayoria": trigger["n_mayoria"],
        "n_votos_total": trigger["n_total"],
        "bucket_precio": f"{_bucket(precio_bucket):.2f}" if precio_bucket is not None else "",
        "precio_trigger": trigger["precio"],
        "ratio_deteccion": ratio_det, "ask_deteccion": ask_det,
        "ratio_decision": ratio_dec, "ask_decision": ask_dec,
        "degradacion_ask_pct": degradacion, "sigue_fillable_en_decision": int(sigue_fillable),
        "outcome_real": "", "acierto": "", "resolved_ts": "",
    })


def _procesar_condition(condition_id: str, votos: list[dict], vistos_trigger: set) -> None:
    if condition_id in vistos_trigger:
        return
    if len(votos) < N_MIN_VOTOS:
        return
    votos_ordenados = sorted(votos, key=lambda r: r["ts"])
    lado_final: dict = defaultdict(int)
    for v in votos_ordenados:
        lado_final[v["lado"]] += 1
    if len(lado_final) < 2:
        return
    lado_mayoria = max(lado_final, key=lado_final.get)
    n_mayoria = lado_final[lado_mayoria]
    n_total = sum(lado_final.values())
    if n_mayoria == n_total - n_mayoria:
        return  # empate, no hay mayoría estricta

    conteo: dict = defaultdict(int)
    trigger_row = None
    for v in votos_ordenados:
        conteo[v["lado"]] += 1
        resto = sum(n for lado, n in conteo.items() if lado != lado_mayoria)
        if conteo[lado_mayoria] > resto and v["lado"] == lado_mayoria:
            trigger_row = v
            break
    if trigger_row is None:
        return

    vistos_trigger.add(condition_id)
    market_slug = trigger_row["market_slug"]
    trigger = {
        "ts": trigger_row["ts"], "precio": trigger_row["precio"],
        "activo": trigger_row["activo"], "marco": trigger_row["marco"],
        "n_mayoria": n_mayoria, "n_total": n_total,
    }

    fill_det = _fillability_mirror(market_slug, lado_mayoria, trigger_row["precio"])
    ask_det = fill_det.get("mejor_ask")
    ratio_det = fill_det.get("ratio_vs_stake") if fill_det.get("ok") else None

    threading.Thread(
        target=_completar_decision_en_hilo,
        args=(condition_id, market_slug, lado_mayoria, trigger, ask_det, ratio_det, fill_det.get("token_id")),
        daemon=True,
    ).start()


def resolver_pendientes() -> int:
    """Mismo patrón exacto que bot_wallets_gate_bucket_fase0.py::
    resolver_pendientes() -- reusa outcome_por_slug() de
    wallet_mirror_tracker.py, sin lock para la lectura/red, lock solo
    para la reescritura final (releer fresco por si el observador vivo
    añadió filas mientras tanto)."""
    if not OUT.exists():
        return 0
    with open(OUT, newline="", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))

    slugs_pendientes = sorted({r["market_slug"] for r in filas
                                if not r.get("outcome_real") and r.get("market_slug")})
    outcomes_por_slug = {}
    for slug in slugs_pendientes[:MAX_SLUGS_POR_CICLO]:
        outcome = outcome_por_slug(slug)
        if outcome is not None:
            outcomes_por_slug[slug] = outcome

    if not outcomes_por_slug:
        return 0

    lock_f = open(OUT_LOCK, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        try:
            with open(OUT, newline="", encoding="utf-8") as f:
                filas = list(csv.DictReader(f))
            resueltas = 0
            for r in filas:
                if r.get("outcome_real"):
                    continue
                outcome = outcomes_por_slug.get(r.get("market_slug"))
                if outcome is None:
                    continue
                r["outcome_real"] = outcome
                r["acierto"] = "1" if outcome == r.get("lado_mayoria") else "0"
                r["resolved_ts"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
                resueltas += 1
            if resueltas:
                # 23-Sep: atómico (ver escritura_atomica.py -- incidente WM executor CSV truncado)
                escribir_csv_atomico(OUT, COLUMNS, filas)
            return resueltas
        finally:
            fcntl.flock(lock_f, fcntl.LOCK_UN)
    finally:
        lock_f.close()


def main() -> None:
    vistos = _vistos_cargar()
    vistos_trigger: set = set()
    votos_por_condition: dict = defaultdict(list)

    _log("bot_consenso_amplio_fase0 arrancado -- vigilando TODOS los activos/marcos, "
         "solo wallets con edge validado (sig_bhfdr+g_kelly>0+edge_pp>0) EN ESE "
         f"(activo,marco) exacto vía {WEDGE_PATH.name}, N_MIN_VOTOS=3")

    # Backlog existente: marcar como visto sin procesar (mismo criterio
    # que candidata9_bot_consenso_reactivo_fase0.py -- medir fill-ability
    # del pasado no tiene sentido, solo importa lo que llegue desde ahora).
    for row in leer_activity_incremental(ACTIVITY_CHECKPOINT_PATH):
        if (row.get("side") or "").strip().upper() != "BUY":
            continue
        w = (row.get("wallet") or "").lower()
        vistos.add(f"{w}|{row.get('market_slug', '')}")
    _vistos_guardar(vistos)
    _log(f"backlog marcado como visto ({len(vistos)} entradas)")

    while True:
        try:
            hubo_matches = False
            for row in leer_activity_incremental(ACTIVITY_CHECKPOINT_PATH):
                if (row.get("side") or "").strip().upper() != "BUY":
                    continue
                w = (row.get("wallet") or "").lower()
                market_slug = row.get("market_slug", "")
                dedup_key = f"{w}|{market_slug}"
                if dedup_key in vistos:
                    continue
                vistos.add(dedup_key)
                hubo_matches = True
                activo = row.get("activo", "")
                marco = row.get("marco", "")
                if not activo or not marco:
                    continue  # sin activo/marco clasificado, no se puede bucketizar
                if w not in _cargar_wallets_validadas_por_activo_marco(activo, marco):
                    continue  # sin edge propio confirmado en ESTE (activo,marco) -- no cuenta como voto
                try:
                    precio = float(row.get("price") or 0)
                except (TypeError, ValueError):
                    continue
                if not (0.0 < precio < 1.0):
                    continue
                condition_id = row.get("condition_id", "")
                if not condition_id:
                    continue
                votos_por_condition[condition_id].append({
                    "ts": row.get("timestamp_utc", ""),
                    "lado": row.get("outcome", ""),
                    "precio": row.get("price", ""),
                    "market_slug": market_slug,
                    "activo": activo, "marco": marco,
                })
            if hubo_matches:
                _vistos_guardar(vistos)

            for condition_id, votos in list(votos_por_condition.items()):
                if condition_id in vistos_trigger:
                    continue
                _procesar_condition(condition_id, votos, vistos_trigger)

            # limpiar condition_ids ya disparados hace tiempo (evita crecer sin límite)
            if len(votos_por_condition) > 2000:
                for cid in list(vistos_trigger)[:1000]:
                    votos_por_condition.pop(cid, None)

        except Exception as e:
            _log(f"🚨 error en ciclo: {type(e).__name__}: {e}")
        time.sleep(POLL_S)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--resolver":
        n = resolver_pendientes()
        _log(f"resueltas: {n}")
    else:
        main()
