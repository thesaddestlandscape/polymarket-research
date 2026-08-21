#!/usr/bin/env python3
"""
nested_arb_loop.py — envoltorio de proceso persistente para
nested_arb_scanner.py, mismo espíritu de consolidación que
observadores_fase0.py/ejecutores_dryrun_fase0.py/vigias_frecuentes_fase0.py
pero SIN mezclarlo con esos schedulers (motivo documentado en el propio
vigias_frecuentes_fase0.py: acoplar esta cadencia de 1min a un scheduler
secuencial con hermanos más lentos arriesga retrasar justo la tarea más
sensible a la cadencia -- se le da su propio proceso, solo para eliminar
el coste de arrancar un intérprete Python nuevo cada minuto).

Origen (20-Ago, Javi: "consolida procesos", incidente OOM real de esta
sesión -- ver logs/vigia_pipeline_latencia.log 21:03 Madrid, y dmesg con
kills reales de git/python por falta de memoria/CPU en 2 cores): el cron
`* * * * *` de nested_arb_scanner.py llevaba horas sin lograr disparar
cada minuto de verdad bajo la carga del incidente (huecos de 13-37min en
logs/nested_arb.log pese al cron por minuto) -- síntoma del mismo cuello
de botella, no un bug propio del script. Convertirlo en loop persistente
no arregla la carga por sí solo, pero quita ~1440 arranques/día de
intérprete (import requests/csv/json + parseo de bytecode) que competían
con el resto.

nested_arb_scanner.main() es de un solo disparo, sale al instante si
está fuera de fase activa (ver su propio docstring) -- se llama en un
bucle con tick=60s, igual de frecuente que el cron que sustituye. Sin
tocar ninguna línea del fichero original (mismo criterio AST-verificado
que las fusiones anteriores: solo defs/imports/sys.path.insert a nivel
de módulo).

Corre en screen propia (no dentro de otro scheduler -- ver motivo arriba):
  screen -dmS nestedarb bash -c "cd /root/polymarket-research && nice -n 10 .venv/bin/python nested_arb_loop.py >> logs/nested_arb_loop.log 2>&1"
"""
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import nested_arb_scanner as _nas

TICK_S = 60.0


def main() -> int:
    print(f"[nested_arb_loop] arrancando, tick={TICK_S:.0f}s "
          f"(sustituye cron '* * * * *' + flock)", flush=True)
    while True:
        t0 = time.time()
        try:
            _nas.main()
        except Exception as e:
            print(f"[nested_arb_loop] 🚨 nested_arb_scanner.main() murió: "
                  f"{type(e).__name__}: {e}", flush=True)
        dt = time.time() - t0
        time.sleep(max(0.0, TICK_S - dt))
    return 0


if __name__ == "__main__":
    sys.exit(main())
