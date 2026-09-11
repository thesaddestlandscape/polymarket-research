#!/usr/bin/env python3
"""
candidata9_bot_consenso_executor.py — 08-Sep, ejecutor de baja latencia
REAL para CANDIDATA9_BOT_CONSENSO (consenso mayoritario de bot wallets),
petición explícita Javi tras completar el checklist de 6 categorías para
ETH#15min[0.50,0.55): gate propio confirmado (n=366, shuffle_p=0.013,
CI90% bootstrap no cruza cero), fill-ability real (n=256 mercados, 75%
fillable, edge+7.2pp sobre ask), cruce con ballenas (señal incremental,
MÁS fuerte fuera de cobertura ballenas: n=279 edge+20.3pp p=0.0000),
Kelly/log-growth (g(f=10%)=+0.02291, sin payout inverso, n=429). Único
punto flojo, aceptado explícitamente por Javi: concentración de wallet
(top1=33.1%, top1+2=61.8% de 21 wallets, por encima del umbral de alarma
30%) -- decisión: "promocionarla igualmente, empezando con stake mínimo
y vigilando si esas 2 wallets siguen activas".

Por qué un ejecutor NUEVO y no basta con activar candidata9_bot_
consenso_reactivo_fase0.py: ese observador solo REGISTRA la predicción
en predictions_YYYY-MM-DD.csv para que entre en el pipeline estándar
(shadow_resolve/postmortem/gate_bucket_propio) -- nunca coloca una orden
real. Añadir "CANDIDATA9_BOT_CONSENSO#ETH#15min#BUY_YES" a
pares_permitidos_live NO habría bastado tampoco: live_trade.py::main()
exige ic_bayes agregado >= min_ic_para_live (0.08) antes de sizear nada,
y el ic_bayes agregado de CANDIDATA9_BOT_CONSENSO hoy es 0.0153 (dominado
por el histórico de BTC#5min, que además acaba de degradar a
sin_concluir) -- la señal se habría bloqueado en la puerta pese al edge
real y confirmado del micro-bucket ETH#15min. Mismo patrón que TODOS los
demás ejecutores de baja latencia de este proyecto (ballenas_executor_
5min.py, favorito_confirmado_btc60min_buyno_executor.py, etc.): un
ejecutor dedicado que bypasea por completo el gate de IC agregado de
live_trade.py::main() y usa el gate propio de MICRO-BUCKET como única
fuente de verdad del precio.

Generalizado igual que candidata9_bot_consenso_reactivo_fase0.py (mismo
día, misma petición Javi "amplía... a todos los marcos y monedas"): NO
hay una lista fija de zonas activadas -- vigila TODOS los activos/marcos
y consulta EN CALIENTE candidata9_10_gate_bucket.json vía
_gate_confirma() (importado del observador fase0, mismo módulo, sin
duplicar la lógica de caché). Cualquier zona nueva que el gate confirme
mañana con el mismo rigor puede llegar a operar real en cuanto Javi la
añada a pares_permitidos_live -- el ejecutor no necesita tocarse.

Mecanismo (idéntico al observador fase0 hasta el punto de decisión,
luego diverge a ejecución real en vez de solo registrar):
  1. Trackea votos por condition_id de bot wallets validadas
     (bot_wallets_universo_25ago.json) sobre TODO el firehose.
  2. Trigger = mayoría ESTRICTA (misma lógica sin look-ahead que
     analisis_candidata9_10_gate_bucket_26ago.py).
  3. Doble consulta de fillability (detección + ~3s después, decisión) --
     mismo patrón P24 que wallet_mirror_executor_dryrun.py.
  4. Si el precio de decisión cae en una zona `bueno_confirmado` del
     gate Y sigue fillable Y la tupla exacta está en pares_permitidos_
     live (puede_operar_live) Y pasa circuit breaker/CLV/correlación,
     ejecuta orden real vía live_trade._ejecutar_orden_polymarket.
     Fuera de zona confirmada o si CUALQUIER guardia falla: no opera,
     solo audita (misma auditoría CSV que el observador fase0, columna
     aparte para no mezclar con las filas de solo-observación).

⚠️ DRY_RUN=True por defecto -- OBLIGATORIO, mismo patrón en dos fases
que TODOS los ejecutores anteriores de este proyecto. Doble protección
real (no solo en teoría): aunque DRY_RUN pasara a False por error,
puede_operar_live() bloquea cualquier tupla que Javi no haya añadido
explícitamente a pares_permitidos_live. Cambiar DRY_RUN a False SOLO
tras: (a) unos días viendo el log en DRY_RUN confirmar que dispara
razonablemente, (b) añadir la tupla exacta a pares_permitidos_live con
nota fechada, (c) aprobación explícita de Javi.

Corre en screen propia:
  screen -dmS cand9exec bash -c "cd /root/polymarket-research && .venv/bin/python candidata9_bot_consenso_executor.py >> logs/candidata9_bot_consenso_executor.log 2>&1"
"""
import csv
import fcntl
import json
import sys
import threading
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import live_trade as lt  # noqa: E402
from live_guard import puede_operar_live  # noqa: E402
from live_stake import bloquear_por_circuit_breaker, calcular_stake  # noqa: E402
from wallet_mirror_tracker import _fillability_mirror, _market_id_y_direccion, leer_activity_incremental  # noqa: E402
from candidata9_bot_consenso_reactivo_fase0 import _cargar_bots, _gate_confirma, BOTS_PATH  # noqa: E402
from candidata9_gate_bucket import permitido_real  # noqa: E402
import ballenas_firehose_cache as _fc  # noqa: E402

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "candidata9_bot_consenso_executor.csv"
ACTIVITY_CHECKPOINT_PATH = DIR_SHADOW / "candidata9_bot_consenso_executor_activity_checkpoint.json"
VISTOS_PATH = DIR_SHADOW / "candidata9_bot_consenso_executor_vistos.json"

