#!/usr/bin/env python3
"""vigia_log_growth.py — Vigía del gate de crecimiento logarítmico (Kelly)
sobre las tuplas YA en pares_permitidos_live (dinero real).

Motivo (21-Jul, hallazgo de /code-review sobre la pausa de FAVORITO_
CONFIRMADO#ETH#60min#BUY_NO): analisis_log_growth.py detectó "payout
inverso" (EV/$ positivo, g(f=10%) negativo) en esa tupla, pero el gate
solo se corre a mano — nada vigilaba si CUALQUIER OTRA tupla live
desarrolla el mismo patrón más adelante. Este vigía cierra ese hueco:
reutiliza gate() de analisis_log_growth.py (misma fórmula, mismo f leído
de config_live.json::riesgo) sobre cada tupla de pares_permitidos_live
(la fuente de verdad — no hay lista propia que mantener sincronizada) y
avisa por Telegram (una vez por tupla, latch) si alguna cae en payout
inverso con n>=15. La decisión de pausar SIEMPRE es de Javi — este script
solo informa, es read-only, no toca config_live.json ni dinero.
"""
import csv
import json
import math
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_log_growth import gate, CONFIG_LIVE, N_MIN

LATCH = REPO / "data/live/vigia_log_growth_latch.json"
TRADES = REPO / "data/live/trades.csv"


