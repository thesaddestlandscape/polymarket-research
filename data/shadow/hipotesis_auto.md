# Hipótesis automáticas — 2026-07-24 17:27 UTC
_Generado por shadow_postmortem.py sobre 33274 resoluciones (PNL=+7339.80€)_

## Patrones causales activos

### FAVORITO_CONFIRMADO
- **PATRÓN** `hora_utc` > `6.0` → IC=+0.199 (n=2094)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 6.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.211 (n=1036)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` > `0.735` → IC=+0.339 (n=704)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.735 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.202 (n=2370)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.206 (n=784)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.180)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.343 (n=786)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.180)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=2569)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.180)

- **PATRÓN** `libro_liquidez` > `4205.4117` → IC=+0.180 (n=1546)

  - _Acción_: Kelly boost +0.90€ cuando `libro_liquidez` > 4205.4117 (IC base=+0.180)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.233 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.216)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.228 (n=222)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.216)

- **PATRÓN** `py_entrada` > `0.605` → IC=+0.275 (n=464)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.605 (IC base=+0.216)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.216 (n=188)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.227 (n=174)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.255` → IC=+0.379 (n=221)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.255 (IC base=+0.202)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` < `15.0` → IC=+0.281 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.214)

- **PATRÓN** `py_entrada` < `0.565` → IC=+0.245 (n=53)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.565 (IC base=+0.214)

- **PATRÓN** `py_entrada` > `0.635` → IC=+0.250 (n=42)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.635 (IC base=+0.214)

- **PATRÓN** `libro_liquidez` > `8909.1861` → IC=+0.225 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 8909.1861 (IC base=+0.214)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.271 (n=68)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.167)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.265 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.405 (IC base=+0.167)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.218 (n=161)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.206)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.214 (n=410)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.206)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.349 (n=216)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.206)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.206 (n=589)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.206)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.219 (n=183)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.208)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.219 (n=358)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.208)

- **PATRÓN** `py_entrada` < `0.235` → IC=+0.358 (n=174)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.235 (IC base=+0.208)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.164 (n=120)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 5.0 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.186 (n=103)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` < 15.0 (IC base=+0.141)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.167 (n=46)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.575 (IC base=+0.141)

- **PATRÓN** `py_entrada` > `0.575` → IC=+0.150 (n=118)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` > 0.575 (IC base=+0.141)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.177 (n=128)

  - _Acción_: Kelly boost +0.88€ cuando `libro_spread` < 0.01 (IC base=+0.141)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.169 (n=125)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.85€ cuando `hora_utc` < 15.0 (IC base=+0.147)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.170 (n=110)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` < 0.405 (IC base=+0.147)

- **PATRÓN** `py_entrada` > `0.365` → IC=+0.151 (n=144)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` > 0.365 (IC base=+0.147)

- **PATRÓN** `libro_liquidez` > `4102.9784` → IC=+0.195 (n=126)

  - _Acción_: Kelly boost +0.98€ cuando `libro_liquidez` > 4102.9784 (IC base=+0.147)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.248 (n=165)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.240 (n=217)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.230)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.329 (n=308)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.230)

- **PATRÓN** `libro_liquidez` > `2367.8144` → IC=+0.250 (n=154)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2367.8144 (IC base=+0.230)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.247 (n=168)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.212)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.345 (n=166)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.212)

- **PATRÓN** `libro_liquidez` > `1588.1821` → IC=+0.218 (n=494)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1588.1821 (IC base=+0.212)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.214 (n=47)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.169)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.172 (n=59)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` < 8.0 (IC base=+0.169)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.245 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.575 (IC base=+0.169)

