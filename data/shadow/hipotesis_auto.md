# Hipótesis automáticas — 2026-07-27 20:47 UTC
_Generado por shadow_postmortem.py sobre 38925 resoluciones (PNL=+7948.72€)_

## Patrones causales activos

### FAVORITO_CONFIRMADO
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.198 (n=2266)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.99€ cuando `hora_utc` > 8.0 (IC base=+0.187)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.190 (n=1215)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.95€ cuando `hora_utc` < 8.0 (IC base=+0.187)

- **PATRÓN** `py_entrada` > `0.725` → IC=+0.327 (n=863)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.725 (IC base=+0.187)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.192 (n=2760)

  - _Acción_: Kelly boost +0.96€ cuando `libro_spread` < 0.01 (IC base=+0.187)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.176 (n=970)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.88€ cuando `hora_utc` > 17.0 (IC base=+0.171)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.188 (n=1177)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.94€ cuando `hora_utc` < 7.0 (IC base=+0.171)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.331 (n=890)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.171)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=2889)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.171)

### FAVORITO_CONFIRMADO#BTC#15min
- **PATRÓN** `hora_utc` > `12.0` → IC=+0.207 (n=370)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.201)

- **PATRÓN** `hora_utc` < `18.0` → IC=+0.204 (n=573)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 18.0 (IC base=+0.201)

- **PATRÓN** `py_entrada` > `0.605` → IC=+0.260 (n=553)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.605 (IC base=+0.201)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.206 (n=219)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `5.0` → IC=+0.217 (n=203)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 5.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` < `0.265` → IC=+0.352 (n=261)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.265 (IC base=+0.194)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.194 (n=743)

  - _Acción_: Kelly boost +0.97€ cuando `libro_spread` < 0.01 (IC base=+0.194)

### FAVORITO_CONFIRMADO#BTC#60min
- **PATRÓN** `hora_utc` < `11.0` → IC=+0.237 (n=97)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.184)

- **PATRÓN** `py_entrada` < `0.565` → IC=+0.212 (n=64)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.565 (IC base=+0.184)

- **PATRÓN** `py_entrada` > `0.635` → IC=+0.222 (n=52)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.635 (IC base=+0.184)

- **PATRÓN** `hora_utc` < `12.0` → IC=+0.246 (n=112)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 12.0 (IC base=+0.168)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.263 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.405 (IC base=+0.168)

- **PATRÓN** `libro_liquidez` > `5976.8472` → IC=+0.183 (n=162)

  - _Acción_: Kelly boost +0.91€ cuando `libro_liquidez` > 5976.8472 (IC base=+0.168)

### FAVORITO_CONFIRMADO#ETH#15min
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.222 (n=505)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.207)

- **PATRÓN** `py_entrada` > `0.715` → IC=+0.343 (n=252)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.715 (IC base=+0.207)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.207 (n=213)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.194)

- **PATRÓN** `hora_utc` < `11.0` → IC=+0.204 (n=380)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 11.0 (IC base=+0.194)

- **PATRÓN** `py_entrada` < `0.275` → IC=+0.326 (n=268)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.275 (IC base=+0.194)

### FAVORITO_CONFIRMADO#ETH#60min
- **PATRÓN** `hora_utc` > `5.0` → IC=+0.158 (n=147)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` > 5.0 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `15.0` → IC=+0.159 (n=127)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.79€ cuando `hora_utc` < 15.0 (IC base=+0.142)

- **PATRÓN** `py_entrada` < `0.575` → IC=+0.154 (n=53)

  - _Acción_: Kelly boost +0.77€ cuando `py_entrada` < 0.575 (IC base=+0.142)

- **PATRÓN** `py_entrada` > `0.575` → IC=+0.151 (n=147)

  - _Acción_: Kelly boost +0.76€ cuando `py_entrada` > 0.575 (IC base=+0.142)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.173 (n=145)

  - _Acción_: Kelly boost +0.87€ cuando `libro_spread` < 0.01 (IC base=+0.142)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.184 (n=74)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.92€ cuando `hora_utc` < 8.0 (IC base=+0.139)

- **PATRÓN** `py_entrada` < `0.405` → IC=+0.158 (n=118)

  - _Acción_: Kelly boost +0.79€ cuando `py_entrada` < 0.405 (IC base=+0.139)

- **PATRÓN** `py_entrada` > `0.42` → IC=+0.162 (n=75)

  - _Acción_: Kelly boost +0.81€ cuando `py_entrada` > 0.42 (IC base=+0.139)

- **PATRÓN** `libro_liquidez` > `4203.8302` → IC=+0.185 (n=144)

  - _Acción_: Kelly boost +0.92€ cuando `libro_liquidez` > 4203.8302 (IC base=+0.139)

### FAVORITO_CONFIRMADO#SOL#15min
- **PATRÓN** `hora_utc` > `18.0` → IC=+0.233 (n=200)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 18.0 (IC base=+0.217)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.219 (n=247)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 8.0 (IC base=+0.217)

- **PATRÓN** `py_entrada` > `0.675` → IC=+0.319 (n=363)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` > 0.675 (IC base=+0.217)

- **PATRÓN** `libro_spread` < `0.01` → IC=+0.219 (n=595)

  - _Acción_: Kelly boost +1.00€ cuando `libro_spread` < 0.01 (IC base=+0.217)

- **PATRÓN** `libro_liquidez` > `2394.6293` → IC=+0.225 (n=180)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 2394.6293 (IC base=+0.217)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.208 (n=207)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 17.0 (IC base=+0.203)

- **PATRÓN** `hora_utc` < `17.0` → IC=+0.209 (n=586)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` < 17.0 (IC base=+0.203)

