# Hipótesis automáticas — 2026-08-17 07:11 UTC
_Generado por shadow_postmortem.py sobre 47592 resoluciones (PNL=+5457.05€)_

## Patrones causales activos

### FAVORITO_CONFIRMADO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.183 (n=455)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 5.0 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.177 (n=388)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 15.0 (IC base=+0.166)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.183 (n=200)

  - _Acción_: Kelly boost +0.92€ cuando `py_entrada` < 0.575 (IC base=+0.166)

- **PATRÓN** `py_entrada` > `0.635` → IC=+0.173 (n=200)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` > 0.635 (IC base=+0.166)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.172 (n=516)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.02 (IC base=+0.166)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.178 (n=340)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 12.0 (IC base=+0.138)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.195 (n=346)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.405 (IC base=+0.138)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.150 (n=576)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.138)

- **PATRÓN** `libro_liquidez` > `4623.5751` → IC=+0.180 (n=317)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 4623.5751 (IC base=+0.138)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.178 (n=150)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.209 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.565` → IC=+0.206 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.565 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.635` → IC=+0.209 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.635 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `6984.5162` → IC=+0.184 (n=96)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 6984.5162 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.246 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.263 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.405 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `5976.8472` → IC=+0.183 (n=162)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 5976.8472 (IC base=+0.168)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.153 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 5.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.151 (n=130)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 15.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` < 0.575 (IC base=+0.134)

- **PATRÓN** `py_entrada` > `0.575` → IC=+0.149 (n=149)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` > 0.575 (IC base=+0.134)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=149)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.134)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.140 (n=84)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 15.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 8.0 (IC base=+0.136)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.158 (n=118)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.405 (IC base=+0.136)

- **PATRÓN** `libro_liquidez` > `4151.9377` → IC=+0.180 (n=145)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 4151.9377 (IC base=+0.136)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.200 (n=148)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` < `0.64` → IC=+0.201 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.64 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.605` → IC=+0.186 (n=100)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.605 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.197 (n=140)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.02 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.124 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 12.0 (IC base=+0.107)

- **PATRÓN** `py_entrada` < `0.345` → IC=+0.254 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.345 (IC base=+0.107)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.152 (n=156)

  - _Acción_: Kelly boost +0.76€ cuando `libro_spread` < 0.02 (IC base=+0.107)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA
- **PATRÓN** `py_entrada` < `0.36` → IC=+0.214 (n=376)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.36 (IC base=+0.139)

- **PATRÓN** `restante_min` < `3.66` → IC=+0.169 (n=364)

  - _Acción_: Kelly boost +0.85€ cuando `restante_min` < 3.66 (IC base=+0.139)

- **PATRÓN** `restante_min` > `4.9` → IC=+0.183 (n=374)

  - _Acción_: Kelly boost +0.92€ cuando `restante_min` > 4.9 (IC base=+0.139)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.145 (n=1160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 4.0 (IC base=+0.139)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.143 (n=1120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 17.0 (IC base=+0.139)

- **PATRÓN** `lag_apertura_s` < `5.88` → IC=+0.188 (n=363)

  - _Acción_: Kelly boost +0.94€ cuando `lag_apertura_s` < 5.88 (IC base=+0.139)

- **PATRÓN** `profundidad_ratio_no` > `8.7` → IC=+0.144 (n=366)

  - _Acción_: Kelly boost +0.72€ cuando `profundidad_ratio_no` > 8.7 (IC base=+0.139)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.228 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.146)

- **PATRÓN** `restante_min` < `3.56` → IC=+0.189 (n=181)

  - _Acción_: Kelly boost +0.94€ cuando `restante_min` < 3.56 (IC base=+0.146)

- **PATRÓN** `restante_min` > `4.87` → IC=+0.190 (n=188)

  - _Acción_: Kelly boost +0.95€ cuando `restante_min` > 4.87 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.152 (n=579)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 4.0 (IC base=+0.146)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.154 (n=495)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 15.0 (IC base=+0.146)

- **PATRÓN** `lag_apertura_s` < `7.63` → IC=+0.194 (n=181)

  - _Acción_: Kelly boost +0.97€ cuando `lag_apertura_s` < 7.63 (IC base=+0.146)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.194 (n=246)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.38 (IC base=+0.132)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.204 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.95 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.138 (n=581)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 4.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.135 (n=565)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 17.0 (IC base=+0.132)

- **PATRÓN** `lag_apertura_s` < `3.17` → IC=+0.206 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 3.17 (IC base=+0.132)

- **PATRÓN** `profundidad_ratio_no` > `16.2` → IC=+0.190 (n=182)

  - _Acción_: Kelly boost +0.95€ cuando `profundidad_ratio_no` > 16.2 (IC base=+0.132)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` < `0.006` → IC=+0.286 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.006 (IC base=+0.292)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.338 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0048 (IC base=+0.292)

