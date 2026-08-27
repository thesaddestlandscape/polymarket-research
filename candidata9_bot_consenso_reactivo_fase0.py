#!/usr/bin/env python3
"""
candidata9_bot_consenso_reactivo_fase0.py -- 27-Ago, observador de baja
latencia dedicado para CANDIDATA9_BOT_CONSENSO#BTC#5min, petición
explícita Javi tras confirmar con rigor completo (n=151 fillable, 4/4
días positivos, 45 wallets, sin concentración) que el consenso mayoritario
de bot wallets en BTC#5min tiene edge real en la zona [0.50,0.55).

Por qué hace falta un observador nuevo, no basta con bot_wallets_gate_
bucket_fase0.py: ese script (25-Ago) mide fill-ability en el instante de
DETECCIÓN de cada trade individual (poll 15s sobre el firehose ya
escrito en disco), pero NUNCA registra el evento en predictions_
YYYY-MM-DD.csv -- vive fuera del pipeline estándar del proyecto
(shadow_resolve.py/shadow_postmortem.py/gate_bucket_propio.py nunca lo
ven). Este observador SÍ registra la predicción con STRATEGY sintética,
para que el candidato entre en la maquinaria estándar (n, IC, gate por
micro-bucket, log-growth) antes de añadirlo a candidatos_evaluacion_live.

Añade además la "segunda consulta" (mismo patrón P24 que
wallet_mirror_executor_dryrun.py, ya probado real en cripto hoy mismo):
mide profundidad en el instante de DETECCIÓN del voto que cruza a
mayoría estricta, y otra vez unos segundos después (instante de
DECISIÓN simulada) -- para saber si la oportunidad se degrada entre
medias, algo que bot_wallets_gate_bucket_fase0.py nunca midió.

Mecanismo (reactivo, poll rápido sobre el firehose ya en disco --
fetch_polymarket_activity_ws.py sigue siendo la fuente real-time, este
script solo lee lo que ya escribió, mismo patrón que bot_wallets_gate_
bucket_fase0.py):
  1. Trackea votos por condition_id (activo=BTC, marco=5min) de las bot
     wallets ya validadas (bot_wallets_universo_25ago.json).
  2. En cuanto un voto hace cruzar a mayoría ESTRICTA (misma lógica
     exacta que analisis_candidata9_10_gate_bucket_26ago.py::
     eventos_candidata9(), sin look-ahead), consulta profundidad real
     AHORA (detección) y otra vez ~3s después (decisión simulada).
  3. Si el precio cae en [0.50,0.55) (la única zona confirmada hoy) Y
     sigue fillable en el instante de decisión, registra la predicción
     en predictions_YYYY-MM-DD.csv con STRATEGY="CANDIDATA9_BOT_CONSENSO"
     -- fuera de esa zona, solo se audita (no se registra como
     predicción, evita contaminar el aprendizaje causal con zonas no
     confirmadas, mismo criterio que el resto de fase0 del proyecto).

NO coloca, cancela ni modifica ninguna orden real. STRATEGY sintética,
nunca puede estar en pares_permitidos_live directamente (se promociona
como el resto: vía gate_bucket_propio + checklist + decisión de Javi).

Se fusiona en observadores_fase0.py (screen "observadores") -- NUNCA
lanzar una screen suelta para este script.
"""
import csv
import fcntl
import json
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from wallet_mirror_tracker import _archivos_activity, _fillability_mirror  # noqa: E402
from market_id_resolver import resolver_inverso  # noqa: E402

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "candidata9_bot_consenso_reactivo_fase0.csv"
VISTOS_PATH = DIR_SHADOW / "candidata9_bot_consenso_reactivo_fase0_vistos.json"
PREDICTIONS_LOCK_PATH = DIR_SHADOW / ".predictions_lock"
BOTS_PATH = DIR_SHADOW / "bot_wallets_universo_25ago.json"

STRATEGY = "CANDIDATA9_BOT_CONSENSO"  # sintética, nunca en pares_permitidos_live directamente
ACTIVO = "BTC"
MARCO = "5min"
BUCKET_LO, BUCKET_HI = 0.50, 0.55  # única zona confirmada hoy con rigor completo
N_MIN_VOTOS = 3  # mismo mínimo que analisis_candidata9_10_gate_bucket_26ago.py
SEGUNDA_CONSULTA_ESPERA_S = 3.0
POLL_S = 5
RATIO_MIN = 5.0