- **PATRÓN** `py_entrada` > `0.61` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `py_entrada` > 0.61 (IC base=+0.169)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.201 (n=115)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.02 (IC base=+0.169)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.128 (n=135)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` > 6.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.143 (n=141)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 17.0 (IC base=+0.128)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.308 (n=45)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.128)

- **PATRÓN** `libro_spread` < `0.02` → IC=+0.160 (n=139)

  - _Acción_: Kelly boost +0.80€ cuando `libro_spread` < 0.02 (IC base=+0.128)

- **PATRÓN** `libro_liquidez` > `3555.22` → IC=+0.160 (n=45)

  - _Acción_: Kelly boost +0.80€ cuando `libro_liquidez` > 3555.22 (IC base=+0.128)

### GBM_LATE_15M
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.126 (n=2286)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.63€ cuando `hora_utc` > 7.0 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.4721` → IC=+0.132 (n=297)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` > 0.4721 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.596` → IC=+0.212 (n=477)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.596 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.2706` → IC=+0.131 (n=407)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.2706 (IC base=+0.099)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.125 (n=502)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.62€ cuando `sigma_h` < 0.0061 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` > `0.441` → IC=+0.167 (n=52)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.441 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.491` → IC=+0.219 (n=62)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.491 (IC base=+0.100)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.169 (n=149)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.84€ cuando `sigma_h` < 0.0044 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.9362` → IC=+0.222 (n=16)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.9362 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.1687` → IC=+0.145 (n=108)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` < 0.1687 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.243` → IC=+0.209 (n=108)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.243 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.6123` → IC=+0.147 (n=83)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` > 0.6123 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.275` → IC=+0.164 (n=123)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` > 7.275 (IC base=+0.069)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `8.718` → IC=-0.283 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.718
  - _Potencial_: sin este filtro IC_bueno=+0.079 (n=473)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.143 (n=267)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 17.0 (IC base=+0.098)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.274` → IC=+0.254 (n=63)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.274 (IC base=+0.098)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.161 (n=269)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 6.0 (IC base=+0.105)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_h` < `0.0103` → IC=+0.158 (n=232)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.0103 (IC base=+0.145)

- **PATRÓN** `sigma_h` > `0.0217` → IC=+0.164 (n=313)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.82€ cuando `sigma_h` > 0.0217 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.153 (n=693)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` > 6.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.147 (n=465)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 11.0 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.609` → IC=+0.191 (n=66)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.609 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `0.1135` → IC=+0.134 (n=326)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1135 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.882` → IC=+0.275 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.882 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0096` → IC=+0.175 (n=266)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0096 (IC base=+0.152)

- **PATRÓN** `sigma_h` > `0.0269` → IC=+0.157 (n=266)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` > 0.0269 (IC base=+0.152)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.173 (n=273)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.86€ cuando `hora_utc` > 18.0 (IC base=+0.152)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.176 (n=291)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` < 6.0 (IC base=+0.152)

- **PATRÓN** `dist_vwap_pct` > `0.3707` → IC=+0.211 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3707 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.734` → IC=+0.138 (n=114)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` > 5.734 (IC base=+0.152)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.757` → IC=+0.141 (n=461)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` < 3.757 (IC base=+0.152)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.191 (n=1008)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.96€ cuando `sigma_h` > 0.0078 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.167 (n=1359)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 8.0 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.2794` → IC=+0.203 (n=419)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2794 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.074` → IC=+0.269 (n=249)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.074 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0071` → IC=+0.166 (n=1134)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` > 0.0071 (IC base=+0.133)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.149 (n=1185)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 12.0 (IC base=+0.133)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.133 (n=630)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` < 6.0 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` > `1.0377` → IC=+0.175 (n=112)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 1.0377 (IC base=+0.133)

- **PATRÓN** `dist_vwap_pct` < `0.7664` → IC=+0.136 (n=1752)

  - _Acción_: Kelly boost +0.68€ cuando `dist_vwap_pct` < 0.7664 (IC base=+0.133)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.2` → IC=+0.157 (n=345)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` > 6.2 (IC base=+0.133)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `sigma_h` < `0.0052` → IC=+0.126 (n=324)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0052 (IC base=+0.116)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.143 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 6.0 (IC base=+0.116)

- **PATRÓN** `dist_vwap_pct` > `0.4643` → IC=+0.206 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4643 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.924` → IC=+0.214 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.924 (IC base=+0.116)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.065` → IC=+0.146 (n=111)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 7.065 (IC base=+0.093)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.0082` → IC=+0.211 (n=126)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0082 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.147 (n=253)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 12.0 (IC base=+0.124)

