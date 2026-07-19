# Hipótesis automáticas — 2026-07-19 06:02 UTC
_Generado por shadow_postmortem.py sobre 22001 resoluciones (PNL=+5322.79€)_

## Patrones causales activos

### FAVORITO_CONFIRMADO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.196 (n=1211)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 8.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.207 (n=1371)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.695` → IC=+0.306 (n=610)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.695 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.198 (n=1542)

  - _Acción_: Kelly boost +0.99€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.185 (n=554)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 17.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=641)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.341 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.176)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=1629)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.176)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.220 (n=212)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.225 (n=303)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.214)

- **PATRÓN** `py_entrada` > `0.615` → IC=+0.270 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.615 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `11311.7874` → IC=+0.217 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11311.7874 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.292 (n=104)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.376 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.206)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.197 (n=74)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 5.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.256 (n=76)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 19.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.565` → IC=+0.269 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.565 (IC base=+0.191)

- **PATRÓN** `py_entrada` > `0.635` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.635 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `8840.0271` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8840.0271 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.288 (n=31)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` < `0.41` → IC=+0.217 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.41 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `6436.3724` → IC=+0.163 (n=87)

  - _Acción_: Kelly boost +0.81€ cuando `libro_liquidez` > 6436.3724 (IC base=+0.141)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.236 (n=267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.225)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.238 (n=303)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.225)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.357 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.225)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.226 (n=374)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.225)

- **PATRÓN** `libro_liquidez` > `4397.2353` → IC=+0.236 (n=195)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4397.2353 (IC base=+0.225)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.227 (n=119)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.257 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.383 (n=109)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.221)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=77)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.196 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 19.0 (IC base=+0.160)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.575 (IC base=+0.160)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.188 (n=78)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.160)

- **PATRÓN** `libro_liquidez` > `6015.6895` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6015.6895 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.222 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.405 (IC base=+0.141)

- **PATRÓN** `libro_liquidez` > `3899.2794` → IC=+0.185 (n=87)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 3899.2794 (IC base=+0.141)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.255 (n=104)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.234)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.252 (n=111)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.234)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.302 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.220 (n=155)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.252 (n=143)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.214)

- **PATRÓN** `py_entrada` < `0.395` → IC=+0.265 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.395 (IC base=+0.214)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.250 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.64` → IC=+0.210 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.64 (IC base=+0.190)

- **PATRÓN** `py_entrada` > `0.575` → IC=+0.188 (n=75)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.575 (IC base=+0.190)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `libro_spread` < 0.02 (IC base=+0.190)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.079)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.127 (n=1799)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 8.0 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.5527` → IC=+0.130 (n=206)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.5527 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.976` → IC=+0.227 (n=170)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.976 (IC base=+0.115)

- **PATRÓN** `sigma_h` > `0.0088` → IC=+0.132 (n=1447)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0088 (IC base=+0.113)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.135 (n=1562)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 12.0 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.1554` → IC=+0.129 (n=365)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.1554 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` < `0.8997` → IC=+0.124 (n=1092)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.8997 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.146` → IC=+0.147 (n=230)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 6.146 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.03` → IC=+0.121 (n=968)

  - _Acción_: Kelly boost +0.60€ cuando `sigma_ewma_delta_pct` < 11.03 (IC base=+0.113)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.125 (n=403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0064 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.5433` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5433 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.154` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.154 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.1355` → IC=+0.136 (n=64)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` > 0.1355 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.5173` → IC=+0.132 (n=221)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.5173 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.933` → IC=+0.204 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 2.933 (IC base=+0.074)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.174 (n=136)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0044 (IC base=+0.098)

- **PATRÓN** `dist_vwap_pct` > `0.8385` → IC=+0.150 (n=18)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.8385 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.301` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.301 (IC base=+0.098)

- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.122 (n=183)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0042 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` > `0.6593` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.6593 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.497` → IC=+0.233 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.497 (IC base=+0.078)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `8.263` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.263
  - _Potencial_: sin este filtro IC_bueno=+0.095 (n=250)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.145 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 18.0 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.298` → IC=+0.216 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.298 (IC base=+0.104)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.138 (n=473)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.013 (IC base=+0.123)

- **PATRÓN** `sigma_h` > `0.009` → IC=+0.128 (n=536)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` > 0.009 (IC base=+0.123)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.169 (n=391)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 12.0 (IC base=+0.123)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_h` > `0.0153` → IC=+0.177 (n=367)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0153 (IC base=+0.153)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.156 (n=550)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 6.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.160 (n=369)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 11.0 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` > `0.5805` → IC=+0.245 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5805 (IC base=+0.153)

- **PATRÓN** `dist_vwap_pct` < `0.1135` → IC=+0.155 (n=204)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.1135 (IC base=+0.153)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.431` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.431 (IC base=+0.153)

- **PATRÓN** `sigma_h` < `0.0098` → IC=+0.196 (n=192)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.0098 (IC base=+0.171)

- **PATRÓN** `sigma_h` > `0.0256` → IC=+0.201 (n=192)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0256 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.231 (n=217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` > `0.3062` → IC=+0.167 (n=88)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.3062 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.5513` → IC=+0.169 (n=318)

  - _Acción_: Kelly boost +0.84€ cuando `dist_vwap_pct` < 0.5513 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.497` → IC=+0.172 (n=288)

  - _Acción_: Kelly boost +0.86€ cuando `sigma_ewma_delta_pct` < 7.497 (IC base=+0.171)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.237 (n=356)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.164)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.185 (n=760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 12.0 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` > `0.1667` → IC=+0.207 (n=397)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1667 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.061` → IC=+0.295 (n=159)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.061 (IC base=+0.164)

- **PATRÓN** `sigma_h` > `0.0045` → IC=+0.189 (n=1043)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` > 0.0045 (IC base=+0.171)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.183 (n=519)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 15.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.199 (n=363)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` < 5.0 (IC base=+0.171)

- **PATRÓN** `dist_vwap_pct` < `0.6261` → IC=+0.190 (n=910)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` < 0.6261 (IC base=+0.171)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.064` → IC=+0.231 (n=128)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.064 (IC base=+0.171)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `sigma_h` < `0.0063` → IC=+0.133 (n=254)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0063 (IC base=+0.129)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.151 (n=227)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.0029 (IC base=+0.129)

- **PATRÓN** `hora_utc` > `13.0` → IC=+0.180 (n=170)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 13.0 (IC base=+0.129)

- **PATRÓN** `dist_vwap_pct` > `0.3426` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.3426 (IC base=+0.129)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.368` → IC=+0.232 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.368 (IC base=+0.129)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.140 (n=265)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0061 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.176 (n=236)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0031 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.172 (n=132)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 15.0 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.116` → IC=+0.143 (n=68)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.116 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.4763` → IC=+0.135 (n=231)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.4763 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.151` → IC=+0.227 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.151 (IC base=+0.136)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.242 (n=91)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.172 (n=190)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 12.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.156 (n=286)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 18.0 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1369` → IC=+0.185 (n=109)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` > 0.1369 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.8688` → IC=+0.145 (n=218)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.8688 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.551` → IC=+0.281 (n=30)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.551 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.139 (n=242)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0066 (IC base=+0.128)

- **PATRÓN** `sigma_h` > `0.0041` → IC=+0.138 (n=244)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0041 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.156 (n=94)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 18.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.177 (n=122)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 7.0 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.619` → IC=+0.194 (n=60)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.619 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `1.1308` → IC=+0.142 (n=258)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 1.1308 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.495` → IC=+0.250 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.495 (IC base=+0.128)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `2.606` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.606
  - _Potencial_: sin este filtro IC_bueno=+0.184 (n=166)

- **PATRÓN** `sigma_h` > `0.0119` → IC=+0.191 (n=134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0119 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.159 (n=209)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 12.0 (IC base=+0.130)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.131 (n=272)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 16.0 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.6132` → IC=+0.195 (n=57)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.6132 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.628` → IC=+0.284 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.628 (IC base=+0.130)

- **PATRÓN** `sigma_h` < `0.0123` → IC=+0.151 (n=250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0123 (IC base=+0.120)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.178 (n=85)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 5.0 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` < `0.7922` → IC=+0.162 (n=208)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.7922 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.606` → IC=+0.184 (n=166)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` < 2.606 (IC base=+0.120)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` < `0.0169` → IC=+0.260 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0169 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.272 (n=244)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.255)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.262 (n=225)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.255)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.264 (n=252)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.255)

