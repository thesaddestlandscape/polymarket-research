# Hipótesis automáticas — 2026-07-21 04:40 UTC
_Generado por shadow_postmortem.py sobre 25970 resoluciones (PNL=+6336.80€)_

## Patrones causales activos

### FAVORITO_CONFIRMADO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.205 (n=1451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.208 (n=1643)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.695` → IC=+0.318 (n=755)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.695 (IC base=+0.202)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.205 (n=1827)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.174 (n=679)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 17.0 (IC base=+0.172)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.211 (n=596)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.340 (n=596)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.172)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=1964)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `4207.6934` → IC=+0.174 (n=1184)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 4207.6934 (IC base=+0.172)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.226 (n=122)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.231 (n=169)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.215)

- **PATRÓN** `py_entrada` > `0.605` → IC=+0.268 (n=355)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.605 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.275 (n=127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.357 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.209)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.217 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.273 (n=95)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 19.0 (IC base=+0.220)

- **PATRÓN** `py_entrada` < `0.565` → IC=+0.286 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.565 (IC base=+0.220)

- **PATRÓN** `py_entrada` > `0.635` → IC=+0.265 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.635 (IC base=+0.220)

- **PATRÓN** `libro_liquidez` > `8909.1861` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8909.1861 (IC base=+0.220)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.284 (n=49)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.164)

- **PATRÓN** `py_entrada` < `0.41` → IC=+0.253 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.41 (IC base=+0.164)

- **PATRÓN** `libro_liquidez` > `7358.3864` → IC=+0.171 (n=71)

  - _Acción_: Kelly boost +0.86€ cuando `libro_liquidez` > 7358.3864 (IC base=+0.164)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.238 (n=353)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.235 (n=360)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.228)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.364 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.228)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.230 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.228)

- **PATRÓN** `libro_liquidez` > `4287.3371` → IC=+0.235 (n=232)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4287.3371 (IC base=+0.228)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.245 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.210)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.387 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.210)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.177 (n=91)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 5.0 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.231 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.175)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.575 (IC base=+0.175)

- **PATRÓN** `py_entrada` > `0.655` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.655 (IC base=+0.175)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=96)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.175)

- **PATRÓN** `libro_liquidez` > `3384.7911` → IC=+0.174 (n=87)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 3384.7911 (IC base=+0.175)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.207 (n=39)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.159 (n=83)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.405 (IC base=+0.132)

- **PATRÓN** `py_entrada` > `0.365` → IC=+0.145 (n=108)

  - _Acción_: Kelly boost +0.73€ cuando `py_entrada` > 0.365 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `6050.5374` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6050.5374 (IC base=+0.132)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.254 (n=128)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.237)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.245 (n=163)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.237)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.333 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.237)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.216 (n=188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.250 (n=126)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.343 (n=125)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.209)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.258 (n=31)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.575 (IC base=+0.180)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.194 (n=60)

  - _Acción_: Kelly boost +0.97€ cuando `py_entrada` > 0.61 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.181 (n=89)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.02 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.257 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.090)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.128 (n=1986)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 8.0 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.6996` → IC=+0.133 (n=197)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.6996 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.066` → IC=+0.241 (n=214)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.066 (IC base=+0.115)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.128 (n=1597)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` > 0.0086 (IC base=+0.110)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.137 (n=824)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.68€ cuando `hora_utc` < 5.0 (IC base=+0.110)

- **PATRÓN** `dist_vwap_pct` > `0.1556` → IC=+0.130 (n=446)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.1556 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.113` → IC=+0.129 (n=289)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` > 6.113 (IC base=+0.110)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.127 (n=440)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0063 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.501` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.501 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` < `0.1056` → IC=+0.142 (n=160)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1056 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.388` → IC=+0.221 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.388 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.285` → IC=+0.167 (n=112)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 4.285 (IC base=+0.071)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.164 (n=141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0044 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.7964` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.7964 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.283` → IC=+0.142 (n=93)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.283 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.243` → IC=+0.216 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.243 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `1.0404` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 1.0404 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.447` → IC=+0.192 (n=92)

  - _Acción_: Kelly boost +0.96€ cuando `sigma_ewma_delta_pct` > 7.447 (IC base=+0.075)

### GBM_LATE_15M#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.147 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 18.0 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.303` → IC=+0.264 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.303 (IC base=+0.097)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.142 (n=389)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.011 (IC base=+0.119)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.169 (n=264)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 7.0 (IC base=+0.119)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.162 (n=208)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0103 (IC base=+0.155)