- **PATRÓN** `drift_60min` |x|≤ `0.1064` → IC=+0.342 (n=17)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1064 (IC base=+0.292)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.300 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.292)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.342 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.292)

- **PATRÓN** `ibs_20min` > `0.5959` → IC=+0.392 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.5959 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.705` → IC=+0.289 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.705 (IC base=+0.292)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.034` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.034 (IC base=+0.292)

- **PATRÓN** `libro_spread` < `0.03` → IC=+0.316 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.03 (IC base=+0.292)

- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.225 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0053 (IC base=+0.194)

- **PATRÓN** `drift_60min` |x|≤ `0.2495` → IC=+0.205 (n=103)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2495 (IC base=+0.194)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.252 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.194)

- **PATRÓN** `ibs_20min` < `0.2969` → IC=+0.252 (n=103)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2969 (IC base=+0.194)

- **PATRÓN** `dist_vwap_pct` > `0.1236` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1236 (IC base=+0.194)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.799` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.799 (IC base=+0.194)

- **PATRÓN** `volumen_regimen` < `0.911` → IC=+0.219 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.911 (IC base=+0.194)

### GBM_LATE_15M_ESPACIO_ATR#DOGE#15min
- **PATRÓN** `libro_spread` < `0.01` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.300)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **FILTRO** `sigma_ewma_delta_pct` < `6.713` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 6.713
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `volumen_regimen` > `0.8338` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.8338
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.367 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.307)

- **PATRÓN** `drift_60min` |x|≤ `0.2313` → IC=+0.333 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2313 (IC base=+0.307)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.309 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.307)

- **PATRÓN** `ibs_20min` < `0.2468` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2468 (IC base=+0.307)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.001` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.001 (IC base=+0.307)

- **PATRÓN** `volumen_regimen` < `1.2726` → IC=+0.321 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.2726 (IC base=+0.307)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.291 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.246)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.292 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.246)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.263 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.246)

- **PATRÓN** `ibs_20min` > `0.9014` → IC=+0.291 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9014 (IC base=+0.246)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.464` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.464 (IC base=+0.246)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.195 (n=103)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.005 (IC base=+0.184)

- **PATRÓN** `sigma_h` > `0.0035` → IC=+0.190 (n=153)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0035 (IC base=+0.184)

- **PATRÓN** `drift_60min` |x|≤ `0.2957` → IC=+0.205 (n=154)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2957 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.300 (n=63)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.184)

- **PATRÓN** `ibs_20min` < `0.4017` → IC=+0.269 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.4017 (IC base=+0.184)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.654` → IC=+0.227 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.654 (IC base=+0.184)

- **PATRÓN** `volumen_regimen` < `0.618` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.618 (IC base=+0.184)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.260 (n=23)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.266)

- **PATRÓN** `drift_60min` |x|≤ `0.1354` → IC=+0.324 (n=15)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1354 (IC base=+0.266)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.309 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.266)

- **PATRÓN** `ibs_20min` < `0.0652` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.0652 (IC base=+0.266)

- **PATRÓN** `ibs_20min` > `0.1979` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.1979 (IC base=+0.266)

- **PATRÓN** `volumen_regimen` < `1.295` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 1.295 (IC base=+0.266)

- **PATRÓN** `volumen_regimen` > `1.0417` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.0417 (IC base=+0.266)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.263 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.196 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 6.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.211 (n=50)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.185)