- **PATRÓN** `dist_vwap_pct` > `0.2782` → IC=+0.327 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2782 (IC base=+0.255)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.801` → IC=+0.396 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.801 (IC base=+0.255)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.330 (n=257)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0077 (IC base=+0.299)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.308 (n=264)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.299)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.303 (n=231)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.299)

- **PATRÓN** `dist_vwap_pct` > `0.307` → IC=+0.325 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.307 (IC base=+0.299)

- **PATRÓN** `dist_vwap_pct` < `0.5452` → IC=+0.311 (n=257)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5452 (IC base=+0.299)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.458` → IC=+0.317 (n=227)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.458 (IC base=+0.299)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.131 (n=326)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.0053 (IC base=+0.128)

- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.189 (n=326)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0136 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.134 (n=887)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 8.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `16.0` → IC=+0.133 (n=906)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 16.0 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.5305` → IC=+0.173 (n=194)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.5305 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1166` → IC=+0.154 (n=495)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1166 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.232` → IC=+0.287 (n=134)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.232 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.131 (n=415)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 6.0 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.774` → IC=+0.129 (n=947)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` < 0.774 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.527` → IC=+0.131 (n=247)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` > 3.527 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.031` → IC=+0.121 (n=846)

  - _Acción_: Kelly boost +0.61€ cuando `sigma_ewma_delta_pct` < 11.031 (IC base=+0.105)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.158 (n=147)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0044 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.155 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 8.0 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.5433` → IC=+0.200 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5433 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` < `0.138` → IC=+0.135 (n=124)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.138 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.025` → IC=+0.262 (n=40)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.025 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.128 (n=92)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 17.0 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.888` → IC=+0.160 (n=98)

  - _Acción_: Kelly boost +0.80€ cuando `sigma_ewma_delta_pct` > 2.888 (IC base=+0.080)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.174 (n=84)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0039 (IC base=+0.080)

- **PATRÓN** `dist_vwap_pct` < `0.272` → IC=+0.139 (n=128)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.272 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.369` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.369 (IC base=+0.080)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.821` → IC=+0.196 (n=54)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 7.821 (IC base=+0.048)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `4.985` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 4.985
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=202)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.126 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 8.0 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.7129` → IC=+0.130 (n=25)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.7129 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` < `0.1406` → IC=+0.125 (n=94)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.1406 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.747` → IC=+0.279 (n=75)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.747 (IC base=+0.077)

- **PATRÓN** `sigma_h` < `0.0083` → IC=+0.122 (n=88)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0083 (IC base=+0.038)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0275` → IC=+0.209 (n=307)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0275 (IC base=+0.208)

- **PATRÓN** `sigma_h` > `0.0148` → IC=+0.244 (n=205)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0148 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.231 (n=117)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` > `0.2339` → IC=+0.265 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2339 (IC base=+0.208)

- **PATRÓN** `dist_vwap_pct` < `0.0994` → IC=+0.211 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0994 (IC base=+0.208)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.899` → IC=+0.292 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.899 (IC base=+0.208)

- **PATRÓN** `sigma_h` < `0.0123` → IC=+0.219 (n=226)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0123 (IC base=+0.216)

- **PATRÓN** `sigma_h` > `0.0167` → IC=+0.235 (n=153)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0167 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.248 (n=113)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.216)

- **PATRÓN** `dist_vwap_pct` < `0.5367` → IC=+0.213 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5367 (IC base=+0.216)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.122` → IC=+0.225 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.122 (IC base=+0.216)

### GBM_LATE_60M
- **FILTRO** `dist_vwap_pct` < `0.129` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` < 0.129
  - _Potencial_: sin este filtro IC_bueno=-0.033 (n=13)

