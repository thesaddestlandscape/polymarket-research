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
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from sports_wallet_mirror_sniper import outcome_por_condition_id  # noqa: E402

TRADES = REPO / "data/sports/trades.csv"
LOCK_PATH = REPO / "data/sports/.trades_lock"
FEE = 0.05
MAX_CIDS_POR_CICLO = 20


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
        except Exception as e:
            _log(f"error en ciclo: {type(e).__name__}: {e}")
        time.sleep(args.loop)


if __name__ == "__main__":
    sys.exit(main())
