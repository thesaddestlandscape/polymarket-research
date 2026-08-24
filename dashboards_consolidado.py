#!/usr/bin/env python3
"""
dashboards_consolidado.py — fusiona dashboard_server.py (crypto+live,
puerto 8888) y sports_dashboard_server.py (puerto 8890) en UN SOLO
proceso, cada uno en su propio hilo daemon. Mismo patrón exacto que
observadores_fase0.py (05-Ago) / ejecutores_dryrun_fase0.py (06-Ago) /
vigias_frecuentes_fase0.py (17-Ago) / sports_fase0_consolidado.py
(20-Ago) / nested_arb_loop.py (20-Ago) — ver esos ficheros para el
razonamiento completo del diseño, no se repite aquí.

Origen (24-Ago, petición explícita Javi tras barrido de salud con CPU
sobresuscrita: load5=8.16 ratio=4.08x en 2 cores, "consolida más
procesos"): dash y dash-sports eran las 2 últimas screens de solo
lectura (HTTP dashboards, sin dinero real, ninguna toca `live_trade.py`)
que seguían sin fusionar tras la ronda de consolidaciones de 05→20-Ago.
weather-dash queda FUERA a propósito (repo independiente
/root/polymarket-weather, CLAUDE.md prohíbe mezclar código entre repos).

dashboard_server.py NO tiene main() propio -- su arranque vive directo
bajo `if __name__ == "__main__":` (últimas líneas del fichero:
ThreadedHTTPServer + Handler + serve_forever()). Se replica EXACTO ese
bloque aquí (mismo patrón "caso especial" que vigias_frecuentes_fase0.py
usa para wallet_mirror_sniper --resolver) en vez de tocar el fichero
original -- así verify_deploy.py sigue detectando STALE si se edita
cualquiera de los 2 ficheros (import estático). sports_dashboard_server.py
sí tiene main(), se llama directo.

Verificado ANTES de fusionar: ambos, a nivel de módulo, solo definen
clases/constantes y leen data/live/.env (auth Basic ya existente en
dashboard_server.py) -- ningún servidor arranca al importar, el arranque
de dashboard_server.py está guardado por `if __name__`.

NO cambia ninguna lógica de ninguno de los 2 dashboards -- mismos puertos
(8888/8890), mismos datos, misma auth -- solo el proceso que los sirve.

Corre en screen propia:
  screen -dmS dash bash -c "cd /root/polymarket-research && nice -n 10 .venv/bin/python dashboards_consolidado.py >> logs/dashboards_consolidado.log 2>&1"
"""
import sys
import threading
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

# Imports ESTÁTICOS a propósito (ver observadores_fase0.py) -- así
# verify_deploy.py sigue detectando STALE si se toca cualquiera de los 2.
import dashboard_server
import sports_dashboard_server


def _correr_crypto() -> None:
    while True:
        try:
            srv = dashboard_server.ThreadedHTTPServer(
                ("::", dashboard_server.PORT), dashboard_server.Handler
            )
            print(f"[dashboards_consolidado] dashboard crypto -> :{dashboard_server.PORT}", flush=True)
            srv.serve_forever()
            print("[dashboards_consolidado] ⚠️ dashboard crypto serve_forever() retornó "
                  "(inesperado) -- reintenta en 10s", flush=True)
        except Exception as e:
            print(f"[dashboards_consolidado] 🚨 dashboard crypto murió: "
                  f"{type(e).__name__}: {e} -- reintenta en 10s", flush=True)
        time.sleep(10)


def _correr_sports() -> None:
    while True:
        try:
            print(f"[dashboards_consolidado] dashboard sports -> :{sports_dashboard_server.PORT}", flush=True)
            sports_dashboard_server.main()
            print("[dashboards_consolidado] ⚠️ dashboard sports main() retornó "
                  "(inesperado) -- reintenta en 10s", flush=True)
        except Exception as e:
            print(f"[dashboards_consolidado] 🚨 dashboard sports murió: "
                  f"{type(e).__name__}: {e} -- reintenta en 10s", flush=True)
        time.sleep(10)


def main() -> int:
    hilos = {
        "crypto": threading.Thread(target=_correr_crypto, daemon=True, name="dash-crypto"),
        "sports": threading.Thread(target=_correr_sports, daemon=True, name="dash-sports"),
    }
    for nombre, t in hilos.items():
        t.start()
        time.sleep(1.0)  # arranque escalonado

    print(f"[dashboards_consolidado] {len(hilos)} hilos arrancados, supervisando cada 60s", flush=True)
    while True:
        time.sleep(60)
        muertos = [n for n, h in hilos.items() if not h.is_alive()]
        if muertos:
            print(f"[dashboards_consolidado] ⚠️ hilos no vivos (el supervisor interno de "
                  f"cada uno ya reintenta solo): {muertos}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
