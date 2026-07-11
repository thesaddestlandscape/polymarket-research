# Estado del bot — 2026-07-11 15:20 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **23.84 $** |
| P&L real total | 🔴 **-1.60 $** |
| P&L real hoy | -1.46 $ |
| P&L real 7 días | +15.85 $ |
| Fees pagados (real) | 7.30 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +975.06 $ |
| P&L sim compuesto | 🟢 +1508.43 $ (ficción Kelly: +5929% s/ operativo) |
| P&L sim hoy (2026-07-11) | 🟢 +229.02 $ |
| Operaciones resueltas | 9347 (5240 WIN / 4107 LOSS) — 56.1% |
| Señales abiertas | 177 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3267 | 61.3% | +0.113 | ➡️ estable | +1062.09$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 664 | 64.8% | +0.147 | ➡️ estable | +293.37$ | 1.47$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 810 | 58.0% | +0.080 | 📈 madura (+0.04) | +178.60$ | 0.80$ | ✅ activa |
| STREAK_FADE_15M | 131 | 61.8% | +0.117 | 📈 madura (+0.12) | +19.89$ | 1.17$ | ✅ activa |
| ORDER_FLOW_5M | 1574 | 51.3% | +0.013 | ➡️ estable | +17.53$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 49 | 63.3% | +0.127 | 📈 madura (+0.17) | +12.80$ | 1.27$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 283 | 38.9% | -0.111 | 📈 madura (+0.09) | +6.08$ | 0.50$ | ⚠️ IC negativo |
| UPDOWN_GBM | 1268 | 48.7% | -0.013 | 📈 madura (+0.03) | +5.78$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| STREAK_FADE_5M | 1 | 100.0% | +0.008 | — | +0.49$ | 0.50$ | ⏳ acumulando |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 134 | 34.3% | -0.154 | 📉 agota (-0.12) | -0.51$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 175 | 57.1% | +0.071 | 📈 madura (+0.17) | -13.32$ | 0.71$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 506 | 66.2% | +0.161 | ➡️ estable | -27.53$ | 1.61$ | ✅ activa |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-11T15:19 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 11, 11:00AM-11:15AM ET… | ✅ WIN | +0.91$ |
| 2026-07-11T15:19 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 11, 11:00AM-11:15AM ET… | ❌ LOSS | -0.51$ |
| 2026-07-11T15:19 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 11, 11:00AM-11:15AM ET… | ✅ WIN | +1.41$ |
| 2026-07-11T15:19 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 11, 11:00AM-11:15AM ET… | ✅ WIN | +1.53$ |
| 2026-07-11T15:16 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 11, 11:00AM-11:15AM ET… | ✅ WIN | +0.15$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-11T15:19 UTC | rechazos 1h: 2 (rango=0, spike=0)

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,358.85 | 0.1min |  |
| ✅ ETH | $1,817.88 | 0.1min |  |
| ✅ SOL | $78.47 | 0.1min |  |
| ✅ XRP | $1.12 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,360.90 | consenso |  |
| ETH | $1,817.88 | consenso |  |
| SOL | $78.47 | consenso |  |
| XRP | $1.12 | consenso |  |

**Alertas activas:**
- ⚠ rechazos_1h:2 (rango=0, spike=0)

---
*Actualizado automáticamente cada ~60s por el fast loop*