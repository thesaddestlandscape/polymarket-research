# Hipótesis automáticas — 2026-07-29 19:09 UTC
_Generado por shadow_postmortem.py sobre 42198 resoluciones (PNL=+9221.54€)_

## Patrones causales activos

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
- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.124 (n=637)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0067 (IC base=+0.106)

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
- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.158 (n=258)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0101 (IC base=+0.140)

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
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.193 (n=1377)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0078 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.170 (n=1853)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 8.0 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.2862` → IC=+0.178 (n=567)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.2862 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.206` → IC=+0.244 (n=693)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.206 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.139 (n=2269)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` > 0.0042 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.136 (n=1548)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 12.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.127 (n=839)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 6.0 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.6713` → IC=+0.136 (n=248)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.6713 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.797` → IC=+0.141 (n=494)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 5.797 (IC base=+0.124)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.139 (n=441)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 7.0 (IC base=+0.109)

- **PATRÓN** `dist_vwap_pct` > `0.4476` → IC=+0.172 (n=65)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.4476 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.697` → IC=+0.159 (n=86)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 11.697 (IC base=+0.109)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.309` → IC=+0.144 (n=209)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 4.309 (IC base=+0.090)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.185 (n=163)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.008 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.139 (n=325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 12.0 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.1183` → IC=+0.142 (n=224)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1183 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.315` → IC=+0.186 (n=135)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 7.315 (IC base=+0.117)

- **PATRÓN** `libro_liquidez` > `4495.7114` → IC=+0.124 (n=344)

  - _Acción_: Kelly boost +0.62€ cuando `libro_liquidez` > 4495.7114 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.389` → IC=+0.179 (n=110)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 9.389 (IC base=+0.084)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **PATRÓN** `sigma_h` > `0.0111` → IC=+0.210 (n=229)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0111 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.150 (n=453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 8.0 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.1896` → IC=+0.163 (n=191)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1896 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.397` → IC=+0.281 (n=222)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.397 (IC base=+0.120)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.121 (n=457)

  - _Acción_: Kelly boost +0.60€ cuando `libro_spread` < 0.01 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `1893.3924` → IC=+0.162 (n=374)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 1893.3924 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.296` → IC=+0.131 (n=445)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 2.296 (IC base=+0.091)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` < `0.0167` → IC=+0.236 (n=475)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0167 (IC base=+0.226)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.226 (n=316)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.237 (n=489)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.226)

- **PATRÓN** `dist_vwap_pct` > `0.513` → IC=+0.273 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.513 (IC base=+0.226)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.493` → IC=+0.360 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.493 (IC base=+0.226)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.220 (n=523)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.226)

- **PATRÓN** `sigma_h` < `0.0165` → IC=+0.213 (n=574)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0165 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.232 (n=573)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.233 (n=518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.1929` → IC=+0.322 (n=116)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1929 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.347` → IC=+0.210 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.347 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.119` → IC=+0.203 (n=632)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 9.119 (IC base=+0.209)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.222 (n=472)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.209)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.124 (n=1369)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` > 0.0083 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.4878` → IC=+0.138 (n=376)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.4878 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.764` → IC=+0.235 (n=341)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.764 (IC base=+0.098)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.4799` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.4799 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.355` → IC=+0.193 (n=73)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 12.355 (IC base=+0.072)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `7.945` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.945
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=515)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.134` → IC=+0.226 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.134 (IC base=+0.048)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0089` → IC=+0.173 (n=197)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0089 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.01` → IC=+0.174 (n=526)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` > 0.01 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.186 (n=301)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 15.0 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.4968` → IC=+0.236 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4968 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.665` → IC=+0.295 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.665 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=452)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0217` → IC=+0.162 (n=685)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0217 (IC base=+0.159)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.172 (n=684)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0076 (IC base=+0.159)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.181 (n=465)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 12.0 (IC base=+0.159)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.163 (n=241)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 6.0 (IC base=+0.159)