- **PATRÓN** `sigma_h` > `0.0148` → IC=+0.168 (n=413)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0148 (IC base=+0.155)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.161 (n=627)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 6.0 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` > `0.6006` → IC=+0.221 (n=66)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6006 (IC base=+0.155)

- **PATRÓN** `dist_vwap_pct` < `0.1141` → IC=+0.158 (n=252)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` < 0.1141 (IC base=+0.155)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.574` → IC=+0.300 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.574 (IC base=+0.155)

- **PATRÓN** `sigma_h` < `0.0094` → IC=+0.185 (n=214)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0094 (IC base=+0.169)

- **PATRÓN** `sigma_h` > `0.0253` → IC=+0.199 (n=214)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0253 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.182 (n=221)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 18.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.216 (n=216)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.169)

- **PATRÓN** `dist_vwap_pct` > `0.4552` → IC=+0.210 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4552 (IC base=+0.169)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.238` → IC=+0.162 (n=382)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 9.238 (IC base=+0.169)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.229 (n=418)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.185 (n=885)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 12.0 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `0.5174` → IC=+0.211 (n=244)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5174 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.167` → IC=+0.291 (n=199)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.167 (IC base=+0.161)

- **PATRÓN** `sigma_h` > `0.0072` → IC=+0.193 (n=833)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.0072 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=628)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.175 (n=438)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 5.0 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` < `0.6268` → IC=+0.179 (n=1118)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.6268 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.101` → IC=+0.203 (n=163)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.101 (IC base=+0.162)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `sigma_h` < `0.0041` → IC=+0.146 (n=196)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0041 (IC base=+0.130)

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.151 (n=262)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0031 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.151 (n=302)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 6.0 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.5162` → IC=+0.196 (n=44)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.5162 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.371` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.371 (IC base=+0.130)

- **PATRÓN** `sigma_h` > `0.0026` → IC=+0.139 (n=322)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0026 (IC base=+0.125)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.157 (n=164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 15.0 (IC base=+0.125)

- **PATRÓN** `dist_vwap_pct` < `0.5143` → IC=+0.129 (n=286)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.5143 (IC base=+0.125)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.745` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.745 (IC base=+0.125)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.236 (n=104)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.176 (n=214)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 12.0 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.1876` → IC=+0.170 (n=116)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.1876 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.778` → IC=+0.275 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.778 (IC base=+0.137)

- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.135 (n=220)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` < 0.0052 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.149 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 18.0 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.133 (n=115)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 5.0 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.5687` → IC=+0.151 (n=84)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.5687 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.51` → IC=+0.198 (n=117)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 4.51 (IC base=+0.113)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.198 (n=157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0119 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.142 (n=325)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 8.0 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.1404` → IC=+0.160 (n=148)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1404 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.667` → IC=+0.294 (n=139)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.667 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.012` → IC=+0.148 (n=291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.012 (IC base=+0.122)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.187 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 5.0 (IC base=+0.122)

- **PATRÓN** `dist_vwap_pct` < `0.8629` → IC=+0.165 (n=249)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.8629 (IC base=+0.122)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.311` → IC=+0.181 (n=211)

  - _Acción_: Kelly boost +0.90€ cuando `sigma_ewma_delta_pct` < 2.311 (IC base=+0.122)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` < `0.0165` → IC=+0.257 (n=306)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0165 (IC base=+0.251)

- **PATRÓN** `sigma_h` > `0.0085` → IC=+0.263 (n=306)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0085 (IC base=+0.251)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.256 (n=289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.251)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.256 (n=313)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.251)

