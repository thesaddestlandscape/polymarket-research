# Hipótesis automáticas — 2026-08-07 20:28 UTC
_Generado por shadow_postmortem.py sobre 88331 resoluciones (PNL=+13665.14€)_

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
- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.189 (n=2273)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0066 (IC base=+0.146)

- **PATRÓN** `drift_60min` |x|≤ `0.1096` → IC=+0.265 (n=32)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1096 (IC base=+0.146)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.156 (n=3188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 7.0 (IC base=+0.146)

- **PATRÓN** `dist_vwap_pct` > `0.2919` → IC=+0.172 (n=814)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.2919 (IC base=+0.146)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.024` → IC=+0.245 (n=1291)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.024 (IC base=+0.146)

- **PATRÓN** `libro_liquidez` > `2043.4085` → IC=+0.152 (n=3052)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 2043.4085 (IC base=+0.146)

- **PATRÓN** `sigma_h` > `0.004` → IC=+0.162 (n=3096)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.004 (IC base=+0.147)

- **PATRÓN** `drift_60min` |x|≤ `0.104` → IC=+0.216 (n=65)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.104 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.152 (n=2099)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 12.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.156 (n=1165)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 6.0 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.6131` → IC=+0.150 (n=321)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.6131 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.141` → IC=+0.171 (n=514)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 8.141 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.837` → IC=+0.147 (n=2553)

  - _Acción_: Kelly boost +0.74€ cuando `sigma_ewma_delta_pct` < 2.837 (IC base=+0.147)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `sigma_h` < `0.0022` → IC=+0.146 (n=190)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0022 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.139 (n=532)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 7.0 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `0.4991` → IC=+0.154 (n=76)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.4991 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.327` → IC=+0.181 (n=111)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 12.327 (IC base=+0.114)

- **PATRÓN** `libro_liquidez` > `11121.4124` → IC=+0.153 (n=312)

  - _Acción_: Kelly boost +0.76€ cuando `libro_liquidez` > 11121.4124 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.708` → IC=+0.194 (n=122)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 11.708 (IC base=+0.108)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.157 (n=208)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0072 (IC base=+0.117)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.127 (n=218)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 5.0 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.6205` → IC=+0.150 (n=115)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.6205 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.339` → IC=+0.166 (n=288)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 4.339 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `7684.6866` → IC=+0.139 (n=347)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 7684.6866 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.489` → IC=+0.169 (n=167)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` > 9.489 (IC base=+0.076)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `drift_60min` |x|> `0.2045` → IC=-0.206 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.2045
  - _Potencial_: sin este filtro IC_bueno=+0.026 (n=17)

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
- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.225 (n=758)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.198)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.214 (n=763)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.198)

- **PATRÓN** `dist_vwap_pct` > `0.1226` → IC=+0.223 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1226 (IC base=+0.198)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.006` → IC=+0.336 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.006 (IC base=+0.198)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=703)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.198)

- **PATRÓN** `libro_liquidez` > `3148.2286` → IC=+0.195 (n=231)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 3148.2286 (IC base=+0.198)

- **PATRÓN** `sigma_h` > `0.0063` → IC=+0.241 (n=774)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0063 (IC base=+0.227)

- **PATRÓN** `drift_60min` |x|≤ `0.4099` → IC=+0.327 (n=50)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.4099 (IC base=+0.227)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.254 (n=538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.227)

- **PATRÓN** `dist_vwap_pct` > `0.8279` → IC=+0.353 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8279 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.231` → IC=+0.240 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.231 (IC base=+0.227)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.625` → IC=+0.224 (n=707)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.625 (IC base=+0.227)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.245 (n=695)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.227)

### GBM_LATE_15M_MULTIHORIZONTE
- **PATRÓN** `sigma_h` > `0.0059` → IC=+0.364 (n=57)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0059 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.286 (n=40)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.282)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.300 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.814` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.814 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` < `12.435` → IC=+0.347 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 12.435 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `1187.4102` → IC=+0.297 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1187.4102 (IC base=+0.282)

- **PATRÓN** `sigma_h` > `0.0034` → IC=+0.210 (n=267)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0034 (IC base=+0.190)

- **PATRÓN** `drift_60min` |x|≤ `0.0997` → IC=+0.233 (n=88)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.0997 (IC base=+0.190)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.234 (n=186)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.190)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.495` → IC=+0.225 (n=234)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.495 (IC base=+0.190)

- **PATRÓN** `libro_liquidez` > `1365.6436` → IC=+0.207 (n=264)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1365.6436 (IC base=+0.190)

### GBM_LATE_15M_MULTIHORIZONTE#BTC#15min
- **PATRÓN** `sigma_h` < `0.0026` → IC=+0.132 (n=36)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0026 (IC base=+0.130)

- **PATRÓN** `sigma_h` > `0.0021` → IC=+0.143 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0021 (IC base=+0.130)