- **PATRÓN** `dist_vwap_pct` > `0.3409` → IC=+0.179 (n=104)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.3409 (IC base=+0.124)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.291` → IC=+0.229 (n=68)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.291 (IC base=+0.124)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.121 (n=299)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.61€ cuando `hora_utc` > 12.0 (IC base=+0.096)

- **PATRÓN** `dist_vwap_pct` > `0.5903` → IC=+0.171 (n=83)

  - _Acción_: Kelly boost +0.85€ cuando `dist_vwap_pct` > 0.5903 (IC base=+0.096)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.167` → IC=+0.198 (n=84)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 10.167 (IC base=+0.096)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **PATRÓN** `sigma_h` > `0.008` → IC=+0.151 (n=405)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.008 (IC base=+0.120)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.146 (n=365)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 8.0 (IC base=+0.120)

- **PATRÓN** `dist_vwap_pct` > `0.3229` → IC=+0.155 (n=114)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` > 0.3229 (IC base=+0.120)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.781` → IC=+0.278 (n=165)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.781 (IC base=+0.120)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.122 (n=406)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.61€ cuando `sigma_h` < 0.0112 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.118` → IC=+0.138 (n=329)

  - _Acción_: Kelly boost +0.69€ cuando `sigma_ewma_delta_pct` < 3.118 (IC base=+0.099)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` < `0.0183` → IC=+0.258 (n=361)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0183 (IC base=+0.235)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.241 (n=361)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.235)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.252 (n=328)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.235)

- **PATRÓN** `dist_vwap_pct` > `0.6283` → IC=+0.312 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6283 (IC base=+0.235)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.15` → IC=+0.356 (n=95)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 8.15 (IC base=+0.235)

- **PATRÓN** `sigma_h` < `0.0186` → IC=+0.246 (n=428)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0186 (IC base=+0.241)

- **PATRÓN** `sigma_h` > `0.008` → IC=+0.251 (n=428)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.008 (IC base=+0.241)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.263 (n=391)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.241)

- **PATRÓN** `dist_vwap_pct` > `0.1675` → IC=+0.349 (n=91)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1675 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.933` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.933 (IC base=+0.241)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.019` → IC=+0.241 (n=377)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.019 (IC base=+0.241)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0134` → IC=+0.158 (n=486)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` > 0.0134 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.121 (n=1364)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 7.0 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` > `0.4729` → IC=+0.166 (n=279)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4729 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.707` → IC=+0.271 (n=229)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.707 (IC base=+0.108)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `hora_utc` > `7.0` → IC=+0.133 (n=303)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 7.0 (IC base=+0.089)

- **PATRÓN** `dist_vwap_pct` > `0.4615` → IC=+0.192 (n=50)

  - _Acción_: Kelly boost +0.96€ cuando `dist_vwap_pct` > 0.4615 (IC base=+0.089)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.244` → IC=+0.222 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.244 (IC base=+0.089)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `13.671` → IC=+0.226 (n=49)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.671 (IC base=+0.063)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `6.783` → IC=-0.180 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 6.783
  - _Potencial_: sin este filtro IC_bueno=+0.091 (n=377)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.139` → IC=+0.244 (n=131)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.139 (IC base=+0.072)

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.176 (n=134)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` < 0.0077 (IC base=+0.065)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.0215` → IC=+0.183 (n=405)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0215 (IC base=+0.181)

- **PATRÓN** `sigma_h` > `0.0282` → IC=+0.199 (n=154)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.99€ cuando `sigma_h` > 0.0282 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.186 (n=463)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 6.0 (IC base=+0.181)

- **PATRÓN** `dist_vwap_pct` > `0.461` → IC=+0.245 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.461 (IC base=+0.181)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.119` → IC=+0.293 (n=85)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.119 (IC base=+0.181)

