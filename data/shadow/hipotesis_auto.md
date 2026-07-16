# Hipótesis automáticas — 2026-07-16 06:47 UTC
_Generado por shadow_postmortem.py sobre 16587 resoluciones (PNL=+3376.49€)_

## Patrones causales activos

### FAVORITO_CONFIRMADO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.184 (n=804)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` > 8.0 (IC base=+0.183)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.192 (n=918)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 18.0 (IC base=+0.183)

- **PATRÓN** `py_entrada` > `0.695` → IC=+0.291 (n=414)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.695 (IC base=+0.183)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.189 (n=1042)

  - _Acción_: Kelly boost +0.94€ cuando `libro_spread` < 0.01 (IC base=+0.183)

- **PATRÓN** `libro_liquidez` > `4371.9525` → IC=+0.187 (n=595)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 4371.9525 (IC base=+0.183)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.197 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 17.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.192 (n=368)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 6.0 (IC base=+0.162)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.329 (n=332)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.162)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.172 (n=1092)

  - _Acción_: Kelly boost +0.86€ cuando `libro_spread` < 0.01 (IC base=+0.162)

- **PATRÓN** `libro_liquidez` > `7377.4888` → IC=+0.184 (n=318)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 7377.4888 (IC base=+0.162)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.201 (n=172)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.202)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.235 (n=66)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` > `0.615` → IC=+0.253 (n=176)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.615 (IC base=+0.202)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.236 (n=70)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.205)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.223 (n=146)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.205)

- **PATRÓN** `py_entrada` < `0.225` → IC=+0.403 (n=70)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.225 (IC base=+0.205)

- **PATRÓN** `libro_liquidez` > `7163.0167` → IC=+0.211 (n=185)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7163.0167 (IC base=+0.205)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.135 (n=50)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 5.0 (IC base=+0.132)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.194 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.97€ cuando `hora_utc` < 12.0 (IC base=+0.132)

- **PATRÓN** `py_entrada` < `0.565` → IC=+0.167 (n=25)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` < 0.565 (IC base=+0.132)

- **PATRÓN** `py_entrada` > `0.585` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` > 0.585 (IC base=+0.132)

- **PATRÓN** `libro_liquidez` > `7023.9191` → IC=+0.138 (n=45)

  - _Acción_: Kelly boost +0.69€ cuando `libro_liquidez` > 7023.9191 (IC base=+0.132)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.214 (n=19)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.153)

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.267 (n=28)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 9.0 (IC base=+0.153)

- **PATRÓN** `py_entrada` < `0.425` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.425 (IC base=+0.153)

- **PATRÓN** `py_entrada` > `0.395` → IC=+0.154 (n=50)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` > 0.395 (IC base=+0.153)

- **PATRÓN** `libro_liquidez` > `7670.1712` → IC=+0.218 (n=37)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 7670.1712 (IC base=+0.153)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.234 (n=175)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.230 (n=198)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.351 (n=92)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.246 (n=69)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.202)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.367 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.202)

- **PATRÓN** `libro_liquidez` > `3759.4964` → IC=+0.212 (n=203)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 3759.4964 (IC base=+0.202)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` < `17.0` → IC=+0.235 (n=47)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.181)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.318 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.575 (IC base=+0.181)

- **PATRÓN** `libro_liquidez` > `6370.4495` → IC=+0.200 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 6370.4495 (IC base=+0.181)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.150 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 17.0 (IC base=+0.134)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.239 (n=21)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.134)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.250 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.134)

- **PATRÓN** `libro_liquidez` > `4587.4443` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `libro_liquidez` > 4587.4443 (IC base=+0.134)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.228 (n=200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.223)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.229 (n=94)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.223)

- **PATRÓN** `py_entrada` > `0.62` → IC=+0.286 (n=171)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.62 (IC base=+0.223)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.240 (n=102)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 15.0 (IC base=+0.204)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.223 (n=92)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 7.0 (IC base=+0.204)

- **PATRÓN** `py_entrada` < `0.365` → IC=+0.261 (n=178)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.365 (IC base=+0.204)

### FAVORITO_CONFIRMADO#SOL#60min
- **PATRÓN** `hora_utc` > `19.0` → IC=+0.200 (n=18)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 19.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.208 (n=22)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` < `0.64` → IC=+0.174 (n=44)

  - _Acción_: Kelly boost +0.87€ cuando `py_entrada` < 0.64 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.615` → IC=+0.139 (n=34)

  - _Acción_: Kelly boost +0.69€ cuando `py_entrada` > 0.615 (IC base=+0.142)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.143 (n=26)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.71€ cuando `hora_utc` > 15.0 (IC base=+0.079)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.121 (n=27)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 7.0 (IC base=+0.079)

- **PATRÓN** `py_entrada` < `0.335` → IC=+0.309 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.335 (IC base=+0.079)

### GBM_LATE_15M
- **PATRÓN** `dist_vwap_pct` > `0.5999` → IC=+0.131 (n=128)

  - _Acción_: Kelly boost +0.65€ cuando `dist_vwap_pct` > 0.5999 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.173` → IC=+0.225 (n=96)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.173 (IC base=+0.108)

- **PATRÓN** `sigma_h` > `0.0091` → IC=+0.134 (n=1225)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0091 (IC base=+0.106)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.131 (n=1335)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` < 12.0 (IC base=+0.106)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.147` → IC=+0.123 (n=136)

  - _Acción_: Kelly boost +0.62€ cuando `sigma_ewma_delta_pct` > 6.147 (IC base=+0.106)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.2776` → IC=+0.133 (n=28)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` > 0.2776 (IC base=+0.074)

