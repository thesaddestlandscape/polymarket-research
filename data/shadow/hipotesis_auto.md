# Hipótesis automáticas — 2026-08-08 21:11 UTC
_Generado por shadow_postmortem.py sobre 94580 resoluciones (PNL=+14023.02€)_

## Patrones causales activos

### BALLENAS_CONFIRMADAS_15M
- **PATRÓN** `py_entrada` < `0.475` → IC=+0.292 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.475 (IC base=+0.189)

- **PATRÓN** `banda_hit_calibrado` > `0.7006` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `banda_hit_calibrado` > 0.7006 (IC base=+0.189)

- **PATRÓN** `banda_z` > `10.624` → IC=+0.333 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `banda_z` > 10.624 (IC base=+0.189)

- **PATRÓN** `hora_utc` > `10.0` → IC=+0.224 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.189)

### BALLENAS_TARDIAS
- **PATRÓN** `restante_s_al_confirmar` < `78.75` → IC=+0.382 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `restante_s_al_confirmar` < 78.75 (IC base=+0.357)

### BALLENAS_TARDIAS#BTC#15min
- **PATRÓN** `restante_s_al_confirmar` < `78.75` → IC=+0.382 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `restante_s_al_confirmar` < 78.75 (IC base=+0.357)

### FAVORITO_CONFIRMADO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.196 (n=2277)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.185)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.188 (n=1673)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 11.0 (IC base=+0.185)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.325 (n=866)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.185)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=2786)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.185)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=970)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.184 (n=1195)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.331 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=2901)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.170)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.206 (n=375)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.200)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.203 (n=578)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.200)

- **PATRÓN** `py_entrada` > `0.605` → IC=+0.258 (n=561)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.605 (IC base=+0.200)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.216 (n=206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.352 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=746)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.194)

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

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.221 (n=507)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.343 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.202 (n=384)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.326 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.193)

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

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.230 (n=202)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.213)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.312 (n=366)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.213)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.215 (n=599)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.213)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.207 (n=591)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` < `0.325` → IC=+0.290 (n=394)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.325 (IC base=+0.201)

- **PATRÓN** `libro_liquidez` > `1588.1821` → IC=+0.204 (n=575)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1588.1821 (IC base=+0.201)

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
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.236 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.128)

- **PATRÓN** `restante_min` < `3.98` → IC=+0.173 (n=221)

  - _Acción_: Kelly boost +0.86€ cuando `restante_min` < 3.98 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.137 (n=502)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 9.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.142 (n=534)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 18.0 (IC base=+0.128)

- **PATRÓN** `profundidad_ratio_no` > `11.4` → IC=+0.162 (n=229)

  - _Acción_: Kelly boost +0.81€ cuando `profundidad_ratio_no` > 11.4 (IC base=+0.128)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.273 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.101)

- **PATRÓN** `restante_min` < `3.9` → IC=+0.149 (n=112)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` < 3.9 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.124 (n=267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 18.0 (IC base=+0.101)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.44` → IC=+0.171 (n=262)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` < 0.44 (IC base=+0.154)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.205 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` < 4.16 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.167 (n=250)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 9.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.158 (n=267)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 18.0 (IC base=+0.154)

- **PATRÓN** `profundidad_ratio_no` > `26.5` → IC=+0.209 (n=84)

  - _Acción_: Kelly boost +1.00€ cuando `profundidad_ratio_no` > 26.5 (IC base=+0.154)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.123 (n=2808)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 5.0 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `0.4559` → IC=+0.130 (n=330)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.4559 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.821` → IC=+0.203 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.821 (IC base=+0.112)

- **PATRÓN** `libro_liquidez` > `2838.6173` → IC=+0.124 (n=1211)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 2838.6173 (IC base=+0.112)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.122 (n=1521)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` > 0.0103 (IC base=+0.093)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.142 (n=426)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0044 (IC base=+0.106)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.131 (n=569)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 8.0 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` > `0.433` → IC=+0.172 (n=59)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.433 (IC base=+0.106)

- **PATRÓN** `dist_vwap_pct` < `0.1011` → IC=+0.133 (n=292)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1011 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.632` → IC=+0.197 (n=74)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 12.632 (IC base=+0.106)

- **PATRÓN** `libro_liquidez` > `10145.3808` → IC=+0.154 (n=281)

  - _Acción_: Kelly boost +0.77€ cuando `libro_liquidez` > 10145.3808 (IC base=+0.106)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.169 (n=158)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0043 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.128 (n=428)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 8.0 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.9129` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.9129 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.1625` → IC=+0.146 (n=125)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1625 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.728` → IC=+0.223 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.728 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `4319.3853` → IC=+0.164 (n=141)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 4319.3853 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.54` → IC=+0.156 (n=152)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 6.54 (IC base=+0.068)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `8.186` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.186
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=625)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.309` → IC=+0.224 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.309 (IC base=+0.097)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.149 (n=363)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 7.0 (IC base=+0.092)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_h` > `0.0204` → IC=+0.144 (n=346)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0204 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.148 (n=765)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 6.0 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` > `0.6566` → IC=+0.185 (n=71)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.6566 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.453` → IC=+0.253 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.453 (IC base=+0.140)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.146 (n=951)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0084 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.163 (n=324)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 18.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.151 (n=356)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 6.0 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.3403` → IC=+0.189 (n=120)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.3403 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.444` → IC=+0.135 (n=94)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 7.444 (IC base=+0.137)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.124 (n=586)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.137)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.189 (n=2281)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0066 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.105` → IC=+0.281 (n=39)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.105 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.157 (n=3203)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.2919` → IC=+0.171 (n=815)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.2919 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.038` → IC=+0.247 (n=1300)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.038 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `2038.84` → IC=+0.152 (n=3066)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2038.84 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.0039` → IC=+0.164 (n=3136)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0039 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2747` → IC=+0.202 (n=206)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.2747 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.157 (n=1065)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.155 (n=1188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 6.0 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6092` → IC=+0.152 (n=323)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.6092 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.186` → IC=+0.172 (n=517)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 8.186 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.845` → IC=+0.148 (n=2595)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 2.845 (IC base=+0.148)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.142 (n=252)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0026 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.149 (n=411)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 11.0 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.4932` → IC=+0.146 (n=77)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.4932 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.349` → IC=+0.190 (n=111)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 12.349 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `11064.4064` → IC=+0.149 (n=314)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 11064.4064 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.309` → IC=+0.171 (n=290)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` > 4.309 (IC base=+0.108)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.157 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0072 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.122 (n=556)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 15.0 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.1183` → IC=+0.140 (n=295)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1183 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.305` → IC=+0.166 (n=288)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 4.305 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `7639.1484` → IC=+0.137 (n=348)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 7639.1484 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.483` → IC=+0.167 (n=169)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 9.483 (IC base=+0.073)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.1914` → IC=-0.237 (n=17)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1914
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

- **PATRÓN** `sigma_h` > `0.011` → IC=+0.200 (n=238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.011 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.154 (n=518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 11.0 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` > `0.194` → IC=+0.148 (n=285)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.194 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.331` → IC=+0.266 (n=323)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.331 (IC base=+0.125)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=682)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `2302.15` → IC=+0.174 (n=418)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2302.15 (IC base=+0.125)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.223 (n=762)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.214 (n=767)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.1226` → IC=+0.221 (n=378)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1226 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.081` → IC=+0.331 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.081 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=705)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `3147.1402` → IC=+0.197 (n=232)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3147.1402 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.245 (n=709)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.229)

- **PATRÓN** `drift_60min` |x|≤ `0.4402` → IC=+0.313 (n=73)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4402 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.257 (n=545)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.229)

- **PATRÓN** `dist_vwap_pct` > `0.8064` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8064 (IC base=+0.229)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.323` → IC=+0.255 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.323 (IC base=+0.229)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.245 (n=712)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.229)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0049` → IC=+0.318 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0049 (IC base=+0.272)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.290 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.272)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.300 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.272)

- **PATRÓN** `dist_vwap_pct` < `0.0931` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0931 (IC base=+0.272)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.958` → IC=+0.329 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.958 (IC base=+0.272)

- **PATRÓN** `libro_liquidez` > `1144.6448` → IC=+0.276 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1144.6448 (IC base=+0.272)

- **PATRÓN** `sigma_h` > `0.0033` → IC=+0.209 (n=318)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0033 (IC base=+0.202)

- **PATRÓN** `drift_60min` |x|≤ `0.0954` → IC=+0.266 (n=105)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0954 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.291 (n=108)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.1881` → IC=+0.185 (n=268)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.1881 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.509` → IC=+0.222 (n=282)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.509 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `1168.4343` → IC=+0.213 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1168.4343 (IC base=+0.202)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.182 (n=61)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0031 (IC base=+0.159)

- **PATRÓN** `drift_60min` |x|≤ `0.0477` → IC=+0.227 (n=20)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0477 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.198 (n=41)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 12.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.167 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 5.0 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.275` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.275 (IC base=+0.159)

- **PATRÓN** `libro_liquidez` > `9297.5026` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 9297.5026 (IC base=+0.159)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.300 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0028 (IC base=+0.152)

- **PATRÓN** `drift_60min` |x|≤ `0.1015` → IC=+0.184 (n=17)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.92€ cuando `drift_60min` |x|≤ 0.1015 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.250 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.721` → IC=+0.241 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.721 (IC base=+0.152)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.235 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.068)