STRATEGY = "CANDIDATA9_BOT_CONSENSO"
N_MIN_VOTOS = 3
SEGUNDA_CONSULTA_ESPERA_S = 3.0
POLL_S = 5
RATIO_MIN = 5.0

DRY_RUN = True  # 10-Sep: REVERTIDO a los ~15min de activarlo -- vigía IC
# live disparó ic=-0.1957/-0.1985 sobre resultados.csv (n=21/15, NO trades
# reales, 0 en trades.csv) que usan py_ref=ask_dec (precio de DECISIÓN,
# ~3s después del trigger) en vez del ask de DETECCIÓN que usó el gate
# retrospectivo (candidata9_10_gate_bucket.json, n=65, positivo). Posible
# selección adversa real entre detección y decisión, sin investigar
# todavía -- pausado por precaución (CLAUDE.md: ante la duda, parar).
# Ver idea_candidata9_eth5min_alarma_ic_post_promocion_10sep. NO reactivar
# sin resolver la discrepancia.

# 08-Sep (hallazgo real, mismo bug que /code-review encontró en
# wallet_mirror_executor_dryrun.py el 06-Ago): edge_dir estimado A FAVOR
# de nuestra dirección, medido HOY con datos reales (fill-ability real,
# n=256 mercados ETH#15min[0.50,0.55): hit=60.2% ask_med=0.53 ->
# edge=+7,2pp). SIN pasar edge_dir a _ejecutar_orden_polymarket, el
# mecanismo de re-quote/abort-si-el-edge-se-evapora (_decidir_requote,
# REQUOTE_EDGE_MIN=0.02) se SALTA por completo -- la orden saldría al
# precio de detección aunque el libro se hubiera movido en contra entre
# la señal y el envío real. Constante por ahora (una sola zona
# confirmada activa) -- si el gate confirma una zona nueva con un edge
# medido distinto, medir y actualizar aquí, no asumir que 0.072 aplica
# a cualquier (activo,marco,bucket) futuro.
EDGE_DIR_ESTIMADO = 0.072

COLUMNS = [
    "timestamp_utc", "condition_id", "market_slug", "activo", "marco",
    "lado_mayoria", "n_votos_trigger", "precio_trigger",
    "ratio_deteccion", "ask_deteccion", "ratio_decision", "ask_decision",
    "degradacion_ask_pct", "sigue_fillable_en_decision", "en_zona_confirmada",
    "en_whitelist", "ejecutado", "motivo_no_ejecuta",
]

_orden_lock = threading.Lock()