- **PATRÓN** `sigma_ewma_delta_pct` > `15.305` → IC=+0.237 (n=17)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 15.305 (IC base=+0.074)

- **PATRÓN** `dist_vwap_pct` < `0.49` → IC=+0.125 (n=150)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.49 (IC base=+0.063)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.004` → IC=+0.202 (n=55)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.004 (IC base=+0.063)

### GBM_LATE_15M#ETH#15min
- **FILTRO** `sigma_ewma_delta_pct` < `7.25` → IC=-0.132 (n=36)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 7.25
  - _Potencial_: sin este filtro IC_bueno=+0.271 (n=46)

- **PATRÓN** `sigma_h` < `0.0045` → IC=+0.154 (n=128)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0045 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.6749` → IC=+0.143 (n=26)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.6749 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` < `0.283` → IC=+0.125 (n=54)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.283 (IC base=+0.094)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.25` → IC=+0.271 (n=46)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.25 (IC base=+0.094)

- **PATRÓN** `dist_vwap_pct` > `0.7151` → IC=+0.146 (n=46)

  - _Acción_: Kelly boost +0.73€ cuando `dist_vwap_pct` > 0.7151 (IC base=+0.067)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.447` → IC=+0.198 (n=41)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` > 7.447 (IC base=+0.067)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `8.125` → IC=-0.278 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.125
  - _Potencial_: sin este filtro IC_bueno=+0.108 (n=151)

- **PATRÓN** `sigma_h` < `0.0108` → IC=+0.140 (n=209)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.70€ cuando `sigma_h` < 0.0108 (IC base=+0.111)

- **PATRÓN** `hora_utc` > `16.0` → IC=+0.141 (n=218)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` > 16.0 (IC base=+0.111)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.477` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.477 (IC base=+0.111)

- **PATRÓN** `sigma_h` < `0.0115` → IC=+0.145 (n=311)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0115 (IC base=+0.129)

- **PATRÓN** `sigma_h` > `0.0092` → IC=+0.133 (n=464)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.67€ cuando `sigma_h` > 0.0092 (IC base=+0.129)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.179 (n=210)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 7.0 (IC base=+0.129)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_h` < `0.0305` → IC=+0.148 (n=444)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` < 0.0305 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0239` → IC=+0.180 (n=201)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.90€ cuando `sigma_h` > 0.0239 (IC base=+0.148)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.156 (n=469)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 5.0 (IC base=+0.148)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.153 (n=301)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 11.0 (IC base=+0.148)

- **PATRÓN** `dist_vwap_pct` > `0.6506` → IC=+0.227 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6506 (IC base=+0.148)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.138` → IC=+0.190 (n=27)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` > 9.138 (IC base=+0.148)

- **PATRÓN** `sigma_h` > `0.0273` → IC=+0.215 (n=156)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0273 (IC base=+0.163)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.237 (n=177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` > `0.3145` → IC=+0.143 (n=54)

  - _Acción_: Kelly boost +0.71€ cuando `dist_vwap_pct` > 0.3145 (IC base=+0.163)

- **PATRÓN** `dist_vwap_pct` < `0.5138` → IC=+0.139 (n=178)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.5138 (IC base=+0.163)

- **PATRÓN** `sigma_ewma_delta_pct` < `7.494` → IC=+0.132 (n=161)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` < 7.494 (IC base=+0.163)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0108` → IC=+0.222 (n=329)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0108 (IC base=+0.160)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.173 (n=518)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.87€ cuando `hora_utc` > 12.0 (IC base=+0.160)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.167 (n=751)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 18.0 (IC base=+0.160)

- **PATRÓN** `dist_vwap_pct` > `0.1486` → IC=+0.194 (n=286)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.1486 (IC base=+0.160)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.022` → IC=+0.311 (n=88)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.022 (IC base=+0.160)

- **PATRÓN** `sigma_h` > `0.0048` → IC=+0.178 (n=741)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.89€ cuando `sigma_h` > 0.0048 (IC base=+0.162)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.165 (n=496)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 12.0 (IC base=+0.162)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.190 (n=259)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 5.0 (IC base=+0.162)

- **PATRÓN** `dist_vwap_pct` < `0.4123` → IC=+0.196 (n=515)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` < 0.4123 (IC base=+0.162)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.032` → IC=+0.276 (n=47)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.032 (IC base=+0.162)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `sigma_h` > `0.0032` → IC=+0.148 (n=157)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0032 (IC base=+0.113)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.161 (n=125)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.81€ cuando `hora_utc` > 12.0 (IC base=+0.113)

- **PATRÓN** `dist_vwap_pct` > `0.5034` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.5034 (IC base=+0.113)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.074` → IC=+0.224 (n=27)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.074 (IC base=+0.113)

- **PATRÓN** `sigma_h` > `0.0028` → IC=+0.175 (n=186)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.0028 (IC base=+0.140)

- **PATRÓN** `hora_utc` > `15.0` → IC=+0.163 (n=90)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` > 15.0 (IC base=+0.140)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.140 (n=134)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.70€ cuando `hora_utc` < 12.0 (IC base=+0.140)

- **PATRÓN** `dist_vwap_pct` < `0.4825` → IC=+0.133 (n=148)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.4825 (IC base=+0.140)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.17` → IC=+0.318 (n=31)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.17 (IC base=+0.140)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.0068` → IC=+0.236 (n=89)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0068 (IC base=+0.145)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.159 (n=136)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 12.0 (IC base=+0.145)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.167 (n=205)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 18.0 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` > `0.699` → IC=+0.181 (n=45)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.699 (IC base=+0.145)

