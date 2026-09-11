# SKILL.md — Memoria institucional del bot Polymarket
# Este fichero es leído por shadow_predict.py al inicio de cada run.
# Es actualizado automáticamente por shadow_postmortem.py tras cada resolución.
# NO modificar manualmente las secciones marcadas como [AUTO].

---

## PRINCIPIOS FUNDAMENTALES

1. **Optimizar EV, no win rate.** Un 60% de aciertos con edge real supera un 90% sin edge.
2. **El libro de órdenes manda.** El precio de mercado ya incorpora toda la información pública.
3. **Señal fresca > señal histórica.** Posiciones antiguas de wallets son ruido. Compras recientes son señal.
4. **Los mercados de predicción convergen a 0 o 1.** No hacen mean-reversion.
5. **Menos operaciones, más convicción.** Filtrar agresivamente es mejor que disparar mucho.
6. **La rentabilidad emerge de la consistencia.** Aplicar el edge de forma disciplinada en cada operación es el mecanismo que produce rentabilidad a largo plazo. No son alternativas — sin consistencia no hay rentabilidad real.

---

## ESTRATEGIAS ACTIVAS

### PRICE_MOMENTUM
- **Lógica**: Tendencia exponencial del precio YES en las últimas 6h (half-life=3h)
- **Condiciones de entrada**:
  - ≥5 snapshots en las últimas 6h
  - Drift > 1.5% respecto a media ponderada
  - ≥60% de pasos consecutivos en la dirección del drift
  - Spread ≤ 8%
  - Liquidez ≥ 500 USDC
- **Estado**: ACTIVA desde 2026-06-22
- **Resultados**: Sin datos suficientes aún (< 24h de vida)

### SMART_FLOW_1H
- **Lógica**: Flujo neto de compras reales (BUY, no SELL, no BOT) en última 1h
- **Condiciones de entrada**:
  - ≥3 wallets distintas en lado dominante
  - Imbalance ≥ 70% (dominante/total)
- **Estado**: ACTIVA desde 2026-06-22
- **Resultados**: Sin datos suficientes aún (< 24h de vida)
- **Referencia**: Evolución de SMART_FLOW (4h) que tuvo 82-89% win rate histórico

### BINANCE_UPDOWN
- **Lógica**: Señal de momentum de klines Binance 1-min para mercados Up/Down
- **Condiciones de entrada**:
  - Pregunta contiene "up or down" O "arriba o abajo"
  - Liquidez > 100 USDC
  - price_yes válido (no vacío)
  - Klines disponibles (≥6 velas)
  - Edge neto > 4% tras slippage
- **Estado**: ACTIVA desde 2026-06-22
- **Resultados**: Sin datos suficientes aún

---

## ESTRATEGIAS ELIMINADAS (NO RESUCITAR)

| Estrategia | Win Rate | Trades | P&L | Motivo eliminación |
|---|---|---|---|---|
| COPY_WALLETS | 3% | 269 | -225€ | Lee posiciones históricas (stale), no actividad reciente |
| CONSENSUS_WEIGHTED | 1% | 235 | -211€ | Misma raíz que COPY_WALLETS, posiciones antiguas = ruido |
| POLYMARKET_SPOT_DIVERGENCE | 8% | 116 | -91€ | Polymarket ajusta precios en segundos, no hay lag explotable |
| MEAN_REVERSION | 0% | 61 | -56€ | Los mercados de predicción convergen a 0/1, no revierten a 0.5 |
| SPOT_MOMENTUM_CORTO | 9% | 22 | -17€ | Señal demasiado ruidosa en horizonte corto |
| CONSENSUS_TURBO | 0% | 1 | -0.92€ | Variante de CONSENSUS_WEIGHTED, mismos problemas |

---

## REGLAS DE FILTRADO GLOBAL

