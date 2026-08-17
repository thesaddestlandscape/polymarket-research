# Hipótesis automáticas — 2026-08-17 18:38 UTC
_Generado por shadow_postmortem.py sobre 52528 resoluciones (PNL=+5821.50€)_

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

- **PATRÓN** `py_entrada` > `0.42` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` > 0.42 (IC base=+0.136)

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
- **PATRÓN** `py_entrada` < `0.36` → IC=+0.221 (n=421)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.36 (IC base=+0.149)

- **PATRÓN** `restante_min` < `3.73` → IC=+0.169 (n=418)

  - _Acción_: Kelly boost +0.85€ cuando `restante_min` < 3.73 (IC base=+0.149)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.197 (n=433)

  - _Acción_: Kelly boost +0.98€ cuando `restante_min` > 4.91 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.159 (n=1299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.155 (n=1330)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 17.0 (IC base=+0.149)

- **PATRÓN** `lag_apertura_s` < `5.37` → IC=+0.202 (n=417)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 5.37 (IC base=+0.149)

- **PATRÓN** `profundidad_ratio_no` > `9.1` → IC=+0.149 (n=417)

  - _Acción_: Kelly boost +0.75€ cuando `profundidad_ratio_no` > 9.1 (IC base=+0.149)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.235 (n=236)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.151)

- **PATRÓN** `restante_min` < `3.65` → IC=+0.187 (n=209)

  - _Acción_: Kelly boost +0.94€ cuando `restante_min` < 3.65 (IC base=+0.151)

- **PATRÓN** `restante_min` > `4.88` → IC=+0.195 (n=211)

  - _Acción_: Kelly boost +0.97€ cuando `restante_min` > 4.88 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.161 (n=650)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.164 (n=579)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 15.0 (IC base=+0.151)

- **PATRÓN** `lag_apertura_s` < `7.47` → IC=+0.195 (n=211)

  - _Acción_: Kelly boost +0.97€ cuando `lag_apertura_s` < 7.47 (IC base=+0.151)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.38` → IC=+0.208 (n=293)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.38 (IC base=+0.147)

- **PATRÓN** `restante_min` < `3.81` → IC=+0.151 (n=210)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` < 3.81 (IC base=+0.147)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.211 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.95 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.160 (n=574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 7.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.157 (n=630)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 16.0 (IC base=+0.147)

- **PATRÓN** `lag_apertura_s` < `3.14` → IC=+0.209 (n=211)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 3.14 (IC base=+0.147)

- **PATRÓN** `profundidad_ratio_no` > `16.1` → IC=+0.197 (n=209)

  - _Acción_: Kelly boost +0.98€ cuando `profundidad_ratio_no` > 16.1 (IC base=+0.147)

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
- **FILTRO** `hora_utc` > `5.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=32)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=89)

- **PATRÓN** `drift_60min` |x|≤ `0.0648` → IC=+0.155 (n=27)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.78€ cuando `drift_60min` |x|≤ 0.0648 (IC base=+0.038)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `libro_liquidez` < `6033.6058` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `libro_liquidez` < 6033.6058
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=17)

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9664` → IC=-0.214 (n=19)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9664
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=60)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=54)

### LIQUIDACIONES_60M#BTC#60min
- **PATRÓN** `hora_utc` < `7.0` → IC=+0.154 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 7.0 (IC base=+0.000)

### MOMENTUM_IBS_15M
- **PATRÓN** `hora_utc` < `14.0` → IC=+0.159 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 14.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.5 (IC base=+0.151)

- **PATRÓN** `drift_20min_pct` |x|≤ `0.2002` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `drift_20min_pct` |x|≤ 0.2002 (IC base=+0.151)

- **PATRÓN** `ibs_20min` > `0.9048` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` > 0.9048 (IC base=+0.151)

- **PATRÓN** `libro_liquidez` > `2343.4046` → IC=+0.160 (n=48)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 2343.4046 (IC base=+0.151)

### MOMENTUM_IBS_15M_BALLENA
- **PATRÓN** `drift_20min_pct` |x|≤ `0.1356` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `drift_20min_pct` |x|≤ 0.1356 (IC base=+0.100)

