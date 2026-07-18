# Hipótesis automáticas — 2026-07-18 18:29 UTC
_Generado por shadow_postmortem.py sobre 21054 resoluciones (PNL=+5006.54€)_

## Patrones causales activos

### FAVORITO_CONFIRMADO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.188 (n=1162)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 8.0 (IC base=+0.188)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.204 (n=1318)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.188)

- **PATRÓN** `py_entrada` > `0.695` → IC=+0.299 (n=574)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.695 (IC base=+0.188)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.193 (n=1467)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.188)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.196 (n=498)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 17.0 (IC base=+0.177)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.221 (n=506)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.177)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.345 (n=469)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.177)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.183 (n=1548)

  - _Acción_: Kelly boost +0.92€ cuando `libro_spread` < 0.01 (IC base=+0.177)

- **PATRÓN** `libro_liquidez` > `7392.3738` → IC=+0.180 (n=454)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 7392.3738 (IC base=+0.177)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.214 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.229 (n=245)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` > `0.615` → IC=+0.269 (n=253)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.615 (IC base=+0.209)

- **PATRÓN** `libro_liquidez` > `11621.3688` → IC=+0.213 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11621.3688 (IC base=+0.209)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.218 (n=115)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.207)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.243 (n=204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.387 (n=104)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.207)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.181 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 6.0 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `19.0` → IC=+0.250 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 19.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` < `0.565` → IC=+0.263 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.565 (IC base=+0.184)

- **PATRÓN** `libro_liquidez` > `8840.0271` → IC=+0.231 (n=24)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8840.0271 (IC base=+0.184)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.224 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.167)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.293 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.237 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.405 (IC base=+0.167)

- **PATRÓN** `libro_liquidez` > `6436.3724` → IC=+0.183 (n=80)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 6436.3724 (IC base=+0.167)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.232 (n=255)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.221)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.236 (n=290)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.221)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.347 (n=129)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.221)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.223 (n=352)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.221)

- **PATRÓN** `libro_liquidez` > `3151.1844` → IC=+0.223 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3151.1844 (IC base=+0.221)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.223 (n=110)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.213)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.231 (n=206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.213)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.379 (n=105)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.213)

- **PATRÓN** `libro_liquidez` > `6768.1568` → IC=+0.217 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6768.1568 (IC base=+0.213)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.212 (n=64)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.286 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.575 (IC base=+0.153)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.179 (n=76)

  - _Acción_: Kelly boost +0.90€ cuando `libro_spread` < 0.01 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `6015.6895` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `libro_liquidez` > 6015.6895 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.219 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.208 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.405 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `3899.2794` → IC=+0.183 (n=80)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 3899.2794 (IC base=+0.148)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.242 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.229)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.248 (n=101)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.229)

- **PATRÓN** `py_entrada` > `0.665` → IC=+0.299 (n=197)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.665 (IC base=+0.229)

- **PATRÓN** `libro_liquidez` > `1584.7176` → IC=+0.230 (n=276)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1584.7176 (IC base=+0.229)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.229 (n=142)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.254 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.217)

- **PATRÓN** `py_entrada` < `0.395` → IC=+0.266 (n=289)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.395 (IC base=+0.217)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `16.0` → IC=+0.194 (n=34)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` > 16.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.66` → IC=+0.199 (n=71)

  - _Acción_: Kelly boost +0.99€ cuando `py_entrada` < 0.66 (IC base=+0.181)

- **PATRÓN** `py_entrada` > `0.575` → IC=+0.181 (n=70)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.575 (IC base=+0.181)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.125 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 7.0 (IC base=+0.087)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.087)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.125 (n=1760)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 8.0 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.7373` → IC=+0.146 (n=128)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.7373 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.463` → IC=+0.198 (n=286)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 6.463 (IC base=+0.113)