- **PATRÓN** `sigma_h` < `0.0097` → IC=+0.203 (n=240)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0097 (IC base=+0.180)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.191 (n=503)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` > 8.0 (IC base=+0.180)

- **PATRÓN** `dist_vwap_pct` > `0.148` → IC=+0.233 (n=144)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.148 (IC base=+0.180)

- **PATRÓN** `sigma_ewma_delta_pct` < `10.122` → IC=+0.182 (n=542)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` < 10.122 (IC base=+0.180)

### GBM_LATE_60M
- **FILTRO** `sigma_ewma_delta_pct` < `13.491` → IC=-0.237 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 13.491
  - _Potencial_: sin este filtro IC_bueno=+0.214 (n=12)

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
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0051 (IC base=-0.014)

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
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=152)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.000 (n=152)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.056 (n=131)

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
  - _Potencial_: sin este filtro IC_bueno=+0.129 (n=87)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.160 (n=48)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 14.0 (IC base=+0.079)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.123 (n=83)

  - _Acción_: Kelly boost +0.62€ cuando `streak_len` < 4.0 (IC base=+0.079)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.129 (n=87)

  - _Acción_: Kelly boost +0.65€ cuando `libro_spread` < 0.01 (IC base=+0.079)

- **PATRÓN** `libro_liquidez` > `2635.2671` → IC=+0.141 (n=51)

  - _Acción_: Kelly boost +0.71€ cuando `libro_liquidez` > 2635.2671 (IC base=+0.079)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.191 (n=53)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 7.0 (IC base=+0.072)

- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.134 (n=39)

  - _Acción_: Kelly boost +0.67€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.072)

### STREAK_FADE_15M#ETH#15min
- **FILTRO** `hora_utc` > `7.0` → IC=-0.167 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 7.0
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

### STREAK_FADE_15M#SOL#15min
- **PATRÓN** `streak_len` < `4.0` → IC=+0.154 (n=24)

  - _Acción_: Kelly boost +0.77€ cuando `streak_len` < 4.0 (IC base=+0.128)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.167 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` > 18.0 (IC base=+0.125)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `py_entrada` < 0.485 (IC base=+0.125)

### STREAK_FADE_15M#XRP#15min
- **PATRÓN** `hora_utc` < `13.0` → IC=+0.160 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` < 13.0 (IC base=+0.086)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.167 (n=28)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.485 (IC base=+0.086)

- **PATRÓN** `regimen_ma_toques` > `4.0` → IC=+0.136 (n=20)

  - _Acción_: Kelly boost +0.68€ cuando `regimen_ma_toques` > 4.0 (IC base=+0.086)

- **PATRÓN** `volumen_racha` < `616514.5` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `volumen_racha` < 616514.5 (IC base=+0.086)

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
- **PATRÓN** `ibs_15` > `0.7617` → IC=+0.236 (n=392)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.7617 (IC base=+0.059)

- **PATRÓN** `dist_vwap_pct` > `0.1779` → IC=+0.193 (n=174)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1779 (IC base=+0.059)

- **PATRÓN** `sigma_ewma_delta_pct` > `22.986` → IC=+0.198 (n=61)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 22.986 (IC base=+0.059)

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

- **PATRÓN** `sigma_h` < `0.0077` → IC=+0.125 (n=289)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0077 (IC base=+0.104)

- **PATRÓN** `drift_60min` |x|≤ `0.2223` → IC=+0.141 (n=279)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.70€ cuando `drift_60min` |x|≤ 0.2223 (IC base=+0.104)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0631` → IC=+0.130 (n=279)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.65€ cuando `delta_ratio_macro` |x|> 0.0631 (IC base=+0.104)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.179 (n=82)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` < 8.0 (IC base=+0.104)

- **PATRÓN** `ibs_15` > `0.724` → IC=+0.250 (n=214)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.724 (IC base=+0.104)

