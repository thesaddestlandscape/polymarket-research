#!/usr/bin/env python3
"""
migrar_trades_columnas_slippage_29jul.py — Stage 0 (P29 ítem 6, "logging
estructurado de slippage"): añade las columnas `signal_ask`/`slip_real`
a `data/live/trades.csv` para las filas ya existentes, escritas antes de
que `live_trade.py`/los ejecutores de ballenas empezaran a rellenarlas
directamente.

Backfill: para filas que ya tenían `slip_real=+X.XXXX` embebido como
texto en `notas` (formato usado desde el 03-Jul), se extrae con regex y
se copia a la columna nueva. El resto (filas sin ese patrón en notas, ej.
trades con error o de antes del 03-Jul) queda en blanco -- no se inventa
ningún valor.

Se ejecuta UNA VEZ a mano (no es un cron), bajo el mismo flock que usa
_registrar_trade() en live_trade.py, para no pisarse con un append
concurrente del fast loop o de los ejecutores de ballenas mientras migra.

Solo lectura+reescritura de trades.csv. No toca ninguna decisión ni
ningún otro fichero.
"""
import csv
import fcntl
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
TRADES = REPO / "data/live/trades.csv"
TRADES_LOCK = REPO / "data/live/.trades_lock"  # MISMO lock que live_trade.py::TRADES_LOCK_PATH

SLIP_RE = re.compile(r"slip_real=([+-]?\d+\.\d+)")


def main() -> int:
    if not TRADES.exists():
        print("Sin trades.csv -- nada que migrar.")
        return 0

    lock_f = open(TRADES_LOCK, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        try:
            with open(TRADES, newline="", encoding="utf-8") as f:
                filas = list(csv.DictReader(f))

            if filas and "signal_ask" in filas[0] and "slip_real" in filas[0]:
                print("Ya migrado (signal_ask/slip_real ya en el header) -- no-op.")
                return 0

            n_backfilled = 0
            for r in filas:
                if "signal_ask" not in r:
                    r["signal_ask"] = ""
                if "slip_real" not in r:
                    notas = r.get("notas", "") or ""
                    m = SLIP_RE.search(notas)
                    if m:
                        r["slip_real"] = m.group(1)
                        n_backfilled += 1
                    else:
                        r["slip_real"] = ""

            campos = list(filas[0].keys()) if filas else []
            for col in ("signal_ask", "slip_real"):
                if col not in campos:
                    campos.append(col)

            with open(TRADES, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=campos)
                w.writeheader()
                w.writerows(filas)

            print(f"Migrado: {len(filas)} filas, {n_backfilled} con slip_real recuperado de notas.")
        finally:
            fcntl.flock(lock_f, fcntl.LOCK_UN)
    finally:
        lock_f.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