- **PATRÓN** `sigma_h` > `0.0089` → IC=+0.129 (n=1413)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` > 0.0089 (IC base=+0.111)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.133 (n=1533)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 12.0 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.1627` → IC=+0.123 (n=322)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.1627 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` < `0.9211` → IC=+0.121 (n=1034)

  - _Acción_: Kelly boost +0.60€ cuando `dist_vwap_pct` < 0.9211 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.189` → IC=+0.138 (n=219)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 6.189 (IC base=+0.111)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.4306` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 0.4306 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.154` → IC=+0.243 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.154 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.1355` → IC=+0.138 (n=56)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` > 0.1355 (IC base=+0.072)

- **PATRÓN** `dist_vwap_pct` < `0.4825` → IC=+0.128 (n=216)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.4825 (IC base=+0.072)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.845` → IC=+0.184 (n=93)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 2.845 (IC base=+0.072)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.172 (n=135)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0045 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.8385` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.8385 (IC base=+0.097)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.476` → IC=+0.214 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.476 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.6698` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.6698 (IC base=+0.075)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.618` → IC=+0.236 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.618 (IC base=+0.075)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `8.125` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.125
  - _Potencial_: sin este filtro IC_bueno=+0.099 (n=235)

- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.121 (n=249)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0103 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.147 (n=188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 18.0 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.298` → IC=+0.204 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.298 (IC base=+0.103)

- **PATRÓN** `sigma_h` < `0.013` → IC=+0.142 (n=464)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.013 (IC base=+0.124)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.126 (n=525)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` > 0.0091 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.180 (n=204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 6.0 (IC base=+0.124)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_h` < `0.0287` → IC=+0.149 (n=533)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0287 (IC base=+0.149)

- **PATRÓN** `sigma_h` > `0.0221` → IC=+0.184 (n=242)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` > 0.0221 (IC base=+0.149)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.152 (n=538)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 6.0 (IC base=+0.149)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.155 (n=482)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 15.0 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` > `0.5822` → IC=+0.244 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5822 (IC base=+0.149)

- **PATRÓN** `dist_vwap_pct` < `0.1141` → IC=+0.148 (n=197)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1141 (IC base=+0.149)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.431` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.431 (IC base=+0.149)

- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.192 (n=186)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0101 (IC base=+0.170)

- **PATRÓN** `sigma_h` > `0.0261` → IC=+0.207 (n=186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0261 (IC base=+0.170)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.226 (n=206)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` > `0.3062` → IC=+0.171 (n=77)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.3062 (IC base=+0.170)

- **PATRÓN** `dist_vwap_pct` < `0.6049` → IC=+0.161 (n=299)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` < 0.6049 (IC base=+0.170)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.722` → IC=+0.168 (n=266)

  - _Acción_: Kelly boost +0.84€ cuando `sigma_ewma_delta_pct` < 7.722 (IC base=+0.170)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0118` → IC=+0.236 (n=339)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0118 (IC base=+0.163)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.181 (n=725)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 12.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.163 (n=1067)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 18.0 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.5839` → IC=+0.213 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5839 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.061` → IC=+0.296 (n=145)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.061 (IC base=+0.163)

- **PATRÓN** `sigma_h` > `0.0046` → IC=+0.187 (n=994)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` > 0.0046 (IC base=+0.168)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.182 (n=482)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.168)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.194 (n=334)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 5.0 (IC base=+0.168)