### Filtros de mercado (aplicar antes de cualquier estrategia)
- **Horizonte mínimo**: 3 minutos (cubre mercados Up/Down 5m)
- **Horizonte máximo**: 1 año
- **price_yes**: debe estar entre 0.01 y 0.99 (excluir mercados ya resueltos)
- **Liquidez mínima**: 500 USDC para mercados de largo plazo
- **Liquidez mínima Up/Down**: 100 USDC
- **No operar** si spread > 8%

### Slippage y edge
- **SLIPPAGE_ESTIMADO**: 0.02 (2%)
- **EDGE_MINIMO**: 0.02 (2%) — edge neto mínimo tras slippage para operar
- **Edge bruto mínimo real**: 4% (EDGE_MINIMO + SLIPPAGE = 0.04)

### Kill switch
- Si una estrategia baja del 40% win rate en los últimos 20 trades resueltos → marcar señales como SKIP hasta revisión manual
- Si P&L acumulado del día cae más de 5€ simulados → parar predicciones del día

---

## LECCIONES APRENDIDAS [AUTO]

- 2026-06-22: COPY_WALLETS destruyó 225€ simulados con 3% win rate. Causa: lee posiciones históricas estáticas, no actividad reciente. Regla: estrategia eliminada permanentemente.
- 2026-06-22: CONSENSUS_WEIGHTED destruyó 211€ simulados con 1% win rate. Causa: mismo problema que COPY_WALLETS. Regla: estrategia eliminada permanentemente.
- 2026-06-22: MEAN_REVERSION 0% win rate en 61 trades. Causa: los mercados de predicción convergen hacia 0/1, no revierten a 0.5. Regla: estrategia eliminada permanentemente.
- 2026-06-22: SMART_FLOW (4h) obtuvo 82-89% win rate con 9-11 trades. Causa del éxito: usa actividad reciente real de wallets. Regla: SMART_FLOW_1H hereda esta ventaja.
- 2026-06-22: MICRO_MOMENTUM obtuvo 100% win rate con 2 trades. Causa del éxito: momentum de precio reciente funciona en Polymarket. Regla: PRICE_MOMENTUM es su evolución.
- 2026-06-22: Mercados "arriba o abajo" en español no se detectaban. Regla: BINANCE_UPDOWN ahora detecta ambos idiomas.
- 2026-06-22: Mercados 5min/15min/4h en español no se capturan. Pendiente: ampliar capture_markets.py.

---

## PARÁMETROS GANADORES CONFIRMADOS

- SMART_FLOW con imbalance ≥ 70%: 82-89% win rate histórico (n=9-11)
- MICRO_MOMENTUM activo: 100% win rate (n=2, muestra pequeña)

---

## MERCADOS PRIORITARIOS

### Universo actual capturado
- **Up/Down Hourly** (inglés): BTC, ETH, SOL, XRP, DOGE, BNB, HYPE — ✅ capturados
- **Price targets** (inglés): "Bitcoin above $X on date" — ✅ capturados
- **Largo plazo** (inglés): "Will BTC hit $150k by Dec 2026?" — ✅ capturados

### Universo pendiente de capturar
- **5m** (español): BTC/ETH/SOL/XRP/DOGE/BNB arriba o abajo 5m — ❌ no capturados
- **15m** (español): ídem 15 minutos — ❌ no capturados
- **4h** (español): ídem 4 horas — ❌ no capturados

### Activos monitorizados en Binance
BTC, ETH, SOL, XRP, DOGE, BNB (klines 1-min, 25 velas)

---

## ESTADO DEL SISTEMA

- **Fase actual**: Shadow paper trading (simulación)
- **Bankroll simulado**: 30€ ficticio
- **Apuesta simulada**: 0.90€ por operación
- **Inicio shadow v7**: 2026-06-22
- **Objetivo antes de ir live**: 3 semanas de shadow con win rate estable > 60%
- **Próximo hito**: VPS 24/7 + 48h de simulación continua
- **Live trading**: pendiente (necesita wallet + Polymarket API key)

---
*Última actualización manual: 2026-06-22*
*Próxima actualización automática: shadow_postmortem.py en el siguiente run diario*