- **PATRÓN** `ibs_20min` > `1.0` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `ibs_20min` > 1.0 (IC base=+0.100)

### MOMENTUM_IBS_15M_FADE
- **FILTRO** `py_entrada` < `0.505` → IC=-0.239 (n=21)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.062 (n=30)

- **FILTRO** `drift_20min_pct` |x|> `0.1191` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `drift_20min_pct` |x|> 0.1191
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=30)

- **FILTRO** `libro_liquidez` < `2462.4476` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 2462.4476
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=35)

### MOMENTUM_IBS_5M
- **PATRÓN** `libro_liquidez` > `3526.4551` → IC=+0.140 (n=48)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 3526.4551 (IC base=+0.060)

### MOMENTUM_IBS_5M#DOGE#5min
- **FILTRO** `ibs_7min` < `1.0` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `ibs_7min` < 1.0
  - _Potencial_: sin este filtro IC_bueno=+0.150 (n=18)

### MOMENTUM_IBS_5M_BALLENA
- **FILTRO** `py_entrada` > `0.5` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `py_entrada` > 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.082 (n=53)

### MOMENTUM_IBS_5M_FADE#BNB#5min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.4012` → IC=+0.161 (n=113)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio` |x|> 0.4012 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.145)

- **PATRÓN** `total_vol_5m` < `447.889` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 447.889 (IC base=+0.145)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.145)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.2125` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.2125
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=38)

- **FILTRO** `pct_vs_K` |x|> `3.4276` → IC=-0.456 (n=43)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4276
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=48)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `pct_vs_K` |x|> `1.4189` → IC=-0.464 (n=26)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 1.4189
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` > `144.5498` → IC=-0.397 (n=27)

  - _Acción_: SKIP cuando `T_h` > 144.5498
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=28)

- **FILTRO** `T_h` < `111.9668` → IC=-0.447 (n=17)

  - _Acción_: SKIP cuando `T_h` < 111.9668
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=37)

### PRICE_TARGET_GBM_FADE#BTC#atexpiry
- **FILTRO** `sigma_h` > `0.0034` → IC=-0.324 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### PRICE_TARGET_GBM_FADE#ETH#atexpiry
- **FILTRO** `T_h` > `95.1632` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `T_h` > 95.1632
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

- **FILTRO** `sigma_h` > `0.0033` → IC=-0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0033
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

### STREAK_FADE_5M
- **FILTRO** `hora_utc` > `14.0` → IC=-0.156 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.035 (n=69)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.027 (n=72)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.204 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=-0.025)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `hora_utc` > `5.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `py_entrada` > `0.495` → IC=-0.250 (n=18)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `py_entrada` < `0.505` → IC=-0.220 (n=23)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `hora_utc` > `8.0` → IC=-0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.231 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.495 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7209.108` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 7209.108 (IC base=+0.125)

### STREAK_MOM_5M#XRP#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=+0.147 (n=49)

- **PATRÓN** `streak_len` < `3.0` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `streak_len` < 3.0 (IC base=+0.076)

### STRUCT_NO_15M#BTC#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.009 (n=631)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=344)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.023 (n=352)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0054` → IC=+0.134 (n=140)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0054 (IC base=+0.099)

### UPDOWN_GBM#5min
- **FILTRO** `sigma_h` < `0.0056` → IC=-0.124 (n=176)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0056
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=65)

- **FILTRO** `sigma_h` > `0.0057` → IC=-0.147 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0057
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=163)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=30)

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `sigma_h` > `0.0023` → IC=+0.147 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0023 (IC base=+0.120)

### UPDOWN_GBM#BTC#5min
- **FILTRO** `sigma_h` < `0.0037` → IC=-0.208 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0037
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.182 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0055 (IC base=+0.156)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.194 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0043 (IC base=+0.156)

### UPDOWN_GBM#ETH#5min
- **FILTRO** `sigma_h` < `0.0027` → IC=-0.167 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0027
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=28)