def log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _vistos_cargar() -> set:
    try:
        return set(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return set()


def _vistos_guardar(vistos: set) -> None:
    VISTOS_PATH.write_text(json.dumps(list(vistos)[-50000:]), encoding="utf-8")


def _escribir_auditoria(fila: dict) -> None:
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        if nuevo:
            w.writeheader()
        w.writerow(fila)


def _disparar(activo: str, marco: str, market_slug: str, lado_mayoria: str, py: float) -> tuple[bool, str]:
    """Cadena real de guardias, mismo orden que favorito_confirmado_
    btc60min_buyno_executor.py::disparar -- este ejecutor tampoco pasa
    por live_trade.py::main(), ninguno de sus guardias se aplica gratis."""
    resuelto = _market_id_y_direccion(market_slug, lado_mayoria)
    if resuelto is None:
        return False, "no se pudo resolver market_id/direction (outcomes inesperados)"
    market_id, direction, end_date = resuelto
    subtype = f"{activo}#{marco}"
    tupla_str = f"{STRATEGY}#{subtype}#{direction}"

    ok_operar, motivo_operar = puede_operar_live(STRATEGY, subtype)
    if not ok_operar:
        return False, motivo_operar

    with _orden_lock:
        if market_id in lt._ya_operados_hoy():
            return False, f"{market_id} ya operado por otro proceso"

        if bloquear_por_circuit_breaker(lambda motivo: log(f"  circuit breaker activo ({motivo})")):
            return False, "circuit_breaker"

        config = lt._cargar_config()
        max_misma_dir = config.get("riesgo", {}).get("max_posiciones_abiertas_misma_direccion", 2)
        abiertas_dir = lt._posiciones_abiertas_misma_direccion(direction)
        if abiertas_dir >= max_misma_dir:
            return False, f"techo correlación: {abiertas_dir}>={max_misma_dir} posiciones {direction} abiertas"

        lt._CLV_CACHE = None
        clv_medio, n_clv = lt._clv_tupla(STRATEGY, subtype, direction, py=py)
        if n_clv >= lt.CLV_VETO_MIN_N and clv_medio < 0:
            return False, f"veto CLV: clv_medio={clv_medio:+.4f} (n={n_clv})"

        # Sin ic_bayes agregado fiable para esta tupla sintética recién
        # nacida (por eso existe este ejecutor -- ver docstring del
        # módulo) -- ic_conviccion mínimo no-cero solo para no chocar con
        # el techo Kelly de calcular_stake(); `stake = max(stake,
        # min_stake)` en live_stake.py YA garantiza el suelo de 1.05€
        # pedido por Javi ("empezando con stake mínimo") sin necesidad de
        # inflar esto artificialmente.
        ic_conviccion = 0.05
        precio_entrada = py if direction == "BUY_YES" else round(1.0 - py, 6)
        stake_info = calcular_stake(ic_conviccion, STRATEGY, subtype, direction=direction,
                                    precio_entrada=precio_entrada)
        if not stake_info.get("viable"):
            return False, f"stake no viable: {stake_info.get('motivo')}"

        if DRY_RUN:
            log(f"  [DRY-RUN] habría ejecutado {direction} {market_id} ({tupla_str}) py={py:.3f} "
                f"stake={stake_info['stake_eur']:.2f}€")
            return True, "dry_run_habria_ejecutado"

        resultado = lt._ejecutar_orden_polymarket(
            market_id, direction, stake_info["stake_eur"], py,
            edge_dir=EDGE_DIR_ESTIMADO, contexto={"strategy": STRATEGY, "subtype": subtype})

        if resultado.get("no_fill"):
            return False, f"no_fill: {resultado.get('error')}"

        trade = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "market_id": market_id, "question": "", "end_date": end_date,
            "strategy": STRATEGY, "subtype": subtype, "direction": direction,
            "stake_eur": stake_info["stake_eur"] if resultado["ok"] else 0.0,
            "entry_price": resultado["entry_price"],
            "signal_ask": round(py, 4), "slip_real": resultado.get("slip_real", ""),
            "ic_modelo": "", "edge_neto": "",
            "conviction_score": "", "kelly_recomendado": stake_info["stake_eur"],
            "status": "OPEN" if resultado["ok"] else "ERROR",
            "close_timestamp": "", "exit_price": "", "outcome_real": "",
            "fee_eur": resultado.get("fee_eur", 0), "pnl_bruto_eur": "", "pnl_neto_eur": "",
            "notas": (f"candidata9_bot_consenso_baja_latencia lado={lado_mayoria}"
                      if resultado.get("ok") else resultado.get("error", "")),
        }
        lt._registrar_trade(trade)
        log(f"  {'EJECUTADO' if resultado['ok'] else 'ERROR'}: {resultado}")
        if resultado["ok"]:
            lt.enviar_telegram(
                f"🎯 *Orden live ejecutada (CANDIDATA9_BOT_CONSENSO baja latencia)*\n"
                f"Estrategia: {tupla_str}\n"
                f"Precio fill: {resultado['entry_price']:.4f} (slip {resultado.get('slip_real', 0):+.4f})\n"
                f"Stake: {stake_info['stake_eur']:.2f}€\n"
                f"Bankroll operativo: {lt.bankroll_actual():.2f}€ (real al cierre de ciclo)"
            )
            return True, "ejecutado"
        lt.enviar_telegram(
            f"❌ *Orden live ERROR (CANDIDATA9_BOT_CONSENSO baja latencia)*\n"
            f"{tupla_str}\n{resultado.get('error', '')[:200]}"
        )
        return False, resultado.get("error", "error_desconocido")


