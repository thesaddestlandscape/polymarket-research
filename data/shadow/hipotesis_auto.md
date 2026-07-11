# Hipótesis automáticas — 2026-07-11 08:37 UTC
_Generado por shadow_postmortem.py sobre 8914 resoluciones (PNL=+1434.53€)_

## Patrones causales activos

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.146 (n=46)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.146 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 4.0 (IC base=+0.044)

### UPDOWN_GBM#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.125 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=304)

- **PATRÓN** `ibs_15` > `0.7103` → IC=+0.124 (n=195)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.62€ cuando `ibs_15` > 0.7103 (IC base=+0.001)

- **PATRÓN** `ibs_15` < `0.0487` → IC=+0.129 (n=122)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.65€ cuando `ibs_15` < 0.0487 (IC base=+0.029)

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
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **FILTRO** `hora_utc` < `20.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `ibs_15` < `0.7622` → IC=-0.150 (n=18)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.7622
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.125 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=113)

- **FILTRO** `ibs_15` > `0.0324` → IC=-0.130 (n=25)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.0324
  - _Potencial_: sin este filtro IC_bueno=+0.300 (n=13)

- **PATRÓN** `drift_60min` |x|≤ `0.0664` → IC=+0.133 (n=47)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.0664 (IC base=+0.040)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.152 (n=113)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 11.0 (IC base=+0.040)

- **PATRÓN** `ibs_15` < `0.908` → IC=+0.135 (n=102)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.67€ cuando `ibs_15` < 0.908 (IC base=+0.040)

- **PATRÓN** `ibs_15` > `0.6323` → IC=+0.135 (n=102)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.67€ cuando `ibs_15` > 0.6323 (IC base=+0.040)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0516` → IC=+0.125 (n=30)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.62€ cuando `pct_spot_vs_ref` |x|≤ 0.0516 (IC base=+0.033)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0061 (IC base=+0.033)

- **PATRÓN** `ibs_15` < `0.1209` → IC=+0.182 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` < 0.1209 (IC base=+0.033)

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
- **PATRÓN** `ibs_15` > `0.8268` → IC=+0.190 (n=56)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.95€ cuando `ibs_15` > 0.8268 (IC base=+0.012)

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

- **FILTRO** `sigma_h` > `0.013` → IC=-0.130 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.013
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=27)

- **FILTRO** `drift_60min` |x|> `0.4251` → IC=-0.206 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.4251
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=31)

- **FILTRO** `drift_15min` |x|> `0.568` → IC=-0.125 (n=22)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.568
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=24)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.0905` → IC=-0.147 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0905
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=31)

- **FILTRO** `hora_utc` < `22.0` → IC=-0.150 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 22.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

### UPDOWN_GBM#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1131` → IC=-0.167 (n=16)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1131
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `sigma_h` > `0.0147` → IC=-0.150 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0147
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `drift_15min` |x|> `0.4751` → IC=-0.237 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4751
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `ibs_15` > `0.0448` → IC=-0.152 (n=21)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.0448
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=22)

- **PATRÓN** `sigma_h` < `0.0137` → IC=+0.200 (n=28)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0137 (IC base=+0.114)

- **PATRÓN** `drift_15min` |x|≤ `0.7781` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `drift_15min` |x|≤ 0.7781 (IC base=+0.114)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1215` → IC=+0.130 (n=25)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio_macro` |x|> 0.1215 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 14.0 (IC base=+0.114)

