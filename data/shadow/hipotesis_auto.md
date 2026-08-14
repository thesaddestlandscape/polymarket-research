# Hipótesis automáticas — 2026-08-14 12:34 UTC
_Generado por shadow_postmortem.py sobre 26269 resoluciones (PNL=+4879.81€)_

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

- **PATRÓN** `py_entrada` > `0.575` → IC=+0.186 (n=151)

  - _Acción_: Kelly boost +0.93€ cuando `py_entrada` > 0.575 (IC base=+0.183)

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
- **PATRÓN** `py_entrada` < `0.39` → IC=+0.204 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.39 (IC base=+0.158)

- **PATRÓN** `py_entrada` > `0.43` → IC=+0.170 (n=104)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.43 (IC base=+0.158)

- **PATRÓN** `restante_min` < `4.74` → IC=+0.164 (n=120)

  - _Acción_: Kelly boost +0.82€ cuando `restante_min` < 4.74 (IC base=+0.158)

- **PATRÓN** `restante_min` > `4.93` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `restante_min` > 4.93 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.221 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.169 (n=137)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 6.0 (IC base=+0.158)

- **PATRÓN** `lag_apertura_s` < `6.69` → IC=+0.191 (n=79)

  - _Acción_: Kelly boost +0.96€ cuando `lag_apertura_s` < 6.69 (IC base=+0.158)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.140)

- **PATRÓN** `py_entrada` > `0.43` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `py_entrada` > 0.43 (IC base=+0.140)

- **PATRÓN** `restante_min` < `4.68` → IC=+0.188 (n=62)

  - _Acción_: Kelly boost +0.94€ cuando `restante_min` < 4.68 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.194 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 9.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `3.0` → IC=+0.200 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 3.0 (IC base=+0.140)

- **PATRÓN** `lag_apertura_s` < `53.38` → IC=+0.143 (n=82)

  - _Acción_: Kelly boost +0.71€ cuando `lag_apertura_s` < 53.38 (IC base=+0.140)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.41` → IC=+0.221 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.41 (IC base=+0.175)

- **PATRÓN** `restante_min` > `4.95` → IC=+0.289 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` > 4.95 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.235 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.174 (n=93)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 9.0 (IC base=+0.175)

- **PATRÓN** `lag_apertura_s` < `3.12` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `lag_apertura_s` < 3.12 (IC base=+0.175)

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

- **PATRÓN** `sigma_ewma_delta_pct` < `7.816` → IC=+0.339 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 7.816 (IC base=+0.292)

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

- **PATRÓN** `libro_liquidez` > `1428.8266` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1428.8266 (IC base=+0.307)

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

- **PATRÓN** `sigma_ewma_delta_pct` < `8.451` → IC=+0.348 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 8.451 (IC base=+0.246)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.193 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0062 (IC base=+0.184)

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

- **PATRÓN** `libro_liquidez` > `1069.035` → IC=+0.191 (n=137)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 1069.035 (IC base=+0.184)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.260 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.266)

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

- **PATRÓN** `drift_60min` |x|≤ `0.2419` → IC=+0.194 (n=47)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.97€ cuando `drift_60min` |x|≤ 0.2419 (IC base=+0.185)

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

- **PATRÓN** `sigma_ewma_delta_pct` < `8.126` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 8.126 (IC base=+0.185)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.156 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0044 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.364` → IC=+0.172 (n=184)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.86€ cuando `drift_60min` |x|≤ 0.364 (IC base=+0.148)

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

- **PATRÓN** `drift_60min` |x|≤ `0.3613` → IC=+0.245 (n=45)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.3613 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.265 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 4.0 (IC base=+0.210)

- **PATRÓN** `ibs_20min` < `0.3438` → IC=+0.266 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `ibs_20min` < 0.3438 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` < `0.6417` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` < 0.6417 (IC base=+0.210)

- **PATRÓN** `volumen_regimen` > `1.3794` → IC=+0.289 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_regimen` > 1.3794 (IC base=+0.210)

- **PATRÓN** `libro_liquidez` > `1559.082` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1559.082 (IC base=+0.210)

### GBM_LATE_5M
- **FILTRO** `ibs_20min` > `0.6176` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `ibs_20min` > 0.6176
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=10)

### GBM_LATE_60M
- **FILTRO** `sigma_ewma_delta_pct` < `5.949` → IC=-0.210 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 5.949
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=51)

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

