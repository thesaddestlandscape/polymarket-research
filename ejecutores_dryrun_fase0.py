#!/usr/bin/env python3
"""
ejecutores_dryrun_fase0.py — Consolida 7 ejecutores DRY_RUN (ninguno ejecuta
dinero real, todos con DRY_RUN=True verificado) en UN SOLO proceso, cada uno
en su propio hilo daemon ejecutando su main() EXISTENTE SIN MODIFICAR
NINGUNA LÍNEA de los 7 ficheros originales. Mismo patrón exacto que
observadores_fase0.py (05-Ago, consolidación de 10 loggers) -- ver ese
fichero para el razonamiento completo del diseño, no se repite aquí.

Origen (06-Ago, ventana 11:30 planificada 05-Ago noche -- ver
project_cpu_consolidacion_pendiente_05ago en memoria): load5 sostenido
6-8 en 2 cores tras la primera consolidación del 05-Ago. Estos 7 procesos
son "ejecutores de baja latencia" (deciden señales, simulan fills) pero
TODOS con DRY_RUN=True verificado -- no son la familia de loggers puros de
observadores_fase0.py, pero comparten la misma propiedad de seguridad
(cero camino a dinero real) que justifica fusionarlos igual.

NUNCA fusionar aquí los ejecutores con DRY_RUN=False (dinero real):
favorito_confirmado_btc60min_buyno_executor.py (screen favbtc60mno),
favorito_altaconviccion_executor_15min.py (screen favaltaconv),
ballenas_executor_btc15m.py (screen ballenas_fast),
ballenas_executor_5min.py (screen ballenas_5m) -- estos siguen cada uno en
su propia screen, con su propia prioridad de scheduling, sin nice -n 10.

Diferencia con observadores_fase0.py: wallet_mirror_sniper.py tiene
`async def main()` (asyncio, websocket propio) en vez de `def main()`
síncrono -- se lanza con `asyncio.run(mod.main())` dentro de su propio
hilo, cada hilo con su propio event loop aislado (seguro, no comparte
loop con nadie).

Verificado ANTES de fusionar (mismo rigor AST que la fusión anterior):
los 7 NO ejecutan trabajo real a nivel de módulo -- solo definiciones,
`sys.path.insert` (idempotente) y una anotación de tipo sin llamada.

NO cambia ninguna lógica de decisión, gate, fichero de salida, ni columna
de ninguno de los 7 -- solo el proceso que los ejecuta. Verificar tras
desplegar que los 7 logs (logs/<nombre>.log) siguen escribiendo con la
misma cadencia que antes de la fusión.

Corre en screen propia:
  screen -dmS ejecdryrun bash -c "cd /root/polymarket-research && nice -n 10 .venv/bin/python ejecutores_dryrun_fase0.py >> logs/ejecutores_dryrun_fase0.log 2>&1"
"""
import asyncio
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
LOGS = REPO / "logs"

# Imports ESTÁTICOS a propósito (ver observadores_fase0.py) -- así
# verify_deploy.py sigue detectando STALE si se toca cualquiera de los 7.
import favorito_confirmado_15min_executor
import favorito_confirmado_60min_executor
import ballenas_executor_15min
import gbm_late_15min_executor
import updown_gbm_15min_tardio_btc_executor
import wallet_mirror_executor_dryrun
import wallet_mirror_sniper

# Verificación de seguridad al import -- si algún día alguien cambia
# DRY_RUN=False en disco sin retirarlo de esta lista, el proceso se niega
# a arrancar en vez de fusionar por error algo que mueve dinero real.
for _mod in (favorito_confirmado_15min_executor, favorito_confirmado_60min_executor,
             ballenas_executor_15min, gbm_late_15min_executor,
             updown_gbm_15min_tardio_btc_executor, wallet_mirror_executor_dryrun):
    if getattr(_mod, "DRY_RUN", None) is not True:
        raise RuntimeError(
            f"🚨 {_mod.__name__} tiene DRY_RUN={getattr(_mod, 'DRY_RUN', None)!r} -- "
            f"este proceso consolidado SOLO puede correr módulos DRY_RUN=True. "
            f"Sácalo de aquí y dale su propia screen antes de tocar dinero real.")

