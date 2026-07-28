# Hipótesis automáticas — 2026-07-28 15:35 UTC
_Generado por shadow_postmortem.py sobre 40316 resoluciones (PNL=+8330.83€)_

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
- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.194 (n=1259)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0076 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.165 (n=1770)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 7.0 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.6733` → IC=+0.197 (n=232)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.6733 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.392` → IC=+0.235 (n=609)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.392 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.155 (n=1443)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0068 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.132 (n=1474)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 12.0 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.3902` → IC=+0.129 (n=340)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.3902 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.186` → IC=+0.152 (n=320)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 8.186 (IC base=+0.120)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.141 (n=430)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 7.0 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` > `0.4428` → IC=+0.205 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4428 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.697` → IC=+0.163 (n=84)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` > 11.697 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.708` → IC=+0.167 (n=85)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 11.708 (IC base=+0.092)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.211 (n=157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.144 (n=338)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 11.0 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.659` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.659 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.083` → IC=+0.197 (n=87)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 10.083 (IC base=+0.120)

- **PATRÓN** `libro_liquidez` > `8305.53` → IC=+0.132 (n=245)

  - _Acción_: Kelly boost +0.66€ cuando `libro_liquidez` > 8305.53 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.42` → IC=+0.186 (n=103)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 9.42 (IC base=+0.088)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.144 (n=470)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0078 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.150 (n=315)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 12.0 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.2996` → IC=+0.162 (n=128)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.2996 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.566` → IC=+0.270 (n=202)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.566 (IC base=+0.115)

- **PATRÓN** `libro_liquidez` > `1892.0225` → IC=+0.159 (n=344)

  - _Acción_: Kelly boost +0.79€ cuando `libro_liquidez` > 1892.0225 (IC base=+0.115)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` < `0.0173` → IC=+0.246 (n=435)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0173 (IC base=+0.228)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.247 (n=397)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.228)

- **PATRÓN** `dist_vwap_pct` > `0.4523` → IC=+0.293 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4523 (IC base=+0.228)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.537` → IC=+0.348 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.537 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.223 (n=470)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.228)

- **PATRÓN** `sigma_h` < `0.0172` → IC=+0.208 (n=553)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0172 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.232 (n=553)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0071 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.242 (n=374)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.1912` → IC=+0.317 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1912 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.487` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.487 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.144` → IC=+0.195 (n=608)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` < 9.144 (IC base=+0.204)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.218 (n=456)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.204)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.126 (n=1245)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` > 0.0083 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.4559` → IC=+0.153 (n=335)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.4559 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.003` → IC=+0.235 (n=304)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.003 (IC base=+0.097)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.121 (n=270)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.004 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.4413` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.4413 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.632` → IC=+0.176 (n=69)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 12.632 (IC base=+0.075)

- **PATRÓN** `libro_liquidez` > `10365.2965` → IC=+0.126 (n=204)

  - _Acción_: Kelly boost +0.63€ cuando `libro_liquidez` > 10365.2965 (IC base=+0.075)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `12.232` → IC=+0.167 (n=64)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 12.232 (IC base=+0.057)

- **PATRÓN** `libro_liquidez` > `6814.1335` → IC=+0.127 (n=226)

  - _Acción_: Kelly boost +0.64€ cuando `libro_liquidez` > 6814.1335 (IC base=+0.057)

### GBM_LATE_15M_TARDIO#SOL#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `9.062` → IC=+0.287 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.062 (IC base=+0.051)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.019` → IC=+0.176 (n=483)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.019 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0103` → IC=+0.169 (n=490)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0103 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.174 (n=556)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 6.0 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.2416` → IC=+0.230 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2416 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.883` → IC=+0.288 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.883 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.168 (n=416)

  - _Acción_: Kelly boost +0.84€ cuando `libro_spread` < 0.01 (IC base=+0.169)

- **PATRÓN** `sigma_h` < `0.0221` → IC=+0.154 (n=668)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0221 (IC base=+0.154)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.167 (n=668)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0077 (IC base=+0.154)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.177 (n=453)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 12.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.158 (n=235)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 6.0 (IC base=+0.154)