def _procesar_condition(condition_id: str, votos: list[dict], vistos_trigger: set) -> None:
    if condition_id in vistos_trigger:
        return
    if len(votos) < N_MIN_VOTOS:
        return
    votos_ordenados = sorted(votos, key=lambda r: r["ts"])
    lado_final = defaultdict(int)
    for v in votos_ordenados:
        lado_final[v["lado"]] += 1
    if len(lado_final) < 2:
        return
    lado_mayoria = max(lado_final, key=lado_final.get)
    n_mayoria = lado_final[lado_mayoria]
    n_total = sum(lado_final.values())
    if n_mayoria == n_total - n_mayoria:
        return

    conteo = defaultdict(int)
    trigger = None
    for v in votos_ordenados:
        conteo[v["lado"]] += 1
        resto = sum(n for lado, n in conteo.items() if lado != lado_mayoria)
        if conteo[lado_mayoria] > resto and v["lado"] == lado_mayoria:
            trigger = v
            break
    if trigger is None:
        return

    vistos_trigger.add(condition_id)
    market_slug = trigger["market_slug"]
    activo, marco = trigger["activo"], trigger["marco"]

    fill_det = _fillability_mirror(market_slug, lado_mayoria, trigger["precio"])
    ask_det = fill_det.get("mejor_ask")
    ratio_det = fill_det.get("ratio_vs_stake") if fill_det.get("ok") else None

    time.sleep(SEGUNDA_CONSULTA_ESPERA_S)
    fill_dec = _fillability_mirror(market_slug, lado_mayoria, trigger["precio"], fill_det.get("token_id"))
    ask_dec = fill_dec.get("mejor_ask")
    ratio_dec = fill_dec.get("ratio_vs_stake") if fill_dec.get("ok") else None

    degradacion = None
    if ask_det is not None and ask_dec is not None and ask_det > 0:
        degradacion = round((ask_dec - ask_det) / ask_det * 100, 2)

    sigue_fillable = bool(ratio_dec is not None and ratio_dec >= RATIO_MIN)
    if ask_dec is not None:
        py_ref = ask_dec
    elif ask_det is not None:
        py_ref = ask_det
    else:
        try:
            py_ref = float(trigger["precio"])
        except (TypeError, ValueError):
            py_ref = None
    en_zona = bool(py_ref is not None and _gate_confirma(activo, marco, py_ref))
    subtype = f"{activo}#{marco}"
    en_whitelist = puede_operar_live(STRATEGY, subtype)[0]
    # 10-Sep: capa adicional de aprobación explícita por micro-bucket,
    # igual que bot_wallets_gate_bucket.py -- `en_zona` (arriba) sigue sin
    # restringir, para que en_zona_confirmada siga auditando TODO el
    # universo en el CSV (decisión Javi 26-Ago). Disparar de verdad exige
    # además que el bucket exacto esté en BUCKETS_APROBADOS_REAL.
    aprobado_real = bool(py_ref is not None and permitido_real(activo, marco, py_ref))

    ejecutado = False
    motivo = "fuera_de_zona_confirmada"
    if not en_zona:
        motivo = "fuera_de_zona_confirmada"
    elif not aprobado_real:
        motivo = "bucket_no_aprobado_para_real"
    elif not sigue_fillable:
        motivo = "no_fillable_en_decision"
    elif not en_whitelist:
        motivo = "tupla_no_en_pares_permitidos_live"
    else:
        ejecutado, motivo = _disparar(activo, marco, market_slug, lado_mayoria, py_ref)

    log(f"[{condition_id}] {activo}#{marco} TRIGGER lado={lado_mayoria} n_votos={n_mayoria}/{n_total} "
        f"ask_det={ask_det} -> ask_dec={ask_dec} degradacion={degradacion}% "
        f"zona_confirmada={en_zona} whitelist={en_whitelist} ejecutado={ejecutado} motivo={motivo}")

    _escribir_auditoria({
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "condition_id": condition_id, "market_slug": market_slug,
        "activo": activo, "marco": marco,
        "lado_mayoria": lado_mayoria, "n_votos_trigger": n_mayoria, "precio_trigger": trigger["precio"],
        "ratio_deteccion": ratio_det, "ask_deteccion": ask_det,
        "ratio_decision": ratio_dec, "ask_decision": ask_dec,
        "degradacion_ask_pct": degradacion, "sigue_fillable_en_decision": int(sigue_fillable),
        "en_zona_confirmada": int(en_zona), "en_whitelist": int(en_whitelist),
        "ejecutado": int(ejecutado), "motivo_no_ejecuta": motivo,
    })