- **PATRÓN** `ibs_20min` > `0.4819` → IC=+0.304 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.4819 (IC base=+0.185)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.983` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.983 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.156 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0044 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0851` → IC=+0.172 (n=62)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.0851 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.189 (n=181)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 4.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.149 (n=186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 14.0 (IC base=+0.148)

- **PATRÓN** `ibs_20min` < `0.5556` → IC=+0.220 (n=184)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.5556 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.048` → IC=+0.222 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.048 (IC base=+0.148)

- **PATRÓN** `volumen_regimen` > `1.313` → IC=+0.159 (n=42)

  - _Acción_: Kelly boost +0.80€ cuando `volumen_regimen` > 1.313 (IC base=+0.148)

### GBM_LATE_15M_TARDIO#DOGE#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.370 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 7.0 (IC base=+0.295)

- **PATRÓN** `ibs_20min` > `0.3333` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.3333 (IC base=+0.295)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.295)

### GBM_LATE_15M_TARDIO#ETH#15min
- **FILTRO** `sigma_h` > `0.0029` → IC=-0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0029
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `volumen_regimen` > `0.7424` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `volumen_regimen` > 0.7424
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `ibs_20min` > `0.2571` → IC=-0.167 (n=34)

  - _Acción_: SKIP cuando `ibs_20min` > 0.2571
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=18)

- **PATRÓN** `ibs_20min` < `0.2571` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.2571 (IC base=-0.037)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0051 (IC base=+0.210)

- **PATRÓN** `drift_60min` |x|≤ `0.1353` → IC=+0.260 (n=23)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1353 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.265 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.3438` → IC=+0.266 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3438 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6417 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `1.3794` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.3794 (IC base=+0.210)

### GBM_LATE_5M
- **FILTRO** `sigma_h` < `0.0037` → IC=-0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=31)

- **FILTRO** `drift_60min` |x|> `0.0797` → IC=-0.156 (n=30)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0797
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=16)

- **FILTRO** `volumen_spike_ratio` > `2.6327` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `volumen_spike_ratio` > 2.6327
  - _Potencial_: sin este filtro IC_bueno=+0.114 (n=55)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.086 (n=68)

### GBM_LATE_60M
- **FILTRO** `ibs_20min` < `1.0` → IC=-0.167 (n=67)

  - _Acción_: SKIP cuando `ibs_20min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.300 (n=43)

- **FILTRO** `sigma_h` > `0.011` → IC=-0.289 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.011
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=108)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.260 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.043 (n=44)

- **FILTRO** `volumen_regimen` < `0.5959` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `volumen_regimen` < 0.5959
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=46)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.009)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.949` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.949 (IC base=+0.009)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `ibs_20min` < `0.8379` → IC=-0.231 (n=24)

  - _Acción_: SKIP cuando `ibs_20min` < 0.8379
  - _Potencial_: sin este filtro IC_bueno=+0.231 (n=24)

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.179 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

- **PATRÓN** `ibs_20min` > `0.8379` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.8379 (IC base=+0.028)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` < `5.134` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 5.134
  - _Potencial_: sin este filtro IC_bueno=+0.267 (n=28)

- **FILTRO** `sigma_h` > `0.0084` → IC=-0.333 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=32)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.333 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=14)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 1.0 (IC base=+0.028)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.134` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.134 (IC base=+0.028)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.129 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

- **FILTRO** `sigma_h` > `0.0103` → IC=-0.271 (n=46)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0103
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.261 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=-0.054)

### GBM_LATE_60M_FADE
- **FILTRO** `drift_60min` |x|> `0.1319` → IC=-0.403 (n=29)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1319
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=30)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.423 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=24)

- **FILTRO** `ibs_20min` > `0.8144` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `ibs_20min` > 0.8144
  - _Potencial_: sin este filtro IC_bueno=-0.186 (n=33)

- **FILTRO** `dist_vwap_pct` > `0.3507` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3507
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=47)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=43)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` < `8.459` → IC=-0.450 (n=18)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 8.459
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=3)

- **FILTRO** `sigma_h` > `0.0022` → IC=-0.342 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0022
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_ewma_delta_pct` < `1.863` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 1.863
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=3)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `ibs_20min` > `0.5789` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `ibs_20min` > 0.5789
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=58)

- **PATRÓN** `volumen_regimen` < `0.8637` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `volumen_regimen` < 0.8637 (IC base=+0.033)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `2.924` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 2.924 (IC base=+0.083)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `sigma_h` > `0.0051` → IC=-0.152 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` > `17.0` → IC=-0.333 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=84)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=84)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=84)

- **FILTRO** `libro_liquidez` < `1970.6128` → IC=-0.389 (n=25)

  - _Acción_: SKIP cuando `libro_liquidez` < 1970.6128
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=75)

- **FILTRO** `hora_utc` < `12.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 12.0
  - _Potencial_: sin este filtro IC_bueno=-0.054 (n=72)

- **FILTRO** `py_entrada` > `0.5` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.059 (n=82)

### LIQUIDACIONES_15M#BTC#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

