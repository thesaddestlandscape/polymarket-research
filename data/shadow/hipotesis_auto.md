# Hipótesis automáticas — 2026-07-17 01:11 UTC
_Generado por shadow_postmortem.py sobre 17857 resoluciones (PNL=+3736.11€)_

## Patrones causales activos

### FAVORITO_CONFIRMADO
- **PATRÓN** `hora_utc` < `18.0` → IC=+0.193 (n=1014)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 18.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` > `0.695` → IC=+0.292 (n=460)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.695 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=1165)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `4371.9525` → IC=+0.183 (n=666)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 4371.9525 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.199 (n=426)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.191 (n=383)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 6.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.339 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=1239)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `7405.3527` → IC=+0.184 (n=362)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 7405.3527 (IC base=+0.170)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` < `8.0` → IC=+0.243 (n=99)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.615` → IC=+0.245 (n=198)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.615 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.226 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.227 (n=159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.370 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.207)

- **PATRÓN** `libro_liquidez` > `7163.0167` → IC=+0.207 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7163.0167 (IC base=+0.207)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=59)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.200 (n=58)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 19.0 (IC base=+0.149)

- **PATRÓN** `py_entrada` < `0.565` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.565 (IC base=+0.149)

- **PATRÓN** `py_entrada` > `0.605` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `py_entrada` > 0.605 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `8909.1861` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8909.1861 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.250 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.288 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` < `0.425` → IC=+0.229 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.425 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `7674.945` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7674.945 (IC base=+0.171)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.214 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.228 (n=222)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.354 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `5265.1543` → IC=+0.213 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5265.1543 (IC base=+0.205)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.210 (n=229)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.361 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `3728.3706` → IC=+0.204 (n=228)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3728.3706 (IC base=+0.202)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` < `18.0` → IC=+0.219 (n=55)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` < `0.595` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.595 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `5380.041` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 5380.041 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.197 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 15.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.220 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.214 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.405 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `4530.0713` → IC=+0.198 (n=61)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 4530.0713 (IC base=+0.163)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.241 (n=83)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.222)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.232 (n=80)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.222)

- **PATRÓN** `py_entrada` > `0.62` → IC=+0.281 (n=194)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.62 (IC base=+0.222)

- **PATRÓN** `libro_liquidez` > `1592.1422` → IC=+0.226 (n=217)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1592.1422 (IC base=+0.222)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.226 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.210 (n=226)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.266 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.206)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.227 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.167 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 7.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.575 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.125 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.080)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.080)

### GBM_LATE_15M
- **PATRÓN** `dist_vwap_pct` > `0.6196` → IC=+0.130 (n=125)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.6196 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.274` → IC=+0.210 (n=143)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.274 (IC base=+0.107)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.131 (n=1292)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0091 (IC base=+0.106)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.129 (n=1393)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 12.0 (IC base=+0.106)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `14.745` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 14.745 (IC base=+0.076)

- **PATRÓN** `dist_vwap_pct` > `0.138` → IC=+0.136 (n=42)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.138 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` < `0.4426` → IC=+0.127 (n=183)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.4426 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.933` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 2.933 (IC base=+0.066)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `sigma_ewma_delta_pct` < `7.476` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 7.476
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=54)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.151 (n=130)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0045 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.6854` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.6854 (IC base=+0.090)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.476` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.476 (IC base=+0.090)

- **PATRÓN** `dist_vwap_pct` > `0.8364` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.8364 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.447` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 7.447 (IC base=+0.067)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `8.263` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.263
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=180)