- **PATRÓN** `libro_liquidez` > `1626.1169` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1626.1169 (IC base=+0.068)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.290 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0077 (IC base=+0.283)

- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.300 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.283)

- **PATRÓN** `drift_60min` |x|≤ `0.1306` → IC=+0.380 (n=23)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1306 (IC base=+0.283)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.278 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.283)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.312 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.283)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.001` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.001 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `2838.0713` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2838.0713 (IC base=+0.283)

### GBM_LATE_15M_PYCONFIRMADO
- **FILTRO** `sigma_h` < `0.0071` → IC=-0.277 (n=119)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0071
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=120)

- **FILTRO** `hora_utc` < `7.0` → IC=-0.234 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=162)

- **FILTRO** `hora_utc` > `18.0` → IC=-0.161 (n=54)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.131 (n=185)

- **FILTRO** `dist_vwap_pct` > `0.1621` → IC=-0.280 (n=57)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1621
  - _Potencial_: sin este filtro IC_bueno=-0.092 (n=182)

- **FILTRO** `sigma_ewma_delta_pct` > `9.967` → IC=-0.227 (n=31)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.967
  - _Potencial_: sin este filtro IC_bueno=-0.124 (n=208)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.321 (n=65)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0047 (IC base=+0.278)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.328 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` > `0.361` → IC=+0.300 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.361 (IC base=+0.278)

- **PATRÓN** `dist_vwap_pct` < `0.0981` → IC=+0.280 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0981 (IC base=+0.278)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.805` → IC=+0.375 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.805 (IC base=+0.278)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.296 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.278)

- **PATRÓN** `libro_liquidez` > `2074.8051` → IC=+0.279 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2074.8051 (IC base=+0.278)

### GBM_LATE_15M_PYCONFIRMADO#ETH#15min
- **FILTRO** `sigma_h` > `0.0047` → IC=-0.368 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0047
  - _Potencial_: sin este filtro IC_bueno=-0.257 (n=68)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.386 (n=33)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.286 (n=101)

- **FILTRO** `hora_utc` < `19.0` → IC=-0.320 (n=98)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=36)

- **FILTRO** `hora_utc` > `5.0` → IC=-0.342 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.244 (n=41)

- **FILTRO** `dist_vwap_pct` > `0.1622` → IC=-0.360 (n=41)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.1622
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=93)

- **FILTRO** `sigma_ewma_delta_pct` < `9.698` → IC=-0.329 (n=109)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 9.698
  - _Potencial_: sin este filtro IC_bueno=-0.241 (n=25)

- **FILTRO** `libro_liquidez` < `4648.6111` → IC=-0.343 (n=100)

  - _Acción_: SKIP cuando `libro_liquidez` < 4648.6111
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=34)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.353 (n=66)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.351)

- **PATRÓN** `sigma_h` > `0.0026` → IC=+0.370 (n=75)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0026 (IC base=+0.351)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.438 (n=30)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.351)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.352 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.351)

- **PATRÓN** `dist_vwap_pct` > `0.1852` → IC=+0.360 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1852 (IC base=+0.351)

- **PATRÓN** `dist_vwap_pct` < `0.1064` → IC=+0.357 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1064 (IC base=+0.351)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.703` → IC=+0.409 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.703 (IC base=+0.351)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.623` → IC=+0.370 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.623 (IC base=+0.351)

- **PATRÓN** `libro_liquidez` > `3648.3953` → IC=+0.389 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3648.3953 (IC base=+0.351)

### GBM_LATE_15M_PYCONFIRMADO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0114` → IC=+0.250 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0114 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.261 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.208 (n=70)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 19.0 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.5944` → IC=+0.273 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5944 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` < `0.1711` → IC=+0.214 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1711 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.795` → IC=+0.458 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.795 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2598.3232` → IC=+0.250 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2598.3232 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0201` → IC=+0.233 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0201 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.759` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.759 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `1928.5167` → IC=+0.198 (n=61)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 1928.5167 (IC base=+0.163)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.126 (n=2296)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` > 0.0069 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.03` → IC=+0.214 (n=1252)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.03 (IC base=+0.098)

- **PATRÓN** `drift_60min` |x|≤ `0.0885` → IC=+0.164 (n=114)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.82€ cuando `drift_60min` |x|≤ 0.0885 (IC base=+0.111)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.131 (n=1216)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.595` → IC=+0.121 (n=2863)

  - _Acción_: Kelly boost +0.60€ cuando `sigma_ewma_delta_pct` < 3.595 (IC base=+0.111)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `10.972` → IC=+0.169 (n=137)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 10.972 (IC base=+0.063)

- **PATRÓN** `libro_liquidez` > `8514.264` → IC=+0.125 (n=294)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 8514.264 (IC base=+0.063)

- **PATRÓN** `drift_60min` |x|≤ `0.0674` → IC=+0.167 (n=19)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.0674 (IC base=+0.056)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `12.755` → IC=+0.154 (n=102)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 12.755 (IC base=+0.055)

- **PATRÓN** `libro_liquidez` > `8931.8205` → IC=+0.158 (n=220)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 8931.8205 (IC base=+0.055)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.068` → IC=+0.273 (n=152)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.068 (IC base=+0.041)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.164 (n=865)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0068 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.165 (n=802)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 7.0 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.6667` → IC=+0.206 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6667 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.597` → IC=+0.284 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.597 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=742)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.186 (n=942)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0064 (IC base=+0.177)

