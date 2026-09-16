#!/usr/bin/env python3
"""
sports_smart_exit_logger_persistente.py — wrapper de bucle persistente
para sports_smart_exit_logger.py, mismo patrón EXACTO que
smart_exit_logger_persistente.py (cripto, 12-Ago): evita arrancar un
intérprete Python nuevo cada ciclo, se fusiona como hilo dentro de
sports_fase0_consolidado.py.

READ-ONLY sobre dinero (igual que el original): sports_smart_exit_
logger.main() solo lee trades.csv y consulta precios públicos, nunca
escribe trades.csv ni envía órdenes.
"""
import time
from datetime import datetime, timezone

import sports_smart_exit_logger

INTERVALO_S = 20.0


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def main() -> None:
    _log("arrancado -- sports_smart_exit_logger.main() cada 20s en bucle persistente")
    while True:
        t0 = time.monotonic()
        try:
            sports_smart_exit_logger.main()
        except Exception as e:
            _log(f"error en sports_smart_exit_logger.main(): {e}")
        transcurrido = time.monotonic() - t0
        time.sleep(max(0.0, INTERVALO_S - transcurrido))


if __name__ == "__main__":
    main()