- **PATRÓN** `sigma_h` < `0.0106` → IC=+0.137 (n=221)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0106 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.146 (n=176)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 18.0 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.605` → IC=+0.200 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.605 (IC base=+0.109)

- **PATRÓN** `sigma_h` < `0.0114` → IC=+0.146 (n=323)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0114 (IC base=+0.127)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.130 (n=484)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.0092 (IC base=+0.127)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.174 (n=354)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 12.0 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.755` → IC=+0.125 (n=142)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 2.755 (IC base=+0.127)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_h` < `0.0305` → IC=+0.148 (n=469)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0305 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0133` → IC=+0.160 (n=419)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0133 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.151 (n=419)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 8.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.154 (n=420)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 15.0 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.6854` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6854 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.328` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.328 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0274` → IC=+0.214 (n=166)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0274 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.235 (n=179)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` > `0.3336` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.3336 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` < `0.9583` → IC=+0.139 (n=225)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.9583 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.088` → IC=+0.136 (n=201)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 9.088 (IC base=+0.162)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.223 (n=363)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0107 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.170 (n=544)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 13.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.159 (n=817)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 18.0 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.3793` → IC=+0.212 (n=175)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3793 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.007` → IC=+0.307 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.007 (IC base=+0.156)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.183 (n=828)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0048 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.176 (n=421)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 15.0 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.174 (n=311)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 6.0 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` < `0.4244` → IC=+0.194 (n=631)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` < 0.4244 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.037` → IC=+0.215 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.037 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.06` → IC=+0.181 (n=462)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 3.06 (IC base=+0.164)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.134 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0028 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.169 (n=131)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 13.0 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.4991` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.4991 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.777` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 8.777 (IC base=+0.111)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.165 (n=213)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0029 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.179 (n=107)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 15.0 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` > `0.138` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.138 (IC base=+0.139)

- **PATRÓN** `dist_vwap_pct` < `0.4426` → IC=+0.136 (n=182)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.4426 (IC base=+0.139)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.17` → IC=+0.233 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.17 (IC base=+0.139)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.226 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.156 (n=152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 12.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.147 (n=219)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 18.0 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.3457` → IC=+0.187 (n=65)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3457 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `1.1207` → IC=+0.121 (n=159)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 1.1207 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.551` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.551 (IC base=+0.133)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.137 (n=188)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0069 (IC base=+0.126)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.146 (n=213)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0039 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.162 (n=72)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.179 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.8403` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8403 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `1.1308` → IC=+0.144 (n=178)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 1.1308 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.618` → IC=+0.208 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.618 (IC base=+0.126)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `3.075` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.075
  - _Potencial_: sin este filtro IC_bueno=+0.177 (n=131)

- **PATRÓN** `sigma_h` < `0.0093` → IC=+0.149 (n=75)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0093 (IC base=+0.140)

- **PATRÓN** `sigma_h` > `0.0123` → IC=+0.214 (n=103)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0123 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.163 (n=84)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.140 (n=201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 16.0 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.2414` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.2414 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.9959` → IC=+0.152 (n=182)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.9959 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.061` → IC=+0.287 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.061 (IC base=+0.140)

- **PATRÓN** `sigma_h` < `0.0124` → IC=+0.139 (n=217)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0124 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.149 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 5.0 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.2663` → IC=+0.183 (n=140)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.2663 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.075` → IC=+0.177 (n=131)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 3.075 (IC base=+0.113)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` < `0.0214` → IC=+0.274 (n=175)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0214 (IC base=+0.252)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.256 (n=174)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.252)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.280 (n=175)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.252)

- **PATRÓN** `dist_vwap_pct` > `1.0058` → IC=+0.364 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0058 (IC base=+0.252)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.831` → IC=+0.357 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.831 (IC base=+0.252)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.315 (n=187)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.293)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.301 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.293)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.310 (n=93)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` > `0.1912` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1912 (IC base=+0.293)

