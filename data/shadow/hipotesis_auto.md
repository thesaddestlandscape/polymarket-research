# Hipótesis automáticas — 2026-06-27 11:03 UTC
_Generado por shadow_postmortem.py sobre 1182 resoluciones (PNL=-22.99€)_

## Patrones causales activos

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0502` → IC=+0.132 (n=17)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.66€ cuando `pct_spot_vs_ref` |x|≤ 0.0502 (IC base=+0.029)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0121` → IC=+0.132 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0121 (IC base=+0.052)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.2212` → IC=-0.132 (n=17)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2212
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

_Sin sugerencias automáticas con datos actuales. Ampliar n por estrategia._

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ ORDER_FLOW_5M | 782 | +0.011 | +6.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#5min | 646 | +0.002 | -5.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 63 | +0.038 | +1.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 63 | +0.038 | +1.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC | 128 | +0.008 | -0.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 128 | +0.008 | -0.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 82 | -0.012 | -1.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 82 | -0.012 | -1.81€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 112 | -0.026 | -4.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 112 | -0.026 | -4.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 145 | +0.017 | +1.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 145 | +0.017 | +1.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 116 | -0.009 | -2.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 116 | -0.009 | -2.01€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 16 | +0.000 | -1.53€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 7 | -0.019 | -0.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 7 | -0.019 | -0.66€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 6 | +0.000 | -1.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 6 | +0.000 | -1.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 16 | +0.000 | -1.53€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 20 | -0.273 | -9.86€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 6 | -0.037 | -1.69€ | 0 | 0 |
| ✅ UPDOWN_GBM | 286 | -0.004 | -1.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 161 | +0.040 | +9.11€ | 0 | 0 |
| 🚫 UPDOWN_GBM#240min | 12 | -0.171 | -4.82€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 56 | -0.155 | -16.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 50 | +0.096 | +5.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 90 | +0.000 | -3.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 49 | +0.029 | -0.44€ | 0 | 1 |
| ✅ UPDOWN_GBM#BTC#240min | 5 | -0.089 | -2.96€ | 0 | 0 |
| 🚫 UPDOWN_GBM#BTC#5min | 16 | -0.133 | -6.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 18 | +0.135 | +3.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 104 | +0.028 | +2.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 65 | +0.052 | +3.80€ | 0 | 1 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 12 | -0.086 | -3.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 20 | +0.091 | +1.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 66 | -0.029 | +1.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 34 | +0.028 | +4.02€ | 1 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 17 | -0.112 | -4.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 12 | +0.000 | +1.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 21 | -0.065 | -0.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 12 | +0.000 | +0.92€ | 0 | 0 |
| 🚫 UPDOWN_GBM#XRP#5min | 9 | -0.061 | -1.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 5 | +0.054 | +7.49€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M | 57 | -0.229 | -13.76€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#5min | 57 | -0.229 | -13.76€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#BNB | 8 | -0.160 | -4.56€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#BNB#5min | 8 | -0.160 | -4.56€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#BTC | 9 | -0.102 | -2.57€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#BTC#5min | 9 | -0.102 | -2.57€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 7 | -0.058 | -1.11€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 7 | -0.058 | -1.11€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#ETH | 12 | -0.129 | -2.82€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#ETH#5min | 12 | -0.129 | -2.82€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 10 | -0.042 | -1.06€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 10 | -0.042 | -1.06€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 11 | -0.064 | -1.65€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 11 | -0.064 | -1.65€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 21 | +0.022 | -3.78€ | 0 | 0 |
| ✅ WEEKLY_PRICE#BTC | 6 | -0.037 | -2.73€ | 0 | 0 |
| ✅ WEEKLY_PRICE#ETH | 8 | +0.000 | -2.41€ | 0 | 0 |
| ✅ WEEKLY_PRICE#SOL | 7 | +0.058 | +1.36€ | 0 | 0 |