# Hipótesis automáticas — 2026-07-15 10:08 UTC
_Generado por shadow_postmortem.py sobre 15149 resoluciones (PNL=+2952.55€)_

## Patrones causales activos

### FAVORITO_CONFIRMADO
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.210 (n=260)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.208 (n=255)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.695` → IC=+0.315 (n=343)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.695 (IC base=+0.192)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.196 (n=867)

  - _Acción_: Kelly boost +0.98€ cuando `libro_spread` < 0.01 (IC base=+0.192)

- **PATRÓN** `libro_liquidez` > `4390.8559` → IC=+0.195 (n=489)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 4390.8559 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.179 (n=328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 17.0 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.202 (n=317)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.163)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.318 (n=283)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.163)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=960)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.163)

- **PATRÓN** `libro_liquidez` > `7292.9528` → IC=+0.184 (n=280)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 7292.9528 (IC base=+0.163)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.210 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.192)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.212 (n=57)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.192)

- **PATRÓN** `py_entrada` > `0.615` → IC=+0.247 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.615 (IC base=+0.192)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.212 (n=71)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.191)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.218 (n=129)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.191)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.384 (n=67)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.191)

- **PATRÓN** `libro_liquidez` > `7240.499` → IC=+0.201 (n=162)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7240.499 (IC base=+0.191)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` < `12.0` → IC=+0.233 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.605` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.605 (IC base=+0.179)

- **PATRÓN** `libro_liquidez` > `6926.0677` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6926.0677 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.289 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.425` → IC=+0.235 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.425 (IC base=+0.172)

- **PATRÓN** `py_entrada` > `0.395` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `py_entrada` > 0.395 (IC base=+0.172)

- **PATRÓN** `libro_liquidez` > `7066.4098` → IC=+0.217 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7066.4098 (IC base=+0.172)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.240 (n=144)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.235 (n=168)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.350 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.230)

- **PATRÓN** `libro_liquidez` > `5171.5093` → IC=+0.247 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 5171.5093 (IC base=+0.230)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.214 (n=180)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.208)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.354 (n=80)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.208)

- **PATRÓN** `libro_liquidez` > `4675.0354` → IC=+0.214 (n=117)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 4675.0354 (IC base=+0.208)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` < `16.0` → IC=+0.295 (n=37)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 16.0 (IC base=+0.241)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.575 (IC base=+0.241)

- **PATRÓN** `py_entrada` > `0.595` → IC=+0.235 (n=32)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.595 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.132 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 17.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.262 (n=19)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.131)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.131)

- **PATRÓN** `libro_liquidez` > `4743.0687` → IC=+0.180 (n=48)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 4743.0687 (IC base=+0.131)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.267 (n=58)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.226)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.326 (n=107)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.226)

- **PATRÓN** `libro_liquidez` > `1636.4687` → IC=+0.231 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1636.4687 (IC base=+0.226)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.214 (n=82)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 16.0 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.216 (n=79)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.193)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.250 (n=158)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.193)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `17.0` → IC=+0.184 (n=17)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 17.0 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.289 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.186)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.575 (IC base=+0.186)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.143 (n=26)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` < 7.0 (IC base=+0.083)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.083)

### GBM_LATE_15M
- **PATRÓN** `sigma_ewma_delta_pct` > `9.358` → IC=+0.214 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.358 (IC base=+0.105)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.135 (n=1161)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0091 (IC base=+0.105)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.124 (n=1163)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 11.0 (IC base=+0.105)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.3124` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.3124 (IC base=+0.078)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.176` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 13.176 (IC base=+0.078)

- **PATRÓN** `dist_vwap_pct` > `0.2044` → IC=+0.133 (n=28)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.2044 (IC base=+0.061)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.004` → IC=+0.188 (n=46)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` > 3.004 (IC base=+0.061)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `sigma_ewma_delta_pct` < `5.943` → IC=-0.139 (n=34)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 5.943
  - _Potencial_: sin este filtro IC_bueno=+0.244 (n=37)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.146 (n=125)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0045 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.6749` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.6749 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.943` → IC=+0.244 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.943 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.7215` → IC=+0.167 (n=31)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.7215 (IC base=+0.062)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `6.245` → IC=-0.125 (n=22)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.245
  - _Potencial_: sin este filtro IC_bueno=+0.097 (n=112)

- **PATRÓN** `sigma_h` < `0.0109` → IC=+0.147 (n=199)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0109 (IC base=+0.110)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.141 (n=207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 16.0 (IC base=+0.110)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.034` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.034 (IC base=+0.110)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.143 (n=292)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0115 (IC base=+0.131)