# (modulo, fichero_log_propio -- EXACTO el que ya usaba pipeline_watchdog.SCREEN_RESTART,
#  nombre_funcion_log_a_reemplazar, es_async)
EJECUTORES = [
    (favorito_confirmado_15min_executor, "favorito_confirmado_15min_executor.log", "log", False),
    (favorito_confirmado_60min_executor, "favorito_confirmado_60min_executor.log", "log", False),
    (ballenas_executor_15min, "ballenas_15m.log", "log", False),
    (gbm_late_15min_executor, "gbm_late_15min_executor.log", "log", False),
    (updown_gbm_15min_tardio_btc_executor, "updown_gbm_15min_tardio_btc_executor.log", "log", False),
    (wallet_mirror_executor_dryrun, "wallet_mirror_executor.log", "_log", True),
    (wallet_mirror_sniper, "wallet_mirror_sniper.log", "_log", True),
]


def _logger_dedicado(nombre_log: str):
    """Idéntico a observadores_fase0.py -- escribe al mismo .log que ya
    usaba la screen individual, ningún hábito de `tail -f` se rompe."""
    path = LOGS / nombre_log
    lock = threading.Lock()

    def _fn(msg, *extra) -> None:
        ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
        linea = f"[{ts}] {msg}"
        if extra:
            linea += " " + " ".join(str(e) for e in extra)
        with lock:
            try:
                with open(path, "a", encoding="utf-8") as f:
                    f.write(linea + "\n")
            except Exception:
                pass  # nunca tumbar al ejecutor por un fallo de logging
    return _fn


def _correr_ejecutor(mod, nombre_log: str, nombre_fn_log: str, es_async: bool) -> None:
    """Mismo bucle de supervisión que observadores_fase0.py::_correr_observador
    -- reintenta a los 10s si main() retorna o lanza (no debería, los 7
    main() son bucles infinitos con su propio try/except interno)."""
    nombre_modulo = mod.__name__
    setattr(mod, nombre_fn_log, _logger_dedicado(nombre_log))
    while True:
        try:
            print(f"[ejecutores_dryrun_fase0] arrancando {nombre_modulo} "
                  f"(log dedicado en logs/{nombre_log}, async={es_async})", flush=True)
            if es_async:
                asyncio.run(mod.main())
            else:
                mod.main()
            print(f"[ejecutores_dryrun_fase0] ⚠️ {nombre_modulo}.main() retornó "
                  f"(inesperado) -- reintenta en 10s", flush=True)
        except Exception as e:
            print(f"[ejecutores_dryrun_fase0] 🚨 {nombre_modulo} murió: "
                  f"{type(e).__name__}: {e} -- reintenta en 10s", flush=True)
        time.sleep(10)


def main() -> int:
    LOGS.mkdir(parents=True, exist_ok=True)
    print(f"[ejecutores_dryrun_fase0] arrancando {len(EJECUTORES)} ejecutores DRY_RUN "
          f"en hilos separados (1 proceso, antes {len(EJECUTORES)} procesos)", flush=True)
    hilos = {}
    for mod, nombre_log, nombre_fn_log, es_async in EJECUTORES:
        t = threading.Thread(
            target=_correr_ejecutor, args=(mod, nombre_log, nombre_fn_log, es_async),
            daemon=True, name=mod.__name__,
        )
        t.start()
        hilos[mod.__name__] = t
        time.sleep(1.0)  # arranque escalonado -- evita golpear las APIs externas a la vez

    print(f"[ejecutores_dryrun_fase0] {len(hilos)} hilos arrancados, supervisando cada 60s", flush=True)
    while True:
        time.sleep(60)
        muertos = [n for n, h in hilos.items() if not h.is_alive()]
        if muertos:
            print(f"[ejecutores_dryrun_fase0] ⚠️ hilos no vivos (el supervisor interno de "
                  f"_correr_ejecutor ya debería haberlos reintentado): {muertos}", flush=True)


if __name__ == "__main__":
    sys.exit(main() or 0)