- **PATRÓN** `drift_60min` |x|≤ `0.395` → IC=+0.234 (n=77)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.395 (IC base=+0.177)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.199 (n=648)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 12.0 (IC base=+0.177)

- **PATRÓN** `dist_vwap_pct` > `0.7518` → IC=+0.278 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7518 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=835)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.177)

### GBM_LATE_5M
- **FILTRO** `sigma_h` < `0.0048` → IC=-0.310 (n=77)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0048
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=232)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.241 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.145 (n=91)

- **FILTRO** `dist_vwap_pct` > `0.5825` → IC=-0.315 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.5825
  - _Potencial_: sin este filtro IC_bueno=-0.203 (n=284)

- **FILTRO** `sigma_ewma_delta_pct` < `9.28` → IC=-0.218 (n=271)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 9.28
  - _Potencial_: sin este filtro IC_bueno=-0.175 (n=38)

- **FILTRO** `sigma_ewma_delta_pct` > `3.582` → IC=-0.236 (n=104)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.582
  - _Potencial_: sin este filtro IC_bueno=-0.201 (n=205)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_h` < `0.0035` → IC=-0.382 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=32)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.333 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=18)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.351 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.262 (n=19)

- **FILTRO** `dist_vwap_pct` < `0.2327` → IC=-0.339 (n=54)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2327
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=10)

- **FILTRO** `sigma_ewma_delta_pct` < `8.938` → IC=-0.346 (n=50)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 8.938
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=14)

- **FILTRO** `libro_liquidez` < `15621.2697` → IC=-0.382 (n=32)

  - _Acción_: SKIP cuando `libro_liquidez` < 15621.2697
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=32)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.193 (n=86)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0055 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.126 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 13.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `13.0` → IC=+0.140 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 13.0 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.1412` → IC=+0.162 (n=72)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.1412 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.3638` → IC=+0.133 (n=205)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.3638 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.005` → IC=+0.191 (n=40)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 12.005 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.38` → IC=+0.139 (n=178)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 7.38 (IC base=+0.124)

### GBM_LATE_5M#ETH#5min
- **FILTRO** `sigma_h` > `0.0052` → IC=-0.375 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0052
  - _Potencial_: sin este filtro IC_bueno=-0.235 (n=32)

- **FILTRO** `sigma_h` < `0.0038` → IC=-0.382 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.276 (n=47)

- **FILTRO** `sigma_ewma_delta_pct` < `5.488` → IC=-0.311 (n=51)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 5.488
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=11)

- **FILTRO** `libro_liquidez` < `4551.0427` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `libro_liquidez` < 4551.0427
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=31)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.145 (n=29)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 14.0 (IC base=+0.064)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.282 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

- **FILTRO** `sigma_h` < `0.0095` → IC=-0.243 (n=99)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0095
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=34)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.375 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=95)

- **FILTRO** `dist_vwap_pct` < `0.6756` → IC=-0.236 (n=127)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.6756
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

- **FILTRO** `dist_vwap_pct` > `0.2447` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.2447
  - _Potencial_: sin este filtro IC_bueno=-0.218 (n=108)

- **FILTRO** `sigma_ewma_delta_pct` < `6.996` → IC=-0.241 (n=106)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 6.996
  - _Potencial_: sin este filtro IC_bueno=-0.190 (n=27)

- **FILTRO** `sigma_ewma_delta_pct` > `3.6` → IC=-0.264 (n=53)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.6
  - _Potencial_: sin este filtro IC_bueno=-0.207 (n=80)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.273 (n=42)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=91)

- **FILTRO** `libro_liquidez` < `2043.8058` → IC=-0.271 (n=33)

  - _Acción_: SKIP cuando `libro_liquidez` < 2043.8058
  - _Potencial_: sin este filtro IC_bueno=-0.216 (n=100)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.463` → IC=+0.167 (n=76)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 6.463 (IC base=+0.011)

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

- **PATRÓN** `sigma_ewma_delta_pct` > `5.949` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 5.949 (IC base=+0.009)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `dist_vwap_pct` < `0.1725` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1725
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=19)

- **FILTRO** `sigma_h` > `0.0046` → IC=-0.179 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0046
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0031 (IC base=+0.028)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` < `5.134` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 5.134
  - _Potencial_: sin este filtro IC_bueno=+0.267 (n=28)

- **FILTRO** `sigma_h` > `0.0084` → IC=-0.333 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0084
  - _Potencial_: sin este filtro IC_bueno=-0.265 (n=32)

- **FILTRO** `hora_utc` < `18.0` → IC=-0.294 (n=32)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.278 (n=16)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.333 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.188 (n=14)

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

- **FILTRO** `hora_utc` < `18.0` → IC=-0.202 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.184 (n=17)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.261 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.214 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=-0.054)

### GBM_LATE_60M_FADE
- **FILTRO** `sigma_h` > `0.0022` → IC=-0.351 (n=45)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0022
  - _Potencial_: sin este filtro IC_bueno=-0.333 (n=16)

- **FILTRO** `sigma_h` < `0.0035` → IC=-0.406 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=31)

- **FILTRO** `drift_60min` |x|> `0.1319` → IC=-0.403 (n=29)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1319
  - _Potencial_: sin este filtro IC_bueno=-0.281 (n=30)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.423 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=24)

- **FILTRO** `dist_vwap_pct` < `0.0718` → IC=-0.357 (n=47)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.0718
  - _Potencial_: sin este filtro IC_bueno=-0.312 (n=14)

- **FILTRO** `sigma_ewma_delta_pct` < `3.163` → IC=-0.351 (n=45)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 3.163
  - _Potencial_: sin este filtro IC_bueno=-0.333 (n=16)

- **FILTRO** `sigma_ewma_delta_pct` > `2.588` → IC=-0.357 (n=19)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.588
  - _Potencial_: sin este filtro IC_bueno=-0.341 (n=42)

- **FILTRO** `libro_liquidez` < `2228.186` → IC=-0.357 (n=40)

  - _Acción_: SKIP cuando `libro_liquidez` < 2228.186
  - _Potencial_: sin este filtro IC_bueno=-0.326 (n=21)

- **FILTRO** `sigma_h` > `0.0024` → IC=-0.316 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0024
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.262 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=-0.231 (n=24)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.287 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=19)

- **FILTRO** `dist_vwap_pct` < `0.2298` → IC=-0.275 (n=38)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2298
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=26)

- **FILTRO** `dist_vwap_pct` > `0.3507` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3507
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=47)

- **FILTRO** `sigma_ewma_delta_pct` < `5.949` → IC=-0.267 (n=41)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 5.949
  - _Potencial_: sin este filtro IC_bueno=-0.220 (n=23)

- **FILTRO** `sigma_ewma_delta_pct` > `4.073` → IC=-0.274 (n=29)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.073
  - _Potencial_: sin este filtro IC_bueno=-0.230 (n=35)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=43)

- **FILTRO** `libro_liquidez` < `3137.1284` → IC=-0.295 (n=42)

  - _Acción_: SKIP cuando `libro_liquidez` < 3137.1284
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=22)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` > `0.0022` → IC=-0.342 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0022
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.278 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `dist_vwap_pct` < `0.2294` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.2294
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=7)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_ewma_delta_pct` < `1.863` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 1.863
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=3)

### GBM_LATE_60M_PYCONFIRMADO
- **PATRÓN** `sigma_ewma_delta_pct` > `4.44` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 4.44 (IC base=+0.095)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.136 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0031 (IC base=+0.000)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.152 (n=21)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 15.0 (IC base=+0.000)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `sigma_h` > `0.006` → IC=-0.200 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.006
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **FILTRO** `hora_utc` < `14.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 14.0
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=10)

