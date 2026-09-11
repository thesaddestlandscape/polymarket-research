#!/usr/bin/env python3
"""
vigias_horarios_fase0.py — Consolida 19 vigías/trackers de un solo disparo
(cron horario, cada uno en su propio minuto) en UN SOLO proceso disparado
UNA VEZ por hora, ejecutando cada main() EXISTENTE SIN MODIFICAR NINGUNA
LÍNEA de los 19 ficheros originales. Mismo espíritu que observadores_fase0.py
/ejecutores_dryrun_fase0.py (05/06-Ago) pero patrón distinto: aquellos son
bucles infinitos (1 hilo daemon por módulo, viven todo el día); estos son
scripts de un solo disparo por hora (cron), así que aquí se ejecutan
SECUENCIALMENTE dentro de un único disparo de cron, no en hilos persistentes.

Origen (11-Ago tarde): load5/nproc sostenido alto, live_trade degradado de
~20-25s a 100-150s por ciclo. Diagnóstico encontró 3 causas ya corregidas
(git pack.threads mal configurado, crons nuevos del día sin nice, 2 scripts
per-minuto sin nice) — con eso el ciclo bajó a 40-49s, todavía por encima
del objetivo de 20s. Esta consolidación ataca la causa que queda: ~19
procesos Python distintos arrancando cada uno su propio intérprete +
imports (pandas/numpy pesados en varios) en minutos dispersos de cada hora,
cada arranque compite por CPU/RAM con el fast loop en marcha. Un solo
arranque de intérprete con 19 imports amortizados y ejecución secuencial
(nunca paralela — evita picos de CPU simultáneos, además más seguro para
el fast loop) reduce el número de arranques de intérprete/hora de 19 a 1.

Verificado ANTES de fusionar (mismo rigor AST+import que las fusiones
anteriores): los 19 tienen `def main()` + `if __name__ == "__main__":`
(ningún trabajo se dispara al importar), ningún `sys.exit()` fuera de ese
guard (seguro llamar a `mod.main()` sin que mate el proceso consolidado),
y a nivel de módulo solo hacen `sys.path.insert` (idempotente) o
`load_dotenv(...)` (idempotente) — cero side-effects reales al importar.

NO cambia ninguna lógica de decisión, gate, fichero de salida, ni columna
de ninguno de los 19 — solo el proceso/horario que los ejecuta. Cada uno
sigue escribiendo en su propio logs/<nombre>.log de siempre (stdout
redirigido por módulo durante su turno), así que ningún hábito de
`tail -f logs/vigia_x.log` se rompe.

Ejecución SECUENCIAL con aislamiento de excepción por módulo — si uno
revienta, los demás siguen. Tiempo total estimado ~2-3min (I/O-bound
leyendo CSVs grandes), muy por debajo de la hora entre disparos.

Corre vía cron (un solo disparo, sustituye los 19 minutos dispersos):
  0 * * * * flock -n /tmp/vigias_horarios_fase0.lock /root/polymarket-research/.venv/bin/python /root/polymarket-research/vigias_horarios_fase0.py >> /root/polymarket-research/logs/vigias_horarios_fase0.log 2>&1
"""
import contextlib
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
LOGS = REPO / "logs"

# Imports ESTÁTICOS a propósito (ver observadores_fase0.py) -- así
# verify_deploy.py / cualquier auditoría de "¿qué corre esto?" sigue
# encontrando los 19 ficheros reales, no un nombre genérico.
import reconciliar_posiciones
import vigia_pybajo
import vigia_streak_fade_calib
import vigia_xrp_10h_maker
import vigia_favorito_60min
import vigia_gates_pendientes
import maker_pilot_sim
import vigia_filtro_gbmlate
import wallet_contraparte_tracker
import wallet_contraparte_shadow
import vigia_sigma_patrones
import vigia_log_loss_vs_mercado
import wallet_edge_tracker
import vigia_wallet_edge_forward
import vigia_ibs_updowngbm_fillable
import vigia_log_growth
import vigia_boost_eth15_ballenas
import vigia_pipeline_latencia
import vigia_resumen_alertas_horario

# (modulo, fichero_log_propio -- EXACTO el que ya usaba su entrada de cron)
VIGIAS = [
    (reconciliar_posiciones, "reconciliar_posiciones.log"),
    (vigia_pybajo, "vigia_pybajo.log"),
    (vigia_streak_fade_calib, "vigia_streak_fade_calib.log"),
    (vigia_xrp_10h_maker, "vigia_xrp_10h_maker.log"),
    (vigia_favorito_60min, "vigia_favorito_60min.log"),
    (vigia_gates_pendientes, "vigia_gates_pendientes.log"),
    (maker_pilot_sim, "maker_pilot_sim.log"),
    (vigia_filtro_gbmlate, "vigia_filtro_gbmlate.log"),
    (wallet_contraparte_tracker, "wallet_contraparte.log"),
    (wallet_contraparte_shadow, "wallet_contraparte_shadow.log"),
    (vigia_sigma_patrones, "vigia_sigma_patrones.log"),
    (vigia_log_loss_vs_mercado, "vigia_log_loss.log"),
    (wallet_edge_tracker, "wallet_edge_tracker.log"),
    (vigia_wallet_edge_forward, "vigia_wallet_edge_forward.log"),
    (vigia_ibs_updowngbm_fillable, "vigia_ibs_updowngbm.log"),
    (vigia_log_growth, "vigia_log_growth.log"),
    (vigia_boost_eth15_ballenas, "vigia_boost_eth15_ballenas.log"),
    (vigia_pipeline_latencia, "vigia_pipeline_latencia.log"),
    (vigia_resumen_alertas_horario, "vigia_resumen_alertas_horario.log"),
]


def _correr_uno(mod, nombre_log: str) -> None:
    """Ejecuta mod.main() con stdout/stderr redirigidos a su log propio
    (append, igual que `>> log 2>&1` en el cron original), aislado de
    excepción -- un vigía roto no debe tumbar a los otros 18."""
    path = LOGS / nombre_log
    t0 = time.time()
    with open(path, "a", encoding="utf-8") as f:
        with contextlib.redirect_stdout(f), contextlib.redirect_stderr(f):
            try:
                mod.main()
            except SystemExit:
                pass  # algunos main() hacen return/sys.exit implícito vía código de salida
            except Exception as e:
                print(f"[vigias_horarios_fase0] 🚨 {mod.__name__} murió: "
                      f"{type(e).__name__}: {e}", flush=True)
    dt = time.time() - t0
    print(f"[vigias_horarios_fase0] {mod.__name__} terminado en {dt:.1f}s", flush=True)


def main() -> int:
    LOGS.mkdir(parents=True, exist_ok=True)
    print(f"[vigias_horarios_fase0] arrancando {len(VIGIAS)} vigías secuenciales "
          f"(1 proceso, antes {len(VIGIAS)} procesos dispersos por hora)", flush=True)
    t0 = time.time()
    for mod, nombre_log in VIGIAS:
        _correr_uno(mod, nombre_log)
    print(f"[vigias_horarios_fase0] {len(VIGIAS)} vigías completados en "
          f"{time.time() - t0:.1f}s totales", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