- **PATRÓN** `drift_60min` |x|≤ `0.0892` → IC=+0.192 (n=24)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.96€ cuando `drift_60min` |x|≤ 0.0892 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.200 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.275` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.275 (IC base=+0.130)

- **PATRÓN** `libro_liquidez` > `4027.3872` → IC=+0.194 (n=47)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 4027.3872 (IC base=+0.130)

### GBM_LATE_15M_MULTIHORIZONTE#ETH#15min
- **PATRÓN** `sigma_h` < `0.003` → IC=+0.273 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.003 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.753` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.753 (IC base=+0.129)

### GBM_LATE_15M_MULTIHORIZONTE#SOL#15min
- **PATRÓN** `drift_60min` |x|≤ `0.3552` → IC=+0.128 (n=49)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.64€ cuando `drift_60min` |x|≤ 0.3552 (IC base=+0.079)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.200 (n=28)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 14.0 (IC base=+0.079)

- **PATRÓN** `libro_liquidez` > `2061.8019` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2061.8019 (IC base=+0.079)

### GBM_LATE_15M_MULTIHORIZONTE#XRP#15min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.293 (n=56)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0089 (IC base=+0.276)

- **PATRÓN** `sigma_h` > `0.0066` → IC=+0.293 (n=56)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0066 (IC base=+0.276)

- **PATRÓN** `drift_60min` |x|≤ `0.1429` → IC=+0.309 (n=19)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1429 (IC base=+0.276)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.326 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 4.0 (IC base=+0.276)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.804` → IC=+0.289 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 2.804 (IC base=+0.276)

- **PATRÓN** `libro_liquidez` > `1592.3808` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1592.3808 (IC base=+0.276)

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

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.336 (n=65)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.282)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.328 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` > `0.361` → IC=+0.300 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.361 (IC base=+0.282)

- **PATRÓN** `dist_vwap_pct` < `0.0981` → IC=+0.287 (n=106)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0981 (IC base=+0.282)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.768` → IC=+0.387 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.768 (IC base=+0.282)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.301 (n=164)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.282)

- **PATRÓN** `libro_liquidez` > `3192.5533` → IC=+0.304 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3192.5533 (IC base=+0.282)

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

- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.346 (n=50)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0039 (IC base=+0.351)

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

- **PATRÓN** `sigma_h` < `0.0085` → IC=+0.239 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0085 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0201` → IC=+0.233 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0201 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.230 (n=61)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.759` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.759 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.558` → IC=+0.167 (n=58)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` < 3.558 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `1928.5167` → IC=+0.198 (n=61)

  - _Acción_: Kelly boost +0.99€ cuando `libro_liquidez` > 1928.5167 (IC base=+0.163)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0069` → IC=+0.126 (n=2286)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` > 0.0069 (IC base=+0.098)

- **PATRÓN** `drift_60min` |x|≤ `0.1227` → IC=+0.218 (n=37)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1227 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.999` → IC=+0.214 (n=1230)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.999 (IC base=+0.098)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `10.972` → IC=+0.169 (n=134)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` > 10.972 (IC base=+0.066)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `12.755` → IC=+0.154 (n=102)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 12.755 (IC base=+0.056)

- **PATRÓN** `libro_liquidez` > `8939.1851` → IC=+0.156 (n=219)

  - _Acción_: Kelly boost +0.78€ cuando `libro_liquidez` > 8939.1851 (IC base=+0.056)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `8.047` → IC=+0.271 (n=151)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.047 (IC base=+0.040)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.167 (n=861)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0068 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.162 (n=904)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 5.0 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.6671` → IC=+0.206 (n=141)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6671 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.554` → IC=+0.288 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.554 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.160 (n=739)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.01 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0065` → IC=+0.188 (n=925)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0065 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.195 (n=640)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 12.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.180 (n=329)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.7543` → IC=+0.269 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7543 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=816)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.176)

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

- **PATRÓN** `sigma_ewma_delta_pct` > `6.463` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 6.463 (IC base=+0.009)

### GBM_LATE_60M
- **FILTRO** `sigma_ewma_delta_pct` < `5.379` → IC=-0.259 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 5.379
  - _Potencial_: sin este filtro IC_bueno=+0.220 (n=48)

- **FILTRO** `sigma_h` > `0.011` → IC=-0.286 (n=54)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.011
  - _Potencial_: sin este filtro IC_bueno=-0.151 (n=107)

- **FILTRO** `hora_utc` > `6.0` → IC=-0.260 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=-0.023 (n=42)

- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.141 (n=76)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0046 (IC base=+0.011)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.379` → IC=+0.220 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.379 (IC base=+0.011)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `sigma_h` > `0.0045` → IC=-0.122 (n=43)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0045
  - _Potencial_: sin este filtro IC_bueno=+0.181 (n=45)

- **FILTRO** `dist_vwap_pct` < `0.1642` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1642
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

- **FILTRO** `sigma_h` > `0.0035` → IC=-0.167 (n=34)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0035
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=17)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.194 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.132 (n=17)