- **PATRÓN** `dist_vwap_pct` < `1.1335` → IC=+0.138 (n=139)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 1.1335 (IC base=+0.145)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.728` → IC=+0.405 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.728 (IC base=+0.145)

- **PATRÓN** `sigma_h` < `0.0068` → IC=+0.143 (n=166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` < 0.0068 (IC base=+0.136)

- **PATRÓN** `sigma_h` > `0.0037` → IC=+0.154 (n=189)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` > 0.0037 (IC base=+0.136)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.177 (n=63)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 18.0 (IC base=+0.136)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.191 (n=66)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.96€ cuando `hora_utc` < 5.0 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` > `0.7151` → IC=+0.196 (n=44)

  - _Acción_: Kelly boost +0.98€ cuando `dist_vwap_pct` > 0.7151 (IC base=+0.136)

- **PATRÓN** `dist_vwap_pct` < `0.3807` → IC=+0.179 (n=104)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` < 0.3807 (IC base=+0.136)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.0` → IC=+0.240 (n=48)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.0 (IC base=+0.136)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `3.13` → IC=-0.167 (n=16)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 3.13
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=113)

- **PATRÓN** `sigma_h` > `0.013` → IC=+0.217 (n=90)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.013 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.156 (n=187)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` > 8.0 (IC base=+0.143)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.148 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 6.0 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.4285` → IC=+0.185 (n=52)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.4285 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `1.0397` → IC=+0.156 (n=149)

  - _Acción_: Kelly boost +0.78€ cuando `dist_vwap_pct` < 1.0397 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.082` → IC=+0.288 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 4.082 (IC base=+0.143)

- **PATRÓN** `sigma_h` < `0.0082` → IC=+0.186 (n=68)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.0082 (IC base=+0.100)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.145 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` < 5.0 (IC base=+0.100)

- **PATRÓN** `dist_vwap_pct` < `0.2503` → IC=+0.167 (n=121)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` < 0.2503 (IC base=+0.100)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.13` → IC=+0.152 (n=113)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 3.13 (IC base=+0.100)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` < `0.0214` → IC=+0.274 (n=157)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0214 (IC base=+0.248)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.252 (n=143)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.248)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.289 (n=140)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 15.0 (IC base=+0.248)

- **PATRÓN** `dist_vwap_pct` > `0.7553` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7553 (IC base=+0.248)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.511` → IC=+0.361 (n=34)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.511 (IC base=+0.248)

- **PATRÓN** `sigma_h` < `0.0165` → IC=+0.292 (n=166)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0165 (IC base=+0.288)

- **PATRÓN** `sigma_h` > `0.0086` → IC=+0.320 (n=165)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0086 (IC base=+0.288)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.296 (n=111)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.288)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.310 (n=56)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` > `0.1789` → IC=+0.300 (n=38)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.1789 (IC base=+0.288)

- **PATRÓN** `dist_vwap_pct` < `0.5145` → IC=+0.307 (n=138)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` < 0.5145 (IC base=+0.288)

- **PATRÓN** `sigma_ewma_delta_pct` < `3.048` → IC=+0.314 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 3.048 (IC base=+0.288)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.015` → IC=+0.195 (n=224)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.97€ cuando `sigma_h` > 0.015 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.124 (n=703)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` < 18.0 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` > `0.3418` → IC=+0.172 (n=175)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.3418 (IC base=+0.114)

- **PATRÓN** `dist_vwap_pct` < `0.1365` → IC=+0.151 (n=239)

  - _Acción_: Kelly boost +0.76€ cuando `dist_vwap_pct` < 0.1365 (IC base=+0.114)

- **PATRÓN** `sigma_ewma_delta_pct` > `13.023` → IC=+0.345 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 13.023 (IC base=+0.114)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.127 (n=301)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.64€ cuando `hora_utc` < 6.0 (IC base=+0.088)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `dist_vwap_pct` > `0.4395` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.4395 (IC base=+0.087)

- **PATRÓN** `dist_vwap_pct` < `0.1006` → IC=+0.133 (n=58)

  - _Acción_: Kelly boost +0.67€ cuando `dist_vwap_pct` < 0.1006 (IC base=+0.087)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.969` → IC=+0.204 (n=25)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.969 (IC base=+0.087)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.123 (n=67)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.62€ cuando `hora_utc` > 17.0 (IC base=+0.069)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.462` → IC=+0.121 (n=56)

  - _Acción_: Kelly boost +0.60€ cuando `sigma_ewma_delta_pct` > 3.462 (IC base=+0.069)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_h` < `0.0039` → IC=+0.150 (n=58)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.75€ cuando `sigma_h` < 0.0039 (IC base=+0.062)

- **PATRÓN** `dist_vwap_pct` < `1.1151` → IC=+0.124 (n=99)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 1.1151 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.175` → IC=+0.326 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.175 (IC base=+0.062)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.821` → IC=+0.167 (n=19)

  - _Acción_: Kelly boost +0.83€ cuando `sigma_ewma_delta_pct` > 7.821 (IC base=+0.017)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` < `7.311` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 7.311
  - _Potencial_: sin este filtro IC_bueno=+0.367 (n=43)

- **FILTRO** `dist_vwap_pct` > `0.8313` → IC=-0.265 (n=15)

  - _Acción_: SKIP cuando `dist_vwap_pct` > 0.8313
  - _Potencial_: sin este filtro IC_bueno=+0.083 (n=149)

- **FILTRO** `sigma_ewma_delta_pct` > `2.471` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 2.471
  - _Potencial_: sin este filtro IC_bueno=+0.064 (n=115)

- **PATRÓN** `sigma_h` > `0.0129` → IC=+0.139 (n=70)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0129 (IC base=+0.085)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.158 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 8.0 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` > `0.9118` → IC=+0.167 (n=16)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.9118 (IC base=+0.085)

