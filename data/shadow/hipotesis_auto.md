# Hipótesis automáticas — 2026-07-12 17:42 UTC
_Generado por shadow_postmortem.py sobre 11221 resoluciones (PNL=+2103.16€)_

## Patrones causales activos

### FAVORITO_CONFIRMADO
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.222 (n=174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.250 (n=166)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.216)

- **PATRÓN** `py_entrada` > `0.585` → IC=+0.249 (n=368)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.585 (IC base=+0.216)

- **PATRÓN** `libro_liquidez` > `2848.6588` → IC=+0.232 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2848.6588 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.216 (n=167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.304 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.148)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.156 (n=431)

  - _Acción_: Kelly boost +0.78€ cuando `libro_spread` < 0.01 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `5969.0343` → IC=+0.161 (n=172)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 5969.0343 (IC base=+0.148)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.233 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.203 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.605` → IC=+0.241 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.605 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `6258.8556` → IC=+0.191 (n=79)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6258.8556 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.259 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.232 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.217)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `6591.3319` → IC=+0.237 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6591.3319 (IC base=+0.217)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.271 (n=81)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.243)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.325 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.243)

- **PATRÓN** `libro_liquidez` > `3157.2453` → IC=+0.263 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3157.2453 (IC base=+0.243)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.233 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` < `0.245` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.245 (IC base=+0.164)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.278 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.235)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.237 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.235)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.342 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.235)

- **PATRÓN** `libro_liquidez` > `1877.4208` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1877.4208 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.238 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.269 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `1598.2993` → IC=+0.235 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1598.2993 (IC base=+0.209)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.132 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 12.0 (IC base=+0.100)

- **PATRÓN** `py_entrada` > `0.425` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` > 0.425 (IC base=+0.100)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.122 (n=1365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 6.0 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.121 (n=1361)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 17.0 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `0.5436` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` > 0.5436 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.1287` → IC=+0.206 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1287 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.579` → IC=+0.395 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.579 (IC base=+0.116)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.150 (n=934)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0091 (IC base=+0.111)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.140 (n=938)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 11.0 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.1754` → IC=+0.185 (n=90)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1754 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.069` → IC=+0.227 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.069 (IC base=+0.111)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `dist_vwap_pct` < `0.134` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.134 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.0721` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.0721 (IC base=+0.054)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.161 (n=113)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` < 0.0045 (IC base=+0.093)

- **PATRÓN** `dist_vwap_pct` > `0.699` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.699 (IC base=+0.093)

### GBM_LATE_15M#SOL#15min
- **PATRÓN** `sigma_h` < `0.0161` → IC=+0.139 (n=364)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0161 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.164 (n=138)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 17.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.133 (n=167)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 8.0 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.536` → IC=+0.150 (n=18)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.536 (IC base=+0.123)

- **PATRÓN** `sigma_h` < `0.01` → IC=+0.181 (n=155)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.01 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.0149` → IC=+0.172 (n=117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0149 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.213 (n=235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.1648` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1648 (IC base=+0.155)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_h` < `0.0316` → IC=+0.176 (n=310)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0316 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.014` → IC=+0.177 (n=277)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.014 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.165 (n=317)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.182 (n=209)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 11.0 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.1365` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1365 (IC base=+0.163)

- **PATRÓN** `sigma_h` < `0.0172` → IC=+0.185 (n=233)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0172 (IC base=+0.179)

- **PATRÓN** `sigma_h` > `0.0298` → IC=+0.206 (n=117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0298 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.258 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.179)

- **PATRÓN** `dist_vwap_pct` < `0.1094` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.1094 (IC base=+0.179)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.195 (n=332)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0049 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.180 (n=248)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 13.0 (IC base=+0.174)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.181 (n=381)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 17.0 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.5381` → IC=+0.295 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5381 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` < `0.1312` → IC=+0.202 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1312 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.579` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.579 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.178 (n=380)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0043 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.187 (n=148)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 6.0 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.2529` → IC=+0.257 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2529 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.075` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.075 (IC base=+0.153)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.216 (n=93)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0028 (IC base=+0.157)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.185 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 16.0 (IC base=+0.157)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.161 (n=107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 18.0 (IC base=+0.157)

- **PATRÓN** `dist_vwap_pct` < `0.1111` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.1111 (IC base=+0.157)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.247 (n=85)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0029 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.163 (n=96)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 6.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.171 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 12.0 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.0721` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.0721 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` < `0.041` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.041 (IC base=+0.156)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.189 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0049 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.183 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 12.0 (IC base=+0.155)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.176 (n=109)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 17.0 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.4503` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4503 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.156 (n=62)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0049 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.129 (n=33)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.103)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.176 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 6.0 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.5163` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.5163 (IC base=+0.103)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **PATRÓN** `sigma_h` > `0.011` → IC=+0.214 (n=61)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.156 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 16.0 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.2965` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2965 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.245 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.106)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.174 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 5.0 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` < `0.2347` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.2347 (IC base=+0.106)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` < `0.0187` → IC=+0.333 (n=70)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0187 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.303 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.266)

- **PATRÓN** `dist_vwap_pct` < `0.1821` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1821 (IC base=+0.266)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.309 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.280)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.282 (n=76)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.280)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.300 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.280)

### GBM_LATE_15M_TARDIO
- **FILTRO** `sigma_ewma_delta_pct` < `6.483` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 6.483
  - _Potencial_: sin este filtro IC_bueno=+0.362 (n=27)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.130 (n=144)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.0135 (IC base=+0.083)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.125 (n=214)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 8.0 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` > `0.4573` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` > 0.4573 (IC base=+0.083)

- **PATRÓN** `dist_vwap_pct` < `0.1146` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1146 (IC base=+0.083)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.483` → IC=+0.362 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.483 (IC base=+0.083)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.149 (n=146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0123 (IC base=+0.082)

- **PATRÓN** `dist_vwap_pct` < `0.2624` → IC=+0.148 (n=106)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.2624 (IC base=+0.082)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `dist_vwap_pct` < `0.1111` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1111 (IC base=+0.082)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0035` → IC=+0.134 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0035 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.4153` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.4153 (IC base=+0.026)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.123 (n=51)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` > 0.0127 (IC base=+0.036)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.250 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0083 (IC base=+0.036)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.143 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.036)

