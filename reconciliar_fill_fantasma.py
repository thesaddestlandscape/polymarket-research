"""
reconciliar_fill_fantasma.py — cierra el hueco real del 14-Sep: una orden
CRIPTO que SÍ ejecutó on-chain (order_id confirmado en get_trades(), tx_hash
real) quedó registrada en trades.csv como ERROR/stake=0 porque el poll
original de `_verificar_fill_real()` (3 intentos, 1.5s cada uno = 4.5s
total) es demasiado corto frente al indexado real del CLOB -- verificado
a mano ese día: la misma consulta 26 minutos después SÍ encontró el fill.
El código ya era fail-closed correcto en el momento (no duplica la orden,
deja rastro para reconciliar) -- lo que faltaba era el "reconciliar" en sí,
que hasta hoy dependía de que un humano viera la alerta de Telegram y lo
investigara a mano.

Qué hace: escanea `data/live/trades.csv` buscando filas `status=="ERROR"`
con la firma exacta de este caso (`notas` contiene "sin evidencia de fill
real" + `order_id=0x...`, añadido automáticamente por live_trade.py desde
este mismo commit). Para cada una, re-consulta `client.get_trades()` con
MUCHO más margen de tiempo que el poll original -- si encuentra un match
real (mismos criterios que `_verificar_fill_real`: maker_address==nuestra
wallet, trader_side=="TAKER", taker_order_id==order_id), corrige la fila
con la economía real (stake, precio de fill, y si el mercado ya resolvió,
outcome/pnl) y avisa por Telegram. Si NO encuentra nada tras
`MIN_ESPERA_MIN` desde el envío, marca la fila como revisada (no vuelve a
intentarlo) -- confirmado que de verdad no hubo fill, el ERROR original
queda como definitivo.

Fail-closed en todo momento: solo escribe cuando encuentra un match
INEQUÍVOCO (mismos 3 criterios que ya usa el motor de dinero real, no
inventa una interpretación nueva). Nunca coloca ni cancela ninguna orden
-- solo lectura de la API + corrección de un registro contable ya escrito.

Cron sugerido: cada 10-15min (independiente del poll inmediato, que sigue
existiendo y sigue siendo fail-closed rápido -- esto es la red de
seguridad para el caso de indexado lento, no un sustituto).
"""
import csv
import fcntl
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

# 20-Sep (hallazgo real: 2 fills fantasma de sports, ~1,05€ cada uno,
# quedaron 18-20h sin registrar -- sports_wallet_mirror_sniper.py solo
# registraba en trades.csv cuando ok=True, así que el caso "sin_fill_
# confirmado" ni siquiera dejaba una fila que reconciliar; corregido ahí
# aparte). Este script cubría solo cripto -- se generaliza a una lista de
# ledgers, cada uno con su propio lock (mismo criterio que ya usa
# reconciliar_sports.py para no mezclar ficheros/dinero de cripto y sports,
# CLAUDE.md "no mezclar"). Sports comparte la MISMA wallet on-chain que
# cripto (no tiene wallet propia, ver reconciliar_sports.py) -- el criterio
# de match (maker_address==wallet, TAKER, taker_order_id==order_id) es
# idéntico, solo cambia qué fichero se lee/escribe y que market_id en
# sports YA es el condition_id completo (no pasa por market_id_resolver,
# que es una tabla de cripto para IDs numéricos cortos -- pasarlo por ahí
# sería un no-op que además ensucia el índice de resolución de cripto).
LEDGERS = [
    {
        "nombre": "cripto",
        "trades_path": REPO / "data/live/trades.csv",
        # Mismo lock que _registrar_trade() en live_trade.py (TRADES_LOCK_PATH) --
        # este script hace un read-modify-write completo del fichero, no un simple
        # append; sin el mismo flock, una escritura de live_trade.py justo entre mi
        # lectura y mi escritura se perdería (yo reescribiría el fichero con la
        # versión vieja que leí, sin su fila nueva). Ruta duplicada a propósito
        # (ver mismo criterio que FEE_RATE_TAKER_CRYPTO en shadow_pnl_fiel.py --
        # importar live_trade.py aquí traería credenciales/requests innecesarios).
        "lock_path": REPO / "data/live/.trades_lock",
        "usar_resolver": True,
        "fee_rate": 0.07,
    },
    {
        "nombre": "sports",
        "trades_path": REPO / "data/sports/trades.csv",
        "lock_path": REPO / "data/sports/.trades_lock",  # mismo TRADES_LOCK_PATH que sports_live_trade.py
        "usar_resolver": False,
        # sports usa feeSchedule.rate=0.05, NO 0.07 (verificado 26-Ago
        # contra gamma-api, ver CLAUDE.md/analisis_sports_wallet_mirror_
        # gate_bucket_26ago.py) -- usar el de cripto aquí habría sobre-
        # estimado el fee (y por tanto infravalorado el pnl) de cualquier
        # trade ganador de sports que se reconciliara por esta vía.
        "fee_rate": 0.05,
    },
]
MIN_ESPERA_MIN = 10  # margen generoso sobre el indexado real observado (~26min en el incidente, pero
                      # ese fue el peor caso visto una vez -- 10min ya es 130x el poll original de 4.5s)