### LEADLAG_BTC_XRP_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=168)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=168)

### LIQUIDACIONES_15M
- **FILTRO** `liq_usd_total` < `2879.67` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `liq_usd_total` < 2879.67
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

- **FILTRO** `hora_utc` < `16.0` → IC=-0.155 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=22)

- **FILTRO** `liq_usd_total` < `1743.17` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `liq_usd_total` < 1743.17
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=24)

- **FILTRO** `hora_utc` < `11.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=32)

- **FILTRO** `py_entrada` > `0.485` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.485
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=20)

### LIQUIDACIONES_5M
- **FILTRO** `liq_usd_total` < `5158.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `liq_usd_total` < 5158.0
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=16)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

- **FILTRO** `libro_liquidez` < `12208.6168` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `libro_liquidez` < 12208.6168
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### LIQUIDACIONES_60M
- **FILTRO** `hora_utc` < `15.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=18)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` > 0.505 (IC base=+0.045)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.250 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.000)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=188)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `total_vol_5m` < `197.886` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `total_vol_5m` < 197.886 (IC base=+0.031)

### ORDER_FLOW_5M#BTC#5min
- **FILTRO** `delta_ratio` |x|≤ `0.3925` → IC=-0.180 (n=23)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.3925
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=80)

### ORDER_FLOW_5M#DOGE#5min
- **FILTRO** `total_vol_5m` > `1109767.0` → IC=-0.274 (n=29)

  - _Acción_: SKIP cuando `total_vol_5m` > 1109767.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=64)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `hora_utc` > `3.0` → IC=+0.175 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 3.0 (IC base=+0.071)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.151 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` < 4.0 (IC base=+0.071)

### ORDER_FLOW_5M#XRP#5min
- **FILTRO** `delta_ratio` |x|≤ `0.4307` → IC=-0.136 (n=20)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.4307
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=45)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` > `0.0072` → IC=-0.312 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

- **FILTRO** `T_h` < `144.7465` → IC=-0.439 (n=47)

  - _Acción_: SKIP cuando `T_h` < 144.7465
  - _Potencial_: sin este filtro IC_bueno=-0.321 (n=26)

- **FILTRO** `pct_vs_K` |x|> `5.1929` → IC=-0.462 (n=24)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 5.1929
  - _Potencial_: sin este filtro IC_bueno=-0.363 (n=49)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0077` → IC=-0.329 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

- **FILTRO** `T_h` > `87.9981` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `T_h` > 87.9981
  - _Potencial_: sin este filtro IC_bueno=-0.400 (n=8)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### STREAK_FADE_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=105)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### STREAK_FADE_15M#SOL#15min
- **PATRÓN** `streak_len` < `4.0` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `streak_len` < 4.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.485 (IC base=+0.100)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `467605.9` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `volumen_racha` > 467605.9
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=28)

- **PATRÓN** `volumen_racha` < `641424.8` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `volumen_racha` < 641424.8 (IC base=+0.054)

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
- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

- **FILTRO** `libro_liquidez` < `6441.4408` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 6441.4408
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

### STREAK_MOM_5M
- **FILTRO** `py_entrada` < `0.5` → IC=-0.250 (n=46)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=98)

- **FILTRO** `streak_len` > `4.0` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `streak_len` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=120)

- **FILTRO** `libro_liquidez` < `3352.7321` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `libro_liquidez` < 3352.7321
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=103)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=76)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.028 (n=89)

### STREAK_MOM_5M#ETH#5min
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

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=+0.005 (n=99)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=104)

### UPDOWN_GBM#15min
- **PATRÓN** `ibs_15` > `0.5954` → IC=+0.177 (n=682)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.88€ cuando `ibs_15` > 0.5954 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.1672` → IC=+0.159 (n=253)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1672 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` < `0.6202` → IC=+0.129 (n=475)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.6202 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.417` → IC=+0.163 (n=176)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.417 (IC base=+0.063)

- **PATRÓN** `libro_liquidez` > `9956.4716` → IC=+0.134 (n=200)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 9956.4716 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.9312` → IC=+0.171 (n=68)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.9312 (IC base=+0.080)

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

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0182` → IC=-0.208 (n=22)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0182
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=24)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.2291` → IC=-0.265 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2291
  - _Potencial_: sin este filtro IC_bueno=+0.088 (n=49)

- **PATRÓN** `drift_60min` |x|≤ `0.1888` → IC=+0.147 (n=284)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1888 (IC base=+0.100)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0644` → IC=+0.134 (n=323)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0644 (IC base=+0.100)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.175 (n=192)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 14.0 (IC base=+0.100)

- **PATRÓN** `ibs_15` > `0.6354` → IC=+0.219 (n=283)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6354 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.2571` → IC=+0.237 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2571 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `25.023` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 25.023 (IC base=+0.100)

- **PATRÓN** `libro_liquidez` > `11672.79` → IC=+0.161 (n=113)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11672.79 (IC base=+0.100)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `ibs_15` > `0.6644` → IC=+0.192 (n=219)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.6644 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.056` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 7.056 (IC base=+0.059)

- **PATRÓN** `sigma_h` < `0.0049` → IC=+0.159 (n=171)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0049 (IC base=+0.081)

- **PATRÓN** `dist_vwap_pct` > `0.9222` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9222 (IC base=+0.081)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `sigma_h` > `0.0204` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0204
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=35)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1932` → IC=-0.167 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1932
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **PATRÓN** `drift_15min` |x|≤ `0.4618` → IC=+0.139 (n=81)

  - _Acción_: Kelly boost +0.69€ cuando `drift_15min` |x|≤ 0.4618 (IC base=+0.069)

### UPDOWN_GBM#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0455` → IC=-0.167 (n=25)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0455
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=13)

