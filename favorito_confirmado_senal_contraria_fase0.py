#!/usr/bin/env python3
"""
favorito_confirmado_senal_contraria_fase0.py — FASE 0 (SOLO OBSERVACIÓN)
del hallazgo nuevo de hoy (04-Ago, petición Javi: "instrumenta el
seguimiento del lado contrario y despliégalo"): cuando la profundidad del
libro del lado ORIGINAL de una señal vetada por profundidad se recupera
de forma EXTREMA (ratio_vs_stake>=1000x) en los 60s siguientes, la
dirección original acierta muy por debajo de coinflip -- 39.5% agregado
(n=301, p_shuffle=0.0007), y 32.2% aislando FAVORITO_CONFIRMADO (n=171,
Wilson90%=[26.6%,38.3%], split-half 31.4%/32.9% muy estable). Ver
idea_p22_senal_contraria_favorito_confirmado_04ago (memoria) para el
análisis completo.

Lo que falta: `p22_cola_posicion_fase0.py` (que generó ese hallazgo) SOLO
trackea la profundidad del lado ORIGINAL vetado -- nunca la del lado
CONTRARIO, que es el que habría que comprar para explotar la señal. Este
script instrumenta AMBOS lados a la vez, reusando exactamente la misma
población y mecanismo de detección que p22_cola_posicion_fase0.py (no
duplica el hallazgo, añade la pieza de datos que falta):

  1. Vigila data/live/libro_snapshots.csv por los mismos eventos que P22
     (motivo=veto_profundidad, o candidato_evaluacion con ratio<5x) --
     misma `_es_evento_relevante` que el script original.
  2. Para cada evento nuevo, sigue el libro público de AMBOS lados (el
     token que se iba a comprar Y su opuesto) cada POLL_INTERVAL_S
     durante VENTANA_S -- dos llamadas de solo lectura a
     `lt._consultar_profundidad_libro`, mismo patrón exacto que usa
     p22_cola_posicion_fase0.py y sol5min_contrario_fase0.py.
  3. Persiste ambas series temporales en
     data/shadow/favorito_confirmado_senal_contraria_fase0.csv -- un
     análisis posterior cruza con el outcome real para responder: cuando
     el lado original se dispara a ratio>=1000x (la señal contraria), ¿el
     lado contrario tenía profundidad real en ese momento, o el precio
     barato del lado contrario esconde el mismo problema de selección
     adversa que el resto del proyecto?

NO coloca, cancela ni modifica ninguna orden real, no llama a ninguna
función de ejecución de live_trade.py -- solo lectura del libro público,
mismo criterio de riesgo que P22/sol5min_contrario/xrp15min_contrario.

Corre en screen propia:
  screen -dmS favcontraria bash -c "cd /root/polymarket-research && .venv/bin/python favorito_confirmado_senal_contraria_fase0.py >> logs/favorito_confirmado_senal_contraria_fase0.log 2>&1"
"""
import csv
import json
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
LIBRO_SNAPSHOTS = REPO / "data" / "live" / "libro_snapshots.csv"
OUT = DIR_SHADOW / "favorito_confirmado_senal_contraria_fase0.csv"

POLL_INTERVAL_S = 5.0
VENTANA_S = 60.0
RATIO_OBJETIVO = 5.0       # mismo umbral que veto_profundidad/analisis_fills.py
RATIO_EXTREMO = 1000.0     # umbral de la señal contraria (idea_p22_senal_contraria..., ratio_max>=1000x)
CICLO_TAIL_S = 3.0
MAX_HILOS_CONCURRENTES = 8

COLUMNS = [
    "veto_timestamp_utc", "market_id", "strategy", "subtype", "direction",
    "motivo_origen",  # veto_profundidad (live) o candidato_evaluacion
    "precio_plan", "stake_eur", "ratio_inicial",
    "muestras_json",  # [[t_offset_s, ratio_propio, ask_propio, ratio_contrario, ask_contrario], ...]
    "mejora_detectada", "t_mejora_s", "ratio_max",
    "senal_contraria_activada", "t_senal_contraria_s",
    "ratio_contrario_en_senal", "ask_contrario_en_senal", "ratio_contrario_max",
]


