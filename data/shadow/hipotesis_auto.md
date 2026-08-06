# Hipótesis automáticas — 2026-08-06 02:47 UTC
_Generado por shadow_postmortem.py sobre 77438 resoluciones (PNL=+13102.21€)_

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
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.185 (n=2232)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0066 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.155 (n=3126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 7.0 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.1187` → IC=+0.165 (n=1208)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1187 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.852` → IC=+0.238 (n=1237)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.852 (IC base=+0.143)

- **PATRÓN** `libro_liquidez` > `2055.4132` → IC=+0.151 (n=2989)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 2055.4132 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.160 (n=2922)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.004 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.153 (n=998)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 18.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.161 (n=1091)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 6.0 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.6234` → IC=+0.146 (n=309)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.6234 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1633` → IC=+0.126 (n=2514)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.1633 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.218` → IC=+0.176 (n=483)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 8.218 (IC base=+0.145)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.137 (n=496)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0046 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.139 (n=527)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 7.0 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `0.4991` → IC=+0.149 (n=75)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.4991 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.024` → IC=+0.185 (n=109)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 12.024 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `11259.528` → IC=+0.149 (n=309)

  - _Acción_: Kelly boost +0.75€ cuando `libro_liquidez` > 11259.528 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.36` → IC=+0.170 (n=277)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 4.36 (IC base=+0.104)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.157 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0072 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.136 (n=418)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 12.0 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.127 (n=548)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 15.0 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.1207` → IC=+0.149 (n=289)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1207 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.51` → IC=+0.196 (n=192)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 7.51 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=648)

  - _Acción_: Kelly boost +0.61€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `7744.8306` → IC=+0.143 (n=343)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 7744.8306 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.483` → IC=+0.185 (n=157)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.483 (IC base=+0.083)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.198 (n=236)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0111 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.138 (n=663)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 7.0 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.1931` → IC=+0.148 (n=282)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.1931 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.323` → IC=+0.267 (n=315)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.323 (IC base=+0.123)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.127 (n=674)

  - _Acción_: Kelly boost +0.64€ cuando `libro_spread` < 0.01 (IC base=+0.123)

- **PATRÓN** `libro_liquidez` > `1796.4601` → IC=+0.159 (n=555)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1796.4601 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.137 (n=265)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 7.0 (IC base=+0.080)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.224 (n=751)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.195)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.211 (n=756)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.195)

- **PATRÓN** `dist_vwap_pct` > `0.1223` → IC=+0.222 (n=375)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1223 (IC base=+0.195)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.116` → IC=+0.311 (n=210)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.116 (IC base=+0.195)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=696)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.195)

- **PATRÓN** `libro_liquidez` > `3147.1402` → IC=+0.193 (n=229)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 3147.1402 (IC base=+0.195)

- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.237 (n=648)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0069 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.249 (n=500)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.221)

- **PATRÓN** `dist_vwap_pct` > `0.7775` → IC=+0.357 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7775 (IC base=+0.221)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.323` → IC=+0.253 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.323 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.237 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.221)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.122 (n=2238)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` > 0.0069 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.845` → IC=+0.208 (n=1167)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.845 (IC base=+0.095)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.140 (n=1071)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 6.0 (IC base=+0.108)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `12.682` → IC=+0.180 (n=101)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` > 12.682 (IC base=+0.065)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `12.592` → IC=+0.183 (n=99)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 12.592 (IC base=+0.061)

- **PATRÓN** `libro_liquidez` > `8979.1015` → IC=+0.151 (n=216)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 8979.1015 (IC base=+0.061)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.047` → IC=+0.267 (n=148)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.047 (IC base=+0.038)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.167 (n=854)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0068 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.165 (n=792)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 7.0 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.6671` → IC=+0.206 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6671 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.43` → IC=+0.279 (n=156)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.43 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.159 (n=731)

  - _Acción_: Kelly boost +0.79€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.185 (n=861)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0065 (IC base=+0.173)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.191 (n=599)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 12.0 (IC base=+0.173)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.178 (n=302)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 6.0 (IC base=+0.173)

- **PATRÓN** `dist_vwap_pct` > `0.5412` → IC=+0.269 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5412 (IC base=+0.173)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.185 (n=738)

  - _Acción_: Kelly boost +0.93€ cuando `libro_spread` < 0.01 (IC base=+0.173)