- **PATRÓN** `dist_vwap_pct` < `0.1589` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1589 (IC base=+0.036)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.033` → IC=+0.206 (n=107)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.033 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.197 (n=107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0113 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.250 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.188)

- **PATRÓN** `dist_vwap_pct` < `0.1011` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.1011 (IC base=+0.188)

- **PATRÓN** `sigma_h` > `0.0311` → IC=+0.256 (n=39)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0311 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.259 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` < `0.2832` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.2832 (IC base=+0.209)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0133` → IC=-0.300 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=118)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.272 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=44)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.167 (n=40)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0047 (IC base=-0.003)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `sigma_h` > `0.0034` → IC=-0.167 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `sigma_h` < `0.008` → IC=-0.167 (n=34)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.008
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.147 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.005 (IC base=+0.062)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0084` → IC=-0.333 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=32)

- **FILTRO** `sigma_h` < `0.005` → IC=-0.324 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.005
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=33)

- **FILTRO** `hora_utc` < `18.0` → IC=-0.294 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.333 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=14)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `sigma_h` < `0.0135` → IC=-0.258 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0135
  - _Potencial_: sin este filtro IC_bueno=+0.237 (n=17)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.125 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

- **FILTRO** `sigma_h` > `0.0103` → IC=-0.271 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `hora_utc` < `18.0` → IC=-0.202 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=17)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.261 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=-0.080)

### LEADLAG_BTC_XRP_15M
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.214 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.200 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.5 (IC base=+0.203)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.214 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `10.0` → IC=+0.200 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 10.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.5 (IC base=+0.203)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=56)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.121 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 4.0 (IC base=+0.043)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `total_vol_5m` < `197.886` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `total_vol_5m` < 197.886 (IC base=+0.031)

### ORDER_FLOW_5M#BTC#5min
- **FILTRO** `delta_ratio` |x|≤ `0.3925` → IC=-0.180 (n=23)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.3925
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=80)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=24)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.192 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 4.0 (IC base=+0.000)

### ORDER_FLOW_5M#DOGE#5min
- **FILTRO** `delta_ratio` |x|≤ `0.4217` → IC=-0.140 (n=23)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.4217
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=70)

- **FILTRO** `total_vol_5m` > `1108292.0` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `total_vol_5m` > 1108292.0
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=61)

- **PATRÓN** `total_vol_5m` < `557706.0` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `total_vol_5m` < 557706.0 (IC base=+0.021)

### ORDER_FLOW_5M#XRP#5min
- **FILTRO** `delta_ratio` |x|≤ `0.4307` → IC=-0.136 (n=20)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.4307
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=45)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0091` → IC=-0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0091
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=33)

- **FILTRO** `sigma_h` > `0.0049` → IC=-0.368 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0049
  - _Potencial_: sin este filtro IC_bueno=+0.260 (n=23)

- **FILTRO** `T_h` < `145.6944` → IC=-0.435 (n=44)

  - _Acción_: SKIP cuando `T_h` < 145.6944
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=15)

- **FILTRO** `pct_vs_K` |x|> `2.6988` → IC=-0.478 (n=44)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6988
  - _Potencial_: sin este filtro IC_bueno=-0.147 (n=15)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.260 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0049 (IC base=-0.203)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.420 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

- **FILTRO** `T_h` > `87.9936` → IC=-0.444 (n=16)

  - _Acción_: SKIP cuando `T_h` > 87.9936
  - _Potencial_: sin este filtro IC_bueno=-0.375 (n=6)

- **FILTRO** `T_h` < `145.912` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `T_h` < 145.912
  - _Potencial_: sin este filtro IC_bueno=-0.389 (n=7)

- **FILTRO** `pct_vs_K` |x|> `3.4276` → IC=-0.441 (n=15)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4276
  - _Potencial_: sin este filtro IC_bueno=-0.389 (n=7)

### STREAK_FADE_15M
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.267 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.505 (IC base=+0.142)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.206 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `streak_len` < 4.0 (IC base=+0.142)

- **PATRÓN** `volumen_racha` < `29764.512` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 29764.512 (IC base=+0.142)

- **PATRÓN** `libro_liquidez` > `2513.3765` → IC=+0.250 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2513.3765 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.315 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.097)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.189 (n=43)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` < 0.485 (IC base=+0.097)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.140 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 6.0 (IC base=+0.085)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.505 (IC base=+0.085)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `streak_len` < 4.0 (IC base=+0.085)

### STREAK_FADE_5M
- **FILTRO** `hora_utc` < `16.0` → IC=-0.167 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=18)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=52)

- **FILTRO** `streak_len` > `4.0` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `streak_len` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=45)

- **FILTRO** `libro_liquidez` < `2804.981` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_liquidez` < 2804.981
  - _Potencial_: sin este filtro IC_bueno=-0.082 (n=53)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `py_entrada` < `0.51` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.51
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=6)

- **FILTRO** `hora_utc` < `18.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

- **FILTRO** `hora_utc` > `3.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `libro_liquidez` < `6441.4408` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 6441.4408
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `libro_liquidez` < `3587.1181` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `libro_liquidez` < 3587.1181
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

### STREAK_FADE_5M#XRP#5min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.150 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 12.0 (IC base=+0.095)

### STREAK_MOM_5M
- **FILTRO** `hora_utc` > `17.0` → IC=-0.132 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=108)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.250 (n=46)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=98)

- **FILTRO** `streak_len` > `4.0` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `streak_len` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=120)

- **FILTRO** `libro_liquidez` < `3352.7321` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `libro_liquidez` < 3352.7321
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=103)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.141 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=128)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=76)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=74)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.133 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **FILTRO** `libro_liquidez` < `8045.5084` → IC=-0.125 (n=30)

  - _Acción_: SKIP cuando `libro_liquidez` < 8045.5084
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

### STREAK_MOM_5M#SOL#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=30)

- **FILTRO** `libro_liquidez` < `3331.5444` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3331.5444
  - _Potencial_: sin este filtro IC_bueno=+0.043 (n=33)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.140 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 9.0 (IC base=+0.041)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` > 0.505 (IC base=+0.041)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.041)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.5` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=32)

- **FILTRO** `hora_utc` < `18.0` → IC=-0.203 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

- **FILTRO** `hora_utc` > `10.0` → IC=-0.188 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=21)

- **FILTRO** `streak_len` > `3.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=35)

- **FILTRO** `libro_liquidez` < `3688.8474` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 3688.8474
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=23)

