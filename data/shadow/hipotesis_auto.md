# Hipótesis automáticas — 2026-07-18 21:21 UTC
_Generado por shadow_postmortem.py sobre 21305 resoluciones (PNL=+5112.96€)_

## Patrones causales activos

### FAVORITO_CONFIRMADO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.192 (n=1191)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.205 (n=1326)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.695` → IC=+0.298 (n=583)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.695 (IC base=+0.191)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.195 (n=1487)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.191)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.192 (n=521)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 17.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=506)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.345 (n=475)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.181 (n=1568)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.175)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` < `18.0` → IC=+0.223 (n=294)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` > `0.615` → IC=+0.269 (n=258)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.615 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `11561.1332` → IC=+0.219 (n=94)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11561.1332 (IC base=+0.212)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.209 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.243 (n=204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.381 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.203)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.185 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 6.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.253 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 19.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` < `0.565` → IC=+0.269 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.565 (IC base=+0.188)

- **PATRÓN** `libro_liquidez` > `8840.0271` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8840.0271 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.177 (n=29)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.154)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.300 (n=33)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.154)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.405 (IC base=+0.154)

- **PATRÓN** `libro_liquidez` > `6436.3724` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 6436.3724 (IC base=+0.154)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.235 (n=262)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.238 (n=292)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.350 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.223)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.225 (n=358)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.223)

- **PATRÓN** `libro_liquidez` > `4437.9283` → IC=+0.230 (n=187)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4437.9283 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.231 (n=206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.214)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.381 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `6777.6499` → IC=+0.220 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6777.6499 (IC base=+0.214)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` < `19.0` → IC=+0.192 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 19.0 (IC base=+0.156)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.575 (IC base=+0.156)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=77)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.156)

- **PATRÓN** `libro_liquidez` > `6015.6895` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6015.6895 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.219 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.145)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.197 (n=64)

  - _Acción_: Kelly boost +0.98€ cuando `py_entrada` < 0.405 (IC base=+0.145)

- **PATRÓN** `libro_liquidez` > `4043.1829` → IC=+0.175 (n=81)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 4043.1829 (IC base=+0.145)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.248 (n=101)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.231)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.248 (n=101)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.231)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.296 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.231)

- **PATRÓN** `libro_liquidez` > `1984.229` → IC=+0.236 (n=127)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1984.229 (IC base=+0.231)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.225 (n=147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.254 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.215)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.257 (n=311)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.405 (IC base=+0.215)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.231 (n=24)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.64` → IC=+0.202 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.64 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.575` → IC=+0.180 (n=73)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.575 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.185 (n=71)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.02 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.125 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.087)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.087)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.128 (n=1784)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 8.0 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `0.7393` → IC=+0.142 (n=135)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.7393 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.024` → IC=+0.218 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.024 (IC base=+0.114)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.130 (n=1420)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.0089 (IC base=+0.112)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.133 (n=1533)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 12.0 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `0.1646` → IC=+0.129 (n=335)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.1646 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` < `0.9126` → IC=+0.122 (n=1047)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.9126 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.188` → IC=+0.144 (n=223)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 6.188 (IC base=+0.112)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.5248` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5248 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.466` → IC=+0.223 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.466 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.1355` → IC=+0.139 (n=59)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.1355 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` < `0.5143` → IC=+0.128 (n=216)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.5143 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.845` → IC=+0.191 (n=95)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 2.845 (IC base=+0.072)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.167 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0045 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.8385` → IC=+0.132 (n=17)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.8385 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.301` → IC=+0.204 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.301 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.6698` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.6698 (IC base=+0.076)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.518` → IC=+0.236 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.518 (IC base=+0.076)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `8.125` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.125
  - _Potencial_: sin este filtro IC_bueno=+0.102 (n=239)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.124 (n=251)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0101 (IC base=+0.104)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.150 (n=195)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 18.0 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.326` → IC=+0.199 (n=81)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 5.326 (IC base=+0.104)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.142 (n=465)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.013 (IC base=+0.125)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.126 (n=528)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` > 0.0091 (IC base=+0.125)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.170 (n=386)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 12.0 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.63` → IC=+0.124 (n=192)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 2.63 (IC base=+0.125)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_h` < `0.0287` → IC=+0.154 (n=539)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0287 (IC base=+0.153)

- **PATRÓN** `sigma_h` > `0.0219` → IC=+0.184 (n=245)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0219 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.162 (n=483)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 8.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.155 (n=482)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 15.0 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.5822` → IC=+0.256 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5822 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.1179` → IC=+0.145 (n=198)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1179 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.574` → IC=+0.288 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.574 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.193 (n=187)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` < 0.0101 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.026` → IC=+0.204 (n=187)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.026 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.226 (n=206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.3099` → IC=+0.191 (n=79)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.3099 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` < `0.6019` → IC=+0.165 (n=302)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` < 0.6019 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.696` → IC=+0.169 (n=270)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 7.696 (IC base=+0.170)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.236 (n=343)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.165)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.186 (n=686)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 13.0 (IC base=+0.165)

