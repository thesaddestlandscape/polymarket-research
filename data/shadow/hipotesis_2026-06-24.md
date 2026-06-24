# Hipótesis — 2026-06-24 ~12:00 UTC

*Generadas manualmente con Claude sobre 112 resoluciones acumuladas*

---

### Hipótesis 1: sigma_h como filtro en slots 5min
**Feature**: sigma_h
**Estrategia**: UPDOWN_GBM#5min (ETH y BTC confirmado, SOL tendencia)
**Condición a probar**: gt 0.003
**Razonamiento**: cuando la volatilidad estimada supera 0.003/hora, el GBM genera probabilidades extremas que el mercado de Polymarket no valida. El mercado mantiene el precio en ~0.50 porque sabe que movimientos bruscos revierten. El modelo se equivoca más en entornos volátiles.
**Evidencia**: ETH#5min sigma_h WIN=0.0024 vs LOSS=0.0035 (Δ=46%). BTC#5min WIN=0.0020 vs LOSS=0.0026 (Δ=30%).
**Prioridad**: Alta
**Estado**: PENDIENTE DE IMPLEMENTAR en FEATURE_RULES

---

### Hipótesis 2: pct_spot_vs_ref también importa en #15min
**Feature**: pct_spot_vs_ref
**Estrategia**: UPDOWN_GBM#BTC#15min (y posiblemente otros 15min)
**Condición a probar**: abs_gt 0.05 (mismo umbral que 5min, o quizás más suave ~0.08)
**Razonamiento**: el mismo efecto mean-reversion de los 5min puede estar activo en #15min cuando el spot se ha movido mucho. Con más tiempo, el umbral tolerable es mayor.
**Evidencia**: BTC#15min pct WIN=0.028% vs LOSS=0.060% (Δ=0.032%, las 3 pérdidas tienen pct doble).
**Prioridad**: Alta
**Estado**: FEATURE_RULES ya incluye pct_spot_vs_ref para #15min — esperar a n≥8 en bucket malo para que el postmortem lo active automáticamente.

---

### Hipótesis 3: ORDER_FLOW_5M — subir umbral delta_ratio a ~0.38-0.40
**Feature**: delta_ratio
**Estrategia**: ORDER_FLOW_5M
**Condición a probar**: abs_gt 0.38 (en vez del 0.20 actual)
**Razonamiento**: el lag Binance→Polymarket solo es explotable cuando el desequilibrio de flujo es claramente dominante. Con delta 0.20-0.35 la señal es demasiado débil y ruidosa.
**Evidencia**: delta_ratio WIN=0.445 vs LOSS=0.384 (Δ=0.061). Las victorias tienen delta 16% más alto en promedio.
**Prioridad**: Alta
**Estado**: PENDIENTE — dos opciones: (a) modificar DELTA_MIN directamente, o (b) dejar que FEATURE_RULES + postmortem lo descubran con n≥8.

---

### Hipótesis 4: BTC#5min tiene comportamiento opuesto a ETH/SOL (investigar)
**Feature**: pct_spot_vs_ref
**Estrategia**: UPDOWN_GBM#BTC#5min
**Condición a probar**: posible patrón momentum (ganar cuando pct ALTO, al contrario de ETH/SOL)
**Razonamiento tentativo**: BTC tiene más momentum que los altcoins. Cuando BTC se mueve, continúa; cuando ETH/SOL se mueven, revierten. Podría justificar NO filtrar BTC#5min por pct alto, o incluso usar una señal contraria para ETH/SOL.
**Evidencia**: BTC#5min pct WIN=0.054% vs LOSS=0.023% — OPUESTO al patrón de ETH/SOL.
**Prioridad**: Baja (n=5W/11L, demasiado ruido para actuar)
**Estado**: OBSERVAR. Implementar solo cuando n≥20 en BTC#5min con patrón consistente.