def _gate_trades_reales(strategy: str, subtype: str, decision: str, f: float) -> dict:
    """Fallback (13-Ago, hueco Wallet Mirror): gate() de analisis_log_growth
    SIEMPRE da n=0 para cualquier tupla que no pase por el pipeline
    shadow_predict/shadow_resolve (results.csv) -- es el caso de
    WALLET_MIRROR, un pipeline paralelo que solo escribe trades.csv
    (dinero real). Antes esto era un no-op permanente y silencioso: la
    tupla nunca podía "confirmar" ni "fallar" el gate de crecimiento
    porque results.csv nunca tendría filas suyas.

    Usa el retorno REALIZADO real (pnl_neto_eur/stake_eur) de cada trade
    CLOSED en vez de reconstruirlo desde precio_yes_mercado -- ventaja
    real sobre el gate shadow: ya incluye fee+slippage reales, no una
    aproximación (SLIPPAGE constante). Solo se usa cuando el gate shadow
    devuelve n=0 (estrategia sin datos en results.csv) -- no cambia el
    comportamiento de ninguna tupla ya cubierta por results.csv."""
    if not TRADES.exists():
        return {"n": 0}
    rs = []
    with open(TRADES, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if (row.get("strategy") != strategy or row.get("subtype") != subtype
                    or row.get("direction") != decision or row.get("status") != "CLOSED"):
                continue
            try:
                stake = float(row.get("stake_eur") or 0)
                pnl = float(row.get("pnl_neto_eur") or 0)
            except (TypeError, ValueError):
                continue
            if stake > 0:
                rs.append(pnl / stake)
    n = len(rs)
    if n == 0:
        return {"n": 0}
    hit = 100 * sum(1 for x in rs if x > 0) / n
    ev = sum(rs) / n
    g = sum(math.log(1 + f * x) for x in rs) / n
    return {"n": n, "hit_pct": hit, "ev_por_dolar": ev, "growth": g,
            "pasa": n >= N_MIN and g > 0, "fuente": "trades_reales"}


def _tuplas_live() -> list[tuple[str, str, str]]:
    """Misma lógica de parseo que analisis_log_growth.py::main() — no
    duplicar con una regex distinta que pudiera divergir."""
    try:
        config = json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
    except Exception:
        return []
    tuplas = []
    for t in config.get("pares_permitidos_live", []):
        strategy, resto = t.split("#", 1)
        subtype, decision = resto.rsplit("#", 1)
        tuplas.append((strategy, subtype, decision))
    return tuplas


def _direcciones_reales_walletmirror(subtype: str) -> list[str]:
    """13-Ago (bug encontrado al conectar este vigía a WALLET_MIRROR): la
    whitelist usa vocabulario BUY_Up/BUY_Down (mirror_lado crudo del
    trade de la wallet), pero trades.csv registra la dirección REAL de
    la orden en vocabulario BUY_YES/BUY_NO (resuelta por
    _market_id_y_direccion en wallet_mirror_executor_dryrun.py) -- son
    dos vocabularios distintos, un filtro `direction==decision` con el
    token de la whitelist nunca casa con ninguna fila real. Este vigía
    (y probablemente vigia_slippage_kill_switch.py, mismo patrón de
    parseo) necesitan descubrir la dirección real desde trades.csv en
    vez de fiarse del token de pares_permitidos_live para esta
    estrategia en concreto."""
    if not TRADES.exists():
        return []
    dirs = set()
    with open(TRADES, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if (row.get("strategy") == "WALLET_MIRROR" and row.get("subtype") == subtype
                    and row.get("status") == "CLOSED" and row.get("direction")):
                dirs.add(row["direction"])
    return sorted(dirs)


def _f_bankroll() -> float:
    try:
        config = json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
    except Exception:
        return 0.10
    return config.get("riesgo", {}).get("max_pct_bankroll_por_trade", 0.10)


def main() -> int:
    from shadow_digest import enviar_telegram

    latch = {}
    if LATCH.exists():
        try:
            latch = json.loads(LATCH.read_text())
        except Exception:
            latch = {}

    def _evaluar_y_avisar(tupla: str, r: dict, fuente_tag: str = "") -> bool:
        n = r.get("n", 0)
        if n < N_MIN:
            print(f"[vigia_log_growth] {tupla}{fuente_tag}: n={n}<{N_MIN}, sin concluir")
            return False
        print(f"[vigia_log_growth] {tupla}{fuente_tag}: n={n} hit={r['hit_pct']:.1f}% "
              f"EV/$={r['ev_por_dolar']:+.3f} g(f={f:.0%})={r['growth']:+.5f} "
              f"{'PASA' if r['pasa'] else 'NO -- payout inverso'}")
        if r["pasa"]:
            return False
        msg = (
            f"🔔 VIGÍA log-growth: {tupla} (dinero real) — payout inverso\n"
            f"n={n} hit={r['hit_pct']:.1f}% EV/$={r['ev_por_dolar']:+.3f} "
            f"g(f={f:.0%})={r['growth']:+.5f}\n"
            f"EV/$ positivo pero crecimiento compuesto negativo -- mismo "
            f"patrón que FAVORITO_CONFIRMADO#{{BTC,SOL,ETH}}#15min#BUY_NO "
            f"(06-Jul) y #ETH#60min#BUY_NO (21-Jul). Revisar con Javi si "
            f"pausar (mover de pares_permitidos_live a "
            f"candidatos_evaluacion_live, y registrar la condición de "
            f"reapertura en gates_pendientes.json)."
        )
        ok = enviar_telegram(msg)
        latch[tupla] = {"avisado": True, "n": n, "growth": r["growth"],
                         "ev_por_dolar": r["ev_por_dolar"], "telegram_ok": ok}
        print(f"[vigia_log_growth] aviso enviado {tupla} (telegram={ok})")
        return True

    f = _f_bankroll()
    cambiado = False
    subtypes_walletmirror_vistos = set()
    for strategy, subtype, decision in _tuplas_live():
        if strategy == "WALLET_MIRROR":
            # Vocabulario BUY_Up/BUY_Down de la whitelist no coincide con
            # BUY_YES/BUY_NO real de trades.csv -- evaluar UNA vez por
            # subtype con las direcciones REALES encontradas, no con el
            # decision literal de pares_permitidos_live (ver docstring
            # de _direcciones_reales_walletmirror).
            if subtype in subtypes_walletmirror_vistos:
                continue
            subtypes_walletmirror_vistos.add(subtype)
            for direction_real in _direcciones_reales_walletmirror(subtype):
                tupla = f"{strategy}#{subtype}#{direction_real}"
                if latch.get(tupla, {}).get("avisado"):
                    continue
                r = _gate_trades_reales(strategy, subtype, direction_real, f)
                if _evaluar_y_avisar(tupla, r, " [trades_reales]"):
                    cambiado = True
            continue

        tupla = f"{strategy}#{subtype}#{decision}"
        if latch.get(tupla, {}).get("avisado"):
            continue
        r = gate(strategy, subtype, decision, f)
        if r.get("n", 0) == 0:
            r = _gate_trades_reales(strategy, subtype, decision, f)
        fuente_tag = f" [{r['fuente']}]" if r.get("fuente") else ""
        if _evaluar_y_avisar(tupla, r, fuente_tag):
            cambiado = True

    if cambiado:
        LATCH.write_text(json.dumps(latch, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_log_growth] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
