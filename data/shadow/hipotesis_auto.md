# Hipótesis automáticas — 2026-07-23 20:23 UTC
_Generado por shadow_postmortem.py sobre 31604 resoluciones (PNL=+6931.16€)_

## Patrones causales activos

### FAVORITO_CONFIRMADO
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.203 (n=2080)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.196)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.204 (n=975)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.196)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.338 (n=678)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.196)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=2242)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.196)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.181 (n=1102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 15.0 (IC base=+0.180)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.218 (n=824)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.344 (n=739)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=2415)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `4244.5716` → IC=+0.182 (n=1447)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 4244.5716 (IC base=+0.180)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.234 (n=152)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.215)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.221 (n=389)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.215)

- **PATRÓN** `py_entrada` > `0.605` → IC=+0.271 (n=443)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.605 (IC base=+0.215)

- **PATRÓN** `libro_liquidez` > `11728.9824` → IC=+0.218 (n=147)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 11728.9824 (IC base=+0.215)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=181)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.239 (n=159)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.379 (n=205)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.206)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.278 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` < `0.565` → IC=+0.250 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.565 (IC base=+0.212)

- **PATRÓN** `py_entrada` > `0.635` → IC=+0.250 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.635 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `8904.9428` → IC=+0.210 (n=36)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8904.9428 (IC base=+0.212)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.316 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.170)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.266 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.405 (IC base=+0.170)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.222 (n=401)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.221 (n=385)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.214)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.348 (n=208)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.214)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.214 (n=555)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.214)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.211 (n=178)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.209)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.236 (n=176)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.209)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.371 (n=161)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.209)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.201 (n=75)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.144)

- **PATRÓN** `py_entrada` < `0.635` → IC=+0.150 (n=98)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.635 (IC base=+0.144)

- **PATRÓN** `py_entrada` > `0.575` → IC=+0.158 (n=112)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` > 0.575 (IC base=+0.144)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.178 (n=119)

  - _Acción_: Kelly boost +0.89€ cuando `libro_spread` < 0.01 (IC base=+0.144)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.200 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.148)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.176 (n=106)

  - _Acción_: Kelly boost +0.88€ cuando `py_entrada` < 0.405 (IC base=+0.148)

- **PATRÓN** `py_entrada` > `0.365` → IC=+0.147 (n=134)

  - _Acción_: Kelly boost +0.74€ cuando `py_entrada` > 0.365 (IC base=+0.148)

- **PATRÓN** `libro_liquidez` > `4211.0402` → IC=+0.194 (n=119)

  - _Acción_: Kelly boost +0.97€ cuando `libro_liquidez` > 4211.0402 (IC base=+0.148)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.242 (n=443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 6.0 (IC base=+0.236)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.337 (n=292)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.236)

- **PATRÓN** `libro_liquidez` > `2354.3031` → IC=+0.257 (n=146)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2354.3031 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.212 (n=311)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.211)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.222 (n=477)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.211)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.346 (n=160)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.211)

- **PATRÓN** `libro_liquidez` > `1611.1896` → IC=+0.216 (n=463)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1611.1896 (IC base=+0.211)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.223 (n=45)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.179)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.245 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.575 (IC base=+0.179)

- **PATRÓN** `py_entrada` > `0.605` → IC=+0.188 (n=78)

  - _Acción_: Kelly boost +0.94€ cuando `py_entrada` > 0.605 (IC base=+0.179)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.205 (n=110)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.179)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.127 (n=132)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` < 17.0 (IC base=+0.115)

- **PATRÓN** `py_entrada` < `0.34` → IC=+0.300 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.34 (IC base=+0.115)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.149 (n=132)

  - _Acción_: Kelly boost +0.75€ cuando `libro_spread` < 0.02 (IC base=+0.115)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.130 (n=2109)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 8.0 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `0.4721` → IC=+0.130 (n=295)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.4721 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.621` → IC=+0.223 (n=452)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.621 (IC base=+0.114)

- **PATRÓN** `sigma_h` > `0.0132` → IC=+0.131 (n=932)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.65€ cuando `sigma_h` > 0.0132 (IC base=+0.097)