COLUMNS = [
    "timestamp_utc", "trade_timestamp", "condition_id", "market_slug",
    "lado_mayoria", "n_votos_trigger", "precio_trigger",
    "ratio_deteccion", "ask_deteccion", "ratio_decision", "ask_decision",
    "degradacion_ask_pct", "sigue_fillable_en_decision",
    "en_zona_confirmada", "registrada_prediccion",
]


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _cargar_bots() -> set:
    try:
        return set(json.loads(BOTS_PATH.read_text(encoding="utf-8")).keys())
    except Exception:
        return set()


def _vistos_cargar() -> set:
    try:
        return set(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return set()


def _vistos_guardar(vistos: set) -> None:
    VISTOS_PATH.write_text(json.dumps(list(vistos)[-50000:]), encoding="utf-8")


def _escribir_auditoria(fila: dict) -> None:
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        if nuevo:
            w.writeheader()
        w.writerow(fila)


def _registrar_prediccion(condition_id: str, market_slug: str, lado_mayoria: str,
                           py: float, restante_s: float | None) -> None:
    """Mismo formato que el resto de ejecutores de baja latencia --
    shadow_resolve.py/shadow_postmortem.py lo resuelven sin duplicar
    lógica aquí.

    27-Ago, bug real corregido (mismo hallazgo que en el gemelo
    candidata10_confirmacion_cruzada_reactivo_fase0.py): `market_id`
    exige el ID numérico de gamma-api, el condition_id crudo daba 422 y
    ninguna predicción se resolvía nunca. Resuelto vía
    market_id_resolver.resolver_inverso(); si no resuelve, se descarta
    fail-closed."""
    market_id = resolver_inverso(condition_id)
    if not market_id:
        _log(f"aviso: no se pudo resolver market_id para condition_id={condition_id} -- predicción descartada")
        return
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    archivo = DIR_SHADOW / f"predictions_{ts[:10]}.csv"
    subtype = f"{ACTIVO}#{MARCO}"
    decision = "BUY_YES" if lado_mayoria in ("Up", "Yes") else "BUY_NO"
    prob_yes = min(0.97, py + 0.03) if decision == "BUY_YES" else max(0.03, py - 0.03)
    edge = prob_yes - py
    horas_venc = (restante_s / 3600.0) if restante_s is not None else 0.02
    features = json.dumps({
        "py_entrada": round(py, 4), "lado_mayoria": lado_mayoria,
        "ejecutor_baja_latencia": True, "fase0_solo_observacion": True,
        "candidata9_zona_confirmada": True,
    }, separators=(",", ":"))
    try:
        with open(PREDICTIONS_LOCK_PATH, "w") as lock_f:
            fcntl.flock(lock_f, fcntl.LOCK_EX)
            try:
                nuevo = not archivo.exists()
                with open(archivo, "a", newline="", encoding="utf-8") as f:
                    w = csv.writer(f)
                    if nuevo:
                        w.writerow([
                            "timestamp_utc", "strategy", "market_id", "question", "end_date",
                            "horas_a_vencimiento", "precio_yes_mercado", "prob_yes_modelo",
                            "edge_bruto", "edge_neto", "edge_direccional", "decision", "razon",
                            "subtype", "apuesta", "features",
                        ])
                    w.writerow([
                        ts, STRATEGY, market_id, "", "",
                        f"{horas_venc:.4f}", f"{py:.4f}", f"{prob_yes:.4f}",
                        f"{edge:.4f}", f"{edge:.4f}", f"{edge:.4f}", decision,
                        "candidata9_bot_consenso_reactivo", subtype, "1.05", features,
                    ])
            finally:
                fcntl.flock(lock_f, fcntl.LOCK_UN)
    except Exception as e:
        _log(f"aviso: no se pudo registrar predicción: {e}")


def _procesar_condition(condition_id: str, votos: list[dict], vistos_trigger: set) -> None:
    if condition_id in vistos_trigger:
        return
    if len(votos) < N_MIN_VOTOS:
        return
    votos_ordenados = sorted(votos, key=lambda r: r["ts"])
    conteo = defaultdict(int)
    lado_final = defaultdict(int)
    for v in votos_ordenados:
        lado_final[v["lado"]] += 1
    if len(lado_final) < 2:
        return
    lado_mayoria = max(lado_final, key=lado_final.get)
    n_mayoria = lado_final[lado_mayoria]
    n_total = sum(lado_final.values())
    if n_mayoria == n_total - n_mayoria:
        return  # empate, no hay mayoría estricta

    trigger = None
    for v in votos_ordenados:
        conteo[v["lado"]] += 1
        resto = sum(n for lado, n in conteo.items() if lado != lado_mayoria)
        if conteo[lado_mayoria] > resto and v["lado"] == lado_mayoria:
            trigger = v
            break
    if trigger is None:
        return

    vistos_trigger.add(condition_id)
    market_slug = trigger["market_slug"]

    fill_det = _fillability_mirror(market_slug, lado_mayoria, trigger["precio"])
    ask_det = fill_det.get("mejor_ask")
    ratio_det = fill_det.get("ratio_vs_stake") if fill_det.get("ok") else None

    time.sleep(SEGUNDA_CONSULTA_ESPERA_S)
    fill_dec = _fillability_mirror(market_slug, lado_mayoria, trigger["precio"],
                                    fill_det.get("token_id"))
    ask_dec = fill_dec.get("mejor_ask")
    ratio_dec = fill_dec.get("ratio_vs_stake") if fill_dec.get("ok") else None

    degradacion = None
    if ask_det is not None and ask_dec is not None and ask_det > 0:
        degradacion = round((ask_dec - ask_det) / ask_det * 100, 2)

    sigue_fillable = bool(ratio_dec is not None and ratio_dec >= RATIO_MIN)
    py_ref = ask_dec if ask_dec is not None else (ask_det if ask_det is not None else trigger["precio"])
    en_zona = bool(py_ref is not None and BUCKET_LO <= py_ref < BUCKET_HI)

    registrada = False
    if en_zona and sigue_fillable:
        _registrar_prediccion(condition_id, market_slug, lado_mayoria, py_ref, None)
        registrada = True

    _log(f"[{condition_id}] TRIGGER lado={lado_mayoria} n_votos={n_mayoria}/{n_total} "
         f"ask_det={ask_det} ratio_det={ratio_det} -> ask_dec={ask_dec} ratio_dec={ratio_dec} "
         f"degradacion={degradacion}% zona_confirmada={en_zona} registrada={registrada}")

    _escribir_auditoria({
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "trade_timestamp": trigger["ts"], "condition_id": condition_id,
        "market_slug": market_slug, "lado_mayoria": lado_mayoria,
        "n_votos_trigger": n_mayoria, "precio_trigger": trigger["precio"],
        "ratio_deteccion": ratio_det, "ask_deteccion": ask_det,
        "ratio_decision": ratio_dec, "ask_decision": ask_dec,
        "degradacion_ask_pct": degradacion, "sigue_fillable_en_decision": int(sigue_fillable),
        "en_zona_confirmada": int(en_zona), "registrada_prediccion": int(registrada),
    })


def main() -> None:
    bots = _cargar_bots()
    if not bots:
        _log(f"⚠️ sin wallets en {BOTS_PATH} -- nada que vigilar")
        return
    vistos = _vistos_cargar()
    vistos_trigger = set()
    votos_por_condition: dict[str, list[dict]] = defaultdict(list)

    _log(f"arrancado -- {len(bots)} bot wallets, vigilando {ACTIVO}#{MARCO} zona [{BUCKET_LO},{BUCKET_HI})")

    # Backlog existente: marcar como visto sin procesar (mismo fix que
    # bot_wallets_gate_bucket_fase0.py -- medir fill-ability del pasado
    # no tiene sentido, solo importa lo que llegue de ahora en adelante).
    for path in _archivos_activity():
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if (row.get("side") or "").strip().upper() != "BUY":
                    continue
                w = (row.get("wallet") or "").lower()
                if w not in bots:
                    continue
                vistos.add(f"{w}|{row.get('market_slug','')}")
    _vistos_guardar(vistos)
    _log(f"backlog marcado como visto ({len(vistos)} matches históricos)")

    while True:
        try:
            for path in _archivos_activity():
                with open(path, encoding="utf-8") as f:
                    for row in csv.DictReader(f):
                        if (row.get("side") or "").strip().upper() != "BUY":
                            continue
                        w = (row.get("wallet") or "").lower()
                        if w not in bots:
                            continue
                        market_slug = row.get("market_slug", "")
                        dedup_key = f"{w}|{market_slug}"
                        if dedup_key in vistos:
                            continue
                        vistos.add(dedup_key)
                        if row.get("activo") != ACTIVO or row.get("marco") != MARCO:
                            continue
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
                        })
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
            _log(f"error en ciclo: {e} -- reintenta en {POLL_S}s")
        time.sleep(POLL_S)


if __name__ == "__main__":
    main()