- **PATRÓN** `sigma_h` < `0.0032` → IC=+0.180 (n=23)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0032 (IC base=+0.033)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_ewma_delta_pct` < `5.134` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 5.134
  - _Potencial_: sin este filtro IC_bueno=+0.315 (n=25)

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

- **PATRÓN** `dist_vwap_pct` < `0.1247` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.1247 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.134` → IC=+0.315 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.134 (IC base=+0.034)

### GBM_LATE_60M#SOL#60min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.129 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

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
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0132 (IC base=-0.064)

### LEADLAG_BTC_XRP_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=168)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=168)

### LIQUIDACIONES_15M
- **FILTRO** `hora_utc` < `16.0` → IC=-0.155 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `py_entrada` < `0.515` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.065 (n=21)

- **FILTRO** `liq_n` < `2.0` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `liq_n` < 2.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `liq_usd_total` < `7879.52` → IC=-0.182 (n=20)

  - _Acción_: SKIP cuando `liq_usd_total` < 7879.52
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `py_entrada` > `0.495` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `py_entrada` > 0.495
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=16)

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

- **FILTRO** `libro_liquidez` < `8260.6016` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `libro_liquidez` < 8260.6016
  - _Potencial_: sin este filtro IC_bueno=-0.167 (n=16)

- **FILTRO** `hora_utc` > `8.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 8.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

### LIQUIDACIONES_60M
- **FILTRO** `hora_utc` < `15.0` → IC=-0.237 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.409 (n=9)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=187)

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

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.156 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 7.0 (IC base=+0.051)

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
- **FILTRO** `volumen_racha` > `467605.9` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `volumen_racha` > 467605.9
  - _Potencial_: sin este filtro IC_bueno=+0.067 (n=28)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.144 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 9.0 (IC base=+0.061)

- **PATRÓN** `volumen_racha` < `641424.8` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `volumen_racha` < 641424.8 (IC base=+0.061)

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

- **FILTRO** `hora_utc` < `10.0` → IC=-0.222 (n=16)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 10.0
  - _Potencial_: sin este filtro IC_bueno=-0.149 (n=35)

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

- **PATRÓN** `sigma_h` < `0.0036` → IC=+0.124 (n=176)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0036 (IC base=+0.102)

- **PATRÓN** `drift_60min` |x|≤ `0.1888` → IC=+0.147 (n=284)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.73€ cuando `drift_60min` |x|≤ 0.1888 (IC base=+0.102)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0644` → IC=+0.134 (n=323)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.67€ cuando `delta_ratio_macro` |x|> 0.0644 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.175 (n=192)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 14.0 (IC base=+0.102)

- **PATRÓN** `ibs_15` > `0.6354` → IC=+0.219 (n=283)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6354 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.2571` → IC=+0.237 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2571 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `25.023` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 25.023 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `11672.79` → IC=+0.161 (n=113)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 11672.79 (IC base=+0.102)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `ibs_15` > `0.6644` → IC=+0.192 (n=219)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.6644 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.056` → IC=+0.158 (n=74)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 7.056 (IC base=+0.059)

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.165 (n=171)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.005 (IC base=+0.081)

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
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.149 (n=406)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0048 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0055` → IC=+0.157 (n=1060)
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

- **PATRÓN** `sigma_ewma_delta_pct` > `5.258` → IC=+0.189 (n=448)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 5.258 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `2545.0995` → IC=+0.133 (n=772)

  - _Acción_: Kelly boost +0.67€ cuando `libro_liquidez` > 2545.0995 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.184 (n=634)
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

- **PATRÓN** `ibs_15` < `0.4444` → IC=+0.238 (n=906)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.4444 (IC base=+0.175)

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

- **FILTRO** `sigma_h` < `0.0043` → IC=-0.151 (n=81)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0043
  - _Potencial_: sin este filtro IC_bueno=-0.018 (n=81)

- **PATRÓN** `sigma_h` < `0.0037` → IC=+0.172 (n=123)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0037 (IC base=+0.150)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.151 (n=164)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.003 (IC base=+0.150)

- **PATRÓN** `drift_60min` |x|≤ `0.1123` → IC=+0.152 (n=90)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.76€ cuando `drift_60min` |x|≤ 0.1123 (IC base=+0.150)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0951` → IC=+0.180 (n=120)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.90€ cuando `delta_ratio_macro` |x|> 0.0951 (IC base=+0.150)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.175 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 16.0 (IC base=+0.150)

- **PATRÓN** `ibs_15` > `0.7488` → IC=+0.271 (n=120)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7488 (IC base=+0.150)