- **PATRÓN** `dist_vwap_pct` < `0.5285` → IC=+0.309 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5285 (IC base=+0.293)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.458` → IC=+0.307 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.458 (IC base=+0.293)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0151` → IC=+0.191 (n=250)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0151 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.130 (n=349)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 8.0 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `0.6728` → IC=+0.169 (n=119)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.6728 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.1434` → IC=+0.142 (n=330)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1434 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.94` → IC=+0.302 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.94 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.122 (n=310)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 6.0 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` < `0.379` → IC=+0.125 (n=608)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.379 (IC base=+0.096)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.120 (n=156)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 8.0 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.4395` → IC=+0.125 (n=22)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.4395 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` < `0.1341` → IC=+0.125 (n=86)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.1341 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.675` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.675 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.167 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 17.0 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.206` → IC=+0.135 (n=72)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 3.206 (IC base=+0.078)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.142 (n=65)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.004 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.68` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.68 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.821` → IC=+0.145 (n=29)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 7.821 (IC base=+0.025)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `3.17` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.17
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=137)

- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.132 (n=74)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0129 (IC base=+0.087)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.162 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 8.0 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` > `0.8694` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.8694 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.3894` → IC=+0.146 (n=80)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.3894 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.065` → IC=+0.333 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.065 (IC base=+0.087)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0331` → IC=+0.205 (n=225)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0331 (IC base=+0.201)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.219 (n=226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.229 (n=164)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 13.0 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.3403` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3403 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.483` → IC=+0.258 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.483 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.203 (n=89)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0099 (IC base=+0.199)

- **PATRÓN** `sigma_h` > `0.0263` → IC=+0.253 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0263 (IC base=+0.199)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.244 (n=88)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.199)

- **PATRÓN** `dist_vwap_pct` < `0.5017` → IC=+0.192 (n=212)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` < 0.5017 (IC base=+0.199)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.074` → IC=+0.193 (n=190)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` < 8.074 (IC base=+0.199)

### GBM_LATE_60M
- **FILTRO** `dist_vwap_pct` < `0.1109` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1109
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `sigma_ewma_delta_pct` < `16.76` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 16.76
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=3)

- **FILTRO** `sigma_h` > `0.0133` → IC=-0.300 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=118)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.272 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=44)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.152 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0047 (IC base=-0.017)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `sigma_h` > `0.0086` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0086
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=52)

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

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.176 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0053 (IC base=+0.043)

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
- **FILTRO** `py_entrada` > `0.505` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=60)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.151 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 11.0 (IC base=+0.095)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` < 0.505 (IC base=+0.095)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.161 (n=60)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.151 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 11.0 (IC base=+0.095)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` < 0.505 (IC base=+0.095)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=87)

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

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `hora_utc` < `4.0` → IC=+0.121 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 4.0 (IC base=+0.065)

### ORDER_FLOW_5M#XRP#5min
- **FILTRO** `delta_ratio` |x|≤ `0.4307` → IC=-0.136 (n=20)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.4307
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=45)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0105` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0105
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

- **FILTRO** `sigma_h` > `0.0062` → IC=-0.363 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=25)

- **FILTRO** `T_h` < `145.8988` → IC=-0.422 (n=49)

  - _Acción_: SKIP cuando `T_h` < 145.8988
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=17)

- **FILTRO** `pct_vs_K` |x|> `2.6724` → IC=-0.480 (n=49)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6724
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.204 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=-0.214)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.431 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **FILTRO** `T_h` > `98.7549` → IC=-0.455 (n=20)

  - _Acción_: SKIP cuando `T_h` > 98.7549
  - _Potencial_: sin este filtro IC_bueno=-0.389 (n=7)

- **FILTRO** `T_h` < `145.9348` → IC=-0.455 (n=20)

  - _Acción_: SKIP cuando `T_h` < 145.9348
  - _Potencial_: sin este filtro IC_bueno=-0.389 (n=7)

- **FILTRO** `pct_vs_K` |x|> `3.4276` → IC=-0.450 (n=18)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4276
  - _Potencial_: sin este filtro IC_bueno=-0.409 (n=9)

### STREAK_FADE_15M
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.191 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 13.0 (IC base=+0.112)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` < 0.505 (IC base=+0.112)

- **PATRÓN** `py_entrada` > `0.515` → IC=+0.123 (n=51)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` > 0.515 (IC base=+0.112)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `streak_len` < 4.0 (IC base=+0.112)

- **PATRÓN** `regimen_ma_toques` > `3.0` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `regimen_ma_toques` > 3.0 (IC base=+0.112)

- **PATRÓN** `volumen_racha` < `249969.2` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 249969.2 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `1959.3298` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 1959.3298 (IC base=+0.112)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.257 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.089)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.485 (IC base=+0.089)

- **PATRÓN** `regimen_ma_toques` > `5.0` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 5.0 (IC base=+0.089)

- **PATRÓN** `volumen_racha` < `234964.8` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 234964.8 (IC base=+0.089)

### STREAK_FADE_15M#SOL#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.237 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.485 (IC base=+0.183)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `305408.9` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `volumen_racha` > 305408.9
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

- **FILTRO** `hora_utc` > `12.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=22)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.130 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.040)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.167 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 12.0 (IC base=+0.023)