- **PATRÓN** `sigma_h` > `0.0093` → IC=+0.136 (n=438)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.68€ cuando `sigma_h` > 0.0093 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.182 (n=199)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` < 7.0 (IC base=+0.131)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_h` < `0.0297` → IC=+0.139 (n=414)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0297 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0225` → IC=+0.168 (n=188)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` > 0.0225 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.145 (n=435)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 5.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.151 (n=290)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` < 11.0 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.6733` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.6733 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.893` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 7.893 (IC base=+0.138)

- **PATRÓN** `sigma_h` > `0.0262` → IC=+0.203 (n=146)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0262 (IC base=+0.164)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.242 (n=161)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.164)

- **PATRÓN** `dist_vwap_pct` < `0.9797` → IC=+0.136 (n=149)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.9797 (IC base=+0.164)

- **PATRÓN** `sigma_ewma_delta_pct` < `6.147` → IC=+0.128 (n=119)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 6.147 (IC base=+0.164)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.012` → IC=+0.227 (n=214)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.012 (IC base=+0.158)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.175 (n=451)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 12.0 (IC base=+0.158)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.162 (n=670)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 18.0 (IC base=+0.158)

- **PATRÓN** `dist_vwap_pct` > `1.0657` → IC=+0.232 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 1.0657 (IC base=+0.158)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.023` → IC=+0.308 (n=71)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.023 (IC base=+0.158)

- **PATRÓN** `sigma_h` > `0.0047` → IC=+0.181 (n=666)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` > 0.0047 (IC base=+0.161)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.170 (n=322)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` > 15.0 (IC base=+0.161)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.189 (n=233)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 5.0 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` > `1.0476` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 1.0476 (IC base=+0.161)

- **PATRÓN** `dist_vwap_pct` < `0.1883` → IC=+0.203 (n=392)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.1883 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.996` → IC=+0.217 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.996 (IC base=+0.161)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.13` → IC=+0.178 (n=327)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 3.13 (IC base=+0.161)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `sigma_h` < `0.0064` → IC=+0.127 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.64€ cuando `sigma_h` < 0.0064 (IC base=+0.124)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.158 (n=159)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0027 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.185 (n=109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 12.0 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.1391` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.1391 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.074` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.074 (IC base=+0.124)

- **PATRÓN** `sigma_h` > `0.0027` → IC=+0.180 (n=170)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0027 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.179 (n=79)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` > 15.0 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.1967` → IC=+0.138 (n=114)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1967 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.18` → IC=+0.278 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.18 (IC base=+0.140)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.212 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0067 (IC base=+0.138)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.164 (n=117)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 12.0 (IC base=+0.138)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.154 (n=180)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 18.0 (IC base=+0.138)

- **PATRÓN** `dist_vwap_pct` > `0.6749` → IC=+0.233 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6749 (IC base=+0.138)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.752` → IC=+0.382 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.752 (IC base=+0.138)

- **PATRÓN** `sigma_h` < `0.0066` → IC=+0.129 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` < 0.0066 (IC base=+0.126)

- **PATRÓN** `sigma_h` > `0.0042` → IC=+0.147 (n=151)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0042 (IC base=+0.126)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.167 (n=85)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 15.0 (IC base=+0.126)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.172 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 5.0 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` > `0.7422` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.7422 (IC base=+0.126)

- **PATRÓN** `dist_vwap_pct` < `0.4151` → IC=+0.153 (n=93)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.4151 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.42` → IC=+0.175 (n=38)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 5.42 (IC base=+0.126)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.121` → IC=+0.156 (n=94)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 10.121 (IC base=+0.126)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `3.243` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.243
  - _Potencial_: sin este filtro IC_bueno=+0.170 (n=89)

- **PATRÓN** `sigma_h` > `0.0127` → IC=+0.216 (n=79)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0127 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.145 (n=164)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 8.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.139 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 6.0 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.4883` → IC=+0.194 (n=47)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.4883 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `1.1149` → IC=+0.132 (n=123)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 1.1149 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.566` → IC=+0.238 (n=59)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.566 (IC base=+0.131)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.188 (n=62)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0082 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.157 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 5.0 (IC base=+0.102)

- **PATRÓN** `dist_vwap_pct` < `0.2503` → IC=+0.183 (n=99)

  - _Acción_: Kelly boost +0.92€ cuando `dist_vwap_pct` < 0.2503 (IC base=+0.102)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.243` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 3.243 (IC base=+0.102)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` < `0.0179` → IC=+0.261 (n=140)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0179 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.0101` → IC=+0.254 (n=140)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0101 (IC base=+0.250)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.248 (n=129)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.250)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.291 (n=127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.250)

- **PATRÓN** `dist_vwap_pct` > `0.8165` → IC=+0.342 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.8165 (IC base=+0.250)

- **PATRÓN** `dist_vwap_pct` < `0.3705` → IC=+0.247 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3705 (IC base=+0.250)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.099` → IC=+0.318 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.099 (IC base=+0.250)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.337 (n=145)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.295)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.292 (n=99)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.295)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.312 (n=131)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.295)