- **PATRÓN** `dist_vwap_pct` > `0.1744` → IC=+0.208 (n=371)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1744 (IC base=+0.165)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.023` → IC=+0.296 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.023 (IC base=+0.165)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.187 (n=1005)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0046 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.182 (n=382)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 6.0 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.8826` → IC=+0.186 (n=914)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.8826 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.027` → IC=+0.230 (n=124)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.027 (IC base=+0.168)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.137 (n=166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0041 (IC base=+0.130)

- **PATRÓN** `sigma_h` > `0.003` → IC=+0.149 (n=220)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.003 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.180 (n=167)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 13.0 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.6064` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6064 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.142` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.142 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.134 (n=255)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0061 (IC base=+0.133)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.162 (n=255)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` > 0.0027 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=126)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.1165` → IC=+0.135 (n=61)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.1165 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.466` → IC=+0.133 (n=224)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.466 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.151` → IC=+0.234 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.151 (IC base=+0.133)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.256 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.172 (n=187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 12.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.157 (n=278)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 18.0 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.5316` → IC=+0.194 (n=60)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.5316 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` < `0.8807` → IC=+0.146 (n=210)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.8807 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.551` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.551 (IC base=+0.148)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.138 (n=230)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.0067 (IC base=+0.126)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.139 (n=261)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0036 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.156 (n=88)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.6262` → IC=+0.191 (n=53)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6262 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.618` → IC=+0.250 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.618 (IC base=+0.126)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `2.556` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.556
  - _Potencial_: sin este filtro IC_bueno=+0.179 (n=160)

- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.201 (n=95)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0136 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.157 (n=205)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 12.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.143 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.132)

- **PATRÓN** `dist_vwap_pct` > `0.6196` → IC=+0.173 (n=53)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.6196 (IC base=+0.132)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.566` → IC=+0.275 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.566 (IC base=+0.132)

- **PATRÓN** `sigma_h` < `0.0122` → IC=+0.148 (n=245)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0122 (IC base=+0.116)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.171 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 5.0 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` < `0.1827` → IC=+0.180 (n=170)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.1827 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.556` → IC=+0.179 (n=160)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 2.556 (IC base=+0.116)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` < `0.0172` → IC=+0.264 (n=235)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0172 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.268 (n=235)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0091 (IC base=+0.256)

- **PATRÓN** `hora_utc` > `9.0` → IC=+0.259 (n=210)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 9.0 (IC base=+0.256)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.266 (n=242)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.256)

- **PATRÓN** `dist_vwap_pct` > `0.288` → IC=+0.318 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.288 (IC base=+0.256)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.801` → IC=+0.391 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.801 (IC base=+0.256)

- **PATRÓN** `sigma_h` > `0.0079` → IC=+0.321 (n=244)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0079 (IC base=+0.298)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.307 (n=257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.298)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.303 (n=221)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` > `0.1814` → IC=+0.315 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1814 (IC base=+0.298)