- **FILTRO** `drift_15min` |x|> `0.4751` → IC=-0.237 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4751
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.130 (n=160)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0074 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.141 (n=179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 12.0 (IC base=+0.116)

- **PATRÓN** `ibs_15` < `0.0448` → IC=+0.143 (n=82)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.71€ cuando `ibs_15` < 0.0448 (IC base=+0.116)

- **PATRÓN** `libro_liquidez` > `3035.0793` → IC=+0.158 (n=71)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3035.0793 (IC base=+0.116)

### UPDOWN_GBM_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.158 (n=1061)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0055 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.0663` → IC=+0.175 (n=340)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0663 (IC base=+0.148)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1937` → IC=+0.138 (n=352)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio_macro` |x|> 0.1937 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.138 (n=525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 12.0 (IC base=+0.148)

- **PATRÓN** `ibs_15` > `0.5385` → IC=+0.220 (n=772)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5385 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.2413` → IC=+0.139 (n=267)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.2413 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.5741` → IC=+0.120 (n=725)

  - _Acción_: Kelly boost +0.60€ cuando `dist_vwap_pct` < 0.5741 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.258` → IC=+0.189 (n=448)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 5.258 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `2545.0995` → IC=+0.133 (n=772)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2545.0995 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.184 (n=644)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0068 (IC base=+0.175)

- **PATRÓN** `drift_60min` |x|≤ `0.2167` → IC=+0.169 (n=599)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2167 (IC base=+0.175)

- **PATRÓN** `drift_15min` |x|≤ `0.4196` → IC=+0.198 (n=299)

  - _Acción_: Kelly boost +0.99€ cuando `drift_15min` |x|≤ 0.4196 (IC base=+0.175)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.169 (n=618)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 12.0 (IC base=+0.175)

- **PATRÓN** `ibs_15` < `0.3269` → IC=+0.247 (n=790)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3269 (IC base=+0.175)

- **PATRÓN** `dist_vwap_pct` > `0.2003` → IC=+0.191 (n=208)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.2003 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.539` → IC=+0.194 (n=119)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 19.539 (IC base=+0.175)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.443` → IC=+0.188 (n=885)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 7.443 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=921)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `3994.029` → IC=+0.174 (n=299)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3994.029 (IC base=+0.175)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `ibs_15` < `0.7488` → IC=-0.139 (n=59)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.7488
  - _Potencial_: sin este filtro IC_bueno=+0.271 (n=120)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.164 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0037 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0026` → IC=+0.147 (n=185)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0026 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1123` → IC=+0.152 (n=90)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1123 (IC base=+0.148)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0951` → IC=+0.180 (n=120)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.0951 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.175 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 16.0 (IC base=+0.148)

- **PATRÓN** `ibs_15` > `0.7488` → IC=+0.271 (n=120)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7488 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.2256` → IC=+0.203 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2256 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.379` → IC=+0.182 (n=83)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.379 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `11198.676` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 11198.676 (IC base=+0.148)

- **PATRÓN** `drift_15min` |x|≤ `0.5515` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `drift_15min` |x|≤ 0.5515 (IC base=-0.079)

- **PATRÓN** `ibs_15` < `0.5537` → IC=+0.139 (n=34)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.69€ cuando `ibs_15` < 0.5537 (IC base=-0.079)

- **PATRÓN** `libro_liquidez` > `9476.9221` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 9476.9221 (IC base=-0.079)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.5405` → IC=-0.143 (n=82)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5405
  - _Potencial_: sin este filtro IC_bueno=+0.202 (n=169)

- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.182 (n=86)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0064 (IC base=+0.125)

- **PATRÓN** `drift_60min` |x|≤ `0.045` → IC=+0.162 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.045 (IC base=+0.125)

- **PATRÓN** `ibs_15` > `0.7007` → IC=+0.289 (n=126)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7007 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.922` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 7.922 (IC base=+0.125)

- **PATRÓN** `libro_liquidez` > `7672.3115` → IC=+0.133 (n=126)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 7672.3115 (IC base=+0.125)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.303 (n=145)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.270)

- **PATRÓN** `drift_60min` |x|≤ `0.1029` → IC=+0.370 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1029 (IC base=+0.270)

- **PATRÓN** `drift_15min` |x|≤ `0.4473` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4473 (IC base=+0.270)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.289 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.270)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.271 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.270)

- **PATRÓN** `ibs_15` < `0.0419` → IC=+0.413 (n=44)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.0419 (IC base=+0.270)

- **PATRÓN** `dist_vwap_pct` > `0.2534` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2534 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.363` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.363 (IC base=+0.270)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.671` → IC=+0.288 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.671 (IC base=+0.270)

### UPDOWN_GBM_15M_TARDIO#SOL#15min
- **FILTRO** `ibs_15` > `0.5507` → IC=-0.179 (n=82)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.5507
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=250)

- **FILTRO** `sigma_ewma_delta_pct` > `10.168` → IC=-0.130 (n=52)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 10.168
  - _Potencial_: sin este filtro IC_bueno=+0.121 (n=280)

- **PATRÓN** `sigma_h` > `0.0096` → IC=+0.143 (n=68)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0096 (IC base=+0.107)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1216` → IC=+0.143 (n=96)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio_macro` |x|> 0.1216 (IC base=+0.107)

- **PATRÓN** `hora_utc` > `20.0` → IC=+0.179 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 20.0 (IC base=+0.107)

- **PATRÓN** `ibs_15` > `0.7419` → IC=+0.296 (n=96)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7419 (IC base=+0.107)

- **PATRÓN** `dist_vwap_pct` < `0.1333` → IC=+0.145 (n=122)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1333 (IC base=+0.107)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.453` → IC=+0.261 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.453 (IC base=+0.107)

- **PATRÓN** `libro_liquidez` > `2689.6584` → IC=+0.144 (n=144)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2689.6584 (IC base=+0.107)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.162 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0077 (IC base=+0.103)

- **PATRÓN** `drift_15min` |x|≤ `0.4799` → IC=+0.143 (n=110)

  - _Acción_: Kelly boost +0.71€ cuando `drift_15min` |x|≤ 0.4799 (IC base=+0.103)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.170 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 5.0 (IC base=+0.103)

- **PATRÓN** `ibs_15` < `0.4444` → IC=+0.189 (n=223)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.94€ cuando `ibs_15` < 0.4444 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.798` → IC=+0.125 (n=254)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 6.798 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `3830.5978` → IC=+0.152 (n=113)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3830.5978 (IC base=+0.103)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.211 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0068 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.232 (n=80)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.170)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2268` → IC=+0.177 (n=60)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.2268 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.181 (n=89)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 14.0 (IC base=+0.170)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.214 (n=180)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.3464` → IC=+0.241 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3464 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` < `0.0823` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.0823 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.559` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 6.559 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.694` → IC=+0.161 (n=166)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 10.694 (IC base=+0.170)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=165)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.170)

- **PATRÓN** `libro_liquidez` > `2778.5195` → IC=+0.152 (n=159)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2778.5195 (IC base=+0.170)

- **PATRÓN** `sigma_h` < `0.0069` → IC=+0.223 (n=153)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0069 (IC base=+0.211)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.213 (n=305)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0088 (IC base=+0.211)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1689` → IC=+0.185 (n=195)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio_macro` |x|> 0.1689 (IC base=+0.211)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.238 (n=204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.211)

- **PATRÓN** `ibs_15` < `0.3571` → IC=+0.267 (n=256)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3571 (IC base=+0.211)

- **PATRÓN** `dist_vwap_pct` > `0.7875` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7875 (IC base=+0.211)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.21` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 20.21 (IC base=+0.211)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.212 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `2792.8241` → IC=+0.191 (n=260)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2792.8241 (IC base=+0.211)

### UPDOWN_OU_5M
- **FILTRO** `pct_spot_vs_ref` |x|> `0.2498` → IC=-0.469 (n=30)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2498
  - _Potencial_: sin este filtro IC_bueno=-0.205 (n=59)

- **FILTRO** `sigma_h` > `0.0062` → IC=-0.382 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=-0.060 (n=23)

- **FILTRO** `drift_60min` |x|> `0.6403` → IC=-0.458 (n=22)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.6403
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=67)

- **FILTRO** `drift_15min` |x|> `1.9892` → IC=-0.458 (n=22)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.9892
  - _Potencial_: sin este filtro IC_bueno=-0.239 (n=67)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1524` → IC=-0.304 (n=44)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1524
  - _Potencial_: sin este filtro IC_bueno=-0.283 (n=44)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.2043` → IC=-0.246 (n=61)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2043
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=187)

- **FILTRO** `sigma_h` < `0.0072` → IC=-0.172 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0072
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=186)