- **PATRÓN** `dist_vwap_pct` > `0.1404` → IC=+0.219 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1404 (IC base=+0.154)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.452` → IC=+0.151 (n=689)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 9.452 (IC base=+0.154)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.162 (n=533)

  - _Acción_: Kelly boost +0.81€ cuando `libro_spread` < 0.01 (IC base=+0.154)

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
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=158)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=158)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=156)

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
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.068)

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
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` < 9.0 (IC base=+0.084)

- **PATRÓN** `volumen_racha` < `497480.0` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 497480.0 (IC base=+0.084)

- **PATRÓN** `libro_liquidez` > `2780.3379` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `libro_liquidez` > 2780.3379 (IC base=+0.084)

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
- **PATRÓN** `ibs_15` > `0.6045` → IC=+0.173 (n=647)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.87€ cuando `ibs_15` > 0.6045 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.1663` → IC=+0.165 (n=237)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.1663 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.106` → IC=+0.152 (n=234)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 5.106 (IC base=+0.055)

- **PATRÓN** `libro_liquidez` > `10314.0826` → IC=+0.141 (n=182)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 10314.0826 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.9648` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.9648 (IC base=+0.046)

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

- **PATRÓN** `sigma_h` < `0.0072` → IC=+0.124 (n=325)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0072 (IC base=+0.101)

- **PATRÓN** `drift_60min` |x|≤ `0.2197` → IC=+0.140 (n=315)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.2197 (IC base=+0.101)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0631` → IC=+0.128 (n=315)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio_macro` |x|> 0.0631 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `14.0` → IC=+0.165 (n=186)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 14.0 (IC base=+0.101)

- **PATRÓN** `ibs_15` > `0.6374` → IC=+0.216 (n=276)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6374 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.2554` → IC=+0.242 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2554 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.506` → IC=+0.183 (n=39)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 24.506 (IC base=+0.101)

- **PATRÓN** `libro_liquidez` > `11693.755` → IC=+0.173 (n=108)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 11693.755 (IC base=+0.101)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.196 (n=21)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0055 (IC base=+0.012)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_h` < `0.012` → IC=-0.143 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.012
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `ibs_15` > `0.6676` → IC=+0.191 (n=208)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.95€ cuando `ibs_15` > 0.6676 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.069` → IC=+0.156 (n=62)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` > 7.069 (IC base=+0.044)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.138 (n=139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0055 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.9222` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.9222 (IC base=+0.055)

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

### WEEKLY_PRICE
- **FILTRO** `T_h` < `144.8242` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `T_h` < 144.8242
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

- **PATRÓN** `T_h` > `146.1332` → IC=+0.440 (n=81)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1332 (IC base=+0.336)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `111.9824` → IC=+0.281 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9824 (IC base=+0.262)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9905` → IC=+0.331 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9905 (IC base=+0.267)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` > `111.9928` → IC=+0.424 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9928 (IC base=+0.407)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6045 sube el IC de +0.055 a +0.173 en UPDOWN_GBM#15min (n=647). Ya aplicado como kelly_boost=+0.87€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.6374 sube el IC de +0.101 a +0.216 en UPDOWN_GBM#BTC#15min (n=276). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6676 sube el IC de +0.044 a +0.191 en UPDOWN_GBM#ETH#15min (n=208). Ya aplicado como kelly_boost=+0.95€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO#XRP` — IC=+0.149 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1423 | +0.098 | +33.44€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1423 | +0.098 | +33.44€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 568 | +0.093 | +3.80€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 568 | +0.093 | +3.80€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 529 | +0.118 | +11.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 529 | +0.118 | +11.31€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 307 | +0.073 | +18.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 307 | +0.073 | +18.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 47 | +0.357 | +3.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 47 | +0.357 | +3.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 47 | +0.357 | +3.24€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 47 | +0.357 | +3.24€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 6913 | +0.176 | -61.67€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 4549 | +0.200 | -52.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 314 | +0.054 | -25.33€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 821 | +0.128 | -56.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 1229 | +0.152 | +73.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 2046 | +0.182 | -11.05€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1520 | +0.197 | -52.21€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 104 | +0.038 | -15.67€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 412 | +0.174 | +60.60€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 8 | +0.120 | +5.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 7 | +0.097 | +4.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 2423 | +0.166 | -49.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1491 | +0.199 | -4.81€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 104 | -0.019 | -23.88€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 416 | +0.127 | -31.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 412 | +0.135 | +10.14€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#SOL | 2397 | +0.181 | -8.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1498 | +0.205 | +0.78€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 104 | +0.141 | +15.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 390 | +0.135 | -27.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 405 | +0.146 | +2.74€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 35 | +0.149 | +1.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 29 | +0.113 | -2.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION | 16 | +0.311 | +0.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#15min | 16 | +0.311 | +0.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC | 6 | +0.075 | -0.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min | 6 | +0.075 | -0.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH | 6 | +0.113 | +0.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min | 6 | +0.113 | +0.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION | 13 | +0.195 | +0.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#60min | 13 | +0.195 | +0.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC | 6 | +0.037 | -0.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#BTC#60min | 6 | +0.037 | -0.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH | 5 | +0.089 | +0.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_60MIN_ALTACONVICCION#ETH#60min | 5 | +0.089 | +0.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 445 | +0.303 | +7.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 445 | +0.303 | +7.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 445 | +0.303 | +7.76€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 445 | +0.303 | +7.76€ | 0 | 0 |
| ✅ GBM_LATE_15M | 8680 | +0.093 | +2582.09€ | 0 | 5 |
| ✅ GBM_LATE_15M#15min | 8680 | +0.093 | +2582.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB | 64 | +0.167 | +26.52€ | 0 | 0 |
| ✅ GBM_LATE_15M#BNB#15min | 64 | +0.167 | +26.52€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 2069 | +0.071 | +349.59€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2069 | +0.071 | +349.59€ | 0 | 6 |
| ✅ GBM_LATE_15M#DOGE | 64 | +0.076 | +7.70€ | 0 | 0 |
| ✅ GBM_LATE_15M#DOGE#15min | 64 | +0.076 | +7.70€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH | 1858 | +0.073 | +310.17€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1858 | +0.073 | +310.17€ | 0 | 7 |
| ✅ GBM_LATE_15M#SOL | 2305 | +0.083 | +784.43€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2305 | +0.083 | +784.43€ | 1 | 3 |
| ✅ GBM_LATE_15M#XRP | 2320 | +0.138 | +1103.68€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2320 | +0.138 | +1103.68€ | 0 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 5905 | +0.117 | +2780.65€ | 0 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 5905 | +0.117 | +2780.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB | 47 | +0.316 | +53.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BNB#15min | 47 | +0.316 | +53.49€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1516 | +0.084 | +508.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1516 | +0.084 | +508.20€ | 0 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE | 61 | +0.182 | +36.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#DOGE#15min | 61 | +0.182 | +36.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1508 | +0.088 | +538.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1508 | +0.088 | +538.24€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1455 | +0.085 | +569.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1455 | +0.085 | +569.05€ | 0 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1318 | +0.214 | +1075.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1318 | +0.214 | +1075.08€ | 0 | 12 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 292 | +0.065 | +100.68€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 292 | +0.065 | +100.68€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC | 9 | -0.102 | -1.94€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 9 | -0.102 | -1.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 128 | -0.061 | +2.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 128 | -0.061 | +2.31€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL | 8 | -0.120 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 8 | -0.120 | -1.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 147 | +0.218 | +102.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 147 | +0.218 | +102.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 5902 | +0.065 | +1552.36€ | 0 | 3 |
| ✅ GBM_LATE_15M_TARDIO#15min | 5902 | +0.065 | +1552.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB | 56 | +0.276 | +43.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BNB#15min | 56 | +0.276 | +43.54€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1382 | +0.026 | +153.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1382 | +0.026 | +153.81€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO#DOGE | 59 | +0.156 | +17.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#DOGE#15min | 59 | +0.156 | +17.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1409 | +0.022 | +118.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1409 | +0.022 | +118.72€ | 0 | 2 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1372 | +0.024 | +251.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1372 | +0.024 | +251.94€ | 0 | 1 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1624 | +0.160 | +966.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1624 | +0.160 | +966.79€ | 0 | 13 |
| ✅ GBM_LATE_5M | 883 | -0.038 | -8.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#5min | 883 | -0.038 | -8.49€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 181 | -0.046 | -13.20€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 181 | -0.046 | -13.20€ | 0 | 0 |
| 🚫 GBM_LATE_5M#ETH | 82 | -0.202 | -15.93€ | 0 | 0 |
| 🚫 GBM_LATE_5M#ETH#5min | 82 | -0.202 | -15.93€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL | 300 | -0.056 | +9.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 300 | -0.056 | +9.35€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 320 | +0.028 | +11.29€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 320 | +0.028 | +11.29€ | 0 | 0 |
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
| ✅ LATE_WINDOW_5MIN | 373 | -0.060 | -5.93€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 373 | -0.060 | -5.93€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 373 | -0.060 | -5.93€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 373 | -0.060 | -5.93€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 305 | +0.002 | +6.94€ | 1 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 305 | +0.002 | +6.94€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 305 | +0.002 | +6.94€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 305 | +0.002 | +6.94€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1687 | +0.011 | +10.51€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1551 | +0.007 | -2.09€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 217 | +0.034 | +4.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 217 | +0.034 | +4.59€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 226 | +0.000 | -2.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 226 | +0.000 | -2.22€ | 1 | 0 |
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
| ✅ RESOLUTION_SNIPER | 13 | +0.195 | +3.10€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 6 | +0.113 | +1.44€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 6 | +0.113 | +1.44€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 13 | +0.195 | +3.10€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 302 | +0.066 | +23.06€ | 1 | 1 |
| ✅ STREAK_FADE_15M#15min | 302 | +0.066 | +23.06€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 63 | +0.038 | -2.53€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 63 | +0.038 | -2.53€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 88 | +0.122 | +20.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 88 | +0.122 | +20.43€ | 0 | 2 |
| ✅ STREAK_FADE_15M#XRP | 150 | +0.046 | +5.89€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 150 | +0.046 | +5.89€ | 0 | 3 |
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
| ✅ UPDOWN_GBM | 2988 | +0.033 | +262.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2724 | +0.050 | +301.03€ | 0 | 5 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 131 | -0.064 | -11.72€ | 6 | 0 |
| ✅ UPDOWN_GBM#BNB | 320 | +0.047 | +57.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 320 | +0.047 | +57.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 598 | +0.055 | +77.14€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 514 | +0.087 | +91.62€ | 1 | 9 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 43 | -0.078 | -6.67€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 267 | +0.017 | +7.37€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 264 | +0.019 | +8.27€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1125 | +0.037 | +73.88€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1031 | +0.050 | +85.45€ | 0 | 4 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 55 | -0.026 | -3.07€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 328 | -0.027 | +4.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 258 | +0.000 | +11.03€ | 4 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 33 | -0.100 | -1.97€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 348 | +0.046 | +43.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 337 | +0.055 | +47.06€ | 4 | 0 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 200 | +0.307 | +42.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 200 | +0.307 | +42.83€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 95 | +0.314 | +22.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 95 | +0.314 | +22.38€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 105 | +0.294 | +20.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 105 | +0.294 | +20.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 2275 | +0.148 | +980.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 2275 | +0.148 | +980.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 220 | +0.212 | +146.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 220 | +0.212 | +146.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 235 | +0.112 | +41.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 235 | +0.112 | +41.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 209 | +0.201 | +136.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 209 | +0.201 | +136.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 432 | +0.159 | +153.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 432 | +0.159 | +153.42€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 537 | +0.084 | +130.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 537 | +0.084 | +130.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 642 | +0.166 | +372.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 642 | +0.166 | +372.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 24 | +0.000 | -0.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 24 | +0.000 | -0.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 24 | +0.000 | -0.74€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 24 | +0.000 | -0.74€ | 0 | 0 |
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
| ✅ WEEKLY_PRICE | 425 | +0.224 | +109.63€ | 1 | 1 |
| ✅ WEEKLY_PRICE#BTC | 120 | +0.147 | -10.94€ | 0 | 1 |
| ✅ WEEKLY_PRICE#ETH | 122 | +0.169 | -2.75€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 183 | +0.305 | +123.32€ | 0 | 1 |