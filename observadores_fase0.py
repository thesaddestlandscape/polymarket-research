#!/usr/bin/env python3
"""
observadores_fase0.py — Consolida 10 observadores/loggers puramente
observacionales (ninguno ejecuta dinero real) en UN SOLO proceso, cada
uno en su propio hilo daemon ejecutando su main() EXISTENTE SIN
MODIFICAR NINGUNA LÍNEA de los 10 ficheros originales.

Origen (05-Ago, decisión explícita Javi tras el incidente de push roto
por sobresuscripción de CPU -- ver project_push_roto_carga_cpu_resuelto_05ago
en memoria): el bankroll no permite subir el VPS (decisión explícita:
"no podemos permitirnos pagar más pasta"), así que la mitigación real es
reducir el número de procesos persistentes. Estos 10 comparten el mismo
patrón (poll cada 1.5-5s o por ventana de mercado, comprueba una
condición, escribe una fila a CSV si dispara) y NINGUNO mueve dinero real
ni decide nada -- son la familia más segura de consolidar sin tocar nada
que afecte a capital.

Diseño (rigor: cero cambios a los 10 scripts originales en disco):
  - Cada módulo se importa normal (import script_x). Verificado a mano,
    los 10 (AST, no solo grep) NO ejecutan trabajo real a nivel de
    módulo -- solo definiciones y 2 construcciones de objeto sin efectos
    secundarios (requests.Session(), _ChainlinkTail.__init__ que solo
    inicializa estado, no arranca hilos ni hace I/O).
  - Se reemplaza (monkeypatch, `setattr(modulo, nombre_fn_log, ...)`) la
    función log()/_log() de cada módulo por un logger dedicado que
    escribe al MISMO fichero que ya usaba esa screen individual
    (logs/<nombre>.log) -- ningún hábito de depuración existente se
    rompe, cada observador sigue teniendo su propio log legible aparte.
  - main() de cada módulo se lanza en su propio threading.Thread daemon.
    Los 10 main() YA son bucles infinitos autocontenidos con su propio
    try/except interno; varios ya usan hilos/ThreadPoolExecutor
    internamente para I/O concurrente -- anidar hilos es seguro y ya es
    el patrón que usan hoy en sus procesos separados.
  - Un supervisor en el hilo principal reinicia cualquier hilo que muera
    (defensa en profundidad -- no debería pasar, cada main() ya atrapa
    sus propias excepciones, pero si algo escapa no debe tumbar a los
    otros 9).
  - Verificado ANTES de fusionar: `ballenas_firehose_cache.iniciar()`
    (lo llaman sol5min_contrario_fase0 y xrp15min_contrario_fase0) es
    IDEMPOTENTE (guardado por `_hilo_iniciado`, ver ballenas_firehose_
    cache.py línea ~221) -- fusionarlos en el mismo proceso además
    ELIMINA una conexión websocket redundante (antes 2 procesos con su
    propia conexión al firehose, ahora comparten una).

Arranque escalonado (1s entre cada hilo) para no golpear las APIs
externas (gamma-api, CLOB, Chainlink) con 10 arranques simultáneos.

NO cambia ninguna estrategia, gate, fichero de salida, ni columna de
ninguno de los 10 -- solo el proceso que los ejecuta. Verificar tras
desplegar que los 10 CSV de salida (data/shadow/*.csv) siguen creciendo
con la misma cadencia que antes de la fusión.

Corre en screen propia:
  screen -dmS observadores bash -c "cd /root/polymarket-research && .venv/bin/python observadores_fase0.py >> logs/observadores_fase0.log 2>&1"
"""
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
LOGS = REPO / "logs"

# Imports ESTÁTICOS (no importlib dinámico) a propósito: verify_deploy.py
# detecta STALE siguiendo el cierre transitivo de imports por regex sobre
# el texto fuente -- con importlib.import_module(str) esa detección sería
# ciega a cambios en los 10 scripts fusionados. Con `import X` normal,
# tocar cualquiera de los 10 (p.ej. box_builder_fase0.py) SÍ marca esta
# screen como STALE hasta reiniciarla, igual que antes de la fusión.
import photo_finish_logger
import favorito_ultimosegundo_5min
import punto_confirmacion_logger
import resolution_sniper_observer
import p22_cola_posicion_fase0
import box_builder_fase0
import sol5min_contrario_fase0
import xrp15min_contrario_fase0
import favorito_confirmado_senal_contraria_fase0
import favorito_5min_altaconviccion_logger