- **PATRÓN** `dist_vwap_pct` > `0.1573` → IC=+0.240 (n=98)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1573 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` > `24.506` → IC=+0.177 (n=29)

  - _Acción_: Kelly boost +0.89€ cuando `sigma_ewma_delta_pct` > 24.506 (IC base=+0.104)

- **PATRÓN** `sigma_ewma_delta_pct` < `14.681` → IC=+0.164 (n=117)

  - _Acción_: Kelly boost +0.82€ cuando `sigma_ewma_delta_pct` < 14.681 (IC base=+0.104)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.182 (n=20)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.91€ cuando `sigma_h` < 0.0055 (IC base=+0.013)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_h` < `0.012` → IC=-0.143 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.012
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `ibs_15` > `0.6814` → IC=+0.192 (n=170)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.96€ cuando `ibs_15` > 0.6814 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` > `0.1647` → IC=+0.143 (n=82)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.1647 (IC base=+0.045)

- **PATRÓN** `dist_vwap_pct` < `0.5087` → IC=+0.134 (n=140)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.5087 (IC base=+0.045)

- **PATRÓN** `sigma_ewma_delta_pct` > `33.067` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 33.067 (IC base=+0.045)

- **PATRÓN** `sigma_h` < `0.006` → IC=+0.139 (n=167)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.006 (IC base=+0.058)

- **PATRÓN** `dist_vwap_pct` > `0.4601` → IC=+0.162 (n=63)

  - _Acción_: Kelly boost +0.81€ cuando `dist_vwap_pct` > 0.4601 (IC base=+0.058)

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

- **FILTRO** `drift_60min` |x|> `0.4844` → IC=-0.167 (n=28)
  - _Por qué funciona_: drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado
  - _Acción_: SKIP cuando `drift_60min` |x|> 0.4844
  - _Potencial_: sin este filtro IC_bueno=+0.063 (n=85)

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
  - _Potencial_: sin este filtro IC_bueno=+0.103 (n=144)

### WEEKLY_PRICE
- **FILTRO** `T_h` < `144.8242` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `T_h` < 144.8242
  - _Potencial_: sin este filtro IC_bueno=-0.056 (n=25)

- **PATRÓN** `T_h` > `146.1132` → IC=+0.410 (n=65)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 146.1132 (IC base=+0.324)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `144.6415` → IC=+0.281 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 144.6415 (IC base=+0.264)

- **PATRÓN** `T_h` > `105.6124` → IC=+0.268 (n=54)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 105.6124 (IC base=+0.264)

- **PATRÓN** `pct_dist` |x|≤ `0.7712` → IC=+0.350 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 0.7712 (IC base=+0.264)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `105.6124` → IC=+0.280 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 105.6124 (IC base=+0.242)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` < `146.1426` → IC=+0.398 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 146.1426 (IC base=+0.390)