### GBM_LATE_5M
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

- **FILTRO** `dist_vwap_pct` < `1.0377` → IC=-0.317 (n=58)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 1.0377
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=4)

- **FILTRO** `sigma_ewma_delta_pct` < `5.488` → IC=-0.311 (n=51)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 5.488
  - _Potencial_: sin este filtro IC_bueno=-0.269 (n=11)

- **FILTRO** `sigma_ewma_delta_pct` > `3.658` → IC=-0.333 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.658
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=46)

- **FILTRO** `libro_liquidez` < `4551.0427` → IC=-0.318 (n=31)

  - _Acción_: SKIP cuando `libro_liquidez` < 4551.0427
  - _Potencial_: sin este filtro IC_bueno=-0.288 (n=31)

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

- **PATRÓN** `sigma_ewma_delta_pct` > `6.638` → IC=+0.200 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.638 (IC base=+0.015)

### GBM_LATE_60M
- **FILTRO** `sigma_h` > `0.0111` → IC=-0.282 (n=53)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0111
  - _Potencial_: sin este filtro IC_bueno=-0.179 (n=104)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.272 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.074 (n=45)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.209 (n=53)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0042 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.1487` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1487 (IC base=+0.024)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.422` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.422 (IC base=+0.024)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `dist_vwap_pct` < `0.1642` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1642
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=17)

- **FILTRO** `sigma_h` > `0.0034` → IC=-0.167 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0034
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.176 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.208 (n=22)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0032 (IC base=+0.034)

### GBM_LATE_60M#ETH#60min
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

- **PATRÓN** `sigma_h` < `0.004` → IC=+0.214 (n=19)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.004 (IC base=+0.066)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.129 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=17)

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

- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=-0.058)

### LEADLAG_BTC_XRP_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=166)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.006 (n=166)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.074 (n=181)

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
- **PATRÓN** `hora_utc` > `3.0` → IC=+0.167 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 3.0 (IC base=+0.067)

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

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0077` → IC=-0.329 (n=33)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=12)

- **FILTRO** `T_h` > `87.9981` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `T_h` > 87.9981
  - _Potencial_: sin este filtro IC_bueno=-0.400 (n=8)

- **FILTRO** `pct_vs_K` |x|> `2.6988` → IC=-0.458 (n=22)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6988
  - _Potencial_: sin este filtro IC_bueno=-0.400 (n=8)

### PRICE_TARGET_GBM#SOL#atexpiry
- **FILTRO** `sigma_h` > `0.0132` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0132
  - _Potencial_: sin este filtro IC_bueno=-0.136 (n=9)

### STREAK_FADE_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=101)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.202 (n=55)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.060)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### STREAK_FADE_15M#SOL#15min
- **PATRÓN** `streak_len` < `4.0` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `streak_len` < 4.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `py_entrada` < 0.485 (IC base=+0.112)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `hora_utc` < `9.0` → IC=+0.174 (n=41)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 9.0 (IC base=+0.070)

- **PATRÓN** `volumen_racha` < `497480.0` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `volumen_racha` < 497480.0 (IC base=+0.070)

- **PATRÓN** `libro_liquidez` > `2537.9562` → IC=+0.147 (n=32)

  - _Acción_: Kelly boost +0.74€ cuando `libro_liquidez` > 2537.9562 (IC base=+0.070)

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
  - _Potencial_: sin este filtro IC_bueno=+0.040 (n=85)

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

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.9312 (IC base=+0.083)

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

### UPDOWN_GBM#BTC#15min
- **PATRÓN** `drift_60min` |x|≤ `0.1888` → IC=+0.147 (n=284)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1888 (IC base=+0.105)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0865` → IC=+0.136 (n=289)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.68€ cuando `delta_ratio_macro` |x|> 0.0865 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.175 (n=192)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 14.0 (IC base=+0.105)

