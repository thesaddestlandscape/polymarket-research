#!/usr/bin/env python3
"""Vigía diario (21-Jul, petición Javi tras leer el artículo de Sharpe/
retorno ajustado a riesgo: "¿puede la estrategia sobrevivir a su peor
racha?"): re-corre analisis_simulacion_supervivencia_breakers.py cada día
con el bankroll y los parámetros de riesgo REALES de hoy (no una foto
fija de hace una semana), persiste la serie temporal y avisa por
Telegram. "Lo tenemos controlado diariamente" -- textual.

Reusa cargar_trades_por_dia()/simular_desde() de analisis_simulacion_
supervivencia_breakers.py tal cual (no reimplementa la simulación) --
solo añade: (a) parámetros dinámicos leídos de balance_real.json/
config_live.json en vez de defaults fijos por CLI, (b) persistencia de
la serie histórica día a día, (c) aviso Telegram.

objetivo = depósito inicial (25.44€) -- "recuperado" = volver a
break-even, milestone más significativo hoy que un número arbitrario.
suelo/racha/freno_diario = los reales de config_live.json::riesgo.
circuit_breaker (valores base, sin considerar overrides puntuales con
fecha -- esos son excepciones temporales, no el perfil de riesgo estable
que esta simulación evalúa).

Solo lectura -- no toca trades.csv/config_live.json/ninguna decisión.

Cron sugerido: una vez al día (ver crontab, se añade tras este commit).
"""
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_simulacion_supervivencia_breakers import cargar_trades_por_dia, simular_desde  # noqa: E402
from live_balance import cargar_balance_real  # noqa: E402

HIST_PATH = REPO / "data/shadow/supervivencia_breakers_historico.csv"
CONFIG_PATH = REPO / "data/live/config_live.json"


def main() -> int:
    balance = cargar_balance_real()
    if balance is None:
        print("[vigia_supervivencia] sin balance_real.json cacheado -- nada que simular hoy")
        return 0
    bkr_actual = balance["total"]
    deposito_inicial = balance.get("deposito_inicial", 25.44)

    config = json.loads(CONFIG_PATH.read_text())
    cb = config.get("riesgo", {}).get("circuit_breaker", {})
    suelo = cb.get("bankroll_minimo_eur", 1.0)
    racha_max = cb.get("max_perdidas_consecutivas", 4)
    freno_diario = cb.get("freno_diario_pct", 0.30)

    dias_pnl = cargar_trades_por_dia()
    n_dias_hist = len(dias_pnl)

    if bkr_actual <= suelo:
        print(f"[vigia_supervivencia] bankroll actual {bkr_actual:.2f}€ ya está en/bajo el suelo "
              f"({suelo:.2f}€) -- circuit breaker ya debería estar activo, simulación trivial (no se corre).")
        pct_bust = pct_recuperado = pct_inconcluso = None
    else:
        resultados = []
        for start_idx in range(max(n_dias_hist - 2, 0)):
            r, _, _ = simular_desde(dias_pnl, start_idx, bkr_actual, racha_max,
                                    freno_diario, suelo, deposito_inicial)
            resultados.append(r)
        n = len(resultados)
        if n == 0:
            print("[vigia_supervivencia] histórico de trades insuficiente para simular todavía.")
            pct_bust = pct_recuperado = pct_inconcluso = None
        else:
            pct_bust = sum(1 for r in resultados if r == "bust") / n * 100
            pct_recuperado = sum(1 for r in resultados if r == "recuperado") / n * 100
            pct_inconcluso = sum(1 for r in resultados if r == "inconcluso") / n * 100
            print(f"[vigia_supervivencia] bkr={bkr_actual:.2f}€ suelo={suelo:.2f}€ "
                  f"racha_max={racha_max} freno_diario={freno_diario:.0%} "
                  f"objetivo={deposito_inicial:.2f}€ (n_caminos={n}, n_dias_historial={n_dias_hist})")
            print(f"  BUST={pct_bust:.1f}%  RECUPERADO={pct_recuperado:.1f}%  INCONCLUSO={pct_inconcluso:.1f}%")

    hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    nuevo = not HIST_PATH.exists()
    with open(HIST_PATH, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(["fecha", "bkr_actual", "suelo", "racha_max", "freno_diario_pct",
                        "objetivo", "n_dias_historial", "pct_bust", "pct_recuperado", "pct_inconcluso"])
        w.writerow([hoy, round(bkr_actual, 4), suelo, racha_max, freno_diario, deposito_inicial,
                    n_dias_hist,
                    round(pct_bust, 1) if pct_bust is not None else "",
                    round(pct_recuperado, 1) if pct_recuperado is not None else "",
                    round(pct_inconcluso, 1) if pct_inconcluso is not None else ""])

    # Aviso Telegram diario -- "controlado diariamente" (petición explícita
    # Javi 21-Jul). Sin latch a propósito: es un digest diario, no una
    # alerta puntual -- se espera un mensaje por día, no uno la primera
    # vez y silencio después.
    try:
        from shadow_digest import enviar_telegram
        if pct_bust is None:
            msg = (f"📉 Supervivencia circuit breakers ({hoy})\n"
                   f"Bankroll {bkr_actual:.2f}€ — {'ya en/bajo el suelo, sin simular' if bkr_actual <= suelo else 'histórico insuficiente'}")
        else:
            msg = (f"📉 Supervivencia circuit breakers ({hoy})\n"
                   f"Bankroll {bkr_actual:.2f}€ | suelo {suelo:.2f}€ | racha={racha_max} | freno_diario={freno_diario:.0%}\n"
                   f"BUST {pct_bust:.0f}% · RECUPERADO {pct_recuperado:.0f}% · INCONCLUSO {pct_inconcluso:.0f}%\n"
                   f"(n_días_histórico={n_dias_hist} — mejora con cada día real que pasa)")
        ok = enviar_telegram(msg)
        print(f"[vigia_supervivencia] telegram={ok}")
    except Exception as e:
        print(f"[vigia_supervivencia] no se pudo notificar Telegram: {e}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
