#!/usr/bin/env python3
"""
vigias_frecuentes_fase0.py — consolida 17 scripts de UN SOLO DISPARO que
hoy corren vía cron cada 5-60 minutos (~130 arranques de intérprete
Python/hora dispersos) en UN SOLO proceso persistente con scheduler
interno. Mismo patrón que vigias_horarios_fase0.py (11-Ago, cadencia
horaria) y observadores_fase0.py (05-Ago, hilos infinitos) pero aplicado
a la capa de cadencia SUB-horaria (5/10/15/30/60 min) que quedó fuera de
esas dos fusiones.

Origen (17-Ago, petición explícita Javi: "vamos a solucionar
vigia_carga_sistema.py, unifica como ya has hecho veces anteriores"):
`vigia_carga_sistema.py` llevaba todo el día oscilando anomalo=True/False
(ratio5 carga/núcleos 3.0-5.0 sobre 2 cores, avisando por Telegram en
cada transición). Diagnóstico: 17 scripts standalone arrancando su propio
intérprete + imports (pandas/numpy en varios) en minutos dispersos de
cada hora -- el más frecuente cada 5min, varios cada 10-15min -- cada
arranque compite por CPU con fast/slow/ejecutores en marcha. Reducir el
número de arranques de intérprete/hora ataca la causa real (no solo el
síntoma que vigía_carga_sistema.py mide).

`nested_arb_scanner.py` (cadencia más fina, cada 1 min) se deja FUERA a
propósito: acoplarlo a un scheduler secuencial junto a 17 hermanos más
lentos arriesga que un hermano colgado retrase justo el más sensible a
la cadencia. Se queda en su cron propio (ya con nice -n 10 + flock).

Diseño: UN proceso, bucle con tick de 20s. Cada tarea tiene su propio
intervalo (idéntico al de su entrada de crontab retirada) y se ejecuta
SECUENCIALMENTE (nunca en paralelo -- mismo criterio que
vigias_horarios_fase0.py, evita picos de CPU simultáneos) cuando su
intervalo vence. Aislamiento de excepción por tarea -- una rota no debe
tumbar a las otras 16. Cada una sigue escribiendo en su propio
logs/<nombre>.log de siempre (stdout/stderr redirigidos durante su turno,
igual que hacía `>> log 2>&1` en su cron original).

Verificado ANTES de fusionar (mismo rigor AST que las fusiones previas):
las 17 tienen `def main()` + guard `if __name__` (o son función standalone
para el caso especial de abajo), sin sys.exit() fuera de ese guard, y a
nivel de módulo solo hacen sys.path.insert (idempotente), mkdir(exist_ok=
True) o un try/except de import -- cero efectos secundarios reales al
importar.

Caso especial -- `wallet_mirror_sniper.py --resolver`: ese modo no tiene
`main()` propio, es un bloque `if __name__` que monkeypatchea 3 atributos
de módulo de `wallet_mirror_tracker` (OUT/OUT_LOCK/COLUMNS, para apuntar
el resolver al CSV de sniper en vez del de tracker) y llama a
`resolver_pendientes()`. `_resolver_wallet_mirror_sniper()` de abajo
replica EXACTO ese bloque, con guardado/restauración de los 3 atributos
alrededor de la llamada -- ningún otro script fusionado aquí importa
`wallet_mirror_tracker`, pero la restauración es defensa en profundidad
por si se añade uno en el futuro.

NO cambia ninguna lógica de decisión, gate, fichero de salida ni columna
de ninguno de los 17 -- solo el proceso/cadencia que los dispara. Ninguno
ejecuta dinero real (son vigías/observadores/resolvers de shadow o de
posiciones ya cerradas); el único que toca `data/live/` es `live_balance.py`
(lectura on-chain, ya read-only hoy).

Corre en screen propia:
  screen -dmS vigiasfreq bash -c "cd /root/polymarket-research && nice -n 10 .venv/bin/python vigias_frecuentes_fase0.py >> logs/vigias_frecuentes_fase0.log 2>&1"
"""
import contextlib
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
LOGS = REPO / "logs"

# Imports ESTÁTICOS a propósito (ver observadores_fase0.py / vigias_horarios_
# fase0.py): así verify_deploy.py sigue detectando STALE si se toca
# cualquiera de los 17 ficheros reales, no un nombre genérico.
import vigia_calidad_datos
import vigia_ballenas_snapshot_freshness
import vigia_nested_arb_gate
import resuelve_ballenas_5min
import resuelve_ballenas_15min
import live_balance
import vigia_carga_sistema
import vigia_wallet_mirror_postfix
import fetch_binance_perp_cvd_oi
import vigia_ballenas_5min_fillability
import vigia_ballenas_bypass
import vigia_causal_vs_fillable
import vigia_ballenas_cobertura
import shadow_pnl_fiel
import vigia_micro_bucket_kill_switch
import vigia_gate_bucket_wallet_mirror
import wallet_mirror_tracker as _wmt
from wallet_mirror_sniper import OUT as _WMS_OUT, COLUMNS as _WMS_COLUMNS
from wallet_mirror_tracker import resolver_pendientes as _resolver_pendientes


