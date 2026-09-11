#!/usr/bin/env python3
"""
bot_wallets_gate_bucket_fase0.py -- P-GALLINA FASE 0, 25-Ago (petición
explícita Javi: "constrúyelo ahora, FASE 0, solo lectura").

Continuación de la Candidata 11 (gallina de los huevos de oro,
idea_gallina_huevos_oro_candidatas_25ago): el cruce retroactivo
(wallet_edge_score_por_activo_marco.json + ballenas_timing_history.csv,
desagregado por arquetipo×activo×marco×micro-bucket) encontró 58 celdas
con n>=100 y g_kelly>0 -- pero eso mide EDGE, no FILL-ABILITY (el precio
histórico de la wallet no es una consulta de libro real, mismo error ya
cazado y corregido en Wallet Mirror el 10-Ago,
project_p24_wallet_mirror_refutado_ask_real_10ago). Este observador
cierra ese hueco EXACTAMENTE como wallet_mirror_executor_dryrun.py
(P24 FASE1) lo hizo para Wallet Mirror: cuando detecta a una de las bot
wallets (bot_wallets_universo_25ago.json) operar en tiempo real vía el
firehose de trades (polyactivity), consulta el libro PÚBLICO real en ese
instante y registra la profundidad -- sin eso, cualquier veredicto de
fill-ability sobre estas celdas sería inventado.

Reusa (import directo, sin duplicar) `_archivos_activity()` (lee el
firehose ya escrito por fetch_polymarket_activity_ws.py) y
`_fillability_mirror()` (consulta pública de libro, mismo criterio de
stake de referencia) de wallet_mirror_tracker.py -- mismo patrón de
detección que ya usa wallet_mirror_sniper.py.

NO coloca, cancela ni modifica ninguna orden real -- puramente
observacional. NO usa la clasificación de arquetipo persistida (no
existe todavía como fichero propio) -- clasifica sobre la marcha con la
MISMA lógica que analisis_bot_arquetipos_25ago.py (marco dominante +
restante_min mediana), recalculada una vez al arrancar desde
ballenas_timing_history.csv.
"""
import csv
import json
import fcntl
import math
import sys
import threading
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from wallet_mirror_tracker import (  # noqa: E402
    _archivos_activity, _fillability_mirror, outcome_por_slug,
    leer_activity_incremental,
)

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "bot_wallets_gate_bucket_fase0.csv"
OUT_LOCK = DIR_SHADOW / "bot_wallets_gate_bucket_fase0.csv.lock"
VISTOS_PATH = DIR_SHADOW / "bot_wallets_gate_bucket_fase0_vistos.json"
ACTIVITY_CHECKPOINT_PATH = DIR_SHADOW / "bot_wallets_gate_bucket_fase0_activity_checkpoint.json"
MAX_SLUGS_POR_CICLO = 150  # mismo cap que wallet_mirror_tracker.py::resolver_pendientes
BOTS_PATH = DIR_SHADOW / "bot_wallets_universo_25ago.json"
HIST = DIR_SHADOW / "ballenas_timing_history.csv"

POLL_S = 15
STEP_BUCKET = 0.05
UMBRAL_SNIPER_MIN = 5.0
# 10-Sep (hallazgo real, feedback_gate_debe_usar_precio_decision_no_
# deteccion_10sep): este fichero era la fuente de TODOS los gates de la
# familia (SNIPER/DISPERSO/WEEKLY_*/CANDIDATA9/CANDIDATA10) y solo
# capturaba el ask en el instante de DETECCIÓN -- ningún gate podía saber
# si ese precio seguía siendo real 3s después, cuando el ejecutor de
# verdad dispara. Confirmado con datos reales el mismo día: CANDIDATA9#
# ETH#5min[0.30,0.35) tenía gate retrospectivo positivo (n=65, +0,645€,
# ask de detección) pero el subconjunto que de verdad sobrevive hasta la
# decisión daba n=16, -0,255€ -- sesgo optimista real, no ruido. Mismo
# patrón de re-quote/segunda consulta que ya usan candidata9_bot_
# consenso_reactivo_fase0.py y los ejecutores reales (wallet_mirror_
# executor_dryrun.py, dispersed_bot_executor_dryrun.py) -- aquí se lleva
# a la CAPTURA de origen para que TODOS los generadores de gate puedan
# usarlo, en vez de mitigar bucket a bucket aguas abajo.
SEGUNDA_CONSULTA_ESPERA_S = 3.0  # mismo valor que candidata9_bot_consenso_reactivo_fase0.py
RATIO_MIN = 5.0  # mismo umbral que el resto del proyecto (fillable de verdad)

