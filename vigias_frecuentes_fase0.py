#!/usr/bin/env python3
"""
vigias_frecuentes_fase0.py — consolida 19 scripts de UN SOLO DISPARO que
antes corrían vía cron cada 5-60 minutos (~130+ arranques de intérprete
Python/hora dispersos) en UN SOLO proceso persistente con scheduler
interno. (20-Ago: 17→19, ver bloque de imports/TAREAS más abajo con fecha
20-Ago -- smart_money_tracker y sports_wallet_mirror_sniper_resolver,
ambos cron */20min retirados, mismo rigor de verificación AST.) Mismo patrón que vigias_horarios_fase0.py (11-Ago, cadencia
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
import csv
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
import vigia_reabrir_overrides_micro_bucket
import vigia_micro_bucket_kill_switch_wallet_mirror
import vigia_reabrir_overrides_wallet_mirror
import vigia_gate_bucket_wallet_mirror
import vigia_sports_micro_bucket_kill_switch_wallet_mirror
import vigia_sports_reabrir_overrides_wallet_mirror
import wallet_mirror_tracker as _wmt
from wallet_mirror_sniper import OUT as _WMS_OUT, COLUMNS as _WMS_COLUMNS
from wallet_mirror_tracker import resolver_pendientes as _resolver_pendientes

# 20-Ago (Javi: "consolida procesos", presión CPU/RAM tras incidente OOM real
# de esta sesión -- ver logs/vigia_pipeline_latencia.log 21:03 Madrid): 2
# candidatos más plegados aquí, mismo rigor AST ya aplicado a los 17
# anteriores (sin trabajo real a nivel de módulo, solo sys.path.insert
# idempotente / anotación de tipo sin llamada / asignaciones puras).
import smart_money_tracker
import sports_wallet_mirror_sniper as _swms


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


def _resolver_sports_wallet_mirror_sniper() -> None:
    """Réplica exacta de `sports_wallet_mirror_sniper.py --resolver` (ver
    su propio main(), bloque `if args.resolver`) -- resolver_pendientes()
    es self-contained en ese módulo (no monkeypatching necesario, a
    diferencia del hermano cripto de arriba)."""
    n = _swms.resolver_pendientes()
    print(f"resueltas este ciclo: {n}")
    if _swms.OUT.exists():
        with open(_swms.OUT, newline="", encoding="utf-8") as f:
            filas = [r for r in csv.DictReader(f) if r.get("outcome_real_index")]
        if filas:
            n_tot = len(filas)
            aciertos = sum(1 for r in filas if r["acierto"] == "1")
            n_seguir = sum(1 for r in filas if r["tipo"] == "SEGUIR")
            print(f"acumulado resuelto: n={n_tot} hit={aciertos/n_tot*100:.1f}% "
                  f"(SEGUIR n={n_seguir}, FADE n={n_tot - n_seguir})")


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
    # 24-Ago (petición explícita Javi: "es tu trabajo revisarlo, si una se
    # bloquea, en el próximo ciclo la revisas y si está OK la desbloqueas"):
    # el kill switch de arriba bloquea un bucket PARA SIEMPRE hasta que
    # alguien borre el override a mano -- este vigía es la mitad que
    # faltaba, revisa cada override automático contra dinero real reciente
    # + el gate fresco y lo reabre solo si ambas señales lo confirman. Va
    # DESPUÉS del kill switch en la lista (incluso con el mismo intervalo,
    # el orden de ejecución del scheduler es el orden de esta lista) para
    # nunca revisar un override en el mismo ciclo en que se acaba de crear.
    ("vigia_reabrir_overrides_micro_bucket", vigia_reabrir_overrides_micro_bucket.main, "vigia_reabrir_overrides_micro_bucket.log", 1800),
    # 24-Ago: mismo par bloqueo+reapertura, pero para el gate paralelo de
    # WALLET_MIRROR (wallet_mirror_gate_bucket.py) -- las 6 tuplas
    # WALLET_MIRROR (dinero real desde 10/11/12-Ago) no tenían NINGÚN
    # backstop hasta hoy. Requiere wallet_mirror_executor_dryrun.py
    # logueando "grande=" en trades.csv (mismo día) -- trades anteriores
    # se excluyen fail-closed, no se reconstruyen retroactivamente.
    ("vigia_micro_bucket_kill_switch_wallet_mirror", vigia_micro_bucket_kill_switch_wallet_mirror.main,
     "vigia_micro_bucket_kill_switch_wallet_mirror.log", 1800),
    ("vigia_reabrir_overrides_wallet_mirror", vigia_reabrir_overrides_wallet_mirror.main,
     "vigia_reabrir_overrides_wallet_mirror.log", 1800),
    ("vigia_gate_bucket_wallet_mirror", vigia_gate_bucket_wallet_mirror.main, "vigia_gate_bucket_wallet_mirror.log", 3600),
    # 27-Ago noche (petición explícita Javi: "construye lo que falte de
    # sports para tenerlo ya hecho cuando toque operar en directo"): mismo
    # par bloqueo+reapertura que WALLET_MIRROR cripto arriba, pero para
    # sports_wallet_mirror_gate_bucket.py -- construido ANTES del primer
    # trade real (sports sigue con pares_permitidos_live=[] hoy), no
    # semanas después como pasó con WALLET_MIRROR (10/11-Ago -> 24-Ago).
    ("vigia_sports_micro_bucket_kill_switch_wallet_mirror", vigia_sports_micro_bucket_kill_switch_wallet_mirror.main,
     "vigia_sports_micro_bucket_kill_switch_wallet_mirror.log", 1800),
    ("vigia_sports_reabrir_overrides_wallet_mirror", vigia_sports_reabrir_overrides_wallet_mirror.main,
     "vigia_sports_reabrir_overrides_wallet_mirror.log", 1800),
    # 20-Ago: 2 más, cadencia EXACTA de sus crons retirados (*/20 * * * * = 1200s)
    ("smart_money_tracker", smart_money_tracker.main, "smart_money.log", 1200),
    ("sports_wallet_mirror_sniper_resolver", _resolver_sports_wallet_mirror_sniper, "sports_wallet_mirror_resolver.log", 1200),
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
