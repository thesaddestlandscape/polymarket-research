# Hipótesis automáticas — 2026-08-10 20:07 UTC
_Generado por shadow_postmortem.py sobre 106735 resoluciones (PNL=+15034.20€)_

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
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.232 (n=435)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.128)

- **PATRÓN** `restante_min` < `3.77` → IC=+0.151 (n=393)

  - _Acción_: Kelly boost +0.75€ cuando `restante_min` < 3.77 (IC base=+0.128)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.138 (n=407)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` > 4.91 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.144 (n=1181)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 7.0 (IC base=+0.128)

- **PATRÓN** `lag_apertura_s` < `5.39` → IC=+0.146 (n=393)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 5.39 (IC base=+0.128)

- **PATRÓN** `profundidad_ratio_no` > `17.7` → IC=+0.150 (n=392)

  - _Acción_: Kelly boost +0.75€ cuando `profundidad_ratio_no` > 17.7 (IC base=+0.128)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.37` → IC=+0.243 (n=204)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.117)

- **PATRÓN** `restante_min` < `4.6` → IC=+0.146 (n=391)

  - _Acción_: Kelly boost +0.73€ cuando `restante_min` < 4.6 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.132 (n=588)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.117)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.41` → IC=+0.197 (n=417)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.41 (IC base=+0.138)

- **PATRÓN** `restante_min` < `4.95` → IC=+0.140 (n=612)

  - _Acción_: Kelly boost +0.70€ cuando `restante_min` < 4.95 (IC base=+0.138)

- **PATRÓN** `restante_min` > `4.91` → IC=+0.149 (n=277)

  - _Acción_: Kelly boost +0.74€ cuando `restante_min` > 4.91 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.151 (n=531)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 9.0 (IC base=+0.138)

- **PATRÓN** `lag_apertura_s` < `17.46` → IC=+0.146 (n=396)

  - _Acción_: Kelly boost +0.73€ cuando `lag_apertura_s` < 17.46 (IC base=+0.138)

- **PATRÓN** `profundidad_ratio_no` > `24.6` → IC=+0.197 (n=199)

  - _Acción_: Kelly boost +0.98€ cuando `profundidad_ratio_no` > 24.6 (IC base=+0.138)

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

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.149 (n=286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.097)

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

- **PATRÓN** `sigma_ewma_delta_pct` < `4.558` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.558 (IC base=+0.283)

- **PATRÓN** `libro_liquidez` > `2838.0713` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2838.0713 (IC base=+0.283)

### GBM_LATE_15M_PYCONFIRMADO
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
  - _Potencial_: sin este filtro IC_bueno=-0.185 (n=236)

- **FILTRO** `dist_vwap_pct` > `0.6179` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.6179
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=291)

- **FILTRO** `sigma_ewma_delta_pct` > `3.527` → IC=-0.236 (n=104)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.527
  - _Potencial_: sin este filtro IC_bueno=-0.206 (n=209)

### GBM_LATE_5M#BTC#5min
- **FILTRO** `sigma_h` < `0.0035` → IC=-0.382 (n=32)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0035
  - _Potencial_: sin este filtro IC_bueno=-0.271 (n=33)

- **PATRÓN** `sigma_h` > `0.0061` → IC=+0.203 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0061 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.1367` → IC=+0.138 (n=78)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1367 (IC base=+0.099)

### GBM_LATE_5M#ETH#5min
- **FILTRO** `sigma_h` < `0.0038` → IC=-0.382 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0038
  - _Potencial_: sin este filtro IC_bueno=-0.280 (n=48)

- **FILTRO** `sigma_ewma_delta_pct` > `3.157` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.157
  - _Potencial_: sin este filtro IC_bueno=-0.296 (n=47)

- **PATRÓN** `sigma_h` < `0.0028` → IC=+0.147 (n=15)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0028 (IC base=+0.083)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.083)

- **PATRÓN** `libro_liquidez` > `5947.4918` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 5947.4918 (IC base=+0.083)

### GBM_LATE_5M#SOL#5min
- **FILTRO** `sigma_h` > `0.0066` → IC=-0.282 (n=99)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0066
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

- **FILTRO** `hora_utc` < `9.0` → IC=-0.375 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.170 (n=95)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.273 (n=42)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.210 (n=91)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.565` → IC=+0.197 (n=87)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 6.565 (IC base=+0.024)

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

- **FILTRO** `sigma_h` > `0.0024` → IC=-0.316 (n=47)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0024
  - _Potencial_: sin este filtro IC_bueno=-0.079 (n=17)

- **FILTRO** `dist_vwap_pct` > `0.3507` → IC=-0.342 (n=17)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.3507
  - _Potencial_: sin este filtro IC_bueno=-0.214 (n=47)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.326 (n=21)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.211 (n=43)

### GBM_LATE_60M_FADE#ETH#60min
- **FILTRO** `sigma_h` > `0.0022` → IC=-0.342 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0022
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_ewma_delta_pct` < `1.863` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 1.863
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=3)