- **PATRÓN** `dist_vwap_pct` < `0.1689` → IC=+0.148 (n=52)

  - _Acción_: Kelly boost +0.74€ cuando `dist_vwap_pct` < 0.1689 (IC base=+0.085)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.311` → IC=+0.367 (n=43)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.311 (IC base=+0.085)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.120 (n=77)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` < 6.0 (IC base=+0.036)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` > `0.0115` → IC=+0.214 (n=197)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0115 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `5.0` → IC=+0.200 (n=208)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 5.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.246 (n=69)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.201)

- **PATRÓN** `dist_vwap_pct` > `0.3134` → IC=+0.276 (n=56)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.3134 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.863` → IC=+0.214 (n=33)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.863 (IC base=+0.201)

- **PATRÓN** `sigma_ewma_delta_pct` < `4.107` → IC=+0.218 (n=69)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` < 4.107 (IC base=+0.201)

- **PATRÓN** `sigma_h` < `0.011` → IC=+0.195 (n=103)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.98€ cuando `sigma_h` < 0.011 (IC base=+0.193)

- **PATRÓN** `sigma_h` > `0.0262` → IC=+0.250 (n=78)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0262 (IC base=+0.193)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.250 (n=86)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 6.0 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` > `0.3031` → IC=+0.179 (n=51)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.3031 (IC base=+0.193)

- **PATRÓN** `dist_vwap_pct` < `0.4841` → IC=+0.178 (n=175)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` < 0.4841 (IC base=+0.193)

- **PATRÓN** `sigma_ewma_delta_pct` < `2.517` → IC=+0.191 (n=137)

  - _Acción_: Kelly boost +0.95€ cuando `sigma_ewma_delta_pct` < 2.517 (IC base=+0.193)

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
- **PATRÓN** `py_entrada` < `0.48` → IC=+0.150 (n=18)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.48 (IC base=+0.056)

- **PATRÓN** `libro_liquidez` > `2012.2085` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2012.2085 (IC base=+0.056)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.495 (IC base=+0.127)

- **PATRÓN** `btc_momentum` |x|≤ `0.03` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `btc_momentum` |x|≤ 0.03 (IC base=+0.127)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **PATRÓN** `py_entrada` < `0.48` → IC=+0.150 (n=18)

  - _Acción_: Kelly boost +0.75€ cuando `py_entrada` < 0.48 (IC base=+0.056)

- **PATRÓN** `libro_liquidez` > `2012.2085` → IC=+0.122 (n=35)

  - _Acción_: Kelly boost +0.61€ cuando `libro_liquidez` > 2012.2085 (IC base=+0.056)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.181 (n=45)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.90€ cuando `hora_utc` < 15.0 (IC base=+0.127)

- **PATRÓN** `py_entrada` < `0.495` → IC=+0.214 (n=26)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.495 (IC base=+0.127)

- **PATRÓN** `btc_momentum` |x|≤ `0.03` → IC=+0.153 (n=47)

  - _Acción_: Kelly boost +0.77€ cuando `btc_momentum` |x|≤ 0.03 (IC base=+0.127)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.073 (n=87)

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

- **FILTRO** `sigma_h` > `0.0055` → IC=-0.363 (n=71)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0055
  - _Potencial_: sin este filtro IC_bueno=+0.231 (n=24)

- **FILTRO** `T_h` < `144.7669` → IC=-0.432 (n=42)

  - _Acción_: SKIP cuando `T_h` < 144.7669
  - _Potencial_: sin este filtro IC_bueno=-0.300 (n=23)

- **FILTRO** `pct_vs_K` |x|> `2.6724` → IC=-0.480 (n=48)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 2.6724
  - _Potencial_: sin este filtro IC_bueno=-0.132 (n=17)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.231 (n=24)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0055 (IC base=-0.211)

### PRICE_TARGET_GBM#ETH#atexpiry
- **FILTRO** `sigma_h` > `0.0077` → IC=-0.429 (n=26)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: SKIP cuando `sigma_h` > 0.0077
  - _Potencial_: sin este filtro IC_bueno=+0.167 (n=10)

- **FILTRO** `T_h` > `98.7549` → IC=-0.452 (n=19)

  - _Acción_: SKIP cuando `T_h` > 98.7549
  - _Potencial_: sin este filtro IC_bueno=-0.389 (n=7)

- **FILTRO** `T_h` < `145.9196` → IC=-0.452 (n=19)

  - _Acción_: SKIP cuando `T_h` < 145.9196
  - _Potencial_: sin este filtro IC_bueno=-0.389 (n=7)

- **FILTRO** `pct_vs_K` |x|> `3.4276` → IC=-0.447 (n=17)

  - _Acción_: SKIP cuando `pct_vs_K` |x|> 3.4276
  - _Potencial_: sin este filtro IC_bueno=-0.409 (n=9)

### STREAK_FADE_15M
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.186 (n=49)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.93€ cuando `hora_utc` > 11.0 (IC base=+0.110)

- **PATRÓN** `py_entrada` < `0.505` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` < 0.505 (IC base=+0.110)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.183 (n=58)

  - _Acción_: Kelly boost +0.92€ cuando `streak_len` < 4.0 (IC base=+0.110)

- **PATRÓN** `regimen_ma_toques` > `3.0` → IC=+0.129 (n=33)

  - _Acción_: Kelly boost +0.64€ cuando `regimen_ma_toques` > 3.0 (IC base=+0.110)

- **PATRÓN** `volumen_racha` < `249969.2` → IC=+0.203 (n=35)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 249969.2 (IC base=+0.110)