- **PATRÓN** `dist_vwap_pct` < `0.3589` → IC=+0.323 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.3589 (IC base=+0.295)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.352` → IC=+0.321 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.352 (IC base=+0.295)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0145` → IC=+0.160 (n=195)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0145 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.131 (n=201)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 5.0 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.6728` → IC=+0.174 (n=87)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.6728 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.39` → IC=+0.314 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.39 (IC base=+0.099)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.134 (n=121)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 7.0 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.3646` → IC=+0.150 (n=18)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.3646 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.702` → IC=+0.214 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.702 (IC base=+0.085)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0043` → IC=+0.127 (n=65)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0043 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.6019` → IC=+0.157 (n=33)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.6019 (IC base=+0.041)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.728` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.728 (IC base=+0.041)

- **PATRÓN** `dist_vwap_pct` > `0.7397` → IC=+0.121 (n=27)

  - _Acción_: Kelly boost +0.60€ cuando `dist_vwap_pct` > 0.7397 (IC base=-0.006)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` < `7.064` → IC=-0.184 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 7.064
  - _Potencial_: sin este filtro IC_bueno=+0.342 (n=36)

- **FILTRO** `sigma_ewma_delta_pct` > `2.471` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.471
  - _Potencial_: sin este filtro IC_bueno=+0.059 (n=91)

- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.132 (n=66)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0134 (IC base=+0.069)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.149 (n=72)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 8.0 (IC base=+0.069)

- **PATRÓN** `dist_vwap_pct` > `0.5711` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.5711 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.064` → IC=+0.342 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.064 (IC base=+0.069)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.129 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 6.0 (IC base=+0.031)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0324` → IC=+0.189 (n=165)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.94€ cuando `sigma_h` < 0.0324 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0172` → IC=+0.196 (n=110)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` > 0.0172 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.232 (n=110)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` > `0.1821` → IC=+0.214 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1821 (IC base=+0.183)

- **PATRÓN** `dist_vwap_pct` < `1.4896` → IC=+0.170 (n=89)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` < 1.4896 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.253` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.253 (IC base=+0.183)

- **PATRÓN** `sigma_ewma_delta_pct` < `11.141` → IC=+0.157 (n=65)

  - _Acción_: Kelly boost +0.78€ cuando `sigma_ewma_delta_pct` < 11.141 (IC base=+0.183)

- **PATRÓN** `sigma_h` > `0.0173` → IC=+0.219 (n=94)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0173 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.247 (n=73)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.5109` → IC=+0.182 (n=146)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` < 0.5109 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.652` → IC=+0.190 (n=111)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.652 (IC base=+0.193)

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
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.219 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.5 (IC base=+0.172)

- **PATRÓN** `btc_momentum` |x|≤ `0.03` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `btc_momentum` |x|≤ 0.03 (IC base=+0.172)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.219 (n=30)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.172)

- **PATRÓN** `py_entrada` < `0.5` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.5 (IC base=+0.172)

- **PATRÓN** `btc_momentum` |x|≤ `0.03` → IC=+0.211 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `btc_momentum` |x|≤ 0.03 (IC base=+0.172)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=74)

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

- **FILTRO** `sigma_h` > `0.0055` → IC=-0.361 (n=70)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=+0.231 (n=24)

- **FILTRO** `T_h` < `144.7669` → IC=-0.432 (n=42)

  - _Acción_: SKIP cuando `T_h` < 144.7669
  - _Potencial_: sin este filtro IC_bueno=-0.292 (n=22)