### STREAK_FADE_5M
- **FILTRO** `hora_utc` < `16.0` → IC=-0.167 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=54)

- **FILTRO** `streak_len` > `4.0` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `streak_len` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.010 (n=47)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `py_entrada` < `0.515` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `libro_liquidez` < `7137.8206` → IC=-0.150 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 7137.8206
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

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
- **FILTRO** `hora_utc` < `17.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=6)

- **FILTRO** `libro_liquidez` < `3416.5722` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3416.5722
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **PATRÓN** `libro_liquidez` > `3531.2061` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3531.2061 (IC base=-0.007)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.150 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=61)

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
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=134)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=149)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=76)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=80)

- **FILTRO** `libro_liquidez` < `3222.7779` → IC=-0.134 (n=39)

  - _Acción_: SKIP cuando `libro_liquidez` < 3222.7779
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=117)

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

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.130 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 9.0 (IC base=+0.031)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=22)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.031)

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
- **FILTRO** `sigma_ewma_delta_pct` > `19.693` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.693
  - _Potencial_: sin este filtro IC_bueno=+0.112 (n=176)

- **PATRÓN** `ibs_15` > `0.7222` → IC=+0.175 (n=269)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.88€ cuando `ibs_15` > 0.7222 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `0.7405` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7405 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` < `0.5084` → IC=+0.133 (n=175)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.5084 (IC base=+0.025)

- **PATRÓN** `sigma_ewma_delta_pct` > `21.641` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 21.641 (IC base=+0.025)

- **PATRÓN** `dist_vwap_pct` > `1.0028` → IC=+0.150 (n=18)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 1.0028 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.932` → IC=+0.128 (n=143)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 5.932 (IC base=+0.046)

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
- **FILTRO** `ibs_15` > `0.0522` → IC=-0.167 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.0522
  - _Potencial_: sin este filtro IC_bueno=+0.180 (n=23)

- **PATRÓN** `drift_60min` |x|≤ `0.2197` → IC=+0.124 (n=171)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.62€ cuando `drift_60min` |x|≤ 0.2197 (IC base=+0.066)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.137 (n=166)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 11.0 (IC base=+0.066)

- **PATRÓN** `ibs_15` > `0.6323` → IC=+0.177 (n=156)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.89€ cuando `ibs_15` > 0.6323 (IC base=+0.066)

- **PATRÓN** `dist_vwap_pct` > `0.7448` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7448 (IC base=+0.066)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0535` → IC=+0.129 (n=33)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.64€ cuando `pct_spot_vs_ref` |x|≤ 0.0535 (IC base=+0.022)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.289 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.022)

- **PATRÓN** `ibs_15` < `0.0522` → IC=+0.180 (n=23)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.90€ cuando `ibs_15` < 0.0522 (IC base=+0.022)

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
- **FILTRO** `sigma_ewma_delta_pct` < `18.799` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 18.799
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

- **FILTRO** `sigma_ewma_delta_pct` > `19.409` → IC=-0.150 (n=18)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 19.409
  - _Potencial_: sin este filtro IC_bueno=+0.096 (n=92)

- **PATRÓN** `ibs_15` > `0.7622` → IC=+0.198 (n=94)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.99€ cuando `ibs_15` > 0.7622 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.221` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.221 (IC base=+0.024)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.130 (n=90)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0059 (IC base=+0.043)

- **PATRÓN** `dist_vwap_pct` > `1.0237` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 1.0237 (IC base=+0.043)

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
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0818` → IC=-0.182 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0818
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `sigma_h` > `0.0147` → IC=-0.150 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0147
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `sigma_h` < `0.0205` → IC=-0.132 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0205
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `drift_15min` |x|> `0.4528` → IC=-0.250 (n=18)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4528
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `ibs_15` > `0.0669` → IC=-0.150 (n=18)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.0669
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=37)