- **PATRÓN** `dist_vwap_pct` > `0.2735` → IC=+0.131 (n=396)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.2735 (IC base=+0.097)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0062` → IC=+0.120 (n=485)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0062 (IC base=+0.096)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.129 (n=496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 8.0 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.433` → IC=+0.160 (n=51)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.433 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.102` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.102 (IC base=+0.096)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.171 (n=147)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` < 0.0044 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.9362` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9362 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` < `0.1625` → IC=+0.148 (n=103)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1625 (IC base=+0.105)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.25` → IC=+0.221 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.25 (IC base=+0.105)

- **PATRÓN** `dist_vwap_pct` > `0.6406` → IC=+0.151 (n=81)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.6406 (IC base=+0.066)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.318` → IC=+0.175 (n=115)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 7.318 (IC base=+0.066)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `9.123` → IC=-0.309 (n=19)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 9.123
  - _Potencial_: sin este filtro IC_bueno=+0.075 (n=436)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.139 (n=264)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 17.0 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.561` → IC=+0.244 (n=123)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.561 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.163 (n=259)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` < 6.0 (IC base=+0.105)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.158 (n=226)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0103 (IC base=+0.147)

- **PATRÓN** `sigma_h` > `0.0219` → IC=+0.159 (n=306)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.80€ cuando `sigma_h` > 0.0219 (IC base=+0.147)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.154 (n=674)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.147)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.148 (n=453)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 11.0 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` > `0.5959` → IC=+0.216 (n=72)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5959 (IC base=+0.147)

- **PATRÓN** `dist_vwap_pct` < `0.113` → IC=+0.136 (n=311)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.113 (IC base=+0.147)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.791` → IC=+0.287 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.791 (IC base=+0.147)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.164 (n=254)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` < 0.0097 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0272` → IC=+0.167 (n=253)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0272 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=268)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.151)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.197 (n=275)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 6.0 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.3707` → IC=+0.208 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3707 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.757` → IC=+0.141 (n=422)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.757 (IC base=+0.151)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0117` → IC=+0.215 (n=479)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0117 (IC base=+0.151)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.173 (n=1309)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 8.0 (IC base=+0.151)

- **PATRÓN** `dist_vwap_pct` > `0.2767` → IC=+0.206 (n=406)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2767 (IC base=+0.151)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.083` → IC=+0.278 (n=237)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.083 (IC base=+0.151)