- **FILTRO** `drift_60min` |x|> `0.0851` → IC=-0.136 (n=185)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0851
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=63)

- **FILTRO** `drift_15min` |x|> `1.0429` → IC=-0.182 (n=61)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0429
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=187)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1556` → IC=-0.143 (n=124)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1556
  - _Potencial_: sin este filtro IC_bueno=-0.111 (n=124)

### UPDOWN_OU_5M#BNB#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1548` → IC=-0.188 (n=30)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1548
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=16)

- **FILTRO** `drift_60min` |x|> `0.1214` → IC=-0.208 (n=22)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1214
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=24)

- **FILTRO** `drift_15min` |x|> `0.6815` → IC=-0.147 (n=15)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.6815
  - _Potencial_: sin este filtro IC_bueno=-0.106 (n=31)

### UPDOWN_OU_5M#DOGE#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1647` → IC=-0.175 (n=38)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1647
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **FILTRO** `drift_15min` |x|> `0.648` → IC=-0.204 (n=25)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.648
  - _Potencial_: sin este filtro IC_bueno=-0.017 (n=27)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.271` → IC=-0.167 (n=34)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.271
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=18)

### UPDOWN_OU_5M#SOL#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1359` → IC=-0.159 (n=42)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1359
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **FILTRO** `sigma_h` > `0.0064` → IC=-0.136 (n=42)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0064
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=15)

- **FILTRO** `drift_60min` |x|> `0.0813` → IC=-0.175 (n=38)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.0813
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=19)

### UPDOWN_OU_5M#XRP#5min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1588` → IC=-0.324 (n=15)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1588
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `sigma_h` > `0.0079` → IC=-0.289 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0079
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=6)

- **FILTRO** `drift_60min` |x|> `0.2585` → IC=-0.324 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2585
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `drift_15min` |x|> `0.5978` → IC=-0.324 (n=15)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5978
  - _Potencial_: sin este filtro IC_bueno=-0.200 (n=8)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1972` → IC=-0.289 (n=17)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1972
  - _Potencial_: sin este filtro IC_bueno=-0.250 (n=6)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.2146` → IC=-0.265 (n=15)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2146
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=47)

- **FILTRO** `drift_60min` |x|> `0.5642` → IC=-0.265 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5642
  - _Potencial_: sin este filtro IC_bueno=-0.051 (n=47)