- **FILTRO** `pct_vs_K` |x|> `2.6988` → IC=-0.480 (n=47)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6988
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.231 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=-0.208)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0076` → IC=-0.429 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0076
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

- **FILTRO** `T_h` > `98.7549` → IC=-0.450 (n=18)

  - _Acción_: SKIP cuando `T_h` > 98.7549
  - _Potencial_: sin este filtro IC_bueno=-0.389 (n=7)

- **FILTRO** `T_h` < `145.912` → IC=-0.447 (n=17)

  - _Acción_: SKIP cuando `T_h` < 145.912
  - _Potencial_: sin este filtro IC_bueno=-0.400 (n=8)

- **FILTRO** `pct_vs_K` |x|> `3.4276` → IC=-0.447 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4276
  - _Potencial_: sin este filtro IC_bueno=-0.400 (n=8)

### STREAK_FADE_15M
- **PATRÓN** `hora_utc` > `13.0` → IC=+0.175 (n=38)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 13.0 (IC base=+0.102)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.144 (n=43)

  - _Acción_: Kelly boost +0.72€ cuando `py_entrada` < 0.505 (IC base=+0.102)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `streak_len` < 4.0 (IC base=+0.102)

- **PATRÓN** `volumen_racha` < `249969.2` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `volumen_racha` < 249969.2 (IC base=+0.102)

- **PATRÓN** `libro_liquidez` > `2048.5069` → IC=+0.174 (n=41)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 2048.5069 (IC base=+0.102)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.200 (n=38)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.078)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.147 (n=49)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` < 0.485 (IC base=+0.078)

- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.078)

- **PATRÓN** `volumen_racha` < `234964.8` → IC=+0.184 (n=36)

  - _Acción_: Kelly boost +0.92€ cuando `volumen_racha` < 234964.8 (IC base=+0.078)

### STREAK_FADE_15M#SOL#15min
- **PATRÓN** `hora_utc` > `10.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 10.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.485 (IC base=+0.167)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `volumen_racha` > `305408.9` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `volumen_racha` > 305408.9
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.024)

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
  - _Potencial_: sin este filtro IC_bueno=-0.015 (n=128)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=76)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.066 (n=74)

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

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.140 (n=23)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 9.0 (IC base=+0.041)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` > 0.505 (IC base=+0.041)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `libro_spread` < 0.01 (IC base=+0.041)

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
- **PATRÓN** `ibs_15` > `0.7204` → IC=+0.176 (n=257)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.88€ cuando `ibs_15` > 0.7204 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` > `0.7415` → IC=+0.197 (n=31)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.7415 (IC base=+0.026)

- **PATRÓN** `dist_vwap_pct` < `0.336` → IC=+0.152 (n=133)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.336 (IC base=+0.026)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.266` → IC=+0.184 (n=17)

  - _Acción_: Kelly boost +0.92€ cuando `sigma_ewma_delta_pct` > 15.266 (IC base=+0.026)

- **PATRÓN** `ibs_15` < `0.0286` → IC=+0.130 (n=133)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.65€ cuando `ibs_15` < 0.0286 (IC base=+0.048)

- **PATRÓN** `dist_vwap_pct` > `0.424` → IC=+0.125 (n=30)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` > 0.424 (IC base=+0.048)

- **PATRÓN** `sigma_ewma_delta_pct` < `16.557` → IC=+0.142 (n=118)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 16.557 (IC base=+0.048)

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
- **FILTRO** `ibs_15` > `0.0986` → IC=-0.182 (n=20)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.0986
  - _Potencial_: sin este filtro IC_bueno=+0.208 (n=22)

- **PATRÓN** `drift_60min` |x|≤ `0.2429` → IC=+0.122 (n=183)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.61€ cuando `drift_60min` |x|≤ 0.2429 (IC base=+0.074)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.158 (n=153)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.074)

- **PATRÓN** `ibs_15` < `0.9252` → IC=+0.137 (n=144)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.68€ cuando `ibs_15` < 0.9252 (IC base=+0.074)

- **PATRÓN** `ibs_15` > `0.6323` → IC=+0.192 (n=144)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.6323 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` > `0.7608` → IC=+0.324 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7608 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.527` → IC=+0.188 (n=30)

  - _Acción_: Kelly boost +0.94€ cuando `sigma_ewma_delta_pct` < 5.527 (IC base=+0.074)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0516` → IC=+0.147 (n=32)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.74€ cuando `pct_spot_vs_ref` |x|≤ 0.0516 (IC base=+0.031)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.333 (n=16)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=+0.031)

