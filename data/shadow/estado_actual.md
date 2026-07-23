# Estado del bot — 2026-07-23 07:00 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Total depositado | 51.22 $ |
| Balance on-chain | **29.39 $** |
| P&L real total | 🔴 **-21.83 $** |
| P&L real hoy | -1.13 $ |
| P&L real 7 días | -2.04 $ |
| Fees pagados (real) | 9.72 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +3630.76 $ |
| P&L sim compuesto | 🟢 +6853.83 $ (ficción Kelly: +26941% s/ operativo) |
| P&L sim hoy (2026-07-23) | 🟢 +141.97 $ |
| Operaciones resueltas | 30417 (18303 WIN / 12114 LOSS) — 60.2% |
| Señales abiertas | 156 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 7057 | 59.7% | +0.097 | 📉 agota (-0.03) | +2220.22$ | 0.97$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 4256 | 62.8% | +0.128 | 📉 agota (-0.04) | +2193.30$ | 1.28$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 4260 | 58.3% | +0.083 | ➡️ estable | +1309.98$ | 0.83$ | ✅ activa |
| UPDOWN_GBM_15M_TARDIO | 1334 | 66.5% | +0.165 | ➡️ estable | +613.99$ | 1.65$ | ✅ activa |
| UPDOWN_GBM | 2303 | 53.1% | +0.031 | 📈 madura (+0.11) | +200.24$ | 0.50$ | ✅ activa |
| GBM_LATE_15M_PYCONFIRMADO | 240 | 60.8% | +0.107 | 📉 agota (-0.07) | +110.47$ | 1.07$ | ✅ activa |
| FAVORITO_CONFIRMADO | 5309 | 68.8% | +0.187 | ➡️ estable | +91.06$ | 1.87$ | ✅ activa |
| WEEKLY_PRICE | 336 | 68.2% | +0.180 | 📈 madura (+0.21) | +67.16$ | 1.80$ | ✅ activa |
| BALLENAS_CONFIRMADAS_15M | 829 | 62.8% | +0.128 | ➡️ estable | +36.29$ | 1.28$ | ✅ activa |
| STREAK_FADE_15M | 267 | 58.4% | +0.084 | 📉 agota (-0.08) | +32.81$ | 0.84$ | ✅ activa |
| UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 128 | 79.7% | +0.292 | 📈 madura (+0.03) | +25.21$ | 2.00$ | ✅ activa |
| FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 281 | 81.9% | +0.316 | ➡️ estable | +14.66$ | 2.00$ | ✅ activa |
| ORDER_FLOW_5M | 1659 | 51.2% | +0.012 | ➡️ estable | +11.80$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 263 | 51.0% | +0.009 | 📉 agota (-0.17) | +9.67$ | 0.50$ | ✅ activa |
| GBM_LATE_5M | 327 | 47.7% | -0.023 | 📉 agota (-0.18) | +6.54$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M | 336 | 38.7% | -0.112 | ➡️ estable | +4.40$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 11 | 90.9% | +0.190 | — | +3.49$ | 1.90$ | ✅ activa |
| BALLENAS_TARDIAS | 22 | 86.4% | +0.333 | — | +1.06$ | 2.00$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| UPDOWN_GBM_ETH_15M_HORA7 | 11 | 45.5% | -0.021 | — | -0.76$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 331 | 45.6% | -0.044 | 📉 agota (-0.15) | -1.92$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_60M_PYCONFIRMADO | 9 | 11.1% | -0.143 | — | -2.77$ | 0.00$ | 🚫 desactivada |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| PRICE_TARGET_GBM | 150 | 32.7% | -0.171 | 📉 agota (-0.14) | -4.78$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 246 | 45.1% | -0.048 | 📉 agota (-0.06) | -24.96$ | 0.50$ | ⚠️ IC negativo |
| STREAK_MOM_5M | 318 | 44.0% | -0.059 | 📉 agota (-0.09) | -25.84$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-23T06:55 | UPDOWN_GBM_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 23, 2:30AM-2:45AM ET… | ❌ LOSS | -0.85$ |
| 2026-07-23T06:55 | GBM_LATE_15M_ESPACIO_ATR#SOL#15min | Solana Up or Down - July 23, 2:30AM-2:45AM ET… | ✅ WIN | +1.37$ |
| 2026-07-23T06:55 | GBM_LATE_15M_TARDIO#SOL#15min | Solana Up or Down - July 23, 2:30AM-2:45AM ET… | ✅ WIN | +0.81$ |
| 2026-07-23T06:55 | GBM_LATE_15M#SOL#15min | Solana Up or Down - July 23, 2:30AM-2:45AM ET… | ✅ WIN | +1.19$ |
| 2026-07-23T06:55 | BALLENAS_CONFIRMADAS_15M#DOGE#15min | Dogecoin Up or Down - July 23, 2:30AM-2:45AM ET… | ✅ WIN | +0.49$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-23T06:58 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $65,776.41 | 0.1min |  |
| ✅ ETH | $1,924.74 | 0.1min |  |
| ✅ SOL | $77.54 | 0.1min |  |
| ✅ XRP | $1.14 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $65,776.41 | consenso |  |
| ETH | $1,924.74 | consenso |  |
| SOL | $77.53 | consenso |  |
| XRP | $1.14 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*