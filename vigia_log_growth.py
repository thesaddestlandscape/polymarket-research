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
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_log_growth import gate, CONFIG_LIVE, N_MIN

LATCH = REPO / "data/live/vigia_log_growth_latch.json"


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

    f = _f_bankroll()
    cambiado = False
    for strategy, subtype, decision in _tuplas_live():
        tupla = f"{strategy}#{subtype}#{decision}"
        if latch.get(tupla, {}).get("avisado"):
            continue
        r = gate(strategy, subtype, decision, f)
        n = r.get("n", 0)
        if n < N_MIN:
            print(f"[vigia_log_growth] {tupla}: n={n}<{N_MIN}, sin concluir")
            continue
        print(f"[vigia_log_growth] {tupla}: n={n} hit={r['hit_pct']:.1f}% "
              f"EV/$={r['ev_por_dolar']:+.3f} g(f={f:.0%})={r['growth']:+.5f} "
              f"{'PASA' if r['pasa'] else 'NO -- payout inverso'}")
        if not r["pasa"]:
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
            cambiado = True
            print(f"[vigia_log_growth] aviso enviado {tupla} (telegram={ok})")

    if cambiado:
        LATCH.write_text(json.dumps(latch, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"[vigia_log_growth] ERROR {type(e).__name__}: {e}")
        sys.exit(0)
