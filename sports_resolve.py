#!/usr/bin/env python3
"""
sports_resolve.py — resuelve trades reales OPEN de data/sports/trades.csv
(contraparte de shadow_resolve.py en cripto, pero para el ledger de
dinero real de sports).

27-Ago noche (petición explícita Javi: "construye lo que falte de sports
para tenerlo ya hecho cuando toque operar en directo"): hallazgo real
-- `sports_wallet_mirror_sniper.py` podía enviar una orden real (DRY_RUN=
False) y registrarla como OPEN, pero NADA la cerraba nunca. Sin este
script, `sports_live_stake.bankroll_actual()` (suma depósitos + PnL de
trades CLOSED) se quedaría ciego a cualquier posición abierta para
siempre, y los circuit breakers (`pnl_hoy()`) nunca verían una pérdida
real. Mismo patrón que shadow_resolve.py (cripto) simplificado al
mínimo necesario -- sin Kelly/IC/aprendizaje causal, sports no tiene
ese pipeline todavía.

Reusa `outcome_por_condition_id()` de sports_wallet_mirror_sniper.py (ya
prueba en producción para resolver el CSV observacional) -- una sola
fuente de verdad para "¿cómo resolvió este condition_id?".

FEE=0.05 (sports_fees_v3, verificado 26-Ago contra gamma-api con
condition_ids reales -- NO 0.07 como cripto, ver
project_sports_wallet_mirror_gate_bucket_paridad_26ago).

Uso:
  python3 sports_resolve.py            # una pasada
  python3 sports_resolve.py --loop 60  # bucle cada 60s (uso en cron/screen)
"""
import argparse
import asyncio
import csv
import fcntl
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from sports_wallet_mirror_sniper import outcome_por_condition_id  # noqa: E402
from sports_smart_exit_logger import fetch as _fetch_mkt, outcome_prices as _outcome_prices, parse_dt as _parse_dt  # noqa: E402
from shadow_digest import enviar_telegram  # noqa: E402 -- bot="sports", solo para el aviso de discrepancia de abajo

