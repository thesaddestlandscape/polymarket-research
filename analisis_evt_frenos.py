#!/usr/bin/env python3
"""
Propuesta #10 backlog quant-desk: ¿un freno diario/ventana basado en VaR/ES
de cola (EVT) sugeriría un % distinto al 30%/20% fijo actual?

Solo lectura — no toca live_stake.py ni config_live.json. Construye la serie
de PnL diario real (trades.csv, CLOSED) y compara contra freno_diario_pct=0.30.
"""
import csv
from collections import defaultdict
from datetime import datetime

TRADES_CSV = "data/live/trades.csv"
FRENO_DIARIO_PCT = 0.30
FRENO_VENTANA_PCT = 0.20

rows = [r for r in csv.DictReader(open(TRADES_CSV)) if r["status"] == "CLOSED" and r["pnl_neto_eur"]]

por_dia = defaultdict(float)
por_dia_n = defaultdict(int)
for r in rows:
    dia = r["timestamp_utc"][:10]
    por_dia[dia] += float(r["pnl_neto_eur"])
    por_dia_n[dia] += 1

dias = sorted(por_dia)
print(f"Días con trades cerrados: {len(dias)} (n_trades total={len(rows)})")
print(f"{'dia':12} {'n':>3} {'pnl_dia_eur':>12}")
for d in dias:
    print(f"{d:12} {por_dia_n[d]:>3} {por_dia[d]:>12.2f}")

pnls = [por_dia[d] for d in dias]
peor = min(pnls)
mejor = max(pnls)
print(f"\nn_dias={len(dias)} peor_dia={peor:.2f} mejor_dia={mejor:.2f}")
print("⚠️ n<15 (regla del proyecto): NINGUNA conclusión estadística válida — "
      "esto es solo una foto descriptiva, no un ajuste EVT/VaR fiable.")

# Bankroll aproximado al inicio de cada día operativo (para expresar el peor
# día como % — mismo criterio que usa freno_diario_pct en live_stake.py).
# No hay snapshot diario de bankroll_inicio_dia guardado fuera de logs, así
# que se aproxima con el bankroll operativo declarado en CLAUDE.md (25.44€)
# como referencia de orden de magnitud, NO como serie real.
BANKROLL_REF = 25.44
print(f"\nComo % de un bankroll de referencia ({BANKROLL_REF}€, orden de magnitud, "
      f"NO el bankroll real de cada día):")
print(f"  peor día: {peor/BANKROLL_REF*100:.1f}% (freno_diario_pct actual={FRENO_DIARIO_PCT*100:.0f}%)")

print("""
Veredicto: con n<15 días de histórico (y 2 de ellos correspondientes al
congelamiento 03-05 Jul, ruido de reapertura, no representativos) no hay
base para ajustar una distribución de cola (Hill estimator, Pareto
generalizada, lo que pide la propuesta #10) — cualquier percentil que salga
de 6-7 puntos es puro artefacto de muestra pequeña, exactamente el tipo de
conclusión que el manual operativo del proyecto prohíbe (n<15).

Recomendación: NO implementar EVT/VaR ahora. Revisar cuando el histórico de
días operativos (fuera de congelaciones) llegue a n≥20-30 — entonces sí
tiene sentido ajustar una Pareto generalizada a la cola de pérdidas diarias
y comparar el VaR/ES resultante contra el 30%/20% fijo actual. Hasta
entonces, los frenos fijos actuales (30% diario, 20% ventana, ambos ya
ajustados a mano tras incidentes reales del 03-Jul) siguen siendo la mejor
opción disponible — no hay señal de que estén mal calibrados, solo falta
dato para calibrarlos de forma más rigurosa.
""")