def _es_evento_relevante(fila: dict) -> bool:
    """Idéntica a p22_cola_posicion_fase0.py -- misma población exacta,
    para no introducir un sesgo de muestreo distinto al que generó el
    hallazgo original."""
    motivo = fila.get("motivo")
    if motivo == "veto_profundidad":
        return True
    if motivo == "candidato_evaluacion":
        try:
            return float(fila.get("ratio_vs_stake") or 0.0) < RATIO_OBJETIVO
        except (TypeError, ValueError):
            return False
    return False


_lock_out = threading.Lock()
_vistos = set()
_sem = threading.Semaphore(MAX_HILOS_CONCURRENTES)


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _cargar_vistos_previos() -> set:
    if not OUT.exists():
        return set()
    with open(OUT, encoding="utf-8") as f:
        return {(r["veto_timestamp_utc"], r["market_id"]) for r in csv.DictReader(f)}


def _escribir_fila(fila: dict) -> None:
    with _lock_out:
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)


def _seguir_veto(fila_veto: dict) -> None:
    """Hilo por evento de veto: consulta el libro de AMBOS lados cada
    POLL_INTERVAL_S durante VENTANA_S. Solo lectura -- ninguna llamada de
    ejecución."""
    try:
        market_id = fila_veto["market_id"]
        strategy = fila_veto["strategy"]
        subtype = fila_veto["subtype"]
        direction = fila_veto["direction"]
        precio_plan = float(fila_veto["precio_plan"])
        stake_eur = float(fila_veto["stake_eur"])
        ratio_inicial = float(fila_veto.get("ratio_vs_stake") or 0.0)

        yes_token, no_token, _cid = lt._get_token_ids(market_id)
        token_propio = yes_token if direction == "BUY_YES" else no_token
        token_contrario = no_token if direction == "BUY_YES" else yes_token
        # precio de referencia del lado contrario: perspectiva YES+NO~=1
        # (mismo criterio que precio_entrada_no en el resto del proyecto,
        # ej. favorito_confirmado_btc60min_buyno_executor.py) -- solo se usa
        # para fijar el techo de profundidad (precio*1.05), no cambia
        # ninguna decisión.
        precio_plan_contrario = round(max(0.01, min(0.99, 1.0 - precio_plan)), 6)

        muestras = []
        t0 = time.monotonic()
        mejora_detectada = False
        t_mejora_s = None
        ratio_max = ratio_inicial
        senal_contraria_activada = False
        t_senal_contraria_s = None
        ratio_contrario_en_senal = None
        ask_contrario_en_senal = None
        ratio_contrario_max = 0.0

        while time.monotonic() - t0 < VENTANA_S:
            time.sleep(POLL_INTERVAL_S)
            t_offset = round(time.monotonic() - t0, 1)

            try:
                prof_propio = lt._consultar_profundidad_libro(None, token_propio, precio_plan, stake_eur)
            except Exception:
                prof_propio = {"ok": False}
            try:
                prof_contrario = lt._consultar_profundidad_libro(
                    None, token_contrario, precio_plan_contrario, stake_eur)
            except Exception:
                prof_contrario = {"ok": False}

            ratio_p = prof_propio.get("ratio_vs_stake") if prof_propio.get("ok") else None
            ask_p = prof_propio.get("mejor_ask") if prof_propio.get("ok") else None
            ratio_c = prof_contrario.get("ratio_vs_stake") if prof_contrario.get("ok") else None
            ask_c = prof_contrario.get("mejor_ask") if prof_contrario.get("ok") else None

            muestras.append([t_offset, ratio_p, ask_p, ratio_c, ask_c])

            if ratio_p is not None:
                ratio_max = max(ratio_max, ratio_p)
                if ratio_p >= RATIO_OBJETIVO and not mejora_detectada:
                    mejora_detectada = True
                    t_mejora_s = t_offset
                if ratio_p >= RATIO_EXTREMO and not senal_contraria_activada:
                    senal_contraria_activada = True
                    t_senal_contraria_s = t_offset
                    ratio_contrario_en_senal = ratio_c
                    ask_contrario_en_senal = ask_c
            if ratio_c is not None:
                ratio_contrario_max = max(ratio_contrario_max, ratio_c)

        _escribir_fila({
            "veto_timestamp_utc": fila_veto["timestamp_utc"],
            "market_id": market_id, "strategy": strategy, "subtype": subtype,
            "direction": direction, "motivo_origen": fila_veto.get("motivo", ""),
            "precio_plan": precio_plan, "stake_eur": stake_eur,
            "ratio_inicial": ratio_inicial,
            "muestras_json": json.dumps(muestras, separators=(",", ":")),
            "mejora_detectada": int(mejora_detectada),
            "t_mejora_s": t_mejora_s if t_mejora_s is not None else "",
            "ratio_max": round(ratio_max, 3),
            "senal_contraria_activada": int(senal_contraria_activada),
            "t_senal_contraria_s": t_senal_contraria_s if t_senal_contraria_s is not None else "",
            "ratio_contrario_en_senal": ratio_contrario_en_senal if ratio_contrario_en_senal is not None else "",
            "ask_contrario_en_senal": ask_contrario_en_senal if ask_contrario_en_senal is not None else "",
            "ratio_contrario_max": round(ratio_contrario_max, 3),
        })
        _log(f"[{market_id}] {strategy} seguido {VENTANA_S:.0f}s -- ratio_max={ratio_max:.1f} "
             f"senal_contraria={senal_contraria_activada} ratio_contrario_en_senal={ratio_contrario_en_senal} "
             f"ratio_contrario_max={ratio_contrario_max:.1f}")
    except Exception as e:
        _log(f"error siguiendo veto {fila_veto.get('market_id')}: {e}")
    finally:
        _sem.release()


