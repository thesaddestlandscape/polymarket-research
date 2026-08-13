#!/usr/bin/env python3
"""
smart_exit_logger_persistente.py — consolidación de procesos (12-Ago,
petición explícita Javi "vamos a consolidar procesos"). `smart_exit_logger.py`
se lanzaba 3 VECES POR MINUTO vía cron (offsets sleep 0/20/40s, tres
entradas de crontab separadas) para aproximar un muestreo cada 20s con
cron (que solo puede disparar 1 vez/minuto) — cada disparo es un proceso
Python nuevo desde cero (arranque intérprete + imports), 3x/min = 4320
arranques/día solo para este logger.

Este wrapper NO toca ni una línea de smart_exit_logger.py (cero riesgo
de romper su lógica, ya en producción) — solo lo invoca en bucle dentro
de UN proceso persistente, mismo cadencia real (~20s) sin el coste de
arrancar el intérprete cada vez. Se fusiona como hilo más en
observadores_fase0.py (mismo patrón que los demás *_fase0.py) en vez de
abrir una screen nueva — el objetivo es reducir procesos, no repartirlos
de otra forma.

READ-ONLY sobre dinero (igual que el original): smart_exit_logger.main()
solo lee trades.csv y consulta precios públicos, nunca escribe trades.csv
ni envía órdenes. Las 3 entradas de crontab de smart_exit_logger.py se
retiran del crontab en el mismo cambio -- si esto necesitara revertirse,
basta con volver a añadirlas (mismo comando, sin dependencias nuevas).
"""
import time
from datetime import datetime, timezone

import smart_exit_logger

INTERVALO_S = 20.0


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def main() -> None:
    _log("arrancado -- smart_exit_logger.main() cada 20s en bucle persistente "
         "(sustituye 3 disparos/min por cron)")
    while True:
        t0 = time.monotonic()
        try:
            smart_exit_logger.main()
        except Exception as e:
            _log(f"error en smart_exit_logger.main(): {e}")
        transcurrido = time.monotonic() - t0
        time.sleep(max(0.0, INTERVALO_S - transcurrido))


if __name__ == "__main__":
    main()
