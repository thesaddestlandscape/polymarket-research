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
import threading
import os
import json
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
import wallet_mirror_pnl_tracker
import analisis_familias_ic_bajo_tuplas_fuertes
import taker_rebate_tracker
import analisis_gate_riguroso_resolution_sniper_precierre_02sep
import vigia_micro_bucket_kill_switch
import vigia_reabrir_overrides_micro_bucket
import vigia_micro_bucket_kill_switch_wallet_mirror
import vigia_reabrir_overrides_wallet_mirror
import vigia_gate_bucket_wallet_mirror
import vigia_gate_bucket_wallet_mirror_fino
import vigia_bot_wallets_gate_bucket_fino
import vigia_sports_micro_bucket_kill_switch_wallet_mirror
import vigia_sports_reabrir_overrides_wallet_mirror
import wallet_mirror_tracker as _wmt
from wallet_mirror_sniper import OUT as _WMS_OUT, COLUMNS as _WMS_COLUMNS
from wallet_mirror_tracker import resolver_pendientes as _resolver_pendientes
from wallet_mirror_executor_dryrun import (
    OUT as _WME_OUT, OUT_LOCK as _WME_LOCK, COLUMNS as _WME_COLUMNS,
)

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


def _resolver_wallet_mirror_executor() -> None:
    """13-Sep: mismo patrón que _resolver_wallet_mirror_sniper() (arriba)
    pero apuntado a wallet_mirror_executor_dryrun.csv -- necesario para
    que analisis_wallet_mirror_gate_bucket_10ago.py calcule pnl/outcome
    desde la propia población de EXECUTOR (roster = wallets_operativas_
    recientes(), el que decide con dinero real) en vez de cruzar con
    wallet_mirror_sniper_dry_run.csv (roster distinto por diseño, ver
    idea_join_wallet_mirror_executor_sniper_roto_13sep)."""
    prev_out, prev_lock, prev_cols = _wmt.OUT, _wmt.OUT_LOCK, _wmt.COLUMNS
    try:
        _wmt.OUT = _WME_OUT
        _wmt.OUT_LOCK = _WME_LOCK
        _wmt.COLUMNS = _WME_COLUMNS
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
    ("wallet_mirror_executor_resolver", _resolver_wallet_mirror_executor, "wallet_mirror_executor_resolver.log", 600),
    ("live_balance", live_balance.main, "balance.log", 900),
    ("vigia_carga_sistema", vigia_carga_sistema.main, "vigia_carga_sistema.log", 900),
    ("vigia_wallet_mirror_postfix", vigia_wallet_mirror_postfix.main, "vigia_wallet_mirror_postfix.log", 900),
    ("fetch_binance_perp_cvd_oi", fetch_binance_perp_cvd_oi.main, "fetch_binance_perp_cvd_oi.log", 900),
    ("vigia_ballenas_5min_fillability", vigia_ballenas_5min_fillability.main, "vigia_ballenas_5min_fillability.log", 900),
    ("vigia_ballenas_bypass", vigia_ballenas_bypass.main, "vigia_ballenas_bypass.log", 900),
    ("vigia_causal_vs_fillable", vigia_causal_vs_fillable.main, "vigia_causal_fillable.log", 1800),
    ("vigia_ballenas_cobertura", vigia_ballenas_cobertura.main, "vigia_ballenas_cobertura.log", 1800),
    ("shadow_pnl_fiel", shadow_pnl_fiel.main, "shadow_pnl_fiel.log", 1800),
    # 02-Sep (propuesta B2, barrido de sesión "edge sin capturar"): PnL real
    # por wallet fuente de WALLET_MIRROR (cripto+sports), ver docstring del
    # módulo -- n todavía bajo por wallet, solo informativo/revisión manual.
    ("wallet_mirror_pnl_tracker", wallet_mirror_pnl_tracker.main, "wallet_mirror_pnl_tracker.log", 1800),
    # 02-Sep (propuesta B9): familias con IC agregado~0 que esconden tuplas
    # individuales fuertes -- generaliza el hallazgo manual de STREAK_MOM_5M.
    ("analisis_familias_ic_bajo_tuplas_fuertes", analisis_familias_ic_bajo_tuplas_fuertes.main,
     "analisis_familias_ic_bajo_tuplas_fuertes.log", 1800),
    # 02-Sep (propuesta C10): KPI de volumen ponderado (wV) del Taker Rebate
    # Program, cripto+sports comparten wallet/cuenta -- mismo contador de tier.
    ("taker_rebate_tracker", taker_rebate_tracker.main, "taker_rebate_tracker.log", 1800),
    # 02-Sep (petición explícita Javi: el gate tiene que reconfirmarse
    # constantemente, no quedarse congelado): regenera el gate riguroso de
    # RESOLUTION_SNIPER_PRECIERRE cada 30min -- dataset todavía muy joven
    # (1.5 días), 30min en vez del cron diario 06:55-06:59 UTC del resto de
    # gates del proyecto mientras n crece rápido. Consumido en vivo por
    # resolution_sniper_precierre_gate.py::evaluar() (caché por mtime).
    ("resolution_sniper_precierre_gate_riguroso",
     analisis_gate_riguroso_resolution_sniper_precierre_02sep.main,
     "resolution_sniper_precierre_gate_riguroso.log", 1800),
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
    # 01-Sep (hallazgo real, petición explícita Javi tras reabrir WALLET_MIRROR
    # restringido por el fino esta misma noche): el fino de WALLET_MIRROR
    # cripto NUNCA tuvo vigía programado -- a diferencia del grid (línea de
    # arriba) y del hermano de sports (cron 07:07). Sin esto, las zonas
    # reabiertas que dependen del fino habrían quedado fail-closed por
    # antigüedad (MAX_ANTIGUEDAD_S=2h15min en wallet_mirror_gate_bucket.py)
    # sin que nada las refrescara nunca.
    ("vigia_gate_bucket_wallet_mirror_fino", vigia_gate_bucket_wallet_mirror_fino.main,
     "vigia_gate_bucket_wallet_mirror_fino.log", 3600),
    # 14-Sep (petición explícita Javi: "como en wallet mirror, que cuando
    # se confirme un micro-bucket propio y fino bueno, nos avise por
    # telegram... estamos dejando dinero de sniper encima de la mesa"):
    # mismo par grid(vigia_bot_wallets_gate_bucket.py, cron diario 06:59)+
    # fino que WALLET_MIRROR arriba, pero para la familia P-GALLINA
    # (SNIPER/DISPERSO/WEEKLY_*) -- que nunca tuvo fino hasta hoy.
    ("vigia_bot_wallets_gate_bucket_fino", vigia_bot_wallets_gate_bucket_fino.main,
     "vigia_bot_wallets_gate_bucket_fino.log", 3600),
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

