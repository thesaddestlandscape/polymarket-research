#!/usr/bin/env python3
"""
dispersed_bot_executor_dryrun.py -- P-GALLINA FASE 1 (25-Ago noche,
petición explícita Javi: "busca alfa, dinero... cerrar el stage 0").
ACTUALIZADO 26-Ago (petición explícita Javi, tras ver 6/8 veredictos
nuevos del aviso de Telegram revertir a sin_concluir en el mismo día --
"actualízalo y déjalo acumulando para que trackee absolutamente todo el
universo, así tenemos datos de todo ya"): se elimina el filtro fijo a 3
combos hardcodeados. La inestabilidad del propio gate (buckets que pasan
y dejan de pasar en horas con solo un poco más de n) es la prueba de que
fijar el ejecutor a un snapshot puntual queda obsoleto casi de inmediato
-- mejor trackear TODO lo que detecta el firehose (4 arquetipos x 6
activos x 5 marcos x buckets de precio) y dejar que `_gate_veredicto()`
decida en vivo, en cada fila, si ese combo/bucket exacto está confirmado
HOY. Así se acumula histórico completo de decisión simulada (stake real,
circuit breakers) para el universo entero, sin tener que re-desplegar
cada vez que el gate cambia de veredicto.

Extensión de bot_wallets_gate_bucket_fase0.py (FASE 0, solo lectura) a
FASE 1 DRY_RUN. Fill-ability real (ratio_vs_stake>=5x) ya verificada
sólida en varios combos (SOL 58%, BTC 85%, XRP 60%, ver histórico) --
señales genuinamente ejecutables cuando el gate las confirma, no solo
teóricas.

Mismo patrón EXACTO de detección que bot_wallets_gate_bucket_fase0.py
(firehose vía _archivos_activity(), fill-ability vía _fillability_mirror()
de wallet_mirror_tracker.py) -- ahora SIN restringir a combos concretos.
Añade la capa que bot_wallets_gate_bucket_fase0.py no tiene: simulación
de decisión de trade real (calcular_stake real, circuit breakers) --
mismo criterio que wallet_mirror_executor_dryrun.py/momentum_ibs_
ballena_executor.py.

⚠️ DRY_RUN=True SIEMPRE. Activar DRY_RUN=False (dinero real) requiere
aprobación explícita de Javi en una sesión futura, con el checklist de
6 categorías (project_checklist_conexion_promocion_live_31jul) revisado
a fondo para el combo concreto -- pendiente: cruce contra ballenas/franja
fina NO hecho todavía (arquetipo de bot wallets no es una estrategia de
shadow_predict.py, zonas_validadas_externas.json no lo cubre), y exigir
ESTABILIDAD del veredicto durante varios días seguidos antes de proponer
nada, dada la fragilidad observada 26-Ago.

NO coloca, cancela ni modifica ninguna orden real mientras DRY_RUN=True.

07-Sep (petición explícita Javi, tras el checklist de 6 categorías sobre
SNIPER#BTC#5min[0.25,0.30): "construye el envío real, con /code-review
antes de comitear"): se añade el TRAMO de envío real
(`lt._ejecutar_orden_polymarket`), mismo patrón EXACTO que P24 FASE 2 en
wallet_mirror_executor_dryrun.py (06-Ago, activado 11-Ago).

08-Sep (petición explícita Javi, ACTIVACIÓN REAL tras 2/2 lecturas
diarias estables del veredicto -- 07-Sep y 08-Sep, sin revertir --
checklist ya completado 07-Sep): **DRY_RUN=False, SOLO para
SNIPER#BTC#5min[0.25,0.30)**. Mismo día se encontraron y corrigieron 2
huecos reales antes de activar (petición explícita: "revisa que todo
esté conectado, el re-quote, revisa mil veces, no podemos permitirnos
fallar"):
  (a) el re-chequeo post-requote de `_ejecutar_orden_polymarket` NUNCA
      había tenido forma de consultar `bot_wallets_gate_bucket.json`
      (la función `_gate_veredicto()` era local a este fichero, no
      registrada en `_GATES_EXTERNOS_POR_ESTRATEGIA`) -- mismo bug ya
      corregido para WALLET_MIRROR (25-Ago) y CANDIDATA9_BOT_CONSENSO
      (mismo día, 08-Sep). Fix: módulo compartido nuevo
      `bot_wallets_gate_bucket.py`, registrado en `live_trade.py`, este
      fichero delega en él (`_gate_veredicto()` ya no relee el JSON a
      mano).
  (b) este gate confirma por (arquetipo,activo,marco,bucket) SIN separar
      por dirección de la orden -- `pares_permitidos_live` solo puede
      restringir por tupla+dirección, así que añadir la whitelist
      habría activado TODOS los buckets bueno_confirmado de
      SNIPER#BTC#5min (incluido [0.05,0.10), que tiene g_kelly NEGATIVO,
      payout inverso, nunca aprobado). Fix: `bot_wallets_gate_bucket.
      py::permitido_real()`/`BUCKETS_APROBADOS_REAL`, lista explícita
      por micro-bucket, consultada TANTO en el chequeo inicial (aquí)
      como en el recheck (`evaluar_para_recheck`) -- ninguno de los dos
      puede aprobar un bucket que el otro no apruebe.
  (c) `log`/`_log` renombrado a `log` (sin guión bajo) -- requisito del
      runner de `executores_live_consolidado.py` (`_parchear_log`
      monkeypatchea `mod.log`, no `mod._log`), necesario para mover este
      proceso de la screen `ejecdryrun` (niced, DRY_RUN) a `ejeclive`
      (dinero real, sin nice) -- mismo criterio que el resto de
      ejecutores de baja latencia con dinero real.

Seguridad -- guardianes vigentes hoy (verificados uno a uno antes de
activar, no solo listados):
  1. `DRY_RUN=False` (abajo) -- SOLO permite continuar si además pasan
     los guardianes 2-6; con `DRY_RUN=True` el tramo de envío real ni se
     evalúa (así sigue funcionando para el resto de arquetipos/buckets
     todavía en investigación).
  2. Whitelist real: la tupla sintética exacta
     ("SNIPER#BTC#5min#BUY_Up"/"...#BUY_Down") tiene que estar en
     `pares_permitidos_live` -- verificado explícitamente, no asumido.
  3. `permitido_real()` -- el micro-bucket exacto tiene que estar en
     `BUCKETS_APROBADOS_REAL` (solo [0.25,0.30) hoy) ADEMÁS de la
     whitelist -- ver (b) arriba.
  4. `veredicto == "bueno_confirmado"` en caliente (`bot_wallets_gate_
     bucket.json`, recalculado cada fila) -- si el autoaprendizaje
     retira la confirmación, deja de disparar aunque siga en
     `BUCKETS_APROBADOS_REAL`.
  5. Re-chequeo post-requote y multi-lectura antes de firmar en
     `live_trade.py::_ejecutar_orden_polymarket`, vía
     `bot_wallets_gate_bucket.evaluar_para_recheck()` (registrado en
     `_GATES_EXTERNOS_POR_ESTRATEGIA`) -- misma fuente que el guardián
     3-4, no puede divergir.
  6. `edge_dir=ic_proxy` pasado a `_ejecutar_orden_polymarket` --
     mecanismo de aborto por edge evaporado (`_decidir_requote`,
     `REQUOTE_EDGE_MIN`) activo, no se salta (mismo bug ya corregido en
     WALLET_MIRROR 06-Ago y CANDIDATA9_BOT_CONSENSO 08-Sep).

Resto de arquetipos/buckets de esta familia (17 candidatos más
detectados a 08-Sep) siguen SOLO en observación -- ninguno en
`pares_permitidos_live` ni en `BUCKETS_APROBADOS_REAL`, el guardián 2/3
los bloquea igual que antes.

NO se replica el veto CLV (`lt._clv_tupla`) que sí usan los ejecutores
hermanos -- ese veto lee `results.csv` por `strategy=arquetipo`, pero
esta familia es un pipeline paralelo que NUNCA escribe en `results.csv`
(mismo motivo por el que WALLET_MIRROR tampoco lo replica) -- devolvería
n=0 y sería un no-op silencioso, se deja fuera explícitamente. Tampoco
se construye un kill-switch de micro-bucket dedicado (como
`vigia_micro_bucket_kill_switch_wallet_mirror.py`) -- pendiente; el
guardián 4 (`_gate_veredicto` recalculado en cada fila desde el JSON
fresco) ya cubre el caso base de "deja de estar confirmado -> deja de
disparar".
"""
import csv
import json
import math
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from wallet_mirror_tracker import (  # noqa: E402
    _archivos_activity, _fillability_mirror, _market_id_y_direccion,
    leer_activity_incremental,
)
from live_stake import calcular_stake, bloquear_por_circuit_breaker  # noqa: E402
import live_trade as lt  # noqa: E402
from live_guard import puede_operar_live  # noqa: E402
import bot_wallets_gate_bucket as _bwgb  # noqa: E402