- **PATRÓN** `py_entrada` < `0.37` → IC=+0.264 (n=503)

  - _Acción_: Kelly boost +1.00€ cuando `py_entrada` < 0.37 (IC base=+0.203)

- **PATRÓN** `libro_liquidez` > `1588.1821` → IC=+0.207 (n=571)

  - _Acción_: Kelly boost +1.00€ cuando `libro_liquidez` > 1588.1821 (IC base=+0.203)

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
- **PATRÓN** `hora_utc` > `8.0` → IC=+0.133 (n=2327)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.67€ cuando `hora_utc` > 8.0 (IC base=+0.115)

- **PATRÓN** `dist_vwap_pct` > `0.4622` → IC=+0.126 (n=327)

  - _Acción_: Kelly boost +0.63€ cuando `dist_vwap_pct` > 0.4622 (IC base=+0.115)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.026` → IC=+0.206 (n=389)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.026 (IC base=+0.115)

- **PATRÓN** `sigma_h` > `0.0125` → IC=+0.126 (n=1105)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` > 0.0125 (IC base=+0.092)

### GBM_LATE_15M#BTC#15min
- **PATRÓN** `sigma_h` < `0.0044` → IC=+0.145 (n=424)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` < 0.0044 (IC base=+0.108)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.133 (n=567)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 8.0 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` > `0.433` → IC=+0.172 (n=59)

  - _Acción_: Kelly boost +0.86€ cuando `dist_vwap_pct` > 0.433 (IC base=+0.108)

- **PATRÓN** `dist_vwap_pct` < `0.1011` → IC=+0.138 (n=288)

  - _Acción_: Kelly boost +0.69€ cuando `dist_vwap_pct` < 0.1011 (IC base=+0.108)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.649` → IC=+0.207 (n=73)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 12.649 (IC base=+0.108)

### GBM_LATE_15M#ETH#15min
- **PATRÓN** `sigma_h` < `0.0042` → IC=+0.167 (n=157)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.83€ cuando `sigma_h` < 0.0042 (IC base=+0.103)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.129 (n=427)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.65€ cuando `hora_utc` > 8.0 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` > `0.9129` → IC=+0.180 (n=23)

  - _Acción_: Kelly boost +0.90€ cuando `dist_vwap_pct` > 0.9129 (IC base=+0.103)

- **PATRÓN** `dist_vwap_pct` < `0.1547` → IC=+0.153 (n=122)

  - _Acción_: Kelly boost +0.77€ cuando `dist_vwap_pct` < 0.1547 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.951` → IC=+0.186 (n=119)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 7.951 (IC base=+0.103)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.6` → IC=+0.149 (n=149)

  - _Acción_: Kelly boost +0.75€ cuando `sigma_ewma_delta_pct` > 6.6 (IC base=+0.065)

### GBM_LATE_15M#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `8.052` → IC=-0.278 (n=25)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 8.052
  - _Potencial_: sin este filtro IC_bueno=+0.065 (n=617)

- **PATRÓN** `hora_utc` > `17.0` → IC=+0.151 (n=282)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 17.0 (IC base=+0.101)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.374` → IC=+0.224 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 5.374 (IC base=+0.101)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.146 (n=408)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` < 8.0 (IC base=+0.093)

### GBM_LATE_15M#XRP#15min
- **PATRÓN** `sigma_h` < `0.0101` → IC=+0.163 (n=250)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.81€ cuando `sigma_h` < 0.0101 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0207` → IC=+0.148 (n=339)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.74€ cuando `sigma_h` > 0.0207 (IC base=+0.143)

- **PATRÓN** `hora_utc` > `6.0` → IC=+0.150 (n=759)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.75€ cuando `hora_utc` > 6.0 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` > `0.6538` → IC=+0.189 (n=72)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.6538 (IC base=+0.143)

- **PATRÓN** `dist_vwap_pct` < `0.1081` → IC=+0.132 (n=378)

  - _Acción_: Kelly boost +0.66€ cuando `dist_vwap_pct` < 0.1081 (IC base=+0.143)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.526` → IC=+0.250 (n=90)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.526 (IC base=+0.143)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.147 (n=944)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.73€ cuando `sigma_h` > 0.0084 (IC base=+0.137)

- **PATRÓN** `hora_utc` > `18.0` → IC=+0.160 (n=319)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.80€ cuando `hora_utc` > 18.0 (IC base=+0.137)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.155 (n=349)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.78€ cuando `hora_utc` < 6.0 (IC base=+0.137)

- **PATRÓN** `dist_vwap_pct` > `0.3403` → IC=+0.189 (n=120)

  - _Acción_: Kelly boost +0.94€ cuando `dist_vwap_pct` > 0.3403 (IC base=+0.137)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.444` → IC=+0.132 (n=93)

  - _Acción_: Kelly boost +0.66€ cuando `sigma_ewma_delta_pct` > 7.444 (IC base=+0.137)

### GBM_LATE_15M_ESPACIO_ATR
- **PATRÓN** `sigma_h` > `0.0074` → IC=+0.190 (n=1168)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` > 0.0074 (IC base=+0.144)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.168 (n=1574)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.84€ cuando `hora_utc` > 8.0 (IC base=+0.144)

- **PATRÓN** `dist_vwap_pct` > `0.2776` → IC=+0.191 (n=496)

  - _Acción_: Kelly boost +0.95€ cuando `dist_vwap_pct` > 0.2776 (IC base=+0.144)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.512` → IC=+0.231 (n=548)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 6.512 (IC base=+0.144)