# 21-Sep (orden explicita Javi: "si" al rediseno, tras medir que este
# scheduler ejecutaba las 31 tareas EN SERIE en un solo hilo): una tarea larga
# frenaba a todas las demas. Medido en el log: vigia_gate_bucket_wallet_mirror
# (grid) media 321s / max 2401s, vigia_causal_vs_fillable media 511s / max
# 1775s, smart_money_tracker 189s, shadow_pnl_fiel 63s/max 456s. Consecuencia
# real: el fino de WALLET_MIRROR (caduca a las 2h15 en wallet_mirror_gate_
# bucket.py::MAX_ANTIGUEDAD_S) no corrio a las 13:55 porque el grid ocupaba
# el bucle -> con ambos caducados el ejecutor real queda fail-closed sin operar.
#
# Ahora hay 4 CARRILES. Dentro de cada carril las tareas siguen siendo
# SECUENCIALES (mismo criterio original: sin picos simultaneos y, sobre todo,
# los resolvers de wallet mirror parchean atributos globales de
# wallet_mirror_tracker y NO pueden solaparse entre si). Solo se separan las
# tareas que no comparten estado con el resto:
#   grid  : vigia_gate_bucket_wallet_mirror        (lanza subprocess propio)
#   fino  : vigia_gate_bucket_wallet_mirror_fino   (lanza subprocess propio)
#   pesado: las 3 tareas largas restantes (se bloquean solo entre si)
#   principal: todo lo demas (hilo principal)
# Pico de concurrencia: 4 tareas a la vez (antes 1). El grid vive en un
# subprocess de ~0.8GB tras el fix de shuffle_chunked.py (antes 4.7GB).
CARRILES_APARTE = {
    "grid": ["vigia_gate_bucket_wallet_mirror"],
    "fino": ["vigia_gate_bucket_wallet_mirror_fino"],
    "pesado": ["vigia_causal_vs_fillable", "smart_money_tracker", "shadow_pnl_fiel"],
}