- **PATRÓN** `sigma_h` > `0.0043` → IC=+0.148 (n=1605)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0043 (IC base=+0.131)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.145 (n=1116)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 12.0 (IC base=+0.131)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.140 (n=598)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 6.0 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` > `0.9945` → IC=+0.158 (n=115)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.9945 (IC base=+0.131)

- **PATRÓN** `dist_vwap_pct` < `0.7459` → IC=+0.133 (n=1621)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.7459 (IC base=+0.131)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.153` → IC=+0.154 (n=319)

  - _Acción_: Kelly boost +0.77€ cuando `sigma_ewma_delta_pct` > 6.153 (IC base=+0.131)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `hora_utc` > `15.0` → IC=+0.189 (n=165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 15.0 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `0.4596` → IC=+0.211 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4596 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.162` → IC=+0.208 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.162 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.895` → IC=+0.145 (n=105)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 6.895 (IC base=+0.091)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.0083` → IC=+0.206 (n=117)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0083 (IC base=+0.130)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.158 (n=241)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 12.0 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.688` → IC=+0.195 (n=57)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.688 (IC base=+0.130)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.773` → IC=+0.234 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.773 (IC base=+0.130)

- **PATRÓN** `dist_vwap_pct` > `0.6052` → IC=+0.163 (n=81)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.6052 (IC base=+0.093)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.179` → IC=+0.194 (n=109)

  - _Acción_: Kelly boost +0.97€ cuando `sigma_ewma_delta_pct` > 7.179 (IC base=+0.093)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **PATRÓN** `sigma_h` > `0.0116` → IC=+0.209 (n=177)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0116 (IC base=+0.127)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.150 (n=358)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 8.0 (IC base=+0.127)

- **PATRÓN** `dist_vwap_pct` > `0.1931` → IC=+0.160 (n=145)

  - _Acción_: Kelly boost +0.80€ cuando `dist_vwap_pct` > 0.1931 (IC base=+0.127)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.781` → IC=+0.292 (n=157)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.781 (IC base=+0.127)

- **PATRÓN** `sigma_h` < `0.0081` → IC=+0.149 (n=169)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0081 (IC base=+0.095)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.125` → IC=+0.130 (n=309)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 3.125 (IC base=+0.095)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` < `0.0183` → IC=+0.260 (n=352)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0183 (IC base=+0.236)

- **PATRÓN** `sigma_h` > `0.0087` → IC=+0.239 (n=351)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0087 (IC base=+0.236)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.254 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.236)

- **PATRÓN** `dist_vwap_pct` > `0.5978` → IC=+0.324 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5978 (IC base=+0.236)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.065` → IC=+0.363 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.065 (IC base=+0.236)

- **PATRÓN** `sigma_h` < `0.0188` → IC=+0.243 (n=403)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0188 (IC base=+0.242)

- **PATRÓN** `sigma_h` > `0.0081` → IC=+0.256 (n=403)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0081 (IC base=+0.242)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.255 (n=370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.242)

- **PATRÓN** `dist_vwap_pct` > `0.1697` → IC=+0.346 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1697 (IC base=+0.242)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.006` → IC=+0.247 (n=354)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.006 (IC base=+0.242)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0136` → IC=+0.158 (n=457)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0136 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.128 (n=1228)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 8.0 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.4541` → IC=+0.162 (n=279)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.4541 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.72` → IC=+0.287 (n=209)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.72 (IC base=+0.113)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.142 (n=272)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 8.0 (IC base=+0.092)

- **PATRÓN** `dist_vwap_pct` > `0.4395` → IC=+0.173 (n=50)

  - _Acción_: Kelly boost +0.87€ cuando `dist_vwap_pct` > 0.4395 (IC base=+0.092)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.284` → IC=+0.219 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.284 (IC base=+0.092)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0046` → IC=+0.122 (n=146)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0046 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.864` → IC=+0.239 (n=44)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.864 (IC base=+0.067)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `6.783` → IC=-0.167 (n=22)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.783
  - _Potencial_: sin este filtro IC_bueno=+0.089 (n=353)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.238` → IC=+0.264 (n=121)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.238 (IC base=+0.076)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.124 (n=336)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0108 (IC base=+0.063)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.154 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 6.0 (IC base=+0.063)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0215` → IC=+0.191 (n=390)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` < 0.0215 (IC base=+0.186)

- **PATRÓN** `sigma_h` > `0.0107` → IC=+0.191 (n=396)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0107 (IC base=+0.186)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.190 (n=443)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` > 6.0 (IC base=+0.186)

- **PATRÓN** `dist_vwap_pct` > `0.2414` → IC=+0.244 (n=135)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2414 (IC base=+0.186)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.089` → IC=+0.315 (n=79)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.089 (IC base=+0.186)

- **PATRÓN** `sigma_h` < `0.0194` → IC=+0.184 (n=454)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0194 (IC base=+0.176)

- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.177 (n=345)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0134 (IC base=+0.176)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.196 (n=179)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` > 18.0 (IC base=+0.176)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.192 (n=183)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.176)

- **PATRÓN** `dist_vwap_pct` > `0.1465` → IC=+0.232 (n=140)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1465 (IC base=+0.176)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.154` → IC=+0.177 (n=506)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` < 10.154 (IC base=+0.176)

### GBM_LATE_60M
- **FILTRO** `sigma_ewma_delta_pct` < `13.491` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 13.491
  - _Potencial_: sin este filtro IC_bueno=+0.192 (n=11)

- **FILTRO** `sigma_h` > `0.0133` → IC=-0.300 (n=38)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0133
  - _Potencial_: sin este filtro IC_bueno=-0.192 (n=118)

- **FILTRO** `hora_utc` > `7.0` → IC=-0.272 (n=112)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=-0.087 (n=44)

- **PATRÓN** `sigma_h` < `0.0051` → IC=+0.145 (n=60)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0051 (IC base=-0.017)

### GBM_LATE_60M#BTC#60min
- **FILTRO** `sigma_h` > `0.0053` → IC=-0.132 (n=36)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0053
  - _Potencial_: sin este filtro IC_bueno=+0.175 (n=38)

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

- **PATRÓN** `sigma_h` < `0.0053` → IC=+0.175 (n=38)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0053 (IC base=+0.026)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=148)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=73)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=148)

- **FILTRO** `py_entrada` > `0.505` → IC=-0.121 (n=27)

  - _Acción_: SKIP cuando `py_entrada` > 0.505
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=73)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.050 (n=129)

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
  - _Potencial_: sin este filtro IC_bueno=+0.155 (n=82)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.188 (n=46)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` > 14.0 (IC base=+0.093)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.139 (n=81)

  - _Acción_: Kelly boost +0.69€ cuando `streak_len` < 4.0 (IC base=+0.093)

- **PATRÓN** `volumen_racha` < `322294.1` → IC=+0.152 (n=67)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_racha` < 322294.1 (IC base=+0.093)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.155 (n=82)

  - _Acción_: Kelly boost +0.77€ cuando `libro_spread` < 0.01 (IC base=+0.093)

- **PATRÓN** `libro_liquidez` > `2649.5751` → IC=+0.167 (n=49)

  - _Acción_: Kelly boost +0.83€ cuando `libro_liquidez` > 2649.5751 (IC base=+0.093)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.220 (n=48)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.079)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.125 (n=70)

  - _Acción_: Kelly boost +0.62€ cuando `py_entrada` < 0.485 (IC base=+0.079)

- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.141 (n=37)

  - _Acción_: Kelly boost +0.71€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.079)

- **PATRÓN** `volumen_racha` < `503163.4` → IC=+0.153 (n=70)

  - _Acción_: Kelly boost +0.76€ cuando `volumen_racha` < 503163.4 (IC base=+0.079)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `hora_utc` > `6.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 6.0
  - _Potencial_: sin este filtro IC_bueno=+0.200 (n=8)

### STREAK_FADE_15M#SOL#15min
- **PATRÓN** `streak_len` < `4.0` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `streak_len` < 4.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.485 (IC base=+0.125)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `hora_utc` < `9.0` → IC=+0.184 (n=36)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 9.0 (IC base=+0.091)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.192 (n=24)

  - _Acción_: Kelly boost +0.96€ cuando `py_entrada` < 0.485 (IC base=+0.091)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `streak_len` < 4.0 (IC base=+0.091)

- **PATRÓN** `regimen_ma_toques` > `3.0` → IC=+0.155 (n=27)

  - _Acción_: Kelly boost +0.78€ cuando `regimen_ma_toques` > 3.0 (IC base=+0.091)

- **PATRÓN** `volumen_racha` < `503163.4` → IC=+0.260 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 503163.4 (IC base=+0.091)

- **PATRÓN** `libro_liquidez` > `2531.1309` → IC=+0.179 (n=26)

  - _Acción_: Kelly boost +0.89€ cuando `libro_liquidez` > 2531.1309 (IC base=+0.091)

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
- **PATRÓN** `ibs_15` > `0.6182` → IC=+0.182 (n=510)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.91€ cuando `ibs_15` > 0.6182 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.1714` → IC=+0.180 (n=167)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.1714 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.482` → IC=+0.179 (n=107)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 12.482 (IC base=+0.055)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=12)