- **PATRÓN** `dist_vwap_pct` > `0.6283` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6283 (IC base=+0.251)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.15` → IC=+0.371 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.15 (IC base=+0.251)

- **PATRÓN** `sigma_h` > `0.0076` → IC=+0.315 (n=311)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0076 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.304 (n=314)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.4366` → IC=+0.357 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4366 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.503` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.503 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.827` → IC=+0.295 (n=291)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.827 (IC base=+0.288)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0135` → IC=+0.181 (n=393)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0135 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.131 (n=1083)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 8.0 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.4944` → IC=+0.169 (n=252)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.4944 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.1126` → IC=+0.141 (n=656)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.1126 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.025` → IC=+0.306 (n=173)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.025 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.8066` → IC=+0.123 (n=1178)

  - _Acción_: Kelly boost +0.61€ cuando `dist_vwap_pct` < 0.8066 (IC base=+0.106)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.176 (n=171)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0044 (IC base=+0.114)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.149 (n=257)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 6.0 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `0.5163` → IC=+0.202 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5163 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.1341` → IC=+0.128 (n=162)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.1341 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.388` → IC=+0.259 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.388 (IC base=+0.114)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.129 (n=95)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.004 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.864` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.864 (IC base=+0.070)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.463` → IC=+0.167 (n=70)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 7.463 (IC base=+0.054)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.793` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.793
  - _Potencial_: sin este filtro IC_bueno=+0.076 (n=255)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.441` → IC=+0.306 (n=101)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.441 (IC base=+0.075)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.173 (n=102)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0083 (IC base=+0.052)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0259` → IC=+0.206 (n=382)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0259 (IC base=+0.202)

- **PATRÓN** `sigma_h` > `0.0137` → IC=+0.215 (n=254)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0137 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.209 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.218 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` > `0.2507` → IC=+0.234 (n=126)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2507 (IC base=+0.202)

- **PATRÓN** `dist_vwap_pct` < `0.1016` → IC=+0.203 (n=224)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1016 (IC base=+0.202)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.566` → IC=+0.319 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.566 (IC base=+0.202)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.211 (n=133)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0082 (IC base=+0.209)

- **PATRÓN** `sigma_h` > `0.0206` → IC=+0.226 (n=133)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0206 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.226 (n=199)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.221 (n=138)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.209)

- **PATRÓN** `dist_vwap_pct` > `0.1094` → IC=+0.234 (n=137)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1094 (IC base=+0.209)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.154` → IC=+0.220 (n=369)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.154 (IC base=+0.209)

### GBM_LATE_60M
- **FILTRO** `dist_vwap_pct` < `0.129` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.129
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=14)

- **FILTRO** `sigma_ewma_delta_pct` < `11.422` → IC=-0.206 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 11.422
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=6)

- **FILTRO** `sigma_h` > `0.0133` → IC=-0.300 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=118)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.272 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=44)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.150 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0053 (IC base=-0.014)

### GBM_LATE_60M#BTC#60min
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
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0053 (IC base=+0.035)

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

### LEADLAG_BTC_XRP_15M
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=126)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=72)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.122 (n=72)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.505 (IC base=+0.054)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.016 (n=126)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=72)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.122 (n=72)

  - _Acción_: Kelly boost +0.61€ cuando `py_entrada` < 0.505 (IC base=+0.054)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=111)

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
  - _Potencial_: sin este filtro IC_bueno=+0.189 (n=72)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.173 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 13.0 (IC base=+0.108)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.505 (IC base=+0.108)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.158 (n=77)

  - _Acción_: Kelly boost +0.79€ cuando `streak_len` < 4.0 (IC base=+0.108)

- **PATRÓN** `volumen_racha` < `302326.1` → IC=+0.172 (n=59)

  - _Acción_: Kelly boost +0.86€ cuando `volumen_racha` < 302326.1 (IC base=+0.108)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.01 (IC base=+0.108)

- **PATRÓN** `libro_liquidez` > `2045.6663` → IC=+0.176 (n=66)

  - _Acción_: Kelly boost +0.88€ cuando `libro_liquidez` > 2045.6663 (IC base=+0.108)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.233 (n=43)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.075)

- **PATRÓN** `volumen_racha` < `503163.4` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `volumen_racha` < 503163.4 (IC base=+0.075)

### STREAK_FADE_15M#SOL#15min
- **PATRÓN** `py_entrada` < `0.505` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.505 (IC base=+0.150)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `streak_len` < 4.0 (IC base=+0.150)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.147 (n=15)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 19.0 (IC base=+0.130)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.485 (IC base=+0.130)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `hora_utc` < `9.0` → IC=+0.156 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 9.0 (IC base=+0.061)

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
  - _Potencial_: sin este filtro IC_bueno=+0.049 (n=80)

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
- **PATRÓN** `ibs_15` > `0.7526` → IC=+0.211 (n=334)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7526 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` > `0.7265` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.7265 (IC base=+0.044)