### UPDOWN_GBM#15min
- **FILTRO** `hora_utc` < `7.0` → IC=-0.125 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=353)

- **PATRÓN** `ibs_15` > `0.7168` → IC=+0.158 (n=220)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.79€ cuando `ibs_15` > 0.7168 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` > `0.1361` → IC=+0.178 (n=85)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.1361 (IC base=+0.018)

- **PATRÓN** `dist_vwap_pct` < `0.272` → IC=+0.185 (n=87)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.272 (IC base=+0.018)

- **PATRÓN** `ibs_15` < `0.0345` → IC=+0.147 (n=100)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.74€ cuando `ibs_15` < 0.0345 (IC base=+0.029)

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
- **FILTRO** `ibs_15` > `0.1169` → IC=-0.167 (n=19)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.1169
  - _Potencial_: sin este filtro IC_bueno=+0.196 (n=21)

- **PATRÓN** `drift_60min` |x|≤ `0.1638` → IC=+0.126 (n=105)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.1638 (IC base=+0.056)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.164 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 12.0 (IC base=+0.056)

- **PATRÓN** `ibs_15` < `0.9235` → IC=+0.150 (n=118)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.75€ cuando `ibs_15` < 0.9235 (IC base=+0.056)

- **PATRÓN** `ibs_15` > `0.6374` → IC=+0.172 (n=117)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.86€ cuando `ibs_15` > 0.6374 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.2347` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2347 (IC base=+0.056)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0516` → IC=+0.136 (n=31)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.68€ cuando `pct_spot_vs_ref` |x|≤ 0.0516 (IC base=+0.032)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.278 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.032)

- **PATRÓN** `ibs_15` < `0.1169` → IC=+0.196 (n=21)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.98€ cuando `ibs_15` < 0.1169 (IC base=+0.032)

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
- **PATRÓN** `ibs_15` > `0.7617` → IC=+0.204 (n=86)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7617 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.3288` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` < 0.3288 (IC base=+0.030)

- **PATRÓN** `ibs_15` < `0.0374` → IC=+0.123 (n=59)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.61€ cuando `ibs_15` < 0.0374 (IC base=+0.037)

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

- **FILTRO** `drift_60min` |x|> `0.4251` → IC=-0.206 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.4251
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=32)

- **FILTRO** `drift_15min` |x|> `0.5673` → IC=-0.140 (n=23)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5673
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=24)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.0905` → IC=-0.147 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0905
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

- **FILTRO** `hora_utc` < `22.0` → IC=-0.150 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 22.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

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

### WEEKLY_PRICE
- **FILTRO** `T_h` > `81.6124` → IC=-0.269 (n=24)

  - _Acción_: SKIP cuando `T_h` > 81.6124
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **FILTRO** `T_h` < `144.6751` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `T_h` < 144.6751
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=18)

- **PATRÓN** `T_h` < `87.9965` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 87.9965 (IC base=+0.239)