- **FILTRO** `drift_15min` |x|> `0.7304` → IC=-0.188 (n=30)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.7304
  - _Potencial_: sin este filtro IC_bueno=-0.029 (n=32)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1242` → IC=-0.167 (n=31)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1242
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=31)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `146.1402` → IC=+0.457 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1402 (IC base=+0.351)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `87.9969` → IC=+0.284 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 87.9969 (IC base=+0.259)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.269 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.259)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9838` → IC=+0.317 (n=118)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9838 (IC base=+0.291)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `135.9824` → IC=+0.456 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 135.9824 (IC base=+0.441)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5954 sube el IC de +0.063 a +0.177 en UPDOWN_GBM#15min (n=682). Ya aplicado como kelly_boost=+0.88€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.6354 sube el IC de +0.100 a +0.219 en UPDOWN_GBM#BTC#15min (n=283). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6644 sube el IC de +0.059 a +0.192 en UPDOWN_GBM#ETH#15min (n=219). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5385 sube el IC de +0.148 a +0.220 en UPDOWN_GBM_15M_TARDIO (n=772). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3269 sube el IC de +0.175 a +0.247 en UPDOWN_GBM_15M_TARDIO (n=790). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7488 sube el IC de +0.148 a +0.271 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=120). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.7007 sube el IC de +0.125 a +0.289 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=126). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.0419 sube el IC de +0.270 a +0.413 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=44). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.7419 sube el IC de +0.107 a +0.296 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=96). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.4444 sube el IC de +0.103 a +0.189 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=223). Ya aplicado como kelly_boost=+0.94€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.170 a +0.214 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=180). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3571 sube el IC de +0.211 a +0.267 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=256). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO#XRP#15min` — IC=+0.134 n=39. Faltan ~1 resoluciones para umbral n≥40. ETA: ~1h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1791 | +0.046 | -28.02€ | 0 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1791 | +0.046 | -28.02€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 821 | +0.021 | -29.99€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 821 | +0.021 | -29.99€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 639 | +0.063 | -17.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 639 | +0.063 | -17.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 312 | +0.073 | +19.97€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 312 | +0.073 | +19.97€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 2259 | -0.072 | -464.06€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS#15min | 414 | +0.209 | -44.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 1845 | -0.136 | -420.01€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#BNB | 369 | -0.290 | -102.08€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#BNB#5min | 369 | -0.290 | -102.08€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 414 | +0.209 | -44.05€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 414 | +0.209 | -44.05€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS#DOGE | 280 | -0.131 | -44.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 280 | -0.131 | -44.09€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 411 | +0.004 | -16.18€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 411 | +0.004 | -16.18€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 393 | -0.161 | -65.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 393 | -0.161 | -65.40€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 392 | -0.112 | -192.26€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 392 | -0.112 | -192.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 25501 | +0.119 | -604.69€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 6202 | +0.195 | -112.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 446 | +0.047 | -43.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 16960 | +0.091 | -502.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 1893 | +0.140 | +53.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 2709 | +0.085 | -136.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 11 | +0.021 | -0.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | +0.018 | +2.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 2693 | +0.086 | -138.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 5505 | +0.132 | -77.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1946 | +0.182 | -102.66€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 143 | +0.052 | -15.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 2699 | +0.096 | -24.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 717 | +0.148 | +65.69€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 2708 | +0.077 | -158.18€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 15 | +0.243 | +10.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 2692 | +0.076 | -170.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 5947 | +0.136 | -19.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2081 | +0.196 | +2.83€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 147 | -0.017 | -32.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 3103 | +0.103 | -4.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 616 | +0.131 | +14.18€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#SOL | 5896 | +0.135 | -179.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2110 | +0.205 | -20.92€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 148 | +0.100 | +1.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 3078 | +0.087 | -134.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 560 | +0.137 | -26.39€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 2736 | +0.096 | -33.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 39 | +0.134 | -2.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 2695 | +0.096 | -30.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2374 | +0.200 | -167.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 2374 | +0.200 | -167.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 373 | +0.151 | -48.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 373 | +0.151 | -48.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 515 | +0.220 | -16.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 515 | +0.220 | -16.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 385 | +0.156 | -49.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 385 | +0.156 | -49.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 611 | +0.268 | -8.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 611 | +0.268 | -8.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 133 | +0.159 | -0.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 133 | +0.159 | -0.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 357 | +0.160 | -42.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 357 | +0.160 | -42.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 121 | +0.427 | -1.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 121 | +0.427 | -1.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 41 | +0.407 | -0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 41 | +0.407 | -0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 43 | +0.411 | -1.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 43 | +0.411 | -1.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 28 | +0.433 | +0.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 28 | +0.433 | +0.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 11268 | +0.197 | -849.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 11268 | +0.197 | -849.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 2018 | +0.157 | -277.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 2018 | +0.157 | -277.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 1780 | +0.222 | -49.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 1780 | +0.222 | -49.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 1954 | +0.182 | -207.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 1954 | +0.182 | -207.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 1811 | +0.218 | -66.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 1811 | +0.218 | -66.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 1838 | +0.215 | -84.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 1838 | +0.215 | -84.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 1867 | +0.192 | -164.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 1867 | +0.192 | -164.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 667 | +0.128 | +12.08€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 667 | +0.128 | +12.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 334 | +0.101 | -12.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 334 | +0.101 | -12.14€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 333 | +0.154 | +24.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 333 | +0.154 | +24.22€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 305 | +0.275 | -16.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 305 | +0.275 | -16.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 127 | +0.252 | -9.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 127 | +0.252 | -9.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 137 | +0.270 | -7.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 137 | +0.270 | -7.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 41 | +0.337 | +1.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 41 | +0.337 | +1.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 116 | +0.364 | -14.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 116 | +0.364 | -14.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 48 | +0.340 | -8.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 48 | +0.340 | -8.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 54 | +0.393 | -5.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 54 | +0.393 | -5.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 14 | +0.175 | -1.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 14 | +0.175 | -1.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 620 | +0.302 | -1.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 620 | +0.302 | -1.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 620 | +0.302 | -1.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 620 | +0.302 | -1.65€ | 0 | 0 |
| ✅ GBM_LATE_15M | 12859 | +0.102 | +4322.57€ | 0 | 5 |
| ✅ GBM_LATE_15M#15min | 12859 | +0.102 | +4322.57€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 857 | +0.173 | +519.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 857 | +0.173 | +519.37€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 2583 | +0.084 | +515.23€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2583 | +0.084 | +515.23€ | 0 | 6 |
| ✅ GBM_LATE_15M#DOGE | 876 | +0.173 | +500.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 876 | +0.173 | +500.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH | 2394 | +0.063 | +343.90€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2394 | +0.063 | +343.90€ | 0 | 7 |
| ✅ GBM_LATE_15M#SOL | 2875 | +0.071 | +843.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2875 | +0.071 | +843.66€ | 1 | 2 |
| ✅ GBM_LATE_15M#XRP | 3274 | +0.134 | +1599.71€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 3274 | +0.134 | +1599.71€ | 0 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 10327 | +0.124 | +5100.39€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 10327 | +0.124 | +5100.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 788 | +0.189 | +577.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 788 | +0.189 | +577.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2291 | +0.080 | +747.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2291 | +0.080 | +747.85€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 760 | +0.213 | +606.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 760 | +0.213 | +606.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 2147 | +0.082 | +669.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 2147 | +0.082 | +669.14€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 2255 | +0.074 | +798.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 2255 | +0.074 | +798.13€ | 1 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2086 | +0.214 | +1701.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2086 | +0.214 | +1701.53€ | 0 | 12 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 581 | +0.217 | +447.17€ | 0 | 12 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 581 | +0.217 | +447.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 90 | +0.359 | +111.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 90 | +0.359 | +111.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 107 | +0.133 | +28.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 107 | +0.133 | +28.37€ | 0 | 6 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 87 | +0.275 | +78.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 87 | +0.275 | +78.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 75 | +0.175 | +55.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 75 | +0.175 | +55.57€ | 0 | 4 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 111 | +0.093 | +63.03€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 111 | +0.093 | +63.03€ | 0 | 2 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 111 | +0.270 | +109.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 111 | +0.270 | +109.69€ | 0 | 7 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 436 | +0.050 | +97.89€ | 5 | 7 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 436 | +0.050 | +97.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 15 | -0.110 | -4.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 15 | -0.110 | -4.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 233 | -0.032 | -1.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 233 | -0.032 | -1.79€ | 7 | 9 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 19 | -0.023 | +2.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 19 | -0.023 | +2.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 169 | +0.190 | +101.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 169 | +0.190 | +101.21€ | 0 | 13 |
| ✅ GBM_LATE_15M_TARDIO | 9884 | +0.088 | +3485.77€ | 0 | 5 |
| ✅ GBM_LATE_15M_TARDIO#15min | 9884 | +0.088 | +3485.77€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 782 | +0.202 | +576.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 782 | +0.202 | +576.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1900 | +0.036 | +273.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1900 | +0.036 | +273.64€ | 0 | 3 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 822 | +0.202 | +591.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 822 | +0.202 | +591.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1914 | +0.019 | +153.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1914 | +0.019 | +153.49€ | 0 | 2 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 2037 | +0.017 | +370.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 2037 | +0.017 | +370.51€ | 0 | 1 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 2429 | +0.167 | +1520.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 2429 | +0.167 | +1520.52€ | 0 | 10 |
| ✅ GBM_LATE_5M | 1517 | -0.015 | +38.60€ | 5 | 0 |
| ✅ GBM_LATE_5M#5min | 1517 | -0.015 | +38.60€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 315 | +0.030 | +33.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 315 | +0.030 | +33.99€ | 6 | 7 |
| ✅ GBM_LATE_5M#ETH | 115 | -0.141 | -18.63€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 115 | -0.141 | -18.63€ | 4 | 1 |
| ✅ GBM_LATE_5M#SOL | 610 | -0.043 | +13.15€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 610 | -0.043 | +13.15€ | 9 | 1 |
| ✅ GBM_LATE_5M#XRP | 477 | +0.020 | +10.09€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 477 | +0.020 | +10.09€ | 0 | 0 |
| ✅ GBM_LATE_60M | 395 | -0.079 | +15.50€ | 3 | 1 |
| ✅ GBM_LATE_60M#60min | 395 | -0.079 | +15.50€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 142 | -0.021 | +0.99€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 142 | -0.021 | +0.99€ | 3 | 1 |
| ✅ GBM_LATE_60M#ETH | 137 | -0.090 | +0.61€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 137 | -0.090 | +0.61€ | 4 | 1 |
| ✅ GBM_LATE_60M#SOL | 116 | -0.136 | +13.90€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 116 | -0.136 | +13.90€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE | 125 | -0.311 | -25.36€ | 17 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 125 | -0.311 | -25.36€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 39 | -0.232 | -2.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 39 | -0.232 | -2.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 45 | -0.372 | -15.64€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 45 | -0.372 | -15.64€ | 3 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 41 | -0.291 | -7.01€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 41 | -0.291 | -7.01€ | 1 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 93 | +0.037 | +4.81€ | 0 | 3 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 93 | +0.037 | +4.81€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 41 | +0.058 | +0.67€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 41 | +0.058 | +0.67€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 5 | -0.054 | -1.93€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 5 | -0.054 | -1.93€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 47 | +0.051 | +6.06€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 47 | +0.051 | +6.06€ | 2 | 0 |
| ✅ LATE_WINDOW_5MIN | 393 | -0.062 | -6.68€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 393 | -0.062 | -6.68€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 393 | -0.062 | -6.68€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 393 | -0.062 | -6.68€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 327 | +0.017 | +13.04€ | 1 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 327 | +0.017 | +13.04€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 327 | +0.017 | +13.04€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 327 | +0.017 | +13.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M | 86 | -0.091 | -10.02€ | 6 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 86 | -0.091 | -10.02€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 19 | +0.023 | +0.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 19 | +0.023 | +0.07€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 10 | -0.125 | -3.21€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 10 | -0.125 | -3.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 18 | +0.000 | -0.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 18 | +0.000 | -0.45€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 17 | -0.067 | -1.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 17 | -0.067 | -1.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 20 | -0.136 | -3.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 20 | -0.136 | -3.49€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M | 62 | -0.188 | -12.68€ | 4 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 62 | -0.188 | -12.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 17 | -0.112 | -2.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 17 | -0.112 | -2.71€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#ETH | 12 | -0.129 | -3.06€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#ETH#5min | 12 | -0.129 | -3.06€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL | 16 | -0.222 | -5.16€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL#5min | 16 | -0.222 | -5.16€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 12 | -0.086 | -2.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 12 | -0.086 | -2.20€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M | 93 | +0.026 | -1.75€ | 1 | 2 |
| ✅ LIQUIDACIONES_60M#60min | 93 | +0.026 | -1.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 32 | +0.000 | -2.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 32 | +0.000 | -2.92€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 27 | +0.017 | -0.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 27 | +0.017 | -0.31€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 34 | +0.056 | +1.47€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 34 | +0.056 | +1.47€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1723 | +0.014 | +15.45€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1587 | +0.010 | +2.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 223 | +0.042 | +6.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 223 | +0.042 | +6.48€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 233 | +0.006 | -0.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 233 | +0.006 | -0.79€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 277 | -0.020 | -9.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 277 | -0.020 | -9.17€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 340 | +0.047 | +16.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 340 | +0.047 | +16.21€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#XRP | 223 | -0.002 | -4.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 223 | -0.002 | -4.63€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM | 193 | -0.162 | -5.71€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 74 | -0.224 | -18.33€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 63 | -0.254 | -16.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 11 | -0.021 | -1.94€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 77 | -0.171 | -1.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 64 | -0.197 | -3.83€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 13 | -0.022 | +2.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 42 | -0.023 | +14.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 37 | +0.013 | +15.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 5 | -0.054 | -1.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 164 | -0.175 | -4.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 29 | -0.081 | -0.95€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 32 | -0.235 | -6.52€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 16 | -0.133 | -2.73€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 16 | -0.133 | -2.73€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 13 | -0.152 | -2.26€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 13 | -0.152 | -2.26€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 32 | -0.235 | -6.52€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 28 | +0.267 | +4.53€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 9 | +0.021 | -1.03€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 9 | +0.021 | -1.03€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 14 | +0.306 | +4.15€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 14 | +0.306 | +4.15€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 28 | +0.267 | +4.53€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 323 | +0.054 | +12.10€ | 1 | 0 |
| ✅ STREAK_FADE_15M#15min | 323 | +0.054 | +12.10€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 12 | +0.000 | -3.33€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 12 | +0.000 | -3.33€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 64 | +0.030 | -3.55€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 64 | +0.030 | -3.55€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 89 | +0.115 | +19.28€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 89 | +0.115 | +19.28€ | 0 | 2 |
| ✅ STREAK_FADE_15M#XRP | 158 | +0.031 | -0.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 158 | +0.031 | -0.30€ | 1 | 1 |
| ✅ STREAK_FADE_5M | 247 | -0.050 | -25.47€ | 3 | 0 |
| ✅ STREAK_FADE_5M#5min | 247 | -0.050 | -25.47€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 47 | -0.153 | -8.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 47 | -0.153 | -8.07€ | 2 | 0 |
| ✅ STREAK_FADE_5M#SOL | 95 | -0.026 | -8.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 95 | -0.026 | -8.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP | 105 | -0.023 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 105 | -0.023 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M | 5 | -0.054 | -1.57€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 5 | -0.054 | -1.57€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 5 | -0.054 | -1.57€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 5 | -0.054 | -1.57€ | 0 | 0 |
| 🚫 STREAK_MOM_5M | 324 | -0.061 | -27.40€ | 4 | 0 |
| ✅ STREAK_MOM_5M#5min | 324 | -0.061 | -27.40€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 111 | -0.066 | -8.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 111 | -0.066 | -8.31€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 115 | -0.013 | -5.74€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 115 | -0.013 | -5.74€ | 2 | 0 |
| ✅ STREAK_MOM_5M#XRP | 98 | -0.110 | -13.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 98 | -0.110 | -13.35€ | 5 | 0 |
| ✅ STRUCT_NO_15M | 469 | +0.024 | +1.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 469 | +0.024 | +1.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 159 | +0.059 | +5.69€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 159 | +0.059 | +5.69€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH | 174 | +0.045 | +4.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 174 | +0.045 | +4.72€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 136 | -0.043 | -8.45€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 136 | -0.043 | -8.45€ | 2 | 0 |
| ✅ UPDOWN_GBM | 4003 | +0.060 | +564.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 3735 | +0.073 | +604.91€ | 0 | 6 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 135 | -0.069 | -12.69€ | 4 | 0 |
| ✅ UPDOWN_GBM#BNB | 464 | +0.092 | +110.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 464 | +0.092 | +110.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 713 | +0.058 | +80.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 628 | +0.086 | +95.24€ | 1 | 7 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 44 | -0.087 | -7.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 412 | +0.031 | +20.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 409 | +0.033 | +21.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1387 | +0.059 | +157.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1293 | +0.071 | +169.32€ | 0 | 4 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 55 | -0.026 | -3.07€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 494 | +0.020 | +47.70€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 421 | +0.046 | +55.11€ | 2 | 1 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 36 | -0.105 | -2.43€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 531 | +0.095 | +150.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 520 | +0.102 | +153.68€ | 3 | 4 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 306 | +0.305 | +61.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 306 | +0.305 | +61.72€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 152 | +0.299 | +27.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 152 | +0.299 | +27.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 154 | +0.308 | +33.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 154 | +0.308 | +33.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 3511 | +0.163 | +1805.25€ | 0 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 3511 | +0.163 | +1805.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 380 | +0.217 | +282.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 380 | +0.217 | +282.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 414 | +0.055 | +60.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 414 | +0.055 | +60.45€ | 1 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 366 | +0.196 | +242.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 366 | +0.196 | +242.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 631 | +0.192 | +278.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 631 | +0.192 | +278.46€ | 1 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 694 | +0.105 | +229.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 694 | +0.105 | +229.08€ | 2 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1026 | +0.195 | +712.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1026 | +0.195 | +712.39€ | 0 | 20 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 32 | +0.000 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 32 | +0.000 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 32 | +0.000 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 32 | +0.000 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 136 | +0.254 | +71.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 136 | +0.254 | +71.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 74 | +0.210 | +22.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 74 | +0.210 | +22.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 62 | +0.297 | +48.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 62 | +0.297 | +48.91€ | 0 | 0 |
| ✅ UPDOWN_OU_5M | 337 | -0.175 | -58.65€ | 10 | 0 |
| ✅ UPDOWN_OU_5M#5min | 337 | -0.175 | -58.65€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 55 | -0.184 | -11.55€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 55 | -0.184 | -11.55€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 29 | -0.177 | -4.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 29 | -0.177 | -4.12€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 60 | -0.161 | -10.58€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 60 | -0.161 | -10.58€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 37 | -0.192 | -5.89€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 37 | -0.192 | -5.89€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 71 | -0.158 | -9.83€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 71 | -0.158 | -9.83€ | 3 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 85 | -0.167 | -16.68€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 85 | -0.167 | -16.68€ | 9 | 0 |
| ✅ WEEKLY_PRICE | 682 | +0.271 | +290.58€ | 0 | 1 |
| ✅ WEEKLY_PRICE#BTC | 203 | +0.173 | -10.04€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 201 | +0.224 | +34.18€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 278 | +0.371 | +266.44€ | 0 | 1 |