DRY_RUN = False  # 08-Sep, aprobación explícita Javi -- SOLO SNIPER#BTC#5min[0.25,0.30) puede ejecutar de verdad (ver guardianes 2-3 en el docstring)

DIR_SHADOW = REPO / "data" / "shadow"
CONFIG_LIVE = REPO / "data" / "live" / "config_live.json"
OUT = DIR_SHADOW / "dispersed_bot_executor_dryrun.csv"
VISTOS_PATH = DIR_SHADOW / "dispersed_bot_executor_dryrun_vistos.json"
ACTIVITY_CHECKPOINT_PATH = DIR_SHADOW / "dispersed_bot_executor_dryrun_activity_checkpoint.json"
BOTS_PATH = DIR_SHADOW / "bot_wallets_universo_25ago.json"
HIST = DIR_SHADOW / "ballenas_timing_history.csv"

POLL_S = 5
STEP_BUCKET = 0.05
UMBRAL_SNIPER_MIN = 5.0

COLUMNS = [
    "timestamp_utc", "trade_timestamp", "wallet", "arquetipo", "activo", "marco",
    "bucket_precio", "market_slug", "lado_wallet", "mejor_ask_deteccion",
    "profundidad_eur_deteccion", "ratio_vs_stake_deteccion", "sigue_fillable",
    "gate_veredicto", "stake_sim_eur", "circuit_breaker_bloquea", "decision_dry_run",
]