# (modulo, fichero_log_propio -- EXACTO el que ya usaba pipeline_watchdog.SCREEN_RESTART, nombre_funcion_log_a_reemplazar)
OBSERVADORES = [
    (photo_finish_logger, "photo_finish.log", "_log"),
    (favorito_ultimosegundo_5min, "favorito_ultimosegundo.log", "_log"),
    (punto_confirmacion_logger, "punto_confirmacion.log", "_log"),
    (resolution_sniper_observer, "resolution_sniper_observer.log", "_log"),
    (p22_cola_posicion_fase0, "p22_cola_posicion_fase0.log", "_log"),
    (box_builder_fase0, "box_builder_fase0.log", "log"),
    (sol5min_contrario_fase0, "sol5min_contrario_fase0.log", "log"),
    (xrp15min_contrario_fase0, "xrp15min_contrario_fase0.log", "log"),
    (favorito_confirmado_senal_contraria_fase0, "favorito_confirmado_senal_contraria_fase0.log", "_log"),
    (favorito_5min_altaconviccion_logger, "favorito_5min_altaconviccion.log", "log"),
]


def _logger_dedicado(nombre_log: str):
    """Escribe directamente al fichero .log propio de ese observador,
    igual que antes cuando la screen redirigía su stdout ahí -- así el
    merge no rompe ningún hábito de `tail -f logs/X.log` existente."""
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
                pass  # nunca tumbar al observador por un fallo de logging
    return _fn


def _correr_observador(mod, nombre_log: str, nombre_fn_log: str) -> None:
    """Bucle de supervisión: inyecta el logger dedicado en el módulo (ya
    importado estáticamente arriba) y corre su main(). Si main() retorna
    o lanza una excepción (no debería -- main() son bucles infinitos con
    su propio try/except), reintenta a los 10s en vez de dejar el
    observador muerto en silencio."""
    nombre_modulo = mod.__name__
    setattr(mod, nombre_fn_log, _logger_dedicado(nombre_log))
    while True:
        try:
            print(f"[observadores_fase0] arrancando {nombre_modulo} "
                  f"(log dedicado en logs/{nombre_log})", flush=True)
            mod.main()
            print(f"[observadores_fase0] ⚠️ {nombre_modulo}.main() retornó "
                  f"(inesperado, sus main() son bucles infinitos) -- reintenta en 10s", flush=True)
        except Exception as e:
            print(f"[observadores_fase0] 🚨 {nombre_modulo} murió: "
                  f"{type(e).__name__}: {e} -- reintenta en 10s", flush=True)
        time.sleep(10)


def main() -> int:
    LOGS.mkdir(parents=True, exist_ok=True)
    print(f"[observadores_fase0] arrancando {len(OBSERVADORES)} observadores "
          f"en hilos separados (1 proceso, antes {len(OBSERVADORES)} procesos)", flush=True)
    hilos = {}
    for mod, nombre_log, nombre_fn_log in OBSERVADORES:
        t = threading.Thread(
            target=_correr_observador, args=(mod, nombre_log, nombre_fn_log),
            daemon=True, name=mod.__name__,
        )
        t.start()
        hilos[mod.__name__] = t
        time.sleep(1.0)  # arranque escalonado -- evita golpear las APIs externas a la vez

    print(f"[observadores_fase0] {len(hilos)} hilos arrancados, supervisando cada 60s", flush=True)
    while True:
        time.sleep(60)
        muertos = [n for n, h in hilos.items() if not h.is_alive()]
        if muertos:
            print(f"[observadores_fase0] ⚠️ hilos no vivos (el supervisor interno de "
                  f"_correr_observador ya debería haberlos reintentado): {muertos}", flush=True)


if __name__ == "__main__":
    sys.exit(main() or 0)