### GBM_LATE_60M_PYCONFIRMADO#BTC#60min
- **PATRÓN** `sigma_ewma_delta_pct` > `2.924` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 2.924 (IC base=+0.083)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `sigma_h` > `0.0051` → IC=-0.152 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0051
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

### LEADLAG_BTC_XRP_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=168)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=168)

### LIQUIDACIONES_15M
- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.208 (n=22)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.194 (n=47)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.154 (n=53)

- **FILTRO** `libro_liquidez` < `2012.8653` → IC=-0.333 (n=22)

  - _Acción_: SKIP cuando `libro_liquidez` < 2012.8653
  - _Potencial_: sin este filtro IC_bueno=-0.133 (n=47)

- **FILTRO** `liq_usd_total` < `618.08` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_usd_total` < 618.08
  - _Potencial_: sin este filtro IC_bueno=+0.010 (n=49)

- **FILTRO** `hora_utc` < `11.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.019 (n=50)

### LIQUIDACIONES_5M
- **FILTRO** `liq_n` < `2.0` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_n` < 2.0
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=31)

- **FILTRO** `liq_usd_total` < `1137.38` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `liq_usd_total` < 1137.38
  - _Potencial_: sin este filtro IC_bueno=-0.095 (n=35)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=35)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.237 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=18)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=20)

### LIQUIDACIONES_60M
- **FILTRO** `hora_utc` < `15.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.176 (n=32)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.176 (n=32)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 15.0 (IC base=+0.018)

### LIQUIDACIONES_60M#BTC#60min
- **FILTRO** `py_entrada` < `0.535` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `py_entrada` < 0.535
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=11)

### LIQUIDACIONES_60M#SOL#60min
- **PATRÓN** `libro_spread` < `0.03` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `libro_spread` < 0.03 (IC base=+0.059)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.068 (n=190)

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
- **FILTRO** `pct_vs_K` |x|> `7.275` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 7.275
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=38)

- **FILTRO** `sigma_h` > `0.0072` → IC=-0.312 (n=83)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0072
  - _Potencial_: sin este filtro IC_bueno=+0.133 (n=28)

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

### PRICE_TARGET_GBM_FADE
- **FILTRO** `T_h` < `143.0075` → IC=-0.413 (n=21)

  - _Acción_: SKIP cuando `T_h` < 143.0075
  - _Potencial_: sin este filtro IC_bueno=-0.389 (n=7)

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

- **PATRÓN** `volumen_racha` < `640372.5` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `volumen_racha` < 640372.5 (IC base=+0.052)

### STREAK_FADE_5M
- **FILTRO** `hora_utc` < `16.0` → IC=-0.167 (n=52)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=-0.061 (n=55)

- **FILTRO** `streak_len` > `4.0` → IC=-0.241 (n=25)

  - _Acción_: SKIP cuando `streak_len` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.020 (n=48)

### STREAK_FADE_5M#ETH#5min
- **FILTRO** `streak_len` > `3.0` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=8)

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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=90)

- **FILTRO** `libro_liquidez` < `3696.7452` → IC=-0.125 (n=54)

  - _Acción_: SKIP cuando `libro_liquidez` < 3696.7452
  - _Potencial_: sin este filtro IC_bueno=-0.026 (n=112)

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

- **FILTRO** `streak_len` > `3.0` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `streak_len` > 3.0
  - _Potencial_: sin este filtro IC_bueno=-0.122 (n=35)

- **FILTRO** `libro_liquidez` < `3688.8474` → IC=-0.260 (n=23)

  - _Acción_: SKIP cuando `libro_liquidez` < 3688.8474
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=23)

### STRUCT_NO_15M#BTC#15min
- **PATRÓN** `hora_utc` > `14.0` → IC=+0.151 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 14.0 (IC base=+0.065)

### STRUCT_NO_15M#SOL#15min
- **FILTRO** `py_entrada` < `0.495` → IC=-0.167 (n=37)

  - _Acción_: SKIP cuando `py_entrada` < 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=158)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=163)

### UPDOWN_GBM#15min
- **PATRÓN** `ibs_15` > `0.5954` → IC=+0.177 (n=682)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.88€ cuando `ibs_15` > 0.5954 (IC base=+0.064)

