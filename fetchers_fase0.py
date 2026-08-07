#!/usr/bin/env python3
"""
fetchers_fase0.py — Consolida 4 fetchers de datos externos (ninguno ejecuta
dinero real, ninguno decide nada) en UN SOLO proceso, cada uno en su propio
hilo daemon ejecutando su main() EXISTENTE SIN MODIFICAR NINGUNA LÍNEA de
los 4 ficheros originales. Mismo patrón exacto que observadores_fase0.py
(05-Ago, 10 observadores fusionados) — ver ese fichero para el razonamiento
completo de por qué fusionar procesos es la mitigación real de CPU
sobresuscrita cuando no hay presupuesto para subir el VPS.

Origen (07-Ago, petición explícita Javi: "consolidación de más procesos"
tras el barrido de salud de la sesión, load5=8.46-9.61 en 2 cores, ratio
4.2-4.8x sobre el umbral 3.0x). Estos 4 (chainlink, liqs, libroambos,
polyactivity) son la siguiente familia más segura de fusionar: puro fetch
de datos externos (websocket o polling HTTP), ninguno lee `pares_permitidos_live`
ni llama nada de live_trade.py que ordene, ninguno tiene DRY_RUN=False.

Diferencia con observadores_fase0.py: 3 de los 4 (chainlink, liqs,
polyactivity) tienen `async def main()` sobre websockets — se lanzan en su
hilo vía `asyncio.run(mod.main())`, que crea un event loop propio y aislado
por hilo (patrón estándar, cada asyncio loop vive confinado a su hilo). El
4º (libroambos) es `def main()` síncrono con su propio time.sleep — se
lanza igual que los 10 de observadores_fase0.py.

Verificado ANTES de fusionar (AST, no solo grep): los 4 módulos NO ejecutan
ningún trabajo real a nivel de módulo, solo definiciones y asignaciones de
constantes — import estático seguro.

NO cambia ninguna fuente, fichero de salida, ni columna de ninguno de los
4 — solo el proceso que los ejecuta. Verificar tras desplegar que los 4
ficheros de salida (data/prices/chainlink_*.csv, data/shadow/bybit_liquidations_state.json,
data/shadow/libro_ambos_lados_*.csv, data/shadow/polymarket_activity_*.csv)
siguen creciendo con la misma cadencia que antes de la fusión.

pipeline_watchdog.py::check_chainlink_fresh / check_polyactivity_fresh
apuntan ahora a la screen "fetchers" (antes "chainlink"/"polyactivity") —
un hilo colgado fuerza el reinicio del proceso entero, mismo trade-off ya
aceptado en observadores_fase0.py (pierde granularidad de reinicio
individual, gana menos procesos persistentes).

Corre en screen propia:
  screen -dmS fetchers bash -c "cd /root/polymarket-research && nice -n 10 .venv/bin/python fetchers_fase0.py >> logs/fetchers_fase0.log 2>&1"
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

# Imports ESTÁTICOS a propósito (ver observadores_fase0.py): verify_deploy.py
# detecta STALE siguiendo el cierre transitivo de imports por regex sobre el
# texto fuente -- con import estático, tocar cualquiera de los 4 SÍ marca
# esta screen como STALE hasta reiniciarla, igual que antes de la fusión.
import fetch_chainlink_prices
import fetch_bybit_liquidations
import fetch_libro_ambos_lados
import fetch_polymarket_activity_ws

# (modulo, fichero_log_propio -- EXACTO el que ya usaba pipeline_watchdog.SCREEN_RESTART,
#  nombre_funcion_log_a_reemplazar, es_async)
FETCHERS = [
    (fetch_chainlink_prices, "chainlink.log", "_log", True),
    (fetch_bybit_liquidations, "bybit_liquidations.log", "_log", True),
    (fetch_libro_ambos_lados, "libro_ambos_lados.log", "_log", False),
    (fetch_polymarket_activity_ws, "polymarket_activity.log", "_log", True),
]


def _logger_dedicado(nombre_log: str):
    """Escribe directamente al fichero .log propio de ese fetcher, igual
    que antes cuando la screen redirigía su stdout ahí."""
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
                pass  # nunca tumbar al fetcher por un fallo de logging
    return _fn


def _correr_fetcher(mod, nombre_log: str, nombre_fn_log: str, es_async: bool) -> None:
    """Bucle de supervisión: inyecta el logger dedicado y corre main() (o
    asyncio.run(main()) si es async). Si retorna o lanza (no debería --
    los 4 main() son bucles infinitos con su propio try/except interno de
    reconexión), reintenta a los 10s en vez de dejar el fetcher muerto en
    silencio."""
    nombre_modulo = mod.__name__
    setattr(mod, nombre_fn_log, _logger_dedicado(nombre_log))
    while True:
        try:
            print(f"[fetchers_fase0] arrancando {nombre_modulo} "
                  f"(log dedicado en logs/{nombre_log})", flush=True)
            if es_async:
                asyncio.run(mod.main())
            else:
                mod.main()
            print(f"[fetchers_fase0] ⚠️ {nombre_modulo}.main() retornó "
                  f"(inesperado, sus main() son bucles infinitos) -- reintenta en 10s", flush=True)
        except Exception as e:
            print(f"[fetchers_fase0] 🚨 {nombre_modulo} murió: "
                  f"{type(e).__name__}: {e} -- reintenta en 10s", flush=True)
        time.sleep(10)


def main() -> int:
    LOGS.mkdir(parents=True, exist_ok=True)
    print(f"[fetchers_fase0] arrancando {len(FETCHERS)} fetchers "
          f"en hilos separados (1 proceso, antes {len(FETCHERS)} procesos)", flush=True)
    hilos = {}
    for mod, nombre_log, nombre_fn_log, es_async in FETCHERS:
        t = threading.Thread(
            target=_correr_fetcher, args=(mod, nombre_log, nombre_fn_log, es_async),
            daemon=True, name=mod.__name__,
        )
        t.start()
        hilos[mod.__name__] = t
        time.sleep(1.0)  # arranque escalonado -- evita golpear las APIs externas a la vez

    print(f"[fetchers_fase0] {len(hilos)} hilos arrancados, supervisando cada 60s", flush=True)
    while True:
        time.sleep(60)
        muertos = [n for n, h in hilos.items() if not h.is_alive()]
        if muertos:
            print(f"[fetchers_fase0] ⚠️ hilos no vivos (el supervisor interno de "
                  f"_correr_fetcher ya debería haberlos reintentado): {muertos}", flush=True)


if __name__ == "__main__":
    sys.exit(main() or 0)
