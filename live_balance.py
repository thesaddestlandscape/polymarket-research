#!/usr/bin/env python3
"""live_balance.py — Lee el balance REAL de Polymarket (read-only) y lo cachea.

Motivo (2026-07-07): el dashboard/`trades.csv` reportaban un PnL live de plan
(precio de entrada previsto, `fee_eur=0.00`) que NUNCA se contrastaba contra el
wallet. Real −3.63 USDC vs registrado −0.78 → dashboard engañoso. Este módulo
ancla el bankroll live a la verdad de suelo: el USDC del wallet + valor de
posiciones abiertas.

- **Read-only**: solo consulta balance/posiciones, jamás envía órdenes.
- **Fail-closed**: si la API falla, NO sobrescribe el JSON cacheado (deja el
  último bueno) y sale con código !=0. El dashboard trata el JSON viejo/ausente
  como "n/d" y no fabrica cifras.
- **No en el hot-path del dashboard**: se invoca periódicamente (slow loop/cron);
  el dashboard solo LEE `data/live/balance_real.json`.

Uso:  python3 live_balance.py          # fetch + cache
      from live_balance import cargar_balance_real   # lectura cacheada
"""
import csv
import json
import os
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

import requests

DIR_LIVE = Path(__file__).parent / "data" / "live"
CACHE_PATH = DIR_LIVE / "balance_real.json"
HIST_PATH = DIR_LIVE / "balance_history.csv"

try:
    from live_stake import CAPITAL_OPERATIVO_INICIAL as _PRIMER_DEPOSITO
except Exception:
    _PRIMER_DEPOSITO = 25.44  # depósito real 2026-06-29 (fallback)

DEPOSITO_INICIAL = _PRIMER_DEPOSITO  # compatibilidad: módulos que importan este símbolo


def _cargar_depositos_config() -> list:
    """Lee config_live.json::depositos. Devuelve lista vacía ante cualquier error (fail-safe)."""
    cfg_path = DIR_LIVE / "config_live.json"
    try:
        deps = json.loads(cfg_path.read_text(encoding="utf-8")).get("depositos", [])
        return [d for d in deps if isinstance(d, dict) and d.get("eur")]
    except Exception:
        return []