- **PATRÓN** `dist_vwap_pct` < `0.8862` → IC=+0.186 (n=902)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` < 0.8862 (IC base=+0.168)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.064` → IC=+0.232 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.064 (IC base=+0.168)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `sigma_h` > `0.003` → IC=+0.150 (n=215)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` > 0.003 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.165 (n=174)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 12.0 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.4991` → IC=+0.210 (n=29)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4991 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.905` → IC=+0.229 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.905 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.139 (n=253)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0062 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.0031` → IC=+0.171 (n=226)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0031 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.180 (n=123)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.116` → IC=+0.156 (n=59)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.116 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.4453` → IC=+0.133 (n=224)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.4453 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.151` → IC=+0.230 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.151 (IC base=+0.136)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.264 (n=87)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.170 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 12.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.167 (n=124)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 8.0 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.1556` → IC=+0.173 (n=99)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.1556 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.551` → IC=+0.267 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.551 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.135 (n=228)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.0067 (IC base=+0.124)

- **PATRÓN** `sigma_h` > `0.0036` → IC=+0.136 (n=259)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0036 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.153 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 17.0 (IC base=+0.124)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.167 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 6.0 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.6273` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.6273 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` < `0.2447` → IC=+0.139 (n=178)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.2447 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.618` → IC=+0.246 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.618 (IC base=+0.124)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `2.606` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.606
  - _Potencial_: sin este filtro IC_bueno=+0.175 (n=158)

- **PATRÓN** `sigma_h` > `0.0137` → IC=+0.198 (n=94)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0137 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.160 (n=201)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 12.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.143 (n=96)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 6.0 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `0.6202` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.6202 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.625` → IC=+0.280 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.625 (IC base=+0.133)

- **PATRÓN** `sigma_h` < `0.0123` → IC=+0.146 (n=244)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0123 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.171 (n=83)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 5.0 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.8313` → IC=+0.157 (n=202)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 0.8313 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.606` → IC=+0.175 (n=158)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` < 2.606 (IC base=+0.114)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` < `0.0173` → IC=+0.259 (n=230)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0173 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.267 (n=230)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0092 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.252 (n=216)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.277 (n=204)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `dist_vwap_pct` > `0.6722` → IC=+0.328 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6722 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.563` → IC=+0.371 (n=60)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.563 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.319 (n=241)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.301)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.311 (n=252)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.301)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.303 (n=221)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.301)

- **PATRÓN** `dist_vwap_pct` > `0.1789` → IC=+0.333 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1789 (IC base=+0.301)

- **PATRÓN** `dist_vwap_pct` < `0.6163` → IC=+0.317 (n=238)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.6163 (IC base=+0.301)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.494` → IC=+0.320 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 5.494 (IC base=+0.301)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.014` → IC=+0.203 (n=308)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.014 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.134 (n=845)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 8.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.134 (n=821)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` < 15.0 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` > `0.5183` → IC=+0.195 (n=165)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.5183 (IC base=+0.128)

- **PATRÓN** `dist_vwap_pct` < `0.1169` → IC=+0.152 (n=475)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1169 (IC base=+0.128)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.43` → IC=+0.282 (n=122)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.43 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.127 (n=387)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 6.0 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.7927` → IC=+0.129 (n=895)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` < 0.7927 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.972` → IC=+0.123 (n=786)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` < 10.972 (IC base=+0.105)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.143 (n=141)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` < 0.0045 (IC base=+0.111)

- **PATRÓN** `sigma_h` > `0.0029` → IC=+0.121 (n=212)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` > 0.0029 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.155 (n=192)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 8.0 (IC base=+0.111)

- **PATRÓN** `dist_vwap_pct` > `0.4428` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.4428 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.045` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.045 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0067` → IC=+0.120 (n=256)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0067 (IC base=+0.079)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.129 (n=95)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 16.0 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` > `2.888` → IC=+0.146 (n=94)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 2.888 (IC base=+0.079)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.179 (n=79)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` < 0.0039 (IC base=+0.079)

- **PATRÓN** `dist_vwap_pct` < `0.272` → IC=+0.132 (n=123)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.272 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.068` → IC=+0.250 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.068 (IC base=+0.079)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.997` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 7.997 (IC base=+0.040)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `dist_vwap_pct` > `0.8066` → IC=-0.167 (n=19)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.8066
  - _Potencial_: sin este filtro IC_bueno=+0.077 (n=218)

- **FILTRO** `sigma_ewma_delta_pct` > `5.112` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 5.112
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=189)

- **PATRÓN** `sigma_h` > `0.0126` → IC=+0.144 (n=85)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.72€ cuando `sigma_h` > 0.0126 (IC base=+0.086)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.148 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 8.0 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` > `0.5019` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` > 0.5019 (IC base=+0.086)

- **PATRÓN** `dist_vwap_pct` < `0.1434` → IC=+0.144 (n=85)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.1434 (IC base=+0.086)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.146` → IC=+0.284 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.146 (IC base=+0.086)