- **PATRÓN** `T_h` > `111.9959` → IC=+0.399 (n=87)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9959 (IC base=+0.390)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.7617 sube el IC de +0.059 a +0.236 en UPDOWN_GBM#15min (n=392). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.724 sube el IC de +0.104 a +0.250 en UPDOWN_GBM#BTC#15min (n=214). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6814 sube el IC de +0.045 a +0.192 en UPDOWN_GBM#ETH#15min (n=170). Ya aplicado como kelly_boost=+0.96€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO#XRP` — IC=+0.136 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `BALLENAS_TARDIAS` — IC=+0.382 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `BALLENAS_TARDIAS#BTC#15min` — IC=+0.382 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `BALLENAS_TARDIAS#BTC` — IC=+0.382 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `BALLENAS_TARDIAS#15min` — IC=+0.382 n=32. Faltan ~8 resoluciones para umbral n≥40. ETA: ~6h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 983 | +0.133 | +53.39€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 983 | +0.133 | +53.39€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 11 | +0.064 | +1.20€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 11 | +0.064 | +1.20€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 377 | +0.144 | +19.34€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 377 | +0.144 | +19.34€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 372 | +0.144 | +13.90€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 372 | +0.144 | +13.90€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 223 | +0.091 | +18.96€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 223 | +0.091 | +18.96€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 32 | +0.382 | +4.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 32 | +0.382 | +4.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 32 | +0.382 | +4.06€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 32 | +0.382 | +4.06€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 5883 | +0.187 | +96.85€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 3864 | +0.212 | +74.27€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 257 | +0.064 | -16.58€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 736 | +0.130 | -46.49€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 1026 | +0.162 | +85.65€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 1724 | +0.195 | +44.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1287 | +0.209 | -10.78€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 85 | +0.063 | -6.79€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 342 | +0.189 | +65.95€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH | 2076 | +0.175 | -2.01€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1273 | +0.207 | +23.37€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 85 | -0.017 | -20.32€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 376 | +0.132 | -23.23€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 342 | +0.145 | +18.18€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#SOL | 2048 | +0.192 | +52.26€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1274 | +0.221 | +62.00€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 86 | +0.148 | +12.57€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 346 | +0.135 | -23.84€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 342 | +0.148 | +1.52€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#XRP | 31 | +0.136 | +0.11€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 26 | +0.107 | -2.20€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 326 | +0.308 | +9.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 326 | +0.308 | +9.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 326 | +0.308 | +9.87€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 326 | +0.308 | +9.87€ | 0 | 0 |
| ✅ GBM_LATE_15M | 7489 | +0.096 | +2330.46€ | 0 | 4 |
| ✅ GBM_LATE_15M#15min | 7489 | +0.096 | +2330.46€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 1821 | +0.067 | +306.32€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1821 | +0.067 | +306.32€ | 0 | 3 |
| ✅ GBM_LATE_15M#ETH | 1667 | +0.076 | +292.51€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1667 | +0.076 | +292.51€ | 0 | 6 |
| ✅ GBM_LATE_15M#SOL | 2018 | +0.088 | +710.58€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2018 | +0.088 | +710.58€ | 1 | 3 |
| ✅ GBM_LATE_15M#XRP | 1983 | +0.149 | +1021.05€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1983 | +0.149 | +1021.05€ | 0 | 14 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 4678 | +0.124 | +2328.64€ | 0 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 4678 | +0.124 | +2328.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1216 | +0.084 | +429.57€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1216 | +0.084 | +429.57€ | 0 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1225 | +0.092 | +447.22€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1225 | +0.092 | +447.22€ | 0 | 7 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1184 | +0.097 | +488.89€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1184 | +0.097 | +488.89€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1053 | +0.238 | +962.97€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1053 | +0.238 | +962.97€ | 0 | 11 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 251 | +0.105 | +112.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 251 | +0.105 | +112.21€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC | 9 | -0.102 | -1.94€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 9 | -0.102 | -1.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 90 | +0.000 | +15.63€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 90 | +0.000 | +15.63€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL | 8 | -0.120 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 8 | -0.120 | -1.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 144 | +0.219 | +100.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 144 | +0.219 | +100.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 4718 | +0.076 | +1354.87€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO#15min | 4718 | +0.076 | +1354.87€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1143 | +0.035 | +143.64€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1143 | +0.035 | +143.64€ | 0 | 3 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1141 | +0.029 | +87.62€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1141 | +0.029 | +87.62€ | 0 | 1 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1094 | +0.038 | +220.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1094 | +0.038 | +220.08€ | 1 | 2 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1340 | +0.180 | +903.53€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1340 | +0.180 | +903.53€ | 0 | 9 |
| ✅ GBM_LATE_5M | 552 | -0.025 | +3.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#5min | 552 | -0.025 | +3.52€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 156 | -0.013 | -9.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 156 | -0.013 | -9.28€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH | 61 | -0.135 | -8.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#ETH#5min | 61 | -0.135 | -8.43€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL | 98 | -0.160 | +5.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 98 | -0.160 | +5.33€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 237 | +0.052 | +15.90€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 237 | +0.052 | +15.90€ | 0 | 0 |
| ✅ GBM_LATE_60M | 337 | -0.111 | +4.86€ | 3 | 1 |
| ✅ GBM_LATE_60M#60min | 337 | -0.111 | +4.86€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 120 | -0.041 | +3.25€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 120 | -0.041 | +3.25€ | 4 | 1 |
| ✅ GBM_LATE_60M#ETH | 107 | -0.142 | -9.65€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 107 | -0.142 | -9.65€ | 4 | 0 |
| ✅ GBM_LATE_60M#SOL | 110 | -0.152 | +11.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 110 | -0.152 | +11.27€ | 5 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO | 9 | -0.143 | -2.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO#60min | 9 | -0.143 | -2.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 350 | -0.051 | -3.04€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 350 | -0.051 | -3.04€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 350 | -0.051 | -3.04€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 350 | -0.051 | -3.04€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 272 | +0.015 | +11.36€ | 1 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 272 | +0.015 | +11.36€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 272 | +0.015 | +11.36€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 272 | +0.015 | +11.36€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1661 | +0.012 | +12.78€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1525 | +0.008 | +0.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 212 | +0.037 | +5.14€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 212 | +0.037 | +5.14€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 222 | +0.000 | -2.18€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 222 | +0.000 | -2.18€ | 1 | 0 |
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
| ✅ RESOLUTION_SNIPER | 13 | +0.195 | +3.10€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#ETH#sniper | 5 | +0.018 | +1.41€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 6 | +0.113 | +1.44€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 6 | +0.113 | +1.44€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 13 | +0.195 | +3.10€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 281 | +0.076 | +27.98€ | 1 | 6 |
| ✅ STREAK_FADE_15M#15min | 281 | +0.076 | +27.98€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 60 | +0.032 | -3.65€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 60 | +0.032 | -3.65€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 87 | +0.129 | +22.47€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 87 | +0.129 | +22.47€ | 0 | 3 |
| ✅ STREAK_FADE_15M#XRP | 134 | +0.059 | +9.17€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 134 | +0.059 | +9.17€ | 0 | 4 |
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
| ✅ UPDOWN_GBM | 2481 | +0.035 | +232.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2218 | +0.055 | +271.06€ | 0 | 3 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 130 | -0.061 | -11.21€ | 6 | 0 |
| ✅ UPDOWN_GBM#BNB | 244 | +0.061 | +50.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 244 | +0.061 | +50.07€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 546 | +0.053 | +66.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 462 | +0.088 | +81.34€ | 1 | 9 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 43 | -0.078 | -6.67€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 189 | +0.039 | +20.87€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 186 | +0.043 | +21.77€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1001 | +0.037 | +69.72€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 907 | +0.052 | +81.29€ | 0 | 6 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 55 | -0.026 | -3.07€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 239 | -0.052 | -7.48€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 170 | -0.023 | -1.05€ | 5 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 32 | -0.088 | -1.46€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 260 | +0.046 | +34.35€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 249 | +0.058 | +37.64€ | 4 | 0 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 144 | +0.308 | +31.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 144 | +0.308 | +31.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 68 | +0.300 | +11.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 68 | +0.300 | +11.95€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 76 | +0.308 | +19.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 76 | +0.308 | +19.77€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 1581 | +0.165 | +748.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 1581 | +0.165 | +748.09€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 146 | +0.196 | +82.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 146 | +0.196 | +82.51€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 177 | +0.120 | +34.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 177 | +0.120 | +34.71€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 145 | +0.214 | +98.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 145 | +0.214 | +98.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 318 | +0.175 | +132.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 318 | +0.175 | +132.37€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 379 | +0.109 | +112.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 379 | +0.109 | +112.63€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 416 | +0.196 | +287.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 416 | +0.196 | +287.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 14 | +0.044 | +0.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 14 | +0.044 | +0.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 14 | +0.044 | +0.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 14 | +0.044 | +0.65€ | 0 | 0 |
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
| ✅ WEEKLY_PRICE | 369 | +0.198 | +72.27€ | 1 | 1 |
| ✅ WEEKLY_PRICE#BTC | 108 | +0.136 | -8.97€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 102 | +0.135 | -7.57€ | 0 | 1 |
| ✅ WEEKLY_PRICE#SOL | 159 | +0.276 | +88.82€ | 0 | 2 |