def main() -> None:
    bots = _cargar_bots()
    if not bots:
        log(f"⚠️ sin wallets en {BOTS_PATH} -- nada que vigilar")
        return
    log(f"arrancado (DRY_RUN={DRY_RUN}) -- {len(bots)} bot wallets, vigilando TODOS los activos/marcos")
    _fc.iniciar()
    time.sleep(3)
    if not DRY_RUN:
        _ = lt._get_clob_client()
        log("ClobClient precalentado")

    vistos = _vistos_cargar()
    vistos_trigger = set()
    votos_por_condition: dict[str, list[dict]] = defaultdict(list)

    for row in leer_activity_incremental(ACTIVITY_CHECKPOINT_PATH):
        if (row.get("side") or "").strip().upper() != "BUY":
            continue
        w = (row.get("wallet") or "").lower()
        if w not in bots:
            continue
        vistos.add(f"{w}|{row.get('market_slug','')}")
    _vistos_guardar(vistos)
    log(f"backlog marcado como visto ({len(vistos)} matches históricos)")

    while True:
        try:
            for row in leer_activity_incremental(ACTIVITY_CHECKPOINT_PATH):
                if (row.get("side") or "").strip().upper() != "BUY":
                    continue
                w = (row.get("wallet") or "").lower()
                if w not in bots:
                    continue
                market_slug = row.get("market_slug", "")
                dedup_key = f"{w}|{market_slug}"
                if dedup_key in vistos:
                    continue
                vistos.add(dedup_key)
                activo, marco = row.get("activo", ""), row.get("marco", "")
                if not activo or not marco:
                    continue
                try:
                    precio = float(row.get("price") or 0)
                except (TypeError, ValueError):
                    continue
                if not (0.0 < precio < 1.0):
                    continue
                condition_id = row.get("condition_id", "")
                if not condition_id:
                    continue
                votos_por_condition[condition_id].append({
                    "ts": row.get("timestamp_utc", ""), "lado": row.get("outcome", ""),
                    "precio": row.get("price", ""), "market_slug": market_slug,
                    "activo": activo, "marco": marco,
                })
            _vistos_guardar(vistos)

            for condition_id, votos in list(votos_por_condition.items()):
                if condition_id in vistos_trigger:
                    continue
                _procesar_condition(condition_id, votos, vistos_trigger)

            if len(votos_por_condition) > 2000:
                for cid in list(vistos_trigger)[:1000]:
                    votos_por_condition.pop(cid, None)

            if not _fc.esta_sano():
                log("⚠️ cache de firehose no sano -- señales de fillability no confiables este ciclo")

        except Exception as e:
            log(f"error en ciclo: {e} -- reintenta en {POLL_S}s")
        time.sleep(POLL_S)


if __name__ == "__main__":
    main()