def _resolver_wallet_mirror_sniper() -> None:
    """Réplica exacta de `wallet_mirror_sniper.py --resolver` (ver
    docstring del módulo) -- monkeypatch acotado con restauración."""
    prev_out, prev_lock, prev_cols = _wmt.OUT, _wmt.OUT_LOCK, _wmt.COLUMNS
    try:
        _wmt.OUT = _WMS_OUT
        _wmt.OUT_LOCK = REPO / "data" / "shadow" / "wallet_mirror_sniper_dry_run.csv.lock"
        _wmt.COLUMNS = _WMS_COLUMNS
        n = _resolver_pendientes()
        print(f"Resueltas: {n}")
    finally:
        _wmt.OUT, _wmt.OUT_LOCK, _wmt.COLUMNS = prev_out, prev_lock, prev_cols


# (nombre, callable, log_propio -- EXACTO el que ya usaba su entrada de
# cron retirada, intervalo_seg -- EXACTO el de esa entrada de cron)
TAREAS = [
    ("vigia_calidad_datos", vigia_calidad_datos.main, "vigia_calidad_datos.log", 300),
    ("vigia_ballenas_snapshot_freshness", vigia_ballenas_snapshot_freshness.main, "vigia_ballenas_snapshot_freshness.log", 300),
    ("vigia_nested_arb_gate", vigia_nested_arb_gate.main, "vigia_nested_arb_gate.log", 600),
    ("resuelve_ballenas_5min", resuelve_ballenas_5min.main, "resuelve_ballenas_5min.log", 600),
    ("resuelve_ballenas_15min", resuelve_ballenas_15min.main, "resuelve_ballenas_15min.log", 600),
    ("wallet_mirror_sniper_resolver", _resolver_wallet_mirror_sniper, "wallet_mirror_sniper_resolver.log", 600),
    ("live_balance", live_balance.main, "balance.log", 900),
    ("vigia_carga_sistema", vigia_carga_sistema.main, "vigia_carga_sistema.log", 900),
    ("vigia_wallet_mirror_postfix", vigia_wallet_mirror_postfix.main, "vigia_wallet_mirror_postfix.log", 900),
    ("fetch_binance_perp_cvd_oi", fetch_binance_perp_cvd_oi.main, "fetch_binance_perp_cvd_oi.log", 900),
    ("vigia_ballenas_5min_fillability", vigia_ballenas_5min_fillability.main, "vigia_ballenas_5min_fillability.log", 900),
    ("vigia_ballenas_bypass", vigia_ballenas_bypass.main, "vigia_ballenas_bypass.log", 900),
    ("vigia_causal_vs_fillable", vigia_causal_vs_fillable.main, "vigia_causal_fillable.log", 1800),
    ("vigia_ballenas_cobertura", vigia_ballenas_cobertura.main, "vigia_ballenas_cobertura.log", 1800),
    ("shadow_pnl_fiel", shadow_pnl_fiel.main, "shadow_pnl_fiel.log", 1800),
    ("vigia_micro_bucket_kill_switch", vigia_micro_bucket_kill_switch.main, "vigia_micro_bucket_kill_switch.log", 1800),
    ("vigia_gate_bucket_wallet_mirror", vigia_gate_bucket_wallet_mirror.main, "vigia_gate_bucket_wallet_mirror.log", 3600),
]

TICK_S = 20.0


def _correr_uno(nombre: str, fn, nombre_log: str) -> None:
    path = LOGS / nombre_log
    t0 = time.time()
    with open(path, "a", encoding="utf-8") as f:
        with contextlib.redirect_stdout(f), contextlib.redirect_stderr(f):
            try:
                fn()
            except SystemExit:
                pass  # algunos main() hacen return/sys.exit implícito vía código de salida
            except Exception as e:
                print(f"[vigias_frecuentes_fase0] 🚨 {nombre} murió: "
                      f"{type(e).__name__}: {e}", flush=True)
    dt = time.time() - t0
    print(f"[vigias_frecuentes_fase0] {nombre} terminado en {dt:.1f}s", flush=True)


def main() -> int:
    LOGS.mkdir(parents=True, exist_ok=True)
    print(f"[vigias_frecuentes_fase0] arrancando scheduler con {len(TAREAS)} tareas "
          f"(antes ~130 arranques de intérprete/hora dispersos, ahora 1 proceso, "
          f"tick={TICK_S:.0f}s)", flush=True)
    ultima_ejecucion = {nombre: 0.0 for nombre, *_ in TAREAS}
    while True:
        ahora = time.time()
        for nombre, fn, nombre_log, intervalo in TAREAS:
            if ahora - ultima_ejecucion[nombre] >= intervalo:
                _correr_uno(nombre, fn, nombre_log)
                ultima_ejecucion[nombre] = time.time()
                time.sleep(1.0)  # pequeño respiro entre tareas, no golpear APIs externas a la vez
        time.sleep(TICK_S)
    return 0


if __name__ == "__main__":
    sys.exit(main())