### UPDOWN_GBM#SOL#5min
- **FILTRO** `sigma_h` > `0.0046` → IC=-0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0061` → IC=-0.222 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0061
  - _Potencial_: sin este filtro IC_bueno=+0.237 (n=17)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` > `0.005` → IC=+0.160 (n=95)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.005 (IC base=+0.083)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.244 (n=37)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.006 (IC base=+0.109)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.2` → IC=+0.240 (n=71)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.2 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.264 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.226)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.2` → IC=+0.235 (n=47)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.2 (IC base=+0.191)

- **PATRÓN** `sigma_h` < `0.0025` → IC=+0.245 (n=45)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0025 (IC base=+0.191)

### UPDOWN_GBM_15M_TARDIO
- **FILTRO** `sigma_h` < `0.0041` → IC=-0.164 (n=230)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0041
  - _Potencial_: sin este filtro IC_bueno=-0.007 (n=779)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0032` → IC=-0.200 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0032
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=152)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `sigma_h` > `0.0041` → IC=-0.167 (n=25)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0041
  - _Potencial_: sin este filtro IC_bueno=-0.085 (n=51)

- **PATRÓN** `sigma_h` > `0.0052` → IC=+0.278 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0052 (IC base=+0.204)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.258 (n=31)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0036 (IC base=+0.246)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.19` → IC=+0.232 (n=54)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.19 (IC base=+0.220)

- **PATRÓN** `sigma_h` < `0.0029` → IC=+0.230 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0029 (IC base=+0.220)

- **PATRÓN** `sigma_h` > `0.0021` → IC=+0.232 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0021 (IC base=+0.220)

### UPDOWN_GBM_IBS_ALTO#ETH#15min
- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.375 (n=22)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.283)

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

- **FILTRO** `pct_spot_vs_ref` |x|> `0.1228` → IC=-0.172 (n=65)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1228
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=203)

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

- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min` — IC=+0.278 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH` — IC=+0.278 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `LEADLAG_BTC_XRP_15M` — IC=+0.149 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `LEADLAG_BTC_XRP_15M#XRP#15min` — IC=+0.149 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `LEADLAG_BTC_XRP_15M#XRP` — IC=+0.149 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `LEADLAG_BTC_XRP_15M#15min` — IC=+0.149 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min` — IC=+0.419 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL` — IC=+0.419 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM#DOGE#15min` — IC=+0.176 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 475 | +0.041 | +32.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 475 | +0.041 | +32.12€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 252 | +0.043 | +24.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 252 | +0.043 | +24.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 202 | +0.020 | -0.36€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 202 | +0.020 | -0.36€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 21 | +0.196 | +7.52€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 21 | +0.196 | +7.52€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 2780 | -0.121 | -423.77€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 407 | +0.016 | -0.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 2373 | -0.145 | -423.22€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 331 | -0.182 | -90.16€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 331 | -0.182 | -90.16€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 407 | +0.016 | -0.55€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 407 | +0.016 | -0.55€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#DOGE | 250 | -0.250 | -158.56€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#DOGE#5min | 250 | -0.250 | -158.56€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 596 | -0.142 | -19.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 596 | -0.142 | -19.20€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 676 | -0.041 | -88.61€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 676 | -0.041 | -88.61€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP | 520 | -0.207 | -66.68€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#XRP#5min | 520 | -0.207 | -66.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 12290 | +0.117 | -686.51€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#15min | 3093 | +0.179 | -120.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 94 | -0.094 | -42.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 6575 | +0.086 | -535.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2528 | +0.130 | +12.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 1114 | +0.036 | -238.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 12 | -0.043 | -1.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 1098 | +0.039 | -231.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 2885 | +0.142 | +3.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 844 | +0.187 | -50.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 38 | -0.100 | -18.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 1096 | +0.119 | +12.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 907 | +0.138 | +60.34€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 1106 | +0.050 | -198.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 8 | -0.040 | -4.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 1098 | +0.051 | -194.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 3119 | +0.127 | -41.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1142 | +0.162 | -21.72€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#ETH#240min | 12 | -0.129 | -8.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 1096 | +0.105 | -11.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 869 | +0.115 | +0.09€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#SOL | 2960 | +0.137 | -182.70€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1076 | +0.198 | -45.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 39 | +0.012 | -7.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 1093 | +0.083 | -81.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 752 | +0.137 | -47.80€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 1106 | +0.121 | -28.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 11 | +0.064 | +3.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 1094 | +0.121 | -30.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 3181 | +0.168 | -270.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 3181 | +0.168 | -270.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 801 | +0.165 | -91.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 801 | +0.165 | -91.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 65 | -0.052 | -1.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 65 | -0.052 | -1.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 790 | +0.163 | -94.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 790 | +0.163 | -94.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 703 | +0.225 | -31.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 703 | +0.225 | -31.50€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 743 | +0.180 | -65.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 743 | +0.180 | -65.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 150 | +0.408 | -10.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 150 | +0.408 | -10.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 55 | +0.412 | -2.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 55 | +0.412 | -2.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 58 | +0.367 | -8.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 58 | +0.367 | -8.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 35 | +0.419 | -0.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 35 | +0.419 | -0.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 4784 | +0.189 | -442.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 4784 | +0.189 | -442.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 905 | +0.099 | -198.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 905 | +0.099 | -198.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 737 | +0.246 | -8.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 737 | +0.246 | -8.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 849 | +0.140 | -138.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 849 | +0.140 | -138.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 777 | +0.224 | -29.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 777 | +0.224 | -29.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 736 | +0.252 | -1.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 736 | +0.252 | -1.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 780 | +0.196 | -65.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 780 | +0.196 | -65.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1667 | +0.149 | +84.77€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 1667 | +0.149 | +84.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 831 | +0.151 | +47.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 831 | +0.151 | +47.78€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 836 | +0.147 | +36.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 836 | +0.147 | +36.99€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 512 | +0.294 | -3.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 512 | +0.294 | -3.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 215 | +0.265 | -13.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 215 | +0.265 | -13.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 239 | +0.297 | +4.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 239 | +0.297 | +4.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 58 | +0.367 | +5.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 58 | +0.367 | +5.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 213 | +0.407 | -10.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 213 | +0.407 | -10.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 96 | +0.398 | -6.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 96 | +0.398 | -6.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 94 | +0.417 | -4.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 94 | +0.417 | -4.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 23 | +0.340 | +0.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 23 | +0.340 | +0.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 227 | +0.260 | -25.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 227 | +0.260 | -25.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 227 | +0.260 | -25.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 227 | +0.260 | -25.37€ | 0 | 0 |
| ✅ GBM_LATE_15M | 4085 | +0.087 | +1365.23€ | 0 | 0 |
| ✅ GBM_LATE_15M#15min | 4085 | +0.087 | +1365.23€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 706 | +0.171 | +429.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 706 | +0.171 | +429.83€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 371 | +0.157 | +143.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 371 | +0.157 | +143.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE | 702 | +0.193 | +486.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 702 | +0.193 | +486.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH | 554 | +0.007 | +20.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 554 | +0.007 | +20.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL | 799 | +0.007 | +66.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 799 | +0.007 | +66.24€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP | 953 | +0.033 | +218.45€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 953 | +0.033 | +218.45€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 5066 | +0.052 | +1501.61€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 5066 | +0.052 | +1501.61€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 978 | -0.021 | +203.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 978 | -0.021 | +203.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 959 | -0.003 | +113.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 959 | -0.003 | +113.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 609 | +0.233 | +540.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 609 | +0.233 | +540.71€ | 0 | 1 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 880 | -0.006 | +22.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 880 | -0.006 | +22.97€ | 1 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 913 | +0.006 | +72.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 913 | +0.006 | +72.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 727 | +0.200 | +549.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 727 | +0.200 | +549.47€ | 0 | 6 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 2908 | +0.172 | +1923.10€ | 0 | 12 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 2908 | +0.172 | +1923.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 524 | +0.186 | +367.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 524 | +0.186 | +367.43€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 375 | +0.192 | +243.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 375 | +0.192 | +243.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 514 | +0.203 | +402.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 514 | +0.203 | +402.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 343 | +0.213 | +250.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 343 | +0.213 | +250.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 559 | +0.067 | +211.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 559 | +0.067 | +211.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 593 | +0.191 | +447.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 593 | +0.191 | +447.26€ | 0 | 7 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 512 | +0.039 | +39.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 512 | +0.039 | +39.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 83 | +0.029 | -2.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 83 | +0.029 | -2.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 111 | +0.164 | +45.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 111 | +0.164 | +45.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 221 | -0.011 | +1.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 221 | -0.011 | +1.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 97 | +0.015 | -5.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 97 | +0.015 | -5.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 3405 | +0.165 | +2159.77€ | 0 | 12 |
| ✅ GBM_LATE_15M_TARDIO#15min | 3405 | +0.165 | +2159.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 678 | +0.182 | +462.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 678 | +0.182 | +462.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 439 | +0.144 | +222.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 439 | +0.144 | +222.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 674 | +0.223 | +572.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 674 | +0.223 | +572.88€ | 0 | 3 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 283 | +0.100 | +101.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 283 | +0.100 | +101.90€ | 2 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 569 | +0.073 | +220.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 569 | +0.073 | +220.26€ | 1 | 1 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 762 | +0.199 | +580.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 762 | +0.199 | +580.35€ | 0 | 6 |
| ✅ GBM_LATE_5M | 152 | +0.013 | -3.14€ | 2 | 1 |
| ✅ GBM_LATE_5M#5min | 152 | +0.013 | -3.14€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 72 | +0.013 | -4.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 72 | +0.013 | -4.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 28 | +0.067 | +1.26€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 28 | +0.067 | +1.26€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL | 42 | -0.068 | -1.47€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 42 | -0.068 | -1.47€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 10 | +0.083 | +1.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 10 | +0.083 | +1.62€ | 0 | 0 |
| ✅ GBM_LATE_60M | 479 | -0.051 | +55.81€ | 4 | 2 |
| ✅ GBM_LATE_60M#60min | 479 | -0.051 | +55.81€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 167 | -0.003 | +6.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 167 | -0.003 | +6.30€ | 3 | 1 |
| ✅ GBM_LATE_60M#ETH | 170 | -0.035 | +32.45€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 170 | -0.035 | +32.45€ | 3 | 2 |
| ✅ GBM_LATE_60M#SOL | 142 | -0.125 | +17.06€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 142 | -0.125 | +17.06€ | 3 | 1 |
| 🚫 GBM_LATE_60M_FADE | 189 | -0.301 | -32.44€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 189 | -0.301 | -32.44€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 75 | -0.253 | -6.85€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 75 | -0.253 | -6.85€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 64 | -0.348 | -18.54€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 64 | -0.348 | -18.54€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 50 | -0.288 | -7.05€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 50 | -0.288 | -7.05€ | 1 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 295 | +0.056 | +14.12€ | 1 | 1 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 295 | +0.056 | +14.12€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 115 | +0.021 | +6.95€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 115 | +0.021 | +6.95€ | 0 | 1 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 64 | +0.151 | +10.49€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 64 | +0.151 | +10.49€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 116 | +0.034 | -3.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 116 | +0.034 | -3.31€ | 1 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 35 | +0.149 | +9.99€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 35 | +0.149 | +9.99€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 35 | +0.149 | +9.99€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 35 | +0.149 | +9.99€ | 0 | 0 |
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
| ✅ LIQUIDACIONES_5M | 69 | -0.176 | -13.35€ | 3 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 69 | -0.176 | -13.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 17 | -0.112 | -2.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 17 | -0.112 | -2.76€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#DOGE#5min | 8 | -0.040 | -1.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 15 | -0.110 | -2.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 15 | -0.110 | -2.67€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL | 14 | -0.175 | -4.13€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL#5min | 14 | -0.175 | -4.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 14 | -0.131 | -3.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 14 | -0.131 | -3.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M | 284 | +0.018 | -0.37€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 284 | +0.018 | -0.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 96 | +0.000 | -6.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 96 | +0.000 | -6.21€ | 0 | 1 |
| ✅ LIQUIDACIONES_60M#ETH | 91 | +0.016 | +1.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 91 | +0.016 | +1.15€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 97 | +0.035 | +4.69€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 97 | +0.035 | +4.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M | 96 | +0.092 | +12.72€ | 0 | 5 |
| ✅ MOMENTUM_IBS_15M#15min | 96 | +0.092 | +12.72€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB | 16 | -0.044 | +0.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BNB#15min | 16 | -0.044 | +0.02€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC | 16 | +0.133 | +6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#BTC#15min | 16 | +0.133 | +6.22€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE | 16 | +0.133 | +4.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#DOGE#15min | 16 | +0.133 | +4.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH | 16 | +0.000 | -0.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#ETH#15min | 16 | +0.000 | -0.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL | 16 | +0.089 | +1.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#SOL#15min | 16 | +0.089 | +1.61€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP | 16 | +0.089 | +0.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M#XRP#15min | 16 | +0.089 | +0.65€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA | 88 | +0.022 | +0.89€ | 0 | 2 |
| ✅ MOMENTUM_IBS_15M_BALLENA#15min | 88 | +0.022 | +0.89€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB | 15 | +0.022 | +0.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BNB#15min | 15 | +0.022 | +0.33€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC | 15 | -0.066 | -1.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#BTC#15min | 15 | -0.066 | -1.59€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE | 14 | +0.087 | +1.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#DOGE#15min | 14 | +0.087 | +1.90€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH | 14 | +0.000 | -0.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#ETH#15min | 14 | +0.000 | -0.53€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL | 15 | -0.022 | -0.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#SOL#15min | 15 | -0.022 | -0.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP | 15 | +0.066 | +1.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_BALLENA#XRP#15min | 15 | +0.066 | +1.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE | 83 | -0.076 | -7.29€ | 3 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#15min | 83 | -0.076 | -7.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB | 12 | +0.043 | +1.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BNB#15min | 12 | +0.043 | +1.01€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC | 13 | -0.108 | -2.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#BTC#15min | 13 | -0.108 | -2.63€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE | 14 | -0.087 | -2.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#DOGE#15min | 14 | -0.087 | -2.20€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH | 14 | +0.000 | -0.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#ETH#15min | 14 | +0.000 | -0.17€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL | 15 | -0.066 | -1.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#SOL#15min | 15 | -0.066 | -1.62€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP | 15 | -0.066 | -1.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_15M_FADE#XRP#15min | 15 | -0.066 | -1.69€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M | 303 | +0.057 | +20.82€ | 0 | 1 |
| ✅ MOMENTUM_IBS_5M#5min | 303 | +0.057 | +20.82€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB | 51 | +0.028 | +1.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BNB#5min | 51 | +0.028 | +1.44€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC | 51 | +0.160 | +11.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#BTC#5min | 51 | +0.160 | +11.73€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE | 49 | -0.029 | -2.80€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#DOGE#5min | 49 | -0.029 | -2.80€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH | 52 | +0.056 | +4.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#ETH#5min | 52 | +0.056 | +4.29€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL | 51 | +0.066 | +3.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#SOL#5min | 51 | +0.066 | +3.77€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP | 49 | +0.049 | +2.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M#XRP#5min | 49 | +0.049 | +2.39€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA | 181 | +0.008 | -2.16€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#5min | 181 | +0.008 | -2.16€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB | 26 | -0.071 | -2.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BNB#5min | 26 | -0.071 | -2.26€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC | 35 | +0.013 | +0.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#BTC#5min | 35 | +0.013 | +0.09€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE | 29 | +0.081 | +1.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#DOGE#5min | 29 | +0.081 | +1.07€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH | 31 | -0.136 | -5.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#ETH#5min | 31 | -0.136 | -5.52€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL | 32 | +0.059 | +1.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#SOL#5min | 32 | +0.059 | +1.50€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP | 28 | +0.100 | +2.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_BALLENA#XRP#5min | 28 | +0.100 | +2.96€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE | 245 | -0.026 | -11.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#5min | 245 | -0.026 | -11.32€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB | 38 | +0.000 | -0.45€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BNB#5min | 38 | +0.000 | -0.45€ | 1 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC | 44 | -0.043 | -5.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#BTC#5min | 44 | -0.043 | -5.51€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE | 40 | +0.000 | -0.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#DOGE#5min | 40 | +0.000 | -0.47€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH | 45 | +0.011 | +0.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#ETH#5min | 45 | +0.011 | +0.74€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL | 41 | -0.081 | -3.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#SOL#5min | 41 | -0.081 | -3.86€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP | 37 | -0.038 | -1.78€ | 0 | 0 |
| ✅ MOMENTUM_IBS_5M_FADE#XRP#5min | 37 | -0.038 | -1.78€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 188 | +0.079 | +28.72€ | 1 | 4 |
| ✅ ORDER_FLOW_5M#5min | 52 | +0.130 | +16.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 12 | +0.171 | +12.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 12 | +0.171 | +12.92€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 9 | -0.021 | -1.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 9 | -0.021 | -1.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 17 | +0.067 | +1.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 17 | +0.067 | +1.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 12 | +0.043 | +0.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 12 | +0.043 | +0.24€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 215 | -0.131 | -6.45€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 87 | -0.174 | -18.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#atexpiry | 74 | -0.184 | -15.78€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 13 | -0.065 | -2.96€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 86 | -0.136 | -1.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 71 | -0.144 | -3.15€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 15 | -0.066 | +1.23€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 42 | -0.023 | +14.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 37 | +0.013 | +15.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 5 | -0.054 | -1.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 182 | -0.130 | -3.47€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 33 | -0.129 | -2.99€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 109 | -0.275 | -25.44€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 45 | -0.202 | -6.50€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 43 | -0.189 | -5.48€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 49 | -0.265 | -11.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 47 | -0.255 | -10.27€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 15 | -0.331 | -7.65€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 14 | -0.306 | -7.14€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 104 | -0.264 | -22.89€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#reach | 5 | -0.089 | -2.55€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 48 | +0.240 | +4.75€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 17 | -0.022 | -2.94€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 15 | +0.199 | +1.27€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 16 | +0.356 | +6.43€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 16 | +0.356 | +6.43€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 48 | +0.240 | +4.75€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 22 | -0.083 | -8.24€ | 0 | 0 |
| ✅ STREAK_FADE_15M#15min | 22 | -0.083 | -8.24€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 10 | +0.000 | -3.01€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 10 | +0.000 | -3.01€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 11 | -0.064 | -4.09€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 11 | -0.064 | -4.09€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 264 | -0.034 | -20.78€ | 2 | 1 |
| ✅ STREAK_FADE_5M#5min | 264 | -0.034 | -20.78€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 54 | +0.036 | +1.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 54 | +0.036 | +1.94€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 99 | -0.005 | -6.85€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 99 | -0.005 | -6.85€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 49 | -0.108 | -8.67€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 49 | -0.108 | -8.67€ | 1 | 0 |
| ✅ STREAK_FADE_5M#XRP | 62 | -0.078 | -7.19€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 62 | -0.078 | -7.19€ | 1 | 0 |
| ✅ STREAK_FADE_60M | 14 | -0.087 | -2.15€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 14 | -0.087 | -2.15€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 8 | -0.080 | -2.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 8 | -0.080 | -2.07€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 418 | +0.026 | +4.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 418 | +0.026 | +4.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE | 126 | +0.000 | -2.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#DOGE#5min | 126 | +0.000 | -2.71€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 89 | +0.028 | +6.42€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 89 | +0.028 | +6.42€ | 1 | 3 |
| ✅ STREAK_MOM_5M#SOL | 105 | +0.042 | +0.12€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 105 | +0.042 | +0.12€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP | 98 | +0.040 | +0.47€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 98 | +0.040 | +0.47€ | 1 | 1 |
| ✅ STRUCT_NO_15M | 1708 | +0.008 | -16.49€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 1708 | +0.008 | -16.49€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 650 | +0.003 | -10.15€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 650 | +0.003 | -10.15€ | 1 | 0 |
| ✅ STRUCT_NO_15M#ETH | 682 | +0.012 | -4.26€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 682 | +0.012 | -4.26€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 376 | +0.011 | -2.08€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 376 | +0.011 | -2.08€ | 2 | 0 |
| ✅ UPDOWN_GBM | 1574 | +0.017 | +69.98€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 712 | +0.092 | +118.79€ | 0 | 1 |
| ✅ UPDOWN_GBM#240min | 105 | +0.033 | +2.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 470 | -0.059 | -42.02€ | 2 | 0 |
| ✅ UPDOWN_GBM#60min | 240 | -0.021 | -8.39€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 53 | +0.045 | +5.31€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 47 | +0.071 | +6.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#5min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 282 | -0.004 | -9.22€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 111 | +0.066 | -2.13€ | 0 | 1 |
| ✅ UPDOWN_GBM#BTC#240min | 30 | +0.062 | +1.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 41 | -0.058 | -2.11€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 82 | -0.059 | -8.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 189 | -0.008 | -3.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 35 | +0.176 | +12.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#5min | 154 | -0.051 | -15.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 383 | +0.051 | +33.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 177 | +0.131 | +37.99€ | 0 | 2 |
| ✅ UPDOWN_GBM#ETH#240min | 31 | +0.076 | +1.45€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 66 | -0.059 | -4.96€ | 1 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 94 | +0.010 | -0.59€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 289 | -0.009 | +1.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 109 | +0.022 | +1.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#240min | 27 | +0.017 | +0.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 77 | -0.019 | -1.11€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 64 | -0.015 | +0.81€ | 1 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 376 | +0.026 | +44.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 233 | +0.096 | +62.82€ | 0 | 2 |
| ✅ UPDOWN_GBM#XRP#240min | 16 | -0.089 | -2.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 127 | -0.081 | -16.42€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 100 | +0.226 | -7.07€ | 0 | 2 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 100 | +0.226 | -7.07€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 66 | +0.191 | -12.57€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 66 | +0.191 | -12.57€ | 0 | 2 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 34 | +0.278 | +5.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 34 | +0.278 | +5.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1438 | -0.039 | +149.17€ | 1 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1438 | -0.039 | +149.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 82 | -0.059 | -1.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 82 | -0.059 | -1.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 290 | -0.134 | -0.36€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 290 | -0.134 | -0.36€ | 1 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 32 | -0.059 | -2.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 32 | -0.059 | -2.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 118 | +0.000 | +19.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 118 | +0.000 | +19.94€ | 1 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 462 | +0.009 | +89.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 462 | +0.009 | +89.93€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 454 | -0.031 | +43.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 454 | -0.031 | +43.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 124 | +0.246 | +54.04€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 124 | +0.246 | +54.04€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 80 | +0.220 | +23.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 80 | +0.220 | +23.88€ | 0 | 3 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 44 | +0.283 | +30.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 44 | +0.283 | +30.16€ | 0 | 1 |
| ✅ UPDOWN_OU_5M | 300 | -0.063 | -24.33€ | 4 | 0 |
| ✅ UPDOWN_OU_5M#5min | 300 | -0.063 | -24.33€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 193 | -0.013 | -11.77€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 193 | -0.013 | -11.77€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 15 | +0.022 | +2.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 15 | +0.022 | +2.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 14 | -0.131 | -3.06€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 14 | -0.131 | -3.06€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 28 | -0.167 | -4.42€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 28 | -0.167 | -4.42€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 28 | -0.200 | -4.70€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 28 | -0.200 | -4.70€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 22 | -0.125 | -3.21€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 22 | -0.125 | -3.21€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 910 | +0.285 | +386.45€ | 0 | 1 |
| ✅ WEEKLY_PRICE#BTC | 270 | +0.199 | +8.22€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 289 | +0.256 | +69.14€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 351 | +0.372 | +309.10€ | 0 | 1 |