- **PATRÓN** `sigma_h` < `0.0111` → IC=+0.184 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0111 (IC base=+0.109)

- **PATRÓN** `sigma_h` > `0.0172` → IC=+0.132 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0172 (IC base=+0.109)

- **PATRÓN** `drift_15min` |x|≤ `1.0416` → IC=+0.128 (n=41)

  - _Acción_: Kelly boost +0.64€ cuando `drift_15min` |x|≤ 1.0416 (IC base=+0.109)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0987` → IC=+0.128 (n=41)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio_macro` |x|> 0.0987 (IC base=+0.109)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.140 (n=23)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 16.0 (IC base=+0.109)

- **PATRÓN** `ibs_15` < `0.0669` → IC=+0.167 (n=37)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.83€ cuando `ibs_15` < 0.0669 (IC base=+0.109)

### WEEKLY_PRICE
- **FILTRO** `T_h` < `145.8516` → IC=-0.230 (n=35)

  - _Acción_: SKIP cuando `T_h` < 145.8516
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **PATRÓN** `T_h` > `111.9928` → IC=+0.312 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9928 (IC base=+0.292)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `144.6192` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 144.6192 (IC base=+0.256)

- **PATRÓN** `T_h` > `144.7029` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 144.7029 (IC base=+0.256)

- **PATRÓN** `pct_dist` |x|≤ `1.2241` → IC=+0.441 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 1.2241 (IC base=+0.256)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `145.7` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7 (IC base=+0.214)