- **PATRÓN** `dist_vwap_pct` < `0.5721` → IC=+0.311 (n=241)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5721 (IC base=+0.298)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.494` → IC=+0.318 (n=212)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.494 (IC base=+0.298)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0139` → IC=+0.203 (n=314)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0139 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.137 (n=868)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` > 8.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.133 (n=876)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 16.0 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.5354` → IC=+0.187 (n=177)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.5354 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.366` → IC=+0.289 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.366 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.127 (n=387)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 6.0 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` < `0.7882` → IC=+0.127 (n=910)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.7882 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.478` → IC=+0.128 (n=237)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 3.478 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.972` → IC=+0.121 (n=803)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` < 10.972 (IC base=+0.104)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.151 (n=144)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0045 (IC base=+0.115)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.122 (n=215)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` > 0.0029 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.158 (n=197)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 8.0 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.5248` → IC=+0.230 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5248 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.025` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.025 (IC base=+0.115)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.129 (n=87)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 17.0 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.888` → IC=+0.153 (n=96)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 2.888 (IC base=+0.078)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.163 (n=81)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0039 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` < `0.2777` → IC=+0.138 (n=125)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2777 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.68` → IC=+0.250 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.68 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.997` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 7.997 (IC base=+0.042)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.7922` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.7922
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=223)

- **FILTRO** `sigma_ewma_delta_pct` > `4.907` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.907
  - _Potencial_: sin este filtro IC_bueno=+0.069 (n=195)

- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.122 (n=88)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` > 0.0124 (IC base=+0.086)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.148 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 8.0 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.3465` → IC=+0.143 (n=40)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.3465 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.1438` → IC=+0.136 (n=86)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.1438 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.184` → IC=+0.263 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.184 (IC base=+0.086)

- **PATRÓN** `sigma_h` < `0.009` → IC=+0.121 (n=114)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.009 (IC base=+0.043)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.121 (n=93)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 6.0 (IC base=+0.043)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0287` → IC=+0.211 (n=296)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0287 (IC base=+0.210)

- **PATRÓN** `sigma_h` > `0.0112` → IC=+0.237 (n=264)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0112 (IC base=+0.210)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.209 (n=276)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.210)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.234 (n=107)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.210)

- **PATRÓN** `dist_vwap_pct` > `0.2413` → IC=+0.269 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2413 (IC base=+0.210)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.976` → IC=+0.279 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.976 (IC base=+0.210)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.229 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0098 (IC base=+0.217)

- **PATRÓN** `sigma_h` > `0.0173` → IC=+0.236 (n=146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0173 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.216 (n=294)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.237 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` > `0.2916` → IC=+0.214 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2916 (IC base=+0.217)

- **PATRÓN** `dist_vwap_pct` < `0.5543` → IC=+0.217 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5543 (IC base=+0.217)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.122` → IC=+0.225 (n=271)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.122 (IC base=+0.217)

### GBM_LATE_60M
- **FILTRO** `dist_vwap_pct` < `0.1109` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.1109
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=12)

- **FILTRO** `sigma_ewma_delta_pct` < `16.76` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 16.76
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=3)

- **FILTRO** `sigma_h` > `0.0133` → IC=-0.300 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=118)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.272 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=44)

- **PATRÓN** `sigma_h` < `0.0047` → IC=+0.152 (n=44)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` < 0.0047 (IC base=-0.017)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `sigma_h` > `0.0086` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0086
  - _Potencial_: sin este filtro IC_bueno=+0.111 (n=52)

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

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.176 (n=35)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0053 (IC base=+0.043)

### GBM_LATE_60M#ETH#60min
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

- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.237 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0135 (IC base=-0.080)

### LEADLAG_BTC_XRP_15M
- **FILTRO** `py_entrada` > `0.505` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=65)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.130 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.083)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.142 (n=65)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.505 (IC base=+0.083)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.142 (n=65)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.130 (n=44)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 11.0 (IC base=+0.083)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.142 (n=65)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.505 (IC base=+0.083)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.078 (n=100)

### ORDER_FLOW_5M#BNB#5min
- **PATRÓN** `total_vol_5m` < `197.886` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `total_vol_5m` < 197.886 (IC base=+0.031)

### ORDER_FLOW_5M#BTC#5min
- **FILTRO** `delta_ratio` |x|≤ `0.3925` → IC=-0.180 (n=23)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.3925
  - _Potencial_: sin este filtro IC_bueno=-0.012 (n=80)

- **FILTRO** `hora_utc` > `4.0` → IC=-0.262 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=24)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.192 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 4.0 (IC base=+0.000)

### ORDER_FLOW_5M#DOGE#5min
- **FILTRO** `delta_ratio` |x|≤ `0.4217` → IC=-0.140 (n=23)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.4217
  - _Potencial_: sin este filtro IC_bueno=+0.014 (n=70)

- **FILTRO** `total_vol_5m` > `1108292.0` → IC=-0.258 (n=31)

  - _Acción_: SKIP cuando `total_vol_5m` > 1108292.0
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=61)

### ORDER_FLOW_5M#SOL#5min
- **PATRÓN** `hora_utc` < `4.0` → IC=+0.121 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 4.0 (IC base=+0.065)

