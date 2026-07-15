# Estado del bot — 2026-07-15 01:58 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **7.10 $** |
| P&L real total | 🔴 **-18.34 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | -16.38 $ |
| Fees pagados (real) | 8.21 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1629.96 $ |
| P&L sim compuesto | 🟢 +2854.92 $ (ficción Kelly: +11222% s/ operativo) |
| P&L sim hoy (2026-07-15) | 🟢 +46.27 $ |
| Operaciones resueltas | 14636 (8499 WIN / 6137 LOSS) — 58.1% |
| Señales abiertas | 64 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 4429 | 60.3% | +0.103 | 📉 agota (-0.03) | +1357.85$ | 1.03$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1709 | 65.4% | +0.154 | ➡️ estable | +1005.47$ | 1.54$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1650 | 58.1% | +0.081 | ➡️ estable | +430.13$ | 0.81$ | ✅ activa |
| UPDOWN_GBM | 1521 | 50.8% | +0.008 | 📈 madura (+0.08) | +67.13$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 111 | 60.4% | +0.102 | 📉 agota (-0.06) | +32.78$ | 1.02$ | ✅ activa |
| STREAK_FADE_15M | 183 | 60.1% | +0.100 | 📈 madura (+0.10) | +20.99$ | 1.00$ | ✅ activa |
| LATE_WINDOW_5MIN | 41 | 73.2% | +0.221 | 📈 madura (+0.06) | +17.23$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1602 | 51.2% | +0.012 | ➡️ estable | +13.74$ | 0.50$ | ✅ activa |
| WEEKLY_PRICE | 239 | 61.1% | +0.110 | 📈 madura (+0.27) | +7.74$ | 1.10$ | ✅ activa |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 326 | 38.3% | -0.116 | ➡️ estable | +3.81$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_PYCONFIRMADO | 12 | 41.7% | -0.043 | — | +0.05$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_5M | 5 | 40.0% | -0.018 | — | -0.57$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_60M_PYCONFIRMADO | 4 | 0.0% | -0.067 | — | -2.04$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 146 | 33.6% | -0.162 | 📉 agota (-0.12) | -2.74$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 1959 | 67.9% | +0.179 | ➡️ estable | -14.58$ | 1.79$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-15T01:57 | ORDER_FLOW_5M#ETH#5min | Ethereum Up or Down - July 14, 9:50PM-9:55PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-15T01:48 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 14, 9:40PM-9:45PM ET… | ✅ WIN | +0.48$ |
| 2026-07-15T01:46 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 14, 9:40PM-9:45PM ET… | ✅ WIN | +0.54$ |
| 2026-07-15T01:46 | GBM_LATE_15M_ESPACIO_ATR#XRP#15min | XRP Up or Down - July 14, 9:30PM-9:45PM ET… | ✅ WIN | +1.84$ |
| 2026-07-15T01:46 | GBM_LATE_15M_TARDIO#XRP#15min | XRP Up or Down - July 14, 9:30PM-9:45PM ET… | ✅ WIN | +1.84$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-15T01:57 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,612.82 | 0.1min |  |
| ✅ ETH | $1,869.03 | 0.1min |  |
| ✅ SOL | $77.43 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,616.40 | consenso |  |
| ETH | $1,869.06 | consenso |  |
| SOL | $77.36 | consenso |  |
| XRP | $1.10 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*