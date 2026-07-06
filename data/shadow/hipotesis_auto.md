# Hipótesis automáticas — 2026-07-06 01:06 UTC
_Generado por shadow_postmortem.py sobre 4093 resoluciones (PNL=+206.13€)_

## Patrones causales activos

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=13)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.150 (n=98)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0085 (IC base=+0.032)

- **PATRÓN** `ibs_15` < `0.0613` → IC=+0.154 (n=76)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.77€ cuando `ibs_15` < 0.0613 (IC base=+0.032)

### UPDOWN_GBM#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.01` → IC=-0.300 (n=28)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `sigma_h` > `0.0024` → IC=-0.333 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0024
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.03` → IC=-0.167 (n=16)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.03
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

- **FILTRO** `sigma_h` > `0.0018` → IC=-0.143 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0018
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### UPDOWN_GBM#60min
- **FILTRO** `sigma_h` < `0.0058` → IC=-0.208 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0058
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=67)

- **FILTRO** `hora_utc` < `11.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=27)

- **FILTRO** `ibs_15` > `0.1935` → IC=-0.175 (n=38)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.1935
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=13)

- **FILTRO** `ibs_15` < `0.5186` → IC=-0.204 (n=25)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5186
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0182` → IC=-0.150 (n=18)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0182
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `hora_utc` < `20.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 20.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `ibs_15` < `0.6667` → IC=-0.147 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.6667
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `sigma_h` < `0.0051` → IC=-0.125 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0051
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=114)

- **FILTRO** `hora_utc` < `10.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=67)

- **FILTRO** `ibs_15` > `0.9404` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.9404
  - _Potencial_: sin este filtro IC_bueno=+0.080 (n=67)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0921` → IC=-0.147 (n=15)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0921
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=32)

- **FILTRO** `ibs_15` > `0.0936` → IC=-0.150 (n=18)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.0936
  - _Potencial_: sin este filtro IC_bueno=+0.318 (n=9)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0366` → IC=+0.154 (n=24)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.77€ cuando `pct_spot_vs_ref` |x|≤ 0.0366 (IC base=+0.031)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.167 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0064 (IC base=+0.031)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_h` < `0.012` → IC=-0.143 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.012
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

- **FILTRO** `ibs_15` < `0.8328` → IC=-0.206 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8328
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `drift_60min` |x|> `0.3562` → IC=-0.128 (n=49)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.3562
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=151)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.0765` → IC=-0.135 (n=50)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0765
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=151)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.121 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.025 (n=120)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.197 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.006 (IC base=+0.074)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.194 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 7.0 (IC base=+0.074)

- **PATRÓN** `ibs_15` < `0.0431` → IC=+0.194 (n=34)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.97€ cuando `ibs_15` < 0.0431 (IC base=+0.074)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.133` → IC=-0.167 (n=19)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.133
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `ibs_15` > `0.2558` → IC=-0.132 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2558
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `sigma_h` > `0.0204` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0204
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33)

- **FILTRO** `drift_15min` |x|> `0.3239` → IC=-0.145 (n=29)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3239
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1932` → IC=-0.155 (n=27)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1932
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **FILTRO** `drift_60min` |x|> `0.1869` → IC=-0.121 (n=27)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1869
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `drift_15min` |x|> `0.7136` → IC=-0.150 (n=18)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7136
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **FILTRO** `hora_utc` < `22.0` → IC=-0.150 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 22.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### UPDOWN_GBM#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1131` → IC=-0.167 (n=16)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1131
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `sigma_h` > `0.015` → IC=-0.132 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.015
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `drift_15min` |x|> `0.5008` → IC=-0.222 (n=16)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5008
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `ibs_15` > `0.0333` → IC=-0.136 (n=20)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.0333
  - _Potencial_: sin este filtro IC_bueno=+0.269 (n=11)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.206 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.012 (IC base=+0.100)

- **PATRÓN** `drift_15min` |x|≤ `0.7351` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.7351 (IC base=+0.100)