### ORDER_FLOW_5M#XRP#5min
- **FILTRO** `delta_ratio` |x|≤ `0.4307` → IC=-0.136 (n=20)
  - _Por qué funciona_: delta_ratio bajo → order flow débil; señal insuficiente para batir el spread
  - _Acción_: SKIP cuando `delta_ratio` |x|≤ 0.4307
  - _Potencial_: sin este filtro IC_bueno=+0.032 (n=45)

### PRICE_TARGET_GBM
- **FILTRO** `sigma_h` < `0.0105` → IC=-0.237 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0105
  - _Potencial_: sin este filtro IC_bueno=+0.013 (n=35)

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

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.204 (n=25)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0062 (IC base=-0.217)

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
- **FILTRO** `volumen_racha` > `305408.9` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `volumen_racha` > 305408.9
  - _Potencial_: sin este filtro IC_bueno=+0.211 (n=50)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.174 (n=44)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 13.0 (IC base=+0.111)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.505 (IC base=+0.111)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.171 (n=68)

  - _Acción_: Kelly boost +0.86€ cuando `streak_len` < 4.0 (IC base=+0.111)

- **PATRÓN** `regimen_ma_toques` > `5.0` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 5.0 (IC base=+0.111)

- **PATRÓN** `volumen_racha` < `305408.9` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 305408.9 (IC base=+0.111)

- **PATRÓN** `libro_liquidez` > `1998.2494` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 1998.2494 (IC base=+0.111)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.269 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.079)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.136 (n=53)

  - _Acción_: Kelly boost +0.68€ cuando `py_entrada` < 0.485 (IC base=+0.079)

- **PATRÓN** `volumen_racha` < `509738.3` → IC=+0.192 (n=50)

  - _Acción_: Kelly boost +0.96€ cuando `volumen_racha` < 509738.3 (IC base=+0.079)

### STREAK_FADE_15M#SOL#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.214 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.515` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `py_entrada` < 0.515 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.206 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.151)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` < 0.485 (IC base=+0.151)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `hora_utc` > `11.0` → IC=-0.125 (n=22)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 11.0
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=24)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.192 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 11.0 (IC base=+0.042)

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
- **FILTRO** `py_entrada` < `0.515` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` < 0.515
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `libro_liquidez` < `7137.8206` → IC=-0.150 (n=18)

  - _Acción_: SKIP cuando `libro_liquidez` < 7137.8206
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

- **FILTRO** `hora_utc` < `18.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 18.0
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=6)

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

### STREAK_FADE_5M#SOL#5min
- **FILTRO** `hora_utc` < `17.0` → IC=-0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 17.0
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=6)

- **FILTRO** `libro_liquidez` < `3416.5722` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `libro_liquidez` < 3416.5722
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **PATRÓN** `libro_liquidez` > `3531.2061` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3531.2061 (IC base=-0.007)

### STREAK_FADE_5M#XRP#5min
- **FILTRO** `hora_utc` < `8.0` → IC=-0.150 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 8.0
  - _Potencial_: sin este filtro IC_bueno=+0.024 (n=61)

### STREAK_MOM_5M
- **FILTRO** `hora_utc` > `17.0` → IC=-0.132 (n=36)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 17.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=108)

- **FILTRO** `py_entrada` < `0.5` → IC=-0.250 (n=46)

  - _Acción_: SKIP cuando `py_entrada` < 0.5
  - _Potencial_: sin este filtro IC_bueno=+0.020 (n=98)

- **FILTRO** `streak_len` > `4.0` → IC=-0.192 (n=24)

  - _Acción_: SKIP cuando `streak_len` > 4.0
  - _Potencial_: sin este filtro IC_bueno=-0.041 (n=120)

- **FILTRO** `libro_liquidez` < `3352.7321` → IC=-0.194 (n=34)

  - _Acción_: SKIP cuando `libro_liquidez` < 3352.7321
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=103)

- **FILTRO** `hora_utc` > `16.0` → IC=-0.141 (n=37)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.022 (n=134)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.125 (n=22)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=-0.036 (n=149)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=76)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=80)

- **FILTRO** `libro_liquidez` < `3222.7779` → IC=-0.134 (n=39)

  - _Acción_: SKIP cuando `libro_liquidez` < 3222.7779
  - _Potencial_: sin este filtro IC_bueno=-0.021 (n=117)

