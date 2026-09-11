# TOOLS.md — Herramientas evaluadas

Librerías y APIs analizadas. Estado y cuándo usarlas.

---

## ✅ Útil — Polymarket Paper Trader
**Repo**: https://github.com/Polymarket/polymarket-paper-trader  
**Qué hace**: opera en los mismos order books reales de Polymarket con dinero ficticio. Mismo modelo de tarifas y slippage.

**Por qué nos sirve**:
- Nuestro shadow mode no toca el order book — el slippage está hardcodeado (`SLIPPAGE_ESTIMADO = 0.02`).
- `live_trade.py` nunca ha ejecutado una orden real (STUB).
- El paper trader valida todo el pipeline de ejecución antes de arriesgar USDC.

**Cuándo usarlo**: cuando tengamos credenciales Polymarket (wallet + API key). Conectar **2-3 días en paper** antes del primer trade real para medir slippage real y depurar `live_trade.py`.

**Bloqueante**: probablemente requiere las mismas credenciales que el live. No elimina el setup de MetaMask/USDC, pero sí permite testear sin capital en riesgo.

**Orden correcto**:
```
Shadow (IC/Kelly calibrado) → Paper Trader (validar ejecución) → Live (dinero real)
```

---

## ❌ No útil ahora — ccxt
**Repo**: https://github.com/ccxt/ccxt  
**Qué hace**: biblioteca unificada para operar en 100+ exchanges cripto.

**Por qué no nos sirve**: operamos en Polymarket (prediction market), no en exchanges cripto. Binance solo es fuente de datos de precio — ya funciona con llamadas REST directas en `fetch_binance_klines.py`. Polymarket no está en ccxt.

**Cuándo revisitar**: si algún día hacemos hedging en Binance Futures contra posiciones en Polymarket (estrategia market-neutral). No está en el roadmap.

---

## ❌ No útil ahora — Binance Execution API
**Docs**: https://binance-docs.github.io/apidocs/  
**Qué hace**: API de Binance para ejecutar órdenes, gestionar balances, operar en spot/futuros.

**Por qué no nos sirve**: misma razón que ccxt. Solo usamos Binance como feed de precio/volumen, no para ejecutar trades.

---

## 📚 Referencia futura — Awesome Quant ML Trading
**Repo**: https://github.com/grananqvist/Awesome-Quant-Machine-Learning-Trading  
**Qué es**: lista curada de libros, cursos, papers y librerías de ML para trading algorítmico.

**Lo más relevante para nosotros**:
- **mlfinlab** (Marcos López de Prado): feature engineering financiero — barras por volumen/información, triple barrier labeling, fractional differentiation. Podría mejorar las features del GBM.
- **Papers de microestructura de mercado**: aplicables a ORDER_FLOW_5M (cómo los order books anticipan precio).

**Cuándo revisitar**: cuando el modelo necesite una revisión profunda de features, o cuando tengamos el dataset Jon-Becker y queramos mejorar la calibración del GBM. No es una prioridad mientras haya estrategias con IC positivo esperando pasar a live.

---

## ❌ No útil ahora — fredapi (FRED Macro Data)
**Repo**: https://github.com/mortada/fredapi  
**Qué hace**: acceso a datos macro de la Fed — IPC, tipos de interés, PIB, rendimientos del Tesoro.

**Por qué no nos sirve ahora**: nuestras ventanas son 5-60min — los datos macro son constantes en ese horizonte.

**Cuándo revisitar**:
- Filtro de eventos: evitar operar en ventanas de FOMC o CPI. Pero esas fechas son públicas — basta un CSV, no hace falta la librería.
- H-WEEKLY-PRICE: cuando tengamos n≥40 por par, los datos macro sí podrían mejorar la predicción semanal de BTC/ETH.
- Estrategias de horizonte diario/semanal si el roadmap va en esa dirección.