TRADES = REPO / "data/sports/trades.csv"
LOCK_PATH = REPO / "data/sports/.trades_lock"
CONFIG_PATH = REPO / "data/sports/config_live_sports.json"
FEE = 0.05
MAX_CIDS_POR_CICLO = 20
HAIRCUT_VENTA = 0.06  # mismo valor que cripto (analisis_smart_exit.py) -- ~2-3c de spread + fee de venta, provisional hasta calibrar con datos propios de sports


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _leer_bajo_lock() -> list[dict]:
    lock_f = open(LOCK_PATH, "w")
    fcntl.flock(lock_f, fcntl.LOCK_EX)
    try:
        with open(TRADES, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    finally:
        fcntl.flock(lock_f, fcntl.LOCK_UN)


def resolver_una_pasada() -> int:
    """Dos lecturas a propósito -- ver hallazgo real 27-Ago noche
    (/code-review post-construcción, petición Javi "revisa que todo esté
    perfecto"): la 1ª lectura decide QUÉ condition_ids consultar (red,
    puede tardar varios segundos -- 20 cids * hasta 15s timeout cada
    uno); si se escribiera de vuelta el resultado sobre esa MISMA lista
    en memoria, cualquier trade real registrado por
    sports_wallet_mirror_sniper.py DURANTE la consulta de red se
    perdería al sobrescribir el fichero entero con datos ya obsoletos
    (TOCTOU clásico). La 2ª lectura (bajo el mismo lock que la escritura,
    justo antes de escribir) es SIEMPRE la fuente de verdad para qué
    filas existen -- los outcomes ya resueltos solo se aplican encima."""
    if not TRADES.exists():
        return 0

    filas_iniciales = _leer_bajo_lock()
    if not filas_iniciales:
        return 0

    abiertas = [r for r in filas_iniciales if r.get("status") == "OPEN"]
    if not abiertas:
        return 0

    cids = sorted({r["market_id"] for r in abiertas if r.get("market_id")})[:MAX_CIDS_POR_CICLO]

    # Consulta de red (lenta) -- SIN mantener el lock, para no bloquear
    # registrar_trade() más de lo necesario.
    outcomes: dict[str, int] = {}
    for cid in cids:
        idx = outcome_por_condition_id(cid)
        if idx is not None:
            outcomes[cid] = idx
    if not outcomes:
        return 0

    lock_f = open(LOCK_PATH, "w")
    fcntl.flock(lock_f, fcntl.LOCK_EX)
    try:
        with open(TRADES, newline="", encoding="utf-8") as f:
            filas = list(csv.DictReader(f))  # relectura fresca, fuente de verdad real
        if not filas:
            return 0
        fieldnames = list(filas[0].keys())

        n_resueltas = 0
        for r in filas:
            if r.get("status") != "OPEN":
                continue
            idx_real = outcomes.get(r.get("market_id"))
            if idx_real is None:
                continue
            try:
                direction_idx = int(r.get("direction", ""))
                entry_price = float(r.get("entry_price", ""))
                stake_eur = float(r.get("stake_eur", ""))
                fee_eur = float(r.get("fee_eur", "") or 0.0)
            except (TypeError, ValueError):
                _log(f"  ⚠️ fila con datos incompletos para {r.get('market_id')}, no se resuelve")
                continue

            acierto = int(idx_real == direction_idx)
            if acierto:
                gross_win = (1.0 - entry_price) / entry_price if entry_price > 0 else 0.0
                pnl_bruto = gross_win * stake_eur
            else:
                pnl_bruto = -stake_eur
            pnl_neto = pnl_bruto - fee_eur

            r["status"] = "CLOSED"
            r["close_timestamp"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            r["exit_price"] = "1.0" if acierto else "0.0"
            r["outcome_real"] = str(idx_real)
            r["pnl_bruto_eur"] = round(pnl_bruto, 4)
            r["pnl_neto_eur"] = round(pnl_neto, 4)
            n_resueltas += 1
            _log(f"  ✅ resuelto {r['market_id']} categoria={r.get('categoria')} tipo={r.get('tipo')} "
                 f"acierto={acierto} pnl_neto={pnl_neto:+.3f}€")

        if n_resueltas:
            with open(TRADES, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=fieldnames)
                w.writeheader()
                w.writerows(filas)
        return n_resueltas
    finally:
        fcntl.flock(lock_f, fcntl.LOCK_UN)


def _cargar_config_smart_exit() -> dict:
    """Bloque `smart_exit` de config_live_sports.json, activo=False por
    defecto (fail-closed) hasta que haya datos propios de sports para
    calibrar (ver sports_smart_exit_logger.py, arrancado hoy -- sin
    histórico todavía, ningún umbral aquí está validado con datos reales
    de sports, son un punto de partida estructural igual al de cripto,
    NUNCA una copia de sus valores 0.45€/0.30€ sin recalibrar)."""
    try:
        cfg = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {"activo": False}
    return cfg.get("smart_exit", {"activo": False})


def check_salidas_tempranas() -> int:
    """16-Sep (petición explícita Javi: "el trade que va a ganar se queda,
    el que va a perder se vende intentando sacarle beneficio. La idea es
    ganar pasta por encima del precio de entrada del trade y no perder
    nada"). Mismo patrón EXACTO que shadow_resolve.py::_check_salidas_
    tempranas_bajo_lock (cripto): TP comprobado ANTES que SL (empate =
    gana TP), corte por tiempo restante para TP (tocar el umbral con poco
    tiempo restante es casi siempre un ganador ya decidido -- dejar
    correr; con tiempo de sobra revierte con frecuencia -- vender
    protege, mismo hallazgo que idea_smart_exit_longshot_tiempo_
    confirmado_16sep mostró en cripto HOY, sin verificar todavía si
    aplica igual en sports).

    Gate maestro `activo` en config_live_sports.json::smart_exit --
    False por defecto (fail-closed), igual que take_profit_activo/
    smart_exit_stop_loss.activo en cripto hasta aprobación explícita.
    Mientras esté en False esta función es INERTE: no vende nada, solo
    sirve para que el mecanismo exista, compile y esté listo para
    activarse en cuanto sports_smart_exit_prices.csv acumule suficiente
    n para calibrar TP/SL/corte con rigor (mismo proceso que
    analisis_smart_exit.py hizo en cripto)."""
    cfg = _cargar_config_smart_exit()
    if cfg.get("activo") is not True:
        return 0

    sl_umbral_eur = float(cfg.get("sl_umbral_perdida_eur", 0.30))
    tp_umbral_precio = float(cfg.get("tp_umbral_precio", 0.85))
    tp_corte_seg = float(cfg.get("tp_corte_tiempo_seg", 60.0))
    longshot_entry_max = float(cfg.get("longshot_entry_price_max", 0.53))

    filas_iniciales = _leer_bajo_lock()
    abiertas = [r for r in filas_iniciales if r.get("status") == "OPEN" and r.get("market_id")]
    if not abiertas:
        return 0

    import sports_live_trade as _slt

    # /code-review 16-Sep (hallazgo real): un fetch de gamma-api SECUENCIAL
    # por posición OPEN reintroducía en sports la misma ineficiencia ya
    # cazada y arreglada en cripto (shadow_resolve.py, 18-Jul,
    # fetch_mercados_paralelo()) -- con varias posiciones OPEN a la vez,
    # cada una con hasta 3 reintentos/backoff en 429, retrasa el resto del
    # ciclo (y con él, la propia protección TP/SL). Prefetch en paralelo
    # por market_id ÚNICO (una misma posición OPEN puede repetirse si hay
    # 2 direcciones del mismo mercado).
    market_ids_unicos = sorted({t["market_id"] for t in abiertas})
    mercados: dict[str, dict] = {}
    if market_ids_unicos:
        with ThreadPoolExecutor(max_workers=min(8, len(market_ids_unicos))) as ex:
            futuros = {ex.submit(_fetch_mkt, mid): mid for mid in market_ids_unicos}
            for fut in as_completed(futuros):
                mid = futuros[fut]
                try:
                    m = fut.result()
                except Exception:
                    m = None
                if m:
                    mercados[mid] = m

    ahora = datetime.now(timezone.utc)
    n_vendidas = 0
    for t in abiertas:
        try:
            entry_price = float(t.get("entry_price") or 0)
            stake_eur = float(t.get("stake_eur") or 0)
            direction = int(t.get("direction", ""))
        except (ValueError, TypeError):
            continue
        if entry_price <= 0 or stake_eur <= 0 or direction not in (0, 1):
            continue

        mkt = mercados.get(t["market_id"])
        if not mkt:
            continue  # fail-closed: sin dato de mercado, no se evalúa esta posición
        op = _outcome_prices(mkt)
        if not op:
            continue
        p_lado = op[direction]

        shares = stake_eur / entry_price
        valor_ajustado = shares * p_lado * (1.0 - HAIRCUT_VENTA)
        pnl_ajustado = valor_ajustado - stake_eur

        # /code-review 16-Sep (hallazgo real): preferir el endDate FRESCO
        # del mercado ya consultado (mkt) sobre el guardado en trades.csv
        # al abrir la posición -- ese puede quedar obsoleto si Polymarket
        # actualiza endDate después (retraso, prórroga, aplazamiento).
        # Mismo criterio que shadow_resolve.py (cripto): `mercado.get(
        # "endDate") or t.get("end_date", "")`.
        te = _parse_dt(mkt.get("endDate") or t.get("end_date"))
        seg_restante = (te - ahora).total_seconds() if te else None

        # /code-review 16-Sep (hallazgo real): sin este margen de gracia,
        # una posición cuyo end_date ya pasó (seg_restante NEGATIVO) caía
        # directa al `else: motivo="take_profit"` de abajo -- justo lo
        # contrario de "dejar correr", vendiendo de inmediato (peor precio
        # + fee taker) una posición que la resolución normal
        # (resolver_una_pasada(), MISMO ciclo, se llama justo antes) está a
        # punto de cerrar a valor completo sola. Mismo mecanismo que
        # GRACIA_RESOLUCION_NORMAL_SEGUNDOS en shadow_resolve.py (cripto,
        # 300s) -- aquí 120s (ciclo de sports_resolve.py cada 60s, dos
        # vueltas de margen es de sobra). Pasado el margen sin resolver,
        # sports_resolve.py::resolver_una_pasada() ya lo habría intentado
        # 2 veces y no lo consiguió -- ahí sí se retoma la protección
        # (seg_restante muy negativo no exime del chequeo, al revés que
        # dentro del margen).
        if seg_restante is not None and -120.0 <= seg_restante < 0:
            continue

        # /code-review 16-Sep (hallazgo real): el corte de tiempo (dejar
        # correr si toca TP con poco tiempo restante) en cripto SOLO se
        # valida para la rama LONGSHOT (entry_price barata) -- aplicarlo a
        # CUALQUIER entrada, incluida una cara, generalizaba sin datos que
        # lo respalden. Mismo criterio que shadow_resolve.py: es_longshot
        # exige entry_price<longshot_entry_max.
        es_longshot = entry_price < longshot_entry_max
        motivo = None
        if p_lado >= tp_umbral_precio:
            # Corte por tiempo -- ver docstring, SOLO longshot. seg_restante
            # >=0 exige que el mercado siga vivo Y fuera del margen de
            # gracia de arriba.
            if es_longshot and seg_restante is not None and 0 <= seg_restante < tp_corte_seg:
                pass  # gana casi seguro y falta poco -- dejar correr
            else:
                motivo = "take_profit"
        if motivo is None and pnl_ajustado <= -sl_umbral_eur:
            motivo = "stop_loss"
        if motivo is None:
            continue

        resultado = _slt.ejecutar_venta_temprana(
            t["market_id"], direction, entry_price, stake_eur,
            contexto={"categoria": t.get("categoria", ""), "tipo": t.get("tipo", "")})
        if not resultado.get("ok"):
            continue

        # /code-review 16-Sep (hallazgo real, mismo bug ya cazado y
        # corregido en cripto el 18-Jul): ejecutar_venta_temprana() solo
        # resta el fee de VENTA -- el fee de APERTURA (ya cobrado al
        # comprar, guardado en t["fee_eur"] por sports_live_trade.py al
        # registrar la compra) nunca se restaba, sobrestimando el PnL neto
        # real en cada venta anticipada. Se resta aquí, en el caller, que
        # es quien tiene acceso a la fila original de trades.csv.
        try:
            fee_apertura = float(t.get("fee_eur") or 0.0)
        except (ValueError, TypeError):
            fee_apertura = 0.0
        pnl_neto_real = round(resultado["pnl_neto_eur"] - fee_apertura, 4)

        # /code-review 16-Sep (hallazgo real): sin este try/except, un
        # fallo AQUÍ (disco, KeyError, lo que sea) tras una venta real ya
        # EJECUTADA en el CLOB dejaba la fila como OPEN para siempre --
        # posición fantasma (vendida on-chain, contabilidad/circuit
        # breakers ciegos a ese PnL) y un reintento de venta en el
        # siguiente ciclo sobre shares que ya no existen. Igual que el
        # patrón fail-loud del resto del proyecto: nunca tragarse en
        # silencio un dinero real ya movido -- avisar por Telegram con
        # todos los datos para arreglarlo a mano si la escritura falla.
        try:
            lock_f = open(LOCK_PATH, "w")
            fcntl.flock(lock_f, fcntl.LOCK_EX)
            try:
                with open(TRADES, newline="", encoding="utf-8") as f:
                    filas = list(csv.DictReader(f))
                fieldnames = list(filas[0].keys()) if filas else list(t.keys())
                for r in filas:
                    # /code-review 16-Sep (hallazgo real): filtrar solo por
                    # market_id+OPEN podía cerrar la fila EQUIVOCADA si
                    # alguna vez hay 2 posiciones OPEN del mismo mercado en
                    # direcciones distintas -- la venta real ejecutada es
                    # de ESTA `direction` exacta, tiene que cerrar ESA fila.
                    try:
                        direction_fila = int(r.get("direction", ""))
                    except (ValueError, TypeError):
                        direction_fila = None
                    if (r.get("market_id") != t["market_id"] or r.get("status") != "OPEN"
                            or direction_fila != direction):
                        continue
                    r["status"] = "CLOSED"
                    r["close_timestamp"] = ahora.isoformat(timespec="seconds")
                    r["exit_price"] = str(resultado["exit_price"])
                    r["pnl_bruto_eur"] = round(resultado["valor_venta_eur"] - stake_eur, 4)
                    r["pnl_neto_eur"] = pnl_neto_real
                    # /code-review 16-Sep (hallazgo real, mismo patrón que
                    # shadow_resolve.py línea ~1341): una venta anticipada
                    # NO resuelve el mercado -- no hay outcome_real 0/1 de
                    # verdad todavía. Marcador de texto explícito (nunca un
                    # índice fabricado) para que cualquier consumidor que
                    # haga int(outcome_real) (ej. sports_wallet_mirror_
                    # clv.py) siga excluyendo estas filas de forma segura,
                    # en vez de asumir un resultado que no existe.
                    r["outcome_real"] = "TAKE_PROFIT_TEMPRANO" if motivo == "take_profit" else "STOP_LOSS_TEMPRANO"
                    # /code-review 16-Sep (hallazgo real): fee_eur debe
                    # reflejar apertura+venta combinado (mismo criterio
                    # que shadow_resolve.py línea ~1342), no quedarse en el
                    # valor de apertura sin actualizar -- si no, cualquier
                    # suma de fee_eur en trades.csv subestima el fee real
                    # pagado en cada venta anticipada.
                    r["fee_eur"] = round(fee_apertura + resultado.get("fee_eur", 0.0), 4)
                    # /code-review 16-Sep (hallazgo real): AÑADIR, nunca
                    # sobrescribir -- notas ya trae el wallet que disparó
                    # el mirror (sports_wallet_mirror_sniper.py), perderlo
                    # rompe cualquier análisis de wallet/concentración
                    # sobre trades cerrados por smart-exit. Mismo criterio
                    # que shadow_resolve.py (cripto): append con .strip().
                    r["notas"] = f"{r.get('notas', '')} smart_exit={motivo}".strip()
                    n_vendidas += 1
                    _log(f"  🎯 Smart-exit {motivo}: {t['market_id']} categoria={t.get('categoria')} "
                         f"tipo={t.get('tipo')} pnl_neto={pnl_neto_real:+.3f}€ "
                         f"(venta={resultado['pnl_neto_eur']:+.3f}€ - fee_apertura={fee_apertura:.3f}€)")
                    break
                with open(TRADES, "w", newline="", encoding="utf-8") as f:
                    w = csv.DictWriter(f, fieldnames=fieldnames)
                    w.writeheader()
                    w.writerows(filas)
            finally:
                fcntl.flock(lock_f, fcntl.LOCK_UN)
        except Exception as e:
            _log(f"  🚨 Smart-exit VENDIDO en el CLOB (order_id={resultado.get('order_id')}) pero "
                 f"FALLÓ al registrar el cierre en trades.csv: {type(e).__name__}: {e} -- "
                 f"posición fantasma, revisar y cerrar a mano")
            enviar_telegram(
                f"⚽ SPORTS\n🚨 *Smart-exit: venta real ejecutada pero NO registrada* (posición fantasma)\n"
                f"market={t['market_id']} order_id={resultado.get('order_id')}\n"
                f"pnl_neto real={pnl_neto_real}\nerror={type(e).__name__}: {e}\n"
                f"Revisar y cerrar la fila en trades.csv A MANO.",
                bot="sports",
            )
    return n_vendidas


async def main_async(loop_s: int = 60) -> None:
    """Wrapper async para sports_fase0_consolidado.py (mismo patrón que
    sports_wallet_mirror_sniper.main_ws()/sports_activity_ws.main() --
    _correr() espera una coroutine, resolver_una_pasada() es síncrono)."""
    _log(f"arrancado (async loop) -- resolviendo trades reales OPEN cada {loop_s}s")
    while True:
        try:
            n = resolver_una_pasada()
            if n:
                _log(f"{n} trade(s) resuelto(s)")
            # 16-Sep: check_salidas_tempranas() es inerte mientras
            # config_live_sports.json::smart_exit.activo no sea True --
            # ver su docstring. Después de resolver_una_pasada() para no
            # evaluar salida anticipada sobre una posición que ya cerró
            # normalmente en este mismo ciclo.
            n_ventas = check_salidas_tempranas()
            if n_ventas:
                _log(f"{n_ventas} venta(s) anticipada(s) (smart-exit)")
        except Exception as e:
            _log(f"error en ciclo: {type(e).__name__}: {e}")
        await asyncio.sleep(loop_s)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--loop", type=int, default=0, help="segundos entre pasadas (0 = una sola pasada)")
    args = ap.parse_args()

    if args.loop <= 0:
        n = resolver_una_pasada()
        _log(f"pasada única: {n} trade(s) resuelto(s)")
        return 0

    _log(f"arrancado -- bucle cada {args.loop}s")
    while True:
        try:
            n = resolver_una_pasada()
            if n:
                _log(f"{n} trade(s) resuelto(s)")
            n_ventas = check_salidas_tempranas()
            if n_ventas:
                _log(f"{n_ventas} venta(s) anticipada(s) (smart-exit)")
        except Exception as e:
            _log(f"error en ciclo: {type(e).__name__}: {e}")
        time.sleep(args.loop)


if __name__ == "__main__":
    sys.exit(main())