def _marcar_backlog_como_visto() -> set:
    """Igual que p22_cola_posicion_fase0.py -- al arrancar, no tratar
    semanas de histórico de libro_snapshots.csv como "nuevo" de golpe."""
    vistos = set()
    if LIBRO_SNAPSHOTS.exists():
        with open(LIBRO_SNAPSHOTS, encoding="utf-8") as f:
            for fila in csv.DictReader(f):
                if _es_evento_relevante(fila):
                    vistos.add((fila["timestamp_utc"], fila["market_id"]))
    return vistos


def main() -> None:
    global _vistos
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    ya_procesados = _cargar_vistos_previos()
    backlog = _marcar_backlog_como_visto()
    _vistos = ya_procesados | backlog
    _log(f"arrancado -- {len(ya_procesados)} vetos ya en {OUT.name}, "
         f"{len(backlog)} en el backlog histórico marcados como vistos (no se procesan) -- "
         f"solo se sigue lo que ocurra desde ahora")

    while True:
        try:
            if LIBRO_SNAPSHOTS.exists():
                with open(LIBRO_SNAPSHOTS, encoding="utf-8") as f:
                    filas = list(csv.DictReader(f))
                for fila in filas:
                    if not _es_evento_relevante(fila):
                        continue
                    clave = (fila["timestamp_utc"], fila["market_id"])
                    if clave in _vistos:
                        continue
                    _vistos.add(clave)
                    if _sem.acquire(blocking=False):
                        threading.Thread(target=_seguir_veto, args=(fila,), daemon=True).start()
                    else:
                        _log(f"[{fila['market_id']}] descartado -- {MAX_HILOS_CONCURRENTES} hilos ya en curso")
        except Exception as e:
            _log(f"error en ciclo principal: {e}")
        time.sleep(CICLO_TAIL_S)


if __name__ == "__main__":
    main()