- **PATRÓN** `dist_vwap_pct` > `0.2256` → IC=+0.203 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2256 (IC base=+0.150)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.379` → IC=+0.182 (n=83)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 9.379 (IC base=+0.150)

- **PATRÓN** `libro_liquidez` > `11198.676` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 11198.676 (IC base=+0.150)

- **PATRÓN** `drift_15min` |x|≤ `0.5515` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `drift_15min` |x|≤ 0.5515 (IC base=-0.085)

- **PATRÓN** `ibs_15` < `0.5537` → IC=+0.139 (n=34)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.69€ cuando `ibs_15` < 0.5537 (IC base=-0.085)

- **PATRÓN** `libro_liquidez` > `9476.9221` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 9476.9221 (IC base=-0.085)

### UPDOWN_GBM_15M_TARDIO#ETH#15min
- **FILTRO** `ibs_15` < `0.5405` → IC=-0.143 (n=82)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.5405
  - _Potencial_: sin este filtro IC_bueno=+0.202 (n=169)

- **PATRÓN** `sigma_h` > `0.0064` → IC=+0.182 (n=86)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0064 (IC base=+0.124)

- **PATRÓN** `drift_60min` |x|≤ `0.045` → IC=+0.162 (n=63)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.81€ cuando `drift_60min` |x|≤ 0.045 (IC base=+0.124)

- **PATRÓN** `ibs_15` > `0.7007` → IC=+0.289 (n=126)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7007 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.922` → IC=+0.163 (n=78)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 7.922 (IC base=+0.124)

- **PATRÓN** `libro_liquidez` > `7672.3115` → IC=+0.133 (n=126)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 7672.3115 (IC base=+0.124)

- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.318 (n=97)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0048 (IC base=+0.269)

- **PATRÓN** `drift_60min` |x|≤ `0.1029` → IC=+0.370 (n=44)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +1.00€ cuando `drift_60min` |x|≤ 0.1029 (IC base=+0.269)

- **PATRÓN** `drift_15min` |x|≤ `0.4473` → IC=+0.304 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `drift_15min` |x|≤ 0.4473 (IC base=+0.269)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.289 (n=93)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.269)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.271 (n=120)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.269)

- **PATRÓN** `ibs_15` < `0.0419` → IC=+0.413 (n=44)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.0419 (IC base=+0.269)

- **PATRÓN** `dist_vwap_pct` > `0.2534` → IC=+0.386 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2534 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` > `16.363` → IC=+0.292 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 16.363 (IC base=+0.269)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.671` → IC=+0.288 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 6.671 (IC base=+0.269)

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

### WEEKLY_PRICE
- **PATRÓN** `T_h` > `146.1332` → IC=+0.462 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1332 (IC base=+0.349)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `111.9965` → IC=+0.261 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9965 (IC base=+0.252)

- **PATRÓN** `T_h` > `111.9824` → IC=+0.253 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9824 (IC base=+0.252)