COLUMNS = [
    "timestamp_utc", "trade_timestamp", "wallet", "arquetipo", "activo", "marco",
    "bucket_precio", "condition_id", "market_slug", "lado_wallet", "precio_wallet",
    "usd_trade", "ratio_vs_stake_deteccion", "mejor_ask_deteccion", "profundidad_eur_deteccion",
    "mejor_ask_decision", "ratio_vs_stake_decision", "profundidad_eur_decision",
    "degradacion_ask_pct", "sigue_fillable_decision",
    "outcome_real", "acierto", "resolved_ts",
]


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _bucket(p: float) -> float:
    return round(math.floor(p / STEP_BUCKET + 1e-9) * STEP_BUCKET, 4)


def clasificar_arquetipos(wallets: set) -> dict:
    """MISMA lógica que analisis_bot_arquetipos_25ago.py::clasificar_wallets()
    -- recalculada aquí en vez de importada porque ese script es de un solo
    disparo (main() con prints), no un módulo de librería reutilizable."""
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


def _migrar_cabecera_si_hace_falta() -> None:
    """10-Sep: el fichero ya existía en producción con la cabecera VIEJA
    (17 columnas, sin las de decisión nuevas) -- sin esto, las filas
    nuevas (22 columnas) quedarían desalineadas para cualquier
    csv.DictReader futuro (usa la primera línea del fichero como nombres
    de columna, no la constante COLUMNS de este módulo). Reescribe el
    fichero entero UNA vez, bajo el mismo lock que resolver_pendientes()/
    _guardar() -- filas viejas quedan con las columnas nuevas vacías
    (mismo comportamiento que csv.DictWriter con un campo ausente),
    ningún dato se pierde. No-op si el fichero no existe o ya tiene la
    cabecera actual."""
    if not OUT.exists():
        return
    with open(OUT, newline="", encoding="utf-8") as f:
        primera_linea = f.readline().rstrip()
    if primera_linea == ",".join(COLUMNS):
        return  # ya migrado
    lock_f = open(OUT_LOCK, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        try:
            with open(OUT, newline="", encoding="utf-8") as f:
                primera_linea = f.readline().rstrip()
            if primera_linea == ",".join(COLUMNS):
                return  # otro proceso ya migró mientras esperábamos el lock
            with open(OUT, newline="", encoding="utf-8") as f:
                filas = list(csv.DictReader(f))
            with open(OUT, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=COLUMNS)
                w.writeheader()
                w.writerows(filas)
            _log(f"cabecera migrada a schema con precio de decisión ({len(filas)} filas preservadas)")
        finally:
            fcntl.flock(lock_f, fcntl.LOCK_UN)
    finally:
        lock_f.close()


def _vistos_cargar() -> set:
    try:
        return set(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return set()


def _vistos_guardar(vistos: set) -> None:
    VISTOS_PATH.write_text(json.dumps(list(vistos)[-50000:]), encoding="utf-8")


def _guardar(filas: list) -> None:
    """10-Sep: con la segunda consulta en hilos aparte (ver
    _completar_decision_en_hilo), varias filas pueden escribirse casi a
    la vez desde hilos distintos -- se bloquea con OUT_LOCK (mismo
    fichero que ya usa resolver_pendientes() para su reescritura) para
    que dos apends concurrentes nunca se entrelacen."""
    if not filas:
        return
    lock_f = open(OUT_LOCK, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        try:
            nuevo = not OUT.exists()
            with open(OUT, "a", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                if nuevo:
                    w.writerow(COLUMNS)
                for fila in filas:
                    w.writerow([fila.get(c, "") for c in COLUMNS])
        finally:
            fcntl.flock(lock_f, fcntl.LOCK_UN)
    finally:
        lock_f.close()


def _seed_vistos_sin_consultar(wallets: set) -> set:
    """25-Ago (fix real, encontrado en el propio despliegue -- el primer
    arranque se quedó procesando ~2 días de backlog del firehose CON una
    consulta de red (_fillability_mirror -> gamma-api) POR CADA evento
    histórico, la inmensa mayoría mercados ya cerrados donde la consulta
    tarda en fallar en vez de fallar rápido -- podía tardar horas y quemar
    CPU/red para nada, mismo patrón de incidente que el fetch_polymarket_
    activity_ws.py del 22-Ago). Al arrancar, se marcan como "vistos" todos
    los matches YA existentes en el firehose SIN consultar profundidad --
    solo se mide profundidad real para eventos que lleguen A PARTIR de
    ahora, que es lo único que tiene sentido medir (el propósito es
    fill-ability EN EL INSTANTE DE DETECCIÓN, no reconstruir el pasado)."""
    vistos = _vistos_cargar()
    nuevos = 0
    # 07-Sep: checkpoint incremental (ver leer_activity_incremental() en
    # wallet_mirror_tracker.py) -- este backlog corría en CADA restart del
    # hilo (dentro de observadores_fase0.py, que se reinicia con cierta
    # frecuencia por el watchdog), releyendo el firehose completo
    # (~1,5GB/4M filas) cada vez. Con checkpoint persistido, un restart
    # solo relee lo escrito desde el último checkpoint de este consumidor.
    for row in leer_activity_incremental(ACTIVITY_CHECKPOINT_PATH):
        if (row.get("side") or "").strip().upper() != "BUY":
            continue
        w = (row.get("wallet") or "").lower()
        if w not in wallets:
            continue
        dedup_key = f"{w}|{row.get('market_slug','')}"
        if dedup_key not in vistos:
            vistos.add(dedup_key)
            nuevos += 1
    _log(f"backlog existente marcado como visto sin consultar profundidad: {nuevos} matches")
    return vistos


def _completar_decision_en_hilo(fila: dict, market_slug: str, lado: str,
                                 precio_wallet: str, token_id: str | None) -> None:
    """Corre en un hilo aparte (daemon, no bloquea el bucle principal):
    espera SEGUNDA_CONSULTA_ESPERA_S y repite la consulta de libro, con
    el mismo token_id ya resuelto (evita una 2ª ida a gamma-api, mismo
    ahorro medido y documentado en wallet_mirror_tracker.py::
    _fillability_mirror). Solo entonces se escribe la fila -- nunca hay
    una fila a medias en el CSV. Si el proceso muere durante la espera
    (restart), esta fila concreta se pierde en silencio -- mismo riesgo
    ya aceptado en candidata9_bot_consenso_reactivo_fase0.py para su
    propio sleep(SEGUNDA_CONSULTA_ESPERA_S)."""
    time.sleep(SEGUNDA_CONSULTA_ESPERA_S)
    try:
        fill_dec = _fillability_mirror(market_slug, lado, precio_wallet, token_id)
    except Exception as e:
        _log(f"🚨 error en 2ª consulta ({fila.get('wallet','?')[:10]}..): {type(e).__name__}: {e}")
        fill_dec = {"ok": False}

    ask_det_raw = fila.get("mejor_ask_deteccion")
    ask_dec = fill_dec.get("mejor_ask") if fill_dec.get("ok") else None
    ratio_dec = fill_dec.get("ratio_vs_stake") if fill_dec.get("ok") else None
    degradacion = None
    try:
        ask_det = float(ask_det_raw) if ask_det_raw not in (None, "") else None
    except (TypeError, ValueError):
        ask_det = None
    if ask_det is not None and ask_dec is not None and ask_det > 0:
        degradacion = round((ask_dec - ask_det) / ask_det * 100, 2)

    fila["mejor_ask_decision"] = ask_dec if ask_dec is not None else ""
    fila["ratio_vs_stake_decision"] = ratio_dec if ratio_dec is not None else ""
    fila["profundidad_eur_decision"] = fill_dec.get("profundidad_eur", "") if fill_dec.get("ok") else ""
    fila["degradacion_ask_pct"] = degradacion if degradacion is not None else ""
    fila["sigue_fillable_decision"] = "1" if (ratio_dec is not None and ratio_dec >= RATIO_MIN) else "0"
    _guardar([fila])


def _procesar_fila(row: dict, wallets: set, arquetipos: dict, vistos: set) -> None:
    """10-Sep: ya NO devuelve la fila para que el llamante la acumule y
    escriba en batch -- lanza un hilo que espera la 2ª consulta y escribe
    la fila completa (detección + decisión) él mismo. El marcado en
    `vistos` sigue siendo inmediato (aquí, no en el hilo) para que un
    evento nunca se procese dos veces aunque lleguen ráfagas."""
    if (row.get("side") or "").strip().upper() != "BUY":
        return
    w = (row.get("wallet") or "").lower()
    if w not in wallets:
        return
    dedup_key = f"{w}|{row.get('market_slug','')}"
    if dedup_key in vistos:
        return
    vistos.add(dedup_key)
    try:
        precio = float(row.get("price") or 0)
    except (TypeError, ValueError):
        return
    if not (0.0 < precio < 1.0):
        return
    lado = row.get("outcome", "")  # "Up"/"Down"
    market_slug = row.get("market_slug", "")
    fill = _fillability_mirror(market_slug, lado, row.get("price", ""))
    try:
        usd_trade = float(row.get("usd_value") or 0)
    except (TypeError, ValueError):
        usd_trade = 0.0
    fila = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "trade_timestamp": row.get("timestamp_utc", ""),
        "wallet": w, "arquetipo": arquetipos.get(w, "?"),
        "activo": row.get("activo", ""), "marco": row.get("marco", ""),
        "bucket_precio": f"{_bucket(precio):.2f}",
        "condition_id": row.get("condition_id", ""),
        "market_slug": market_slug,
        "lado_wallet": lado, "precio_wallet": row.get("price", ""),
        "usd_trade": usd_trade,
        "ratio_vs_stake_deteccion": fill.get("ratio_vs_stake", "") if fill.get("ok") else "",
        "mejor_ask_deteccion": fill.get("mejor_ask", "") if fill.get("ok") else "",
        "profundidad_eur_deteccion": fill.get("profundidad_eur", "") if fill.get("ok") else "",
    }
    _log(f"[{fila['arquetipo']}] {fila['activo']}#{fila['marco']}"
         f"[{fila['bucket_precio']}) wallet={w[:10]}.. "
         f"ratio_deteccion={fila['ratio_vs_stake_deteccion']} -- 2ª consulta en {SEGUNDA_CONSULTA_ESPERA_S}s")
    threading.Thread(
        target=_completar_decision_en_hilo,
        args=(fila, market_slug, lado, row.get("price", ""), fill.get("token_id")),
        daemon=True,
    ).start()


def resolver_pendientes() -> int:
    """25-Ago (P-GALLINA FASE0, cierre del hueco de instrumentación pedido
    por Javi): reusa `outcome_por_slug()` de wallet_mirror_tracker.py
    (misma fuente, mismo criterio de mercado ya resuelto vía gamma-api) --
    sin esto, `bot_wallets_gate_bucket_fase0.csv` medía fill-ability pero
    nunca PnL real, porque nadie comparaba `lado_wallet` contra el
    resultado oficial del mercado. Mismo patrón exacto que `wallet_mirror_
    sniper.py::resolver_pendientes` (reexportado de wallet_mirror_
    tracker.py) -- leer sin lock, resolver red sin lock, lock solo para
    el tramo final de escritura (releer fresco por si el observador live
    añadió filas mientras tanto)."""
    if not OUT.exists():
        return 0
    with open(OUT, newline="", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))

    slugs_pendientes = sorted({r["market_slug"] for r in filas
                                if not r.get("outcome_real") and r.get("market_slug")})
    outcomes_por_slug = {}
    for slug in slugs_pendientes[:MAX_SLUGS_POR_CICLO]:
        outcome = outcome_por_slug(slug)
        if outcome is not None:
            outcomes_por_slug[slug] = outcome

    if not outcomes_por_slug:
        return 0

    lock_f = open(OUT_LOCK, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        try:
            with open(OUT, newline="", encoding="utf-8") as f:
                filas = list(csv.DictReader(f))
            resueltas = 0
            for r in filas:
                if r.get("outcome_real"):
                    continue
                outcome = outcomes_por_slug.get(r.get("market_slug"))
                if outcome is None:
                    continue
                r["outcome_real"] = outcome
                r["acierto"] = "1" if outcome == r.get("lado_wallet") else "0"
                r["resolved_ts"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
                resueltas += 1
            if resueltas:
                with open(OUT, "w", newline="", encoding="utf-8") as f:
                    w = csv.DictWriter(f, fieldnames=COLUMNS)
                    w.writeheader()
                    w.writerows(filas)
            return resueltas
        finally:
            fcntl.flock(lock_f, fcntl.LOCK_UN)
    finally:
        lock_f.close()


def main() -> None:
    _migrar_cabecera_si_hace_falta()
    bots = json.loads(BOTS_PATH.read_text(encoding="utf-8"))
    wallets = set(bots.keys())
    arquetipos = clasificar_arquetipos(wallets)
    _log(f"bot_wallets_gate_bucket_fase0 arrancado -- {len(wallets)} bot wallets, "
         f"{len(arquetipos)} clasificadas por arquetipo")

    vistos = _seed_vistos_sin_consultar(wallets)
    _vistos_guardar(vistos)

    # 25-Ago: trackear posición de lectura evita releer el firehose entero
    # en CADA ciclo. 07-Sep (/code-review): pero esa posición vivía solo en
    # memoria -- en cada RESTART de este hilo (dentro de observadores_
    # fase0.py, que se reinicia con frecuencia por el watchdog) volvía a
    # arrancar desde justo tras la cabecera, releyendo el fichero completo
    # una vez más. Usar leer_activity_incremental() (mismo checkpoint
    # persistido que ya usa el seed de arriba) elimina también ese coste:
    # un restart solo relee lo escrito desde el último checkpoint, nunca
    # el fichero entero.
    while True:
        try:
            hubo_matches = False
            for row in leer_activity_incremental(ACTIVITY_CHECKPOINT_PATH):
                # 10-Sep: _procesar_fila ya no devuelve la fila -- lanza su
                # propio hilo para la 2ª consulta y se guarda sola (ver
                # _completar_decision_en_hilo). Aquí solo se marca que hubo
                # actividad para persistir `vistos` este ciclo.
                antes = len(vistos)
                _procesar_fila(row, wallets, arquetipos, vistos)
                if len(vistos) != antes:
                    hubo_matches = True
            if hubo_matches:
                _vistos_guardar(vistos)
        except Exception as e:
            _log(f"🚨 error en ciclo: {type(e).__name__}: {e}")
        time.sleep(POLL_S)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--resolver":
        _migrar_cabecera_si_hace_falta()
        n = resolver_pendientes()
        _log(f"resueltas: {n}")
    else:
        main()
