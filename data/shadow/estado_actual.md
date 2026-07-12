# Estado del bot — 2026-07-12 18:34 UTC

## Live — dinero real (on-chain)
| | |
|---|---|
| Depósito inicial | 25.44 $ |
| Balance on-chain | **14.13 $** |
| P&L real total | 🔴 **-11.31 $** |
| P&L real hoy | -3.85 $ |
| P&L real 7 días | +6.15 $ |
| Fees pagados (real) | 7.67 $ |

## Shadow — MODELO SIMULADO (no cobrable)
| | |
|---|---|
| P&L fiel (stake fijo 1$) | +1318.87 $ |
| P&L sim compuesto | 🟢 +2141.08 $ (ficción Kelly: +8416% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +536.37 $ |
| Operaciones resueltas | 11277 (6454 WIN / 4823 LOSS) — 57.2% |
| Señales abiertas | 150 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3659 | 61.4% | +0.113 | ➡️ estable | +1229.13$ | 1.14$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 1010 | 66.5% | +0.165 | ➡️ estable | +585.81$ | 1.65$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 1165 | 58.2% | +0.082 | ➡️ estable | +291.80$ | 0.82$ | ✅ activa |
| STREAK_FADE_15M | 154 | 62.3% | +0.122 | 📈 madura (+0.18) | +24.62$ | 1.22$ | ✅ activa |
| UPDOWN_GBM | 1334 | 49.3% | -0.007 | 📈 madura (+0.06) | +23.65$ | 0.50$ | ⚠️ IC negativo |
| LEADLAG_BTC_XRP_15M | 69 | 63.8% | +0.134 | 📈 madura (+0.04) | +21.47$ | 1.34$ | ✅ activa |
| ORDER_FLOW_5M | 1586 | 51.3% | +0.013 | ➡️ estable | +16.48$ | 0.50$ | ✅ activa |
| FAVORITO_CONFIRMADO | 992 | 68.3% | +0.183 | 📈 madura (+0.06) | +12.44$ | 1.83$ | ✅ activa |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 314 | 38.5% | -0.114 | ➡️ estable | +6.21$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 10 | 100.0% | +0.208 | — | +4.00$ | 2.00$ | ✅ activa |
| PRICE_TARGET_GBM | 138 | 34.8% | -0.150 | 📉 agota (-0.11) | +0.19$ | 0.50$ | ⚠️ IC negativo |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| STREAK_FADE_5M | 164 | 46.3% | -0.036 | ➡️ estable | -9.97$ | 0.50$ | ⚠️ IC negativo |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 204 | 57.4% | +0.073 | 📈 madura (+0.24) | -13.93$ | 0.73$ | ✅ activa |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| STREAK_MOM_5M | 309 | 44.3% | -0.056 | 📉 agota (-0.06) | -23.67$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T18:32 | FAVORITO_CONFIRMADO#ETH#5min | Ethereum Up or Down - July 12, 2:25PM-2:30PM ET… | ✅ WIN | +1.27$ |
| 2026-07-12T18:30 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 12, 2:25PM-2:30PM ET… | ✅ WIN | +1.06$ |
| 2026-07-12T18:30 | GBM_LATE_15M_ESPACIO_ATR#ETH#15min | Ethereum Up or Down - July 12, 2:15PM-2:30PM ET… | ✅ WIN | +4.52$ |
| 2026-07-12T18:30 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 12, 2:15PM-2:30PM ET… | ❌ LOSS | -2.04$ |
| 2026-07-12T18:30 | GBM_LATE_15M_TARDIO#ETH#15min | Ethereum Up or Down - July 12, 2:15PM-2:30PM ET… | ❌ LOSS | -0.51$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T18:33 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,034.88 | 0.1min |  |
| ✅ ETH | $1,818.01 | 0.1min |  |
| ✅ SOL | $77.37 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,034.88 | consenso |  |
| ETH | $1,818.01 | consenso |  |
| SOL | $77.33 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*