- **PATRÓN** `dist_vwap_pct` > `0.1405` → IC=+0.233 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1405 (IC base=+0.159)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.452` → IC=+0.158 (n=709)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 9.452 (IC base=+0.159)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.166 (n=546)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.159)

### GBM_LATE_60M
- **FILTRO** `sigma_ewma_delta_pct` < `11.142` → IC=-0.222 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 11.142
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

- **FILTRO** `sigma_h` > `0.0133` → IC=-0.300 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=118)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.272 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=44)

- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.173 (n=47)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0044 (IC base=-0.013)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `sigma_h` > `0.005` → IC=-0.125 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.005
  - _Potencial_: sin este filtro IC_bueno=+0.159 (n=39)

- **FILTRO** `dist_vwap_pct` < `0.1109` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1109
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

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

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.159 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.005 (IC base=+0.019)

### GBM_LATE_60M#ETH#60min
- **FILTRO** `sigma_h` > `0.0058` → IC=-0.125 (n=30)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0058
  - _Potencial_: sin este filtro IC_bueno=+0.118 (n=32)

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

### LEADLAG_BTC_XRP_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=159)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.009 (n=159)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.041 (n=157)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `total_vol_5m` < `197.886` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `total_vol_5m` < 197.886 (IC base=+0.031)

### ORDER_FLOW_5M#BTC#5min
- **FILTRO** `delta_ratio` |x|≤ `0.3925` → IC=-0.180 (n=23)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.3925
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=80)

### ORDER_FLOW_5M#DOGE#5min
- **FILTRO** `total_vol_5m` > `1108292.0` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `total_vol_5m` > 1108292.0
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=61)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `hora_utc` > `3.0` → IC=+0.167 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 3.0 (IC base=+0.069)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.132 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 4.0 (IC base=+0.069)

### ORDER_FLOW_5M#XRP#5min
- **FILTRO** `delta_ratio` |x|≤ `0.4307` → IC=-0.136 (n=20)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.4307
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=45)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0105` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0105
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=36)

- **FILTRO** `sigma_h` > `0.0062` → IC=-0.365 (n=72)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0062
  - _Potencial_: sin este filtro IC_bueno=+0.204 (n=25)

- **FILTRO** `T_h` < `145.8988` → IC=-0.423 (n=50)

  - _Acción_: SKIP cuando `T_h` < 145.8988
  - _Potencial_: sin este filtro IC_bueno=-0.289 (n=17)

- **FILTRO** `pct_vs_K` |x|> `2.6724` → IC=-0.481 (n=50)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6724
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.433 (n=28)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **FILTRO** `T_h` > `111.9936` → IC=-0.455 (n=20)

  - _Acción_: SKIP cuando `T_h` > 111.9936
  - _Potencial_: sin este filtro IC_bueno=-0.400 (n=8)

- **FILTRO** `T_h` < `145.9348` → IC=-0.457 (n=21)

  - _Acción_: SKIP cuando `T_h` < 145.9348
  - _Potencial_: sin este filtro IC_bueno=-0.389 (n=7)

- **FILTRO** `pct_vs_K` |x|> `3.4276` → IC=-0.452 (n=19)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4276
  - _Potencial_: sin este filtro IC_bueno=-0.409 (n=9)

### STREAK_FADE_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=98)

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

- **FILTRO** `py_entrada` > `0.505` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=149)

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
- **PATRÓN** `ibs_15` > `0.6011` → IC=+0.173 (n=665)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.87€ cuando `ibs_15` > 0.6011 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.1672` → IC=+0.159 (n=247)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.1672 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` < `0.6153` → IC=+0.127 (n=464)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` < 0.6153 (IC base=+0.056)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.864` → IC=+0.151 (n=247)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 4.864 (IC base=+0.056)

- **PATRÓN** `libro_liquidez` > `10150.9729` → IC=+0.139 (n=192)

  - _Acción_: Kelly boost +0.70€ cuando `libro_liquidez` > 10150.9729 (IC base=+0.056)

- **PATRÓN** `dist_vwap_pct` > `0.9422` → IC=+0.171 (n=68)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.9422 (IC base=+0.054)

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

- **FILTRO** `hora_utc` < `19.0` → IC=-0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 19.0
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

- **FILTRO** `ibs_15` < `0.7377` → IC=-0.200 (n=18)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.7377
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.2291` → IC=-0.265 (n=15)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2291
  - _Potencial_: sin este filtro IC_bueno=+0.092 (n=47)

- **PATRÓN** `sigma_h` < `0.0073` → IC=+0.122 (n=329)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0073 (IC base=+0.102)

- **PATRÓN** `drift_60min` |x|≤ `0.2189` → IC=+0.139 (n=319)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.2189 (IC base=+0.102)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0631` → IC=+0.130 (n=320)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio_macro` |x|> 0.0631 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.168 (n=188)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` < 14.0 (IC base=+0.102)