- **PATRÓN** `sigma_h` < `0.009` → IC=+0.132 (n=112)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` < 0.009 (IC base=+0.044)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.121 (n=93)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` < 6.0 (IC base=+0.044)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0289` → IC=+0.206 (n=291)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0289 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.0113` → IC=+0.240 (n=260)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0113 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.225 (n=256)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.2297` → IC=+0.253 (n=83)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2297 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` < `0.0994` → IC=+0.207 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.0994 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.899` → IC=+0.273 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.899 (IC base=+0.204)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.236 (n=142)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0099 (IC base=+0.218)

- **PATRÓN** `sigma_h` > `0.0217` → IC=+0.241 (n=106)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0217 (IC base=+0.218)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.218 (n=289)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.218)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.237 (n=116)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.218)

- **PATRÓN** `dist_vwap_pct` < `0.5545` → IC=+0.221 (n=288)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5545 (IC base=+0.218)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.154` → IC=+0.229 (n=267)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 10.154 (IC base=+0.218)

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
- **FILTRO** `sigma_ewma_delta_pct` > `17.588` → IC=-0.155 (n=27)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 17.588
  - _Potencial_: sin este filtro IC_bueno=+0.136 (n=267)

- **PATRÓN** `ibs_15` > `0.734` → IC=+0.190 (n=295)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.95€ cuando `ibs_15` > 0.734 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` > `0.133` → IC=+0.159 (n=133)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.133 (IC base=+0.033)

- **PATRÓN** `dist_vwap_pct` < `0.2737` → IC=+0.141 (n=168)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.2737 (IC base=+0.033)

- **PATRÓN** `sigma_ewma_delta_pct` > `18.602` → IC=+0.167 (n=37)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 18.602 (IC base=+0.033)

- **PATRÓN** `ibs_15` < `0.0263` → IC=+0.129 (n=173)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.64€ cuando `ibs_15` < 0.0263 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.9263` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.9263 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` < `17.588` → IC=+0.136 (n=267)

  - _Acción_: Kelly boost +0.68€ cuando `sigma_ewma_delta_pct` < 17.588 (IC base=+0.061)

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

- **PATRÓN** `drift_60min` |x|≤ `0.1545` → IC=+0.132 (n=142)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.66€ cuando `drift_60min` |x|≤ 0.1545 (IC base=+0.074)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.148 (n=160)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 12.0 (IC base=+0.074)

- **PATRÓN** `ibs_15` > `0.6374` → IC=+0.182 (n=174)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` > 0.6374 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.7265` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7265 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` < `13.975` → IC=+0.161 (n=60)

  - _Acción_: Kelly boost +0.81€ cuando `sigma_ewma_delta_pct` < 13.975 (IC base=+0.074)

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
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=20)

- **FILTRO** `sigma_ewma_delta_pct` > `21.947` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 21.947
  - _Potencial_: sin este filtro IC_bueno=+0.098 (n=120)

- **PATRÓN** `ibs_15` > `0.7686` → IC=+0.207 (n=97)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7686 (IC base=+0.032)

- **PATRÓN** `dist_vwap_pct` < `0.5043` → IC=+0.141 (n=90)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` < 0.5043 (IC base=+0.032)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.506` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.506 (IC base=+0.032)

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
  - _Potencial_: sin este filtro IC_bueno=+0.188 (n=62)

- **PATRÓN** `sigma_h` < `0.0099` → IC=+0.250 (n=30)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0099 (IC base=+0.148)

