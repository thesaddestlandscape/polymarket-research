# Hipótesis automáticas — 2026-08-09 05:20 UTC
_Generado por shadow_postmortem.py sobre 96612 resoluciones (PNL=+14119.01€)_

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
- **PATRÓN** `py_entrada` < `0.36` → IC=+0.260 (n=215)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.36 (IC base=+0.143)

- **PATRÓN** `restante_min` < `4.57` → IC=+0.172 (n=412)

  - _Acción_: Kelly boost +0.86€ cuando `restante_min` < 4.57 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.147 (n=636)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 5.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.148 (n=632)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 18.0 (IC base=+0.143)

- **PATRÓN** `profundidad_ratio_no` > `11.3` → IC=+0.170 (n=280)

  - _Acción_: Kelly boost +0.85€ cuando `profundidad_ratio_no` > 11.3 (IC base=+0.143)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min
- **PATRÓN** `py_entrada` < `0.36` → IC=+0.304 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.36 (IC base=+0.125)

- **PATRÓN** `restante_min` < `4.86` → IC=+0.138 (n=313)

  - _Acción_: Kelly boost +0.69€ cuando `restante_min` < 4.86 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.136 (n=317)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 18.0 (IC base=+0.125)

### FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min
- **PATRÓN** `py_entrada` < `0.43` → IC=+0.193 (n=275)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` < 0.43 (IC base=+0.161)

- **PATRÓN** `restante_min` < `4.16` → IC=+0.215 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `restante_min` < 4.16 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.179 (n=306)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 6.0 (IC base=+0.161)

- **PATRÓN** `profundidad_ratio_no` > `25.4` → IC=+0.231 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `profundidad_ratio_no` > 25.4 (IC base=+0.161)

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

- **PATRÓN** `dist_vwap_pct` < `0.54` → IC=+0.359 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.54 (IC base=+0.351)

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

- **FILTRO** `hora_utc` > `5.0` → IC=-0.333 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 5.0
  - _Potencial_: sin este filtro IC_bueno=-0.222 (n=16)

- **FILTRO** `sigma_ewma_delta_pct` < `5.488` → IC=-0.311 (n=51)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 5.488
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=11)

- **FILTRO** `libro_liquidez` < `4551.0427` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `libro_liquidez` < 4551.0427
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=31)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.054)

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

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 6.463 (IC base=+0.013)

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

- **FILTRO** `sigma_ewma_delta_pct` < `5.022` → IC=-0.365 (n=50)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 5.022
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=11)

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

### GBM_LATE_60M_FADE#SOL#60min
- **FILTRO** `sigma_ewma_delta_pct` < `1.863` → IC=-0.262 (n=19)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 1.863
  - _Potencial_: sin este filtro IC_bueno=-0.100 (n=3)

### GBM_LATE_60M_PYCONFIRMADO
- **FILTRO** `sigma_h` > `0.0067` → IC=-0.206 (n=15)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0067
  - _Potencial_: sin este filtro IC_bueno=+0.060 (n=48)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.4075` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4075 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.572` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 3.572 (IC base=+0.056)

### GBM_LATE_60M_PYCONFIRMADO#SOL#60min
- **FILTRO** `sigma_h` > `0.0051` → IC=-0.152 (n=21)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0051
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
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
- **FILTRO** `liq_usd_total` < `5745.64` → IC=-0.289 (n=17)

  - _Acción_: SKIP cuando `liq_usd_total` < 5745.64
  - _Potencial_: sin este filtro IC_bueno=-0.050 (n=18)

- **FILTRO** `liq_imbalance_60min` |x|≤ `1.0` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `liq_imbalance_60min` |x|≤ 1.0
  - _Potencial_: sin este filtro IC_bueno=-0.119 (n=19)

- **FILTRO** `hora_utc` > `9.0` → IC=-0.265 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 9.0
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=20)

- **FILTRO** `py_entrada` < `0.505` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `py_entrada` < 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.091 (n=20)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

- **FILTRO** `libro_liquidez` < `10825.5484` → IC=-0.196 (n=21)

  - _Acción_: SKIP cuando `libro_liquidez` < 10825.5484
  - _Potencial_: sin este filtro IC_bueno=-0.115 (n=11)

### LIQUIDACIONES_60M
- **FILTRO** `hora_utc` < `15.0` → IC=-0.208 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=20)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.227 (n=20)
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
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=111)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.017 (n=116)

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
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0049 (IC base=+0.080)

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

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.183 (n=645)
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

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.297 (n=146)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0058 (IC base=+0.267)

- **PATRÓN** `drift_60min` |x|≤ `0.1029` → IC=+0.370 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1029 (IC base=+0.267)

- **PATRÓN** `drift_15min` |x|≤ `0.4473` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4473 (IC base=+0.267)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.289 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.267)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.271 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.267)

- **PATRÓN** `ibs_15` < `0.0419` → IC=+0.413 (n=44)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.0419 (IC base=+0.267)

- **PATRÓN** `dist_vwap_pct` > `0.2534` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2534 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.363` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.363 (IC base=+0.267)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.671` → IC=+0.288 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.671 (IC base=+0.267)

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
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.0419 sube el IC de +0.267 a +0.413 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=44). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.7419 sube el IC de +0.107 a +0.296 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=96). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.2632 sube el IC de +0.103 a +0.240 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=167). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.170 a +0.214 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=180). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3571 sube el IC de +0.211 a +0.267 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=256). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min` — IC=+0.438 n=30. Faltan ~10 resoluciones para umbral n≥40. ETA: ~7h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL` — IC=+0.438 n=30. Faltan ~10 resoluciones para umbral n≥40. ETA: ~7h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1804 | +0.047 | -21.77€ | 0 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1804 | +0.047 | -21.77€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 831 | +0.023 | -25.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 831 | +0.023 | -25.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 642 | +0.064 | -16.14€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 642 | +0.064 | -16.14€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 312 | +0.073 | +19.97€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 312 | +0.073 | +19.97€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 2416 | -0.071 | -534.70€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS#15min | 425 | +0.214 | -42.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 1991 | -0.132 | -492.70€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#BNB | 376 | -0.280 | -100.84€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#BNB#5min | 376 | -0.280 | -100.84€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 425 | +0.214 | -42.00€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 425 | +0.214 | -42.00€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS#DOGE | 311 | -0.139 | -65.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 311 | -0.139 | -65.79€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 428 | +0.009 | -17.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 428 | +0.009 | -17.93€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 436 | -0.114 | -64.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 436 | -0.114 | -64.47€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 440 | -0.154 | -243.67€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 440 | -0.154 | -243.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 26225 | +0.119 | -656.45€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 6305 | +0.195 | -118.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 447 | +0.048 | -42.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 17548 | +0.091 | -548.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 1925 | +0.139 | +52.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 2808 | +0.084 | -152.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 12 | +0.000 | -1.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | +0.018 | +2.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 2791 | +0.084 | -153.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 5643 | +0.131 | -92.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1973 | +0.183 | -102.16€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 144 | +0.055 | -14.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 2798 | +0.094 | -40.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 728 | +0.147 | +64.92€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 2806 | +0.077 | -173.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 16 | +0.222 | +8.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 2789 | +0.075 | -183.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 6093 | +0.136 | -16.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 2117 | +0.196 | +1.94€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 147 | -0.017 | -32.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 3201 | +0.105 | -1.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 628 | +0.132 | +15.21€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#SOL | 6040 | +0.135 | -190.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2147 | +0.206 | -23.21€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 148 | +0.100 | +1.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 3176 | +0.087 | -141.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 569 | +0.136 | -27.37€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 2835 | +0.098 | -31.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 40 | +0.143 | -1.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 2793 | +0.098 | -28.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2469 | +0.198 | -178.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 2469 | +0.198 | -178.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 397 | +0.149 | -53.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 397 | +0.149 | -53.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 522 | +0.223 | -14.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 522 | +0.223 | -14.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 407 | +0.145 | -59.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 407 | +0.145 | -59.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 630 | +0.271 | -7.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 630 | +0.271 | -7.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 135 | +0.157 | +0.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 135 | +0.157 | +0.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 378 | +0.161 | -45.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 378 | +0.161 | -45.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 123 | +0.428 | -1.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 123 | +0.428 | -1.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 41 | +0.407 | -0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 41 | +0.407 | -0.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 43 | +0.411 | -1.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 43 | +0.411 | -1.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 30 | +0.438 | +0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 30 | +0.438 | +0.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 11651 | +0.197 | -886.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 11651 | +0.197 | -886.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 2098 | +0.158 | -289.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 2098 | +0.158 | -289.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 1840 | +0.219 | -58.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 1840 | +0.219 | -58.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 2017 | +0.180 | -220.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 2017 | +0.180 | -220.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 1873 | +0.217 | -71.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 1873 | +0.217 | -71.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 1898 | +0.217 | -83.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 1898 | +0.217 | -83.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 1925 | +0.195 | -162.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 1925 | +0.195 | -162.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 822 | +0.143 | +31.02€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 822 | +0.143 | +31.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 414 | +0.125 | -0.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 414 | +0.125 | -0.19€ | 0 | 3 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 408 | +0.161 | +31.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 408 | +0.161 | +31.20€ | 0 | 4 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 312 | +0.274 | -17.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 312 | +0.274 | -17.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 130 | +0.250 | -10.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 130 | +0.250 | -10.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 141 | +0.269 | -8.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 141 | +0.269 | -8.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 41 | +0.337 | +1.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 41 | +0.337 | +1.47€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 118 | +0.367 | -14.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 118 | +0.367 | -14.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 48 | +0.340 | -8.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 48 | +0.340 | -8.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 56 | +0.397 | -4.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 56 | +0.397 | -4.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 14 | +0.175 | -1.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 14 | +0.175 | -1.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 625 | +0.301 | -5.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 625 | +0.301 | -5.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 625 | +0.301 | -5.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 625 | +0.301 | -5.03€ | 0 | 0 |
| ✅ GBM_LATE_15M | 12973 | +0.102 | +4376.54€ | 0 | 5 |
| ✅ GBM_LATE_15M#15min | 12973 | +0.102 | +4376.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 872 | +0.174 | +530.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 872 | +0.174 | +530.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 2592 | +0.084 | +517.10€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2592 | +0.084 | +517.10€ | 0 | 6 |
| ✅ GBM_LATE_15M#DOGE | 894 | +0.176 | +522.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 894 | +0.176 | +522.07€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH | 2401 | +0.063 | +342.89€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2401 | +0.063 | +342.89€ | 0 | 7 |
| ✅ GBM_LATE_15M#SOL | 2908 | +0.070 | +848.10€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2908 | +0.070 | +848.10€ | 1 | 2 |
| ✅ GBM_LATE_15M#XRP | 3306 | +0.133 | +1615.91€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 3306 | +0.133 | +1615.91€ | 0 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 10471 | +0.124 | +5201.82€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 10471 | +0.124 | +5201.82€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 821 | +0.183 | +619.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 821 | +0.183 | +619.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2321 | +0.080 | +765.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2321 | +0.080 | +765.67€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 775 | +0.216 | +627.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 775 | +0.216 | +627.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 2163 | +0.081 | +667.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 2163 | +0.081 | +667.21€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 2288 | +0.073 | +802.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 2288 | +0.073 | +802.56€ | 1 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2103 | +0.214 | +1719.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2103 | +0.214 | +1719.08€ | 0 | 12 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 656 | +0.217 | +495.81€ | 0 | 12 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 656 | +0.217 | +495.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 99 | +0.342 | +117.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 99 | +0.342 | +117.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 119 | +0.136 | +33.04€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 119 | +0.136 | +33.04€ | 0 | 6 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 101 | +0.296 | +102.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 101 | +0.296 | +102.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 83 | +0.159 | +49.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 83 | +0.159 | +49.37€ | 0 | 4 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 126 | +0.094 | +62.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 126 | +0.094 | +62.69€ | 0 | 2 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 128 | +0.277 | +130.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 128 | +0.277 | +130.65€ | 0 | 7 |
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
| ✅ GBM_LATE_15M_TARDIO | 9961 | +0.089 | +3535.94€ | 0 | 5 |
| ✅ GBM_LATE_15M_TARDIO#15min | 9961 | +0.089 | +3535.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 795 | +0.201 | +585.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 795 | +0.201 | +585.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1911 | +0.036 | +276.46€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1911 | +0.036 | +276.46€ | 0 | 3 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 839 | +0.203 | +608.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 839 | +0.203 | +608.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1918 | +0.019 | +149.73€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1918 | +0.019 | +149.73€ | 0 | 2 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 2050 | +0.018 | +369.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 2050 | +0.018 | +369.59€ | 0 | 1 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 2448 | +0.168 | +1545.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 2448 | +0.168 | +1545.64€ | 0 | 10 |
| ✅ GBM_LATE_5M | 1519 | -0.015 | +37.38€ | 5 | 0 |
| ✅ GBM_LATE_5M#5min | 1519 | -0.015 | +37.38€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 315 | +0.030 | +33.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 315 | +0.030 | +33.99€ | 6 | 7 |
| ✅ GBM_LATE_5M#ETH | 116 | -0.144 | -20.03€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 116 | -0.144 | -20.03€ | 5 | 1 |
| ✅ GBM_LATE_5M#SOL | 611 | -0.042 | +13.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 611 | -0.042 | +13.33€ | 9 | 1 |
| ✅ GBM_LATE_5M#XRP | 477 | +0.020 | +10.09€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 477 | +0.020 | +10.09€ | 0 | 0 |
| ✅ GBM_LATE_60M | 398 | -0.075 | +16.84€ | 3 | 1 |
| ✅ GBM_LATE_60M#60min | 398 | -0.075 | +16.84€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 143 | -0.017 | +1.11€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 143 | -0.017 | +1.11€ | 3 | 1 |
| ✅ GBM_LATE_60M#ETH | 138 | -0.086 | +1.12€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 138 | -0.086 | +1.12€ | 4 | 1 |
| ✅ GBM_LATE_60M#SOL | 117 | -0.130 | +14.61€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 117 | -0.130 | +14.61€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE | 125 | -0.311 | -25.36€ | 17 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 125 | -0.311 | -25.36€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 39 | -0.232 | -2.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 39 | -0.232 | -2.70€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 45 | -0.372 | -15.64€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 45 | -0.372 | -15.64€ | 2 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 41 | -0.291 | -7.01€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 41 | -0.291 | -7.01€ | 1 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 106 | +0.018 | -0.02€ | 1 | 3 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 106 | +0.018 | -0.02€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 44 | +0.043 | -0.17€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 44 | +0.043 | -0.17€ | 0 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO#ETH | 9 | -0.102 | -5.58€ | 0 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 9 | -0.102 | -5.58€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 53 | +0.045 | +5.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 53 | +0.045 | +5.73€ | 2 | 0 |
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
| ✅ LIQUIDACIONES_5M | 67 | -0.181 | -13.28€ | 7 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 67 | -0.181 | -13.28€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 19 | -0.158 | -3.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 19 | -0.158 | -3.73€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH | 13 | -0.108 | -2.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#ETH#5min | 13 | -0.108 | -2.61€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL | 17 | -0.246 | -5.67€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL#5min | 17 | -0.246 | -5.67€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 13 | -0.065 | -1.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 13 | -0.065 | -1.72€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M | 100 | +0.020 | -4.32€ | 1 | 1 |
| ✅ LIQUIDACIONES_60M#60min | 100 | +0.020 | -4.32€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 35 | -0.041 | -6.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 35 | -0.041 | -6.96€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 29 | +0.016 | -1.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 29 | +0.016 | -1.08€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 36 | +0.079 | +3.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 36 | +0.079 | +3.71€ | 0 | 0 |
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
| ✅ STREAK_FADE_5M#ETH#5min | 47 | -0.153 | -8.07€ | 1 | 0 |
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
| ✅ STRUCT_NO_15M | 516 | +0.029 | +4.17€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 516 | +0.029 | +4.17€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 178 | +0.050 | +4.41€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 178 | +0.050 | +4.41€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH | 190 | +0.052 | +6.40€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 190 | +0.052 | +6.40€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 148 | -0.027 | -6.65€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 148 | -0.027 | -6.65€ | 2 | 0 |
| ✅ UPDOWN_GBM | 4004 | +0.059 | +563.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 3736 | +0.073 | +603.52€ | 0 | 6 |
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
| ✅ UPDOWN_GBM#ETH | 1388 | +0.058 | +156.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1294 | +0.070 | +167.93€ | 0 | 4 |
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
| ✅ UPDOWN_GBM_15M_TARDIO | 3512 | +0.163 | +1803.21€ | 0 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 3512 | +0.163 | +1803.21€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 380 | +0.217 | +282.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 380 | +0.217 | +282.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 414 | +0.055 | +60.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 414 | +0.055 | +60.45€ | 1 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 366 | +0.196 | +242.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 366 | +0.196 | +242.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 632 | +0.191 | +276.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 632 | +0.191 | +276.42€ | 1 | 14 |
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
## Hipótesis pendientes — tracking automático


### 🔴 Listas para implementar YA

**🔴 H-GBM-18H** — Bloquear hora 18h UTC en GBM
  - _Umbral_: n≥15 y IC<-0.05
  - _Acción_: Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py
  - _Estado_: Confirma: IC=-0.161 n=119 PNL=-29.87€ → añadir 18 a GBM_BLACKLIST_HOURS
  - _Datos_: n=119 IC=-0.161 PNL=-29.87€


### 🟡 Listas para evaluar

**🟡 H-IBS-15** — IBS-15 como señal de mean-reversion
  - _Umbral_: n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets
  - _Acción_: Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py
  - _Estado_: Spread=0.159: overbought→boost, neutral→filtro | oversold(IBS<0.3): IC=+0.115 n=2530 | neutral: IC=+0.043 n=1967 | overbought(IBS>0.7): IC=+0.201 n=2510
  - _Datos_: n=7471 IC=+0.130 PNL=+2527.15€

**🟡 H-HORA-GBM** — hora_utc causal automático en GBM (forward)
  - _Umbral_: n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10
  - _Acción_: El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.
  - _Estado_: H=05h: IC=+0.162 n=131 PNL=+61.09€ → BOOST | H=10h: IC=-0.154 n=15 PNL=-6.77€ → FILTRAR | H=12h: IC=+0.151 n=173 PNL=+57.67€ → BOOST | H=14h: IC=+0.133 n=178 PNL=+57.11€ → BOOST | H=16h: IC=+0.111 n=165 PNL=+42.79€ → BOOST | H=21h: IC=+0.119 n=158 PNL=+36.34€ → BOOST | H=22h: IC=+0.168 n=188 PNL=+61.92€ → BOOST

**🟡 H-OF-PAR** — ORDER_FLOW per-pair delta_ratio ranges
  - _Umbral_: n≥200 por par con delta_ratio feature en shadow
  - _Acción_: Añadir DELTA_MIN/MAX por par dict en shadow_predict.py
  - _Estado_: BTC: 187 ops con delta_ratio | SOL: 237 ops con delta_ratio

**🟡 H-KELLY-HORA** — Kelly boost ×1.2 por celda (estrategia#subtype#dirección#hora)
  - _Umbral_: n≥40 por celda + gate riguroso completo (Wilson+shuffle+PnL bootstrap)
  - _Acción_: Añadir claves 'ESTRATEGIA#SUBTYPE#DIRECCION#HORA':1.2 a meta.hora_boost_factor, solo por celda confirmada
  - _Estado_: 38 celda(s) pasan gate riguroso completo de 159 evaluadas (n>=40) y 336 trackeadas (n>=15). Detalle: kelly_hora_segmentado.json

**⚠️ H-SOL-15MIN** — SOL#15min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: SOL#15min: n≥40 pero IC=+0.046 < 0.08 — monitorear
  - _Datos_: n=421 IC=+0.046 PNL=+55.11€

**🟡 H-WEEKLY** — Predicciones semanales de precio por par
  - _Umbral_: n≥15 por par con IC≥+0.05
  - _Acción_: Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal
  - _Estado_: ETH: n=201/15 IC=+0.224 PNL=+34.18€ | BTC: n=203/15 IC=+0.173 PNL=-10.04€ | SOL: n=278/15 IC=+0.371 PNL=+266.44€

**🟡 H-STREAK-COOLDOWN** — Cooldown tras 2 derrotas consecutivas (mismo subtype)
  - _Umbral_: n≥40 tras 2 losses y gap(IC_tras_win - IC_tras_2loss)≥0.05
  - _Acción_: Reducir stake (no desactivar) 1-2h tras 2 derrotas consecutivas en el mismo subtype
  - _Estado_: tras_win IC=+0.130 n=59078 | tras_1loss IC=+0.086 n=37282 | tras_2loss IC=+0.051 n=15382/40 | gap=+0.079 (umbral 0.05)

**🟡 H-KALMAN** — Kalman filter para drift adaptativo
  - _Umbral_: n≥200 por subtipo para calibrar parámetros Q/R del KF
  - _Acción_: Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py
  - _Estado_: 14 subtypes con n≥200: UPDOWN_GBM, UPDOWN_GBM#SOL, UPDOWN_GBM#ETH, UPDOWN_GBM#BTC, UPDOWN_GBM#SOL#15min
  - _Bloqueante_: N_INSUFICIENTE


### ⏳ Acumulando datos

**⏳ H-WINDOW-MOMENTUM** — Momentum de outcome entre ventanas 15min contiguas
  - _Umbral_: n≥60 alineadas y gap IC≥0.08 vs contrarias — y descartar que sea proxy de drift_15min/60min
  - _Acción_: Si confirma e independiente de drift → capturar prev_window_outcome como feature en shadow_predict y boost ×1.1-1.2 en señales alineadas
  - _Estado_: alineada_con_outcome_prev IC=+0.027 n=182/60 | contraria IC=+0.114 n=68 | gap=-0.087 (umbral 0.08) — verificar independencia de drift_15min/60min antes de actuar

**⏳ H-CROSS-ASSET** — Cross-asset confirmation GBM+OF BUY_NO
  - _Umbral_: n_overlaps≥20 y IC_overlap > IC_base + 0.05
  - _Acción_: Cambiar _aplicar_kelly_compuesto: match por activo, no market_id
  - _Estado_: n_overlaps=49, boost estimado=-0.052. Necesita 0 más y boost>0.05

**⏳ H-60MIN-LIVE** — Estrategias 60min → umbral live (IC≥0.08 n≥40)
  - _Umbral_: IC≥0.08 y n≥40 en cualquier subtipo 60min
  - _Acción_: Activar live cuando haya credenciales Polymarket API
  - _Estado_: ETH#60min: n=55/40 IC=-0.026 PNL=-3.07€ | BTC#60min: n=44/40 IC=-0.087 PNL=-7.18€ | SOL#60min: n=36/40 IC=-0.105 PNL=-2.43€

**⏳ H-BTC-LEADS-ETH** — ETH/SOL GBM contrario al drift_15min de BTC del mismo ciclo
  - _Umbral_: n≥40 en contrario_BTC y gap≥0.08 — y descartar confound con drift propio antes de actuar
  - _Acción_: Si se confirma y no es confound → boost en ETH/SOL cuando decisión contraria a drift_15min BTC
  - _Estado_: alineado_BTC IC=+0.007 n=201 | contrario_BTC IC=-0.032 n=92/40 | gap=-0.039 (umbral 0.08) — SIN CONFIRMAR independencia de filtros propios de ETH


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

**🟡 H-24H-GBM-BUYYES-MADRUGADA** — GBM BUY_YES en madrugada europea (05-07h UTC) — señal alcista
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona en horas 05-07h UTC (7-9h Madrid). IC=+0.087 n=14 a las 06h, +0.063 n=11 a las 05h, +0.067 n=17 a las 07h. Hipótesis: apertura europea genera momentum alcista que el GBM captura. La dirección dominante cambia de BUY_NO (madrugada americana 13h) a BUY_YES (apertura europea). Objetivo: cubrir franja horaria 05-07h UTC en el camino hacia operación 24h.
  - _Umbral_: n≥40 en franja 05-07h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → añadir GBM BUY_YES a subtypes_permitidos_live para horas 05-07h UTC
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.093 > 0.08 con n=187 PNL=+62.19€
  - _Datos_: n=187 IC=+0.093 PNL=+62.19€

**〰️ H-24H-GBM-BUYYES-TARDE** — GBM BUY_YES en tarde europea (15-19h UTC) — señal alcista sostenida
  - _Hipótesis_: Patrón detectado 2026-06-30: GBM BUY_YES funciona consistentemente en 15-19h UTC (17-21h Madrid). IC=+0.136 n=7 a las 17h, +0.097 n=7 a las 19h, +0.080 n=8 a las 15h. Franja de sesión americana donde el mercado tiende a subir. Complementa BUY_NO de las 13-14h. Objetivo: cubrir tarde completa 15-19h UTC.
  - _Umbral_: n≥40 en franja 15-19h y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → habilitar GBM BUY_YES en live para horas 15-19h UTC (además del BUY_NO actual)
  - _Estado_: n=381 IC=+0.027 PNL=+18.80€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=381 IC=+0.027 PNL=+18.80€

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
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.335 > 0.1 con n=574 PNL=+297.75€
  - _Datos_: n=574 IC=+0.335 PNL=+297.75€

**🟡 H-CUSTOM-GBM-17H-BTC** — GBM BTC a las 17h UTC — ¿edge real?
  - _Hipótesis_: La hora 17h UTC aparece como la mejor en historial. ¿Se confirma solo en BTC?
  - _Umbral_: n≥15 y IC>+0.08
  - _Acción_: Boost ×1.2 en GBM BTC a las 17h si se confirma
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.122 > 0.08 con n=35 PNL=+6.48€
  - _Datos_: n=35 IC=+0.122 PNL=+6.48€

**〰️ H-CUSTOM-OF-MADRUGADA** — ORDER_FLOW de madrugada (0h-6h UTC) BTC+SOL — ¿neutralizar?
  - _Hipótesis_: Las horas 0-6h UTC en ORDER_FLOW. El blacklist fue calculado con todos los pares incluyendo los negativos (ETH/XRP/DOGE). ¿Con BTC+SOL sigue siendo negativo?
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Mantener bloqueo si IC<-0.05; desbloquear si IC>0 con n≥30
  - _Estado_: n=113 IC=+0.091 PNL=+15.74€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=113 IC=+0.091 PNL=+15.74€

**〰️ H-CUSTOM-GBM-SIGMA-ALTO** — GBM con sigma_h alto (>0.002/h) — ¿destruye edge?
  - _Hipótesis_: Cuando la volatilidad horaria es muy alta el GBM puede sobreestimar el edge. Testear.
  - _Umbral_: n≥30 y IC<-0.05
  - _Acción_: Filtrar señales GBM cuando sigma_h > 0.002 si se confirma IC negativo
  - _Estado_: n=3828 IC=+0.063 PNL=+569.31€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=3828 IC=+0.063 PNL=+569.31€

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
  - _Estado_: n=46 IC=-0.083 PNL=-5.09€ — sin señal clara aún (umbral IC: min=0.05 max=None)
  - _Datos_: n=46 IC=-0.083 PNL=-5.09€

**🔴 H-CUSTOM-GBM-18H** — GBM a las 18h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.148 con n=11 en GBM a las 18h UTC. P5 del roadmap: bloquear cuando n≥15. Esta hipótesis hace el tracking automático.
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Auto-añadir 18h a GBM_BLACKLIST cuando IC<-0.08 con n≥15 (P5 roadmap)
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.118 < -0.08 con n=226 PNL=-48.80€
  - _Datos_: n=226 IC=-0.118 PNL=-48.80€

**〰️ H-CUSTOM-BUYYES-15MIN-POSTFILTRO** — BUY_YES #15min con filtro drift_60min activo — ¿funciona en forward?
  - _Hipótesis_: El filtro drift_60min ∈ [0,+0.5%) se implementó el 2026-06-26. Datos forward desde 2026-06-27: 8/18 (44%) IC=-0.045. Aún n pequeño. Monitorear si el IC sube a +0.10 con n≥40. ACTUALIZADO 2026-07-05: el filtro NO funciona en forward (27jun-05jul): [0,0.25) IC=-0.018 n=195, [0.25,0.5) IC=-0.071 n=82. Se estrecha DRIFT_60_BUY_YES_15M_HI de 0.5 a 0.25 (quita el tramo peor). Ninguna zona drift es positiva — si el IC forward de [0,0.25) no mejora con n≥250, considerar cerrar BUY_YES #15min por completo (coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO).
  - _Umbral_: n≥40 y IC>+0.10 para confirmar el filtro funciona en forward
  - _Acción_: Filtro estrechado a [0,0.25) el 2026-07-05. Si IC forward sigue <0 con n≥250 en la zona restante → proponer cierre total de BUY_YES #15min en shadow_predict.
  - _Estado_: n=1507 IC=+0.063 PNL=+219.89€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=1507 IC=+0.063 PNL=+219.89€

**🟡 H-CUSTOM-GBM-SIGMA-BAJO** — GBM con sigma_h muy bajo (<0.0018/h, p1 real) — ¿mercado dormido = más predecible?
  - _Hipótesis_: Hipótesis opuesta a sigma_alto: cuando el mercado está muy quieto, ¿el GBM captura mejor la señal porque hay menos ruido? RECALIBRADO 06-Ago (checkpoint 05-Ago, 'sin verificar todavía'): el umbral original (<0.0008) no era imposible (mínimo real 0.000046) pero SÍ prácticamente congelado -- solo 2/7438 filas de UPDOWN_GBM lo cruzan (p0.1 real ya es 0.001068), a ese ritmo n≥30 tardaría ~100+ días. Recalibrado a p1 real (0.0018, n=68 ya disponibles, >>umbral_n=30) -- mismo espíritu 'sigma muy bajo' pero anclado a un percentil real en vez de un número arbitrario.
  - _Umbral_: n≥30 y IC>+0.10
  - _Acción_: Si IC>0.10 con n≥30 → boost ×1.2 en señales GBM con sigma_h<0.0018
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.105 > 0.1 con n=36 PNL=+10.18€
  - _Datos_: n=36 IC=+0.105 PNL=+10.18€

**〰️ H-CUSTOM-BTC15-TENDENCIA** — BTC#15min — ¿el edge está decayendo?
  - _Hipótesis_: Análisis split: primeras 20 ops IC=+0.136 (65%); últimas 20 ops IC=-0.091 (40%). El edge era real pero puede estar desapareciendo. n=43 actual con IC=+0.056 ya bajo umbral. Tracking continuo. ACTUALIZADO 2026-07-02: el agregado IC=-0.022 n=159 mezcla historia pre-filtros. Supervivientes a filtros causales actuales: IC=+0.008 n=131 (break-even). Tercio reciente (30jun-2jul): IC=+0.057. NO desactivar por el agregado — ver H-CUSTOM-BTC15-TARDE para el bolsillo rentable (hora>=16).
  - _Umbral_: n≥50 — si IC<0.04 con n≥50 considerar desactivar BTC#15min
  - _Acción_: NO desactivar por el agregado (confundido por historia pre-filtros). Evaluar sobre supervivientes post-filtro: si IC post-filtro <0 con n>=60 forward → desactivar; si H-CUSTOM-BTC15-TARDE confirma → acotar a tarde en vez de matar.
  - _Estado_: n=628 IC=+0.086 PNL=+95.24€ — sin señal clara aún (umbral IC: min=None max=0.02)
  - _Datos_: n=628 IC=+0.086 PNL=+95.24€

**〰️ H-CUSTOM-DRIFT15-ZONA-MUERTA** — GBM#15min drift_15min ∈ [-0.3,+0.3] — zona muerta de señal
  - _Hipótesis_: Análisis n=127 GBM#15min: cuando drift_15min está entre -0.3 y +0.3 (mercado sin dirección clara) el IC es negativo (-0.043). Cuando drift>0.3 IC=+0.100 (n=28). Cuando drift<-1 IC=+0.048 (reversión). La señal requiere mercado con dirección clara.
  - _Umbral_: n≥50 en zona muerta y IC<-0.03
  - _Acción_: Filtrar señales GBM#15min cuando drift_15min ∈ [-0.3, +0.3] — validar con n≥50 antes de implementar
  - _Estado_: n=80 IC=-0.024 PNL=-1.28€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=80 IC=-0.024 PNL=-1.28€

**🟡 H-CUSTOM-DRIFT15-MOMENTUM** — GBM#15min drift_15min > 0.3 — zona de momentum (señal fuerte)
  - _Hipótesis_: Cuando drift_15min > 0.3%/h el GBM captura bien la dirección: IC=+0.100 n=28 en todos GBM#15min; IC=+0.152 n=13 solo BTC. El mercado tiene dirección clara y el GBM la sigue. Hipótesis: este rango es donde la señal es real.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma IC>0.10 con n≥40 → boost ×1.2 en GBM#15min cuando drift_15min>0.3
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.092 > 0.08 con n=1983 PNL=+363.08€
  - _Datos_: n=1983 IC=+0.092 PNL=+363.08€

**⏳ H-CUSTOM-LONGSHOT-BIAS** — Longshot bias — ¿mejor IC cuando py_mkt < 0.20 o > 0.80?
  - _Hipótesis_: Jon-Becker repo documenta formalmente: contratos a 1-20 cents tienen win_rate < precio implícito (compradores pierden sistemáticamente en longshots). En nuestro sistema: cuando py_mkt<0.20 el GBM predice BUY_NO con edge estructural adicional al del modelo. ¿Se confirma en nuestros datos? Buscar en feature pct_spot_vs_ref si los mercados extremos tienen mejor IC en BUY_NO.
  - _Umbral_: 30
  - _Acción_: Si IC>0.10 con n≥30 en mercados extremos → boost ×1.2 en BUY_NO cuando py_mkt<0.20
  - _Estado_: 28/30 ops en el filtro definido (IC actual=-0.167 PNL=-1.29€)
  - _Datos_: n=28 IC=-0.167 PNL=-1.29€

**〰️ H-CUSTOM-ETH15-REVERSION** — ETH#15min con drift_15min < -1 — ¿mean reversion?
  - _Hipótesis_: ETH y BTC tienen patrones opuestos: BTC funciona con momentum (drift>0.3). ETH funciona con reversión (drift<-1): 9/14 (64%) IC=+0.087. La hipótesis es que ETH tiene más mean-reversion que BTC en 15min.
  - _Umbral_: n≥20 y IC>+0.08
  - _Acción_: Si ETH drift<-1 confirma IC>0.08 con n≥20 → boost ×1.1 en ETH#15min cuando drift_15min<-1
  - _Estado_: n=135 IC=+0.040 PNL=+11.37€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=135 IC=+0.040 PNL=+11.37€

**〰️ H-CUSTOM-GBM-09H** — GBM a las 09h UTC — bloqueada 2026-06-29
  - _Hipótesis_: IC=-0.158 n=19 PNL=-11.62€. Bloqueada manualmente el 2026-06-29 añadiendo hora 9 a meta.gbm_blacklist_hours_auto. Esta hipótesis monitorea que el IC siga siendo negativo para justificar el bloqueo.
  - _Umbral_: n≥25 para confirmar el bloqueo es necesario
  - _Acción_: Si IC sube a >-0.05 con n≥30 → evaluar desbloquear. Si se mantiene <-0.10 → confirmar bloqueo permanente.
  - _Estado_: n=54 IC=-0.054 PNL=-3.82€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=54 IC=-0.054 PNL=-3.82€

**🔴 H-CUSTOM-GBM-10H** — GBM a las 10h UTC — ¿blacklist necesario?
  - _Hipótesis_: IC=-0.175 n=14 PNL=-7.70€. Muy cercano al umbral n≥15 para bloquear. Si IC<-0.08 con n≥15, considerar añadir al blacklist (igual que se hizo con 09h).
  - _Umbral_: n≥15 y IC<-0.08
  - _Acción_: Si IC<-0.08 con n≥15 → añadir 10h a meta.gbm_blacklist_hours_auto en strategy_params.json
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.155 < -0.08 con n=27 PNL=-10.44€
  - _Datos_: n=27 IC=-0.155 PNL=-10.44€

**🟡 H-FUNDING-HIGH-BUYNO** — Funding rate alto (>p90 real ≈0.009%/8h) → BUY_NO tiene más edge
  - _Hipótesis_: Cuando funding perps Binance está en el decil superior real (>0.009%/8h, ver recalibración 06-Ago), los longs están sobrecargados y pagan por mantener. Hipótesis: BUY_NO GBM tiene IC superior en este régimen vs funding neutral. RECALIBRADO 06-Ago: el umbral original (0.03) era FÍSICAMENTE IMPOSIBLE -- el máximo real observado en 5428 filas de UPDOWN_GBM (feature funding_rate_8h = round(fr*100,5), fr=lastFundingRate crudo de Binance) es 0.01, y nunca lo cruzaba -- n=0 desde que se creó, atrapada sin poder acumular ni una fila. Recalibrado a p90 real (percentiles: p50=0.00368, p75=0.00651, p90=0.00943, p95=p99=p100=0.01 -- el feature satura en 0.01 en el 8.4% de las filas, sin evidencia de que sea un bug de captura, no de que sea funding genuinamente extremo). n=332 BUY_NO ya disponibles con el umbral nuevo (>>umbral_n=40), frente a n=0 con el original.
  - _Umbral_: n≥40 y IC>+0.05 diferencial vs baseline
  - _Acción_: Si IC_funding_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en BUY_NO cuando funding_rate_8h > 0.009
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.110 > 0.08 con n=180 PNL=+48.75€
  - _Datos_: n=180 IC=+0.110 PNL=+48.75€

**⏳ H-FUNDING-NEGATIVE-BUYYES** — Funding rate negativo (<-0.01%/8h) → BUY_YES tiene más edge (short squeeze)
  - _Hipótesis_: Cuando funding < -0.01%/8h, los shorts están pagando por mantener la posición. Históricamente precede squeezes en cripto. Hipótesis: BUY_YES GBM tiene IC superior en régimen de funding negativo.
  - _Umbral_: 30
  - _Acción_: Si se confirma → boost ×1.1 en BUY_YES cuando funding_rate_8h < -0.01
  - _Estado_: 0/30 ops en el filtro definido (IC actual=+0.000 PNL=+0.00€)

**〰️ H-LATE-WINDOW-5MIN** — Late-window BTC 5min — arbitraje timing vs Polymarket
  - _Hipótesis_: Inspirado en VyvanseWithMarijuana (36.5% ROI, $42k vol). A T+160-270s dentro de una ventana BTC 5min, si BTC ya se movió >0.3%, Polymarket no ha actualizado precio → edge estructural. Estrategia LATE_WINDOW_5MIN en shadow hasta n≥30. FIX 2026-07-02: la estrategia llevaba 0 predicciones desde su creacion porque HORIZONTE_MIN_HORAS=0.05 (3min) descartaba todo mercado a <3min de expirar — y su zona de entrada (160-270s de una ventana de 5min) deja 30-140s restantes, siempre bajo el suelo. Corregido en shadow_predict (zona late-window marcada _solo_late, 30s-3min, solo evaluada por esta estrategia). El reloj de acumulacion empieza de verdad hoy. Contexto extra: el estudio de ballenas de hoy confirma que comprar el lado ganador a mitad/final de ventana es el playbook comun de los 3 mayores ganadores verificados de estos mercados (Bonereaper +$19.9k/mes, wowitsamazing +$10k/mes, zhangfan151 +$8.7k/mes).
  - _Umbral_: n≥30 y IC>+0.05
  - _Acción_: Si IC≥0.08 con n≥30 → proponer pasar a live con stake mínimo (0.50€). Si IC<0 con n≥30 → el lag de Polymarket en BTC es insuficiente.
  - _Estado_: n=393 IC=-0.062 PNL=-6.68€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=393 IC=-0.062 PNL=-6.68€

**〰️ H-DVOL-SPIKE-BUYNO** — DVOL spike (sigma_h alto) → BUY_NO tiene más edge (panic regime)
  - _Hipótesis_: Inspirado en 'The Volatility Edge' (Concretum Research, 2025): en equities, VIX spikes identifican regímenes de pánico donde los moves están sobreamplificados por feedback loops (deleveraging, hedgers, etc). En cripto el análogo es DVOL (Deribit BTC IV). Sin acceso a DVOL, usamos sigma_h como proxy (vol realizada 1h). Hipótesis: cuando sigma_h > 0.004/h (≈ vol diaria >9.6%), los mercados de predicción exageran la bajada en 15min → BUY_NO tiene IC superior porque el pánico se revierte intraday. Activar cuando n≥200 en BUY_NO #15min para tener potencia suficiente para subdividir por régimen.
  - _Umbral_: n≥200 BUY_NO #15min total, luego n≥40 en subconjunto sigma_h>0.004 y IC>+0.10
  - _Acción_: Si IC_sigma_alto > IC_baseline + 0.08 con n≥40 → boost ×1.2 en BUY_NO cuando sigma_h>0.004. Pendiente integrar DVOL real (Deribit API) cuando n≥500.
  - _Estado_: n=2106 IC=+0.072 PNL=+324.53€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=2106 IC=+0.072 PNL=+324.53€

**〰️ H-CUSTOM-POLY-DRIFT-CONFIRM** — poly_drift_5obs: ¿el precio YES interno de Polymarket confirma nuestra señal?
  - _Hipótesis_: Feature nueva 2026-06-27: drift del precio YES en Polymarket en últimas 5 obs (~5min). Si poly_drift<0 y decidimos BUY_NO (o poly_drift>0 y BUY_YES) → confluencia. Si diverge → reducción de stake. Hipótesis: confluencia Binance+Polymarket mejora IC; divergencia empeora.
  - _Umbral_: n≥40 en confluencia vs divergencia para validar el boost ×1.1
  - _Acción_: Si IC_confluencia>IC_divergencia con n≥40 → mantener el boost. Si no → retirar.
  - _Estado_: n=698 IC=+0.071 PNL=+83.94€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=698 IC=+0.071 PNL=+83.94€

**〰️ H-CUSTOM-OF-VOLUMEN-ALTO** — ORDER_FLOW_5M con total_vol_5m alto — ¿volumen extremo mejora el IC?
  - _Hipótesis_: Inspirado en un artículo sobre 'volume trading strategy' (mean-reversion en SPY): la idea es que un mismo movimiento de precio con volumen inusualmente alto refleja pánico/liquidación forzada y tiene más probabilidad de revertir que el mismo movimiento con volumen normal. No es transplantable tal cual (esa estrategia opera en barras diarias de SPY, nosotros en ventanas de 15-60min de cripto), pero el feature total_vol_5m ya se captura en cada predicción de ORDER_FLOW_5M (shadow_predict.py) y nunca se ha usado como filtro independiente — solo sirve de denominador para calcular delta_ratio. Hipótesis: dentro de las señales que ya pasan el filtro de delta_ratio, un total_vol_5m alto (volumen real, no solo desequilibrio) mejora el IC. Distribución real en predictions_*.csv (n=843): mediana=1696, p75=108522 (muy asimétrica) — se usa p75 como umbral de 'volumen alto'.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC_volumen_alto > IC_baseline + 0.05 con n≥40 → boost ×1.1 en ORDER_FLOW_5M cuando total_vol_5m>100000
  - _Estado_: n=394 IC=-0.010 PNL=-9.77€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=394 IC=-0.010 PNL=-9.77€

**🟡 H-CUSTOM-CROSS-WINDOW-SPREAD-POS** — GBM 15min/60min: spread positivo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Inspirado en un artículo sobre bots de Polymarket: mercados de distinta duración del mismo activo (ej. BTC#15min vs BTC#60min) no repriciician a la misma velocidad — uno puede quedarse rezagado tras un movimiento. Si el spread entre ambos se sale de lo normal, puede indicar que uno de los dos aún no ha incorporado la información que el otro ya tiene. No es transplantable tal cual (el artículo lo usa para arbitraje comprando ambos lados a la vez, algo que no hacemos — ver idea_bidirectional_accumulation aparcada), pero el feature cross_window_spread (precio_yes propio menos precio_yes de la ventana relacionada, sin normalizar aún por z-score) ya se captura para GBM#15min (contra 60min) y GBM#60min (contra 15min) desde el 2026-07-01, sin cambiar ninguna decisión. Esta hipótesis cubre el lado positivo (mercado propio más caro que el relacionado); ver H-CUSTOM-CROSS-WINDOW-SPREAD-NEG para el lado negativo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread, y evaluar si merece la pena normalizar a z-score con más histórico
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.234 > 0.08 con n=303 PNL=+66.72€
  - _Datos_: n=303 IC=+0.234 PNL=+66.72€

**〰️ H-CUSTOM-CROSS-WINDOW-SPREAD-NEG** — GBM 15min/60min: spread negativo alto de precio_yes contra la ventana relacionada
  - _Hipótesis_: Lado negativo de H-CUSTOM-CROSS-WINDOW-SPREAD-POS (mercado propio más barato que el relacionado). Mismo feature cross_window_spread, mismo origen (artículo sobre bots de Polymarket), umbral simétrico.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si se confirma con n≥40 → considerar boost/filtro por cross_window_spread
  - _Estado_: n=275 IC=+0.034 PNL=+65.10€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=275 IC=+0.034 PNL=+65.10€

**〰️ H-CUSTOM-MOON-LLENA** — Fase lunar: ¿rendimiento peor cerca de luna llena?
  - _Hipótesis_: Inspirado en el paper de Fornero (2023, 43 Jornadas SADAF) sobre astrología financiera: 5 estudios peer-review (Dichev & Janes 2003, Yuan et al. 2006, Keef & Khaled 2011, Floros & Tan 2013, Liu & Tseng 2009) en 25-62 mercados bursátiles encuentran rendimientos 5-10%/año más bajos cerca de luna llena que de luna nueva. El propio paper es escéptico de la astrología como tal, pero el mecanismo que documenta no es místico: sesgo de humor de inversores minoristas (más fuerte en acciones con dominancia retail, casi nulo en institucional). Polymarket es un mercado muy retail/cripto — hipótesis: si el mecanismo transfiere, debería verse peor IC cerca de luna llena (moon_phase≈0.5) que en el resto del ciclo.
  - _Umbral_: n≥200 PERO ADEMÁS necesita cubrir al menos 3 ciclos lunares completos (~90 días de calendario) — no evaluar solo por n, aunque el volumen diario ya lo cruce en horas
  - _Acción_: Si IC cerca de luna llena < IC resto del ciclo con margen ≥0.05 y ≥3 ciclos lunares cubiertos → considerar boost/filtro por moon_phase. No implementar con menos de 3 ciclos aunque n sea alto — el efecto es de calendario lento, no de volumen.
  - _Estado_: n=11007 IC=+0.107 PNL=+3126.54€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=11007 IC=+0.107 PNL=+3126.54€

**〰️ H-CUSTOM-MERCURY-RETROGRADO** — Mercurio retrógrado: ¿rendimiento peor durante la ventana?
  - _Hipótesis_: Mismo origen que H-CUSTOM-MOON-LLENA (paper de Fornero, 43 Jornadas SADAF 2023). Qi, Wang & Zhang (2022, 48 mercados, 1973-2019): rendimientos 3.33%/año más bajos durante Mercurio retrógrado. Kou & Ma (2022) en China (99.8% cuentas retail): hasta -31% anualizado. Ambos estudios confirman que el mecanismo es la creencia/superstición de inversores retail (mayor efecto cuanto más retail y más supersticioso el mercado), no un efecto astral literal — Polymarket encaja en ese perfil. Ventanas 2026 (fuente pública, actualizar cada año): 26-feb a 20-mar, 29-jun a 23-jul, 24-oct a 13-nov.
  - _Umbral_: n≥100 PERO ADEMÁS necesita cubrir al menos 2-3 ventanas de retrogradación distintas (no solo la de jun-jul 2026) — esperar mínimo hasta después de la ventana de oct-nov 2026
  - _Acción_: Si IC en mercury_retrogrado=1 < IC en mercury_retrogrado=0 con margen ≥0.05 y ≥2 ventanas distintas cubiertas → considerar boost/filtro. No implementar tras una sola ventana (jun-jul 2026) por more que n sea alto — sería solo un evento, no un patrón.
  - _Estado_: n=27547 IC=+0.113 PNL=+6842.82€ — sin señal clara aún (umbral IC: min=None max=-0.03)
  - _Datos_: n=27547 IC=+0.113 PNL=+6842.82€

**〰️ H-CUSTOM-SMART-MONEY-CONSENSUS** — Consenso de wallets 'smart money' — ¿confirma nuestra dirección?
  - _Hipótesis_: Javi propuso estudiar bots/wallets que operan bien en nuestros mismos mercados. En vez de creer artículos (ya verificamos 2 veces esta semana que las narrativas no aguantan el cruce con datos reales), smart_money_tracker.py mide el track record REAL de wallets activas en BTC/ETH/SOL/XRP Up-or-Down 5/15/60min vía data-api.polymarket.com/positions, filtrado a posiciones 'Up or Down'. Clasifica como 'smart' las wallets con n>=10 posiciones, win_rate>=0.55 y pnl_total>0. smart_money_consensus es el sesgo direccional reciente (Up-Down)/(Up+Down) de esas wallets 'smart' por activo. Hipótesis: si nuestra decisión (BUY_YES/BUY_NO) coincide con el consenso smart money, mejor IC que cuando diverge. RESET METODOLOGICO 2026-07-02: la clasificacion 'smart' original via /positions estaba INVERTIDA para wallets de alta frecuencia (el endpoint solo retiene el residuo perdedor sin redimir; verificado: 'wowitsamazing' figuraba como -$478k y es +$10k/mes en el leaderboard oficial). Desde 2026-07-02T06:12Z el consenso se construye solo con wallets verificadas en el leaderboard oficial (pnl_mes>=$1000, 24 wallets). Los valores de smart_money_consensus capturados en features ANTES de esa fecha provienen de la clasificacion rota — descontar ese tramo al evaluar.
  - _Umbral_: n≥40 y IC>+0.08 — además necesita que existan wallets 'smart' acumuladas (0 al empezar, se van descubriendo cada ciclo)
  - _Acción_: Si IC en confluencia (decisión coincide con signo de smart_money_consensus) supera en >=0.05 al IC en divergencia, con n≥40 en cada lado → boost ×1.1-1.2 cuando coincide, considerar reducir stake cuando diverge fuerte.
  - _Estado_: n=582 IC=+0.053 PNL=+64.59€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=582 IC=+0.053 PNL=+64.59€

**🟡 H-CUSTOM-OF-EDGE-ALTO** — ORDER_FLOW_5M: edge alto (>0.20) rinde mejor que edge cerca del suelo
  - _Hipótesis_: Analizado 2026-07-01 sobre 794 resoluciones de ORDER_FLOW_5M: edge_neto en [0.025,0.198) -> IC=-0.009 (n=397, PNL=-10.49€) vs edge_neto en [0.198,0.385] -> IC=+0.029 (n=397, PNL=+16.43€). Comprobado que NO es un efecto general: en UPDOWN_GBM el patrón se invierte (edge bajo IC=-0.002 vs edge alto IC=-0.033), así que este filtro debe quedar scoped solo a ORDER_FLOW_5M, no aplicarse a otras estrategias. CORREGIDO 2026-07-01 (mismo día, encontrado por auditoría): el filtro original usaba 'edge_neto' con solo feature_lo, pero edge_neto está firmado por dirección (negativo en BUY_NO, positivo en BUY_YES) y ORDER_FLOW_5M solo genera BUY_NO desde 2026-06-25 — el filtro nunca podía matchear ningún BUY_NO real, solo el remanente BUY_YES histórico de antes del 25-jun (n=151, datos muertos, no crecen hacia adelante). Cambiado a 'edge_direccional' (siempre positivo, = abs(edge_neto)) + decision=BUY_NO explícito. Con el fix: n=227, IC=+0.0502, PNL=+19.15€ — señal real y viva.
  - _Umbral_: n≥80 en cada mitad (bajo/alto) para confirmar con más margen que el análisis inicial
  - _Acción_: Si se confirma con n≥80 y el gap se mantiene ≥0.03 → subir EDGE_MINIMO solo para ORDER_FLOW_5M a ~0.20 (o escalar Kelly con la magnitud del edge)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.035 > 0.02 con n=456 PNL=+22.18€
  - _Datos_: n=456 IC=+0.035 PNL=+22.18€

**〰️ H-CUSTOM-PRICETARGET-BUYYES-MALO** — PRICE_TARGET_GBM BUY_YES estructuralmente roto (BUY_NO no)
  - _Hipótesis_: Analizado 2026-07-01: BTC#atexpiry BUY_YES 2/16 (12%) IC=-0.267 PNL=-8.83€; ETH#atexpiry BUY_YES 2/8 (25%) IC=-0.080 PNL=-3.70€. Mientras BUY_NO en ambos activos está en break-even (IC≈0 a +0.02). Prácticamente toda la sangría de la estrategia completa (-13€ de -13.08€ totales) es BUY_YES. Podría rescatar una estrategia que hoy está en la lista de revisar-desactivación.
  - _Umbral_: n≥30 en BUY_YES y IC<-0.15 para confirmar bloqueo
  - _Acción_: Si se confirma con n≥30 → filtro causal decision==BUY_YES → skip en PRICE_TARGET_GBM, dejar solo BUY_NO activo
  - _Estado_: n=82 IC=-0.107 PNL=+16.08€ — sin señal clara aún (umbral IC: min=None max=-0.15)
  - _Datos_: n=82 IC=-0.107 PNL=+16.08€

**〰️ H-CUSTOM-WEEKLY-INRANGE-BUYYES** — WEEKLY_PRICE BUY_YES con in_range=1 — ¿estructuralmente sobrevalorado?
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_YES cuando in_range=1 fue 0/3 (todo pérdida). Mecanismo propuesto: acertar un rango de precio estrecho al vencimiento es intrínsecamente poco probable, el mercado puede estar sobrevalorando el 'sí'. Ver H-CUSTOM-WEEKLY-PCTDIST-BUYNO para el lado complementario (BUY_NO con pct_dist alto).
  - _Umbral_: n≥25 y IC<-0.10 para confirmar (evidencia inicial es de solo 3 ops)
  - _Acción_: Si se confirma con n≥25 → filtro causal in_range==1 + BUY_YES → skip en WEEKLY_PRICE
  - _Estado_: n=81 IC=-0.030 PNL=+3.88€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=81 IC=-0.030 PNL=+3.88€

**🟡 H-CUSTOM-WEEKLY-PCTDIST-BUYNO** — WEEKLY_PRICE BUY_NO con pct_dist alto — cuanto más lejos del rango, más seguro
  - _Hipótesis_: Analizado 2026-07-01, n=10 (evidencia mínima): BUY_NO con pct_dist>=2.09% fue 4/4 victorias (rango 2.09%-23.4%); BUY_NO con pct_dist<8% (pero fuera del corte anterior) tuvo derrotas. Patrón: cuanto más lejos está el spot del rango objetivo al momento de la predicción, más fiable el BUY_NO. Complementa H-CUSTOM-WEEKLY-INRANGE-BUYYES.
  - _Umbral_: n≥25 y IC>+0.10 para confirmar
  - _Acción_: Si se confirma con n≥25 → boost ×1.2 en WEEKLY_PRICE BUY_NO cuando pct_dist≥2
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.429 > 0.1 con n=392 PNL=+329.25€
  - _Datos_: n=392 IC=+0.429 PNL=+329.25€

**〰️ H-CUSTOM-GBM-BUYYES-GLOBAL-MALO** — UPDOWN_GBM BUY_YES global — ¿estructuralmente peor que BUY_NO en todas las estrategias activas?
  - _Hipótesis_: Analizado 2026-07-01: patrón cross-estrategia consistente en las 4 estrategias activas — BUY_NO gana a BUY_YES sin excepción (UPDOWN_GBM IC=+0.058 n=154 vs -0.046 n=412; ORDER_FLOW_5M +0.053 n=439 vs -0.043 n=355; PRICE_TARGET_GBM +0.011 n=45 vs -0.267 n=28; WEEKLY_PRICE +0.115 n=50 vs -0.315 n=25). Mecanismo propuesto: sesgo retail comprando 'Up'/'YES' en cripto infla el precio de YES por encima de su valor justo en Polymarket — consistente con la sobreconfianza del modelo en probabilidades altas de YES detectada en la calibración Platt (ver idea_calibracion_platt). ORDER_FLOW_5M (solo genera BUY_NO desde 2026-06-25) y WEEKLY_PRICE (H-WEEKLY-BUYNO) ya actúan sobre este mismo patrón; UPDOWN_GBM y PRICE_TARGET_GBM (ver H-CUSTOM-PRICETARGET-BUYYES-MALO) todavía no tienen un tratamiento sistemático equivalente, solo filtros puntuales por hora/subtipo.
  - _Umbral_: n≥50 y IC<-0.05 para confirmar bloqueo global (a día de hoy ya está en n=412, IC=-0.046 — muy cerca)
  - _Acción_: Si se confirma con n≥50 → exigir evidencia direccional más fuerte por subtipo antes de permitir BUY_YES en live (barra asimétrica frente a BUY_NO), en vez de auto-desactivar de golpe todo BUY_YES de GBM
  - _Estado_: n=1657 IC=+0.044 PNL=+189.34€ — sin señal clara aún (umbral IC: min=None max=-0.05)
  - _Datos_: n=1657 IC=+0.044 PNL=+189.34€

**🟡 H-CUSTOM-LATE-ENTRY-15MIN** — Entrada tardía en ventanas 15min (T_h<0.2) — el edge vive al final de la ventana
  - _Hipótesis_: Detectado 2026-07-02 sobre results.csv: GBM#15min con T_h<0.2 (≤12min restantes al predecir) IC=+0.279 n=61 PNL=+6.38€, vs entrada temprana (T_h≥0.2) IC=-0.024 n=123. Por buckets: T_h 0.15-0.2 (9-12min) IC=+0.353 n=34; T_h 0.08-0.15 (5-9min) IC=+0.217 n=23. Sin confound aparente: las 61 ops tardías están repartidas entre 5 pares, 19 horas distintas y 8 fechas. Mecanismo: con menos tiempo restante la varianza residual cae y el drift observado pesa más en el outcome, pero Polymarket sigue cotizando cerca de 50/50 — mismo mecanismo que el bot VyvanseWithMarijuana explota en ventanas de 5min (H-LATE-WINDOW-5MIN), aplicado a 15min donde hay menos competencia. Hoy las entradas tardías solo ocurren por accidente (mercado descubierto tarde); si confirma, hacerlas deliberadas.
  - _Umbral_: n≥120 y IC>+0.10 (el n=61 del descubrimiento está incluido — exigir ~doble para confirmar forward)
  - _Acción_: Si confirma → segunda pasada deliberada en shadow_predict a mitad de ventana 15min (re-evaluar mercados ya vistos con T_h<0.2), y considerar variante live con la misma barra IC≥0.08 n≥40
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.165 > 0.1 con n=1635 PNL=+566.00€
  - _Datos_: n=1635 IC=+0.165 PNL=+566.00€

**〰️ H-CUSTOM-BUYNO-LONGSHOT-15MIN** — BUY_NO longshot en 15min (py_mkt≥0.55) — comprar NO barato pierde
  - _Hipótesis_: Detectado 2026-07-02: GBM#15min BUY_NO con precio_yes_mercado≥0.55 (NO cotiza <0.45, es underdog) IC=-0.333 n=21 PNL=-9.03€, mientras BUY_NO en zona moneda py∈[0.45,0.55) IC=+0.162 n=167 PNL=+31.94€. Es el mismo favorite-longshot bias que documenta Jon-Becker, pero aplicado a nuestro lado NO: cuando el mercado ya cree que sube, comprar NO barato es apostar contra el favorito y pierde sistemáticamente. Complementa H-CUSTOM-LONGSHOT-BIAS (que mide el lado py<0.20 y va mal: IC=-0.133 n=16 — coherente con esta).
  - _Umbral_: n≥40 y IC<-0.10
  - _Acción_: Si confirma → filtro causal en shadow_predict: skip BUY_NO en #15min cuando py_mkt≥0.55 (equivale a exigir que NO sea favorito o moneda justa)
  - _Estado_: n=85 IC=-0.029 PNL=+19.12€ — sin señal clara aún (umbral IC: min=None max=-0.1)
  - _Datos_: n=85 IC=-0.029 PNL=+19.12€

**🟡 H-CUSTOM-XRP15-BUYNO-LIVE** — XRP#15min BUY_NO — candidato live nº2 (detrás de ETH#15min)
  - _Hipótesis_: Detectado 2026-07-02: XRP#15min BUY_NO IC=+0.257 n=35 PNL=+8.53€ (vs BUY_YES IC=-0.143 n=21 — mismo patrón direccional que ETH). Además el postmortem ya le descubrió patrón ganador propio: sigma_h<0.0125 → IC=+0.200 n=18. XRP es el único par además de ETH con IC positivo sostenido en 15min. Objetivo: segundo subtype live para diversificar — ETH#15min es hoy la única señal con dinero real y un solo subtype es fragilidad estructural (si su edge decae como pasó con BTC#15min, live se queda a cero).
  - _Umbral_: n≥50 y IC>+0.10 (barra live es n≥40 IC≥0.08; se exige margen porque el n=35 del descubrimiento está incluido)
  - _Acción_: Si confirma con n≥50 → proponer añadir XRP#15min a la operativa live (ya cumple estrategias_permitidas_live=UPDOWN_GBM; revisar liquidez del libro XRP antes)
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.116 > 0.1 con n=482 PNL=+155.71€
  - _Datos_: n=482 IC=+0.116 PNL=+155.71€

**〰️ H-CUSTOM-DAILY-BUYNO** — UPDOWN_GBM#daily BUY_NO — el sesgo anti-YES amplificado en ventanas diarias
  - _Hipótesis_: Detectado 2026-07-02: BUY_NO en ventanas daily va 7/8 (BTC 3/3, ETH 2/2, SOL 2/3), IC=+0.750 n=8 PNL=+11.64€ — el agregado daily completo (IC=+0.110 n=15, único subtipo-ventana de GBM en verde) lo sostiene íntegramente la pata BUY_NO. Mecanismo: extensión de H-CUSTOM-GBM-BUYYES-GLOBAL-MALO — el sesgo retail 'Up' debería ser MÁS fuerte en daily que en 15min (la apuesta optimista direccional de largo plazo es la apuesta retail típica), y en daily el drift damping del GBM importa menos. n mínimo, pero el prior direccional viene de n=507 del patrón global confirmado.
  - _Umbral_: n≥20 y IC>+0.10
  - _Acción_: Si confirma con n≥20 → subir apuesta_kelly del subtipo daily en shadow y trackear hacia barra live (n≥40); daily genera ~1 op/día/par — considerar añadir pares (XRP/DOGE/BNB) para acumular más rápido
  - _Estado_: n=30 IC=-0.188 PNL=+2.99€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=30 IC=-0.188 PNL=+2.99€

**〰️ H-CUSTOM-BTC15-TARDE** — BTC#15min en tarde UTC (hora>=16) — el bolsillo rentable dentro de un subtipo mediocre
  - _Hipótesis_: Detectado 2026-07-02 al analizar si BTC#15min es rescatable en vez de desactivarla: sobre los supervivientes a los filtros causales actuales, hora_utc>=16 da IC=+0.385 n=26 PNL=+4.16€, mientras el agregado del subtipo es IC=-0.044 n=159. Convergen 3 señales independientes: el patron ganador del postmortem (BUY_YES hora>17 IC=+0.125 n=22), H-KELLY-HORA (17h IC=+0.221 n=41 global) y este split. Ademas el tercio temporal reciente (30-jun a 2-jul, ya con filtros activos) esta en IC=+0.057 — el 'declive' de H-CUSTOM-BTC15-TENDENCIA mezclaba historia pre-filtros. CAVEAT: n=26 y encontrado explorando varios splits (riesgo de comparaciones multiples) — la convergencia con las otras 2 señales mitiga pero no elimina; exigir confirmacion forward.
  - _Umbral_: n>=50 y IC>+0.10 en forward
  - _Acción_: Si confirma con n>=50 → candidato live acotado a horas 16-23 UTC (la ventana 15:00-21:30 Madrid ya cubre 14-19:30 UTC, encaja); si ademas H-KELLY-HORA confirma → boost conjunto
  - _Estado_: n=284 IC=+0.070 PNL=+12.72€ — sin señal clara aún (umbral IC: min=0.1 max=None)
  - _Datos_: n=284 IC=+0.070 PNL=+12.72€

**⏳ H-CUSTOM-ETH15-BUYNO-PRECIO-ALTO** — ETH#15min BUY_NO con precio_yes>0.55 pierde (NO longshot contra favorito)
  - _Hipótesis_: Detectado 2026-07-02: ult.60 shadow ETH15 BUY_NO — py_mkt~0.5 wr=0.67 PNL=+29.3 (n=49); py_mkt 0.6-0.8 wr 0.33-0 PNL=-5.75 (n=9). Filtro RETURN NONE (no SKIP) aplicado en shadow_predict.py (PY_MKT_MAX_BUY_NO_ETH15=0.55) el mismo dia -- bloquea la GENERACIÓN de la fila, no solo la decisión. Esta hipotesis trackea la zona filtrada: si las ops que HABRIAN caido aqui siguen apareciendo en otras estrategias o el IC forward de la zona se vuelve positivo, revisar el filtro. CAVEAT: n=9, muestra chica — el filtro se aplico por asimetria de riesgo (afecta a dinero live), no por significancia. ⚠️ 05-Ago (fix): la clave del filtro decía 'py_mkt', que NUNCA existió ni en features de UPDOWN_GBM (T_h/delta_ratio_macro/drift_15min/drift_60min/pct_spot_vs_ref/sigma_h) ni como columna top-level de results.csv -- corregida a 'precio_yes_mercado' (columna real). Aun así, con la clave correcta esta hipótesis NUNCA podrá acumular n mientras el filtro RETURN NONE siga activo -- es el mismo patrón 'frozen by design' que H-CUSTOM-LATE15-PHOTO-FINISH (más abajo): la propia protección impide generar los datos necesarios para volver a evaluarla. Para monitorearla de verdad haría falta un logger separado que capture la señal SIN aplicar el filtro (mismo patrón que gate_bucket_propio con data/markets histórico) -- no construido, pendiente decisión.
  - _Umbral_: 20
  - _Acción_: Si IC forward de la zona >0 con n>=20 → retirar filtro; si confirma negativo → considerar extender a BTC/SOL 15min
  - _Estado_: 10/20 ops en el filtro definido (IC actual=-0.042 PNL=-4.06€)
  - _Datos_: n=10 IC=-0.042 PNL=-4.06€

**〰️ H-PRECIO-YES-BARATO** — BUY_YES con precio de mercado 0.30-0.40 — mercado infravalora YES
  - _Hipótesis_: Detectado 2026-07-03 en benchmark de calibración del mercado (7d, estrategias GBM): en el bucket precio_yes_mercado [0.3-0.4) la frecuencia real de YES fue 0.45 vs 0.35 implícito (+0.10, n=38). Posible sesgo favorito-longshot suave en binarios de 15min (complemento del LONGSHOT ya activo para BUY_NO con py<0.20). Si se confirma, BUY_YES comprado en esa banda lleva viento de cola estructural del propio mercado, independiente del modelo.
  - _Umbral_: n≥40 y IC>+0.08
  - _Acción_: Si IC>+0.08 con n≥40 → kelly_boost ×1.1 para BUY_YES con precio_yes_mercado en [0.30,0.40), simétrico al longshot BUY_NO existente
  - _Estado_: n=1705 IC=-0.082 PNL=+397.79€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=1705 IC=-0.082 PNL=+397.79€

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
  - _Estado_: n=1487 IC=+0.068 PNL=+171.70€ — sin señal clara aún (umbral IC: min=None max=0.03)
  - _Datos_: n=1487 IC=+0.068 PNL=+171.70€

**🟡 H-CUSTOM-BUYYES15-SOLO-TARDIO** — UPDOWN_GBM BUY_YES #15min solo tardío (T_h<0.2) — gate forward hacia live
  - _Hipótesis_: Implementado 2026-07-06 (BUY_YES_15M_TH_MAX=0.2 en shadow_predict): BUY_YES #15min solo se permite en zona tardía. Motivo medido: temprana IC=-0.062 n=404 PNL=-46.2€ vs tardía IC=+0.123 n=51 — el sesgo retail 'Up' infla el YES al inicio de la ventana y se disuelve cerca del cierre (mismo mecanismo que GBM_LATE_15M BUY_YES +0.119 n=672, y coherente con H-CUSTOM-GBM-BUYYES-GLOBAL-MALO y H-CUSTOM-LATE-ENTRY-15MIN). El skip temprano deja el mercado sin predecir y el loop lo re-evalúa → la entrada tardía es deliberada, no accidental. CAVEAT: el n=51 tardío es retrospectivo y multi-par; esta hipótesis mide el FORWARD post-implementación con la barra live (n≥40 IC≥0.08). No proponer live sin además comprobar solapamiento con GBM_LATE_15M (misma ventana/mercados → correlación, techo 2 posiciones misma dirección).
  - _Umbral_: n≥40 forward y IC>+0.08 (barra live estándar)
  - _Acción_: Si confirma forward con n≥40 IC≥0.08 → discutir whitelist live SOLO si aporta algo que GBM_LATE_15M no cubre (franja T_h u ocasiones distintas); si IC<0 con n≥40 → cerrar BUY_YES #15min por completo (culmina H-CUSTOM-BUYYES-15MIN-POSTFILTRO).
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.109 > 0.08 con n=1103 PNL=+266.14€
  - _Datos_: n=1103 IC=+0.109 PNL=+266.14€

**🟡 H-CUSTOM-GBM-04H-ASIA** — UPDOWN_GBM 04h-05h UTC — media sesión asiática, ¿mejor franja nocturna?
  - _Hipótesis_: Detectado 2026-07-06 al evaluar si la apertura china (01:30 UTC) merece ventana: la apertura en sí es NEGATIVA (01h IC=0.000, 02h IC=-0.066 — mismo mecanismo que los opens US 9/10/18h: flujo informado rompe el GBM), pero la media sesión asiática 04h-05h UTC es la mejor franja nocturna sin ventana: UPDOWN_GBM+GBM_LATE 04h IC=+0.112 n=96, 05h IC=+0.067 n=125, +63€. Mecanismo: mercado tranquilo, sigma baja — coherente con el patrón causal sigma_h<0.0084→IC=+0.125 confirmado el mismo día. CAVEATS: (1) mejor-de-9-horas mirado a posteriori — sesgo de selección, por eso barra n≥40 forward; (2) el shadow no mide fill-ability y a las 04h UTC los libros pueden estar vacíos — medir profundidad con libro_snapshots (motivo fuera_ventana, 24/7) antes de proponer ventana live 06:00-07:00 Madrid. Ver gemela H-CUSTOM-LATE-04H-ASIA. BASELINE 2026-07-06: n=62 IC=-0.016 — en UPDOWN_GBM la franja es PLANA (el edge agregado que motivó la hipótesis era de GBM_LATE); umbral_n=102 para que la evaluación sea forward (+40 sobre baseline).
  - _Umbral_: n≥102 (baseline 62 + 40 forward) y IC>+0.08
  - _Acción_: Si confirma IC≥0.08 n≥40 forward Y la profundidad de libro a 04-05h es viable → proponer a Javi ventana live 06:00-07:00 Madrid (decisión suya, dinero real). Si IC<0 con n≥40 → archivar y no volver a mirar horas sueltas sin mecanismo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.087 > 0.08 con n=313 PNL=+57.16€
  - _Datos_: n=313 IC=+0.087 PNL=+57.16€

**🟡 H-CUSTOM-LATE-04H-ASIA** — GBM_LATE_15M 04h-05h UTC — media sesión asiática (gemela de GBM-04H-ASIA)
  - _Hipótesis_: Gemela de H-CUSTOM-GBM-04H-ASIA para la estrategia live principal (GBM_LATE_15M). El tracker no soporta dos strategy_prefix en un filtro — mismas horas, misma barra, misma acción. Se evalúan por separado y solo se propone ventana si AMBAS confirman o la que confirme tiene n≥40 propio. BASELINE 2026-07-06: n=112 IC=+0.123 PNL=+40.09€ — retrospectivo ya positivo, pero es el mismo dato que generó la hipótesis (sesgo de selección). umbral_n=152 exige 40 resoluciones forward antes de confirmar. El edge 04-05h es de GBM_LATE, no de UPDOWN_GBM (ver gemela: plana).
  - _Umbral_: n≥152 (baseline 112 + 40 forward) y IC>+0.08
  - _Acción_: Ver H-CUSTOM-GBM-04H-ASIA — misma decisión conjunta.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.108 > 0.08 con n=1066 PNL=+369.66€
  - _Datos_: n=1066 IC=+0.108 PNL=+369.66€

**🟡 H-CUSTOM-UPDOWNGBM-BTC15-TARDIO** — UPDOWN_GBM BTC#15min BUY_YES tardío (T_h<0.2) — lane nueva, no cubierta por GBM_LATE_15M
  - _Hipótesis_: Detectado 2026-07-09 al recalcular el checklist del item 13 (el análisis previo de esa misma sesión, n=510 IC=-0.0195, estaba mal filtrado — mezclaba entrada temprana+tardía; el filtro T_h<0.2 real da n=120 IC=+0.164 agregado, coincidiendo con H-CUSTOM-BUYYES15-SOLO-TARDIO). Aislando BTC: n=49 IC=+0.225 hit 73.5% PNL=+16.68€. BTC no está en pares_permitidos_live en ninguna tupla hoy (GBM_LATE_15M live es solo SOL/XRP/ETH BUY_YES), así que no hay riesgo de duplicar posición real. Comprobado solapamiento con GBM_LATE_15M (misma ventana/mercado): de los 49, 23 son mercados donde GBM_LATE_15M no dispara nada (IC=+0.260 ahí, el edge no depende de colarse en mercados ya cubiertos) y 26 solapan con un BTC BUY_YES de GBM_LATE_15M que existe en shadow pero no está whitelisted (IC=+0.179 en ese subconjunto). CAVEAT: n=49 es un recorte por-par posterior al hallazgo agregado (multiple comparisons) — por eso el umbral aquí es más exigente que el estándar (n≥80, no 40). CAVEAT 2: cero datos de fill-ability — libro_snapshots solo captura tuplas ya en pares_permitidos_live, y esta nunca lo estuvo (12 filas UPDOWN_GBM en todo el histórico, ninguna BTC#15min#BUY_YES). No proponer whitelist sin eso, ver tarea de instrumentación en dev.
  - _Umbral_: n≥80 (elevado desde el estándar 40, por ser recorte post-hoc) y IC>+0.08 en BTC específicamente
  - _Acción_: Si confirma con n≥80 IC≥0.08 Y hay datos de fill-ability viables (pendiente instrumentar) → proponer a Javi añadir UPDOWN_GBM#BTC#15min#BUY_YES a pares_permitidos_live con stake mínimo (dinero real, decisión suya). Si IC cae <0.05 con n≥80 → archivar, era ruido del recorte por-par.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.152 > 0.08 con n=398 PNL=+113.57€
  - _Datos_: n=398 IC=+0.152 PNL=+113.57€

**🔴 H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT** — GBM_LATE_15M BUY_YES con prob_yes_modelo<0.53 — mismo sesgo favorito-longshot que el resto del sistema. IMPLEMENTADO 21-Jul
  - _Hipótesis_: Detectado 2026-07-09 buscando por qué correlacionan las pérdidas en la misma ventana (no se encontró causa cruzada limpia — ver H-CUSTOM-GBMLATE-ANCHURA-MERCADO — pero apareció esto por otra vía). Deciles de prob_yes_modelo en GBM_LATE_15M BUY_YES (n=1257, 4 pares): relación MONÓTONA fuerte (decil1 hit 28.8% IC=-0.209 → decil10 hit 81.0% IC=+0.305), el modelo SÍ está bien calibrado en general. Pero por debajo de ≈0.53 el signo es negativo y consistente en los 4 pares (BTC IC=-0.185, ETH -0.171, SOL -0.153, XRP -0.015), n=249, PNL=-32.89€, y EMPEORANDO con el tiempo (1ª mitad IC=-0.095, 2ª mitad IC=-0.209) — no es un efecto que se esté corrigiendo solo. Comprobado el mecanismo: precio_yes_mercado medio en esta zona es 0.35 (min 0.105), el 76% por debajo de 0.45 — es comprar un YES que el propio mercado ya trata de longshot, y GBM_LATE dispara solo porque su estimación (aun siendo <0.53) queda por encima del precio aún más barato del mercado (edge técnico +0.10 de media). Es el MISMO sesgo favorito-longshot que el sistema ya filtra en otros sitios (H-CUSTOM-BUYNO-LONGSHOT-15MIN, PY_MKT_MAX_BUY_NO_ETH15). CAVEAT histórico (ya resuelto, ver ACTUALIZACIÓN 21-Jul): en LIVE (dinero real) la misma zona daba +14.03€ en n=27 — no confirmaba el signo negativo. Cruzado con H-CUSTOM-GBMLATE-ANCHURA-MERCADO (n=802, 05-09jul): esta señal (prob_yes_modelo) es la DOMINANTE — con conviccion sana (>=0.53) la anchura baja no hunde el resultado (sigue en +41.81€); con conviccion baja Y anchura baja juntas es la peor celda (n=86, hit 24.4%, IC=-0.250, PNL=-29.63€); con solo conviccion baja (anchura ok) ya es negativo por sí solo (n=37, IC=-0.090). Tratar como filtro PRIMARIO, la anchura como agravante secundario. ACTUALIZACIÓN 21-Jul (gate cruzado 11-Jul por vigia_pybajo.py, n=290 IC=-0.154; refrescado hoy n=520 IC=-0.190 PNL=-82.41€, reforzado no diluido): filtro IMPLEMENTADO en shadow_predict.py::main() (GBM_LATE_PYBAJO_LONGSHOT_MIN=0.53, aprobado Javi), tras /code-review que exigió el test de permutación que faltaba. Test corrido (analisis_shuffle_pybajo_longshot_21jul.py, reusa sp._shuffle_pvalue): zona baja n=524 hit=30.7% IC=-0.1920 PNL=-87.63€, shuffle p=0.0000/20000 (cola baja) — sobrevive holgadamente, NO es ruido de partición. Split temporal 1ª/2ª mitad ambas negativas y empeorando (-0.159→-0.223), consistente. El caveat live QUEDA RESUELTO: recalculado con metodología del shuffle sobre n=21 trades reales en la zona (join trades.csv↔predictions por market_id), IC=-0.0217, shuffle p=0.4944 — el antiguo +14.03€/n=27 era ruido de muestra pequeña, no una señal real contraria; no hay contradicción entre shadow y live, solo falta de potencia estadística en live. Vigilar forward n del bucket filtrado (ahora congelado, no seguirá creciendo salvo que se reactive) por si el mecanismo cambia.
  - _Umbral_: n≥289 (baseline 249 + 40 forward) e IC<-0.10 en las 4 monedas conjuntas para confirmar — CUMPLIDO, ver ACTUALIZACIÓN 21-Jul
  - _Acción_: IMPLEMENTADO 21-Jul: filtro causal decision==BUY_YES + prob_yes_modelo<0.53 → skip en GBM_LATE_15M, activo en shadow_predict.py (afecta a GBM_LATE_15M#ETH#15min#BUY_YES, live hoy). Validado con shuffle test (p=0.0000, n=524) tras el gap de rigor detectado en /code-review — ya no queda ninguna condición pendiente para archivar.
  - _Estado_: SEÑAL NEGATIVA confirmada: IC=-0.191 < -0.1 con n=532 PNL=-86.38€
  - _Datos_: n=532 IC=-0.191 PNL=-86.38€

**〰️ H-CUSTOM-GBMLATE-ANCHURA-MERCADO** — GBM_LATE_15M BUY_YES — anchura de mercado (retorno concurrente de los otros 3 majors) como modificador secundario
  - _Hipótesis_: Detectado 2026-07-09 buscando explicar por qué varias pérdidas de la racha=4 comparten ventana de 15min. Con precios reales (05-09jul, ~20k muestras BTC) se calculó el retorno concurrente de los OTROS 3 majors desde el inicio de la ventana hasta el momento exacto de la decisión (sin fuga de datos, nunca el precio de cierre) y se cruzó con resultados reales de GBM_LATE_15M BUY_YES: n=802, magnitud media de los otros 3 en deciles limpios y monótonos (decil1 IC=-0.146 hit 35% → decil6-9 IC≈+0.20/+0.29 hit 70-80%). NO es redundante con drift_ventana_pct propio del par (correlación solo 0.26); controlando por el drift propio, la anchura sigue añadiendo información (dentro de drift propio>=0, que es el 90% de los casos: IC=0.127 si anchura baja vs IC=0.211 si anchura alta). Funciona en espejo para BUY_NO (shadow, n=685, anchura negativa 0/3→3/3: hit 47.4%→70.3%). CAVEAT importante: NO explica los clusters concretos de racha=4 en vivo — 6 de los 8 eventos históricos tienen anchura ALTA en al menos 2 de las 4 pérdidas (ver notas de sesión 09-Jul), y el backtest directo sobre trades.csv real (n=105-116) es inconcluso/contradictorio (gate anchura>=3 empeora el PnL real, -2.11€ vs +32.32€ sin filtro — probablemente confusión por mezcla de pares en una muestra pequeña, SOL domina ese bucket y SOL es el par MENOS sensible a esta señal: IC 0.132→0.143 apenas cambia, vs ETH 0.038→0.192). Tratar como MODIFICADOR del filtro primario H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT, no como filtro independiente — ver esa hipótesis para la tabla cruzada. Feature `mercado_anchura_pct` añadida 2026-07-09 en shadow_predict.py (_s_gbm_late), puro logging, no cambia ninguna decisión — empieza a acumular desde cero en predicciones nuevas. ACTUALIZACIÓN 12-Jul (desagregación por activo, n fresco): BTC n=35 ic=+0.392 z=+4.90, ETH n=32 ic=+0.353 z=+4.24, XRP n=31 ic=+0.288 z=+3.41 -- los 3 MUY fuertes y consistentes. SOL sigue siendo el único débil (n=30 ic=+0.094 z=+1.10), confirma el caveat ya escrito arriba (SOL insensible). Con XRP incluido, el patrón deja de ser '3 activos + SOL raro' para ser una regla casi universal salvo SOL -- candidato fuerte para boost Kelly restringido a BTC/ETH/XRP (excluir SOL explícitamente) en vez de aplicar a las 4 monedas por igual.
  - _Umbral_: n≥100 forward (feature nueva, sin histórico) e IC>+0.20 en la zona alta (mercado_anchura_pct≥0.056, el decil superior observado)
  - _Acción_: Si confirma con n≥100 IC≥0.20 → boost Kelly cuando mercado_anchura_pct≥0.056 Y prob_yes_modelo≥0.53 (la celda 'doble buena', hit 72.7% retrospectivo). No usar como filtro solo — ver CAVEAT de los clusters de racha en la descripción, y el análisis por-par (SOL insensible) antes de aplicar a las 4 monedas por igual.
  - _Estado_: n=1727 IC=+0.189 PNL=+993.70€ — sin señal clara aún (umbral IC: min=0.2 max=None)
  - _Datos_: n=1727 IC=+0.189 PNL=+993.70€

**⏳ H-CUSTOM-OF5M-SMARTMONEY-CONTRARIO** — ORDER_FLOW_5M SOL BUY_NO — smart money EN CONTRA del flujo CEX, no a favor, predice mejor
  - _Hipótesis_: Detectado 11-Jul revisando el backlog quant-desk (reencuadre de ORDER_FLOW_5M). ORDER_FLOW_5M solo dispara BUY_NO (presión vendedora en Binance). Split retrospectivo SOL#5min por smart_money_consensus (ya logueado, nunca cruzado con esta estrategia): cuando el consenso on-chain es BAJISTA (smart_money_consensus<0, 'confirma' la señal CEX) el hit cae a 47.1% (ic_bayes=-0.026, n=17); cuando el consenso es ALCISTA/neutro (smart_money_consensus>=0, CONTRARIO a la señal CEX) el hit sube a 65.0% (ic_bayes=+0.136, n=20, pnl/trade+0.294). Contraintuitivo: la 'confirmación' de dos fuentes empeora, la divergencia mejora. Hipótesis mecánica: el flujo de Binance ya captura la información rápida de 5min; smart money on-chain se mueve más lento (posiciones ya tomadas), así que cuando coincide con el flujo CEX puede ser la MISMA información ya vista dos veces sin dar nada nuevo (o incluso momentum ya agotado), mientras que la divergencia indica que el flujo CEX es el que se está moviendo AHORA sobre información fresca que smart money aún no reflejó. Distinto del cierre 08-Jul del consenso poblacional plano (n=2494, ruido puro) — aquello era agregado sobre TODAS las estrategias; esto es específico del mecanismo de ORDER_FLOW_5M. n=17/20 insuficiente para concluir (regla del proyecto n≥15 es el mínimo absoluto, no un veredicto) — vigilar forward.
  - _Umbral_: 40
  - _Acción_: Si confirma con n≥40 e ic_bayes contrario≥+0.08 (con alineado claramente peor) → boost Kelly en ORDER_FLOW_5M BUY_NO cuando smart_money_consensus>=0; considerar filtro/veto cuando smart_money_consensus<0 y muy negativo (posible señal 'ya vista', sin ventaja).
  - _Estado_: 25/40 ops en el filtro definido (IC actual=+0.167 PNL=+6.91€)
  - _Datos_: n=25 IC=+0.167 PNL=+6.91€

**🟡 H-CUSTOM-ETH15-SIGMA-ACCEL** — GBM_LATE_15M ETH — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: sigma_ewma_delta_pct = (sigma_h_ewma10-sigma_h)/sigma_h. Verificado ad-hoc n=47: cuando la vol reciente (EWMA half-life 10min) supera la ventana plana, hit sube de 59.5% (agregado ETH) a 66.0%, ic_bayes=+0.153. Efecto NO uniforme entre activos (ver hermanas BTC/XRP) -- desagregar por activo es obligatorio, el agregado GBM_LATE_15M diluye esto a ruido.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en ETH#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.082 > 0.08 con n=891 PNL=+168.47€
  - _Datos_: n=891 IC=+0.082 PNL=+168.47€

**🟡 H-CUSTOM-BTC15-SIGMA-ACCEL** — GBM_LATE_15M BTC — vol acelerando (EWMA10>flat) mejora la señal
  - _Hipótesis_: 12-Jul: mismo mecanismo que ETH (ver H-CUSTOM-ETH15-SIGMA-ACCEL). Verificado ad-hoc n=35: hit sube de 63.6% (agregado BTC) a 68.6%, ic_bayes=+0.176.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: Si confirma con n>=40 -> proponer kelly_boost condicionado a sigma_ewma_delta_pct>=0 en BTC#15min
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.115 > 0.08 con n=951 PNL=+302.40€
  - _Datos_: n=951 IC=+0.115 PNL=+302.40€

**🟡 H-CUSTOM-XRP15-SIGMA-DECEL** — GBM_LATE_15M XRP — vol DESacelerando (EWMA10<=flat) mejora la señal (signo opuesto a ETH/BTC)
  - _Hipótesis_: 12-Jul: XRP muestra el signo CONTRARIO a ETH/BTC -- cuando la vol reciente cae por debajo de la ventana plana, hit sube de 63.9% (agregado XRP) a 68.8%, ic_bayes=+0.180 (n=48). Cuando acelera, hit CAE a 57.1%. Confirma que este feature no puede tratarse con un umbral global -- cada activo necesita su propio signo. REFUTADA 13-Jul: recalculado con n=61 (más del doble del n original) usando el mismo método riguroso (percentiles + permutación 20k) que confirmó BTC/SOL/ETH -- el signo se INVIRTIÓ: decel (sigma<0) da IC=-0.065 n=21 (malo), accel (sigma>=0) da IC=+0.071 n=40 (bueno). XRP en realidad tiene el MISMO signo que BTC/ETH (sigma alto=bueno), solo que más débil -- coherente con el patrón ganador ya auto-descubierto por postmortem (sigma_ewma_delta_pct>5.563, ic_patron=+0.20 n=18, mismo signo). El hallazgo ad-hoc del 12-Jul con n=48 no replicó con más datos -- probable ruido de una muestra menor/distinta. Ver idea_estrategia_mercado_bajista... no, ver project_sigma_filtro_sol_xrp_no_promociona_13jul (memoria) para el detalle completo.
  - _Umbral_: n>=40 y IC>+0.08
  - _Acción_: REFUTADA -- no implementar kelly_boost por sigma<0 en XRP. El signo correcto es el opuesto (sigma alto=bueno), ya cubierto por el patron_ganador automático de postmortem sobre GBM_LATE_15M#XRP#15min -- no hace falta ninguna acción manual adicional.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.123 > 0.08 con n=1323 PNL=+647.59€
  - _Datos_: n=1323 IC=+0.123 PNL=+647.59€

**🟡 H-CUSTOM-SMARTMONEY-FAVORITO-SOL** — FAVORITO_CONFIRMADO SOL — alineado con smart_money_consensus bate ir en contra (REABRE hallazgo cerrado 08-Jul)
  - _Hipótesis_: 12-Jul: el cierre 08-Jul (n=2494, sin desagregar por estrategia/activo) encontro ruido puro. Desagregando por estrategia+activo (mecanismo nuevo): FAVORITO_CONFIRMADO#SOL alineado con smart_money_consensus (|consenso|>0.1, n_wallets>=3) hit=78.4% (n=37) vs contrario hit=52.4% (n=42), z=+2.41. GBM_LATE_15M tambien muestra el mismo signo en BTC/ETH/XRP (z=0.86-1.61, mas debil) pero SOL plano ahi -- inconsistencia entre estrategias que hay que entender antes de actuar.
  - _Umbral_: n>=40 por lado y z>=2
  - _Acción_: Si confirma con n>=40 y z>=2 -> considerar boost condicionado a alineacion con smart_money_consensus en FAVORITO_CONFIRMADO#SOL
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.199 > 0.08 con n=483 PNL=+20.90€
  - _Datos_: n=483 IC=+0.199 PNL=+20.90€

**🟡 H-CUSTOM-FAVORITO-SOL-ALTACONVICCION** — FAVORITO_CONFIRMADO SOL BUY_YES alta conviccion (py_entrada alto) — UNICO caso positivo en fill-ability de hoy
  - _Hipótesis_: 12-Jul: auditoria de fill-ability de las 8 candidatas encontro las 8 negativas en agregado. Pero desagregando FAVORITO_CONFIRMADO por activo (mecanismo nuevo, no mirado hasta hoy): SOL#BUY_YES con py_entrada>=0.665-0.695 da pnl/trade POSITIVO en el subconjunto fillable real (+0.12 a +0.41 EUR/trade, n=6-17 segun el corte exacto) -- unico resultado positivo de toda la auditoria de candidatas. n todavia bajo, necesita mas dato antes de proponer nada.
  - _Umbral_: n>=40 y pnl/trade fillable > 0 sostenido
  - _Acción_: Seguir acumulando snapshots candidato_evaluacion para SOL#15min#BUY_YES en FAVORITO_CONFIRMADO; re-evaluar fill-ability con n>=40 antes de proponer whitelist
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.265 > 0.08 con n=837 PNL=-37.68€
  - _Datos_: n=837 IC=+0.265 PNL=-37.68€

**⏳ H-CUSTOM-GBM18H-XRP-EXCEPCION** — UPDOWN_GBM XRP a las 18h UTC -- puede estar mal incluida en el blacklist horario global
  - _Hipótesis_: 12-Jul: gbm_blacklist_hours_auto=[9,10,18] bloquea GBM en las 4 monedas a las 18h. Desagregando por activo (h9/h10 no tienen dato retrospectivo -- el propio blacklist impide que se genere): BTC ic=-0.140 (n=48), ETH ic=-0.136 (n=42), SOL ic=-0.167 (n=22) consistentes con el bloqueo, pero XRP ic=+0.100 (n=23) -- signo OPUESTO. El bloqueo agregado puede estar sobre-bloqueando XRP especificamente.
  - _Umbral_: 40
  - _Acción_: Si confirma con n>=40 IC>0.08 -> considerar excepcion de XRP en gbm_blacklist_hours_auto para la hora 18 (shadow puro, UPDOWN_GBM no esta live)
  - _Estado_: 35/40 ops en el filtro definido (IC actual=+0.095 PNL=+7.70€)
  - _Datos_: n=35 IC=+0.095 PNL=+7.70€

**〰️ H-CUSTOM-LEADLAG-XRP-BUYNO** — LEADLAG_BTC_XRP_15M -- la señal se concentra en BUY_NO, BUY_YES está plano
  - _Hipótesis_: 12-Jul: revisando dead/tracking ideas por petición Javi. El tracker agregado (activa=True, ic_bayes=+0.1154 n=63) ya cruza el umbral histórico de gate n>=40 IC>=0.08, pero mezclaba direcciones. Desagregado: BUY_NO hit=71.9% n=32 z=+2.47 (fuerte); BUY_YES hit=51.6% n=31 z=+0.18 (plano, sin señal). Coherente con el hallazgo offline previo (idea_leadlag_btc_xrp_revive_parcial: BTC-momentum-fills predice BTC->XRP estable en split-half, mecanismo distinto del spot-drift ya refutado). No confirmado a nivel BH-FDR (K=223, z individual no llega a 2.677), pero es la única sub-hipotesis de LEADLAG con dirección consistente con el hallazgo offline. Shadow puro, LEADLAG no esta en pares_permitidos_live ni candidatos_evaluacion_live -- cero riesgo, cero dato de fill-ability todavia.
  - _Umbral_: n>=40 y IC>0.08 (en BUY_NO especificamente, no agregado)
  - _Acción_: Si BUY_NO confirma n>=40 IC>=0.08 sostenido -> considerar instrumentar fill-ability (candidatos_evaluacion_live) antes de cualquier propuesta de whitelist, dado el patron ya conocido de selección adversa en BUY_NO
  - _Estado_: n=142 IC=+0.056 PNL=+15.75€ — sin señal clara aún (umbral IC: min=0.08 max=None)
  - _Datos_: n=142 IC=+0.056 PNL=+15.75€

**🟡 H-CUSTOM-ETH15-BUYNO-TARDIO** — UPDOWN_GBM ETH#15min BUY_NO tardío (T_h<0.2) -- edge fuerte no capturado por el aprendizaje causal automático
  - _Hipótesis_: 12-Jul: desagregando por (activo, dirección) la hipótesis agregada H-CUSTOM-LATE-ENTRY-15MIN (T_h<0.2, sin filtro de dirección, n=261 ic+0.173 agregado). Split por dirección: BTC BUY_YES n=81 ic=+0.235 z=+4.33 (fuerte, coincide con el mecanismo ya conocido/implementado en GBM_LATE_15M#BTC BUY_YES); BTC BUY_NO n=12 z=+0.58 (débil, n insuficiente). ETH BUY_YES n=102 ic=+0.144 z=+2.97 (fuerte); **ETH BUY_NO n=38 ic=+0.250 z=+3.24 -- tan fuerte como el BUY_YES, y NUNCA se había mirado por separado**. Verificado contra strategy_params.json: UPDOWN_GBM#ETH#15min tiene ic_BUY_NO agregado=+0.038 (n=249, sin filtro T_h) -- el aprendizaje causal automático (FEATURE_RULES) no ha encontrado todavía este corte T_h<0.2 específico pese a tener la feature T_h en su base. UPDOWN_GBM no está en pares_permitidos_live en ninguna tupla BUY_NO -- shadow puro, cero riesgo. Casi cruza el gate estándar (n=38 de 40).
  - _Umbral_: n>=40 y IC>=0.08
  - _Acción_: Si confirma con n>=40 (2 resoluciones más) -> vigilar si el postmortem automático lo descubre solo vía FEATURE_RULES; si no, considerar patrón manual. Dado que BUY_NO ya tiene selección adversa conocida en otras estrategias (GBM_LATE_15M), NO proponer para whitelist sin antes medir fill-ability (candidatos_evaluacion_live) -- mismo patrón de cautela que el resto de hallazgos BUY_NO de esta sesión.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.313 > 0.08 con n=164 PNL=+90.50€
  - _Datos_: n=164 IC=+0.313 PNL=+90.50€

**⏳ H-CUSTOM-WEEKLY-SOL-BUYNO-PRECIO-ALTO** — WEEKLY_PRICE SOL BUY_NO -- edge fuerte concentrado en precio alto (py>=0.45), posible pero sin fill-ability medida
  - _Hipótesis_: 06-Ago: hallazgo al minar gate_bucket_propio.json tras extender su cobertura a TODA estrategia en shadow (antes WEEKLY_PRICE era invisible para este mecanismo -- su formato de 3 segmentos, sin marco, no lo soportaba el parseo original). WEEKLY_PRICE#SOL#BUY_NO ya tenia IC agregado fuerte (ic_bayes=0.3605 global, ic_BUY_NO=0.4159 n=224, strategy_params.json) pero JAMAS se habia desagregado por precio. Al hacerlo: el edge NO es uniforme -- buckets bajos [0.20,0.25)/[0.40,0.45) dan pnl/trade positivo pero modesto (+0.459/+0.445, marcados malo_confirmado por quedar muy por debajo del resto, shuffle p=0.000/0.001) mientras [0.45,0.50) (n=133, el bucket mas grande) da pnl/trade +1.249 y [0.50,0.55) (n=19, gate riguroso completo: shuffle p=0.000, split-half consistente ambas mitades) da +1.878, veredicto bueno_confirmado. CAVEAT SERIO -- bucket 0.45 (n=133, el de mas peso) NO pasa split-half: primera mitad diff=-0.006 (nula), segunda mitad diff=+1.123 -- el edge podria ser reciente/emergente, no necesariamente estructural, sin mas n no se puede afirmar que sea estable. CAVEAT MAS SERIO -- WEEKLY_PRICE NUNCA ha estado en pares_permitidos_live ni ha pasado por el camino de ejecucion real: las 429 filas en libro_snapshots.csv son TODAS motivo=candidato_evaluacion (solo observacion de libro), CERO intentos de fill real -- fill-ability completamente desconocida. Antes de proponer cualquier promocion hace falta (1) que bucket 0.45 pase split-half con mas n, (2) medir fill-ability real (requiere activarlo primero solo como observador de ejecucion, sin dinero), (3) cruzar contra ballenas (no aplica directo -- mercados semanales de precio, no UP/DOWN, el timing de ballenas de corto plazo no es la fuente natural aqui).
  - _Umbral_: 200
  - _Acción_: Vigilar crecimiento de gate_bucket_propio.json (cron diario) para este par exacto. Si bucket 0.45 pasa split-half con mas n, siguiente paso es medir fill-ability real (instrumentar solo observacion de libro, cero riesgo) antes de cualquier propuesta de whitelist.
  - _Estado_: 175/200 ops en el filtro definido (IC actual=+0.466 PNL=+245.73€)
  - _Datos_: n=175 IC=+0.466 PNL=+245.73€

**〰️ H-CUSTOM-FAVALTACONV-BNB5M-PAYOUT-NEGATIVO** — ALERTA -- FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES pierde dinero en TODOS los buckets de precio pese a IC positivo
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json completo tras la extension de hoy. strategy_params.json muestra ic_bayes=+0.158 (n=1448, activa=True) -- a primera vista parece una candidata razonable. Desagregado por precio (gate_bucket_propio.json): pnl/trade NEGATIVO en 5 de 6 buckets (0.70:-0.071 bueno_confirmado[relativo, sigue siendo negativo]/0.75:-0.212 malo_confirmado/0.80:-0.263/0.85:-0.506 malo_confirmado/0.90:-0.090), solo 0.95 (n=6, ruido) da +0.025. pnl/trade ponderado por n en TODO el rango = -0.132EUR/trade sobre n=1447. Mismo patron payout-asimetrico ya conocido en el proyecto (hit-rate alto, breakeven=precio de entrada, entra caro 0.70-0.95 -> paga poco cuando gana, pierde el stake completo cuando falla). IC positivo mide correlacion/direccion, NO mide si el payout deja margen -- exactamente el gap que motivo kelly_precio_gate.py en su dia. Esta hipotesis es una ALERTA, no una oportunidad: documentar para que nadie proponga esta tupla a whitelist guiandose solo por el ic_bayes agregado.
  - _Umbral_: NO promocionar sin resolver el payout asimetrico -- ningun n adicional lo arregla si el mecanismo de precio de entrada no cambia
  - _Acción_: Bloqueo informativo -- si alguna sesion futura propone FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES para pares_permitidos_live, releer esta nota antes de aprobar. No requiere accion de codigo, es memoria del hallazgo.
  - _Estado_: n=2098 IC=+0.158 PNL=-289.98€ — sin señal clara aún (umbral IC: min=999 max=None)
  - _Datos_: n=2098 IC=+0.158 PNL=-289.98€

**🟡 H-CUSTOM-GBMLATE15M-SOL-RESCATE-PRECIO** — GBM_LATE_15M#SOL#15min#BUY_YES (pausada 05-Ago) -- posible rescate con filtro py en [0.45,0.55)
  - _Hipótesis_: 06-Ago: hallazgo al barrer gate_bucket_propio.json. GBM_LATE_15M#SOL#15min#BUY_YES fue PAUSADA el 05-Ago por veto sigma_ewma_delta_pct (ver project_veto_sigma_ewma_gbmlate_05ago). Desagregando por precio: bucket [0.50,0.55) tiene n=411, pnl/trade +0.498, gate riguroso COMPLETO (bueno_confirmado, split-half consistente ambas mitades [0.305,0.273]). El bucket vecino [0.45,0.50) (n=356, sin_concluir todavia) tambien da pnl positivo +0.323. Juntos (0.45-0.55) suman n=767, la mayoria del volumen de la tupla. En cambio [0.20,0.25) (n=20) da pnl=-0.866, malo_confirmado -- el problema parece concentrado en precio bajo, no en toda la tupla. HIPOTESIS: restringir la reactivacion a un filtro de precio py en [0.45,0.55) en vez de mantener la pausa total podria rescatar la mayor parte del edge sin el drenaje que motivo la pausa -- pero el veto sigma_ewma que causo la pausa es una dimension DISTINTA (volatilidad reciente, no precio), asi que ambos filtros podrian ser complementarios, no sustitutos. NO proponer reactivacion sin cruzar este hallazgo con el analisis original de sigma_ewma que motivo la pausa. ACTUALIZADO 06-Ago mismo dia, cruce con sigma_ewma pedido por Javi: filtros COMPLEMENTARIOS confirmado, no redundantes. 4 grupos (n con sigma_ewma disponible, n=1169 total, 767 filtrado a py[0.45,0.55)): solo_precio n=348 hit=59.8% pnl=+0.266; solo_sigma n=41 hit=63.4% pnl=+0.322; AMBOS n=92 hit=75.0% pnl=+0.755 (shuffle p=0.0014, split-half CONSISTENTE ambas mitades +0.511/+0.632); ninguno n=226 hit=42.5% pnl=+0.033 (casi breakeven). El filtro combinado casi TRIPLICA el pnl/trade del filtro de precio solo y confirma con rigor completo -- el edge real de esta tupla esta concentrado en la interseccion de ambos filtros, no en cualquiera de los dos por separado. Sigue pendiente medir fill-ability real antes de proponer reactivacion (mismo caveat que siempre).
  - _Umbral_: YA CONFIRMADO con rigor (shuffle p=0.0014, split-half OK, n=92) -- falta fill-ability real antes de proponer reactivacion
  - _Acción_: Investigacion pendiente: cruzar bucket de precio con el estado de sigma_ewma_delta_pct en las mismas filas. Si son independientes, un filtro combinado (precio Y sigma_ewma) podria ser mas preciso que cualquiera de los dos solo.
  - _Estado_: SEÑAL POSITIVA confirmada: IC=+0.152 > 0.1 con n=769 PNL=+319.47€
  - _Datos_: n=769 IC=+0.152 PNL=+319.47€