### STREAK_MOM_5M#ETH#5min
- **FILTRO** `hora_utc` < `16.0` → IC=-0.133 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 16.0
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=20)

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

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.130 (n=25)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 9.0 (IC base=+0.031)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.125 (n=22)

  - _Acción_: Kelly boost +0.62€ cuando `libro_spread` < 0.01 (IC base=+0.031)

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
- **FILTRO** `sigma_ewma_delta_pct` > `17.593` → IC=-0.143 (n=26)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.593
  - _Potencial_: sin este filtro IC_bueno=+0.131 (n=269)

- **PATRÓN** `ibs_15` > `0.7359` → IC=+0.190 (n=298)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.95€ cuando `ibs_15` > 0.7359 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` > `0.7265` → IC=+0.196 (n=44)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.7265 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` < `0.2815` → IC=+0.140 (n=170)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.2815 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.602` → IC=+0.159 (n=39)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 18.602 (IC base=+0.034)

- **PATRÓN** `ibs_15` < `0.0259` → IC=+0.126 (n=172)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.63€ cuando `ibs_15` < 0.0259 (IC base=+0.060)

- **PATRÓN** `dist_vwap_pct` > `0.9263` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.9263 (IC base=+0.060)

- **PATRÓN** `sigma_ewma_delta_pct` < `17.593` → IC=+0.131 (n=269)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 17.593 (IC base=+0.060)

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

- **FILTRO** `pct_spot_vs_ref` |x|> `0.0182` → IC=-0.150 (n=18)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0182
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=20)

- **FILTRO** `hora_utc` < `20.0` → IC=-0.132 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 20.0
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=7)

- **FILTRO** `ibs_15` < `0.7622` → IC=-0.150 (n=18)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.7622
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=6)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.1613` → IC=-0.222 (n=16)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.1613
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=33)

- **PATRÓN** `drift_60min` |x|≤ `0.237` → IC=+0.122 (n=215)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.237 (IC base=+0.075)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.148 (n=163)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 12.0 (IC base=+0.075)

- **PATRÓN** `ibs_15` > `0.6428` → IC=+0.180 (n=176)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.90€ cuando `ibs_15` > 0.6428 (IC base=+0.075)

- **PATRÓN** `dist_vwap_pct` > `0.7448` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7448 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.975` → IC=+0.156 (n=62)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 13.975 (IC base=+0.075)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.250 (n=18)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.007)

- **PATRÓN** `ibs_15` < `0.0451` → IC=+0.130 (n=25)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.65€ cuando `ibs_15` < 0.0451 (IC base=+0.007)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_h` < `0.012` → IC=-0.143 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.012
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

- **FILTRO** `ibs_15` < `0.8328` → IC=-0.206 (n=15)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.8328
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=5)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `sigma_ewma_delta_pct` < `14.506` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 14.506
  - _Potencial_: sin este filtro IC_bueno=+0.196 (n=21)

- **FILTRO** `sigma_ewma_delta_pct` > `21.947` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 21.947
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=120)

- **PATRÓN** `ibs_15` > `0.7721` → IC=+0.197 (n=97)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.98€ cuando `ibs_15` > 0.7721 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.5087` → IC=+0.145 (n=91)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.5087 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.327` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.327 (IC base=+0.030)

- **PATRÓN** `sigma_h` < `0.0058` → IC=+0.126 (n=97)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0058 (IC base=+0.049)

- **PATRÓN** `dist_vwap_pct` > `0.9766` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9766 (IC base=+0.049)

### UPDOWN_GBM#ETH#60min
- **FILTRO** `delta_ratio_macro` |x|≤ `0.133` → IC=-0.167 (n=19)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.133
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=19)

- **FILTRO** `hora_utc` < `15.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 15.0
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=9)

- **FILTRO** `ibs_15` > `0.2558` → IC=-0.132 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.2558
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `sigma_h` > `0.0204` → IC=-0.167 (n=16)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0204
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

- **FILTRO** `sigma_h` < `0.0139` → IC=-0.167 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0139
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=34)

- **FILTRO** `drift_60min` |x|> `0.1038` → IC=-0.125 (n=30)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.1038
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `drift_15min` |x|> `0.3193` → IC=-0.125 (n=30)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3193
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1211` → IC=-0.196 (n=21)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1211
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

- **FILTRO** `drift_60min` |x|> `0.4237` → IC=-0.167 (n=16)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.4237
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