- **PATRÓN** `pct_dist` |x|≤ `2.4966` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 2.4966 (IC base=+0.214)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` < `146.1332` → IC=+0.351 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 146.1332 (IC base=+0.335)

- **PATRÓN** `T_h` > `111.9928` → IC=+0.352 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9928 (IC base=+0.335)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: IBS > 0.7222 correlaciona con éxito en UPDOWN_GBM#15min (IC=+0.175 n=269). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#BTC#15min**: IBS > 0.6323 correlaciona con éxito en UPDOWN_GBM#BTC#15min (IC=+0.177 n=156). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#BTC#15min**: IBS < 0.0522 correlaciona con éxito en UPDOWN_GBM#BTC#15min (IC=+0.180 n=23). Confirma señal de reversión media → alinear con BUY_YES.
- **H-IBS-UPDOWN_GBM#ETH#15min**: IBS > 0.7622 correlaciona con éxito en UPDOWN_GBM#ETH#15min (IC=+0.198 n=94). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#XRP#15min**: IBS < 0.0669 correlaciona con éxito en UPDOWN_GBM#XRP#15min (IC=+0.167 n=37). Confirma señal de reversión media → alinear con BUY_YES.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ FAVORITO_CONFIRMADO | 2776 | +0.174 | -64.64€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#15min | 1789 | +0.206 | +1.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 118 | +0.025 | -15.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 395 | +0.097 | -63.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 474 | +0.151 | +13.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 803 | +0.179 | -11.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 596 | +0.201 | -19.19€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 39 | +0.037 | -4.75€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 158 | +0.163 | +15.73€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#ETH | 989 | +0.171 | -13.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 593 | +0.204 | +4.44€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 39 | -0.037 | -9.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 199 | +0.112 | -24.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 158 | +0.169 | +15.71€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL | 974 | +0.172 | -37.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 590 | +0.214 | +17.43€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 40 | +0.071 | -1.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 186 | +0.101 | -35.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 158 | +0.119 | -17.90€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 10 | +0.042 | -1.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 10 | +0.042 | -1.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 60 | +0.306 | +1.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 60 | +0.306 | +1.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 60 | +0.306 | +1.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 60 | +0.306 | +1.64€ | 0 | 0 |
| ✅ GBM_LATE_15M | 5062 | +0.102 | +1577.05€ | 0 | 4 |
| ✅ GBM_LATE_15M#15min | 5062 | +0.102 | +1577.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 1218 | +0.067 | +183.44€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1218 | +0.067 | +183.44€ | 0 | 4 |
| ✅ GBM_LATE_15M#ETH | 1201 | +0.074 | +198.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1201 | +0.074 | +198.67€ | 1 | 5 |
| ✅ GBM_LATE_15M#SOL | 1355 | +0.108 | +546.99€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1355 | +0.108 | +546.99€ | 1 | 7 |
| ✅ GBM_LATE_15M#XRP | 1288 | +0.154 | +647.95€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1288 | +0.154 | +647.95€ | 0 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 2270 | +0.150 | +1312.85€ | 0 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 2270 | +0.150 | +1312.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 583 | +0.110 | +284.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 583 | +0.110 | +284.29€ | 0 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 600 | +0.120 | +260.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 600 | +0.120 | +260.98€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 606 | +0.117 | +267.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 606 | +0.117 | +267.51€ | 1 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 481 | +0.274 | +500.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 481 | +0.274 | +500.08€ | 0 | 11 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 112 | +0.140 | +53.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 112 | +0.140 | +53.46€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC | 9 | -0.102 | -1.94€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 9 | -0.102 | -1.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 13 | +0.065 | +1.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 13 | +0.065 | +1.54€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL | 8 | -0.120 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 8 | -0.120 | -1.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 82 | +0.238 | +55.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 82 | +0.238 | +55.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 2250 | +0.094 | +700.32€ | 0 | 7 |
| ✅ GBM_LATE_15M_TARDIO#15min | 2250 | +0.094 | +700.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 561 | +0.063 | +106.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 561 | +0.063 | +106.47€ | 0 | 6 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 528 | +0.023 | +18.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 528 | +0.023 | +18.16€ | 0 | 3 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 515 | +0.067 | +108.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 515 | +0.067 | +108.46€ | 1 | 5 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 646 | +0.201 | +467.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 646 | +0.201 | +467.22€ | 0 | 10 |
| ✅ GBM_LATE_5M | 11 | -0.021 | -0.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#5min | 11 | -0.021 | -0.62€ | 0 | 0 |
| ✅ GBM_LATE_60M | 326 | -0.116 | +3.81€ | 4 | 1 |
| ✅ GBM_LATE_60M#60min | 326 | -0.116 | +3.81€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 114 | -0.035 | +5.51€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 114 | -0.035 | +5.51€ | 4 | 1 |
| ✅ GBM_LATE_60M#ETH | 102 | -0.164 | -12.97€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 102 | -0.164 | -12.97€ | 4 | 0 |
| ✅ GBM_LATE_60M#SOL | 110 | -0.152 | +11.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 110 | -0.152 | +11.27€ | 5 | 1 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO | 9 | -0.143 | -2.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO#60min | 9 | -0.143 | -2.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 46 | +0.229 | +22.79€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 46 | +0.229 | +22.79€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 46 | +0.229 | +22.79€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 46 | +0.229 | +22.79€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 153 | +0.068 | +20.69€ | 1 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 153 | +0.068 | +20.69€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 153 | +0.068 | +20.69€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 153 | +0.068 | +20.69€ | 1 | 2 |
| ✅ ORDER_FLOW_5M | 1617 | +0.012 | +13.02€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1481 | +0.008 | +0.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 198 | +0.045 | +6.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 198 | +0.045 | +6.48€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 2 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 216 | +0.000 | -2.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 216 | +0.000 | -2.12€ | 2 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 259 | -0.021 | -8.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 259 | -0.021 | -8.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 324 | +0.043 | +14.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 324 | +0.043 | +14.48€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#XRP | 193 | -0.003 | -4.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 193 | -0.003 | -4.19€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM | 148 | -0.167 | -3.76€ | 4 | 1 |
| 🚫 PRICE_TARGET_GBM#BTC | 62 | -0.250 | -18.09€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 56 | -0.276 | -17.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 6 | +0.000 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 56 | -0.172 | +0.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 51 | -0.198 | -3.02€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 5 | +0.018 | +3.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 30 | +0.031 | +13.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 28 | +0.033 | +13.27€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 135 | -0.186 | -7.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 13 | +0.022 | +3.34€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 10 | +0.208 | +4.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 10 | +0.208 | +4.00€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 206 | +0.101 | +31.61€ | 0 | 11 |
| ✅ STREAK_FADE_15M#15min | 206 | +0.101 | +31.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 44 | +0.087 | +1.24€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 44 | +0.087 | +1.24€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 72 | +0.189 | +32.87€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 72 | +0.189 | +32.87€ | 0 | 2 |
| ✅ STREAK_FADE_15M#XRP | 90 | +0.033 | -2.50€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 90 | +0.033 | -2.50€ | 2 | 2 |
| ✅ STREAK_FADE_5M | 246 | -0.048 | -24.96€ | 3 | 0 |
| ✅ STREAK_FADE_5M#5min | 246 | -0.048 | -24.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 47 | -0.153 | -8.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 47 | -0.153 | -8.07€ | 6 | 0 |
| ✅ STREAK_FADE_5M#SOL | 94 | -0.021 | -7.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 94 | -0.021 | -7.62€ | 2 | 1 |
| ✅ STREAK_FADE_5M#XRP | 105 | -0.023 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 105 | -0.023 | -9.27€ | 1 | 0 |
| 🚫 STREAK_MOM_5M | 315 | -0.058 | -25.36€ | 8 | 0 |
| ✅ STREAK_MOM_5M#5min | 315 | -0.058 | -25.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 106 | -0.056 | -6.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 106 | -0.056 | -6.82€ | 2 | 0 |
| ✅ STREAK_MOM_5M#SOL | 111 | -0.013 | -5.19€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 111 | -0.013 | -5.19€ | 2 | 2 |
| ✅ STREAK_MOM_5M#XRP | 98 | -0.110 | -13.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 98 | -0.110 | -13.35€ | 5 | 0 |
| 🚫 STRUCT_NO_15M | 15 | -0.199 | -4.68€ | 0 | 0 |
| 🚫 STRUCT_NO_15M#15min | 15 | -0.199 | -4.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ UPDOWN_GBM | 1627 | +0.009 | +69.97€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1368 | +0.035 | +107.51€ | 1 | 6 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 127 | -0.058 | -10.76€ | 7 | 0 |
| ✅ UPDOWN_GBM#BNB | 85 | +0.063 | +16.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 85 | +0.063 | +16.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 419 | +0.020 | +22.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 337 | +0.058 | +36.37€ | 1 | 7 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 42 | -0.068 | -6.16€ | 2 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 17 | -0.112 | +2.34€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 58 | +0.017 | -0.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 55 | +0.026 | +0.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 788 | +0.018 | +34.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 695 | +0.034 | +45.50€ | 2 | 4 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 54 | -0.018 | -2.56€ | 3 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 170 | -0.087 | -14.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 102 | -0.058 | -7.39€ | 7 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 31 | -0.106 | -2.03€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 105 | +0.014 | +12.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 94 | +0.042 | +15.75€ | 5 | 6 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 44 | -0.196 | +1.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 21 | +0.239 | +1.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 21 | +0.239 | +1.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 7 | +0.019 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 7 | +0.019 | -0.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 14 | +0.219 | +2.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 14 | +0.219 | +2.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 185 | +0.163 | +53.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 185 | +0.163 | +53.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 7 | -0.019 | +2.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 7 | -0.019 | +2.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 25 | +0.018 | +2.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 25 | +0.018 | +2.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 60 | +0.161 | +6.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 60 | +0.161 | +6.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 60 | +0.177 | +27.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 60 | +0.177 | +27.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 29 | +0.242 | +11.32€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 29 | +0.242 | +11.32€ | 0 | 0 |
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
| ✅ WEEKLY_PRICE | 273 | +0.136 | +29.85€ | 1 | 1 |
| ✅ WEEKLY_PRICE#BTC | 80 | +0.098 | -7.40€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 77 | +0.082 | -9.07€ | 0 | 2 |
| ✅ WEEKLY_PRICE#SOL | 116 | +0.195 | +46.33€ | 0 | 2 |