- **PATRÓN** `sigma_h` > `0.0067` → IC=+0.151 (n=1389)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.76€ cuando `sigma_h` > 0.0067 (IC base=+0.117)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.131 (n=1440)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.66€ cuando `hora_utc` > 12.0 (IC base=+0.117)

- **PATRÓN** `dist_vwap_pct` > `0.3982` → IC=+0.129 (n=340)

  - _Acción_: Kelly boost +0.64€ cuando `dist_vwap_pct` > 0.3982 (IC base=+0.117)

- **PATRÓN** `sigma_ewma_delta_pct` > `8.218` → IC=+0.144 (n=307)

  - _Acción_: Kelly boost +0.72€ cuando `sigma_ewma_delta_pct` > 8.218 (IC base=+0.117)

### GBM_LATE_15M_ESPACIO_ATR#BTC#15min
- **PATRÓN** `sigma_h` < `0.0048` → IC=+0.127 (n=392)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.63€ cuando `sigma_h` < 0.0048 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.145 (n=398)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.73€ cuando `hora_utc` > 8.0 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `0.4476` → IC=+0.217 (n=58)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.4476 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `12.024` → IC=+0.195 (n=80)

  - _Acción_: Kelly boost +0.98€ cuando `sigma_ewma_delta_pct` > 12.024 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `4.43` → IC=+0.141 (n=193)

  - _Acción_: Kelly boost +0.71€ cuando `sigma_ewma_delta_pct` > 4.43 (IC base=+0.089)

### GBM_LATE_15M_ESPACIO_ATR#ETH#15min
- **PATRÓN** `sigma_h` > `0.0075` → IC=+0.201 (n=152)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0075 (IC base=+0.123)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.151 (n=305)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.76€ cuando `hora_utc` > 12.0 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `0.6746` → IC=+0.167 (n=79)

  - _Acción_: Kelly boost +0.83€ cuando `dist_vwap_pct` > 0.6746 (IC base=+0.123)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.301` → IC=+0.186 (n=119)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 7.301 (IC base=+0.123)

- **PATRÓN** `dist_vwap_pct` > `1.0412` → IC=+0.176 (n=32)

  - _Acción_: Kelly boost +0.88€ cuando `dist_vwap_pct` > 1.0412 (IC base=+0.088)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.42` → IC=+0.176 (n=100)

  - _Acción_: Kelly boost +0.88€ cuando `sigma_ewma_delta_pct` > 9.42 (IC base=+0.088)

### GBM_LATE_15M_ESPACIO_ATR#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `7.938` → IC=-0.250 (n=22)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.938
  - _Potencial_: sin este filtro IC_bueno=+0.093 (n=514)

- **PATRÓN** `sigma_h` > `0.0078` → IC=+0.141 (n=447)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.71€ cuando `sigma_h` > 0.0078 (IC base=+0.112)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.144 (n=400)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.72€ cuando `hora_utc` > 8.0 (IC base=+0.112)

- **PATRÓN** `dist_vwap_pct` > `0.1796` → IC=+0.151 (n=164)

  - _Acción_: Kelly boost +0.75€ cuando `dist_vwap_pct` > 0.1796 (IC base=+0.112)

- **PATRÓN** `sigma_ewma_delta_pct` > `3.667` → IC=+0.270 (n=189)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 3.667 (IC base=+0.112)

### GBM_LATE_15M_ESPACIO_ATR#XRP#15min
- **PATRÓN** `sigma_h` < `0.0179` → IC=+0.256 (n=408)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0179 (IC base=+0.234)

- **PATRÓN** `sigma_h` > `0.0084` → IC=+0.234 (n=408)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.0084 (IC base=+0.234)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.251 (n=376)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 8.0 (IC base=+0.234)

- **PATRÓN** `dist_vwap_pct` > `0.6709` → IC=+0.288 (n=50)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.6709 (IC base=+0.234)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.801` → IC=+0.351 (n=112)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.801 (IC base=+0.234)

- **PATRÓN** `sigma_h` < `0.0174` → IC=+0.209 (n=537)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` < 0.0174 (IC base=+0.204)

- **PATRÓN** `sigma_h` > `0.007` → IC=+0.233 (n=538)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +1.00€ cuando `sigma_h` > 0.007 (IC base=+0.204)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.243 (n=368)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +1.00€ cuando `hora_utc` > 12.0 (IC base=+0.204)