- **PATRÓN** `pct_dist` |x|≤ `0.6014` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.6014 (IC base=+0.252)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9966` → IC=+0.322 (n=99)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9966 (IC base=+0.285)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `135.9824` → IC=+0.455 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 135.9824 (IC base=+0.439)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.5954 sube el IC de +0.064 a +0.177 en UPDOWN_GBM#15min (n=682). Ya aplicado como kelly_boost=+0.88€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.6354 sube el IC de +0.102 a +0.219 en UPDOWN_GBM#BTC#15min (n=283). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6644 sube el IC de +0.059 a +0.192 en UPDOWN_GBM#ETH#15min (n=219). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_YES, IBS > 0.5385 sube el IC de +0.148 a +0.220 en UPDOWN_GBM_15M_TARDIO (n=772). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO**: dentro de BUY_NO, IBS < 0.4444 sube el IC de +0.175 a +0.238 en UPDOWN_GBM_15M_TARDIO (n=906). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#BTC#15min**: dentro de BUY_YES, IBS > 0.7488 sube el IC de +0.150 a +0.271 en UPDOWN_GBM_15M_TARDIO#BTC#15min (n=120). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_YES, IBS > 0.7007 sube el IC de +0.124 a +0.289 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=126). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#ETH#15min**: dentro de BUY_NO, IBS < 0.0419 sube el IC de +0.269 a +0.413 en UPDOWN_GBM_15M_TARDIO#ETH#15min (n=44). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_YES, IBS > 0.7419 sube el IC de +0.107 a +0.296 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=96). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#SOL#15min**: dentro de BUY_NO, IBS < 0.4444 sube el IC de +0.103 a +0.189 en UPDOWN_GBM_15M_TARDIO#SOL#15min (n=223). Ya aplicado como kelly_boost=+0.94€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_YES, IBS > 0.5 sube el IC de +0.170 a +0.214 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=180). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM_15M_TARDIO#XRP#15min**: dentro de BUY_NO, IBS < 0.3571 sube el IC de +0.211 a +0.267 en UPDOWN_GBM_15M_TARDIO#XRP#15min (n=256). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO#XRP#15min` — IC=+0.150 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min` — IC=+0.389 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC` — IC=+0.389 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min` — IC=+0.414 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH` — IC=+0.414 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1739 | +0.047 | -44.16€ | 0 | 4 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1739 | +0.047 | -44.16€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 786 | +0.017 | -51.38€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 786 | +0.017 | -51.38€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 622 | +0.070 | -12.41€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 622 | +0.070 | -12.41€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 312 | +0.073 | +19.97€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 312 | +0.073 | +19.97€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 1838 | -0.085 | -327.55€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS#15min | 374 | +0.197 | -46.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 1464 | -0.158 | -281.18€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#BNB | 330 | -0.322 | -86.63€ | 0 | 0 |
| 🚫 BALLENAS_TARDIAS#BNB#5min | 330 | -0.322 | -86.63€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 374 | +0.197 | -46.37€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 374 | +0.197 | -46.37€ | 0 | 1 |
| ✅ BALLENAS_TARDIAS#DOGE | 254 | -0.156 | -38.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#DOGE#5min | 254 | -0.156 | -38.91€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH | 305 | -0.076 | -7.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#ETH#5min | 305 | -0.076 | -7.66€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL | 300 | -0.189 | -56.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#SOL#5min | 300 | -0.189 | -56.45€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP | 275 | -0.013 | -91.54€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#XRP#5min | 275 | -0.013 | -91.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 23339 | +0.118 | -578.51€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 5923 | +0.195 | -100.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 437 | +0.051 | -38.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 15174 | +0.088 | -500.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 1805 | +0.142 | +61.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB | 2411 | +0.085 | -123.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#15min | 10 | +0.000 | -3.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#240min | 5 | +0.018 | +2.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BNB#5min | 2396 | +0.086 | -121.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 5103 | +0.129 | -101.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1881 | +0.182 | -100.21€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 140 | +0.056 | -14.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#5min | 2401 | +0.085 | -53.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 681 | +0.151 | +67.13€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 2409 | +0.077 | -136.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 15 | +0.243 | +10.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#5min | 2393 | +0.075 | -148.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 5504 | +0.136 | -19.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1969 | +0.198 | +12.60€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 143 | -0.017 | -32.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 2807 | +0.101 | -12.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 585 | +0.132 | +12.82€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#SOL | 5474 | +0.135 | -160.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 2010 | +0.204 | -19.34€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 146 | +0.108 | +4.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 2779 | +0.086 | -126.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 539 | +0.140 | -18.75€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 2438 | +0.092 | -38.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 38 | +0.150 | -0.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#5min | 2398 | +0.091 | -37.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 2043 | +0.198 | -155.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 2043 | +0.198 | -155.93€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB | 297 | +0.142 | -41.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min | 297 | +0.142 | -41.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 481 | +0.212 | -17.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 481 | +0.212 | -17.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE | 308 | +0.142 | -45.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min | 308 | +0.142 | -45.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 551 | +0.272 | -5.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 551 | +0.272 | -5.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 118 | +0.192 | -7.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 118 | +0.192 | -7.07€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP | 288 | +0.148 | -39.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min | 288 | +0.148 | -39.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 101 | +0.422 | -1.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 101 | +0.422 | -1.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC | 34 | +0.389 | -1.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#BTC#15min | 34 | +0.389 | -1.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH | 33 | +0.414 | -0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#ETH#15min | 33 | +0.414 | -0.86€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL | 25 | +0.426 | +0.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#SOL#15min | 25 | +0.426 | +0.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION | 9984 | +0.194 | -767.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#5min | 9984 | +0.194 | -767.83€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB | 1790 | +0.154 | -248.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min | 1790 | +0.154 | -248.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC | 1577 | +0.218 | -48.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BTC#5min | 1577 | +0.218 | -48.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE | 1724 | +0.181 | -179.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#DOGE#5min | 1724 | +0.181 | -179.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH | 1611 | +0.215 | -59.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#ETH#5min | 1611 | +0.215 | -59.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL | 1624 | +0.210 | -84.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#SOL#5min | 1624 | +0.210 | -84.25€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP | 1658 | +0.191 | -147.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#XRP#5min | 1658 | +0.191 | -147.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA | 202 | +0.132 | +11.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#5min | 202 | +0.132 | +11.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE | 98 | +0.120 | +2.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#DOGE#5min | 98 | +0.120 | +2.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP | 104 | +0.141 | +9.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_5MIN_BAJALATENCIA#XRP#5min | 104 | +0.141 | +9.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 288 | +0.266 | -22.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 288 | +0.266 | -22.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 120 | +0.238 | -13.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 120 | +0.238 | -13.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 128 | +0.262 | -10.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 128 | +0.262 | -10.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 40 | +0.333 | +1.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 40 | +0.333 | +1.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO | 105 | +0.360 | -13.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#60min | 105 | +0.360 | -13.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC | 43 | +0.344 | -6.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#BTC#60min | 43 | +0.344 | -6.48€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH | 49 | +0.382 | -5.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#ETH#60min | 49 | +0.382 | -5.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL | 13 | +0.152 | -1.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_EXTREMO#SOL#60min | 13 | +0.152 | -1.21€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 601 | +0.306 | +5.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 601 | +0.306 | +5.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 601 | +0.306 | +5.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 601 | +0.306 | +5.05€ | 0 | 0 |
| ✅ GBM_LATE_15M | 12557 | +0.102 | +4184.21€ | 0 | 5 |
| ✅ GBM_LATE_15M#15min | 12557 | +0.102 | +4184.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 827 | +0.162 | +466.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 827 | +0.162 | +466.97€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 2567 | +0.083 | +504.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2567 | +0.083 | +504.46€ | 0 | 6 |
| ✅ GBM_LATE_15M#DOGE | 830 | +0.168 | +457.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 830 | +0.168 | +457.75€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH | 2362 | +0.064 | +336.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 2362 | +0.064 | +336.00€ | 0 | 7 |
| ✅ GBM_LATE_15M#SOL | 2781 | +0.075 | +857.01€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2781 | +0.075 | +857.01€ | 1 | 2 |
| ✅ GBM_LATE_15M#XRP | 3190 | +0.134 | +1562.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 3190 | +0.134 | +1562.02€ | 0 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 9897 | +0.128 | +4977.30€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 9897 | +0.128 | +4977.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 694 | +0.214 | +559.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 694 | +0.214 | +559.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 2202 | +0.084 | +737.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 2202 | +0.084 | +737.98€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 721 | +0.211 | +570.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 721 | +0.211 | +570.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 2069 | +0.084 | +652.48€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 2069 | +0.084 | +652.48€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 2166 | +0.078 | +801.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 2166 | +0.078 | +801.97€ | 1 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 2045 | +0.212 | +1655.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 2045 | +0.212 | +1655.01€ | 0 | 13 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 432 | +0.207 | +310.15€ | 0 | 11 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 432 | +0.207 | +310.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB | 65 | +0.321 | +66.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BNB#15min | 65 | +0.321 | +66.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC | 85 | +0.121 | +24.92€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#BTC#15min | 85 | +0.121 | +24.92€ | 0 | 6 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE | 62 | +0.281 | +54.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#DOGE#15min | 62 | +0.281 | +54.17€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH | 60 | +0.129 | +24.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#ETH#15min | 60 | +0.129 | +24.11€ | 0 | 3 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL | 81 | +0.102 | +57.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#SOL#15min | 81 | +0.102 | +57.08€ | 0 | 3 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP | 79 | +0.290 | +83.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#XRP#15min | 79 | +0.290 | +83.64€ | 0 | 6 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 434 | +0.051 | +98.98€ | 5 | 7 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 434 | +0.051 | +98.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC | 13 | -0.108 | -3.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 13 | -0.108 | -3.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 233 | -0.032 | -1.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 233 | -0.032 | -1.79€ | 7 | 9 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL | 19 | -0.023 | +2.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 19 | -0.023 | +2.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 169 | +0.190 | +101.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 169 | +0.190 | +101.21€ | 0 | 15 |
| ✅ GBM_LATE_15M_TARDIO | 9694 | +0.085 | +3299.83€ | 0 | 3 |
| ✅ GBM_LATE_15M_TARDIO#15min | 9694 | +0.085 | +3299.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 754 | +0.191 | +521.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 754 | +0.191 | +521.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1880 | +0.036 | +257.52€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1880 | +0.036 | +257.52€ | 0 | 1 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 779 | +0.195 | +540.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 779 | +0.195 | +540.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1900 | +0.020 | +152.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1900 | +0.020 | +152.39€ | 0 | 2 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1998 | +0.016 | +355.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1998 | +0.016 | +355.02€ | 0 | 1 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 2383 | +0.165 | +1473.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 2383 | +0.165 | +1473.02€ | 0 | 10 |
| ✅ GBM_LATE_5M | 1507 | -0.016 | +38.89€ | 5 | 0 |
| ✅ GBM_LATE_5M#5min | 1507 | -0.016 | +38.89€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 315 | +0.030 | +33.99€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 315 | +0.030 | +33.99€ | 6 | 7 |
| ✅ GBM_LATE_5M#ETH | 107 | -0.151 | -17.75€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 107 | -0.151 | -17.75€ | 4 | 0 |
| ✅ GBM_LATE_5M#SOL | 608 | -0.044 | +12.55€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 608 | -0.044 | +12.55€ | 9 | 1 |
| ✅ GBM_LATE_5M#XRP | 477 | +0.020 | +10.09€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 477 | +0.020 | +10.09€ | 0 | 0 |
| ✅ GBM_LATE_60M | 388 | -0.077 | +18.21€ | 3 | 2 |
| ✅ GBM_LATE_60M#60min | 388 | -0.077 | +18.21€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 139 | -0.011 | +3.59€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 139 | -0.011 | +3.59€ | 4 | 1 |
| ✅ GBM_LATE_60M#ETH | 134 | -0.088 | +1.41€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 134 | -0.088 | +1.41€ | 4 | 2 |
| ✅ GBM_LATE_60M#SOL | 115 | -0.141 | +13.22€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 115 | -0.141 | +13.22€ | 4 | 1 |
| 🚫 GBM_LATE_60M_FADE | 96 | -0.357 | -27.69€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#60min | 96 | -0.357 | -27.69€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC | 32 | -0.265 | -5.38€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#BTC#60min | 32 | -0.265 | -5.38€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH | 34 | -0.389 | -12.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#ETH#60min | 34 | -0.389 | -12.46€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL | 30 | -0.375 | -9.86€ | 0 | 0 |
| 🚫 GBM_LATE_60M_FADE#SOL#60min | 30 | -0.375 | -9.86€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO | 75 | +0.019 | +1.78€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#60min | 75 | +0.019 | +1.78€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 32 | +0.059 | +1.03€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 32 | +0.059 | +1.03€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH | 5 | -0.054 | -1.93€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#ETH#60min | 5 | -0.054 | -1.93€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL | 38 | +0.025 | +2.68€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#SOL#60min | 38 | +0.025 | +2.68€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 393 | -0.062 | -6.68€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 393 | -0.062 | -6.68€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 393 | -0.062 | -6.68€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 393 | -0.062 | -6.68€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 327 | +0.017 | +13.04€ | 1 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 327 | +0.017 | +13.04€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 327 | +0.017 | +13.04€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 327 | +0.017 | +13.04€ | 1 | 0 |
| ✅ LIQUIDACIONES_15M | 69 | -0.106 | -9.06€ | 5 | 0 |
| ✅ LIQUIDACIONES_15M#15min | 69 | -0.106 | -9.06€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC | 18 | +0.000 | -0.38€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#BTC#15min | 18 | +0.000 | -0.38€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE | 10 | -0.125 | -3.21€ | 0 | 0 |
| 🚫 LIQUIDACIONES_15M#DOGE#15min | 10 | -0.125 | -3.21€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH | 16 | -0.044 | -1.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#ETH#15min | 16 | -0.044 | -1.37€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL | 11 | -0.021 | -0.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#SOL#15min | 11 | -0.021 | -0.75€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP | 13 | -0.108 | -2.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_15M#XRP#15min | 13 | -0.108 | -2.83€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M | 56 | -0.190 | -11.61€ | 5 | 0 |
| ✅ LIQUIDACIONES_5M#5min | 56 | -0.190 | -11.61€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC | 17 | -0.112 | -2.71€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#BTC#5min | 17 | -0.112 | -2.71€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#ETH | 12 | -0.129 | -3.06€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#ETH#5min | 12 | -0.129 | -3.06€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL | 14 | -0.175 | -4.14€ | 0 | 0 |
| 🚫 LIQUIDACIONES_5M#SOL#5min | 14 | -0.175 | -4.14€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP | 9 | -0.061 | -1.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_5M#XRP#5min | 9 | -0.061 | -1.66€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M | 67 | +0.007 | -0.86€ | 1 | 0 |
| ✅ LIQUIDACIONES_60M#60min | 67 | +0.007 | -0.86€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC | 25 | -0.018 | -1.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#BTC#60min | 25 | -0.018 | -1.13€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH | 19 | -0.023 | -0.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#ETH#60min | 19 | -0.023 | -0.63€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL | 23 | +0.060 | +0.89€ | 0 | 0 |
| ✅ LIQUIDACIONES_60M#SOL#60min | 23 | +0.060 | +0.89€ | 0 | 0 |
| ✅ ORDER_FLOW_5M | 1722 | +0.014 | +15.96€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1586 | +0.010 | +3.37€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 223 | +0.042 | +6.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 223 | +0.042 | +6.48€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 232 | +0.009 | -0.28€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 232 | +0.009 | -0.28€ | 1 | 0 |
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
| 🚫 PRICE_TARGET_GBM_FADE | 23 | -0.220 | -4.37€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC | 12 | -0.086 | -1.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM_FADE#BTC#atexpiry | 12 | -0.086 | -1.74€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH | 9 | -0.102 | -1.60€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#ETH#atexpiry | 9 | -0.102 | -1.60€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM_FADE#atexpiry | 23 | -0.220 | -4.37€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 27 | +0.259 | +4.05€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 9 | +0.021 | -1.03€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 9 | +0.021 | -1.03€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 13 | +0.282 | +3.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 13 | +0.282 | +3.67€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 27 | +0.259 | +4.05€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 319 | +0.058 | +14.76€ | 1 | 1 |
| ✅ STREAK_FADE_15M#15min | 319 | +0.058 | +14.76€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE | 10 | +0.000 | -3.28€ | 0 | 0 |
| ✅ STREAK_FADE_15M#DOGE#15min | 10 | +0.000 | -3.28€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 64 | +0.030 | -3.55€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 64 | +0.030 | -3.55€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 88 | +0.122 | +20.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 88 | +0.122 | +20.43€ | 0 | 2 |
| ✅ STREAK_FADE_15M#XRP | 157 | +0.035 | +1.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 157 | +0.035 | +1.17€ | 1 | 2 |
| ✅ STREAK_FADE_5M | 247 | -0.050 | -25.47€ | 3 | 0 |
| ✅ STREAK_FADE_5M#5min | 247 | -0.050 | -25.47€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 47 | -0.153 | -8.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 47 | -0.153 | -8.07€ | 3 | 0 |
| ✅ STREAK_FADE_5M#SOL | 95 | -0.026 | -8.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 95 | -0.026 | -8.13€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP | 105 | -0.023 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 105 | -0.023 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_60M | 5 | -0.054 | -1.57€ | 0 | 0 |
| ✅ STREAK_FADE_60M#60min | 5 | -0.054 | -1.57€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH | 5 | -0.054 | -1.57€ | 0 | 0 |
| ✅ STREAK_FADE_60M#ETH#60min | 5 | -0.054 | -1.57€ | 0 | 0 |
| 🚫 STREAK_MOM_5M | 320 | -0.059 | -26.41€ | 4 | 0 |
| ✅ STREAK_MOM_5M#5min | 320 | -0.059 | -26.41€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 107 | -0.060 | -7.33€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 107 | -0.060 | -7.33€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 115 | -0.013 | -5.74€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 115 | -0.013 | -5.74€ | 2 | 0 |
| ✅ STREAK_MOM_5M#XRP | 98 | -0.110 | -13.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 98 | -0.110 | -13.35€ | 5 | 0 |
| ✅ STRUCT_NO_15M | 287 | +0.026 | +1.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#15min | 287 | +0.026 | +1.96€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC | 90 | +0.054 | +2.87€ | 0 | 0 |
| ✅ STRUCT_NO_15M#BTC#15min | 90 | +0.054 | +2.87€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH | 108 | +0.036 | +2.16€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 108 | +0.036 | +2.16€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 89 | -0.017 | -3.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 89 | -0.017 | -3.07€ | 0 | 0 |
| ✅ UPDOWN_GBM | 3992 | +0.060 | +569.05€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 3724 | +0.074 | +609.04€ | 0 | 5 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 135 | -0.069 | -12.69€ | 4 | 0 |
| ✅ UPDOWN_GBM#BNB | 464 | +0.092 | +110.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 464 | +0.092 | +110.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 708 | +0.059 | +84.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 623 | +0.087 | +99.50€ | 1 | 8 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 44 | -0.087 | -7.18€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 412 | +0.031 | +20.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 409 | +0.033 | +21.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1381 | +0.059 | +157.63€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1287 | +0.071 | +169.19€ | 0 | 4 |
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
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 302 | +0.309 | +64.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 302 | +0.309 | +64.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 148 | +0.307 | +30.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 148 | +0.307 | +30.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 154 | +0.308 | +33.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 154 | +0.308 | +33.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 3497 | +0.163 | +1794.29€ | 0 | 21 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 3497 | +0.163 | +1794.29€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 380 | +0.217 | +282.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 380 | +0.217 | +282.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 406 | +0.056 | +55.50€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 406 | +0.056 | +55.50€ | 2 | 12 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 366 | +0.196 | +242.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 366 | +0.196 | +242.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 625 | +0.191 | +272.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 625 | +0.191 | +272.45€ | 1 | 14 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 694 | +0.105 | +229.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 694 | +0.105 | +229.08€ | 2 | 13 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 1026 | +0.195 | +712.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 1026 | +0.195 | +712.39€ | 0 | 20 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 32 | +0.000 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 32 | +0.000 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 32 | +0.000 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 32 | +0.000 | +0.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 129 | +0.271 | +75.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 129 | +0.271 | +75.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC | 68 | +0.243 | +28.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#BTC#15min | 68 | +0.243 | +28.84€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH | 61 | +0.294 | +46.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#ETH#15min | 61 | +0.294 | +46.99€ | 0 | 0 |
| ✅ UPDOWN_OU_5M | 318 | -0.172 | -55.04€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#5min | 318 | -0.172 | -55.04€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB | 55 | -0.184 | -11.55€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BNB#5min | 55 | -0.184 | -11.55€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC | 24 | -0.154 | -3.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#BTC#5min | 24 | -0.154 | -3.02€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE | 56 | -0.172 | -10.55€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#DOGE#5min | 56 | -0.172 | -10.55€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH | 36 | -0.184 | -5.38€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#ETH#5min | 36 | -0.184 | -5.38€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL | 65 | -0.157 | -9.39€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#SOL#5min | 65 | -0.157 | -9.39€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP | 82 | -0.155 | -15.15€ | 0 | 0 |
| ✅ UPDOWN_OU_5M#XRP#5min | 82 | -0.155 | -15.15€ | 0 | 0 |
| ✅ WEEKLY_PRICE | 657 | +0.265 | +265.94€ | 0 | 1 |
| ✅ WEEKLY_PRICE#BTC | 194 | +0.163 | -11.71€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 191 | +0.215 | +22.50€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 272 | +0.369 | +255.14€ | 0 | 1 |