- **FILTRO** `drift_15min` |x|> `0.5673` → IC=-0.140 (n=23)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5673
  - _Potencial_: sin este filtro IC_bueno=+0.018 (n=25)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.0905` → IC=-0.147 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0905
  - _Potencial_: sin este filtro IC_bueno=-0.014 (n=33)

- **FILTRO** `hora_utc` < `22.0` → IC=-0.150 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 22.0
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=21)

### UPDOWN_GBM#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0818` → IC=-0.182 (n=20)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0818
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

- **FILTRO** `sigma_h` > `0.0147` → IC=-0.150 (n=18)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0147
  - _Potencial_: sin este filtro IC_bueno=-0.045 (n=9)

- **FILTRO** `sigma_h` < `0.0205` → IC=-0.132 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.0205
  - _Potencial_: sin este filtro IC_bueno=-0.083 (n=10)

- **FILTRO** `drift_15min` |x|> `0.4528` → IC=-0.250 (n=18)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4528
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=7)

- **FILTRO** `hora_utc` < `4.0` → IC=-0.147 (n=15)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.177 (n=63)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.219 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0094 (IC base=+0.141)

- **PATRÓN** `drift_60min` |x|≤ `0.2343` → IC=+0.177 (n=29)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.89€ cuando `drift_60min` |x|≤ 0.2343 (IC base=+0.141)

