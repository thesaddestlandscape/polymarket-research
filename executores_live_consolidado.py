#!/usr/bin/env python3
"""
executores_live_consolidado.py -- Consolida los 4 ejecutores de baja
latencia de dinero real que hoy corren en 4 screens separadas
(ballenas_fast=ballenas_executor_btc15m.py, ballenas_5m=ballenas_executor_
5min.py, favaltaconv=favorito_altaconviccion_executor_15min.py,
favbtc60mno=favorito_confirmado_btc60min_buyno_executor.py) en UN SOLO
proceso (10-Ago, petición explícita Javi: "consolida más procesos" tras
detectar CPU sobresuscrita, load5/nproc=5.0x).

Motivo cuantificado: los 4 ejecutores importan ballenas_firehose_cache
y cada uno llama a su propio `_fc.iniciar()` -- pero cada uno vive en su
PROPIO proceso, así que cada uno abre su PROPIA conexión websocket
independiente a RTDS (wss://ws-live-data.polymarket.com, topic
activity/trades) y parsea el stream COMPLETO por separado -- 4 conexiones
y 4x el trabajo de parseo/filtrado para exactamente el mismo dato. Como
`ballenas_firehose_cache.iniciar()` ya es idempotente A NIVEL DE PROCESO
(guardado en el global `_hilo_iniciado` del módulo), basta con que los 4
ejecutores compartan UN proceso para que solo la primera llamada abra
conexión real -- las otras 3 se vuelven no-ops automáticos, sin tocar ni
una línea de ballenas_firehose_cache.py ni de los 4 ejecutores.

Diseño (mínimo riesgo, CERO cambios en los 4 ejecutores originales,
que siguen operando con dinero real exactamente igual que antes):
  - Importa los 4 módulos tal cual, sin modificarlos.
  - Parchea SOLO su función `log()` (monkeypatch en runtime, no en
    disco) para prefijar un tag por origen -- sin esto, los 4 imprimirían
    a la misma stdout sin forma de distinguir qué estrategia generó cada
    línea. `log` se resuelve en cada módulo como global a nivel de
    llamada, así que reasignar `modulo.log` SÍ afecta a las llamadas ya
    existentes dentro de ese módulo (no hace falta editar el .py).
  - Lanza cada `modulo.main()` en su propio hilo -- cada main() YA es un
    supervisor de sus propios hilos de trabajo internos (por activo),
    exactamente igual que cuando corría en su propio proceso.
  - Si CUALQUIERA de los 4 `main()` lanza una excepción no capturada
    (no debería -- cada uno ya envuelve su propio bucle interno en
    try/except), se termina el proceso ENTERO con os._exit(1) en vez de
    intentar reiniciar solo ese hilo. Motivo: reiniciar un módulo
    individual sin matar el proceso podría duplicar sus hilos de trabajo
    internos (los hilos daemon del intento anterior no se garantiza que
    hayan muerto) -- riesgo real de ejecutar la misma señal dos veces con
    dinero real. Terminar el proceso entero es más seguro: pipeline_
    watchdog.py reinicia la screen completa desde cero, limpio, mismo
    mecanismo de red de seguridad que ya existía por-proceso antes de
    consolidar. Contrapartida explícita: un bug en CUALQUIERA de los 4
    ahora tumba a los 4 durante el reinicio (antes solo tumbaba al suyo)
    -- blast radius mayor a cambio de 75% menos conexiones redundantes.

NO toca live_trade.py, NO toca la lógica de ninguno de los 4 ejecutores,
NO cambia ningún umbral/gate/decisión -- solo el modelo de procesos.
"""
import os
import threading
import time
from datetime import datetime, timezone

import ballenas_executor_5min as _m_ballenas5m
import ballenas_executor_btc15m as _m_ballenasbtc15m
import ballenas_executor_15min as _m_ballenas15m
import favorito_altaconviccion_executor_15min as _m_altaconv
import favorito_confirmado_btc60min_buyno_executor as _m_btc60mno

# 20-Ago: ballenas_executor_15min.py añadido -- pasó a DRY_RUN=False para
# BALLENAS_CONFIRMADAS_15M#ETH#15min#BUY_YES (checklist 6 categorías
# completo, ver idea_gate_bucket_fino_ventana_deslizante_20ago). Sacado de
# ejecutores_dryrun_fase0.py (screen ejecdryrun, exige DRY_RUN=True en
# todos sus módulos) -- este consolidado es el destino correcto para
# dinero real, mismo patrón que los 4 anteriores. No usa
# ballenas_firehose_cache (a diferencia de los otros 4) -- no gana la
# optimización de conexión compartida, pero sí gana supervisión de
# watchdog/verify_deploy y consistencia con el resto de ejecutores live.
MODULOS = [
    ("BALLENAS_5M", _m_ballenas5m),
    ("BALLENAS_BTC15M", _m_ballenasbtc15m),
    ("BALLENAS_15M", _m_ballenas15m),
    ("ALTACONVICCION_15M", _m_altaconv),
    ("FAV_BTC60M_BUYNO", _m_btc60mno),
]


def _log_runner(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] [runner] {msg}", flush=True)


def _parchear_log(tag: str, mod) -> None:
    log_original = mod.log

    def log_taggeado(msg, *a, **kw):
        return log_original(f"[{tag}] {msg}", *a, **kw)

    mod.log = log_taggeado


def _correr_modulo(tag: str, mod) -> None:
    try:
        mod.main()
    except Exception as e:
        _log_runner(f"🔥 {tag}: main() lanzó excepción no capturada ({e!r}) -- "
                     f"terminando proceso ENTERO para forzar restart limpio vía watchdog")
        os._exit(1)
    _log_runner(f"🔥 {tag}: main() retornó sin excepción (no debería pasar nunca) -- "
                 f"terminando proceso ENTERO para forzar restart limpio vía watchdog")
    os._exit(1)


def main() -> None:
    tags = [t for t, _ in MODULOS]
    _log_runner(f"arrancando {len(MODULOS)} ejecutores consolidados: {tags}")
    for tag, mod in MODULOS:
        _parchear_log(tag, mod)

    hilos = []
    for tag, mod in MODULOS:
        h = threading.Thread(target=_correr_modulo, args=(tag, mod), daemon=False, name=tag)
        h.start()
        hilos.append(h)
        time.sleep(2)  # escalonar arranque -- no golpear firehose/gamma-api/ClobClient a la vez

    while True:
        time.sleep(60)
        vivos = [h.name for h in hilos if h.is_alive()]
        if len(vivos) != len(hilos):
            _log_runner(f"⚠️ hilos vivos: {vivos} (esperados {tags}) -- "
                         f"alguno debería haber tumbado el proceso ya, revisar")


if __name__ == "__main__":
    main()