- **PATRÓN** `T_h` > `145.8516` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.8516 (IC base=+0.239)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` < `146.1118` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 146.1118 (IC base=+0.255)

- **PATRÓN** `T_h` > `105.6124` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 105.6124 (IC base=+0.255)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: IBS > 0.7168 correlaciona con éxito en UPDOWN_GBM#15min (IC=+0.158 n=220). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#BTC#15min**: IBS > 0.6374 correlaciona con éxito en UPDOWN_GBM#BTC#15min (IC=+0.172 n=117). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#BTC#15min**: IBS < 0.1169 correlaciona con éxito en UPDOWN_GBM#BTC#15min (IC=+0.196 n=21). Confirma señal de reversión media → alinear con BUY_YES.
- **H-IBS-UPDOWN_GBM#ETH#15min**: IBS > 0.7617 correlaciona con éxito en UPDOWN_GBM#ETH#15min (IC=+0.204 n=86). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#XRP#15min**: IBS < 0.0448 correlaciona con éxito en UPDOWN_GBM#XRP#15min (IC=+0.250 n=22). Confirma señal de reversión media → alinear con BUY_YES.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN` — IC=+0.203 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#BTC#5min` — IC=+0.203 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#BTC` — IC=+0.203 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `LATE_WINDOW_5MIN#5min` — IC=+0.203 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH#15min` — IC=+0.149 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `STREAK_FADE_15M#ETH` — IC=+0.149 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ FAVORITO_CONFIRMADO | 974 | +0.181 | +7.83€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 627 | +0.212 | +12.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 40 | +0.048 | +1.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 145 | +0.092 | -12.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 162 | +0.171 | +6.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 286 | +0.184 | -5.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 209 | +0.206 | -7.14€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 13 | +0.108 | +2.62€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 54 | +0.179 | +3.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 346 | +0.164 | -1.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 208 | +0.205 | +2.58€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 13 | -0.065 | -1.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 71 | +0.089 | -8.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 54 | +0.161 | +6.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL | 340 | +0.196 | +14.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 208 | +0.224 | +17.15€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 14 | +0.044 | +0.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 64 | +0.151 | -0.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 54 | +0.161 | -2.61€ | 0 | 2 |
| ✅ GBM_LATE_15M | 3647 | +0.114 | +1217.37€ | 0 | 9 |
| ✅ GBM_LATE_15M#15min | 3647 | +0.114 | +1217.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 895 | +0.070 | +118.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 895 | +0.070 | +118.69€ | 0 | 2 |
| ✅ GBM_LATE_15M#ETH | 923 | +0.074 | +159.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 923 | +0.074 | +159.46€ | 0 | 2 |
| ✅ GBM_LATE_15M#SOL | 951 | +0.139 | +473.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 951 | +0.139 | +473.05€ | 0 | 8 |
| ✅ GBM_LATE_15M#XRP | 878 | +0.172 | +466.18€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 878 | +0.172 | +466.18€ | 0 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 1001 | +0.164 | +565.28€ | 0 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 1001 | +0.164 | +565.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 264 | +0.158 | +167.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 264 | +0.158 | +167.41€ | 0 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 267 | +0.132 | +108.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 267 | +0.132 | +108.17€ | 0 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 280 | +0.121 | +98.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 280 | +0.121 | +98.70€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 190 | +0.276 | +190.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 190 | +0.276 | +190.99€ | 0 | 6 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 1154 | +0.082 | +287.86€ | 1 | 7 |
| ✅ GBM_LATE_15M_TARDIO#15min | 1154 | +0.082 | +287.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 268 | +0.078 | +40.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 268 | +0.078 | +40.34€ | 0 | 1 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 288 | +0.010 | +11.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 288 | +0.010 | +11.53€ | 0 | 2 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 300 | +0.036 | +36.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 300 | +0.036 | +36.94€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 298 | +0.200 | +199.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 298 | +0.200 | +199.05€ | 0 | 7 |
| ✅ GBM_LATE_60M | 313 | -0.113 | +7.56€ | 2 | 1 |
| ✅ GBM_LATE_60M#60min | 313 | -0.113 | +7.56€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 108 | -0.027 | +6.52€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 108 | -0.027 | +6.52€ | 3 | 1 |
| ✅ GBM_LATE_60M#ETH | 95 | -0.160 | -10.23€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 95 | -0.160 | -10.23€ | 4 | 0 |
| ✅ GBM_LATE_60M#SOL | 110 | -0.152 | +11.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 110 | -0.152 | +11.27€ | 5 | 1 |
| ✅ LATE_WINDOW_5MIN | 35 | +0.203 | +10.30€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 35 | +0.203 | +10.30€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 35 | +0.203 | +10.30€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 35 | +0.203 | +10.30€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 68 | +0.129 | +20.94€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 68 | +0.129 | +20.94€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 68 | +0.129 | +20.94€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 68 | +0.129 | +20.94€ | 0 | 3 |
| ✅ ORDER_FLOW_5M | 1584 | +0.013 | +17.50€ | 1 | 1 |
| ✅ ORDER_FLOW_5M#5min | 1448 | +0.009 | +4.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 192 | +0.051 | +8.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 192 | +0.051 | +8.62€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 2 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 208 | +0.000 | -1.36€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 208 | +0.000 | -1.36€ | 2 | 1 |
| ✅ ORDER_FLOW_5M#ETH | 250 | -0.016 | -7.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 250 | -0.016 | -7.42€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 320 | +0.040 | +13.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 320 | +0.040 | +13.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 187 | -0.003 | -2.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 187 | -0.003 | -2.88€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM | 138 | -0.150 | +0.19€ | 4 | 1 |
| 🚫 PRICE_TARGET_GBM#BTC | 62 | -0.250 | -18.09€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 56 | -0.276 | -17.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 6 | +0.000 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 49 | -0.128 | +4.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 46 | -0.167 | -0.47€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 27 | +0.052 | +13.93€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 26 | +0.036 | +13.14€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 128 | -0.177 | -4.68€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 10 | +0.083 | +4.87€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 10 | +0.208 | +4.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 10 | +0.208 | +4.00€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 154 | +0.122 | +24.62€ | 0 | 7 |
| ✅ STREAK_FADE_15M#15min | 154 | +0.122 | +24.62€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 35 | +0.149 | +7.63€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 35 | +0.149 | +7.63€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 55 | +0.149 | +13.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 55 | +0.149 | +13.31€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 64 | +0.076 | +3.68€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 64 | +0.076 | +3.68€ | 0 | 3 |
| ✅ STREAK_FADE_5M | 163 | -0.039 | -10.45€ | 4 | 0 |
| ✅ STREAK_FADE_5M#5min | 163 | -0.039 | -10.45€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 45 | -0.138 | -7.05€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 45 | -0.138 | -7.05€ | 5 | 0 |
| ✅ STREAK_FADE_5M#SOL | 58 | -0.033 | -3.85€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 58 | -0.033 | -3.85€ | 1 | 0 |
| ✅ STREAK_FADE_5M#XRP | 60 | +0.032 | +0.46€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 60 | +0.032 | +0.46€ | 0 | 1 |
| 🚫 STREAK_MOM_5M | 309 | -0.056 | -23.67€ | 6 | 0 |
| ✅ STREAK_MOM_5M#5min | 309 | -0.056 | -23.67€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 103 | -0.052 | -6.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 103 | -0.052 | -6.34€ | 2 | 0 |
| ✅ STREAK_MOM_5M#SOL | 108 | -0.009 | -3.98€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 108 | -0.009 | -3.98€ | 2 | 3 |
| ✅ STREAK_MOM_5M#XRP | 98 | -0.110 | -13.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 98 | -0.110 | -13.35€ | 5 | 0 |
| 🚫 STRUCT_NO_15M | 15 | -0.199 | -4.68€ | 0 | 0 |
| 🚫 STRUCT_NO_15M#15min | 15 | -0.199 | -4.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ UPDOWN_GBM | 1333 | -0.006 | +25.21€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1077 | +0.023 | +62.68€ | 1 | 4 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 127 | -0.058 | -10.76€ | 7 | 0 |
| ✅ UPDOWN_GBM#BNB | 24 | -0.154 | -7.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 24 | -0.154 | -7.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 360 | +0.011 | +7.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 281 | +0.051 | +20.83€ | 1 | 8 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 42 | -0.068 | -6.16€ | 2 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 14 | -0.087 | +2.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 27 | -0.086 | -4.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 24 | -0.077 | -3.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 659 | +0.014 | +36.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 566 | +0.034 | +47.24€ | 0 | 3 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 54 | -0.018 | -2.56€ | 3 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 170 | -0.087 | -14.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 102 | -0.058 | -7.39€ | 7 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 31 | -0.106 | -2.03€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 91 | +0.005 | +9.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 80 | +0.037 | +13.02€ | 4 | 5 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 41 | -0.198 | +1.92€ | 0 | 0 |
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
| ✅ WEEKLY_PRICE | 204 | +0.073 | -13.93€ | 2 | 2 |
| ✅ WEEKLY_PRICE#BTC | 62 | +0.047 | -10.26€ | 0 | 0 |
| ✅ WEEKLY_PRICE#ETH | 62 | +0.078 | -7.26€ | 0 | 0 |
| ✅ WEEKLY_PRICE#SOL | 80 | +0.085 | +3.58€ | 0 | 2 |
## Hipótesis pendientes — tracking automático


### 🔴 Listas para implementar YA

**🔴 H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Confirma: IC=-0.161 n=119 PNL=-29.87€ → añadir 18 a GBM_BLACKLIST_HOURS
  - _Datos_: n=119 IC=-0.161 PNL=-29.87€


### 🟡 Listas para evaluar