- **PATRÓN** `drift_15min` |x|≤ `0.4045` → IC=+0.147 (n=15)

  - _Acción_: Kelly boost +0.74€ cuando `drift_15min` |x|≤ 0.4045 (IC base=+0.031)

- **PATRÓN** `ibs_15` < `0.0986` → IC=+0.208 (n=22)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` < 0.0986 (IC base=+0.031)

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
  - _Potencial_: sin este filtro IC_bueno=+0.250 (n=6)

- **PATRÓN** `ibs_15` > `0.7622` → IC=+0.192 (n=92)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.7622 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` < `0.5099` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.5099 (IC base=+0.024)

- **PATRÓN** `dist_vwap_pct` > `0.6579` → IC=+0.152 (n=21)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` > 0.6579 (IC base=+0.047)

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
  - _Potencial_: sin este filtro IC_bueno=-0.071 (n=33)

- **FILTRO** `drift_15min` |x|> `0.3239` → IC=-0.145 (n=29)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.3239
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=11)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.1932` → IC=-0.155 (n=27)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.1932
  - _Potencial_: sin este filtro IC_bueno=+0.062 (n=14)

- **FILTRO** `drift_60min` |x|> `0.4251` → IC=-0.206 (n=15)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.4251
  - _Potencial_: sin este filtro IC_bueno=+0.029 (n=32)

- **FILTRO** `drift_15min` |x|> `0.5673` → IC=-0.140 (n=23)
  - _Por qué funciona_: drift fuerte en 15min → momentum reciente ya en el precio Polymarket
  - _Acción_: SKIP cuando `drift_15min` |x|> 0.5673
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=24)

- **FILTRO** `delta_ratio_macro` |x|≤ `0.0905` → IC=-0.147 (n=15)
  - _Por qué funciona_: flow macro débil → el mercado no ha procesado aún la presión; lag explotable
  - _Acción_: SKIP cuando `delta_ratio_macro` |x|≤ 0.0905
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=32)

- **FILTRO** `hora_utc` < `22.0` → IC=-0.150 (n=18)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: SKIP cuando `hora_utc` < 22.0
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=20)

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

- **FILTRO** `ibs_15` > `0.0769` → IC=-0.132 (n=17)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.0769
  - _Potencial_: sin este filtro IC_bueno=+0.122 (n=35)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.184 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0112 (IC base=+0.091)

- **PATRÓN** `drift_15min` |x|≤ `0.7907` → IC=+0.125 (n=30)

  - _Acción_: Kelly boost +0.62€ cuando `drift_15min` |x|≤ 0.7907 (IC base=+0.091)

- **PATRÓN** `ibs_15` < `0.0769` → IC=+0.122 (n=35)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.61€ cuando `ibs_15` < 0.0769 (IC base=+0.091)

### WEEKLY_PRICE
- **FILTRO** `T_h` > `81.6124` → IC=-0.219 (n=30)

  - _Acción_: SKIP cuando `T_h` > 81.6124
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=11)

- **FILTRO** `T_h` < `144.7452` → IC=-0.273 (n=20)

  - _Acción_: SKIP cuando `T_h` < 144.7452
  - _Potencial_: sin este filtro IC_bueno=-0.152 (n=21)

- **PATRÓN** `T_h` < `144.8754` → IC=+0.279 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 144.8754 (IC base=+0.271)

- **PATRÓN** `T_h` > `87.9928` → IC=+0.291 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9928 (IC base=+0.271)

### WEEKLY_PRICE#BTC
- **PATRÓN** `pct_dist` |x|≤ `2.3456` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 2.3456 (IC base=+0.244)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `135.9981` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 135.9981 (IC base=+0.222)