- **PATRÓN** `ibs_15` > `0.6354` → IC=+0.216 (n=280)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6354 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` > `0.2571` → IC=+0.232 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2571 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` > `25.023` → IC=+0.204 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 25.023 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `11693.755` → IC=+0.164 (n=111)

  - _Acción_: Kelly boost +0.82€ cuando `libro_liquidez` > 11693.755 (IC base=+0.102)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.196 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0055 (IC base=+0.012)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_h` < `0.012` → IC=-0.143 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.012
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `ibs_15` > `0.6674` → IC=+0.188 (n=213)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.94€ cuando `ibs_15` > 0.6674 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.038` → IC=+0.152 (n=67)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 7.038 (IC base=+0.045)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.128 (n=189)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.006 (IC base=+0.063)

- **PATRÓN** `dist_vwap_pct` > `0.9222` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9222 (IC base=+0.063)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `sigma_h` > `0.0204` → IC=-0.184 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0204
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

- **FILTRO** `sigma_h` < `0.0133` → IC=-0.222 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.068 (n=35)

- **FILTRO** `drift_15min` |x|> `0.3058` → IC=-0.136 (n=31)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3058
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1932` → IC=-0.167 (n=28)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1932
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=15)

- **PATRÓN** `libro_liquidez` > `3934.6153` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 3934.6153 (IC base=+0.049)

### UPDOWN_GBM#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0549` → IC=-0.192 (n=24)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0549
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=13)

- **FILTRO** `sigma_h` > `0.0086` → IC=-0.154 (n=24)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0086
  - _Potencial_: sin este filtro IC_bueno=+0.033 (n=13)

- **FILTRO** `drift_15min` |x|> `0.4751` → IC=-0.237 (n=17)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4751
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=18)