**〰️ H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread bajo (0.123) — sin ventaja clara. oversold(IBS<0.3): IC=-0.023 n=346 | neutral: IC=-0.047 n=263 | overbought(IBS>0.7): IC=+0.076 n=293
  - _Datos_: n=943 IC=+0.008 PNL=+50.44€

**🟡 H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: H=02h: IC=-0.156 n=30 PNL=-6.41€ → FILTRAR | H=07h: IC=+0.110 n=39 PNL=+13.58€ → BOOST | H=10h: IC=-0.154 n=15 PNL=-6.77€ → FILTRAR | H=14h: IC=+0.128 n=41 PNL=+13.00€ → BOOST | H=17h: IC=+0.112 n=47 PNL=+12.54€ → BOOST | H=22h: IC=+0.108 n=49 PNL=+7.56€ → BOOST

**🟡 H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 187 ops con delta_ratio | SOL: 219 ops con delta_ratio

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=-0.058 < 0.08 — monitorear
  - _Datos_: n=102 IC=-0.058 PNL=-7.39€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=62/15 IC=+0.078 PNL=-7.26€ | BTC: n=62/15 IC=+0.047 PNL=-10.26€ | SOL: n=80/15 IC=+0.085 PNL=+3.58€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.092 n=6351 | tras_1loss IC=+0.047 n=4732 | tras_2loss IC=+0.013 n=2117/40 | gap=+0.079 (umbral 0.05)

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 6 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#ETH, UPDOWN_GBM#BTC, UPDOWN_GBM#15min, UPDOWN_GBM#BTC#15min
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.127 n=73/60 | contraria IC=+0.065 n=21 | gap=+0.061 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=31, boost estimado=-0.027. Necesita 0 más y boost>0.05

**⏳ H-KELLY-HORA** — Kelly boost ×1.2 en horas top (15/17/19h UTC)
  - _Umbral_: n≥40 por hora con IC estable ≥+0.10 confirmado en forward
  - _Acción_: Añadir HORA_BOOST = {13: 1.2, 15: 1.2, 17: 1.2, 19: 1.2} en shadow_predict.py
  - _Estado_: H=13h UTC: IC=+0.081 n=501/40 PNL=+118.88€ | H=15h UTC: IC=+0.097 n=502/40 PNL=+126.74€ | H=17h UTC: IC=+0.136 n=429/40 PNL=+150.47€ | H=19h UTC: IC=+0.063 n=385/40 PNL=+49.78€

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=54/40 IC=-0.018 PNL=-2.56€ | BTC#60min: n=42/40 IC=-0.068 PNL=-6.16€ | SOL#60min: n=31/40 IC=-0.106 PNL=-2.03€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=-0.004 n=123 | contrario_BTC IC=-0.059 n=57/40 | gap=-0.055 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


### 🔒 Bloqueadas (requieren dataset/API)

**🔒 H-OBI** — Orderbook Imbalance como señal
  - _Umbral_: Dataset Jon-Becker + API CLOB con orderbook histórico
  - _Acción_: Implementar s_obi en shadow_predict.py usando L2 orderbook
  - _Estado_: Descargar github.com/Jon-Becker/prediction-market-analysis (36GB). Analizar spread bid/ask e imbalance por mercado en 60min previos a resolución.
  - _Bloqueante_: JON_BECKER_DATASET

**🔒 H-OU-THETA** — Calibrar theta OU con datos históricos
  - _Umbral_: Dataset Jon-Becker con series de precios históricos suficientes
  - _Acción_: Ajustar THETA_OU por par en strategy_params.json (BTC/ETH/SOL independientes)
  - _Estado_: Descargar github.com/Jon-Becker/prediction-market-analysis (36GB). Fit OU sobre series históricas por par y estimar theta por MLE.
  - _Bloqueante_: JON_BECKER_DATASET

**🔒 H-HMM-REGIME** — HMM para régimen de mercado
  - _Umbral_: n≥200 ops GBM forward con hora_utc/ibs_15, o dataset Jon-Becker
  - _Acción_: Implementar hmmlearn sobre features GBM; condicionar estrategia al régimen detectado
  - _Estado_: Descargar github.com/Jon-Becker/prediction-market-analysis (36GB). Entrenar HMM 3-estado sobre (drift_60min, sigma_h) histórico. Validar en forward.
  - _Bloqueante_: JON_BECKER_DATASET

**🔒 H-CROSS-ARB** — Arbitraje Polymarket vs Kalshi
  - _Umbral_: API Kalshi activa + credenciales Polymarket live
  - _Acción_: Extender arb_scanner.py con endpoints Kalshi; comparar mismo evento cross-plataforma
  - _Estado_: Requiere acceso API Kalshi + credenciales Polymarket live
  - _Bloqueante_: API_KALSHI


### 🧪 Hipótesis custom (editables en hipotesis_custom.json)

**〰️ H-24H-GBM-BUYYES-MADRUGADA** — GBM BUY_YES en madrugada europea (05-07h UTC) — señal alcista
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona en horas 05-07h UTC (7-9h Madrid). IC=+0.087 n=14 a las 06h, +0.063 n=11 a las 05h, +0.067 n=17 a las 07h. Hipótesis: apertura europea genera momentum alcista que el GBM captura. La dirección dominante cambia de BUY_NO (madrugada americana 13h) a BUY_YES (apertura europea). Objetivo: cubrir franja horaria 05-07h UTC en el camino hacia operación 24h.
  - _Umbral_: n≥40 en franja 05-07h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → añadir GBM BUY_YES a subtypes_permitidos_live para horas 05-07h UTC
  - _Estado_: n=70 IC=+0.069 PNL=+13.50€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=70 IC=+0.069 PNL=+13.50€

**〰️ H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: n=213 IC=+0.002 PNL=+7.10€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=213 IC=+0.002 PNL=+7.10€

**〰️ H-24H-OF-18H** — ORDER_FLOW BUY_NO a las 18h UTC — GBM bloqueado pero OF funciona
  - _Hipótesis_: GBM está en blacklist a las 18h UTC (IC muy negativo). Pero ORDER_FLOW BUY_NO BTC+SOL a las 18h: IC=+0.106 n=11. El blacklist de GBM no debería afectar a OF. Hipótesis: son señales independientes — OF captura flujo real de órdenes mientras GBM falla con el modelo de precios en esa hora. Objetivo: activar OF BUY_NO específicamente a las 18h sin tocar blacklist GBM.
  - _Umbral_: n≥25 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥25 → eliminar 18h del blacklist ORDER_FLOW (no del GBM) para recuperar esa hora
  - _Estado_: n=433 IC=+0.038 PNL=+13.82€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=433 IC=+0.038 PNL=+13.82€