- **PATRÓN** `dist_vwap_pct` < `0.4761` → IC=+0.143 (n=242)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.4761 (IC base=+0.044)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.791` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `sigma_ewma_delta_pct` > 23.791 (IC base=+0.044)

- **PATRÓN** `ibs_15` < `0.0333` → IC=+0.136 (n=215)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.68€ cuando `ibs_15` < 0.0333 (IC base=+0.053)

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
  - _Potencial_: sin este filtro IC_bueno=-0.038 (n=11)

- **FILTRO** `ibs_15` < `0.7576` → IC=-0.214 (n=19)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.7576
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.0451` → IC=-0.155 (n=27)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.0451
  - _Potencial_: sin este filtro IC_bueno=+0.145 (n=29)

- **PATRÓN** `drift_60min` |x|≤ `0.2293` → IC=+0.126 (n=244)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.63€ cuando `drift_60min` |x|≤ 0.2293 (IC base=+0.088)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.149 (n=189)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 12.0 (IC base=+0.088)

- **PATRÓN** `ibs_15` > `0.6374` → IC=+0.205 (n=205)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6374 (IC base=+0.088)

- **PATRÓN** `dist_vwap_pct` > `0.7608` → IC=+0.237 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7608 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.017` → IC=+0.163 (n=84)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 14.017 (IC base=+0.088)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.182 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0056 (IC base=+0.013)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_h` < `0.012` → IC=-0.143 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.012
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

### UPDOWN_GBM#ETH#15min
- **FILTRO** `sigma_ewma_delta_pct` < `18.413` → IC=-0.154 (n=24)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 18.413
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=31)

- **PATRÓN** `ibs_15` > `0.7738` → IC=+0.211 (n=102)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7738 (IC base=+0.034)

- **PATRÓN** `dist_vwap_pct` < `0.5043` → IC=+0.141 (n=101)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` < 0.5043 (IC base=+0.034)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.413` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 18.413 (IC base=+0.034)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.131 (n=139)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0061 (IC base=+0.051)

- **PATRÓN** `dist_vwap_pct` > `0.9454` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.9454 (IC base=+0.051)