- **PATRÓN** `dist_vwap_pct` > `0.1672` → IC=+0.159 (n=253)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1672 (IC base=+0.064)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.417` → IC=+0.163 (n=176)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.417 (IC base=+0.064)

- **PATRÓN** `libro_liquidez` > `9956.4716` → IC=+0.134 (n=200)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 9956.4716 (IC base=+0.064)

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
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1888 (IC base=+0.099)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0644` → IC=+0.134 (n=323)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0644 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.175 (n=192)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 14.0 (IC base=+0.099)

- **PATRÓN** `ibs_15` > `0.6354` → IC=+0.219 (n=283)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6354 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.2571` → IC=+0.237 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2571 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `25.023` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 25.023 (IC base=+0.099)

- **PATRÓN** `libro_liquidez` > `11672.79` → IC=+0.161 (n=113)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11672.79 (IC base=+0.099)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `ibs_15` > `0.6644` → IC=+0.192 (n=219)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.6644 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.056` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 7.056 (IC base=+0.062)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.150 (n=232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0055 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.9222` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9222 (IC base=+0.080)

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
- **FILTRO** `drift_15min` |x|> `0.4751` → IC=-0.237 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4751
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

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
- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.150 (n=398)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0047 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.157 (n=1069)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0055 (IC base=+0.149)

- **PATRÓN** `drift_60min` |x|≤ `0.0663` → IC=+0.175 (n=340)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0663 (IC base=+0.149)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1937` → IC=+0.138 (n=352)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio_macro` |x|> 0.1937 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.138 (n=525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 12.0 (IC base=+0.149)

- **PATRÓN** `ibs_15` > `0.5385` → IC=+0.220 (n=772)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5385 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.2413` → IC=+0.139 (n=267)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.2413 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.258` → IC=+0.189 (n=448)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 5.258 (IC base=+0.149)

- **PATRÓN** `libro_liquidez` > `2545.0995` → IC=+0.133 (n=772)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2545.0995 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.006` → IC=+0.178 (n=1493)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.006 (IC base=+0.169)

- **PATRÓN** `drift_60min` |x|≤ `0.2167` → IC=+0.169 (n=599)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2167 (IC base=+0.169)

- **PATRÓN** `drift_15min` |x|≤ `0.4196` → IC=+0.198 (n=299)

  - _Acción_: Kelly boost +0.99€ cuando `drift_15min` |x|≤ 0.4196 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.169 (n=618)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 12.0 (IC base=+0.169)

- **PATRÓN** `ibs_15` < `0.3269` → IC=+0.247 (n=790)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3269 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.2003` → IC=+0.191 (n=208)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.2003 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.539` → IC=+0.194 (n=119)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 19.539 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.443` → IC=+0.188 (n=885)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 7.443 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=921)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.169)

- **PATRÓN** `libro_liquidez` > `3994.029` → IC=+0.174 (n=299)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3994.029 (IC base=+0.169)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `ibs_15` < `0.7488` → IC=-0.139 (n=59)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.7488
  - _Potencial_: sin este filtro IC_bueno=+0.271 (n=120)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.169 (n=125)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.85€ cuando `sigma_h` < 0.0037 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.1123` → IC=+0.152 (n=90)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1123 (IC base=+0.148)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0951` → IC=+0.180 (n=120)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.0951 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.208 (n=63)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.148)

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

  - _Acción_: Kelly boost +0.89€ cuando `drift_15min` |x|≤ 0.5515 (IC base=-0.096)

- **PATRÓN** `ibs_15` < `0.5537` → IC=+0.139 (n=34)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.69€ cuando `ibs_15` < 0.5537 (IC base=-0.096)

- **PATRÓN** `libro_liquidez` > `9476.9221` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 9476.9221 (IC base=-0.096)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.5405` → IC=-0.143 (n=82)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5405
  - _Potencial_: sin este filtro IC_bueno=+0.202 (n=169)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.148 (n=174)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0045 (IC base=+0.130)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.185 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0063 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.045` → IC=+0.162 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.045 (IC base=+0.130)

- **PATRÓN** `ibs_15` > `0.7007` → IC=+0.289 (n=126)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7007 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.922` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 7.922 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `7672.3115` → IC=+0.133 (n=126)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 7672.3115 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0057` → IC=+0.312 (n=152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0057 (IC base=+0.276)

- **PATRÓN** `drift_60min` |x|≤ `0.1029` → IC=+0.370 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1029 (IC base=+0.276)

- **PATRÓN** `drift_15min` |x|≤ `0.4473` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4473 (IC base=+0.276)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.289 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.276)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.271 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.276)

- **PATRÓN** `ibs_15` < `0.0419` → IC=+0.413 (n=44)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.0419 (IC base=+0.276)

- **PATRÓN** `dist_vwap_pct` > `0.2534` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2534 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.363` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.363 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.671` → IC=+0.288 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.671 (IC base=+0.276)

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

- **PATRÓN** `libro_liquidez` > `3043.8234` → IC=+0.134 (n=129)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 3043.8234 (IC base=+0.107)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.162 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0077 (IC base=+0.103)

- **PATRÓN** `drift_15min` |x|≤ `0.4799` → IC=+0.143 (n=110)

  - _Acción_: Kelly boost +0.71€ cuando `drift_15min` |x|≤ 0.4799 (IC base=+0.103)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.170 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 5.0 (IC base=+0.103)

- **PATRÓN** `ibs_15` < `0.2632` → IC=+0.240 (n=167)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.2632 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.798` → IC=+0.125 (n=254)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 6.798 (IC base=+0.103)

- **PATRÓN** `libro_liquidez` > `3830.5978` → IC=+0.152 (n=113)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3830.5978 (IC base=+0.103)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.203 (n=210)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0081 (IC base=+0.170)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.232 (n=80)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.170)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2268` → IC=+0.177 (n=60)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.2268 (IC base=+0.170)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.167 (n=181)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 4.0 (IC base=+0.170)

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

- **PATRÓN** `libro_liquidez` > `3116.9997` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 3116.9997 (IC base=+0.170)

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
- **FILTRO** `pct_spot_vs_ref` |x|> `0.1377` → IC=-0.365 (n=72)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.1377
  - _Potencial_: sin este filtro IC_bueno=-0.093 (n=25)

- **FILTRO** `sigma_h` > `0.0065` → IC=-0.379 (n=64)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0065
  - _Potencial_: sin este filtro IC_bueno=-0.129 (n=33)

- **FILTRO** `drift_60min` |x|> `0.5932` → IC=-0.423 (n=24)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.5932
  - _Potencial_: sin este filtro IC_bueno=-0.247 (n=73)

- **FILTRO** `drift_15min` |x|> `1.844` → IC=-0.462 (n=24)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.844
  - _Potencial_: sin este filtro IC_bueno=-0.233 (n=73)

- **FILTRO** `pct_spot_vs_ref` |x|> `0.2043` → IC=-0.246 (n=61)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.2043
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=187)

- **FILTRO** `sigma_h` < `0.0072` → IC=-0.172 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0072
  - _Potencial_: sin este filtro IC_bueno=-0.112 (n=186)

- **FILTRO** `drift_15min` |x|> `1.0429` → IC=-0.182 (n=61)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 1.0429
  - _Potencial_: sin este filtro IC_bueno=-0.108 (n=187)

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

### UPDOWN_OU_5M#SOL#5min
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
- **PATRÓN** `T_h` > `146.1402` → IC=+0.460 (n=149)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1402 (IC base=+0.354)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `111.996` → IC=+0.292 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.996 (IC base=+0.270)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `135.9969` → IC=+0.298 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 135.9969 (IC base=+0.299)

- **PATRÓN** `T_h` > `111.996` → IC=+0.318 (n=119)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.996 (IC base=+0.299)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `135.9824` → IC=+0.459 (n=192)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 135.9824 (IC base=+0.436)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5954 sube el IC de +0.064 a +0.177 en UPDOWN_GBM#15min (n=682). Ya aplicado como kelly_boost=+0.88€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.6354 sube el IC de +0.099 a +0.219 en UPDOWN_GBM#BTC#15min (n=283). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6644 sube el IC de +0.062 a +0.192 en UPDOWN_GBM#ETH#15min (n=219). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5385 sube el IC de +0.149 a +0.220 en UPDOWN_GBM_15M_TARDIO (n=772). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.3269 sube el IC de +0.169 a +0.247 en UPDOWN_GBM_15M_TARDIO (n=790). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7488 sube el IC de +0.148 a +0.271 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=120). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.7007 sube el IC de +0.130 a +0.289 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=126). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.0419 sube el IC de +0.276 a +0.413 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=44). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.7419 sube el IC de +0.107 a +0.296 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=96). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.2632 sube el IC de +0.103 a +0.240 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=167). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.170 a +0.214 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=180). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3571 sube el IC de +0.211 a +0.267 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=256). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER` — IC=+0.294 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `RESOLUTION_SNIPER#sniper` — IC=+0.294 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min` — IC=+0.444 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL` — IC=+0.444 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `GBM_LATE_60M_PYCONFIRMADO#ETH#60min` — IC=+0.083 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `GBM_LATE_60M_PYCONFIRMADO#ETH` — IC=+0.083 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1884 | +0.051 | -1.86€ | 0 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1884 | +0.051 | -1.86€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 885 | +0.028 | -16.56€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 885 | +0.028 | -16.56€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 668 | +0.070 | -4.92€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 668 | +0.070 | -4.92€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 312 | +0.073 | +19.97€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 312 | +0.073 | +19.97€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 3137 | -0.053 | -618.86€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS#15min | 485 | +0.221 | -43.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 2652 | -0.103 | -575.62€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#BNB | 387 | -0.266 | -101.92€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#BNB#5min | 387 | -0.266 | -101.92€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 485 | +0.221 | -43.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 485 | +0.221 | -43.24€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS#DOGE | 462 | -0.162 | -35.19€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 462 | -0.162 | -35.19€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 577 | +0.061 | -26.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 577 | +0.061 | -26.49€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 626 | -0.022 | -78.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 626 | -0.022 | -78.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 600 | -0.193 | -333.51€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 600 | -0.193 | -333.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 29640 | +0.118 | -776.78€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 6772 | +0.195 | -125.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 458 | +0.050 | -40.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 20353 | +0.092 | -653.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 2057 | +0.137 | +42.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 3277 | +0.082 | -195.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 13 | -0.022 | -3.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | +0.018 | +2.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 3259 | +0.082 | -195.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 6302 | +0.131 | -96.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 2108 | +0.186 | -94.84€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 149 | +0.056 | -15.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 3266 | +0.095 | -54.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 779 | +0.145 | +68.38€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 3273 | +0.080 | -192.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 16 | +0.222 | +8.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 3256 | +0.079 | -202.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 6782 | +0.133 | -40.74€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2287 | +0.193 | +3.63€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 149 | -0.017 | -32.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 3668 | +0.103 | -22.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 678 | +0.129 | +10.35€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#SOL | 6703 | +0.133 | -228.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2307 | +0.206 | -35.98€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 151 | +0.108 | +5.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 3645 | +0.087 | -160.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 600 | +0.135 | -36.42€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 3303 | +0.103 | -23.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 41 | +0.128 | -3.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 3259 | +0.103 | -17.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2930 | +0.199 | -191.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 2930 | +0.199 | -191.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 517 | +0.159 | -61.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 517 | +0.159 | -61.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 527 | +0.222 | -16.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 527 | +0.222 | -16.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 520 | +0.163 | -61.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 520 | +0.163 | -61.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 729 | +0.267 | -8.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 729 | +0.267 | -8.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 153 | +0.119 | +5.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 153 | +0.119 | +5.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 484 | +0.173 | -48.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 484 | +0.173 | -48.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 143 | +0.431 | -1.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 143 | +0.431 | -1.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 50 | +0.404 | -1.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 50 | +0.404 | -1.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 50 | +0.423 | -0.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 50 | +0.423 | -0.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 34 | +0.444 | +1.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 34 | +0.444 | +1.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 13628 | +0.199 | -1009.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 13628 | +0.199 | -1009.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 2434 | +0.161 | -331.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 2434 | +0.161 | -331.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 2164 | +0.223 | -61.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 2164 | +0.223 | -61.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 2359 | +0.184 | -246.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 2359 | +0.184 | -246.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 2206 | +0.217 | -84.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 2206 | +0.217 | -84.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 2216 | +0.217 | -99.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 2216 | +0.217 | -99.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 2249 | +0.197 | -186.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 2249 | +0.197 | -186.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 1568 | +0.128 | +19.54€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 1568 | +0.128 | +19.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 777 | +0.117 | -4.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 777 | +0.117 | -4.28€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 791 | +0.138 | +23.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 791 | +0.138 | +23.83€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 350 | +0.270 | -23.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 350 | +0.270 | -23.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 146 | +0.257 | -10.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 146 | +0.257 | -10.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 163 | +0.258 | -14.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 163 | +0.258 | -14.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 41 | +0.337 | +1.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 41 | +0.337 | +1.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 134 | +0.368 | -16.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 134 | +0.368 | -16.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 56 | +0.345 | -9.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 56 | +0.345 | -9.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 64 | +0.394 | -5.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 64 | +0.394 | -5.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 14 | +0.175 | -1.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 14 | +0.175 | -1.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 653 | +0.295 | -14.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 653 | +0.295 | -14.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 653 | +0.295 | -14.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 653 | +0.295 | -14.65€ | 0 | 0 |
| ✅ GBM_LATE_15M | 13499 | +0.102 | +4587.08€ | 0 | 5 |
| ✅ GBM_LATE_15M#15min | 13499 | +0.102 | +4587.08€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 936 | +0.184 | +608.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 936 | +0.184 | +608.66€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 2636 | +0.087 | +543.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2636 | +0.087 | +543.17€ | 0 | 6 |
| ✅ GBM_LATE_15M#DOGE | 959 | +0.188 | +608.12€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 959 | +0.188 | +608.12€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH | 2474 | +0.060 | +340.71€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2474 | +0.060 | +340.71€ | 0 | 7 |
| ✅ GBM_LATE_15M#SOL | 3052 | +0.067 | +850.93€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 3052 | +0.067 | +850.93€ | 1 | 3 |
| ✅ GBM_LATE_15M#XRP | 3442 | +0.129 | +1635.50€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 3442 | +0.129 | +1635.50€ | 0 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 11146 | +0.120 | +5513.23€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 11146 | +0.120 | +5513.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 967 | +0.150 | +724.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 967 | +0.150 | +724.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2462 | +0.076 | +808.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2462 | +0.076 | +808.07€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 831 | +0.229 | +717.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 831 | +0.229 | +717.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 2293 | +0.075 | +653.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 2293 | +0.075 | +653.11€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 2423 | +0.069 | +807.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 2423 | +0.069 | +807.73€ | 1 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2170 | +0.218 | +1802.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2170 | +0.218 | +1802.72€ | 0 | 12 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 944 | +0.248 | +873.35€ | 0 | 12 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 944 | +0.248 | +873.35€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 145 | +0.357 | +187.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 145 | +0.357 | +187.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 164 | +0.193 | +84.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 164 | +0.193 | +84.05€ | 0 | 6 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 145 | +0.330 | +172.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 145 | +0.330 | +172.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 127 | +0.205 | +105.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 127 | +0.205 | +105.37€ | 0 | 4 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 176 | +0.112 | +115.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 176 | +0.112 | +115.69€ | 0 | 2 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 187 | +0.294 | +207.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 187 | +0.294 | +207.81€ | 0 | 7 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 445 | +0.046 | +96.50€ | 4 | 7 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 445 | +0.046 | +96.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 19 | -0.113 | -4.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 19 | -0.113 | -4.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 233 | -0.032 | -1.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 233 | -0.032 | -1.79€ | 2 | 9 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 24 | -0.077 | +2.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 24 | -0.077 | +2.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 169 | +0.190 | +101.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 169 | +0.190 | +101.21€ | 0 | 13 |
| ✅ GBM_LATE_15M_TARDIO | 10303 | +0.093 | +3858.84€ | 0 | 5 |
| ✅ GBM_LATE_15M_TARDIO#15min | 10303 | +0.093 | +3858.84€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 856 | +0.212 | +669.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 856 | +0.212 | +669.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1956 | +0.039 | +297.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1956 | +0.039 | +297.96€ | 0 | 3 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 902 | +0.212 | +692.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 902 | +0.212 | +692.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1954 | +0.017 | +151.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1954 | +0.017 | +151.11€ | 0 | 2 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 2113 | +0.021 | +412.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 2113 | +0.021 | +412.50€ | 0 | 1 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 2522 | +0.172 | +1634.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 2522 | +0.172 | +1634.81€ | 0 | 10 |
| ✅ GBM_LATE_5M | 1612 | -0.012 | +33.62€ | 3 | 0 |
| ✅ GBM_LATE_5M#5min | 1612 | -0.012 | +33.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 350 | +0.017 | +21.61€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 350 | +0.017 | +21.61€ | 1 | 2 |
| ✅ GBM_LATE_5M#ETH | 121 | -0.126 | -17.18€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 121 | -0.126 | -17.18€ | 2 | 3 |
| ✅ GBM_LATE_5M#SOL | 652 | -0.029 | +20.90€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 652 | -0.029 | +20.90€ | 3 | 1 |
| ✅ GBM_LATE_5M#XRP | 489 | +0.019 | +8.29€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 489 | +0.019 | +8.29€ | 0 | 0 |
| ✅ GBM_LATE_60M | 407 | -0.077 | +16.62€ | 3 | 1 |
| ✅ GBM_LATE_60M#60min | 407 | -0.077 | +16.62€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 148 | -0.020 | +0.92€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 148 | -0.020 | +0.92€ | 3 | 1 |
| ✅ GBM_LATE_60M#ETH | 140 | -0.085 | +3.95€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 140 | -0.085 | +3.95€ | 3 | 1 |
| ✅ GBM_LATE_60M#SOL | 119 | -0.136 | +11.75€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 119 | -0.136 | +11.75€ | 3 | 1 |
| 🚫 GBM_LATE_60M_FADE | 131 | -0.312 | -27.01€ | 5 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 131 | -0.312 | -27.01€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 44 | -0.239 | -3.84€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 44 | -0.239 | -3.84€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 46 | -0.375 | -16.15€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 46 | -0.375 | -16.15€ | 1 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 41 | -0.291 | -7.01€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 41 | -0.291 | -7.01€ | 1 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 160 | +0.018 | -2.94€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 160 | +0.018 | -2.94€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 52 | +0.037 | +2.55€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 52 | +0.037 | +2.55€ | 0 | 1 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 34 | +0.083 | +2.38€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 34 | +0.083 | +2.38€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 74 | -0.026 | -7.87€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 74 | -0.026 | -7.87€ | 1 | 0 |
| ✅ LATE_WINDOW_5MIN | 394 | -0.063 | -7.19€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 394 | -0.063 | -7.19€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 394 | -0.063 | -7.19€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 394 | -0.063 | -7.19€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 327 | +0.017 | +13.04€ | 1 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 327 | +0.017 | +13.04€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 327 | +0.017 | +13.04€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 327 | +0.017 | +13.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M | 134 | -0.132 | -21.77€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 134 | -0.132 | -21.77€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 30 | -0.094 | -3.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 30 | -0.094 | -3.89€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 14 | -0.175 | -4.30€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 14 | -0.175 | -4.30€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 27 | +0.017 | -0.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 27 | +0.017 | -0.56€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 24 | -0.077 | -2.68€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 24 | -0.077 | -2.68€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#XRP | 36 | -0.210 | -8.82€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#XRP#15min | 36 | -0.210 | -8.82€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M | 86 | -0.182 | -17.18€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 86 | -0.182 | -17.18€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#BTC | 23 | -0.220 | -5.77€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#BTC#5min | 23 | -0.220 | -5.77€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#ETH | 22 | -0.208 | -5.28€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#ETH#5min | 22 | -0.208 | -5.28€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL | 21 | -0.239 | -5.80€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL#5min | 21 | -0.239 | -5.80€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 15 | -0.022 | -0.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 15 | -0.022 | -0.79€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M | 147 | +0.003 | -4.36€ | 1 | 1 |
| ✅ LIQUIDACIONES_60M#60min | 147 | +0.003 | -4.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 52 | -0.018 | -5.78€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 52 | -0.018 | -5.78€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 46 | +0.000 | +0.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 46 | +0.000 | +0.07€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 49 | +0.029 | +1.36€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 49 | +0.029 | +1.36€ | 0 | 1 |
| ✅ ORDER_FLOW_5M | 1725 | +0.014 | +15.43€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1589 | +0.010 | +2.84€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 225 | +0.042 | +6.46€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 225 | +0.042 | +6.46€ | 0 | 1 |
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
| ✅ PRICE_TARGET_GBM | 195 | -0.165 | -6.73€ | 3 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 75 | -0.227 | -18.84€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 63 | -0.254 | -16.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 12 | -0.043 | -2.45€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 78 | -0.175 | -2.10€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 64 | -0.197 | -3.83€ | 2 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 14 | -0.044 | +1.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 42 | -0.023 | +14.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 37 | +0.013 | +15.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 5 | -0.054 | -1.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 164 | -0.175 | -4.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 31 | -0.106 | -1.97€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE | 52 | -0.278 | -13.27€ | 1 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC | 24 | -0.231 | -5.78€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#BTC#atexpiry | 23 | -0.220 | -5.27€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 22 | -0.250 | -4.43€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 21 | -0.239 | -3.92€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL | 6 | -0.113 | -3.06€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#SOL#atexpiry | 5 | -0.089 | -2.55€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 49 | -0.265 | -11.74€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 32 | +0.294 | +6.65€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 9 | +0.021 | -1.03€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 9 | +0.021 | -1.03€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 8 | +0.080 | +1.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 8 | +0.080 | +1.76€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 15 | +0.331 | +5.92€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 15 | +0.331 | +5.92€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 32 | +0.294 | +6.65€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 328 | +0.051 | +11.28€ | 1 | 0 |
| ✅ STREAK_FADE_15M#15min | 328 | +0.051 | +11.28€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 13 | -0.022 | -3.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 13 | -0.022 | -3.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 64 | +0.030 | -3.55€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 64 | +0.030 | -3.55€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 89 | +0.115 | +19.28€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 89 | +0.115 | +19.28€ | 0 | 2 |
| ✅ STREAK_FADE_15M#XRP | 162 | +0.030 | -0.61€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 162 | +0.030 | -0.61€ | 1 | 1 |
| ✅ STREAK_FADE_5M | 251 | -0.053 | -26.50€ | 3 | 0 |
| ✅ STREAK_FADE_5M#5min | 251 | -0.053 | -26.50€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 48 | -0.140 | -7.57€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 48 | -0.140 | -7.57€ | 1 | 0 |
| ✅ STREAK_FADE_5M#SOL | 96 | -0.031 | -8.64€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 96 | -0.031 | -8.64€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP | 107 | -0.032 | -10.29€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 107 | -0.032 | -10.29€ | 0 | 0 |
| ✅ STREAK_FADE_60M | 6 | -0.075 | -2.08€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 6 | -0.075 | -2.08€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 5 | -0.054 | -1.57€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 5 | -0.054 | -1.57€ | 0 | 0 |
| 🚫 STREAK_MOM_5M | 325 | -0.063 | -27.91€ | 5 | 0 |
| ✅ STREAK_MOM_5M#5min | 325 | -0.063 | -27.91€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 111 | -0.066 | -8.31€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 111 | -0.066 | -8.31€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 116 | -0.017 | -6.25€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 116 | -0.017 | -6.25€ | 2 | 0 |
| ✅ STREAK_MOM_5M#XRP | 98 | -0.110 | -13.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 98 | -0.110 | -13.35€ | 3 | 0 |
| ✅ STRUCT_NO_15M | 766 | +0.033 | +14.70€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 766 | +0.033 | +14.70€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 285 | +0.065 | +16.94€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 285 | +0.065 | +16.94€ | 0 | 1 |
| ✅ STRUCT_NO_15M#ETH | 286 | +0.049 | +8.58€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 286 | +0.049 | +8.58€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 195 | -0.038 | -10.81€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 195 | -0.038 | -10.81€ | 2 | 0 |
| ✅ UPDOWN_GBM | 4055 | +0.059 | +566.17€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 3784 | +0.073 | +607.69€ | 0 | 5 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 138 | -0.079 | -14.22€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 464 | +0.092 | +110.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 464 | +0.092 | +110.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 730 | +0.056 | +77.09€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 644 | +0.084 | +92.60€ | 1 | 7 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 45 | -0.096 | -7.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 412 | +0.031 | +20.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 409 | +0.033 | +21.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1421 | +0.059 | +162.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1326 | +0.071 | +174.75€ | 0 | 4 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 56 | -0.035 | -3.58€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 495 | +0.019 | +47.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 421 | +0.046 | +55.11€ | 2 | 1 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 37 | -0.115 | -2.94€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 531 | +0.095 | +150.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 520 | +0.102 | +153.68€ | 1 | 4 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 323 | +0.306 | +65.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 323 | +0.306 | +65.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 164 | +0.301 | +29.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 164 | +0.301 | +29.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 159 | +0.307 | +36.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 159 | +0.307 | +36.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 3581 | +0.160 | +1817.24€ | 0 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 3581 | +0.160 | +1817.24€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 380 | +0.217 | +282.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 380 | +0.217 | +282.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 466 | +0.034 | +46.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 466 | +0.034 | +46.71€ | 1 | 11 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 366 | +0.196 | +242.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 366 | +0.196 | +242.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 649 | +0.199 | +304.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 649 | +0.199 | +304.19€ | 1 | 15 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 694 | +0.105 | +229.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 694 | +0.105 | +229.08€ | 2 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1026 | +0.195 | +712.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1026 | +0.195 | +712.39€ | 0 | 20 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 33 | -0.014 | -0.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 33 | -0.014 | -0.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 33 | -0.014 | -0.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 33 | -0.014 | -0.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 155 | +0.264 | +83.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 155 | +0.264 | +83.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 86 | +0.227 | +27.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 86 | +0.227 | +27.43€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 69 | +0.303 | +55.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 69 | +0.303 | +55.90€ | 0 | 0 |
| ✅ UPDOWN_OU_5M | 345 | -0.177 | -60.20€ | 7 | 0 |
| ✅ UPDOWN_OU_5M#5min | 345 | -0.177 | -60.20€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 55 | -0.184 | -11.55€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 55 | -0.184 | -11.55€ | 3 | 0 |
| 🚫 UPDOWN_OU_5M#BTC | 35 | -0.203 | -6.11€ | 0 | 0 |
| 🚫 UPDOWN_OU_5M#BTC#5min | 35 | -0.203 | -6.11€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 60 | -0.161 | -10.58€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 60 | -0.161 | -10.58€ | 2 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 37 | -0.192 | -5.89€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 37 | -0.192 | -5.89€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 73 | -0.153 | -9.40€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 73 | -0.153 | -9.40€ | 1 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 85 | -0.167 | -16.68€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 85 | -0.167 | -16.68€ | 9 | 0 |
| ✅ WEEKLY_PRICE | 732 | +0.278 | +326.70€ | 0 | 1 |
| ✅ WEEKLY_PRICE#BTC | 219 | +0.192 | -4.25€ | 0 | 1 |
| ✅ WEEKLY_PRICE#ETH | 220 | +0.234 | +47.04€ | 0 | 2 |
| ✅ WEEKLY_PRICE#SOL | 293 | +0.371 | +283.91€ | 0 | 1 |