**🟡 H-WEEKLY-BUYNO** — WEEKLY_PRICE BUY_NO — dirección dominante con IC muy alto
  - _Hipótesis_: Split por dirección en WEEKLY_PRICE: BUY_NO n=38 WR=66% IC=+0.316 vs BUY_YES n=19 WR=21% IC=-0.579. El mercado semanal de precios tiende a NO cumplir el target → BUY_NO tiene edge estructural fuerte. PNL negativo por apuestas pequeñas y slippage, no por dirección. Candidata live si se confirma con n≥50.
  - _Umbral_: n≥50 y IC>+0.10
  - _Acción_: Si IC>+0.10 con n≥50 → activar WEEKLY_PRICE BUY_NO en live (filtrar BUY_YES). Si IC cae <+0.05 con n≥50 → el edge se ha erosionado.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.202 > 0.1 con n=149 PNL=+4.24€
  - _Datos_: n=149 IC=+0.202 PNL=+4.24€

**🔶 H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.249 n=19) pero sin cruzar ≥2 pares más — DOGE: n=1 IC=+0.008; ETH: n=31 IC=+0.136 ✓; SOL: n=3 IC=+0.015; XRP: n=1 IC=-0.008
  - _Datos_: n=19 IC=+0.249 PNL=+12.62€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=96 IC=+0.061 PNL=+11.20€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=96 IC=+0.061 PNL=+11.20€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=1206 IC=+0.000 PNL=+39.21€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1206 IC=+0.000 PNL=+39.21€

**⏳ H-CUSTOM-OF-02H-BTCSOL** — ORDER_FLOW H=02h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 02h está en el blacklist basado en TODOS los pares. Con BTC+SOL solo, el historial muestra 4/5 (80%) IC=+0.054. ¿Se confirma la señal positiva con más datos?
  - _Umbral_: 15
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 02h del blacklist ORDER_FLOW
  - _Estado_: 6/15 ops en el filtro definido (IC actual=+0.075 PNL=+2.93€)
  - _Datos_: n=6 IC=+0.075 PNL=+2.93€

**⏳ H-CUSTOM-OF-07H-BTCSOL** — ORDER_FLOW H=07h UTC — BTC+SOL solamente (revisar blacklist)
  - _Hipótesis_: La hora 07h está en el blacklist. Con BTC+SOL solo, el historial muestra 7/12 (58%) IC=+0.043. El blacklist puede estar basado en pares negativos que ya están excluidos.
  - _Umbral_: 20
  - _Acción_: Si IC>0.05 con n≥20 → proponer eliminar 07h del blacklist ORDER_FLOW
  - _Estado_: 12/20 ops en el filtro definido (IC actual=+0.043 PNL=+0.95€)
  - _Datos_: n=12 IC=+0.043 PNL=+0.95€

**〰️ H-CUSTOM-GBM-60MIN-BUYYES** — GBM 60min BUY_YES — ¿edge superior al BUY_NO?
  - _Hipótesis_: Análisis actual muestra BUY_YES 60min: 22/36 (61%) IC=+0.105 vs BUY_NO 60min: 8/14 (57%) IC=+0.044. En 60min parece que BUY_YES es la dirección dominante, al contrario que en 15min.
  - _Umbral_: n≥30 y IC>+0.08
  - _Acción_: Si BUY_YES 60min confirma IC≥0.10 n≥40 → prioridad live por encima de BUY_NO
  - _Estado_: n=89 IC=-0.060 PNL=-7.60€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=89 IC=-0.060 PNL=-7.60€

**〰️ H-CUSTOM-GBM-60MIN-BUYNO** — GBM 60min BUY_NO — tracking por separado
  - _Hipótesis_: En 15min BUY_NO tiene IC=+0.119. ¿Se repite en 60min? Datos actuales: 8/14 (57%) IC=+0.044 — positivo pero débil. Puede ser que 60min requiera dirección alcista (BUY_YES) y no bajista.
  - _Umbral_: n≥30 para confirmar dirección
  - _Acción_: Si IC<0.05 con n≥30 → en 60min priorizar solo BUY_YES; si IC>0.08 → igualar al BUY_YES
  - _Estado_: n=38 IC=-0.050 PNL=-3.16€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=38 IC=-0.050 PNL=-3.16€

**🔴 H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.138 < -0.08 con n=172 PNL=-38.45€
  - _Datos_: n=172 IC=-0.138 PNL=-38.45€

**〰️ H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: n=614 IC=+0.018 PNL=+26.52€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=614 IC=+0.018 PNL=+26.52€

**⏳ H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0008/h) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? sigma_h<0.0008 equivale a volatilidad diaria <0.8%.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0008
  - _Estado_: 2/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.01€)
  - _Datos_: n=2 IC=+0.000 PNL=+0.01€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=281 IC=+0.051 PNL=+20.83€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=281 IC=+0.051 PNL=+20.83€

**〰️ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: n≥50 en zona muerta y IC<-0.03
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: n=80 IC=-0.024 PNL=-1.28€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=80 IC=-0.024 PNL=-1.28€

**〰️ H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: n=558 IC=+0.052 PNL=+45.53€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=558 IC=+0.052 PNL=+45.53€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 20/30 ops en el filtro definido (IC actual=-0.136 PNL=-3.39€)
  - _Datos_: n=20 IC=-0.136 PNL=-3.39€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=77 IC=+0.032 PNL=+7.28€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=77 IC=+0.032 PNL=+7.28€

**⏳ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: 25
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: 20/25 ops en el filtro definido (IC actual=-0.182 PNL=-10.59€)
  - _Datos_: n=20 IC=-0.182 PNL=-10.59€

**🔴 H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.155 < -0.08 con n=27 PNL=-10.44€
  - _Datos_: n=27 IC=-0.155 PNL=-10.44€

**⏳ H-FUNDING-HIGH-BUYNO** — Funding rate alto (>0.03%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance > 0.03%/8h, los longs están sobrecargados y pagan por mantener. El mercado es structuralmente vulnerable a corrección. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral.
  - _Umbral_: 40
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.03
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**⏳ H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: 30
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**🔶 H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.203 n=35) pero sin cruzar ≥2 pares más — sin otros pares con datos
  - _Datos_: n=35 IC=+0.203 PNL=+10.30€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=433 IC=+0.013 PNL=+16.84€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=433 IC=+0.013 PNL=+16.84€