- **FILTRO** `hora_utc` > `4.0` → IC=-0.183 (n=39)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=14)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0031 (IC base=+0.028)

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
  - _Potencial_: sin este filtro IC_bueno=-0.048 (n=71)

- **FILTRO** `py_entrada` > `0.485` → IC=-0.151 (n=41)

  - _Acción_: SKIP cuando `py_entrada` > 0.485
  - _Potencial_: sin este filtro IC_bueno=-0.032 (n=60)

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

### LIQUIDACIONES_60M
- **FILTRO** `liq_imbalance_60min` |x|≤ `0.9658` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 0.9658
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=54)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.167 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=50)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `py_entrada` > `0.465` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.465
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.167 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 13.0 (IC base=+0.009)

### LIQUIDACIONES_60M#SOL#60min
- **PATRÓN** `libro_spread` < `0.03` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.03 (IC base=+0.115)

### ORDER_FLOW_5M
- **FILTRO** `total_vol_5m` > `215.224` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `total_vol_5m` > 215.224
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **PATRÓN** `delta_ratio` |x|> `0.4026` → IC=+0.163 (n=81)
  - _Por qué funciona_: delta_ratio alto → flow informado visible; edge real en el desequilibrio
  - _Acción_: Kelly boost +0.81€ cuando `delta_ratio` |x|> 0.4026 (IC base=+0.145)

- **PATRÓN** `total_vol_5m` < `618.066` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `total_vol_5m` < 618.066 (IC base=+0.145)

### PRICE_TARGET_GBM
- **FILTRO** `pct_vs_K` |x|> `7.275` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.275
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=38)

- **FILTRO** `sigma_h` > `0.0055` → IC=-0.320 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=+0.281 (n=30)

- **FILTRO** `pct_vs_K` |x|> `4.7494` → IC=-0.464 (n=26)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 4.7494
  - _Potencial_: sin este filtro IC_bueno=-0.264 (n=53)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.338 (n=35)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.233 (n=13)

- **FILTRO** `T_h` > `63.9981` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `T_h` > 63.9981
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### PRICE_TARGET_GBM_FADE
- **FILTRO** `sigma_h` < `0.0047` → IC=-0.350 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **FILTRO** `T_h` < `135.9668` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `T_h` < 135.9668
  - _Potencial_: sin este filtro IC_bueno=-0.196 (n=21)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.147 (n=32)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=224)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=232)

### UPDOWN_GBM#15min
- **PATRÓN** `sigma_h` > `0.0053` → IC=+0.163 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0053 (IC base=+0.104)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.120 (n=135)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` > 0.0048 (IC base=+0.071)

### UPDOWN_GBM#60min
- **FILTRO** `hora_utc` < `11.0` → IC=-0.269 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=-0.052 (n=27)

- **FILTRO** `ibs_15` < `0.5186` → IC=-0.204 (n=25)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5186
  - _Potencial_: sin este filtro IC_bueno=-0.107 (n=26)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0121` → IC=-0.192 (n=24)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0121
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.128 (n=41)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` > 0.0028 (IC base=+0.056)

- **PATRÓN** `sigma_h` > `0.0038` → IC=+0.186 (n=49)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0038 (IC base=+0.140)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `sigma_h` < `0.006` → IC=-0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=16)

### UPDOWN_GBM#SOL#60min
- **FILTRO** `sigma_h` > `0.0061` → IC=-0.222 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0061
  - _Potencial_: sin este filtro IC_bueno=+0.318 (n=9)

### UPDOWN_GBM#XRP#15min
- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.227 (n=31)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0059 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.175 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0055 (IC base=+0.172)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.192 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0063 (IC base=+0.141)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD
- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.214 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0022 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.259 (n=27)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0027 (IC base=+0.209)

### UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min
- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.19` → IC=+0.200 (n=38)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +1.00€ cuando `pct_spot_vs_ref` |x|≤ 0.19 (IC base=+0.179)

- **PATRÓN** `sigma_h` < `0.0019` → IC=+0.265 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0019 (IC base=+0.179)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `sigma_h` > `0.0022` → IC=-0.161 (n=107)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0022
  - _Potencial_: sin este filtro IC_bueno=-0.097 (n=60)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.318 (n=20)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0043 (IC base=+0.232)

### UPDOWN_GBM_IBS_ALTO
- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.269 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.211)

