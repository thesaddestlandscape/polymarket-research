#!/usr/bin/env python3
"""
candidata10_confirmacion_cruzada_reactivo_fase0.py -- 27-Ago, observador
de baja latencia dedicado para CANDIDATA10_CONFIRMACION_CRUZADA#BTC,
petición explícita Javi tras confirmar con rigor completo (26-Ago, sin
look-ahead + split-half + BH-FDR, ver idea_candidata9_10_edge_precio_
confirmado_26ago): cuando una bot wallet ya validada opera BTC y esa
MISMA wallet operó OTRO activo en la MISMA dirección en los 30 minutos
previos, el trade de BTC acierta significativamente más que el ask real
implica -- BTC#5min con_confirm n=3.530 edge+5.7pp p=0.0000 fill=55.2%,
BTC#15min con_confirm n=1.455 edge+3.4pp p=0.0036 fill=61.6%, ambos
split-half consistentes.

Mismo hueco que motivó el observador de Candidata 9 (candidata9_bot_
consenso_reactivo_fase0.py, mismo día): bot_wallets_gate_bucket_fase0.py
mide fill-ability en detección pero NUNCA registra en predictions_
YYYY-MM-DD.csv -- este observador sí, para que el candidato entre en la
maquinaria estándar (gate_bucket_propio, log-growth) camino a
candidatos_evaluacion_live.

A diferencia de Candidata 9 (una zona de PRECIO concreta [0.50,0.55)),
Candidata 10 no tiene restricción de bucket de precio en el hallazgo
original -- la señal es la confirmación cruzada en sí (edge = hit -
ask_mediana agregado). Aun así, se exige `ratio_vs_stake>=5x` en la
segunda consulta (patrón P24, igual que Candidata 9) antes de registrar
nada -- auditar todo, registrar solo lo fillable.

Mecanismo:
  1. Trackea, por wallet bot validada, los trades recientes (<=30min) en
     CUALQUIER activo -- necesario para saber si hay confirmación
     cruzada cuando llegue un trade de BTC.
  2. Cuando llega un trade BUY de BTC 5min o 15min de una bot wallet, si
     esa MISMA wallet tiene un trade PREVIO (<=30min, activo distinto,
     MISMO lado) ya registrado -> CONFIRMACIÓN CRUZADA, dispara.
  3. Segunda consulta 3s después (mismo patrón P24/Candidata 9) --
     registra predicción SOLO si sigue fillable (ratio_vs_stake>=5x) en
     el instante de decisión. Sin restricción de bucket de precio (a
     diferencia de Candidata 9).

NO coloca, cancela ni modifica ninguna orden real. STRATEGY sintética,
nunca puede estar en pares_permitidos_live directamente.

Se fusiona en observadores_fase0.py (screen "observadores") -- NUNCA
lanzar una screen suelta para este script.
"""
import csv
import fcntl
import json
import sys
import time
from collections import defaultdict, deque
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from wallet_mirror_tracker import _archivos_activity, _fillability_mirror  # noqa: E402

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "candidata10_confirmacion_cruzada_reactivo_fase0.csv"
VISTOS_PATH = DIR_SHADOW / "candidata10_confirmacion_cruzada_reactivo_fase0_vistos.json"
PREDICTIONS_LOCK_PATH = DIR_SHADOW / ".predictions_lock"
BOTS_PATH = DIR_SHADOW / "bot_wallets_universo_25ago.json"

STRATEGY = "CANDIDATA10_CONFIRMACION_CRUZADA"  # sintética, nunca en pares_permitidos_live directamente
ACTIVO_OBJETIVO = "BTC"
MARCOS_OBJETIVO = {"5min", "15min"}  # únicos 2 confirmados con rigor 26-Ago
VENTANA_CONFIRM_S = 30 * 60  # mismo criterio que analisis_candidata10_v2_sinlookahead_26ago.py
SEGUNDA_CONSULTA_ESPERA_S = 3.0
POLL_S = 5
RATIO_MIN = 5.0