**⏳ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: 40
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: 0/40 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: n=347 IC=-0.007 PNL=-5.82€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=347 IC=-0.007 PNL=-5.82€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.250 > 0.08 con n=62 PNL=+16.47€
  - _Datos_: n=62 IC=+0.250 PNL=+16.47€

**〰️ H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: n=54 IC=+0.036 PNL=+28.24€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=54 IC=+0.036 PNL=+28.24€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=503 IC=+0.033 PNL=+28.68€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=503 IC=+0.033 PNL=+28.68€

**〰️ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: n≥100 PERO ADEMÁS necesita cubrir al menos 2-3 ventanas de retrogradación distintas (no solo la de jun-jul 2026) — esperar mínimo hasta después de la ventana de oct-nov 2026
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: n=8763 IC=+0.098 PNL=+2179.05€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=8763 IC=+0.098 PNL=+2179.05€

**〰️ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: n≥40 y IC>+0.08 — además necesita que existan wallets 'smart' acumuladas (0 al empezar, se van descubriendo cada ciclo)
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: n=121 IC=+0.004 PNL=+0.53€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=121 IC=+0.004 PNL=+0.53€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.036 > 0.02 con n=453 PNL=+22.75€
  - _Datos_: n=453 IC=+0.036 PNL=+22.75€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=49 IC=-0.049 PNL=+20.99€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=49 IC=-0.049 PNL=+20.99€

**🔴 H-CUSTOM-WEEKLY-INRANGE-BUYYES** — WEEKLY_PRICE BUY_YES con in_range=1 — ¿estructuralmente sobrevalorado?
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_YES cuando in_range=1 fue 0/3 (todo pérdida). Mecanismo propuesto: acertar un rango de precio estrecho al vencimiento es intrínsecamente poco probable, el mercado puede estar sobrevalorando el 'sí'. Ver H-CUSTOM-WEEKLY-PCTDIST-BUYNO para el lado complementario (BUY_NO con pct_dist alto).
  - _Umbral_: n≥25 y IC<-0.10 para confirmar (evidencia inicial es de solo 3 ops)
  - _Acción_: Si se confirma con n≥25 → filtro causal in_range==1 + BUY_YES → skip en WEEKLY_PRICE
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.257 < -0.1 con n=35 PNL=-7.43€
  - _Datos_: n=35 IC=-0.257 PNL=-7.43€

**🟡 H-CUSTOM-WEEKLY-PCTDIST-BUYNO** — WEEKLY_PRICE BUY_NO con pct_dist alto — cuanto más lejos del rango, más seguro
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_NO con pct_dist>=2.09% fue 4/4 victorias (rango 2.09%-23.4%); BUY_NO con pct_dist<8% (pero fuera del corte anterior) tuvo derrotas. Patrón: cuanto más lejos está el spot del rango objetivo al momento de la predicción, más fiable el BUY_NO. Complementa H-CUSTOM-WEEKLY-INRANGE-BUYYES.
  - _Umbral_: n≥25 y IC>+0.10 para confirmar
  - _Acción_: Si se confirma con n≥25 → boost ×1.2 en WEEKLY_PRICE BUY_NO cuando pct_dist≥2
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.285 > 0.1 con n=77 PNL=+12.82€
  - _Datos_: n=77 IC=+0.285 PNL=+12.82€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=761 IC=-0.015 PNL=-3.95€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=761 IC=-0.015 PNL=-3.95€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.169 > 0.1 con n=276 PNL=+99.72€
  - _Datos_: n=276 IC=+0.169 PNL=+99.72€

**⏳ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: 40
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: 32/40 ops en el filtro definido (IC actual=-0.118 PNL=-3.36€)
  - _Datos_: n=32 IC=-0.118 PNL=-3.36€

**🟡 H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.114 > 0.1 con n=55 PNL=+16.18€
  - _Datos_: n=55 IC=+0.114 PNL=+16.18€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=29 IC=-0.177 PNL=+3.50€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=29 IC=-0.177 PNL=+3.50€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=152 IC=+0.071 PNL=+11.39€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=152 IC=+0.071 PNL=+11.39€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro skip aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 0/20 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=375 IC=-0.068 PNL=+62.77€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=375 IC=-0.068 PNL=+62.77€

**⏳ H-CUSTOM-LATE15-PHOTO-FINISH** — GBM_LATE_15M photo finish — entrar pegado al strike es moneda al aire cobrada como favorito
  - _Hipótesis_: Detectado 2026-07-05 validando contra nuestros datos la única idea aprovechable de un artículo-anuncio de copy-bot: GBM_LATE_15M con |drift_ventana_pct|<0.02 tenía IC=-0.145 n=181 (win 35%, -9.70€), estable en ambas mitades temporales (-0.163/-0.127), monótono con la distancia (0.02-0.05: IC=+0.061; ≥0.05: IC=+0.14..0.19) y consistente en crudo y normalizado por sigma (|d_gbm|<0.1 IC=-0.081 n=244). BTC (IC=-0.163 n=90) y ETH (-0.130 n=79) concentraban el daño; SOL/XRP apenas entran en esa zona. Mecanismo: sin distancia real al strike el resultado es ~50/50 pero py_entrada ya cobra favorito. Filtro GBM_LATE_DRIFT_VENT_MIN_PCT=0.02 aplicado en shadow_predict el 2026-07-05. Esta hipótesis trackea la zona filtrada: si vuelven a aparecer ops aquí, el filtro se ha roto.
  - _Umbral_: 200
  - _Acción_: Si aparecen ops nuevas en la zona → el filtro está roto, revisar shadow_predict. Si el buffer [0.02,0.05) se vuelve negativo con n≥60 forward → subir el corte a 0.05.
  - _Estado_: 183/200 ops en el filtro definido (IC actual=-0.143 PNL=-10.06€)
  - _Datos_: n=183 IC=-0.143 PNL=-10.06€