- **PATRÓN** `ibs_15` > `0.6354` → IC=+0.219 (n=283)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6354 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.2571` → IC=+0.237 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2571 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `25.023` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 25.023 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `11672.79` → IC=+0.161 (n=113)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11672.79 (IC base=+0.105)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `ibs_15` > `0.6644` → IC=+0.192 (n=219)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.6644 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.056` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 7.056 (IC base=+0.056)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.179 (n=163)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` < 0.0051 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` > `0.9222` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9222 (IC base=+0.080)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `sigma_h` > `0.0204` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0204
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1932` → IC=-0.167 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1932
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **PATRÓN** `drift_15min` |x|≤ `0.4618` → IC=+0.139 (n=81)

  - _Acción_: Kelly boost +0.69€ cuando `drift_15min` |x|≤ 0.4618 (IC base=+0.075)

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

- **PATRÓN** `sigma_h` < `0.0074` → IC=+0.136 (n=152)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0074 (IC base=+0.118)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.141 (n=179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 12.0 (IC base=+0.118)

- **PATRÓN** `ibs_15` < `0.0448` → IC=+0.143 (n=82)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.71€ cuando `ibs_15` < 0.0448 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `3035.0793` → IC=+0.158 (n=71)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 3035.0793 (IC base=+0.118)

### UPDOWN_GBM_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.153 (n=378)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0048 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.0056` → IC=+0.159 (n=998)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0056 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.0663` → IC=+0.175 (n=340)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.88€ cuando `drift_60min` |x|≤ 0.0663 (IC base=+0.150)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1937` → IC=+0.138 (n=352)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.69€ cuando `delta_ratio_macro` |x|> 0.1937 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.138 (n=776)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 5.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.138 (n=525)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 12.0 (IC base=+0.150)

- **PATRÓN** `ibs_15` > `0.5385` → IC=+0.220 (n=772)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5385 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.2413` → IC=+0.139 (n=267)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.2413 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` < `0.5741` → IC=+0.120 (n=725)

  - _Acción_: Kelly boost +0.60€ cuando `dist_vwap_pct` < 0.5741 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.258` → IC=+0.189 (n=448)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 5.258 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `2545.0995` → IC=+0.133 (n=772)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2545.0995 (IC base=+0.150)

- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.212 (n=457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0064 (IC base=+0.182)

- **PATRÓN** `drift_60min` |x|≤ `0.2167` → IC=+0.169 (n=599)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.84€ cuando `drift_60min` |x|≤ 0.2167 (IC base=+0.182)

- **PATRÓN** `drift_15min` |x|≤ `0.4196` → IC=+0.198 (n=299)

  - _Acción_: Kelly boost +0.99€ cuando `drift_15min` |x|≤ 0.4196 (IC base=+0.182)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.173 (n=325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 17.0 (IC base=+0.182)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.169 (n=618)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 12.0 (IC base=+0.182)

- **PATRÓN** `ibs_15` < `0.4444` → IC=+0.238 (n=906)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.4444 (IC base=+0.182)

- **PATRÓN** `dist_vwap_pct` > `0.2003` → IC=+0.191 (n=208)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.2003 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` > `19.539` → IC=+0.194 (n=119)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 19.539 (IC base=+0.182)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.443` → IC=+0.188 (n=885)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 7.443 (IC base=+0.182)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.169 (n=921)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.182)

- **PATRÓN** `libro_liquidez` > `3994.029` → IC=+0.174 (n=299)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3994.029 (IC base=+0.182)

### UPDOWN_GBM_15M_TARDIO#BTC#15min
- **FILTRO** `ibs_15` < `0.7488` → IC=-0.139 (n=59)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.7488
  - _Potencial_: sin este filtro IC_bueno=+0.271 (n=120)

- **PATRÓN** `sigma_h` < `0.0031` → IC=+0.188 (n=75)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0031 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.163 (n=170)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0027 (IC base=+0.161)

- **PATRÓN** `drift_60min` |x|≤ `0.1123` → IC=+0.152 (n=90)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1123 (IC base=+0.161)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1237` → IC=+0.152 (n=90)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1237 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.175 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 16.0 (IC base=+0.161)

- **PATRÓN** `ibs_15` > `0.7488` → IC=+0.271 (n=120)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7488 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.2256` → IC=+0.203 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2256 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.379` → IC=+0.182 (n=83)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.379 (IC base=+0.161)

- **PATRÓN** `libro_liquidez` > `11198.676` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 11198.676 (IC base=+0.161)

- **PATRÓN** `drift_15min` |x|≤ `0.5515` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `drift_15min` |x|≤ 0.5515 (IC base=-0.066)

- **PATRÓN** `ibs_15` < `0.5537` → IC=+0.139 (n=34)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.69€ cuando `ibs_15` < 0.5537 (IC base=-0.066)

