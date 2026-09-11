#!/usr/bin/env python3
"""vigia_wallet_mirror_postfix.py -- vigía de la ventana de confianza POST-FIX
de WALLET_MIRROR (14-Ago, petición explícita Javi tras auditar por qué
WALLET_MIRROR llevaba perdidos 5/8 trades reales).

Contexto: el fix de rendimiento reciente (commit 8160213fad, 13-Ago 11:57 UTC,
wallets_operativas_recientes()) resolvió la causa raíz confirmada -- 7/8
trades perdedores/ganadores ocurrieron ANTES del fix, sin filtro de
degradación. Solo hay n=1 trade real bajo el gate nuevo (13-Ago 20:00,
pérdida) -- insuficiente para confirmar que el gate nuevo funciona con
dinero real.

Decisión explícita de Javi 14-Ago (bankroll de emergencia sin más margen,
"no podemos perder más trades"): seguir operando en vivo con vigilancia
estrecha -- pausar SOLO si se acumulan >=2 pérdidas post-fix antes de
llegar a n=15 trades post-fix. Este vigía convierte esa regla en código
que se audita solo (mismo principio de todo el proyecto: nunca prometer
"estar atento", vigilar con un vigía) -- SOLO ALERTA por Telegram, nunca
pausa sola (mismo patrón que vigia_log_growth.py/vigia_slippage_kill_
switch.py) -- la decisión de pausar sigue siendo de Javi.

Cron sugerido: cada 15min (barato, solo lee trades.csv).
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import csv  # noqa: E402
from shadow_digest import enviar_telegram  # noqa: E402

TRADES = REPO / "data" / "live" / "trades.csv"
LOG = REPO / "logs" / "vigia_wallet_mirror_postfix.log"
LATCH = REPO / "data" / "live" / "vigia_wallet_mirror_postfix_latch.json"

FIX_TIMESTAMP = datetime(2026, 8, 13, 11, 57, 7, tzinfo=timezone.utc)
N_MIN_VEREDICTO = 15
MAX_PERDIDAS_ANTES_DE_N = 2


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def _cargar_latch() -> dict:
    try:
        return json.loads(LATCH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _guardar_latch(d: dict) -> None:
    LATCH.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")


def trades_post_fix() -> list:
    if not TRADES.exists():
        return []
    out = []
    with open(TRADES, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if "WALLET_MIRROR" not in (row.get("strategy") or ""):
                continue
            if row.get("status") != "CLOSED":
                continue
            try:
                ts = datetime.fromisoformat(row.get("timestamp_utc", ""))
            except (TypeError, ValueError):
                continue
            if ts < FIX_TIMESTAMP:
                continue
            out.append(row)
    return out


def main() -> int:
    trades = trades_post_fix()
    n = len(trades)
    perdidas = [t for t in trades if float(t.get("pnl_neto_eur") or 0) < 0]
    ganadas = [t for t in trades if float(t.get("pnl_neto_eur") or 0) >= 0]
    pnl_total = sum(float(t.get("pnl_neto_eur") or 0) for t in trades)
    n_perdidas = len(perdidas)
    n_ganadas = len(ganadas)

    _log(f"trades post-fix (>= {FIX_TIMESTAMP.isoformat()}): n={n} "
         f"ganadas={n_ganadas} perdidas={n_perdidas} pnl_total={pnl_total:.4f}")

    latch = _cargar_latch()

    # Caso 1: umbral de pausa alcanzado (>=2 pérdidas antes de n=15) -- avisa UNA vez.
    if n_perdidas >= MAX_PERDIDAS_ANTES_DE_N and n < N_MIN_VEREDICTO and not latch.get("aviso_pausa_enviado"):
        msg = (
            f"🚨 WALLET_MIRROR post-fix: {n_perdidas} pérdidas en solo n={n} trades "
            f"reales (umbral acordado: pausar si >=2 pérdidas antes de n={N_MIN_VEREDICTO}).\n"
            f"PnL post-fix: {pnl_total:+.2f}€. Decisión de pausar pendiente de Javi -- "
            f"este vigía NO pausa solo."
        )
        ok = enviar_telegram(msg)
        _log(f"aviso umbral de pausa enviado (telegram={ok})")
        latch["aviso_pausa_enviado"] = True
        _guardar_latch(latch)

    # Caso 2: n=15 alcanzado -- veredicto final, una vez.
    if n >= N_MIN_VEREDICTO and not latch.get("aviso_veredicto_enviado"):
        hit_pct = 100 * n_ganadas / n if n else 0.0
        msg = (
            f"📊 WALLET_MIRROR post-fix alcanzó n={n} (umbral de veredicto). "
            f"hit={hit_pct:.1f}% ({n_ganadas}W/{n_perdidas}L), pnl_total={pnl_total:+.2f}€. "
            f"Revisar si el gate de rendimiento reciente sostiene edge real."
        )
        ok = enviar_telegram(msg)
        _log(f"aviso veredicto n={N_MIN_VEREDICTO} enviado (telegram={ok})")
        latch["aviso_veredicto_enviado"] = True
        _guardar_latch(latch)

    return 0


if __name__ == "__main__":
    sys.exit(main())