- **PATRÓN** `drift_15min` |x|≤ `0.9428` → IC=+0.172 (n=56)

  - _Acción_: Kelly boost +0.86€ cuando `drift_15min` |x|≤ 0.9428 (IC base=+0.141)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1253` → IC=+0.159 (n=42)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.1253 (IC base=+0.141)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.177 (n=63)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 4.0 (IC base=+0.141)

- **PATRÓN** `ibs_15` < `0.0769` → IC=+0.179 (n=54)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.89€ cuando `ibs_15` < 0.0769 (IC base=+0.141)

### WEEKLY_PRICE
- **FILTRO** `T_h` < `144.8242` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `T_h` < 144.8242
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

- **PATRÓN** `T_h` > `145.7688` → IC=+0.361 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 145.7688 (IC base=+0.307)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `144.6231` → IC=+0.278 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 144.6231 (IC base=+0.260)

- **PATRÓN** `pct_dist` |x|≤ `1.2005` → IC=+0.389 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 1.2005 (IC base=+0.260)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.9965` → IC=+0.288 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9965 (IC base=+0.250)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` < `146.1402` → IC=+0.367 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 146.1402 (IC base=+0.349)

- **PATRÓN** `T_h` > `87.9959` → IC=+0.363 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9959 (IC base=+0.349)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: IBS > 0.7359 correlaciona con éxito en UPDOWN_GBM#15min (IC=+0.190 n=298). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#BTC#15min**: IBS > 0.6428 correlaciona con éxito en UPDOWN_GBM#BTC#15min (IC=+0.180 n=176). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#ETH#15min**: IBS > 0.7721 correlaciona con éxito en UPDOWN_GBM#ETH#15min (IC=+0.197 n=97). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#XRP#15min**: IBS < 0.0769 correlaciona con éxito en UPDOWN_GBM#XRP#15min (IC=+0.179 n=54). Confirma señal de reversión media → alinear con BUY_YES.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min` — IC=+0.316 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH` — IC=+0.316 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_TARDIO#DOGE#15min` — IC=+0.265 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_TARDIO#DOGE` — IC=+0.265 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 227 | +0.138 | +11.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 227 | +0.138 | +11.15€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 97 | +0.157 | +5.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 97 | +0.157 | +5.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 80 | +0.159 | +5.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 80 | +0.159 | +5.37€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 50 | +0.058 | +0.75€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 50 | +0.058 | +0.75€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 3545 | +0.183 | +29.91€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 2303 | +0.216 | +76.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 151 | +0.075 | +3.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 485 | +0.096 | -76.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 606 | +0.153 | +26.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 1030 | +0.192 | +26.60€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 768 | +0.208 | -4.32€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 50 | +0.115 | +6.59€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 202 | +0.172 | +28.10€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#ETH | 1261 | +0.177 | +7.56€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 763 | +0.219 | +38.64€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 50 | -0.019 | -9.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 246 | +0.105 | -33.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 202 | +0.152 | +11.76€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL | 1241 | +0.182 | -3.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 761 | +0.224 | +44.79€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 51 | +0.123 | +6.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 227 | +0.098 | -41.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 202 | +0.132 | -13.32€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#XRP | 13 | +0.065 | -0.66€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 11 | +0.021 | -2.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 127 | +0.306 | +2.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 127 | +0.306 | +2.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 127 | +0.306 | +2.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 127 | +0.306 | +2.99€ | 0 | 0 |
| ✅ GBM_LATE_15M | 5631 | +0.105 | +1875.69€ | 0 | 8 |
| ✅ GBM_LATE_15M#15min | 5631 | +0.105 | +1875.69€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 1347 | +0.075 | +239.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1347 | +0.075 | +239.15€ | 0 | 5 |
| ✅ GBM_LATE_15M#ETH | 1299 | +0.078 | +245.45€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1299 | +0.078 | +245.45€ | 0 | 5 |
| ✅ GBM_LATE_15M#SOL | 1520 | +0.101 | +596.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1520 | +0.101 | +596.46€ | 1 | 7 |
| ✅ GBM_LATE_15M#XRP | 1465 | +0.162 | +794.63€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1465 | +0.162 | +794.63€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 2857 | +0.151 | +1689.64€ | 0 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 2857 | +0.151 | +1689.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 730 | +0.115 | +339.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 730 | +0.115 | +339.38€ | 0 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 751 | +0.117 | +356.66€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 751 | +0.117 | +356.66€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 738 | +0.111 | +318.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 738 | +0.111 | +318.09€ | 1 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 638 | +0.278 | +675.51€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 638 | +0.278 | +675.51€ | 0 | 12 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 165 | +0.165 | +93.99€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 165 | +0.165 | +93.99€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC | 9 | -0.102 | -1.94€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 9 | -0.102 | -1.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 28 | +0.100 | +3.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 28 | +0.100 | +3.65€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL | 8 | -0.120 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 8 | -0.120 | -1.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 120 | +0.246 | +94.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 120 | +0.246 | +94.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 2801 | +0.102 | +991.06€ | 0 | 9 |
| ✅ GBM_LATE_15M_TARDIO#15min | 2801 | +0.102 | +991.06€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 680 | +0.070 | +143.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 680 | +0.070 | +143.24€ | 0 | 7 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 674 | +0.038 | +67.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 674 | +0.038 | +67.16€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 624 | +0.058 | +134.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 624 | +0.058 | +134.64€ | 2 | 7 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 823 | +0.214 | +646.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 823 | +0.214 | +646.02€ | 0 | 13 |
| ✅ GBM_LATE_5M | 38 | +0.025 | -0.23€ | 0 | 0 |
| ✅ GBM_LATE_5M#5min | 38 | +0.025 | -0.23€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 5 | +0.018 | -0.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 5 | +0.018 | -0.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 5 | +0.018 | -0.29€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 5 | +0.018 | -0.29€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL | 14 | -0.087 | -1.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 14 | -0.087 | -1.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 14 | +0.087 | +1.87€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 14 | +0.087 | +1.87€ | 0 | 0 |
| ✅ GBM_LATE_60M | 326 | -0.116 | +3.81€ | 4 | 1 |
| ✅ GBM_LATE_60M#60min | 326 | -0.116 | +3.81€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 114 | -0.035 | +5.51€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 114 | -0.035 | +5.51€ | 4 | 1 |
| ✅ GBM_LATE_60M#ETH | 102 | -0.164 | -12.97€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 102 | -0.164 | -12.97€ | 4 | 0 |
| ✅ GBM_LATE_60M#SOL | 110 | -0.152 | +11.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 110 | -0.152 | +11.27€ | 5 | 1 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO | 9 | -0.143 | -2.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO#60min | 9 | -0.143 | -2.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 49 | +0.226 | +24.54€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 49 | +0.226 | +24.54€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 49 | +0.226 | +24.54€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 49 | +0.226 | +24.54€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 180 | +0.050 | +17.10€ | 1 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 180 | +0.050 | +17.10€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 180 | +0.050 | +17.10€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 180 | +0.050 | +17.10€ | 1 | 2 |
| ✅ ORDER_FLOW_5M | 1630 | +0.013 | +14.21€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1494 | +0.009 | +1.62€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 202 | +0.044 | +6.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 202 | +0.044 | +6.33€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 2 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 218 | +0.000 | -2.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 218 | +0.000 | -2.14€ | 2 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 260 | -0.019 | -8.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 260 | -0.019 | -8.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 324 | +0.043 | +14.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 324 | +0.043 | +14.48€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#XRP | 199 | +0.003 | -3.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 199 | +0.003 | -3.33€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM | 149 | -0.169 | -4.27€ | 4 | 1 |
| 🚫 PRICE_TARGET_GBM#BTC | 62 | -0.250 | -18.09€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 56 | -0.276 | -17.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 6 | +0.000 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 57 | -0.178 | +0.27€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#ETH#atexpiry | 52 | -0.204 | -3.53€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 5 | +0.018 | +3.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 30 | +0.031 | +13.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 28 | +0.033 | +13.27€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 136 | -0.188 | -7.61€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 13 | +0.022 | +3.34€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 10 | +0.208 | +4.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 10 | +0.208 | +4.00€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 223 | +0.096 | +33.70€ | 1 | 9 |
| ✅ STREAK_FADE_15M#15min | 223 | +0.096 | +33.70€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 48 | +0.100 | +5.88€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 48 | +0.100 | +5.88€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 76 | +0.167 | +28.84€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 76 | +0.167 | +28.84€ | 0 | 5 |
| ✅ STREAK_FADE_15M#XRP | 99 | +0.035 | -1.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 99 | +0.035 | -1.02€ | 1 | 1 |
| ✅ STREAK_FADE_5M | 246 | -0.048 | -24.96€ | 3 | 0 |
| ✅ STREAK_FADE_5M#5min | 246 | -0.048 | -24.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 47 | -0.153 | -8.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 47 | -0.153 | -8.07€ | 6 | 0 |
| ✅ STREAK_FADE_5M#SOL | 94 | -0.021 | -7.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 94 | -0.021 | -7.62€ | 2 | 1 |
| ✅ STREAK_FADE_5M#XRP | 105 | -0.023 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 105 | -0.023 | -9.27€ | 1 | 0 |
| 🚫 STREAK_MOM_5M | 315 | -0.058 | -25.36€ | 8 | 0 |
| ✅ STREAK_MOM_5M#5min | 315 | -0.058 | -25.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 106 | -0.056 | -6.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 106 | -0.056 | -6.82€ | 2 | 0 |
| ✅ STREAK_MOM_5M#SOL | 111 | -0.013 | -5.19€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 111 | -0.013 | -5.19€ | 2 | 2 |
| ✅ STREAK_MOM_5M#XRP | 98 | -0.110 | -13.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 98 | -0.110 | -13.35€ | 5 | 0 |
| 🚫 STRUCT_NO_15M | 15 | -0.199 | -4.68€ | 0 | 0 |
| 🚫 STRUCT_NO_15M#15min | 15 | -0.199 | -4.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ UPDOWN_GBM | 1783 | +0.021 | +134.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1523 | +0.047 | +172.64€ | 1 | 7 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 127 | -0.058 | -10.76€ | 7 | 0 |
| ✅ UPDOWN_GBM#BNB | 123 | +0.084 | +37.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 123 | +0.084 | +37.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 451 | +0.025 | +29.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 368 | +0.062 | +43.56€ | 1 | 7 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 42 | -0.068 | -6.16€ | 2 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 83 | +0.065 | +11.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 80 | +0.073 | +12.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 824 | +0.024 | +42.90€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 731 | +0.040 | +53.96€ | 2 | 5 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 54 | -0.018 | -2.56€ | 3 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 172 | -0.092 | -16.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 104 | -0.066 | -9.62€ | 9 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 31 | -0.106 | -2.03€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 128 | +0.054 | +31.75€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 117 | +0.080 | +35.04€ | 5 | 6 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 54 | +0.268 | +9.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 54 | +0.268 | +9.12€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 18 | +0.135 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 18 | +0.135 | -2.16€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 36 | +0.316 | +11.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 36 | +0.316 | +11.28€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 508 | +0.184 | +222.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 508 | +0.184 | +222.48€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 41 | +0.198 | +16.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 41 | +0.198 | +16.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 58 | +0.083 | +8.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 58 | +0.083 | +8.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 32 | +0.265 | +18.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 32 | +0.265 | +18.46€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 126 | +0.211 | +51.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 126 | +0.211 | +51.05€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 132 | +0.134 | +47.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 132 | +0.134 | +47.67€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 119 | +0.219 | +79.76€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 119 | +0.219 | +79.76€ | 0 | 0 |
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
| ✅ WEEKLY_PRICE | 295 | +0.157 | +49.68€ | 1 | 1 |
| ✅ WEEKLY_PRICE#BTC | 86 | +0.102 | -6.63€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 84 | +0.116 | -5.35€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 125 | +0.216 | +61.65€ | 0 | 2 |