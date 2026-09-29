#!/usr/bin/env python3
"""desfase_twap_apertura_fase0.py -- FASE 0 (solo lectura, NUNCA orden real), 29-Sep.

Ronda 1 #2 de las 30 propuestas 28-Sep: "Desfase TWAP en la apertura --
ref = TWAP60 de apertura va detrás del spot; si el precio subió fuerte en
los 60s previos, Up parte con ventaja y el libro puede abrir ~0,50."
Paso 1 pedido: TWAP60 oficial × libro ambos lados en los primeros 5-10s de
cada ventana.

Hipótesis: la resolución oficial de los mercados Up/Down usa TWAP60
Chainlink (verificado en el proyecto, ver CLAUDE.md "auditoría TWAP" y
project_auditoria_twap_todas_estrategias_24sep) -- el TWAP de los 60s
JUSTO ANTES de abrir la ventana es un promedio que reacciona más lento que
el spot instantáneo. Si el spot ha subido con fuerza en esos 60s, el TWAP
pre-apertura queda POR DEBAJO del spot -- y como la referencia real que
se usará para resolver el PRÓXIMO tramo también parte de ahí, el "Up"
recién abierto puede tener ventaja estructural que el libro (que suele
abrir cerca de 0,50 por inercia) no refleja todavía.

Mide, para cada apertura de ventana (6 monedas x 5/15min), en los
primeros 10s:
  - TWAP60 de los 60s previos a la apertura (mismo _TAIL que ya usa
    resolution_sniper_observer.py, sin arrancar una segunda cola).
  - spot en el instante de apertura.
  - desfase_pct = (spot_apertura / twap60_pre - 1) * 100.
  - ask/bid REAL de AMBOS lados (Up y Down) en el instante de la
    consulta -- para ver si el libro ya refleja ese desfase o sigue
    anclado a 0,50.

Solo observación -- nunca coloca ninguna orden real.

Cron: N/A -- corre como hilo dentro de observadores_fase0.py (polling
propio cada 0,5s, no es un proceso de un solo ciclo).
"""
import statistics
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import live_trade as lt  # noqa: E402
from resolution_sniper_observer import _TAIL, mercado_slot, token_ids  # noqa: E402

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "desfase_twap_apertura_fase0.csv"

ASSETS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
MARCOS = {"5m": 300, "15m": 900}
VENTANA_CAPTURA_S = 10   # primeros N segundos de la ventana en los que se busca capturar
TWAP_WINDOW_S = 60
STAKE_REF = 1.05

CAMPOS = ["timestamp_utc", "activo", "marco", "market_id", "ts_start", "ts_desde_apertura_s",
          "twap60_pre", "n_ticks_twap", "spot_apertura", "desfase_pct",
          "ask_up", "profundidad_up_eur", "ask_down", "profundidad_down_eur",
          "mid_up", "error", "outcome_real", "resolved_ts"]

_SESSION = requests.Session()
_lock = threading.Lock()
_cache_mkt: dict = {}


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _guardar(fila: dict) -> None:
    with _lock:
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            import csv
            w = csv.writer(f)
            if nuevo:
                w.writerow(CAMPOS)
            w.writerow([fila.get(c, "") for c in CAMPOS])


def _twap60_pre(activo: str, ts_start: float) -> tuple[float | None, int]:
    """Media de los ticks Chainlink en [ts_start-60, ts_start], leyendo
    directamente el buffer de _TAIL (mismo patrón que _media() en
    saltos_chainlink_fase0.py, sin arrancar una cola nueva)."""
    with _TAIL._lock:
        dq = list(_TAIL._buf.get(activo, ()))
    vals = [p for t, p in dq if ts_start - TWAP_WINDOW_S <= t <= ts_start]
    if len(vals) < 5:
        return None, len(vals)
    return statistics.mean(vals), len(vals)


def _libro(token_id: str):
    book = lt._fetch_book_publico(token_id)
    if book is None:
        return None, None
    try:
        asks = sorted((float(a["price"]), float(a["size"])) for a in (book.get("asks") or []))
    except (TypeError, ValueError, KeyError):
        return None, None
    if not asks:
        return None, 0.0
    mejor = asks[0][0]
    prof = sum(p * s for p, s in asks if p <= mejor * 1.05)
    return mejor, round(prof, 2)


def _procesar_apertura(activo: str, marco_tag: str, ts_start: int) -> None:
    twap, n_ticks = _twap60_pre(activo, ts_start)
    spot = _TAIL.precio_en(activo, ts_start) or _TAIL.precio_ultimo(activo)
    desfase = ((spot / twap - 1) * 100) if (spot and twap) else None

    try:
        slug, mkt = mercado_slot(activo, marco_tag, ts_start)
    except Exception:
        mkt = None
    err = ""
    ask_up = prof_up = ask_down = prof_down = mid_up = market_id = ""
    if not mkt:
        err = "sin_mercado"
    else:
        market_id = mkt.get("id", "")
        ty, tn = token_ids(mkt)
        if not ty or not tn:
            err = "sin_token"
        else:
            ask_up, prof_up = _libro(ty)
            ask_down, prof_down = _libro(tn)
            if ask_up is not None and ask_down is not None:
                mid_up = round((ask_up + (1 - ask_down)) / 2, 4)

    fila = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
        "activo": activo, "marco": marco_tag, "market_id": market_id, "ts_start": ts_start,
        "ts_desde_apertura_s": round(time.time() - ts_start, 2),
        "twap60_pre": round(twap, 4) if twap else "", "n_ticks_twap": n_ticks,
        "spot_apertura": round(spot, 4) if spot else "",
        "desfase_pct": round(desfase, 4) if desfase is not None else "",
        "ask_up": ask_up if ask_up is not None else "", "profundidad_up_eur": prof_up if prof_up is not None else "",
        "ask_down": ask_down if ask_down is not None else "", "profundidad_down_eur": prof_down if prof_down is not None else "",
        "mid_up": mid_up, "error": err,
    }
    _guardar(fila)
    if not err:
        _log(f"[{activo}#{marco_tag}] desfase={desfase:+.3f}% (twap60={twap:.2f} spot={spot:.2f}) "
             f"ask_up={ask_up} ask_down={ask_down} mid_up={mid_up}")


class _Estado:
    __slots__ = ("ts_start", "capturado")

    def __init__(self):
        self.ts_start = None
        self.capturado = False


def main() -> None:
    _log(f"desfase_twap_apertura_fase0 arrancado (activos={ASSETS}, marcos={list(MARCOS)}, solo lectura)")
    estado: dict = {}
    while True:
        ahora = time.time()
        for activo in ASSETS:
            for tag, dur in MARCOS.items():
                ts_start = int(ahora // dur) * dur
                e = estado.setdefault((activo, tag), _Estado())
                if e.ts_start != ts_start:
                    e.ts_start = ts_start
                    e.capturado = False
                if e.capturado:
                    continue
                edad = ahora - ts_start
                if edad < 2 or edad > VENTANA_CAPTURA_S:
                    continue
                e.capturado = True
                threading.Thread(target=_procesar_apertura, args=(activo, tag, ts_start), daemon=True).start()
        time.sleep(0.5)


if __name__ == "__main__":
    # standalone: arrancar la cola de Chainlink (dentro de observadores_fase0.py
    # ya la arranca resolution_sniper_observer.py, no se arranca una segunda).
    _TAIL.arrancar()
    time.sleep(5)
    main()
