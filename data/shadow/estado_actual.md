# Estado del bot — 2026-07-12 01:13 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **17.99 $** |
| P&L real total | 🔴 **-7.45 $** |
| P&L real hoy | +0.00 $ |
| P&L real 7 días | +10.01 $ |
| Fees pagados (real) | 7.61 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1071.36 $ |
| P&L sim compuesto | 🟢 +1654.05 $ (ficción Kelly: +6502% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +49.34 $ |
| Operaciones resueltas | 10085 (5686 WIN / 4399 LOSS) — 56.4% |
| Señales abiertas | 152 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3407 | 61.2% | +0.112 | ➡️ estable | +1092.42$ | 1.12$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 783 | 64.9% | +0.148 | 📉 agota (-0.05) | +356.56$ | 1.48$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 949 | 57.9% | +0.078 | ➡️ estable | +210.50$ | 0.78$ | ✅ activa |
| STREAK_FADE_15M | 139 | 61.2% | +0.110 | 📈 madura (+0.15) | +19.02$ | 1.10$ | ✅ activa |
| ORDER_FLOW_5M | 1579 | 51.4% | +0.014 | ➡️ estable | +18.78$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 59 | 62.7% | +0.123 | ➡️ estable | +16.77$ | 1.23$ | ✅ activa |
| UPDOWN_GBM | 1297 | 49.1% | -0.009 | 📈 madura (+0.05) | +15.10$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 302 | 38.4% | -0.115 | ➡️ estable | +8.19$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| STREAK_FADE_5M | 68 | 52.9% | +0.029 | ➡️ estable | +1.24$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 689 | 66.5% | +0.164 | ➡️ estable | -23.96$ | 1.64$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T01:12 | STREAK_FADE_5M#ETH#5min | Ethereum Up or Down - July 11, 9:05PM-9:10PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-12T01:06 | STREAK_FADE_15M#SOL#15min | Solana Up or Down - July 11, 8:45PM-9:00PM ET… | ✅ WIN | +0.83$ |
| 2026-07-12T01:06 | FAVORITO_CONFIRMADO#BTC#15min | Bitcoin Up or Down - July 11, 8:45PM-9:00PM ET… | ✅ WIN | +1.38$ |
| 2026-07-12T01:06 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 11, 8:45PM-9:00PM ET… | ✅ WIN | +1.75$ |
| 2026-07-12T01:06 | GBM_LATE_15M_TARDIO#BTC#15min | Bitcoin Up or Down - July 11, 8:45PM-9:00PM ET… | ✅ WIN | +0.66$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T01:12 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $63,892.99 | 0.1min |  |
| ✅ ETH | $1,793.32 | 0.1min |  |
| ✅ SOL | $76.28 | 0.1min |  |
| ✅ XRP | $1.09 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $63,892.99 | consenso |  |
| ETH | $1,793.57 | consenso |  |
| SOL | $76.15 | consenso |  |
| XRP | $1.09 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*