- **FILTRO** `hora_utc` < `17.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=8)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.133 (n=175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 12.0 (IC base=+0.084)

- **PATRÓN** `ibs_15` < `0.04` → IC=+0.154 (n=79)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.77€ cuando `ibs_15` < 0.04 (IC base=+0.084)

- **PATRÓN** `libro_liquidez` > `2978.7595` → IC=+0.142 (n=93)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2978.7595 (IC base=+0.084)

### WEEKLY_PRICE
- **FILTRO** `T_h` < `144.8242` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `T_h` < 144.8242
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

- **PATRÓN** `T_h` > `111.9928` → IC=+0.374 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9928 (IC base=+0.340)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `144.6415` → IC=+0.260 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 144.6415 (IC base=+0.261)

- **PATRÓN** `T_h` > `111.9936` → IC=+0.271 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9936 (IC base=+0.261)

- **PATRÓN** `pct_dist` |x|≤ `0.836` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.836 (IC base=+0.261)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9879` → IC=+0.331 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9879 (IC base=+0.266)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` < `146.1674` → IC=+0.413 (n=113)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 146.1674 (IC base=+0.416)

- **PATRÓN** `T_h` > `111.9959` → IC=+0.430 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9959 (IC base=+0.416)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6011 sube el IC de +0.056 a +0.173 en UPDOWN_GBM#15min (n=665). Ya aplicado como kelly_boost=+0.87€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.6354 sube el IC de +0.102 a +0.216 en UPDOWN_GBM#BTC#15min (n=280). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6674 sube el IC de +0.045 a +0.188 en UPDOWN_GBM#ETH#15min (n=213). Ya aplicado como kelly_boost=+0.94€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.04 sube el IC de +0.084 a +0.154 en UPDOWN_GBM#XRP#15min (n=79). Ya aplicado como kelly_boost=+0.77€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO#XRP` — IC=+0.149 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION` — IC=+0.395 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min` — IC=+0.395 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1452 | +0.094 | +30.48€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1452 | +0.094 | +30.48€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 585 | +0.091 | +7.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 585 | +0.091 | +7.18€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 541 | +0.110 | +4.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 541 | +0.110 | +4.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 307 | +0.073 | +18.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 307 | +0.073 | +18.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 76 | +0.321 | +8.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 69 | +0.331 | +2.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#5min | 7 | +0.058 | +5.33€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 69 | +0.331 | +2.73€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 69 | +0.331 | +2.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 6999 | +0.176 | -55.43€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 4601 | +0.199 | -59.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 321 | +0.057 | -23.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 821 | +0.128 | -56.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 1256 | +0.153 | +83.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 2090 | +0.182 | -1.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1546 | +0.196 | -47.79€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 107 | +0.041 | -15.06€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 427 | +0.174 | +64.86€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 8 | +0.120 | +5.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 7 | +0.097 | +4.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 2453 | +0.166 | -48.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1508 | +0.197 | -12.83€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 106 | -0.009 | -21.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 416 | +0.127 | -31.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 423 | +0.140 | +17.26€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#SOL | 2409 | +0.181 | -12.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1507 | +0.204 | -1.92€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 106 | +0.139 | +14.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 390 | +0.135 | -27.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 406 | +0.145 | +1.63€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 35 | +0.149 | +1.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 29 | +0.113 | -2.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 61 | +0.309 | -4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 61 | +0.309 | -4.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 20 | +0.273 | -1.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 20 | +0.273 | -1.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 24 | +0.308 | -1.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 24 | +0.308 | -1.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL | 14 | +0.175 | -2.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min | 14 | +0.175 | -2.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO | 5 | +0.089 | +0.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_EXTREMO#15min | 5 | +0.089 | +0.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 36 | +0.395 | +6.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 36 | +0.395 | +6.55€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 15 | +0.243 | +2.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 15 | +0.243 | +2.50€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 16 | +0.311 | +3.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 16 | +0.311 | +3.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL | 5 | +0.089 | +0.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#SOL#60min | 5 | +0.089 | +0.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 455 | +0.301 | +4.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 455 | +0.301 | +4.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 455 | +0.301 | +4.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 455 | +0.301 | +4.66€ | 0 | 0 |
| ✅ GBM_LATE_15M | 9111 | +0.095 | +2775.87€ | 0 | 5 |
| ✅ GBM_LATE_15M#15min | 9111 | +0.095 | +2775.87€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 152 | +0.208 | +104.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 152 | +0.208 | +104.76€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 2130 | +0.068 | +350.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2130 | +0.068 | +350.09€ | 0 | 6 |
| ✅ GBM_LATE_15M#DOGE | 150 | +0.118 | +46.93€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 150 | +0.118 | +46.93€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH | 1907 | +0.069 | +300.12€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1907 | +0.069 | +300.12€ | 0 | 7 |
| ✅ GBM_LATE_15M#SOL | 2363 | +0.086 | +807.36€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2363 | +0.086 | +807.36€ | 1 | 3 |
| ✅ GBM_LATE_15M#XRP | 2409 | +0.140 | +1166.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2409 | +0.140 | +1166.61€ | 0 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 6305 | +0.121 | +3095.97€ | 0 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 6305 | +0.121 | +3095.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 113 | +0.309 | +131.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 113 | +0.309 | +131.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1571 | +0.079 | +519.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1571 | +0.079 | +519.60€ | 0 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 136 | +0.188 | +92.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 136 | +0.188 | +92.50€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1564 | +0.086 | +559.70€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1564 | +0.086 | +559.70€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1523 | +0.092 | +640.37€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1523 | +0.092 | +640.37€ | 0 | 7 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1398 | +0.216 | +1152.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1398 | +0.216 | +1152.63€ | 0 | 13 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 318 | +0.050 | +97.47€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 318 | +0.050 | +97.47€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC | 9 | -0.102 | -1.94€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 9 | -0.102 | -1.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 137 | -0.083 | -1.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 137 | -0.083 | -1.93€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL | 8 | -0.120 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 8 | -0.120 | -1.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 164 | +0.199 | +103.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 164 | +0.199 | +103.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 6295 | +0.068 | +1777.55€ | 0 | 3 |
| ✅ GBM_LATE_15M_TARDIO#15min | 6295 | +0.068 | +1777.55€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 128 | +0.246 | +106.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 128 | +0.246 | +106.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1437 | +0.021 | +169.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1437 | +0.021 | +169.21€ | 0 | 2 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 137 | +0.169 | +68.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 137 | +0.169 | +68.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1469 | +0.018 | +121.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1469 | +0.018 | +121.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1425 | +0.027 | +278.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1425 | +0.027 | +278.51€ | 1 | 1 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1699 | +0.163 | +1034.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1699 | +0.163 | +1034.44€ | 0 | 13 |
| ✅ GBM_LATE_5M | 986 | -0.028 | +2.53€ | 0 | 0 |
| ✅ GBM_LATE_5M#5min | 986 | -0.028 | +2.53€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 226 | -0.013 | -1.51€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 226 | -0.013 | -1.51€ | 0 | 0 |
| 🚫 GBM_LATE_5M#ETH | 82 | -0.202 | -15.93€ | 0 | 0 |
| 🚫 GBM_LATE_5M#ETH#5min | 82 | -0.202 | -15.93€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL | 309 | -0.059 | +7.87€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 309 | -0.059 | +7.87€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 369 | +0.028 | +12.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 369 | +0.028 | +12.11€ | 0 | 0 |
| ✅ GBM_LATE_60M | 343 | -0.109 | +4.07€ | 3 | 1 |
| ✅ GBM_LATE_60M#60min | 343 | -0.109 | +4.07€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 123 | -0.044 | +0.69€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 123 | -0.044 | +0.69€ | 5 | 1 |
| ✅ GBM_LATE_60M#ETH | 110 | -0.134 | -7.88€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 110 | -0.134 | -7.88€ | 5 | 0 |
| ✅ GBM_LATE_60M#SOL | 110 | -0.152 | +11.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 110 | -0.152 | +11.27€ | 5 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO | 9 | -0.143 | -2.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO#60min | 9 | -0.143 | -2.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 383 | -0.064 | -7.23€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 383 | -0.064 | -7.23€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 383 | -0.064 | -7.23€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 383 | -0.064 | -7.23€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 309 | +0.008 | +9.11€ | 1 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 309 | +0.008 | +9.11€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 309 | +0.008 | +9.11€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 309 | +0.008 | +9.11€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1688 | +0.011 | +11.00€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1552 | +0.007 | -1.60€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 217 | +0.034 | +4.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 217 | +0.034 | +4.59€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 227 | +0.002 | -1.73€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 227 | +0.002 | -1.73€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 269 | -0.017 | -8.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 269 | -0.017 | -8.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 334 | +0.045 | +14.88€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 334 | +0.045 | +14.88€ | 0 | 2 |
| ✅ ORDER_FLOW_5M#XRP | 214 | -0.009 | -6.01€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 214 | -0.009 | -6.01€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM | 150 | -0.171 | -4.78€ | 4 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC | 62 | -0.250 | -18.09€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 56 | -0.276 | -17.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 6 | +0.000 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 58 | -0.183 | -0.24€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#ETH#atexpiry | 52 | -0.204 | -3.53€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 6 | +0.000 | +3.29€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 30 | +0.031 | +13.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 28 | +0.033 | +13.27€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 136 | -0.188 | -7.61€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 14 | +0.000 | +2.83€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 17 | +0.291 | +3.97€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC | 5 | +0.089 | +1.01€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#BTC#sniper | 5 | +0.089 | +1.01€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 7 | +0.136 | +1.55€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 7 | +0.136 | +1.55€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 17 | +0.291 | +3.97€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 304 | +0.062 | +20.40€ | 1 | 1 |
| ✅ STREAK_FADE_15M#15min | 304 | +0.062 | +20.40€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 63 | +0.038 | -2.53€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 63 | +0.038 | -2.53€ | 1 | 0 |
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
| 🚫 STREAK_MOM_5M | 320 | -0.059 | -26.41€ | 5 | 0 |
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
| ✅ UPDOWN_GBM | 3103 | +0.039 | +299.51€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2839 | +0.055 | +338.53€ | 0 | 6 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 131 | -0.064 | -11.72€ | 6 | 0 |
| ✅ UPDOWN_GBM#BNB | 338 | +0.053 | +61.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 338 | +0.053 | +61.74€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 604 | +0.056 | +78.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 520 | +0.088 | +93.33€ | 1 | 9 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 43 | -0.078 | -6.67€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 276 | +0.014 | +7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 273 | +0.016 | +8.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1152 | +0.042 | +84.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1058 | +0.055 | +95.96€ | 0 | 4 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 55 | -0.026 | -3.07€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 356 | -0.011 | +13.93€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 286 | +0.017 | +20.88€ | 4 | 1 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 33 | -0.100 | -1.97€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 375 | +0.057 | +55.25€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 364 | +0.066 | +58.54€ | 4 | 3 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 205 | +0.307 | +45.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 205 | +0.307 | +45.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 99 | +0.312 | +23.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 99 | +0.312 | +23.98€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 106 | +0.296 | +21.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 106 | +0.296 | +21.03€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 2397 | +0.151 | +1060.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 2397 | +0.151 | +1060.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 238 | +0.217 | +165.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 238 | +0.217 | +165.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 247 | +0.110 | +42.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 247 | +0.110 | +42.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 219 | +0.201 | +143.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 219 | +0.201 | +143.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 455 | +0.165 | +171.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 455 | +0.165 | +171.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 563 | +0.084 | +133.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 563 | +0.084 | +133.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 675 | +0.172 | +403.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 675 | +0.172 | +403.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 25 | -0.018 | -1.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 25 | -0.018 | -1.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 25 | -0.018 | -1.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 25 | -0.018 | -1.25€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO | 8 | +0.120 | +2.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_IBS_ALTO#15min | 8 | +0.120 | +2.18€ | 0 | 0 |
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
| ✅ WEEKLY_PRICE | 457 | +0.234 | +132.04€ | 1 | 1 |
| ✅ WEEKLY_PRICE#BTC | 128 | +0.154 | -11.62€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 130 | +0.174 | -3.87€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 199 | +0.321 | +147.53€ | 0 | 2 |