- **PATRÓN** `libro_liquidez` > `1959.3298` → IC=+0.173 (n=47)

  - _Acción_: Kelly boost +0.87€ cuando `libro_liquidez` > 1959.3298 (IC base=+0.110)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.257 (n=35)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.085)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.135 (n=50)

  - _Acción_: Kelly boost +0.67€ cuando `py_entrada` < 0.485 (IC base=+0.085)

- **PATRÓN** `regimen_ma_toques` > `5.0` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `regimen_ma_toques` > 5.0 (IC base=+0.085)

- **PATRÓN** `volumen_racha` < `234964.8` → IC=+0.207 (n=39)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 234964.8 (IC base=+0.085)

### STREAK_FADE_15M#SOL#15min
- **PATRÓN** `hora_utc` > `11.0` → IC=+0.222 (n=16)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 11.0 (IC base=+0.176)

- **PATRÓN** `py_entrada` < `0.485` → IC=+0.208 (n=22)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.485 (IC base=+0.183)

### STREAK_FADE_15M#XRP#15min
- **FILTRO** `hora_utc` > `12.0` → IC=-0.136 (n=20)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 12.0
  - _Potencial_: sin este filtro IC_bueno=+0.152 (n=21)

- **PATRÓN** `hora_utc` > `7.0` → IC=+0.130 (n=25)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 7.0 (IC base=+0.051)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.184 (n=17)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 7.0 (IC base=+0.012)

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
  - _Potencial_: sin este filtro IC_bueno=-0.011 (n=129)

- **FILTRO** `libro_spread` > `0.01` → IC=-0.154 (n=76)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=+0.071 (n=75)

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

- **PATRÓN** `hora_utc` < `9.0` → IC=+0.154 (n=24)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.77€ cuando `hora_utc` < 9.0 (IC base=+0.048)

- **PATRÓN** `py_entrada` > `0.505` → IC=+0.167 (n=22)

  - _Acción_: Kelly boost +0.83€ cuando `py_entrada` > 0.505 (IC base=+0.048)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `libro_spread` < 0.01 (IC base=+0.048)

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
- **FILTRO** `sigma_ewma_delta_pct` > `20.272` → IC=-0.136 (n=20)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 20.272
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=153)

