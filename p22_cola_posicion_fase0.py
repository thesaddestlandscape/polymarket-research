#!/usr/bin/env python3
"""
p22_cola_posicion_fase0.py — FASE 0 de P22 (Bot de gestión activa de cola
de posición / maker inteligente, CLAUDE.md P22). Petición explícita Javi,
29-Jul: "ataca con P22 a ver".

Objetivo: reunir el dato que falta para diseñar P22 de verdad. El piloto
maker YA REFUTADO (ver idea_maker_veto_profundidad_ya_probado_refutado_28jul)
probó "coloca una orden a precio fijo y espera" (pasivo) — perdió porque
llenar tarde = llenar cuando el mercado ya se movió en tu contra (selección
adversa). P22 es la hipótesis DISTINTA, nunca probada: vigilar el libro en
tiempo real tras un veto por profundidad y ver si la ventana en la que
mejora la profundidad llega ANTES de que el precio se mueva mal, o si
mejora y empeora a la vez (mismo problema que el piloto estático, solo que
más lento).

Mecanismo (FASE 0, SOLO OBSERVACIÓN — no coloca, cancela ni modifica
ninguna orden real, no llama a ninguna función de ejecución de
live_trade.py):
  1. Vigila data/live/libro_snapshots.csv por nuevas filas motivo=
     veto_profundidad (señal real que YA pasó todos los gates y solo
     murió por profundidad de libro — la población exacta que P22
     querría rescatar).
  2. Para cada veto nuevo, sigue consultando el libro público
     (_consultar_profundidad_libro, misma función de solo lectura que ya
     usa live_trade.py/ballenas_executor_btc15m.py) cada POLL_INTERVAL_S
     durante VENTANA_S segundos, registrando cómo evoluciona
     ratio_vs_stake y mejor_ask.
  3. Persiste en data/shadow/p22_cola_posicion_fase0.csv — market_id,
     tupla, precio_plan, y una serie temporal de (t_offset_s, ratio,
     mejor_ask). Un análisis posterior (cuando el mercado resuelva) cruza
     esto con outcome_real para responder la pregunta real: "si hubiéramos
     esperado pacientemente, ¿nos habrían llenado a tiempo de ganar, o
     tarde y ya perdiendo?"

Corre en screen propia:
  screen -dmS p22fase0 bash -c "cd /root/polymarket-research && .venv/bin/python p22_cola_posicion_fase0.py >> logs/p22_cola_posicion_fase0.log 2>&1"
"""
import csv
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
LIBRO_SNAPSHOTS = REPO / "data" / "live" / "libro_snapshots.csv"
OUT = DIR_SHADOW / "p22_cola_posicion_fase0.csv"

POLL_INTERVAL_S = 5.0
VENTANA_S = 60.0
RATIO_OBJETIVO = 5.0  # mismo umbral que veto_profundidad/analisis_fills.py
CICLO_TAIL_S = 3.0
MAX_HILOS_CONCURRENTES = 8

COLUMNS = [
    "veto_timestamp_utc", "market_id", "strategy", "subtype", "direction",
    "precio_plan", "stake_eur", "ratio_inicial",
    "muestras_json",  # [[t_offset_s, ratio, mejor_ask], ...]
    "mejora_detectada", "t_mejora_s", "ratio_max",
]

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
    """Hilo por evento de veto: consulta el libro cada POLL_INTERVAL_S
    durante VENTANA_S. Solo lectura -- ninguna llamada de ejecución."""
    try:
        market_id = fila_veto["market_id"]
        strategy = fila_veto["strategy"]
        subtype = fila_veto["subtype"]
        direction = fila_veto["direction"]
        precio_plan = float(fila_veto["precio_plan"])
        stake_eur = float(fila_veto["stake_eur"])
        ratio_inicial = float(fila_veto.get("ratio_vs_stake") or 0.0)

        yes_token, no_token, _cid = lt._get_token_ids(market_id)
        token_id = yes_token if direction == "BUY_YES" else no_token

        muestras = []
        t0 = time.monotonic()
        mejora_detectada = False
        t_mejora_s = None
        ratio_max = ratio_inicial

        while time.monotonic() - t0 < VENTANA_S:
            time.sleep(POLL_INTERVAL_S)
            t_offset = round(time.monotonic() - t0, 1)
            try:
                prof = lt._consultar_profundidad_libro(None, token_id, precio_plan, stake_eur)
            except Exception as e:
                muestras.append([t_offset, None, None])
                continue
            if not prof.get("ok"):
                muestras.append([t_offset, None, None])
                continue
            ratio = prof.get("ratio_vs_stake")
            mejor_ask = prof.get("mejor_ask")
            muestras.append([t_offset, ratio, mejor_ask])
            if ratio is not None:
                ratio_max = max(ratio_max, ratio)
                if ratio >= RATIO_OBJETIVO and not mejora_detectada:
                    mejora_detectada = True
                    t_mejora_s = t_offset

        import json as _json
        _escribir_fila({
            "veto_timestamp_utc": fila_veto["timestamp_utc"],
            "market_id": market_id, "strategy": strategy, "subtype": subtype,
            "direction": direction, "precio_plan": precio_plan, "stake_eur": stake_eur,
            "ratio_inicial": ratio_inicial,
            "muestras_json": _json.dumps(muestras, separators=(",", ":")),
            "mejora_detectada": int(mejora_detectada),
            "t_mejora_s": t_mejora_s if t_mejora_s is not None else "",
            "ratio_max": round(ratio_max, 3),
        })
        _log(f"[{market_id}] veto seguido {VENTANA_S:.0f}s -- mejora={mejora_detectada} "
             f"t_mejora={t_mejora_s} ratio_max={ratio_max:.2f}")
    except Exception as e:
        _log(f"error siguiendo veto {fila_veto.get('market_id')}: {e}")
    finally:
        _sem.release()


def _marcar_backlog_como_visto() -> set:
    """Al arrancar, libro_snapshots.csv ya trae semanas de histórico de
    veto_profundidad -- sin esto, el primer ciclo trataría TODO el
    backlog como "nuevo" a la vez, saturando el semáforo de hilos con
    eventos ya viejos (bug real encontrado en el smoke test antes de
    desplegar). Solo se vigilan vetos que ocurran DESDE que arranca este
    proceso hacia adelante."""
    vistos = set()
    if LIBRO_SNAPSHOTS.exists():
        with open(LIBRO_SNAPSHOTS, encoding="utf-8") as f:
            for fila in csv.DictReader(f):
                if fila.get("motivo") == "veto_profundidad":
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

    ultimo_tamano = 0
    while True:
        try:
            if LIBRO_SNAPSHOTS.exists():
                with open(LIBRO_SNAPSHOTS, encoding="utf-8") as f:
                    filas = list(csv.DictReader(f))
                for fila in filas:
                    if fila.get("motivo") != "veto_profundidad":
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
