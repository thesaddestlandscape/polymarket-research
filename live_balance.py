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


def _positions_value_sumada(wallet: str) -> float | None:
    """Suma currentValue de data-api /positions -- fuente independiente de
    /value, usada solo como cross-check (08-11). Devuelve None si la llamada
    falla (best-effort, no debe tumbar _positions_value)."""
    try:
        r = requests.get(f"{DATA_API}/positions", params={"user": wallet}, timeout=20)
        r.raise_for_status()
        d = r.json()
        if not isinstance(d, list):
            return None
        return sum(float(p.get("currentValue") or 0.0) for p in d)
    except Exception:
        return None


def _positions_value(wallet: str) -> float:
    """Valor mark-to-market de las posiciones abiertas (data-api /value),
    con cross-check contra la suma de currentValue de /positions.

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
    """
    r = requests.get(f"{DATA_API}/value", params={"user": wallet}, timeout=20)
    r.raise_for_status()
    d = r.json()
    if isinstance(d, list) and d:
        val = float(d[0].get("value") or 0.0)
    elif isinstance(d, dict):
        val = float(d.get("value") or 0.0)
    else:
        val = 0.0

    suma = _positions_value_sumada(wallet)
    if suma is not None:
        tolerancia = max(_POSITIONS_VALUE_TOLERANCIA_ABS,
                          _POSITIONS_VALUE_TOLERANCIA_PCT * val)
        if abs(val - suma) > tolerancia:
            print(f"⚠️  /value ({val:.4f}€) discrepa de suma /positions "
                  f"({suma:.4f}€) más de la tolerancia ({tolerancia:.2f}€) "
                  f"-- usando suma /positions", file=sys.stderr)
            return suma
    return val


def _daily_real_pnl_balance(depositos: list, total_actual: float,
                            ts_actual: str) -> tuple[list, float, float]:
    """PnL real por día desde balance_history.csv (delta de `total` on-chain
    por día MADRID) -- reemplaza a _daily_real_pnl() (31-Jul, bug diagnosticado
    en sesión: comparado día a día contra balance_history.csv, el método viejo
    de actividad on-chain (buy/redeem) desviaba hasta -9.31$/+7.42$ en un solo
    día, ej. 29-Jul real=+8.13 vs activity=-1.18, 30-Jul real=-10.90 vs
    activity=-3.48 -- una posición que ABRE un día y REDIME al siguiente
    (habitual cerca de medianoche UTC) atribuye el cash-flow al día del
    evento, no al día real del resultado, desplazando PnL entre días
    contiguos. Además el método viejo tenía `limit=500` sin paginación
    (riesgo de truncar actividad antigua en silencio) y asumía que TODO
    evento TRADE es una compra (frágil si algún día hay ventas reales, ej.
    Smart Exit). Esta versión usa la MISMA fuente que ya es "verdad de
    suelo" para real_total/real_pnl -- el delta de balance total incluye
    de forma natural el mark-to-market de posiciones abiertas, así que no
    depende de que compra y redención caigan el mismo día.

    Día MADRID (no UTC) a propósito: es el mismo criterio que usa
    dashboard_server.py para 'pnl_hoy' (el lado modelo/trades.csv) -- antes
    los dos lados del dashboard usaban fronteras de día distintas (UTC aquí,
    Madrid allá), comparando cifras de "hoy" que en realidad correspondían
    a ventanas de tiempo distintas.
    """
    from collections import defaultdict
    from zoneinfo import ZoneInfo

    filas = []
    if HIST_PATH.exists():
        with open(HIST_PATH, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                try:
                    dt = datetime.fromisoformat(r["ts"].replace("Z", "+00:00"))
                    total = float(r["total"])
                except (ValueError, KeyError):
                    continue
                filas.append((dt, total))
    # snapshot actual (aún no escrito en el CSV -- se añade tras esta llamada)
    try:
        filas.append((datetime.fromisoformat(ts_actual), total_actual))
    except ValueError:
        pass
    if not filas:
        return [], None, None
    filas.sort()

    madrid = ZoneInfo("Europe/Madrid")
    dep_por_dia = defaultdict(float)
    for d in depositos:
        dep_por_dia[d.get("fecha", "")] += float(d.get("eur") or 0)

    # último snapshot de cada día Madrid = "cierre" de ese día
    cierre_por_dia = {}
    for dt, total in filas:
        dia = dt.astimezone(madrid).strftime("%Y-%m-%d")
        cierre_por_dia[dia] = total

    dias = sorted(cierre_por_dia.keys())
    daily_list = []
    prev = None
    for dia in dias:
        if prev is not None:
            delta = cierre_por_dia[dia] - prev - dep_por_dia.get(dia, 0.0)
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
    pos = _positions_value(wallet)
    total = round(free + pos, 4)
    total_bruto = total  # 27-Ago noche: guardado ANTES de restar sports --
    # única forma de que reconciliar_sports.py pueda aislar por diferencia
    # cuánto del movimiento real de la wallet es atribuible a sports (ver
    # docstring de reconciliar_sports.py). Sin esto, la resta de más abajo
    # destruye la información necesaria para reconciliar sports por su cuenta.

    # 27-Ago (bug real, encontrado por Javi al ver +5€ de sports colados en
    # el dashboard de cripto): esta wallet on-chain es COMPARTIDA con sports
    # (mismo mecanismo ya documentado en live_stake._capital_ajeno_en_wallet_
    # compartida, usado ahí para el bankroll operativo de Kelly/circuit
    # breaker -- pero live_balance.py, la fuente que alimenta dashboard/
    # /status/pnl_real, seguía usando el `total` crudo sin esta resta).
    # Mismo criterio: SOLO sports (nunca weather, ver docstring del import).
    try:
        from live_stake import _capital_ajeno_en_wallet_compartida
        capital_ajeno = _capital_ajeno_en_wallet_compartida()
    except Exception:
        capital_ajeno = 0.0
    if capital_ajeno:
        free = round(free - capital_ajeno, 4)
        total = round(total - capital_ajeno, 4)

    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    depositos = _cargar_depositos_config()
    # PnL real por día — best-effort (no debe tumbar el balance si algo falla).
    # 31-Jul: usa balance_history.csv (ground truth), NO el feed de actividad
    # (buy/redeem) -- ver docstring de _daily_real_pnl_balance, bug real
    # diagnosticado con Javi (desviaciones de hasta 9$/día).
    try:
        daily_real, pnl_hoy_real, pnl_7d_real = _daily_real_pnl_balance(depositos, total, ts)
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