def _pnl_por_deposito(depositos: list) -> list:
    """PNL de trades CLOSED agrupado por período de depósito (ledger, trades.csv).

    Para cada depósito i, suma los trades cuyo timestamp_utc cae entre
    deposito[i].fecha y deposito[i+1].fecha (o hasta hoy para el último).
    Puramente informativo — no toca ninguna decisión de trading.
    """
    if not depositos:
        return []
    deps = sorted(depositos, key=lambda d: d.get("fecha", ""))
    cortes = [d["fecha"] for d in deps]  # fecha de inicio de cada período
    pnls = [0.0] * len(deps)
    ns   = [0]   * len(deps)
    trades_csv = DIR_LIVE.parent / "live" / "trades.csv"
    if trades_csv.exists():
        with open(trades_csv, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("status") != "CLOSED":
                    continue
                ts = (row.get("timestamp_utc") or "")[:10]
                if not ts:
                    continue
                try:
                    pnl = float(row.get("pnl_neto_eur", 0) or 0)
                except ValueError:
                    continue
                # Asignar al período más reciente cuya fecha de inicio ≤ ts
                idx = 0
                for i, corte in enumerate(cortes):
                    if ts >= corte:
                        idx = i
                pnls[idx] += pnl
                ns[idx]   += 1
    return [
        {
            "fecha": d["fecha"],
            "eur": d["eur"],
            "nota": d.get("nota", ""),
            "pnl_ledger": round(pnls[i], 4),
            "n_trades": ns[i],
            "rendimiento_pct": round(pnls[i] / d["eur"] * 100, 1) if d["eur"] else None,
        }
        for i, d in enumerate(deps)
    ]

DATA_API = "https://data-api.polymarket.com"
USDC_DECIMALS = 1_000_000  # USDC = 6 decimales


def _get_clob_client():
    """Cliente CLOB V2 autenticado (mismo flujo que live_trade)."""
    from dotenv import load_dotenv
    from py_clob_client_v2 import ClobClient, ApiCreds
    from py_clob_client_v2.constants import POLYGON
    load_dotenv(DIR_LIVE / ".env")
    creds = ApiCreds(
        api_key=os.getenv("POLY_API_KEY"),
        api_secret=os.getenv("POLY_API_SECRET"),
        api_passphrase=os.getenv("POLY_API_PASSPHRASE"),
    )
    return ClobClient(
        "https://clob.polymarket.com",
        key=os.getenv("POLY_PRIVATE_KEY"),
        chain_id=POLYGON,
        creds=creds,
        signature_type=3,
        funder=os.getenv("POLY_DEPOSIT_WALLET"),
    )


def _saldo_pusd_onchain() -> float | None:
    """Saldo pUSD real on-chain (mismo método que taker_rebate_tracker.py::
    _saldo_pusd -- RPC directo a Polygon, balanceOf, sin librería web3).

    Origen (02-Sep, hallazgo de sesión): la API de balance del CLOB
    (`_free_usdc`, AssetType.COLLATERAL) reportó 9,60 USDC mientras el
    saldo pUSD real on-chain era 13,55 -- una diferencia de ~4€ invisible
    al bankroll reportado (`total`/`pnl_real`). Verificado que NO es un
    bloqueo de aprobación (`allowance()` de pUSD hacia exchange_v2/
    neg_risk_exchange_v2 ya está en máximo/ilimitado) -- la causa más
    probable es un desfase de indexación del backend de Polymarket tras
    el pago automático del Taker Rebate. Puramente informativo por ahora
    (no se suma a `total`/`pnl_real` sin verificar primero, en una
    próxima sesión, si ese saldo es realmente utilizable como margen de
    trading o si Polymarket tarda en reconciliarlo solo) -- fail-soft,
    nunca tumba el resto del balance si el RPC falla."""
    import requests
    wallet = os.getenv("POLY_DEPOSIT_WALLET")
    if not wallet:
        return None
    pusd_contrato = "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB"
    selector = "0x70a08231" + wallet[2:].rjust(64, "0").lower()
    try:
        r = requests.post(
            "https://polygon-bor-rpc.publicnode.com",
            json={"jsonrpc": "2.0", "id": 1, "method": "eth_call",
                  "params": [{"to": pusd_contrato, "data": selector}, "latest"]},
            timeout=10,
        )
        r.raise_for_status()
        result = r.json().get("result")
        if not result:
            return None
        return int(result, 16) / 1_000_000
    except Exception as e:
        print(f"[live_balance] aviso: no se pudo leer saldo pUSD on-chain ({type(e).__name__}: {e})")
        return None


def _free_usdc(client) -> float:
    """USDC libre (colateral) del wallet, en unidades USDC."""
    from py_clob_client_v2.clob_types import BalanceAllowanceParams, AssetType
    ba = client.get_balance_allowance(
        BalanceAllowanceParams(asset_type=AssetType.COLLATERAL))
    raw = ba.get("balance") if isinstance(ba, dict) else None
    if raw is None:
        raise RuntimeError(f"balance_allowance sin 'balance': {ba!r}")
    return int(raw) / USDC_DECIMALS


_POSITIONS_VALUE_TOLERANCIA_ABS = 1.0    # € — margen antes de desconfiar de /value
_POSITIONS_VALUE_TOLERANCIA_PCT = 0.15   # 15% del propio /value, lo que sea mayor


def _fetch_posiciones_wallet(wallet: str) -> list | None:
    """Trae TODAS las posiciones de la wallet (`/positions`, redeemable=false
    + redeemable=true con currentValue>0, mismo criterio de paginación
    acotada que `_positions_value_sumada` documenta abajo) en UNA sola
    pasada de 2 llamadas HTTP, compartida entre `_positions_value_sumada`
    (cross-check crudo de cripto) y `_sports_positions_value_actual` (split
    sports) -- antes cada una hacía sus propias 2 llamadas por separado,
    duplicando red/IO en cada `fetch_balance_real()` donde sports tuviera
    una posición abierta (/code-review 03-Sep). Devuelve None si falla
    (best-effort, cada caller decide su propio fallback)."""
    try:
        out = []
        r = requests.get(f"{DATA_API}/positions",
                          params={"user": wallet, "redeemable": "false", "limit": 500},
                          timeout=20)
        r.raise_for_status()
        d = r.json()
        if isinstance(d, list):
            out.extend(d)
        r2 = requests.get(f"{DATA_API}/positions",
                           params={"user": wallet, "redeemable": "true", "limit": 500},
                           timeout=20)
        r2.raise_for_status()
        d2 = r2.json()
        if isinstance(d2, list):
            out.extend(p for p in d2 if float(p.get("currentValue") or 0.0) > 0)
        return out
    except Exception:
        return None


def _positions_value_sumada(wallet: str, posiciones: list | None = None) -> float | None:
    """Suma currentValue de data-api /positions -- fuente independiente de
    /value, usada solo como cross-check (08-11). Devuelve None si la llamada
    falla (best-effort, no debe tumbar _positions_value).

    `posiciones`: lista ya traída por `_fetch_posiciones_wallet()` (evita
    repetir las 2 llamadas HTTP si el caller ya las hizo); si es None, las
    trae aquí mismo (comportamiento previo, sin cambios para otros
    callers).

    01-Sep (bug real de dinero, encontrado en el barrido de esta sesión tras
    2 alertas de reconciliación -- cripto TE delta_dia=-2.12$, sports
    delta_dia=-1.07€, el mismo día que sports abrió su primera posición
    OPEN real de verdad, `LoL#SEGUIR` 1.05€): `/positions` SIN filtro
    devuelve por defecto solo ~100 filas (paginación silenciosa de la API,
    sin error ni aviso), y esta wallet ya acumula 200+ posiciones
    históricas -- casi todas resueltas hace tiempo con currentValue=0. La
    única posición REALMENTE abierta (`redeemable=false`) puede quedar
    fuera de esa página si su `size` no está entre las ~100 mayores de
    todo el historial (aquí: size=2.19 de la posición viva vs decenas de
    posiciones históricas más grandes ya resueltas). La suma salía 0.0,
    /value devolvía el valor correcto (1.0391€), pero como la discrepancia
    superó la tolerancia de _positions_value(), el cross-check DESCARTÓ el
    valor correcto y usó la suma incompleta -- exactamente al revés de lo
    que ese cross-check existe para prevenir (ver docstring de abajo, caso
    11-Ago). Fix: filtrar por `redeemable=false` -- servidor devuelve SOLO
    las posiciones aún no resueltas (por diseño no puede haber cientos,
    nunca trunca), sin depender de un límite fijo que la cuenta puede
    volver a desbordar según crezca el historial.

    /code-review de este mismo fix (01-Sep) señaló un hueco teórico: una
    posición GANADA pero todavía no reclamada también sale con
    `redeemable=true` (mismo flag que una posición vieja ya resuelta y sin
    valor, ver candidata2_weekly_temprano_espejo_fase0.py:70-71) -- filtrar
    solo por `redeemable=false` la excluiría con currentValue real. Nunca
    observado en esta wallet (verificado en vivo: 0/220 posiciones
    `redeemable=true` con currentValue>0 -- Polymarket parece liquidar el
    payout sin dejar posición reclamable pendiente), pero se cubre igual
    sin reintroducir el problema de paginación original: sumar TAMBIÉN
    cualquier `redeemable=true` con currentValue>0 dentro de una página
    igual de acotada (nunca puede haber cientos de posiciones ganadas con
    saldo pendiente de golpe, a diferencia del histórico completo)."""
    if posiciones is None:
        posiciones = _fetch_posiciones_wallet(wallet)
    if posiciones is None:
        return None
    return sum(float(p.get("currentValue") or 0.0) for p in posiciones)


def _positions_value(wallet: str) -> tuple[float, list | None]:
    """Valor mark-to-market de las posiciones abiertas (data-api /value),
    con cross-check contra la suma de currentValue de /positions. Devuelve
    (valor, lista_posiciones_cruda_o_None) -- ver nota 03-Sep abajo.

    Devuelve 0.0 si no hay posiciones vivas (todo resuelto/redimido).

    2026-08-11 (hallazgo real, ver bankroll_inicio_dia_override en
    live_stake.py): /value devolvió un valor fantasma (0→27€→33€→0 en
    ~75min) sin ninguna posición real que lo justificara -- /positions
    mostraba currentValue=0 en TODAS las filas al mismo tiempo. El pico
    falso cayó justo en el cierre de día Madrid y disparó el freno diario
    por una "pérdida" del 76% que nunca ocurrió. Cross-check: si /value y
    la suma de /positions discrepan más de la tolerancia, /value es el
    sospechoso (una sola cifra agregada de un endpoint que ya demostró
    fallar así) -- se usa la suma de /positions en su lugar y se deja
    rastro en el log del caller. Si /positions falla (best-effort), se
    confía en /value solo (comportamiento previo, sin cross-check).

    03-Sep: devuelve también la lista cruda de `/positions` (o None si
    falló) para que `fetch_balance_real()` se la pase a
    `_sports_positions_value_actual()` sin repetir las 2 llamadas HTTP."""
    r = requests.get(f"{DATA_API}/value", params={"user": wallet}, timeout=20)
    r.raise_for_status()
    d = r.json()
    if isinstance(d, list) and d:
        val = float(d[0].get("value") or 0.0)
    elif isinstance(d, dict):
        val = float(d.get("value") or 0.0)
    else:
        val = 0.0

    posiciones = _fetch_posiciones_wallet(wallet)
    suma = _positions_value_sumada(wallet, posiciones)
    if suma is not None:
        tolerancia = max(_POSITIONS_VALUE_TOLERANCIA_ABS,
                          _POSITIONS_VALUE_TOLERANCIA_PCT * val)
        if abs(val - suma) > tolerancia:
            print(f"⚠️  /value ({val:.4f}€) discrepa de suma /positions "
                  f"({suma:.4f}€) más de la tolerancia ({tolerancia:.2f}€) "
                  f"-- usando suma /positions", file=sys.stderr)
            return suma, posiciones
    return val, posiciones


SPORTS_CONFIG_PATH = Path(__file__).parent / "data" / "sports" / "config_live_sports.json"
SPORTS_TRADES_PATH = Path(__file__).parent / "data" / "sports" / "trades.csv"


def _sports_open_condition_ids_y_coste() -> dict:
    """conditionId (=market_id en data/sports/trades.csv) -> coste combinado
    (suma de stake_eur, por si dos filas OPEN compartieran el mismo
    conditionId) de las posiciones de sports actualmente OPEN.

    dict por-id (no un total agregado) a propósito -- /code-review 03-Sep
    encontró que un fallback todo-o-nada (si `/positions` devuelve ALGUNA
    posición, usar la suma completa de valores reales; si no, el coste
    agregado completo) puede ocultar una posición real: si `/positions`
    devuelve solo 1 de 2 posiciones abiertas (paginación, o indexado con
    lag justo tras abrir una nueva), un fallback agregado no cubre la que
    falta. Con este dict, `_sports_positions_value_actual()` hace fallback
    POR POSICIÓN -- la que sí aparece usa su valor real, la que no,
    su propio coste.

    Filtro `status != "CLOSED"` (no `== "OPEN"`) a propósito -- segunda
    ronda /code-review 03-Sep: `_cargar_sports_eventos()`/
    `_sports_capital_en_free_usdc()` ya tratan cualquier status que no sea
    "CLOSED" (incluido un futuro "ERROR" con stake real) como todavía
    abierto y restan su stake del lado de caja -- si esta función solo
    reconocía "OPEN", una fila así habría restado de caja sin ningún
    fallback de posición que la compensara, infravalorando `total` de
    cripto en silencio. No observado hoy (el único escritor de sports solo
    escribe filas cuando la orden se confirma), pero ambas funciones deben
    coincidir en qué cuenta como "abierta"."""
    costes: dict = {}
    try:
        if SPORTS_TRADES_PATH.exists():
            with open(SPORTS_TRADES_PATH, encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    if row.get("status") == "CLOSED" or not row.get("market_id"):
                        continue
                    try:
                        stake = float(row.get("stake_eur", 0) or 0)
                    except ValueError:
                        stake = 0.0
                    if stake <= 0:
                        continue
                    costes[row["market_id"]] = costes.get(row["market_id"], 0.0) + stake
    except Exception:
        pass
    return costes


def _sports_positions_value_actual(wallet: str, posiciones: list | None = None) -> float:
    """Valor mark-to-market REAL (data-api /positions, `currentValue`) de
    las posiciones de sports actualmente abiertas en la wallet compartida
    -- contraparte de `_sports_capital_en_free_usdc()` (que cubre el lado
    `free_usdc`/caja) para el lado `positions_value` de `fetch_balance_
    real()`.

    03-Sep noche (bug real, encontrado en el barrido de esta sesión tras
    la pregunta de Javi sobre por qué el balance de cripto oscilaba sin
    ningún trade de cripto ejecutándose): la función que existía para esto
    (`live_stake._capital_ajeno_en_wallet_compartida()`, 27-Ago) restaba
    `sports_live_stake.bankroll_actual() + stakes_abiertos_total()` de
    AMBOS `free_usdc` y `total` -- dos bugs a la vez:
      1. El stake de una posición de sports abierta ya salió de `free_usdc`
         en el momento de abrir (está en `positions_value`, no en
         `free_usdc`) -- restarlo TAMBIÉN de `free_usdc` lo cuenta dos
         veces (`bankroll_actual()` = depósitos+pnl_cerrado YA incluye ese
         coste, a precio de coste, dentro de su cifra agregada). Mismo bug
         de fondo que motivó `_sports_capital_en_free_usdc()` el mismo día,
         pero esa función solo se conectó a la reconstrucción histórica de
         `_daily_real_pnl_balance()`, nunca al snapshot EN VIVO de
         `fetch_balance_real()` -- este es el hueco real.
      2. Restar el COSTE (`stakes_abiertos_total()`, precio de apertura) en
         vez del VALOR DE MERCADO actual de `total`/`positions_value`
         sobre/sub-estima según se haya movido el precio desde la apertura.
         Verificado en vivo 03-Sep ~14:30 UTC: 2 posiciones abiertas
         (LoL + CS2), coste combinado 2,10€, valor de mercado real
         (`/positions::currentValue`) 1,12€ -- la de CS2 cayó de 0,49 a
         0,09 (partida en curso yendo mal para esa wallet). Usar el coste
         ahí sub-restaba ~0,98€ del lado de `total`/`positions_value` de
         cripto en ese instante, y el error crece o decrece con cada
         movimiento de precio de la partida en vivo -- exactamente el
         vaivén sin trades de cripto que motivó la pregunta.
      Combinado: `total`/`free_usdc` de cripto llegaron a estar
      infravalorados varios euros de golpe (verificado: ~3-4€ el 03-Sep)
      sin que ningún trade de cripto real lo justificara -- afecta
      directamente a `live_stake.bankroll_actual()` (Kelly + circuit
      breaker), no solo al dashboard.

    Fix: caja exacta (`_sports_capital_en_free_usdc()`) restada de
    `free_usdc`, y VALOR DE MERCADO real (esta función, matched por
    `conditionId`) restado de `total` -- NUNCA de `positions_value`
    reportado, que se deja crudo a propósito (ver comentario en
    `fetch_balance_real()` sobre por qué: `_daily_real_pnl_balance()`
    depende de que `positions_value` sea crudo).

    Fail-safe POR POSICIÓN (/code-review 03-Sep, ver docstring de
    `_sports_open_condition_ids_y_coste`): cada conditionId abierto empieza
    con su propio coste como valor por defecto; si `/positions` lo
    devuelve, se sustituye por su `currentValue` real. Si `/positions`
    falla por completo, TODOS quedan en su coste (mismo comportamiento
    conservador que antes) -- pero si falla a medias (devuelve 1 de 2), la
    que sí aparece usa valor real y la otra no queda en 0 silencioso.

    03-Sep, segunda ronda /code-review -- 2 hallazgos más, ambos cerrados:
      - Dos filas OPEN con el mismo conditionId (outcomes opuestos del
        mismo mercado, o reentrada): `/positions` las devuelve como
        entradas SEPARADAS (comparten conditionId, difieren en `asset` --
        el token). La primera vez que se ve ese conditionId se sustituye
        el coste por su currentValue; la SEGUNDA vez se SUMA (no se pisa)
        -- coherente con `_sports_open_condition_ids_y_coste()`, que ya
        suma los costes de ambas filas bajo la misma clave. No requiere
        matchear por `asset` porque no nos importa distinguir CUÁL de las
        dos es cada una, solo que ninguna se pierda.
      - `posiciones`: lista ya traída por `_fetch_posiciones_wallet()`
        (compartida con el cross-check de `_positions_value`) -- si es
        None, se trae aquí (comportamiento previo). Antes esta función
        siempre hacía sus 2 llamadas HTTP propias, duplicando red/IO con
        el cross-check de cripto cada vez que sports tenía una posición
        abierta."""
    costes = _sports_open_condition_ids_y_coste()
    if not costes:
        return 0.0
    if posiciones is None:
        posiciones = _fetch_posiciones_wallet(wallet)
    valores = dict(costes)  # default: coste; se sustituye/acumula con valor real si aparece
    if posiciones is not None:
        vistos: set = set()
        for p in posiciones:
            cid = p.get("conditionId")
            if cid in costes:
                val = float(p.get("currentValue") or 0.0)
                if cid in vistos:
                    valores[cid] += val       # 2ª+ posición bajo el mismo mercado: se suma
                else:
                    valores[cid] = val        # 1ª vez: sustituye el coste fallback
                vistos.add(cid)
    return sum(valores.values())


def _cargar_sports_eventos() -> tuple[list, list]:
    """03-Sep (`/code-review`, hallazgo real de rendimiento): lee UNA sola
    vez los depósitos de sports y las filas de `data/sports/trades.csv`,
    en vez de que `_sports_capital_en_free_usdc()` reabra y re-parsee
    ambos ficheros en CADA llamada -- `_daily_real_pnl_balance()` la llama
    una vez por fila de `balance_history.csv` (5978 filas hoy, creciendo
    en cada trade real abierto/cerrado, y `fetch_balance_real()` corre en
    cada apertura/resolución real) -- sin este cache, cada refresco de
    balance reabría los 2 ficheros ~6000 veces. Mismo patrón de fondo que
    el incidente real de `shadow_postmortem.py` (CLAUDE.md pt.18, 02-Sep):
    crecimiento sin límite × trabajo repetido en un camino que bloquea
    resolución de dinero real.

    Devuelve (depositos, eventos): depositos = [(fecha_dt_utc, eur), ...];
    eventos = [(ts_open, ts_close_o_None, stake, pnl, closed_bool), ...],
    ya parseados y listos para que `_sports_capital_en_free_usdc()` solo
    itere en memoria."""
    depositos = []
    try:
        cfg = json.loads(SPORTS_CONFIG_PATH.read_text(encoding="utf-8"))
        for d in cfg.get("depositos", []):
            if not (isinstance(d, dict) and d.get("eur") and d.get("fecha")):
                continue
            try:
                fecha_dt = datetime.strptime(d["fecha"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
            except ValueError:
                continue
            depositos.append((fecha_dt, float(d["eur"])))
    except Exception:
        pass

    def _parse_ts(raw: str):
        if not raw:
            return None
        try:
            return datetime.fromisoformat(raw.replace("Z", "+00:00"))
        except ValueError:
            return None

    eventos = []
    try:
        if SPORTS_TRADES_PATH.exists():
            with open(SPORTS_TRADES_PATH, encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    try:
                        stake = float(row.get("stake_eur", 0) or 0)
                    except ValueError:
                        stake = 0.0
                    if stake <= 0:
                        continue
                    ts_open = _parse_ts(row.get("timestamp_utc") or "")
                    if ts_open is None:
                        continue
                    closed = row.get("status") == "CLOSED"
                    ts_close = _parse_ts(row.get("close_timestamp") or "") if closed else None
                    if closed and ts_close is None:
                        ts_close = ts_open
                    try:
                        pnl = float(row.get("pnl_neto_eur", 0) or 0) if closed else 0.0
                    except ValueError:
                        pnl = 0.0
                    eventos.append((ts_open, ts_close, stake, pnl, closed))
    except Exception:
        pass
    return depositos, eventos


def _sports_capital_en_free_usdc(ts: datetime, depositos: list | None = None,
                                  eventos: list | None = None) -> float:
    """03-Sep (sustituye TRES intentos previos en la misma sesión -- ver
    `feedback_no_mezclar_dinero_sports_cripto_03sep` en memoria nativa --
    mismo bug de fondo repetido por cuarta vez desde 31-Ago: un trade de
    sports se leía como ganancia/pérdida de cripto).

    Petición explícita de Javi: "el dinero de sports va por un lado y el
    de cripto por otro, los trades de sports se tienen que ajustar al
    dinero de sports y los de cripto a cripto, no puedes estar mezclando
    así."

    Intento 1 (día anterior, cash-flow por día Madrid, ya borrado):
    asumía que `/value` tarda "horas" en reflejar una posición nueva y
    compensaba con un débito/crédito de UN DÍA ENTERO -- el 03-Sep
    `/value` reflejó la posición nueva en 11 minutos, no horas, y la
    compensación quedó sobrando (+1,05€ de más en `pnl_hoy_real`).

    Intento 2 (misma sesión, ~20 min después): `deposits + realizado -
    stakes_abiertos` restado de `total_bruto` (free_usdc+positions_value)
    -- si `/value` SÍ se actualiza rápido, `positions_value` ya refleja
    el stake nuevo, y sumarlo (signo `+stakes_abiertos`) lo contaba dos
    veces sobre esa misma base.

    Intento 3 (misma sesión, ~15 min después): cambiar la base a
    `free_usdc` (sin lag de API, ambigüedad cero) pero SIN el término de
    stakes abiertos -- error en la dirección contraria: cuando sports
    ABRE una posición, el stake sale de `free_usdc` de verdad (movimiento
    de caja real), y sin restar ese movimiento aparte, esa salida de caja
    se atribuía entera a cripto (-1,05€ de más).

    Fix real, verificado con aritmética completa contra los 3 trades
    reales de cripto del día (-3,33€) antes de aceptarlo: la caja de
    sports dentro de `free_usdc` en el instante `ts` es su equity total
    (depósitos + PnL realizado de CERRADOS) MENOS lo que tiene
    ACTUALMENTE inmovilizado en posiciones abiertas (ese dinero ya no
    está en `free_usdc`, está en `positions_value`, y no hace falta
    tocar ese lado para nada -- por eso no hay término de `positions_
    value` en ningún sitio de esta función, a diferencia de los intentos
    1 y 2):

        sports_en_free_usdc(ts) = depósitos(ts) + realizado_cerrados(ts)
                                   - stakes_abiertos_en(ts)

    Caveat aceptado y acotado (no un lag de API, estructural): la
    revalorización NO REALIZADA de una posición de sports abierta (su
    `positions_value` real puede diferir un poco de su stake por
    spread/movimiento de precio) no se atribuye a nadie hasta que la
    posición cierra -- acotado por el stake máximo de sports (2€) y el
    nº de posiciones concurrentes (normalmente 1-2), verificado hoy en
    ~1 céntimo por posición, no ~1€ como los intentos anteriores.

    Fail-safe: cualquier error (ficheros de sports ausentes/corruptos)
    devuelve 0.0 -- sin este ajuste el comportamiento es "sports en 0€",
    igual que un sports inactivo.

    `depositos`/`eventos` opcionales (`_cargar_sports_eventos()`, ver esa
    función) -- si no se pasan, se cargan aquí una sola vez para esta
    llamada suelta; el llamante que itera muchos `ts` (`_daily_real_pnl_
    balance()`) los carga UNA vez fuera del bucle y los pasa siempre,
    para no reabrir los ficheros por cada fila de `balance_history.csv`."""
    if depositos is None or eventos is None:
        depositos, eventos = _cargar_sports_eventos()

    total = 0.0
    for fecha_dt, eur in depositos:
        if fecha_dt <= ts:
            total += eur

    for ts_open, ts_close, stake, pnl, closed in eventos:
        if ts_open > ts:
            continue  # todavía no había abierto en ts
        if closed and ts_close is not None and ts_close <= ts:
            # ya realizado en ts -- suma el PnL (el stake ya volvió a
            # free_usdc con la redención, no se resta aparte)
            total += pnl
        else:
            total -= stake  # seguía abierta en ts (o cerró después de ts)
            # -- ese stake ya había salido de free_usdc, no cuenta como
            # caja de sports todavía disponible
    return total


def _daily_real_pnl_balance(depositos: list, free_usdc_bruto_actual: float,
                            ts_actual: str) -> tuple[list, float, float]:
    """PnL real por día desde balance_history.csv (delta de `free_usdc`
    on-chain por día MADRID) -- reemplaza a _daily_real_pnl() (31-Jul, bug diagnosticado
    en sesión: comparado día a día contra balance_history.csv, el método viejo
    de actividad on-chain (buy/redeem) desviaba hasta -9.31$/+7.42$ en un solo
    día, ej. 29-Jul real=+8.13 vs activity=-1.18, 30-Jul real=-10.90 vs
    activity=-3.48 -- una posición que ABRE un día y REDIME al siguiente
    (habitual cerca de medianoche UTC) atribuye el cash-flow al día del
    evento, no al día real del resultado, desplazando PnL entre días
    contiguos. Además el método viejo tenía `limit=500` sin paginación
    (riesgo de truncar actividad antigua en silencio) y asumía que TODO
    evento TRADE es una compra (frágil si algún día hay ventas reales, ej.
    Smart Exit).

    Día MADRID (no UTC) a propósito: es el mismo criterio que usa
    dashboard_server.py para 'pnl_hoy' (el lado modelo/trades.csv) -- antes
    los dos lados del dashboard usaban fronteras de día distintas (UTC aquí,
    Madrid allá), comparando cifras de "hoy" que en realidad correspondían
    a ventanas de tiempo distintas.

    03-Sep: usa `free_usdc` (caja líquida real, sin ambigüedad de API) en
    vez de `total_bruto`/`total` (que incluyen `positions_value`, sujeto al
    lag de `/value` que causó 3 incidentes reales de dinero mezclando
    cripto/sports -- 31-Ago, 01-Sep, 03-Sep, ver `_sports_capital_en_
    free_usdc()`). Cada snapshot se neta de sports ANTES de bucketear por
    día -- ya no existe un ajuste "por día" separado para sports, así una
    posición de sports abriéndose/cerrándose nunca puede aparecer como
    ganancia o pérdida de cripto. `positions_value` (de cripto o de
    sports) queda fuera de este cálculo por completo -- ver caveat acotado
    en el docstring de `_sports_capital_en_free_usdc()`.
    """
    from collections import defaultdict
    from zoneinfo import ZoneInfo

    # `free_usdc` en balance_history.csv ya sale NETO de la resta de
    # `capital_ajeno_en_wallet_compartida()` (ver fetch_balance_real() --
    # `free` se muta ANTES de escribirse) -- no sirve como base aquí,
    # restaríamos sports dos veces con dos fórmulas distintas. `total_bruto`
    # y `positions_value` sí quedan crudos (nunca se tocan), así que se
    # reconstruye el free_usdc CRUDO como total_bruto - positions_value.
    #
    # 03-Sep (`/code-review`, hallazgo real de rendimiento): depósitos y
    # trades de sports se cargan UNA sola vez aquí, no una vez POR FILA de
    # balance_history.csv (5978 filas hoy, creciendo en cada trade real) --
    # ver `_cargar_sports_eventos()`.
    sports_dep, sports_ev = _cargar_sports_eventos()
    filas = []
    if HIST_PATH.exists():
        with open(HIST_PATH, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                try:
                    dt = datetime.fromisoformat(r["ts"].replace("Z", "+00:00"))
                    bruto_raw = r.get("total_bruto")
                    total_bruto_fila = float(bruto_raw) if bruto_raw not in (None, "") else float(r["total"])
                    free_bruto = total_bruto_fila - float(r["positions_value"])
                except (ValueError, KeyError):
                    continue
                filas.append((dt, free_bruto - _sports_capital_en_free_usdc(dt, sports_dep, sports_ev)))
    # snapshot actual (aún no escrito en el CSV -- se añade tras esta llamada)
    try:
        dt_actual = datetime.fromisoformat(ts_actual)
        filas.append((dt_actual,
                      free_usdc_bruto_actual - _sports_capital_en_free_usdc(dt_actual, sports_dep, sports_ev)))
    except ValueError:
        pass
    if not filas:
        return [], None, None
    filas.sort()

    madrid = ZoneInfo("Europe/Madrid")
    dep_por_dia = defaultdict(float)
    for d in depositos:
        dep_por_dia[d.get("fecha", "")] += float(d.get("eur") or 0)

    # último snapshot de cada día Madrid = "cierre" de ese día (ya neto de sports)
    cierre_por_dia = {}
    for dt, total in filas:
        dia = dt.astimezone(madrid).strftime("%Y-%m-%d")
        cierre_por_dia[dia] = total

    dias = sorted(cierre_por_dia.keys())
    daily_list = []
    prev = None
    for dia in dias:
        if prev is not None:
            ajeno_dia = dep_por_dia.get(dia, 0.0)  # solo depósitos PROPIOS de cripto -- sports ya se netó por snapshot arriba
            delta = cierre_por_dia[dia] - prev - ajeno_dia
            daily_list.append({"date": dia, "pnl": round(delta, 2)})
        prev = cierre_por_dia[dia]

    hoy = datetime.now(madrid).strftime("%Y-%m-%d")
    pnl_hoy = next((d["pnl"] for d in daily_list if d["date"] == hoy), 0.0)
    hace_7d = (datetime.now(madrid) - timedelta(days=7)).strftime("%Y-%m-%d")
    pnl_7d = round(sum(d["pnl"] for d in daily_list if d["date"] >= hace_7d), 2)
    return daily_list, pnl_hoy, pnl_7d


def _daily_real_pnl(wallet: str) -> tuple[list, float, float]:
    """PnL real por día desde la actividad on-chain (redeems − buys por fecha).

    Base caja: para mercados up/down (15min) compra y redención caen el mismo
    día, así que el flujo neto diario ≈ PnL realizado real de ese día. La suma
    cuadra con la variación del balance del wallet. Best-effort: si falla,
    devuelve vacío (el balance sigue siendo la métrica crítica).
    """
    from collections import defaultdict
    # limit=500 (23-Jul): Polymarket empezó a rechazar >500 con 400 "max
    # activity limit of 500 exceeded" (~22:19-22:32 UTC 23-Jul, cambio de
    # la API, sin tocar este código) -- el 400 se tragaba en el except de
    # abajo y dejaba pnl_hoy_real/pnl_7d_real/daily_real en None/[] en
    # silencio durante horas.
    r = requests.get(f"{DATA_API}/activity",
                     params={"user": wallet, "limit": 500}, timeout=25)
    r.raise_for_status()
    evs = r.json()
    if not isinstance(evs, list):
        return [], 0.0, 0.0
    daily = defaultdict(float)
    for a in evs:
        t = (a.get("type") or "").upper()
        try:
            u = float(a.get("usdcSize") or 0)
            day = datetime.fromtimestamp(int(a.get("timestamp") or 0),
                                         tz=timezone.utc).strftime("%Y-%m-%d")
        except Exception:
            continue
        if t == "TRADE":
            # ⚠️ Asume TODO TRADE es compra (sin leer campo `side`) — cierto
            # hoy porque live_trade.py solo envía side="BUY". Si Smart Exit
            # (ver MEMORY.md, paso 1 en marcha) añade ventas de salida
            # anticipada, un TRADE de venta sumaría aquí como si fuera una
            # compra más, invirtiendo el signo real de ese evento. Desde
            # 13-Jul pnl_hoy_real alimenta directamente el freno diario
            # live (live_stake.pnl_live_hoy) — revisar este `if` (leer
            # `side`) ANTES de activar ventas reales.
            daily[day] -= u          # compra: USDC sale
        elif t == "REDEEM":
            daily[day] += u          # redención: USDC entra
    daily_list = [{"date": d, "pnl": round(v, 2)} for d, v in sorted(daily.items())]
    hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    d7 = (datetime.now(timezone.utc) - timedelta(days=7)).strftime("%Y-%m-%d")
    pnl_hoy = round(daily.get(hoy, 0.0), 2)
    pnl_7d = round(sum(v for d, v in daily.items() if d >= d7), 2)
    return daily_list, pnl_hoy, pnl_7d


def fetch_balance_real() -> dict:
    """Consulta el balance real. Lanza excepción si algo falla (fail-closed)."""
    wallet = os.getenv("POLY_DEPOSIT_WALLET")
    client = _get_clob_client()
    if not wallet:
        wallet = os.getenv("POLY_DEPOSIT_WALLET")
    free = _free_usdc(client)
    free_bruto = free  # 03-Sep: capturado ANTES de restar sports (igual que
    # total_bruto abajo) -- lo necesita _daily_real_pnl_balance() para
    # netear con su propia fórmula (_sports_capital_en_free_usdc), sin
    # heredar la resta de capital_ajeno de más abajo y contar dos veces.
    pos, posiciones_wallet = _positions_value(wallet)
    total = round(free + pos, 4)
    pusd_onchain = _saldo_pusd_onchain()
    pusd_no_reflejado = (round(pusd_onchain - free, 4)
                          if pusd_onchain is not None and pusd_onchain > free else None)
    total_bruto = total  # 27-Ago noche: guardado ANTES de restar sports --
    # única forma de que reconciliar_sports.py pueda aislar por diferencia
    # cuánto del movimiento real de la wallet es atribuible a sports (ver
    # docstring de reconciliar_sports.py). Sin esto, la resta de más abajo
    # destruye la información necesaria para reconciliar sports por su cuenta.

    # 27-Ago (bug real, encontrado por Javi al ver +5€ de sports colados en
    # el dashboard de cripto): esta wallet on-chain es COMPARTIDA con sports
    # (mismo mecanismo usado para el bankroll operativo de Kelly/circuit
    # breaker de cripto vía live_stake.bankroll_actual(), que lee `total`
    # de este mismo snapshot -- no solo el dashboard). Mismo criterio: SOLO
    # sports (nunca weather, ver docstring de `_sports_positions_value_
    # actual`). 03-Sep noche: sustituido `live_stake._capital_ajeno_en_
    # wallet_compartida()` (bug real, doble resta del stake abierto + coste
    # en vez de valor de mercado -- ver docstring de
    # `_sports_positions_value_actual`) por las dos piezas YA correctas y
    # ya revisadas por separado: caja exacta (`_sports_capital_en_free_
    # usdc()`, usada hasta hoy solo en la reconstrucción histórica) y
    # valor de mercado real de posiciones (`_sports_positions_value_
    # actual()`, nueva).
    try:
        capital_ajeno_cash = _sports_capital_en_free_usdc(datetime.now(timezone.utc))
    except Exception:
        capital_ajeno_cash = 0.0
    try:
        capital_ajeno_pos = _sports_positions_value_actual(wallet, posiciones_wallet)
    except Exception:
        capital_ajeno_pos = 0.0
    if capital_ajeno_cash or capital_ajeno_pos:
        free = round(free - capital_ajeno_cash, 4)
        # `pos` NO se toca aquí a propósito (/code-review 03-Sep, hallazgo
        # real): `_daily_real_pnl_balance()` reconstruye `free_bruto =
        # total_bruto_fila - positions_value` asumiendo que ambos son
        # crudos (comentario de `total_bruto` arriba) -- restar sports de
        # `pos` también rompería esa reconstrucción y reintroduciría el
        # mismo bug de mezcla sports/cripto por la puerta de atrás
        # (`pnl_hoy_real` volvería a oscilar con el mark-to-market de
        # sports). `total` sí se corrige (lo que de verdad alimenta
        # `bankroll_actual()`/Kelly/circuit breaker), restando el
        # componente de posiciones aparte, sin persistir esa resta en
        # `pos`/`positions_value`.
        total = round(total - capital_ajeno_cash - capital_ajeno_pos, 4)

    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    depositos = _cargar_depositos_config()
    # PnL real por día — best-effort (no debe tumbar el balance si algo falla).
    # 31-Jul: usa balance_history.csv (ground truth), NO el feed de actividad
    # (buy/redeem) -- ver docstring de _daily_real_pnl_balance, bug real
    # diagnosticado con Javi (desviaciones de hasta 9$/día).
    try:
        daily_real, pnl_hoy_real, pnl_7d_real = _daily_real_pnl_balance(depositos, free_bruto, ts)
    except Exception:
        daily_real, pnl_hoy_real, pnl_7d_real = [], None, None
    deposito_total = (sum(float(d["eur"]) for d in depositos)
                      if depositos else DEPOSITO_INICIAL)
    pnl_desglose = _pnl_por_deposito(depositos)
    return {
        "ts": ts,
        "wallet": wallet,
        "free_usdc": round(free, 4),
        "positions_value": round(pos, 4),
        "total": total,
        "total_bruto": total_bruto,  # wallet compartida completa, SIN restar sports
        "deposito_inicial": round(deposito_total, 4),  # total acumulado (sum de todos los depósitos)
        "pnl_real": round(total - deposito_total, 4),
        "pnl_por_deposito": pnl_desglose,              # nuevo: desglose por período
        "pusd_onchain": round(pusd_onchain, 4) if pusd_onchain is not None else None,
        "pusd_no_reflejado_en_collateral": pusd_no_reflejado,  # informativo, ver _saldo_pusd_onchain
        "daily_real": daily_real,
        "pnl_hoy_real": pnl_hoy_real,
        "pnl_7d_real": pnl_7d_real,
    }


def _append_history(snap: dict) -> None:
    """Serie temporal del balance real (para la equity curve fiel).
    `total_bruto` al FINAL a propósito (27-Ago noche) -- ~5300 filas ya
    escritas con el header viejo, una columna en medio habría desalineado
    todo bajo DictReader (mismo criterio que la migración de
    wallet_mirror_sniper_dry_run.csv el mismo día)."""
    nuevo = not HIST_PATH.exists()
    with open(HIST_PATH, "a", encoding="utf-8") as f:
        if nuevo:
            f.write("ts,free_usdc,positions_value,total,pnl_real,total_bruto\n")
        f.write(f"{snap['ts']},{snap['free_usdc']},{snap['positions_value']},"
                f"{snap['total']},{snap['pnl_real']},{snap.get('total_bruto', '')}\n")


def actualizar_balance_real() -> dict | None:
    """Refresca el cache de balance AHORA (fetch + write). Guardado: nunca lanza.

    Pensado para engancharse tras abrir/cerrar un trade real, de modo que el
    dashboard y los mensajes de Telegram reflejen el balance del wallet al
    instante en vez de esperar al cron de 15min. Devuelve el snapshot o None.
    """
    try:
        snap = fetch_balance_real()
        CACHE_PATH.write_text(json.dumps(snap, indent=1), encoding="utf-8")
        try:
            _append_history(snap)
        except Exception:
            pass
        return snap
    except Exception:
        return None


def cargar_balance_real(max_edad_s: int | None = None) -> dict | None:
    """Lee el JSON cacheado. Devuelve None si falta o está rancio (fail-closed)."""
    try:
        snap = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return None
    if max_edad_s is not None:
        try:
            ts = datetime.fromisoformat(snap["ts"])
            edad = (datetime.now(timezone.utc) - ts).total_seconds()
            if edad > max_edad_s:
                snap["_rancio"] = True
                snap["_edad_s"] = round(edad)
        except Exception:
            return None
    return snap


def main() -> int:
    try:
        snap = fetch_balance_real()
    except Exception as e:
        # Fail-closed: no tocar el cache; el último bueno se conserva.
        print(f"[live_balance] ERROR fetch (cache intacto): {e!r}", file=sys.stderr)
        return 1
    CACHE_PATH.write_text(json.dumps(snap, indent=1), encoding="utf-8")
    try:
        _append_history(snap)
    except Exception as e:
        print(f"[live_balance] aviso: no se pudo escribir history: {e!r}", file=sys.stderr)
    print(f"[live_balance] real total={snap['total']} USDC "
          f"(libre={snap['free_usdc']} pos={snap['positions_value']}) "
          f"pnl_real={snap['pnl_real']} vs deposito {snap['deposito_inicial']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