### UPDOWN_GBM_IBS_ALTO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.220 (n=48)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0026 (IC base=+0.192)

- **PATRÓN** `sigma_h` > `0.0022` → IC=+0.200 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0022 (IC base=+0.192)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1285` → IC=-0.237 (n=17)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1285
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

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

- **LIVE-CANDIDATA**: `UPDOWN_GBM_IBS_ALTO#ETH#15min` — IC=+0.235 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_IBS_ALTO#ETH` — IC=+0.235 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min` — IC=+0.350 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH` — IC=+0.350 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 383 | +0.030 | +19.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 383 | +0.030 | +19.70€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 249 | +0.042 | +23.56€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 249 | +0.042 | +23.56€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 125 | +0.004 | -4.00€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 125 | +0.004 | -4.00€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 9 | +0.021 | +0.14€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 9 | +0.021 | +0.14€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 652 | -0.038 | -117.19€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 265 | +0.167 | -2.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 387 | -0.179 | -114.80€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB | 67 | +0.007 | -17.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BNB#5min | 67 | +0.007 | -17.44€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 265 | +0.167 | -2.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 265 | +0.167 | -2.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE | 60 | -0.145 | -28.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 60 | -0.145 | -28.73€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#ETH | 94 | -0.302 | +3.62€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#ETH#5min | 94 | -0.302 | +3.62€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 108 | -0.191 | -54.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 108 | -0.191 | -54.95€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 58 | -0.183 | -17.29€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 58 | -0.183 | -17.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 5409 | +0.140 | -180.27€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#15min | 2126 | +0.184 | -87.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 60 | -0.081 | -23.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 901 | +0.065 | -103.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2322 | +0.133 | +34.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 160 | +0.018 | -31.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 8 | -0.040 | -1.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 149 | +0.036 | -26.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 1625 | +0.147 | -0.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 586 | +0.180 | -49.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 24 | -0.038 | -8.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 150 | +0.053 | -16.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 865 | +0.145 | +73.59€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 155 | -0.003 | -42.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 152 | +0.006 | -37.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 1739 | +0.137 | -13.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 795 | +0.175 | +4.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 11 | -0.106 | -7.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 151 | +0.049 | -15.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 782 | +0.120 | +4.94€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#SOL | 1572 | +0.161 | -93.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 726 | +0.203 | -38.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 21 | +0.022 | -2.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 150 | +0.092 | -9.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 675 | +0.134 | -43.93€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 158 | +0.144 | +0.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 8 | +0.040 | +0.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 149 | +0.149 | +1.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2260 | +0.184 | -148.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 2260 | +0.184 | -148.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 561 | +0.177 | -54.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 561 | +0.177 | -54.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 84 | +0.326 | +1.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 84 | +0.326 | +1.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 544 | +0.176 | -55.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 544 | +0.176 | -55.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 478 | +0.242 | -10.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 478 | +0.242 | -10.33€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 79 | -0.204 | +13.76€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 79 | -0.204 | +13.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 514 | +0.182 | -43.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 514 | +0.182 | -43.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 105 | +0.397 | -8.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 105 | +0.397 | -8.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 43 | +0.411 | -1.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 43 | +0.411 | -1.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 38 | +0.350 | -5.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 38 | +0.350 | -5.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 22 | +0.375 | -1.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 22 | +0.375 | -1.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 623 | +0.156 | -85.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 623 | +0.156 | -85.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 116 | +0.085 | -28.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 116 | +0.085 | -28.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 99 | +0.124 | -16.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 99 | +0.124 | -16.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 107 | +0.142 | -18.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 107 | +0.142 | -18.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 104 | +0.151 | -14.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 104 | +0.151 | -14.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 97 | +0.237 | -0.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 97 | +0.237 | -0.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 100 | +0.196 | -7.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 100 | +0.196 | -7.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 238 | +0.158 | +17.22€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 238 | +0.158 | +17.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 123 | +0.140 | +5.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 123 | +0.140 | +5.38€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 115 | +0.175 | +11.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 115 | +0.175 | +11.84€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 442 | +0.284 | -11.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 442 | +0.284 | -11.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 187 | +0.262 | -11.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 187 | +0.262 | -11.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 209 | +0.287 | -1.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 209 | +0.287 | -1.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 46 | +0.333 | +0.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 46 | +0.333 | +0.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 176 | +0.393 | -13.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 176 | +0.393 | -13.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 80 | +0.378 | -8.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 80 | +0.378 | -8.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 80 | +0.415 | -3.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 80 | +0.415 | -3.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 16 | +0.222 | -0.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 16 | +0.222 | -0.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 160 | +0.241 | -23.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 160 | +0.241 | -23.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 160 | +0.241 | -23.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 160 | +0.241 | -23.75€ | 0 | 0 |
| ✅ GBM_LATE_15M | 2675 | +0.094 | +1014.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#15min | 2675 | +0.094 | +1014.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 412 | +0.234 | +356.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 412 | +0.234 | +356.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 232 | +0.107 | +73.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 232 | +0.107 | +73.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE | 428 | +0.235 | +373.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 428 | +0.235 | +373.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH | 372 | +0.005 | +5.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 372 | +0.005 | +5.64€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL | 585 | +0.001 | +37.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 585 | +0.001 | +37.40€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP | 646 | +0.040 | +168.38€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 646 | +0.040 | +168.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 3289 | +0.059 | +1125.82€ | 0 | 16 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 3289 | +0.059 | +1125.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 661 | -0.005 | +218.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 661 | -0.005 | +218.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 650 | +0.005 | +104.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 650 | +0.005 | +104.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 363 | +0.270 | +374.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 363 | +0.270 | +374.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 575 | -0.013 | -16.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 575 | -0.013 | -16.16€ | 2 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 607 | -0.003 | +49.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 607 | -0.003 | +49.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 433 | +0.238 | +393.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 433 | +0.238 | +393.99€ | 0 | 7 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 1743 | +0.199 | +1357.10€ | 0 | 13 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 1743 | +0.199 | +1357.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 305 | +0.262 | +309.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 305 | +0.262 | +309.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 262 | +0.178 | +149.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 262 | +0.178 | +149.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 293 | +0.239 | +271.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 293 | +0.239 | +271.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 229 | +0.201 | +159.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 229 | +0.201 | +159.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 318 | +0.069 | +150.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 318 | +0.069 | +150.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 336 | +0.237 | +317.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 336 | +0.237 | +317.66€ | 0 | 8 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 341 | +0.034 | +6.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 341 | +0.034 | +6.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 51 | +0.066 | -0.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 51 | +0.066 | -0.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 77 | +0.133 | +18.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 77 | +0.133 | +18.74€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 117 | -0.038 | -6.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 117 | -0.038 | -6.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 96 | +0.020 | -4.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 96 | +0.020 | -4.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 2073 | +0.179 | +1495.81€ | 0 | 14 |
| ✅ GBM_LATE_15M_TARDIO#15min | 2073 | +0.179 | +1495.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 390 | +0.247 | +369.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 390 | +0.247 | +369.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 297 | +0.115 | +139.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 297 | +0.115 | +139.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 410 | +0.255 | +399.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 410 | +0.255 | +399.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 184 | +0.027 | +39.40€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 184 | +0.027 | +39.40€ | 2 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 334 | +0.051 | +117.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 334 | +0.051 | +117.13€ | 1 | 1 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 458 | +0.243 | +430.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 458 | +0.243 | +430.55€ | 0 | 7 |
| ✅ GBM_LATE_5M | 48 | -0.020 | -2.56€ | 1 | 0 |
| ✅ GBM_LATE_5M#5min | 48 | -0.020 | -2.56€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 17 | -0.022 | -2.89€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 17 | -0.022 | -2.89€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 8 | +0.040 | -0.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 8 | +0.040 | -0.45€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL | 23 | -0.060 | +0.77€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 23 | -0.060 | +0.77€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 110 | +0.125 | +38.82€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 110 | +0.125 | +38.82€ | 0 | 0 |
| ✅ GBM_LATE_60M | 450 | -0.053 | +52.38€ | 4 | 2 |
| ✅ GBM_LATE_60M#60min | 450 | -0.053 | +52.38€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 158 | -0.013 | +6.83€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 158 | -0.013 | +6.83€ | 3 | 2 |
| ✅ GBM_LATE_60M#ETH | 162 | -0.030 | +33.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 162 | -0.030 | +33.30€ | 3 | 2 |
| ✅ GBM_LATE_60M#SOL | 130 | -0.129 | +12.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 130 | -0.129 | +12.25€ | 3 | 1 |
| 🚫 GBM_LATE_60M_FADE | 170 | -0.296 | -31.44€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 170 | -0.296 | -31.44€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 66 | -0.250 | -7.72€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 66 | -0.250 | -7.72€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 58 | -0.333 | -15.48€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 58 | -0.333 | -15.48€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 46 | -0.292 | -8.23€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 46 | -0.292 | -8.23€ | 1 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 251 | +0.045 | +4.72€ | 1 | 1 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 251 | +0.045 | +4.72€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 83 | +0.006 | +1.97€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 83 | +0.006 | +1.97€ | 0 | 1 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 53 | +0.118 | +5.55€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 53 | +0.118 | +5.55€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 115 | +0.038 | -2.80€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 115 | +0.038 | -2.80€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M | 201 | -0.111 | -29.01€ | 6 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 201 | -0.111 | -29.01€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BNB#15min | 5 | -0.054 | -1.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 48 | -0.120 | -8.11€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 48 | -0.120 | -8.11€ | 1 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 22 | -0.208 | -5.32€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 22 | -0.208 | -5.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 41 | -0.012 | -2.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 41 | -0.012 | -2.33€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 39 | -0.037 | -2.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 39 | -0.037 | -2.70€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 46 | -0.167 | -8.95€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 46 | -0.167 | -8.95€ | 1 | 0 |
| ✅ LIQUIDACIONES_5M | 5 | -0.018 | -0.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 5 | -0.018 | -0.59€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 21 | -0.152 | -3.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 21 | -0.152 | -3.90€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 12 | +0.086 | +2.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 12 | +0.086 | +2.55€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M | 227 | +0.033 | +4.64€ | 2 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 227 | +0.033 | +4.64€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 76 | +0.000 | -5.24€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 76 | +0.000 | -5.24€ | 1 | 1 |
| ✅ LIQUIDACIONES_60M#ETH | 74 | +0.026 | +0.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 74 | +0.026 | +0.53€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 77 | +0.070 | +9.35€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 77 | +0.070 | +9.35€ | 0 | 1 |
| ✅ ORDER_FLOW_5M | 146 | +0.061 | +13.49€ | 1 | 2 |
| ✅ ORDER_FLOW_5M#5min | 10 | +0.042 | +0.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 9 | +0.061 | +2.34€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 9 | +0.061 | +2.34€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM | 201 | -0.145 | -5.67€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM#BTC | 78 | -0.200 | -18.28€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 66 | -0.221 | -15.83€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 12 | -0.043 | -2.45€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 81 | -0.151 | -1.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 67 | -0.167 | -3.33€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 14 | -0.044 | +1.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 42 | -0.023 | +14.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 37 | +0.013 | +15.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 5 | -0.054 | -1.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 170 | -0.151 | -3.71€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 31 | -0.106 | -1.97€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 78 | -0.275 | -19.02€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 33 | -0.214 | -6.12€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 32 | -0.206 | -5.61€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 34 | -0.250 | -7.29€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 33 | -0.243 | -6.78€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL | 11 | -0.233 | -5.61€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#SOL#atexpiry | 10 | -0.208 | -5.10€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 75 | -0.266 | -17.49€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 44 | +0.304 | +7.91€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 14 | +0.044 | -1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 14 | +0.044 | -1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 14 | +0.219 | +2.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 14 | +0.219 | +2.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 16 | +0.356 | +6.43€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 16 | +0.356 | +6.43€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 44 | +0.304 | +7.91€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 18 | -0.135 | -9.19€ | 0 | 0 |
| ✅ STREAK_FADE_15M#15min | 18 | -0.135 | -9.19€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 8 | -0.040 | -4.01€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 8 | -0.040 | -4.01€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP | 9 | -0.061 | -4.04€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 9 | -0.061 | -4.04€ | 0 | 0 |
| ✅ STREAK_FADE_5M | 39 | -0.037 | -6.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#5min | 39 | -0.037 | -6.65€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE | 7 | +0.019 | +1.09€ | 0 | 0 |
| ✅ STREAK_FADE_5M#DOGE#5min | 7 | +0.019 | +1.09€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 13 | +0.022 | -0.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 13 | +0.022 | -0.97€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL | 13 | -0.108 | -5.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 13 | -0.108 | -5.30€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP | 6 | +0.000 | -1.47€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 6 | +0.000 | -1.47€ | 0 | 0 |
| ✅ STREAK_FADE_60M | 13 | -0.108 | -2.67€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 13 | -0.108 | -2.67€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 7 | -0.097 | -2.59€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 7 | -0.097 | -2.59€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_FADE_60M#SOL#60min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ STREAK_MOM_5M | 20 | -0.136 | -3.18€ | 0 | 0 |
| ✅ STREAK_MOM_5M#5min | 20 | -0.136 | -3.18€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 7 | -0.097 | -2.56€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 7 | -0.097 | -2.56€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL | 5 | -0.018 | -0.55€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 5 | -0.018 | -0.55€ | 0 | 0 |
| ✅ STRUCT_NO_15M | 1181 | +0.014 | -5.10€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 1181 | +0.014 | -5.10€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 453 | +0.021 | +0.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 453 | +0.021 | +0.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH | 472 | +0.015 | -1.57€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 472 | +0.015 | -1.57€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 256 | +0.000 | -4.25€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 256 | +0.000 | -4.25€ | 2 | 0 |
| ✅ UPDOWN_GBM | 767 | +0.025 | +57.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 416 | +0.088 | +69.50€ | 0 | 2 |
| ✅ UPDOWN_GBM#240min | 51 | -0.028 | -3.03€ | 0 | 0 |
| ✅ UPDOWN_GBM#5min | 69 | -0.007 | -0.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#60min | 184 | -0.027 | -8.05€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 14 | +0.131 | +5.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 13 | +0.152 | +5.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 203 | -0.027 | -15.65€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 88 | +0.011 | -10.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#240min | 13 | -0.022 | -0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#5min | 22 | +0.042 | +1.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 62 | -0.062 | -7.50€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 14 | +0.044 | +0.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 10 | +0.000 | -0.12€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 259 | +0.036 | +19.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 134 | +0.103 | +23.03€ | 0 | 2 |
| ✅ UPDOWN_GBM#ETH#240min | 15 | +0.022 | -0.71€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#5min | 20 | -0.045 | -0.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 75 | -0.006 | -1.88€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 137 | -0.040 | -3.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 53 | -0.009 | -2.17€ | 1 | 0 |
| ✅ UPDOWN_GBM#SOL#240min | 14 | -0.044 | -1.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#5min | 11 | -0.021 | -1.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 47 | -0.010 | +1.33€ | 1 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 138 | +0.129 | +52.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 118 | +0.158 | +53.85€ | 0 | 3 |
| ✅ UPDOWN_GBM#XRP#240min | 9 | -0.021 | -0.73€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#5min | 11 | -0.021 | -0.60€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 77 | +0.209 | -9.92€ | 0 | 2 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 77 | +0.209 | -9.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 54 | +0.179 | -12.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 54 | +0.179 | -12.47€ | 0 | 2 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 23 | +0.260 | +2.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 23 | +0.260 | +2.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 792 | -0.024 | +68.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 792 | -0.024 | +68.06€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 35 | +0.068 | +10.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 35 | +0.068 | +10.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 215 | -0.090 | +3.60€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 215 | -0.090 | +3.60€ | 1 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 7 | -0.058 | -1.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 7 | -0.058 | -1.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 99 | +0.054 | +25.68€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 99 | +0.054 | +25.68€ | 0 | 1 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 215 | -0.021 | +8.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 215 | -0.021 | +8.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 221 | -0.007 | +21.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 221 | -0.007 | +21.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 95 | +0.211 | +23.50€ | 0 | 1 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 95 | +0.211 | +23.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 63 | +0.192 | +6.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 63 | +0.192 | +6.79€ | 0 | 2 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 32 | +0.235 | +16.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 32 | +0.235 | +16.71€ | 0 | 0 |
| ✅ UPDOWN_OU_5M | 44 | -0.109 | -4.91€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#5min | 44 | -0.109 | -4.91€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 14 | +0.000 | -0.16€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 14 | +0.000 | -0.16€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 7 | -0.058 | -1.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 7 | -0.058 | -1.51€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 6 | +0.037 | +1.44€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 6 | +0.037 | +1.44€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 7 | -0.136 | -3.57€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 7 | -0.136 | -3.57€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 7 | +0.019 | +0.43€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 7 | +0.019 | +0.43€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 800 | +0.278 | +344.10€ | 0 | 1 |
| ✅ WEEKLY_PRICE#BTC | 238 | +0.192 | +2.25€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 246 | +0.238 | +50.84€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 316 | +0.371 | +291.01€ | 0 | 1 |