- **FILTRO** `sigma_ewma_delta_pct` < `14.597` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 14.597
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=4)

- **FILTRO** `sigma_h` > `0.0133` → IC=-0.300 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=118)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.272 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=44)

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.144 (n=57)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0053 (IC base=-0.015)

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
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=68)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.125 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 11.0 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.505 (IC base=+0.075)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **FILTRO** `py_entrada` > `0.505` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=68)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.125 (n=46)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 11.0 (IC base=+0.075)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.129 (n=68)

  - _Acción_: Kelly boost +0.64€ cuando `py_entrada` < 0.505 (IC base=+0.075)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=101)

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
- **FILTRO** `sigma_ewma_delta_pct` > `17.588` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.588
  - _Potencial_: sin este filtro IC_bueno=+0.124 (n=285)

- **PATRÓN** `ibs_15` > `0.737` → IC=+0.190 (n=304)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.95€ cuando `ibs_15` > 0.737 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.133` → IC=+0.146 (n=145)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.133 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` < `0.5084` → IC=+0.141 (n=210)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.5084 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `23.684` → IC=+0.136 (n=31)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` > 23.684 (IC base=+0.033)

- **PATRÓN** `ibs_15` < `0.0263` → IC=+0.120 (n=177)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.60€ cuando `ibs_15` < 0.0263 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` > `0.8904` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.8904 (IC base=+0.058)

- **PATRÓN** `sigma_ewma_delta_pct` < `17.588` → IC=+0.124 (n=285)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 17.588 (IC base=+0.058)

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

- **PATRÓN** `drift_60min` |x|≤ `0.2359` → IC=+0.120 (n=222)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.60€ cuando `drift_60min` |x|≤ 0.2359 (IC base=+0.074)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.143 (n=169)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 12.0 (IC base=+0.074)

- **PATRÓN** `ibs_15` > `0.6374` → IC=+0.186 (n=183)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.93€ cuando `ibs_15` > 0.6374 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.8291` → IC=+0.242 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8291 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.498` → IC=+0.179 (n=54)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 5.498 (IC base=+0.074)

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
- **FILTRO** `sigma_ewma_delta_pct` < `22.327` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 22.327
  - _Potencial_: sin este filtro IC_bueno=+0.278 (n=16)

- **FILTRO** `sigma_ewma_delta_pct` > `21.947` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 21.947
  - _Potencial_: sin este filtro IC_bueno=+0.109 (n=126)

- **PATRÓN** `ibs_15` > `0.7721` → IC=+0.200 (n=98)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7721 (IC base=+0.030)

- **PATRÓN** `dist_vwap_pct` < `0.5087` → IC=+0.149 (n=92)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.5087 (IC base=+0.030)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.327` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 22.327 (IC base=+0.030)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.126 (n=129)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0061 (IC base=+0.054)

- **PATRÓN** `dist_vwap_pct` > `0.9454` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.9454 (IC base=+0.054)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.993` → IC=+0.121 (n=114)

  - _Acción_: Kelly boost +0.60€ cuando `sigma_ewma_delta_pct` < 11.993 (IC base=+0.054)

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
  - _Potencial_: sin este filtro IC_bueno=+0.162 (n=66)

- **PATRÓN** `sigma_h` < `0.0139` → IC=+0.172 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0139 (IC base=+0.132)

- **PATRÓN** `drift_60min` |x|≤ `0.1743` → IC=+0.154 (n=24)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.77€ cuando `drift_60min` |x|≤ 0.1743 (IC base=+0.132)