def log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _bucket(p: float) -> float:
    return round(math.floor(p / STEP_BUCKET + 1e-9) * STEP_BUCKET, 4)


def _en_whitelist(tupla: str) -> bool:
    """Mismo patrón que wallet_mirror_executor_dryrun.py::_en_whitelist --
    guardián #2, independiente de DRY_RUN."""
    try:
        c = json.loads(CONFIG_LIVE.read_text())
        return tupla in set(c.get("pares_permitidos_live", []))
    except Exception:
        return False


def clasificar_arquetipos(wallets: set) -> dict:
    """MISMA lógica que bot_wallets_gate_bucket_fase0.py::clasificar_arquetipos()."""
    from collections import defaultdict
    por_wallet = defaultdict(lambda: defaultdict(list))
    with open(HIST, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            w = r.get("wallet", "").lower()
            if w not in wallets:
                continue
            try:
                rm = float(r["restante_min"])
            except (TypeError, ValueError):
                continue
            por_wallet[w][r.get("marco", "?")].append(rm)
    out = {}
    for w, marcos in por_wallet.items():
        marco_dom = max(marcos, key=lambda m: len(marcos[m]))
        mediana = sorted(marcos[marco_dom])[len(marcos[marco_dom]) // 2]
        if marco_dom == "weekly":
            out[w] = "WEEKLY_TEMPRANO" if mediana > 500 else "WEEKLY_TARDIO"
        else:
            out[w] = "SNIPER" if mediana <= UMBRAL_SNIPER_MIN else "DISPERSO"
    return out


def _gate_veredicto(arquetipo: str, activo: str, marco: str, bucket: float) -> str:
    """08-Sep: delegado a bot_wallets_gate_bucket.py (antes releía el JSON
    aquí mismo, sin caché, y el re-chequeo post-requote de live_trade.py
    no tenía forma de consultar esta misma fuente -- mismo bug ya
    corregido para WALLET_MIRROR/CANDIDATA9_BOT_CONSENSO. Única fuente de
    verdad ahora, para que el chequeo inicial (aquí) y el recheck
    (evaluar_para_recheck, registrado en _GATES_EXTERNOS_POR_ESTRATEGIA)
    nunca puedan divergir."""
    return _bwgb.evaluar(arquetipo, activo, marco, bucket).get("veredicto", "sin_concluir")


def _vistos_cargar() -> dict:
    """dict en vez de set: mismo fix 01-Sep que wallet_mirror_sniper.py/
    wallet_mirror_executor_dryrun.py -- Python preserva orden de inserción
    en dict (NO en set), necesario para que el cap de abajo descarte las
    entradas más VIEJAS, no un subconjunto arbitrario por hash."""
    try:
        return dict.fromkeys(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return {}


def _vistos_guardar(vistos: dict) -> None:
    VISTOS_PATH.write_text(json.dumps(list(vistos)[-20000:]), encoding="utf-8")


def _guardar(filas: list) -> None:
    if not filas:
        return
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(COLUMNS)
        for fila in filas:
            w.writerow([fila.get(c, "") for c in COLUMNS])


def _seed_vistos_sin_consultar(wallets: set) -> dict:
    vistos = _vistos_cargar()
    nuevos = 0
    # 07-Sep: checkpoint incremental (ver leer_activity_incremental() en
    # wallet_mirror_tracker.py) -- este backlog corría en CADA restart del
    # proceso, releyendo el firehose completo (~1,5GB/4M filas) cada vez.
    # Con checkpoint persistido, un restart solo relee lo escrito desde el
    # último checkpoint de este consumidor.
    for row in leer_activity_incremental(ACTIVITY_CHECKPOINT_PATH):
        if (row.get("side") or "").strip().upper() != "BUY":
            continue
        w = (row.get("wallet") or "").lower()
        if w not in wallets:
            continue
        # 01-Sep: mismo fix que wallet_mirror -- dedup por
        # transaction_hash, no permanente por (wallet,mercado), para
        # no perder trades de convicción repetida de la misma bot
        # wallet en el mismo mercado.
        tx_hash = row.get("transaction_hash", "")
        dedup_key = f"{w}|{row.get('market_slug','')}|{tx_hash}" if tx_hash else f"{w}|{row.get('market_slug','')}|{row.get('ws_timestamp','')}"
        if dedup_key not in vistos:
            vistos[dedup_key] = None
            nuevos += 1
    log(f"backlog existente marcado como visto sin consultar profundidad: {nuevos} matches")
    return vistos


def _procesar_fila(row: dict, wallets: set, arquetipos: dict, vistos: dict) -> dict | None:
    if (row.get("side") or "").strip().upper() != "BUY":
        return None
    w = (row.get("wallet") or "").lower()
    if w not in wallets:
        return None
    arquetipo = arquetipos.get(w, "?")
    activo = row.get("activo", "")
    marco = row.get("marco", "")
    # 01-Sep (mismo fix que wallet_mirror, petición explícita Javi): antes
    # dedup_key era f"{w}|{market_slug}", PERMANENTE -- una bot wallet que
    # opera el mismo mercado varias veces solo se capturaba la primera vez,
    # para siempre, perdiendo evidencia real que alimenta bot_wallets_gate_
    # bucket_fase0.csv (Candidata 9/10 "gallina de huevos de oro").
    tx_hash = row.get("transaction_hash", "")
    dedup_key = f"{w}|{row.get('market_slug','')}|{tx_hash}" if tx_hash else f"{w}|{row.get('market_slug','')}|{row.get('ws_timestamp','')}"
    if dedup_key in vistos:
        return None
    vistos[dedup_key] = None
    try:
        precio = float(row.get("price") or 0)
    except (TypeError, ValueError):
        return None
    if not (0.0 < precio < 1.0):
        return None
    b = _bucket(precio)
    # 26-Ago: sin filtro de combo -- se procesa TODO el universo (4
    # arquetipos x 6 activos x 5 marcos x bucket), el gate decide en vivo
    # por fila si ese combo/bucket exacto está confirmado hoy.

    lado = row.get("outcome", "")
    fill = _fillability_mirror(row.get("market_slug", ""), lado, row.get("price", ""))
    ratio = fill.get("ratio_vs_stake") if fill.get("ok") else None
    sigue_fillable = bool(ratio is not None and ratio >= 5.0)

    veredicto = _gate_veredicto(arquetipo, activo, marco, b)

    # Simulación de stake real (mismo camino que un ejecutor live real,
    # pero DRY_RUN -- nunca se envía). ic_proxy conservador: usamos el
    # hit-rate confirmado del bucket como proxy de IC (mismo patrón que
    # wallet_mirror_executor_dryrun.py/momentum_ibs_ballena_executor.py).
    ic_proxy = 0.15  # conservador -- no hay IC real para señales de wallet
    stake_sim = 0.0
    try:
        r_stake = calcular_stake(ic_proxy, strategy="DISPERSED_BOT", subtype=f"{activo}#{marco}",
                                  direction="BUY_YES" if lado == "Up" else "BUY_NO",
                                  precio_entrada=precio)
        stake_sim = r_stake.get("stake_eur", 0.0)
    except Exception as e:
        log(f"WARN calcular_stake falló: {e}")

    cb_bloquea = False
    try:
        cb_bloquea = bool(bloquear_por_circuit_breaker(lambda motivo: log(f"circuit breaker: {motivo}")))
    except Exception:
        pass

    decision = "DISPARARIA" if (veredicto == "bueno_confirmado" and sigue_fillable and not cb_bloquea) else "NO_dispara"

    # --- Tramo de envío real (07-Sep, petición explícita Javi; ACTIVO desde
    # 08-Sep, DRY_RUN=False). Solo llega aquí de verdad si pasan los 6
    # guardianes del docstring del módulo -- whitelist (guardián #2) y
    # BUCKETS_APROBADOS_REAL (guardián #3) hoy solo dejan pasar
    # SNIPER#BTC#5min[0.25,0.30), el resto del universo sigue bloqueado. ---
    tupla_sintetica = f"{arquetipo}#{activo}#{marco}#BUY_{lado}"
    if not DRY_RUN and decision == "DISPARARIA":
        en_wl = _en_whitelist(tupla_sintetica)
        # 08-Sep: guardián adicional -- este gate confirma por (arquetipo,
        # activo,marco,bucket) SIN separar por dirección, así que estar en
        # pares_permitidos_live habilitaría CUALQUIER bucket bueno_confirmado
        # de esa tupla, no solo el aprobado explícitamente por Javi (algunos
        # buckets confirmados tienen g_kelly negativo, payout inverso -- ver
        # bot_wallets_gate_bucket.py::BUCKETS_APROBADOS_REAL). permitido_real()
        # exige el bucket exacto en esa lista, además del veredicto en caliente.
        if en_wl and not _bwgb.permitido_real(arquetipo, activo, marco, precio):
            log(f"  ⛔ {tupla_sintetica} bucket[{b:.2f}) no está en "
                 f"BUCKETS_APROBADOS_REAL -- fail-closed, no se ejecuta")
        elif not en_wl:
            log(f"  ⛔ {tupla_sintetica} no está en pares_permitidos_live -- "
                 f"fail-closed, no se ejecuta pese a DRY_RUN=False")
        else:
            puede_ventana, motivo_ventana = True, ""
            try:
                puede_ventana, motivo_ventana = puede_operar_live(arquetipo, f"{activo}#{marco}")
            except Exception:
                puede_ventana = False
            if not puede_ventana:
                log(f"  ⛔ fuera de ventana horaria live ({motivo_ventana}) -- no se ejecuta")
            else:
                resuelto = _market_id_y_direccion(row.get("market_slug", ""), lado)
                if resuelto is None:
                    log("  ⛔ no se pudo resolver market_id/dirección con seguridad "
                         "(outcomes inesperados o Gamma sin datos) -- fail-closed, no se ejecuta")
                else:
                    market_id, direction, end_date_real = resuelto
                    max_correl = lt._cargar_config().get("riesgo", {}).get(
                        "max_posiciones_abiertas_misma_direccion", 2)
                    if lt._posiciones_abiertas_misma_direccion(direction) >= max_correl:
                        log(f"  ⛔ techo de correlación ({direction}) alcanzado -- no se ejecuta")
                    # /code-review 07-Sep: re-chequeo del circuit breaker justo
                    # antes de disparar -- el primer chequeo (cb_bloquea,
                    # arriba) es ANTES de la ida-y-vuelta de red a
                    # _market_id_y_direccion (Gamma /events, ~90-300ms según
                    # el perfilado de wallet_mirror_tracker.py), así que un
                    # freno que se dispare DURANTE esa espera (p.ej. otro
                    # ejecutor cierra una pérdida en la misma ventana) no se
                    # habría detectado sin este segundo chequeo. Mismo patrón
                    # que wallet_mirror_executor_dryrun.py:395-397 (último
                    # guardián antes de firmar, no solo el chequeo temprano).
                    elif bloquear_por_circuit_breaker(
                            lambda motivo: log(f"  ⛔ circuit breaker activo ({motivo}) -- no se ejecuta")):
                        pass
                    elif fill.get("mejor_ask") in (None, "") or not (float(stake_sim or 0) > 0):
                        log("  ⛔ precio/stake sin resolver -- fail-closed, no se ejecuta")
                    else:
                        ask_f = float(fill["mejor_ask"])
                        precio_orden_yes = ask_f if direction == "BUY_YES" else round(1.0 - ask_f, 6)
                        # edge_dir: mismo ic_proxy conservador ya usado arriba
                        # para el stake -- _ejecutar_orden_polymarket lo usa
                        # para el re-quote/abort si el edge se evaporó entre
                        # detección y decisión (_decidir_requote), mismo
                        # guardián que exige el resto de ejecutores live.
                        resultado = lt._ejecutar_orden_polymarket(
                            market_id, direction, float(stake_sim), precio_orden_yes,
                            edge_dir=ic_proxy,
                            contexto={"strategy": arquetipo, "subtype": f"{activo}#{marco}",
                                      "tupla_sintetica": tupla_sintetica})
                        log(f"  🚨 ORDEN REAL enviada ({tupla_sintetica}): {resultado}")
                        if not resultado.get("no_fill"):
                            trade = {
                                "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                "market_id": market_id, "question": "", "end_date": end_date_real,
                                "strategy": arquetipo, "subtype": f"{activo}#{marco}",
                                "direction": direction,
                                "stake_eur": float(stake_sim) if resultado.get("ok") else 0.0,
                                "entry_price": resultado.get("entry_price", ""),
                                "signal_ask": round(ask_f, 4),
                                "slip_real": resultado.get("slip_real", ""),
                                "ic_modelo": round(ic_proxy, 4), "edge_neto": round(ic_proxy, 4),
                                "conviction_score": round(ic_proxy, 4),
                                "kelly_recomendado": stake_sim,
                                "status": "OPEN" if resultado.get("ok") else "ERROR",
                                "close_timestamp": "", "exit_price": "", "outcome_real": "",
                                "fee_eur": resultado.get("fee_eur", 0),
                                "pnl_bruto_eur": "", "pnl_neto_eur": "",
                                "notas": (f"dispersed_bot wallet={w} arquetipo={arquetipo}"
                                          if resultado.get("ok") else resultado.get("error", "")),
                            }
                            lt._registrar_trade(trade)
                            if resultado.get("ok"):
                                lt.enviar_telegram(
                                    f"🎯 *Orden live ejecutada ({arquetipo})*\n"
                                    f"Tupla: {tupla_sintetica}\n"
                                    f"Wallet copiada: {w}\n"
                                    f"Precio fill: {resultado['entry_price']:.4f} "
                                    f"(slip {resultado.get('slip_real', 0):+.4f})\n"
                                    f"Stake: {float(stake_sim):.2f}€\n"
                                    f"Bankroll operativo: {lt.bankroll_actual():.2f}$ (real al cierre de ciclo)"
                                )
                            else:
                                lt.enviar_telegram(
                                    f"❌ *Orden live ERROR ({arquetipo})*\n"
                                    f"{tupla_sintetica}\n{str(resultado.get('error', ''))[:200]}"
                                )

    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "trade_timestamp": row.get("timestamp_utc", ""),
        "wallet": w, "arquetipo": arquetipo, "activo": activo, "marco": marco,
        "bucket_precio": f"{b:.2f}", "market_slug": row.get("market_slug", ""),
        "lado_wallet": lado, "mejor_ask_deteccion": fill.get("mejor_ask", "") if fill.get("ok") else "",
        "profundidad_eur_deteccion": fill.get("profundidad_eur", "") if fill.get("ok") else "",
        "ratio_vs_stake_deteccion": ratio if ratio is not None else "",
        "sigue_fillable": int(sigue_fillable), "gate_veredicto": veredicto,
        "stake_sim_eur": stake_sim, "circuit_breaker_bloquea": int(cb_bloquea),
        "decision_dry_run": decision,
    }


def main() -> None:
    bots = json.loads(BOTS_PATH.read_text(encoding="utf-8"))
    wallets = set(bots.keys())
    arquetipos = clasificar_arquetipos(wallets)
    log(f"dispersed_bot_executor_dryrun arrancado (DRY_RUN={DRY_RUN}) -- "
         f"{len(wallets)} bot wallets, universo completo (sin filtro de combo)")

    vistos = _seed_vistos_sin_consultar(wallets)
    _vistos_guardar(vistos)

    # 07-Sep (/code-review): antes trackeaba posición de lectura solo en
    # memoria -- en cada restart del proceso volvía a leer el fichero
    # completo desde justo tras la cabecera. leer_activity_incremental()
    # usa el mismo checkpoint persistido que el seed de arriba, así que un
    # restart solo relee lo escrito desde el último checkpoint.
    while True:
        try:
            filas = []
            for row in leer_activity_incremental(ACTIVITY_CHECKPOINT_PATH):
                fila = _procesar_fila(row, wallets, arquetipos, vistos)
                if fila is not None:
                    filas.append(fila)
                    log(f"[{fila['arquetipo']}] {fila['activo']}#{fila['marco']}"
                         f"[{fila['bucket_precio']}) wallet={fila['wallet'][:10]}.. "
                         f"veredicto={fila['gate_veredicto']} fillable={fila['sigue_fillable']} "
                         f"stake_sim={fila['stake_sim_eur']} -> {fila['decision_dry_run']}")
            if filas:
                _guardar(filas)
                _vistos_guardar(vistos)
        except Exception as e:
            log(f"🚨 error en ciclo: {type(e).__name__}: {e}")
        time.sleep(POLL_S)


if __name__ == "__main__":
    main()
