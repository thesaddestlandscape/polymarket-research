#!/usr/bin/env python3
"""
weeklyprice_fade_depth_fase0.py — FASE 0 (SOLO OBSERVACIÓN), 13-Ago,
petición Javi "primero el 1" (generalizar el fade de GBM_LATE_15M_ESPACIO_
ATR#XRP#15min a otras estrategias arquetipo A).

Segundo caso de prueba del mecanismo fade, tras GBM_LATE_15M (ver
gbmlate_fade_depth_fase0.py). WEEKLY_PRICE#SOL#BUY_NO es el caso más
extremo de arquetipo A documentado en el proyecto: shadow n=277 hit=92.1%
pnl=+1.064€/trade (results.csv, 13-Ago), pero el libro del lado propio
(BUY_NO) casi NUNCA tiene profundidad real — verificado hoy cruzando
libro_snapshots.csv colapsado por market_id: solo 6/240 (2.5%) alcanzan
ratio_vs_stake>=5x, frente a GBM_LATE_15M donde ese mismo umbral se
alcanza ~21% de las veces. BTC/ETH#WEEKLY_PRICE#BUY_NO tienen fill-ability
mucho mejor (91%/38%) pero edge mucho más débil (pnl +0.009€/+0.271€ vs
+1.064€ de SOL) — mismo patrón inverso profundidad↔edge de toda la
familia GBM_LATE, ahora confirmado también aquí.

Diferencia de diseño respecto a gbmlate_fade_depth_fase0.py: ese script
dispara SOLO cuando el lado propio YA es fillable (ratio_vs_stake>=5,
~21% de las señales GBM_LATE) porque esa es la población "mala" a medir.
Para WEEKLY_PRICE#SOL esa condición casi nunca se cumple (2.5%) — filtrar
igual dejaría el observador casi sin eventos. Aquí se registra el lado
CONTRARIO en TODA señal candidata (motivo=candidato_evaluacion), sin
filtrar por ratio propio, para poder comparar directamente:
  (a) los pocos casos con lado propio fillable (arquetipo A: ¿pierden
      igual que en GBM_LATE?)
  (b) el resto (lado propio vacío, la mayoría): ¿tiene el lado CONTRARIO
      profundidad ejecutable con la frecuencia suficiente para plantear
      un fade sistemático, o está igual de vacío (mismo callejón sin
      salida que Box Builder/Spread-Harvest, ambos refutados)?

Los mercados WEEKLY_PRICE duran ~1 semana (no 15min) — la dinámica de
vaciado/recuperación del libro es de otra escala temporal, así que (a
diferencia de gbmlate_fade_depth_fase0.py) NO hace falta un hilo de
polling de 30s por evento: una sola consulta por señal basta, y como la
misma estrategia se reevalúa cada ciclo del fast loop (~20-100s) sobre el
mismo market_id mientras el mercado semanal siga abierto, el propio
histórico de libro_snapshots.csv ya aporta repetición temporal gratis.

Mecanismo (mismo patrón exacto que gbmlate_fade_depth_fase0.py/
p22_cola_posicion_fase0.py/favorito_confirmado_senal_contraria_fase0.py —
reusa lt._consultar_profundidad_libro, solo lectura, nunca ordena):
  1. Vigila data/live/libro_snapshots.csv por filas NUEVAS de
     strategy=="WEEKLY_PRICE" con motivo=="candidato_evaluacion".
  2. Para cada evento nuevo, UNA consulta del libro público del lado
     CONTRARIO (el token que NO recomienda la estrategia).
  3. Persiste en data/shadow/weeklyprice_fade_depth_fase0.csv: identidad
     de la señal, ratio/precio del lado original (ya viene en la fila de
     libro_snapshots.csv, no hace falta reconsultarlo), y ratio/ask del
     lado contrario en ese instante.

NO coloca, cancela ni modifica ninguna orden real, no llama a ninguna
función de ejecución de live_trade.py, no toca pares_permitidos_live ni
candidatos_evaluacion_live — puramente observacional, mismo criterio de
riesgo que el resto de la familia *_fase0.py.

Se fusiona en observadores_fase0.py (screen "observadores") como los
demás — NUNCA lanzar una screen suelta para este script.
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
OUT = DIR_SHADOW / "weeklyprice_fade_depth_fase0.csv"

CICLO_TAIL_S = 3.0
MAX_HILOS_CONCURRENTES = 8

COLUMNS = [
    "evento_timestamp_utc", "market_id", "subtype", "direction",
    "precio_original", "stake_eur", "ratio_original",
    "precio_contrario", "ratio_contrario", "ask_contrario", "profundidad_contrario_eur",
]


def _es_evento_relevante(fila: dict) -> bool:
    return (fila.get("motivo") == "candidato_evaluacion"
            and fila.get("strategy") == "WEEKLY_PRICE")


_lock_out = threading.Lock()
_vistos = set()
_sem = threading.Semaphore(MAX_HILOS_CONCURRENTES)
_libro_pos = 0
_libro_header: list[str] | None = None


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _iniciar_tail_libro() -> None:
    global _libro_pos, _libro_header
    if not LIBRO_SNAPSHOTS.exists():
        return
    with open(LIBRO_SNAPSHOTS, encoding="utf-8") as f:
        primera = f.readline()
        if primera:
            _libro_header = next(csv.reader([primera]))
    _libro_pos = LIBRO_SNAPSHOTS.stat().st_size


def _leer_filas_nuevas() -> list:
    global _libro_pos, _libro_header
    if not LIBRO_SNAPSHOTS.exists() or _libro_header is None:
        return []
    tam = LIBRO_SNAPSHOTS.stat().st_size
    if tam < _libro_pos:
        _libro_pos = 0
        _libro_header = None
        return []
    if tam == _libro_pos:
        return []
    with open(LIBRO_SNAPSHOTS, encoding="utf-8") as f:
        f.seek(_libro_pos)
        nuevas = f.readlines()
        _libro_pos = f.tell()
    if not nuevas:
        return []
    return list(csv.DictReader(nuevas, fieldnames=_libro_header))


def _cargar_vistos_previos() -> set:
    if not OUT.exists():
        return set()
    with open(OUT, encoding="utf-8") as f:
        return {(r["evento_timestamp_utc"], r["market_id"]) for r in csv.DictReader(f)}


def _escribir_fila(fila: dict) -> None:
    with _lock_out:
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLUMNS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)


def _procesar_evento(fila_ev: dict) -> None:
    """Una sola consulta de solo lectura al libro del lado CONTRARIO."""
    try:
        market_id = fila_ev["market_id"]
        subtype = fila_ev["subtype"]
        direction = fila_ev["direction"]
        precio_original = float(fila_ev["precio_plan"])
        stake_eur = float(fila_ev["stake_eur"])
        ratio_original = fila_ev.get("ratio_vs_stake") or ""

        yes_token, no_token, _cid = lt._get_token_ids(market_id)
        token_contrario = no_token if direction == "BUY_YES" else yes_token
        precio_contrario = round(max(0.01, min(0.99, 1.0 - precio_original)), 6)

        try:
            prof = lt._consultar_profundidad_libro(None, token_contrario, precio_contrario, stake_eur)
        except Exception:
            prof = {"ok": False}

        ratio_c = prof.get("ratio_vs_stake") if prof.get("ok") else ""
        ask_c = prof.get("mejor_ask") if prof.get("ok") else ""
        prof_c = prof.get("profundidad_eur") if prof.get("ok") else ""

        _escribir_fila({
            "evento_timestamp_utc": fila_ev["timestamp_utc"],
            "market_id": market_id, "subtype": subtype, "direction": direction,
            "precio_original": precio_original, "stake_eur": stake_eur,
            "ratio_original": ratio_original,
            "precio_contrario": precio_contrario,
            "ratio_contrario": ratio_c, "ask_contrario": ask_c,
            "profundidad_contrario_eur": prof_c,
        })
        _log(f"[{market_id}] WEEKLY_PRICE#{subtype} {direction} ratio_original={ratio_original} "
             f"-- ratio_contrario={ratio_c}")
    except Exception as e:
        _log(f"error procesando evento {fila_ev.get('market_id')}: {e}")
    finally:
        _sem.release()


def _marcar_backlog_como_visto() -> set:
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
    _iniciar_tail_libro()
    _log(f"arrancado -- {len(ya_procesados)} eventos ya en {OUT.name}, "
         f"{len(backlog)} en el backlog histórico marcados como vistos (no se procesan) -- "
         f"solo se sigue lo que ocurra desde ahora (tail incremental desde byte {_libro_pos})")

    while True:
        try:
            for fila in _leer_filas_nuevas():
                if not _es_evento_relevante(fila):
                    continue
                clave = (fila["timestamp_utc"], fila["market_id"])
                if clave in _vistos:
                    continue
                _vistos.add(clave)
                if _sem.acquire(blocking=False):
                    threading.Thread(target=_procesar_evento, args=(fila,), daemon=True).start()
                else:
                    _log(f"[{fila['market_id']}] descartado -- {MAX_HILOS_CONCURRENTES} hilos ya en curso")
        except Exception as e:
            _log(f"error en ciclo principal: {e}")
        time.sleep(CICLO_TAIL_S)


if __name__ == "__main__":
    main()