- **PATRÓN** `libro_liquidez` > `9476.9221` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 9476.9221 (IC base=-0.066)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.5405` → IC=-0.143 (n=82)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5405
  - _Potencial_: sin este filtro IC_bueno=+0.202 (n=169)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.179 (n=82)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0065 (IC base=+0.118)

- **PATRÓN** `drift_60min` |x|≤ `0.045` → IC=+0.162 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.045 (IC base=+0.118)

- **PATRÓN** `ibs_15` > `0.7007` → IC=+0.289 (n=126)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7007 (IC base=+0.118)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.922` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 7.922 (IC base=+0.118)

- **PATRÓN** `libro_liquidez` > `7672.3115` → IC=+0.133 (n=126)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 7672.3115 (IC base=+0.118)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.343 (n=87)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.276)

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

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.134 (n=91)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0089 (IC base=+0.104)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1216` → IC=+0.143 (n=96)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.71€ cuando `delta_ratio_macro` |x|> 0.1216 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `20.0` → IC=+0.179 (n=51)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 20.0 (IC base=+0.104)

- **PATRÓN** `ibs_15` > `0.7419` → IC=+0.296 (n=96)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7419 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` < `0.1333` → IC=+0.145 (n=122)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1333 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.453` → IC=+0.261 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.453 (IC base=+0.104)

- **PATRÓN** `libro_liquidez` > `2689.6584` → IC=+0.144 (n=144)

  - _Acción_: Kelly boost +0.72€ cuando `libro_liquidez` > 2689.6584 (IC base=+0.104)

- **PATRÓN** `sigma_h` < `0.0087` → IC=+0.154 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0087 (IC base=+0.105)

- **PATRÓN** `drift_15min` |x|≤ `0.4799` → IC=+0.143 (n=110)

  - _Acción_: Kelly boost +0.71€ cuando `drift_15min` |x|≤ 0.4799 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.170 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 5.0 (IC base=+0.105)

- **PATRÓN** `ibs_15` < `0.4444` → IC=+0.189 (n=223)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.94€ cuando `ibs_15` < 0.4444 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.798` → IC=+0.125 (n=254)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 6.798 (IC base=+0.105)

- **PATRÓN** `libro_liquidez` > `3830.5978` → IC=+0.152 (n=113)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 3830.5978 (IC base=+0.105)

### UPDOWN_GBM_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.214 (n=131)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0067 (IC base=+0.171)

- **PATRÓN** `drift_60min` |x|≤ `0.0733` → IC=+0.232 (n=80)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0733 (IC base=+0.171)

- **PATRÓN** `delta_ratio_macro` |x|> `0.2268` → IC=+0.177 (n=60)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.89€ cuando `delta_ratio_macro` |x|> 0.2268 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.167 (n=181)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 4.0 (IC base=+0.171)

- **PATRÓN** `ibs_15` > `0.5` → IC=+0.214 (n=180)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.5 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.3464` → IC=+0.241 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3464 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.0823` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.0823 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.559` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 6.559 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.694` → IC=+0.161 (n=166)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` < 10.694 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.141 (n=165)

  - _Acción_: Kelly boost +0.70€ cuando `libro_spread` < 0.01 (IC base=+0.171)

- **PATRÓN** `libro_liquidez` > `2778.5195` → IC=+0.152 (n=159)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2778.5195 (IC base=+0.171)

- **PATRÓN** `sigma_h` < `0.007` → IC=+0.218 (n=147)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.007 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.211 (n=392)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0074 (IC base=+0.209)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1689` → IC=+0.185 (n=195)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.93€ cuando `delta_ratio_macro` |x|> 0.1689 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.238 (n=204)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.209)

- **PATRÓN** `ibs_15` < `0.3571` → IC=+0.267 (n=256)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.3571 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.7875` → IC=+0.271 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7875 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.21` → IC=+0.192 (n=37)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 20.21 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.212 (n=269)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `2792.8241` → IC=+0.191 (n=260)

  - _Acción_: Kelly boost +0.95€ cuando `libro_liquidez` > 2792.8241 (IC base=+0.209)

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `146.1132` → IC=+0.452 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.345)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9838` → IC=+0.260 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9838 (IC base=+0.252)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.252)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `145.8281` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.8281 (IC base=+0.276)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` < `146.1681` → IC=+0.431 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 146.1681 (IC base=+0.435)