- **PATRÓN** `ibs_15` > `0.7204` → IC=+0.180 (n=264)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.90€ cuando `ibs_15` > 0.7204 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.7415` → IC=+0.194 (n=34)

  - _Acción_: Kelly boost +0.97€ cuando `dist_vwap_pct` > 0.7415 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` < `0.5084` → IC=+0.145 (n=167)

  - _Acción_: Kelly boost +0.72€ cuando `dist_vwap_pct` < 0.5084 (IC base=+0.028)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.541` → IC=+0.152 (n=44)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 3.541 (IC base=+0.028)

- **PATRÓN** `dist_vwap_pct` > `0.8904` → IC=+0.140 (n=23)

  - _Acción_: Kelly boost +0.70€ cuando `dist_vwap_pct` > 0.8904 (IC base=+0.047)

- **PATRÓN** `sigma_ewma_delta_pct` < `16.748` → IC=+0.128 (n=146)

  - _Acción_: Kelly boost +0.64€ cuando `sigma_ewma_delta_pct` < 16.748 (IC base=+0.047)

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
- **FILTRO** `ibs_15` > `0.0522` → IC=-0.167 (n=22)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.0522
  - _Potencial_: sin este filtro IC_bueno=+0.180 (n=23)

- **PATRÓN** `drift_60min` |x|≤ `0.2412` → IC=+0.130 (n=190)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.65€ cuando `drift_60min` |x|≤ 0.2412 (IC base=+0.077)

- **PATRÓN** `hora_utc` > `11.0` → IC=+0.158 (n=159)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 11.0 (IC base=+0.077)

- **PATRÓN** `ibs_15` < `0.9306` → IC=+0.141 (n=151)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.70€ cuando `ibs_15` < 0.9306 (IC base=+0.077)

- **PATRÓN** `ibs_15` > `0.6354` → IC=+0.197 (n=150)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.99€ cuando `ibs_15` > 0.6354 (IC base=+0.077)

- **PATRÓN** `dist_vwap_pct` > `0.7736` → IC=+0.300 (n=18)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.7736 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.517` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 4.517 (IC base=+0.077)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.986` → IC=+0.158 (n=36)

  - _Acción_: Kelly boost +0.79€ cuando `sigma_ewma_delta_pct` < 5.986 (IC base=+0.077)

- **PATRÓN** `pct_spot_vs_ref` |x|≤ `0.0535` → IC=+0.129 (n=33)
  - _Por qué funciona_: precio spot cerca de la referencia → señal GBM más calibrada
  - _Acción_: Kelly boost +0.64€ cuando `pct_spot_vs_ref` |x|≤ 0.0535 (IC base=+0.022)

- **PATRÓN** `sigma_h` < `0.0056` → IC=+0.289 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0056 (IC base=+0.022)

- **PATRÓN** `ibs_15` < `0.0522` → IC=+0.180 (n=23)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.90€ cuando `ibs_15` < 0.0522 (IC base=+0.022)

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
- **FILTRO** `sigma_ewma_delta_pct` < `21.876` → IC=-0.140 (n=23)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 21.876
  - _Potencial_: sin este filtro IC_bueno=+0.333 (n=4)

- **FILTRO** `sigma_ewma_delta_pct` > `21.947` → IC=-0.147 (n=15)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 21.947
  - _Potencial_: sin este filtro IC_bueno=+0.113 (n=73)

- **PATRÓN** `ibs_15` > `0.7617` → IC=+0.184 (n=93)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.92€ cuando `ibs_15` > 0.7617 (IC base=+0.022)

- **PATRÓN** `dist_vwap_pct` < `0.5087` → IC=+0.125 (n=78)

  - _Acción_: Kelly boost +0.62€ cuando `dist_vwap_pct` < 0.5087 (IC base=+0.022)

- **PATRÓN** `sigma_h` < `0.0059` → IC=+0.121 (n=85)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.60€ cuando `sigma_h` < 0.0059 (IC base=+0.046)

- **PATRÓN** `dist_vwap_pct` > `0.9454` → IC=+0.182 (n=20)

  - _Acción_: Kelly boost +0.91€ cuando `dist_vwap_pct` > 0.9454 (IC base=+0.046)

- **PATRÓN** `sigma_ewma_delta_pct` < `15.796` → IC=+0.127 (n=65)

  - _Acción_: Kelly boost +0.63€ cuando `sigma_ewma_delta_pct` < 15.796 (IC base=+0.046)

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

- **FILTRO** `ibs_15` > `0.0669` → IC=-0.150 (n=18)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.0669
  - _Potencial_: sin este filtro IC_bueno=+0.149 (n=35)

- **PATRÓN** `sigma_h` < `0.0112` → IC=+0.184 (n=17)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.92€ cuando `sigma_h` < 0.0112 (IC base=+0.097)

- **PATRÓN** `sigma_h` > `0.0172` → IC=+0.132 (n=17)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.66€ cuando `sigma_h` > 0.0172 (IC base=+0.097)

- **PATRÓN** `drift_15min` |x|≤ `0.7907` → IC=+0.125 (n=30)

  - _Acción_: Kelly boost +0.62€ cuando `drift_15min` |x|≤ 0.7907 (IC base=+0.097)

- **PATRÓN** `delta_ratio_macro` |x|> `0.1253` → IC=+0.125 (n=30)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.62€ cuando `delta_ratio_macro` |x|> 0.1253 (IC base=+0.097)

- **PATRÓN** `ibs_15` < `0.0669` → IC=+0.149 (n=35)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.74€ cuando `ibs_15` < 0.0669 (IC base=+0.097)

### WEEKLY_PRICE
- **FILTRO** `T_h` < `144.7646` → IC=-0.292 (n=22)

  - _Acción_: SKIP cuando `T_h` < 144.7646
  - _Potencial_: sin este filtro IC_bueno=-0.125 (n=22)

- **PATRÓN** `T_h` > `87.9936` → IC=+0.293 (n=114)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 87.9936 (IC base=+0.279)

### WEEKLY_PRICE#BTC
- **PATRÓN** `T_h` < `144.6231` → IC=+0.239 (n=21)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 144.6231 (IC base=+0.238)

- **PATRÓN** `T_h` > `144.7029` → IC=+0.265 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 144.7029 (IC base=+0.238)

- **PATRÓN** `pct_dist` |x|≤ `2.3456` → IC=+0.300 (n=23)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 2.3456 (IC base=+0.238)

### WEEKLY_PRICE#ETH
- **PATRÓN** `T_h` > `135.9981` → IC=+0.262 (n=19)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 135.9981 (IC base=+0.218)

- **PATRÓN** `pct_dist` |x|≤ `2.4966` → IC=+0.227 (n=20)

  - _Acción_: Kelly boost +1.00€ cuando `pct_dist` |x|≤ 2.4966 (IC base=+0.218)

### WEEKLY_PRICE#SOL
- **PATRÓN** `T_h` < `146.1132` → IC=+0.331 (n=57)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` < 146.1132 (IC base=+0.318)

- **PATRÓN** `T_h` > `111.9928` → IC=+0.330 (n=51)

  - _Acción_: Kelly boost +1.00€ cuando `T_h` > 111.9928 (IC base=+0.318)

## Estrategias nuevas sugeridas
_Derivadas de los patrones aprendidos:_