- **PATRÓN** `dist_vwap_pct` > `0.189` → IC=+0.317 (n=102)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.189 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` > `7.495` → IC=+0.214 (n=61)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 7.495 (IC base=+0.204)

- **PATRÓN** `sigma_ewma_delta_pct` < `5.458` → IC=+0.197 (n=536)

  - _Acción_: Kelly boost +0.99€ cuando `sigma_ewma_delta_pct` < 5.458 (IC base=+0.204)

### GBM_LATE_15M_TARDIO
- **PATRÓN** `sigma_h` > `0.0124` → IC=+0.138 (n=572)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` > 0.0124 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.4705` → IC=+0.158 (n=328)

  - _Acción_: Kelly boost +0.79€ cuando `dist_vwap_pct` > 0.4705 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `11.281` → IC=+0.241 (n=272)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 11.281 (IC base=+0.099)

### GBM_LATE_15M_TARDIO#BTC#15min
- **PATRÓN** `sigma_h` < `0.004` → IC=+0.139 (n=258)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.69€ cuando `sigma_h` < 0.004 (IC base=+0.084)

- **PATRÓN** `dist_vwap_pct` > `0.4413` → IC=+0.178 (n=57)

  - _Acción_: Kelly boost +0.89€ cuando `dist_vwap_pct` > 0.4413 (IC base=+0.084)

- **PATRÓN** `sigma_ewma_delta_pct` > `10.89` → IC=+0.200 (n=78)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 10.89 (IC base=+0.084)

### GBM_LATE_15M_TARDIO#ETH#15min
- **PATRÓN** `sigma_ewma_delta_pct` > `12.377` → IC=+0.182 (n=61)

  - _Acción_: Kelly boost +0.91€ cuando `sigma_ewma_delta_pct` > 12.377 (IC base=+0.062)

### GBM_LATE_15M_TARDIO#SOL#15min
- **FILTRO** `sigma_ewma_delta_pct` > `7.827` → IC=-0.152 (n=21)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` > 7.827
  - _Potencial_: sin este filtro IC_bueno=+0.070 (n=486)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.2` → IC=+0.295 (n=86)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.2 (IC base=+0.054)

### GBM_LATE_15M_TARDIO#XRP#15min
- **PATRÓN** `sigma_h` < `0.02` → IC=+0.186 (n=457)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.93€ cuando `sigma_h` < 0.02 (IC base=+0.174)

- **PATRÓN** `sigma_h` > `0.014` → IC=+0.175 (n=346)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.88€ cuando `sigma_h` > 0.014 (IC base=+0.174)

- **PATRÓN** `hora_utc` > `8.0` → IC=+0.182 (n=466)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.91€ cuando `hora_utc` > 8.0 (IC base=+0.174)

- **PATRÓN** `dist_vwap_pct` > `0.2426` → IC=+0.230 (n=150)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2426 (IC base=+0.174)

- **PATRÓN** `sigma_ewma_delta_pct` > `9.987` → IC=+0.278 (n=97)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 9.987 (IC base=+0.174)

- **PATRÓN** `sigma_h` < `0.0228` → IC=+0.157 (n=653)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.78€ cuando `sigma_h` < 0.0228 (IC base=+0.156)

- **PATRÓN** `sigma_h` > `0.0077` → IC=+0.172 (n=653)
  - _Por qué funciona_: alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio
  - _Acción_: Kelly boost +0.86€ cuando `sigma_h` > 0.0077 (IC base=+0.156)

- **PATRÓN** `hora_utc` > `12.0` → IC=+0.179 (n=446)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.89€ cuando `hora_utc` > 12.0 (IC base=+0.156)

- **PATRÓN** `hora_utc` < `6.0` → IC=+0.164 (n=227)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.82€ cuando `hora_utc` < 6.0 (IC base=+0.156)

- **PATRÓN** `dist_vwap_pct` > `0.344` → IC=+0.226 (n=111)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.344 (IC base=+0.156)

- **PATRÓN** `sigma_ewma_delta_pct` < `9.452` → IC=+0.153 (n=672)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` < 9.452 (IC base=+0.156)

### GBM_LATE_60M
- **FILTRO** `sigma_ewma_delta_pct` < `14.633` → IC=-0.200 (n=18)

  - _Acción_: SKIP cuando `sigma_ewma_delta_pct` < 14.633
  - _Potencial_: sin este filtro IC_bueno=+0.206 (n=15)

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
  - _Acción_: Kelly boost +0.87€ cuando `sigma_h` < 0.0044 (IC base=-0.008)

- **PATRÓN** `sigma_ewma_delta_pct` > `14.633` → IC=+0.206 (n=15)

  - _Acción_: Kelly boost +1.00€ cuando `sigma_ewma_delta_pct` > 14.633 (IC base=-0.008)

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

- **PATRÓN** `sigma_h` < `0.005` → IC=+0.159 (n=39)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.79€ cuando `sigma_h` < 0.005 (IC base=+0.026)

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
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=158)

### LEADLAG_BTC_XRP_15M#XRP#15min
- **FILTRO** `libro_spread` > `0.01` → IC=-0.132 (n=17)

  - _Acción_: SKIP cuando `libro_spread` > 0.01
  - _Potencial_: sin este filtro IC_bueno=-0.013 (n=158)

### ORDER_FLOW_5M
- **FILTRO** `hora_utc` > `4.0` → IC=-0.122 (n=35)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: SKIP cuando `hora_utc` > 4.0
  - _Potencial_: sin este filtro IC_bueno=+0.038 (n=154)

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
- **PATRÓN** `hora_utc` > `4.0` → IC=+0.121 (n=27)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.60€ cuando `hora_utc` > 4.0 (IC base=+0.069)

- **PATRÓN** `hora_utc` < `4.0` → IC=+0.139 (n=34)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` < 4.0 (IC base=+0.069)

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
  - _Potencial_: sin este filtro IC_bueno=+0.115 (n=94)

- **PATRÓN** `hora_utc` > `14.0` → IC=+0.148 (n=52)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` > 14.0 (IC base=+0.071)

- **PATRÓN** `streak_len` < `4.0` → IC=+0.122 (n=88)

  - _Acción_: Kelly boost +0.61€ cuando `streak_len` < 4.0 (IC base=+0.071)