### UPDOWN_GBM#SOL#15min
- **FILTRO** `drift_15min` |x|> `0.3193` → IC=-0.125 (n=30)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3193
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=11)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1211` → IC=-0.196 (n=21)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1211
  - _Potencial_: sin este filtro IC_bueno=+0.022 (n=21)

- **FILTRO** `drift_15min` |x|> `0.5363` → IC=-0.125 (n=30)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5363
  - _Potencial_: sin este filtro IC_bueno=+0.045 (n=31)

- **FILTRO** `hora_utc` < `21.0` → IC=-0.154 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 21.0
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=28)

- **PATRÓN** `sigma_h` < `0.0092` → IC=+0.289 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0092 (IC base=-0.007)

### UPDOWN_GBM#XRP#15min
- **FILTRO** `pct_spot_vs_ref` |x|> `0.0748` → IC=-0.196 (n=21)
  - _Por qué funciona_: precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión
  - _Acción_: SKIP cuando `pct_spot_vs_ref` |x|> 0.0748
  - _Potencial_: sin este filtro IC_bueno=+0.100 (n=8)

- **FILTRO** `sigma_h` > `0.0141` → IC=-0.167 (n=19)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0141
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=10)

- **FILTRO** `drift_15min` |x|> `0.4528` → IC=-0.250 (n=18)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.4528
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=9)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.143 (n=68)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 12.0 (IC base=+0.097)

- **PATRÓN** `ibs_15` < `0.1467` → IC=+0.135 (n=83)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.68€ cuando `ibs_15` < 0.1467 (IC base=+0.097)

### WEEKLY_PRICE
- **FILTRO** `T_h` < `144.8242` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `T_h` < 144.8242
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

- **PATRÓN** `T_h` > `146.1118` → IC=+0.368 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.307)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` > `144.7029` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 144.7029 (IC base=+0.259)

- **PATRÓN** `pct_dist` |x|≤ `1.2005` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 1.2005 (IC base=+0.259)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` < `135.9981` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 135.9981 (IC base=+0.250)

- **PATRÓN** `T_h` > `111.9928` → IC=+0.278 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9928 (IC base=+0.250)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` < `146.1402` → IC=+0.368 (n=74)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 146.1402 (IC base=+0.353)