### LIQUIDACIONES_15M#XRP#15min
- **FILTRO** `hora_utc` > `10.0` → IC=-0.309 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 10.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_5M
- **FILTRO** `py_entrada` < `0.505` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `libro_liquidez` < `6033.6058` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 6033.6058
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9664` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9664
  - _Potencial_: sin este filtro IC_bueno=+0.107 (n=59)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=53)

### LIQUIDACIONES_60M#BTC#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.149 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 12.0 (IC base=-0.007)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.4028` → IC=+0.151 (n=104)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.75€ cuando `delta_ratio` |x|> 0.4028 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.143)

- **PATRÓN** `total_vol_5m` < `1208.765` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 1208.765 (IC base=+0.143)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.2125` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.2125
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=38)

- **FILTRO** `pct_vs_K` |x|> `3.4276` → IC=-0.456 (n=43)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4276
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=45)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `1.4189` → IC=-0.464 (n=26)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.4189
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0037` → IC=-0.444 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=34)

- **FILTRO** `T_h` > `143.1632` → IC=-0.460 (n=23)

  - _Acción_: SKIP cuando `T_h` > 143.1632
  - _Potencial_: sin este filtro IC_bueno=-0.121 (n=27)

- **FILTRO** `sigma_h` > `0.0035` → IC=-0.325 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=14)

- **FILTRO** `T_h` < `111.9668` → IC=-0.447 (n=17)

  - _Acción_: SKIP cuando `T_h` < 111.9668
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=35)

### STREAK_FADE_5M
- **FILTRO** `libro_liquidez` < `3472.3984` → IC=-0.174 (n=41)

  - _Acción_: SKIP cuando `libro_liquidez` < 3472.3984
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=86)