- **FILTRO** `ibs_15` < `0.7622` → IC=-0.182 (n=20)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: SKIP cuando `ibs_15` < 0.7622
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=7)

### UPDOWN_GBM#BTC#15min
- **FILTRO** `ibs_15` > `0.0344` → IC=-0.133 (n=28)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.0344
  - _Potencial_: sin este filtro IC_bueno=+0.125 (n=30)

- **PATRÓN** `sigma_h` < `0.0078` → IC=+0.122 (n=281)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0078 (IC base=+0.101)

- **PATRÓN** `drift_60min` |x|≤ `0.2235` → IC=+0.137 (n=271)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.69€ cuando `drift_60min` |x|≤ 0.2235 (IC base=+0.101)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0644` → IC=+0.128 (n=272)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.64€ cuando `delta_ratio_macro` |x|> 0.0644 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.175 (n=78)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 8.0 (IC base=+0.101)

- **PATRÓN** `ibs_15` > `0.6374` → IC=+0.218 (n=232)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.6374 (IC base=+0.101)

- **PATRÓN** `dist_vwap_pct` > `0.1484` → IC=+0.235 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1484 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.299` → IC=+0.170 (n=110)

  - _Acción_: Kelly boost +0.85€ cuando `sigma_ewma_delta_pct` < 14.299 (IC base=+0.101)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.182 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0055 (IC base=+0.013)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_h` < `0.012` → IC=-0.143 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.012
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `ibs_15` > `0.6794` → IC=+0.189 (n=165)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.94€ cuando `ibs_15` > 0.6794 (IC base=+0.039)

- **PATRÓN** `dist_vwap_pct` < `0.4866` → IC=+0.123 (n=128)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.4866 (IC base=+0.039)

- **PATRÓN** `sigma_ewma_delta_pct` > `33.067` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 33.067 (IC base=+0.039)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.134 (n=159)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` < 0.006 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.4577` → IC=+0.156 (n=62)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.4577 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` < `8.385` → IC=+0.130 (n=163)

  - _Acción_: Kelly boost +0.65€ cuando `sigma_ewma_delta_pct` < 8.385 (IC base=+0.059)

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

