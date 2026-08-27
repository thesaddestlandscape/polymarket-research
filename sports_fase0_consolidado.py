#!/usr/bin/env python3
"""
sports_fase0_consolidado.py — Consolida 2 procesos DRY_RUN puros de la
vertical sports (ninguno ejecuta dinero real, no confundir con
wallet_mirror_executor_dryrun.py de crypto que SÍ tiene DRY_RUN=False --
ese sigue en su propia screen, nunca aquí) en UN SOLO proceso, cada uno en
su propio hilo daemon, EXISTENTE SIN MODIFICAR NINGUNA LÍNEA de los 2
ficheros originales. Mismo patrón exacto que observadores_fase0.py
(05-Ago) / ejecutores_dryrun_fase0.py (06-Ago) -- ver esos ficheros para
el razonamiento completo del diseño, no se repite aquí.

Origen (20-Ago, petición explícita Javi tras el barrido diario de salud:
load5 sostenido ~8 en 2 cores, ratio~4x sobre el umbral 3x -- pendiente
desde 18-Ago, ver project_cpu_sobresuscrita_18ago en memoria). Candidatos
evaluados y descartados a propósito:
  - weather_wallet_mirror_sniper.py: corre desde /root/polymarket-weather,
    repo INDEPENDIENTE con su propio CLAUDE.md -- CLAUDE.md de este repo
    prohíbe explícitamente mezclar código/procesos entre ambos. NUNCA
    fusionar aquí.
  - wallet_mirror_executor_dryrun.py (screen walletmirror, crypto): pese
    al nombre, DRY_RUN=False desde el 11-Ago (activación real aprobada por
    Javi) -- mismo motivo por el que ejecutores_dryrun_fase0.py ya lo
    excluye explícitamente. Dinero real, su propia screen, sin nice -n 10.
  - sports_dashboard_server.py (screen dash-sports): servidor HTTP con
    bind de puerto propio -- arquitectura distinta (listener bloqueante),
    más riesgo fusionarlo sin rediseño. Se deja para una consolidación
    futura si hace falta seguir bajando carga.

Verificado ANTES de fusionar (mismo rigor AST que las fusiones previas):
los 2 NO ejecutan trabajo real a nivel de módulo -- solo definiciones,
`sys.path.insert` (idempotente), una anotación de tipo con dict vacío y
`DIR_SPORTS.mkdir(parents=True, exist_ok=True)` (idempotente).

sports_wallet_mirror_sniper.py::main() envuelve argparse (soporta
`--resolver` para un modo puntual que esta screen nunca usaba) -- aquí se
llama directo a `main_ws()` (la función async de bucle infinito real),
saltándose la capa de argparse por completo, mismo comportamiento que
tenía la screen standalone sin flags.

NO cambia ninguna lógica de decisión, gate, fichero de salida, ni columna
de ninguno de los 2 -- solo el proceso que los ejecuta. Verificar tras
desplegar que logs/sports_wallet_mirror_sniper.log y
logs/sports_activity_ws.log siguen escribiendo con la misma cadencia que
antes de la fusión.

Corre en screen propia (sustituye a sports-mirror + sports-ws):
  screen -dmS sportsfase0 bash -c "cd /root/polymarket-research && nice -n 10 .venv/bin/python sports_fase0_consolidado.py >> logs/sports_fase0_consolidado.log 2>&1"
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
# verify_deploy.py sigue detectando STALE si se toca cualquiera de los 2.
import sports_wallet_mirror_sniper
import sports_activity_ws
import sports_resolve  # 27-Ago noche: resuelve trades reales OPEN, ver docstring del módulo

# (modulo, fichero_log_propio -- EXACTO el que ya usaba la screen individual,
#  nombre_funcion_log_a_reemplazar, coroutine_a_lanzar)
PROCESOS = [
    (sports_wallet_mirror_sniper, "sports_wallet_mirror_sniper.log", "_log",
     lambda: sports_wallet_mirror_sniper.main_ws()),
    (sports_activity_ws, "sports_activity_ws.log", "_log",
     lambda: sports_activity_ws.main()),
    (sports_resolve, "sports_resolve.log", "_log",
     lambda: sports_resolve.main_async(60)),
]


def _logger_dedicado(nombre_log: str):
    """Idéntico a observadores_fase0.py/ejecutores_dryrun_fase0.py --
    escribe al mismo .log que ya usaba la screen individual, ningún hábito
    de `tail -f` se rompe."""
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
                pass  # nunca tumbar al proceso por un fallo de logging
    return _fn


def _correr(mod, nombre_log: str, nombre_fn_log: str, coro_factory) -> None:
    """Mismo bucle de supervisión que observadores_fase0.py::_correr_observador
    -- reintenta a los 10s si la coroutine retorna o lanza (no debería,
    ambas son bucles infinitos con su propio try/except interno)."""
    nombre_modulo = mod.__name__
    setattr(mod, nombre_fn_log, _logger_dedicado(nombre_log))
    while True:
        try:
            print(f"[sports_fase0_consolidado] arrancando {nombre_modulo} "
                  f"(log dedicado en logs/{nombre_log})", flush=True)
            asyncio.run(coro_factory())
            print(f"[sports_fase0_consolidado] ⚠️ {nombre_modulo} retornó "
                  f"(inesperado) -- reintenta en 10s", flush=True)
        except Exception as e:
            print(f"[sports_fase0_consolidado] 🚨 {nombre_modulo} murió: "
                  f"{type(e).__name__}: {e} -- reintenta en 10s", flush=True)
        time.sleep(10)


def main() -> int:
    LOGS.mkdir(parents=True, exist_ok=True)
    print(f"[sports_fase0_consolidado] arrancando {len(PROCESOS)} procesos DRY_RUN "
          f"en hilos separados (1 proceso, antes {len(PROCESOS)} procesos)", flush=True)
    hilos = {}
    for mod, nombre_log, nombre_fn_log, coro_factory in PROCESOS:
        t = threading.Thread(
            target=_correr, args=(mod, nombre_log, nombre_fn_log, coro_factory),
            daemon=True, name=mod.__name__,
        )
        t.start()
        hilos[mod.__name__] = t
        time.sleep(1.0)  # arranque escalonado -- evita golpear las APIs externas a la vez

    print(f"[sports_fase0_consolidado] {len(hilos)} hilos arrancados, supervisando cada 60s", flush=True)
    while True:
        time.sleep(60)
        muertos = [n for n, h in hilos.items() if not h.is_alive()]
        if muertos:
            print(f"[sports_fase0_consolidado] ⚠️ hilos no vivos (el supervisor interno de "
                  f"_correr ya debería haberlos reintentado): {muertos}", flush=True)


if __name__ == "__main__":
    sys.exit(main() or 0)