- **PATRÓN** `T_h` > `111.9928` → IC=+0.371 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9928 (IC base=+0.353)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: IBS > 0.7526 correlaciona con éxito en UPDOWN_GBM#15min (IC=+0.211 n=334). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#BTC#15min**: IBS > 0.6374 correlaciona con éxito en UPDOWN_GBM#BTC#15min (IC=+0.205 n=205). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#ETH#15min**: IBS > 0.7738 correlaciona con éxito en UPDOWN_GBM#ETH#15min (IC=+0.211 n=102). Confirma señal de reversión media → alinear con BUY_NO.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 541 | +0.128 | +17.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 541 | +0.128 | +17.65€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 202 | +0.142 | +5.27€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 202 | +0.142 | +5.27€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 215 | +0.131 | +1.63€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 215 | +0.131 | +1.63€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 124 | +0.095 | +10.74€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 124 | +0.095 | +10.74€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 6 | +0.113 | +1.04€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 6 | +0.113 | +1.04€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 6 | +0.113 | +1.04€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 6 | +0.113 | +1.04€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 4489 | +0.186 | +64.35€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#15min | 2920 | +0.218 | +101.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 193 | +0.064 | -7.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 605 | +0.105 | -81.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 771 | +0.160 | +52.28€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 1304 | +0.199 | +57.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 973 | +0.213 | +8.48€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 64 | +0.091 | +1.32€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 257 | +0.191 | +51.05€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#ETH | 1590 | +0.178 | +7.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 962 | +0.219 | +42.43€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 64 | -0.015 | -13.85€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 307 | +0.112 | -37.44€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 257 | +0.152 | +16.17€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#SOL | 1572 | +0.183 | -1.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 966 | +0.223 | +52.90€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 65 | +0.112 | +4.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 284 | +0.105 | -44.82€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 257 | +0.133 | -14.94€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 23 | +0.140 | +1.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 19 | +0.068 | -2.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 205 | +0.316 | +9.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 205 | +0.316 | +9.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 205 | +0.316 | +9.51€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 205 | +0.316 | +9.51€ | 0 | 0 |
| ✅ GBM_LATE_15M | 6379 | +0.103 | +2145.67€ | 0 | 7 |
| ✅ GBM_LATE_15M#15min | 6379 | +0.103 | +2145.67€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 1523 | +0.076 | +294.54€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1523 | +0.076 | +294.54€ | 0 | 5 |
| ✅ GBM_LATE_15M#ETH | 1445 | +0.076 | +268.81€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1445 | +0.076 | +268.81€ | 0 | 6 |
| ✅ GBM_LATE_15M#SOL | 1730 | +0.092 | +637.32€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1730 | +0.092 | +637.32€ | 0 | 4 |
| ✅ GBM_LATE_15M#XRP | 1681 | +0.163 | +945.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1681 | +0.163 | +945.00€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 3575 | +0.145 | +2092.56€ | 0 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 3575 | +0.145 | +2092.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 911 | +0.109 | +423.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 911 | +0.109 | +423.60€ | 0 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 934 | +0.103 | +397.00€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 934 | +0.103 | +397.00€ | 0 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 908 | +0.112 | +415.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 908 | +0.112 | +415.65€ | 0 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 822 | +0.269 | +856.32€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 822 | +0.269 | +856.32€ | 0 | 11 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 203 | +0.139 | +104.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 203 | +0.139 | +104.87€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC | 9 | -0.102 | -1.94€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 9 | -0.102 | -1.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 47 | +0.031 | +6.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 47 | +0.031 | +6.08€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL | 8 | -0.120 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 8 | -0.120 | -1.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 139 | +0.231 | +102.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 139 | +0.231 | +102.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 3557 | +0.095 | +1236.29€ | 0 | 6 |
| ✅ GBM_LATE_15M_TARDIO#15min | 3557 | +0.095 | +1236.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 850 | +0.065 | +169.33€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 850 | +0.065 | +169.33€ | 0 | 5 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 857 | +0.034 | +89.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 857 | +0.034 | +89.93€ | 0 | 3 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 811 | +0.049 | +173.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 811 | +0.049 | +173.72€ | 1 | 2 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1039 | +0.206 | +803.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1039 | +0.206 | +803.31€ | 0 | 13 |
| ✅ GBM_LATE_5M | 228 | +0.048 | +24.82€ | 0 | 0 |
| ✅ GBM_LATE_5M#5min | 228 | +0.048 | +24.82€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 27 | +0.052 | -1.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 27 | +0.052 | -1.76€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 22 | +0.042 | +2.61€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 22 | +0.042 | +2.61€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL | 48 | -0.100 | +4.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 48 | -0.100 | +4.10€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 131 | +0.102 | +19.88€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 131 | +0.102 | +19.88€ | 0 | 0 |
| ✅ GBM_LATE_60M | 329 | -0.113 | +5.97€ | 4 | 1 |
| ✅ GBM_LATE_60M#60min | 329 | -0.113 | +5.97€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 115 | -0.038 | +5.00€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 115 | -0.038 | +5.00€ | 3 | 1 |
| ✅ GBM_LATE_60M#ETH | 104 | -0.151 | -10.30€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 104 | -0.151 | -10.30€ | 4 | 0 |
| ✅ GBM_LATE_60M#SOL | 110 | -0.152 | +11.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 110 | -0.152 | +11.27€ | 5 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO | 9 | -0.143 | -2.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO#60min | 9 | -0.143 | -2.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 108 | +0.109 | +21.00€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 108 | +0.109 | +21.00€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 108 | +0.109 | +21.00€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 108 | +0.109 | +21.00€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 242 | +0.021 | +12.71€ | 2 | 1 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 242 | +0.021 | +12.71€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 242 | +0.021 | +12.71€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 242 | +0.021 | +12.71€ | 2 | 1 |
| ✅ ORDER_FLOW_5M | 1641 | +0.011 | +11.65€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1505 | +0.007 | -0.94€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 206 | +0.038 | +5.20€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 206 | +0.038 | +5.20€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 219 | -0.002 | -2.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 219 | -0.002 | -2.65€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 262 | -0.019 | -8.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 262 | -0.019 | -8.49€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 325 | +0.044 | +15.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 325 | +0.044 | +15.10€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 202 | -0.005 | -4.86€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 202 | -0.005 | -4.86€ | 1 | 0 |
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
| ✅ RESOLUTION_SNIPER | 11 | +0.190 | +3.49€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 11 | +0.190 | +3.49€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 248 | +0.092 | +35.04€ | 1 | 8 |
| ✅ STREAK_FADE_15M#15min | 248 | +0.092 | +35.04€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 55 | +0.079 | +4.00€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 55 | +0.079 | +4.00€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 82 | +0.143 | +24.58€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 82 | +0.143 | +24.58€ | 0 | 4 |
| ✅ STREAK_FADE_15M#XRP | 111 | +0.058 | +6.46€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 111 | +0.058 | +6.46€ | 0 | 1 |
| ✅ STREAK_FADE_5M | 246 | -0.048 | -24.96€ | 3 | 0 |
| ✅ STREAK_FADE_5M#5min | 246 | -0.048 | -24.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 47 | -0.153 | -8.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 47 | -0.153 | -8.07€ | 3 | 0 |
| ✅ STREAK_FADE_5M#SOL | 94 | -0.021 | -7.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 94 | -0.021 | -7.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP | 105 | -0.023 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 105 | -0.023 | -9.27€ | 0 | 0 |
| 🚫 STREAK_MOM_5M | 315 | -0.058 | -25.36€ | 4 | 0 |
| ✅ STREAK_MOM_5M#5min | 315 | -0.058 | -25.36€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 106 | -0.056 | -6.82€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 106 | -0.056 | -6.82€ | 1 | 0 |
| ✅ STREAK_MOM_5M#SOL | 111 | -0.013 | -5.19€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 111 | -0.013 | -5.19€ | 2 | 0 |
| ✅ STREAK_MOM_5M#XRP | 98 | -0.110 | -13.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 98 | -0.110 | -13.35€ | 5 | 0 |
| 🚫 STRUCT_NO_15M | 15 | -0.199 | -4.68€ | 0 | 0 |
| 🚫 STRUCT_NO_15M#15min | 15 | -0.199 | -4.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ UPDOWN_GBM | 2029 | +0.025 | +155.96€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1767 | +0.049 | +195.04€ | 0 | 5 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 129 | -0.065 | -11.78€ | 6 | 0 |
| ✅ UPDOWN_GBM#BNB | 175 | +0.076 | +41.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 175 | +0.076 | +41.92€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 498 | +0.038 | +40.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 414 | +0.074 | +54.63€ | 1 | 6 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 43 | -0.078 | -6.67€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 118 | +0.033 | +11.64€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 115 | +0.038 | +12.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 874 | +0.027 | +46.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 780 | +0.043 | +58.04€ | 1 | 5 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 55 | -0.026 | -3.07€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 185 | -0.083 | -14.53€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 117 | -0.055 | -7.53€ | 4 | 1 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 31 | -0.106 | -2.03€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 177 | +0.042 | +32.15€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 166 | +0.059 | +35.44€ | 3 | 2 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 95 | +0.283 | +15.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 95 | +0.283 | +15.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 41 | +0.244 | +2.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 41 | +0.244 | +2.90€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 54 | +0.304 | +12.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 54 | +0.304 | +12.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 919 | +0.171 | +421.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 919 | +0.171 | +421.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 86 | +0.193 | +44.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 86 | +0.193 | +44.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 108 | +0.109 | +12.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 108 | +0.109 | +12.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 73 | +0.233 | +48.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 73 | +0.233 | +48.08€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 199 | +0.167 | +64.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 199 | +0.167 | +64.81€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 225 | +0.103 | +69.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 225 | +0.103 | +69.45€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 228 | +0.235 | +181.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 228 | +0.235 | +181.94€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 6 | +0.037 | +0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 6 | +0.037 | +0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 6 | +0.037 | +0.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 6 | +0.037 | +0.87€ | 0 | 0 |
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
| ✅ WEEKLY_PRICE | 305 | +0.161 | +51.01€ | 1 | 1 |
| ✅ WEEKLY_PRICE#BTC | 90 | +0.109 | -7.35€ | 0 | 2 |
| ✅ WEEKLY_PRICE#ETH | 88 | +0.122 | -5.63€ | 0 | 2 |
| ✅ WEEKLY_PRICE#SOL | 127 | +0.221 | +63.98€ | 0 | 2 |