FIRMA_RE = re.compile(r"order_id=(0x[0-9a-fA-F]+)")


def _cargar_filas(trades_path: Path):
    with open(trades_path, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    return rows[0], rows[1:]


def _guardar_filas(trades_path: Path, header, filas):
    tmp = str(trades_path) + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(filas)
    os.replace(tmp, trades_path)


def _cliente():
    from dotenv import load_dotenv
    load_dotenv(REPO / "data/live/.env")
    from py_clob_client_v2.client import ClobClient
    from py_clob_client_v2.clob_types import ApiCreds
    creds = ApiCreds(api_key=os.getenv("POLY_API_KEY"), api_secret=os.getenv("POLY_API_SECRET"),
                      api_passphrase=os.getenv("POLY_API_PASSPHRASE"))
    return ClobClient("https://clob.polymarket.com", key=os.getenv("POLY_PRIVATE_KEY"),
                       chain_id=137, creds=creds)


def _buscar_fill_real(client, condition_id: str, order_id: str, wallet: str) -> dict | None:
    from py_clob_client_v2.clob_types import TradeParams
    try:
        trades = client.get_trades(TradeParams(market=condition_id))
    except Exception as e:
        print(f"[reconciliar_fill_fantasma] error consultando get_trades({condition_id}): {e}")
        return None
    for t in trades:
        if (str(t.get("maker_address", "")).lower() == wallet
                and t.get("trader_side") == "TAKER"
                and t.get("taker_order_id") == order_id):
            return t
    return None


def _reconciliar_ledger(ledger: dict, wallet: str) -> int:
    from shadow_digest import enviar_telegram
    import market_id_resolver

    nombre = ledger["nombre"]
    trades_path = ledger["trades_path"]
    lock_path = ledger["lock_path"]
    usar_resolver = ledger["usar_resolver"]
    fee_rate = ledger["fee_rate"]
    bot = "sports" if nombre == "sports" else "cripto"

    if not trades_path.exists():
        print(f"[reconciliar_fill_fantasma][{nombre}] {trades_path} no existe todavía, se salta")
        return 0

    header, filas = _cargar_filas(trades_path)
    idx = {h: i for i, h in enumerate(header)}
    ahora = datetime.now(timezone.utc)

    candidatas = []
    for i, r in enumerate(filas):
        if len(r) <= idx["notas"]:
            continue
        if r[idx["status"]] != "ERROR":
            continue
        notas = r[idx["notas"]]
        if "sin evidencia de fill real" not in notas or "revisado_sin_fill=" in notas:
            continue
        m = FIRMA_RE.search(notas)
        if not m:
            continue
        try:
            ts = datetime.fromisoformat(r[idx["timestamp_utc"]])
        except Exception:
            continue
        if (ahora - ts).total_seconds() < MIN_ESPERA_MIN * 60:
            continue  # todavía dentro del margen de indexado, revisar en el próximo ciclo
        candidatas.append((i, r, m.group(1), ts))

    if not candidatas:
        print(f"[reconciliar_fill_fantasma][{nombre}] 0 filas candidatas (ERROR+sin evidencia de fill+order_id, "
              "fuera del margen de indexado)")
        return 0

    print(f"[reconciliar_fill_fantasma][{nombre}] {len(candidatas)} fila(s) candidata(s)")
    # Fase 1 (SIN lock): toda la parte lenta (llamadas de red a la API de
    # Polymarket) vive aquí -- mantener el lock de trades.csv durante
    # segundos de I/O de red bloquearía innecesariamente los appends del
    # fast loop. Las actualizaciones se guardan indexadas por (market_id,
    # order_id), no por índice de fila -- la Fase 2 vuelve a leer el
    # fichero fresco y localiza las filas por ese par, robusto a que
    # live_trade.py haya añadido filas nuevas mientras tanto.
    actualizaciones: dict[tuple[str, str], dict] = {}
    client = None
    for i, r, order_id, ts in candidatas:
        mid = r[idx["market_id"]]
        # sports: market_id YA es el condition_id completo (verificado
        # 20-Sep contra la API real) -- market_id_resolver es una tabla de
        # cripto para IDs numéricos cortos, pasar un condition_id por ahí
        # sería un no-op que además ensucia su índice de resolución.
        condition_id = market_id_resolver.resolver(mid) if usar_resolver else mid
        if not condition_id:
            print(f"[reconciliar_fill_fantasma][{nombre}] {mid}: sin condition_id resoluble, se reintenta otro ciclo")
            continue
        if client is None:
            client = _cliente()
        fill = _buscar_fill_real(client, condition_id, order_id, wallet)
        if fill is None:
            # Sin evidencia tras un margen generoso -- se marca revisada para no
            # reintentar cada ciclo; el ERROR original queda como definitivo.
            actualizaciones[(mid, order_id)] = {"notas_extra": " revisado_sin_fill=1"}
            print(f"[reconciliar_fill_fantasma][{nombre}] {mid} order_id={order_id}: SIN fill tras "
                  f"{(datetime.now(timezone.utc)-ts).total_seconds()/60:.0f}min -- ERROR confirmado, no reintenta más")
            continue

        precio_fill = float(fill.get("price", 0) or 0)
        size = float(fill.get("size", 0) or 0)
        stake_real = round(precio_fill * size, 4)
        tx_hash = fill.get("transaction_hash", "")
        trade_id = fill.get("id", "")

        cerrado = None
        try:
            mercado = client.get_market(condition_id)
            if mercado.get("closed"):
                cerrado = {t.get("outcome"): float(t.get("price", 0)) for t in mercado.get("tokens", [])}
        except Exception as e:
            print(f"[reconciliar_fill_fantasma] {mid}: no se pudo consultar resolución del mercado: {e}")

        upd = {"stake_eur": str(stake_real), "entry_price": str(precio_fill)}
        aviso_extra = ""
        if cerrado is not None:
            precio_final = cerrado.get(fill.get("outcome", ""))
            if precio_final is not None:
                ganado = precio_final >= 0.5
                upd["status"] = "CLOSED"
                upd["close_timestamp"] = ahora.isoformat(timespec="seconds")
                upd["exit_price"] = str(precio_final)
                upd["outcome_real"] = "1" if ganado else "0"
                if ganado:
                    fee = fee_rate * precio_fill * (1 - precio_fill) * (stake_real / max(precio_fill, 0.01))
                    pnl = stake_real * (1.0 / max(precio_fill, 0.01) - 1.0) - fee
                else:
                    fee = 0.0
                    pnl = -stake_real
                upd["fee_eur"] = str(round(fee, 4))
                upd["pnl_bruto_eur"] = str(round(pnl, 4))
                upd["pnl_neto_eur"] = str(round(pnl, 4))
                aviso_extra = f"Mercado ya resuelto: {'GANADA' if ganado else 'PERDIDA'} pnl={pnl:+.2f}€"
            else:
                upd["status"] = "OPEN"
                aviso_extra = "Mercado cerrado pero sin precio de outcome claro -- queda OPEN, revisar a mano"
        else:
            upd["status"] = "OPEN"
            aviso_extra = "Mercado sigue abierto -- posición real, queda OPEN para que shadow_resolve/resolve la cierre normalmente"

        upd["notas"] = (f"RECONCILIADO AUTO {ahora.isoformat(timespec='seconds')}: fill real confirmado "
                        f"(trade_id={trade_id} tx={tx_hash} size={size}@{precio_fill}). "
                        f"Antes ERROR/stake=0 por indexado lento del poll original. " + aviso_extra)
        actualizaciones[(mid, order_id)] = upd
        print(f"[reconciliar_fill_fantasma][{nombre}] {mid} order_id={order_id}: fill real encontrado, "
              f"stake_real={stake_real:.2f}€ (se aplicará en Fase 2)")
        actualizaciones[(mid, order_id)]["_telegram"] = (
            f"🔧 *Reconciliación automática: fill fantasma corregido* ({nombre})\n"
            f"market={mid} order_id={order_id}\n"
            f"Stake real: {stake_real:.2f}€ @ {precio_fill:.4f}\n"
            f"{aviso_extra}\n"
            f"Fila corregida en trades.csv, tx={tx_hash}"
        )

    if not actualizaciones:
        return 0

    # Fase 2 (CON lock, misma ruta que _registrar_trade en live_trade.py/
    # sports_live_trade.py::registrar_trade): relee el fichero FRESCO
    # (puede haber cambiado desde la Fase 1) y localiza cada fila por
    # (market_id, order_id) en `notas`, no por el índice de la Fase 1 --
    # robusto a filas nuevas insertadas mientras tanto por el loop dueño
    # de este ledger.
    cambios = 0
    with open(lock_path, "w") as lock_f:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        try:
            header2, filas2 = _cargar_filas(trades_path)
            idx2 = {h: i for i, h in enumerate(header2)}
            for j, r2 in enumerate(filas2):
                if len(r2) <= idx2["notas"] or r2[idx2["status"]] != "ERROR":
                    continue
                m2 = FIRMA_RE.search(r2[idx2["notas"]])
                if not m2:
                    continue
                clave = (r2[idx2["market_id"]], m2.group(1))
                upd = actualizaciones.get(clave)
                if upd is None or "revisado_sin_fill=1" in r2[idx2["notas"]]:
                    continue
                if "notas_extra" in upd:
                    r2[idx2["notas"]] = r2[idx2["notas"]] + upd["notas_extra"]
                else:
                    for campo, valor in upd.items():
                        if campo in idx2 and campo != "_telegram":
                            r2[idx2[campo]] = valor
                filas2[j] = r2
                cambios += 1
            if cambios:
                _guardar_filas(trades_path, header2, filas2)
        finally:
            fcntl.flock(lock_f, fcntl.LOCK_UN)

    if cambios:
        print(f"[reconciliar_fill_fantasma][{nombre}] {cambios} fila(s) actualizada(s) en trades.csv (Fase 2, con lock)")
        for upd in actualizaciones.values():
            if "_telegram" in upd:
                enviar_telegram(upd["_telegram"], bot=bot)
    return cambios


def main() -> int:
    wallet = (os.getenv("POLY_DEPOSIT_WALLET") or "").lower()
    if not wallet:
        from dotenv import load_dotenv
        load_dotenv(REPO / "data/live/.env")
        wallet = (os.getenv("POLY_DEPOSIT_WALLET") or "").lower()

    for ledger in LEDGERS:
        try:
            _reconciliar_ledger(ledger, wallet)
        except Exception as e:
            print(f"[reconciliar_fill_fantasma][{ledger['nombre']}] ERROR {type(e).__name__}: {e}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[reconciliar_fill_fantasma] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
