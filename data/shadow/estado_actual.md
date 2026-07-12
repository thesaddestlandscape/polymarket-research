# Estado del bot — 2026-07-12 02:29 UTC

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
| P&L fiel (stake fijo 1$) | +1101.83 $ |
| P&L sim compuesto | 🟢 +1699.61 $ (ficción Kelly: +6681% s/ operativo) |
| P&L sim hoy (2026-07-12) | 🟢 +94.89 $ |
| Operaciones resueltas | 10185 (5759 WIN / 4426 LOSS) — 56.5% |
| Señales abiertas | 150 |

## Estrategias (visión global)

| Estrategia | n | Win% | IC_efectivo | Tendencia | PNL | Apuesta | Estado |
|---|---|---|---|---|---|---|---|
| GBM_LATE_15M | 3427 | 61.3% | +0.113 | ➡️ estable | +1105.39$ | 1.13$ | ✅ activa |
| GBM_LATE_15M_ESPACIO_ATR | 801 | 65.5% | +0.155 | ➡️ estable | +378.77$ | 1.55$ | ✅ activa |
| GBM_LATE_15M_TARDIO | 969 | 58.2% | +0.082 | ➡️ estable | +219.77$ | 0.82$ | ✅ activa |
| STREAK_FADE_15M | 144 | 61.1% | +0.110 | 📈 madura (+0.16) | +19.13$ | 1.10$ | ✅ activa |
| ORDER_FLOW_5M | 1579 | 51.4% | +0.014 | ➡️ estable | +18.78$ | 0.50$ | ✅ activa |
| LEADLAG_BTC_XRP_15M | 59 | 62.7% | +0.123 | ➡️ estable | +16.77$ | 1.23$ | ✅ activa |
| UPDOWN_GBM | 1298 | 49.2% | -0.008 | 📈 madura (+0.05) | +16.19$ | 0.50$ | ⚠️ IC negativo |
| LATE_WINDOW_5MIN | 35 | 71.4% | +0.203 | 📉 agota (-0.09) | +10.30$ | 2.00$ | ✅ activa |
| GBM_LATE_60M | 302 | 38.4% | -0.115 | ➡️ estable | +8.19$ | 0.50$ | ⚠️ IC negativo |
| RESOLUTION_SNIPER | 8 | 100.0% | +0.160 | — | +3.47$ | 1.60$ | ✅ activa |
| GBM_LATE_15M_MULTIHORIZONTE | 6 | 50.0% | +0.000 | — | -0.08$ | 0.50$ | ⏳ acumulando |
| PRICE_TARGET_GBM | 136 | 34.6% | -0.152 | 📉 agota (-0.13) | -0.14$ | 0.50$ | ⚠️ IC negativo |
| STREAK_FADE_5M | 85 | 48.2% | -0.017 | 📉 agota (-0.12) | -3.77$ | 0.50$ | ⚠️ IC negativo |
| STRUCT_NO_15M | 15 | 20.0% | -0.199 | — | -4.68$ | 0.00$ | 🚫 desactivada |
| WEEKLY_PRICE | 192 | 57.8% | +0.077 | 📈 madura (+0.23) | -13.59$ | 0.77$ | ✅ activa |
| SMART_FLOW_1H | 29 | 20.7% | -0.274 | — | -13.82$ | 0.00$ | 🚫 desactivada |
| UPDOWN_OU_5M | 84 | 28.6% | -0.209 | 📉 agota (-0.14) | -18.89$ | 0.00$ | 🚫 desactivada |
| FAVORITO_CONFIRMADO | 708 | 66.9% | +0.169 | ➡️ estable | -19.02$ | 1.69$ | ✅ activa |
| STREAK_MOM_5M | 308 | 44.5% | -0.055 | 📉 agota (-0.06) | -23.16$ | 0.50$ | 🚫 desactivada |

## Últimas 5 resoluciones

| Timestamp | Estrategia | Mercado | Resultado | PNL |
|---|---|---|---|---|
| 2026-07-12T02:27 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 11, 10:20PM-10:25PM ET… | ✅ WIN | +0.65$ |
| 2026-07-12T02:24 | FAVORITO_CONFIRMADO#SOL#5min | Solana Up or Down - July 11, 10:15PM-10:20PM ET… | ❌ LOSS | -0.51$ |
| 2026-07-12T02:22 | STREAK_FADE_5M#XRP#5min | XRP Up or Down - July 11, 10:15PM-10:20PM ET… | ❌ LOSS | -0.66$ |
| 2026-07-12T02:16 | FAVORITO_CONFIRMADO#ETH#15min | Ethereum Up or Down - July 11, 10:00PM-10:15PM ET… | ✅ WIN | +0.20$ |
| 2026-07-12T02:16 | FAVORITO_CONFIRMADO#SOL#15min | Solana Up or Down - July 11, 10:00PM-10:15PM ET… | ✅ WIN | +0.34$ |

## Calidad de datos

✅ **OK** — última verificación 2026-07-12T02:28 UTC

| Asset | Precio | Age | Alertas |
|---|---|---|---|
| ✅ BTC | $64,072.11 | 0.1min |  |
| ✅ ETH | $1,805.30 | 0.1min |  |
| ✅ SOL | $76.86 | 0.1min |  |
| ✅ XRP | $1.10 | 0.1min |  |

**Cross-source** (binance, coinbase, kraken):

| Asset | Consenso | Fuente | Estado |
|---|---|---|---|
| BTC | $64,072.11 | consenso |  |
| ETH | $1,805.48 | consenso |  |
| SOL | $76.80 | consenso |  |
| XRP | $1.10 | consenso |  |

---
*Actualizado automáticamente cada ~60s por el fast loop*