- **PATRÓN** `drift_15min` |x|≤ `1.1387` → IC=+0.147 (n=66)

  - _Acción_: Kelly boost +0.74€ cuando `drift_15min` |x|≤ 1.1387 (IC base=+0.132)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1253` → IC=+0.152 (n=44)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.76€ cuando `delta_ratio_macro` |x|> 0.1253 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.162 (n=66)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 4.0 (IC base=+0.132)

- **PATRÓN** `ibs_15` < `0.0769` → IC=+0.172 (n=56)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.86€ cuando `ibs_15` < 0.0769 (IC base=+0.132)

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
- **H-IBS-UPDOWN_GBM#15min**: IBS > 0.737 correlaciona con éxito en UPDOWN_GBM#15min (IC=+0.190 n=304). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#BTC#15min**: IBS > 0.6374 correlaciona con éxito en UPDOWN_GBM#BTC#15min (IC=+0.186 n=183). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#ETH#15min**: IBS > 0.7721 correlaciona con éxito en UPDOWN_GBM#ETH#15min (IC=+0.200 n=98). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#XRP#15min**: IBS < 0.0769 correlaciona con éxito en UPDOWN_GBM#XRP#15min (IC=+0.172 n=56). Confirma señal de reversión media → alinear con BUY_YES.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min` — IC=+0.325 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH` — IC=+0.325 n=38. Faltan ~2 resoluciones para umbral n≥40. ETA: ~1h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_TARDIO#DOGE#15min` — IC=+0.263 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_TARDIO#DOGE` — IC=+0.263 n=36. Faltan ~4 resoluciones para umbral n≥40. ETA: ~3h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 275 | +0.146 | +18.19€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 275 | +0.146 | +18.19€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 116 | +0.170 | +9.87€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 116 | +0.170 | +9.87€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 99 | +0.144 | +4.51€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 99 | +0.144 | +4.51€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 60 | +0.097 | +3.81€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 60 | +0.097 | +3.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 3694 | +0.185 | +54.34€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 2397 | +0.219 | +99.43€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 157 | +0.079 | +5.69€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 510 | +0.102 | -74.41€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 630 | +0.150 | +23.63€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 1071 | +0.193 | +32.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 799 | +0.210 | +3.61€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 52 | +0.111 | +6.08€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 210 | +0.165 | +26.16€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#ETH | 1311 | +0.180 | +19.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 793 | +0.223 | +50.73€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 52 | -0.018 | -9.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 256 | +0.108 | -33.10€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 210 | +0.151 | +11.82€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#SOL | 1296 | +0.184 | +0.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 793 | +0.225 | +47.66€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 53 | +0.136 | +9.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 240 | +0.103 | -41.90€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 210 | +0.132 | -14.35€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 16 | +0.133 | +1.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 12 | +0.043 | -2.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 137 | +0.313 | +6.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 137 | +0.313 | +6.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 137 | +0.313 | +6.13€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 137 | +0.313 | +6.13€ | 0 | 0 |
| ✅ GBM_LATE_15M | 5734 | +0.106 | +1915.30€ | 0 | 9 |
| ✅ GBM_LATE_15M#15min | 5734 | +0.106 | +1915.30€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 1365 | +0.077 | +247.87€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1365 | +0.077 | +247.87€ | 0 | 6 |
| ✅ GBM_LATE_15M#ETH | 1318 | +0.080 | +250.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1318 | +0.080 | +250.09€ | 0 | 6 |
| ✅ GBM_LATE_15M#SOL | 1552 | +0.099 | +600.55€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1552 | +0.099 | +600.55€ | 1 | 5 |
| ✅ GBM_LATE_15M#XRP | 1499 | +0.162 | +816.78€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1499 | +0.162 | +816.78€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 2965 | +0.153 | +1764.93€ | 0 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 2965 | +0.153 | +1764.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 756 | +0.116 | +354.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 756 | +0.116 | +354.64€ | 0 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 780 | +0.119 | +368.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 780 | +0.119 | +368.24€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 761 | +0.113 | +336.69€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 761 | +0.113 | +336.69€ | 1 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 668 | +0.278 | +705.36€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 668 | +0.278 | +705.36€ | 0 | 12 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 166 | +0.161 | +91.95€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 166 | +0.161 | +91.95€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC | 9 | -0.102 | -1.94€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 9 | -0.102 | -1.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 28 | +0.100 | +3.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 28 | +0.100 | +3.65€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL | 8 | -0.120 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 8 | -0.120 | -1.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 121 | +0.240 | +92.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 121 | +0.240 | +92.15€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 2910 | +0.101 | +1010.72€ | 0 | 11 |
| ✅ GBM_LATE_15M_TARDIO#15min | 2910 | +0.101 | +1010.72€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 698 | +0.073 | +148.31€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 698 | +0.073 | +148.31€ | 0 | 7 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 701 | +0.041 | +69.90€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 701 | +0.041 | +69.90€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 654 | +0.047 | +124.41€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 654 | +0.047 | +124.41€ | 1 | 5 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 857 | +0.212 | +668.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 857 | +0.212 | +668.10€ | 0 | 11 |
| ✅ GBM_LATE_5M | 89 | +0.071 | +4.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#5min | 89 | +0.071 | +4.71€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 7 | +0.058 | -0.06€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 7 | +0.058 | -0.06€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 10 | +0.042 | -0.90€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 10 | +0.042 | -0.90€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL | 19 | -0.158 | -3.31€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 19 | -0.158 | -3.31€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 53 | +0.136 | +8.98€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 53 | +0.136 | +8.98€ | 0 | 0 |
| ✅ GBM_LATE_60M | 327 | -0.114 | +6.13€ | 4 | 1 |
| ✅ GBM_LATE_60M#60min | 327 | -0.114 | +6.13€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 114 | -0.035 | +5.51€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 114 | -0.035 | +5.51€ | 4 | 1 |
| ✅ GBM_LATE_60M#ETH | 103 | -0.157 | -10.66€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 103 | -0.157 | -10.66€ | 4 | 0 |
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
| ✅ LEADLAG_BTC_XRP_15M | 188 | +0.037 | +13.87€ | 1 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 188 | +0.037 | +13.87€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 188 | +0.037 | +13.87€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 188 | +0.037 | +13.87€ | 1 | 2 |
| ✅ ORDER_FLOW_5M | 1631 | +0.013 | +13.70€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1495 | +0.008 | +1.11€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 202 | +0.044 | +6.33€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 202 | +0.044 | +6.33€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 2 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 218 | +0.000 | -2.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 218 | +0.000 | -2.14€ | 2 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 261 | -0.021 | -8.99€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 261 | -0.021 | -8.99€ | 0 | 0 |
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
| ✅ UPDOWN_GBM | 1812 | +0.020 | +129.81€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1552 | +0.046 | +167.87€ | 1 | 7 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 127 | -0.058 | -10.76€ | 7 | 0 |
| ✅ UPDOWN_GBM#BNB | 129 | +0.065 | +30.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 129 | +0.065 | +30.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 460 | +0.026 | +30.26€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 377 | +0.062 | +44.23€ | 1 | 7 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 42 | -0.068 | -6.16€ | 2 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 86 | +0.057 | +10.56€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 83 | +0.065 | +11.46€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 832 | +0.026 | +46.61€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 739 | +0.043 | +57.67€ | 2 | 6 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 54 | -0.018 | -2.56€ | 3 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 172 | -0.092 | -16.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 104 | -0.066 | -9.62€ | 9 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 31 | -0.106 | -2.03€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 131 | +0.049 | +30.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 120 | +0.074 | +33.53€ | 5 | 6 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 58 | +0.283 | +11.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 58 | +0.283 | +11.17€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 20 | +0.182 | -1.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 20 | +0.182 | -1.31€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 38 | +0.325 | +12.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 38 | +0.325 | +12.47€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 582 | +0.185 | +264.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 582 | +0.185 | +264.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 48 | +0.180 | +18.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 48 | +0.180 | +18.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 68 | +0.086 | +9.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 68 | +0.086 | +9.01€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 36 | +0.263 | +21.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 36 | +0.263 | +21.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 143 | +0.197 | +55.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 143 | +0.197 | +55.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 145 | +0.153 | +61.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 145 | +0.153 | +61.56€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 142 | +0.222 | +99.62€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 142 | +0.222 | +99.62€ | 0 | 0 |
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