- **FILTRO** `sigma_ewma_delta_pct` > `20.946` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.946
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=125)

### WEEKLY_PRICE
- **FILTRO** `T_h` < `144.8242` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `T_h` < 144.8242
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

- **PATRÓN** `T_h` > `146.1118` → IC=+0.392 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1118 (IC base=+0.320)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `144.6231` → IC=+0.300 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 144.6231 (IC base=+0.261)

- **PATRÓN** `T_h` > `111.9936` → IC=+0.265 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9936 (IC base=+0.261)

- **PATRÓN** `pct_dist` |x|≤ `1.2005` → IC=+0.333 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 1.2005 (IC base=+0.261)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `111.996` → IC=+0.267 (n=41)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.996 (IC base=+0.242)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` < `146.1402` → IC=+0.389 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 146.1402 (IC base=+0.382)

- **PATRÓN** `T_h` > `87.9977` → IC=+0.395 (n=93)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9977 (IC base=+0.382)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6182 sube el IC de +0.055 a +0.182 en UPDOWN_GBM#15min (n=510). Ya aplicado como kelly_boost=+0.91€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.6374 sube el IC de +0.101 a +0.218 en UPDOWN_GBM#BTC#15min (n=232). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6794 sube el IC de +0.039 a +0.189 en UPDOWN_GBM#ETH#15min (n=165). Ya aplicado como kelly_boost=+0.94€ automático (shadow) — no es señal de reversión a la dirección contraria.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 883 | +0.128 | +41.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 883 | +0.128 | +41.93€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 10 | +0.083 | +2.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 10 | +0.083 | +2.04€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 336 | +0.133 | +9.78€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 336 | +0.133 | +9.78€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 338 | +0.144 | +14.87€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 338 | +0.144 | +14.87€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 199 | +0.087 | +15.25€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 199 | +0.087 | +15.25€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 26 | +0.357 | +2.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 26 | +0.357 | +2.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 26 | +0.357 | +2.42€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 26 | +0.357 | +2.42€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 5529 | +0.188 | +95.34€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#15min | 3628 | +0.215 | +92.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 241 | +0.060 | -15.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 697 | +0.124 | -59.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 963 | +0.162 | +78.68€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 1618 | +0.196 | +47.08€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1207 | +0.210 | -5.23€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 80 | +0.061 | -6.93€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 321 | +0.190 | +63.00€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH | 1953 | +0.177 | +6.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1196 | +0.212 | +35.27€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 80 | -0.024 | -18.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 356 | +0.129 | -26.62€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 321 | +0.147 | +16.39€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#SOL | 1928 | +0.191 | +39.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1199 | +0.224 | +63.68€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 81 | +0.139 | +9.96€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 327 | +0.126 | -33.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 321 | +0.147 | -0.71€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 28 | +0.133 | +0.40€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 24 | +0.077 | -3.95€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 298 | +0.320 | +18.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 298 | +0.320 | +18.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 298 | +0.320 | +18.19€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 298 | +0.320 | +18.19€ | 0 | 0 |
| ✅ GBM_LATE_15M | 7226 | +0.096 | +2247.13€ | 0 | 5 |
| ✅ GBM_LATE_15M#15min | 7226 | +0.096 | +2247.13€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 1749 | +0.065 | +284.82€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1749 | +0.065 | +284.82€ | 0 | 4 |
| ✅ GBM_LATE_15M#ETH | 1619 | +0.075 | +286.72€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1619 | +0.075 | +286.72€ | 0 | 6 |
| ✅ GBM_LATE_15M#SOL | 1947 | +0.088 | +694.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1947 | +0.088 | +694.02€ | 1 | 3 |
| ✅ GBM_LATE_15M#XRP | 1911 | +0.149 | +981.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1911 | +0.149 | +981.58€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 4417 | +0.125 | +2200.20€ | 0 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 4417 | +0.125 | +2200.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1140 | +0.082 | +394.81€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1140 | +0.082 | +394.81€ | 0 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1152 | +0.092 | +421.86€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1152 | +0.092 | +421.86€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1118 | +0.098 | +460.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1118 | +0.098 | +460.22€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1007 | +0.239 | +923.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1007 | +0.239 | +923.30€ | 0 | 10 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 245 | +0.107 | +111.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 245 | +0.107 | +111.22€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC | 9 | -0.102 | -1.94€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 9 | -0.102 | -1.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 84 | +0.000 | +14.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 84 | +0.000 | +14.64€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL | 8 | -0.120 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 8 | -0.120 | -1.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 144 | +0.219 | +100.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 144 | +0.219 | +100.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 4440 | +0.077 | +1291.89€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO#15min | 4440 | +0.077 | +1291.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1070 | +0.035 | +136.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1070 | +0.035 | +136.22€ | 0 | 3 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1068 | +0.028 | +81.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1068 | +0.028 | +81.18€ | 0 | 2 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1025 | +0.043 | +212.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1025 | +0.043 | +212.62€ | 1 | 3 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1277 | +0.181 | +861.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1277 | +0.181 | +861.87€ | 0 | 11 |
| ✅ GBM_LATE_5M | 487 | -0.024 | +0.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#5min | 487 | -0.024 | +0.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 110 | -0.036 | -11.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 110 | -0.036 | -11.65€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 55 | -0.114 | -7.08€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 55 | -0.114 | -7.08€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL | 85 | -0.155 | +3.15€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 85 | -0.155 | +3.15€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 237 | +0.052 | +15.90€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 237 | +0.052 | +15.90€ | 0 | 0 |
| ✅ GBM_LATE_60M | 336 | -0.112 | +4.40€ | 3 | 1 |
| ✅ GBM_LATE_60M#60min | 336 | -0.112 | +4.40€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 120 | -0.041 | +3.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 120 | -0.041 | +3.25€ | 4 | 1 |
| ✅ GBM_LATE_60M#ETH | 106 | -0.148 | -10.12€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 106 | -0.148 | -10.12€ | 4 | 0 |
| ✅ GBM_LATE_60M#SOL | 110 | -0.152 | +11.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 110 | -0.152 | +11.27€ | 5 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO | 9 | -0.143 | -2.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO#60min | 9 | -0.143 | -2.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 347 | -0.053 | -4.82€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 347 | -0.053 | -4.82€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 347 | -0.053 | -4.82€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 347 | -0.053 | -4.82€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 265 | +0.009 | +9.65€ | 2 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 265 | +0.009 | +9.65€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 265 | +0.009 | +9.65€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 265 | +0.009 | +9.65€ | 2 | 0 |
| ✅ ORDER_FLOW_5M | 1659 | +0.012 | +11.80€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1523 | +0.007 | -0.79€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 211 | +0.035 | +4.65€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 211 | +0.035 | +4.65€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 221 | -0.002 | -2.67€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 221 | -0.002 | -2.67€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 266 | -0.015 | -7.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 266 | -0.015 | -7.54€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 328 | +0.045 | +14.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 328 | +0.045 | +14.91€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP | 206 | -0.005 | -4.90€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 206 | -0.005 | -4.90€ | 1 | 0 |
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
| ✅ RESOLUTION_SNIPER | 12 | +0.171 | +2.98€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 12 | +0.171 | +2.98€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 271 | +0.086 | +35.54€ | 1 | 9 |
| ✅ STREAK_FADE_15M#15min | 271 | +0.086 | +35.54€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 58 | +0.050 | -0.08€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 58 | +0.050 | -0.08€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 87 | +0.129 | +22.47€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 87 | +0.129 | +22.47€ | 0 | 3 |
| ✅ STREAK_FADE_15M#XRP | 126 | +0.070 | +13.15€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 126 | +0.070 | +13.15€ | 0 | 6 |
| ✅ STREAK_FADE_5M | 246 | -0.048 | -24.96€ | 3 | 0 |
| ✅ STREAK_FADE_5M#5min | 246 | -0.048 | -24.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 47 | -0.153 | -8.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 47 | -0.153 | -8.07€ | 3 | 0 |
| ✅ STREAK_FADE_5M#SOL | 94 | -0.021 | -7.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 94 | -0.021 | -7.62€ | 0 | 0 |
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
| ✅ UPDOWN_GBM | 2382 | +0.032 | +206.04€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2119 | +0.052 | +244.55€ | 0 | 3 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 130 | -0.061 | -11.21€ | 6 | 0 |
| ✅ UPDOWN_GBM#BNB | 238 | +0.062 | +51.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 238 | +0.062 | +51.08€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 536 | +0.050 | +60.67€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 452 | +0.086 | +75.16€ | 1 | 8 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 43 | -0.078 | -6.67€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 185 | +0.040 | +20.76€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 182 | +0.043 | +21.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 966 | +0.035 | +59.44€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 872 | +0.050 | +71.00€ | 0 | 6 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 55 | -0.026 | -3.07€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 214 | -0.069 | -12.89€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 145 | -0.044 | -6.46€ | 4 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 32 | -0.088 | -1.46€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 241 | +0.031 | +28.82€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 230 | +0.043 | +32.11€ | 4 | 0 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 134 | +0.294 | +25.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 134 | +0.294 | +25.87€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 63 | +0.285 | +9.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 63 | +0.285 | +9.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 71 | +0.294 | +15.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 71 | +0.294 | +15.92€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1423 | +0.163 | +657.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1423 | +0.163 | +657.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 141 | +0.206 | +84.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 141 | +0.206 | +84.41€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 161 | +0.126 | +31.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 161 | +0.126 | +31.88€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 138 | +0.214 | +93.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 138 | +0.214 | +93.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 281 | +0.157 | +100.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 281 | +0.157 | +100.75€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 344 | +0.101 | +94.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 344 | +0.101 | +94.59€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 358 | +0.203 | +252.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 358 | +0.203 | +252.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 13 | +0.022 | +0.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 13 | +0.022 | +0.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 13 | +0.022 | +0.20€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 13 | +0.022 | +0.20€ | 0 | 0 |
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
| ✅ WEEKLY_PRICE | 352 | +0.189 | +69.51€ | 1 | 1 |
| ✅ WEEKLY_PRICE#BTC | 103 | +0.129 | -8.56€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 98 | +0.130 | -6.98€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 151 | +0.265 | +85.05€ | 0 | 2 |