# Ultima ejecucion por tarea, persistida: un reinicio del proceso (watchdog,
# restart diario) ya no pone todo a 0 y lanza las 31 tareas a la vez. Nombre
# cubierto por .gitignore (data/shadow/_cache_vigiasfreq_*.json).
ESTADO_PATH = REPO / "data" / "shadow" / "_cache_vigiasfreq_ultima_ejecucion.json"
_estado_lock = threading.Lock()
REINTENTO_FALLO_S = 300  # tras un fallo se reintenta en 5min, no tras el intervalo completo
_NOMBRES_CARRIL_APARTE = {n for ns in CARRILES_APARTE.values() for n in ns}


class _EnrutadorSalida:
    """Sustituye a sys.stdout/sys.stderr: cada hilo escribe en SU fichero de
    log mientras ejecuta una tarea (contextlib.redirect_stdout cambia el
    stream GLOBAL y con varios hilos mezclaria los logs de tareas distintas)."""

    def __init__(self, original):
        self._orig = original
        self._local = threading.local()

    def destino(self, f):
        self._local.f = f

    def write(self, texto):
        return (getattr(self._local, "f", None) or self._orig).write(texto)

    def flush(self):
        try:
            (getattr(self._local, "f", None) or self._orig).flush()
        except Exception:
            pass

    def __getattr__(self, nombre):
        return getattr(self._orig, nombre)


_SALIDA = {"out": None, "err": None}


def _instalar_enrutador() -> None:
    if _SALIDA["out"] is None:
        _SALIDA["out"] = _EnrutadorSalida(sys.stdout)
        _SALIDA["err"] = _EnrutadorSalida(sys.stderr)
        sys.stdout, sys.stderr = _SALIDA["out"], _SALIDA["err"]


def _correr_uno(nombre: str, fn, nombre_log: str) -> bool:
    """Devuelve True si la tarea termino bien. Fallo = excepcion, o, SOLO para
    las tareas de CARRILES_APARTE (cuyo main() devuelve 0/1 por convencion),
    un retorno distinto de 0 (/code-review 21-Sep: un fallo no debe contar como
    ejecucion normal -- el fino caduca a las 2h15 y esperar 3600s lo deja
    fail-closed)."""
    _instalar_enrutador()  # idempotente; permite llamar a _correr_uno sin pasar por ejecutar()
    path = LOGS / nombre_log
    t0 = time.time()
    ok = True
    with open(path, "a", encoding="utf-8") as f:
        _SALIDA["out"].destino(f)
        _SALIDA["err"].destino(f)
        try:
            ret = fn()
            if nombre in _NOMBRES_CARRIL_APARTE and isinstance(ret, int) and ret != 0:
                ok = False
        except SystemExit as e:
            # algunos main() hacen return/sys.exit implícito vía código de salida;
            # en las tareas de carril aparte un exit != 0 SI es fallo (/code-review 21-Sep)
            if nombre in _NOMBRES_CARRIL_APARTE and e.code not in (None, 0):
                ok = False
        except Exception as e:
            ok = False
            print(f"[vigias_frecuentes_fase0] 🚨 {nombre} murió: "
                  f"{type(e).__name__}: {e}", flush=True)
        finally:
            _SALIDA["out"].destino(None)
            _SALIDA["err"].destino(None)
    dt = time.time() - t0
    print(f"[vigias_frecuentes_fase0] {nombre} terminado en {dt:.1f}s"
          + ("" if ok else " (FALLO -- reintento en %ds)" % REINTENTO_FALLO_S), flush=True)
    return ok


