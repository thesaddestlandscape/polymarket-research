#!/usr/bin/env python3
"""vigia_touch_vs_win_p18.py — Vigía de madurez para el gate riguroso
touch-vs-win de P18/Smart Exit (analisis_gate_riguroso_touch_vs_win_28jul.py).

Petición explícita Javi 28-Jul: FAVORITO_CONFIRMADO ya se cerró como
resultado NEGATIVO confirmado (cualquier take-profit probado 0.55-0.85
empeora el PnL real, -3.49€ a -13.72€ peor que sostener — ver memoria
idea_moondev_10_hallazgos_priorizados_28jul). GBM_LATE_15M queda
PENDIENTE: entry medio 0.417 (mucho más barato que FAVORITO_CONFIRMADO,
0.64) es candidato real a que un take-profit SÍ mejore el EV, pero su n
(con al menos un tick vivo + un tick de cierre en smart_exit_prices.csv)
estaba en 33 el 28-Jul, por debajo del gate n>=40 del proyecto — no se
concluye nada con menos.

Este vigía NO decide ni activa nada — solo avisa por Telegram UNA VEZ
(latch) por estrategia cuando cruza n>=40, con el resultado completo del
gate riguroso (Wilson+shuffle+split-half+EV€) ya calculado, para que la
decisión de diseño (cómo repartir el TP por familia, directiva Javi
22-Jul) se tome con el dato ya listo, sin tener que re-lanzar el análisis
a mano cada sesión.

29-Jul: extendido a BALLENAS_TARDIAS (petición Javi: atacar el payout
inverso de esta familia en live, mismo mecanismo touch-vs-win/Flip
Harvester del repo Moon Dev que ya cerró P18 para FAVORITO_CONFIRMADO
-- ver idea_moondev_10_hallazgos_priorizados_28jul). Hoy (29-Jul) n=11
mercados distintos en smart_exit_prices.csv, muy por debajo del gate --
este vigía la vigila igual que a GBM_LATE_15M sin que haga falta
relanzar nada a mano cuando madure. FAVORITO_CONFIRMADO NO se añade --
ya cerrado con resultado NEGATIVO CONFIRMADO, no necesita re-vigilancia.

Cron sugerido: diario, mismo bloque que el resto de vigías 06:xx UTC.
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_gate_riguroso_touch_vs_win_28jul import (  # noqa: E402
    N_MIN_GATE, UMBRALES, cargar, p_lose_touched, wilson_ci, shuffle_test,
    split_half, pnl_hold_euros, pnl_tp_euros,
)

LATCH = REPO / "data" / "live" / "vigia_touch_vs_win_p18_latch.json"
# FAVORITO_CONFIRMADO NO está aquí -- ya cerrado 28-Jul con resultado
# NEGATIVO CONFIRMADO (cualquier TP 0.55-0.85 empeora el PnL real), no
# necesita re-vigilancia. GBM_LATE_15M sigue pendiente de madurar (n=33
# el 28-Jul). BALLENAS_TARDIAS añadida 29-Jul (petición Javi, payout
# inverso en live) -- n=11 mercados hoy, lejos del gate.
ESTRATEGIAS = ["GBM_LATE_15M", "BALLENAS_TARDIAS"]


def _log(msg: str) -> None:
    from datetime import datetime, timezone
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _cargar_latch() -> dict:
    if not LATCH.exists():
        return {}
    try:
        return json.loads(LATCH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _revisar_estrategia(estrategia: str, latch: dict) -> str | None:
    """Devuelve el mensaje a enviar por Telegram si esta estrategia acaba
    de cruzar el gate por primera vez, o None si no hay nada que avisar."""
    ya_avisado = latch.get(estrategia, {}).get("avisado", False)
    resultados = cargar(estrategia)
    n = len(resultados)
    _log(f"{estrategia}: n(tick vivo + cierre)={n} (gate n>={N_MIN_GATE}) — "
         f"{'ya avisado antes' if ya_avisado else 'sin avisar todavía'}")

    if n < N_MIN_GATE or ya_avisado:
        return None

    gano_total = sum(1 for r in resultados if r[2])
    pnl_hold = pnl_hold_euros(resultados)
    lineas = [
        f"🔬 {estrategia} cruzó n≥{N_MIN_GATE} en el gate touch-vs-win de P18 "
        f"(n={n}, win-rate hold={100*gano_total/n:.1f}%, "
        f"PnL hold={pnl_hold:+.2f}€/{pnl_hold/n:+.3f}€ por trade)",
    ]
    for u in UMBRALES:
        r = p_lose_touched(resultados, u)
        if r is None:
            continue
        n_toc, perd, tasa = r
        lo, hi = wilson_ci(perd, n_toc)
        p_sh = shuffle_test(resultados, u)
        pnl_tp, n_vendidos = pnl_tp_euros(resultados, u)
        mejora = pnl_tp - pnl_hold
        lineas.append(
            f"  TP={u:.2f}: tocaron={n_toc} tasa_pérdida={100*tasa:.1f}% "
            f"[{100*lo:.1f}%,{100*hi:.1f}%] p_shuffle={p_sh:.4f} "
            f"PnL={pnl_tp:+.2f}€ mejora={mejora:+.2f}€"
        )
    return "\n".join(lineas)


def main() -> int:
    from shadow_digest import enviar_telegram

    latch = _cargar_latch()
    for estrategia in ESTRATEGIAS:
        msg = _revisar_estrategia(estrategia, latch)
        if msg is None:
            continue
        _log(msg)
        enviar_telegram(msg)
        latch[estrategia] = {"avisado": True}
        LATCH.write_text(json.dumps(latch, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