- **PATRÓN** `ibs_15` < `0.0448` → IC=+0.250 (n=22)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.0448 (IC base=+0.114)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#BTC#15min**: IBS < 0.1209 correlaciona con éxito en UPDOWN_GBM#BTC#15min (IC=+0.182 n=20). Confirma señal de reversión media → alinear con BUY_YES.
- **H-IBS-UPDOWN_GBM#ETH#15min**: IBS > 0.8268 correlaciona con éxito en UPDOWN_GBM#ETH#15min (IC=+0.190 n=56). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#XRP#15min**: IBS < 0.0448 correlaciona con éxito en UPDOWN_GBM#XRP#15min (IC=+0.250 n=22). Confirma señal de reversión media → alinear con BUY_YES.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN` — IC=+0.203 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#BTC#5min` — IC=+0.203 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#BTC` — IC=+0.203 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#5min` — IC=+0.203 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ FAVORITO_CONFIRMADO | 389 | +0.173 | -13.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#15min | 248 | +0.180 | -19.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 16 | +0.044 | -0.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 62 | +0.078 | -3.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 63 | +0.254 | +9.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 116 | +0.152 | -8.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 80 | +0.171 | -10.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 5 | +0.018 | +0.14€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 21 | +0.283 | +5.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 133 | +0.167 | -1.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 83 | +0.194 | -1.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 5 | -0.018 | -0.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 24 | +0.077 | -1.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 21 | +0.196 | +2.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL | 139 | +0.188 | -3.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 84 | +0.163 | -7.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 6 | +0.037 | +0.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 28 | +0.200 | +2.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 21 | +0.239 | +1.73€ | 0 | 0 |
| ✅ GBM_LATE_15M | 3173 | +0.114 | +1033.08€ | 0 | 0 |
| ✅ GBM_LATE_15M#15min | 3173 | +0.114 | +1033.08€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 797 | +0.062 | +83.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 797 | +0.062 | +83.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH | 808 | +0.073 | +126.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 808 | +0.073 | +126.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL | 819 | +0.146 | +418.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 819 | +0.146 | +418.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP | 749 | +0.179 | +405.08€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 749 | +0.179 | +405.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 575 | +0.159 | +266.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 575 | +0.159 | +266.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 149 | +0.189 | +98.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 149 | +0.189 | +98.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 158 | +0.144 | +56.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 158 | +0.144 | +56.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 166 | +0.077 | +26.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 166 | +0.077 | +26.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 102 | +0.260 | +84.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 102 | +0.260 | +84.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 716 | +0.079 | +154.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#15min | 716 | +0.079 | +154.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 173 | +0.071 | +15.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 173 | +0.071 | +15.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 180 | +0.000 | +2.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 180 | +0.000 | +2.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 182 | +0.016 | +12.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 182 | +0.016 | +12.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 181 | +0.227 | +124.12€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 181 | +0.227 | +124.12€ | 0 | 0 |
| ✅ GBM_LATE_60M | 266 | -0.104 | +10.96€ | 0 | 0 |
| ✅ GBM_LATE_60M#60min | 266 | -0.104 | +10.96€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 89 | -0.038 | +4.84€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 89 | -0.038 | +4.84€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH | 82 | -0.143 | -5.71€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 82 | -0.143 | -5.71€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL | 95 | -0.129 | +11.83€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 95 | -0.129 | +11.83€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 35 | +0.203 | +10.30€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 35 | +0.203 | +10.30€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 35 | +0.203 | +10.30€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 35 | +0.203 | +10.30€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 45 | +0.117 | +8.93€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 45 | +0.117 | +8.93€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 45 | +0.117 | +8.93€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 45 | +0.117 | +8.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1574 | +0.013 | +17.53€ | 1 | 1 |
| ✅ ORDER_FLOW_5M#5min | 1438 | +0.009 | +4.93€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 191 | +0.049 | +7.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 191 | +0.049 | +7.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 206 | -0.005 | -3.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 206 | -0.005 | -3.04€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 248 | -0.012 | -5.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 248 | -0.012 | -5.66€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 318 | +0.041 | +13.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 318 | +0.041 | +13.23€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 184 | +0.000 | -1.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 184 | +0.000 | -1.63€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 134 | -0.154 | -0.51€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 62 | -0.250 | -18.09€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 56 | -0.276 | -17.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 6 | +0.000 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 47 | -0.112 | +5.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 44 | -0.152 | +0.55€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 25 | +0.018 | +12.20€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 24 | +0.000 | +11.42€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 124 | -0.182 | -5.38€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 10 | +0.083 | +4.87€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 8 | +0.160 | +3.47€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 8 | +0.160 | +3.47€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 127 | +0.120 | +20.22€ | 0 | 0 |
| ✅ STREAK_FADE_15M#15min | 127 | +0.120 | +20.22€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 27 | +0.224 | +11.86€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 27 | +0.224 | +11.86€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 44 | +0.109 | +6.38€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 44 | +0.109 | +6.38€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 56 | +0.069 | +1.99€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 56 | +0.069 | +1.99€ | 0 | 0 |
| 🚫 STREAK_MOM_5M | 308 | -0.055 | -23.16€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 308 | -0.055 | -23.16€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 102 | -0.048 | -5.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 102 | -0.048 | -5.83€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL | 108 | -0.009 | -3.98€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 108 | -0.009 | -3.98€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP | 98 | -0.110 | -13.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 98 | -0.110 | -13.35€ | 0 | 0 |
| 🚫 STRUCT_NO_15M | 15 | -0.199 | -4.68€ | 0 | 0 |
| 🚫 STRUCT_NO_15M#15min | 15 | -0.199 | -4.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ UPDOWN_GBM | 1255 | -0.015 | -2.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1000 | +0.013 | +34.53€ | 1 | 2 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 127 | -0.058 | -10.76€ | 7 | 0 |
| ✅ UPDOWN_GBM#BNB | 24 | -0.154 | -7.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 24 | -0.154 | -7.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 336 | +0.000 | -5.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 258 | +0.038 | +7.43€ | 2 | 7 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 42 | -0.068 | -6.16€ | 2 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 13 | -0.065 | +2.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 27 | -0.086 | -4.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 24 | -0.077 | -3.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 606 | +0.005 | +21.94€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 513 | +0.024 | +32.99€ | 0 | 1 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 54 | -0.018 | -2.56€ | 3 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 169 | -0.091 | -14.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 101 | -0.063 | -7.89€ | 8 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 31 | -0.106 | -2.03€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 91 | +0.005 | +9.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 80 | +0.037 | +13.02€ | 4 | 5 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 40 | -0.191 | +2.43€ | 0 | 0 |
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
| ✅ WEEKLY_PRICE | 175 | +0.071 | -13.32€ | 0 | 0 |
| ✅ WEEKLY_PRICE#BTC | 54 | +0.054 | -7.69€ | 0 | 0 |
| ✅ WEEKLY_PRICE#ETH | 54 | +0.089 | -5.57€ | 0 | 0 |
| ✅ WEEKLY_PRICE#SOL | 67 | +0.065 | -0.06€ | 0 | 0 |