def _cargar_estado() -> dict:
    try:
        d = json.loads(ESTADO_PATH.read_text(encoding="utf-8"))
        return {k: float(v) for k, v in d.items()}
    except Exception:
        return {}


def _marcar_ejecutada(ultima: dict, nombre: str, intervalo: float, ok: bool) -> None:
    """Muta `ultima` y persiste BAJO EL MISMO LOCK (varios carriles escriben
    claves distintas: sin lock, json.dumps podia lanzar 'dictionary changed
    size during iteration' y el except lo tragaba). Tras un fallo se deja la
    marca de forma que la tarea venza en REINTENTO_FALLO_S."""
    with _estado_lock:
        ahora = time.time()
        ultima[nombre] = ahora if ok else ahora - max(0.0, intervalo - REINTENTO_FALLO_S)
        try:
            tmp = ESTADO_PATH.with_name(ESTADO_PATH.stem + ".tmp.json")
            tmp.write_text(json.dumps(dict(ultima)), encoding="utf-8")
            os.replace(tmp, ESTADO_PATH)
        except Exception as e:
            print(f"[vigias_frecuentes_fase0] aviso: no se pudo persistir el estado ({e})", flush=True)


def _bucle_carril(carril: str, tareas: list, ultima: dict, parar: threading.Event) -> None:
    """Bucle de un carril: tareas en serie dentro del carril, cada una con su
    intervalo. `ultima` es compartido (dict, escrituras de claves distintas
    por carril) y se persiste tras cada ejecucion."""
    while not parar.is_set():
        try:
            ahora = time.time()
            for nombre, fn, nombre_log, intervalo in tareas:
                if parar.is_set():
                    return
                if ahora - ultima.get(nombre, 0.0) >= intervalo:
                    ok = _correr_uno(nombre, fn, nombre_log)
                    _marcar_ejecutada(ultima, nombre, intervalo, ok)
                    parar.wait(1.0)  # pequeño respiro entre tareas, no golpear APIs externas a la vez
        except Exception as e:  # un fallo del propio bucle no debe matar el carril
            print(f"[vigias_frecuentes_fase0] 🚨 carril {carril} fallo interno: "
                  f"{type(e).__name__}: {e} -- reintenta en 60s", flush=True)
            parar.wait(60.0)
            continue
        parar.wait(TICK_S)


def _repartir_carriles(tareas: list) -> dict:
    aparte = {n for ns in CARRILES_APARTE.values() for n in ns}
    carriles = {c: [t for t in tareas if t[0] in ns] for c, ns in CARRILES_APARTE.items()}
    carriles["principal"] = [t for t in tareas if t[0] not in aparte]
    return carriles


def ejecutar(tareas: list, parar: threading.Event = None) -> None:
    """Arranca los carriles: los apartes en hilos daemon, `principal` en el
    hilo llamante. Con `parar` (Event) se puede detener limpiamente (tests)."""
    parar = parar or threading.Event()
    _instalar_enrutador()
    ultima = _cargar_estado()
    carriles = _repartir_carriles(tareas)
    hilos = []
    for carril, ts in carriles.items():
        if carril == "principal" or not ts:
            continue
        h = threading.Thread(target=_bucle_carril, args=(carril, ts, ultima, parar),
                             name=f"carril-{carril}", daemon=True)
        h.start()
        hilos.append(h)
    print(f"[vigias_frecuentes_fase0] carriles: "
          + ", ".join(f"{c}={len(ts)}" for c, ts in carriles.items()), flush=True)
    _bucle_carril("principal", carriles["principal"], ultima, parar)


def main() -> int:
    LOGS.mkdir(parents=True, exist_ok=True)
    print(f"[vigias_frecuentes_fase0] arrancando scheduler con {len(TAREAS)} tareas "
          f"(4 carriles, ver CARRILES_APARTE; tick={TICK_S:.0f}s)", flush=True)
    ejecutar(TAREAS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