COLUMNS = [
    "timestamp_utc", "trade_timestamp", "wallet", "condition_id", "market_slug",
    "marco", "lado", "confirm_activo", "confirm_lag_s",
    "precio_trigger", "ratio_deteccion", "ask_deteccion",
    "ratio_decision", "ask_decision", "degradacion_ask_pct",
    "sigue_fillable_en_decision", "registrada_prediccion",
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


def _registrar_prediccion(condition_id: str, marco: str, lado: str, py: float) -> None:
    """Mismo formato que candidata9_bot_consenso_reactivo_fase0.py --
    shadow_resolve.py/shadow_postmortem.py lo resuelven sin duplicar
    lógica aquí."""
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    archivo = DIR_SHADOW / f"predictions_{ts[:10]}.csv"
    subtype = f"{ACTIVO_OBJETIVO}#{marco}"
    decision = "BUY_YES" if lado in ("Up", "Yes") else "BUY_NO"
    prob_yes = min(0.97, py + 0.03) if decision == "BUY_YES" else max(0.03, py - 0.03)
    edge = prob_yes - py
    features = json.dumps({
        "py_entrada": round(py, 4), "lado": lado,
        "ejecutor_baja_latencia": True, "fase0_solo_observacion": True,
        "candidata10_confirmacion_cruzada": True,
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
                        ts, STRATEGY, condition_id, "", "",
                        "0.02", f"{py:.4f}", f"{prob_yes:.4f}",
                        f"{edge:.4f}", f"{edge:.4f}", f"{edge:.4f}", decision,
                        "candidata10_confirmacion_cruzada_reactivo", subtype, "1.05", features,
                    ])
            finally:
                fcntl.flock(lock_f, fcntl.LOCK_UN)
    except Exception as e:
        _log(f"aviso: no se pudo registrar predicción: {e}")


def main() -> None:
    bots = _cargar_bots()
    if not bots:
        _log(f"⚠️ sin wallets en {BOTS_PATH} -- nada que vigilar")
        return
    vistos = _vistos_cargar()

    # {wallet: deque[(ts, activo, lado)]} -- historial corto (30min) por wallet,
    # de CUALQUIER activo, para detectar confirmación cruzada al llegar BTC.
    historial_wallet: dict[str, deque] = defaultdict(deque)

    _log(f"arrancado -- {len(bots)} bot wallets, vigilando confirmación cruzada -> "
         f"{ACTIVO_OBJETIVO}#{{{','.join(sorted(MARCOS_OBJETIVO))}}}")

    # Backlog existente: marcar como visto sin procesar (mismo criterio que
    # candidata9 -- medir el pasado no aporta, solo lo que llegue de ahora en
    # adelante).
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
            eventos_nuevos = []
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
                        activo = row.get("activo", "")
                        marco = row.get("marco", "")
                        lado = row.get("outcome", "")
                        if not activo or not marco or not lado:
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
                        ts_raw = row.get("timestamp_utc", "")
                        try:
                            ts = datetime.fromisoformat(ts_raw.replace("Z", "+00:00"))
                            if ts.tzinfo is None:
                                ts = ts.replace(tzinfo=timezone.utc)
                        except Exception:
                            continue
                        eventos_nuevos.append({
                            "wallet": w, "activo": activo, "marco": marco, "lado": lado,
                            "precio": precio, "condition_id": condition_id,
                            "market_slug": market_slug, "ts": ts, "ts_raw": ts_raw,
                        })
            _vistos_guardar(vistos)

            # Procesar en orden cronológico (mismo criterio sin-lookahead que
            # el script retrospectivo: la confirmación solo puede venir de
            # trades YA vistos antes de este).
            eventos_nuevos.sort(key=lambda e: e["ts"])

            for ev in eventos_nuevos:
                w, activo, ts = ev["wallet"], ev["activo"], ev["ts"]
                hist = historial_wallet[w]

                # limpiar entradas viejas (>30min) del historial de esta wallet
                corte = ts - timedelta(seconds=VENTANA_CONFIRM_S)
                while hist and hist[0][0] < corte:
                    hist.popleft()

                if activo == ACTIVO_OBJETIVO and ev["marco"] in MARCOS_OBJETIVO:
                    confirm_activo = None
                    confirm_lag_s = None
                    for (ts_j, activo_j, lado_j) in hist:
                        if activo_j != activo and lado_j == ev["lado"]:
                            confirm_activo = activo_j
                            confirm_lag_s = round((ts - ts_j).total_seconds(), 1)
                            break
                    if confirm_activo is not None:
                        _procesar_trigger(ev, confirm_activo, confirm_lag_s)

                # registrar este evento en el historial DESPUÉS de evaluarlo
                # (un trade no puede confirmarse a sí mismo)
                hist.append((ts, activo, ev["lado"]))

        except Exception as e:
            _log(f"error en ciclo: {e} -- reintenta en {POLL_S}s")
        time.sleep(POLL_S)


def _procesar_trigger(ev: dict, confirm_activo: str, confirm_lag_s: float) -> None:
    condition_id = ev["condition_id"]
    market_slug = ev["market_slug"]
    lado = ev["lado"]
    marco = ev["marco"]

    fill_det = _fillability_mirror(market_slug, lado, str(ev["precio"]))
    ask_det = fill_det.get("mejor_ask")
    ratio_det = fill_det.get("ratio_vs_stake") if fill_det.get("ok") else None

    time.sleep(SEGUNDA_CONSULTA_ESPERA_S)
    fill_dec = _fillability_mirror(market_slug, lado, str(ev["precio"]), fill_det.get("token_id"))
    ask_dec = fill_dec.get("mejor_ask")
    ratio_dec = fill_dec.get("ratio_vs_stake") if fill_dec.get("ok") else None

    degradacion = None
    if ask_det is not None and ask_dec is not None and ask_det > 0:
        degradacion = round((ask_dec - ask_det) / ask_det * 100, 2)

    sigue_fillable = bool(ratio_dec is not None and ratio_dec >= RATIO_MIN)
    py_ref = ask_dec if ask_dec is not None else (ask_det if ask_det is not None else ev["precio"])

    registrada = False
    if sigue_fillable:
        _registrar_prediccion(condition_id, marco, lado, py_ref)
        registrada = True

    _log(f"[{condition_id}] TRIGGER confirmado por {confirm_activo} (lag={confirm_lag_s}s) "
         f"marco={marco} lado={lado} ask_det={ask_det} ratio_det={ratio_det} -> "
         f"ask_dec={ask_dec} ratio_dec={ratio_dec} degradacion={degradacion}% registrada={registrada}")

    _escribir_auditoria({
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "trade_timestamp": ev["ts_raw"], "wallet": ev["wallet"], "condition_id": condition_id,
        "market_slug": market_slug, "marco": marco, "lado": lado,
        "confirm_activo": confirm_activo, "confirm_lag_s": confirm_lag_s,
        "precio_trigger": ev["precio"], "ratio_deteccion": ratio_det, "ask_deteccion": ask_det,
        "ratio_decision": ratio_dec, "ask_decision": ask_dec, "degradacion_ask_pct": degradacion,
        "sigue_fillable_en_decision": int(sigue_fillable), "registrada_prediccion": int(registrada),
    })


if __name__ == "__main__":
    main()