- **PATRÓN** `hora_utc` < `7.0` → IC=+0.196 (n=54)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.98€ cuando `hora_utc` < 7.0 (IC base=+0.069)

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
- **PATRÓN** `hora_utc` < `9.0` → IC=+0.167 (n=40)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.83€ cuando `hora_utc` < 9.0 (IC base=+0.079)

- **PATRÓN** `volumen_racha` < `497480.0` → IC=+0.200 (n=28)

  - _Acción_: Kelly boost +1.00€ cuando `volumen_racha` < 497480.0 (IC base=+0.079)

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
- **PATRÓN** `ibs_15` > `0.6075` → IC=+0.175 (n=632)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.88€ cuando `ibs_15` > 0.6075 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.1676` → IC=+0.164 (n=230)

  - _Acción_: Kelly boost +0.82€ cuando `dist_vwap_pct` > 0.1676 (IC base=+0.055)

- **PATRÓN** `sigma_ewma_delta_pct` > `5.224` → IC=+0.152 (n=228)

  - _Acción_: Kelly boost +0.76€ cuando `sigma_ewma_delta_pct` > 5.224 (IC base=+0.055)

- **PATRÓN** `dist_vwap_pct` > `0.182` → IC=+0.121 (n=180)

  - _Acción_: Kelly boost +0.60€ cuando `dist_vwap_pct` > 0.182 (IC base=+0.047)

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
- **FILTRO** `ibs_15` > `0.1169` → IC=-0.182 (n=20)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: SKIP cuando `ibs_15` > 0.1169
  - _Potencial_: sin este filtro IC_bueno=+0.119 (n=40)

- **PATRÓN** `drift_60min` |x|≤ `0.2204` → IC=+0.137 (n=309)
  - _Por qué funciona_: drift moderado → precio aún no ha reaccionado del todo; lag explotable
  - _Acción_: Kelly boost +0.68€ cuando `drift_60min` |x|≤ 0.2204 (IC base=+0.099)

- **PATRÓN** `delta_ratio_macro` |x|> `0.0647` → IC=+0.124 (n=309)
  - _Por qué funciona_: flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket
  - _Acción_: Kelly boost +0.62€ cuando `delta_ratio_macro` |x|> 0.0647 (IC base=+0.099)

- **PATRÓN** `hora_utc` > `19.0` → IC=+0.138 (n=114)
  - _Por qué funciona_: hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas
  - _Acción_: Kelly boost +0.69€ cuando `hora_utc` > 19.0 (IC base=+0.099)

- **PATRÓN** `hora_utc` < `8.0` → IC=+0.147 (n=100)
  - _Por qué funciona_: hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor
  - _Acción_: Kelly boost +0.74€ cuando `hora_utc` < 8.0 (IC base=+0.099)

- **PATRÓN** `ibs_15` > `0.724` → IC=+0.241 (n=241)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +1.00€ cuando `ibs_15` > 0.724 (IC base=+0.099)

- **PATRÓN** `dist_vwap_pct` > `0.2571` → IC=+0.236 (n=89)

  - _Acción_: Kelly boost +1.00€ cuando `dist_vwap_pct` > 0.2571 (IC base=+0.099)

- **PATRÓN** `sigma_ewma_delta_pct` > `20.875` → IC=+0.186 (n=49)

  - _Acción_: Kelly boost +0.93€ cuando `sigma_ewma_delta_pct` > 20.875 (IC base=+0.099)

- **PATRÓN** `sigma_h` < `0.0061` → IC=+0.190 (n=27)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.95€ cuando `sigma_h` < 0.0061 (IC base=+0.024)

### UPDOWN_GBM#BTC#60min
- **FILTRO** `sigma_h` < `0.012` → IC=-0.143 (n=26)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: SKIP cuando `sigma_h` < 0.012
  - _Potencial_: sin este filtro IC_bueno=+0.227 (n=9)

### UPDOWN_GBM#ETH#15min
- **PATRÓN** `ibs_15` > `0.6679` → IC=+0.189 (n=204)
  - _Por qué funciona_: IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable
  - _Acción_: Kelly boost +0.95€ cuando `ibs_15` > 0.6679 (IC base=+0.043)

- **PATRÓN** `sigma_ewma_delta_pct` > `6.232` → IC=+0.145 (n=60)

  - _Acción_: Kelly boost +0.73€ cuando `sigma_ewma_delta_pct` > 6.232 (IC base=+0.043)

- **PATRÓN** `sigma_h` < `0.0055` → IC=+0.154 (n=134)
  - _Por qué funciona_: baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge
  - _Acción_: Kelly boost +0.77€ cuando `sigma_h` < 0.0055 (IC base=+0.061)

- **PATRÓN** `dist_vwap_pct` > `0.9222` → IC=+0.186 (n=33)

  - _Acción_: Kelly boost +0.93€ cuando `dist_vwap_pct` > 0.9222 (IC base=+0.061)

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

- **PATRÓN** `drift_15min` |x|≤ `0.427` → IC=+0.129 (n=60)

  - _Acción_: Kelly boost +0.65€ cuando `drift_15min` |x|≤ 0.427 (IC base=+0.027)

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

- **PATRÓN** `ibs_15` < `0.0286` → IC=+0.157 (n=65)
  - _Por qué funciona_: IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable
  - _Acción_: Kelly boost +0.78€ cuando `ibs_15` < 0.0286 (IC base=+0.075)

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
- **H-IBS-UPDOWN_GBM#15min**: dentro de BUY_YES, IBS > 0.6075 sube el IC de +0.055 a +0.175 en UPDOWN_GBM#15min (n=632). Ya aplicado como kelly_boost=+0.88€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#BTC#15min**: dentro de BUY_YES, IBS > 0.724 sube el IC de +0.099 a +0.241 en UPDOWN_GBM#BTC#15min (n=241). Ya aplicado como kelly_boost=+1.00€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#ETH#15min**: dentro de BUY_YES, IBS > 0.6679 sube el IC de +0.043 a +0.189 en UPDOWN_GBM#ETH#15min (n=204). Ya aplicado como kelly_boost=+0.95€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **H-IBS-UPDOWN_GBM#XRP#15min**: dentro de BUY_NO, IBS < 0.0286 sube el IC de +0.075 a +0.157 en UPDOWN_GBM#XRP#15min (n=65). Ya aplicado como kelly_boost=+0.78€ automático (shadow) — no es señal de reversión a la dirección contraria.
- **LIVE-CANDIDATA**: `FAVORITO_CONFIRMADO#XRP` — IC=+0.149 n=35. Faltan ~5 resoluciones para umbral n≥40. ETA: ~4h.