- **PATRÓN** `drift_60min` |x|≤ `0.2258` → IC=+0.167 (n=28)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.83€ cuando `drift_60min` |x|≤ 0.2258 (IC base=+0.148)

- **PATRÓN** `drift_15min` |x|≤ `0.9428` → IC=+0.184 (n=55)

  - _Acción_: Kelly boost +0.92€ cuando `drift_15min` |x|≤ 0.9428 (IC base=+0.148)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1253` → IC=+0.159 (n=42)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.80€ cuando `delta_ratio_macro` |x|> 0.1253 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `4.0` → IC=+0.188 (n=62)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 4.0 (IC base=+0.148)

- **PATRÓN** `ibs_15` < `0.0769` → IC=+0.191 (n=53)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.95€ cuando `ibs_15` < 0.0769 (IC base=+0.148)

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
- **H-IBS-UPDOWN_GBM#15min**: IBS > 0.734 correlaciona con éxito en UPDOWN_GBM#15min (IC=+0.190 n=295). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#BTC#15min**: IBS > 0.6374 correlaciona con éxito en UPDOWN_GBM#BTC#15min (IC=+0.182 n=174). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#ETH#15min**: IBS > 0.7686 correlaciona con éxito en UPDOWN_GBM#ETH#15min (IC=+0.207 n=97). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#XRP#15min**: IBS < 0.0769 correlaciona con éxito en UPDOWN_GBM#XRP#15min (IC=+0.191 n=53). Confirma señal de reversión media → alinear con BUY_YES.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min` — IC=+0.329 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH` — IC=+0.329 n=33. Faltan ~7 resoluciones para umbral n≥40. ETA: ~5h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_TARDIO#DOGE#15min` — IC=+0.281 n=30. Faltan ~10 resoluciones para umbral n≥40. ETA: ~7h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_TARDIO#DOGE` — IC=+0.281 n=30. Faltan ~10 resoluciones para umbral n≥40. ETA: ~7h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 202 | +0.142 | +11.62€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 202 | +0.142 | +11.62€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 90 | +0.141 | +2.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 90 | +0.141 | +2.07€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 70 | +0.167 | +6.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 70 | +0.167 | +6.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 42 | +0.091 | +2.87€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 42 | +0.091 | +2.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 3491 | +0.182 | +17.89€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#15min | 2269 | +0.216 | +72.02€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 148 | +0.080 | +4.34€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 477 | +0.089 | -86.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 597 | +0.154 | +28.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 1014 | +0.193 | +29.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 756 | +0.208 | -2.07€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 49 | +0.108 | +5.06€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 199 | +0.177 | +29.95€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#ETH | 1243 | +0.175 | -0.39€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 752 | +0.217 | +34.40€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 49 | -0.010 | -8.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 243 | +0.100 | -36.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 199 | +0.152 | +10.89€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL | 1222 | +0.181 | -9.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 750 | +0.223 | +42.67€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 50 | +0.135 | +8.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 223 | +0.091 | -47.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 199 | +0.132 | -12.68€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 12 | +0.043 | -1.80€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 11 | +0.021 | -2.97€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 124 | +0.309 | +4.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 124 | +0.309 | +4.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 124 | +0.309 | +4.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 124 | +0.309 | +4.06€ | 0 | 0 |
| ✅ GBM_LATE_15M | 5591 | +0.105 | +1839.82€ | 0 | 8 |
| ✅ GBM_LATE_15M#15min | 5591 | +0.105 | +1839.82€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 1337 | +0.074 | +230.03€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1337 | +0.074 | +230.03€ | 0 | 5 |
| ✅ GBM_LATE_15M#ETH | 1293 | +0.078 | +245.48€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1293 | +0.078 | +245.48€ | 0 | 5 |
| ✅ GBM_LATE_15M#SOL | 1508 | +0.101 | +589.11€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1508 | +0.101 | +589.11€ | 1 | 6 |
| ✅ GBM_LATE_15M#XRP | 1453 | +0.160 | +775.20€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1453 | +0.160 | +775.20€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 2817 | +0.150 | +1662.25€ | 0 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 2817 | +0.150 | +1662.25€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 719 | +0.114 | +337.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 719 | +0.114 | +337.19€ | 0 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 741 | +0.116 | +351.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 741 | +0.116 | +351.57€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 731 | +0.110 | +313.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 731 | +0.110 | +313.29€ | 1 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 626 | +0.277 | +660.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 626 | +0.277 | +660.20€ | 0 | 12 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 163 | +0.161 | +93.39€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 163 | +0.161 | +93.39€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC | 9 | -0.102 | -1.94€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 9 | -0.102 | -1.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 26 | +0.071 | +3.05€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 26 | +0.071 | +3.05€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL | 8 | -0.120 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 8 | -0.120 | -1.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 120 | +0.246 | +94.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 120 | +0.246 | +94.19€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 2757 | +0.102 | +968.24€ | 0 | 9 |
| ✅ GBM_LATE_15M_TARDIO#15min | 2757 | +0.102 | +968.24€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 670 | +0.070 | +137.44€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 670 | +0.070 | +137.44€ | 0 | 8 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 664 | +0.037 | +66.23€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 664 | +0.037 | +66.23€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 612 | +0.059 | +133.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 612 | +0.059 | +133.85€ | 2 | 7 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 811 | +0.212 | +630.71€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 811 | +0.212 | +630.71€ | 0 | 12 |
| ✅ GBM_LATE_5M | 29 | +0.048 | +0.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#5min | 29 | +0.048 | +0.66€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 5 | +0.018 | -0.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 5 | +0.018 | -0.37€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL | 12 | -0.043 | -0.41€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 12 | -0.043 | -0.41€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 9 | +0.061 | +1.42€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 9 | +0.061 | +1.42€ | 0 | 0 |
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
| ✅ LEADLAG_BTC_XRP_15M | 179 | +0.052 | +17.61€ | 1 | 2 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 179 | +0.052 | +17.61€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 179 | +0.052 | +17.61€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 179 | +0.052 | +17.61€ | 1 | 2 |
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
| ✅ UPDOWN_GBM | 1776 | +0.021 | +132.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1516 | +0.047 | +170.82€ | 1 | 7 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 127 | -0.058 | -10.76€ | 7 | 0 |
| ✅ UPDOWN_GBM#BNB | 122 | +0.081 | +35.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 122 | +0.081 | +35.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 448 | +0.024 | +27.78€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 365 | +0.061 | +41.75€ | 1 | 7 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 42 | -0.068 | -6.16€ | 2 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 82 | +0.059 | +9.52€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 79 | +0.068 | +10.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 823 | +0.025 | +44.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 730 | +0.041 | +55.64€ | 2 | 5 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 54 | -0.018 | -2.56€ | 3 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 172 | -0.092 | -16.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 104 | -0.066 | -9.62€ | 9 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 31 | -0.106 | -2.03€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 127 | +0.058 | +33.79€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 116 | +0.085 | +37.08€ | 5 | 6 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 50 | +0.288 | +10.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 50 | +0.288 | +10.00€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 17 | +0.157 | -0.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 17 | +0.157 | -0.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 33 | +0.329 | +10.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 33 | +0.329 | +10.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 486 | +0.184 | +212.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 486 | +0.184 | +212.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 40 | +0.191 | +15.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 40 | +0.191 | +15.70€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 55 | +0.079 | +7.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 55 | +0.079 | +7.69€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 30 | +0.281 | +19.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 30 | +0.281 | +19.55€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 122 | +0.210 | +48.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 122 | +0.210 | +48.27€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 126 | +0.133 | +45.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 126 | +0.133 | +45.79€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 113 | +0.222 | +75.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 113 | +0.222 | +75.75€ | 0 | 0 |
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