**⏳ H-CUSTOM-PHOTO-FINISH-SNIPER** — Photo finish sniper — comprar el lado rezagado a 1-3c en los últimos segundos (estilo egig)
  - _Hipótesis_: 2026-07-05: wallet 'egig' verificada on-chain (leaderboard oficial +$41k all-time; flujo 23h: -$729 compras / +$2,140 redeems). Forense de 497 trades: compra a 1-3c (mediana 2c) el lado rezagado a mediana 2s del cierre, exclusivamente en photo finishes (dist spot-strike mediana 0.027%). Mecanismo: el mercado cobra los finales de foto como decididos cuando son ~moneda al aire — es el espejo del filtro photo finish que aplicamos a GBM_LATE el mismo día. Win rate implícito ~6% con breakeven 2% (~3x por ticket). photo_finish_logger.py (screen pfinish) acumula dataset en data/shadow/photo_finish_YYYY-MM-DD.csv: libro del lado rezagado a T-10s + outcome oficial vía outcomePrices. CAVEATS a medir: profundidad real del ask a 1-3c (egig compite por asks rancios), frecuencia del setup, y que nuestro T-10s no es su T-2s.
  - _Umbral_: 200
  - _Acción_: Si EV>2x sostenido con n≥200 → proponer watcher de ejecución dedicado (decisión de Javi: toca dinero real y requiere loop sub-5s). Si win rate ≈ ask (mercado calibrado también aquí) → archivar.
  - _Estado_: 0/200 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-CUSTOM-LATE15-BTC-BUYNO-COINFLIP** — GBM_LATE_15M BTC#BUY_NO es moneda al aire — candidata a quitar del motor estrella
  - _Hipótesis_: Detectado 2026-07-06 desglosando la estrategia que carga el bankroll shadow (GBM_LATE_15M, +364€): por par×dirección, BTC#BUY_NO es la única tupla sin edge — 90/182 (49.5%) PNL=+8.92€, prácticamente coinflip, arrastrando a la baja el IC medio del subtipo. Contraste con las estrellas del mismo motor: SOL#BUY_NO 66.1% (+86.70€), XRP#BUY_YES 67.4% (+80.35€), SOL#BUY_YES 64.4% (+77.08€). ETH#BUY_NO (53.6%) es débil pero positivo; BTC#BUY_YES (57.8%) sí funciona. Hipótesis: el edge de entrada tardía en 15min es fuerte en SOL/XRP, medio en ETH/BTC alcista, y NULO en BTC bajista (BTC es el par más eficiente/arbitrado). Quitar BTC#BUY_NO sube el IC del subtipo sin perder PNL real. NO afecta live (la whitelist live es SOL/XRP BUY_NO + ETH BUY_YES, BTC no está).
  - _Umbral_: n≥150 y IC<+0.03 (n=182 ya disponible al crearla)
  - _Acción_: Si IC<+0.03 con n≥150 → filtro causal skip GBM_LATE_15M BTC#BUY_NO en shadow_predict (deja de diluir el subtipo). Si IC sube >+0.08 → mantener.
  - _Estado_: n=460 IC=+0.054 PNL=+39.04€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=460 IC=+0.054 PNL=+39.04€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.170 > 0.08 con n=210 PNL=+72.77€
  - _Datos_: n=210 IC=+0.170 PNL=+72.77€

**⏳ H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: 102
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: 79/102 ops en el filtro definido (IC actual=-0.031 PNL=-1.97€)
  - _Datos_: n=79 IC=-0.031 PNL=-1.97€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.158 > 0.08 con n=302 PNL=+127.94€
  - _Datos_: n=302 IC=+0.158 PNL=+127.94€

**🔶 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA en BTC (IC=+0.225 n=89) pero sin cruzar ≥2 pares más — ETH: n=109 IC=+0.140 ✓; SOL: n=7 IC=-0.019; XRP: n=5 IC=+0.018
  - _Datos_: n=89 IC=+0.225 PNL=+37.20€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema, sin filtrar todavía
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15) pero nunca aplicado al lado BUY_YES de GBM_LATE_15M — el pipeline causal automático no lo ha cazado porque `filtros_causales` está a null en las 4 tuplas de GBM_LATE_15M en strategy_params.json (no bucketiza esta columna todavía). CAVEAT: en LIVE (dinero real) la misma zona da +14.03€ en n=27 — no confirma el signo negativo, posiblemente ruido de muestra pequeña o que el re-quote/veto de profundidad ya filtra parcialmente los peores casos antes de ejecutar. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar
  - _Acción_: Si confirma con n≥289 IC<-0.10 → filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M (afecta a estrategia LIVE, dinero real — proponer a Javi antes de tocar shadow_predict.py). Si el signo se revierte con n≥289 (como sugiere el n=27 de live) → archivar, era ruido de la muestra shadow retrospectiva.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.157 < -0.1 con n=316 PNL=-34.85€
  - _Datos_: n=316 IC=-0.157 PNL=-34.85€

**🟡 H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.309 > 0.2 con n=145 PNL=+104.00€
  - _Datos_: n=145 IC=+0.309 PNL=+104.00€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 20/40 ops en el filtro definido (IC actual=+0.136 PNL=+5.87€)
  - _Datos_: n=20 IC=+0.136 PNL=+5.87€

**⏳ H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: 17/40 ops en el filtro definido (IC actual=+0.157 PNL=+14.16€)
  - _Datos_: n=17 IC=+0.157 PNL=+14.16€

**⏳ H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: 13/40 ops en el filtro definido (IC actual=+0.108 PNL=+13.05€)
  - _Datos_: n=13 IC=+0.108 PNL=+13.05€

**⏳ H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct<0 en XRP#15min
  - _Estado_: 22/40 ops en el filtro definido (IC actual=+0.208 PNL=+18.85€)
  - _Datos_: n=22 IC=+0.208 PNL=+18.85€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.176 > 0.08 con n=66 PNL=+1.29€
  - _Datos_: n=66 IC=+0.176 PNL=+1.29€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.327 > 0.08 con n=73 PNL=+10.59€
  - _Datos_: n=73 IC=+0.327 PNL=+10.59€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 23/40 ops en el filtro definido (IC actual=+0.100 PNL=+4.68€)
  - _Datos_: n=23 IC=+0.100 PNL=+4.68€

**⏳ H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: 40
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: 35/40 ops en el filtro definido (IC actual=+0.203 PNL=+20.04€)
  - _Datos_: n=35 IC=+0.203 PNL=+20.04€

**⏳ H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: 38/40 ops en el filtro definido (IC actual=+0.250 PNL=+23.98€)
  - _Datos_: n=38 IC=+0.250 PNL=+23.98€