## Estado de aprendizaje por estrategia

| Estrategia | n | IC | PNL | Filtros | Patrones |
|---|---|---|---|---|---|
| ✅ BALLENAS_CONFIRMADAS_15M | 1404 | +0.098 | +31.29€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#15min | 1404 | +0.098 | +31.29€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#DOGE#15min | 19 | +0.068 | -0.35€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH | 556 | +0.090 | -0.59€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#ETH#15min | 556 | +0.090 | -0.59€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL | 522 | +0.122 | +13.54€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#SOL#15min | 522 | +0.122 | +13.54€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP | 307 | +0.073 | +18.69€ | 0 | 0 |
| ✅ BALLENAS_CONFIRMADAS_15M#XRP#15min | 307 | +0.073 | +18.69€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS | 46 | +0.375 | +4.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#15min | 46 | +0.375 | +4.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC | 46 | +0.375 | +4.31€ | 0 | 0 |
| ✅ BALLENAS_TARDIAS#BTC#15min | 46 | +0.375 | +4.31€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO | 6832 | +0.179 | -24.38€ | 0 | 8 |
| ✅ FAVORITO_CONFIRMADO#15min | 4502 | +0.203 | -24.99€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#240min | 309 | +0.056 | -21.15€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#5min | 815 | +0.128 | -57.61€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#60min | 1206 | +0.155 | +79.37€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC | 2015 | +0.183 | -6.54€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#15min | 1500 | +0.198 | -49.55€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#BTC#240min | 102 | +0.038 | -14.60€ | 0 | 0 |
| 🚫 FAVORITO_CONFIRMADO#BTC#5min | 10 | -0.125 | -3.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#BTC#60min | 403 | +0.176 | +61.39€ | 0 | 6 |
| ✅ FAVORITO_CONFIRMADO#DOGE | 8 | +0.120 | +5.71€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#DOGE#15min | 7 | +0.097 | +4.78€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH | 2398 | +0.169 | -32.91€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#15min | 1481 | +0.201 | +2.11€ | 0 | 5 |
| ✅ FAVORITO_CONFIRMADO#ETH#240min | 102 | -0.019 | -22.81€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#5min | 413 | +0.129 | -28.77€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#ETH#60min | 402 | +0.141 | +16.56€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#SOL | 2372 | +0.184 | +7.30€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#15min | 1481 | +0.210 | +19.06€ | 0 | 9 |
| ✅ FAVORITO_CONFIRMADO#SOL#240min | 103 | +0.148 | +17.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#5min | 387 | +0.132 | -30.35€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#SOL#60min | 401 | +0.145 | +1.42€ | 0 | 7 |
| ✅ FAVORITO_CONFIRMADO#XRP | 35 | +0.149 | +1.45€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO#XRP#15min | 29 | +0.113 | -2.00€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION | 434 | +0.305 | +11.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#15min | 434 | +0.305 | +11.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL | 434 | +0.305 | +11.16€ | 0 | 0 |
| ✅ FAVORITO_CONFIRMADO_SOL_ALTACONVICCION#SOL#15min | 434 | +0.305 | +11.16€ | 0 | 0 |
| ✅ GBM_LATE_15M | 8374 | +0.094 | +2516.02€ | 0 | 4 |
| ✅ GBM_LATE_15M#15min | 8374 | +0.094 | +2516.02€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC | 2031 | +0.073 | +352.32€ | 0 | 0 |
| ✅ GBM_LATE_15M#BTC#15min | 2031 | +0.073 | +352.32€ | 0 | 5 |
| ✅ GBM_LATE_15M#ETH | 1835 | +0.073 | +304.85€ | 0 | 0 |
| ✅ GBM_LATE_15M#ETH#15min | 1835 | +0.073 | +304.85€ | 0 | 6 |
| ✅ GBM_LATE_15M#SOL | 2252 | +0.083 | +770.61€ | 0 | 0 |
| ✅ GBM_LATE_15M#SOL#15min | 2252 | +0.083 | +770.61€ | 1 | 3 |
| ✅ GBM_LATE_15M#XRP | 2253 | +0.140 | +1087.22€ | 0 | 0 |
| ✅ GBM_LATE_15M#XRP#15min | 2253 | +0.140 | +1087.22€ | 0 | 11 |
| ✅ GBM_LATE_15M_ESPACIO_ATR | 5608 | +0.114 | +2569.21€ | 0 | 8 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#15min | 5608 | +0.114 | +2569.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC | 1472 | +0.083 | +498.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#BTC#15min | 1472 | +0.083 | +498.08€ | 0 | 5 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH | 1472 | +0.089 | +506.34€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#ETH#15min | 1472 | +0.089 | +506.34€ | 0 | 6 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL | 1401 | +0.081 | +520.21€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#SOL#15min | 1401 | +0.081 | +520.21€ | 1 | 4 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP | 1260 | +0.217 | +1042.88€ | 0 | 0 |
| ✅ GBM_LATE_15M_ESPACIO_ATR#XRP#15min | 1260 | +0.217 | +1042.88€ | 0 | 11 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_MULTIHORIZONTE#15min | 6 | +0.000 | -0.08€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO | 284 | +0.066 | +100.76€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#15min | 284 | +0.066 | +100.76€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC | 9 | -0.102 | -1.94€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#BTC#15min | 9 | -0.102 | -1.94€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH | 123 | -0.060 | +4.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#ETH#15min | 123 | -0.060 | +4.18€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL | 8 | -0.120 | -1.91€ | 0 | 0 |
| 🚫 GBM_LATE_15M_PYCONFIRMADO#SOL#15min | 8 | -0.120 | -1.91€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP | 144 | +0.219 | +100.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_PYCONFIRMADO#XRP#15min | 144 | +0.219 | +100.42€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO | 5597 | +0.065 | +1464.60€ | 0 | 3 |
| ✅ GBM_LATE_15M_TARDIO#15min | 5597 | +0.065 | +1464.60€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC | 1340 | +0.031 | +158.18€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#BTC#15min | 1340 | +0.031 | +158.18€ | 0 | 3 |
| ✅ GBM_LATE_15M_TARDIO#ETH | 1370 | +0.024 | +108.58€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#ETH#15min | 1370 | +0.024 | +108.58€ | 0 | 1 |
| ✅ GBM_LATE_15M_TARDIO#SOL | 1320 | +0.025 | +242.02€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#SOL#15min | 1320 | +0.025 | +242.02€ | 1 | 1 |
| ✅ GBM_LATE_15M_TARDIO#XRP | 1564 | +0.164 | +954.30€ | 0 | 0 |
| ✅ GBM_LATE_15M_TARDIO#XRP#15min | 1564 | +0.164 | +954.30€ | 0 | 11 |
| ✅ GBM_LATE_5M | 849 | -0.036 | -6.53€ | 0 | 0 |
| ✅ GBM_LATE_5M#5min | 849 | -0.036 | -6.53€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC | 177 | -0.048 | -13.94€ | 0 | 0 |
| ✅ GBM_LATE_5M#BTC#5min | 177 | -0.048 | -13.94€ | 0 | 0 |
| 🚫 GBM_LATE_5M#ETH | 82 | -0.202 | -15.93€ | 0 | 0 |
| 🚫 GBM_LATE_5M#ETH#5min | 82 | -0.202 | -15.93€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL | 296 | -0.054 | +9.70€ | 0 | 0 |
| ✅ GBM_LATE_5M#SOL#5min | 296 | -0.054 | +9.70€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP | 294 | +0.037 | +13.64€ | 0 | 0 |
| ✅ GBM_LATE_5M#XRP#5min | 294 | +0.037 | +13.64€ | 0 | 0 |
| ✅ GBM_LATE_60M | 341 | -0.106 | +7.13€ | 3 | 2 |
| ✅ GBM_LATE_60M#60min | 341 | -0.106 | +7.13€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC | 122 | -0.040 | +2.22€ | 0 | 0 |
| ✅ GBM_LATE_60M#BTC#60min | 122 | -0.040 | +2.22€ | 3 | 1 |
| ✅ GBM_LATE_60M#ETH | 109 | -0.131 | -6.35€ | 0 | 0 |
| ✅ GBM_LATE_60M#ETH#60min | 109 | -0.131 | -6.35€ | 4 | 0 |
| ✅ GBM_LATE_60M#SOL | 110 | -0.152 | +11.27€ | 0 | 0 |
| ✅ GBM_LATE_60M#SOL#60min | 110 | -0.152 | +11.27€ | 5 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO | 9 | -0.143 | -2.77€ | 0 | 0 |
| 🚫 GBM_LATE_60M_PYCONFIRMADO#60min | 9 | -0.143 | -2.77€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ GBM_LATE_60M_PYCONFIRMADO#BTC#60min | 5 | -0.054 | -0.73€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN | 369 | -0.061 | -5.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#5min | 369 | -0.061 | -5.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC | 369 | -0.061 | -5.89€ | 0 | 0 |
| ✅ LATE_WINDOW_5MIN#BTC#5min | 369 | -0.061 | -5.89€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M | 299 | +0.002 | +6.84€ | 1 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#15min | 299 | +0.002 | +6.84€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP | 299 | +0.002 | +6.84€ | 0 | 0 |
| ✅ LEADLAG_BTC_XRP_15M#XRP#15min | 299 | +0.002 | +6.84€ | 1 | 0 |
| ✅ ORDER_FLOW_5M | 1685 | +0.011 | +10.63€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#5min | 1549 | +0.007 | -1.96€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB | 217 | +0.034 | +4.59€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BNB#5min | 217 | +0.034 | +4.59€ | 0 | 1 |
| ✅ ORDER_FLOW_5M#BTC | 291 | -0.019 | -5.24€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#BTC#5min | 291 | -0.019 | -5.24€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#DOGE | 226 | +0.000 | -2.22€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#DOGE#5min | 226 | +0.000 | -2.22€ | 1 | 0 |
| ✅ ORDER_FLOW_5M#ETH | 269 | -0.017 | -8.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#ETH#5min | 269 | -0.017 | -8.08€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL | 332 | +0.045 | +15.00€ | 0 | 0 |
| ✅ ORDER_FLOW_5M#SOL#5min | 332 | +0.045 | +15.00€ | 0 | 2 |
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
| ✅ STREAK_FADE_15M | 296 | +0.070 | +23.91€ | 1 | 3 |
| ✅ STREAK_FADE_15M#15min | 296 | +0.070 | +23.91€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH | 63 | +0.038 | -2.53€ | 0 | 0 |
| ✅ STREAK_FADE_15M#ETH#15min | 63 | +0.038 | -2.53€ | 1 | 0 |
| ✅ STREAK_FADE_15M#SOL | 88 | +0.122 | +20.43€ | 0 | 0 |
| ✅ STREAK_FADE_15M#SOL#15min | 88 | +0.122 | +20.43€ | 0 | 2 |
| ✅ STREAK_FADE_15M#XRP | 145 | +0.051 | +6.02€ | 0 | 0 |
| ✅ STREAK_FADE_15M#XRP#15min | 145 | +0.051 | +6.02€ | 0 | 2 |
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
| ✅ UPDOWN_GBM | 2867 | +0.034 | +252.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#15min | 2603 | +0.051 | +291.22€ | 0 | 4 |
| 🚫 UPDOWN_GBM#240min | 11 | -0.148 | -4.31€ | 0 | 0 |
| 🚫 UPDOWN_GBM#5min | 75 | -0.162 | -22.48€ | 4 | 0 |
| ✅ UPDOWN_GBM#60min | 131 | -0.064 | -11.72€ | 6 | 0 |
| ✅ UPDOWN_GBM#BNB | 304 | +0.056 | +59.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#BNB#15min | 304 | +0.056 | +59.80€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC | 588 | +0.054 | +71.59€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#15min | 504 | +0.087 | +86.07€ | 1 | 8 |
| 🚫 UPDOWN_GBM#BTC#5min | 19 | -0.158 | -7.19€ | 0 | 0 |
| ✅ UPDOWN_GBM#BTC#60min | 43 | -0.078 | -6.67€ | 1 | 0 |
| ✅ UPDOWN_GBM#BTC#daily | 18 | -0.135 | +1.83€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE | 251 | +0.006 | +7.16€ | 0 | 0 |
| ✅ UPDOWN_GBM#DOGE#15min | 248 | +0.008 | +8.06€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH | 1096 | +0.039 | +75.54€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#15min | 1002 | +0.053 | +87.10€ | 0 | 4 |
| ✅ UPDOWN_GBM#ETH#240min | 5 | -0.018 | -0.44€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#5min | 19 | -0.204 | -7.68€ | 0 | 0 |
| ✅ UPDOWN_GBM#ETH#60min | 55 | -0.026 | -3.07€ | 0 | 0 |
| 🚫 UPDOWN_GBM#ETH#daily | 15 | -0.154 | -0.38€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL | 307 | -0.034 | +0.95€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#15min | 237 | -0.006 | +7.90€ | 4 | 1 |
| 🚫 UPDOWN_GBM#SOL#5min | 23 | -0.060 | -3.42€ | 0 | 0 |
| ✅ UPDOWN_GBM#SOL#60min | 33 | -0.100 | -1.97€ | 0 | 0 |
| 🚫 UPDOWN_GBM#SOL#daily | 12 | -0.129 | -0.13€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP | 319 | +0.045 | +39.00€ | 0 | 0 |
| ✅ UPDOWN_GBM#XRP#15min | 308 | +0.055 | +42.29€ | 4 | 1 |
| 🚫 UPDOWN_GBM#XRP#5min | 11 | -0.106 | -3.29€ | 0 | 0 |
| 🚫 UPDOWN_GBM#daily | 45 | -0.202 | +1.33€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD | 193 | +0.305 | +39.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#15min | 193 | +0.305 | +39.10€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC | 90 | +0.315 | +20.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#BTC#15min | 90 | +0.315 | +20.66€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH | 103 | +0.290 | +18.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_CROSS_WINDOW_SPREAD#ETH#15min | 103 | +0.290 | +18.44€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO | 2128 | +0.150 | +930.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#15min | 2128 | +0.150 | +930.89€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB | 204 | +0.214 | +134.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BNB#15min | 204 | +0.214 | +134.58€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC | 223 | +0.113 | +39.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#BTC#15min | 223 | +0.113 | +39.80€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE | 193 | +0.203 | +127.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#DOGE#15min | 193 | +0.203 | +127.26€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH | 406 | +0.159 | +146.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#ETH#15min | 406 | +0.159 | +146.53€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL | 505 | +0.088 | +127.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#SOL#15min | 505 | +0.088 | +127.73€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP | 597 | +0.169 | +354.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_15M_TARDIO#XRP#15min | 597 | +0.169 | +354.97€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7 | 21 | +0.065 | +1.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#15min | 21 | +0.065 | +1.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH | 21 | +0.065 | +1.65€ | 0 | 0 |
| ✅ UPDOWN_GBM_ETH_15M_HORA7#ETH#15min | 21 | +0.065 | +1.65€ | 0 | 0 |
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