- **PATRÓN** `ibs_15` < `0.0952` → IC=+0.167 (n=16)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` < 0.0952 (IC base=+0.100)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: IBS < 0.0613 correlaciona con éxito en UPDOWN_GBM#15min (IC=+0.154 n=76). Confirma señal de reversión media → alinear con BUY_YES.
- **H-IBS-UPDOWN_GBM#ETH#15min**: IBS < 0.0431 correlaciona con éxito en UPDOWN_GBM#ETH#15min (IC=+0.194 n=34). Confirma señal de reversión media → alinear con BUY_YES.
- **H-IBS-UPDOWN_GBM#XRP#15min**: IBS < 0.0952 correlaciona con éxito en UPDOWN_GBM#XRP#15min (IC=+0.167 n=16). Confirma señal de reversión media → alinear con BUY_YES.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ GBM_LATE_15M | 1219 | +0.093 | +305.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#15min | 1219 | +0.093 | +305.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 318 | +0.031 | +30.22€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 318 | +0.031 | +30.22€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH | 319 | +0.058 | +37.31€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 319 | +0.058 | +37.31€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL | 320 | +0.134 | +128.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 320 | +0.134 | +128.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP | 262 | +0.159 | +108.70€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 262 | +0.159 | +108.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M | 8 | -0.120 | -3.18€ | 0 | 0 |
| 🚫 GBM_LATE_60M#60min | 8 | -0.120 | -3.18€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 11 | +0.064 | +1.47€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 11 | +0.064 | +1.47€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 11 | +0.064 | +1.47€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 11 | +0.064 | +1.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1541 | +0.011 | +7.96€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1405 | +0.006 | -4.64€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 191 | +0.049 | +7.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 191 | +0.049 | +7.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC | 272 | -0.033 | -11.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 272 | -0.033 | -11.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 206 | -0.005 | -3.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 206 | -0.005 | -3.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 248 | -0.012 | -5.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 248 | -0.012 | -5.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 304 | +0.039 | +9.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 304 | +0.039 | +9.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 184 | +0.000 | -1.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 184 | +0.000 | -1.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 102 | -0.115 | +4.75€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 50 | -0.211 | -12.66€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 46 | -0.229 | -11.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 35 | -0.041 | +6.12€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 34 | -0.056 | +5.97€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 17 | +0.022 | +11.29€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 17 | +0.022 | +11.29€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 97 | -0.126 | +5.34€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 5 | +0.018 | -0.58€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 6 | +0.113 | +2.85€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 6 | +0.113 | +2.85€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| 🚫 STRUCT_NO_15M | 15 | -0.199 | -4.68€ | 0 | 0 |
| 🚫 STRUCT_NO_15M#15min | 15 | -0.199 | -4.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ UPDOWN_GBM | 974 | -0.035 | -51.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 735 | -0.011 | -21.08€ | 0 | 2 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 126 | -0.055 | -10.25€ | 7 | 0 |
| ✅ UPDOWN_GBM#BNB | 24 | -0.154 | -7.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 24 | -0.154 | -7.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 272 | -0.036 | -31.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 199 | -0.012 | -21.52€ | 5 | 2 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 42 | -0.068 | -6.16€ | 2 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 8 | +0.040 | +5.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 27 | -0.086 | -4.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 24 | -0.077 | -3.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 416 | -0.002 | +5.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 329 | +0.017 | +13.54€ | 3 | 3 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 53 | -0.009 | -2.05€ | 3 | 0 |
| ✅ UPDOWN_GBM#ETH#daily | 10 | -0.042 | +2.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 155 | -0.092 | -14.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 92 | -0.074 | -8.39€ | 6 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 31 | -0.106 | -2.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#daily | 7 | -0.058 | +1.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 78 | -0.013 | +3.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 67 | +0.022 | +6.33€ | 4 | 3 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 25 | -0.056 | +8.91€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M | 84 | -0.209 | -18.89€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#5min | 84 | -0.209 | -18.89€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#BNB | 13 | -0.195 | -5.11€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#BNB#5min | 13 | -0.195 | -5.11€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 14 | -0.087 | -1.98€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 14 | -0.087 | -1.98€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 13 | -0.108 | -2.68€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 13 | -0.108 | -2.68€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#ETH | 18 | -0.225 | -4.88€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#ETH#5min | 18 | -0.225 | -4.88€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 13 | -0.065 | -1.58€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 13 | -0.065 | -1.58€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 13 | -0.108 | -2.67€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 13 | -0.108 | -2.67€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 100 | -0.049 | -24.34€ | 0 | 0 |
| ✅ WEEKLY_PRICE#BTC | 35 | -0.013 | -8.65€ | 0 | 0 |
| ✅ WEEKLY_PRICE#ETH | 36 | +0.000 | -8.64€ | 0 | 0 |
| ✅ WEEKLY_PRICE#SOL | 29 | -0.145 | -7.05€ | 0 | 0 |