- **PATRÓN** `pct_dist` |x|≤ `2.4966` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 2.4966 (IC base=+0.222)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` < `111.9959` → IC=+0.346 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 111.9959 (IC base=+0.297)

- **PATRÓN** `T_h` > `87.9959` → IC=+0.296 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9959 (IC base=+0.297)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: IBS > 0.7204 correlaciona con éxito en UPDOWN_GBM#15min (IC=+0.176 n=257). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#BTC#15min**: IBS > 0.6323 correlaciona con éxito en UPDOWN_GBM#BTC#15min (IC=+0.192 n=144). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#BTC#15min**: IBS < 0.0986 correlaciona con éxito en UPDOWN_GBM#BTC#15min (IC=+0.208 n=22). Confirma señal de reversión media → alinear con BUY_YES.
- **H-IBS-UPDOWN_GBM#ETH#15min**: IBS > 0.7622 correlaciona con éxito en UPDOWN_GBM#ETH#15min (IC=+0.192 n=92). Confirma señal de reversión media → alinear con BUY_NO.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ FAVORITO_CONFIRMADO | 2096 | +0.176 | -34.38€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#15min | 1355 | +0.206 | -3.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 88 | +0.000 | -17.12€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 296 | +0.104 | -36.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 357 | +0.166 | +23.03€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 611 | +0.177 | -17.79€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 453 | +0.192 | -28.24€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 29 | +0.081 | -1.58€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 119 | +0.178 | +15.79€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH | 742 | +0.180 | +14.73€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 447 | +0.219 | +21.16€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 29 | -0.145 | -13.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 147 | +0.117 | -12.53€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 119 | +0.186 | +19.19€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL | 737 | +0.174 | -27.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 449 | +0.209 | +7.93€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 30 | +0.062 | -2.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 139 | +0.117 | -20.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 119 | +0.128 | -11.96€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#XRP | 6 | -0.037 | -4.17€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 6 | -0.037 | -4.17€ | 0 | 0 |
| ✅ GBM_LATE_15M | 4538 | +0.102 | +1381.49€ | 0 | 3 |
| ✅ GBM_LATE_15M#15min | 4538 | +0.102 | +1381.49€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 1089 | +0.067 | +160.73€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1089 | +0.067 | +160.73€ | 0 | 4 |
| ✅ GBM_LATE_15M#ETH | 1107 | +0.073 | +181.15€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1107 | +0.073 | +181.15€ | 1 | 4 |
| ✅ GBM_LATE_15M#SOL | 1207 | +0.111 | +491.53€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1207 | +0.111 | +491.53€ | 1 | 6 |
| ✅ GBM_LATE_15M#XRP | 1135 | +0.152 | +548.09€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1135 | +0.152 | +548.09€ | 0 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 1801 | +0.151 | +1043.16€ | 0 | 12 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 1801 | +0.151 | +1043.16€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 461 | +0.124 | +231.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 461 | +0.124 | +231.79€ | 0 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 474 | +0.122 | +210.85€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 474 | +0.122 | +210.85€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 487 | +0.107 | +206.26€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 487 | +0.107 | +206.26€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 379 | +0.274 | +394.27€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 379 | +0.274 | +394.27€ | 0 | 12 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 27 | -0.121 | -1.56€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 27 | -0.121 | -1.56€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC | 9 | -0.102 | -1.94€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 9 | -0.102 | -1.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 7 | +0.019 | +0.79€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 7 | +0.019 | +0.79€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL | 8 | -0.120 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 8 | -0.120 | -1.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 1755 | +0.084 | +484.01€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO#15min | 1755 | +0.084 | +484.01€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 435 | +0.065 | +75.10€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 435 | +0.065 | +75.10€ | 0 | 3 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 390 | +0.010 | +7.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 390 | +0.010 | +7.97€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 436 | +0.048 | +71.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 436 | +0.048 | +71.81€ | 2 | 5 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 494 | +0.190 | +329.13€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 494 | +0.190 | +329.13€ | 0 | 11 |
| ✅ GBM_LATE_5M | 10 | +0.000 | -0.11€ | 0 | 0 |
| ✅ GBM_LATE_5M#5min | 10 | +0.000 | -0.11€ | 0 | 0 |
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
| ✅ LATE_WINDOW_5MIN | 41 | +0.221 | +17.23€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 41 | +0.221 | +17.23€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 41 | +0.221 | +17.23€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 41 | +0.221 | +17.23€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 116 | +0.093 | +30.80€ | 0 | 3 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 116 | +0.093 | +30.80€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 116 | +0.093 | +30.80€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 116 | +0.093 | +30.80€ | 0 | 3 |
| ✅ ORDER_FLOW_5M | 1604 | +0.012 | +12.52€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1468 | +0.007 | -0.07€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 195 | +0.048 | +7.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 195 | +0.048 | +7.22€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 2 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 213 | +0.002 | -1.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 213 | +0.002 | -1.59€ | 2 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 255 | -0.021 | -8.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 255 | -0.021 | -8.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 321 | +0.039 | +12.69€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 321 | +0.039 | +12.69€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 193 | -0.003 | -4.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 193 | -0.003 | -4.19€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM | 146 | -0.162 | -2.74€ | 4 | 1 |
| 🚫 PRICE_TARGET_GBM#BTC | 62 | -0.250 | -18.09€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 56 | -0.276 | -17.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 6 | +0.000 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 54 | -0.161 | +1.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 49 | -0.186 | -2.00€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 5 | +0.018 | +3.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 30 | +0.031 | +13.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 28 | +0.033 | +13.27€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 133 | -0.181 | -6.08€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 13 | +0.022 | +3.34€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 10 | +0.208 | +4.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 10 | +0.208 | +4.00€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 196 | +0.091 | +21.28€ | 0 | 9 |
| ✅ STREAK_FADE_15M#15min | 196 | +0.091 | +21.28€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 42 | +0.068 | -2.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 42 | +0.068 | -2.03€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 68 | +0.171 | +25.11€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 68 | +0.171 | +25.11€ | 0 | 2 |
| ✅ STREAK_FADE_15M#XRP | 86 | +0.034 | -1.80€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 86 | +0.034 | -1.80€ | 1 | 1 |
| ✅ STREAK_FADE_5M | 246 | -0.048 | -24.96€ | 3 | 0 |
| ✅ STREAK_FADE_5M#5min | 246 | -0.048 | -24.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 47 | -0.153 | -8.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 47 | -0.153 | -8.07€ | 6 | 0 |
| ✅ STREAK_FADE_5M#SOL | 94 | -0.021 | -7.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 94 | -0.021 | -7.62€ | 2 | 1 |
| ✅ STREAK_FADE_5M#XRP | 105 | -0.023 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 105 | -0.023 | -9.27€ | 1 | 0 |
| 🚫 STREAK_MOM_5M | 309 | -0.056 | -23.67€ | 6 | 0 |
| ✅ STREAK_MOM_5M#5min | 309 | -0.056 | -23.67€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 103 | -0.052 | -6.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 103 | -0.052 | -6.34€ | 2 | 0 |
| ✅ STREAK_MOM_5M#SOL | 108 | -0.009 | -3.98€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 108 | -0.009 | -3.98€ | 2 | 3 |
| ✅ STREAK_MOM_5M#XRP | 98 | -0.110 | -13.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 98 | -0.110 | -13.35€ | 5 | 0 |
| 🚫 STRUCT_NO_15M | 15 | -0.199 | -4.68€ | 0 | 0 |
| 🚫 STRUCT_NO_15M#15min | 15 | -0.199 | -4.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ UPDOWN_GBM | 1543 | +0.009 | +73.11€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1286 | +0.036 | +109.64€ | 0 | 7 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 127 | -0.058 | -10.76€ | 7 | 0 |
| ✅ UPDOWN_GBM#BNB | 76 | +0.077 | +17.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 76 | +0.077 | +17.58€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 398 | +0.028 | +28.86€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 318 | +0.066 | +41.30€ | 1 | 10 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 42 | -0.068 | -6.16€ | 2 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 15 | -0.066 | +3.36€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 54 | +0.000 | -1.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 51 | +0.009 | -0.69€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 741 | +0.018 | +37.20€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 648 | +0.035 | +48.26€ | 1 | 3 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 54 | -0.018 | -2.56€ | 3 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 170 | -0.087 | -14.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 102 | -0.058 | -7.39€ | 7 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 31 | -0.106 | -2.03€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 102 | +0.000 | +7.28€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 91 | +0.027 | +10.57€ | 5 | 3 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 42 | -0.182 | +2.86€ | 0 | 0 |
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
| ✅ WEEKLY_PRICE | 239 | +0.110 | +7.74€ | 2 | 2 |
| ✅ WEEKLY_PRICE#BTC | 72 | +0.081 | -8.41€ | 0 | 1 |
| ✅ WEEKLY_PRICE#ETH | 69 | +0.091 | -6.63€ | 0 | 2 |
| ✅ WEEKLY_PRICE#SOL | 98 | +0.140 | +22.78€ | 0 | 2 |