- **PATRÓN** `T_h` > `111.9981` → IC=+0.444 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9981 (IC base=+0.435)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5954 sube el IC de +0.064 a +0.177 en UPDOWN_GBM#15min (n=682). Ya aplicado como kelly_boost=+0.88€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.6354 sube el IC de +0.105 a +0.219 en UPDOWN_GBM#BTC#15min (n=283). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6644 sube el IC de +0.056 a +0.192 en UPDOWN_GBM#ETH#15min (n=219). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5385 sube el IC de +0.150 a +0.220 en UPDOWN_GBM_15M_TARDIO (n=772). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.4444 sube el IC de +0.182 a +0.238 en UPDOWN_GBM_15M_TARDIO (n=906). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7488 sube el IC de +0.161 a +0.271 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=120). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.7007 sube el IC de +0.118 a +0.289 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=126). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.0419 sube el IC de +0.276 a +0.413 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=44). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.7419 sube el IC de +0.104 a +0.296 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=96). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.4444 sube el IC de +0.105 a +0.189 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=223). Ya aplicado como kelly_boost=+0.94€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.171 a +0.214 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=180). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3571 sube el IC de +0.209 a +0.267 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=256). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO#XRP#15min` — IC=+0.141 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min` — IC=+0.321 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL` — IC=+0.321 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min` — IC=+0.350 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH` — IC=+0.350 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min` — IC=+0.316 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC` — IC=+0.316 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1662 | +0.054 | -26.52€ | 0 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1662 | +0.054 | -26.52€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 719 | +0.030 | -32.27€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 719 | +0.030 | -32.27€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 617 | +0.072 | -12.59€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 617 | +0.072 | -12.59€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 307 | +0.073 | +18.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 307 | +0.073 | +18.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 1151 | -0.039 | -101.68€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS#15min | 307 | +0.277 | -10.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 844 | -0.154 | -90.93€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#BNB | 220 | -0.293 | -28.88€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#BNB#5min | 220 | -0.293 | -28.88€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 307 | +0.277 | -10.75€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 307 | +0.277 | -10.75€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS#DOGE | 193 | -0.105 | -37.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 193 | -0.105 | -37.87€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 162 | -0.189 | +11.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 162 | -0.189 | +11.86€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 158 | -0.144 | -23.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 158 | -0.144 | -23.68€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 111 | +0.084 | -12.36€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 111 | +0.084 | -12.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 19718 | +0.122 | -461.61€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 5487 | +0.194 | -105.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 421 | +0.056 | -31.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 12156 | +0.090 | -381.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 1654 | +0.143 | +57.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 1903 | +0.084 | -97.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 9 | -0.021 | -4.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 1891 | +0.085 | -95.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 4433 | +0.134 | -78.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1780 | +0.185 | -83.98€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 136 | +0.051 | -15.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 1898 | +0.085 | -43.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 619 | +0.155 | +63.99€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 1906 | +0.079 | -95.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 15 | +0.243 | +10.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 1890 | +0.076 | -107.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 4768 | +0.141 | -14.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1791 | +0.197 | -3.78€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 137 | -0.004 | -26.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 2305 | +0.109 | +13.22€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 535 | +0.126 | +2.08€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#SOL | 4775 | +0.138 | -141.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1855 | +0.201 | -22.66€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 142 | +0.111 | +6.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 2278 | +0.086 | -116.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 500 | +0.145 | -8.83€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 1933 | +0.093 | -33.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 37 | +0.141 | -1.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 1894 | +0.092 | -31.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 1475 | +0.210 | -99.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 1475 | +0.210 | -99.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 165 | +0.153 | -20.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 165 | +0.153 | -20.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 429 | +0.208 | -15.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 429 | +0.208 | -15.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 174 | +0.136 | -25.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 174 | +0.136 | -25.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 437 | +0.277 | -5.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 437 | +0.277 | -5.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 102 | +0.279 | -2.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 102 | +0.279 | -2.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 168 | +0.123 | -29.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 168 | +0.123 | -29.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 77 | +0.411 | -2.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 77 | +0.411 | -2.72€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 22 | +0.333 | -2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 22 | +0.333 | -2.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 27 | +0.431 | +0.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 27 | +0.431 | +0.52€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 20 | +0.409 | -0.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 20 | +0.409 | -0.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 7798 | +0.200 | -531.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 7798 | +0.200 | -531.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 1396 | +0.160 | -181.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 1396 | +0.160 | -181.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 1240 | +0.219 | -35.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 1240 | +0.219 | -35.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 1333 | +0.188 | -122.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 1333 | +0.188 | -122.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 1254 | +0.225 | -29.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 1254 | +0.225 | -29.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 1279 | +0.211 | -62.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 1279 | +0.211 | -62.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 1296 | +0.200 | -100.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 1296 | +0.200 | -100.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 235 | +0.289 | -5.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 235 | +0.289 | -5.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 95 | +0.283 | +0.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 95 | +0.283 | +0.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 103 | +0.271 | -6.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 103 | +0.271 | -6.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 37 | +0.321 | +0.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 37 | +0.321 | +0.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 86 | +0.330 | -15.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 86 | +0.330 | -15.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 36 | +0.316 | -7.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 36 | +0.316 | -7.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 38 | +0.350 | -6.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 38 | +0.350 | -6.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 12 | +0.129 | -1.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 12 | +0.129 | -1.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 573 | +0.300 | -1.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 573 | +0.300 | -1.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 573 | +0.300 | -1.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 573 | +0.300 | -1.87€ | 0 | 0 |
| ✅ GBM_LATE_15M | 11979 | +0.102 | +3897.81€ | 0 | 5 |
| ✅ GBM_LATE_15M#15min | 11979 | +0.102 | +3897.81€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 741 | +0.149 | +383.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 741 | +0.149 | +383.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 2492 | +0.083 | +491.42€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2492 | +0.083 | +491.42€ | 0 | 6 |
| ✅ GBM_LATE_15M#DOGE | 750 | +0.157 | +378.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 750 | +0.157 | +378.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH | 2261 | +0.068 | +343.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2261 | +0.068 | +343.75€ | 0 | 7 |
| ✅ GBM_LATE_15M#SOL | 2675 | +0.079 | +849.55€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2675 | +0.079 | +849.55€ | 1 | 2 |
| ✅ GBM_LATE_15M#XRP | 3060 | +0.136 | +1450.92€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 3060 | +0.136 | +1450.92€ | 0 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 9339 | +0.129 | +4677.62€ | 0 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 9339 | +0.129 | +4677.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 609 | +0.210 | +486.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 609 | +0.210 | +486.80€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2057 | +0.090 | +701.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2057 | +0.090 | +701.66€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 657 | +0.200 | +489.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 657 | +0.200 | +489.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1988 | +0.090 | +672.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1988 | +0.090 | +672.33€ | 0 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 2058 | +0.084 | +774.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 2058 | +0.084 | +774.94€ | 0 | 7 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1970 | +0.207 | +1552.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1970 | +0.207 | +1552.23€ | 0 | 11 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 57 | +0.314 | +22.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 57 | +0.314 | +22.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 6 | +0.113 | +2.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 6 | +0.113 | +2.96€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 12 | +0.086 | +1.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 12 | +0.086 | +1.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 11 | +0.148 | +4.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 11 | +0.148 | +4.67€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 5 | +0.054 | +1.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 5 | +0.054 | +1.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 10 | +0.167 | +4.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 10 | +0.167 | +4.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 13 | +0.195 | +7.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 13 | +0.195 | +7.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 412 | +0.048 | +95.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 412 | +0.048 | +95.41€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC | 9 | -0.102 | -1.94€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 9 | -0.102 | -1.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 230 | -0.030 | -1.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 230 | -0.030 | -1.95€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL | 8 | -0.120 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 8 | -0.120 | -1.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 165 | +0.195 | +101.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 165 | +0.195 | +101.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 9231 | +0.083 | +3051.09€ | 0 | 3 |
| ✅ GBM_LATE_15M_TARDIO#15min | 9231 | +0.083 | +3051.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 681 | +0.179 | +438.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 681 | +0.179 | +438.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1800 | +0.035 | +248.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1800 | +0.035 | +248.81€ | 0 | 1 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 703 | +0.184 | +451.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 703 | +0.184 | +451.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1835 | +0.026 | +173.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1835 | +0.026 | +173.47€ | 0 | 2 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1921 | +0.017 | +346.07€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1921 | +0.017 | +346.07€ | 0 | 1 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 2291 | +0.163 | +1392.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 2291 | +0.163 | +1392.55€ | 0 | 10 |
| ✅ GBM_LATE_5M | 1415 | -0.019 | +34.43€ | 4 | 0 |
| ✅ GBM_LATE_5M#5min | 1415 | -0.019 | +34.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 315 | +0.030 | +33.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 315 | +0.030 | +33.99€ | 6 | 7 |
| 🚫 GBM_LATE_5M#ETH | 82 | -0.202 | -15.93€ | 0 | 0 |
| 🚫 GBM_LATE_5M#ETH#5min | 82 | -0.202 | -15.93€ | 7 | 0 |
| ✅ GBM_LATE_5M#SOL | 552 | -0.045 | +9.57€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 552 | -0.045 | +9.57€ | 9 | 1 |
| ✅ GBM_LATE_5M#XRP | 466 | +0.013 | +6.80€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 466 | +0.013 | +6.80€ | 0 | 0 |
| ✅ GBM_LATE_60M | 367 | -0.080 | +24.78€ | 2 | 3 |
| ✅ GBM_LATE_60M#60min | 367 | -0.080 | +24.78€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 133 | -0.026 | +2.61€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 133 | -0.026 | +2.61€ | 3 | 1 |
| ✅ GBM_LATE_60M#ETH | 122 | -0.081 | +8.75€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 122 | -0.081 | +8.75€ | 3 | 1 |
| ✅ GBM_LATE_60M#SOL | 112 | -0.140 | +13.42€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 112 | -0.140 | +13.42€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE | 8 | -0.160 | -4.08€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 8 | -0.160 | -4.08€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 17 | -0.067 | -1.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 17 | -0.067 | -1.31€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 8 | +0.000 | +0.65€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 8 | +0.000 | +0.65€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 7 | -0.058 | -1.56€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 7 | -0.058 | -1.56€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 392 | -0.064 | -7.16€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 392 | -0.064 | -7.16€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 392 | -0.064 | -7.16€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 392 | -0.064 | -7.16€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 324 | +0.015 | +12.60€ | 1 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 324 | +0.015 | +12.60€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 324 | +0.015 | +12.60€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 324 | +0.015 | +12.60€ | 1 | 0 |
| 🚫 LIQUIDACIONES_15M | 9 | -0.143 | -3.73€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#15min | 9 | -0.143 | -3.73€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M | 33 | -0.214 | -7.83€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#5min | 33 | -0.214 | -7.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 9 | -0.021 | -0.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 9 | -0.021 | -0.61€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#ETH | 8 | -0.120 | -3.00€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#ETH#5min | 8 | -0.120 | -3.00€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL | 8 | -0.120 | -3.09€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL#5min | 8 | -0.120 | -3.09€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 5 | -0.018 | -0.60€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 5 | -0.018 | -0.60€ | 0 | 0 |
| 🚫 LIQUIDACIONES_60M | 12 | -0.171 | -4.21€ | 0 | 0 |
| 🚫 LIQUIDACIONES_60M#60min | 12 | -0.171 | -4.21€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1716 | +0.014 | +15.71€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1580 | +0.010 | +3.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 221 | +0.043 | +6.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 221 | +0.043 | +6.54€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 232 | +0.009 | -0.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 232 | +0.009 | -0.28€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 275 | -0.016 | -8.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 275 | -0.016 | -8.15€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 338 | +0.044 | +14.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 338 | +0.044 | +14.88€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#XRP | 223 | -0.002 | -4.63€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 223 | -0.002 | -4.63€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM | 193 | -0.162 | -5.71€ | 2 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 74 | -0.224 | -18.33€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 63 | -0.254 | -16.39€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 11 | -0.021 | -1.94€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 77 | -0.171 | -1.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 64 | -0.197 | -3.83€ | 3 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 13 | -0.022 | +2.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 42 | -0.023 | +14.21€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 37 | +0.013 | +15.46€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#reach | 5 | -0.054 | -1.25€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 164 | -0.175 | -4.76€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 29 | -0.081 | -0.95€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE | 7 | -0.058 | -1.28€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#atexpiry | 7 | -0.058 | -1.28€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 26 | +0.250 | +3.90€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 9 | +0.021 | -1.03€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 9 | +0.021 | -1.03€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 12 | +0.257 | +3.52€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 12 | +0.257 | +3.52€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 26 | +0.250 | +3.90€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 307 | +0.060 | +19.35€ | 1 | 1 |
| ✅ STREAK_FADE_15M#15min | 307 | +0.060 | +19.35€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 64 | +0.030 | -3.55€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 64 | +0.030 | -3.55€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 88 | +0.122 | +20.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 88 | +0.122 | +20.43€ | 0 | 2 |
| ✅ STREAK_FADE_15M#XRP | 152 | +0.039 | +3.23€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 152 | +0.039 | +3.23€ | 0 | 3 |
| ✅ STREAK_FADE_5M | 247 | -0.050 | -25.47€ | 3 | 0 |
| ✅ STREAK_FADE_5M#5min | 247 | -0.050 | -25.47€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 47 | -0.153 | -8.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 47 | -0.153 | -8.07€ | 3 | 0 |
| ✅ STREAK_FADE_5M#SOL | 95 | -0.026 | -8.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 95 | -0.026 | -8.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP | 105 | -0.023 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 105 | -0.023 | -9.27€ | 0 | 0 |
| 🚫 STREAK_MOM_5M | 320 | -0.059 | -26.41€ | 4 | 0 |
| ✅ STREAK_MOM_5M#5min | 320 | -0.059 | -26.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 107 | -0.060 | -7.33€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 107 | -0.060 | -7.33€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 115 | -0.013 | -5.74€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 115 | -0.013 | -5.74€ | 2 | 0 |
| ✅ STREAK_MOM_5M#XRP | 98 | -0.110 | -13.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 98 | -0.110 | -13.35€ | 5 | 0 |
| 🚫 STRUCT_NO_15M | 15 | -0.199 | -4.68€ | 0 | 0 |
| 🚫 STRUCT_NO_15M#15min | 15 | -0.199 | -4.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ UPDOWN_GBM | 3816 | +0.061 | +548.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 3552 | +0.075 | +587.50€ | 0 | 5 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 131 | -0.064 | -11.72€ | 3 | 0 |
| ✅ UPDOWN_GBM#BNB | 441 | +0.098 | +107.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 441 | +0.098 | +107.84€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 676 | +0.063 | +89.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 592 | +0.093 | +103.78€ | 0 | 7 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 43 | -0.078 | -6.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 391 | +0.032 | +19.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 388 | +0.033 | +20.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1336 | +0.056 | +144.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1242 | +0.068 | +155.96€ | 0 | 4 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 55 | -0.026 | -3.07€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 465 | +0.022 | +45.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 395 | +0.049 | +52.86€ | 2 | 1 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 33 | -0.100 | -1.97€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 505 | +0.096 | +143.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 494 | +0.103 | +146.82€ | 3 | 4 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 279 | +0.311 | +62.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 279 | +0.311 | +62.11€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 133 | +0.322 | +34.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 133 | +0.322 | +34.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 146 | +0.297 | +27.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 146 | +0.297 | +27.34€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 3283 | +0.168 | +1721.65€ | 0 | 22 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 3283 | +0.168 | +1721.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 347 | +0.228 | +270.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 347 | +0.228 | +270.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 345 | +0.082 | +66.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 345 | +0.082 | +66.03€ | 1 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 339 | +0.201 | +230.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 339 | +0.201 | +230.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 589 | +0.189 | +254.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 589 | +0.189 | +254.48€ | 1 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 682 | +0.105 | +224.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 682 | +0.105 | +224.45€ | 2 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 981 | +0.194 | +676.22€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 981 | +0.194 | +676.22€ | 0 | 20 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 30 | +0.000 | +0.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 30 | +0.000 | +0.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 30 | +0.000 | +0.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 30 | +0.000 | +0.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 96 | +0.296 | +65.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 96 | +0.296 | +65.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 50 | +0.288 | +29.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 50 | +0.288 | +29.52€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 46 | +0.292 | +35.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 46 | +0.292 | +35.53€ | 0 | 0 |
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
| ✅ WEEKLY_PRICE | 617 | +0.256 | +220.45€ | 0 | 1 |
| ✅ WEEKLY_PRICE#BTC | 186 | +0.160 | -11.63€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 175 | +0.201 | +6.71€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 256 | +0.360 | +225.37€ | 0 | 2 |