- **H-HORA-OF**: ORDER_FLOW_5M tiene IC=-0.122 cuando hora_utc > 4.0. Añadir hora 4 a ORDER_FLOW_BLACKLIST_HOURS si n≥20.
- **H-IBS-UPDOWN_GBM#15min**: IBS > 0.7204 correlaciona con éxito en UPDOWN_GBM#15min (IC=+0.180 n=264). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#BTC#15min**: IBS > 0.6354 correlaciona con éxito en UPDOWN_GBM#BTC#15min (IC=+0.197 n=150). Confirma señal de reversión media → alinear con BUY_NO.
- **H-IBS-UPDOWN_GBM#BTC#15min**: IBS < 0.0522 correlaciona con éxito en UPDOWN_GBM#BTC#15min (IC=+0.180 n=23). Confirma señal de reversión media → alinear con BUY_YES.
- **H-IBS-UPDOWN_GBM#ETH#15min**: IBS > 0.7617 correlaciona con éxito en UPDOWN_GBM#ETH#15min (IC=+0.184 n=93). Confirma señal de reversión media → alinear con BUY_NO.
- **LIVE-CANDIDATA**: `GBM_LATE_15M_PYCONFIRMADO#XRP#15min` — IC=+0.244 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `GBM_LATE_15M_PYCONFIRMADO#XRP` — IC=+0.244 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_SOL_ALTACONVICCION` — IC=+0.288 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min` — IC=+0.288 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL` — IC=+0.288 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min` — IC=+0.288 n=31. Faltan ~9 resoluciones para umbral n≥40. ETA: ~6h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_TARDIO#SOL#15min` — IC=+0.192 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_TARDIO#SOL` — IC=+0.192 n=37. Faltan ~3 resoluciones para umbral n≥40. ETA: ~2h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_TARDIO#ETH#15min` — IC=+0.194 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.
- **LIVE-CANDIDATA**: `UPDOWN_GBM_15M_TARDIO#ETH` — IC=+0.194 n=34. Faltan ~6 resoluciones para umbral n≥40. ETA: ~4h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ FAVORITO_CONFIRMADO | 2461 | +0.172 | -70.06€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#15min | 1583 | +0.210 | +10.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 103 | +0.014 | -17.36€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 358 | +0.086 | -60.64€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 417 | +0.140 | -2.67€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 712 | +0.179 | -16.14€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 529 | +0.204 | -13.97€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 34 | +0.056 | -4.16€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 139 | +0.145 | +5.76€ | 0 | 10 |
| ✅ FAVORITO_CONFIRMADO#ETH | 875 | +0.172 | -8.46€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 524 | +0.213 | +13.23€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 34 | -0.083 | -10.92€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 178 | +0.106 | -21.89€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 139 | +0.160 | +11.13€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#SOL | 866 | +0.167 | -42.09€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 522 | +0.214 | +14.73€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 35 | +0.068 | -2.29€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 170 | +0.087 | -34.98€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 139 | +0.110 | -19.55€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 8 | +0.000 | -3.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 8 | +0.000 | -3.38€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 31 | +0.288 | +0.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 31 | +0.288 | +0.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 31 | +0.288 | +0.59€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 31 | +0.288 | +0.59€ | 0 | 0 |
| ✅ GBM_LATE_15M | 4808 | +0.103 | +1502.55€ | 0 | 5 |
| ✅ GBM_LATE_15M#15min | 4808 | +0.103 | +1502.55€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 1152 | +0.064 | +164.21€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 1152 | +0.064 | +164.21€ | 0 | 4 |
| ✅ GBM_LATE_15M#ETH | 1154 | +0.077 | +203.26€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1154 | +0.077 | +203.26€ | 1 | 6 |
| ✅ GBM_LATE_15M#SOL | 1287 | +0.110 | +522.08€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 1287 | +0.110 | +522.08€ | 1 | 6 |
| ✅ GBM_LATE_15M#XRP | 1215 | +0.156 | +613.00€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 1215 | +0.156 | +613.00€ | 0 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 2042 | +0.150 | +1190.18€ | 0 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 2042 | +0.150 | +1190.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 520 | +0.109 | +248.59€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 520 | +0.109 | +248.59€ | 0 | 9 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 542 | +0.131 | +260.38€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 542 | +0.131 | +260.38€ | 0 | 13 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 552 | +0.112 | +243.09€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 552 | +0.112 | +243.09€ | 1 | 10 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 428 | +0.270 | +438.11€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 428 | +0.270 | +438.11€ | 0 | 12 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 65 | +0.067 | +15.65€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 65 | +0.067 | +15.65€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC | 9 | -0.102 | -1.94€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 9 | -0.102 | -1.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 11 | +0.021 | +1.20€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 11 | +0.021 | +1.20€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL | 8 | -0.120 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 8 | -0.120 | -1.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 37 | +0.244 | +18.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 37 | +0.244 | +18.29€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 2009 | +0.091 | +608.83€ | 0 | 6 |
| ✅ GBM_LATE_15M_TARDIO#15min | 2009 | +0.091 | +608.83€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 496 | +0.058 | +89.14€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 496 | +0.058 | +89.14€ | 0 | 5 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 463 | +0.027 | +19.78€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 463 | +0.027 | +19.78€ | 0 | 4 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 477 | +0.059 | +95.98€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 477 | +0.059 | +95.98€ | 3 | 6 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 573 | +0.197 | +403.93€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 573 | +0.197 | +403.93€ | 0 | 12 |
| ✅ GBM_LATE_5M | 11 | -0.021 | -0.62€ | 0 | 0 |
| ✅ GBM_LATE_5M#5min | 11 | -0.021 | -0.62€ | 0 | 0 |
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
| ✅ LATE_WINDOW_5MIN | 44 | +0.217 | +18.78€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 44 | +0.217 | +18.78€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 44 | +0.217 | +18.78€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 44 | +0.217 | +18.78€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 135 | +0.091 | +28.09€ | 0 | 5 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 135 | +0.091 | +28.09€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 135 | +0.091 | +28.09€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 135 | +0.091 | +28.09€ | 0 | 5 |
| ✅ ORDER_FLOW_5M | 1617 | +0.012 | +13.02€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1481 | +0.008 | +0.43€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 198 | +0.045 | +6.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 198 | +0.045 | +6.48€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 2 | 1 |
| ✅ ORDER_FLOW_5M#DOGE | 216 | +0.000 | -2.12€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 216 | +0.000 | -2.12€ | 2 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 259 | -0.021 | -8.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 259 | -0.021 | -8.98€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 324 | +0.043 | +14.48€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 324 | +0.043 | +14.48€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#XRP | 193 | -0.003 | -4.19€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#XRP#5min | 193 | -0.003 | -4.19€ | 1 | 0 |
| ✅ PRICE_TARGET_GBM | 147 | -0.164 | -3.25€ | 4 | 1 |
| 🚫 PRICE_TARGET_GBM#BTC | 62 | -0.250 | -18.09€ | 0 | 0 |
| 🚫 PRICE_TARGET_GBM#BTC#atexpiry | 56 | -0.276 | -17.35€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#BTC#reach | 6 | +0.000 | -0.74€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH | 55 | -0.167 | +1.29€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#atexpiry | 50 | -0.192 | -2.51€ | 4 | 0 |
| ✅ PRICE_TARGET_GBM#ETH#reach | 5 | +0.018 | +3.80€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL | 30 | +0.031 | +13.54€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#SOL#atexpiry | 28 | +0.033 | +13.27€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#atexpiry | 134 | -0.184 | -6.59€ | 0 | 0 |
| ✅ PRICE_TARGET_GBM#reach | 13 | +0.022 | +3.34€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER | 10 | +0.208 | +4.00€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#SOL#sniper | 5 | +0.089 | +1.32€ | 0 | 0 |
| ✅ RESOLUTION_SNIPER#sniper | 10 | +0.208 | +4.00€ | 0 | 0 |
| 🚫 SMART_FLOW_1H | 29 | -0.274 | -13.82€ | 0 | 0 |
| ✅ SMART_FLOW_1H#BTC | 12 | -0.086 | -3.30€ | 0 | 0 |
| ✅ STREAK_FADE_15M | 202 | +0.098 | +28.64€ | 0 | 10 |
| ✅ STREAK_FADE_15M#15min | 202 | +0.098 | +28.64€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 43 | +0.078 | -0.53€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 43 | +0.078 | -0.53€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL | 71 | +0.185 | +30.87€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 71 | +0.185 | +30.87€ | 0 | 2 |
| ✅ STREAK_FADE_15M#XRP | 88 | +0.033 | -1.71€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 88 | +0.033 | -1.71€ | 1 | 2 |
| ✅ STREAK_FADE_5M | 246 | -0.048 | -24.96€ | 3 | 0 |
| ✅ STREAK_FADE_5M#5min | 246 | -0.048 | -24.96€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH | 47 | -0.153 | -8.07€ | 0 | 0 |
| ✅ STREAK_FADE_5M#ETH#5min | 47 | -0.153 | -8.07€ | 6 | 0 |
| ✅ STREAK_FADE_5M#SOL | 94 | -0.021 | -7.62€ | 0 | 0 |
| ✅ STREAK_FADE_5M#SOL#5min | 94 | -0.021 | -7.62€ | 2 | 1 |
| ✅ STREAK_FADE_5M#XRP | 105 | -0.023 | -9.27€ | 0 | 0 |
| ✅ STREAK_FADE_5M#XRP#5min | 105 | -0.023 | -9.27€ | 1 | 0 |
| 🚫 STREAK_MOM_5M | 310 | -0.054 | -22.30€ | 6 | 0 |
| ✅ STREAK_MOM_5M#5min | 310 | -0.054 | -22.30€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH | 103 | -0.052 | -6.34€ | 0 | 0 |
| ✅ STREAK_MOM_5M#ETH#5min | 103 | -0.052 | -6.34€ | 2 | 0 |
| ✅ STREAK_MOM_5M#SOL | 109 | -0.004 | -2.61€ | 0 | 0 |
| ✅ STREAK_MOM_5M#SOL#5min | 109 | -0.004 | -2.61€ | 2 | 3 |
| ✅ STREAK_MOM_5M#XRP | 98 | -0.110 | -13.35€ | 0 | 0 |
| ✅ STREAK_MOM_5M#XRP#5min | 98 | -0.110 | -13.35€ | 5 | 0 |
| 🚫 STRUCT_NO_15M | 15 | -0.199 | -4.68€ | 0 | 0 |
| 🚫 STRUCT_NO_15M#15min | 15 | -0.199 | -4.68€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#ETH#15min | 5 | -0.054 | -1.56€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ STRUCT_NO_15M#SOL#15min | 6 | -0.075 | -2.07€ | 0 | 0 |
| ✅ UPDOWN_GBM | 1592 | +0.010 | +77.30€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 1334 | +0.037 | +114.34€ | 1 | 6 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 127 | -0.058 | -10.76€ | 7 | 0 |
| ✅ UPDOWN_GBM#BNB | 85 | +0.063 | +16.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 85 | +0.063 | +16.62€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 411 | +0.028 | +31.57€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 330 | +0.066 | +44.52€ | 1 | 10 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 42 | -0.068 | -6.16€ | 2 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 16 | -0.089 | +2.85€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 58 | +0.017 | -0.24€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 55 | +0.026 | +0.66€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 763 | +0.018 | +36.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 670 | +0.034 | +47.74€ | 2 | 5 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 54 | -0.018 | -2.56€ | 3 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 170 | -0.087 | -14.39€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 102 | -0.058 | -7.39€ | 7 | 0 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 31 | -0.106 | -2.03€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 103 | +0.005 | +8.91€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 92 | +0.032 | +12.20€ | 5 | 5 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| ✅ UPDOWN_GBM#daily | 43 | -0.189 | +2.35€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 16 | +0.178 | -0.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 16 | +0.178 | -0.19€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 6 | +0.037 | -0.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 6 | +0.037 | -0.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 10 | +0.125 | +0.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 10 | +0.125 | +0.14€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 116 | +0.186 | +32.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 116 | +0.186 | +32.82€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 7 | -0.019 | +2.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 7 | -0.019 | +2.23€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 16 | +0.133 | +5.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 16 | +0.133 | +5.99€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 34 | +0.194 | +3.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 34 | +0.194 | +3.91€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 37 | +0.192 | +15.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 37 | +0.192 | +15.39€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 18 | +0.135 | +2.18€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 18 | +0.135 | +2.18€ | 0 | 0 |
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
| ✅ WEEKLY_PRICE | 256 | +0.120 | +13.84€ | 1 | 1 |
| ✅ WEEKLY_PRICE#BTC | 76 | +0.077 | -9.85€ | 0 | 3 |
| ✅ WEEKLY_PRICE#ETH | 73 | +0.087 | -8.24€ | 0 | 2 |
| ✅ WEEKLY_PRICE#SOL | 107 | +0.170 | +31.93€ | 0 | 2 |