- **FILTRO** `hora_utc` > `14.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=65)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.057 (n=68)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=-0.005)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=18)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### STREAK_MOM_5M
- **FILTRO** `hora_utc` < `6.0` → IC=-0.149 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=86)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.136 (n=86)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 6.0 (IC base=+0.053)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.024 (n=19)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.283 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` > `0.5` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` > 0.5 (IC base=+0.125)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=43)

- **PATRÓN** `streak_len` < `3.0` → IC=+0.122 (n=43)

  - _Acción_: Kelly boost +0.61€ cuando `streak_len` < 3.0 (IC base=+0.050)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.015 (n=602)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=319)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=327)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.154 (n=128)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0053 (IC base=+0.105)

### UPDOWN_GBM#5min
- **FILTRO** `sigma_h` > `0.0058` → IC=-0.138 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0058
  - _Potencial_: sin este filtro IC_bueno=+0.021 (n=138)

### UPDOWN_GBM#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=27)

- **FILTRO** `ibs_15` < `0.5186` → IC=-0.204 (n=25)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5186
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0016` → IC=-0.200 (n=28)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0016
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=29)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` > `0.0019` → IC=+0.134 (n=69)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0019 (IC base=+0.118)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` < `0.0035` → IC=-0.227 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.152 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0032 (IC base=+0.131)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.149 (n=55)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0036 (IC base=+0.131)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `sigma_h` < `0.0027` → IC=-0.167 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0027
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=19)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `sigma_h` > `0.0046` → IC=-0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.167 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.005 (IC base=+0.088)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.214 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.104)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.21` → IC=+0.247 (n=73)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.21 (IC base=+0.237)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.264 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.237)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.257 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0029 (IC base=+0.237)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.21` → IC=+0.231 (n=50)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.21 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.245 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.202)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` < `0.0041` → IC=-0.167 (n=226)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0041
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=701)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` < `0.0036` → IC=-0.201 (n=162)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0036
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=55)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.324 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.214)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **FILTRO** `sigma_h` < `0.0053` → IC=-0.129 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=60)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.246 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.244)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.278 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.244)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.2` → IC=+0.233 (n=58)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.2 (IC base=+0.222)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.230 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.222)

- **PATRÓN** `sigma_h` > `0.0023` → IC=+0.233 (n=43)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0023 (IC base=+0.222)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.324 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0036 (IC base=+0.273)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.047` → IC=-0.180 (n=23)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.047
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **FILTRO** `sigma_h` > `0.0028` → IC=-0.196 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0028
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `drift_60min` |x|> `0.1471` → IC=-0.206 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1471
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1237` → IC=-0.161 (n=57)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1237
  - _Potencial_: sin este filtro IC_bueno=-0.047 (n=179)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0931` → IC=-0.278 (n=16)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0931
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `sigma_h` > `0.0045` → IC=-0.289 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0045
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `146.1359` → IC=+0.462 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1359 (IC base=+0.352)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `111.9965` → IC=+0.300 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9965 (IC base=+0.264)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.264)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9969` → IC=+0.327 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9969 (IC base=+0.301)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `135.992` → IC=+0.455 (n=200)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 135.992 (IC base=+0.433)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min` — IC=+0.294 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH` — IC=+0.294 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min` — IC=+0.414 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL` — IC=+0.414 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM#BNB#15min` — IC=+0.156 n=30. Faltan ~10 resoluciones para umbral n≥40. ETA: ~7h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM#BNB` — IC=+0.105 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 454 | +0.031 | +21.45€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 454 | +0.031 | +21.45€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 252 | +0.043 | +24.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 252 | +0.043 | +24.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 188 | +0.005 | -5.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 188 | +0.005 | -5.05€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 14 | +0.087 | +1.55€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 14 | +0.087 | +1.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 2413 | -0.126 | -383.48€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 382 | +0.023 | -16.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 2031 | -0.154 | -367.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 286 | -0.153 | -80.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 286 | -0.153 | -80.39€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 382 | +0.023 | -16.17€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 382 | +0.023 | -16.17€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#DOGE | 230 | -0.272 | -155.50€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#DOGE#5min | 230 | -0.272 | -155.50€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 483 | -0.151 | -0.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 483 | -0.151 | -0.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 585 | -0.071 | -93.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 585 | -0.071 | -93.45€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP | 447 | -0.202 | -37.45€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP#5min | 447 | -0.202 | -37.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 11257 | +0.119 | -594.59€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#15min | 2953 | +0.180 | -104.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 89 | -0.104 | -43.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 5714 | +0.086 | -460.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2501 | +0.130 | +13.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 968 | +0.038 | -204.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 12 | -0.043 | -1.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 952 | +0.042 | -196.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 2696 | +0.142 | +7.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 808 | +0.189 | -43.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 35 | -0.095 | -17.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 952 | +0.114 | +6.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 901 | +0.138 | +61.09€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 962 | +0.055 | -162.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 8 | -0.040 | -4.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 954 | +0.057 | -158.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 2913 | +0.126 | -46.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1090 | +0.161 | -20.93€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 953 | +0.099 | -18.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 858 | +0.116 | +1.04€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#SOL | 2755 | +0.140 | -170.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1024 | +0.200 | -37.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 37 | -0.013 | -10.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 952 | +0.082 | -74.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 742 | +0.137 | -48.86€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 963 | +0.124 | -17.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 11 | +0.064 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 951 | +0.124 | -19.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3049 | +0.170 | -250.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 3049 | +0.170 | -250.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 768 | +0.166 | -86.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 768 | +0.166 | -86.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 59 | -0.025 | -2.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 59 | -0.025 | -2.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 753 | +0.166 | -86.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 753 | +0.166 | -86.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 676 | +0.229 | -26.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 676 | +0.229 | -26.45€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 714 | +0.180 | -62.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 714 | +0.180 | -62.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 145 | +0.405 | -10.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 145 | +0.405 | -10.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 54 | +0.411 | -2.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 54 | +0.411 | -2.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 56 | +0.362 | -8.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 56 | +0.362 | -8.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 33 | +0.414 | -0.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 33 | +0.414 | -0.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 4193 | +0.192 | -375.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 4193 | +0.192 | -375.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 793 | +0.098 | -178.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 793 | +0.098 | -178.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 638 | +0.247 | -6.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 638 | +0.247 | -6.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 748 | +0.143 | -119.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 748 | +0.143 | -119.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 680 | +0.232 | -18.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 680 | +0.232 | -18.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 647 | +0.250 | -3.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 647 | +0.250 | -3.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 687 | +0.207 | -48.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 687 | +0.207 | -48.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1449 | +0.139 | +45.89€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 1449 | +0.139 | +45.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 721 | +0.146 | +32.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 721 | +0.146 | +32.43€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 728 | +0.132 | +13.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 728 | +0.132 | +13.45€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 503 | +0.294 | -0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 503 | +0.294 | -0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 211 | +0.265 | -11.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 211 | +0.265 | -11.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 235 | +0.297 | +5.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 235 | +0.297 | +5.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 57 | +0.364 | +5.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 57 | +0.364 | +5.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 208 | +0.405 | -11.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 208 | +0.405 | -11.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 94 | +0.396 | -6.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 94 | +0.396 | -6.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 91 | +0.414 | -4.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 91 | +0.414 | -4.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 23 | +0.340 | +0.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 23 | +0.340 | +0.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 218 | +0.259 | -23.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 218 | +0.259 | -23.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 218 | +0.259 | -23.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 218 | +0.259 | -23.93€ | 0 | 0 |
| ✅ GBM_LATE_15M | 3852 | +0.087 | +1290.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#15min | 3852 | +0.087 | +1290.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 663 | +0.177 | +418.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 663 | +0.177 | +418.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 336 | +0.157 | +130.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 336 | +0.157 | +130.88€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE | 657 | +0.198 | +467.92€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 657 | +0.198 | +467.92€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH | 526 | +0.002 | +9.62€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 526 | +0.002 | +9.62€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL | 762 | +0.004 | +57.28€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 762 | +0.004 | +57.28€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP | 908 | +0.032 | +207.04€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 908 | +0.032 | +207.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 4802 | +0.053 | +1443.52€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 4802 | +0.053 | +1443.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 933 | -0.013 | +219.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 933 | -0.013 | +219.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 913 | -0.002 | +109.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 913 | -0.002 | +109.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 570 | +0.238 | +515.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 570 | +0.238 | +515.84€ | 0 | 1 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 833 | -0.010 | +16.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 833 | -0.010 | +16.07€ | 2 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 869 | +0.004 | +61.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 869 | +0.004 | +61.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 684 | +0.201 | +520.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 684 | +0.201 | +520.95€ | 0 | 6 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 2718 | +0.173 | +1784.17€ | 0 | 12 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 2718 | +0.173 | +1784.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 494 | +0.198 | +368.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 494 | +0.198 | +368.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 347 | +0.188 | +202.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 347 | +0.188 | +202.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 479 | +0.205 | +377.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 479 | +0.205 | +377.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 322 | +0.216 | +231.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 322 | +0.216 | +231.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 522 | +0.063 | +182.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 522 | +0.063 | +182.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 554 | +0.192 | +422.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 554 | +0.192 | +422.06€ | 0 | 7 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 498 | +0.040 | +29.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 498 | +0.040 | +29.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 76 | +0.026 | -7.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 76 | +0.026 | -7.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 109 | +0.167 | +44.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 109 | +0.167 | +44.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 216 | -0.009 | -2.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 216 | -0.009 | -2.28€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 97 | +0.015 | -5.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 97 | +0.015 | -5.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 3191 | +0.165 | +2012.83€ | 0 | 12 |
| ✅ GBM_LATE_15M_TARDIO#15min | 3191 | +0.165 | +2012.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 638 | +0.186 | +443.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 638 | +0.186 | +443.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 402 | +0.141 | +199.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 402 | +0.141 | +199.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 632 | +0.227 | +546.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 632 | +0.227 | +546.25€ | 0 | 3 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 259 | +0.105 | +90.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 259 | +0.105 | +90.97€ | 2 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 543 | +0.063 | +180.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 543 | +0.063 | +180.94€ | 1 | 1 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 717 | +0.201 | +551.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 717 | +0.201 | +551.98€ | 0 | 6 |
| ✅ GBM_LATE_5M | 129 | +0.004 | -3.03€ | 4 | 0 |
| ✅ GBM_LATE_5M#5min | 129 | +0.004 | -3.03€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 56 | +0.000 | -4.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 56 | +0.000 | -4.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 26 | +0.071 | +1.30€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 26 | +0.071 | +1.30€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL | 40 | -0.071 | -0.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 40 | -0.071 | -0.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 7 | +0.058 | +0.44€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 7 | +0.058 | +0.44€ | 0 | 0 |
| ✅ GBM_LATE_60M | 477 | -0.051 | +56.03€ | 4 | 2 |
| ✅ GBM_LATE_60M#60min | 477 | -0.051 | +56.03€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 166 | -0.006 | +6.00€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 166 | -0.006 | +6.00€ | 3 | 1 |
| ✅ GBM_LATE_60M#ETH | 170 | -0.035 | +32.45€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 170 | -0.035 | +32.45€ | 3 | 2 |
| ✅ GBM_LATE_60M#SOL | 141 | -0.122 | +17.57€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 141 | -0.122 | +17.57€ | 3 | 1 |
| 🚫 GBM_LATE_60M_FADE | 189 | -0.301 | -32.44€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 189 | -0.301 | -32.44€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 75 | -0.253 | -6.85€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 75 | -0.253 | -6.85€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 64 | -0.348 | -18.54€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 64 | -0.348 | -18.54€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 50 | -0.288 | -7.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 50 | -0.288 | -7.05€ | 1 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 285 | +0.054 | +9.64€ | 1 | 1 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 285 | +0.054 | +9.64€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 107 | +0.014 | +6.06€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 107 | +0.014 | +6.06€ | 0 | 1 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 63 | +0.146 | +6.38€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 63 | +0.146 | +6.38€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 115 | +0.038 | -2.80€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 115 | +0.038 | -2.80€ | 1 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 27 | +0.121 | +4.90€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 27 | +0.121 | +4.90€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 27 | +0.121 | +4.90€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 27 | +0.121 | +4.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M | 202 | -0.113 | -29.52€ | 6 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 202 | -0.113 | -29.52€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 48 | -0.120 | -8.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 48 | -0.120 | -8.11€ | 1 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 22 | -0.208 | -5.32€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 22 | -0.208 | -5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 42 | -0.023 | -2.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 42 | -0.023 | -2.84€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 39 | -0.037 | -2.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 39 | -0.037 | -2.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 46 | -0.167 | -8.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 46 | -0.167 | -8.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 58 | -0.150 | -9.72€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 58 | -0.150 | -9.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 13 | -0.065 | -1.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 13 | -0.065 | -1.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 10 | -0.042 | -1.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 10 | -0.042 | -1.11€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL | 13 | -0.152 | -3.62€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL#5min | 13 | -0.152 | -3.62€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 13 | -0.108 | -2.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 13 | -0.108 | -2.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M | 276 | +0.018 | +0.08€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 276 | +0.018 | +0.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 93 | -0.005 | -6.17€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 93 | -0.005 | -6.17€ | 0 | 1 |
| ✅ LIQUIDACIONES_60M#ETH | 88 | +0.022 | +1.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 88 | +0.022 | +1.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 95 | +0.036 | +4.40€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 95 | +0.036 | +4.40€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 176 | +0.073 | +23.07€ | 1 | 3 |
| ✅ ORDER_FLOW_5M#5min | 40 | +0.119 | +10.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 5 | +0.089 | +7.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 5 | +0.089 | +7.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 7 | -0.019 | -0.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 7 | -0.019 | -0.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 15 | +0.066 | +1.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 15 | +0.066 | +1.31€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 11 | +0.021 | -0.26€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 11 | +0.021 | -0.26€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 212 | -0.126 | -4.87€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 85 | -0.167 | -17.67€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 72 | -0.176 | -14.71€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 13 | -0.065 | -2.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 85 | -0.132 | -1.41€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 70 | -0.139 | -2.64€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 15 | -0.066 | +1.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 42 | -0.023 | +14.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 37 | +0.013 | +15.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 5 | -0.054 | -1.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 179 | -0.124 | -1.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 33 | -0.129 | -2.99€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 102 | -0.279 | -24.06€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 42 | -0.204 | -6.05€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 40 | -0.191 | -5.03€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 46 | -0.271 | -10.87€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 44 | -0.261 | -9.85€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 14 | -0.306 | -7.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 13 | -0.282 | -6.63€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 97 | -0.268 | -21.51€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 5 | -0.089 | -2.55€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 45 | +0.287 | +6.28€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 14 | +0.044 | -1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 14 | +0.044 | -1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 16 | +0.356 | +6.43€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 16 | +0.356 | +6.43€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 45 | +0.287 | +6.28€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 22 | -0.083 | -8.24€ | 0 | 0 |
| ✅ STREAK_FADE_15M#15min | 22 | -0.083 | -8.24€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 10 | +0.000 | -3.01€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 10 | +0.000 | -3.01€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 11 | -0.064 | -4.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 11 | -0.064 | -4.09€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 222 | -0.027 | -17.37€ | 3 | 1 |
| ✅ STREAK_FADE_5M#5min | 222 | -0.027 | -17.37€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 41 | +0.012 | +0.55€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 41 | +0.012 | +0.55€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 85 | -0.006 | -6.69€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 85 | -0.006 | -6.69€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 47 | -0.112 | -8.66€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 47 | -0.112 | -8.66€ | 1 | 0 |
| ✅ STREAK_FADE_5M#XRP | 49 | -0.010 | -2.58€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 49 | -0.010 | -2.58€ | 0 | 0 |
| ✅ STREAK_FADE_60M | 14 | -0.087 | -2.15€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 14 | -0.087 | -2.15€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 8 | -0.080 | -2.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 8 | -0.080 | -2.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 348 | +0.031 | +8.02€ | 1 | 1 |
| ✅ STREAK_MOM_5M#5min | 348 | +0.031 | +8.02€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 104 | +0.028 | +1.93€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 104 | +0.028 | +1.93€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 73 | +0.020 | +4.97€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 73 | +0.020 | +4.97€ | 1 | 2 |
| ✅ STREAK_MOM_5M#SOL | 83 | +0.053 | +1.46€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 83 | +0.053 | +1.46€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP | 88 | +0.022 | -0.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 88 | +0.022 | -0.34€ | 1 | 1 |
| ✅ STRUCT_NO_15M | 1626 | +0.007 | -18.17€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 1626 | +0.007 | -18.17€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 621 | +0.009 | -6.22€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 621 | +0.009 | -6.22€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 654 | +0.003 | -9.75€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 654 | +0.003 | -9.75€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 351 | +0.010 | -2.20€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 351 | +0.010 | -2.20€ | 2 | 0 |
| ✅ UPDOWN_GBM | 1421 | +0.011 | +45.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 633 | +0.086 | +94.61€ | 0 | 1 |
| ✅ UPDOWN_GBM#240min | 97 | -0.005 | -2.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 412 | -0.058 | -38.08€ | 1 | 0 |
| ✅ UPDOWN_GBM#60min | 232 | -0.017 | -7.32€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 36 | +0.105 | +11.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 30 | +0.156 | +12.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 269 | -0.005 | -10.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 108 | +0.064 | -3.31€ | 0 | 1 |
| ✅ UPDOWN_GBM#BTC#240min | 27 | +0.017 | +0.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 37 | -0.038 | -1.38€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 79 | -0.056 | -8.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 159 | -0.047 | -15.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 20 | +0.000 | -0.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 139 | -0.053 | -15.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 348 | +0.046 | +22.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 161 | +0.126 | +27.59€ | 0 | 2 |
| ✅ UPDOWN_GBM#ETH#240min | 29 | +0.048 | +0.01€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 52 | -0.056 | -3.46€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 91 | +0.005 | -1.02€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 267 | -0.020 | -2.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 98 | +0.010 | +0.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#240min | 25 | -0.018 | -0.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 70 | -0.042 | -3.22€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 62 | +0.000 | +1.83€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 340 | +0.032 | +41.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 216 | +0.096 | +57.92€ | 0 | 2 |
| ✅ UPDOWN_GBM#XRP#240min | 15 | -0.110 | -2.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 109 | -0.068 | -13.26€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 97 | +0.237 | -4.05€ | 0 | 3 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 97 | +0.237 | -4.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 65 | +0.202 | -10.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 65 | +0.202 | -10.53€ | 0 | 2 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 32 | +0.294 | +6.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 32 | +0.294 | +6.49€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1313 | -0.040 | +91.00€ | 1 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1313 | -0.040 | +91.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 62 | +0.000 | +11.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 62 | +0.000 | +11.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 276 | -0.137 | -35.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 276 | -0.137 | -35.84€ | 1 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 20 | -0.045 | -1.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 20 | -0.045 | -1.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 108 | +0.027 | +21.54€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 108 | +0.027 | +21.54€ | 0 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 424 | +0.000 | +74.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 424 | +0.000 | +74.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 423 | -0.039 | +21.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 423 | -0.039 | +21.07€ | 1 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 119 | +0.244 | +48.39€ | 0 | 2 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 119 | +0.244 | +48.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 77 | +0.222 | +21.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 77 | +0.222 | +21.92€ | 0 | 3 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 42 | +0.273 | +26.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 42 | +0.273 | +26.47€ | 0 | 1 |
| ✅ UPDOWN_OU_5M | 268 | -0.078 | -26.21€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 268 | -0.078 | -26.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 165 | -0.027 | -13.48€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 165 | -0.027 | -13.48€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 13 | -0.022 | +1.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 13 | -0.022 | +1.64€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 13 | -0.108 | -2.55€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 13 | -0.108 | -2.55€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 27 | -0.155 | -3.91€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 27 | -0.155 | -3.91€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 28 | -0.200 | -4.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 28 | -0.200 | -4.70€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 22 | -0.125 | -3.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 22 | -0.125 | -3.21€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 884 | +0.284 | +379.36€ | 0 | 1 |
| ✅ WEEKLY_PRICE#BTC | 265 | +0.200 | +11.50€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 277 | +0.253 | +65.00€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 342 | +0.372 | +302.86€ | 0 | 1 |